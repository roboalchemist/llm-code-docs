# Dappier Tool

## Overview

The `DappierRealTimeSearchTool` and `DappierAIRecommendationTool` empower AI applications with real-time data and AI-driven insights. The `DappierRealTimeSearchTool` provides access to up-to-date information across news, weather, travel, and financial markets, while the `DappierAIRecommendationTool` enhances applications with factual, premium content from domains like News, Finance, and Sports, powered by Dappier's pre-trained RAG models and natural language APIs.

## DappierRealTimeSearchTool

You can also check this cookbook in colab [here](https://colab.research.google.com/drive/1rgQS9h2RaIjL-o7ofVEdRhQeKPguNmDb?usp=sharing)

### Watch the Video

If you prefer a visual walkthrough, check out the accompanying video below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/VSoffX2-1yM?si=SeXum8BeROvqe8TD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

### Features

The `DappierRealTimeSearchTool` provides real-time Google search results, including:

* Latest news, weather, and travel deals
* Up-to-date financial news, stock prices, and trades
* AI-enhanced insights for accurate and fast information retrieval

### Instantiation

```python Python theme={null}
from langchain_dappier import DappierRealTimeSearchTool

tool = DappierRealTimeSearchTool(
    # ai_model_id="...", # Overwrite default AI model ID
    # name="...",        # Overwrite default tool name
    # description="...", # Overwrite default tool description
)
```

### Usage

#### Direct Invocation

```python Python theme={null}
tool.invoke({"query": "What happened at the last Wimbledon"})
```

```json  theme={null}
"At the last Wimbledon in 2024, Carlos Alcaraz won the title by defeating Novak Djokovic. This victory marked Alcaraz's fourth Grand Slam title at just 21 years old! 🎉🏆🎾"
```

#### Using ToolCall

```python Python theme={null}
model_generated_tool_call = {
    "args": {"query": "Euro 2024 host nation"},
    "id": "1",
    "name": "dappier",
    "type": "tool_call",
}
tool_msg = tool.invoke(model_generated_tool_call)
print(tool_msg.content[:400])
```

```json  theme={null}
Euro 2024 is being hosted by Germany! 🇩🇪 The tournament runs from June 14 to July 14, 2024, featuring 24 teams competing across various cities like Berlin and Munich. It's going to be an exciting summer of football! ⚽️🏆
```

#### Chaining with LLM

```python Python theme={null}
from langchain.chat_models import init_chat_model

llm = init_chat_model(model="gpt-4o", model_provider="openai", temperature=0)
```

```python Python theme={null}
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableConfig, chain

today = datetime.datetime.today().strftime("%D")
prompt = ChatPromptTemplate([
    ("system", f"You are a helpful assistant. The date today is {today}.")
])

llm_with_tools = llm.bind_tools([tool])
llm_chain = prompt | llm_with_tools

tool_chain = chain(lambda user_input, config: llm_chain.invoke({"user_input": user_input}, config=config))

tool_chain.invoke("Who won the last women's singles Wimbledon?")
```

```json  theme={null}
AIMessage(content="Barbora Krejčíková won the women's singles title at Wimbledon 2024, defeating Jasmine Paolini in the final with a score of 6–2, 2–6, 6–4. This victory marked her first Wimbledon singles title and her second major singles title overall! 🎉🏆🎾", additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 69, 'prompt_tokens': 222, 'total_tokens': 291, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': 'fp_4691090a87', 'finish_reason': 'stop', 'logprobs': None}, id='run-87a385dd-103b-4344-a3be-2d6fd1dcfdf5-0', usage_metadata={'input_tokens': 222, 'output_tokens': 69, 'total_tokens': 291, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})
```

### Parameters

#### `ai_model_id` (str) *Optional*:

* The AI model ID to use for the query.
* AI model IDs always start with the prefix `"am_"`.
* Defaults to `"am_01j06ytn18ejftedz6dyhz2b15"`.
* Multiple AI model IDs are available, which can be found at
  [Dappier marketplace.](https://platform.dappier.com/marketplace)

***

## DappierAIRecommendationTool

### Watch the Video

If you prefer a visual walkthrough, check out the accompanying video below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/oFaCY3K0iTw?si=frdByRZEqLBejq4q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

### Features

The `DappierAIRecommendationTool` delivers AI-powered recommendations using Dappier's pre-trained RAG models:

* Provides factual and up-to-date responses
* Sources premium content from News, Finance, Sports, and more

### Instantiation

```python Python theme={null}
from langchain_dappier import DappierAIRecommendationTool

tool = DappierAIRecommendationTool(
    data_model_id="dm_01j0pb465keqmatq9k83dthx34",
    similarity_top_k=3,
    ref="sportsnaut.com",
    num_articles_ref=2,
    search_algorithm="most_recent",
)
```

### Usage

#### Direct Invocation

```python Python theme={null}
tool.invoke({"query": "latest sports news"})
```

```json  theme={null}
[
    {
        "author": "Matt Weaver",
        "image_url": "https://images.dappier.com/dm_01j0pb465keqmatq9k83dthx34/Screenshot_20250117_021643_Gallery_.jpg?width=428&height=321",
        "pubdate": "Fri, 17 Jan 2025 08:04:03 +0000",
        "source_url": "https://sportsnaut.com/chili-bowl-thursday-bell-column/",
        "summary": "The article highlights the thrilling unpredictability of the Chili Bowl Midget Nationals, focusing on the dramatic shifts in fortune for drivers like Christopher Bell, Tanner Thorson, and Karter Sarff during Thursday's events. Key moments included Sarff's unfortunate pull-off and a last-lap crash that allowed Ryan Bernal to capitalize and improve his standing, showcasing the chaotic nature of the race and the importance of strategy and luck.\n\nAs the competition intensifies leading up to Championship Saturday, Bell faces the challenge of racing from a Last Chance Race, reflecting on the excitement and difficulties of the sport. The article emphasizes the emotional highs and lows experienced by racers, with insights from Bell and Bernal on the unpredictable nature of racing. Overall, it captures the camaraderie and passion that define the Chili Bowl, illustrating how each moment contributes to the event's narrative.",
        "title": "Thursday proves why every lap of Chili Bowl is so consequential"
    },
    {
        "author": "Matt Higgins",
        "image_url": "https://images.dappier.com/dm_01j0pb465keqmatq9k83dthx34/Pete-Alonso-24524027_.jpg?width=428&height=321",
        "pubdate": "Fri, 17 Jan 2025 02:48:42 +0000",
        "source_url": "https://sportsnaut.com/new-york-mets-news-pete-alonso-rejected-last-ditch-contract-offer/",
        "summary": "The New York Mets are likely parting ways with star first baseman Pete Alonso after failing to finalize a contract agreement. Alonso rejected a last-minute three-year offer worth between $68 and $70 million, leading the Mets to redirect funds towards acquiring a top reliever. With Alonso's free-agent options dwindling, speculation arises about his potential signing with another team for the 2025 season, while the Mets plan to shift Mark Vientos to first base.\n\nIn a strategic move, the Mets are also considering a trade for Toronto Blue Jays' star first baseman Vladimir Guerrero Jr. This potential acquisition aims to enhance the Mets' competitiveness as they reshape their roster. Guerrero's impressive offensive stats make him a valuable target, and discussions are in the early stages. Fans and analysts are keenly watching the situation, as a trade involving such a prominent player could significantly impact both teams.",
        "title": "MLB insiders reveal New York Mets’ last-ditch contract offer that Pete Alonso rejected"
    },
    {
        "author": "Jim Cerny",
        "image_url": "https://images.dappier.com/dm_01j0pb465keqmatq9k83dthx34/NHL-New-York-Rangers-at-Utah-25204492_.jpg?width=428&height=321",
        "pubdate": "Fri, 17 Jan 2025 05:10:39 +0000",
        "source_url": "https://www.foreverblueshirts.com/new-york-rangers-news/stirring-5-3-comeback-win-utah-close-road-trip/",
        "summary": "The New York Rangers achieved a thrilling 5-3 comeback victory against the Utah Hockey Club, showcasing their resilience after a prior overtime loss. The Rangers scored three unanswered goals in the third period, with key contributions from Reilly Smith, Chris Kreider, and Artemi Panarin, who sealed the win with an empty-net goal. This victory marked their first win of the season when trailing after two periods and capped off a successful road trip, improving their record to 21-20-3.\n\nIgor Shesterkin's strong performance in goal, along with Arthur Kaliyev's first goal for the team, helped the Rangers overcome an early deficit. The game featured multiple lead changes, highlighting the competitive nature of both teams. As the Rangers prepare for their next game against the Columbus Blue Jackets, they aim to close the gap in the playoff race, with the Blue Jackets currently holding a five-point lead in the Eastern Conference standings.",
        "title": "Rangers score 3 times in 3rd period for stirring 5-3 comeback win against Utah to close road trip"
    }
]
```

#### Using ToolCall

```python Python theme={null}
model_generated_tool_call = {
    "args": {"query": "top 3 news articles"},
    "id": "1",
    "name": "dappier",
    "type": "tool_call",
}
tool_msg = tool.invoke(model_generated_tool_call)
print(tool_msg.content[:400])
```

```json  theme={null}
[{"author": "Matt Johnson", "image_url": "https://images.dappier.com/dm_01j0pb465keqmatq9k83dthx34/MLB-New-York-Mets-at-Colorado-Rockies-23948644_.jpg?width=428&height=321", "pubdate": "Fri, 17 Jan 2025 13:31:02 +0000", "source_url": "https://sportsnaut.com/new-york-mets-rumors-vladimir-guerrero-jr-news/", "summary": "The New York Mets are refocusing their strategy after failing to extend a contra
```

### Parameters

#### `data_model_id` (str) *Optional*:

* The data model ID to use for recommendations.
* Data model IDs always start with the prefix `"dm_"`.
* Defaults to `"dm_01j0pb465keqmatq9k83dthx34"`.

#### `similarity_top_k` (int) *Optional*:

* The number of top documents to retrieve based on similarity.
* Defaults to `9`.

#### `ref` (str) *Optional*:

* The site domain where AI recommendations should be displayed.
* Defaults to `None`.

#### `num_articles_ref` (int) *Optional*:

* The minimum number of articles to return from the specified reference domain (`ref`).
* The remaining articles will come from other sites in the RAG model.
* Defaults to `0`.

#### `search_algorithm` (str) *Optional*:

* The search algorithm to use for retrieving articles.
* Options:
  * `"most_recent"` (default),
  * `"semantic"`,
  * `"most_recent_semantic"`,
  * `"trending"`.

***