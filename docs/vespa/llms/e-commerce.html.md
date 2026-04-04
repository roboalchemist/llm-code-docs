# Source: https://docs.vespa.ai/en/learn/tutorials/e-commerce.html.md

# Use Case - shopping

 

The [e-commerce, or shopping, use case](https://github.com/vespa-engine/sample-apps/tree/master/use-case-shopping)is an example of an e-commerce site complete with sample data and a web front end to browse product data and reviews. To quick start the application, follow the instructions in the[README](https://github.com/vespa-engine/sample-apps/blob/master/use-case-shopping/README.md)in the sample app.

![Shopping sample app screenshot](/assets/img/shopping-1.png)

To browse the application, navigate to[localhost:8080/site](http://localhost:8080/site). This site is implemented through a custom [request handler](../../applications/request-handlers.html)and is meant to be a simple example of creating a front end / middleware that sits in front of the Vespa back end. As such it is fairly independent of Vespa features, and the code is designed to be fairly easy to follow and as non-magical as possible. All the queries against Vespa are sent as HTTP requests, and the JSON results from Vespa are parsed and rendered.

This sample application is built around the Amazon product data set found at[https://cseweb.ucsd.edu/~jmcauley/datasets.html](https://cseweb.ucsd.edu/~jmcauley/datasets.html). A small sample of this data is included in the sample application, and full data sets are available from the above site. This sample application contains scripts to convert from the data set format to Vespa format:[convert\_meta.py](https://github.com/vespa-engine/sample-apps/blob/master/use-case-shopping/convert_meta.py) and[convert\_reviews.py](https://github.com/vespa-engine/sample-apps/blob/master/use-case-shopping/convert_reviews.py). See [README](https://github.com/vespa-engine/sample-apps/tree/master/use-case-shopping#readme) for example use.

When feeding reviews, there is a custom [document processor](../../applications/document-processors.html)that intercepts document writes and updates the parent item with the review rating, so the aggregated review rating is kept stored with the item - see [ReviewProcessor](https://github.com/vespa-engine/sample-apps/blob/master/use-case-shopping/src/main/java/ai/vespa/example/shopping/ReviewProcessor.java). This is more an example of a custom document processor than a recommended way to do this, as feeding the reviews more than once will result in inflated values. To do this correctly, one should probably calculate this offline so a re-feed does not cause unexpected results.

### Highlighted features

- [Multiple document types](../../basics/schemas.html)

- [Custom document processor](../../applications/document-processors.html)

- [Custom searcher processor](../../applications/searchers.html)

- [Custom handlers](../../applications/request-handlers.html)

- [Custom configuration](../../applications/configuring-components.html)

- [Partial update](../../reference/schemas/document-json-format.html#update)

- [Search using YQL](../../querying/query-language.html)

- [Grouping](../../querying/grouping.html)

- [Rank profiles](../../basics/ranking.html)

- [Native embedders](../../rag/embedding.html)

- [Vector search](../../querying/nearest-neighbor-search)

- [Ranking functions](../../reference/schemas/schemas.html#function-rank)

 Copyright © 2026 - [Cookie Preferences](#)

