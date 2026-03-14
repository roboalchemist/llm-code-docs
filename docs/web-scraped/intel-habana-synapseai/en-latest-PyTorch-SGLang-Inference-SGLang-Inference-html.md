# Source: https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html

Title: Inference Using SGLang — Gaudi Documentation 1.23.0 documentation

URL Source: https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html

Published Time: Fri, 06 Mar 2026 20:28:13 GMT

Markdown Content:
Inference Using SGLang — Gaudi Documentation 1.23.0 documentation
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
    *   [Inference Using SGLang](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#)
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

*   [Prerequisites](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#prerequisites)
    *   [Creating and Running a Docker Image for Gaudi](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#creating-and-running-a-docker-image-for-gaudi)
    *   [Building and Installing SGLang for Gaudi](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#building-and-installing-sglang-for-gaudi)
    *   [Sending an Inference Request](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#sending-an-inference-request)
    *   [Analyzing SGLang Logs](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#analyzing-sglang-logs)
    *   [Troubleshooting](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#troubleshooting)

*   [Troubleshooting OOM Errors](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#troubleshooting-oom-errors)
    *   [Guidelines for Performance Tuning](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#guidelines-for-performance-tuning)

*   [Performance Monitoring](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#performance-monitoring)
*   [Environment Variables](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#environment-variables)

Inference Using SGLang
======================

On this Page
------------

*   [Prerequisites](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#prerequisites)
    *   [Creating and Running a Docker Image for Gaudi](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#creating-and-running-a-docker-image-for-gaudi)
    *   [Building and Installing SGLang for Gaudi](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#building-and-installing-sglang-for-gaudi)
    *   [Sending an Inference Request](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#sending-an-inference-request)
    *   [Analyzing SGLang Logs](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#analyzing-sglang-logs)
    *   [Troubleshooting](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#troubleshooting)

*   [Troubleshooting OOM Errors](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#troubleshooting-oom-errors)
    *   [Guidelines for Performance Tuning](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#guidelines-for-performance-tuning)

*   [Performance Monitoring](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#performance-monitoring)
*   [Environment Variables](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#environment-variables)

Inference Using SGLang[¶](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#inference-using-sglang "Permalink to this headline")
==============================================================================================================================================================

This document outlines the process of deploying models with SGLang using the Intel® Gaudi® AI accelerator. It covers how to create a Gaudi-compatible SGLang Docker image, build and install the SGLang Inference Server, and send inference requests.

Prerequisites[¶](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#prerequisites "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------

*   Intel® Gaudi® software and drivers installed. Refer to [Driver and Software Installation](https://docs.habana.ai/en/latest/Installation_Guide/Driver_Installation.html#driver-installation).

*   Dockers (optional - for containerized deployment). Refer to [Docker Installation](https://docs.habana.ai/en/latest/Installation_Guide/Additional_Installation/Docker_Installation.html#docker-installation).

### Creating and Running a Docker Image for Gaudi[¶](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#creating-and-running-a-docker-image-for-gaudi "Permalink to this headline")

Since a SGLang server is launched within a Docker container, a Docker image tailored for Gaudi is needed. Follow the instructions below to create and run a Docker image for SGLang on Gaudi.

1.   Clone SGLang repository:

git clone https://github.com/HabanaAI/sglang-fork.git
cd sglang-fork  
2.   Build the SGLang Docker image optimized for Gaudi:

docker build -f docker/Dockerfile.gaudi -t sglang-gaudi:latest .  
3.   Launch the SGLang container with Gaudi device access:

docker run -it --runtime=habana \
    -e HABANA_VISIBLE_DEVICES=all \
    -e OMPI_MCA_btl_vader_single_copy_mechanism=none \
    --cap-add=sys_nice \
    --net=host \
    --ipc=host \
    -v /path/to/models:/models \
    sglang-gaudi:latest  

### Building and Installing SGLang for Gaudi[¶](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#building-and-installing-sglang-for-gaudi "Permalink to this headline")

To build and install SGLang with Gaudi, follow the steps below:

1.   Clone the SGLang repository with Gaudi support:

git clone https://github.com/HabanaAI/sglang-fork.git
cd sglang-fork  
2.   Install the required dependencies:

pip install -e python[all_hpu]  

### Sending an Inference Request[¶](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#sending-an-inference-request "Permalink to this headline")

The following sections describe the available methods to send inference requests to SGLang running on Gaudi.

 OpenAI-Compatible Server 

Use an API endpoint that mimics the OpenAI interface, allowing for easy integration with existing OpenAI-compatible clients.

1.   Start the SGLang server with OpenAI-compatible API:

> python -m sglang.launch_server \
>     --model-path meta-llama/Meta-Llama-3.1-8B \
>     --host 0.0.0.0 \
>     --port 30000 \
>     --tp-size 1 \
>     --dtype bfloat16

2.   Send requests using OpenAI Python client:

> from openai import OpenAI
> 
> client = OpenAI(
>     base_url="http://localhost:30000/v1",
>     api_key="EMPTY"
> )
> 
> response = client.chat.completions.create(
>     model="meta-llama/Meta-Llama-3.1-8B",
>     messages=[
>         {"role": "user", "content": "What is the capital of France?"}
>     ],
>     max_tokens=100,
>     temperature=0.7
> )
> 
> print(response.choices[0].message.content)

 Native SGLang API 

Use SGLang’s native API for advanced features such as structured generation:

> import sglang as sgl
> from sglang import function, system, user, assistant, gen, select
> 
> @function
> def multi_turn_question(s, question_1, question_2):
>     s += system("You are a helpful assistant.")
>     s += user(question_1)
>     s += assistant(gen("answer_1", max_tokens=256))
>     s += user(question_2)
>     s += assistant(gen("answer_2", max_tokens=256))
> 
> # Set the default backend
> sgl.set_default_backend(sgl.Runtime(model_path="meta-llama/Meta-Llama-3.1-8B"))
> 
> # Run the function
> state = multi_turn_question.run(
>     question_1="What is the capital of the United States?",
>     question_2="List two local attractions there."
> )
> 
> for key, value in state.text():
>     print(f"{key}: {value}")

For a list of popular models and supported configurations validated on Gaudi, see the supported models documentation.

### Analyzing SGLang Logs[¶](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#analyzing-sglang-logs "Permalink to this headline")

This section demonstrates how to interpret SGLang server logs using a basic example that runs the [Meta-Llama-3.1-8B](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B) model on a Gaudi-based SGLang server with default settings:

python -m sglang.launch_server --model-path meta-llama/Meta-Llama-3.1-8B --dtype bfloat16 --tp-size 1 --host 0.0.0.0 --port 30000

Below is an excerpt from the initial server log output:

    INFO 2025-01-15 10:30:15 server.py:123] Loading model meta-llama/Meta-Llama-3.1-8B
    INFO 2025-01-15 10:30:16 habana_worker.py:89] Initializing Gaudi device: hpu:0
 INFO 2025-01-15 10:30:16 habana_worker.py:156] Model loading on hpu:0 took 12.8 GiB of device memory (12.8 GiB/94.62 GiB used) and 950 MiB of host memory INFO 2025-01-15 10:30:17 habana_worker.py:178] HPU Graph compilation started INFO 2025-01-15 10:30:18 habana_worker.py:201] Free device memory: 81.82 GiB, 73.64 GiB usable (memory_utilization=0.9), 65.27 GiB reserved for KV cache    INFO 2025-01-15 10:30:18 habana_executor.py:67] # HPU blocks: 4181, # CPU blocks: 512
 INFO 2025-01-15 10:30:19 habana_worker.py:234] Cache engine initialization took 65.27 GiB of device memory (78.07 GiB/94.62 GiB used) and 1.2 GiB of host memory

These logs illustrate the memory usage pattern during the model initialization phase. They highlight how much device memory is consumed for loading model weights, compiling HPU Graphs, and allocating KV cache memory prior to the warmup stage. This data is useful for tuning memory utilization and optimizing server performance.

Below is an excerpt from the warmup phase logs:

> INFO 2025-01-15 10:30:25 habana_model_runner.py:445] Warmup started with batch_sizes=[1, 2, 4, 8] and seq_lens=[128, 256, 512, 1024, 2048]
> INFO 2025-01-15 10:30:27 habana_model_runner.py:467] Prefill warmup: batch_size=1, seq_len=128, time=0.12s
> INFO 2025-01-15 10:30:28 habana_model_runner.py:467] Prefill warmup: batch_size=1, seq_len=256, time=0.15s
> INFO 2025-01-15 10:30:30 habana_model_runner.py:467] Prefill warmup: batch_size=4, seq_len=1024, time=0.35s
> INFO 2025-01-15 10:30:32 habana_model_runner.py:489] Decode warmup: batch_size=8, seq_len=128, time=0.08s
> INFO 2025-01-15 10:30:33 habana_model_runner.py:512] Warmup finished in 8.2 secs, allocated 156 MiB of additional device memory
> INFO 2025-01-15 10:30:33 server.py:234] SGLang server is ready at http://0.0.0.0:30000

By analyzing this warmup phase, you gain insight into the remaining available memory for runtime overhead and how much headroom remains for further optimization. These details help you fine-tune memory utilization settings by balancing the requirements between HPU Graphs and KV Cache according to your specific workload and performance goals.

### Troubleshooting[¶](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#troubleshooting "Permalink to this headline")

This section provides troubleshooting tips for common OOM errors as well as instructions for reducing server startup time during development.

Troubleshooting OOM Errors[¶](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#troubleshooting-oom-errors "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Out-of-memory (OOM) errors may occur due to factors such as available HPU memory, model size, or input sequence length. If the standard inference command fails, the following options can help mitigate OOM issues:

| **Option** | **Description** |
| --- | --- |
| `--mem-fraction-static` | Increases the memory fraction pre-allocated for HPU cache. Helps allocate more space for the KV cache to avoid OOM errors. |
| `--max-running-requests` | Reduces the number of concurrent requests in a batch. This lowers the overall KV cache usage. |
| `--tp-size` | Enables tensor parallelism by sharding model weights across multiple HPUs. This frees up memory on each HPU for the KV cache. |
| `--chunked-prefill-size` | Breaks large prefill sequences into smaller chunks. Reduces peak memory consumption during the prefill stage. |

### Guidelines for Performance Tuning[¶](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#guidelines-for-performance-tuning "Permalink to this headline")

The following guidelines can help you optimize performance. Results may vary depending on your specific workload and configuration:

| Aspect | Guidelines |
| --- | --- |
| Warmup | Enable warmup during deployment for optimal performance. Warmup duration depends on factors such as input/output sequence lengths, batch size, number of prefill/decode combinations, and data type. Typically, warmup takes from 30 seconds to a few minutes. |
| Memory Management | HPU Graphs and KV Cache share the same memory pool, therefore, balancing them is crucial: - Maximizing KV Cache size supports larger batches and higher throughput. - Enabling HPU Graphs reduces host overhead and can help lower latency. - Control static memory allocation fraction using `--mem-fraction-static`. |
| Batch Size Optimization | * Use `--max-running-requests` to limit the number of concurrent requests. * Use `--max-prefill-tokens` to restrict tokens processed during the prefill stage. * Use `--max-total-tokens` to set the maximum total tokens processed per request. |
| Chunked Prefill | Use `--chunked-prefill-size` to split large prefill sequences into smaller chunks, which helps: - Improve memory utilization - Reduce time-to-first-token for long sequences - Stabilize memory usage patterns |
| Tensor Parallelism | Use `--tp-size` to shard model weights across multiple HPUs, which: - Reduces per-device memory usage - Enables serving larger models - Can improve throughput for certain workloads |
| Data Types | Choose precision formats based on your needs: - `--dtype bfloat16`: Standard precision balancing accuracy and performance - `--dtype float16`: Lower precision with potential speed gains, may affect output quality |
| Advanced Features | * **RadixAttention**: Enables automatic prefix caching for efficiency with repeated prefixes. * **Speculative Decoding**: Uses smaller draft models to accelerate generation. * **Continuous Batching**: Automatically batches requests to improve throughput. |

Performance Monitoring[¶](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#performance-monitoring "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------

Monitor the following key metrics during inference:

| Metric | Description |
| --- | --- |
| Throughput | Tokens generated per second |
| Latency | Time to first token and inter-token latency |
| Memory Usage | HPU memory utilization |
| Request Queue | Number of pending requests |

Use the built-in metrics endpoint to track these metrics:

curl http://localhost:30000/metrics

Environment Variables[¶](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Inference.html#environment-variables "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------

The following table provides the environment variables for performance tuning:

[previous SGLang Quick Start Guide](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/SGLang_Quick_Start.html "previous page")[next Managing and Reducing SGLang Warmup Time](https://docs.habana.ai/en/latest/PyTorch/SGLang_Inference/Managing_SGLang_Warmup_Time.html "next page")

By Habana Labs

 © Copyright 2026, Habana Labs.
