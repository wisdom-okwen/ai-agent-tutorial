from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

API_KEY = load_dotenv('GROQ_API_KEY')
print(API_KEY)

agent = Agent(
    model=Groq(id='llama-3.3-70b-versatile')
)

agent.print_response("What's science?")