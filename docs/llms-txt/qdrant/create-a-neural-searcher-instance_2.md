# Create a neural searcher instance
neural_searcher = NeuralSearcher(collection_name="startups")

@app.get("/api/search")
def search_startup(q: str):
    return {"result": neural_searcher.search(text=q)}

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

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/neural-search/\#next-steps) Next steps

The code from this tutorial has been used to develop a [live online demo](https://qdrant.to/semantic-search-demo).
You can try it to get an intuition for cases when the neural search is useful.
The demo contains a switch that selects between neural and full-text searches.
You can turn the neural search on and off to compare your result with a regular full-text search.

> **Note**: The code for this tutorial can be found here: \| [Step 1: Data Preparation Process](https://colab.research.google.com/drive/1kPktoudAP8Tu8n8l-iVMOQhVmHkWV_L9?usp=sharing) \| [Step 2: Full Code for Neural Search](https://github.com/qdrant/qdrant_demo/tree/sentense-transformers). \|

Join our [Discord community](https://qdrant.to/discord), where we talk about vector search and similarity learning, publish other examples of neural networks and neural search applications.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/beginner-tutorials/neural-search.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/beginner-tutorials/neural-search.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-58-lllmstxt|>
## observability
- [Documentation](https://qdrant.tech/documentation/)
- Observability

## [Anchor](https://qdrant.tech/documentation/observability/\#observability-integrations) Observability Integrations

| Tool | Description |
| --- | --- |
| [OpenLIT](https://qdrant.tech/documentation/observability/openlit/) | Platform for OpenTelemetry-native Observability & Evals for LLMs and Vector Databases. |
| [OpenLLMetry](https://qdrant.tech/documentation/observability/openllmetry/) | Set of OpenTelemetry extensions to add Observability for your LLM application. |
| [Datadog](https://qdrant.tech/documentation/observability/datadog/) | Cloud-based monitoring and analytics platform. |

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/observability/_index.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/observability/_index.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-59-lllmstxt|>
## cloud-quickstart
- [Documentation](https://qdrant.tech/documentation/)
- Cloud Quickstart