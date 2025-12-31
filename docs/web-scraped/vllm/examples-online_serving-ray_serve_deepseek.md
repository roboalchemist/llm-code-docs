# Source: https://docs.vllm.ai/en/stable/examples/online_serving/ray_serve_deepseek/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/ray_serve_deepseek.md "Edit this page")

# Ray Serve Deepseek[¶](#ray-serve-deepseek "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/ray_serve_deepseek.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    Deploy DeepSeek R1 or V3 with Ray Serve LLM.

    Ray Serve LLM is a scalable and production-grade model serving library built
    on the Ray distributed computing framework and first-class support for the vLLM engine.

    Key features:
    - Automatic scaling, back-pressure, and load balancing across a Ray cluster.
    - Unified multi-node multi-model deployment.
    - Exposes an OpenAI-compatible HTTP API.
    - Multi-LoRA support with shared base models.

    Run `python3 ray_serve_deepseek.py` to launch an endpoint.

    Learn more in the official Ray Serve LLM documentation:
    https://docs.ray.io/en/latest/serve/llm/serving-llms.html
    """

    from ray import serve
    from ray.serve.llm import LLMConfig, build_openai_app

    llm_config = LLMConfig(
        model_loading_config=,
        deployment_config=
        },
        # Set to the node's accelerator type.
        accelerator_type="H100",
        # Customize engine arguments as required (for example, vLLM engine kwargs).
        engine_kwargs=,
    )

    # Deploy the application.
    llm_app = build_openai_app()
    serve.run(llm_app)