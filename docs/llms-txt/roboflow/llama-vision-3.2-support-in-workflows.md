# Source: https://docs.roboflow.com/changelog/january-2025/llama-vision-3.2-support-in-workflows.md

# Llama Vision 3.2 Support in Workflows

<figure><img src="https://cdn.prod.website-files.com/5f6bc60e665f54db361e52a9/678a6c33cfea0646ec47b08b_678a6bcea3ea94a45bb74fc1_402619266-61f5b741-5963-422e-a449-187f0704ec71.png" alt=""><figcaption></figcaption></figure>

[Llama Vision 3.2](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/), a multimodal LLM developed by Meta AI, can now be used in Roboflow Workflows.

You can use the model to ask questions about the contents of images and retrieve a text response.

For example, you could use the block to:

1. Read the text in an image.
2. Ask questions about the text in an image.
3. Classify an image according to a specific prompt.

This response can then be returned by your Workflow, or processed further by other blocks (i.e. the Expression block).

[Try it in Workflows today.](https://app.roboflow.com/)

*Note: The Llama Vision 3.2 block is configured to use* [*OpenRouter*](https://openrouter.ai/) *for inference. You will need an OpenRouter API key to use the Llama Vision 3.2 block.*
