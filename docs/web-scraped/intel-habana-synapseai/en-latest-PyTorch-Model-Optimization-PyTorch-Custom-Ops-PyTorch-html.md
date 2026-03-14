# Source: https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html

Title: Fused Optimizers and Custom Ops for Intel Gaudi — Gaudi Documentation 1.23.0 documentation

URL Source: https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html

Markdown Content:
Fused Optimizers and Custom Ops for Intel Gaudi — Gaudi Documentation 1.23.0 documentation
===============
- [x] 

Toggle navigation sidebar

 - [x] 

Toggle in-page Table of Contents

 

[![Image 1: logo](https://docs.habana.ai/en/latest/_static/Intel_gaudi_logo.png) Gaudi Documentation 1.23.0 documentation ========================================](https://docs.habana.ai/en/latest/index.html)

*   [Welcome to Intel® Gaudi® v1.23 Documentation](https://docs.habana.ai/en/latest/index.html)

Getting Started

*   [Gaudi Architecture and Software Overview](https://docs.habana.ai/en/latest/Gaudi_Overview/index.html)- [x] 
    *   [Gaudi Architecture](https://docs.habana.ai/en/latest/Gaudi_Overview/Gaudi_Architecture.html)
    *   [Intel Gaudi Software Suite](https://docs.habana.ai/en/latest/Gaudi_Overview/Intel_Gaudi_Software_Suite.html)

*   [Support Matrix](https://docs.habana.ai/en/latest/Support_Matrix/Support_Matrix.html)
*   [Release Notes](https://docs.habana.ai/en/latest/Release_Notes/GAUDI_Release_Notes.html)
*   [Installation](https://docs.habana.ai/en/latest/Installation_Guide/index.html)- [x] 
    *   [Hardware and Network Requirements](https://docs.habana.ai/en/latest/Installation_Guide/Platform_Readiness.html)
    *   [Driver and Software Installation](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html)
    *   [Firmware Upgrade and Platform Level Components](https://docs.habana.ai/en/latest/Installation_Guide/Firmware_and_Platform_Components/index.html)- [x] 
        *   [Firmware Upgrade](https://docs.habana.ai/en/latest/Installation_Guide/Firmware_and_Platform_Components/Firmware_Upgrade.html)
        *   [HL-325 In-Band (IB) CPLD Programming](https://docs.habana.ai/en/latest/Installation_Guide/Firmware_and_Platform_Components/HL325_InBand_CPLD_Programming.html)
        *   [HL-338 In-Band (IB) CPLD Programming](https://docs.habana.ai/en/latest/Installation_Guide/Firmware_and_Platform_Components/HL338_InBand_CPLD_Programming.html)

    *   [Additional Installation](https://docs.habana.ai/en/latest/Installation_Guide/Additional_Installation/index.html)- [x] 
        *   [Bare Metal Installation](https://docs.habana.ai/en/latest/Installation_Guide/Additional_Installation/Bare_Metal_Installation.html)
        *   [Docker Installation](https://docs.habana.ai/en/latest/Installation_Guide/Additional_Installation/Docker_Installation.html)
        *   [Kubernetes Installation](https://docs.habana.ai/en/latest/Installation_Guide/Additional_Installation/Kubernetes_Installation/index.html)- [x] 
            *   [Intel Gaudi Base Operator for Kubernetes](https://docs.habana.ai/en/latest/Installation_Guide/Additional_Installation/Kubernetes_Installation/Kubernetes_Operator.html)
            *   [Intel Gaudi Device Plugin for Kubernetes](https://docs.habana.ai/en/latest/Installation_Guide/Additional_Installation/Kubernetes_Installation/Intel_Gaudi_Kubernetes_Device_Plugin.html)

        *   [OpenShift Installation](https://docs.habana.ai/en/latest/Installation_Guide/Additional_Installation/OpenShift_Installation/index.html)

    *   [System Verifications and Final Tests](https://docs.habana.ai/en/latest/Installation_Guide/System_Verification_and_Final_Tests.html)

*   [Quick Start Guides](https://docs.habana.ai/en/latest/Quick_Start_Guides/index.html)- [x] 
    *   [Intel Tiber AI Cloud Quick Start Guide](https://docs.habana.ai/en/latest/Quick_Start_Guides/Intel_DevCloud_Quick_Start.html)
    *   [IBM Cloud Quick Start Guide](https://docs.habana.ai/en/latest/Quick_Start_Guides/IBM_Quick_Start.html)
    *   [Running Workloads on Bare Metal](https://docs.habana.ai/en/latest/Quick_Start_Guides/Bare_Metal_Quick_Start.html)
    *   [Running Workloads on Docker](https://docs.habana.ai/en/latest/Quick_Start_Guides/Docker_Quick_Start.html)
    *   [Running Workloads on Kubernetes](https://docs.habana.ai/en/latest/Quick_Start_Guides/Kubernetes_Quick_Start.html)

PyTorch

*   [Training](https://docs.habana.ai/en/latest/PyTorch/index.html)- [x] 
    *   [Getting Started with Training on Intel Gaudi](https://docs.habana.ai/en/latest/PyTorch/Getting_Started_with_PyTorch_and_Gaudi/Getting_Started_with_PyTorch.html)
    *   [PyTorch Model Porting](https://docs.habana.ai/en/latest/PyTorch/PyTorch_Model_Porting/index.html)- [x] 
        *   [GPU Migration Toolkit](https://docs.habana.ai/en/latest/PyTorch/PyTorch_Model_Porting/GPU_Migration_Toolkit/GPU_Migration_Toolkit.html)
        *   [Importing PyTorch Models Manually](https://docs.habana.ai/en/latest/PyTorch/PyTorch_Model_Porting/Porting_PyTorch_Models_to_Gaudi.html)

    *   [Mixed Precision Training with PyTorch Autocast](https://docs.habana.ai/en/latest/PyTorch/PyTorch_Mixed_Precision/index.html)
    *   [Intel Gaudi Media Loader](https://docs.habana.ai/en/latest/PyTorch/Using_Media_Loader_with_PyTorch/Media_Loader_PT.html)
    *   [FP8 Training with Intel Gaudi Transformer Engine](https://docs.habana.ai/en/latest/PyTorch/PyTorch_FP8_Training/index.html)
    *   [Distributed Training with PyTorch](https://docs.habana.ai/en/latest/PyTorch/PyTorch_Scaling_Guide/index.html)- [x] 
        *   [Scale-out Topology](https://docs.habana.ai/en/latest/PyTorch/PyTorch_Scaling_Guide/Scale_Out_Topology.html)
        *   [Distributed Backend Initialization](https://docs.habana.ai/en/latest/PyTorch/PyTorch_Scaling_Guide/Distributed_Backend_Initialization.html)
        *   [Gaudi-to-process Assignment](https://docs.habana.ai/en/latest/PyTorch/PyTorch_Scaling_Guide/Gaudi_Assignment.html)
        *   [DDP-based Scaling of Gaudi on PyTorch](https://docs.habana.ai/en/latest/PyTorch/PyTorch_Scaling_Guide/DDP_Based_Scaling.html)
        *   [Theory of Distributed Training](https://docs.habana.ai/en/latest/PyTorch/PyTorch_Scaling_Guide/Theory_of_Distributed_Training.html)

    *   [Using Fully Sharded Data Parallel (FSDP) with Intel Gaudi](https://docs.habana.ai/en/latest/PyTorch/PyTorch_FSDP/Pytorch_FSDP.html)
    *   [Using DistributedTensor with Intel Gaudi](https://docs.habana.ai/en/latest/PyTorch/PyTorch_DistributedTensor/PyTorch_DistributedTensor.html)

*   [Inference](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/index.html)- [x] 
    *   [Getting Started with Inference on Intel Gaudi](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Getting_Started_with_Inference.html)
    *   [AI Model Serving with Intel Gaudi](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Model_Serving.html)
    *   [Run Inference Using HPU Graphs](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Inference_Using_HPU_Graphs.html)
    *   [Inference with Quantization](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/index.html)- [x] 
        *   [Run Inference Using FP8](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html)
        *   [Run Inference Using UINT4](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_UINT4.html)
        *   [Run Inference Using NF4](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_NF4.html)

    *   [Optimize Inference on PyTorch](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Inference_Optimization.html)
    *   [Using Gaudi Trained Checkpoints on Xeon](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Gaudi_Checkpoints_Xeon.html)
    *   [Triton Inference Server with Gaudi](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Triton_Inference.html)
    *   [TorchServe Inference Server with Gaudi](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/TorchServe_Inference.html)

*   [vLLM Fork](https://docs.habana.ai/en/latest/PyTorch/vLLM_Inference/index.html)- [x] 
    *   [vLLM Quick Start Guide](https://docs.habana.ai/en/latest/PyTorch/vLLM_Inference/vLLM_Quick_Start.html)
    *   [Inference Using vLLM](https://docs.habana.ai/en/latest/PyTorch/vLLM_Inference/vLLM_Inference.html)
    *   [FP8 Calibration and Inference with vLLM](https://docs.habana.ai/en/latest/PyTorch/vLLM_Inference/vLLM_FP8_Inference.html)
    *   [Managing and Reducing vLLM Warmup Time](https://docs.habana.ai/en/latest/PyTorch/vLLM_Inference/Managing_vLLM_Warmup_Time.html)
    *   [Deployable vLLM Containers Tutorial](https://github.com/HabanaAI/Gaudi-tutorials/tree/main/PyTorch/vLLM_Tutorials/Deploying_vLLM)
    *   [Profiling with vLLM](https://docs.habana.ai/en/latest/PyTorch/vLLM_Inference/vLLM_Profiling.html)
    *   [vLLM with Intel Gaudi FAQs](https://docs.habana.ai/en/latest/PyTorch/vLLM_Inference/vLLM_FAQs.html)

*   [vLLM Plugin](https://vllm-gaudi.readthedocs.io/en/latest/index.html)
*   [SGLang](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/index.html)- [x] 
    *   [SGLang Quick Start Guide](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Quick_Start.html)
    *   [Inference Using SGLang](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html)
    *   [Managing and Reducing SGLang Warmup Time](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/Managing_SGLang_Warmup_Time.html)
    *   [Profiling with SGLang](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Profiling.html)
    *   [SGLang with Gaudi FAQs](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_FAQs.html)

*   [DeepSpeed](https://docs.habana.ai/en/latest/PyTorch/DeepSpeed/index.html)- [x] 
    *   [Getting Started with DeepSpeed](https://docs.habana.ai/en/latest/PyTorch/DeepSpeed/Getting_Started_with_DeepSpeed/Getting_Started_with_DeepSpeed.html)
    *   [DeepSpeed Training](https://docs.habana.ai/en/latest/PyTorch/DeepSpeed/DeepSpeed_User_Guide/DeepSpeed_User_Guide.html)
    *   [Optimizing Large Language Models](https://docs.habana.ai/en/latest/PyTorch/DeepSpeed/Optimizing_LLM.html)
    *   [Inference Using DeepSpeed](https://docs.habana.ai/en/latest/PyTorch/DeepSpeed/Inference_Using_DeepSpeed.html)

*   [Optimization](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/index.html)- [x] 
    *   [Model Optimization Checklist](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_Getting_Started.html)
    *   [Optimizations of PyTorch Models](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html)
    *   [Inference Optimizations](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Inference_Optimization.html)
    *   [Handling Dynamic Shapes](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html)
    *   [Fused Optimizers and Custom Ops for Intel Gaudi](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#)
    *   [HPU Graphs for Training](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/HPU_Graphs_Training.html)
    *   [Optimizing Training Platform](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_Training_Platform.html)
    *   [Parallel Compilation](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Parallel_Compilation.html)

*   [Reference](https://docs.habana.ai/en/latest/PyTorch/Reference/index.html)- [x] 
    *   [Debugging and Troubleshooting](https://docs.habana.ai/en/latest/PyTorch/Reference/Debugging_Guide/index.html)- [x] 
        *   [Debugging with Intel Gaudi Logs](https://docs.habana.ai/en/latest/PyTorch/Reference/Debugging_Guide/Debugging_with_Intel_Gaudi_Logs.html)
        *   [Debugging Model Divergence](https://docs.habana.ai/en/latest/PyTorch/Reference/Debugging_Guide/Debugging_Model_Divergence.html)
        *   [Debugging Slow Convergence](https://docs.habana.ai/en/latest/PyTorch/Reference/Debugging_Guide/Debugging_Slow_Convergence.html)
        *   [Troubleshooting PyTorch Model](https://docs.habana.ai/en/latest/PyTorch/Reference/Debugging_Guide/Model_Troubleshooting.html)

    *   [Runtime Environment Variables](https://docs.habana.ai/en/latest/PyTorch/Reference/Runtime_Flags.html)
    *   [Intel Gaudi PyTorch Python API (habana_frameworks.torch)](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html)
    *   [PyTorch Operators](https://docs.habana.ai/en/latest/PyTorch/Reference/Pytorch_Operators/Pytorch_Operators.html)
    *   [PyTorch CustomOp API](https://docs.habana.ai/en/latest/PyTorch/Reference/PyTorch_CustomOp_API/page_index.html)
    *   [PyTorch Support Matrix](https://docs.habana.ai/en/latest/PyTorch/Reference/PyTorch_Support_Matrix.html)
    *   [PyTorch Gaudi Theory of Operations](https://docs.habana.ai/en/latest/PyTorch/Reference/PyTorch_Gaudi_Theory_of_Operations.html)
    *   [mark_step](https://docs.habana.ai/en/latest/PyTorch/Reference/mark_step.html)

*   [Hugging Face Optimum for Intel Gaudi](https://huggingface.co/docs/optimum/habana_index)

Guides

*   [MediaPipe](https://docs.habana.ai/en/latest/Media_Pipeline/index.html)- [x] 
    *   [Creating and Executing Media Pipeline](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html)
    *   [MediaPipe for PyTorch ResNet](https://docs.habana.ai/en/latest/Media_Pipeline/Pytorch_Resnet_Media_Pipe.html)
    *   [MediaPipe for PyTorch ResNet3d](https://docs.habana.ai/en/latest/Media_Pipeline/Pytorch_Resnet3d_Media_Pipe.html)
    *   [Operators](https://docs.habana.ai/en/latest/Media_Pipeline/Operators.html)- [x] 
        *   [fn.Add](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Add.html)
        *   [fn.BasicCrop](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_BasicCrop.html)
        *   [fn.BitwiseAnd](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_BitwiseAnd.html)
        *   [fn.BitwiseOr](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_BitwiseOr.html)
        *   [fn.BitwiseXor](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_BitwiseXor.html)
        *   [fn.Brightness](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Brightness.html)
        *   [fn.Cast](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Cast.html)
        *   [fn.Clamp](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Clamp.html)
        *   [fn.CocoReader](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_CocoReader.html)
        *   [fn.CoinFlip](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_CoinFlip.html)
        *   [fn.ColorSpaceConversion](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_ColorSpaceConversion.html)
        *   [fn.Concat](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Concat.html)
        *   [fn.Constant](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Constant.html)
        *   [fn.Contrast](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Contrast.html)
        *   [fn.Crop](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Crop.html)
        *   [fn.CropMirrorNorm](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_CMN.html)
        *   [fn.ExtCpuOp](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_ExtCpuOp.html)
        *   [fn.ExtHpuOp](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_ExtHpuOp.html)
        *   [fn.Flip](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Flip.html)
        *   [fn.GatherND](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_GatherND.html)
        *   [fn.GaussianBlur](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_GaussianBlur.html)
        *   [fn.Hue](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Hue.html)
        *   [fn.ImageDecoder](https://docs.habana.ai/en/latest/Media_Pipeline/Decoder.html)
        *   [fn.MediaConst](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_MediaConst.html)
        *   [fn.MediaExtReaderOp](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Reader_MediaExtReaderOp.html)
        *   [fn.MediaFunc](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_MediaFunc.html)
        *   [fn.MemCpy](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_MemCopy.html)
        *   [fn.Mult](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Mult.html)
        *   [fn.Neg](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Neg.html)
        *   [fn.Normalize](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Normalize.html)
        *   [fn.Pad](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Pad.html)
        *   [fn.RandomBiasedCrop](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_RandomBiasedCrop.html)
        *   [fn.RandomFlip](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_RandomFlip.html)
        *   [fn.RandomNormal](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_RandomNormal.html)
        *   [fn.RandomUniform](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_RandomUniform.html)
        *   [fn.ReadImageDatasetFromDir](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Reader_ReadImageDatasetFromDir.html)
        *   [fn.ReadNumpyDatasetFromDir](https://docs.habana.ai/en/latest/Media_Pipeline/Reader_Numpy.html)
        *   [fn.ReadVideoDatasetFromDir](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Reader_ReadVideoDatasetFromDir.html)
        *   [fn.ReadVideoDatasetFromDirGen](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Reader_ReadVideoDatasetFromDirGen.html)
        *   [fn.ReduceMax](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_ReduceMax.html)
        *   [fn.ReduceMin](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_ReduceMin.html)
        *   [fn.Reshape](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Reshape.html)
        *   [fn.Resize](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Resize.html)
        *   [fn.Saturation](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Saturation.html)
        *   [fn.Slice](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Slice.html)
        *   [fn.Split](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Split.html)
        *   [fn.SSDBBoxFlip](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_SSDBBoxFlip.html)
        *   [fn.SSDCropWindowGen](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_SSDCropWindowGen.html)
        *   [fn.SSDEncode](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_SSDEncode.html)
        *   [fn.SSDMetadata](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_SSDMetadata.html)
        *   [fn.Sub](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Sub.html)
        *   [fn.Transpose](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Transpose.html)
        *   [fn.VideoDecoder](https://docs.habana.ai/en/latest/Media_Pipeline/Video_Decoder.html)
        *   [fn.Where](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Where.html)
        *   [fn.Zoom](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_Zoom.html)

*   [Profiling](https://docs.habana.ai/en/latest/Profiling/index.html)- [x] 
    *   [Profiling Workflow](https://docs.habana.ai/en/latest/Profiling/Profiling_Workflow.html)
    *   [Profiling Real-World Examples](https://docs.habana.ai/en/latest/Profiling/Profiling_Examples.html)
    *   [Profiling with PyTorch](https://docs.habana.ai/en/latest/Profiling/Profiling_with_PyTorch.html)
    *   [Profiling with Intel Gaudi Software](https://docs.habana.ai/en/latest/Profiling/Intel_Gaudi_Profiling/index.html)- [x] 
        *   [Getting Started with Intel Gaudi Profiler](https://docs.habana.ai/en/latest/Profiling/Intel_Gaudi_Profiling/Getting_Started_with_Profiler.html)
        *   [Configuration](https://docs.habana.ai/en/latest/Profiling/Intel_Gaudi_Profiling/Configuration.html)
        *   [Analysis](https://docs.habana.ai/en/latest/Profiling/Intel_Gaudi_Profiling/Analysis.html)
        *   [Remote Trace Viewer Tool](https://docs.habana.ai/en/latest/Profiling/Intel_Gaudi_Profiling/Remote_Trace_Viewer_Tool.html)
        *   [Offline Trace Parser Tool](https://docs.habana.ai/en/latest/Profiling/Intel_Gaudi_Profiling/Offline_Trace_Parser.html)
        *   [Tips and Tricks to Accelerate the Training](https://docs.habana.ai/en/latest/Profiling/Intel_Gaudi_Profiling/Profiling_Tips_and_Tricks.html)

*   [Management and Monitoring](https://docs.habana.ai/en/latest/Management_and_Monitoring/index.html)- [x] 
    *   [Qualification Tool Library Guide (hl_qual)](https://docs.habana.ai/en/latest/Management_and_Monitoring/Qualification_Library/index.html)- [x] 
        *   [hl_qual Common Plugin Switches and Parameters](https://docs.habana.ai/en/latest/Management_and_Monitoring/Qualification_Library/Common_Plugin_Switches_and_Parameters.html)
        *   [hl_qual Report Structure](https://docs.habana.ai/en/latest/Management_and_Monitoring/Qualification_Library/hl_qual_Report_Structure.html)
        *   [hl_qual Expected Output and Failure Debug](https://docs.habana.ai/en/latest/Management_and_Monitoring/Qualification_Library/hl_qual_Expected_Output_and_Failure_Debug.html)
        *   [Memory Stress Test Plugins Design, Switches and Parameters](https://docs.habana.ai/en/latest/Management_and_Monitoring/Qualification_Library/Memory_Stress_Tests_Plugin.html)
        *   [Power Stress and EDP Tests Plugins Design, Switches and Parameters](https://docs.habana.ai/en/latest/Management_and_Monitoring/Qualification_Library/Power_Stress_Tests_Plugin.html)
        *   [Connectivity Serdes Test Plugins Design, Switches and Parameters](https://docs.habana.ai/en/latest/Management_and_Monitoring/Qualification_Library/Connectivity_Serdes_Tests_Plugin.html)
        *   [Functional Test Plugins Design, Switches and Parameters](https://docs.habana.ai/en/latest/Management_and_Monitoring/Qualification_Library/Functional_Tests_Plugin.html)
        *   [Bandwidth Test Plugins Design, Switches and Parameters](https://docs.habana.ai/en/latest/Management_and_Monitoring/Qualification_Library/Bandwidth_Tests_Plugin.html)
        *   [hl_qual Monitor Textual UI](https://docs.habana.ai/en/latest/Management_and_Monitoring/Qualification_Library/hl_qual_Monitor.html)
        *   [Package Content](https://docs.habana.ai/en/latest/Management_and_Monitoring/Qualification_Library/Package_Content.html)
        *   [hl_qual Design](https://docs.habana.ai/en/latest/Management_and_Monitoring/Qualification_Library/hl_qual_Design.html)
        *   [Diagnostic Tool](https://docs.habana.ai/en/latest/Management_and_Monitoring/Qualification_Library/Diagnostic_Tool/index.html)- [x] 
            *   [Test Plan Automation](https://docs.habana.ai/en/latest/Management_and_Monitoring/Qualification_Library/Diagnostic_Tool/Test_Plan_Automation.html)
            *   [Log Analysis](https://docs.habana.ai/en/latest/Management_and_Monitoring/Qualification_Library/Diagnostic_Tool/Log_Analysis.html)
            *   [Qual Package Installation Validator](https://docs.habana.ai/en/latest/Management_and_Monitoring/Qualification_Library/Diagnostic_Tool/Qual_Package_Installation_Validator.html)
            *   [Rack Scale Script](https://docs.habana.ai/en/latest/Management_and_Monitoring/Qualification_Library/Diagnostic_Tool/Rack_Scale_Script.html)

    *   [Embedded System Tools User Guide](https://docs.habana.ai/en/latest/Management_and_Monitoring/Embedded_System_Tools_Guide/index.html)- [x] 
        *   [Firmware Update Tool](https://docs.habana.ai/en/latest/Management_and_Monitoring/Embedded_System_Tools_Guide/Firmware_Update_Tool.html)
        *   [System Management Interface Tool ( ``` hl-smi ``` )](https://docs.habana.ai/en/latest/Management_and_Monitoring/Embedded_System_Tools_Guide/System_Management_Interface_Tool.html)
        *   [Intel Gaudi Secure Firmware Flow](https://docs.habana.ai/en/latest/Management_and_Monitoring/Embedded_System_Tools_Guide/Intel_Gaudi_Secure_Firmware.html)
        *   [Intel Gaudi Secure Boot Flow](https://docs.habana.ai/en/latest/Management_and_Monitoring/Embedded_System_Tools_Guide/Enable_Secure_Boot.html)
        *   [Disable/Enable NICs](https://docs.habana.ai/en/latest/Management_and_Monitoring/Embedded_System_Tools_Guide/Disable_Enable_NICs.html)

    *   [Hypervisor Tools Installation and Usage](https://docs.habana.ai/en/latest/Management_and_Monitoring/Hypervisor_Tools/index.html)- [x] 
        *   [Installing Hypervisor Tools Package](https://docs.habana.ai/en/latest/Management_and_Monitoring/Hypervisor_Tools/Hpervisor_Tools_Installation.html)
        *   [Memory Scrub Verification Tool](https://docs.habana.ai/en/latest/Management_and_Monitoring/Hypervisor_Tools/Memory_Scrub_Verification_Tool.html)
        *   [hl_smi_async Tool](https://docs.habana.ai/en/latest/Management_and_Monitoring/Hypervisor_Tools/hl_smi_async_Tool.html)

    *   [Intel Gaudi RDMA PerfTest Tool](https://docs.habana.ai/en/latest/Management_and_Monitoring/RDMA_PerfTest_Tool/RDMA_PerfTest_Tool.html)
    *   [Intel Gaudi ReportNCheck Tool](https://docs.habana.ai/en/latest/Management_and_Monitoring/ReportNCheck_Tool/ReportNCheck_Tool.html)
    *   [Intel Gaudi Network Configuration](https://docs.habana.ai/en/latest/Management_and_Monitoring/Network_Configuration/index.html)- [x] 
        *   [Arista Switch L2 Configuration Example](https://docs.habana.ai/en/latest/Management_and_Monitoring/Network_Configuration/Configuration_Files_Example_L2.html)
        *   [Arista Switch L3 Configuration Example](https://docs.habana.ai/en/latest/Management_and_Monitoring/Network_Configuration/Configuration_Files_Example_L3.html)
        *   [Configure E2E Test in L2/L3 Switching Environment](https://docs.habana.ai/en/latest/Management_and_Monitoring/Network_Configuration/Configure_E2E_Test_in_L3.html)
        *   [Expected Switch Configuration](https://docs.habana.ai/en/latest/Management_and_Monitoring/Network_Configuration/Expected_Switch_Configuration.html)
        *   [Monitoring Switch and Gaudi 3 Accelerator](https://docs.habana.ai/en/latest/Management_and_Monitoring/Network_Configuration/Monitoring_Switch_and_Gaudi_Accelerator.html)
        *   [Collectives Performance](https://docs.habana.ai/en/latest/Management_and_Monitoring/Network_Configuration/Collectives_Performance.html)
        *   [Congestion Test](https://docs.habana.ai/en/latest/Management_and_Monitoring/Network_Configuration/Congestion_Test.html)
        *   [How to Pick Good Nodes in the Datacenter](https://docs.habana.ai/en/latest/Management_and_Monitoring/Network_Configuration/Pick_Good_Nodes_in_Datacenter.html)

    *   [Habana Labs Management Library (HLML) C API Reference](https://docs.habana.ai/en/latest/Management_and_Monitoring/HLML_API/index.html)- [x] 
        *   [C APIs](https://docs.habana.ai/en/latest/Management_and_Monitoring/HLML_API/HLML_C_API.html)
        *   [Common APIs](https://docs.habana.ai/en/latest/Management_and_Monitoring/HLML_API/Common_APIs.html)
        *   [Per Device APIs](https://docs.habana.ai/en/latest/Management_and_Monitoring/HLML_API/Per_Device_APIs.html)
        *   [Linkage HLML](https://docs.habana.ai/en/latest/Management_and_Monitoring/HLML_API/Linkage_HLML.html)

    *   [Habana Labs Management Library (PYHLML) Python API Reference](https://docs.habana.ai/en/latest/Management_and_Monitoring/PYHLML_APIs/index.html)- [x] 
        *   [Python APIs](https://docs.habana.ai/en/latest/Management_and_Monitoring/PYHLML_APIs/HLML_PY_API.html)
        *   [Common APIs](https://docs.habana.ai/en/latest/Management_and_Monitoring/PYHLML_APIs/Common_APIs.html)
        *   [Per Device APIs](https://docs.habana.ai/en/latest/Management_and_Monitoring/PYHLML_APIs/Per_Device_APIs.html)

    *   [Kernel Module Diagnostics](https://docs.habana.ai/en/latest/Management_and_Monitoring/Kernel_Module_Diagnostics/index.html)- [x] 
        *   [Dmesg Error Causes](https://docs.habana.ai/en/latest/Management_and_Monitoring/Kernel_Module_Diagnostics/Dmesg_Error_Causes.html)
        *   [Scalable Ethernet Interface (SEI) error causes](https://docs.habana.ai/en/latest/Management_and_Monitoring/Kernel_Module_Diagnostics/SEI_Error_Causes.html)
        *   [Queue Pair (QP) error causes](https://docs.habana.ai/en/latest/Management_and_Monitoring/Kernel_Module_Diagnostics/QP_Error_Causes.html)

*   [Orchestration](https://docs.habana.ai/en/latest/Orchestration/index.html)- [x] 
    *   [Running Workloads on Kubernetes](https://docs.habana.ai/en/latest/Quick_Start_Guides/Kubernetes_Quick_Start.html)
    *   [VMware Tanzu User Guide](https://docs.habana.ai/en/latest/Orchestration/VMware_Tanzu/VMware_Tanzu_Guide.html)
    *   [Enabling Multiple Tenants on PyTorch](https://docs.habana.ai/en/latest/Orchestration/Multiple_Tenants_on_HPU/index.html)- [x] 
        *   [Multiple Workloads on a Single Docker](https://docs.habana.ai/en/latest/Orchestration/Multiple_Tenants_on_HPU/Multiple_Workloads_Single_Docker.html)
        *   [Multiple Dockers Each with a Single Workload](https://docs.habana.ai/en/latest/Orchestration/Multiple_Tenants_on_HPU/Multiple_Dockers_each_with_Single_Workload.html)

    *   [BMC Exporter User Guide](https://docs.habana.ai/en/latest/Orchestration/BMC_Exporter/BMC_Exporter.html)
    *   [Prometheus Metric Exporter](https://docs.habana.ai/en/latest/Orchestration/Prometheus_Metric_Exporter.html)
    *   [Using Slurm Workload Manager with Intel Gaudi](https://docs.habana.ai/en/latest/Orchestration/SLURM/SLURM.html)

*   [Virtualization](https://docs.habana.ai/en/latest/Virtualization/Configuring_VMs_on_Gaudi.html)
*   [APIs](https://docs.habana.ai/en/latest/API_Reference_Guides/index.html)- [x] 
    *   [Habana Collective Communications Library (HCCL) API Reference](https://docs.habana.ai/en/latest/API_Reference_Guides/HCCL_APIs/index.html)- [x] 
        *   [Supported Collective Primitives](https://docs.habana.ai/en/latest/API_Reference_Guides/HCCL_APIs/Overview.html)
        *   [Using HCCL](https://docs.habana.ai/en/latest/API_Reference_Guides/HCCL_APIs/Using_HCCL.html)
        *   [Scale-out via Host NIC](https://docs.habana.ai/en/latest/API_Reference_Guides/HCCL_APIs/Scale_Out_via_Host_NIC.html)
        *   [C APIs](https://docs.habana.ai/en/latest/API_Reference_Guides/HCCL_APIs/C_API.html)
        *   [Testing and Benchmarking](https://docs.habana.ai/en/latest/API_Reference_Guides/HCCL_APIs/Testing_and_Benchmarking.html)

    *   [Habana Labs Management Library (HLML) C API Reference](https://docs.habana.ai/en/latest/API_Reference_Guides/HLML_APIs/index.html)- [x] 
        *   [C APIs](https://docs.habana.ai/en/latest/API_Reference_Guides/HLML_APIs/HLML_C_API.html)
        *   [Common APIs](https://docs.habana.ai/en/latest/API_Reference_Guides/HLML_APIs/Common_APIs.html)
        *   [Per Device APIs](https://docs.habana.ai/en/latest/API_Reference_Guides/HLML_APIs/Per_Device_APIs.html)
        *   [Linkage HLML](https://docs.habana.ai/en/latest/API_Reference_Guides/HLML_APIs/Linkage_HLML.html)

    *   [Habana Labs Management Library (PYHLML) Python API Reference](https://docs.habana.ai/en/latest/API_Reference_Guides/PYHLML_APIs/index.html)- [x] 
        *   [Python APIs](https://docs.habana.ai/en/latest/API_Reference_Guides/PYHLML_APIs/HLML_PY_API.html)
        *   [Common APIs](https://docs.habana.ai/en/latest/API_Reference_Guides/PYHLML_APIs/Common_APIs.html)
        *   [Per Device APIs](https://docs.habana.ai/en/latest/API_Reference_Guides/PYHLML_APIs/Per_Device_APIs.html)

    *   [Intel Gaudi PyTorch Python API](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html)

*   [TPC Programming](https://docs.habana.ai/en/latest/TPC/index.html)- [x] 
    *   [TPC Getting Started Guide](https://docs.habana.ai/en/latest/TPC/TPC_Getting_Started/TPC_Getting_Started.html)
    *   [TPC Tools Installation Guide](https://docs.habana.ai/en/latest/TPC/TPC_Tools_Installation/TPC_Tools_Installation_Guide.html)
    *   [TPC User Guide](https://docs.habana.ai/en/latest/TPC/TPC_User_Guide/index.html)- [x] 
        *   [TPC Programming Language](https://docs.habana.ai/en/latest/TPC/TPC_User_Guide/TPC_Programming_Language.html)
        *   [Processor Architectural Overview](https://docs.habana.ai/en/latest/TPC/TPC_User_Guide/Processor_Architectural_Overview.html)
        *   [TPC Programming Model](https://docs.habana.ai/en/latest/TPC/TPC_User_Guide/TPC_Programming_Model.html)
        *   [TPC-C Language](https://docs.habana.ai/en/latest/TPC/TPC_User_Guide/TPC_C_Language.html)
        *   [Built-in Functions](https://docs.habana.ai/en/latest/TPC/TPC_User_Guide/Built_in_Functions.html)
        *   [Implementing and Integrating New lib](https://docs.habana.ai/en/latest/TPC/TPC_User_Guide/Implementing_and_Integrating_New_lib.html)
        *   [TPC Coherency](https://docs.habana.ai/en/latest/TPC/TPC_User_Guide/TPC_Coherency.html)
        *   [Multiple Kernel Libraries](https://docs.habana.ai/en/latest/TPC/TPC_User_Guide/Multiple_Kernels_Library.html)
        *   [Abbreviations](https://docs.habana.ai/en/latest/TPC/TPC_User_Guide/Abbreviations.html)

    *   [TPC Tools Debugger](https://docs.habana.ai/en/latest/TPC/TPC_Debugger/index.html)- [x] 
        *   [Installation](https://docs.habana.ai/en/latest/TPC/TPC_Debugger/Installation.html)
        *   [Starting a Debug Session](https://docs.habana.ai/en/latest/TPC/TPC_Debugger/Start_Debug_Session.html)
        *   [TPC-C Source or Disassembly Level Debugging](https://docs.habana.ai/en/latest/TPC/TPC_Debugger/Source_Disassembly_Debugging.html)
        *   [Debug Session Views and Operations](https://docs.habana.ai/en/latest/TPC/TPC_Debugger/Views_and_Operations.html)

    *   [TPC-C Language Specification](https://docs.habana.ai/en/latest/TPC/TPC_C_Language_Spec/index.html)- [x] 
        *   [Supported Data Types](https://docs.habana.ai/en/latest/TPC/TPC_C_Language_Spec/Supported_Data_Types.html)
        *   [Conversions and Type Casting](https://docs.habana.ai/en/latest/TPC/TPC_C_Language_Spec/Conversions_and_Type_Casting.html)
        *   [Operators](https://docs.habana.ai/en/latest/TPC/TPC_C_Language_Spec/Operators.html)
        *   [Vector Operations](https://docs.habana.ai/en/latest/TPC/TPC_C_Language_Spec/Vector_Operations.html)
        *   [Address Space Qualifiers](https://docs.habana.ai/en/latest/TPC/TPC_C_Language_Spec/Address_Space_Qualifiers.html)
        *   [Storage-Class Specifiers](https://docs.habana.ai/en/latest/TPC/TPC_C_Language_Spec/Storage_Class_Specifiers.html)
        *   [Exceptions to C99 standard](https://docs.habana.ai/en/latest/TPC/TPC_C_Language_Spec/Exceptions_to_C99_Standard.html)
        *   [Exceptions to C++ 11 Standard](https://docs.habana.ai/en/latest/TPC/TPC_C_Language_Spec/Exceptions_to_C_11_Standard.html)
        *   [Preprocessor Directives and Macros](https://docs.habana.ai/en/latest/TPC/TPC_C_Language_Spec/Preprocessor_Directives_and_Macros.html)
        *   [Functions](https://docs.habana.ai/en/latest/TPC/TPC_C_Language_Spec/Functions.html)
        *   [Built-in Special Functions](https://docs.habana.ai/en/latest/TPC/TPC_C_Language_Spec/Built_in_Special_Functions.html)

    *   [TPC Intrinsics Guide](https://docs.habana.ai/en/latest/TPC/TPC_Intrinsics_Guide/index.html)- [x] 
        *   [Arithmetic](https://docs.habana.ai/en/latest/TPC/TPC_Intrinsics_Guide/Arithmetic.html)
        *   [Bitwise](https://docs.habana.ai/en/latest/TPC/TPC_Intrinsics_Guide/Bitwise.html)
        *   [Cache](https://docs.habana.ai/en/latest/TPC/TPC_Intrinsics_Guide/Cache.html)
        *   [Convert](https://docs.habana.ai/en/latest/TPC/TPC_Intrinsics_Guide/Convert.html)
        *   [IRF](https://docs.habana.ai/en/latest/TPC/TPC_Intrinsics_Guide/IRF.html)
        *   [LUT](https://docs.habana.ai/en/latest/TPC/TPC_Intrinsics_Guide/LUT.html)
        *   [Load](https://docs.habana.ai/en/latest/TPC/TPC_Intrinsics_Guide/Load.html)
        *   [Logical](https://docs.habana.ai/en/latest/TPC/TPC_Intrinsics_Guide/Logical.html)
        *   [Move](https://docs.habana.ai/en/latest/TPC/TPC_Intrinsics_Guide/Move.html)
        *   [Pack/Unpack](https://docs.habana.ai/en/latest/TPC/TPC_Intrinsics_Guide/Pack_Unpack.html)
        *   [Select](https://docs.habana.ai/en/latest/TPC/TPC_Intrinsics_Guide/Select.html)
        *   [Store](https://docs.habana.ai/en/latest/TPC/TPC_Intrinsics_Guide/Store.html)
        *   [Miscellaneous](https://docs.habana.ai/en/latest/TPC/TPC_Intrinsics_Guide/Miscellaneous.html)

    *   [TPC I64 Built-ins Guide](https://docs.habana.ai/en/latest/TPC/TPC_I64_Builtins/index.html)- [x] 
        *   [Arithmetic](https://docs.habana.ai/en/latest/TPC/TPC_I64_Builtins/Arithmetic.html)
        *   [Load](https://docs.habana.ai/en/latest/TPC/TPC_I64_Builtins/Load.html)
        *   [Move](https://docs.habana.ai/en/latest/TPC/TPC_I64_Builtins/Move.html)
        *   [Select](https://docs.habana.ai/en/latest/TPC/TPC_I64_Builtins/Select.html)
        *   [Store](https://docs.habana.ai/en/latest/TPC/TPC_I64_Builtins/Store.html)

Support

*   [Support and Legal Notice](https://docs.habana.ai/en/latest/Support/index.html)

 Theme by the [Executable Book Project](https://ebp.jupyterbook.org/)

 On this Page 

*   [Fused Optimizers](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fused-optimizers)
    *   [FusedAdagrad](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedadagrad)
    *   [FusedAdamW](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedadamw)
    *   [FusedEMA](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedema)
    *   [FusedLamb](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedlamb)
    *   [FusedSGD](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedsgd)
    *   [Functional FusedAdamW](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#functional-fusedadamw)
    *   [FusedLars](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedlars)

*   [Custom Ops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#custom-ops)
    *   [FusedClipNorm](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedclipnorm)
    *   [Mixture of Experts Forward (MoE)](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#mixture-of-experts-forward-moe)

Fused Optimizers and Custom Ops for Intel Gaudi
===============================================

On this Page
------------

*   [Fused Optimizers](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fused-optimizers)
    *   [FusedAdagrad](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedadagrad)
    *   [FusedAdamW](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedadamw)
    *   [FusedEMA](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedema)
    *   [FusedLamb](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedlamb)
    *   [FusedSGD](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedsgd)
    *   [Functional FusedAdamW](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#functional-fusedadamw)
    *   [FusedLars](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedlars)

*   [Custom Ops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#custom-ops)
    *   [FusedClipNorm](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedclipnorm)
    *   [Mixture of Experts Forward (MoE)](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#mixture-of-experts-forward-moe)

Fused Optimizers and Custom Ops for Intel Gaudi[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fused-optimizers-and-custom-ops-for-intel-gaudi "Permalink to this headline")
============================================================================================================================================================================================================================

The Intel® Gaudi® AI accelerator provides its own implementation of complex PyTorch ops customized for Gaudi devices. Replacing these complex ops with custom Gaudi versions enhances model performance.

Fused Optimizers[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fused-optimizers "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------

The following fused optimizers are supported:

*   FusedAdagrad

*   FusedAdamW

*   FusedEMA

*   FusedLamb

*   FusedSGD

*   Functional FusedAdamW

*   FusedLars

Following is an example demonstrating optimizer usage with the FusedAdagrad optimizer:

import torch
import torch.nn as nn
from habana_frameworks.torch.hpex.optimizers import FusedAdagrad

# Define a simple model
class SimpleModel(nn.Module):
    def  __init__ (self):
        super(SimpleModel, self). __init__ ()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)

model = SimpleModel()

# Define the optimizer with all parameters
optimizer = FusedAdagrad(
    model.parameters(),
    lr=0.01,
    lr_decay=0.001,
    weight_decay=0.01,
    initial_accumulator_value=0.1,
    eps=1e-10
)

# Dummy input and target
input = torch.randn(32, 10)
target = torch.randn(32, 1)

# Define a loss function
loss = nn.MSELoss()

# Forward pass
output = model(input)
loss = loss(output, target)

# Zero the parameter gradients and call backward
optimizer.zero_grad()
loss.backward()

# Perform a single optimization step
optimizer.step()

### FusedAdagrad[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedadagrad "Permalink to this headline")

> FusedAdagrad is a fused implementation of the Adagrad optimizer for Gaudi devices. Refer to the original PyTorch op documentation - [torch.optim.Adagrad](https://pytorch.org/docs/stable/generated/torch.optim.Adagrad.html):

_class_`habana_frameworks.torch.hpex.optimizers.``FusedAdagrad`(_params_, _lr=0.01_, _lr\_decay=0_, _weight\_decay=0_, _initial\_accumulator\_value=0_, _eps=1e-10_)[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#habana_frameworks.torch.hpex.optimizers.FusedAdagrad "Permalink to this definition")Parameters
*   **params** – (iterable) - Iterable of parameters to optimize or dicts defining parameter groups.

*   **lr** – (float, optional) - Learning rate (default: 1e-2).

*   **lr_decay** – (float, optional) - Learning rate decay (default: 0).

*   **weight_decay** – (float, optional) - Weight decay (L2 penalty) (default: 0).

*   **initial_accumulator_value** – (float, optional) - Initial accumulator value (default: 0).

*   **eps** – (float, optional) - Term added to the denominator to improve numerical stability (default: 1e-10).

### FusedAdamW[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedadamw "Permalink to this headline")

> FusedAdamW is a fused implementation of the AdamW optimizer for Gaudi devices. Refer to the original [AdamW from Hugging Face](https://huggingface.co/docs/bitsandbytes/main/en/reference/optim/adamw) optimizer documentation:

_class_`habana_frameworks.torch.hpex.optimizers.``FusedAdamW`(_params_, _lr=0.001_, _betas=0.9, 0.999_, _eps=1e-06_, _weight\_decay=0.0_, _bias\_correction=True_, _moments\_dtype=None_)[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#habana_frameworks.torch.hpex.optimizers.FusedAdamW "Permalink to this definition")Parameters
*   **params** – (iterable) - Iterable of parameters to optimize or dicts defining parameter groups.

*   **lr** – (float, optional) - Learning rate (default: 1e-3).

*   **betas** – (Tuple[float, float], optional) - Coefficients used for computing running averages of gradient and its square (default: (0.9, 0.999)).

*   **eps** – (float, optional) - Term added to the denominator to improve numerical stability (default: 1e-6).

*   **weight_decay** – (float, optional) - Weight decay (L2 penalty) (default: 0.0).

*   **bias_correction** – (bool, optional) - Whether to use bias correction (default: True).

*   **moments_dtype** – (Optional[Union[torch.dtype, Tuple[torch.dtype, torch.dtype]]], optional) - Data type for moments (default: None).

### FusedEMA[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedema "Permalink to this headline")

> FusedEMA is a fused implementation of the EMA optimizer for Gaudi devices. Refer to the original PyTorch op documentation - [torch.optim.swa_utils.AveragedModel](https://pytorch.org/docs/stable/generated/torch.optim.swa_utils.AveragedModel.html):

_class_`habana_frameworks.torch.hpex.movingavrg.``FusedEMA`(_model_, _decay=0.9999_, _updates=0_)[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#habana_frameworks.torch.hpex.movingavrg.FusedEMA "Permalink to this definition")Parameters
*   **model** – (nn.Module) - Model to use with EMA

*   **decay** – (float, optional) - Decay parameter, scale to exponential function ‘decay * (1 - exp(-x / 2000))’ (default: 0.9999).

*   **updates** – (float, optional) - Counter incremented by 1 every update. Input ‘x’ to the above exponential function. (default: 0).

### FusedLamb[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedlamb "Permalink to this headline")

> Implements a version of LAMB optimizer customized for Gaudi devices. LAMB is proposed in [Large Batch Optimization for Deep Learning - Training BERT in 76 minutes](https://arxiv.org/abs/1904.00962):

_class_`habana_frameworks.torch.hpex.optimizers.``FusedLamb`(_params_, _lr=0.001_, _bias\_correction=True_, _betas=0.9, 0.999_, _eps=1e-06_, _weight\_decay=0.0_, _amsgrad=False_, _adam\_w\_mode=True_, _grad\_averaging=True_, _set\_grad\_none=True_, _max\_grad\_norm=1.0_, _use\_lamb=False_, _fused=False_, _dtype=None_)[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#habana_frameworks.torch.hpex.optimizers.FusedLamb "Permalink to this definition")Parameters
*   **params** – (iterable) - Iterable of parameters to optimize or dicts defining parameter groups.

*   **lr** – (float, optional) - Learning rate (default: 1e-3).

*   **bias_correction** – (bool, optional) - Whether to use bias correction (default: True).

*   **betas** – (Tuple[float, float], optional) - Coefficients used for computing running averages of gradient and its norm (default: (0.9, 0.999)).

*   **eps** – (float, optional) - Term added to the denominator to improve numerical stability (default: 1e-6).

*   **weight_decay** – (float, optional) - Weight decay (L2 penalty) (default: 0).

*   **amsgrad** – (boolean, optional) - Whether to use the AMSGrad variant of this algorithm (default: False).

*   **adam_w_mode** – (boolean, optional) - Apply L2 regularization or weight decay. True for decoupled weight decay (also known as AdamW) (default: True).

*   **grad_averaging** – (bool, optional) - Whether to apply (1-beta2) to grad when calculating running averages of gradient (default: True).

*   **set_grad_none** – (bool, optional) - Whether to set grad to None when zero_grad() method is called (default: True).

*   **max_grad_norm** – (float, optional) - Value used to clip global grad norm. If set to None, prior gradient clipping is disabled (default: 1.0).

*   **use_lamb** – (boolean, optional) - When set to True, force calculation of trust_ratio used for gradient update when weight_decay is 0 (default: False).

*   **dtype** – (torch.dtype, optional) - The desired data type of the parameters (grads). If specified, the parameters will be cast to this data type. (default: None)

### FusedSGD[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedsgd "Permalink to this headline")

> FusedSGD is a fused implementation of the SGD optimizer for Gaudi devices. Refer to the original PyTorch op documentation - [torch.optim.SGD](https://pytorch.org/docs/stable/generated/torch.optim.SGD.html):

_class_`habana_frameworks.torch.hpex.optimizers.``FusedSGD`(_params_, _lr_, _momentum=0_, _dampening=0_, _weight\_decay=0_, _nesterov=False_)[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#habana_frameworks.torch.hpex.optimizers.FusedSGD "Permalink to this definition")Parameters
*   **params** – (iterable) - Iterable of parameters to optimize or dicts defining parameter groups.

*   **lr** – (float) - Learning rate.

*   **momentum** – (float, optional) - Momentum factor (default: 0).

*   **weight_decay** – (float, optional) - Weight decay (L2 penalty) (default: 0).

*   **dampening** – (float, optional) - Dampening for momentum (default: 0).

*   **nesterov** – (bool, optional) - Enables Nesterov momentum (default: False).

### Functional FusedAdamW[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#functional-fusedadamw "Permalink to this headline")

> Functional FusedAdamW is a functional implementation of the AdamW optimizer for Gaudi devices. This functional version of FusedAdamW is based on [torch.distributed.optim._FunctionalAdamW](https://github.com/pytorch/pytorch/blob/master/torch/distributed/optim/functional_adamw.py). It can be enabled with `habana_frameworks.torch.hpex.optimizers.distributed.FusedAdamW`:

_class_`habana_frameworks.torch.hpex.optimizers.distributed.``FusedAdamW`(_params_, _lr=0.001_, _betas=0.9, 0.999_, _eps=1e-06_, _weight\_decay=0.0_, _\_allow\_empty\_param\_list=False_, _moments\_dtype=None_)[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#habana_frameworks.torch.hpex.optimizers.distributed.FusedAdamW "Permalink to this definition")Parameters
*   **params** – (List[torch.Tensor]) - List of parameters to optimize or dicts defining parameter groups.

*   **lr** – (float, optional) - Learning rate (default: 1e-3).

*   **betas** – (Tuple[float, float], optional) - Coefficients used for computing running averages of gradient and its square (default: (0.9, 0.999)).

*   **eps** – (float, optional) - Term added to the denominator to improve numerical stability (default: 1e-6).

*   **weight_decay** – (float, optional) - Weight decay (L2 penalty) (default: 0.0).

*   **_allow_empty_param_list** – (bool, optional) - Retained for PyTorch compatibility (default: False).

*   **moments_dtype** – (Optional[Union[torch.dtype, Tuple[torch.dtype, torch.dtype]]], optional) - Data type for moments (default: None).

### FusedLars[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedlars "Permalink to this headline")

> FusedLars is a fused implementation of the LARS optimizer for Gaudi devices. For more details, refer to the [LARS optimizer paper](https://arxiv.org/abs/1708.03888):

_class_`habana_frameworks.torch.hpex.optimizers.``FusedLars`(_optimizer_, _skip\_mask_, _eeta=0.001_, _eps=1e-08_)[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#habana_frameworks.torch.hpex.optimizers.FusedLars "Permalink to this definition")Parameters
*   **optimizer** – (torch.optim.Optimizer) - The base optimizer to be wrapped by FusedLars.

*   **skip_mask** – (torch.Tensor) - Mask to skip certain layers from LARS scaling.

*   **a** – (float, optional) - LARS coefficient as used in the paper (default: 0.001).

*   **eps** – (float, optional) - Term added to the denominator to improve numerical stability (default: 1e-8).

Note

For models using Lazy mode execution, `mark_step()` must be added right after `loss.backward()` and `optimizer.step()`. For further details on `mark_step`, refer to [mark_step](https://docs.habana.ai/en/latest/PyTorch/Reference/mark_step.html#mark-step-section) section.

Custom Ops[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#custom-ops "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------

### FusedClipNorm[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#fusedclipnorm "Permalink to this headline")

A class to perform gradient clipping by norm for parameters on Habana devices. Only norm_type 2.0 is supported. Refer to [torch.nn.utils.clip_grad_norm_](https://pytorch.org/docs/stable/_modules/torch/nn/utils/clip_grad.html#clip_grad_norm_) for more details.

_class_`habana_frameworks.torch.hpex.normalization.``FusedClipNorm`(_parameters:Iterable[torch.nn.parameter.Parameter]_, _max\_norm:float_)[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#habana_frameworks.torch.hpex.normalization.FusedClipNorm "Permalink to this definition")Parameters
*   **parameters** – (Iterable[torch.nn.parameter.Parameter]) - The parameters whose gradients will be clipped.

*   **max_norm** – (float) - The maximum norm value to clip gradients to.

`clip_norm`(_parameters:Union[Iterable[torch.nn.parameter.Parameter], torch.Tensor]_)[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#clip_norm "Permalink to this definition")
Clips the gradients of the given parameters to the maximum norm value.

Parameters
**parameters** – Union[Iterable[torch.nn.parameter.Parameter], torch.Tensor] - The parameters whose gradients will be clipped. If a single tensor is provided, its gradient will be clipped.

try:
   from habana_frameworks.torch.hpex.normalization import FusedClipNorm
except ImportError:
   raise ImportError("Please install habana_torch package")
   FusedNorm = FusedClipNorm(model.parameters(), args.max_grad_norm)

FusedNorm.clip_norm(model.parameters())

### Mixture of Experts Forward (MoE)[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#mixture-of-experts-forward-moe "Permalink to this headline")

Note

This feature is supported on Gaudi 3 and Gaudi 2 only.

This custom op is designed to replace the MoE block in Mixtral and LLaMA models. In Eager mode, this op is lowered into basic ops, which are used in the original Hugging Face implementation. Refer to [HuggingFace modelling_mixtral.py](https://github.com/huggingface/transformers/blob/2e24ee4dfa39cc0bc264b89edbccc373c8337086/src/transformers/models/mixtral/modeling_mixtral.py#L688) for more details. In Lazy and `torch.compile` modes, it utilizes a dedicated kernel optimized for Gaudi. This design ensures that computational resources are used efficiently, leading to faster execution times and improved overall performance. The following data types are supported: float32 and bfloat16 for both training and inference. Additionally, float8 and bfloat8 are supported for inference only.

The op supports the following:

*   MLP/Feed Forward structure of Mixtral and LLaMA, replacing the experts blocks along with the subsequent weighted sum in case where a token is sent to multiple experts.

*   Both the HuggingFace flavor of the MLP, where all 3 GEMM operations are separate, as well as the vLLM use case, where the first two GEMM operations are fused.

Each expert weight numbering is based on the order of the corresponding Linear operations and differs from the Mixtral HF/vLLM numbering. This means that for HF Mixtral, w2 and w3 are swapped, and for vLLM Mixtral, w13 is replaced by w12. In the HF LLaMA notation, w1 corresponds to gate_proj, w2 corresponds to up_proj, and w3 corresponds to down_proj.

Currently, the custom op supports training, but only for non-FP8 flavors and with disabled measurement_mode. During training, the op performs additional computations to calculate backward, such as storing intermediate outputs. To avoid these additional computations while running in inference mode, the op should be called within the inference context manager (`torch.inference_mode()`).

_class_`mixture_of_experts`(_hidden\_states_, _expert\_routing\_table_, _router\_weights_, _w1_, _w2_, _w12_, _w3_, _permuted\_weights_, _activation_, _experts\_min_, _experts\_max_, _*_, _recomp=True_)[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#mixture_of_experts "Permalink to this definition")Input hidden_states
(Tensor) - The input tensor containing the hidden states that will be processed by the experts.

Input expert_routing_table
(Tensor) - A tensor that maps each input to the corresponding experts that will process it.

Input router_weights
(Tensor) - Weights used by the router to determine the routing probabilities for each expert.

Input w1
(TensorList, optional) - Expert weights for the first matrix multiplication operation for non fused GEMM flavor. TensorList size is equal to the number of experts.

Input w2
(TensorList, optional) - Expert weights for the second matrix multiplication operation for non fused GEMM flavor. This can be concatenated with `w1` for compatibility with different frameworks. TensorList size is equal to the number of experts.

Input w12
(TensorList, optional) - Expert weights for the first matrix multiplication operation for fused GEMM flavor. TensorList size is equal to the number of experts.

Input w3
(TensorList) - Expert weights for the last matrix multiplication operation. TensorList size is equal to the number of experts.

Input d_scale_hidden_states
(TensorList or Scalar) - hidden_states scale for FP8. Used only in FP8 flavor. Scale can be provided in F32 or BF16 format.

Input d_scale_intermediate_hidden_states
(TensorList or ScalarList) - Third GEMM first input scale for FP8. Number of scales equals number of experts. Used only in FP8 flavor. This scale can be either provided by user or calculated dynamically in runtime. Scales can be provided in F32 or BF16 format.

Input d_scale_w1
(TensorList or ScalarList) - First GEMM weight scale for FP8. Number of scales equals number of experts. Used only in FP8 flavor. Scales can be provided in F32 or BF16 format.

Input d_scale_w2
(TensorList or ScalarList) - Second GEMM weight scale for FP8. Number of scales equals number of experts. Used only in FP8 flavor. Scales can be provided in F32 or BF16 format.

Input d_scale_w12
(TensorList or ScalarList) - First GEMM fused weight scale for FP8. Number of scales equals number of experts. Used only in FP8 flavor. Scales can be provided in F32 or BF16 format.

Input d_scale_w3
(TensorList or ScalarList) - Third GEMM weight scale for FP8. Number of scales equals number of experts. Used only in FP8 flavor. Scales can be provided in F32 or BF16 format.

Parameters
*   **block_size** – (int64_t) - The block size used in block-wise (de)quantization flavor. Used to upscale experts weights to BF16 with each scale corresponding to square block of given size.

*   **permuted_weights** – (bool) - flag used to specify if expert weights are already permuted.

*   **activation** – (std::string_view) - activation function used in MoE block. Supported activations are `gelu`, `relu` and `silu`.

*   **experts_min** – (int64_t) - used for device parallelism to support expert parallelism. It specifies for each device the experts subset it is responsible for. This is inclusive.

*   **experts_max** – (int64_t) - used for device parallelism to support expert parallelism. It specifies for each device the experts subset it is responsible for. This is inclusive.

*   **recomp** – (bool) - flag used in lazy and `torch.compile` modes during non-inference. It specifies if the operator should store additional intermediate outputs required for backward calculation or recompute them if needed. Recompute mode results in slower performance but requires less memory during training.

Params measurement_mode
(bool) - flag used in FP32 and BF16 flavor to measure absolute max values of third GEMM first operand for each expert. Used for static quantization dry runs.

Output
(Tensor or (Tensor, Tensor)) - The output of MoE block. Shape is equal to input shape. With “measurement_mode” parameter MoE returns two outputs.

 Example 1 - Non-Fused GEMM flavor 

import habana_frameworks.torch.core as htcore
import torch
import torch.nn.functional as F

dtype = torch.float
activation = "gelu"
hidden_dim = 64
ffn_dim = 224
num_experts = 8
num_tokens = 32
fused_weights = False
permuted_weights = False
k = 2
hidden_states = torch.randn((num_tokens, hidden_dim), dtype=dtype)
score = torch.randn((num_tokens, num_experts), dtype=torch.float32)
routing_weights = F.softmax(score, dim=1, dtype=torch.float32)
router_weights, expert_routing_table = torch.topk(routing_weights,
                                              k,
                                              dim=-1)
router_weights /= router_weights.sum(dim=-1, keepdim=True)
router_weights = router_weights.to(dtype=dtype)
w1 = [torch.randn((hidden_dim, ffn_dim), dtype=dtype).to("hpu") for _ in range(num_experts)]
w2 = [torch.randn((hidden_dim, ffn_dim), dtype=dtype).to("hpu") for _ in range(num_experts)]
w3 = [torch.randn((ffn_dim, hidden_dim), dtype=dtype).to("hpu") for _ in range(num_experts)]

with torch.inference_mode():
  result = torch.ops.hpu.mixture_of_experts(
      hidden_states.to("hpu"),
      expert_routing_table.to("hpu"),
      router_weights.to("hpu"),
      w1,
      w2,
      w3,
      permuted_weights,
      activation,
      0,
      num_experts - 1,
  )

 Example 2 - Fused GEMM Flavor 

import habana_frameworks.torch.core as htcore
import torch
import torch.nn.functional as F

dtype = torch.float
activation = "gelu"
hidden_dim = 64
ffn_dim = 224
num_experts = 8
num_tokens = 32
fused_weights = False
permuted_weights = False
k = 2
hidden_states = torch.randn((num_tokens, hidden_dim), dtype=dtype)
score = torch.randn((num_tokens, num_experts), dtype=torch.float32)
routing_weights = F.softmax(score, dim=1, dtype=torch.float32)
router_weights, expert_routing_table = torch.topk(routing_weights,
                                              k,
                                              dim=-1)
router_weights /= router_weights.sum(dim=-1, keepdim=True)
router_weights = router_weights.to(dtype=dtype)
w12 = [torch.randn((hidden_dim, 2 * ffn_dim), dtype=dtype).to("hpu") for _ in range(num_experts)]
w3 = [torch.randn((ffn_dim, hidden_dim), dtype=dtype).to("hpu") for _ in range(num_experts)]

with torch.inference_mode():
  result = torch.ops.hpu.mixture_of_experts(
      hidden_states.to("hpu"),
      expert_routing_table.to("hpu"),
      router_weights.to("hpu"),
      w12,
      w3,
      permuted_weights,
      activation,
      0,
      num_experts - 1,
  )

 Example 3 - Non-Fused GEMM flavor with measurement_mode 

import habana_frameworks.torch.core as htcore
import torch
import torch.nn.functional as F

dtype = torch.bfloat16
activation = "gelu"
hidden_dim = 64
ffn_dim = 224
num_experts = 8
num_tokens = 32
fused_weights = False
permuted_weights = False
k = 2
hidden_states = torch.randn((num_tokens, hidden_dim), dtype=dtype)
score = torch.randn((num_tokens, num_experts), dtype=torch.float32)
routing_weights = F.softmax(score, dim=1, dtype=torch.float32)
router_weights, expert_routing_table = torch.topk(routing_weights,
                                            k,
                                            dim=-1)
router_weights /= router_weights.sum(dim=-1, keepdim=True)
router_weights = router_weights.to(dtype=dtype)
w1 = [torch.randn((hidden_dim, ffn_dim), dtype=dtype).to("hpu") for _ in range(num_experts)]
w2 = [torch.randn((hidden_dim, ffn_dim), dtype=dtype).to("hpu") for _ in range(num_experts)]
w3 = [torch.randn((ffn_dim, hidden_dim), dtype=dtype).to("hpu") for _ in range(num_experts)]

with torch.inference_mode():
  result, amax = torch.ops.hpu.mixture_of_experts(
      hidden_states.to("hpu"),
      expert_routing_table.to("hpu"),
      router_weights.to("hpu"),
      w1,
      w2,
      w3,
      permuted_weights,
      activation,
      0,
      num_experts - 1,
      measurement_mode=True,
  )

 Example 4 - Non-Fused GEMM flavor with FP8 data type 

import habana_frameworks.torch.core as htcore
import torch
import torch.nn.functional as F

dtype = torch.bfloat16
fp8_dtype = torch.float8_e5m2
activation = "gelu"
hidden_dim = 64
ffn_dim = 224
num_experts = 8
num_tokens = 32
fused_weights = False
permuted_weights = False
k = 2
hidden_states = torch.randn((num_tokens, hidden_dim), dtype=dtype)
score = torch.randn((num_tokens, num_experts), dtype=dtype)
routing_weights = F.softmax(score, dim=1, dtype=dtype)
router_weights, expert_routing_table = torch.topk(routing_weights,
                                            k,
                                            dim=-1)
router_weights /= router_weights.sum(dim=-1, keepdim=True)
router_weights = router_weights.to(dtype=dtype)

d_scale_hidden_states = 3.27
d_scale_intermediate_hidden_states = [1.0 for _ in range(num_experts)]
d_scale_w1 = [4.35, 1.49, 1.12, 2.22, 8.33, 1.28, 2.94, 1.79]
d_scale_w2 = [1.10, 2.13, 2.78, 1.22, 3.45, 1.59, 1.35, 1.72]
d_scale_w3 = [6.67, 1.09, 2.08, 2.70, 1.56, 1.23, 1.89, 3.85]

hidden_states = (hidden_states / d_scale_hidden_states).to(fp8_dtype)
w1_hpu = [(torch.randn((hidden_dim, ffn_dim), dtype=dtype).to("hpu") / scale).to(fp8_dtype) for scale in d_scale_w1]
w2_hpu = [(torch.randn((hidden_dim, ffn_dim), dtype=dtype).to("hpu") / scale).to(fp8_dtype) for scale in d_scale_w2]
w3_hpu = [(torch.randn((ffn_dim, hidden_dim), dtype=dtype).to("hpu") / scale).to(fp8_dtype) for scale in d_scale_w3]

with torch.inference_mode():
  result = torch.ops.hpu.mixture_of_experts(
      hidden_states.to("hpu"),
      expert_routing_table.to("hpu"),
      router_weights.to("hpu"),
      w1_hpu,
      w2_hpu,
      w3_hpu,
      d_scale_hidden_states,
      d_scale_intermediate_hidden_states,
      d_scale_w1,
      d_scale_w2,
      d_scale_w3,
      permuted_weights,
      activation,
      0,
      num_experts - 1,
  )

 Example 5 - Non-Fused GEMM flavor with FP8 data type and dynamic quantization 

import habana_frameworks.torch.core as htcore
import torch
import torch.nn.functional as F

dtype = torch.bfloat16
fp8_dtype = torch.float8_e4m3fn
activation = "gelu"
hidden_dim = 64
ffn_dim = 224
num_experts = 8
num_tokens = 32
fused_weights = False
permuted_weights = False
k = 2
hidden_states = torch.randn((num_tokens, hidden_dim), dtype=dtype)
score = torch.randn((num_tokens, num_experts), dtype=dtype)
routing_weights = F.softmax(score, dim=1, dtype=dtype)
router_weights, expert_routing_table = torch.topk(routing_weights,
                                            k,
                                            dim=-1)
router_weights /= router_weights.sum(dim=-1, keepdim=True)
router_weights = router_weights.to(dtype=dtype)

# For per-token quantization, scales can be provided either as 1D tensor or unsqueezed 2D tensor
d_scale_hidden_states = torch.randn((num_tokens, 1), dtype=dtype).to("hpu")
d_scale_w1 = [1 + 0.1 * torch.randn((1, ffn_dim), dtype=dtype).to("hpu") for _ in range(num_experts)]
d_scale_w2 = [1 + 0.1 * torch.randn((1, ffn_dim), dtype=dtype).to("hpu") for _ in range(num_experts)]
d_scale_w3 = [1 + 0.1 * torch.randn((1, hidden_dim), dtype=dtype).to("hpu")  for _ in range(num_experts)]

hidden_states_hpu = (hidden_states.to("hpu") / d_scale_hidden_states).to(fp8_dtype)
w1_hpu = [(torch.randn((hidden_dim, ffn_dim), dtype=dtype).to("hpu") / scale).to(fp8_dtype) for scale in d_scale_w1]
w2_hpu = [(torch.randn((hidden_dim, ffn_dim), dtype=dtype).to("hpu") / scale).to(fp8_dtype) for scale in d_scale_w2]
w3_hpu = [(torch.randn((ffn_dim, hidden_dim), dtype=dtype).to("hpu") / scale).to(fp8_dtype) for scale in d_scale_w3]

with torch.inference_mode():
  result = torch.ops.hpu.mixture_of_experts(
      hidden_states_hpu,
      expert_routing_table.to("hpu"),
      router_weights.to("hpu"),
      w1_hpu,
      w2_hpu,
      w3_hpu,
      d_scale_hidden_states,
      d_scale_w1,
      d_scale_w2,
      d_scale_w3,
      permuted_weights,
      activation,
      0,
      num_experts - 1,
  )

 Example 6 - Non-Fused GEMM flavor with blockwise FP8 dequantization 

import habana_frameworks.torch.core as htcore
import torch
import torch.nn.functional as F

dtype = torch.bfloat16
fp8_dtype = torch.float8_e4m3fn
activation = "gelu"
hidden_dim = 64
ffn_dim = 224
num_experts = 8
num_tokens = 32
block_size = 30
fused_weights = False
permuted_weights = False
k = 2
hidden_states = torch.randn((num_tokens, hidden_dim), dtype=dtype)
score = torch.randn((num_tokens, num_experts), dtype=dtype)
routing_weights = F.softmax(score, dim=1, dtype=dtype)
router_weights, expert_routing_table = torch.topk(routing_weights,
                                            k,
                                            dim=-1)
router_weights /= router_weights.sum(dim=-1, keepdim=True)
router_weights = router_weights.to(dtype=dtype)

w1_hpu = [torch.randn((hidden_dim, ffn_dim), dtype=dtype).to("hpu").to(fp8_dtype) for _ in range(num_experts)]
w2_hpu = [torch.randn((hidden_dim, ffn_dim), dtype=dtype).to("hpu").to(fp8_dtype) for _ in range(num_experts)]
w3_hpu = [torch.randn((ffn_dim, hidden_dim), dtype=dtype).to("hpu").to(fp8_dtype) for _ in range(num_experts)]

hidden_dim_block = (hidden_dim + block_size - 1) // block_size
ffn_dim_block = (ffn_dim + block_size - 1) // block_size

d_scale_w1 = [torch.randn((hidden_dim_block, ffn_dim_block), dtype=dtype).to("hpu") for _ in range(num_experts)]
d_scale_w2 = [torch.randn((hidden_dim_block, ffn_dim_block), dtype=dtype).to("hpu") for _ in range(num_experts)]
d_scale_w3 = [torch.randn((ffn_dim_block, hidden_dim_block), dtype=dtype).to("hpu") for _ in range(num_experts)]

with torch.inference_mode():
  result = torch.ops.hpu.mixture_of_experts(
      hidden_states.to("hpu"),
      expert_routing_table.to("hpu"),
      router_weights.to("hpu"),
      w1_hpu,
      w2_hpu,
      w3_hpu,
      d_scale_w1,
      d_scale_w2,
      d_scale_w3,
      block_size,
      permuted_weights,
      activation,
      0,
      num_experts - 1,
  )

 Example 7 - Non-Fused GEMM flavor - Training 

import habana_frameworks.torch.core as htcore
import torch
import torch.nn.functional as F

dtype = torch.float
activation = "gelu"
hidden_dim = 64
ffn_dim = 224
num_experts = 8
num_tokens = 32
fused_weights = False
permuted_weights = False
k = 2
hidden_states = torch.randn((num_tokens, hidden_dim), dtype=dtype, requires_grad=True)
score = torch.randn((num_tokens, num_experts), dtype=torch.float32, requires_grad=True)
routing_weights = F.softmax(score, dim=1, dtype=torch.float32)
router_weights, expert_routing_table = torch.topk(routing_weights, k, dim=-1)
router_weights /= router_weights.sum(dim=-1, keepdim=True)
router_weights = router_weights.to(dtype=dtype)
w1 = [
    torch.randn((hidden_dim, ffn_dim), dtype=dtype, requires_grad=True, device="hpu")
    for _ in range(num_experts)
]
w2 = [
    torch.randn((hidden_dim, ffn_dim), dtype=dtype, requires_grad=True, device="hpu")
    for _ in range(num_experts)
]
w3 = [
    torch.randn((ffn_dim, hidden_dim), dtype=dtype, requires_grad=True, device="hpu")
    for _ in range(num_experts)
]

result = torch.ops.hpu.mixture_of_experts(
    hidden_states.to("hpu"),
    expert_routing_table.to("hpu"),
    router_weights.to("hpu"),
    w1,
    w2,
    w3,
    permuted_weights,
    activation,
    0,
    num_experts - 1,
    recomp=True,
)

result.backward(torch.randn_like(result))

[previous Handling Dynamic Shapes](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html "previous page")[next HPU Graphs for Training](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/HPU_Graphs_Training.html "next page")

By Habana Labs

 © Copyright 2026, Habana Labs.
