# Source: https://docs.vllm.ai/en/stable/design/optimization_levels/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/design/optimization_levels.md "Edit this page")

# Optimization Levels[¶](#optimization-levels "Permanent link")

## Overview[¶](#overview "Permanent link")

vLLM now supports optimization levels (`-O0`, `-O1`, `-O2`, `-O3`). Optimization levels provide an intuitive mechanism for users to trade startup time for performance. Higher levels have better performance but worse startup time. These optimization levels have associated defaults to help users get desired out-of-the-box performance. Importantly, defaults set by optimization levels are purely defaults; explicit user settings will not be overwritten.

## Level Summaries and Usage Examples[¶](#level-summaries-and-usage-examples "Permanent link")

    # CLI usage
    python -m vllm.entrypoints.api_server --model RedHatAI/Llama-3.2-1B-FP8 -O0

    # Python API usage
    from vllm.entrypoints.llm import LLM

    llm = LLM(
        model="RedHatAI/Llama-3.2-1B-FP8",
        optimization_level=0
    )

#### `-O1`: Quick Optimizations[¶](#-o1-quick-optimizations "Permanent link") 

-   **Startup**: Moderate startup time
-   **Performance**: Inductor compilation, CUDAGraphMode.PIECEWISE
-   **Use case**: Balance for most development scenarios

    # CLI usage
    python -m vllm.entrypoints.api_server --model RedHatAI/Llama-3.2-1B-FP8 -O1

    # Python API usage
    from vllm.entrypoints.llm import LLM

    llm = LLM(
        model="RedHatAI/Llama-3.2-1B-FP8",
        optimization_level=1
    )

#### `-O2`: Full Optimizations (Default)[¶](#-o2-full-optimizations-default "Permanent link") 

-   **Startup**: Longer startup time
-   **Performance**: `-O1` + CUDAGraphMode.FULL_AND_PIECEWISE
-   **Use case**: Production workloads where performance is important. This is the default use case. It is also very similar to the previous default. The primary difference is that noop & fusion flags are enabled.

    # CLI usage (default, so optional)
    python -m vllm.entrypoints.api_server --model RedHatAI/Llama-3.2-1B-FP8 -O2

    # Python API usage
    from vllm.entrypoints.llm import LLM

    llm = LLM(
        model="RedHatAI/Llama-3.2-1B-FP8",
        optimization_level=2  # This is the default
    )

#### `-O3`: Full Optimization[¶](#-o3-full-optimization "Permanent link") 

Still in development. Added infrastructure to prevent changing API in future release. Currently behaves the same O2.

## Troubleshooting[¶](#troubleshooting "Permanent link")

### Common Issues[¶](#common-issues "Permanent link")

1.  **Startup Time Too Long**: Use `-O0` or `-O1` for faster startup
2.  **Compilation Errors**: Use `debug_dump_path` for additional debugging information
3.  **Performance Issues**: Ensure using `-O2` for production

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 14, 2025] ]