## cuVS Overview 

[cuVS](https://github.com/rapidsai/cuvs) contains state-of-the-art implementations of several algorithms for running approximate nearest neighbors and clustering on the GPU. The primary goal of cuVS is to simplify the use of GPUs for vector similarity search and clustering. cuVS is built on top of the [RAPIDS RAFT](https://github.com/rapidsai/raft) library of high performance machine learning primitives.

## Implemented Indexes

cuVS has been integrated into Faiss, so that users have the ability to choose between classic and cuVS implementations for the supported algorithms. The GPU indexes - ```GpuIndexFlat```, ```GpuIndexIVFFlat``` and ```GpuIndexIVFPQ``` can use cuVS implementations. In addition, the graph-based [CAGRA](https://arxiv.org/pdf/2308.15136) index has been added to Faiss for faster search at high recall levels through the ```GpuIndexCagra``` index type.

### CAGRA

[CAGRA](https://arxiv.org/pdf/2308.15136), or (C)UDA (A)NN (GRA)ph-based, is a new graph-based index supported in Faiss through cuVS. It is based loosely on the popular navigable small-world graph (NSG) algorithm, but which has been built from the ground-up specifically for the GPU. CAGRA constructs a flat graph representation by first building a kNN graph of the training points and then removing redundant paths between neighbors.

The CAGRA algorithm has two basic steps:
1. Construct a kNN graph
2. Prune redundant routes from the kNN graph.

cuVS provides IVF-PQ and NN-Descent strategies for building the initial kNN graph and these can be selected in index params object during index construction. A cuVS CAGRA index can be built through Faiss and serialized to a CPU HNSW index, thereby benefitting users with faster GPU graph build for HNSW indexes. More details on this are in the next chapter.

## Improvements over Classic Faiss GPU indexes

* Relaxed parameter settings for `GpuIndexIVFPQ`:
  * The number of subquantizers representing a vector can be any value less than or equal to the base dimension of the dataset, whereas classic IVF-PQ indexes have fixed values up to 96 subquantizers to choose from.
  * `GpuIndexIVFPQ` indexes with 64 bytes per code or more do not require the use of the float16 lookup tables for residual distances.
  * cuVS allows for the number of bits per code to be in the closed interval `[4, 8]`, whereas classic Faiss GPU indexes only support 8 bits per PQ code.
* The use of RMM allows for automatic temporary memory allocations with pooled memory resources and gives users more control over how memory is allocated.
* Performance: cuVS indexes are highly optimized with faster index build times.
* New algorithms such as CAGRA are made available through the integration.

## Limitations

* multi-GPU is not supported for cuVS indexes.
* precomputed tables are not supported for GpuIndexIVFPQ built with cuVS.
* Pre-allocation using `reserveVecs` on a `GpuIndexIVFPQ` or `GpuIndexIVFFlat` is not supported for cuVS indexes.
* `searchPreassigned` to find nearest neighbors for IVF indexes with pre-assigned centroids is not supported for cuVS indexes.
* `indexes_64_BIT` is the only storage option for indexes available for cuVS indexes.
* Building from source: Building Faiss from source with cuVS enabled is slower.