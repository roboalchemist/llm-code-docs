# Create an instance of the neural searcher
neural_searcher = NeuralSearcher(collection_name='startups')

@app.get("/api/search")
def search_startup(q: str):
    return {
        "result": neural_searcher.search(text=q)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

```

Now, if you run the service with

```bash
python service.py

```

and open your browser at [http://localhost:8000/docs](http://localhost:8000/docs) , you should be able to see a debug interface for your service.

![FastAPI Swagger interface](https://gist.githubusercontent.com/generall/c229cc94be8c15095286b0c55a3f19d7/raw/d866e37a60036ebe65508bd736faff817a5d27e9/fastapi_neural_search.png)

Feel free to play around with it, make queries and check out the results.
This concludes the tutorial.

### [Anchor](https://qdrant.tech/articles/neural-search-tutorial/\#experience-neural-search-with-qdrants-free-demo) Experience Neural Search With Qdrant’s Free Demo

Excited to see neural search in action? Take the next step and book a [free demo](https://qdrant.to/semantic-search-demo) with Qdrant! Experience firsthand how this cutting-edge technology can transform your search capabilities.

Our demo will help you grow intuition for cases when the neural search is useful. The demo contains a switch that selects between neural and full-text searches. You can turn neural search on and off to compare the result with regular full-text search.
Try to use a startup description to find similar ones.

Join our [Discord community](https://qdrant.to/discord), where we talk about vector search and similarity learning, and publish other examples of neural networks and neural search applications.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/neural-search-tutorial.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/neural-search-tutorial.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-110-lllmstxt|>
## multitenancy
- [Articles](https://qdrant.tech/articles/)
- How to Implement Multitenancy and Custom Sharding in Qdrant

[Back to Vector Search Manuals](https://qdrant.tech/articles/vector-search-manuals/)