# Faiss + SVS - Overview

Faiss supports Intel [Scalable Vector Search](https://github.com/intel/ScalableVectorSearch) (SVS) indexes. The integration lets you build, query, save, and load SVS indexes with the usual Faiss `Index` API. For end-to-end examples and code snippets, see [Faiss + SVS usage guide](CPU-Faiss---Intel-SVS-‐-Usage).

## Key capabilities at a glance
- **Faiss-native workflow** — SVS indexes have the standard `Index` lifecycle (train/add/search, I/O, factory strings), facilitating the migration of existing code.
- **Graph or flat search** — Use Vamana for high-recall graph-based ANN search or SVS Flat for brute-force baselines, each exposed with the same Faiss abstractions.
- **Intel compression stack** — LVQ and LeanVec operate entirely on compressed vectors, trimming memory while preserving recall when running on Intel CPUs.

## Supported SVS indexes in Faiss
- **SVS Vamana** — Combines the Vamana graph-based search algorithm, introduced by [Subramanya et al.](https://proceedings.neurips.cc/paper_files/paper/2019/file/09853c7fb1d3f8ee67a61b6bf4a7f8e6-Paper.pdf),  with Intel's LVQ and LeanVec compression. It uses a single-layer proximity graph (vs. HNSW’s multi-layer) for efficient search, and supports float32, float16, 8-bit quantization with global scaling, plus Intel-specific compression for low memory footprint and higher throughput.

- **SVS Flat** — A brute-force implementation that streams queries through the SVS runtime. 

## SVS vector compression: LVQ & LeanVec
SVS indexes in Faiss operate on plain float32 vectors out of the box, but they can also leverage Intel's proprietary compression [**Locally-Adaptive Vector Quantization**](https://vldb.org/pvldb/volumes/16/paper/Similarity%20search%20in%20the%20blink%20of%20an%20eye%20with%20compressed%20indices) (LVQ) and [**LeanVec**](https://openreview.net/pdf?id=wczqrpOrIc). Both compressors shrink the dataset footprint to reduce memory usage while preserving accuracy for large-scale vector search. **LVQ and LeanVec are available on Intel CPUs only**.

#### **Locally-Adaptive Vector Quantization (LVQ)**

*   **Method:** Per-vector normalization + scalar quantization.
*   **Benefits:**
    *   Fast, on-the-fly decompression for distance computation.
    *   SIMD-optimized layout ([Turbo LVQ](https://arxiv.org/abs/2402.02044)).
    * Robust to distribution shifts.
*   **Variants:**
    *   **LVQ4x4:** 8 bits/dim, fast search, large memory savings.
    *   **LVQ4x8:** 12 bits/dim, higher recall when needed.
    *   **LVQ4x0:** 4 bits/dim, single-level, maximum memory savings.

#### **LeanVec**

*   **Method:** Query-aware dimensionality reduction + LVQ.
*   **Benefits:**
    *   Ideal for high-dimensional vectors.
    *   Significant memory and performance gains.
*   **Variants:**
    *   **LeanVec4x8:** Best for high-dimensional datasets, fastest search.
    *   **LeanVec4x4:** Larger memory savings.
    *   **LeanVec8x8:** Higher recall when needed.
*   **Optional:** Further reduce dimensions using `leanvec_dim` argument. Default is d//2.


### **Two-Level Compression**

Both LVQ and LeanVec support **two-level schemes**:

*   **Level 1:** Compress vectors for fast candidate retrieval.
*   **Level 2:** Encode residuals for accurate re-ranking.
*   **Full-precision vectors are not used at query time**, search operates entirely on compressed representations.

**Naming Convention:** `<B₁>x<B₂>`

*   **B₁:** Bits per dimension (first level).
*   **B₂:** Bits per dimension (second level).
*   Example: **LVQ4x8** = 4 bits/dim (level 1) + 8 bits/dim (level 2); **LeanVec4x8_256** = 256 dims with 4 bits/dim (level 1) + original dimensionality with 8 bits/dim (level 2).

## Operational notes
- LeanVec requires training on a representative data sample; large distribution drifts may degrade recall.
- LVQ, which uses the global vector average, may also be impacted by distribution shifts but is highly robust. LVQ automatically determines the global vector average from the first batch of added vectors; it does not support explicit training.
- Two-level presets keep all computations in the compressed domain. Float32 vectors are not required at query time.
- LeanVec's out-of-distribution mode will be available soon!

