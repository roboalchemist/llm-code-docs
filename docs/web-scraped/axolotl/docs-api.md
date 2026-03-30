# Source: https://docs.axolotl.ai/docs/api/

Title: index – Axolotl

URL Source: https://docs.axolotl.ai/docs/api/

Markdown Content:
API Reference
-------------

Core
----

Core functionality for training

[train](https://docs.axolotl.ai/docs/api/train.html#axolotl.train)Prepare and train a model on a dataset. Can also infer from a model or merge lora
[evaluate](https://docs.axolotl.ai/docs/api/evaluate.html#axolotl.evaluate)Module for evaluating models.
[datasets](https://docs.axolotl.ai/docs/api/datasets.html#axolotl.datasets)Module containing dataset functionality.
[convert](https://docs.axolotl.ai/docs/api/convert.html#axolotl.convert)Module containing File Reader, File Writer, Json Parser, and Jsonl Serializer classes
[prompt_tokenizers](https://docs.axolotl.ai/docs/api/prompt_tokenizers.html#axolotl.prompt_tokenizers)Module containing PromptTokenizingStrategy and Prompter classes
[logging_config](https://docs.axolotl.ai/docs/api/logging_config.html#axolotl.logging_config)Common logging module for axolotl.
[core.builders.base](https://docs.axolotl.ai/docs/api/core.builders.base.html#axolotl.core.builders.base)Base class for trainer builder
[core.builders.causal](https://docs.axolotl.ai/docs/api/core.builders.causal.html#axolotl.core.builders.causal)Builder for causal trainers
[core.builders.rl](https://docs.axolotl.ai/docs/api/core.builders.rl.html#axolotl.core.builders.rl)Builder for RLHF trainers
[core.training_args](https://docs.axolotl.ai/docs/api/core.training_args.html#axolotl.core.training_args)extra axolotl specific training args
[core.chat.messages](https://docs.axolotl.ai/docs/api/core.chat.messages.html#axolotl.core.chat.messages)internal message representations of chat messages
[core.chat.format.chatml](https://docs.axolotl.ai/docs/api/core.chat.format.chatml.html#axolotl.core.chat.format.chatml)ChatML transformation functions for MessageContents
[core.chat.format.llama3x](https://docs.axolotl.ai/docs/api/core.chat.format.llama3x.html#axolotl.core.chat.format.llama3x)Llama 3.x chat formatting functions for MessageContents
[core.chat.format.shared](https://docs.axolotl.ai/docs/api/core.chat.format.shared.html#axolotl.core.chat.format.shared)shared functions for format transforms
[core.datasets.chat](https://docs.axolotl.ai/docs/api/core.datasets.chat.html#axolotl.core.datasets.chat)chat dataset module
[core.datasets.transforms.chat_builder](https://docs.axolotl.ai/docs/api/core.datasets.transforms.chat_builder.html#axolotl.core.datasets.transforms.chat_builder)This module contains a function that builds a transform that takes a row from the

CLI
---

Command-line interface

[cli.main](https://docs.axolotl.ai/docs/api/cli.main.html#axolotl.cli.main)Click CLI definitions for various axolotl commands.
[cli.train](https://docs.axolotl.ai/docs/api/cli.train.html#axolotl.cli.train)CLI to run training on a model.
[cli.evaluate](https://docs.axolotl.ai/docs/api/cli.evaluate.html#axolotl.cli.evaluate)CLI to run evaluation on a model.
[cli.args](https://docs.axolotl.ai/docs/api/cli.args.html#axolotl.cli.args)Module for axolotl CLI command arguments.
[cli.art](https://docs.axolotl.ai/docs/api/cli.art.html#axolotl.cli.art)Axolotl ASCII logo utils.
[cli.checks](https://docs.axolotl.ai/docs/api/cli.checks.html#axolotl.cli.checks)Various checks for Axolotl CLI.
[cli.config](https://docs.axolotl.ai/docs/api/cli.config.html#axolotl.cli.config)Configuration loading and processing.
[cli.delinearize_llama4](https://docs.axolotl.ai/docs/api/cli.delinearize_llama4.html#axolotl.cli.delinearize_llama4)CLI tool to delinearize quantized/Linearized Llama-4 models.
[cli.inference](https://docs.axolotl.ai/docs/api/cli.inference.html#axolotl.cli.inference)CLI to run inference on a trained model.
[cli.merge_lora](https://docs.axolotl.ai/docs/api/cli.merge_lora.html#axolotl.cli.merge_lora)CLI to merge a trained LoRA into a base model.
[cli.merge_sharded_fsdp_weights](https://docs.axolotl.ai/docs/api/cli.merge_sharded_fsdp_weights.html#axolotl.cli.merge_sharded_fsdp_weights)CLI to merge sharded FSDP model checkpoints into a single combined checkpoint.
[cli.preprocess](https://docs.axolotl.ai/docs/api/cli.preprocess.html#axolotl.cli.preprocess)CLI to run preprocessing of a dataset.
[cli.quantize](https://docs.axolotl.ai/docs/api/cli.quantize.html#axolotl.cli.quantize)CLI to post-training quantize a model using torchao
[cli.vllm_serve](https://docs.axolotl.ai/docs/api/cli.vllm_serve.html#axolotl.cli.vllm_serve)CLI to start the vllm server for online RL
[cli.cloud.base](https://docs.axolotl.ai/docs/api/cli.cloud.base.html#axolotl.cli.cloud.base)base class for cloud platforms from cli
[cli.cloud.modal_](https://docs.axolotl.ai/docs/api/cli.cloud.modal_.html#axolotl.cli.cloud.modal_)Modal Cloud support from CLI
[cli.utils](https://docs.axolotl.ai/docs/api/cli.utils.html#axolotl.cli.utils)Init for axolotl.cli.utils module.
[cli.utils.args](https://docs.axolotl.ai/docs/api/cli.utils.args.html#axolotl.cli.utils.args)Utilities for axolotl CLI args.
[cli.utils.fetch](https://docs.axolotl.ai/docs/api/cli.utils.fetch.html#axolotl.cli.utils.fetch)Utilities for axolotl fetch CLI command.
[cli.utils.load](https://docs.axolotl.ai/docs/api/cli.utils.load.html#axolotl.cli.utils.load)Utilities for model, tokenizer, etc. loading.
[cli.utils.sweeps](https://docs.axolotl.ai/docs/api/cli.utils.sweeps.html#axolotl.cli.utils.sweeps)Utilities for handling sweeps over configs for axolotl train CLI command
[cli.utils.train](https://docs.axolotl.ai/docs/api/cli.utils.train.html#axolotl.cli.utils.train)Utilities for axolotl train CLI command.

Trainers
--------

Training implementations

[core.trainers.base](https://docs.axolotl.ai/docs/api/core.trainers.base.html#axolotl.core.trainers.base)Module for customized trainers
[core.trainers.trl](https://docs.axolotl.ai/docs/api/core.trainers.trl.html#axolotl.core.trainers.trl)Module for TRL RL trainers
[core.trainers.mamba](https://docs.axolotl.ai/docs/api/core.trainers.mamba.html#axolotl.core.trainers.mamba)Module for mamba trainer
[core.trainers.dpo.trainer](https://docs.axolotl.ai/docs/api/core.trainers.dpo.trainer.html#axolotl.core.trainers.dpo.trainer)DPO trainer for axolotl
[core.trainers.grpo.trainer](https://docs.axolotl.ai/docs/api/core.trainers.grpo.trainer.html#axolotl.core.trainers.grpo.trainer)Axolotl GRPO trainers (with and without sequence parallelism handling)
[core.trainers.grpo.sampler](https://docs.axolotl.ai/docs/api/core.trainers.grpo.sampler.html#axolotl.core.trainers.grpo.sampler)Repeat random sampler (similar to the one implemented in
[core.trainers.utils](https://docs.axolotl.ai/docs/api/core.trainers.utils.html#axolotl.core.trainers.utils)Utils for Axolotl trainers

Model Loading
-------------

Functionality for loading and patching models, tokenizers, etc.

[loaders.model](https://docs.axolotl.ai/docs/api/loaders.model.html#axolotl.loaders.model)Model loader class implementation for loading, configuring, and patching various models.
[loaders.tokenizer](https://docs.axolotl.ai/docs/api/loaders.tokenizer.html#axolotl.loaders.tokenizer)Tokenizer loading functionality and associated utils
[loaders.processor](https://docs.axolotl.ai/docs/api/loaders.processor.html#axolotl.loaders.processor)Processor loading functionality for multi-modal models
[loaders.adapter](https://docs.axolotl.ai/docs/api/loaders.adapter.html#axolotl.loaders.adapter)Adapter loading functionality, including LoRA / QLoRA and associated utils
[loaders.patch_manager](https://docs.axolotl.ai/docs/api/loaders.patch_manager.html#axolotl.loaders.patch_manager)Patch manager class implementation to complement `axolotl.loaders.ModelLoader`.
[loaders.constants](https://docs.axolotl.ai/docs/api/loaders.constants.html#axolotl.loaders.constants)Shared constants for axolotl.loaders module

Mixins
------

Mixin classes for augmenting trainers

Context Managers
----------------

Context managers for altering trainer behaviors

Prompt Strategies
-----------------

Prompt formatting strategies

[prompt_strategies.base](https://docs.axolotl.ai/docs/api/prompt_strategies.base.html#axolotl.prompt_strategies.base)module for base dataset transform strategies
[prompt_strategies.chat_template](https://docs.axolotl.ai/docs/api/prompt_strategies.chat_template.html#axolotl.prompt_strategies.chat_template)HF Chat Templates prompt strategy
[prompt_strategies.alpaca_chat](https://docs.axolotl.ai/docs/api/prompt_strategies.alpaca_chat.html#axolotl.prompt_strategies.alpaca_chat)Module for Alpaca prompt strategy classes
[prompt_strategies.alpaca_instruct](https://docs.axolotl.ai/docs/api/prompt_strategies.alpaca_instruct.html#axolotl.prompt_strategies.alpaca_instruct)Module loading the AlpacaInstructPromptTokenizingStrategy class
[prompt_strategies.alpaca_w_system](https://docs.axolotl.ai/docs/api/prompt_strategies.alpaca_w_system.html#axolotl.prompt_strategies.alpaca_w_system)Prompt strategies loader for alpaca instruction datasets with system prompts
[prompt_strategies.user_defined](https://docs.axolotl.ai/docs/api/prompt_strategies.user_defined.html#axolotl.prompt_strategies.user_defined)User Defined prompts with configuration from the YML config
[prompt_strategies.llama2_chat](https://docs.axolotl.ai/docs/api/prompt_strategies.llama2_chat.html#axolotl.prompt_strategies.llama2_chat)Prompt Strategy for finetuning Llama2 chat models
[prompt_strategies.completion](https://docs.axolotl.ai/docs/api/prompt_strategies.completion.html#axolotl.prompt_strategies.completion)Basic completion text
[prompt_strategies.input_output](https://docs.axolotl.ai/docs/api/prompt_strategies.input_output.html#axolotl.prompt_strategies.input_output)Module for plain input/output prompt pairs
[prompt_strategies.stepwise_supervised](https://docs.axolotl.ai/docs/api/prompt_strategies.stepwise_supervised.html#axolotl.prompt_strategies.stepwise_supervised)Module for stepwise datasets, typically including a prompt and reasoning traces,
[prompt_strategies.metharme](https://docs.axolotl.ai/docs/api/prompt_strategies.metharme.html#axolotl.prompt_strategies.metharme)Module containing the MetharmenPromptTokenizingStrategy and MetharmePrompter class
[prompt_strategies.orcamini](https://docs.axolotl.ai/docs/api/prompt_strategies.orcamini.html#axolotl.prompt_strategies.orcamini)Prompt Strategy for finetuning Orca Mini (v2) models
[prompt_strategies.pygmalion](https://docs.axolotl.ai/docs/api/prompt_strategies.pygmalion.html#axolotl.prompt_strategies.pygmalion)Module containing the PygmalionPromptTokenizingStrategy and PygmalionPrompter class
[prompt_strategies.messages.chat](https://docs.axolotl.ai/docs/api/prompt_strategies.messages.chat.html#axolotl.prompt_strategies.messages.chat)Chat dataset wrapping strategy for new internal messages representations
[prompt_strategies.dpo.chat_template](https://docs.axolotl.ai/docs/api/prompt_strategies.dpo.chat_template.html#axolotl.prompt_strategies.dpo.chat_template)DPO prompt strategies for using tokenizer chat templates.
[prompt_strategies.dpo.llama3](https://docs.axolotl.ai/docs/api/prompt_strategies.dpo.llama3.html#axolotl.prompt_strategies.dpo.llama3)DPO strategies for llama-3 chat template
[prompt_strategies.dpo.chatml](https://docs.axolotl.ai/docs/api/prompt_strategies.dpo.chatml.html#axolotl.prompt_strategies.dpo.chatml)DPO strategies for chatml
[prompt_strategies.dpo.zephyr](https://docs.axolotl.ai/docs/api/prompt_strategies.dpo.zephyr.html#axolotl.prompt_strategies.dpo.zephyr)DPO strategies for zephyr
[prompt_strategies.dpo.user_defined](https://docs.axolotl.ai/docs/api/prompt_strategies.dpo.user_defined.html#axolotl.prompt_strategies.dpo.user_defined)User-defined DPO strategies
[prompt_strategies.dpo.passthrough](https://docs.axolotl.ai/docs/api/prompt_strategies.dpo.passthrough.html#axolotl.prompt_strategies.dpo.passthrough)DPO prompt strategies passthrough/zero-processing strategy
[prompt_strategies.kto.llama3](https://docs.axolotl.ai/docs/api/prompt_strategies.kto.llama3.html#axolotl.prompt_strategies.kto.llama3)KTO strategies for llama-3 chat template
[prompt_strategies.kto.chatml](https://docs.axolotl.ai/docs/api/prompt_strategies.kto.chatml.html#axolotl.prompt_strategies.kto.chatml)KTO strategies for chatml
[prompt_strategies.kto.user_defined](https://docs.axolotl.ai/docs/api/prompt_strategies.kto.user_defined.html#axolotl.prompt_strategies.kto.user_defined)User-defined KTO strategies
[prompt_strategies.orpo.chat_template](https://docs.axolotl.ai/docs/api/prompt_strategies.orpo.chat_template.html#axolotl.prompt_strategies.orpo.chat_template)chatml prompt tokenization strategy for ORPO
[prompt_strategies.bradley_terry.llama3](https://docs.axolotl.ai/docs/api/prompt_strategies.bradley_terry.llama3.html#axolotl.prompt_strategies.bradley_terry.llama3)chatml transforms for datasets with system, input, chosen, rejected to match llama3 chat template

Kernels
-------

Low-level performance optimizations

Monkey Patches
--------------

Runtime patches for model optimizations

[monkeypatch.llama_attn_hijack_flash](https://docs.axolotl.ai/docs/api/monkeypatch.llama_attn_hijack_flash.html#axolotl.monkeypatch.llama_attn_hijack_flash)Flash attention monkey patch for llama model
[monkeypatch.llama_attn_hijack_xformers](https://docs.axolotl.ai/docs/api/monkeypatch.llama_attn_hijack_xformers.html#axolotl.monkeypatch.llama_attn_hijack_xformers)Directly copied the code from https://raw.githubusercontent.com/oobabooga/text-generation-webui/main/modules/llama_attn_hijack.py and made some adjustments
[monkeypatch.mistral_attn_hijack_flash](https://docs.axolotl.ai/docs/api/monkeypatch.mistral_attn_hijack_flash.html#axolotl.monkeypatch.mistral_attn_hijack_flash)Flash attention monkey patch for mistral model
[monkeypatch.multipack](https://docs.axolotl.ai/docs/api/monkeypatch.multipack.html#axolotl.monkeypatch.multipack)multipack patching for v2 of sample packing
[monkeypatch.relora](https://docs.axolotl.ai/docs/api/monkeypatch.relora.html#axolotl.monkeypatch.relora)Implements the ReLoRA training procedure from https://arxiv.org/abs/2307.05695, minus the initial full fine-tune.
[monkeypatch.llama_expand_mask](https://docs.axolotl.ai/docs/api/monkeypatch.llama_expand_mask.html#axolotl.monkeypatch.llama_expand_mask)expands the binary attention mask per 3.2.2 of https://arxiv.org/pdf/2107.02027.pdf
[monkeypatch.lora_kernels](https://docs.axolotl.ai/docs/api/monkeypatch.lora_kernels.html#axolotl.monkeypatch.lora_kernels)Module for patching custom LoRA Triton kernels and `torch.autograd` functions.
[monkeypatch.utils](https://docs.axolotl.ai/docs/api/monkeypatch.utils.html#axolotl.monkeypatch.utils)Shared utils for the monkeypatches
[monkeypatch.btlm_attn_hijack_flash](https://docs.axolotl.ai/docs/api/monkeypatch.btlm_attn_hijack_flash.html#axolotl.monkeypatch.btlm_attn_hijack_flash)Flash attention monkey patch for cerebras btlm model
[monkeypatch.llama_patch_multipack](https://docs.axolotl.ai/docs/api/monkeypatch.llama_patch_multipack.html#axolotl.monkeypatch.llama_patch_multipack)Patched LlamaAttention to use torch.nn.functional.scaled_dot_product_attention
[monkeypatch.stablelm_attn_hijack_flash](https://docs.axolotl.ai/docs/api/monkeypatch.stablelm_attn_hijack_flash.html#axolotl.monkeypatch.stablelm_attn_hijack_flash)PyTorch StableLM Epoch model.
[monkeypatch.trainer_fsdp_optim](https://docs.axolotl.ai/docs/api/monkeypatch.trainer_fsdp_optim.html#axolotl.monkeypatch.trainer_fsdp_optim)fix for FSDP optimizer save in trainer w 4.47.0
[monkeypatch.transformers_fa_utils](https://docs.axolotl.ai/docs/api/monkeypatch.transformers_fa_utils.html#axolotl.monkeypatch.transformers_fa_utils)see https://github.com/huggingface/transformers/pull/35834
[monkeypatch.unsloth_](https://docs.axolotl.ai/docs/api/monkeypatch.unsloth_.html#axolotl.monkeypatch.unsloth_)module for patching with unsloth optimizations
[monkeypatch.data.batch_dataset_fetcher](https://docs.axolotl.ai/docs/api/monkeypatch.data.batch_dataset_fetcher.html#axolotl.monkeypatch.data.batch_dataset_fetcher)Monkey patches for the dataset fetcher to handle batches of packed indexes.
[monkeypatch.mixtral](https://docs.axolotl.ai/docs/api/monkeypatch.mixtral.html#axolotl.monkeypatch.mixtral)Patches to support multipack for mixtral
[monkeypatch.gradient_checkpointing.offload_cpu](https://docs.axolotl.ai/docs/api/monkeypatch.gradient_checkpointing.offload_cpu.html#axolotl.monkeypatch.gradient_checkpointing.offload_cpu)CPU offloaded checkpointing
[monkeypatch.gradient_checkpointing.offload_disk](https://docs.axolotl.ai/docs/api/monkeypatch.gradient_checkpointing.offload_disk.html#axolotl.monkeypatch.gradient_checkpointing.offload_disk)DISCO - DIsk-based Storage and Checkpointing with Optimized prefetching

Utils
-----

Utility functions

[utils.tokenization](https://docs.axolotl.ai/docs/api/utils.tokenization.html#axolotl.utils.tokenization)Module for tokenization utilities
[utils.chat_templates](https://docs.axolotl.ai/docs/api/utils.chat_templates.html#axolotl.utils.chat_templates)This module provides functionality for selecting chat templates based on user choices.
[utils.lora](https://docs.axolotl.ai/docs/api/utils.lora.html#axolotl.utils.lora)module to get the state dict of a merged lora model
[utils.model_shard_quant](https://docs.axolotl.ai/docs/api/utils.model_shard_quant.html#axolotl.utils.model_shard_quant)module to handle loading model on cpu/meta device for FSDP
[utils.bench](https://docs.axolotl.ai/docs/api/utils.bench.html#axolotl.utils.bench)Benchmarking and measurement utilities
[utils.freeze](https://docs.axolotl.ai/docs/api/utils.freeze.html#axolotl.utils.freeze)module to freeze/unfreeze parameters by name
[utils.trainer](https://docs.axolotl.ai/docs/api/utils.trainer.html#axolotl.utils.trainer)Module containing the Trainer class and related functions
[utils.schedulers](https://docs.axolotl.ai/docs/api/utils.schedulers.html#axolotl.utils.schedulers)Module for custom LRScheduler class
[utils.distributed](https://docs.axolotl.ai/docs/api/utils.distributed.html#axolotl.utils.distributed)Utilities for distributed functionality.
[utils.dict](https://docs.axolotl.ai/docs/api/utils.dict.html#axolotl.utils.dict)Module containing the DictDefault class
[utils.optimizers.adopt](https://docs.axolotl.ai/docs/api/utils.optimizers.adopt.html#axolotl.utils.optimizers.adopt)Copied from https://github.com/iShohei220/adopt
[utils.data.streaming](https://docs.axolotl.ai/docs/api/utils.data.streaming.html#axolotl.utils.data.streaming)Data handling specific to streaming datasets.
[utils.data.sft](https://docs.axolotl.ai/docs/api/utils.data.sft.html#axolotl.utils.data.sft)Data handling specific to SFT.
[utils.quantization](https://docs.axolotl.ai/docs/api/utils.quantization.html#axolotl.utils.quantization)Utilities for quantization including QAT and PTQ using torchao.

Schemas
-------

Pydantic data models for Axolotl config

[utils.schemas.config](https://docs.axolotl.ai/docs/api/utils.schemas.config.html#axolotl.utils.schemas.config)Module with Pydantic models for configuration.
[utils.schemas.model](https://docs.axolotl.ai/docs/api/utils.schemas.model.html#axolotl.utils.schemas.model)Pydantic models for model input / output, etc. configuration
[utils.schemas.training](https://docs.axolotl.ai/docs/api/utils.schemas.training.html#axolotl.utils.schemas.training)Pydantic models for training hyperparameters
[utils.schemas.datasets](https://docs.axolotl.ai/docs/api/utils.schemas.datasets.html#axolotl.utils.schemas.datasets)Pydantic models for datasets-related configuration
[utils.schemas.peft](https://docs.axolotl.ai/docs/api/utils.schemas.peft.html#axolotl.utils.schemas.peft)Pydantic models for PEFT-related configuration
[utils.schemas.trl](https://docs.axolotl.ai/docs/api/utils.schemas.trl.html#axolotl.utils.schemas.trl)Pydantic models for TRL trainer configuration
[utils.schemas.multimodal](https://docs.axolotl.ai/docs/api/utils.schemas.multimodal.html#axolotl.utils.schemas.multimodal)Pydantic models for multimodal-related configuration
[utils.schemas.integrations](https://docs.axolotl.ai/docs/api/utils.schemas.integrations.html#axolotl.utils.schemas.integrations)Pydantic models for Axolotl integrations
[utils.schemas.enums](https://docs.axolotl.ai/docs/api/utils.schemas.enums.html#axolotl.utils.schemas.enums)Enums for Axolotl input config
[utils.schemas.utils](https://docs.axolotl.ai/docs/api/utils.schemas.utils.html#axolotl.utils.schemas.utils)Utilities for Axolotl Pydantic models

Integrations
------------

Third-party integrations and extensions

[integrations.base](https://docs.axolotl.ai/docs/api/integrations.base.html#axolotl.integrations.base)Base class for all plugins.
[integrations.cut_cross_entropy.args](https://docs.axolotl.ai/docs/api/integrations.cut_cross_entropy.args.html#axolotl.integrations.cut_cross_entropy.args)Module for handling Cut Cross Entropy input arguments.
[integrations.grokfast.optimizer](https://docs.axolotl.ai/docs/api/integrations.grokfast.optimizer.html#axolotl.integrations.grokfast.optimizer)
[integrations.kd.trainer](https://docs.axolotl.ai/docs/api/integrations.kd.trainer.html#axolotl.integrations.kd.trainer)KD trainer
[integrations.liger.args](https://docs.axolotl.ai/docs/api/integrations.liger.args.html#axolotl.integrations.liger.args)Module for handling LIGER input arguments.
[integrations.lm_eval.args](https://docs.axolotl.ai/docs/api/integrations.lm_eval.args.html#axolotl.integrations.lm_eval.args)Module for handling lm eval harness input arguments.
[integrations.spectrum.args](https://docs.axolotl.ai/docs/api/integrations.spectrum.args.html#axolotl.integrations.spectrum.args)Module for handling Spectrum input arguments.

Common
------

Common utilities and shared functionality

Models
------

Custom model implementations

Data Processing
---------------

Data processing utilities

Callbacks
---------

Training callbacks

[utils.callbacks.perplexity](https://docs.axolotl.ai/docs/api/utils.callbacks.perplexity.html#axolotl.utils.callbacks.perplexity)callback to calculate perplexity as an evaluation metric.
[utils.callbacks.profiler](https://docs.axolotl.ai/docs/api/utils.callbacks.profiler.html#axolotl.utils.callbacks.profiler)HF Trainer callback for creating pytorch profiling snapshots
[utils.callbacks.lisa](https://docs.axolotl.ai/docs/api/utils.callbacks.lisa.html#axolotl.utils.callbacks.lisa)module for LISA
[utils.callbacks.mlflow_](https://docs.axolotl.ai/docs/api/utils.callbacks.mlflow_.html#axolotl.utils.callbacks.mlflow_)MLFlow module for trainer callbacks
[utils.callbacks.comet_](https://docs.axolotl.ai/docs/api/utils.callbacks.comet_.html#axolotl.utils.callbacks.comet_)Comet module for trainer callbacks
[utils.callbacks.qat](https://docs.axolotl.ai/docs/api/utils.callbacks.qat.html#axolotl.utils.callbacks.qat)QAT Callback for HF Causal Trainer
