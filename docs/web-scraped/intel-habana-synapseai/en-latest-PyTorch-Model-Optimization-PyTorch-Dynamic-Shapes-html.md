# Source: https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html

Title: Handling Dynamic Shapes — Gaudi Documentation 1.23.0 documentation

URL Source: https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html

Published Time: Tue, 27 Jan 2026 14:00:20 GMT

Markdown Content:
Handling Dynamic Shapes — Gaudi Documentation 1.23.0 documentation
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
    *   [Handling Dynamic Shapes](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#)
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

*   [Types of Dynamicity](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#types-of-dynamicity)
*   [Detecting and Mitigating Dynamicity Overview](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#detecting-and-mitigating-dynamicity-overview)
*   [Graph Compiler Dynamicity Support](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#graph-compiler-dynamicity-support)
*   [Dynamic Shapes due to Varying Inputs](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#dynamic-shapes-due-to-varying-inputs)
    *   [Detecting Dynamic Inputs](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#detecting-dynamic-inputs)
    *   [Mitigation Through Bucketing and Padding](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#mitigation-through-bucketing-and-padding)
        *   [Preprocessing Input Dataset](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#preprocessing-input-dataset)
        *   [Saving Bucketing Results](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#saving-bucketing-results)
        *   [Variable Batch Size](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#variable-batch-size)

*   [Dynamic Shapes due to Ops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#dynamic-shapes-due-to-ops)
    *   [Detecting Dynamic Ops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#detecting-dynamic-ops)
    *   [Mitigation Techniques for Dynamic Ops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#mitigation-techniques-for-dynamic-ops)
        *   [Replacing Dynamic Ops with Static Ops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#replacing-dynamic-ops-with-static-ops)
        *   [Explicit CPU Fallback](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#explicit-cpu-fallback)
        *   [Splitting Dynamic and Static Sections](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#splitting-dynamic-and-static-sections)

*   [Dynamic Shapes in Distributed Training](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#dynamic-shapes-in-distributed-training)
*   [Case Study Using Wav2vec2 for Dynamic Inputs to Models](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#case-study-using-wav2vec2-for-dynamic-inputs-to-models)
    *   [Bucketing and Padding Solution Example](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#bucketing-and-padding-solution-example)

Handling Dynamic Shapes
=======================

On this Page
------------

*   [Types of Dynamicity](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#types-of-dynamicity)
*   [Detecting and Mitigating Dynamicity Overview](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#detecting-and-mitigating-dynamicity-overview)
*   [Graph Compiler Dynamicity Support](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#graph-compiler-dynamicity-support)
*   [Dynamic Shapes due to Varying Inputs](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#dynamic-shapes-due-to-varying-inputs)
    *   [Detecting Dynamic Inputs](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#detecting-dynamic-inputs)
    *   [Mitigation Through Bucketing and Padding](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#mitigation-through-bucketing-and-padding)
        *   [Preprocessing Input Dataset](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#preprocessing-input-dataset)
        *   [Saving Bucketing Results](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#saving-bucketing-results)
        *   [Variable Batch Size](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#variable-batch-size)

*   [Dynamic Shapes due to Ops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#dynamic-shapes-due-to-ops)
    *   [Detecting Dynamic Ops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#detecting-dynamic-ops)
    *   [Mitigation Techniques for Dynamic Ops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#mitigation-techniques-for-dynamic-ops)
        *   [Replacing Dynamic Ops with Static Ops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#replacing-dynamic-ops-with-static-ops)
        *   [Explicit CPU Fallback](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#explicit-cpu-fallback)
        *   [Splitting Dynamic and Static Sections](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#splitting-dynamic-and-static-sections)

*   [Dynamic Shapes in Distributed Training](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#dynamic-shapes-in-distributed-training)
*   [Case Study Using Wav2vec2 for Dynamic Inputs to Models](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#case-study-using-wav2vec2-for-dynamic-inputs-to-models)
    *   [Bucketing and Padding Solution Example](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#bucketing-and-padding-solution-example)

Handling Dynamic Shapes[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#handling-dynamic-shapes "Permalink to this headline")
========================================================================================================================================================================

This document uses “dynamic shapes” as a broad term describing model behaviors where certain topologies generate variable output tensor shapes due to dynamic input data or operators. This dynamicity may cause constant re-compilations, leading to longer training time.

The following sections discuss methods to detect dynamic shapes and mitigate their impact on model performance.

Types of Dynamicity[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#types-of-dynamicity "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Dynamic shapes can be broadly classified into two categories:

*   Inputs - Dynamic shapes due to varying input shapes during training, such as:

    *   Varying sentence lengths in language models

    *   Differing image resolutions in image model

*   Ops - Dynamic shapes due to ops where the output shape depends on the specific input data, rather than just the input shapes, such as ops with non-inferable output shapes based solely on input data.

Detecting and Mitigating Dynamicity Overview[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#detecting-and-mitigating-dynamicity-overview "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Dynamicity, resulting from changing input shapes or dynamic ops, can lead to multiple recompilations, causing a longer training time and reducing performance. Below are the guidelines to detect and mitigate this issue:

1.   **Detecting model recompilation** - To detect if the model is recompiling, set the following environment flags: `PT_HPU_METRICS_FILE=/root/metricslog.json`. The image below displays the text `graph_compilation`, which is dumped into the specified JSON file when the process exits. For static graphs, a reduction in recompilations is expected after a few steps. If recompilations continue to occur after adding the above flags, go to step 2.

[![Image 2: ../../_images/recompiles.png](https://docs.habana.ai/en/latest/_images/recompiles.png)](https://docs.habana.ai/en/latest/_images/recompiles.png)

1.   **Enabling dynamicity support from graph compiler** - To enable dynamicity support, set the `PT_HPU_ENABLE_REFINE_DYNAMIC_SHAPES=1` flag, as it is disabled by default. For further details, refer to [Graph Compiler Dynamicity Support](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#graph-compiler-dynamicity-support). If recompilations occur, or you encounter instability and want to achieve better performance, go to step 3 and 4.

2.   **Detecting dynamic shapes due to varying inputs** - Use the `data_dynamicity` tool to generate a report on input dynamicity as described in [Detecting Dynamic Inputs](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#detect-inputs). If there is a large amount of variability in the input data, use data bucketing and padding as described in [Mitigation Through Bucketing and Padding](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#mitigation).

3.   **Detecting dynamic shapes due to ops** - Use the `detect_recompilation_auto_model` tool to automatically detect which part of the model has dynamic ops as described in [Detecting Dynamic Ops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#detect-ops). If the model has dynamic ops, replace the dynamic ops with static ops as described in [Replacing Dynamic Ops with Static Ops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#static-ops). If replacing dynamic ops with static ops is not possible, split dynamic and static sections to make recompiling section smaller as described in [Splitting Dynamic and Static Sections](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#splitting-ops).

4.   If you are running steps 2-4 in a multi-card scenario, enable recipe caching via `PT_HPU_RECIPE_CACHE_CONFIG`. For more details, refer to [Runtime Environment Variables](https://docs.habana.ai/en/latest/PyTorch/Reference/Runtime_Flags.html#pytorch-runtime-flags). This allows one card to use the previously compiled graphs from another card.

Graph Compiler Dynamicity Support[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#graph-compiler-dynamicity-support "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To enable dynamicity support, set the `PT_HPU_ENABLE_REFINE_DYNAMIC_SHAPES=1`, as it is disabled by default. If a model experiences excessive recompilations due to dynamic data or ops, this variable can be set to enable the Intel Gaudi PyTorch bridge and graph compiler to automatically manage dynamic shapes in model scripts. The graphs will be automatically bucketed and padded into ranges to achieve a common size, reducing recompilations and improving performance when working with dynamic workloads.

In a multi-card scenario, enable recipe caching via `PT_HPU_RECIPE_CACHE_CONFIG`. For more details, refer to [Runtime Environment Variables](https://docs.habana.ai/en/latest/PyTorch/Reference/Runtime_Flags.html#pytorch-runtime-flags). This allows one card to use previously compiled graphs from another card. If recompilations continue to exist, or you encounter instability, refer to the following sections to detect dynamicity and find tips on rewriting the model.

Dynamic Shapes due to Varying Inputs[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#dynamic-shapes-due-to-varying-inputs "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Detecting Dynamic Inputs[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#detecting-dynamic-inputs "Permalink to this headline")

The `data_dynamicity` tool detects the distribution of the input data’s shapes and generates a report on input dynamicity. The below examples demonstrate the tool usage.

*   MNIST dataset:

> from habana_frameworks.torch.utils.experimental import data_dynamicity
> import torchvision
> from torch.utils.data import DataLoader
> 
> # Creating a sample MNIST dataloader
> mnist_ds = torchvision.datasets.MNIST('mnist', download=True, transform=torchvision.transforms.ToTensor())
> mnist_dl = DataLoader(mnist_ds, batch_size=7, num_workers=2)
> 
> data_dynamicity(mnist_dl)  
> Expected output:
> 
> [![Image 3: ../../_images/dataloader_analysis_tool.png](https://docs.habana.ai/en/latest/_images/dataloader_analysis_tool.png)](https://docs.habana.ai/en/latest/_images/dataloader_analysis_tool.png) 
> The MNIST dataset has a constant image shape, but two distinct input shapes are obtained, since the last batch has less number of images if there is no `drop_last=True` (in mnist_dl = DataLoader). In this case input dynamicity is low, so no changes are required for the input.

*   Food101 dataset:

from habana_frameworks.torch.utils.experimental import data_dynamicity
import torchvision
from torch.utils.data import DataLoader
import torch

def collate(batch):
   dim1 = min([k[0].shape[1] for k in batch])
   dim2 = min([k[0].shape[2] for k in batch])
   images = torch.stack([k[0][:,:dim1,:dim2] for k in batch])
   labels = torch.tensor([k[1] for k in batch])
   return (images,labels)

food101_ds = torchvision.datasets.Food101('food101', download=True, transform=torchvision.transforms.ToTensor())
food101_dl = DataLoader(food101_ds, batch_size=7, num_workers=2, collate_fn=collate)
data_dynamicity(food101_dl)  
This dataset contains images of different shapes. In the example above, batches are created by cropping the images to the size of the smallest image in each batch.

A large amount of input dynamicity is obtained for Food101:

> Number of unique shapes:  66
> # There is a lot of dynamicity in input data shapes

If there is a large amount of variability in the input data, data padding and/or data bucketing can be used. Refer to the section below.

### Mitigation Through Bucketing and Padding[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#mitigation-through-bucketing-and-padding "Permalink to this headline")

Bucketing and padding can reduce the number of unique shapes in input data. The input data shapes are divided into buckets of varying sizes, and data points are padded up to the smallest bucket larger than the largest data in each batch. In bucketing algorithms, the number of buckets is a hyperparameter. Choosing a large number of buckets causes many recompilations, while choosing a low number of buckets requires excessive padding and, therefore, causes unnecessary computations.

The example below shows how to take a random dataset of wav files, create two buckets and then sort and pad the data.

[![Image 4: ../../_images/bucketing_and_padding.png](https://docs.habana.ai/en/latest/_images/bucketing_and_padding.png)](https://docs.habana.ai/en/latest/_images/bucketing_and_padding.png)

Bucketing algorithms can be classified into two categories. You can use any novel padding/bucketing strategy to get the best tradeoff between bucketing algorithm time, compilation delays and HPU runtime speeds. The following table lists the suggested bucketing algorithms:

| Bucketing Algorithm Type | Description |
| --- | --- |
| Optimization-based | These algorithms have a criterion function to optimize. For example, the linear programming approach to reduce amount of padding wastage is used in [fairseq](https://github.com/HabanaAI/Fairseq/blob/1.17.0/fairseq/data/bucket_utils.py). Usually these methods are slower, but are more optimal when using less padding. |
| Fast heuristics-based | These bucketing algorithms are quick and easy to use. However, these methods usually have more padding wastage than the optimization-based methods. * [percentile-based bucketing](https://github.com/HabanaAI/Fairseq/blob/1.17.0/fairseq/data/data_utils.py#L555), which is also discussed in the [Case Study Using Wav2vec2 for Dynamic Inputs to Models](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#case-study). * Constant width bucketing where each bucket is of constant width between minimum and maximum data length. * Padding to max length. |

#### Preprocessing Input Dataset[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#preprocessing-input-dataset "Permalink to this headline")

When the input dataset is large, processing all the shapes in it, especially for costlier optimization based bucketing algorithms, might be too slow. To bypass this issue, perform the following:

*   Shuffle the shapes of the dataset and pick a small number of shapes to pass to the bucketing algorithm, reducing its workload.

*   Rather than creating a histogram for each shape, create a histogram with a wider bin, so that multiple contiguous shapes fall in the same bin.

#### Saving Bucketing Results[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#saving-bucketing-results "Permalink to this headline")

If the bucketing algorithm takes a lot of time, computing it every time you run the script is inefficient. You can store the results of the bucketing algorithm based on the hash of the input shapes. For example, see [here](https://github.com/HabanaAI/Fairseq/blob/1.17.0/fairseq/data/bucket_utils.py#L58). For example:

import hashlib
lst = [2, 4, 5, 3, 6, 3, 2]
key = hashlib.sha256(bytes(sorted(lst))).hexdigest().upper()

#### Variable Batch Size[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#variable-batch-size "Permalink to this headline")

You can adjust the batch size using bucketing. When using a fixed batch size, shorter input data may not fully utilize the device because a larger batch size could have been accommodated. If the batch size is too large, it might lead to Out of Memory errors when processing larger input data. Thus, it is advisable to use a larger batch size for shorter sequences and vice versa: `batch_size=max_num_words/sentence_length`.

Refer to [Memory Stats APIs](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#memory-stats-apis) for more information on memory usage.

Note

When there is a possibility of dynamic shapes distribution, running bucketing is beneficial. Some examples of multiple distributions are:

> *   Multiple inputs - A model might have two inputs, each with its own dynamic distribution of input shapes. Running bucketing separately on both inputs is recommended. An example of such a scenario is translation task, where the [source](https://github.com/HabanaAI/Fairseq/blob/b2917d7eeddfc487d4fd78a9d4a884ac5202230f/fairseq/data/language_pair_dataset.py#L271) and [target](https://github.com/HabanaAI/Fairseq/blob/b2917d7eeddfc487d4fd78a9d4a884ac5202230f/fairseq/data/language_pair_dataset.py#L283) language sentences might have different distributions.

*   Multiple datasets - If you use multiple datasets, running bucketing algorithm for each dataset separately is recommended. For example, [Roboflow](https://public.roboflow.com/) is made of 100 different datasets, all training on the same model in 100 different runs.

Dynamic Shapes due to Ops[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#dynamic-shapes-due-to-ops "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For certain ops, such as the following, the output shape cannot be predicted, even if the input shape is known:

*   [Unique](https://pytorch.org/docs/stable/generated/torch.unique.html)

*   Single input [Where](https://pytorch.org/docs/stable/generated/torch.where.html) (identical to Nonzero)

*   [Nonzero](https://pytorch.org/docs/stable/generated/torch.nonzero.html)

*   [Boolean indexing](https://discuss.pytorch.org/t/boolean-indexing/39626)

*   [Argwhere](https://pytorch.org/docs/stable/generated/torch.argwhere.html#torch.argwhere)

*   [Arange](https://pytorch.org/docs/stable/generated/torch.arange.html)

Note

For arbitrary inputs, `torch.arange` behaves dynamically, but in specific cases such as `torch.arange(x, x+5)`, the output has a static shape. However, the graph compiler may incorrectly classify it as static. To bypass this, rewrite the computation as `x + torch.arange(0, 5)`. 

### Detecting Dynamic Ops[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#detecting-dynamic-ops "Permalink to this headline")

To detect dynamic ops, perform a simple string search in the repo for ops or run the script with `GRAPH_VISUALIZATION=1` to create a `.graph_dumps` folder and monitor it to see if the number of graphs dumped keeps increasing. If dynamic shapes are present, multiple recompilations cause the number of dumps in the `.graph_dumps` folder to increase.

Note

To detect dynamic ops, make sure to use same sized inputs to avoid recompilations due to varying input shapes.

To find out which part of the model has dynamic ops, use the `detect_recompilation_auto_model` tool. The code snippet below shows inference on a model with a dynamic op (boolean indexing) and dynamic inputs (changing batch size):

from habana_frameworks.torch.utils.experimental import detect_recompilation_auto_model
import torch

class InnerNet(torch.nn.Module):
   def  __init__ (self):
      super(InnerNet, self). __init__ ()
      self.conv = torch.nn.Conv2d(1, 8, 3, 3)

   def forward(self, x):
      x = torch.flatten(self.conv(x), 1)
      x = x[x>0] # This is dynamic
      return x.sum()

net = torch.nn.Sequential(torch.nn.ReLU(), InnerNet())
net = detect_recompilation_auto_model(net)

for bs in [20,20,20,30,30]: #Input shape changes at 4th step
   inp = torch.rand(bs, 1, 50, 50).to('hpu')
   print(net(inp))
net.analyse_dynamicity() # Call this after a few steps to generate the dynamicity report

This produces the following report (along with the CSV versions of it):

[![Image 5: ../../_images/dynmodel_analysis_tool1.png](https://docs.habana.ai/en/latest/_images/dynmodel_analysis_tool1.png)](https://docs.habana.ai/en/latest/_images/dynmodel_analysis_tool1.png)

1.   The first four lines of the first table show all four modules recompile since it is the initial step.

2.   The next two lines show `Net` and `InnerNet` recompile. The “Comment” column, however, shows that `InnerNet` might be dynamic because it recompiled even without dynamic children modules. `Net` may not be dynamic as it might have recompiled because its child (`InnerNet`) has recompiled.

3.   The next two lines show step 2 which is similar to step 1.

4.   The next four lines show step 3, where a new input shape is seen, so every module recompiles as expected shown in the “Comment” column.

5.   The last two lines for step 4 point to `InnerNet` as having dynamic ops.

The table below is a summarized view that shows which modules recompile the most. As expected, `Net/1` of type `InnerNet` (and its parent) show up at the top.

[![Image 6: ../../_images/dynmodel_analysis_tool2.PNG](https://docs.habana.ai/en/latest/_images/dynmodel_analysis_tool2.PNG)](https://docs.habana.ai/en/latest/_images/dynmodel_analysis_tool2.PNG)

Note

The `detect_recompilation_auto_model` tool slows down model execution, so it is only intended for debugging purposes and should be removed for the actual run.

### Mitigation Techniques for Dynamic Ops[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#mitigation-techniques-for-dynamic-ops "Permalink to this headline")

#### Replacing Dynamic Ops with Static Ops[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#replacing-dynamic-ops-with-static-ops "Permalink to this headline")

Removing dynamicity needs a case-by-case inspection but the general guideline is to identify the section of the code where dynamicity starts and ends, then replace it with static code. See the below examples.

*   **Example 1** - [This example](https://github.com/microsoft/ProphetNet/blob/0a1b59cb95783319b7b58ede65b768587dc49daf/ProphetNet_Multi/prophetnet/ngram_criterions.py#L79) of boolean indexing which is dynamic can be replaced to make the code static:

> #Dynamic code
> 
> non_pad_mask = targets.ne(self.padding_idx).view(-1)
> smooth_loss = smooth_loss[non_pad_mask]
> smooth_loss = smooth_loss.sum()
> 
> #Static Code
> 
> non_pad_mask = targets.ne(self.padding_idx).view(-1)
> smooth_loss = smooth_loss.squeeze() * non_pad_mask.int()
> smooth_loss = smooth_loss.sum()

*   **Example 2** - If a tensor A, B, and C of length N is given, with `C[i]` being `–1`, the corresponding elements are filtered out. The remaining elements are then multiplied `A[i]*B[i]`, and the results are added up.

Pseudocode: `res = sum([A[i]*B[i] for i in range(len(C)) if C[i] != -1])`.

> #Dynamic code
> 
> import torch
> import habana_frameworks.torch.core as htcore
> 
> A = torch.tensor([1,2,3,4,5]).to('hpu')
> B = torch.tensor([6,7,8,9,10]).to('hpu')
> C = torch.tensor([1,-1,1,1,-1]).to('hpu')
> 
> indices=torch.where(C!=-1)
> A_filtered=torch.gather(A, 0, indices[0])
> B_filtered=torch.gather(B, 0, indices[0])
> 
> res_dyn = torch.sum(A_filtered * B_filtered)
> 
> #Static Code
> 
> res_tmp = A*B
> prod_filtererd = torch.where(C!=-1, res_tmp, torch.zeros_like(res_tmp))
> res_stat = torch.sum(prod_filtererd)
> 
> assert (res_stat == res_dyn).item()  
> In this example we identify the start of dynamicity (where) and its end (sum) and replace it with a static implementation. The diagram below shows the two possible paths, with the dynamic nodes and tensors marked in red.

[![Image 7: ../../_images/Static_Implementation.png](https://docs.habana.ai/en/latest/_images/Static_Implementation.png)](https://docs.habana.ai/en/latest/_images/Static_Implementation.png)

#### Explicit CPU Fallback[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#explicit-cpu-fallback "Permalink to this headline")

In normal mode, ops that are not supported on HPU are already automatically placed on the CPU as explained in [Placement of Ops on HPU](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#placement-of-ops). Explicit CPU fallback refers to moving certain ops to the CPU (and possibly later bringing them back on the HPU) explicitly for dynamic ops. For example:

#say x is on HPU
z = torch.unique(x) #this op is done on HPU because input x is on HPU
# can be replaced by:
x=x.to('cpu')
z = torch.unique(x) # runs on cpu
#move tensors back to HPU if needed
x = x.to('hpu')
z = z.to('hpu')

Sections on the CPU can be sped up using [torch jit](https://pytorch.org/docs/stable/generated/torch.jit.script.html) by wrapping them in the @torch.jit.script decorator.

#### Splitting Dynamic and Static Sections[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#splitting-dynamic-and-static-sections "Permalink to this headline")

Consider a case where the network starts with static layers, has a few dynamic layers, and then ends with static layers. Under normal circumstances, the whole network recompiles in each step, making execution slow. However, we can add `mark_step` between the static and dynamic sections of the network (refer to [mark_step](https://docs.habana.ai/en/latest/PyTorch/Reference/mark_step.html#mark-step-section) section). With this change, the static part compiles only once, and the dynamic part is smaller (compared to the whole network) and hence compiles faster.

# The whole network static1->dynamic->static2 recompiles
x = static1(x)
x = dynamic(x)
x = static2(x)

# After splitting them, now only dynamic recompiles. static1 and static2 compile only once
x = static1(x)
mark_step()
x = dynamic(x)
mark_step()
x = static2(x)

Note

When possible, replacing dynamic code with static code, as detailed in [Replacing Dynamic Ops with Static Ops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#static-ops), is recommended. If it cannot be done, try [CPU fallback](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#explicit-cpu) or [splitting dynamic and static ops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#splitting-ops) or do not make any change to figure out which option is fastest. Depending on the model, each method has its own advantages and disadvantages. CPU fallback might trigger costly host-to-device or device-to-host copies. While splitting reduces the compile time, there is still dynamicity and hence compilations happen.

Dynamic Shapes in Distributed Training[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#dynamic-shapes-in-distributed-training "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If we have `S` shapes and `N` cards, in the worst case scenario, `N*(S-1) + 1` compilation delays is observed. This means only one card is compiling a new shape, while the other cards receive shapes they have compiled before. Those cards finish compiling faster and remain idle. The figures below show the inefficiency of cards having to sit idle while waiting to compile new shapes (highlighted).

[![Image 8: ../../_images/Unique_Shapes.png](https://docs.habana.ai/en/latest/_images/Unique_Shapes.png)](https://docs.habana.ai/en/latest/_images/Unique_Shapes.png)

To mitigate this issue, use across rank caching. When a new shape is encountered, its recipe is saved to file, allowing other cards to use it instead of recompiling each new shape. To do this, set the below:

PT_HPU_RECIPE_CACHE_CONFIG=/tmp/iter1_recipe_cache/,true,1024

Case Study Using Wav2vec2 for Dynamic Inputs to Models[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#case-study-using-wav2vec2-for-dynamic-inputs-to-models "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Models with dynamic input shapes are constantly recompiled resulting in longer training time. In audio models, it is common that the input contains wave files with variant length. The steps below outline the bucketing and padding solution steps required to achieve better training performance on Gaudi using [Wav2vec2](https://github.com/HabanaAI/Fairseq/tree/1.17.0/examples/wav2vec) as an example.

### Bucketing and Padding Solution Example[¶](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#bucketing-and-padding-solution-example "Permalink to this headline")

1.   Sort the wave files according to the length. This is to make sure that wave files with similar length are grouped together to decrease possible padding.

2.   Define the size of buckets. According to the distribution of wave file length in the dataset and the number of bucket slots the user defined, define the length of each bucket slot. A general rule in Wave2vec is to define the length of a bucket so that the number of files falling into different buckets are similar.

Below is the example code that Wav2vec uses to define the length of different bucket via numpys percentile function, where `sizes` is an array that contains the size of all wave files and `num_buckets` is the number of buckets you want to use:

def get_buckets(sizes, num_buckets):
   buckets = np.unique(
      np.percentile(
            sizes,
            np.linspace(0, 100, num_buckets + 1),
            interpolation="lower",
      )[1:]
   )
   return buckets  
3.   Split the dataset into different batches. For example, in Wav2vec, a threshold value is defined to make sure the total file size in one batch does not exceed this threshold value. Refer to the example [here](https://github.com/HabanaAI/Fairseq/blob/1.17.0/fairseq/tasks/fairseq_task.py#L296).

4.   Padding:

    1.   Pad wave files in the same batch to the same file size. To make sure each wave file in the same batch has the same size, it is padded to the max file size in that batch.

    2.   Pad wave files in the same batch to the bucket size. When the file length in the batch is not the same as the bucket length, it needs to be padded to match the length of the bucket with the closest distance. This way, even if there are a lot of batches, the shape of those batches will be limited.

You can find a padding example using Wav2vec2 [here](https://github.com/HabanaAI/Fairseq/blob/1.17.0/fairseq/data/audio/raw_audio_dataset.py#L126).

With this bucketing and padding solution, the number of dynamic shapes of the input to Wav2vec can be greatly decreased. Refer to the implementation in [Wav2vec2 Model Reference on GitHub](https://github.com/HabanaAI/Fairseq/tree/1.17.0/examples/wav2vec).

[previous Optimizations of PyTorch Models](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html "previous page")[next Fused Optimizers and Custom Ops for Intel Gaudi](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html "next page")

By Habana Labs

 © Copyright 2026, Habana Labs.
