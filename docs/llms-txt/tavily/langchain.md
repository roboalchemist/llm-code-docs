# Source: https://docs.tavily.com/documentation/integrations/langchain.md

# LangChain

> We're excited to partner with Langchain as their recommended search tool!

> **Warning**: The [`langchain_community.tools.tavily_search.tool`](https://python.langchain.com/docs/integrations/tools/tavily_search/) is deprecated. While it remains functional for now, we strongly recommend migrating to the new `langchain-tavily` Python package which supports [Search](#tavily-search), [Extract](#tavily-extract), [Map](#tavily-mapcrawl), and [Crawl](#tavily-mapcrawl) functionality and receives continuous updates with the latest features.

The [langchain-tavily](https://pypi.org/project/langchain-tavily/) Python package is the official LangChain integration of Tavily, including [Search](#tavily-search), [Extract](#tavily-extract), [Map](#tavily-mapcrawl), and [Crawl](#tavily-mapcrawl) functionality.

## Installation

```bash  theme={null}
pip install -U langchain-tavily
```

### Credentials

We also need to set our Tavily API key. You can get an API key by visiting [this site](https://app.tavily.com/sign-in) and creating an account.

```bash  theme={null}
import getpass
import os

if not os.environ.get("TAVILY_API_KEY"):
    os.environ["TAVILY_API_KEY"] = getpass.getpass("Tavily API key:\n")
```

## Tavily Search

Here we show how to instantiate the Tavily search tool. This tool allows you to complete search queries using Tavily's Search API endpoint.

### Available Parameters

The Tavily Search API accepts various parameters to customize the search:

* `max_results` (optional, int): Maximum number of search results to return. Default is 5.
* `topic` (optional, str): Category of the search. Can be "general", "news", or "finance". Default is "general".
* `include_answer` (optional, bool): Include an answer to original query in results. Default is False.
* `include_raw_content` (optional, bool): Include cleaned and parsed HTML of each search result. Default is False.
* `include_images` (optional, bool): Include a list of query related images in the response. Default is False.
* `include_image_descriptions` (optional, bool): Include descriptive text for each image. Default is False.
* `search_depth` (optional, str): Depth of the search, either "basic" or "advanced". Default is "basic".
* `time_range` (optional, str): The time range back from the current date ( publish date ) to filter results - "day", "week", "month", or "year". Default is None.
* `start_date` (optional, str): Will return all results after the specified start date ( publish date ). Required to be written in the format YYYY-MM-DD. Default is None.
* `end_date` (optional, str): Will return all results before the specified end date. Required to be written in the format YYYY-MM-DD. Default is None.
* `include_domains` (optional, List\[str]): List of domains to specifically include. Maximum 300 domains. Default is None.
* `exclude_domains` (optional, List\[str]): List of domains to specifically exclude. Maximum 150 domains. Default is None.

For a comprehensive overview of the available parameters, refer to the [Tavily Search API documentation](https://docs.tavily.com/documentation/api-reference/endpoint/search)

### Instantiation

```python  theme={null}
from langchain_tavily import TavilySearch

tool = TavilySearch(
    max_results=5,
    topic="general",
    # include_answer=False,
    # include_raw_content=False,
    # include_images=False,
    # include_image_descriptions=False,
    # search_depth="basic",
    # time_range="day",
    # start_date=None,
    # end_date=None,
    # include_domains=None,
    # exclude_domains=None
)
```

### Invoke directly with args

The Tavily search tool accepts the following arguments during invocation:

* `query` (required): A natural language search query
* The following arguments can also be set during invocation: `include_images`, `search_depth`, `time_range`, `include_domains`, `exclude_domains`, `start_date`, `end_date`
* For reliability and performance reasons, certain parameters that affect response size cannot be modified during invocation: `include_answer` and `include_raw_content`. These limitations prevent unexpected context window issues and ensure consistent results.

NOTE: The optional arguments are available for agents to dynamically set. If you set an argument during instantiation and then invoke the tool with a different value, the tool will use the value you passed during invocation.

### Direct Tool Invocation

```python  theme={null}
# Basic usage
result = tavily_search.invoke({"query": "What happened at the last wimbledon"})
```

Example output:

```python  theme={null}
{
 'query': 'What happened at the last wimbledon',
 'follow_up_questions': None,
 'answer': None,
 'images': [],
 'results': [
   {'url': 'https://en.wikipedia.org/wiki/Wimbledon_Championships',
    'title': 'Wimbledon Championships - Wikipedia',
    'content': 'Due to the COVID-19 pandemic, Wimbledon 2020 was cancelled ...',
    'score': 0.62365627198,
    'raw_content': None},
   {'url': 'https://www.cbsnews.com/news/wimbledon-men-final-carlos-alcaraz-novak-djokovic/',
    'title': "Carlos Alcaraz beats Novak Djokovic at Wimbledon men's final to ...",
    'content': 'In attendance on Sunday was Catherine, the Princess of Wales ...',
    'score': 0.5154731446,
    'raw_content': None}
 ],
 'response_time': 2.3
}
```

### Use with Agent

```python  theme={null}
# !pip install -qU langchain langchain-openai langchain-tavily
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

# Initialize the Tavily Search tool
tavily_search = TavilySearch(max_results=5, topic="general")

# Initialize the agent with the search tool
agent = create_agent(
    model=ChatOpenAI(model="gpt-5"),
    tools=[tavily_search],
    system_prompt="You are a helpful research assistant. Use web search to find accurate, up-to-date information."
)

# Use the agent
response = agent.invoke({
    "messages": [{"role": "user", "content": "What is the most popular sport in the world? Include only Wikipedia sources."}]
})
```

> **Tip**: For more relevant and time-aware results, inject today's date into your system prompt. This helps the agent understand the current context when searching for recent information. For example: `f"You are a helpful research assistant. Today's date is {datetime.today().strftime('%B %d, %Y')}. Use web search to find accurate, up-to-date information."`

## Tavily Extract

Here we show how to instantiate the Tavily extract tool. This tool allows you to extract content from URLs using Tavily's Extract API endpoint.

### Available Parameters

The Tavily Extract API accepts various parameters:

* `extract_depth` (optional, str): The depth of the extraction, either "basic" or "advanced". Default is "basic".
* `include_images` (optional, bool): Whether to include images in the extraction. Default is False.

For a comprehensive overview of the available parameters, refer to the [Tavily Extract API documentation](https://docs.tavily.com/documentation/api-reference/endpoint/extract)

### Instantiation

```python  theme={null}
from langchain_tavily import TavilyExtract

tool = TavilyExtract(
    extract_depth="basic",
    # include_images=False
)
```

### Invoke directly with args

The Tavily extract tool accepts the following arguments during invocation:

* `urls` (required): A list of URLs to extract content from.
* Both `extract_depth` and `include_images` can also be set during invocation

NOTE: The optional arguments are available for agents to dynamically set. If you set an argument during instantiation and then invoke the tool with a different value, the tool will use the value you passed during invocation.

### Direct Tool Invocation

```python  theme={null}
# Extract content from a URL
result = tavily_extract.invoke({
    "urls": ["https://en.wikipedia.org/wiki/Lionel_Messi"]
})
```

Example output:

```python  theme={null}
{
    'results': [{
        'url': 'https://en.wikipedia.org/wiki/Lionel_Messi',
        'raw_content': 'Lionel Messi\nLionel Andrés "Leo" Messi...',
        'images': []
    }],
    'failed_results': [],
    'response_time': 0.79
}
```

## Tavily Map/Crawl

Tavily provides two complementary tools for website exploration: **Map** and **Crawl**. The `map` tool discovers and lists URLs from a website, providing a structural overview without extracting content. The `crawl` tool then extracts the full content from these discovered URLs, making it ideal for data extraction, documentation indexing, and building knowledge bases.

### Tavily Map

The Map tool discovers all internal links starting from a base URL, perfect for understanding site structure or planning content extraction.

#### Available Parameters

* `url` (required, str): The root URL to begin mapping.
* `instructions` (optional, str): Natural language instructions guiding the mapping process.

For a comprehensive overview, refer to the [Tavily Map API documentation](https://docs.tavily.com/documentation/api-reference/endpoint/map)

#### Instantiation

```python  theme={null}
from langchain_tavily import TavilyMap

tool = TavilyMap()
```

#### Direct Tool Invocation

```python  theme={null}
# Map a website structure
result = tavily_map.invoke({
    "url": "https://docs.example.com",
    "instructions": "Find all documentation and tutorial pages"
})
```

Example output:

```python  theme={null}
{
    'base_url': 'https://docs.example.com',
    'results': [
        'https://docs.example.com',
        'https://docs.example.com/api',
        'https://docs.example.com/tutorials',
        'https://docs.example.com/api/endpoints',
        'https://docs.example.com/tutorials/getting-started'
    ],
    'request_id': 'req_abc123',
    'response_time': 2.1
}
```

### Tavily Crawl

The Crawl tool extracts full content from URLs. It works perfectly with mapped URLs or can be used standalone to crawl from a starting point.

#### Available Parameters

* `url` (required, str): The root URL to begin the crawl.
* `instructions` (optional, str): Natural language instructions guiding content extraction.

For a comprehensive overview, refer to the [Tavily Crawl API documentation](https://docs.tavily.com/documentation/api-reference/endpoint/crawl)

#### Instantiation

```python  theme={null}
from langchain_tavily import TavilyCrawl

tool = TavilyCrawl()
```

#### Direct Tool Invocation

```python  theme={null}
# Crawl and extract content
result = tavily_crawl.invoke({
    "url": "https://docs.example.com",
    "instructions": "Extract API documentation and code examples"
})
```

Example output:

```python  theme={null}
{
    'base_url': 'https://docs.example.com',
    'results': [
        {
            'url': 'https://docs.example.com',
            'raw_content': '# Documentation\nWelcome to our API documentation...'
        },
        {
            'url': 'https://docs.example.com/api',
            'raw_content': '# API Reference\nComplete API reference guide...'
        }
    ],
    'response_time': 4.5,
    'request_id': 'req_abc123'
}
```

## Tavily Research Agent

This example demonstrates how to build a powerful web research agent using Tavily's search and extract tools with `create_agent`.

### Features

* Internet Search: Query the web for up-to-date information using Tavily's search API
* Content Extraction: Extract and analyze specific content from web pages
* Seamless Integration: Simple, elegant agent setup with LangChain v1

```python  theme={null}
# !pip install -qU langchain langchain-openai langchain-tavily
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch, TavilyExtract

# Initialize Tavily tools
tavily_search = TavilySearch(max_results=5, topic="general")
tavily_extract = TavilyExtract()

# Create the research agent
agent = create_agent(
    model=ChatOpenAI(model="gpt-5"),
    tools=[tavily_search, tavily_extract],
    system_prompt="""You are a helpful research assistant. Use web search to find relevant 
    information, then extract detailed content from the most promising sources to provide 
    comprehensive insights."""
)

# Use the agent
response = agent.invoke({
    "messages": [{
        "role": "user", 
        "content": "Research the latest developments in quantum computing and provide a detailed summary of how it might impact cybersecurity in the next decade."
    }]
})
```

> **Tip**: For more relevant and time-aware results, inject today's date into your system prompt. This helps the agent understand the current context when searching for recent information. For example: `f"You are a helpful research assistant. Today's date is {datetime.today().strftime('%B %d, %Y')}. Use web search to find relevant information..."`


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.tavily.com/llms.txt