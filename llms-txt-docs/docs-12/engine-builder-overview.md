# Source: https://docs.baseten.co/development/model/performance/engine-builder-overview.md

# Engine builder overview

> Deploy optimized model inference servers in minutes

If you have a foundation model like Llama 3 or a fine-tuned variant and want to create a low-latency, high-throughput model inference server, TensorRT-LLM via the Engine Builder is likely the tool for you.

TensorRT-LLM is an open source performance optimization toolbox created by NVIDIA. It helps you build TensorRT engines for large language models like Llama and Mistral as well as certain other models like Whisper and large vision models.

Baseten's TensorRT-LLM Engine Builder simplifies and automates the process of using TensorRT-LLM for development and production. All you need to do is write a few lines of configuration and an optimized model serving engine will be built automatically during the model deployment process.

## FAQs

### Where are the engines stored?

The engines are stored in Baseten but owned by the user — we're working on a mechanism for downloading them. In the meantime, reach out if you need access to an engine that you created using the Engine Builder.

### Does the Engine Builder support quantization?

Yes. The Engine Builder can perform post-training quantization during the building process. For supported options, see [quantization in the config reference](/development/model/performance/engine-builder-config#quantization-type).

### Can I customize the engine behavior?

For further control over the TensorRT-LLM engine during inference, use the `model/model.py` file to access the engine object at runtime. See [controlling engines with Python](/development/model/performance/engine-builder-customization) for details.
