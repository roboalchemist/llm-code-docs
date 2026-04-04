# Create a neural searcher instance
hybrid_searcher = HybridSearcher(collection_name="startups")

@app.get("/api/search")
def search_startup(q: str):
    return {"result": hybrid_searcher.search(text=q)}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

```

3. Run the service.

```bash
python service.py

```

4. Open your browser at [http://localhost:8000/docs](http://localhost:8000/docs).

You should be able to see a debug interface for your service.

![FastAPI Swagger interface](https://qdrant.tech/docs/fastapi_neural_search.png)

Feel free to play around with it, make queries regarding the companies in our corpus, and check out the results.

Join our [Discord community](https://qdrant.to/discord), where we talk about vector search and similarity learning, publish other examples of neural networks and neural search applications.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/beginner-tutorials/hybrid-search-fastembed.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/beginner-tutorials/hybrid-search-fastembed.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-40-lllmstxt|>
## hybrid-cloud-setup
- [Documentation](https://qdrant.tech/documentation/)
- [Hybrid cloud](https://qdrant.tech/documentation/hybrid-cloud/)
- Setup Hybrid Cloud