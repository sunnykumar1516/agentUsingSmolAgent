from smolagents import CodeAgent , LiteLLMModel
from dotenv import load_dotenv
from smolagents import DuckDuckGoSearchTool

model = LiteLLMModel(model_id="gpt-4o")
agent = CodeAgent( tools=[DuckDuckGoSearchTool()],
                  model = model
                  
)
agent.run("whats happening with israel and gaza war?")