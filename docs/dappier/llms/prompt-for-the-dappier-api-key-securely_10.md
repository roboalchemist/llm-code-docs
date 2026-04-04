# Prompt for the Dappier API key securely
dappier_api_key = getpass("Enter your API key: ")
os.environ["DAPPIER_API_KEY"] = dappier_api_key
```

## Dappier Real Time Search Tool

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/198d5yecGz48Yd84L8d04tcwmGS-Kk0xs?usp=sharing)

The `DappierRealTimeSearchToolSpec` allows LLMs to access real-time data across the web, including the latest news, weather, financial updates, and more.

### Watch the Video Guide

If you prefer a visual walkthrough, check out the accompanying video guide below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/7yZZE-9S7LM?si=CGLURgnTqQyyJjzb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

### Initialize the Tool

You can initialize the real-time search tool and convert it into a list of tools ready for use:

```python Python theme={null}
from llama_index.tools.dappier import DappierRealTimeSearchToolSpec

dappier_tool = DappierRealTimeSearchToolSpec()

dappier_tool_list = dappier_tool.to_tool_list()
for tool in dappier_tool_list:
    print(tool.metadata.name)
```

```json  theme={null}
search_real_time_data
search_stock_market_data
```

### Real-Time Web Search

Query real-time web content such as news, weather, or general updates.

```python Python theme={null}
print(dappier_tool.search_real_time_data("How is the weather in New York today?"))
```

```json  theme={null}
"Partly cloudy in New York today with highs around 65°F and a chance of light rain in the evening."
```

### Stock Market Data

Access real-time financial insights and stock news.

```python Python theme={null}
print(dappier_tool.search_stock_market_data("latest financial news on Meta"))
```

```json  theme={null}
"Meta shares rose 2.5% following an announcement of new AI products, as reported by Bloomberg."
```

### Parameters

The `DappierRealTimeSearchToolSpec` methods support the following parameter:

#### `query` (str)

* A natural language query used to retrieve real-time data from web sources or financial platforms.
* This parameter is required for both `search_real_time_data` and `search_stock_market_data`.

## Dappier AI Recommendations Tool

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kPoOWhk63aNbBM5uqd9A55jmYY4EbtPL?usp=sharing)

The `DappierAIRecommendationsToolSpec` provides intelligent, real-time content recommendations across a variety of verticals including sports, lifestyle, pet care, sustainable living, and local news. These recommendations come from trusted content partners and are tailored based on user queries.

### Watch the Video Guide

If you prefer a visual walkthrough, check out the accompanying video guide below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/jq4y5f-WuXQ?si=e6ZTjGNtJmDQb-bA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

### Initialize the Tool

```python Python theme={null}
from llama_index.tools.dappier import DappierAIRecommendationsToolSpec

dappier_tool = DappierAIRecommendationsToolSpec()

dappier_tool_list = dappier_tool.to_tool_list()
for tool in dappier_tool_list:
    print(tool.metadata.name)
```

```json  theme={null}
get_sports_news_recommendations
get_lifestyle_news_recommendations
get_iheartdogs_recommendations
get_iheartcats_recommendations
get_greenmonster_recommendations
get_wishtv_recommendations
get_nine_and_ten_news_recommendations
```

### Sports News Recommendations

```python Python theme={null}
print(
    dappier_tool.get_sports_news_recommendations(
        query="latest sports news", similarity_top_k=1
    )
)
```

```json  theme={null}
Result 1:
Title: Vincent Trocheck’s overtime goal lifts Rangers past Wild 5-4 for crucial victory
Author: Jim Cerny
Published on: Thu, 03 Apr 2025 02:23:30 +0000
Source: Forever Blueshirts (www.foreverblueshirts.com)
URL: https://www.foreverblueshirts.com/new-york-rangers-news/vincent-trocheck-overtime-goal-victory-wild/
Image URL: https://images.dappier.com/dm_01j0pb465keqmatq9k83dthx34/NHL-Edmonton-Oilers-at-New-York-Rangers-25723775_.jpg?width=428&height=321
Summary: Vincent Trocheck's overtime goal gave the Rangers a 5-4 win over the Minnesota Wild, tying them with the Canadiens in the playoff race. Panarin had a goal and two assists.
Score: None
```

### Lifestyle News

```python Python theme={null}
print(
    dappier_tool.get_lifestyle_news_recommendations(
        query="latest lifestyle updates", similarity_top_k=1
    )
)
```

```json  theme={null}
Result 1:
Title: Top 10 Travel Trends for 2025
Author: Jane Doe
Published on: Thu, 03 Apr 2025 02:00:00 +0000
Source: The Mix (www.themix.com)
URL: https://www.themix.com/travel/travel-trends-2025/
Image URL: https://images.dappier.com/example/travel-trends.jpg
Summary: From eco-tourism to remote work getaways, these are the top trends shaping how we explore the world in 2025.
Score: None
```

### iHeartDogs Articles

```python Python theme={null}
print(
    dappier_tool.get_iheartdogs_recommendations(
        query="dog care tips", similarity_top_k=1
    )
)
```

```json  theme={null}
Result 1:
Title: 5 Essential Grooming Tips for Your Dog
Author: Sarah Barkley
Published on: Thu, 03 Apr 2025 01:45:00 +0000
Source: iHeartDogs (www.iheartdogs.com)
URL: https://www.iheartdogs.com/grooming-tips-for-dogs/
Image URL: https://images.dappier.com/example/grooming-tips.jpg
Summary: Keep your pup clean and healthy with these five simple grooming tips from pet care professionals.
Score: None
```

### iHeartCats Articles

```python Python theme={null}
print(
    dappier_tool.get_iheartcats_recommendations(
        query="cat care advice", similarity_top_k=1
    )
)
```

```json  theme={null}
Result 1:
Title: Understanding Your Cat's Body Language
Author: Jenna Whiskers
Published on: Thu, 03 Apr 2025 01:35:00 +0000
Source: iHeartCats (www.iheartcats.com)
URL: https://www.iheartcats.com/cat-body-language-guide/
Image URL: https://images.dappier.com/example/cat-language.jpg
Summary: Learn how to interpret your cat’s posture, eyes, and tail to better understand their mood and needs.
Score: None
```

### GreenMonster Articles

```python Python theme={null}
print(
    dappier_tool.get_greenmonster_recommendations(
        query="sustainable living", similarity_top_k=1
    )
)
```

```json  theme={null}
Result 1:
Title: How to Start a Zero-Waste Lifestyle
Author: Emily Earth
Published on: Thu, 03 Apr 2025 01:25:00 +0000
Source: GreenMonster (www.greenmonster.com)
URL: https://www.greenmonster.com/zero-waste-guide/
Image URL: https://images.dappier.com/example/zero-waste.jpg
Summary: This beginner’s guide will help you transition into a sustainable, zero-waste lifestyle with simple steps.
Score: None
```

### WISH-TV News

```python Python theme={null}
print(
    dappier_tool.get_wishtv_recommendations(
        query="latest breaking news", similarity_top_k=1
    )
)
```

```json  theme={null}
Result 1:
Title: Indiana Legislature Passes Major Education Bill
Author: Mark Newsman
Published on: Thu, 03 Apr 2025 01:15:00 +0000
Source: WISH-TV (www.wishtv.com)
URL: https://www.wishtv.com/news/indiana-education-bill/
Image URL: https://images.dappier.com/example/education-bill.jpg
Summary: The new bill will allocate additional funds to public schools and implement updated curriculum standards across Indiana.
Score: None
```

### 9 and 10 News

```python Python theme={null}
print(
    dappier_tool.get_nine_and_ten_news_recommendations(
        query="northern michigan local news", similarity_top_k=1
    )
)
```

```json  theme={null}
Result 1:
Title: Cadillac Hosts Spring Festival to Kick Off the Season
Author: Lauren Local
Published on: Thu, 03 Apr 2025 01:05:00 +0000
Source: 9 & 10 News (www.9and10news.com)
URL: https://www.9and10news.com/spring-festival-cadillac/
Image URL: https://images.dappier.com/example/cadillac-festival.jpg
Summary: Northern Michigan communities gather to celebrate the start of spring with live music, food trucks, and local vendors in downtown Cadillac.
Score: None
```

### Parameters

All recommendation methods in `DappierAIRecommendationsToolSpec` support the following parameters:

#### `query` (str)

* The user query for retrieving recommendations.

#### `data_model_id` (str) *Optional*

* The data model ID to use for recommendations.
* Data model IDs always start with the prefix `"dm_"`.
* Defaults to `"dm_01j0pb465keqmatq9k83dthx34"`.

#### `similarity_top_k` (int) *Optional*

* The number of top documents to retrieve based on similarity.
* Defaults to `9`.

#### `ref` (str) *Optional*

* The site domain where AI recommendations should be displayed.
* Defaults to `None`.

#### `num_articles_ref` (int) *Optional*

* The minimum number of articles to return from the specified reference domain (`ref`).
* The remaining articles will come from other sites in the RAG model.
* Defaults to `0`.

#### `search_algorithm` (str) *Optional*

* The search algorithm to use for retrieving articles. Available options:
  * `"most_recent"` (default)
  * `"semantic"`
  * `"most_recent_semantic"`
  * `"trending"`

These parameters offer flexibility in customizing how results are retrieved and displayed, depending on the application needs.

## Conclusion

Integrating Dappier with LlamaIndex enables powerful, real-time, and context-aware capabilities for your LLM applications. Whether you're looking to pull the latest updates from the web or generate tailored content recommendations, Dappier's tools make it easy to deliver accurate and relevant results using natural language.

With just a few lines of code, you can bring trusted, live data into your AI workflows—empowering your models with factual, fresh, and focused responses.