import os
import time
import yaml
import pyperclip
import keyboard  # <--- New Import

try:
    from config.secrets import GEMINI_API_KEY
except ImportError:
    GEMINI_API_KEY = None

from core import generator, researcher

# --- GLOBAL STATE ---
# We need a global variable to track settings in real-time
current_state = {
    "mode": "startup",  # Default
    "paused": False
}

def load_config():
    try:
        with open("config/settings.yaml", "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        return {"modes": {}, "ai_preferences": {"model": "gemini-1.5-flash"}}

def load_resume():
    path = os.path.join("data", "my_resume.txt")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    return ""

def on_hotkey_startup():
    current_state["mode"] = "startup"
    print("\n🚀 MODE SWITCHED: STARTUP (High Energy)")

def on_hotkey_corporate():
    current_state["mode"] = "corporate"
    print("\n👔 MODE SWITCHED: CORPORATE (Professional)")

def on_hotkey_pause():
    current_state["paused"] = not current_state["paused"]
    status = "PAUSED ⏸️" if current_state["paused"] else "ACTIVE ▶️"
    print(f"\n{status}")

def start_app():
    api_key = GEMINI_API_KEY
    if not api_key:
        print("❌ Error: Key missing in secrets.py")
        return

    print("🚀 JobApplyPro v2.0 is Starting...")
    print("   [F9]  -> Startup Mode")
    print("   [F10] -> Corporate Mode")
    print("   [F8]  -> Pause/Resume")
    
    config = load_config()
    resume_text = load_resume()
    
    if not resume_text: return

    try:
        model = generator.configure_ai(api_key, config['ai_preferences']['model'])
        print("✅ AI Connected.")
    except Exception as e:
        print(f"❌ Error: {e}")
        return

    # --- SETUP HOTKEYS ---
    keyboard.add_hotkey('F9', on_hotkey_startup)
    keyboard.add_hotkey('F10', on_hotkey_corporate)
    keyboard.add_hotkey('F8', on_hotkey_pause)

    last_text = ""
    
    while True:
        try:
            if current_state["paused"]:
                time.sleep(0.5)
                continue

            current_text = pyperclip.paste()
            
            if current_text != last_text and len(current_text) > 100:
                print("\n✨ New Job Description Detected!")
                
                # Update config with the LIVE mode from keypress
                config['current_mode'] = current_state["mode"]
                
                # A. Extract Name
                company_name = generator.extract_company_name(model, current_text)
                print(f"   🏢 Target: {company_name}")
                
                # B. Research
                company_info = researcher.get_company_info(company_name)
                
                # C. Write
                print(f"   ✍️  Drafting ({current_state['mode']} mode)...")
                answer = generator.write_cover_note(
                    model, resume_text, current_text, company_info, config
                )
                
                # D. Deliver
                pyperclip.copy(answer)
                print(f"\n✅ DONE! Copied to clipboard.")
                print("-" * 40)
                print(answer)
                print("-" * 40)
                
                last_text = answer 
                
            time.sleep(0.5)
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(1)

if __name__ == "__main__":
    start_app()