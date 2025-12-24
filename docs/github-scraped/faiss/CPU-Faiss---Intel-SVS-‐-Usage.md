# Faiss + SVS - Usage

This guide shows how to instantiate, configure, and query SVS indices and how to enable LVQ/LeanVec compression in Faiss. To build Faiss with SVS support, see [Building with Intel SVS](https://github.com/facebookresearch/faiss/blob/main/INSTALL.md#building-with-intelr-svs).

SVS indexes behave as any other Faiss index.

In Python

```python
graph_max_degree = 32
index = faiss.IndexSVSVamana(d, graph_max_degree) # build the index (DynamicVamana, float32)

print(index.is_trained)        # no training necessary
index.add(xb)                  # add vectors to the index
print(index.ntotal)

k = 4                          # we want to see 4 nearest neighbors
D, I = index.search(xq, k)  
```

SVS indices are available through the index factory as well:
```python
# example of using factory for SVS Vamana uncompressed
index = faiss.index_factory(d, 'SVSVamana32', faiss.METRIC_L2)           
index.add(xb)
index.search(xq, k)
```

In C++

```
auto graph_max_degree = 32;
faiss::IndexSVSVamana index(d, graph_max_degree);
index.add(nb, xb);
index.search(nq, xq, k, D, I);
```

## Enabling vector compression: LVQ and LeanVec

The following examples show how to use the SVS Vamana index with LVQ and LeanVec vector compression. **These are enabled on Intel CPUs only**.

```python
# LVQ
lvq_idx = faiss.IndexSVSVamanaLVQ(d, graph_max_degree, faiss.METRIC_L2, faiss.SVS_LVQ4x8)  
lvq_idx.add(xb)
lvq_idx.search(xq, k)
```

```python
# LeanVec
leanvec_dims = 128  # Target reduced dimensionality, set to 0 for default d//2; must be < d
leanvec_idx = faiss.IndexSVSVamanaLeanVec(d, graph_max_degree, faiss.METRIC_L2, leanvec_dims, faiss.SVS_LeanVec4x8)
leanvec_idx.train(xb)  # must train on representative sample of vectors
leanvec_idx.add(xb)
leanvec_idx.search(xq, k)

```

Note that the **index needs to be trained** when using LeanVec compression.


Same examples using the index factory:

```python
# example of using index factory for SVS Vamana with LVQ compression
lvq_idx = faiss.index_factory(d, 'SVSVamana32,LVQ4x4', faiss.METRIC_L2)           

# example of using index factory for SVS Vamana LeanVec, default leanvec_dims = d//2
leanvec_idx = faiss.index_factory(d, 'SVSVamana32,LeanVec4x8', faiss.METRIC_L2)     

# example of using index factory for SVS Vamana LeanVec with leanvec_dims = 128
leanvec_idx2 = faiss.index_factory(d, 'SVSVamana32,LeanVec4x8_128', faiss.METRIC_L2) 
```

In C++

```c++
// LVQ
faiss::IndexSVSVamanaLVQ index(d, graph_max_degree, faiss::METRIC_L2, faiss::SVSStorageKind::SVS_LVQ4x4);
index.add(nb, xb);
index.search(nq, xq, k, D, I);
```

```c++
// LeanVec
auto leanvec_dims = 128;
faiss::IndexSVSVamanaLeanVec index(d, graph_max_degree, faiss::METRIC_L2,leanvec_dims, faiss::SVSStorageKind::SVS_LeanVec4x8);
index.train(nb, xb);
index.add(nb, xb);
index.search(nq, xq, k, D, I);
```


See [Faiss + SVS Overview](CPU-Faiss---Intel-SVS-‐-Overview) for the LVQ and LeanVec available configurations.