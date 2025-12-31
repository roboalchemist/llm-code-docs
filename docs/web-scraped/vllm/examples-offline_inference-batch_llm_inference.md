# Source: https://docs.vllm.ai/en/stable/examples/offline_inference/batch_llm_inference/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/offline_inference/batch_llm_inference.md "Edit this page")

# Batch LLM Inference[¶](#batch-llm-inference "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/batch_llm_inference.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    This example shows how to use Ray Data for data parallel batch inference.

    Ray Data is a data processing framework that can process very large datasets
    with first-class support for vLLM.

    Ray Data provides functionality for:
    * Reading and writing to most popular file formats and cloud object storage.
    * Streaming execution, so you can run inference on datasets that far exceed
      the aggregate RAM of the cluster.
    * Scale up the workload without code changes.
    * Automatic sharding, load-balancing, and autoscaling across a Ray cluster,
      with built-in fault-tolerance and retry semantics.
    * Continuous batching that keeps vLLM replicas saturated and maximizes GPU
      utilization.
    * Compatible with tensor/pipeline parallel inference.

    Learn more about Ray Data's LLM integration:
    https://docs.ray.io/en/latest/data/working-with-llms.html
    """

    import ray
    from packaging.version import Version
    from ray.data.llm import build_llm_processor, vLLMEngineProcessorConfig

    assert Version(ray.__version__) >= Version("2.44.1"), (
        "Ray version must be at least 2.44.1"
    )

    # Uncomment to reduce clutter in stdout
    # ray.init(log_to_driver=False)
    # ray.data.DataContext.get_current().enable_progress_bars = False

    # Read one text file from S3. Ray Data supports reading multiple files
    # from cloud storage (such as JSONL, Parquet, CSV, binary format).
    ds = ray.data.read_text("s3://anonymous@air-example-data/prompts.txt")
    print(ds.schema())

    size = ds.count()
    print(f"Size of dataset:  prompts")

    # Configure vLLM engine.
    config = vLLMEngineProcessorConfig(
        model_source="unsloth/Llama-3.1-8B-Instruct",
        engine_kwargs=,
        concurrency=1,  # set the number of parallel vLLM replicas
        batch_size=64,
    )

    # Create a Processor object, which will be used to
    # do batch inference on the dataset
    vllm_processor = build_llm_processor(
        config,
        preprocess=lambda row: dict(
            messages=[
                ,
                ,
            ],
            sampling_params=dict(
                temperature=0.3,
                max_tokens=250,
            ),
        ),
        postprocess=lambda row: dict(
            answer=row["generated_text"],
            **row,  # This will return all the original columns in the dataset.
        ),
    )

    ds = vllm_processor(ds)

    # Peek first 10 results.
    # NOTE: This is for local testing and debugging. For production use case,
    # one should write full result out as shown below.
    outputs = ds.take(limit=10)

    for output in outputs:
        prompt = output["prompt"]
        generated_text = output["generated_text"]
        print(f"Prompt: ")
        print(f"Generated text: ")

    # Write inference output data out as Parquet files to S3.
    # Multiple files would be written to the output destination,
    # and each task would write one or more files separately.
    #
    # ds.write_parquet("s3://<your-output-bucket>")