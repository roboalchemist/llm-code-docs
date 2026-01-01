# Source: https://docs.promptlayer.com/features/prompt-history/tagging-requests.md

# Tags

While using PromptLayer, over time the number of logs will grow, making it difficult to find what you are looking for. Tags are a great way to help keep things organized.

Tags can be used for whatever you want, but the top 2 ways are to:

1. Keep track of which application you are working on
2. If you are chaining prompts together, where you are in the pipeline

For example, if you are working on an email application that has three chained stages, it would be a good idea to tag all the requests in this application with `email` and the corresponding stage `stage-x`

To add a tag, add the keyword argument `pl_tags` into your OpenAI request like so:

<CodeGroup>
  ```python Python SDK theme={null}
  openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",
    prompt="My name is",
    pl_tags=["pipeline3", "world"] # 🍰 PromptLayer tags
  )
  ```

  ```js JavaScript theme={null}
  openai.completions.create({
    model: "gpt-3.5-turbo-instruct",
    prompt: "My name is",
    pl_tags: ["pipeline3", "world"], // 🍰 PromptLayer tags
  });
  ```

  ```python Python (LangChain) theme={null}
  llm = OpenAI(
      model_name="gpt-3.5-turbo-instruct",
      callbacks=[
          PromptLayerCallbackHandler(
              pl_tags=["pipeline3", "world"] # 🍰 PromptLayer tags
          ),
      ],
  )
  response = llm("My name is")
  ```

  ```js Javascript (LangChain) theme={null}
  const llm = new PromptLayerOpenAI({
    temperature: 0.9,
    openAIApiKey: process.env.OPENAI_API_KEY,
    promptLayerApiKey: process.env.PROMPTLAYER_API_KEY,
    plTags: ["pipeline3", "world"], // 🍰 PromptLayer tags
  });
  llm.call("My name is");
  ```
</CodeGroup>

Alternatively, use the REST API endpoint `/log-request` ([read more](/reference/log-request)).

This will then show up on your PromptLayer dashboard:

<img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/tags.png?fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=12e8c5889e88daef3bcd2f795529bb7b" alt="" srcSet="" width="50%" data-og-width="2000" data-og-height="440" data-path="images/tags.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/tags.png?w=280&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=39de63c8c6e8b19d2ab24921dc6a8cae 280w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/tags.png?w=560&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=45962a8f057b53db1c763f1cb0da441d 560w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/tags.png?w=840&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=4795a54deda368b67a425dbf6893b050 840w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/tags.png?w=1100&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=ae3746a85af0f44bb8d0aad2cc8128e5 1100w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/tags.png?w=1650&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=8f83b590ffad26a256acc4c2bf313ca0 1650w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/tags.png?w=2500&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=d93bb820417c53cb07e4a9d4b4d9ae74 2500w" />

And can be filtered by clicking on the tags button by the search-bar:

## <img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/tag-filter.png?fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=f0fe4776add090dbb7991cefac014cd5" alt="" srcSet="" width="50%" data-og-width="2000" data-og-height="2984" data-path="images/tag-filter.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/tag-filter.png?w=280&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=905bc334f0c291882bf120f77a5df9d2 280w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/tag-filter.png?w=560&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=dcb0bd60a34de7144cc2c68ff1ac7494 560w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/tag-filter.png?w=840&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=13fa6a336ba94bb1b43127fcc01915c3 840w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/tag-filter.png?w=1100&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=f513331856c41f0cad05adfe1e763516 1100w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/tag-filter.png?w=1650&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=96786bbaf45f2255e635ad7b5d9e575c 1650w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/tag-filter.png?w=2500&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=d56e6b50790eaaf38a467023d8790aea 2500w" />

Please note that tags are optimized for categorization based on a small number of predefined options. For request enrichments with n > 1000 options, please use [metadata](/features/prompt-history/metadata) instead.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt