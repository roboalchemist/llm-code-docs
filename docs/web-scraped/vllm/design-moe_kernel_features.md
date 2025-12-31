# Source: https://docs.vllm.ai/en/stable/design/moe_kernel_features/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/design/moe_kernel_features.md "Edit this page")

# Fused MoE Kernel Features[¶](#fused-moe-kernel-features "Permanent link")

The purpose of this document is to provide an overview of the various MoE kernels (both modular and non-modular) so it will be easier to select an appropriate set of kernels for any particular situation. This includes information about the all2all backends used by modular kernels.

## Fused MoE Modular All2All backends[¶](#fused-moe-modular-all2all-backends "Permanent link")

There are a number of all2all communication backends that are used to implement expert parallelism (EP) for the `FusedMoE` layer. The different `FusedMoEPrepareAndFinalize` subclasses provide an interface for each all2all backend.

The following table describes the relevant features of each backend, i.e. activation format, supported quantization schemes and async support.

The output activation format (standard or batched) corresponds to the output of the prepare step of the `FusedMoEPrepareAndFinalize` subclass, and the finalize step requires the same format. All the backend `prepare` methods expect activations in the standard format and all the `finalize` methods return activations in standard format. More details on the formats can be found in the [Fused MoE Modular Kernel](../fused_moe_modular_kernel/) document.

The quantization types and formats enumerate which quantization schemes are supported by each `FusedMoEPrepareAndFinalize` class. The quantization can happen before or after the dispatch based on the format the all2all backend supports, e.g. deepep_high_throughput supports only block-quantized fp8 format. Any other format will result in dispatching in higher precision and quantizing afterwards. The output of the prepare step for each backend is the quantized type. The finalize step generally requires the same input type as the original activations, e.g. if the original input is bfloat16 and the quantization scheme is fp8 with per-tensor scales, `prepare` will return fp8/per-tensor scale activations and `finalize` will take bfloat16 activations. See the diagrams in [Fused MoE Modular Kernel](../fused_moe_modular_kernel/) for more details on the types and formats of activations at each step of the MoE process. If no quantization type is specified, the kernel operates on float16 and/or bfloat16.

Async backends support the use of DBO (Dual Batch Overlap) and shared expert overlap (where shared experts are computed during the combine step).

Certain models require the topk weights to be applied to the input activations rather than the output activations when topk==1, e.g. Llama. For modular kernels, this feature is supported by the `FusedMoEPrepareAndFinalize` subclass. For non-modular kernels, it is up to the experts function to deal with this flag.

Unless otherwise specified, backends are controlled via `VLLM_ALL2ALL_BACKEND`. All backends except `flashinfer` only work with EP+DP or EP+TP. `Flashinfer` can work with EP or DP without EP.

  Backend                        Output act. format   Quant. types   Quant. format   Async   Apply Weight On Input   Subclass
  ------------------------------ -------------------- -------------- --------------- ------- ----------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  naive                          standard             all^1^         G,A,T           N       ^6^                     [layer.py](../../api/vllm/model_executor/layers/fused_moe/layer/#vllm.model_executor.layers.fused_moe.layer.FusedMoE.forward_impl "            forward_impl")
  pplx                           batched              fp8,int8       G,A,T           Y       Y                       [`PplxPrepareAndFinalize`](../../api/vllm/model_executor/layers/fused_moe/pplx_prepare_finalize/#vllm.model_executor.layers.fused_moe.pplx_prepare_finalize.PplxPrepareAndFinalize "            PplxPrepareAndFinalize")
  deepep_high_throughput         standard             fp8            G(128),A,T^2^   Y       Y                       [`DeepEPLLPrepareAndFinalize`](../../api/vllm/model_executor/layers/fused_moe/deepep_ll_prepare_finalize/#vllm.model_executor.layers.fused_moe.deepep_ll_prepare_finalize.DeepEPLLPrepareAndFinalize "            DeepEPLLPrepareAndFinalize")
  deepep_low_latency             batched              fp8            G(128),A,T^3^   Y       Y                       [`DeepEPHTPrepareAndFinalize`](../../api/vllm/model_executor/layers/fused_moe/deepep_ht_prepare_finalize/#vllm.model_executor.layers.fused_moe.deepep_ht_prepare_finalize.DeepEPHTPrepareAndFinalize "            DeepEPHTPrepareAndFinalize")
  flashinfer_all2allv            standard             nvfp4,fp8      G,A,T           N       N                       [`FlashInferAllToAllMoEPrepareAndFinalize`](../../api/vllm/model_executor/layers/fused_moe/flashinfer_cutlass_prepare_finalize/#vllm.model_executor.layers.fused_moe.flashinfer_cutlass_prepare_finalize.FlashInferAllToAllMoEPrepareAndFinalize "            FlashInferAllToAllMoEPrepareAndFinalize")
  flashinfer^4^                  standard             nvfp4,fp8      G,A,T           N       N                       [`FlashInferCutlassMoEPrepareAndFinalize`](../../api/vllm/model_executor/layers/fused_moe/flashinfer_cutlass_prepare_finalize/#vllm.model_executor.layers.fused_moe.flashinfer_cutlass_prepare_finalize.FlashInferCutlassMoEPrepareAndFinalize "            FlashInferCutlassMoEPrepareAndFinalize")
  MoEPrepareAndFinalizeNoEP^5^   standard             fp8,int8       G,A,T           N       Y                       [`MoEPrepareAndFinalizeNoEP`](../../api/vllm/model_executor/layers/fused_moe/prepare_finalize/#vllm.model_executor.layers.fused_moe.prepare_finalize.MoEPrepareAndFinalizeNoEP "            MoEPrepareAndFinalizeNoEP")
  BatchedPrepareAndFinalize^5^   batched              fp8,int8       G,A,T           N       Y                       [`BatchedPrepareAndFinalize`](../../api/vllm/model_executor/layers/fused_moe/fused_batched_moe/#vllm.model_executor.layers.fused_moe.fused_batched_moe.BatchedPrepareAndFinalize "            BatchedPrepareAndFinalize")

Table key

1.  All types: mxfp4, nvfp4, int4, int8, fp8
2.  A,T quantization occurs after dispatch.
3.  All quantization happens after dispatch.
4.  Controlled by different env vars (`VLLM_FLASHINFER_MOE_BACKEND` \"throughput\" or \"latency\")
5.  This is a no-op dispatcher that can be used to pair with any modular experts to produce a modular kernel that runs without dispatch or combine. These cannot be selected via environment variable. These are generally use for testing or adapting an expert subclass to the `fused_experts` API.
6.  This depends on the experts implementation.

------------------------------------------------------------------------

-   G - Grouped
-   G(N) - Grouped w/block size N
-   A - Per activation token
-   T - Per tensor

Modular kernels are supported by the following `FusedMoEMethodBase` classes.

-   [`ModelOptFp8MoEMethod`](../../api/vllm/model_executor/layers/quantization/modelopt/#vllm.model_executor.layers.quantization.modelopt.ModelOptFp8MoEMethod "            ModelOptFp8MoEMethod")
-   [`Fp8MoEMethod`](../../api/vllm/model_executor/layers/quantization/fp8/#vllm.model_executor.layers.quantization.fp8.Fp8MoEMethod "            Fp8MoEMethod")
-   [`CompressedTensorsW4A4Nvfp4MoEMethod`](../../api/vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/#vllm.model_executor.layers.quantization.compressed_tensors.compressed_tensors_moe.CompressedTensorsW4A4Nvfp4MoEMethod "            CompressedTensorsW4A4Nvfp4MoEMethod")
-   [`CompressedTensorsW8A8Fp8MoEMethod`](../../api/vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/#vllm.model_executor.layers.quantization.compressed_tensors.compressed_tensors_moe.CompressedTensorsW8A8Fp8MoEMethod "            CompressedTensorsW8A8Fp8MoEMethod")
-   [`Mxfp4MoEMethod`](../../api/vllm/model_executor/layers/quantization/mxfp4/#vllm.model_executor.layers.quantization.mxfp4.Mxfp4MoEMethod "            Mxfp4MoEMethod")
-   [`UnquantizedFusedMoEMethod`](../../api/vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method/#vllm.model_executor.layers.fused_moe.unquantized_fused_moe_method.UnquantizedFusedMoEMethod "            UnquantizedFusedMoEMethod")

## Fused Experts Kernels[¶](#fused-experts-kernels "Permanent link")

There are a number of MoE experts kernel implementations for different quantization types and architectures. Most follow the general API of the base Triton [`fused_experts`](../../api/vllm/model_executor/layers/fused_moe/fused_moe/#vllm.model_executor.layers.fused_moe.fused_moe.fused_experts "            fused_experts") function. Many have modular kernel adapters, so they can be used with compatible all2all backends. This table lists each experts kernel and its particular properties.

Each kernel must be provided with one of the supported input activation formats. Some flavors of kernels support both standard and batched formats through different entry points, e.g. `TritonExperts` and `BatchedTritonExperts`. Batched format kernels are currently only needed for matching with certain all2all backends, e.g. `pplx` and `DeepEPLLPrepareAndFinalize`.

Similar to the backend kernels, each experts kernel only supports certain quantization formats. For non-modular experts, the activations will be in the original type and quantized internally by the kernel. Modular experts will expect the activations to already be in the quantized format. Both types of experts will yield outputs in the original activation type.

Each experts kernel supports one or more activation functions, e.g. silu or gelu, which are applied to the intermediate results.

As with the backends, some experts support applying topk weights on the input activations. The entries in the column in this table only apply to the non-modular experts.

Most experts flavors include an equivalent modular interface which will be a subclass of `FusedMoEPermuteExpertsUnpermute`.

To be used with a particular `FusedMoEPrepareAndFinalize` subclass, MoE kernels must have compatible activation formats, quantization types and quantization formats.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Kernel             Input act. format   Quant. types   Quant. format   Activation function   Apply Weight On Input   Modular   Source
  ------------------ ------------------- -------------- --------------- --------------------- ----------------------- --------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  triton             standard            all^1^         G,A,T           silu, gelu,\          Y                       Y         [`fused_experts`](../../api/vllm/model_executor/layers/fused_moe/fused_moe/#vllm.model_executor.layers.fused_moe.fused_moe.fused_experts "            fused_experts"),\
                                                                        swigluoai,\                                             [`TritonExperts`](../../api/vllm/model_executor/layers/fused_moe/fused_moe/#vllm.model_executor.layers.fused_moe.fused_moe.TritonExperts "            TritonExperts")
                                                                        silu_no_mul,\                                           
                                                                        gelu_no_mul                                             

  triton (batched)   batched             all^1^         G,A,T           silu, gelu            ^6^                     Y         [`BatchedTritonExperts`](../../api/vllm/model_executor/layers/fused_moe/fused_batched_moe/#vllm.model_executor.layers.fused_moe.fused_batched_moe.BatchedTritonExperts "            BatchedTritonExperts")

  deep gemm          standard,\          fp8            G(128),A,T      silu, gelu            ^6^                     Y         [`deep_gemm_moe_fp8`](../../api/vllm/model_executor/layers/fused_moe/deep_gemm_moe/#vllm.model_executor.layers.fused_moe.deep_gemm_moe.deep_gemm_moe_fp8 "            deep_gemm_moe_fp8"),\
                     batched                                                                                                    [`DeepGemmExperts`](../../api/vllm/model_executor/layers/fused_moe/deep_gemm_moe/#vllm.model_executor.layers.fused_moe.deep_gemm_moe.DeepGemmExperts "            DeepGemmExperts"),\
                                                                                                                                [`BatchedDeepGemmExperts`](../../api/vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe/#vllm.model_executor.layers.fused_moe.batched_deep_gemm_moe.BatchedDeepGemmExperts "            BatchedDeepGemmExperts")

  cutlass_fp4        standard,\          nvfp4          A,T             silu                  Y                       Y         [`cutlass_moe_fp4`](../../api/vllm/model_executor/layers/fused_moe/cutlass_moe/#vllm.model_executor.layers.fused_moe.cutlass_moe.cutlass_moe_fp4 "            cutlass_moe_fp4"),\
                     batched                                                                                                    [`CutlassExpertsFp4`](../../api/vllm/model_executor/layers/fused_moe/cutlass_moe/#vllm.model_executor.layers.fused_moe.cutlass_moe.CutlassExpertsFp4 "            CutlassExpertsFp4")

  cutlass_fp8        standard,\          fp8            A,T             silu, gelu            Y                       Y         [`cutlass_moe_fp8`](../../api/vllm/model_executor/layers/fused_moe/cutlass_moe/#vllm.model_executor.layers.fused_moe.cutlass_moe.cutlass_moe_fp8 "            cutlass_moe_fp8"),\
                     batched                                                                                                    [`CutlassExpertsFp8`](../../api/vllm/model_executor/layers/fused_moe/cutlass_moe/#vllm.model_executor.layers.fused_moe.cutlass_moe.CutlassExpertsFp8 "            CutlassExpertsFp8"),\
                                                                                                                                [`CutlasBatchedExpertsFp8`](../../api/vllm/model_executor/layers/fused_moe/cutlass_moe/#vllm.model_executor.layers.fused_moe.cutlass_moe.CutlassBatchedExpertsFp8 "            CutlassBatchedExpertsFp8")

  flashinfer         standard            nvfp4,\        T               ^5^                   N                       Y         [`flashinfer_cutlass_moe_fp4`](../../api/vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe/#vllm.model_executor.layers.fused_moe.flashinfer_cutlass_moe.flashinfer_cutlass_moe_fp4 "            flashinfer_cutlass_moe_fp4"),\
                                         fp8                                                                                    [`FlashInferExperts`](../../api/vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe/#vllm.model_executor.layers.fused_moe.flashinfer_cutlass_moe.FlashInferExperts "            FlashInferExperts")

  gpt oss triton     standard            N/A            N/A             ^5^                   Y                       Y         [`triton_kernel_fused_experts`](../../api/vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe/#vllm.model_executor.layers.fused_moe.gpt_oss_triton_kernels_moe.triton_kernel_fused_experts "            triton_kernel_fused_experts"),\
                                                                                                                                [`OAITritonExperts`](../../api/vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe/#vllm.model_executor.layers.fused_moe.gpt_oss_triton_kernels_moe.OAITritonExperts "            OAITritonExperts")

  marlin             standard,\          ^3^ / N/A      ^3^ / N/A       silu,\                Y                       Y         [`fused_marlin_moe`](../../api/vllm/model_executor/layers/fused_moe/fused_marlin_moe/#vllm.model_executor.layers.fused_moe.fused_marlin_moe.fused_marlin_moe "            fused_marlin_moe"),\
                     batched                                            swigluoai                                               [`MarlinExperts`](../../api/vllm/model_executor/layers/fused_moe/fused_marlin_moe/#vllm.model_executor.layers.fused_moe.fused_marlin_moe.MarlinExperts "            MarlinExperts"),\
                                                                                                                                [`BatchedMarlinExperts`](../../api/vllm/model_executor/layers/fused_moe/fused_marlin_moe/#vllm.model_executor.layers.fused_moe.fused_marlin_moe.BatchedMarlinExperts "            BatchedMarlinExperts")

  trtllm             standard            mxfp4,\        G(16),G(32)     ^5^                   N                       Y         [`TrtLlmGenExperts`](../../api/vllm/model_executor/layers/fused_moe/trtllm_moe/#vllm.model_executor.layers.fused_moe.trtllm_moe.TrtLlmGenExperts "            TrtLlmGenExperts")
                                         nvfp4                                                                                  

  pallas             standard            N/A            N/A             silu                  N                       N         [`fused_moe`](../../api/vllm/model_executor/layers/fused_moe/moe_pallas/#vllm.model_executor.layers.fused_moe.moe_pallas.fused_moe "            fused_moe")

  iterative          standard            N/A            N/A             silu                  N                       N         [`fused_moe`](../../api/vllm/model_executor/layers/fused_moe/moe_torch_iterative/#vllm.model_executor.layers.fused_moe.moe_torch_iterative.fused_moe "            fused_moe")

  rocm aiter moe     standard            fp8            G(128),A,T      silu, gelu            Y                       N         [`rocm_aiter_fused_experts`](../../api/vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe/#vllm.model_executor.layers.fused_moe.rocm_aiter_fused_moe.rocm_aiter_fused_experts "            rocm_aiter_fused_experts")

  cpu_fused_moe      standard            N/A            N/A             silu                  N                       N         [`CPUFusedMOE`](../../api/vllm/model_executor/layers/fused_moe/cpu_fused_moe/#vllm.model_executor.layers.fused_moe.cpu_fused_moe.CPUFusedMOE "            CPUFusedMOE")

  naive batched^4^   batched             int8,\         G,A,T           silu, gelu            ^6^                     Y         [`NaiveBatchedExperts`](../../api/vllm/model_executor/layers/fused_moe/fused_batched_moe/#vllm.model_executor.layers.fused_moe.fused_batched_moe.NaiveBatchedExperts "            NaiveBatchedExperts")
                                         fp8                                                                                    
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Table key

1.  All types: mxfp4, nvfp4, int4, int8, fp8
2.  A dispatcher wrapper around triton and deep gemm experts. Will select based on type + shape + quantization params
3.  uint4, uint8, fp8, fp4
4.  This is a naive implementation of experts that supports batched format. Mainly used for testing.
5.  The `activation` parameter is ignored and SwiGlu is used by default instead.
6.  Only handled by or supported when used with modular kernels.

## Modular Kernel \"families\"[¶](#modular-kernel-families "Permanent link")

The following table shows \"families\" of modular kernels that are intended to work together. There are some combinations which may work but have not yet been tested, e.g. flashinfer with other fp8 experts. Note that the \"naive\" backend will work with any non-modular experts.

  ------------------------------------------------------------------------------------------------------------------
  backend                  `FusedMoEPrepareAndFinalize` subclasses    `FusedMoEPermuteExpertsUnpermute` subclasses
  ------------------------ ------------------------------------------ ----------------------------------------------
  deepep_high_throughput   `DeepEPHTPrepareAndFinalize`               `DeepGemmExperts`,\
                                                                      `TritonExperts`,\
                                                                      `TritonOrDeepGemmExperts`,\
                                                                      `CutlassExpertsFp8`,\
                                                                      `MarlinExperts`

  deepep_low_latency,\     `DeepEPLLPrepareAndFinalize`,\             `BatchedDeepGemmExperts`,\
  pplx                     `PplxPrepareAndFinalize`                   `BatchedTritonExperts`,\
                                                                      `CutlassBatchedExpertsFp8`,\
                                                                      `BatchedMarlinExperts`

  flashinfer               `FlashInferCutlassMoEPrepareAndFinalize`   `FlashInferExperts`
  ------------------------------------------------------------------------------------------------------------------

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 3, 2025] ]