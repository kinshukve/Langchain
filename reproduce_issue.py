from langchain.tools import tool
try:
    from langchain_groq import ChatGroq
except ImportError:
    # Mocking ChatGroq if not installed or credentials missing just to test the pydantic error
    # But the error happens at import of langchain.tools usually if pydantic is messed up
    pass

@tool
def get_weather(location: str) -> str:
    """Get the weather for a location."""
    return f"The weather in {location} is sunny."

print("Successfully imported and defined tool.")

import pydantic
print(f"Pydantic version: {pydantic.VERSION}")

try:
    from langchain_core.pydantic_v1 import BaseModel
    print("Imported BaseModel from langchain_core.pydantic_v1")
except ImportError as e:
    print(f"Failed to import from pydantic_v1: {e}")

try:
    model = ChatGroq(model="llama-3.1-8b-instant")
    model_with_tools = model.bind(tools=[get_weather])
    print("Successfully bound tools.")
except Exception as e:
    print(f"Error during execution: {e}")
