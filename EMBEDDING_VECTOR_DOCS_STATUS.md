# Documentation Status: Embedding Models & Vector Search

Current state of embedding and vector search documentation in llm-code-docs repository.

---

## Current Documentation (Already in Repository)

### Vector Search Libraries

#### FAISS (Complete)
- **Location**: `/Users/joe/github/llm-code-docs/docs/github-scraped/faiss/`
- **Source**: Facebook AI Similarity Search GitHub repository
- **Status**: ✅ Complete - All official documentation
- **Coverage**: Indexing strategies, GPU usage, API reference, examples
- **Completeness**: Excellent

### Embedding Models

#### BAAI/Flag Embeddings (Complete)
- **Location**: `/Users/joe/github/llm-code-docs/docs/github-scraped/flagembedding/`
- **Source**: GitHub BAAI/flag-embedding
- **Status**: ✅ Complete
- **Models Covered**: BGE-M3, BGE variants, instruction tuning
- **Documentation**: Model cards, benchmarks, usage examples
- **Completeness**: Excellent

#### Qwen3 Embeddings (Complete)
- **Location**: `/Users/joe/github/llm-code-docs/docs/github-scraped/qwen3-embedding/`
- **Source**: Alibaba Qwen3 Embeddings GitHub
- **Status**: ✅ Complete
- **Model Type**: Chinese/multilingual embeddings
- **Documentation**: Model specifications, API reference
- **Completeness**: Good

### Vector Databases & Related

#### Vespa (Complete)
- **Location**: `/Users/joe/github/llm-code-docs/docs/llms-txt/vespa/`
- **Source**: Yahoo's Vespa documentation site (llms.txt)
- **Status**: ✅ Complete
- **Coverage**:
  - Vector search introduction
  - Paged vectors indexing
  - Vector binarization
  - Hybrid search documentation
- **Completeness**: Excellent

#### pgvector (Complete)
- **Location**: `/Users/joe/github/llm-code-docs/docs/llms-txt/pgvector/`
- **Source**: pgvector GitHub/docs (llms.txt)
- **Status**: ✅ Complete
- **Files**:
  - `pgvector-full.md` (comprehensive guide)
  - Individual feature docs
- **Coverage**: PostgreSQL extension, SQL API, indexing, performance
- **Completeness**: Excellent

#### Qdrant (Partial)
- **Location**: `/Users/joe/github/llm-code-docs/docs/llms-txt/squared-ai/qdrant.md`
- **Source**: Squared AI integration documentation
- **Status**: ⚠️ Limited - Integration guide only, not full Qdrant docs
- **Coverage**: Basic Qdrant integration, not comprehensive API
- **Completeness**: Partial - need full Qdrant documentation

### Embedding Provider APIs

#### Cohere (Not Downloaded)
- **Status**: ⏳ Configured but not downloaded
- **Config Location**: `/Users/joe/github/llm-code-docs/scripts/llms-sites.yaml`
- **Base URL**: https://docs.cohere.com/
- **Action**: Run `python3 scripts/llms-txt-scraper.py --site cohere` to download

### Integration Examples

#### CrewAI Vector Tools (Partial)
- **Location**: `/Users/joe/github/llm-code-docs/docs/llms-txt/crewai/`
- **Files**:
  - `qdrantvectorsearchtool.md` - Qdrant integration
  - `weaviatevectorsearchtool.md` - Weaviate integration
  - `mongodbvectorsearchtool.md` - MongoDB integration
- **Status**: ⚠️ Integration examples, not full library docs
- **Completeness**: Partial - framework integration, not library docs

---

## Missing Documentation (Priority Order)

### Tier 1: Critical (Most Used)

#### Sentence-Transformers
- **Why Critical**: Most popular Python library for embeddings (our recommendation)
- **llms.txt Available**: Yes (https://www.sbert.net/)
- **GitHub Docs**: https://github.com/UKPLab/sentence-transformers
- **Action**: `python3 scripts/llms-txt-scraper.py --site sentence-transformers`
- **Priority**: 🔴 HIGHEST - Foundational library

#### Ollama
- **Why Critical**: Easiest local embedding/LLM platform
- **llms.txt Available**: Check at https://ollama.ai/
- **GitHub Docs**: https://github.com/ollama/ollama
- **Action**: Verify llms.txt, then scrape
- **Priority**: 🔴 HIGHEST - Beginner-friendly entry point

#### OpenAI API (Embeddings)
- **Why Critical**: Industry standard for embedding APIs
- **Docs**: https://platform.openai.com/docs/guides/embeddings
- **Action**: May need custom scraper (not standard llms.txt)
- **Status**: Check if Anthropic docs include OpenAI embeddings
- **Priority**: 🔴 HIGHEST - Market standard

### Tier 2: High Priority (Important)

#### Milvus
- **Why Important**: Top open-source vector database (35k+ stars)
- **llms.txt Available**: Check https://milvus.io/
- **GitHub Docs**: https://github.com/milvus-io/milvus
- **Action**: `python3 scripts/llms-txt-scraper.py --site milvus`
- **Priority**: 🟠 HIGH - Major distributed vector DB

#### Weaviate
- **Why Important**: Popular open-source vector DB with hybrid search
- **llms.txt Available**: Yes (https://weaviate.io/)
- **GitHub Docs**: https://github.com/weaviate/weaviate
- **Action**: `python3 scripts/llms-txt-scraper.py --site weaviate`
- **Priority**: 🟠 HIGH - Enterprise option

#### Qdrant (Full Docs)
- **Why Important**: Modern Rust-based vector DB
- **Current State**: Only CrewAI integration available
- **llms.txt Available**: Yes (https://qdrant.tech/)
- **GitHub Docs**: https://github.com/qdrant/qdrant
- **Action**: `python3 scripts/llms-txt-scraper.py --site qdrant`
- **Priority**: 🟠 HIGH - Need full Qdrant docs, not just integration

#### Hugging Face Transformers (Embeddings Focus)
- **Current State**: General docs exist, but need embeddings-specific
- **llms.txt Available**: https://huggingface.co/
- **Action**: Ensure embeddings section is complete
- **Priority**: 🟠 HIGH - Critical for model selection

### Tier 3: Medium Priority (Valuable)

#### Text Embeddings Inference (TEI)
- **Why Valuable**: HF inference server for embeddings
- **GitHub Docs**: https://github.com/huggingface/text-embeddings-inference
- **Action**: `python3 scripts/llms-txt-scraper.py --site huggingface-inference`
- **Priority**: 🟡 MEDIUM - Production inference

#### Chroma
- **Why Valuable**: Simple, popular vector DB
- **llms.txt Available**: Check https://docs.trychroma.com/
- **GitHub Docs**: https://github.com/chroma-core/chroma
- **Action**: Scrape from llms.txt or GitHub
- **Priority**: 🟡 MEDIUM - RAG-friendly

#### vLLM
- **Why Valuable**: High-performance inference for LLMs + embeddings
- **GitHub Docs**: https://github.com/vllm-project/vllm
- **Action**: Check for llms.txt at https://vllm.readthedocs.io/
- **Priority**: 🟡 MEDIUM - Production serving

#### Pinecone
- **Why Valuable**: Managed vector database (industry standard SaaS)
- **Docs**: https://docs.pinecone.io/
- **Status**: Proprietary, may need custom scraper
- **Action**: Custom scraper or request from Pinecone
- **Priority**: 🟡 MEDIUM - Managed service option

### Tier 4: Lower Priority (Nice to Have)

#### NVIDIA Triton Inference Server
- **Why Valuable**: Multi-framework inference
- **Docs**: https://github.com/triton-inference-server/server
- **Priority**: 🟢 LOW - Advanced deployment

#### hnswlib
- **Why Valuable**: Fastest CPU vector search
- **GitHub Docs**: https://github.com/nmslib/hnswlib
- **Priority**: 🟢 LOW - Performance-focused subset

#### ScaNN (Google)
- **Why Valuable**: Compressed vector search
- **GitHub Docs**: https://github.com/google-research/scann
- **Priority**: 🟢 LOW - Specialized use case

#### FastEmbed
- **Why Valuable**: Lightweight embedding library
- **GitHub Docs**: https://github.com/qdrant/fastembed
- **Priority**: 🟢 LOW - Alternative to Sentence-Transformers

#### DiskANN (Microsoft)
- **Why Valuable**: Disk-based billion-scale search
- **GitHub Docs**: https://github.com/microsoft/DiskANN
- **Priority**: 🟢 LOW - Specialized large-scale

#### PyTorch & TensorFlow
- **Current State**: Probably in repository already
- **Action**: Verify embedding-specific content
- **Priority**: 🟢 LOW - General frameworks

#### Cohere Full Docs
- **Current State**: Configured but not downloaded
- **Action**: Run scraper to download
- **Priority**: 🟢 LOW - Complete provider coverage

---

## Download Strategy

### Phase 1: Immediate (Critical Tools)

```bash
# Download Tier 1 tools
python3 scripts/llms-txt-scraper.py --site sentence-transformers
python3 scripts/llms-txt-scraper.py --site ollama

# Verify OpenAI/Anthropic embedding docs already present
grep -r "text-embedding" docs/
```

### Phase 2: High Priority (Week 1)

```bash
# Download Tier 2 tools
python3 scripts/llms-txt-scraper.py --site milvus
python3 scripts/llms-txt-scraper.py --site weaviate
python3 scripts/llms-txt-scraper.py --site qdrant
python3 scripts/llms-txt-scraper.py --site cohere  # Finish this
python3 scripts/llms-txt-scraper.py --site huggingface-docs  # Verify embedding section
```

### Phase 3: Medium Priority (Week 2)

```bash
# Download Tier 3 tools
python3 scripts/llms-txt-scraper.py --site chroma
python3 scripts/llms-txt-scraper.py --site huggingface-inference  # TEI
python3 scripts/llms-txt-scraper.py --site vllm
```

### Phase 4: Nice to Have (As Time Allows)

```bash
# Download remaining tools
python3 scripts/llms-txt-scraper.py --site triton-inference
python3 scripts/llms-txt-scraper.py --site fastembed
# Others as needed
```

---

## Documentation Quality Checklist

When downloading new docs, verify:

- [ ] **Source Headers**: Files contain `# Source: URL` at top
- [ ] **Code Examples**: For libraries, check `grep -l '```' docs/*/\*.md`
- [ ] **API Reference**: Major APIs documented
- [ ] **Installation**: Setup/install instructions present
- [ ] **Quick Start**: Beginner-friendly examples
- [ ] **Troubleshooting**: Common issues and solutions
- [ ] **File Sizes**: Critical files > 15KB (suggests completeness)
- [ ] **No Artifacts**: Check for broken `javascript:void(0)` or CSS classes

### Quick Verification Commands

```bash
# Check for code examples in a downloaded tool
grep -l '```' docs/llms-txt/TOOLNAME/*.md | wc -l

# Verify source headers
grep -L "^# Source:" docs/llms-txt/TOOLNAME/*.md

# Check file sizes (should have some > 15KB)
ls -lh docs/llms-txt/TOOLNAME/*.md | awk '{print $5, $9}'
```

---

## Integration with llm-code-docs Workflow

### Current Setup
- **llms-sites.yaml**: Configuration for 170+ llms.txt sites
- **llms-txt-scraper.py**: Parallel downloader (15 concurrent workers)
- **extract_docs.py**: Git repository cloner for 15 specific repos
- **Caching**: 23-hour freshness window for efficient updates

### Adding New Sites

To add Sentence-Transformers to the configuration:

```yaml
# Add to scripts/llms-sites.yaml in alphabetical order:
- name: sentence-transformers
  base_url: https://www.sbert.net/
  description: Sentence Transformers - Python library for semantic embeddings
```

Then run:
```bash
python3 scripts/llms-txt-scraper.py --site sentence-transformers
```

### Git-Based Extraction (Alternative)

For tools without good llms.txt support, consider adding to `repo_config.yaml`:

```yaml
- name: sentence-transformers
  repo_url: https://github.com/UKPLab/sentence-transformers.git
  source_folder: docs
  target_folder: docs/github-scraped/sentence-transformers
  branch: main
```

Then run:
```bash
python3 scripts/extract_docs.py
```

---

## Recommended Next Steps

1. **This Week**:
   - Download Sentence-Transformers documentation
   - Verify Ollama llms.txt availability
   - Download full Qdrant docs (replace CrewAI snippet)

2. **Next Week**:
   - Download Milvus, Weaviate, Chroma
   - Verify OpenAI/Cohere embedding docs completeness
   - Test all download scripts

3. **Quality Assurance**:
   - Run verification commands on all new downloads
   - Check for broken links or missing sections
   - Update EMBEDDING_VECTOR_RESEARCH.md with direct links

4. **Integration**:
   - Update AGENTS.md with embedding/vector search guidance
   - Add to llm-code-docs README
   - Create index/navigation for the new docs

---

## Current Repository Statistics

**Before Downloads**:
- Embedding libraries with docs: 2 (Flag Embeddings, Qwen3)
- Vector search libraries: 1 (FAISS)
- Vector databases: 2 (Vespa, pgvector)
- Embedding APIs: 0 (Cohere configured but not downloaded)
- Total embedding/vector docs: ~5 directories

**After Phase 1 & 2 Downloads** (estimated):
- Embedding libraries: +3 (Sentence-Transformers, Ollama, TEI)
- Vector databases: +3 (Milvus, Weaviate, Qdrant full docs)
- Embedding APIs: +1 (Cohere)
- Total new docs: ~50MB+ from 8+ major tools
- Total documents: 1000+ markdown files

---

## Notes

- Some tools (Pinecone) are SaaS and may not have publicly available llms.txt
- Custom web scrapers may be needed for some providers
- Consider reaching out to projects without llms.txt files to suggest adoption
- Prioritize tools by GitHub stars, citations, and community usage

---

**Last Updated**: December 31, 2025
**Repository**: /Users/joe/github/llm-code-docs
**Status**: Ready for Phase 1 downloads
**Estimated Time**: Phase 1 (1-2 hours), Phase 2 (2-3 hours), Phase 3 (1-2 hours)
