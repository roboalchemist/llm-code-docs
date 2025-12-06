## Usage

The `use_cuvs=True` flag in GPU index configurations can be used to enable cuVS imeplementations for an index. Note that this flag is automatically set to True for supported index types if `FAISS_ENABLE_CUVS=ON` is set while building Faiss from source or with the `faiss-gpu-cuvs` conda package. If `use_cuvs=False`, the classic Faiss GPU implementations are used.

### Building a cuVS GPU index

#### RMM

cuVS internally uses [Rapids Memory Manager (RMM)](https://github.com/facebookresearch/faiss/blob/master/faiss/gpu/GpuClonerOptions.h) to allow customizing device and host memory allocation patterns. With cuVS enabled, Faiss' GPU resource manager is also configured to use RMM. The following example shows how to construct a best fit pool allocator with an initial size of 1 GiB. The pool uses `rmm::mr::cuda_memory_resource` as its “upstream” resource for pure device allocations.

#### In C++:
```
#include <rmm/mr/device/device_memory_resource.hpp>
#include<rmm/mr/per_device_resource.hpp>
// Set pool memory resource for the current device with 1 GiB initial pool size. All allocations use the same pool.
rmm::mr::pool_memory_resource<rmm::mr::device_memory_resource> pool_mr(
rmm::mr::get_current_device_resource(), 1024 * 1024 * 1024ull);
rmm::mr::set_current_device_resource(&pool_mr);
```

#### In Python:
```
import rmm
pool = rmm.mr.PoolMemoryResource(rmm.mr.CudaMemoryResource(),
                                 initial_pool_size=2 ** 30)
# Set the RMM resource for the current device
rmm.mr.set_per_device_resource(pool)
# Or set the RMM resource for a particular device
rmm.mr.set_per_device_resource(0, pool)
```

In a cuVS enabled build, the StandardGpuResources object uses the current RMM device resource set by the user to do device allocations.

Note: RMM's Python interface is not a direct dependency of Faiss and must be installed externally:
```
conda install -c rapidsai -c conda-forge rmm
```

Setting such an allocator for the device typically yields better search performance than using the default CUDA memory resource. The next step is to set the `use_cuvs` flag to `True` in the index configuration.

#### In C++: 
```
faiss::gpu::StandardGpuResources res;
faiss::gpu::GpuIndexIVFFlatConfig config;
config.use_cuvs = true;
faiss::gpu::GpuIndexIVFFlat index_gpu =
    faiss::gpu::GpuIndexIVFFlat(res, d, nlist, faiss::METRIC_L2, config);
```

#### In Python:
```
res = faiss.StandardGpuResources()
co = faiss.GpuIndexIVFFlatConfig()
co.use_cuvs = True
index_gpu = faiss.GpuIndexIVFFlat(res, ncols, nlist, faiss.METRIC_L2, co)
```
Once the index has been initialized with this config, all supported operations on the index, such as `add` and `search` can be done using regular GPU Faiss function calls. They are internally applied to the underlying cuVS index.
```
index_gpu.add(xb)
D, I = index.search(xq, k)
```

### Cloning a CPU index
The same `use_cuvs` flag exists for cloning a CPU index to a cuVS index.
#### In C++:
```
faiss::gpu::GpuClonerOptions co;
co.use_cuvs = true;
index_gpu = faiss.GpuIndexIVFFlat(res, ncols, nlist, faiss.METRIC_L2, co)
index_gpu = faiss::gpu::index_cpu_to_gpu(
                res,
                0,
                &index_cpu,
                &co);
```
#### In Python:
```
co = faiss.GpuClonerOptions()
co.use_cuvs = True
index_gpu = faiss.index_cpu_to_gpu(res, 0, index_cpu, co)
```

### CAGRA + HNSW
In addition to faster search times on the GPU for a CAGRA index, a `GpuIndexCagra` object can be cloned to initialize the base layer of a CPU HNSW index. This is done via the `IndexHNSWCagra` class. Thus building an HNSW index can be accelerated on the GPU using faster CAGRA index build times.`IndexHNSWCagra` has a parameter called `base_level_only`. If `base_level_only=True`, only the base layer of the HNSW index is initialized from the CAGRA graph. The resultant HNSW index is immutable and does not support adding new vectors after the original graph has been built. If `base_level_only=False`, the CAGRA index is still used to initialize the base layer of the HNSW index, but new vectors can be added to the index using the HNSW `add` API.
```
faiss::gpu::GpuIndexCagra gpu_cagra_index(res, d);
// For the CAGRA index, the `train` stage is used for building a graph with all the vectors.
gpu_cagra_index.train(n, xb);
faiss::IndexHNSWCagra* cpu_hnsw_index;
// Additional vectors can be added to the index if `base_level_only` is set to `false` for the
// HNSW index.
cpu_hnsw_index->base_level_only = false;
// Initialize the HNSW index from the CAGRA graph.
gpu_cagra_index.copyTo(cpu_hnsw_index);
// By now, the HNSW index has all the vectors from the original CAGRA index. And it also has the
// ability to add new vectors.
cpu_hnsw_index->add(n, newVecs);
```