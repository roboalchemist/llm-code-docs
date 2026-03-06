# Source: https://docs.salad.com/container-engine/how-to-guides/job-processing/use-container-gateway.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Use SaladCloud's Container Gateway

> Enable Real-Time AI Inference on SaladCloud

*Last Updated: February 25, 2025*

## Main Requirements of Real-Time AI Inference

* Typical use cases include image generation, large language models (LLMs), and transcription, where inference times
  range from a few seconds to minutes, and responses must be delivered in real time to enhance a seamless user
  experience.

* Unlike traditional web applications, which typically have more consistent response times, AI inference times can be
  significantly longer and vary widely, even for the same application. For instance, inference times for LLMs are
  closely tied to the length of generated tokens.

* The ability to return partial responses (such as progress, chunks and tokens) as soon as they are ready, rather than
  making users wait for the entire response to be generated, can significantly enhance the quality of the user
  experience.

* As request volumes may fluctuate over time, inference systems should be able to scale efficiently to handle varying
  demand.

* During system congestion or failures, rejecting new requests early is a better strategy than allowing them to wait for
  extended periods, only to result in inevitable failures. Fail fast not failure-proof!

## Real-Time AI Inference with SaladCloud’s Container Gateway

Deploying SaladCloud’s Container Gateway is the fastest way to enable input/output to your applications, but additional
considerations are required to ensure their success.

**In the following diagram, all function points highlighted in green must be thoroughly reviewed, correctly configured,
and properly implemented.**

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1ucg.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=023e6640127729718a466a689246a248" data-og-width="1159" width="1159" data-og-height="541" height="541" data-path="container-engine/images/1ucg.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1ucg.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=4064785bbdfee661f9dd5f87f77db99e 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1ucg.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=1659e0a1a7ce2e475e9eafeba713a033 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1ucg.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=fa092c0749523fd0c0f7819e263109a1 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1ucg.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=4f25f209e01c939b4649b8aebbb56a97 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1ucg.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=7a84e250b2935788efdaebed8761eea6 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/1ucg.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=d0800a71c7cc1be6b7ef5a55dcd969df 2500w" />

## Key Considerations

Currently, all container instances, regardless of location, are centrally accessed through SaladCloud’s Container
Gateway in the U.S. Using the gateway for instances in other regions may introduce additional latency, typically in the
range of several hundred milliseconds. This is generally acceptable for most applications, as AI inference times are
typically much longer. **However, for latency-sensitive applications that require local access, a Redis-based queue
should be considered.**

The gateway’s Round Robin algorithm may lead to some instances being overwhelmed while others remain idle, due to the
variability in AI inference times. In most cases,
[the Least Number of Connections algorithm](/container-engine/explanation/gateway/load-balancer-options#algorithms) is
more effective, as it can better manage these disparities.

Real-time autoscaling to match GPU resources with AI system load at the minute level is not feasible. Instead, you will
need to adjust the GPU resource pool based on historical data, and slightly overprovision resources in anticipation of
spikes. Please check
[this link](/container-engine/tutorials/performance/high-performance-apps#implement-auto-scaling-at-the-quarter-hour-granularity)
for more information.

Some inference servers use a single thread, and when performing long-running inference tasks, they may fail to respond
to liveness or readiness probes, leading to node reallocation or servers not receiving further requests from the
gateway. To address this, inference servers typically require
[a robust architecture](/container-engine/tutorials/performance/high-performance-apps#select-a-robust-inference-server)
supporting multiple threads or asynchronous concurrency with batched inference].

Some implementations of liveness or readiness probes in servers simply return "OK" without accurately reflecting the
true status of the inference servers, which requires improvement to distinguish between different states, such as READY,
BUSY and FAILED.

The gateway has a
[server response timeout](/container-engine/explanation/gateway/load-balancer-options#server-response-timeout) of up to
100 seconds for all requests. Inferences, such as video generation, may exceed this time limit and result in failures.
Furthermore, sending more requests than the system can handle will cause them to queue up either in the gateway (while
configured in the single-connection mode) or on the instances, eventually resulting in timeout errors.
[To improve system robustness](/container-engine/tutorials/performance/high-performance-apps#adopt-adaptive-architectures),
inference servers can proactively reject excessive requests as a back-pressure mechanism, while client applications can
implement traffic control to stop accepting new requests from users during periods of congestion.

There is always **a delay of tens of seconds** between node failures and reallocation, when these nodes stop receiving
requests from the gateway (via the Readiness Probe), and the point at which client applications start receiving errors.
This delay may pose challenges for real-time inferences and requires optimization in the client applications.

Please review these links
([LLM](/container-engine/explanation/ai-machine-learning/llm-overview#recommendation-for-production),
[image generation](/container-engine/explanation/ai-machine-learning/image-generation-overview#container-gateway-or-job-queue))
thoroughly before building real-time applications using the Container Gateway.
