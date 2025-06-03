import os
import vertexai
from vertexai.generative_models import GenerativeModel
from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT", "blocks-gcp-xxxx")
LOCATION = "global"
API_KEY = os.environ.get("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is required")

print(f"Project ID: {PROJECT_ID}")
print(f"Location: {LOCATION}")
print("Initializing Vertex AI...")

try:
    vertexai.init(project=PROJECT_ID, location=LOCATION, api_key=API_KEY)
    print("✓ Vertex AI initialized successfully")
    
    model = GenerativeModel("gemini-2.0-flash-001")
    print("✓ Model loaded successfully")
    
    # 簡単なテスト
    print("\nTesting model with a simple prompt...")
    response = model.generate_content("Hello! Please respond with 'Hello, World!'")
    print(f"Response: {response.text}")
    print("✓ Test completed successfully")
    
except Exception as e:
    print(f"✗ Error: {e}")
    raise