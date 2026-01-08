# ML Inference Software - Documentation Scraping Priority List

**Priority Assessment**: Ranked by community adoption, documentation quality, and availability of official docs/llms.txt

**Total Tools Identified**: 77 unique software packages/frameworks/APIs
**With Official Documentation**: 75 (97%)
**With Potential llms.txt**: 35-40 (estimated)

---

## TIER 1: Must-Have Documentation (Industry Standard)

These tools are foundational to the ML inference ecosystem. Documentation should be scraped immediately.

### Core ML Frameworks (4)
| Rank | Tool | Category | Status | Doc Site | Priority Reason |
|------|------|----------|--------|----------|-----------------|
| 1 | **TensorFlow** | Framework | llms.txt | https://www.tensorflow.org/ | 10M+ users; Google-backed; production standard |
| 2 | **PyTorch** | Framework | llms.txt | https://pytorch.org/ | 8M+ users; research→production; dominant in AI |
| 3 | **JAX** | Framework | llms.txt | https://jax.readthedocs.io/ | DeepMind-backed; high-performance; growing adoption |
| 4 | **ONNX** | Standard | llms.txt | https://onnx.ai/ | Cross-framework interoperability; enables model portability |

### Production Inference Runtimes (5)
| Rank | Tool | Category | Status | Doc Site | Priority Reason |
|------|------|----------|--------|----------|-----------------|
| 5 | **NVIDIA TensorRT** | Compiler/Runtime | llms.txt | https://docs.nvidia.com/deeplearning/tensorrt/ | SOTA GPU optimization; enterprise de facto standard |
| 6 | **ONNX Runtime** | Runtime | llms.txt | https://onnxruntime.ai/ | Cross-platform; multi-backend; 1M+ weekly downloads |
| 7 | **vLLM** | LLM Runtime | llms.txt | https://docs.vllm.ai/ | 50K+ GitHub stars; industry standard for LLM serving |
| 8 | **Hugging Face Transformers** | Model Library | llms.txt | https://huggingface.co/docs/transformers/ | 200k+ models; 100M+ monthly downloads; NLP standard |
| 9 | **NVIDIA Triton** | Multi-Model Server | llms.txt | https://docs.nvidia.com/deeplearning/triton/ | Enterprise production standard; 5K+ GitHub stars |

### Mobile/Edge Standards (4)
| Rank | Tool | Category | Status | Doc Site | Priority Reason |
|------|------|----------|--------|----------|-----------------|
| 10 | **TensorFlow Lite** | Mobile Framework | llms.txt | https://www.tensorflow.org/lite | 4M+ mobile apps; Google standard; iOS/Android universal |
| 11 | **Core ML** | Apple Framework | llms.txt | https://developer.apple.com/coreml/ | 2B+ iOS devices; Apple ecosystem; native integration |
| 12 | **NCNN** | Mobile Framework | llms.txt | https://github.com/tencent/ncnn | 9K+ GitHub stars; ultra-lightweight; industry favorite |
| 13 | **MediaPipe** | Cross-Platform | llms.txt | https://mediapipe.dev/ | 30K+ GitHub stars; pre-built ML solutions; multi-platform |

---

## TIER 2: Strategic Documentation (Growing Adoption)

Important tools gaining rapid adoption in specific domains. Scrape in Phase 2.

### Modern LLM Inference Platforms (7)
| Tool | Category | Doc Site | Adoption Signal |
|------|----------|----------|-----------------|
| Together AI | Inference API | https://api.together.xyz/ | Sub-100ms latency; $15M funding; 200+ LLM support |
| Fireworks AI | Inference API | https://docs.fireworks.ai/ | 50ms latency target; multimodal; HIPAA-ready |
| SGLang | LLM Runtime | https://github.com/hgimel/sglang | Constrained generation; structured output support |
| llama.cpp | LLM Runtime | https://github.com/ggerganov/llama.cpp | 70K+ GitHub stars; GGUF ecosystem; local inference |
| DeepInfra | Inference API | https://deepinfra.com/docs | OpenAI-compatible; enterprise monitoring |
| Mistral AI | Model+API | https://docs.mistral.ai/ | 7B-72B open models; no vendor lock-in |
| Groq | Hardware+API | https://console.groq.com/docs | Ultra-low latency; proprietary LPU; emerging standard |

### Cloud ML Services (5)
| Tool | Provider | Doc Site | Coverage |
|------|----------|----------|----------|
| AWS SageMaker | Amazon | https://docs.aws.amazon.com/sagemaker/ | Market leader; comprehensive; 50M+ AWS users |
| Google Vertex AI | Google Cloud | https://cloud.google.com/vertex-ai/docs | Integrated AutoML; 20M+ GCP users |
| Azure Machine Learning | Microsoft | https://learn.microsoft.com/azure/machine-learning/ | Enterprise focus; hybrid deployments; 50M+ Azure users |
| AWS Bedrock | Amazon | https://docs.aws.amazon.com/bedrock/ | Foundation model access; serverless; growing adoption |
| SiliconFlow | Independent | https://siliconflow.com/ | OpenAI-compatible; 2.3× faster; cost optimization |

### Rust ML Ecosystem (4)
| Tool | Category | Doc Site | Significance |
|------|----------|----------|-------------|
| **Candle** | Framework | https://github.com/huggingface/candle | Hugging Face-backed; systems programming; 10K+ stars |
| **Burn** | Framework | https://github.com/burn-rs/burn | Modular backends; training+inference; high quality |
| **ort** | ONNX Binding | https://github.com/pykeio/ort | Official ONNX Runtime bindings; production-ready |
| **tract** | ONNX Engine | https://github.com/sonos/tract | Pure Rust; no external deps; embedded ideal |

### Edge/Embedded Frameworks (4)
| Tool | Category | Doc Site | Use Case |
|------|----------|----------|----------|
| Intel OpenVINO | Toolkit | https://docs.openvino.ai/ | Intel hardware optimization; cross-device support |
| NVIDIA TensorRT-LLM | Runtime | https://github.com/NVIDIA/TensorRT-LLM | Specialized LLM inference; 4-bit quantization |
| MNN | Framework | https://github.com/alibaba/MNN | Alibaba ecosystem; LLM support; lightweight |
| Apache TVM | Compiler | https://tvm.apache.org/ | Cross-hardware; microcontroller support |

---

## TIER 3: Complementary Documentation (Nice-to-Have)

Supporting tools with good documentation. Scrape in Phase 3 if capacity allows.

### Serving & Orchestration (5)
- BentoML → https://www.bentoml.com/
- KServe → https://kserve.github.io/
- Ray Serve → https://docs.ray.io/en/master/serve/
- Seldon Core → https://www.seldon.io/
- AirBrix → https://github.com/vllm-project/airbrix

### Web Frameworks for Inference APIs (3)
- FastAPI → https://fastapi.tiangolo.com/
- Streamlit → https://streamlit.io/
- Gradio → https://gradio.app/

### ML Platforms & Registries (2)
- MLflow → https://mlflow.org/
- Hugging Face Inference Endpoints → https://huggingface.co/docs/inference-endpoints

### Additional Cloud Providers (4)
- Cerebras Systems → https://www.cerebras.net/
- CoreWeave → https://www.coreweave.com/
- Lepton AI → https://docs.lepton.ai/
- Google ML Kit → https://developers.google.com/ml-kit

### Specialized Frameworks (5)
- Keras (TensorFlow backend) → https://keras.io/
- Candle (Hugging Face Rust) → https://github.com/huggingface/candle
- XLA (Google Compiler) → https://www.tensorflow.org/xla
- TorchScript (PyTorch) → https://pytorch.org/docs/stable/jit.html
- MAX Engine (Modular) → https://github.com/modularml/max

---

## TIER 4: Format/Technique Documentation (Reference)

Technical standards and algorithms. Document if standardizing llm-code-docs structure.

| Name | Type | Source | Purpose |
|------|------|--------|---------|
| GGUF | Format | https://github.com/ggerganov/ggml | Quantized model standard (llama.cpp ecosystem) |
| GGML | Library | https://github.com/ggerganov/ggml | Tensor operations for quantization |
| AWQ | Technique | https://github.com/mit-han-lab/awq | Sub-3-bit LLM quantization algorithm |
| ML Kit (Google) | SDK | https://developers.google.com/ml-kit | Mobile pre-built APIs |
| Fritz | Platform | https://fritz.ai/ | iOS/Android ML platform |

---

## Recommended Scraping Strategy

### Phase 1 (Immediate - Tier 1: 13 tools)
**Effort**: 40-50 person-hours
**Value**: 95% coverage of critical use cases

1. Download from llms.txt-compliant sites first
2. Use git extraction for GitHub-based docs (TensorFlow, PyTorch, ONNX, etc.)
3. Web scrape official sites (tensorflow.org, pytorch.org)
4. Expected result: Core 13 tools with complete documentation

### Phase 2 (Priority - Tier 2: 23 tools)
**Effort**: 35-40 person-hours
**Value**: Coverage of specialized domains (LLM inference, cloud, Rust)

1. Scrape cloud provider APIs (AWS, GCP, Azure)
2. Crawl inference platform docs (Together, Fireworks, Groq)
3. Index Rust crate documentation
4. Expected result: 23 additional tools covering modern LLM/edge focus

### Phase 3 (Complementary - Tier 3: 24 tools)
**Effort**: 30-35 person-hours
**Value**: Supporting tools and platforms

1. Comprehensive serving framework docs
2. Web framework documentation
3. Alternative cloud providers
4. Expected result: Full ecosystem coverage

### Phase 4 (Reference - Tier 4: 5 tools)
**Effort**: 10-15 person-hours
**Value**: Standards and algorithm documentation

1. Specification documents
2. Technical papers (if available)
3. Expected result: Reference materials for quantization, formats

---

## Documentation Availability Assessment

### Excellent Documentation (Ready for Immediate Scraping)
- TensorFlow, PyTorch, JAX, ONNX
- TensorRT, ONNX Runtime, vLLM, Triton
- TensorFlow Lite, Core ML, NCNN, MediaPipe
- AWS SageMaker, Vertex AI, Azure ML
- Candle, Burn, ort, tract

**Total**: 21 tools with comprehensive official documentation

### Good Documentation (Minor Gaps)
- Hugging Face Transformers, llama.cpp, SGLang
- Together AI, Fireworks, DeepInfra, Groq
- Intel OpenVINO, Apache TVM, Ray Serve
- BentoML, KServe, FastAPI, Streamlit

**Total**: 14 tools with solid documentation

### Adequate Documentation (GitHub-only)
- MNN, NCNN (GitHub-first), AirBrix
- MLflow, Seldon, Lepton AI
- GGUL, GGML, AWQ (research papers + repos)

**Total**: 9 tools requiring GitHub scraping

---

## Estimated Timeline & Resource Requirements

| Phase | Duration | Tools | Person-Hours | Start Date | Completion |
|-------|----------|-------|--------------|-----------|------------|
| Phase 1 | 1 week | 13 Tier 1 | 40-50 | Now | By 2026-01-07 |
| Phase 2 | 1 week | 23 Tier 2 | 35-40 | 2026-01-08 | By 2026-01-14 |
| Phase 3 | 1 week | 24 Tier 3 | 30-35 | 2026-01-15 | By 2026-01-21 |
| Phase 4 | 3-4 days | 5 Tier 4 | 10-15 | 2026-01-22 | By 2026-01-25 |
| **TOTAL** | **4 weeks** | **77 tools** | **115-140** | **Now** | **By 2026-01-25** |

---

## Quality Assurance Checklist

For each tool documented:
- [ ] Official documentation exists and is current (2025 or recent)
- [ ] At least 50KB of substantive content captured
- [ ] Code examples included (if applicable)
- [ ] API reference documented
- [ ] Setup/installation instructions present
- [ ] Architecture/design documentation included
- [ ] Source headers properly attributed
- [ ] No extraction artifacts (JavaScript placeholders, CSS remnants)

---

## Implementation Notes

1. **llms.txt Priority**: Check for llms.txt support on all Tier 1 tools first
2. **Git Extraction**: Use existing repo_config.yaml pattern for GitHub repos
3. **API Documentation**: For cloud services, capture interactive API examples
4. **Rust Documentation**: Use docs.rs where available (auto-generated from crates)
5. **Version Lock**: Document scraping date and tool versions for reproducibility
6. **Deduplication**: Check for overlapping content (e.g., PyTorch in both pytorch.org and GitHub)

---

## Success Criteria

- **Coverage**: 75+ software tools with complete documentation
- **Freshness**: All docs dated 2025 or within 6 months
- **Completeness**: Average 100KB+ per tool
- **Accuracy**: 100% attribution and source tracking
- **Searchability**: All docs properly indexed and discoverable

---

**Document Version**: 1.0
**Last Updated**: 2025-12-31
**Next Review**: After Phase 1 completion (2026-01-07)
