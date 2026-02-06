#!/usr/bin/env python3
"""Simple test script to verify AutoGen installation and basic functionality."""

import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

async def main() -> None:
    """Test basic AutoGen functionality."""
    print("Testing AutoGen installation...")
    print("Note: This requires OPENAI_API_KEY to be set for full functionality.")
    
    # Check if OpenAI API key is set
    import os
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("\n[WARNING] OPENAI_API_KEY not set. The agent will not be able to make API calls.")
        print("To test fully, set your OpenAI API key:")
        print("  export OPENAI_API_KEY='sk-...'")
        print("\n[SUCCESS] AutoGen packages are installed correctly!")
        print("[SUCCESS] You can now use AutoGen Studio at http://localhost:8080")
        return
    
    print(f"\n[SUCCESS] OpenAI API key found (starts with: {api_key[:7]}...)")
    
    try:
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
        agent = AssistantAgent("assistant", model_client=model_client)
        
        print("\n[INFO] Running a simple test task...")
        result = await agent.run(task="Say 'Hello World!' in a friendly way.")
        print(f"\n[SUCCESS] Agent response: {result}")
        
        await model_client.close()
        print("\n[SUCCESS] AutoGen is working correctly!")
    except Exception as e:
        print(f"\n[ERROR] Error running agent: {e}")
        print("This might be due to API key issues or network connectivity.")

if __name__ == "__main__":
    asyncio.run(main())
