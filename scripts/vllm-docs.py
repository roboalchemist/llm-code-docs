#!/usr/bin/env python3
"""
vLLM Documentation Scraper
Downloads all vLLM documentation pages and converts to markdown.
vLLM is a high-throughput and memory-efficient inference and serving engine for LLMs.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import re
import subprocess

# vLLM documentation pages from sitemap (excluding API reference)
VLLM_DOC_PAGES = [
    "/",
    "/api/",
    "/benchmarking/",
    "/benchmarking/cli/",
    "/benchmarking/dashboard/",
    "/benchmarking/sweeps/",
    "/cli/",
    "/cli/bench/latency/",
    "/cli/bench/serve/",
    "/cli/bench/sweep/plot/",
    "/cli/bench/sweep/plot_pareto/",
    "/cli/bench/sweep/serve/",
    "/cli/bench/sweep/serve_sla/",
    "/cli/bench/throughput/",
    "/cli/chat/",
    "/cli/complete/",
    "/cli/run-batch/",
    "/cli/serve/",
    "/community/contact_us/",
    "/community/meetups/",
    "/community/sponsors/",
    "/configuration/",
    "/configuration/conserving_memory/",
    "/configuration/engine_args/",
    "/configuration/env_vars/",
    "/configuration/model_resolution/",
    "/configuration/optimization/",
    "/configuration/serve_args/",
    "/contributing/",
    "/contributing/ci/failures/",
    "/contributing/ci/nightly_builds/",
    "/contributing/ci/update_pytorch_version/",
    "/contributing/deprecation_policy/",
    "/contributing/dockerfile/dockerfile/",
    "/contributing/incremental_build/",
    "/contributing/model/",
    "/contributing/model/basic/",
    "/contributing/model/multimodal/",
    "/contributing/model/registration/",
    "/contributing/model/tests/",
    "/contributing/model/transcription/",
    "/contributing/profiling/",
    "/contributing/vulnerability_management/",
    "/deployment/docker/",
    "/deployment/frameworks/anyscale/",
    "/deployment/frameworks/anything-llm/",
    "/deployment/frameworks/autogen/",
    "/deployment/frameworks/bentoml/",
    "/deployment/frameworks/cerebrium/",
    "/deployment/frameworks/chatbox/",
    "/deployment/frameworks/dify/",
    "/deployment/frameworks/dstack/",
    "/deployment/frameworks/haystack/",
    "/deployment/frameworks/helm/",
    "/deployment/frameworks/hf_inference_endpoints/",
    "/deployment/frameworks/litellm/",
    "/deployment/frameworks/lobe-chat/",
    "/deployment/frameworks/lws/",
    "/deployment/frameworks/modal/",
    "/deployment/frameworks/open-webui/",
    "/deployment/frameworks/retrieval_augmented_generation/",
    "/deployment/frameworks/skypilot/",
    "/deployment/frameworks/streamlit/",
    "/deployment/frameworks/triton/",
    "/deployment/integrations/kaito/",
    "/deployment/integrations/kserve/",
    "/deployment/integrations/kthena/",
    "/deployment/integrations/kubeai/",
    "/deployment/integrations/kuberay/",
    "/deployment/integrations/llamastack/",
    "/deployment/integrations/llmaz/",
    "/deployment/integrations/production-stack/",
    "/deployment/k8s/",
    "/deployment/nginx/",
    "/design/arch_overview/",
    "/design/cuda_graphs/",
    "/design/dbo/",
    "/design/debug_vllm_compile/",
    "/design/fused_moe_modular_kernel/",
    "/design/huggingface_integration/",
    "/design/hybrid_kv_cache_manager/",
    "/design/io_processor_plugins/",
    "/design/logits_processors/",
    "/design/lora_resolver_plugins/",
    "/design/metrics/",
    "/design/mm_processing/",
    "/design/moe_kernel_features/",
    "/design/multiprocessing/",
    "/design/optimization_levels/",
    "/design/p2p_nccl_connector/",
    "/design/paged_attention/",
    "/design/plugin_system/",
    "/design/prefix_caching/",
    "/design/torch_compile/",
    "/examples/",
    "/examples/offline_inference/async_llm_streaming/",
    "/examples/offline_inference/audio_language/",
    "/examples/offline_inference/automatic_prefix_caching/",
    "/examples/offline_inference/basic/",
    "/examples/offline_inference/batch_llm_inference/",
    "/examples/offline_inference/chat_with_tools/",
    "/examples/offline_inference/context_extension/",
    "/examples/offline_inference/data_parallel/",
    "/examples/offline_inference/disaggregated_prefill/",
    "/examples/offline_inference/disaggregated-prefill-v1/",
    "/examples/offline_inference/encoder_decoder_multimodal/",
    "/examples/offline_inference/kv_load_failure_recovery/",
    "/examples/offline_inference/llm_engine_example/",
    "/examples/offline_inference/llm_engine_reset_kv/",
    "/examples/offline_inference/load_sharded_state/",
    "/examples/offline_inference/logits_processor/",
    "/examples/offline_inference/lora_with_quantization_inference/",
    "/examples/offline_inference/metrics/",
    "/examples/offline_inference/mistral-small/",
    "/examples/offline_inference/mlpspeculator/",
    "/examples/offline_inference/multilora_inference/",
    "/examples/offline_inference/openai_batch/",
    "/examples/offline_inference/prefix_caching/",
    "/examples/offline_inference/prompt_embed_inference/",
    "/examples/offline_inference/qwen_1m/",
    "/examples/offline_inference/qwen2_5_omni/",
    "/examples/offline_inference/qwen3_omni/",
    "/examples/offline_inference/reproducibility/",
    "/examples/offline_inference/rlhf/",
    "/examples/offline_inference/rlhf_colocate/",
    "/examples/offline_inference/rlhf_online_quant/",
    "/examples/offline_inference/rlhf_utils/",
    "/examples/offline_inference/save_sharded_state/",
    "/examples/offline_inference/simple_profiling/",
    "/examples/offline_inference/skip_loading_weights_in_engine_init/",
    "/examples/offline_inference/spec_decode/",
    "/examples/offline_inference/structured_outputs/",
    "/examples/offline_inference/torchrun_dp_example/",
    "/examples/offline_inference/torchrun_example/",
    "/examples/offline_inference/vision_language/",
    "/examples/offline_inference/vision_language_multi_image/",
    "/examples/online_serving/api_client/",
    "/examples/online_serving/chart-helm/",
    "/examples/online_serving/dashboards/",
    "/examples/online_serving/disaggregated_encoder/",
    "/examples/online_serving/disaggregated_prefill/",
    "/examples/online_serving/disaggregated_serving/",
    "/examples/online_serving/disaggregated_serving_p2p_nccl_xpyd/",
    "/examples/online_serving/elastic_ep/",
    "/examples/online_serving/gradio_openai_chatbot_webserver/",
    "/examples/online_serving/gradio_webserver/",
    "/examples/online_serving/kv_events_subscriber/",
    "/examples/online_serving/multi_instance_data_parallel/",
    "/examples/online_serving/multi-node-serving/",
    "/examples/online_serving/openai_chat_completion_client/",
    "/examples/online_serving/openai_chat_completion_client_for_multimodal/",
    "/examples/online_serving/openai_chat_completion_client_with_tools/",
    "/examples/online_serving/openai_chat_completion_client_with_tools_required/",
    "/examples/online_serving/openai_chat_completion_client_with_tools_xlam/",
    "/examples/online_serving/openai_chat_completion_client_with_tools_xlam_streaming/",
    "/examples/online_serving/openai_chat_completion_tool_calls_with_reasoning/",
    "/examples/online_serving/openai_chat_completion_with_reasoning/",
    "/examples/online_serving/openai_chat_completion_with_reasoning_streaming/",
    "/examples/online_serving/openai_completion_client/",
    "/examples/online_serving/openai_responses_client/",
    "/examples/online_serving/openai_responses_client_with_mcp_tools/",
    "/examples/online_serving/openai_responses_client_with_tools/",
    "/examples/online_serving/openai_transcription_client/",
    "/examples/online_serving/openai_translation_client/",
    "/examples/online_serving/opentelemetry/",
    "/examples/online_serving/prometheus_grafana/",
    "/examples/online_serving/prompt_embed_inference_with_openai_client/",
    "/examples/online_serving/ray_serve_deepseek/",
    "/examples/online_serving/retrieval_augmented_generation_with_langchain/",
    "/examples/online_serving/retrieval_augmented_generation_with_llamaindex/",
    "/examples/online_serving/run_cluster/",
    "/examples/online_serving/sagemaker-entrypoint/",
    "/examples/online_serving/streamlit_openai_chatbot_webserver/",
    "/examples/online_serving/structured_outputs/",
    "/examples/online_serving/token_generation_client/",
    "/examples/online_serving/utils/",
    "/examples/others/lmcache/",
    "/examples/others/logging_configuration/",
    "/examples/others/tensorize_vllm_model/",
    "/examples/pooling/classify/",
    "/examples/pooling/embed/",
    "/examples/pooling/plugin/",
    "/examples/pooling/pooling/",
    "/examples/pooling/score/",
    "/examples/pooling/token_classify/",
    "/examples/pooling/token_embed/",
    "/features/",
    "/features/automatic_prefix_caching/",
    "/features/batch_invariance/",
    "/features/custom_arguments/",
    "/features/custom_logitsprocs/",
    "/features/disagg_encoder/",
    "/features/disagg_prefill/",
    "/features/interleaved_thinking/",
    "/features/lora/",
    "/features/mooncake_connector_usage/",
    "/features/multimodal_inputs/",
    "/features/nixl_connector_usage/",
    "/features/prompt_embeds/",
    "/features/quantization/",
    "/features/quantization/auto_awq/",
    "/features/quantization/auto_round/",
    "/features/quantization/bitblas/",
    "/features/quantization/bnb/",
    "/features/quantization/fp8/",
    "/features/quantization/gguf/",
    "/features/quantization/gptqmodel/",
    "/features/quantization/inc/",
    "/features/quantization/int4/",
    "/features/quantization/int8/",
    "/features/quantization/modelopt/",
    "/features/quantization/quantized_kvcache/",
    "/features/quantization/quark/",
    "/features/quantization/torchao/",
    "/features/reasoning_outputs/",
    "/features/sleep_mode/",
    "/features/spec_decode/",
    "/features/structured_outputs/",
    "/features/tool_calling/",
    "/generated/metrics/general/",
    "/generated/metrics/nixl_connector/",
    "/generated/metrics/spec_decode/",
    "/getting_started/installation/",
    "/getting_started/installation/cpu/",
    "/getting_started/installation/gpu/",
    "/getting_started/quickstart/",
    "/governance/collaboration/",
    "/governance/committers/",
    "/governance/process/",
    "/models/extensions/fastsafetensor/",
    "/models/extensions/runai_model_streamer/",
    "/models/extensions/tensorizer/",
    "/models/generative_models/",
    "/models/hardware_supported_models/cpu/",
    "/models/hardware_supported_models/xpu/",
    "/models/pooling_models/",
    "/models/supported_models/",
    "/serving/context_parallel_deployment/",
    "/serving/data_parallel_deployment/",
    "/serving/distributed_troubleshooting/",
    "/serving/expert_parallel_deployment/",
    "/serving/integrations/langchain/",
    "/serving/integrations/llamaindex/",
    "/serving/offline_inference/",
    "/serving/openai_compatible_server/",
    "/serving/parallelism_scaling/",
    "/training/rlhf/",
    "/training/trl/",
    "/usage/",
    "/usage/faq/",
    "/usage/metrics/",
    "/usage/reproducibility/",
    "/usage/security/",
    "/usage/troubleshooting/",
    "/usage/usage_stats/",
    "/usage/v1_guide/",
]

BASE_URL = "https://docs.vllm.ai/en/stable"


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # MkDocs Material uses <article class="md-content__inner md-typeset">
    article_match = re.search(
        r'<article[^>]*class="[^"]*md-content__inner[^"]*"[^>]*>(.*?)</article>',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    if article_match:
        html_content = article_match.group(1)
    else:
        # Try alternate selector
        main_match = re.search(
            r'<div[^>]*class="[^"]*md-content[^"]*"[^>]*>(.*?)</div>\s*<script',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )
        if main_match:
            html_content = main_match.group(1)

    # Remove tabbed content duplicates (MkDocs shows same content in tabs)
    html_content = re.sub(r'<div[^>]*class="[^"]*tabbed-block[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL)

    # Try pandoc on cleaned content
    try:
        result = subprocess.run(
            ['pandoc', '-f', 'html', '-t', 'markdown', '--wrap=none'],
            input=html_content,
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            markdown = result.stdout
            # Clean up pandoc artifacts
            markdown = re.sub(r'^::+.*$', '', markdown, flags=re.MULTILINE)  # Remove ::: div markers
            markdown = re.sub(r'\{[^}]*\}', '', markdown)  # Remove {.class} attributes
            markdown = re.sub(r'\n{3,}', '\n\n', markdown)  # Normalize whitespace
            markdown = markdown.strip()
            return f"# Source: {url}\n\n{markdown}"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: basic HTML to text extraction
    # Remove script and style elements
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<header[^>]*>.*?</header>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Extract main content (MkDocs Material uses md-content class)
    main_match = re.search(r'<article[^>]*class="[^"]*md-content[^"]*"[^>]*>(.*?)</article>', html_content, flags=re.DOTALL | re.IGNORECASE)
    if main_match:
        html_content = main_match.group(1)

    # Convert common HTML elements to markdown
    # Headers
    for i in range(6, 0, -1):
        html_content = re.sub(rf'<h{i}[^>]*>(.*?)</h{i}>', r'\n' + '#' * i + r' \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Code blocks
    html_content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'\n```\n\1\n```\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Links
    html_content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Bold and italic
    html_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Lists
    html_content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<[ou]l[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</[ou]l>', '\n', html_content, flags=re.IGNORECASE)

    # Paragraphs and line breaks
    html_content = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<br\s*/?>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<div[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</div>', '\n', html_content, flags=re.IGNORECASE)

    # Remove remaining HTML tags
    html_content = re.sub(r'<[^>]+>', '', html_content)

    # Decode HTML entities
    html_content = html_content.replace('&nbsp;', ' ')
    html_content = html_content.replace('&lt;', '<')
    html_content = html_content.replace('&gt;', '>')
    html_content = html_content.replace('&amp;', '&')
    html_content = html_content.replace('&quot;', '"')
    html_content = html_content.replace('&#39;', "'")

    # Clean up whitespace
    html_content = re.sub(r'\n\s*\n\s*\n', '\n\n', html_content)
    html_content = html_content.strip()

    return f"# Source: {url}\n\n{html_content}"


def download_page(url, output_path):
    """Download a page and convert to markdown."""
    try:
        print(f"Downloading: {url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        # Convert HTML to markdown
        markdown = html_to_markdown(response.text, url)

        # Create directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"  -> Saved: {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  -> Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  -> Error processing {url}: {e}")
        return False


def path_to_filename(path):
    """Convert URL path to filename."""
    if path == "/" or path == "":
        return "index.md"

    # Remove leading/trailing slashes and convert to filename
    clean_path = path.strip("/")

    # Handle nested paths like /getting_started/installation/
    if "/" in clean_path:
        # Convert to flat filename: getting_started/installation -> getting_started-installation.md
        return clean_path.replace("/", "-") + ".md"

    return clean_path + ".md"


def main():
    """Main function to download all vLLM documentation."""
    print("=" * 60)
    print("vLLM Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Pages to download: {len(VLLM_DOC_PAGES)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "vllm"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, page_path in enumerate(VLLM_DOC_PAGES, 1):
        url = BASE_URL + page_path
        filename = path_to_filename(page_path)
        output_path = output_dir / filename

        print(f"[{i:3d}/{len(VLLM_DOC_PAGES)}] ", end="")

        if download_page(url, output_path):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(0.5)

    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

    # Calculate total size
    total_size = sum(f.stat().st_size for f in output_dir.glob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} pages failed to download")
        sys.exit(1)
    else:
        print("All pages downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
