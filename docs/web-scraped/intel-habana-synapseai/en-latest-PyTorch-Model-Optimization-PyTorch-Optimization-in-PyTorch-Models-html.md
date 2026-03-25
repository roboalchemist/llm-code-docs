# Source: https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html

Title: Optimizations of PyTorch Models — Gaudi Documentation 1.23.0 documentation

URL Source: https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html

Published Time: Tue, 27 Jan 2026 14:00:21 GMT

Markdown Content:
Optimizations of PyTorch Models — Gaudi Documentation 1.23.0 documentation
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
    *   [Optimizations of PyTorch Models](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#)
    *   [Inference Optimizations](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Inference_Optimization.html)
    *   [Handling Dynamic Shapes](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html)
    *   [Fused Optimizers and Custom Ops for Intel Gaudi](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html)
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

*   [General Model Optimizations](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#general-model-optimizations)
    *   [PyTorch Execution Modes Usage](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#pytorch-execution-modes-usage)
    *   [Placement of Ops on HPU](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#placement-of-ops-on-hpu)
    *   [Usage of ``` mark_step ```](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#usage-of-mark-step)
    *   [Batch Size](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#batch-size)
    *   [PyTorch Mixed Precision](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#pytorch-mixed-precision)
    *   [Usage of Fused Optimizers and Custom Ops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#usage-of-fused-optimizers-and-custom-ops)
    *   [Perf Tool and TensorBoard Model Scanning](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#perf-tool-and-tensorboard-model-scanning)

*   [Model-specific Optimizations](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#model-specific-optimizations)
    *   [Using Fused Scaled Dot Product Attention (FusedSDPA)](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#using-fused-scaled-dot-product-attention-fusedsdpa)
        *   [FusedSDPA Custom Features](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#fusedsdpa-custom-features)
            *   [Operation Modes](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#operation-modes)
            *   [Fast Softmax](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#fast-softmax)
            *   [Valid Sequence Length](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#valid-sequence-length)
            *   [Returning Dropout Mask](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#returning-dropout-mask)
            *   [Returning Attention Probabilities](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#returning-attention-probabilities)

    *   [Disk Caching Eviction Policy](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#disk-caching-eviction-policy)
    *   [Adjust the Gradient Bucket Size in Multi-Card/Server Training](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#adjust-the-gradient-bucket-size-in-multi-card-server-training)
    *   [Setting Gradients as View of Gradient Buckets in Multi-Card/Server Training](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#setting-gradients-as-view-of-gradient-buckets-in-multi-card-server-training)
    *   [Reducing the Printing Quantities Frequency](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#reducing-the-printing-quantities-frequency)
    *   [Pinning Memory For Dataloader](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#pinning-memory-for-dataloader)
    *   [Avoiding Constant Variables in Loops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#avoiding-constant-variables-in-loops)
    *   [Weight Sharing](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#weight-sharing)
    *   [Switch Host Memory Allocator](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#switch-host-memory-allocator)

Optimizations of PyTorch Models
===============================

On this Page
------------

*   [General Model Optimizations](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#general-model-optimizations)
    *   [PyTorch Execution Modes Usage](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#pytorch-execution-modes-usage)
    *   [Placement of Ops on HPU](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#placement-of-ops-on-hpu)
    *   [Usage of ``` mark_step ```](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#usage-of-mark-step)
    *   [Batch Size](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#batch-size)
    *   [PyTorch Mixed Precision](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#pytorch-mixed-precision)
    *   [Usage of Fused Optimizers and Custom Ops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#usage-of-fused-optimizers-and-custom-ops)
    *   [Perf Tool and TensorBoard Model Scanning](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#perf-tool-and-tensorboard-model-scanning)

*   [Model-specific Optimizations](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#model-specific-optimizations)
    *   [Using Fused Scaled Dot Product Attention (FusedSDPA)](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#using-fused-scaled-dot-product-attention-fusedsdpa)
        *   [FusedSDPA Custom Features](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#fusedsdpa-custom-features)
            *   [Operation Modes](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#operation-modes)
            *   [Fast Softmax](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#fast-softmax)
            *   [Valid Sequence Length](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#valid-sequence-length)
            *   [Returning Dropout Mask](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#returning-dropout-mask)
            *   [Returning Attention Probabilities](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#returning-attention-probabilities)

    *   [Disk Caching Eviction Policy](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#disk-caching-eviction-policy)
    *   [Adjust the Gradient Bucket Size in Multi-Card/Server Training](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#adjust-the-gradient-bucket-size-in-multi-card-server-training)
    *   [Setting Gradients as View of Gradient Buckets in Multi-Card/Server Training](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#setting-gradients-as-view-of-gradient-buckets-in-multi-card-server-training)
    *   [Reducing the Printing Quantities Frequency](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#reducing-the-printing-quantities-frequency)
    *   [Pinning Memory For Dataloader](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#pinning-memory-for-dataloader)
    *   [Avoiding Constant Variables in Loops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#avoiding-constant-variables-in-loops)
    *   [Weight Sharing](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#weight-sharing)
    *   [Switch Host Memory Allocator](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#switch-host-memory-allocator)

Optimizations of PyTorch Models[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#optimizations-of-pytorch-models "Permalink to this headline")
========================================================================================================================================================================================================

The following optimization methods can be applied to PyTorch models run on the Intel® Gaudi® AI accelerator to enhance their performance.

General Model Optimizations[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#general-model-optimizations "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The optimization methods below can be used with all PyTorch models.

### PyTorch Execution Modes Usage[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#pytorch-execution-modes-usage "Permalink to this headline")

For the recommended PyTorch execution modes usage, refer to the [Recommended Usage](https://docs.habana.ai/en/latest/PyTorch/Reference/PyTorch_Gaudi_Theory_of_Operations.html#pt-execution-modes-workflow) section.

### Placement of Ops on HPU[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#placement-of-ops-on-hpu "Permalink to this headline")

When a model is ported to HPU, the Intel Gaudi software stack distributes ops between CPU and HPU. In order to achieve an optimal performance on HPU, avoid execution of ops on CPU.

The distribution is based on whether the op is registered on PyTorch with HPU backend and whether the requested data type is supported on HPU. Execution of an op automatically falls back to CPU if it is not registered with its backend as HPU or if the op is registered but the requested data type is not supported on HPU.

To enable CPU fallback logs to check whether ops were executed on CPU, set the environment variables as shown below:

ENABLE_CONSOLE=true LOG_LEVEL_PT_FALLBACK=1

**Example:**

When _aten::digamma_ op falls back to CPU, the logs display the below:

CPU fallback digamma : self=HPUBFloat16Type

Frequency of op and op name that were executed on CPU:
1       aten::digamma

### Usage of `mark_step`[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#usage-of-mark-step "Permalink to this headline")

`mark_step` is added after backward and optimizer step; however, adding `mark_step` to further optimize your model may be used. The following are examples of when adding `mark_step` is beneficial:

*   `mark_step` is added to avoid Out of Memory issues. In cases where the size of the graph exceeds memory usage, the graph is broken using `mark_step`. This reduces memory consumption, overcoming Out of Memory issues. See [DeepSpeed Bert](https://github.com/HabanaAI/Model-References/tree/1.23.0/PyTorch/nlp/DeepSpeedExamples/deepspeed-bert) for example.

*   `mark_step` can also be used when the graph has static and dynamic shapes. Due to dynamicity, the graph is recompiled causing performance degradation. Adding `mark_step` after static graph may reduce recompilations or recompile with small dynamic graphs.

For further information on `mark_step`, refer to [mark_step](https://docs.habana.ai/en/latest/PyTorch/Reference/mark_step.html#mark-step-section) section.

### Batch Size[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#batch-size "Permalink to this headline")

Throughput is usually improved when the batch sizes are large. However, there are limitations that apply when using large batch size:

*   Batch size is limited by Gaudi’s device memory (HBM) size that is fixed. Usually, larger batch size means more memory consumption in the device.

*   Large batch size cannot be used when low latency instead of throughput is required.

*   Large batch size in each Gaudi device may impact the convergence in data parallelism distributed training. For example, the highest global batch size that gives ResNet50 convergence is around 32K. This means that with an increasing number of Gaudi devices, batch size should be reduced in each device.

The below table provides examples of batch sizes used in different models, all using mixed precision.

| Models | Batch Size |
| --- | --- |
| ResNet50 | 256 |
| Bert Large pre-training Phase 1 | 64 |
| Bert Large pre-training Phase 2 | 8 |
| MaskRCNN | 4 |

### PyTorch Mixed Precision[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#pytorch-mixed-precision "Permalink to this headline")

For details on how to run mixed precision training of PyTorch models on Gaudi, refer to [Mixed Precision Training with PyTorch Autocast](https://docs.habana.ai/en/latest/PyTorch/PyTorch_Mixed_Precision/index.html#pytorch-mixed-precision-training).

### Usage of Fused Optimizers and Custom Ops[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#usage-of-fused-optimizers-and-custom-ops "Permalink to this headline")

Create a custom op for PyTorch optimizers (FusedSGD, FusedAdamW) and other complex ops (FusedClipNorm) to minimize host performance overheads of running many small ops. This can improve the overlap of execution between host and device.

The Intel Gaudi PyTorch package provides its own implementation of PyTorch ops customized for Gaudi. For more details, see [Fused Optimizers and Custom Ops for Intel Gaudi](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#custom-operators).

**Example:**

For the custom _FusedSGD_ operator, refer to [ResNet50 FusedSGD](https://github.com/HabanaAI/Model-References/blob/1.23.0/PyTorch/computer_vision/classification/torchvision/train.py).

### Perf Tool and TensorBoard Model Scanning[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#perf-tool-and-tensorboard-model-scanning "Permalink to this headline")

The `habana_perf_tool` scans and provides guidance on existing log files generated for TensorBoard, without having to run the TensorBoard UI. The tool scans the log file, shows a list of metrics that it measures, and then provides specific guidance for optimization, such as increasing batch size or MME and TPC usages and timings. This analysis capability is also built directly into TensorBoard. The tool can be initiated with the following command:

root@ubuntu2204:~/traces# habana_perf_tool --trace trace_example.json

Model-specific Optimizations[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#model-specific-optimizations "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The optimization methods below are supported on specific PyTorch models.

### Using Fused Scaled Dot Product Attention (FusedSDPA)[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#using-fused-scaled-dot-product-attention-fusedsdpa "Permalink to this headline")

FusedSDPA is a fused implementation of `torch.nn.functional.scaled_dot_product_attention()` for Gaudi. It maintains the same functionality as the original function with reduced memory usage and implements selected Flash Attention optimization approaches. For further information on the original functionality and parameters, refer to [Scaled Dot Product Attention](https://pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html).

Note

*   FusedSDPA is designed to accelerate training and inference of Transformer-based models.

*   The supported data types are FP32 and BF16. Running inference with FP8 data type is possible with [Intel Neural Compressor (INC)](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#inference-using-fp8).

*   Memory usage profiling to characterize memory reduction on standard topologies is in progress. Users are advised to try both modes and choose the optimal mode for a given topology.

*   FusedSDPA does not support broadcasting on batch size dimension. Input tensors should have same batch size.

#### FusedSDPA Custom Features[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#fusedsdpa-custom-features "Permalink to this headline")

The features described in the following sections are configured via FusedSDPA custom API parameters. For further details, see [hpex/kernels/FusedSDPA](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#fusedsdpa-section).

##### Operation Modes[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#operation-modes "Permalink to this headline")

FusedSDPA has two operation modes: Recompute mode (default) and No-recompute mode. The operation mode can be selected either using the context manager API variable or the custom API parameter.

Note

Do not use the context manager mechanism to set the operation mode when running workloads in `torch.compile` mode as this causes breaks in the compiled graphs. These breaks occur due to PyTorch’s current handling of context managers. Instead, use the API parameter to set the FusedSDPA operation mode and avoid graph breaks. To maintain consistent code across `torch.compile` and other execution modes, topology scripts can rely on the API parameter mechanism regardless of the execution mode.

*   Recompute mode - This is the default mode. In this mode, necessary parts of the forward pass are recomputed during backward pass to reduce memory usage. This helps topologies to run with a higher batch size and/or sequence length. In addition to memory optimizations related to recompute, this mode has additional memory optimizations. You can try running this mode in inference scenarios that result in Out of Memory issues with non-fused attention implementations.

*   Non-recompute mode - In this mode, recomputing is not done. Therefore, this mode can have larger memory needs compared to recompute mode. This mode still provides memory advantages over non-fused attention implementations. It is also beneficial as recomputation is avoided.

Setting operation mode using the `recompute_mode` API parameter:

*   Set `True` for recompute mode.

*   Set `False` for non-recompute mode.

*   Set `None` to use the context variable mechanism to set the operation mode.

**Example:**

import torch
from habana_frameworks.torch.hpex.kernels import FusedSDPA
import habana_frameworks.torch.hpu as ht

query = torch.rand(32, 8, 128, 64, dtype=torch.bfloat16, device="hpu")
key = torch.rand(32, 8, 128, 64, dtype=torch.bfloat16, device="hpu")
value = torch.rand(32, 8, 128, 64, dtype=torch.bfloat16, device="hpu")
# Set recompute_mode API parameter to False to run in non-recompute mode
sdpa_out = FusedSDPA.apply(query, key, value, None, 0.0, True, None, 'None', False)
print(sdpa_out.to("cpu"))

Setting the operation mode using context manager mechanism:

*   `habana_frameworks.torch.hpu.sdp_kernel(enable_recompute = True)` - Context manager based control to temporarily/locally (i.e, within the current context) enable recompute mode.

*   `habana_frameworks.torch.hpu.sdp_kernel(enable_recompute = False)` - Context manager based control to temporarily/locally (i.e, within the current context) disable recompute mode.

*   `habana_frameworks.torch.hpu.enable_recompute_sdp(True)` - Globally enable recompute. The recompute state set by this API remains effective until this API is used again to change the state.

*   `habana_frameworks.torch.hpu.enable_recompute_sdp(False)` - Globally disable recompute. The recompute state set by this API remains effective until this API is used again to change the state.

*   `habana_frameworks.torch.hpu.recompute_sdp_enabled()` - Query if recompute mode is enabled or not.

**Example:**

import torch
from habana_frameworks.torch.hpex.kernels import FusedSDPA
import habana_frameworks.torch.hpu as ht

query = torch.rand(32, 8, 128, 64, dtype=torch.bfloat16, device="hpu")
key = torch.rand(32, 8, 128, 64, dtype=torch.bfloat16, device="hpu")
value = torch.rand(32, 8, 128, 64, dtype=torch.bfloat16, device="hpu")
# Use the context manager to set non-recompute mode and leave the recompute_mode API parameter as None
with habana_frameworks.torch.hpu.sdp_kernel(enable_recompute = False):
    sdpa_out = FusedSDPA.apply(query, key, value, None, 0.1, True, None, 'None')
    print(sdpa_out.to("cpu"))

##### Fast Softmax[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#fast-softmax "Permalink to this headline")

FusedSDPA supports fast Softmax function execution with `softmax_mode='fast'` enabled. If the default `softmax_mode='None'` is set, the default Softmax is used. The feature is supported in both non-triangular and triangular masking modes.

**Example:**

import torch
from habana_frameworks.torch.hpex.kernels import FusedSDPA
import habana_frameworks.torch.hpu as ht

query = torch.rand(32, 8, 128, 64, dtype=torch.bfloat16, device="hpu")
key = torch.rand(32, 8, 128, 64, dtype=torch.bfloat16, device="hpu")
value = torch.rand(32, 8, 128, 64, dtype=torch.bfloat16, device="hpu")
with ht.sdp_kernel(enable_recompute = True):
    sdpa_out = FusedSDPA.apply(query, key, value, None, 0.0, True, None, 'fast')
    print(sdpa_out.to("cpu"))

Note

*   Using fast Softmax may affect inference accuracy.

*   Only BF16 data type is supported with fast Softmax.

*   Fast Softmax is not supported when running training in recompute mode with `is_causal = False`.

##### Valid Sequence Length[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#valid-sequence-length "Permalink to this headline")

The valid sequence length represents the actual length of the sequence, excluding any padding. Sequences with varying lengths can be padded to a common maximum length, either at the beginning (left padding) or the end (right padding). The region corresponding to the padding is ignored during Softmax calculations when attention computations are run. In certain topologies, combining triangular masking (`is_causal=True`) with specifying the valid sequence length allows to ignore the invalid areas more efficiently. FusedSDPA’s `valid_seq_len` and `seq_padding_type` API parameters facilitate this optimization.

The example below illustrates a case involving a batch of three sequences with a maximum length of 128. The actual sequence lengths are 100, 120, and 80, with padding added after each sequence:

> import torch
> from habana_frameworks.torch.hpex.kernels import FusedSDPA
> import habana_frameworks.torch.hpu as ht
> 
>   query = torch.rand(3, 8, 128, 64, dtype=torch.bfloat16, device="hpu") # seq len=128 after padding
>   key = torch.rand(3, 8, 128, 64, dtype=torch.bfloat16, device="hpu")   # seq len=128 after padding
>   value = torch.rand(3, 8, 128, 64, dtype=torch.bfloat16, device="hpu") # seq len=128 after padding
>   valid_s_len = torch.tensor([100, 120, 80], dtype=torch.int32, device="hpu") # actual seq len of 100,120,80
>   sdpa_out = FusedSDPA.apply(query, key, value, None, 0.0, True, None, 'fast', False, valid_s_len, "right")
>   print(sdpa_out.to("cpu"))

Note

*   This feature is supported only with `is_causal=True` and `attn_mask=None`.

*   `seq_padding_type` is relevant only when `valid_seq_len` is not `None`.

##### Returning Dropout Mask[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#returning-dropout-mask "Permalink to this headline")

FusedSDPA returns dropout mask if `return_dropout_mask=True`. The parameter is used for debug purposes only.

**Example:**

import torch
from habana_frameworks.torch.hpex.kernels import FusedSDPA
import habana_frameworks.torch.hpu as ht

  query = torch.rand(3, 8, 128, 64, dtype=torch.bfloat16, device="hpu")
  key = torch.rand(3, 8, 128, 64, dtype=torch.bfloat16, device="hpu")
  value = torch.rand(3, 8, 128, 64, dtype=torch.bfloat16, device="hpu")

  sdpa_out, drp_out_mask = FusedSDPA.apply(query, key, value, None, 0.1, True, None, 'None', False, None, "right", True)
  print(sdpa_out.to("cpu"))
  print(drp_out_mask.to("cpu"))

Note

Returning dropout mask is supported only in no-recompute mode.

##### Returning Attention Probabilities[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#returning-attention-probabilities "Permalink to this headline")

FusedSDPA returns attention probabilities (Softmax operation output) if `return_return_attn_probs=True`.

**Example:**

import torch
from habana_frameworks.torch.hpex.kernels import FusedSDPA
import habana_frameworks.torch.hpu as ht

  query = torch.rand(3, 8, 128, 64, dtype=torch.bfloat16, device="hpu")
  key = torch.rand(3, 8, 128, 64, dtype=torch.bfloat16, device="hpu")
  value = torch.rand(3, 8, 128, 64, dtype=torch.bfloat16, device="hpu")

  sdpa_out, attn_probs = FusedSDPA.apply(query, key, value, None, 0.0, True, None, 'None', False, None, "right", False, True)
  print(sdpa_out.to("cpu"))
  print(attn_probs.to("cpu"))

Output order for `return_dropout_mask` and `return_attn_probs`:

| return_dropout_mask | return_attn_probs | Output Order |
| --- | --- | --- |
| False | False | sdpa_out |
| False | True | sdpa_out, attn_probs |
| True | False | sdpa_out, dropout_mask |
| True | True | sdpa_out, attn_probs, dropout_mask |

Note

Returning attention probabilities is supported only in inference when `query`, `key`, and `value` data type is either FP32 or BF16.

### Disk Caching Eviction Policy[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#disk-caching-eviction-policy "Permalink to this headline")

Disk caching is a mechanism that limits the number of graph compilations for both training and inference workloads. Initially, the Intel Gaudi PyTorch bridge checks if a recipe is already cached in memory and then in disk cache. Refer to the [Runtime Environment Variables](https://docs.habana.ai/en/latest/PyTorch/Reference/Runtime_Flags.html#pytorch-runtime-flags) section to configure the disk caching variables. If you want to keep the disk cache size under a predefined threshold, an eviction policy can be implemented.

When a compiled recipe is added to the cache, the algorithm checks whether the total size of all recipes fits the cache directory max size that is specified in `PT_HPU_RECIPE_CACHE_CONFIG`. When the total size of the cache directory, including new recipes, exceeds the defined maximum size, the Intel Gaudi PyTorch bridge iterates through the recipes in the cache. It removes the oldest recipes on the file system first until the total size is under the limit.

**Highlights:**

*   Eviction is performed after the recipe is serialized and stored on disk by every worker.

*   To ensure that eviction logic removes recipes in a coherent way, only one process may perform eviction at a time. This is implemented using an `eviction.lock` file in disk cache directory and locking it using flock ([https://linux.die.net/man/2/flock](https://linux.die.net/man/2/flock)). The cache directory is locked by a particular worker only for eviction time.

*   Both serialization and eviction are performed in a separate thread, so graph launch is not delayed.

*   Since the size of recipe being stored is unknown prior to serialization, the eviction tries to keep the size of cache directory `<= 0.99 * <RECIPE_CACHE_SIZE_MB>`. It limits the possibility of exceeding the specified cache dir size during next serialization.

*   If info logs from `PT_HABHELPER` are enabled, `LOG_LEVEL_PT_HABHELPER=2`, then you should see the following PyTorch log message: “Removed <recipe id> successfully. Disk cache size after removal: <size>”. If too many eviction messages are observed, it is recommended to reset the recipe cache directory size to a larger number. For specific models, you can fine-tune this size to get the best performance.

**Example:**

PT_HPU_RECIPE_CACHE_CONFIG=/tmp/iter1_recipe_cache/,true,1024 \
python your_model.py

In the above example, the recipes are stored in `/tmp/iter1_recipe_cache/`. The cache is cleared at the beginning of each script execution and the size of the recipe cache is limited to 1024MB.

### Adjust the Gradient Bucket Size in Multi-Card/Server Training[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#adjust-the-gradient-bucket-size-in-multi-card-server-training "Permalink to this headline")

Based on the size of the model, the size of the gradient bucket can be adjusted to minimize the number of allreduce invocations in the backward pass of every training iteration. Refer to [PyTorch DDP](https://pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html) for more details.

**Example:**

In ResNet50, bucket size of 100MB is optimal whereas ResNext101 requires bucket size of 200MB. Refer to the implementation [here](https://github.com/HabanaAI/Model-References/blob/1.23.0/PyTorch/computer_vision/classification/torchvision/train.py).

### Setting Gradients as View of Gradient Buckets in Multi-Card/Server Training[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#setting-gradients-as-view-of-gradient-buckets-in-multi-card-server-training "Permalink to this headline")

PyTorch DDP allows parameter gradient tensors to be views of the gradient bucket. This improves performance as device-to-device copies can be reduced and also reduces device memory requirement. Refer to [PyTorch DDP](https://pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html) for more details.

**Example:**

Refer to [ResNet50](https://github.com/HabanaAI/Model-References/blob/1.23.0/PyTorch/computer_vision/classification/torchvision/train.py).

### Reducing the Printing Quantities Frequency[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#reducing-the-printing-quantities-frequency "Permalink to this headline")

Some output messaging should be reduced or eliminated for enhanced performance when models have been fully optimized and set up for production use. Two examples are provided below:

*   Reporting loss using `loss.item()` or calculating loss to display.

*   Showing the progress bar (using TDQM or other libraries) during runtime.

Both of these items rely on additional communication between the host CPU and Gaudi to calculate loss or progress and then display the results. Printing these tensors in the training script requires pulling the device tensors to the host CPU and, therefore, requires device execution to finish. This can result in non-overlapped execution between host and device leading to sub-optimal performance.

To reduce loss calculation or progress bar update, set the print frequency `--print-freq` to a high value or eliminate it altogether. You can set the `--print-freq` variable in the model run command to a size similar to the optimizer step size. For the progress bar, it is recommended to wait until a run completes 20 or more iterations to minimize unnecessary synchronization.

### Pinning Memory For Dataloader[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#pinning-memory-for-dataloader "Permalink to this headline")

Pinning the memory while instantiating the dataloader avoids a redundant copy in host during the training iteration. Refer to support [PyTorch Dataloader](https://pytorch.org/docs/stable/data.html#memory-pinning) for more details.

**Example:**

Refer to [ResNet50 Dataloader](https://github.com/HabanaAI/Model-References/blob/1.23.0/PyTorch/computer_vision/classification/torchvision/train.py).

### Avoiding Constant Variables in Loops[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#avoiding-constant-variables-in-loops "Permalink to this headline")

Avoiding loop iterator variables within a loop may reduce the recompilations occurrences in consecutive iterations. This loop iterator variable can create different constant operators in the execution graph each time the loop is executed.

For example, in the [original V-Diffusion code](https://github.com/crowsonkb/v-diffusion-pytorch/blob/93b6a54986d8259837a100046777fba52d812554/diffusion/sampling.py#L212) the value of the iterator variable changes each time the loop iterates. To avoid triggering recompilations after each iteration, the loop iterator variable `i` is not used in [the Intel Gaudi V-Diffusion](https://github.com/HabanaAI/Model-References/blob/cb8230e63db23694fe067955f12ab4411783fcc6/PyTorch/generative_models/v-diffusion/diffusion/sampling.py#L234) model. See the example below:

for i in range(4, num_steps):
     # The following 3 lines remove graph recompilation (variable "i" is not used)
     t_1 = steps[0] # before: steps[i]
     t_2 = steps[1] # before: steps[i+1]
     steps = torch.roll(steps, shifts=(-1), dims=(0))

**Example:**

Refer to the implementation for [the Intel Gaudi V-Diffusion](https://github.com/HabanaAI/Model-References/blob/cb8230e63db23694fe067955f12ab4411783fcc6/PyTorch/generative_models/v-diffusion/diffusion/sampling.py#L234) model and compare it with the [original V-Diffusion code](https://github.com/crowsonkb/v-diffusion-pytorch/blob/93b6a54986d8259837a100046777fba52d812554/diffusion/sampling.py#L212).

### Weight Sharing[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#weight-sharing "Permalink to this headline")

Weight sharing is a technique in which the module weights are shared among two or more layers. Weights can be shared using PyTorch with Gaudi only if they are created inside the module. See the example below:

import torch
import habana_frameworks.torch.core as ht

# Example module
class WeightShareModule(torch.nn.Module):
 def  __init__ (self):
     super(WeightShareModule, self). __init__ ()
     self.a = torch.nn.Parameter(torch.ones([2]))
     self.b = torch.nn.Parameter(torch.ones([2]))
 def forward(self, input):
     c = self.a*input + self.b*input
     return c

module = WeightShareModule()
#module.a and module.b are shared
module.a = module.b
# Move the module to HPU device
module.to("hpu")

**Example:**

Refer to [BERT Pre-Training](https://github.com/HabanaAI/Model-References/blob/1.23.0/PyTorch/nlp/bert/run_pretraining.py) on GitHub.

### Switch Host Memory Allocator[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#switch-host-memory-allocator "Permalink to this headline")

For deep learning workloads, jemalloc or TCMalloc achieve better performance by reusing memory as much as possible. Both Jemalloc and TCMalloc are pre-installed using the [Intel Gaudi dockers](https://docs.habana.ai/en/latest/Installation_Guide/index.html#gaudi-installation-guide).

*   Jemalloc - A general purpose malloc implementation that emphasizes fragmentation avoidance and scalable concurrency support.

*   TCMalloc - Features optimizations to speed up program executions including holding memory in caches to speed up access of commonly-used objects. Holding such caches even after deallocation also helps avoid costly system calls if such memory is later re-allocated.

By default, HPU uses TCMalloc allocator for host memory. For some workloads, this can cause host Out-Of-Memory issues as it holds memory in cache. This can be mitigated adjusting TCMalloc cache size via its config or switching to the jemalloc allocator using the `LD_PRELOAD` environment variable.

To switch to the jemalloc allocator:

*   Clear the existing allocator from LD_PRELOAD

*   export LD_PRELOAD=/lib/x86_64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD

[previous Model Optimization Checklist](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_Getting_Started.html "previous page")[next Handling Dynamic Shapes](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html "next page")

By Habana Labs

 © Copyright 2026, Habana Labs.
