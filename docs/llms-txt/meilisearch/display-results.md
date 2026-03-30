# Display results
for result in results:
    print(result.page_content)
```

Run `search.py`. If everything is working correctly, you should see an output like this:

```
{"id": 155, "title": "The Dark Knight", "overview": "Batman raises the stakes in his war on crime. With the help of Lt. Jim Gordon and District Attorney Harvey Dent, Batman sets out to dismantle the remaining criminal organizations that plague the streets. The partnership proves to be effective, but they soon find themselves prey to a reign of chaos unleashed by a rising criminal mastermind known to the terrified citizens of Gotham as the Joker."}
{"id": 314, "title": "Catwoman", "overview": "Liquidated after discovering a corporate conspiracy, mild-mannered graphic artist Patience Phillips washes up on an island, where she's resurrected and endowed with the prowess of a cat -- and she's eager to use her new skills ... as a vigilante. Before you can say \"cat and mouse,\" handsome gumshoe Tom Lone is on her tail."}
{"id": 268, "title": "Batman", "overview": "Batman must face his most ruthless nemesis when a deformed madman calling himself \"The Joker\" seizes control of Gotham's criminal underworld."}
```

Congrats 🎉 You managed to make a similarity search using Meilisearch as a LangChain vector store.

## Going further

Using Meilisearch as a LangChain vector store allows you to load documents and search for them in different ways:

* [Import documents from text](https://python.langchain.com/docs/integrations/vectorstores/meilisearch#adding-text-and-embeddings)
* [Similarity search with score](https://python.langchain.com/docs/integrations/vectorstores/meilisearch#similarity-search-with-score)
* [Similarity search by vector](https://python.langchain.com/docs/integrations/vectorstores/meilisearch#similarity-search-by-vector)

For additional information, consult:

[Meilisearch Python SDK docs](https://python-sdk.meilisearch.com/)

Finally, should you want to use Meilisearch's vector search capabilities without LangChain or its hybrid search feature, refer to the [dedicated tutorial](/learn/ai_powered_search/getting_started_with_ai_search).