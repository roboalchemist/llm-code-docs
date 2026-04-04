# Source: https://pypi.org/project/axolotl/

Title: axolotl

URL Source: https://pypi.org/project/axolotl/

Markdown Content:
![Image 1: Axolotl](https://pypi-camo.freetls.fastly.net/ac9586b0b61b7968cd6a4395dcfe7cb23900dcb4/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f61786f6c6f746c2d61692d636c6f75642f61786f6c6f746c2f383837353133323835643938313332313432626635646232613734656235653039323837383766312f696d6167652f61786f6c6f746c5f6c6f676f5f6469676974616c5f626c61636b2e737667)

**A Free and Open Source LLM Fine-tuning Framework**

![Image 2: GitHub License](https://pypi-camo.freetls.fastly.net/6f0d2023deec93cb95b25b5283f98fb696e60af8/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f61786f6c6f746c2d61692d636c6f75642f61786f6c6f746c2e7376673f636f6c6f723d626c7565)![Image 3: tests](https://pypi-camo.freetls.fastly.net/d29ad02c3235d03c385fba18d0417479ce0319ff/68747470733a2f2f6769746875622e636f6d2f61786f6c6f746c2d61692d636c6f75642f61786f6c6f746c2f616374696f6e732f776f726b666c6f77732f74657374732e796d6c2f62616467652e737667)[![Image 4: codecov](https://pypi-camo.freetls.fastly.net/1bb8f76abf28951e16e8161ca35743b664adebbe/68747470733a2f2f636f6465636f762e696f2f67682f61786f6c6f746c2d61692d636c6f75642f61786f6c6f746c2f6272616e63682f6d61696e2f67726170682f62616467652e737667)](https://codecov.io/gh/axolotl-ai-cloud/axolotl)[![Image 5: Releases](https://pypi-camo.freetls.fastly.net/869f66bf6de93eca7001dccf3f0b7a9070479ffc/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f72656c656173652f61786f6c6f746c2d61692d636c6f75642f61786f6c6f746c2e737667)](https://github.com/axolotl-ai-cloud/axolotl/releases)

[![Image 6: contributors](https://pypi-camo.freetls.fastly.net/a2254fd931a93d39aebce030adfb6d14855859f2/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6e7472696275746f72732d616e6f6e2f61786f6c6f746c2d61692d636c6f75642f61786f6c6f746c3f636f6c6f723d79656c6c6f77267374796c653d666c61742d737175617265)](https://github.com/axolotl-ai-cloud/axolotl/graphs/contributors)![Image 7: GitHub Repo stars](https://pypi-camo.freetls.fastly.net/af51031b4d652e86af93ad935ef49fa8ae194e49/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f61786f6c6f746c2d61692d636c6f75642f61786f6c6f746c)

[![Image 8: discord](https://pypi-camo.freetls.fastly.net/82b3e12d9738e1c4c6ecd8768e216a1322193e8e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646973636f72642d3732383964612e7376673f7374796c653d666c61742d737175617265266c6f676f3d646973636f7264)](https://discord.com/invite/HhrNrHJPRb)[![Image 9: twitter](https://pypi-camo.freetls.fastly.net/399fc35ee010939d91e449456f6905cd802b582b/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f61786f6c6f746c5f61693f7374796c653d736f6369616c)](https://twitter.com/axolotl_ai)[![Image 10: Open In Colab](https://pypi-camo.freetls.fastly.net/74d996556a82b2f1dd5252d2fd8bead60f9e9d21/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/github/axolotl-ai-cloud/axolotl/blob/main/examples/colab-notebooks/colab-axolotl-example.ipynb)

![Image 11: tests-nightly](https://pypi-camo.freetls.fastly.net/951b771187e3eb09a5a2098144a01518d061c263/68747470733a2f2f6769746875622e636f6d2f61786f6c6f746c2d61692d636c6f75642f61786f6c6f746c2f616374696f6e732f776f726b666c6f77732f74657374732d6e696768746c792e796d6c2f62616467652e737667)![Image 12: multigpu-semi-weekly tests](https://pypi-camo.freetls.fastly.net/58b9781d307d59795e91d15ce8e2f6c03575d434/68747470733a2f2f6769746875622e636f6d2f61786f6c6f746c2d61692d636c6f75642f61786f6c6f746c2f616374696f6e732f776f726b666c6f77732f6d756c74692d6770752d6532652e796d6c2f62616467652e737667)

🎉 Latest Updates
-----------------

* 2026/03:
  * New model support has been added in Axolotl for [Qwen3.5, Qwen3.5 MoE](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/qwen3.5), [GLM-4.7-Flash](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/glm47-flash), [GLM-4.6V](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/glm46v), and [GLM-4.5-Air](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/glm45).
  * [MoE expert quantization](https://docs.axolotl.ai/docs/expert_quantization.html) support (via `quantize_moe_experts: true`) greatly reduces VRAM when training MoE models (FSDP2 compat).

* 2026/02:
  * [ScatterMoE LoRA](https://github.com/axolotl-ai-cloud/axolotl/pull/3410) support. LoRA fine-tuning directly on MoE expert weights using custom Triton kernels.
  * Axolotl now has support for [SageAttention](https://github.com/axolotl-ai-cloud/axolotl/pull/2823) and [GDPO](https://github.com/axolotl-ai-cloud/axolotl/pull/3353) (Generalized DPO).

* 2026/01:
  * New integration for [EAFT](https://github.com/axolotl-ai-cloud/axolotl/pull/3366) (Entropy-Aware Focal Training), weights loss by entropy of the top-k logit distribution, and [Scalable Softmax](https://github.com/axolotl-ai-cloud/axolotl/pull/3338), improves long context in attention.

* 2025/12:
  * Axolotl now includes support for [Kimi-Linear](https://docs.axolotl.ai/docs/models/kimi-linear.html), [Plano-Orchestrator](https://docs.axolotl.ai/docs/models/plano.html), [MiMo](https://docs.axolotl.ai/docs/models/mimo.html), [InternVL 3.5](https://docs.axolotl.ai/docs/models/internvl3_5.html), [Olmo3](https://docs.axolotl.ai/docs/models/olmo3.html), [Trinity](https://docs.axolotl.ai/docs/models/trinity.html), and [Ministral3](https://docs.axolotl.ai/docs/models/ministral3.html).
  * [Distributed Muon Optimizer](https://github.com/axolotl-ai-cloud/axolotl/pull/3264) support has been added for FSDP2 pretraining.

* 2025/10: New model support has been added in Axolotl for: [Qwen3 Next](https://docs.axolotl.ai/docs/models/qwen3-next.html), [Qwen2.5-vl, Qwen3-vl](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/qwen2_5-vl), [Qwen3, Qwen3MoE](https://docs.axolotl.ai/docs/models/qwen3.html), [Granite 4](https://docs.axolotl.ai/docs/models/granite4.html), [HunYuan](https://docs.axolotl.ai/docs/models/hunyuan.html), [Magistral 2509](https://docs.axolotl.ai/docs/models/magistral/vision.html), [Apertus](https://docs.axolotl.ai/docs/models/apertus.html), and [Seed-OSS](https://docs.axolotl.ai/docs/models/seed-oss.html).

Expand older updates

* 2025/09: Axolotl now has text diffusion training. Read more [here](https://github.com/axolotl-ai-cloud/axolotl/tree/main/src/axolotl/integrations/diffusion).
* 2025/08: QAT has been updated to include NVFP4 support. See [PR](https://github.com/axolotl-ai-cloud/axolotl/pull/3107).
* 2025/07:
  * ND Parallelism support has been added into Axolotl. Compose Context Parallelism (CP), Tensor Parallelism (TP), and Fully Sharded Data Parallelism (FSDP) within a single node and across multiple nodes. Check out the [blog post](https://huggingface.co/blog/accelerate-nd-parallel) for more info.
  * Axolotl adds more models: [GPT-OSS](https://docs.axolotl.ai/docs/models/gpt-oss.html), [Gemma 3n](https://docs.axolotl.ai/docs/models/gemma3n.html), [Liquid Foundation Model 2 (LFM2)](https://docs.axolotl.ai/docs/models/LiquidAI.html), and [Arcee Foundation Models (AFM)](https://docs.axolotl.ai/docs/models/arcee.html).
  * FP8 finetuning with fp8 gather op is now possible in Axolotl via `torchao`. Get started [here](https://docs.axolotl.ai/docs/mixed_precision.html#sec-fp8)!
  * [Voxtral](https://docs.axolotl.ai/docs/models/voxtral.html), [Magistral 1.1](https://docs.axolotl.ai/docs/models/magistral.html), and [Devstral](https://docs.axolotl.ai/docs/models/devstral.html) with mistral-common tokenizer support has been integrated in Axolotl!
  * TiledMLP support for single-GPU to multi-GPU training with DDP, DeepSpeed and FSDP support has been added to support Arctic Long Sequence Training. (ALST). See [examples](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/alst) for using ALST with Axolotl!

* 2025/06: Magistral with mistral-common tokenizer support has been added to Axolotl. See [docs](https://docs.axolotl.ai/docs/models/magistral.html) to start training your own Magistral models with Axolotl!
* 2025/05: Quantization Aware Training (QAT) support has been added to Axolotl. Explore the [docs](https://docs.axolotl.ai/docs/qat.html) to learn more!
* 2025/04: Llama 4 support has been added in Axolotl. See [docs](https://docs.axolotl.ai/docs/models/llama-4.html) to start training your own Llama 4 models with Axolotl's linearized version!
* 2025/03: Axolotl has implemented Sequence Parallelism (SP) support. Read the [blog](https://huggingface.co/blog/axolotl-ai-co/long-context-with-sequence-parallelism-in-axolotl) and [docs](https://docs.axolotl.ai/docs/sequence_parallelism.html) to learn how to scale your context length when fine-tuning.
* 2025/03: (Beta) Fine-tuning Multimodal models is now supported in Axolotl. Check out the [docs](https://docs.axolotl.ai/docs/multimodal.html) to fine-tune your own!
* 2025/02: Axolotl has added LoRA optimizations to reduce memory usage and improve training speed for LoRA and QLoRA in single GPU and multi-GPU training (DDP and DeepSpeed). Jump into the [docs](https://docs.axolotl.ai/docs/lora_optims.html) to give it a try.
* 2025/02: Axolotl has added GRPO support. Dive into our [blog](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm) and [GRPO example](https://github.com/axolotl-ai-cloud/grpo_code) and have some fun!
* 2025/01: Axolotl has added Reward Modelling / Process Reward Modelling fine-tuning support. See [docs](https://docs.axolotl.ai/docs/reward_modelling.html).

✨ Overview
----------

Axolotl is a free and open-source tool designed to streamline post-training and fine-tuning for the latest large language models (LLMs).

Features:

* **Multiple Model Support**: Train various models like GPT-OSS, LLaMA, Mistral, Mixtral, Pythia, and many more models available on the Hugging Face Hub.
* **Multimodal Training**: Fine-tune vision-language models (VLMs) including LLaMA-Vision, Qwen2-VL, Pixtral, LLaVA, SmolVLM2, GLM-4.6V, InternVL 3.5, Gemma 3n, and audio models like Voxtral with image, video, and audio support.
* **Training Methods**: Full fine-tuning, LoRA, QLoRA, GPTQ, QAT, Preference Tuning (DPO, IPO, KTO, ORPO), RL (GRPO, GDPO), and Reward Modelling (RM) / Process Reward Modelling (PRM).
* **Easy Configuration**: Re-use a single YAML configuration file across the full fine-tuning pipeline: dataset preprocessing, training, evaluation, quantization, and inference.
* **Performance Optimizations**: [Multipacking](https://docs.axolotl.ai/docs/multipack.html), [Flash Attention](https://github.com/Dao-AILab/flash-attention), [Xformers](https://github.com/facebookresearch/xformers), [Flex Attention](https://pytorch.org/blog/flexattention/), [SageAttention](https://github.com/thu-ml/SageAttention), [Liger Kernel](https://github.com/linkedin/Liger-Kernel), [Cut Cross Entropy](https://github.com/apple/ml-cross-entropy/tree/main), [ScatterMoE](https://docs.axolotl.ai/docs/custom_integrations.html#kernels-integration), [Sequence Parallelism (SP)](https://docs.axolotl.ai/docs/sequence_parallelism.html), [LoRA optimizations](https://docs.axolotl.ai/docs/lora_optims.html), [Multi-GPU training (FSDP1, FSDP2, DeepSpeed)](https://docs.axolotl.ai/docs/multi-gpu.html), [Multi-node training (Torchrun, Ray)](https://docs.axolotl.ai/docs/multi-node.html), and many more!
* **Flexible Dataset Handling**: Load from local, HuggingFace, and cloud (S3, Azure, GCP, OCI) datasets.
* **Cloud Ready**: We ship [Docker images](https://hub.docker.com/u/axolotlai) and also [PyPI packages](https://pypi.org/project/axolotl/) for use on cloud platforms and local hardware.

🚀 Quick Start - LLM Fine-tuning in Minutes
-------------------------------------------

**Requirements**:

* NVIDIA GPU (Ampere or newer for `bf16` and Flash Attention) or AMD GPU
* Python 3.11
* PyTorch ≥2.8.0

### Google Colab

[![Image 13: Open In Colab](https://pypi-camo.freetls.fastly.net/74d996556a82b2f1dd5252d2fd8bead60f9e9d21/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/github/axolotl-ai-cloud/axolotl/blob/main/examples/colab-notebooks/colab-axolotl-example.ipynb#scrollTo=msOCO4NRmRLa)

### Installation

#### Using pip

pip3 install -U packaging==26.0 setuptools==75.8.0 wheel ninja
pip3 install --no-build-isolation axolotl[flash-attn,deepspeed]

# Download example axolotl configs, deepspeed configs

axolotl fetch examples
axolotl fetch deepspeed_configs # OPTIONAL

#### Using Docker

Installing with Docker can be less error prone than installing in your own environment.

docker run --gpus '"all"' --rm -it axolotlai/axolotl:main-latest

Other installation approaches are described [here](https://docs.axolotl.ai/docs/installation.html).

#### Cloud Providers

* [RunPod](https://runpod.io/gsc?template=v2ickqhz9s&ref=6i7fkpdz)
* [Vast.ai](https://cloud.vast.ai/?ref_id=62897&template_id=bdd4a49fa8bce926defc99471864cace&utm_source=github&utm_medium=developer_community&utm_campaign=template_launch_axolotl&utm_content=readme)
* [PRIME Intellect](https://app.primeintellect.ai/dashboard/create-cluster?image=axolotl&location=Cheapest&security=Cheapest&show_spot=true)
* [Modal](https://www.modal.com/?utm_source=github&utm_medium=github&utm_campaign=axolotl)
* [Novita](https://novita.ai/gpus-console?templateId=311)
* [JarvisLabs.ai](https://jarvislabs.ai/templates/axolotl)
* [Latitude.sh](https://latitude.sh/blueprint/989e0e79-3bf6-41ea-a46b-1f246e309d5c)

### Your First Fine-tune

# Fetch axolotl examples

axolotl fetch examples

# Or, specify a custom path

axolotl fetch examples --dest path/to/folder

# Train a model using LoRA

axolotl train examples/llama-3/lora-1b.yml

That's it! Check out our [Getting Started Guide](https://docs.axolotl.ai/docs/getting-started.html) for a more detailed walkthrough.

📚 Documentation
----------------

* [Installation Options](https://docs.axolotl.ai/docs/installation.html) - Detailed setup instructions for different environments
* [Configuration Guide](https://docs.axolotl.ai/docs/config-reference.html) - Full configuration options and examples
* [Dataset Loading](https://docs.axolotl.ai/docs/dataset_loading.html) - Loading datasets from various sources
* [Dataset Guide](https://docs.axolotl.ai/docs/dataset-formats/) - Supported formats and how to use them
* [Multi-GPU Training](https://docs.axolotl.ai/docs/multi-gpu.html)
* [Multi-Node Training](https://docs.axolotl.ai/docs/multi-node.html)
* [Multipacking](https://docs.axolotl.ai/docs/multipack.html)
* [API Reference](https://docs.axolotl.ai/docs/api/) - Auto-generated code documentation
* [FAQ](https://docs.axolotl.ai/docs/faq.html) - Frequently asked questions

🤝 Getting Help
---------------

* Join our [Discord community](https://discord.gg/HhrNrHJPRb) for support
* Check out our [Examples](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/) directory
* Read our [Debugging Guide](https://docs.axolotl.ai/docs/debugging.html)
* Need dedicated support? Please contact [✉️wing@axolotl.ai](mailto:wing@axolotl.ai) for options

🌟 Contributing
---------------

Contributions are welcome! Please see our [Contributing Guide](https://github.com/axolotl-ai-cloud/axolotl/blob/main/.github/CONTRIBUTING.md) for details.

📈 Telemetry
------------

Axolotl has opt-out telemetry that helps us understand how the project is being used and prioritize improvements. We collect basic system information, model types, and error rates—never personal data or file paths. Telemetry is enabled by default. To disable it, set AXOLOTL_DO_NOT_TRACK=1. For more details, see our [telemetry documentation](https://docs.axolotl.ai/docs/telemetry.html).

❤️ Sponsors
-----------

Interested in sponsoring? Contact us at [wing@axolotl.ai](mailto:wing@axolotl.ai)

📝 Citing Axolotl
-----------------

If you use Axolotl in your research or projects, please cite it as follows:

@software{axolotl,
 title = {Axolotl: Open Source LLM Post-Training},
 author = {{Axolotl maintainers and contributors}},
 url = {https://github.com/axolotl-ai-cloud/axolotl},
 license = {Apache-2.0},
 year = {2023}
}

📜 License
----------

This project is licensed under the Apache 2.0 License - see the [LICENSE](https://pypi.org/project/axolotl/LICENSE) file for details.
