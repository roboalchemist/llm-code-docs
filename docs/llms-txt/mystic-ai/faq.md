# Source: https://docs.mystic.ai/docs/faq.md

# FAQ

Commonly asked questions

# Whats the price of your GPUs per hour?

If you're using our bring your own cloud integration ([read more here](https://www.mystic.ai/bring-your-own-cloud)) you get GPUs at the direct cost of the cloud provider or for free using your credits.

But if you're using our serverless endpoints you can find specific GPU pricing on our pricing page: [https://www.mystic.ai/pricing/serverless](https://www.mystic.ai/bring-your-own-cloud) .

# What GPUs do you support?

* A100 (40GB + 80GB)
* A100 fractions of 5GB, 10GB, & 20GB
* T4 (16GB)
* L4 (22GB)

Coming soon:

* A10
* A40
* H100 (80GB)
* H100 fractions of 10GB, 20GB, and 40GB

Find the pricing list here: <https://www.mystic.ai/pricing/serverless>

# Can I upload custom models?

Yes! Read more in [Pipeline building](https://docs.mystic.ai/docs/pipeline-building).

# I have cloud credits, can I use them with Mystic?

You can! We offer a direct cloud integration to run our stack on your cloud account, read more here: <https://www.mystic.ai/bring-your-own-cloud>.

# Do you support streaming?

We support output streaming, but not input or bidirectional streaming. Read more: [Streaming](https://docs.mystic.ai/docs/streaming).

# Do you offer versioning support?

We do. On Mystic we use a system called Pointers which are very similar to tags in Docker. On uploading a new pipeline a new pointer with a version is generated for you, and you can also create custom pointers. Read more here: [Pointers](https://docs.mystic.ai/docs/pointers-1).

# Can I integrate Mystic in my CI/CD flows?

Yes. We don't have a guide on this right now but you can use our versioning system called Pointers to swap models in and out of production in an automated way. Read more here: [Pointers](https://docs.mystic.ai/reference/pointers-2).

# Whats on your product roadmap for the next few months?

Lots of things! But the hottest features are:

* Custom accelerated docker registry written in rust to reduce cold starts
* Team/organisation support
* Bi-directional (input/output) streaming
* Push notifications
* Machine runtime statistics