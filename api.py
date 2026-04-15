import os
import json
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
# Ollama configuration
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL = "qwen3:4b"
OPENAI_MODEL = "gpt-3.5-turbo"

def build_prompt_a(intent, facts, tone):
    facts_str = "\n".join([f"{i+1}. {f}" for i, f in enumerate(facts)])
    system = "You are a professional email writer. Write clear, well-structured business emails."
    user = f"Write a professional email with the following details:\n\nINTENT: {intent}\n\nKEY FACTS TO INCLUDE:\n{facts_str}\n\nTONE: {tone}\n\nGenerate only the email (subject line + body). No preamble or explanation."
    return system, user

def build_prompt_b(intent, facts, tone):
    facts_str = "\n".join([f"{i+1}. {f}" for i, f in enumerate(facts)])
    system = """You are Dr. Elena Vasquez, a master business communications strategist... 
    [Insert the rest of your Chain-of-Thought System Prompt from the JS file here]"""
    
    user = f"Apply your chain-of-thought protocol and write a professional email with these exact parameters:\n\nINTENT: {intent}\n\nKEY FACTS:\n{facts_str}\n\nREQUIRED TONE: {tone}\n\nOutput ONLY the email — subject line followed by body. No explanatory text before or after."
    return system, user

def generate_email(intent, facts, tone, strategy, openai_api_key=None):
    try:
        system, user = build_prompt_a(intent, facts, tone) if strategy == "A" else build_prompt_b(intent, facts, tone)
        
        # Use OpenAI if API key is provided
        if openai_api_key:
            try:
                client = OpenAI(api_key=openai_api_key)
                response = client.chat.completions.create(
                    model=OPENAI_MODEL,
                    messages=[
                        {"role": "system", "content": system},
                        {"role": "user", "content": user}
                    ],
                    temperature=0.7,
                    max_tokens=1024
                )
                return response.choices[0].message.content
            except Exception as e:
                return f"⚠️ Error: OpenAI API failed: {str(e)}"
        
        # Fall back to Ollama
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": MODEL,
                "prompt": f"System: {system}\n\nUser: {user}",
                "stream": False
            },
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            return result.get("response", "Error: No response generated")
        else:
            return f"⚠️ Error: Ollama API returned status {response.status_code}. Make sure Ollama is running at {OLLAMA_URL}"
    except requests.exceptions.ConnectionError:
        return f"⚠️ Error: Cannot connect to Ollama at {OLLAMA_URL}. Please start Ollama and try again.\n\nTo start Ollama:\n1. Install from https://ollama.ai\n2. Run: ollama serve\n3. In another terminal: ollama pull llama3"
    except Exception as e:
        return f"⚠️ Error: {str(e)}"