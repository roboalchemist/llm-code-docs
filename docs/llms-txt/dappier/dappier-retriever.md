# Dappier Retriever

You can also check this cookbook in colab [here](https://colab.research.google.com/drive/1hRplPRCNSfb5MUxlCz-L9Q1gjkGGYwnR?usp=sharing)

## Overview

The Dappier AI Recommendations Retriever is a custom retriever built using LangChain’s retriever interface. It enhances AI applications by providing real-time, AI-driven recommendations from premium content sources across industries like News, Finance, and Sports.

By leveraging Dappier’s pre-trained RAG models and natural language APIs, this retriever ensures that responses are not only accurate but also contextually relevant. It takes a user query as input and returns a list of LangChain Document objects with high-quality recommendations, making it a powerful tool for AI applications requiring up-to-date, content-aware insights.

## Watch the Video

If you prefer a visual walkthrough, check out the accompanying video below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/WuVT2gYnR1A?si=9W-FGqkAuVOh6os7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## Usage

```python Python theme={null}
from langchain_dappier import DappierRetriever

retriever = DappierRetriever(data_model_id="dm_01jagy9nqaeer9hxx8z1sk1jx6")

query = "latest news"

retriever.invoke(query)
```

```
[Document(metadata={'title': 'Man shot and killed on Wells Street near downtown Fort Wayne', 'author': 'Gregg Montgomery', 'source_url': 'https://www.wishtv.com/news/indiana-news/man-shot-dies-fort-wayne-december-25-2024/', 'image_url': 'https://images.dappier.com/dm_01jagy9nqaeer9hxx8z1sk1jx6/fort-wayne-police-department-vehicle-via-Flickr_.jpg?width=428&height=321', 'pubdata': 'Thu, 26 Dec 2024 01:00:33 +0000'}, page_content='A man was shot and killed on December 25, 2024, in Fort Wayne, Indiana, near West Fourth and Wells streets. Police arrived shortly after 6:30 p.m. following reports of gunfire and found the victim in the 1600 block of Wells Street, where he was pronounced dead. The area features a mix of businesses, including a daycare and restaurants.\n\nAs of the latest updates, police have not provided details on the safety of the area, potential suspects, or the motive for the shooting. Authorities are encouraging anyone with information to reach out to the Fort Wayne Police Department or Crime Stoppers.'),
Document(metadata={'title': 'House cat dies from bird flu in pet food, prompting recall', 'author': 'Associated Press', 'source_url': 'https://www.wishtv.com/news/business/house-cat-bird-flu-pet-food-recall/', 'image_url': 'https://images.dappier.com/dm_01jagy9nqaeer9hxx8z1sk1jx6/BACKGROUND-Northwest-Naturals-cat-food_.jpg?width=428&height=321', 'pubdata': 'Wed, 25 Dec 2024 23:12:41 +0000'}, page_content='An Oregon house cat has died after eating pet food contaminated with the H5N1 bird flu virus, prompting a nationwide recall of Northwest Naturals\' 2-pound Feline Turkey Recipe raw frozen pet food. The Oregon Department of Agriculture confirmed that the strictly indoor cat contracted the virus solely from the food, which has "best if used by" dates of May 21, 2026, and June 23, 2026. \n\nThe affected product was distributed across several states, including Arizona, California, and Florida, as well as British Columbia, Canada. Consumers are urged to dispose of the recalled food and seek refunds. This incident raises concerns about the spread of bird flu and its potential impact on domestic animals, particularly as California has declared a state of emergency due to the outbreak affecting various bird species.'),
Document(metadata={'title': '20 big cats die from bird flu at Washington sanctuary', 'author': 'Nic F. Anderson, CNN', 'source_url': 'https://www.wishtv.com/news/national/bird-flu-outbreak-wild-felid-center-2024/', 'image_url': 'https://images.dappier.com/dm_01jagy9nqaeer9hxx8z1sk1jx6/BACKGROUND-Amur-Bengal-tiger-at-Wild-Felid-Advocacy-Center-of-Washington-FB-post_.jpg?width=428&height=321', 'pubdata': 'Wed, 25 Dec 2024 23:04:34 +0000'}, page_content='The Wild Felid Advocacy Center in Washington state has experienced a devastating bird flu outbreak, resulting in the deaths of 20 big cats, over half of its population. The first death was reported around Thanksgiving, affecting various species, including cougars and a tiger mix. The sanctuary is currently under quarantine, closed to the public, and working with animal health officials to disinfect enclosures and implement prevention strategies.\n\nAs the situation unfolds, the Washington Department of Fish and Wildlife has noted an increase in bird flu cases statewide, including infections in cougars. While human infections from bird flu through contact with mammals are rare, the CDC acknowledges the potential risk. The sanctuary hopes to reopen in the new year, focusing on the recovery of the remaining animals and taking measures to prevent further outbreaks, marking an unprecedented challenge in its 20-year history.')]
```

### Use within a chain

Like other retrievers, DappierRetriever can be incorporated into LLM applications via [chains](https://python.langchain.com/docs/how_to/sequence/).

We will need a LLM or chat model. Let's use OpenAI as an example.

```bash  theme={null}
pip install -U langchain_core langchain-openai
export OPENAI_API_KEY="your-api-key"
```

```python Python theme={null}
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0)

prompt = ChatPromptTemplate.from_template(
    """Answer the question based only on the context provided.

Context: {context}

Question: {question}"""
)


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

chain.invoke(
    "What are the key highlights and outcomes from the latest events covered in the article?"
)
```

```json  theme={null}
"The key highlights and outcomes from the latest events covered in the article include:\n\n1. An Israeli airstrike in Gaza killed five journalists from Al-Quds Today Television, leading to condemnation from their outlet and raising concerns about violence against media professionals in the region.\n2. The Committee to Protect Journalists reported that since October 7, 2023, at least 141 journalists have been killed in the region, marking the deadliest period for journalists since 1992, with the majority being Palestinians in Gaza.\n3. A man was shot and killed in Fort Wayne, Indiana, with police not providing details on suspects, motive, or the safety of the area.\n4. An Oregon house cat died after eating pet food contaminated with the H5N1 bird flu virus, leading to a nationwide recall of Northwest Naturals' Feline Turkey Recipe raw frozen pet food and raising concerns about the spread of bird flu among domestic animals."
```

## Parameters

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

## Conclusion

Dappier's tools and retrievers empower AI models with real-time search and AI-driven content recommendations, ensuring seamless and up-to-date knowledge retrieval. For further exploration, visit our [marketplace](https://marketplace.dappier.com/marketplace).