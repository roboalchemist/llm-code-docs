# ML Inference Tools - Quick Reference by Use Case

**Quick lookup for finding the right tool for your inference scenario**

---

## 1. LLM Serving & GenAI Inference

### Self-Hosted (On-Premises)
```
Priority   | Tool              | Best For                              | Key Feature
-----------|-------------------|---------------------------------------|------------------
Tier 1     | vLLM              | High throughput, multi-model LLM      | PagedAttention, OpenAI-compatible
Tier 1     | llama.cpp         | Local/quantized inference             | GGUF format, CPU-friendly, 4-bit
Tier 2     | SGLang            | Structured/constrained generation     | Grammar control, efficient batching
Tier 2     | NVIDIA TensorRT   | NVIDIA GPU optimization               | TensorRT-LLM, extreme performance
Tier 3     | Ray Serve         | Distributed scaling with composition  | Actor-based, cost optimization
```

### Managed APIs
```
Priority   | Tool              | Best For                              | Key Feature
-----------|-------------------|---------------------------------------|------------------
Tier 2     | Together AI       | 200+ open LLMs, reliable API          | OpenAI-compatible, token caching
Tier 2     | Fireworks AI      | Fast multi-modal (text/image/audio)   | 50ms latency, HIPAA-compliant
Tier 2     | Groq              | Ultra-low latency                     | Language Processing Unit hardware
Tier 2     | DeepInfra         | OpenAI-compatible, enterprise-grade   | Monitoring, scaling, private models
Tier 2     | SiliconFlow       | Cost-optimized with 2.3× speedup      | Elastic GPU scaling
Tier 2     | Mistral AI        | Open-weight models, no lock-in        | Mistral 7B/Large API
Tier 3     | Lepton AI         | Container-based inference             | Custom models, multi-cloud
Tier 2     | AWS Bedrock       | Foundation models (Claude, Llama)     | Serverless, compliance-ready
```

### When to Use What:
- **vLLM** → Self-hosted, high-throughput, full control needed
- **llama.cpp** → Local/offline inference, quantized models, limited VRAM
- **Together AI** → Managed API, 200+ models, cost optimization
- **Fireworks AI** → Managed API, multimodal, compliance requirements
- **Groq** → Absolute lowest latency requirements (<10ms)
- **AWS Bedrock** → Enterprise, CloudFormation integration

---

## 2. Mobile App Inference (iOS/Android)

### Recommended Stack by Priority
```
Rank | iOS                    | Android              | Cross-Platform
-----|------------------------|----------------------|---------------
1    | Core ML                | TensorFlow Lite      | MediaPipe
2    | TensorFlow Lite        | ML Kit               | NCNN
3    | ML Kit                 | NCNN                 | TensorFlow Lite
4    | N/A                    | MNN                  | N/A
```

### Detailed Breakdown:

#### iOS-Native (Recommended for iOS-only)
| Tool | Setup | Performance | Privacy | GPU Support |
|------|-------|-------------|---------|-------------|
| **Core ML** | Xcode integration | SOTA (Neural Engine) | On-device | Full (A-series chips) |
| **TensorFlow Lite** | Swift package | Good | On-device | GPU delegate |
| **ML Kit** | Firebase SDK | Good (pre-built) | On-device | Limited |

#### Android-Native (Recommended for Android-only)
| Tool | Setup | Performance | Privacy | GPU Support |
|------|-------|-------------|---------|-------------|
| **TensorFlow Lite** | Gradle dependency | Excellent | On-device | NNAPI, GPU |
| **ML Kit** | Google Play Services | Good (pre-built) | On-device | Limited |
| **NCNN** | CMake/JNI | Very Good (lightweight) | On-device | Some models |

#### Cross-Platform (Best for code reuse)
| Tool | Coverage | Code Reuse | Size | Setup Complexity |
|------|----------|-----------|------|------------------|
| **MediaPipe** | iOS/Android/Web | ~90% (C++/Python) | 30-50MB | Medium |
| **TensorFlow Lite** | iOS/Android/Web | ~80% (C++/Java/Swift) | 15-25MB | Easy |
| **NCNN** | iOS/Android/embedded | ~95% (C++) | 2-5MB | Complex |

### Quick Decision Tree:
```
Q: iOS only?                → Use Core ML (fastest, Native Engine)
Q: Android only?            → Use TensorFlow Lite (best ecosystem)
Q: Both iOS + Android?      → Use MediaPipe or TensorFlow Lite
Q: Minimal app size?        → Use NCNN
Q: Pre-trained solutions?   → Use ML Kit or MediaPipe
Q: Custom model inference?  → Use TensorFlow Lite or Core ML
Q: Real-time performance?   → Use Core ML (iOS) or TFLite (Android)
Q: Privacy critical?        → All recommended options handle on-device
```

---

## 3. Edge Device Inference (IoT, Embedded, RPi)

### By Device Type & Constraints:

#### Raspberry Pi / ARM Linux
```
Priority | Tool              | Size    | Setup  | Performance | Notes
---------|-------------------|---------|--------|-------------|----------
1        | TensorFlow Lite   | 20-30MB | Easy   | Good        | Official RPi support
2        | NCNN              | 2-5MB   | Easy   | Excellent   | Ultra-lightweight
3        | ONNX Runtime      | 15-25MB | Easy   | Good        | Multi-framework
2        | llama.cpp         | 5-10MB  | Easy   | Good        | LLM-specific, quantized
```

#### Microcontroller / Ultra-Constrained
```
Priority | Tool              | Size    | Memory | Architecture | Notes
---------|-------------------|---------|--------|--------------|----------
1        | TensorFlow Lite Micro | 200KB | <1MB  | ARM M4/M7   | Designed for MCU
2        | Apache TVM        | Variable| Tunable| Custom       | Compiler-based
1        | NCNN              | 2-5MB   | 10-50MB| ARM M4+     | Minimal deps
```

#### NVIDIA Jetson (Orin, Xavier, Nano)
```
Tool                        | GPU Memory | Use Case | Latency
----------------------------|------------|----------|----------
NVIDIA TensorRT             | Full GPU   | Inference | <5ms (Orin)
NVIDIA TensorRT-LLM         | 8-16GB     | LLM/GenAI | <50ms (quantized)
TensorFlow Lite (GPU Delegate) | 2-4GB    | Mobile models | <50ms
vLLM + GPU                  | Full GPU   | Multi-LLM serving | <100ms
```

#### IoT Cloud Gateway
```
Priority | Tool              | Deployment | Scaling | Monitoring
---------|-------------------|------------|---------|----------
Tier 2   | ONNX Runtime      | Container  | Horizontal | Built-in
Tier 2   | Ray Serve         | Kubernetes | Auto-scale | Integrated
Tier 1   | TensorFlow Lite   | Docker     | Manual  | External
Tier 3   | KServe            | Kubernetes | Auto    | Grafana
```

---

## 4. Cloud ML Inference Services

### Major Cloud Providers

#### AWS (Amazon Web Services)
| Service | Use Case | Model Types | Pricing Model |
|---------|----------|-------------|---------------|
| **SageMaker** | Full ML lifecycle, multi-model | Custom, TensorFlow, PyTorch | Pay-per-endpoint |
| **Bedrock** | Foundation models (Claude, Llama) | Pre-trained only | Pay-per-token |
| **EC2 (DIY)** | Maximum control, custom setup | Any | Pay-per-instance |

#### Google Cloud
| Service | Use Case | Model Types | Pricing Model |
|---------|----------|-------------|---------------|
| **Vertex AI** | Managed inference, AutoML | Custom, TensorFlow, scikit-learn | Pay-per-prediction |
| **AI Platform** (legacy) | Training + serving integrated | Custom, TensorFlow, scikit-learn | Variable |

#### Microsoft Azure
| Service | Use Case | Model Types | Pricing Model |
|---------|----------|-------------|---------------|
| **Azure ML** | Enterprise, hybrid deployments | Custom, PyTorch, scikit-learn | Pay-per-compute |
| **Azure OpenAI** | Foundation models (GPT-4, Claude) | Pre-trained only | Pay-per-token |

### Specialized Inference Platforms (API-First)
```
Tier | Platform      | API Type          | Cost Model    | Best For
-----|---------------|-------------------|---------------|------------------
Tier 2| Together AI  | REST (OpenAI-compat) | Per token    | 200+ LLMs, cost
Tier 2| Fireworks AI | REST (OpenAI-compat) | Per token    | Multimodal, speed
Tier 2| Groq         | REST               | Per token    | Ultra-low latency
Tier 2| DeepInfra    | REST (OpenAI-compat) | Per token    | Enterprise features
Tier 2| SiliconFlow  | REST (OpenAI-compat) | Per token    | Cost optimization
```

### Quick Selection:
```
Q: Using AWS already?           → SageMaker or Bedrock
Q: Using Google Cloud?          → Vertex AI
Q: Using Azure/Microsoft?       → Azure ML or Azure OpenAI
Q: Want to avoid vendor lock-in?→ Together AI, Fireworks, Mistral
Q: Need lowest latency?         → Groq
Q: Need lowest cost?            → SiliconFlow, Together AI
Q: Need compliance (HIPAA)?     → Fireworks AI, Azure, AWS
Q: Need enterprise support?     → DeepInfra, CoreWeave
```

---

## 5. Training-to-Inference Pipeline Integration

### Framework Combinations:
```
Training Framework | Inference Runtime    | Model Exchange | Notes
-------------------|----------------------|-----------------|----------
PyTorch           | ONNX Runtime         | ONNX export     | Industry standard
PyTorch           | TorchScript + Triton | TorchScript     | PyTorch-native
TensorFlow        | TensorFlow Lite      | SavedModel      | Mobile-optimized
TensorFlow        | TensorFlow Serving   | SavedModel      | Full pipeline
JAX               | ONNX Runtime         | ONNX export     | High-performance
Hugging Face      | vLLM                 | Transformers    | LLM-optimized
Custom (Keras)    | ONNX Runtime         | ONNX export     | Universal export
```

### Recommended Stacks by Scenario:

#### Production PyTorch Model
```python
# Training
model = MyPyTorchModel()
torch.onnx.export(model, ...)  # Export to ONNX

# Inference Options:
1. ONNX Runtime (portable)
2. TorchScript (PyTorch-native)
3. NVIDIA TensorRT (GPU optimization)
4. Triton Inference Server (multi-model)
```

#### Production TensorFlow Model
```python
# Training
model = keras.Sequential([...])
model.save('model/', format='tf')

# Inference Options:
1. TensorFlow Serving (native)
2. TensorFlow Lite (mobile)
3. ONNX Runtime (portability)
4. Triton Inference Server (enterprise)
```

#### Production LLM Model
```python
# Training/Fine-tuning with Hugging Face
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained("mistral-7b")

# Inference Options:
1. vLLM (high-throughput self-hosted)
2. llama.cpp (local/quantized)
3. Together AI (managed API)
4. Fireworks AI (managed API, multimodal)
```

---

## 6. Developer Experience Comparison

### Easiest to Get Started
```
Tier | Tool              | Setup Time | Learning Curve | Code Complexity
-----|-------------------|------------|----------------|----------------
Tier 1| Streamlit        | 5 minutes  | Minutes        | < 50 lines
Tier 2| Gradio           | 5 minutes  | Minutes        | < 50 lines
Tier 3| FastAPI          | 15 minutes | Hours          | 100-200 lines
Tier 2| AWS Bedrock      | 5 minutes  | Minutes        | 10-20 lines
Tier 2| Hugging Face API | 5 minutes  | Minutes        | 10-20 lines
```

### Highest Performance (Latency-Critical)
```
Tier | Tool              | Latency | Setup Effort | Complexity
-----|-------------------|---------|--------------|----------
Tier 1| Groq             | <10ms   | Low          | Low
Tier 2| Fireworks AI     | ~50ms   | Low          | Low
Tier 1| vLLM + NVIDIA    | ~50ms   | Medium       | Medium
Tier 1| llama.cpp        | ~20ms   | Low          | Low
Tier 1| NVIDIA TensorRT  | <5ms    | High         | High
```

### Most Flexible/Customizable
```
Tier | Tool              | Flexibility | Learning Curve | Deployment Options
-----|-------------------|-------------|----------------|-------------------
Tier 1| PyTorch          | Extreme     | Steep          | Any (via ONNX)
Tier 1| vLLM             | Very High   | Moderate       | Self-hosted, Ray
Tier 1| ONNX Runtime     | High        | Moderate       | Any hardware
Tier 2| Ray Serve        | High        | Moderate-Steep | Kubernetes, cloud
Tier 1| TensorFlow Lite  | High        | Easy           | iOS, Android, Web
```

---

## 7. Hardware-Specific Recommendations

### NVIDIA GPUs
```
GPU Type       | Best Tool              | Alternative          | Typical Use Case
---------------|------------------------|----------------------|------------------
A100 / H100    | NVIDIA TensorRT        | vLLM                 | Data center LLM
A6000 / A5000  | NVIDIA TensorRT        | vLLM, PyTorch        | High-throughput inference
L4             | vLLM                   | NVIDIA TensorRT      | Cost-effective serving
RTX 4090/6000  | NVIDIA TensorRT        | vLLM, TensorFlow     | Workstation inference
T4             | vLLM                   | TensorFlow Lite      | Edge + mobile
Jetson Orin    | NVIDIA TensorRT        | TensorFlow Lite      | Edge AI
```

### Apple Silicon (M1/M2/M3)
```
Chip      | Best Tool           | Alternative              | Performance
-----------|---------------------|--------------------------|----------
M1 Pro    | Core ML             | ONNX Runtime, TFLite     | Excellent
M1 Max    | Core ML (full GPU)  | ONNX Runtime, TFLite     | Excellent
M2 Ultra  | Core ML             | vLLM, ONNX Runtime       | Exceptional
MacBook   | Core ML, TFLite     | PyTorch (native)         | Good
```

### Intel Hardware
```
Hardware   | Best Tool              | Alternative          | Notes
-----------|------------------------|-----------------------|----------
Xeon CPU   | Intel OpenVINO         | ONNX Runtime, TFLite  | Optimized for Intel
Core i9    | ONNX Runtime           | Intel OpenVINO        | Cross-platform
GPU Arc    | Intel OpenVINO         | ONNX Runtime          | Newer Intel GPUs
VPU/Gaudi  | Intel OpenVINO + SDK   | TensorRT alternative  | Specialized accelerators
```

### ARM/Mobile
```
Device        | Best Tool              | Alternative          | Model Size
--------------|------------------------|-----------------------|----------
Raspberry Pi  | TensorFlow Lite        | NCNN, ONNX Runtime   | <100MB
Android Phone | TensorFlow Lite        | NCNN, ML Kit         | <50MB
iOS iPhone    | Core ML                | TFLite               | <50MB
Microcontrol  | TFLite Micro           | NCNN, Apache TVM     | <1MB
```

---

## 8. Decision Flowchart (Text Format)

```
START: What are you building?
│
├─ LLM / Generative AI Inference?
│  ├─ Self-hosted, full control?  → vLLM or llama.cpp
│  └─ Managed API, minimal ops?   → Together AI or Fireworks AI
│
├─ Mobile App (iOS/Android)?
│  ├─ iOS only?                   → Core ML
│  ├─ Android only?               → TensorFlow Lite
│  └─ Cross-platform?             → MediaPipe or TensorFlow Lite
│
├─ Edge Device / IoT / Raspberry Pi?
│  ├─ Minimal footprint?          → NCNN
│  ├─ GPU acceleration (Jetson)?  → NVIDIA TensorRT
│  └─ Balanced?                   → TensorFlow Lite or ONNX Runtime
│
├─ Cloud-Hosted Service?
│  ├─ AWS?                        → SageMaker or Bedrock
│  ├─ Google Cloud?               → Vertex AI
│  ├─ Azure / Microsoft?          → Azure ML or OpenAI Service
│  └─ Vendor-agnostic API?        → Together AI or Fireworks AI
│
├─ Web Demo / Quick Prototype?
│  ├─ Minimal code?               → Streamlit or Gradio
│  ├─ Custom API?                 → FastAPI
│  └─ Serverless?                 → AWS Lambda + Bedrock
│
└─ High-Performance / Research?
   ├─ PyTorch model?              → ONNX Runtime or TorchScript
   ├─ TensorFlow model?           → TensorFlow Serving
   ├─ Extreme latency critical?   → Groq or NVIDIA TensorRT
   └─ Distributed / multi-model?  → Triton or KServe
```

---

## 9. Ecosystem Map (Relationships & Integration)

```
Training & Model Development
        ↓
    [PyTorch / TensorFlow / JAX]
        ↓
    ┌───────────────────────────┐
    ↓                           ↓
Model Conversion          Model Optimization
ONNX / TorchScript        TensorRT / OpenVINO
    ↓                           ↓
    └───────────────────────────┘
            ↓
    Serving & Deployment
        ↓
    ┌─────────────────────────────┐
    │                             │
    ↓                             ↓
Self-Hosted                  Managed APIs
├─ vLLM                    ├─ Together AI
├─ ONNX Runtime            ├─ Fireworks AI
├─ Triton                  ├─ AWS Bedrock
├─ TensorFlow Serving      ├─ Vertex AI
└─ Ray Serve               └─ Azure OpenAI
    │
    ├─ Mobile (TFLite, Core ML)
    ├─ Edge (NCNN, MNN)
    └─ Cloud (K8s via KServe)
```

---

## 10. Common Pitfalls & Solutions

| Problem | Common Cause | Solution |
|---------|--------------|----------|
| Model works in training, fails in inference | Framework mismatch | Use ONNX for portability |
| High latency in production | Single-threaded serving | Switch to vLLM or Triton |
| Mobile app crashes with OOM | Wrong model size | Use TensorFlow Lite or NCNN + quantization |
| GPU memory exhausted | Batch size too large | Enable dynamic batching (Triton, vLLM) |
| Inconsistent results across platforms | Precision differences | Use same inference runtime everywhere |
| Can't scale beyond single server | Monolithic deployment | Switch to distributed framework (Ray, KServe) |
| Vendor lock-in to one cloud | Proprietary APIs | Use ONNX + ONNX Runtime for portability |
| Model performance degrades over time | Stale dependencies | Pin versions, automated monitoring |

---

## Document Metadata

**Version**: 1.0
**Last Updated**: 2025-12-31
**Coverage**: 77 ML inference tools across all major categories
**Audience**: ML engineers, full-stack developers, DevOps engineers
**Related Documents**:
- ML_INFERENCE_RESEARCH.md (comprehensive reference)
- ML_INFERENCE_TOOLS.csv (searchable tool list)
- ML_INFERENCE_SCRAPING_PRIORITY.md (documentation priorities)
