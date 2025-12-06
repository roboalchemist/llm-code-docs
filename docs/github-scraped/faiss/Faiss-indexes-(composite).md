This page presents more advanced features of Faiss indexes. The best operating points can be obtained by combining several of the indexing methods described in the previous section.

## Cell probe method with a PQ index as coarse quantizer

A product quantizer can also be used as a coarse quantizer. This corresponds to the Multi-Index described in [The inverted multi-index, Babenko & Lempitsky, CVPR'12]. For a PQ with m segments each encoded as c centroids, the number of inverted lists is c^m. Therefore, m=2 is the only practical option.

In Faiss, the corresponding coarse quantizer index is the `MultiIndexQuantizer`. This index is special because no vector is added to it. Therefore a specific flag (`quantizer_trains_alone`) has to be set on the `IndexIVF`.

```python
nbits_mi = 12  # c
M_mi = 2       # m
coarse_quantizer_mi = faiss.MultiIndexQuantizer(d, M_mi, nbits_mi)
ncentroids_mi = 2 ** (M_mi * nbits_mi)

index = faiss.IndexIVFFlat(coarse_quantizer_mi, d, ncentroids_mi)
index.nprobe = 2048
index.quantizer_trains_alone = True
```

The `MultiIndexQuantizer` typically is competitive compared to an `IndexFlat` in fast/low-precision operating points.


## Pre-filtering PQ codes with polysemous codes

It is about 6x faster to compare codes with Hamming distances than to use a product quantizer. However, by a proper reordering of the quantization centroids, the Hamming distances between PQ codes become correlated with the true distances. The by applying a threshold on the Hamming distance, most expensive PQ code comparisons can be avoided.

To enable this on an `IndexPQ`:

```python
index = faiss.IndexPQ (d, 16, 8)
# before training
index.do_polysemous_training = true
index.train (...)

# before searching
index.search_type = faiss.IndexPQ.ST_polysemous
index.polysemous_ht = 54    # the Hamming threshold
index.search (...)
```

For an `IndexIVFPQ`:

```python
index = faiss.IndexIVFPQ (coarse_quantizer, d, 16, 8)
# before training
index. do_polysemous_training = true
index.train (...)

# before searching
index.polysemous_ht = 54 # the Hamming threshold
index.search (...)
```

To set a reasonable threshold, keep in mind that:

- the threshold should be between 0 and the number of bits per code (128 = 16*8 in this case), and  codes follow a binomial distribution

- setting the threshold to 1/2 the number of bits per code will spare 1/2 of the code comparisons, which is not enough. It should be set to a lower value (hence the 54 for 128 bit codes).

Typically, the speed-accuracy tradeoffs that can be obtained for an IndexPQ are in the following blue curve:
<img width="852" height="634" alt="image" src="https://github.com/user-attachments/assets/dfb67ab6-d123-4709-8a1c-eaa74feda980" />


## IndexIVFPQR: refining IVFPQ search results with an additional product quantizer

The `IndexIVFPQR` adds an additional level of quantization (the third!) on top of an IndexIVFPQ. Similar to the IndexRefineFlat It refines the distances computed by an IndexIVFPQ and reorders the results based on these.

## IndexIVFPQFastScan w/ Refine

This is the FastScan version of IVFPQ with refinement. See https://github.com/facebookresearch/faiss/wiki/Fast-accumulation-of-PQ-and-AQ-codes-(FastScan) for more details on FastScan; that page already includes details about Refinement for FastScan.

The difference is that the product-quantized codes in the inverted lists are stored grouped in blocks of size "bbs", making it fast to compute distances with SIMD.


## IndexIVFSpectralHash

IndexIVFSpectralHash is only loosely based on the Spectral Hash paper by _Weiss et al_: https://papers.nips.cc/paper_files/paper/2008/file/d58072be2820e8682c0a27c0518e805e-Paper.pdf

The adaptations are:
1. A first-level IVF (as indicated by the name) which narrows down the search on a subset of inverted lists (just like regular IVF)
2. Then the residual is transformed by a VectorTransform. This can be PCA like in the paper, but there are other supported transforms for versatility.
3. The binarization is done independently on each dimension via periodic function. Usually the period is very large so this binarization is just thresholding. This is similar to equation 4 from the paper, where only the sign is kept. The two parameters of the periodic function are the period (given at index construction time) and the offset (determined at training time using threshold_type).

Other notes:
- The period is infinity in practice. We have not yet found a distribution where it was useful to set it otherwise, but it may exist, so it is configurable.
- This does not subclass IndexBinaryIVF because IndexBinary takes binary vectors as input, and SpectralHash must do the binarization internally. 
- Readers may notice that is quite similar to IndexLSH. The differences are A) The IVF and B) the periodic binarization.
- Training consists of A) Training the VectorTransform, then B) Getting the offset of the periodic function for each dimension.

## Whole class hierarchy 

For the curious, the CPU Faiss class hierarchy looks like this [faiss_class_hierarchy.pdf](./faiss_class_hierarchy.pdf)