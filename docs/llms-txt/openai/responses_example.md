# Source: https://developers.openai.com/cookbook/examples/responses_api/responses_example.md

## What is the Responses API?

The Responses API is a new way to interact with OpenAI models, designed to be simpler and more flexible than previous APIs. It makes it easy to build advanced AI applications that use multiple tools, handle multi-turn conversations, and work with different types of data (not just text).

Unlike older APIs—such as Chat Completions, which were built mainly for text, or the Assistants API, which can require a lot of setup—the Responses API is built from the ground up for:

- Seamless multi-turn interactions (carry on a conversation across several steps in a single API call)
- Easy access to powerful hosted tools (like file search, web search, and code interpreter)
- Fine-grained control over the context you send to the model

As AI models become more capable of complex, long-running reasoning, developers need an API that is both asynchronous and stateful. The Responses API is designed to meet these needs.

In this guide, you'll see some of the new features the Responses API offers, along with practical examples to help you get started.

## Basics
By design, on the surface, the Responses API is very similar to the Completions API.

```python
from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input="tell me a joke",
)
```

```python
print(response.output[0].content[0].text)
```

```text
Why did the scarecrow win an award?

Because he was outstanding in his field!
```

One key feature of the Response API is that it is stateful. This means that you do not have to manage the state of the conversation by yourself, the API will handle it for you. For example, you can retrieve the response at any time and it will include the full conversation history.

```python
fetched_response = client.responses.retrieve(
response_id=response.id)

print(fetched_response.output[0].content[0].text)
```

```text
Why did the scarecrow win an award?

Because he was outstanding in his field!
```

You can continue the conversation by referring to the previous response.

```python
response_two = client.responses.create(
    model="gpt-4o-mini",
    input="tell me another",
    previous_response_id=response.id
)
```

```python
print(response_two.output[0].content[0].text)
```

```text
Why don't skeletons fight each other?

They don't have the guts!
```

You can of course manage the context yourself. But one benefit of OpenAI maintaining the context for you is that you can fork the response at any point and continue the conversation from that point.

```python
response_two_forked = client.responses.create(
    model="gpt-4o-mini",
    input="I didn't like that joke, tell me another and tell me the difference between the two jokes",
    previous_response_id=response.id # Forking and continuing from the first response
)

output_text = response_two_forked.output[0].content[0].text
print(output_text)
```

```text
Sure! Here’s another joke:

Why don’t scientists trust atoms?

Because they make up everything!

**Difference:** The first joke plays on a pun involving "outstanding" in a literal sense versus being exceptional, while the second joke relies on a play on words about atoms "making up" matter versus fabricating stories. Each joke uses wordplay, but they target different concepts (farming vs. science).
```

## Hosted Tools

Another benefit of the Responses API is that it adds support for hosted tools like `file_search` and `web_search`. Instead of manually calling the tools, simply pass in the tools and the API will decide which tool to use and use it.

Here is an example of using the `web_search` tool to incorporate web search results into the response.

```python
response = client.responses.create(
    model="gpt-4o",  # or another supported model
    input="What's the latest news about AI?",
    tools=[
        {
            "type": "web_search"
        }
    ]
)
```

```python
import json
print(json.dumps(response.output, default=lambda o: o.__dict__, indent=2))
```

_Matrix output omitted from the markdown export._

## Multimodal, Tool-augmented conversation

The Responses API natively supports text, images, and audio modalities. 
Tying everything together, we can build a fully multimodal, tool-augmented interaction with one API call through the responses API.

```python
import base64

from IPython.display import Image, display

# Display the image from the provided URL
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/2880px-Cat_August_2010-4.jpg"
display(Image(url=url, width=400))

response_multimodal = client.responses.create(
    model="gpt-4o",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": 
                 "Come up with keywords related to the image, and search on the web using the search tool for any news related to the keywords"
                 ", summarize the findings and cite the sources."},
                {"type": "input_image", "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/2880px-Cat_August_2010-4.jpg"}
            ]
        }
    ],
    tools=[
        {"type": "web_search"}
    ]
)
```

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/2880px-Cat_August_2010-4.jpg" width="400"/>

```python
import json
print(json.dumps(response_multimodal.__dict__, default=lambda o: o.__dict__, indent=4))
```

```text
{
    "id": "resp_67bd65392a088191a3b802a61f4fba14",
    "created_at": 1740465465.0,
    "error": null,
    "metadata": {},
    "model": "gpt-4o-2024-08-06",
    "object": "response",
    "output": [
        {
            "id": "msg_67bd653ab9cc81918db973f0c1af9fbb",
            "content": [
                {
                    "annotations": [],
                    "text": "Based on the image of a cat, some relevant keywords could be:\n\n- Cat\n- Feline\n- Pet\n- Animal care\n- Cat behavior\n\nI'll search for recent news related to these keywords.",
                    "type": "output_text",
                    "logprobs": null
                }
            ],
            "role": "assistant",
            "type": "message"
        },
        {
            "id": "ws_67bd653c7a548191af86757fbbca96e1",
            "status": "completed",
            "type": "web_search_call"
        },
        {
            "id": "msg_67bd653f34fc8191989241b2659fd1b5",
            "content": [
                {
                    "annotations": [
                        {
                            "index": null,
                            "title": "Cat miraculously survives 3 weeks trapped in sofa during family's cross-country move",
                            "type": "url_citation",
                            "url": "https://nypost.com/2025/02/24/us-news/cat-miraculously-survives-3-weeks-trapped-in-sofa-during-familys-cross-country-move/?utm_source=chatgpt.com"
                        },
                        {
                            "index": null,
                            "title": "Ex-College Soccer Player Accused of Killing Fellow Athlete Brother, Cat Using Knife, Golf Club: Prosecutors",
                            "type": "url_citation",
                            "url": "https://people.com/princeton-murder-soccer-player-accused-murdering-athlete-brother-11685671?utm_source=chatgpt.com"
                        },
                        {
                            "index": null,
                            "title": "Cuddly 8-Year-Old Cat Surrendered to Shelter for Being 'Too Affectionate' Inspires Dozens of Adoption Applications",
                            "type": "url_citation",
                            "url": "https://people.com/cat-surrendered-connecticut-shelter-too-affectionate-11684130?utm_source=chatgpt.com"
                        },
                        {
                            "index": null,
                            "title": "Emaciated cat found in Meriden abandoned in snow dies after rescue attempt, officials say",
                            "type": "url_citation",
                            "url": "https://www.ctinsider.com/recordjournal/article/meriden-animal-control-cat-neglected-abandoned-20172924.php?utm_source=chatgpt.com"
                        },
                        {
                            "index": null,
                            "title": "Cat proves mom correct by using human toilet",
                            "type": "url_citation",
                            "url": "https://nypost.com/video/cat-proves-mom-correct-by-using-human-toilet/?utm_source=chatgpt.com"
                        },
                        {
                            "index": null,
                            "title": "Litter-Robot 3 Connect Review",
                            "type": "url_citation",
                            "url": "https://www.thesprucepets.com/litter-robot-3-connect-review-8780105?utm_source=chatgpt.com"
                        },
                        {
                            "index": null,
                            "title": "Taylor Swift's favourite cat faces breeding ban",
                            "type": "url_citation",
                            "url": "https://www.thetimes.co.uk/article/taylor-swifts-favourite-cat-faces-breeding-ban-k32nvf6kv?utm_source=chatgpt.com"
                        }
                    ],
                    "text": "Here are some recent news stories related to cats:\n\n**1. Cat Survives Three Weeks Trapped in Sofa During Move**\n\nA cat named Sunny-Loo survived three weeks trapped inside a sofa during the Hansons' move from Washington state to Colorado. After disappearing during the move, she was discovered emaciated but alive when the family unpacked their furniture. Sunny-Loo received intensive care and has since been reunited with her family. ([nypost.com](https://nypost.com/2025/02/24/us-news/cat-miraculously-survives-3-weeks-trapped-in-sofa-during-familys-cross-country-move/?utm_source=chatgpt.com))\n\n**2. Man Charged with Killing Brother and Family Cat**\n\nMatthew Hertgen, a former college soccer player, has been charged with the murder of his younger brother, Joseph Hertgen, and animal cruelty for allegedly killing the family cat. The incident occurred in Princeton, New Jersey, where authorities found Joseph's body with signs of trauma. Matthew faces multiple charges, including first-degree murder. ([people.com](https://people.com/princeton-murder-soccer-player-accused-murdering-athlete-brother-11685671?utm_source=chatgpt.com))\n\n**3. \"Too Affectionate\" Cat Sparks Adoption Interest**\n\nAn 8-year-old cat named Ravi was surrendered to a Connecticut shelter for being \"too affectionate.\" A TikTok video highlighting his story went viral, amassing over 12.6 million views and leading to more than 160 adoption applications. Ravi now has an adoption appointment, and the shelter has gained increased attention for its other adoptable pets. ([people.com](https://people.com/cat-surrendered-connecticut-shelter-too-affectionate-11684130?utm_source=chatgpt.com))\n\n**4. Emaciated Cat Found in Snow Dies After Rescue Attempt**\n\nA severely neglected cat named Lizzy was found abandoned in a snowbank in Meriden, Connecticut. Despite rescue efforts, Lizzy did not survive. Authorities are seeking information to identify the person responsible for her abandonment, with a reward offered for leads. ([ctinsider.com](https://www.ctinsider.com/recordjournal/article/meriden-animal-control-cat-neglected-abandoned-20172924.php?utm_source=chatgpt.com))\n\n**5. Cat Uses Human Toilet, Surprising Family**\n\nIn the UK, a cat named Cruise surprised his family by using a human toilet. Despite initial skepticism from her partner and son, Hayley Bibby captured footage of Cruise's bathroom habits, validating her claims. The family now accommodates Cruise's preference by leaving the toilet seat up. ([nypost.com](https://nypost.com/video/cat-proves-mom-correct-by-using-human-toilet/?utm_source=chatgpt.com))\n\n**6. Litter-Robot 3 Connect: A High-Tech Litter Box Review**\n\nThe Litter-Robot 3 Connect, priced at $499, offers a self-cleaning solution for cat owners averse to scooping litter. While effective and reducing litter usage by 50%, some users note that odor prevention could be improved. The device includes features like a night light and smartphone app integration. ([thesprucepets.com](https://www.thesprucepets.com/litter-robot-3-connect-review-8780105?utm_source=chatgpt.com))\n\n**7. Taylor Swift's Favorite Cat Breed Faces Breeding Ban**\n\nThe Scottish Fold cat breed, favored by celebrities like Taylor Swift, may face a breeding ban in Britain due to inheritable health issues. These cats often suffer from painful conditions caused by defective cartilage formation. The Animal Welfare Committee has recommended prohibiting the breeding of such cats to prevent further health problems. ([thetimes.co.uk](https://www.thetimes.co.uk/article/taylor-swifts-favourite-cat-faces-breeding-ban-k32nvf6kv?utm_source=chatgpt.com))\n\n\n# Recent Cat-Related News Stories:\n- [Cat miraculously survives 3 weeks trapped in sofa during family's cross-country move](https://nypost.com/2025/02/24/us-news/cat-miraculously-survives-3-weeks-trapped-in-sofa-during-familys-cross-country-move/?utm_source=chatgpt.com)\n- [Ex-College Soccer Player Accused of Killing Fellow Athlete Brother, Cat Using Knife, Golf Club: Prosecutors](https://people.com/princeton-murder-soccer-player-accused-murdering-athlete-brother-11685671?utm_source=chatgpt.com)\n- [Cuddly 8-Year-Old Cat Surrendered to Shelter for Being 'Too Affectionate' Inspires Dozens of Adoption Applications](https://people.com/cat-surrendered-connecticut-shelter-too-affectionate-11684130?utm_source=chatgpt.com)\n ",
                    "type": "output_text",
                    "logprobs": null
                }
            ],
            "role": "assistant",
            "type": "message"
        }
    ],
    "temperature": 1.0,
    "tool_choice": "auto",
    "tools": [
        {
            "type": "web_search",
            "location": null,
            "sites": null
        }
    ],
    "top_p": 1.0,
    "max_completion_tokens": null,
    "previous_response_id": null,
    "reasoning_effort": null,
    "text": {
        "format": {
            "type": "text"
        },
        "stop": null
    },
    "top_logprobs": null,
    "truncation": "disabled",
    "usage": {
        "completion_tokens": null,
        "prompt_tokens": null,
        "total_tokens": 1370,
        "completion_tokens_details": null,
        "prompt_tokens_details": null
    }
}
```

In the above example, we were able to use the `web_search` tool to search the web for news related to the image in one API call instead of multiple round trips that would be required if we were using the Chat Completions API.

With the responses API
🔥 a single API call can handle:

✅ Analyze a given image using a multimodal input.

✅ Perform web search via the `web_search` hosted tool

✅ Summarize the results.

In contrast, With Chat Completions API would require multiple steps, each requiring a round trip to the API:

1️⃣ Upload image and get analysis → 1 request

2️⃣ Extract info, call external web search → manual step + tool execution

3️⃣ Re-submit tool results for summarization → another request

See the following diagram for a side by side visualized comparison!

![Responses vs Completions](https://developers.openai.com/cookbook/assets/images/comparisons.png)


We are very excited for you to try out the Responses API and see how it can simplify your code and make it easier to build complex, multimodal, tool-augmented interactions!