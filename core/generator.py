import google.generativeai as genai

# Initialize the AI once when the app starts
def configure_ai(api_key, model_name="gemini-1.5-flash"):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name)

def extract_company_name(model, job_text):
    """Asks AI to find the company name in the text."""
    prompt = f"""
    Analyze the following Job Description and extract the COMPANY NAME.
    If the name is not explicitly stated, output 'Unknown'.
    Output ONLY the name, nothing else.
    
    Job Text:
    {job_text[:1000]}
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"   ⚠️ Extraction Error: {e}")
        return "Unknown"

def write_cover_note(model, resume, job_desc, company_info, config):
    # 1. Load the selected mode
    mode_name = config.get('current_mode', 'startup') # Default to startup
    mode_settings = config['modes'].get(mode_name, config['modes']['startup'])
    
    tone = mode_settings['tone']
    focus = mode_settings['focus']
    
    print(f"   🎭 Mode: {mode_name.upper()} (Focus: {focus})")

    # 2. Enhanced Prompt
    prompt = f"""
    ROLE: You are an expert career strategist.
    
    CANDIDATE PROFILE:
    {resume[:1000]}
    
    TARGET COMPANY DATA:
    {company_info}
    
    JOB LISTING:
    {job_desc[:1500]}
    
    TASK:
    Write a 60-80 word "Why do you want to work here?" response.
    
    STYLE GUIDELINES (Critical):
    - TONE: {tone}
    - FOCUS: Highlight the company's {focus}.
    - STRUCTURE: Start with their specific mission/goals found in the text. Connect it to my technical ability (specifically mentioning BioChase or scaling systems).
    - VOID: Do not use generic phrases like "I am a passionate coder." Be specific.
    
    Output ONLY the answer text.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"AI Error: {e}"