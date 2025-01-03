from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

API_KEY = load_dotenv('GROQ_API_KEY')
print(API_KEY)

agent = Agent(
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[
        YFinanceTools(stock_fundamentals=True, stock_price=True, analyst_recommendations=True)
    ],
    show_tool_calls=True,
    markdown=True,
    instructions=['Use tables to display data']
)

agent.print_response("Summarize and compare analyst recommendations & fundamentals for Tesla and Microsoft")