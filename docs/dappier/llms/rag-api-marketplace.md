# RAG API Marketplace
Source: https://docs.dappier.com/rag-marketplace



Supercharge your AI applications with Dappier's pre-trained, LLM ready RAG models and natural language APIs to ensure factual, up-to-date, responses from premium content providers across key verticals like News, Finance, Sports, Weather, and more.

[Dappier Marketplace](https://marketplace.dappier.com) includes all the data models that are vetted by dappier.

<img className="block" src="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/dappier_marketplace.png?fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=ffa1658117e0849dd6f8adf88c2832cb" alt="Dappier Profile" data-og-width="1648" width="1648" data-og-height="768" height="768" data-path="images/dappier_marketplace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/dappier_marketplace.png?w=280&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=e3aa6bbe57464e6616e1b6e632a72970 280w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/dappier_marketplace.png?w=560&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=c2b0009c11403170b0c5c33f0991f697 560w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/dappier_marketplace.png?w=840&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=d18958f51fc8b324d7b5d2611c559015 840w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/dappier_marketplace.png?w=1100&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=0fc2b81ee34d58f3af7a3db3e399215a 1100w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/dappier_marketplace.png?w=1650&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=e95d55df2d939166884b95aca4b3c597 1650w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/dappier_marketplace.png?w=2500&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=30735b83aff8b8e00f982003035e617a 2500w" />

## How it works

This flowchart shows how Dappier's RAG Model works. Data flows from three sources—Your Data Source, Trusted Sources, and Real-Time Data—into Dappier's RAG Model. A user query is processed by Dappier, which uses the combined data to generate trusted, vetted results. These results are then passed to an LLM, which produces the final response, ensuring reliable and accurate output for any application.

```mermaid  theme={null}
flowchart TB
    subgraph Dappier
        A2(Your Data Source) --> A5(Dappier RAG Model)
        A3(Trusted Source) --> A5
        A4(Real Time Data) --> A5
    end
    A5 -- Trusted and Real-Time Knowledge --> LLM
    LLM -- Natural Language Query --> A5
    LLM --> Response[Response]
```