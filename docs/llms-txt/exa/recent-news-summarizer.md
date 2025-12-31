# Source: https://docs.exa.ai/examples/recent-news-summarizer.md

# Building a News Summarizer

> Learn how to build an AI-powered news summarizer that searches and summarizes recent articles using Exa and GPT.

***

In this example, we will build an LLM-based news summarizer with the Exa API to keep us up-to-date with the latest news on a given topic. We'll do this in three steps:

1. Generate search queries for Exa using an LLM
2. Retrieve relevant URLs and their contents using Exa
3. Summarize webpage contents using GPT-3.5 Turbo

This is a form of Retrieval Augmented Generation (RAG), combining Exa's search capabilities with GPT's summarization abilities.

The Jupyter notebook for this tutorial is available on [Colab](https://colab.research.google.com/drive/1uZ0kxFCWmCqozl3ArTJohNpRbeEYlwlT?usp=sharing) for easy experimentation. You can also [check it out on Github](https://github.com/exa-labs/exa-py/tree/master/examples/newssummarizer/summarizer.ipynb), including a [plain Python version](https://github.com/exa-labs/exa-py/tree/master/examples/newssummarizer/summarizer.py) if you want to skip to the complete product.

***

## Get Started

<Steps>
  <Step title="Pre-requisites and installation">
    Install the required packages:

    ```python  theme={null}
    pip install exa_py openai
    ```

    <Note> You'll need both an Exa API key and an OpenAI API key to run this example. You can get your OpenAI API key [here](https://platform.openai.com/api-keys).</Note>

    <Card title="Get your Exa API key" icon="key" horizontal href="https://dashboard.exa.ai/api-keys" />

    Set up your API keys:

    ```python  theme={null}
    from google.colab import userdata # comment this out if you're not using Colab

    EXA_API_KEY = userdata.get('EXA_API_KEY') # replace with your Exa API key
    OPENAI_API_KEY = userdata.get('OPENAI_API_KEY') # replace with your OpenAI API key
    ```
  </Step>

  <Step title="Initialize the clients">
    Import and set up both the OpenAI and Exa clients:

    ```python  theme={null}
    import openai
    from exa_py import Exa

    openai.api_key = OPENAI_API_KEY
    exa = Exa(EXA_API_KEY)
    ```
  </Step>

  <Step title="Generate a search query">
    First, we'll use GPT to generate an optimized search query based on the user's question:

    ```python  theme={null}
    SYSTEM_MESSAGE = "You are a helpful assistant that generates search queries based on user questions. Only generate one search query."
    USER_QUESTION = "What's the recent news in physics this week?"

    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": USER_QUESTION},
        ],
    )

    search_query = completion.choices[0].message.content

    print("Search query:")
    print(search_query)
    ```
  </Step>

  <Step title="Search for recent articles">
    Now we'll use Exa to search for recent articles, filtering by publication date:

    ```python  theme={null}
    from datetime import datetime, timedelta

    one_week_ago = (datetime.now() - timedelta(days=7))
    date_cutoff = one_week_ago.strftime("%Y-%m-%d")

    search_response = exa.search_and_contents(
        search_query, start_published_date=date_cutoff
    )

    urls = [result.url for result in search_response.results]
    print("URLs:")
    for url in urls:
        print(url)
    ```

    <Note>
      We use `start_published_date` to filter for recent content.
    </Note>
  </Step>

  <Step title="Get article contents">
    Exa's `search_and_contents` already retrieved the article contents for us, so we can access them directly:

    ```python  theme={null}
    results = search_response.results
    result_item = results[0]
    print(f"{len(results)} items total, printing the first one:")
    print(result_item.text)
    ```

    <Note>
      Unlike traditional search engines that only return URLs, Exa gives us direct access to the webpage contents, eliminating the need for web scraping.
    </Note>
  </Step>

  <Step title="Generate a summary">
    Finally, we'll use GPT to create a concise summary of the article:

    ```python  theme={null}
    import textwrap

    SYSTEM_MESSAGE = "You are a helpful assistant that briefly summarizes the content of a webpage. Summarize the users input."

    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": result_item.text},
        ],
    )

    summary = completion.choices[0].message.content

    print(f"Summary for {urls[0]}:")
    print(result_item.title)
    print(textwrap.fill(summary, 80))
    ```

    And we're done! We've built an app that translates a question into a search query, uses Exa to search for useful links and their contents, and summarizes the content to effortlessly answer questions about the latest news.

    **Through Exa, we have given our LLM access to the entire Internet.** The possibilities are endless.
  </Step>
</Steps>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt