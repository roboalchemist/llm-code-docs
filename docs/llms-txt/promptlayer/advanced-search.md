# Source: https://docs.promptlayer.com/why-promptlayer/advanced-search.md

# Advanced Search

PromptLayer advanced search capabilities allows you to find exactly what you want using tags, search queries, metadata, favorites, and score filtering.

## Using the Search Bar

To start your search, enter the keywords you want to find into the search bar and click on the "Search" button. You can use freeform search to find any text within the PromptLayer.

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/advanced-search.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=f28362116ebc148ec471a3084f0fbac1" alt="Advanced Search" data-og-width="318" width="318" data-og-height="346" height="346" data-path="images/advanced-search.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/advanced-search.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=b75da1ce6d99ea87409f7c099a460a2c 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/advanced-search.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=2b0a332230fa67778fc89186a919a743 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/advanced-search.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=a8b75522e84fc32f330132f66697aaf0 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/advanced-search.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=91f59c1bf008a0869bc20833a4580beb 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/advanced-search.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=d788cd2a597ad7b0bfe3108f06ec63f0 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/advanced-search.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=ce7b92db118c9171f9bdbbb7ede8dc09 2500w" />

## Advanced Search Filters

#### Metadata Search

Use the metadata search filter to search for specific metadata within the PromptLayer. You can search for user IDs, session IDs, tokens, error messages, status codes, and other metadata by entering the metadata field name and value into the search bar.

PromptLayer allows you to attach multiple key value pairs as metadata to a request. In the dashboard, you can look up requests and analyze analytics using metadata. The method for adding metadata to a request can be found in our documentation [here](/features/prompt-history/tracking-metadata-and-request-ids.mdx).

<CodeGroup>
  ```python Python theme={null}
  promptlayer_client.track.metadata(
    request_id=pl_request_id,
    metadata={
        "user_id":"1abf2345f",
        "session_id": "2cef2345f",
        "error_message": "None"
    }
  )
  ```

  ```js JavaScript theme={null}
  promptLayerClient.track.metadata({
    request_id:pl_request_id,
    metadata:{
        "user_id":"1abf2345f",
        "session_id": "2cef2345f",
        "error_message": "None"
    }
  })
  ```
</CodeGroup>

The metadata search filter works by clicking on "Key" in the advanced search filter, selecting the desired metadata key (in this case, user\_id), selecting the relevant value under "Value", and clicking "Add filter".

<img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/metadata-search.gif?s=4305dfa2b63187fdc51eb9ada1ad237d" width="80%" data-og-width="738" data-og-height="580" data-path="images/metadata-search.gif" data-optimize="true" data-opv="3" />

#### Score Filtering

Use the score filtering feature to search for prompts based on their scores. You can filter prompts by selecting the score range in the "Score" dropdown.

Score filtering is a powerful tool for analyzing the performance of your prompts. You can use it to identify high-performing prompts, or to find prompts that may need improvement.

<img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/score-filter.gif?s=1b9da2d38eff3c549dafe85a535a5b05" width="80%" data-og-width="800" data-og-height="480" data-path="images/score-filter.gif" data-optimize="true" data-opv="3" />

Below is an example of how you can score a request programmatically. It can also be done through the dashboard as shown [here](/features/prompt-history/scoring-requests).

<CodeGroup>
  ```python Python theme={null}
  promptlayer_client.track.score(
    request_id=pl_request_id, 
    score_name="summarization", # optional score name
    score=100
  )
  ```

  ```js JavaScript theme={null}
  promptLayerClient.track.score({
    request_id: pl_request_id,
    score: 100
  })
  ```
</CodeGroup>

#### Tags Search

Use the tags search filter to search for specific tags within the PromptLayer.

Tags are used to group product features, prod/dev versions, and other categories. You can search for tags by selecting them in the "Tags" dropdown.

Tagging a request is easy. Read more about it [here](/features/prompt-history/organizing-with-tags).

<CodeGroup>
  ```python Python Native theme={null}
  openai.Completion.create(
    engine="text-ada-001", 
    prompt="My name is", 
    pl_tags=["mytag1", "mytag2"]
  )
  ```

  ```js JavaScript theme={null}
  openai.completions.create({
    model:"text-ada-001", 
    prompt:"My name is", 
    pl_tags:["mytag1", "mytag2"]
  })
  ```

  ```python Python LangChain theme={null}
  from langchain.llms import PromptLayerOpenAI
  llm = PromptLayerOpenAI(pl_tags=["mytag1", "mytag2"])
  resp = llm("tell me a joke")
  ```
</CodeGroup>

#### Favorites

By selecting the "favorite" tag, you can narrow by favorited requests. To favorite a request, click the star on the top right on the dashboard.

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/favorites.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=55a51b8e7e425801be43b62c1b72366d" alt="Favorites" data-og-width="1472" width="1472" data-og-height="857" height="857" data-path="images/favorites.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/favorites.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=9a5dc4c602f01ca9a142100526a68861 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/favorites.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=e938bb79344794aa13b803e9600748a4 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/favorites.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=734d4728f74934134ed2fb86808058ce 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/favorites.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=687f3e40429a1968727c31008d5373a8 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/favorites.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=29d75ed5a7fb637cee3baf0e6b011d65 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/favorites.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=2d116d1a6a01af7dae0f766f3444c202 2500w" />


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt