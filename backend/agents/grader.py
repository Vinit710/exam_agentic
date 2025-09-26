from agents.llm_client import query_gemini
from agents.question_generator import mcqs_store

def grade_exam(user_answers: dict):
    """
    user_answers: {question_id: selected_option}
    Returns a detailed report with score and feedback from LLM.
    """
    total = len(mcqs_store)
    correct_count = 0
    details = []

    for mcq in mcqs_store:
        qid = str(mcq["id"])
        selected = user_answers.get(qid, "")
        is_correct = selected == mcq["answer"]
        if is_correct:
            correct_count += 1
        details.append({
            "question": mcq["question"],
            "your_answer": selected,
            "correct_answer": mcq["answer"],
            "is_correct": is_correct
        })
    
    score = round((correct_count / total) * 100, 2) if total > 0 else 0

    # Ask LLM to generate improvement suggestions
    feedback_prompt = f"""
    User took an exam with the following questions and answers:
    {details}
    Generate a concise feedback report for the user, 
    highlighting topics to improve and suggested study tips.
    """
    feedback = query_gemini(feedback_prompt)

    return {"score": score, "details": details, "feedback": feedback}
