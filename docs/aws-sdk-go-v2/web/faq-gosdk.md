# Source: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/faq-gosdk.html

[](/pdfs/sdk-for-go/v2/developer-guide/aws-sdk-go-v2-dg.pdf#faq-gosdk "Open PDF")

[Documentation](/index.html)[AWS SDK for Go v2](/sdk-for-go/index.html)[Developer Guide](welcome.html)

How do I configure my SDK's HTTP client? Are there any guidelines or best practices?How should I configure operation timeouts?Requests made by the SDK are timing out or taking too long, how do I fix this?How do I fix a read: connection reset error?Why am I getting "invalid signature" errors when using an HTTP proxy with the SDK?

# Frequently Asked Questions

## How do I configure my SDK's HTTP client? Are there any guidelines or best practices?

We are unable to provide guidance to customers on how to configure their HTTP workflow in a manner that is most effective for their particular workload. The answer to this is the product of a multivariate equation, with input factors including but not limited to: 

  * the network footprint of the application (TPS, throughput, etc.) 

  * the services being used 

  * the compute characteristics of the deployment 

  * the geographical nature of the deployment 

  * the desired application behavior or needs of the application itself (SLAs, timings, etc.) 




## How should I configure operation timeouts?

Much like the previous question, it depends. Elements to consider here include the following: 

  * All of the above factors concerning HTTP client config 

  * Your own application timing or SLA constraints (e.g. if you yourself serve traffic to other consumers) 




**The answer to this question should almost NEVER be based on pure empirical observation of upstream behavior** \- e.g. "I made 1000 calls to this operation, it took at most 5 seconds so I will set the timeout based on that with a safety factor of 2x to 10 seconds". Environment conditions can change, services can temporarily degrade, and these types of assumptions can become wrong without warning. 

## Requests made by the SDK are timing out or taking too long, how do I fix this?

We are unable to assist with extended or timed-out operation calls due to extended time spent on the wire. "Wire time" in the SDK is defined as any of the following: 

  * Time spent in an SDK client's `HTTPClient.Do()` method 

  * Time spent in `Read()`s on an HTTP response body that has been forwarded to the caller (e.g. `GetObject`) 




If you are experiencing issues due to operation latency or timeouts, your first course of action should be to obtain telemetry of the SDK operation lifecycle to determine the timing breakdown between time spent on the wire and the surrounding overhead of the operation. See the guide on [timing SDK operations](./sdk-timing.html), which contains a reusable code snippet that can achieve this. 

## How do I fix a `read: connection reset` error?

The SDK retries any errors matching the `connection reset` pattern by default. This will cover error handling for most operations, where the operation's HTTP response is fully consumed and deserialized into its modeled result type. 

However, this error can still occur in a context **outside** of the retry loop: certain service operations directly forward the API's HTTP response body to the caller to be consumed from the wire directly via `io.ReadCloser` (e.g. `GetObject`'s object payload). You may encounter this error when performing a `Read` on the response body. 

This error indicates that your host, the service or any intermediary party (e.g. NAT gateways, proxies, load balancers) closed the connection while attempting to read the response. 

This can occur for several reasons: 

  * You did not consume the response body for some time after the response itself was received (after the service operation was called). **We recommend you consume the HTTP response body as soon as possible for these types of operations.**

  * You did not close a previously-received response body. This can cause connection resets on certain platforms. **You MUST close any`io.ReadCloser` instances provided in an operation's response, regardless of whether you consume its contents.**




Beyond that, try running a `tcpdump` for an affected connection at the edge of your network (e.g. after any proxies that you control). If you see that the AWS endpoint seems to be sending a TCP RST, you should use the AWS support console to open a case against the offending service. Be prepared to provide request IDs and specific timestamps of when the issue occured. 

## Why am I getting "invalid signature" errors when using an HTTP proxy with the SDK?

The signature algorithm for AWS services (generally sigv4) is tied to the serialized request's headers, more specifically most headers prefixed with `X-`. Proxies are prone to modifying the outgoing request by adding additional forwarding information (often via an `X-Forwarded-For` header) which effectively breaks the signature that the SDK calculated. 

If you're using an HTTP proxy and experiencing signature errors, you should work to capture the request **as it appears outgoing from the proxy** and determine whether it is different. 

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png) **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Middleware

Timing SDK operations

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.
