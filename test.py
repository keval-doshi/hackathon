import google.genai as genai

API_KEYS = [
    "AIzaSyAiWCoFRGdk-AriwGhHjE_3xRCemxd7eWU",
    "AIzaSyDlsceT-buDljc_oVuP4b3HrwLQaaLq8A4",
    "AIzaSyCRIivqKuKLkjX4nwsy0b6ZCPn-U1WsAkI",
    "AIzaSyAzV2VVBDPkQYj4HJdRTeD6GK-Zm9cXDB0",
    "AIzaSyAzV2VVBDPkQYj4HJdRTeD6GK-Zm9cXDB0"
    
]

MODELS = [
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
    "gemini-1.5-flash",
    "gemini-1.5-pro",
]

for i, key in enumerate(API_KEYS, 1):
    print(f"\n🔑 Testing Key {i}:")
    client = genai.Client(api_key=key)
    for model_name in MODELS:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents="Say hi in one word"
            )
            print(f"  ✅ {model_name} — WORKS: {response.text.strip()}")
        except Exception as e:
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                print(f"  ⚠️  {model_name} — QUOTA EXHAUSTED")
            elif "404" in str(e):
                print(f"  ❌ {model_name} — NOT FOUND")
            elif "403" in str(e):
                print(f"  🔒 {model_name} — INVALID KEY")
            else:
                print(f"  ❓ {model_name} — {str(e)[:60]}")