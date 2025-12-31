# Source: https://docs.tavily.com/examples/open-sources/gpt-researcher.md

# GPT Researcher

## Multi Agent Frameworks

We are strong advocates for the future of AI agents, envisioning a world where autonomous agents communicate and collaborate as a cohesive team to undertake and complete complex tasks.

We hold the belief that research is a pivotal element in successfully tackling these complex tasks, ensuring superior outcomes.

Consider the scenario of developing a coding agent responsible for coding tasks using the latest API documentation and best practices. It would be wise to integrate an agent specializing in research to curate the most recent and relevant documentation, before crafting a technical design that would subsequently be handed off to the coding assistant tasked with generating the code. This approach is applicable across various sectors, including finance, business analysis, healthcare, marketing, and legal, among others.

One multi-agent framework that we're excited about is [LangGraph](https://langchain-ai.github.io/langgraph/), built by the team at [Langchain](https://www.langchain.com/). LangGraph is a Python library for building stateful, multi-actor applications with LLMs. It extends the [LangChain Expression Language](https://python.langchain.com/docs/concepts/lcel/) with the ability to coordinate multiple chains (or actors) across multiple steps of computation.

What's great about LangGraph is that it follows a DAG architecture, enabling each specialized agent to communicate with one another, and subsequently trigger actions among other agents within the graph.

We've added an example for leveraging [GPT Researcher with LangGraph](https://github.com/assafelovic/gpt-researcher/tree/master/multi_agents) which can be found in `/multi_agents`.

The example demonstrates a generic use case for an editorial agent team that works together to complete a research report on a given task.

### The Multi Agent Team

The research team is made up of 7 AI agents:

1. Chief Editor - Oversees the research process and manages the team. This is the "master" agent that coordinates the other agents using Langgraph.
2. Researcher (gpt-researcher) - A specialized autonomous agent that conducts in depth research on a given topic.
3. Editor - Responsible for planning the research outline and structure.
4. Reviewer - Validates the correctness of the research results given a set of criteria.
5. Revisor - Revises the research results based on the feedback from the reviewer.
6. Writer - Responsible for compiling and writing the final report.
7. Publisher - Responsible for publishing the final report in various formats.

### How it works

Generally, the process is based on the following stages:

1. Planning stage
2. Data collection and analysis
3. Writing and submission
4. Review and revision
5. Publication

### Architecture

<img height="100" src="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/gpt-researcher.png?fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=a8aef7f5d088a0bf5180e6f276162d5a" data-og-width="440" data-og-height="1016" data-path="images/gpt-researcher.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/gpt-researcher.png?w=280&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=dc949a38f93d91cd49931c68dc5722d0 280w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/gpt-researcher.png?w=560&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=f1cac1c381681c02886f22238ad4fb75 560w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/gpt-researcher.png?w=840&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=ba26f16aab7c291fe72d3bcc588f9caa 840w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/gpt-researcher.png?w=1100&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=4e7353199cd35fde1f1d76a04fd57667 1100w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/gpt-researcher.png?w=1650&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=0de484c4e18c27aa58b4ed325c0d3b6c 1650w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/gpt-researcher.png?w=2500&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=f4b2fe52fff74badb71ca554a4a51d33 2500w" />

### Steps

More specifically (as seen in the architecture diagram) the process is as follows:

1. Browser (gpt-researcher) - Browses the internet for initial research based on the given research task.
2. Editor - Plans the report outline and structure based on the initial research.
3. For each outline topic (in parallel):
4. Researcher (gpt-researcher) - Runs an in depth research on the subtopics and writes a draft.
5. Reviewer - Validates the correctness of the draft given a set of criteria and provides feedback.
6. Revisor - Revises the draft until it is satisfactory based on the reviewer feedback.
7. Writer - Compiles and writes the final report including an introduction, conclusion and references section from the given research findings.
8. Publisher - Publishes the final report to multi formats such as PDF, Docx, Markdown, etc.

### How to run

1. Install required packages:

```python  theme={null}
pip install -r requirements.txt
```

2. Run the application:

```python  theme={null}
python main.py
```

### Usage

To change the research query and customize the report, edit the `task.json` file in the main directory.

## Customization

The config.py enables you to customize GPT Researcher to your specific needs and preferences.

Thanks to our amazing community and contributions, GPT Researcher supports multiple LLMs and Retrievers. In addition, GPT Researcher can be tailored to various report formats (such as APA), word count, research iterations depth, etc.

GPT Researcher defaults to our recommended suite of integrations: [OpenAI](https://platform.openai.com/docs/overview) for LLM calls and [Tavily API](https://app.tavily.com/home) for retrieving realtime online information.

As seen below, OpenAI still stands as the superior LLM. We assume it will stay this way for some time, and that prices will only continue to decrease, while performance and speed increase over time.

It may not come as a surprise that our default search engine is Tavily. We're aimed at building our search engine to tailor the exact needs of searching and aggregating for the most factual and unbiased information for research tasks. We highly recommend using it with GPT Researcher, and more generally with LLM applications that are built with RAG.

Here is an example of the default config.py file found in `/gpt_researcher/config/`:

```python  theme={null}
def __init__(self, config_file: str = None):
    self.config_file = config_file
    self.retriever = "tavily"
    self.llm_provider = "openai"
    self.fast_llm_model = "gpt-3.5-turbo"
    self.smart_llm_model = "gpt-4o"
    self.fast_token_limit = 2000
    self.smart_token_limit = 4000
    self.browse_chunk_max_length = 8192
    self.summary_token_limit = 700
    self.temperature = 0.6
    self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)" \
                      " Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
    self.memory_backend = "local"
    self.total_words = 1000
    self.report_format = "apa"
    self.max_iterations = 1

    self.load_config_file()
```

Please note that you can also include your own external JSON file by adding the path in the config\_file param.

To learn more about additional LLM support you can check out the [Langchain supported LLMs documentation](https://python.langchain.com/docs/integrations/llms/). Simply pass different provider names in the `llm_provider` config param.

You can also change the search engine by modifying the retriever param to others such as `duckduckgo`, `googleAPI`, `googleSerp`, `searx` and more.

Please note that you might need to sign up and obtain an API key for any of the other supported retrievers and LLM providers.

## Agent Example

If you're interested in using GPT Researcher as a standalone agent, you can easily import it into any existing Python project. Below, is an example of calling the agent to generate a research report:

```python  theme={null}
from gpt_researcher import GPTResearcher
import asyncio

# It is best to define global constants at the top of your script
QUERY = "What happened in the latest burning man floods?"
REPORT_TYPE = "research_report"

async def fetch_report(query, report_type):
    """
    Fetch a research report based on the provided query and report type.
    """
    researcher = GPTResearcher(query=query, report_type=report_type, config_path=None)
    await researcher.conduct_research()
    report = await researcher.write_report()
    return report

async def generate_research_report():
    """
    This is a sample script that executes an async main function to run a research report.
    """
    report = await fetch_report(QUERY, REPORT_TYPE)
    print(report)

if __name__ == "__main__":
    asyncio.run(generate_research_report())
```

You can further enhance this example to use the returned report as context for generating valuable content such as news article, marketing content, email templates, newsletters, etc.

You can also use GPT Researcher to gather information about code documentation, business analysis, financial information and more. All of which can be used to complete much more complex tasks that require factual and high quality realtime information.

## Getting Started

**Step 0** - Install Python 3.11 or later. [See here](https://www.tutorialsteacher.com/python/install-python) for a step-by-step guide.

**Step 1** - Download the project and navigate to its directory

```python  theme={null}
$ git clone https://github.com/assafelovic/gpt-researcher.git
$ cd gpt-researcher
```

**Step 2** - Set up API keys using two methods: exporting them directly or storing them in a `.env` file.

For Linux/Temporary Windows Setup, use the export method:

```python  theme={null}
export OPENAI_API_KEY={Your OpenAI API Key here}
export TAVILY_API_KEY={Your Tavily API Key here}
```

For a more permanent setup, create a `.env` file in the current gpt-researcher folder and input the keys as follows:

```python  theme={null}
OPENAI_API_KEY={Your OpenAI API Key here}
TAVILY_API_KEY={Your Tavily API Key here}
```

For LLM, we recommend [OpenAI GPT](https://platform.openai.com/docs/guides/text-generation), but you can use any other LLM model (including open sources), simply change the llm model and provider in config/config.py.
For search engine, we recommend [Tavily Search API](https://app.tavily.com/home), but you can also refer to other search engines of your choice by changing the search provider in config/config.py to `duckduckgo`, `googleAPI`, `googleSerp`, `searx`, or `bing`. Then add the corresponding env API key as seen in the config.py file.

### Quickstart

**Step 1** - Install dependencies

```python  theme={null}
$ pip install -r requirements.txt
```

**Step 2** - Run the agent with FastAPI

```python  theme={null}
$ uvicorn main:app --reload
```

**Step 3** - Go to [http://localhost:8000](http://localhost:8000) on any browser and enjoy researching!

### Using Virtual Environment or Poetry

Select either based on your familiarity with each:

### Virtual Environment

Establishing the Virtual Environment with Activate/Deactivate configuration
Create a virtual environment using the `venv` package with the environment name `<your_name>`, for example, `env`. Execute the following command in the PowerShell/CMD terminal:

```python  theme={null}
python -m venv env
```

To activate the virtual environment, use the following activation script in PowerShell/CMD terminal:

```python  theme={null}
.\env\Scripts\activate
```

To deactivate the virtual environment, run the following deactivation script in PowerShell/CMD terminal:

```python  theme={null}
deactivate
```

Install the dependencies for a Virtual environment
After activating the `env` environment, install dependencies using the `requirements.txt` file with the following command:

```python  theme={null}
python -m pip install -r requirements.txt
```

### Poetry

Establishing the Poetry dependencies and virtual environment with Poetry version `~1.7.1`
Install project dependencies and simultaneously create a virtual environment for the specified project. By executing this command, Poetry reads the project's "pyproject.toml" file to determine the required dependencies and their versions, ensuring a consistent and isolated development environment. The virtual environment allows for a clean separation of project-specific dependencies, preventing conflicts with system-wide packages and enabling more straightforward dependency management throughout the project's lifecycle.

```python  theme={null}
poetry install
```

Activate the virtual environment associated with a Poetry project
By running this command, the user enters a shell session within the isolated environment associated with the project, providing a dedicated space for development and execution. This virtual environment ensures that the project dependencies are encapsulated, avoiding conflicts with system-wide packages. Activating the Poetry shell is essential for seamlessly working on a project, as it ensures that the correct versions of dependencies are used and provides a controlled environment conducive to efficient development and testing.

```python  theme={null}
poetry shell
```

### Run the app

Launch the FastAPI application agent on a Virtual Environment or Poetry setup by executing the following command:

```python  theme={null}
python -m uvicorn main:app --reload
```

Visit [http://localhost:8000](http://localhost:8000) in any web browser and explore your research!

### Try it with Docker

**Step 1** - Install Docker

Follow the instructions [here](https://docs.docker.com/engine/install/)

**Step 2** - Create `.env` file with your OpenAI Key or simply export it

```python  theme={null}
$ export OPENAI_API_KEY={Your API Key here}
$ export TAVILY_API_KEY={Your Tavily API Key here}
```

**Step 3** - Run the application

```python  theme={null}
$ docker-compose up
```

**Step 4** - Go to [http://localhost:8000](http://localhost:8000) on any browser and enjoy researching!

## Introduction

[GPT Researcher](https://gptr.dev/) is an autonomous agent designed for comprehensive online research on a variety of tasks.

The agent can produce detailed, factual and unbiased research reports, with customization options for focusing on relevant resources, outlines, and lessons. Inspired by the recent [Plan-and-Solve](https://arxiv.org/abs/2305.04091) and [RAG](https://arxiv.org/abs/2005.11401) papers, GPT Researcher addresses issues of speed, determinism and reliability, offering a more stable performance and increased speed through parallelized agent work, as opposed to synchronous operations.

### Why GPT Researcher?

1. To form objective conclusions for manual research tasks can take time, sometimes weeks to find the right resources and information.
2. Current LLMs are trained on past and outdated information, with heavy risks of hallucinations, making them almost irrelevant for research tasks.
3. Solutions that enable web search (such as ChatGPT + Web Plugin), only consider limited resources and content that in some cases result in superficial conclusions or biased answers.
4. Using only a selection of resources can create bias in determining the right conclusions for research questions or tasks.

### Architecture

The main idea is to run "planner" and "execution" agents, whereas the planner generates questions to research, and the execution agents seek the most related information based on each generated research question. Finally, the planner filters and aggregates all related information and creates a research report.

The agents leverage both gpt3.5-turbo and gpt-4-turbo (128K context) to complete a research task. We optimize for costs using each only when necessary. The average research task takes around 3 minutes to complete, and costs \~\$0.1.

<img height="100" src="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/report-flow.png?fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=6c2ab8b5efbc595b5dca4683f98ac1fa" data-og-width="874" data-og-height="1220" data-path="images/report-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/report-flow.png?w=280&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=2ae5dd7bd54c04d560730cf2e7e24d5e 280w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/report-flow.png?w=560&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=d7061e2c1302c358ee4304544d07dd3d 560w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/report-flow.png?w=840&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=8357d273e52a1072d388c679cd3ded82 840w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/report-flow.png?w=1100&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=3507184a15efbc6c053671b5b8272c57 1100w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/report-flow.png?w=1650&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=1d8e5c6eca62d75a8b6407a705ea823a 1650w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/report-flow.png?w=2500&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=c076ee152a159ef6aadd493574da3ebc 2500w" />

More specifically:

1. Create a domain specific agent based on research query or task.
2. Generate a set of research questions that together form an objective opinion on any given task.
3. For each research question, trigger a crawler agent that scrapes online resources for information relevant to the given task.
4. For each scraped resources, summarize based on relevant information and keep track of its sources.
5. Finally, filter and aggregate all summarized sources and generate a final research report.

### Demo

<iframe height="400" width="700" src="https://github.com/assafelovic/gpt-researcher/assets/13554167/a00c89a6-a295-4dd0-b58d-098a31c40fda" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen />

### Tutorials

1. [How it Works](https://medium.com/better-programming/how-i-built-an-autonomous-ai-agent-for-online-research-93435a97c6c)
2. [How to Install](https://www.loom.com/share/04ebffb6ed2a4520a27c3e3addcdde20?sid=da1848e8-b1f1-42d1-93c3-5b0b9c3b24ea)
3. [Live Demo](https://www.loom.com/share/6a3385db4e8747a1913dd85a7834846f?sid=a740fd5b-2aa3-457e-8fb7-86976f59f9b8)
4. [Home Page](https://gptr.dev/)

### Features

1. 📝 Generate research, outlines, resources and lessons reports
2. 📜 Can generate long and detailed research reports (over 2K words)
3. 🌐 Aggregates over 20 web sources per research to form objective and factual conclusions
4. 🖥️ Includes an easy-to-use web interface (HTML/CSS/JS)
5. 🔍 Scrapes web sources with javascript support
6. 📂 Keeps track and context of visited and used web sources
7. 📄 Export research reports to PDF, Word and more...

### Disclaimer

This project, GPT Researcher, is an experimental application and is provided "as-is" without any warranty, express or implied. We are sharing codes for academic purposes under the MIT license. Nothing herein is academic advice, and NOT a recommendation to use in academic or research papers.

Our view on unbiased research claims:

The whole point of our scraping system is to reduce incorrect fact. How? The more sites we scrape the less chances of incorrect data. We are scraping 20 per research, the chances that they are all wrong is extremely low.
We do not aim to eliminate biases; we aim to reduce it as much as possible. We are here as a community to figure out the most effective human/llm interactions.
In research, people also tend towards biases as most have already opinions on the topics they research about. This tool scrapes many opinions and will evenly explain diverse views that a biased person would never have read.
Please note that the use of the GPT-4 language model can be expensive due to its token usage. By utilizing this project, you acknowledge that you are responsible for monitoring and managing your own token usage and the associated costs. It is highly recommended to check your OpenAI API usage regularly and set up any necessary limits or alerts to prevent unexpected charges.

## PIP Package

🌟 Exciting News! Now, you can integrate gpt-researcher with your apps seamlessly!

### Steps to Install GPT Researcher 🛠️

Follow these easy steps to get started:

0. Pre-requisite: Ensure Python 3.10+ is installed on your machine 💻
1. Install gpt-researcher: Grab the official package from [PyPi](https://pypi.org/project/gpt-researcher/).

```python  theme={null}
pip install gpt-researcher
```

2. Environment Variables: Create a .env file with your OpenAI API key or simply export it

```python  theme={null}
export OPENAI_API_KEY={Your OpenAI API Key here}
export TAVILY_API_KEY={Your Tavily API Key here}
```

3. Start using GPT Researcher in your own codebase

### Example Usage 📝

```python  theme={null}
from gpt_researcher import GPTResearcher
import asyncio


from gpt_researcher import GPTResearcher
import asyncio


async def get_report(query: str, report_type: str) -> str:
    researcher = GPTResearcher(query, report_type)
    research_result = await researcher.conduct_research()
    report = await researcher.write_report()
    return report

if __name__ == "__main__":
    query = "what team may win the NBA finals?"
    report_type = "research_report"

    report = asyncio.run(get_report(query, report_type))
    print(report)
```

### Specific Examples 🌐

Example 1: Research Report 📚

```python  theme={null}
query = "Latest developments in renewable energy technologies"
report_type = "research_report"
```

Example 2: Resource Report 📋

```python  theme={null}
query = "List of top AI conferences in 2023"
report_type = "resource_report"
```

Example 3: Outline Report 📝

```python  theme={null}
query = "Outline for an article on the impact of AI in education"
report_type = "outline_report"
```

### Integration with Web Frameworks 🌍

FastAPI Example:

```python  theme={null}
from fastapi import FastAPI
from gpt_researcher import GPTResearcher
import asyncio

app = FastAPI()

@app.get("/report/{report_type}")
async def get_report(query: str, report_type: str) -> dict:
    researcher = GPTResearcher(query, report_type)
    research_result = await researcher.conduct_research()
    report = await researcher.write_report()
    return {"report": report}

# Run the server
# uvicorn main:app --reload
```

Flask Example
Pre-requisite: Install flask with the async extra.

```python  theme={null}
pip install 'flask[async]'
```

```python  theme={null}
from flask import Flask, request
from gpt_researcher import GPTResearcher

app = Flask(__name__)

@app.route('/report/<report_type>', methods=['GET'])
async def get_report(report_type):
    query = request.args.get('query')
    researcher = GPTResearcher(query, report_type)
    research_result = await researcher.conduct_research()
    report = await researcher.write_report()
    return report

# Run the server
# flask run
```

Run the server:

```python  theme={null}
flask run
```

Example Request:

```python  theme={null}
curl -X GET "http://localhost:5000/report/research_report?query=what team may win the nba finals?"
```

Note: The above code snippets are just examples. You can customize them as per your requirements.

## Roadmap

We're constantly working on additional features and improvements to our products and services. We're also working on new products and services to help you build better AI applications using [GPT Researcher](https://gptr.dev/).

Our vision is to build the #1 autonomous research agent for AI developers and researchers, and we're excited to have you join us on this journey!

The roadmap is prioritized based on the following goals: Performance, Quality, Modularity and Conversational flexibility. The roadmap is public and can be found [here](https://trello.com/b/3O7KBePw/gpt-researcher-roadmap).

## Tailored Research

The GPT Researcher package allows you to tailor the research to your needs such as researching on specific sources or local documents, and even specify the agent prompt instruction upon which the research is conducted.

### Research on Specific Sources 📚

You can specify the sources you want the GPT Researcher to research on by providing a list of URLs. The GPT Researcher will then conduct research on the provided sources.

```python  theme={null}
from gpt_researcher import GPTResearcher
import asyncio

async def get_report(query: str, report_type: str, sources: list) -> str:
    researcher = GPTResearcher(query=query, report_type=report_type, source_urls=sources)
    await researcher.conduct_research()
    report = await researcher.write_report()
    return report

if __name__ == "__main__":
    query = "What are the latest advancements in AI?"
    report_type = "research_report"
    sources = ["https://en.wikipedia.org/wiki/Artificial_intelligence", "https://www.ibm.com/watson/ai"]

    report = asyncio.run(get_report(query, report_type, sources))
    print(report)
```

### Specify Agent Prompt 📝

You can specify the agent prompt instruction upon which the research is conducted. This allows you to guide the research in a specific direction and tailor the report layout. Simplay pass the prompt as the `query` argument to the `GPTResearcher` class and the "custom\_report" `report_type`.

```python  theme={null}
from gpt_researcher import GPTResearcher
import asyncio

async def get_report(prompt: str, report_type: str) -> str:
    researcher = GPTResearcher(query=prompt, report_type=report_type)
    await researcher.conduct_research()
    report = await researcher.write_report()
    return report

if __name__ == "__main__":
    report_type = "custom_report"
    prompt = "Research the latest advancements in AI and provide a detailed report in APA format including sources."

    report = asyncio.run(get_report(prompt=prompt, report_type=report_type))
    print(report)
```

### Research on Local Documents 📄

TBD!

## Troubleshooting

We're constantly working to provide a more stable version. If you're running into any issues, please first check out the resolved issues or ask us via our [Discord community](https://discord.com/invite/2pFkc83fRq).

### Model: gpt-4 does not exist

This relates to not having permission to use gpt-4 yet. Based on OpenAI, it will be [widely available for all by end of July](https://help.openai.com/en/articles/7102672-how-can-i-access-gpt-4-gpt-4-turbo-gpt-4o-and-gpt-4o-mini).

### Cannot load library 'gobject-2.0-0'

The issue relates to the library WeasyPrint (which is used to generate PDFs from the research report). Please follow this guide to resolve it: [https://doc.courtbouillon.org/weasyprint/stable/first\_steps.html](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html), or you can install this package manually.

In case of MacOS you can install this lib using `brew install glib gobject-introspection`

In case of Linux you can install this lib using `sudo apt install libglib2.0-dev`

### Cannot load library 'pango'

In case of MacOS you can install this lib using `brew install pango`

In case of Linux you can install this lib using `sudo apt install libpango-1.0-0`

### Workaround for Mac M chip users

If the above solutions don't work, you can try the following:

1. Install a fresh version of Python 3.11 pointed to brew: `brew install python@3.11`
2. Install the required libraries: `brew install pango glib gobject-introspection`
3. Install the required GPT Researcher Python packages: `pip3.11 install -r requirements.txt`
4. Run the app with Python 3.11 (using brew): `python3.11 -m uvicorn main:app --reload`

### Error processing the url

We're using [Selenium](https://www.selenium.dev/) for site scraping. Some sites fail to be scraped. In these cases, restart and try running again.

### Chrome version issues

Many users have an issue with their chromedriver because the latest chrome browser version doesn't have a compatible chrome driver yet.

To downgrade your Chrome web browser using [slimjet](https://www.slimjet.com/chrome/google-chrome-old-version.php), follow these steps. First, visit the website and scroll down to find the list of available older Chrome versions. Choose the version you wish to install making sure it's compatible with your operating system. Once you've selected the desired version, click on the corresponding link to download the installer. Before proceeding with the installation, it's crucial to uninstall your current version of Chrome to avoid conflicts.

It's important to check if the version you downgrade to, has a chromedriver available in the official [chrome driver website](https://developer.chrome.com/docs/chromedriver/downloads).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.tavily.com/llms.txt