#!/usr/bin/env python3
"""
ONNX Runtime Documentation Scraper
Downloads all ONNX Runtime documentation pages and converts to markdown.
ONNX Runtime is a cross-platform machine-learning model accelerator.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import re
import subprocess

# ONNX Runtime documentation pages extracted from sidebar
ONNX_DOC_PAGES = [
    "/docs/",
    "/docs/install/",
    "/docs/get-started/",
    "/docs/get-started/with-python.html",
    "/docs/get-started/with-cpp.html",
    "/docs/get-started/with-c.html",
    "/docs/get-started/with-csharp.html",
    "/docs/get-started/with-java.html",
    "/docs/get-started/with-javascript/",
    "/docs/get-started/with-javascript/web.html",
    "/docs/get-started/with-javascript/node.html",
    "/docs/get-started/with-javascript/react-native.html",
    "/docs/get-started/with-obj-c.html",
    "/docs/get-started/community-projects.html",
    "/docs/get-started/with-windows.html",
    "/docs/get-started/with-mobile.html",
    "/docs/get-started/training-on-device.html",
    "/docs/get-started/training-pytorch.html",
    "/docs/tutorials/",
    "/docs/tutorials/api-basics.html",
    "/docs/tutorials/accelerate-pytorch/",
    "/docs/tutorials/accelerate-pytorch/pytorch.html",
    "/docs/tutorials/accelerate-pytorch/resnet-inferencing.html",
    "/docs/tutorials/accelerate-pytorch/ort-training.html",
    "/docs/tutorials/tensorflow.html",
    "/docs/tutorials/huggingface.html",
    "/docs/tutorials/azureml.html",
    "/docs/tutorials/mobile/",
    "/docs/tutorials/mobile/pose-detection.html",
    "/docs/tutorials/mobile/deploy-android.html",
    "/docs/tutorials/mobile/superres.html",
    "/docs/tutorials/mobile/deploy-ios.html",
    "/docs/tutorials/mobile/helpers/",
    "/docs/tutorials/web/",
    "/docs/tutorials/web/build-web-app.html",
    "/docs/tutorials/web/env-flags-and-session-options.html",
    "/docs/tutorials/web/ep-webgpu.html",
    "/docs/tutorials/web/ep-webnn.html",
    "/docs/tutorials/web/large-models.html",
    "/docs/tutorials/web/performance-diagnosis.html",
    "/docs/tutorials/web/deploy.html",
    "/docs/tutorials/web/trouble-shooting.html",
    "/docs/tutorials/web/classify-images-nextjs-github-template.html",
    "/docs/tutorials/web/excel-addin-bert-js.html",
    "/docs/tutorials/iot-edge/",
    "/docs/tutorials/iot-edge/rasp-pi-cv.html",
    "/docs/tutorials/traditional-ml.html",
    "/docs/tutorials/csharp/",
    "/docs/tutorials/csharp/basic_csharp.html",
    "/docs/tutorials/csharp/bert-nlp-csharp-console-app.html",
    "/docs/tutorials/csharp/csharp-gpu.html",
    "/docs/tutorials/csharp/resnet50_csharp.html",
    "/docs/tutorials/csharp/stable-diffusion-csharp.html",
    "/docs/tutorials/csharp/yolov3_object_detection_csharp.html",
    "/docs/tutorials/csharp/fasterrcnn_csharp.html",
    "/docs/tutorials/on-device-training/",
    "/docs/tutorials/on-device-training/android-app.html",
    "/docs/tutorials/on-device-training/ios-app.html",
    "/docs/api/",
    # Python API
    "/docs/api/python",
    "/docs/api/python/tutorial.html",
    "/docs/api/python/api_summary.html",
    # C API (Doxygen)
    "/docs/api/c/struct_ort_api.html",
    "/docs/api/c/struct_ort_custom_op.html",
    "/docs/api/c/struct_ort_1_1_value.html",
    "/docs/api/c/group___global.html",
    # C# API
    "/docs/api/csharp/api",
    "/docs/api/csharp/api/Microsoft.ML.OnnxRuntime.SessionOptions.html",
    # Java API
    "/docs/api/java/ai/onnxruntime/OrtEnvironment.html",
    "/docs/api/java/ai/onnxruntime/OrtSession.html",
    "/docs/api/java/ai/onnxruntime/OnnxTensor.html",
    "/docs/api/java/ai/onnxruntime/OnnxJavaType.html",
    # JavaScript API
    "/docs/api/js/interfaces/InferenceSession.SessionOptions.html",
    "/docs/api/js/interfaces/Env.WebAssemblyFlags.html",
    "/docs/api/js/interfaces/Env.WebGpuFlags.html",
    "/docs/api/js/interfaces/Env-1.html",
    # Objective-C API
    "/docs/api/objectivec/index.html",
    "/docs/build/",
    "/docs/build/inferencing.html",
    "/docs/build/training.html",
    "/docs/build/eps.html",
    "/docs/build/web.html",
    "/docs/build/android.html",
    "/docs/build/ios.html",
    "/docs/build/custom.html",
    "/docs/build/dependencies.html",
    "/docs/execution-providers/",
    "/docs/execution-providers/CUDA-ExecutionProvider.html",
    "/docs/execution-providers/TensorRT-ExecutionProvider.html",
    "/docs/execution-providers/TensorRTRTX-ExecutionProvider.html",
    "/docs/execution-providers/OpenVINO-ExecutionProvider.html",
    "/docs/execution-providers/oneDNN-ExecutionProvider.html",
    "/docs/execution-providers/DirectML-ExecutionProvider.html",
    "/docs/execution-providers/QNN-ExecutionProvider.html",
    "/docs/execution-providers/NNAPI-ExecutionProvider.html",
    "/docs/execution-providers/CoreML-ExecutionProvider.html",
    "/docs/execution-providers/Xnnpack-ExecutionProvider.html",
    "/docs/execution-providers/ROCm-ExecutionProvider.html",
    "/docs/execution-providers/MIGraphX-ExecutionProvider.html",
    "/docs/execution-providers/Vitis-AI-ExecutionProvider.html",
    "/docs/execution-providers/Azure-ExecutionProvider.html",
    "/docs/execution-providers/community-maintained/",
    "/docs/execution-providers/community-maintained/ACL-ExecutionProvider.html",
    "/docs/execution-providers/community-maintained/ArmNN-ExecutionProvider.html",
    "/docs/execution-providers/community-maintained/TVM-ExecutionProvider.html",
    "/docs/execution-providers/community-maintained/RKNPU-ExecutionProvider.html",
    "/docs/execution-providers/community-maintained/CANN-ExecutionProvider.html",
    "/docs/execution-providers/add-execution-provider.html",
    "/docs/execution-providers/EP-Context-Design.html",
    "/docs/execution-providers/plugin-ep-libraries.html",
    "/docs/genai/",
    "/docs/genai/tutorials/",
    "/docs/genai/tutorials/phi3-v.html",
    "/docs/genai/tutorials/phi3-python.html",
    "/docs/genai/tutorials/phi2-python.html",
    "/docs/genai/tutorials/finetune.html",
    "/docs/genai/tutorials/deepseek-python.html",
    "/docs/genai/tutorials/snapdragon.html",
    "/docs/genai/api/",
    "/docs/genai/api/python.html",
    "/docs/genai/api/csharp.html",
    "/docs/genai/api/c.html",
    "/docs/genai/api/cpp.html",
    "/docs/genai/api/java.html",
    "/docs/genai/howto/",
    "/docs/genai/howto/install.html",
    "/docs/genai/howto/build-from-source.html",
    "/docs/genai/howto/build-model.html",
    "/docs/genai/howto/build-models-for-snapdragon.html",
    "/docs/genai/howto/troubleshoot.html",
    "/docs/genai/howto/migrate.html",
    "/docs/genai/howto/past-present-share-buffer.html",
    "/docs/genai/reference/",
    "/docs/genai/reference/config.html",
    "/docs/genai/reference/adapter.html",
    "/docs/extensions/",
    "/docs/extensions/add-op.html",
    "/docs/extensions/build.html",
    "/docs/performance/",
    "/docs/performance/tune-performance/",
    "/docs/performance/tune-performance/profiling-tools.html",
    "/docs/performance/tune-performance/logging_tracing.html",
    "/docs/performance/tune-performance/memory.html",
    "/docs/performance/tune-performance/threading.html",
    "/docs/performance/tune-performance/iobinding.html",
    "/docs/performance/tune-performance/troubleshooting.html",
    "/docs/performance/model-optimizations/",
    "/docs/performance/model-optimizations/quantization.html",
    "/docs/performance/model-optimizations/float16.html",
    "/docs/performance/model-optimizations/graph-optimizations.html",
    "/docs/performance/model-optimizations/ort-format-models.html",
    "/docs/performance/model-optimizations/ort-format-model-runtime-optimization.html",
    "/docs/performance/transformers-optimization.html",
    "/docs/performance/olive.html",
    "/docs/performance/device-tensor.html",
    "/docs/reference/",
    "/docs/reference/compatibility.html",
    "/docs/reference/high-level-design.html",
    "/docs/reference/operators/",
    "/docs/reference/operators/add-custom-op.html",
    "/docs/reference/operators/ContribOperators.html",
    "/docs/reference/operators/OperatorKernels.html",
    "/docs/reference/operators/reduced-operator-config-file.html",
    "/docs/reference/releases-servicing.html",
    "/docs/reference/citing.html",
    "/docs/ecosystem/",
    "/docs/ecosystem/acpt.html",
]

BASE_URL = "https://onnxruntime.ai"


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # Just the Docs uses <main> with id="main-content" or class="main"
    main_match = re.search(
        r'<main[^>]*id="main-content"[^>]*>(.*?)</main>',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    if main_match:
        html_content = main_match.group(1)
    else:
        # Try alternate selector for main content
        main_match = re.search(
            r'<div[^>]*class="[^"]*main-content[^"]*"[^>]*>(.*?)</div>\s*</main>',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )
        if main_match:
            html_content = main_match.group(1)

    # Remove navigation and side elements
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<aside[^>]*>.*?</aside>', '', html_content, flags=re.DOTALL)

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
    # Remove /docs/ prefix
    path = path.replace("/docs/", "")

    if path == "" or path == "/":
        return "index.md"

    # Remove leading/trailing slashes
    clean_path = path.strip("/")

    # If it ends with .html, replace with .md
    if clean_path.endswith(".html"):
        clean_path = clean_path[:-5] + ".md"
    else:
        # It's a directory index
        clean_path = clean_path.replace("/", "-") + "-index.md"

    # Convert slashes to dashes for flat structure
    clean_path = clean_path.replace("/", "-")

    return clean_path


def main():
    """Main function to download all ONNX Runtime documentation."""
    print("=" * 60)
    print("ONNX Runtime Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Pages to download: {len(ONNX_DOC_PAGES)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "onnxruntime"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, page_path in enumerate(ONNX_DOC_PAGES, 1):
        url = BASE_URL + page_path
        filename = path_to_filename(page_path)
        output_path = output_dir / filename

        print(f"[{i:3d}/{len(ONNX_DOC_PAGES)}] ", end="")

        if download_page(url, output_path):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(0.3)

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
