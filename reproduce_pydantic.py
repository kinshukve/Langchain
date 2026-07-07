from langchain_core.tools import tool
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()
api_key = os.getenv("GROQ_API_KEY") or os.getenv("groq_api_key")
if api_key:
    os.environ["GROQ_API_KEY"] = api_key

print(f"Pydantic version: {BaseModel.__module__}")

# Setup simple tool
@tool
def check_weather(location: str):
    """Check weather."""
    return "Sunny"

# Setup Pydantic tool
class WeatherInput(BaseModel):
    location: str = Field(description="City")

@tool("weather_tool", args_schema=WeatherInput)
def weather_tool(location: str):
    """Check weather."""
    return "Rainy"

try:
    llm = ChatGroq(model="llama-3.1-8b-instant")
    
    # Test 1: Simple tool
    print("\n--- Testing Simple Tool ---")
    model_with_tools = llm.bind_tools([check_weather])
    res = model_with_tools.invoke("Weather in NY")
    print("Simple tool success")
    
    # Test 2: Pydantic tool
    print("\n--- Testing Pydantic Tool ---")
    model_with_tools_2 = llm.bind_tools([weather_tool])
    res = model_with_tools_2.invoke("Weather in London")
    print("Pydantic tool success")

except Exception as e:
    print(f"\nERROR: {type(e).__name__}: {e}")

try:
    print("\n--- Testing Pydantic Class Binding ---")
    model_with_tools_3 = llm.bind_tools([WeatherInput])
    res = model_with_tools_3.invoke("Weather in Paris")
    print("Pydantic class binding success")
except Exception as e:
    print(f"\nERROR in Class Binding: {type(e).__name__}: {e}")

from langchain.tools import StructuredTool

try:
    print("\n--- Testing StructuredTool with Pydantic v2 ---")
    def my_func(location: str):
        return "Windy"
    
    struct_tool = StructuredTool.from_function(
        func=my_func,
        name="wind_tool",
        args_schema=WeatherInput
    )
    model_with_tools_4 = llm.bind_tools([struct_tool])
    res = model_with_tools_4.invoke("Wind in Chicago")
    print("StructuredTool success")
except Exception as e:
    print(f"\nERROR in StructuredTool: {type(e).__name__}: {e}")
