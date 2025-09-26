from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware


from agents.question_generator import generate_mcqs
from agents.grader import grade_exam
from agents.exam_planner import parse_topics

# File to persist topics
import os
TOPICS_FILE = "topics.txt"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/upload-topics")
async def upload_topics(file: UploadFile = File(...)):
    content = await file.read()
    topics_text = content.decode("utf-8")
    parsed_topics = parse_topics(topics_text)
    # Save topics to file
    with open(TOPICS_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(parsed_topics))
    return {"message": "Topics uploaded successfully", "topics": parsed_topics}



@app.get("/generate-mcqs")
def get_mcqs():
    # Load topics from file
    if not os.path.exists(TOPICS_FILE):
        print("[DEBUG] Topics file not found.")
        return {"mcqs": []}
    with open(TOPICS_FILE, "r", encoding="utf-8") as f:
        topics = [line.strip() for line in f if line.strip()]
    print(f"[DEBUG] Loaded topics: {topics}")
    if not topics:
        print("[DEBUG] No topics found in file.")
        return {"mcqs": []}
    mcqs = generate_mcqs(topics)
    print(f"[DEBUG] Generated MCQs: {mcqs}")
    return {"mcqs": mcqs}


from fastapi import Request

@app.post("/submit-exam")
async def submit_exam(request: Request):
    form = await request.form()
    answers = dict(form)
    report = grade_exam(answers)
    return {"report": report}
