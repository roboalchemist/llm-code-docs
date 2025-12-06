# Source: https://www.sbert.net/docs/cross_encoder/usage/efficiency.html

# Speeding up Inference[ïƒ?](#speeding-up-inference "Link to this heading")

Sentence Transformers supports 3 backends for performing inference with Cross Encoder models, each with its own optimizations for speeding up inference:

[](#pytorch)

PyTorch

The default backend for Cross Encoders. [](#onnx)

ONNX

Flexible and efficient model accelerator. [](#openvino)

OpenVINO

Optimization of models, mainly for Intel Hardware. [](#benchmarks)

Benchmarks

Benchmarks for the different backends. [](#user-interface)

User Interface

GUI to export, optimize, and quantize models.

\

## PyTorch[ïƒ?](#pytorch "Link to this heading")

The PyTorch backend is the default backend for Cross Encoders. If you donâ€™t specify a device, it will use the strongest available option across â€œcudaâ€?, â€œmpsâ€?, and â€œcpuâ€?. Its default usage looks like this:

    from sentence_transformers import CrossEncoder

    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2")

    query = "Which planet is known as the Red Planet?"
    passages = [
       "Venus is often called Earth's twin because of its similar size and proximity.",
       "Mars, known for its reddish appearance, is often referred to as the Red Planet.",
       "Jupiter, the largest planet in our solar system, has a prominent red spot.",
       "Saturn, famous for its rings, is sometimes mistaken for the Red Planet."
    ]

    scores = model.predict([(query, passage) for passage in passages])
    print(scores)

If youâ€™re using a GPU, then you can use the following options to speed up your inference:

float16 (fp16)

Float32 (fp32, full precision) is the default floating-point format in [`torch`], whereas float16 (fp16, half precision) is a reduced-precision floating-point format that can speed up inference on GPUs at a minimal loss of model accuracy. To use it, you can specify the [`torch_dtype`] during initialization or call [[`model.half()`]](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.half.html#torch.Tensor.half "(in PyTorch v2.9)") on the initialized model:

    from sentence_transformers import CrossEncoder

    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2", model_kwargs=)
    # or: model.half()

    query = "Which planet is known as the Red Planet?"
    passages = [
       "Venus is often called Earth's twin because of its similar size and proximity.",
       "Mars, known for its reddish appearance, is often referred to as the Red Planet.",
       "Jupiter, the largest planet in our solar system, has a prominent red spot.",
       "Saturn, famous for its rings, is sometimes mistaken for the Red Planet."
    ]

    scores = model.predict([(query, passage) for passage in passages])
    print(scores)

bfloat16 (bf16)

Bfloat16 (bf16) is similar to fp16, but preserves more of the original accuracy of fp32. To use it, you can specify the [`torch_dtype`] during initialization or call [[`model.bfloat16()`]](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.bfloat16.html#torch.Tensor.bfloat16 "(in PyTorch v2.9)") on the initialized model:

    from sentence_transformers import CrossEncoder

    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2", model_kwargs=)
    # or: model.bfloat16()

    query = "Which planet is known as the Red Planet?"
    passages = [
       "Venus is often called Earth's twin because of its similar size and proximity.",
       "Mars, known for its reddish appearance, is often referred to as the Red Planet.",
       "Jupiter, the largest planet in our solar system, has a prominent red spot.",
       "Saturn, famous for its rings, is sometimes mistaken for the Red Planet."
    ]

    scores = model.predict([(query, passage) for passage in passages])
    print(scores)

## ONNX[ïƒ?](#onnx "Link to this heading")

ONNX can be used to speed up inference by converting the model to ONNX format and using ONNX Runtime to run the model. To use the ONNX backend, you must install Sentence Transformers with the [`onnx`] or [`onnx-gpu`] extra for CPU or GPU acceleration, respectively:

    pip install sentence-transformers[onnx-gpu]
    # or
    pip install sentence-transformers[onnx]

To convert a model to ONNX format, you can use the following code:

    from sentence_transformers import CrossEncoder

    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2", backend="onnx")

    query = "Which planet is known as the Red Planet?"
    passages = [
       "Venus is often called Earth's twin because of its similar size and proximity.",
       "Mars, known for its reddish appearance, is often referred to as the Red Planet.",
       "Jupiter, the largest planet in our solar system, has a prominent red spot.",
       "Saturn, famous for its rings, is sometimes mistaken for the Red Planet."
    ]

    scores = model.predict([(query, passage) for passage in passages])
    print(scores)

If the model path or repository already contains a model in ONNX format, Sentence Transformers will automatically use it. Otherwise, it will convert the model to the ONNX format.

Note

If you wish to use the ONNX model outside of Sentence Transformers, you might need to apply your chosen activation function (e.g. Sigmoid) to get identical results as the Cross Encoder in Sentence Transformers.

All keyword arguments passed via [`model_kwargs`] will be passed on to [`ORTModelForSequenceClassification.from_pretrained`]. Some notable arguments include:

- [`provider`]: ONNX Runtime provider to use for loading the model, e.g. [`"CPUExecutionProvider"`] . See [https://onnxruntime.ai/docs/execution-providers/](https://onnxruntime.ai/docs/execution-providers/) for possible providers. If not specified, the strongest provider (E.g. [`"CUDAExecutionProvider"`]) will be used.

- [`file_name`]: The name of the ONNX file to load. If not specified, will default to [`"model.onnx"`] or otherwise [`"onnx/model.onnx"`]. This argument is useful for specifying optimized or quantized models.

- [`export`]: A boolean flag specifying whether the model will be exported. If not provided, [`export`] will be set to [`True`] if the model repository or directory does not already contain an ONNX model.

Tip

Itâ€™s heavily recommended to save the exported model to prevent having to re-export it every time you run your code. You can do this by calling [[`model.save_pretrained()`]](../../package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.save_pretrained "sentence_transformers.cross_encoder.CrossEncoder.save_pretrained") if your model was local:

    model = CrossEncoder("path/to/my/model", backend="onnx")
    model.save_pretrained("path/to/my/model")

or with [[`model.push_to_hub()`]](../../package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.push_to_hub "sentence_transformers.cross_encoder.CrossEncoder.push_to_hub") if your model was from the Hugging Face Hub:

    model = CrossEncoder("Alibaba-NLP/gte-reranker-modernbert-base", backend="onnx")
    model.push_to_hub("Alibaba-NLP/gte-reranker-modernbert-base", create_pr=True)

### Optimizing ONNX Models[ïƒ?](#optimizing-onnx-models "Link to this heading")

ONNX models can be optimized using [Optimum](https://huggingface.co/docs/optimum/index), allowing for speedups on CPUs and GPUs alike. To do this, you can use the [[`export_optimized_onnx_model()`]](../../package_reference/util.html#sentence_transformers.backend.export_optimized_onnx_model "sentence_transformers.backend.export_optimized_onnx_model") function, which saves the optimized in a directory or model repository that you specify. It expects:

- [`model`]: a Sentence Transformer, Sparse Encoder, or Cross Encoder model loaded with the ONNX backend.

- [`optimization_config`]: [`"O1"`], [`"O2"`], [`"O3"`], or [`"O4"`] representing optimization levels from [`AutoOptimizationConfig`], or an [`OptimizationConfig`] instance.

- [`model_name_or_path`]: a path to save the optimized model file, or the repository name if you want to push it to the Hugging Face Hub.

- [`push_to_hub`]: (Optional) a boolean to push the optimized model to the Hugging Face Hub.

- [`create_pr`]: (Optional) a boolean to create a pull request when pushing to the Hugging Face Hub. Useful when you donâ€™t have write access to the repository.

- [`file_suffix`]: (Optional) a string to append to the model name when saving it. If not specified, the optimization level name string will be used, or just [`"optimized"`] if the optimization config was not just a string optimization level.

See this example for exporting a model with [optimization level 3] (basic and extended general optimizations, transformers-specific fusions, fast Gelu approximation):

Hugging Face Hub Model

Only optimize once:

    from sentence_transformers import CrossEncoder, export_optimized_onnx_model

    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2", backend="onnx")
    export_optimized_onnx_model(
        model=model,
        optimization_config="O3",
        model_name_or_path="cross-encoder/ms-marco-MiniLM-L6-v2",
        push_to_hub=True,
        create_pr=True,
    )

Before the pull request gets merged:

    from sentence_transformers import CrossEncoder

    pull_request_nr = 2 # TODO: Update this to the number of your pull request
    model = CrossEncoder(
        "cross-encoder/ms-marco-MiniLM-L6-v2",
        backend="onnx",
        model_kwargs=,
        revision=f"refs/pr/"
    )

Once the pull request gets merged:

    from sentence_transformers import CrossEncoder

    model = CrossEncoder(
        "cross-encoder/ms-marco-MiniLM-L6-v2",
        backend="onnx",
        model_kwargs=,
    )

Local Model

Only optimize once:

    from sentence_transformers import CrossEncoder, export_optimized_onnx_model

    model = CrossEncoder("path/to/my/mpnet-legal-finetuned", backend="onnx")
    export_optimized_onnx_model(
        model=model, optimization_config="O3", model_name_or_path="path/to/my/mpnet-legal-finetuned"
    )

After optimizing:

    from sentence_transformers import CrossEncoder

    model = CrossEncoder(
        "path/to/my/mpnet-legal-finetuned",
        backend="onnx",
        model_kwargs=,
    )

### Quantizing ONNX Models[ïƒ?](#quantizing-onnx-models "Link to this heading")

ONNX models can be quantized to int8 precision using [Optimum](https://huggingface.co/docs/optimum/index), allowing for faster inference on CPUs. To do this, you can use the [[`export_dynamic_quantized_onnx_model()`]](../../package_reference/util.html#sentence_transformers.backend.export_dynamic_quantized_onnx_model "sentence_transformers.backend.export_dynamic_quantized_onnx_model") function, which saves the quantized in a directory or model repository that you specify. Dynamic quantization, unlike static quantization, does not require a calibration dataset. It expects:

- [`model`]: a Sentence Transformer, Sparse Encoder, or Cross Encoder model loaded with the ONNX backend.

- [`quantization_config`]: [`"arm64"`], [`"avx2"`], [`"avx512"`], or [`"avx512_vnni"`] representing quantization configurations from [`AutoQuantizationConfig`], or an [`QuantizationConfig`] instance.

- [`model_name_or_path`]: a path to save the quantized model file, or the repository name if you want to push it to the Hugging Face Hub.

- [`push_to_hub`]: (Optional) a boolean to push the quantized model to the Hugging Face Hub.

- [`create_pr`]: (Optional) a boolean to create a pull request when pushing to the Hugging Face Hub. Useful when you donâ€™t have write access to the repository.

- [`file_suffix`]: (Optional) a string to append to the model name when saving it. If not specified, [`"qint8_quantized"`] will be used.

On my CPU, each of the default quantization configurations ([`"arm64"`], [`"avx2"`], [`"avx512"`], [`"avx512_vnni"`]) resulted in roughly equivalent speedups.

See this example for quantizing a model to [`int8`] with [avx512_vnni]:

Hugging Face Hub Model

Only quantize once:

    from sentence_transformers import CrossEncoder, export_dynamic_quantized_onnx_model

    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2", backend="onnx")
    export_dynamic_quantized_onnx_model(
        model=model,
        quantization_config="avx512_vnni",
        model_name_or_path="sentence-transformers/cross-encoder/ms-marco-MiniLM-L6-v2",
        push_to_hub=True,
        create_pr=True,
    )

Before the pull request gets merged:

    from sentence_transformers import CrossEncoder

    pull_request_nr = 2 # TODO: Update this to the number of your pull request
    model = CrossEncoder(
        "cross-encoder/ms-marco-MiniLM-L6-v2",
        backend="onnx",
        model_kwargs=,
        revision=f"refs/pr/",
    )

Once the pull request gets merged:

    from sentence_transformers import CrossEncoder

    model = CrossEncoder(
        "cross-encoder/ms-marco-MiniLM-L6-v2",
        backend="onnx",
        model_kwargs=,
    )

Local Model

Only quantize once:

    from sentence_transformers import CrossEncoder, export_dynamic_quantized_onnx_model

    model = CrossEncoder("path/to/my/mpnet-legal-finetuned", backend="onnx")
    export_dynamic_quantized_onnx_model(
        model=model, quantization_config="avx512_vnni", model_name_or_path="path/to/my/mpnet-legal-finetuned"
    )

After quantizing:

    from sentence_transformers import CrossEncoder

    model = CrossEncoder(
        "path/to/my/mpnet-legal-finetuned",
        backend="onnx",
        model_kwargs=,
    )

## OpenVINO[ïƒ?](#openvino "Link to this heading")

OpenVINO allows for accelerated inference on CPUs by exporting the model to the OpenVINO format. To use the OpenVINO backend, you must install Sentence Transformers with the [`openvino`] extra:

    pip install sentence-transformers[openvino]

To convert a model to OpenVINO format, you can use the following code:

    from sentence_transformers import CrossEncoder

    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2", backend="openvino")

    query = "Which planet is known as the Red Planet?"
    passages = [
       "Venus is often called Earth's twin because of its similar size and proximity.",
       "Mars, known for its reddish appearance, is often referred to as the Red Planet.",
       "Jupiter, the largest planet in our solar system, has a prominent red spot.",
       "Saturn, famous for its rings, is sometimes mistaken for the Red Planet."
    ]

    scores = model.predict([(query, passage) for passage in passages])
    print(scores)

If the model path or repository already contains a model in OpenVINO format, Sentence Transformers will automatically use it. Otherwise, it will convert the model to the OpenVINO format.

Note

If you wish to use the OpenVINO model outside of Sentence Transformers, you might need to apply your chosen activation function (e.g. Sigmoid) to get identical results as the Cross Encoder in Sentence Transformers.

All keyword arguments passed via `model_kwargs` will be passed on to [`OVBaseModel.from_pretrained()`](https://huggingface.co/docs/optimum/intel/openvino/reference#optimum.intel.openvino.modeling_base.OVBaseModel.from_pretrained). Some notable arguments include:

- [`file_name`]: The name of the ONNX file to load. If not specified, will default to [`"openvino_model.xml"`] or otherwise [`"openvino/openvino_model.xml"`]. This argument is useful for specifying optimized or quantized models.

- [`export`]: A boolean flag specifying whether the model will be exported. If not provided, [`export`] will be set to [`True`] if the model repository or directory does not already contain an OpenVINO model.

Tip

Itâ€™s heavily recommended to save the exported model to prevent having to re-export it every time you run your code. You can do this by calling [[`model.save_pretrained()`]](../../package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.save_pretrained "sentence_transformers.cross_encoder.CrossEncoder.save_pretrained") if your model was local:

    model = CrossEncoder("path/to/my/model", backend="openvino")
    model.save_pretrained("path/to/my/model")

or with [[`model.push_to_hub()`]](../../package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder.push_to_hub "sentence_transformers.cross_encoder.CrossEncoder.push_to_hub") if your model was from the Hugging Face Hub:

    model = CrossEncoder("Alibaba-NLP/gte-reranker-modernbert-base", backend="openvino")
    model.push_to_hub("Alibaba-NLP/gte-reranker-modernbert-base", create_pr=True)

### Quantizing OpenVINO Models[ïƒ?](#quantizing-openvino-models "Link to this heading")

OpenVINO models can be quantized to int8 precision using [Optimum Intel](https://huggingface.co/docs/optimum/main/en/intel/index) to speed up inference. To do this, you can use the [[`export_static_quantized_openvino_model()`]](../../package_reference/util.html#sentence_transformers.backend.export_static_quantized_openvino_model "sentence_transformers.backend.export_static_quantized_openvino_model") function, which saves the quantized model in a directory or model repository that you specify. Post-Training Static Quantization expects:

- [`model`]: a Sentence Transformer, Sparse Encoder, or Cross Encoder model loaded with the OpenVINO backend.

- [`quantization_config`]: (Optional) The quantization configuration. This parameter accepts either: [`None`] for the default 8-bit quantization, a dictionary representing quantization configurations, or an [`OVQuantizationConfig`] instance.

- [`model_name_or_path`]: a path to save the quantized model file, or the repository name if you want to push it to the Hugging Face Hub.

- [`dataset_name`]: (Optional) The name of the dataset to load for calibration. If not specified, defaults to [`sst2`] subset from the [`glue`] dataset.

- [`dataset_config_name`]: (Optional) The specific configuration of the dataset to load.

- [`dataset_split`]: (Optional) The split of the dataset to load (e.g., â€˜trainâ€™, â€˜testâ€™).

- [`column_name`]: (Optional) The column name in the dataset to use for calibration.

- [`push_to_hub`]: (Optional) a boolean to push the quantized model to the Hugging Face Hub.

- [`create_pr`]: (Optional) a boolean to create a pull request when pushing to the Hugging Face Hub. Useful when you donâ€™t have write access to the repository.

- [`file_suffix`]: (Optional) a string to append to the model name when saving it. If not specified, [`"qint8_quantized"`] will be used.

See this example for quantizing a model to [`int8`] with [static quantization](https://huggingface.co/docs/optimum/main/en/intel/openvino/optimization#static-quantization):

Hugging Face Hub Model

Only quantize once:

    from sentence_transformers import CrossEncoder, export_static_quantized_openvino_model

    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L6-v2", backend="openvino")
    export_static_quantized_openvino_model(
        model=model,
        quantization_config=None,
        model_name_or_path="cross-encoder/ms-marco-MiniLM-L6-v2",
        push_to_hub=True,
        create_pr=True,
    )

Before the pull request gets merged:

    from sentence_transformers import CrossEncoder

    pull_request_nr = 2 # TODO: Update this to the number of your pull request
    model = CrossEncoder(
        "cross-encoder/ms-marco-MiniLM-L6-v2",
        backend="openvino",
        model_kwargs=,
        revision=f"refs/pr/"
    )

Once the pull request gets merged:

    from sentence_transformers import CrossEncoder

    model = CrossEncoder(
        "cross-encoder/ms-marco-MiniLM-L6-v2",
        backend="openvino",
        model_kwargs=,
    )

Local Model

Only quantize once:

    from sentence_transformers import CrossEncoder, export_static_quantized_openvino_model
    from optimum.intel import OVQuantizationConfig

    model = CrossEncoder("path/to/my/mpnet-legal-finetuned", backend="openvino")
    quantization_config = OVQuantizationConfig()
    export_static_quantized_openvino_model(
        model=model, quantization_config=quantization_config, model_name_or_path="path/to/my/mpnet-legal-finetuned"
    )

After quantizing:

    from sentence_transformers import CrossEncoder

    model = CrossEncoder(
        "path/to/my/mpnet-legal-finetuned",
        backend="openvino",
        model_kwargs=,
    )

## Benchmarks[ïƒ?](#benchmarks "Link to this heading")

The following images show the benchmark results for the different backends on GPUs and CPUs. The results are averaged across 4 models of various sizes, 3 datasets, and numerous batch sizes.

Expand the benchmark details

\
Speedup ratio:

- **Hardware:** RTX 3090 GPU, i7-17300K CPU
- **Datasets:** 2000 samples for GPU tests, 1000 samples for CPU tests.
  - [sentence-transformers/stsb](https://huggingface.co/datasets/sentence-transformers/stsb): `sentence1` and `sentence2` columns as pairs, with 38.94 Â± 13.97 and 38.96 Â± 14.05 characters on average, respectively.
  - [sentence-transformers/natural-questions](https://huggingface.co/datasets/sentence-transformers/natural-questions): `query` and `answer` columns as pairs, with 46.99 Â± 10.98 and 619.63 Â± 345.30 characters on average, respectively.
  - [stanfordnlp/imdb](https://huggingface.co/datasets/stanfordnlp/imdb): Two variants used from the `text` column: first 100 characters (100.00 Â± 0.00 characters) and each sample repeated 4 times (16804.25 Â± 10178.26 characters).
- **Models:**
  - [cross-encoder/ms-marco-MiniLM-L6-v2](https://huggingface.co/cross-encoder/ms-marco-MiniLM-L6-v2): 22.7M parameters; batch sizes of 16, 32, 64, 128 and 256.
  - [BAAI/bge-reranker-base](https://huggingface.co/BAAI/bge-reranker-base): 278M parameters; batch sizes of 16, 32, 64, and 128.
  - [mixedbread-ai/mxbai-rerank-large-v1](https://huggingface.co/mixedbread-ai/mxbai-rerank-large-v1): 435M parameters; batch sizes of 8, 16, 32, and 64. Also 128 and 256 for GPU tests.
  - [BAAI/bge-reranker-v2-m3](https://huggingface.co/BAAI/bge-reranker-v2-m3): 568M parameters; batch sizes of 2, 4. Also 8, 16, and 32 for GPU tests.

Performance ratio: The same models and hardware was used. We compare the performance against the performance of PyTorch with fp32, i.e. the default backend and precision.

- **Evaluation:**
  - **Information Retrieval:** NDCG@10 based on cosine similarity on the MS MARCO and NQ subsets from the [NanoBEIR](https://huggingface.co/collections/zeta-alpha-ai/nanobeir-66e1a0af21dfd93e620cd9f6) collection of datasets, computed via the CrossEncoderNanoBEIREvaluator.

<!-- -->

- **Backends:**
  - `torch-fp32`: PyTorch with float32 precision (default).
  - `torch-fp16`: PyTorch with float16 precision, via `model_kwargs=`.
  - `torch-bf16`: PyTorch with bfloat16 precision, via `model_kwargs=`.
  - `onnx`: ONNX with float32 precision, via `backend="onnx"`.
  - `onnx-O1`: ONNX with float32 precision and O1 optimization, via `export_optimized_onnx_model(..., optimization_config="O1", ...)` and `backend="onnx"`.
  - `onnx-O2`: ONNX with float32 precision and O2 optimization, via `export_optimized_onnx_model(..., optimization_config="O2", ...)` and `backend="onnx"`.
  - `onnx-O3`: ONNX with float32 precision and O3 optimization, via `export_optimized_onnx_model(..., optimization_config="O3", ...)` and `backend="onnx"`.
  - `onnx-O4`: ONNX with float16 precision and O4 optimization, via `export_optimized_onnx_model(..., optimization_config="O4", ...)` and `backend="onnx"`.
  - `onnx-qint8`: ONNX quantized to int8 with \"avx512_vnni\", via `export_dynamic_quantized_onnx_model(..., quantization_config="avx512_vnni", ...)` and `backend="onnx"`. The different quantization configurations resulted in roughly equivalent speedups.
  - `openvino`: OpenVINO, via `backend="openvino"`.
  - `openvino-qint8`: OpenVINO quantized to int8 via `export_static_quantized_openvino_model(..., quantization_config=OVQuantizationConfig(), ...)` and `backend="openvino"`.

Note that the aggressive averaging across models, datasets, and batch sizes prevents some more intricate patterns from being visible. For example, ONNX seems to perform stronger at low batch sizes. However, ONNX and OpenVINO can even perform slightly worse than PyTorch, so we recommend testing the different backends with your specific model and data to find the best one for your use case.

\
[![Benchmark for GPUs](../../../_images/ce_backends_benchmark_gpu.png)](../../../_images/ce_backends_benchmark_gpu.png) [![Benchmark for CPUs](../../../_images/ce_backends_benchmark_cpu.png)](../../../_images/ce_backends_benchmark_cpu.png)

### Recommendations[ïƒ?](#recommendations "Link to this heading")

Based on the benchmarks, this flowchart should help you decide which backend to use for your model:

``` mermaid

        %%
}}%%
graph TD
A("What is your hardware?") -->|GPU| B("Are you using a small<br>batch size?")
A -->|CPU| C("Are minor performance<br>degradations acceptable?")
B -->|yes| D[onnx-O4]
B -->|no| F[float16]
C -->|yes| G[openvino-qint8]
C -->|no| H("Do you have an Intel CPU?")
H -->|yes| I[openvino]
H -->|no| J[onnx]
click D "#optimizing-onnx-models"
click F "#pytorch"
click G "#quantizing-openvino-models"
click I "#openvino"
click J "#onnx"
    
```

Note

Your milage may vary, and you should always test the different backends with your specific model and data to find the best one for your use case.

### User Interface[ïƒ?](#user-interface "Link to this heading")

This Hugging Face Space provides a user interface for exporting, optimizing, and quantizing models for either ONNX or OpenVINO:

- [sentence-transformers/backend-export](https://huggingface.co/spaces/sentence-transformers/backend-export)