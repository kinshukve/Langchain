import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Handle varying case for API key
api_key = os.getenv("GROQ_API_KEY") or os.getenv("groq_api_key")

if not api_key:
    print("❌ Error: GROQ_API_KEY not found in environment variables.")
    print("Please check your .env file.")
else:
    print("✅ API Key found.")
    # Ensure it's set for the library
    os.environ["GROQ_API_KEY"] = api_key

    try:
        print("initializing ChatGroq...")
        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0
        )
        print("Testing basic invocation...")
        response = llm.invoke("Hello! Just checking if LangChain is working.")
        print("\n🎉 Success! LangChain is working correctly.")
        print("Response from Groq:", response.content)
    except Exception as e:
        print(f"\n❌ validation failed: {e}")
