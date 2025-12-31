# Source: https://docs.helicone.ai/references/latency-affect.md

# Latency Impact

> Helicone minimizes latency for your LLM applications using Cloudflare's global network. Detailed benchmarking results and performance metrics included.

Helicone leverages [Cloudflare Workers](https://developers.cloudflare.com/workers), which run code instantly across the globe on [Cloudflare's global network](https://workers.cloudflare.com/), to provide a fast and reliable proxy for your LLM requests. By utilizing this extensive network of servers, Helicone minimizes latency by ensuring that requests are handled by the servers closest to your users.

### How Cloudflare Workers Minimize Latency

Cloudflare Workers operate on a serverless architecture running on [Cloudflare's global edge network](https://developers.cloudflare.com/workers/reference/how-workers-works/). This means your requests are processed at the edge, reducing the distance data has to travel and significantly lowering latency. Workers are powered by V8 isolates, which are lightweight and have extremely fast startup times. This eliminates cold starts and ensures quick response times for your applications.

### Benchmarking Helicone's Proxy Service

To demonstrate the negligible latency introduced by Helicone's proxy, we conducted the following experiment:

* We interleaved 500 requests with unique prompts to both OpenAI and Helicone.
* Both received the same requests within the same 1-second window, varying which endpoint was called first for each request.
* We maximized the prompt context window to make these requests as large as possible.
* We used the `text-ada-001` model.
* We logged the roundtrip latency for both sets of requests.

#### Results

| Statistic          | OpenAI (s) | Helicone (s) |
| ------------------ | ---------- | ------------ |
| Mean               | 2.21       | 2.21         |
| Median             | 2.87       | 2.90         |
| Standard Deviation | 1.12       | 1.12         |
| Min                | 0.14       | 0.14         |
| Max                | 3.56       | 3.76         |
| p10                | 0.52       | 0.52         |
| p90                | 3.27       | 3.29         |

The metrics show that Helicone's latency **closely matches that of direct requests to OpenAI**. The slight differences at the right tail indicate a minimal overhead introduced by Helicone, which is negligible in most practical applications. This demonstrates that using Helicone's proxy does not significantly impact the performance of your LLM requests.

<Frame>
    <img
      src="https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/getting-started/openai-helicone.png?fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=3b111dbcf889d3a84e263f94d0736280"
      alt="Comparison of latency between OpenAI and Helicone proxies for LLM
  requests"
      data-og-width="562"
      width="562"
      data-og-height="432"
      height="432"
      data-path="images/getting-started/openai-helicone.png"
      data-optimize="true"
      data-opv="3"
      srcset="https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/getting-started/openai-helicone.png?w=280&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=5df3c97c5ff1fcb815db5f9e4330742b 280w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/getting-started/openai-helicone.png?w=560&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=4a21d2c6a3cb02905a888a0a7dcef939 560w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/getting-started/openai-helicone.png?w=840&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=63df84591ec53b2dd7839f132dd2a70a 840w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/getting-started/openai-helicone.png?w=1100&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=9201483c62337953e5dff1775db1ff90 1100w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/getting-started/openai-helicone.png?w=1650&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=044877488a358ba0854762e6e6e9f868 1650w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/getting-started/openai-helicone.png?w=2500&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=2719cc5d6132f8df500cbc59612c258f 2500w"
    />
</Frame>

# FAQ

* [Concerns about reliability?](/references/availability)

***

<Accordion title="Need more help?">
  Additional questions or feedback? Reach out to
  [help@helicone.ai](mailto:help@helicone.ai) or [schedule a
  call](https://cal.com/team/helicone/helicone-discovery) with us.
</Accordion>
