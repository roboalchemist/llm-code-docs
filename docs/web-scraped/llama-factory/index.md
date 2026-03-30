# Source: https://llamafactory.readthedocs.io/

Title: LLaMA Factory

URL Source: https://llamafactory.readthedocs.io/

Markdown Content:
[View this page](https://llamafactory.readthedocs.io/zh-cn/latest/_sources/index.rst.txt "View this page")

Toggle table of contents sidebar

Welcome to LLaMA Factory![¶](https://llamafactory.readthedocs.io/#welcome-to-llama-factory "此标题的永久链接")
------------------------------------------------------------------------------------------------------

[![Image 1: logo](https://llamafactory.readthedocs.io/zh-cn/latest/_images/logo.png)](https://llamafactory.readthedocs.io/zh-cn/latest/_images/logo.png)
LLaMA Factory 是一个简单易用且高效的大型语言模型（Large Language Model）训练与微调平台。通过 LLaMA Factory，可以在无需编写任何代码的前提下，在本地完成上百种预训练模型的微调，框架特性包括：

* 模型种类：LLaMA、LLaVA、Mistral、Mixtral-MoE、Qwen、Yi、Gemma、Baichuan、ChatGLM、Phi 等等。

* 训练算法：（增量）预训练、（多模态）指令监督微调、奖励模型训练、PPO 训练、DPO 训练、KTO 训练、ORPO 训练等等。

* 运算精度：16 比特全参数微调、冻结微调、LoRA 微调和基于 AQLM/AWQ/GPTQ/LLM.int8/HQQ/EETQ 的 2/3/4/5/6/8 比特 QLoRA 微调。

* 优化算法：GaLore、BAdam、DoRA、LongLoRA、LLaMA Pro、Mixture-of-Depths、LoRA+、LoftQ 和 PiSSA。

* 加速算子：FlashAttention-2 和 Unsloth。

* 推理引擎：Transformers 和 vLLM。

* 实验监控：LlamaBoard、TensorBoard、Wandb、MLflow、SwanLab 等等。

Documentation[¶](https://llamafactory.readthedocs.io/#documentation "此标题的永久链接")
-------------------------------------------------------------------------------

高级选项

* [加速](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/acceleration.html)
  * [FlashAttention](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/acceleration.html#flashattention)
  * [Unsloth](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/acceleration.html#unsloth)
  * [Liger Kernel](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/acceleration.html#liger-kernel)

* [调优算法](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/tuning_algorithms.html)
  * [Full Parameter Fine-tuning](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/tuning_algorithms.html#full-parameter-fine-tuning)
  * [Freeze](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/tuning_algorithms.html#freeze)
  * [LoRA](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/tuning_algorithms.html#lora)
    * [LoRA+](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/tuning_algorithms.html#id5)
    * [rsLoRA](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/tuning_algorithms.html#rslora)
    * [DoRA](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/tuning_algorithms.html#dora)
    * [PiSSA](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/tuning_algorithms.html#pissa)

  * [Galore](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/tuning_algorithms.html#galore)
  * [BAdam](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/tuning_algorithms.html#badam)

* [分布训练](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/distributed.html)
  * [NativeDDP](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/distributed.html#nativeddp)
    * [单机多卡](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/distributed.html#id4)
    * [多机多卡](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/distributed.html#id7)

  * [DeepSpeed](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/distributed.html#deepspeed)
    * [单机多卡](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/distributed.html#id12)
    * [多机多卡](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/distributed.html#id16)
    * [DeepSpeed 配置文件](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/distributed.html#id20)

  * [FSDP](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/distributed.html#fsdp)
    * [单机多卡](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/distributed.html#id25)
    * [多机多卡](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/distributed.html#id29)

  * [FSDP2](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/distributed.html#fsdp2)
  * [Ray](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/distributed.html#ray)
    * [单机多卡](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/distributed.html#id33)
    * [多机多卡](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/distributed.html#id35)

* [量化](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/quantization.html)
  * [PTQ](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/quantization.html#ptq)
    * [GPTQ](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/quantization.html#gptq)

  * [QAT](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/quantization.html#qat)
    * [AWQ](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/quantization.html#awq)

  * [AQLM](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/quantization.html#aqlm)
  * [OFTQ](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/quantization.html#oftq)
    * [bitsandbytes](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/quantization.html#bitsandbytes)
    * [HQQ](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/quantization.html#hqq)
    * [EETQ](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/quantization.html#eetq)

* [训练方法](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/trainers.html)
  * [Pre-training](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/trainers.html#pre-training)
  * [Post-training](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/trainers.html#post-training)
    * [Supervised Fine-Tuning](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/trainers.html#supervised-fine-tuning)
    * [RLHF](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/trainers.html#rlhf)
    * [DPO](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/trainers.html#dpo)
    * [KTO](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/trainers.html#kto)

* [实验监控](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/monitor.html)
  * [LlamaBoard](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/monitor.html#llamaboard)
  * [SwanLab](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/monitor.html#swanlab)
  * [TensorBoard](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/monitor.html#tensorboard)
  * [Wandb](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/monitor.html#wandb)
  * [MLflow](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/monitor.html#mlflow)

* [NPU安装及配置](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_installation.html)
  * [核心依赖说明](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_installation.html#id1)
  * [方式一：手动安装环境](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_installation.html#install-form-pip)
    * [1. 版本及下载链接](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_installation.html#id3)
    * [2. 驱动及固件](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_installation.html#id4)
    * [3. CANN](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_installation.html#cann)
    * [4. torch-npu](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_installation.html#torch-npu)
    * [5. 验证安装](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_installation.html#id5)

  * [方式二：Docker 预安装镜像](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_installation.html#docker)
    * [1. 拉取镜像](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_installation.html#id6)
    * [2. 启动容器](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_installation.html#id7)
    * [3. 进入容器](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_installation.html#id8)

  * [方式三：Docker 本地构建](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_installation.html#install-form-docker)
    * [1. 使用 Docker Build 构建](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_installation.html#docker-build)
    * [2. 使用 Docker Compose 构建](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_installation.html#docker-compose)

* [NPU训练](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_training.html)
  * [支持设备](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_training.html#id1)
  * [支持功能](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_training.html#id2)
  * [快速开始](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_training.html#id3)
  * [分布式训练](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_training.html#id4)
    * [关键环境变量](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_training.html#id5)
    * [单机训练](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_training.html#id6)
    * [多机训练](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_training.html#id7)

  * [训练方式](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_training.html#id8)
    * [预训练 (PT)](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_training.html#pt)
    * [监督微调 (SFT)](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_training.html#sft)
    * [奖励模型 (RM)](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_training.html#rm)
    * [DPO 训练](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_training.html#dpo)
    * [全参数微调 (Full)](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_training.html#full)

  * [性能优化](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_training.html#id9)
    * [融合算子](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_training.html#id10)
    * [算子下发优化](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_training.html#id11)

* [NPU推理](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_inference.html)
  * [vLLM-Ascend安装](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_inference.html#vllm-ascend)
  * [LLaMA-Factory安装](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_inference.html#llama-factory)
    * [推理测试](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_inference.html#id1)

  * [可视化界面](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_inference.html#id2)
  * [性能对比](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/npu_inference.html#id3)

* [参数介绍](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html)
  * [微调参数](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#id2)
    * [基本参数](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#id3)
    * [LoRA](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#lora)
    * [RLHF](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#rlhf)
    * [Freeze](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#freeze)
    * [Apollo](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#apollo)
    * [BAdam](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#badam)
    * [GaLore](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#galore)

  * [数据参数](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#id4)
  * [模型参数](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#id5)
    * [基本参数](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#id6)
    * [多模态模型](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#id7)
    * [vllm 推理](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#vllm)
    * [模型量化](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#id8)
    * [模型导出](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#id9)

  * [评估参数](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#id10)
  * [生成参数](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#id11)
  * [SwanLab 参数](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#swanlab)
  * [训练参数](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#id12)
    * [RAY](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#ray)

  * [环境变量](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/arguments.html#id13)

* [模型支持](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/model_support.html)
  * [注册 template](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/model_support.html#template)
  * [多模态数据构建](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/model_support.html#id2)
  * [提供模型路径](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/model_support.html#id5)

* [额外选项](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/extras.html)
  * [LLaMA Pro](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/extras.html#llama-pro)

* [微调最佳实践](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/best_practice/index.html)
  * [GPT-OSS](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/best_practice/gpt-oss.html)
    * [3步实现 GPT-OSS 的 LoRA 微调](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/best_practice/gpt-oss.html#gpt-oss-lora)
