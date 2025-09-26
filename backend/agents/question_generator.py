from agents.llm_client import query_gemini
from agents.exam_planner import uploaded_topics

mcqs_store = []

def generate_mcqs(topics, num_questions=10):
    global mcqs_store
    mcqs_store = []
    if not topics:
        return []

    for i, topic in enumerate(topics[:num_questions]):
        prompt = f"""
        Generate one multiple-choice question (with 4 options and the correct answer) 
        based on the topic: "{topic}". 
        Format as JSON:
        {{
            "question": "...",
            "options": ["...", "...", "...", "..."],
            "answer": "..."
        }}
        """
        result = query_gemini(prompt)
        try:
            import json
            mcq = json.loads(result)
        except:
            mcq = {
                "question": f"What is the key idea of '{topic}'?",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "answer": "Option A"
            }
        mcq["id"] = i+1
        mcqs_store.append(mcq)
    return mcqs_store
