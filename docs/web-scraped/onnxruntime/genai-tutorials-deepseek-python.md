# Source: https://onnxruntime.ai/docs/genai/tutorials/deepseek-python.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#reasoning-in-python-with-deepseek-r1-distill-models) Reasoning in Python with DeepSeek-R1-Distill models

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#1-pre-requisites-make-a-virtual-environment-and-install-onnx-runtime-genai) 1. Pre-Requisites: Make a virtual environment and install ONNX Runtime GenAI 

``` highlight
# Installing onnxruntime-genai, olive, and dependencies for CPU
python -m venv .venv && source .venv/bin/activate
pip install requests numpy --pre onnxruntime-genai olive-ai
```

``` highlight
# Installing onnxruntime-genai, olive, and dependencies for CUDA GPU
python -m venv .venv && source .venv/bin/activate
pip install requests numpy --pre onnxruntime-genai-cuda "olive-ai[gpu]"
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#2-acquire-model) 2. Acquire model 

Choose your model and convert to ONNX. Note that many LLMs work, so feel free to try with other models too:

``` highlight
# Using Olive auto-opt to pull a huggingface model, optimize for CPU, and quantize to INT4 using RTN. 
olive auto-opt --model_name_or_path deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B --output_path ./deepseek-r1-distill-qwen-1.5B --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1
```

``` highlight
# Using Olive auto-opt to pull a huggingface model, optimize for CUDA GPUs, and quantize to INT4 using RTN. 
olive auto-opt --model_name_or_path deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B --output_path ./deepseek-r1-distill-qwen-1.5B --device gpu --provider CUDAExecutionProvider --precision int4 --use_model_builder --log_level 1
```

OR download directly using the Huggingface CLI:

``` highlight
# Download the model directly using the huggingface cli
huggingface-cli download onnxruntime/DeepSeek-R1-Distill-ONNX --include 'deepseek-r1-distill-qwen-1.5B/*' --local-dir .
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#3-play-with-your-model-on-device) 3. Play with your model on device! 

``` highlight
# CPU Chat inference. If you pulled the model from huggingface, adjust the model directory (-m) accordingly 
curl -o https://raw.githubusercontent.com/microsoft/onnxruntime-genai/refs/heads/main/examples/python/model-chat.py
python model-chat.py -m deepseek-r1-distill-qwen-1.5B/model -e cpu --chat_template "<|begin▁of▁sentence|><|User|><|Assistant|>"
```

``` highlight
# On-Device GPU Chat inference. Works on devices with Nvidia GPUs. If you pulled the model from huggingface, adjust the model directory (-m) accordingly 
curl -o https://raw.githubusercontent.com/microsoft/onnxruntime-genai/refs/heads/main/examples/python/model-chat.py
python model-chat.py -m deepseek-r1-distill-qwen-1.5B/model -e cuda --chat_template "<|begin▁of▁sentence|><|User|><|Assistant|>"
```