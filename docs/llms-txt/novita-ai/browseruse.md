# Source: https://novita.ai/docs/guides/browseruse.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Browser Use

> Easily enhance your browsing experience by integrating Novita AI with Browser Use for intelligent web interactions.

Browser Use is an open-source library that empowers LLMs to directly control web browsers, revolutionizing web interaction with advanced automation. By integrating Novita AI's powerful LLMs and tools, Browser Use enables seamless browsing, content generation, and task automation for an optimized user experience.

This tutorial will show you how to integrate the Novita AI API with Browser Use to automate browser interactions.

## **How to Use Browser Use with Novita AI**

### **Prerequisites**

* Python 3.11 or higher
* A Novita AI API key

### **Installation**

Step 1: Install Browser Use using pip:

```bash  theme={"system"}
pip install browser-use
```

Step 2: Install Playwright (required for browser automation):

```bash  theme={"system"}
playwright install chromium
```

### **Obtaining Novita AI LLM API Key**

* Create an account: Visit [Novita AI’s website](https://novita.ai/) and sign up for an account.
* Generate your API Key: After logging in, navigate to the [Key Management](https://novita.ai/settings/key-management) page to generate your API key. This key is essential to connect Novita AI’s models to Cursor.

  <Frame>
    ![Novita AI key management](https://mintlify.s3.us-west-1.amazonaws.com/novitaai/images/third-party/dify-1.png)
  </Frame>

### **Environment Setup**

Create a `.env` file in your project root and add your Novita API key:

```bash  theme={"system"}
NOVITA_API_KEY=your_api_key_here
```

### Basic Implementation

* Here's a complete example of using Browser Use with Novita AI's API:

```python  theme={"system"}
"""
Web automation using Novita AI and Browser Use
"""

import asyncio
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from browser_use import Agent

# Load environment variables
load_dotenv()

api_key = os.getenv('NOVITA_API_KEY', '')
if not api_key:
    raise ValueError('NOVITA_API_KEY is not set')


async def run_search():
    agent = Agent(
        task=(
            '1. Go to https://www.reddit.com/r/LocalLLaMA '
            "2. Search for 'browser use' in the search bar "
            '3. Click on first result '
            '4. Return the first comment'
        ),
        llm=ChatOpenAI(
            base_url='https://api.novita.ai/openai',
            model='deepseek/deepseek-v3-0324',
            api_key=SecretStr(api_key),
        ),
        use_vision=False,
    )

    await agent.run()


if __name__ == '__main__':
    asyncio.run(run_search())
```

### **Creating Your Own Tasks**

* You can customize the `task` parameter to perform a wide variety of web tasks:

```python  theme={"system"}
task="Compare the price of gpt-4o and DeepSeek-V3"
```

* For more complex tasks, you might want to enable vision capabilities:

```python  theme={"system"}
agent = Agent(
    task="Find and summarize the latest news about AI on TechCrunch",
    llm=ChatOpenAI(
        base_url='https://api.novita.ai/openai',
        model='deepseek/deepseek-v3-0324',
        api_key=SecretStr(api_key),
    ),
    use_vision=True,
)
```


Built with [Mintlify](https://mintlify.com).