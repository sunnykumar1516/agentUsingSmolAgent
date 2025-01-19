from smolagents import CodeAgent
from dotenv import load_dotenv
from smolagents import DuckDuckGoSearchTool
from smolagents import HfApiModel ,  GradioUI

agent = CodeAgent(tools=[DuckDuckGoSearchTool()],
                  model=HfApiModel(token=""),
                  add_base_tools=True,
                  )
GradioUI(agent).launch()

