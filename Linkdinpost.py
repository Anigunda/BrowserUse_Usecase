from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from pydantic import SecretStr
import asyncio
import os

api_key = os.getenv("GEMINI_API")
login_email = os.getenv("LOGIN")
login_password = os.getenv("PASSWORD")

topic= "Python learning for data science"  

# Initialize the model
llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

# Create agent with the model
async def main():
    agent = Agent(
        task=f"Create script for a detailed, informative post for beginners on the topic of {topic}. Post should cover all the aspects in the given topic "
             "use only your knowledge instead of browsing to write the post. keep the character limit to 2500. "
             "post should include the topic name, module name, a concise explanation, and a link to an additional resource for further guidance. "
             f"once the post is ready open the linkedin login and login using {login_email} and {login_password}. ONLY Proceed to linkdin login when post script is ready. once you receive my input go ahead and post this article on linkedin.", 
        llm=llm,
    
    )
    history = await agent.run()

    # Extract the structured result
    result = history.final_result()


asyncio.run(main())