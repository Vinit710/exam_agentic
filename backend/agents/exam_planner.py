from agents.llm_client import query_gemini

uploaded_topics = []

def parse_topics(raw_text: str):
    """
    Preprocess topics to extract meaningful list of topics.
    LLM will split them properly if not comma/line separated.
    """
    global uploaded_topics
    prompt = f"""
    Extract a clean list of topics from the following text. 
    Return only the list as JSON array.
    
    Text:
    {raw_text}
    """
    result = query_gemini(prompt)
    
    try:
        # try to parse JSON array
        import json
        uploaded_topics = json.loads(result)
    except:
        # fallback: split by newlines if LLM fails
        uploaded_topics = [line.strip() for line in raw_text.split("\n") if line.strip()]
    
    return uploaded_topics
