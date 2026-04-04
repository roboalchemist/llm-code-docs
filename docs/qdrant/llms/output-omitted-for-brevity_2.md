# [..] output omitted for brevity
    Finished release [optimized] target(s) in 1m 27s
$ # Update the function
$ aws lambda update-function-code --function-name $LAMBDA_FUNCTION_NAME \
     --zip-file fileb://./target/lambda/page-search/bootstrap.zip \
     --region $LAMBDA_REGION

```

## [Anchor](https://qdrant.tech/articles/serverless/\#discussion) Discussion

Lambda works by spinning up your function once the URL is called, so they don’t need to keep the compute on hand unless it is actually used. This means that the first call will be burdened by some 1-2 seconds of latency for loading the function, later calls will resolve faster. Of course, there is also the latency for calling the embeddings provider and Qdrant. On the other hand, the free tier doesn’t cost a thing, so you certainly get what you pay for. And for many use cases, a result within one or two seconds is acceptable.

Rust minimizes the overhead for the function, both in terms of file size and runtime. Using an embedding service means you don’t need to care about the details. Knowing the URL, API key and embedding size is sufficient. Finally, with free tiers for both Lambda and Qdrant as well as free credits for the embedding provider, the only cost is your time to set everything up. Who could argue with free?

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/serverless.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/serverless.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-127-lllmstxt|>
## rag-chatbot-vultr-dspy-ollama
- [Documentation](https://qdrant.tech/documentation/)
- [Examples](https://qdrant.tech/documentation/examples/)
- Private RAG Information Extraction Engine