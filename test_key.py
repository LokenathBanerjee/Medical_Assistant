import os, time
from dotenv import load_dotenv
from google import genai

load_dotenv()
key = os.getenv("GOOGLE_API_KEY")
print("USING KEY:", (key[:6] + "..." + key[-4:]) if key else None)

client = genai.Client(api_key=key)

MODEL = "models/gemini-2.0-flash-lite"   # ✅ free-friendly

for _ in range(5):
    try:
        resp = client.models.generate_content(
            model=MODEL,
            contents="Say 'ok' only"
        )
        print(resp.text)
        break
    except Exception as e:
        msg = str(e)
        if "RESOURCE_EXHAUSTED" in msg or "429" in msg:
            time.sleep(35)   # wait and retry
            continue
        raise



