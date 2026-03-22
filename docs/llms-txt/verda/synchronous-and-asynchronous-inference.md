# Source: https://docs.verda.com/containers/synchronous-and-asynchronous-inference.md

# Async Inference

By default Verda services process inference requests as synchronous requests.

Enabling asynchronous inference with Verda services is done by using `Prefer` header with `X-Inference-Id` header. Our services recognize 3 values for `Prefer` header:

* `Prefer: respond-async` - use when your container is implemented to work synchronously, with Verda adding async layer for your convenience. Verda will maintain the response and the status of the request for later retrieval (for example by polling).
* `Prefer: respond-async-proxy` - fire-and-forget - assuming that your container will call a webhook or perform some other action that does not require an HTTP response.
* `Prefer: respond-async-container` - similar to above, but lets your container return a task identifier that you can use later, for example by mapping responses returned to the webhook address or output stored in the object storage (S3) bucket.

Anything else in the `Prefer` header is not recognized and is transported to the inference container as a part of the synchronous inference request.

## Fully asynchronous inference requests

By setting the `Prefer: respond-async` header you dictate that you want to execute the the inference request fully asynchronously and you want the Verda systems to maintain the status and the result of the inference.

Sending an asynchronous inference request will result in a json displaying information about the request:

```json
{
    "Id": "bi249e6b-66e6-41f1-8bcb-b26548dace0a",
    "StatusPath": "/status/name-of-your-deployment",
    "ResultPath": "/result/name-of-your-deployment"
}
```

`Id` is the identifier that is required to access the status and result. This value will be found also in the response headers as `X-Inference-Id` header.`StatusPath` is path used to acess the status of the inference request.`ResultPath` is path used to fetch the results of the inference. This value will be found also in the response headers as `Location` header.

When accessing the result or the status of your request you need to set the `X-Inference-Id` header value to the identifier you received.

## Partially asynchronous inference requests

In scenario where you have a container that itself does asynchronous workload or you don't want the Verda systems to store your result or status you can trigger a partially asynchronous flow by setting the `Prefer` header either to `respond-async-proxy` or `respond-async-container`.

These both operate so that when you send a request with these values to the `Prefer` header, the inference services will process accordingly and send `Prefer: respond-async` header to your container.

The main difference with these two is `respond-async-container` will relay your inference request to the deployed inference container and return you the response it returned. This is useful when your container produces an identifier for your asynchronous operation that you'll need later.

`respond-async-proxy` will send your inference request to queue and instantly returns you an empty response with http statuscode `202`. This is the "fire-and-forget" style approach where your don't need any information about the workload and inference container will take care of the operations themselves. For example, upload the inference result to a webhook.
