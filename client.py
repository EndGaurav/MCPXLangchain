from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                # Make sure to update to the full absolute path to your math_server.py file
                "args": ["math_server.py"],
                "transport": "stdio",
            },
            "weather": {
                # make sure you start your weather server on port 8000
                "url": "http://localhost:8000/mcp/",
                "transport": "streamable_http",
            }
        }
    )


    tools = await client.get_tools()
    model = ChatGroq(model="qwen-qwq-32b", api_key=os.getenv("GROQ_API_KEY"))
    agent = create_react_agent(model, tools)
    math_response = await agent.ainvoke({"messages": "what's 3 + 5 ?"})
    weather_response = await agent.ainvoke({"messages": "what is the weather in nyc?"})
    # print(math_response['messages'][-1].content)
    print(weather_response['messages'][-1].content)

    
asyncio.run(main())
    
    

    

    