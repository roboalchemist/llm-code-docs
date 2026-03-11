# Source: https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html

Title: Creating and Executing Media Pipeline — Gaudi Documentation 1.23.0 documentation

URL Source: https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html

Markdown Content:
Creating and Executing Media Pipeline — Gaudi Documentation 1.23.0 documentation
===============
- [x] 

Toggle navigation sidebar

 - [x] 

Toggle in-page Table of Contents

 

[![Image 7: logo](https://docs.habana.ai/en/latest/_static/Intel_gaudi_logo.png) Gaudi Documentation 1.23.0 documentation ========================================](https://docs.habana.ai/en/latest/index.html)

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
    *   [Creating and Executing Media Pipeline](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#)
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

*   [Creating a New Pipeline](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#creating-a-new-pipeline)
*   [Supported Device Type Per Operator](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#supported-device-type-per-operator)
*   [Defining Operators and Processing Sequence](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#defining-operators-and-processing-sequence)
*   [Building and Initializing the Pipeline](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#building-and-initializing-the-pipeline)
*   [Executing the Pipeline](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#executing-the-pipeline)
*   [MediaPipe Example Using HPU Device](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#mediapipe-example-using-hpu-device)
*   [Adding Crop as Augmentation Operators](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#adding-crop-as-augmentation-operators)
*   [MediaPipe with CPU Operators Only](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#mediapipe-with-cpu-operators-only)
*   [MediaConst and MediaFunc](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#mediaconst-and-mediafunc)
*   [CPU-HPU Operators Ordering Limitation](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#cpu-hpu-operators-ordering-limitation)

Creating and Executing Media Pipeline
=====================================

On this Page
------------

*   [Creating a New Pipeline](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#creating-a-new-pipeline)
*   [Supported Device Type Per Operator](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#supported-device-type-per-operator)
*   [Defining Operators and Processing Sequence](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#defining-operators-and-processing-sequence)
*   [Building and Initializing the Pipeline](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#building-and-initializing-the-pipeline)
*   [Executing the Pipeline](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#executing-the-pipeline)
*   [MediaPipe Example Using HPU Device](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#mediapipe-example-using-hpu-device)
*   [Adding Crop as Augmentation Operators](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#adding-crop-as-augmentation-operators)
*   [MediaPipe with CPU Operators Only](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#mediapipe-with-cpu-operators-only)
*   [MediaConst and MediaFunc](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#mediaconst-and-mediafunc)
*   [CPU-HPU Operators Ordering Limitation](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#cpu-hpu-operators-ordering-limitation)

Creating and Executing Media Pipeline[¶](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#creating-and-executing-media-pipeline "Permalink to this headline")
================================================================================================================================================================================

This section describes the steps required to create and execute a media processing pipeline. The steps include:

*   Creating a derived class from `MediaPipe` e.g `myMediaPipe` and initializing the super class arguments `device`, `prefetch_depth`, `batch_size`, `num_threads`, and `pipe_name`.

*   Creating operators required in the pipeline along with their parameters. All supported operators are listed in [Operators](https://docs.habana.ai/en/latest/Media_Pipeline/Operators.html#media-operators) table.

*   Defining the sequence of media processing in `definegraph()` method.

*   Building and initializing the pipeline.

*   Executing the pipeline.

It also provides a [MediaPipe Example Using HPU Device](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#media-pipeline-example) with the above steps implemented.

Note

**Before you Start:** Make sure to set up your environment as shown in the [Installation Guide and On-Premise System Update](https://docs.habana.ai/en/latest/Installation_Guide/index.html#gaudi-installation-guide).

Creating a New Pipeline[¶](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#creating-a-new-pipeline "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------

The Intel Gaudi framework provides a `MediaPipe` class which includes necessary functions for defining, building and running a `Media` data processing pipeline. You can define a new pipeline (for example `myMediaPipe`) by:

*   Creating a derived class from `MediaPipe`.

*   Passing the following parameters to the base class constructor:

**Keyword Arguments:**

| kwargs | Description |
| --- | --- |
| device | Device on which MediaPipe is to be executed. When the entire pipeline is executed on CPU, the device should be set to `cpu`. When the pipeline is executed on both CPU and HPU, the device should be set to `mixed`. Note that `legacy` option is deprecated. > * Type: str > > * Default: None |
| prefetch_depth | Input batch queue depth for circular buffering. Controls how many image batches can be preloaded by MediaPipe. > * Type: int > > * Optional: yes > > * Default: 2 |
| batch_size | Batch size for each Media Pipeline execution. This should be aligned to the number of examples in a batch on one worker for a neural network model. > * Type: int > > * Optional: yes > > * Default: 1 |
| num_threads | Number of CPU threads for Media Pipeline. > * Type: int > > * Optional: yes > > * Default: 1 |
| pipe_name | Pipeline name used to identify specific pipe in the logs. > * Type: str > > * Default: None |

The below is an example of a derived class constructor. In the below example, additional parameters which are not part of the MediaPipe base class were added to the code: `dir`, `channel`, `height` and `width`. These parameters are used when defining operators specific to `myMediaPipe` implementation.

class myMediaPipe(MediaPipe):
    def  __init__ (self, device, dir, queue_depth, batch_size, num_threads, channel, height, width):
        super(
            myMediaPipe,
            self). __init__ (
            device,
            queue_depth,
            batch_size,
            num_threads,
            self. __class__ . __name__ )

# Create MediaPipe object
pipe = myMediaPipe('hpu', dir, queue_depth, batch_size, num_threads,
                   channels, height, width)

Supported Device Type Per Operator[¶](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#supported-device-type-per-operator "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`myMediaPipe` supports a number of operators implemented either on HPU or CPU. Some operators can be implemented on both HPU and CPU, allowing you to select which device to run on. See [Operators](https://docs.habana.ai/en/latest/Media_Pipeline/Operators.html#media-operators) for a full list of operators and supported devices.

When defining `myMediaPipe`, make sure to follow the below guidelines:

*   When using `device='mixed'`, each operator in the MediaPipe should have a device type (HPU or CPU) on which it will be executed. See [MediaPipe with CPU Operators Only](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#cpu-operator-example) for examples.

*   If all operators in a pipeline are CPU, `device='cpu'` should be set and the device type for operators should specified as ‘cpu’.

*   In any type of MediaPipe (CPU/HPU), the reader operator always runs on the CPU.

Note

All CPU operations must be performed prior to HPU operations. See [CPU-HPU Operators Ordering Limitation](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#ordering-limitation) for further details.

Defining Operators and Processing Sequence[¶](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#defining-operators-and-processing-sequence "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The MediaPipe is constructed using operators. All operators and their parameter options are available [here](https://docs.habana.ai/en/latest/Media_Pipeline/Operators.html#media-operators). First, a set of operators needs to be created in the pipeline along with their parameters e.g. `ReadImageDatasetFromDir`, `ImageDecoder`, `Crop`. Such operations include reading and decoding data, and an optional set of operations such as image cropping or flipping can be augmented. After creating the operators, define the sequence of media processing in `definegraph()` method.

Internally, `MediaPipe` converts operators to nodes and builds graphs according to the specification of `definegraph`. The graph is then executed on input batches performing the required operations.

The below example shows the derived class constructor, the set of operators used and the sequence of media processing defined in `definegraph()` method:

class myMediaPipe(MediaPipe):
        def  __init__ (self, device, dir, queue_depth, batch_size, num_threads, img_h, img_w):
            super(
                myMediaPipe,
                self). __init__ (
                device,
                queue_depth,
                batch_size,
                num_threads,
                self. __class__ . __name__ )

            self.input = fn.ReadImageDatasetFromDir(shuffle=False,
                                                    dir=dir,
                                                    format="jpg")

            self.decode = fn.ImageDecoder(device="hpu",
                                          output_format=it.RGB_I,
                                          resize=[img_w, img_h])

        def definegraph(self):
            images, labels = self.input()
            images = self.decode(images)
            return images, labels

Building and Initializing the Pipeline[¶](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#building-and-initializing-the-pipeline "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Once the class is defined with the required nodes and sequence of media processing (using `definegraph`), the `build()` and `iter_init()` methods should be called on the class object to build the MediaPipe and initialize the iterator. The iterator is an internal part of the MediaPipe class which retrieves a sequence of data batches.

pipe.build()
pipe.iter_init()

Executing the Pipeline[¶](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#executing-the-pipeline "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------

To produce an output from MediaPipe, the `run()` method should be called on the class object. The `run()` method gives an output for a batch of data, already defined in the returned data given in the `definegraph()` method. After the processing is complete, if the pipeline data is present on the device, you can call the `as_cpu()` method on the device tensor object to view or manipulate tensors on the host, which gives a host tensor object. For numpy manipulation, the `as_nparray()` method of host tensor object can be called to get a numpy host array.

As shown below, the defined graph returns images and labels which are also the output of the `pipe.run()`.

def definegraph(self):
    images, labels = self.input()
    images = self.decode(images)
    return images, labels

images, labels = pipe.run()

Please note that image batch is not necessarily prepared at the time of calling `pipe.run()`. Depending on the value of `prefetch_depth` passed to MediaPipe constructor, a given number of batches will be prepared ahead of time.

MediaPipe Example Using HPU Device[¶](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#mediapipe-example-using-hpu-device "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following example shows how to create a MediaPipe with image decode operation and resizing these images to a fixed height and width after decoding.

*   `fn.ReadImageDatasetFromDir` reads JPEG files and labels from a given directory

*   `fn.ImageDecoder` decodes and resizes jpeg images

from habana_frameworks.mediapipe import fn
from habana_frameworks.mediapipe.mediapipe import MediaPipe
from habana_frameworks.mediapipe.media_types import imgtype as it
import matplotlib.pyplot as plt
import os

g_display_timeout = os.getenv("DISPLAY_TIMEOUT") or 5

# Create MediaPipe derived class

class myMediaPipe(MediaPipe):
    def  __init__ (self, device, dir, queue_depth, batch_size, num_threads, img_h, img_w):
        super(
            myMediaPipe,
            self). __init__ (
            device,
            queue_depth,
            batch_size,
            num_threads,
            self. __class__ . __name__ )

        self.input = fn.ReadImageDatasetFromDir(shuffle=False,
                                                dir=dir,
                                                format="jpg")

        self.decode = fn.ImageDecoder(device="hpu",
                                    output_format=it.RGB_I,
                                    resize=[img_w, img_h])

    def definegraph(self):
        images, labels = self.input()
        images = self.decode(images)
        return images, labels

def display_images(images, labels, batch_size, cols):
    rows = (batch_size + 1) // cols
    plt.figure(figsize=(10, 10))
    for i in range(batch_size):
        ax = plt.subplot(rows, cols, i + 1)
        plt.imshow(images[i])
        plt.title("label:"+str(labels[i]))
        plt.axis("off")
    plt.show(block=False)
    plt.pause(g_display_timeout)
    plt.close()

def main():
    batch_size = 6
    num_threads = 1
    img_width = 200
    img_height = 200
    queue_depth = 2
    base_dir = os.environ['DATASET_DIR']
    dir = base_dir + "/img_data/"
    columns = 3

    # Create MediaPipe object
    pipe = myMediaPipe('mixed', dir, queue_depth, batch_size, num_threads,
                    img_height, img_width)

    # Build MediaPipe
    pipe.build()

    # Initialize MediaPipe iterator
    pipe.iter_init()

    # Run MediaPipe
    images, labels = pipe.run()

    def as_cpu(tensor):
        if (callable(getattr(tensor, "as_cpu", None))):
            tensor = tensor.as_cpu()
        return tensor

    # Copy data to host from device as numpy array
    images = as_cpu(images).as_nparray()
    labels = as_cpu(labels).as_nparray()

    del pipe

    # Display images
    display_images(images, labels, batch_size, columns)

if  __name__  == "__main__":
    main()

**Decoded and Resized Images**[1](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#id2)

[![Image 8: Image1 of decoded batch.](https://docs.habana.ai/en/latest/_images/img0_resize.png)](https://docs.habana.ai/en/latest/_images/img0_resize.png)

[![Image 9: Image2 of decoded batch.](https://docs.habana.ai/en/latest/_images/img1_resize.png)](https://docs.habana.ai/en/latest/_images/img1_resize.png)

[![Image 10: Image3 of decoded batch.](https://docs.habana.ai/en/latest/_images/img2_resize.png)](https://docs.habana.ai/en/latest/_images/img2_resize.png)

[![Image 11: Image4 of decoded batch.](https://docs.habana.ai/en/latest/_images/img3_resize.png)](https://docs.habana.ai/en/latest/_images/img3_resize.png)

[![Image 12: Image5 of decoded batch.](https://docs.habana.ai/en/latest/_images/img4_resize.png)](https://docs.habana.ai/en/latest/_images/img4_resize.png)

[![Image 13: Image6 of decoded batch.](https://docs.habana.ai/en/latest/_images/img5_resize.png)](https://docs.habana.ai/en/latest/_images/img5_resize.png)

1
Licensed under a [CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license. The images used here are taken from [https://data.caltech.edu/records/mzrjq-6wc02](https://data.caltech.edu/records/mzrjq-6wc02).

Adding Crop as Augmentation Operators[¶](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#adding-crop-as-augmentation-operators "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following code snippet shows augmenting the decoded images with crop operation:

from habana_frameworks.mediapipe import fn
from habana_frameworks.mediapipe.mediapipe import MediaPipe
from habana_frameworks.mediapipe.media_types import imgtype as it
from habana_frameworks.mediapipe.media_types import dtype as dt
import matplotlib.pyplot as plt
import os

g_display_timeout = os.getenv("DISPLAY_TIMEOUT") or 5

# Create MediaPipe derived class

class myMediaPipe(MediaPipe):
    def  __init__ (self, device, dir, queue_depth, batch_size, num_threads, img_h, img_w):
        super(
            myMediaPipe,
            self). __init__ (
            device,
            queue_depth,
            batch_size,
            num_threads,
            self. __class__ . __name__ )

        self.input = fn.ReadImageDatasetFromDir(shuffle=False,
                                                dir=dir,
                                                format="jpg")

        self.decode = fn.ImageDecoder(device="hpu",
                                    output_format=it.RGB_I,
                                    resize=[img_w, img_h])

        self.crop = fn.Crop(crop_w=150,
                            crop_h=150,
                            dtype=dt.UINT8)

    def definegraph(self):
        images, labels = self.input()
        images = self.decode(images)
        images = self.crop(images)
        return images, labels

def display_images(images, labels, batch_size, cols):
    rows = (batch_size + 1) // cols
    plt.figure(figsize=(10, 10))
    for i in range(batch_size):
        ax = plt.subplot(rows, cols, i + 1)
        plt.imshow(images[i])
        plt.title("label:" + str(labels[i]))
        plt.axis("off")
    plt.show(block=False)
    plt.pause(g_display_timeout)
    plt.close()

def main():
    batch_size = 6
    num_threads = 1
    img_width = 200
    img_height = 200
    queue_depth = 2
    base_dir = os.environ['DATASET_DIR']
    dir = base_dir + "/img_data/"
    columns = 3

    # Create MediaPipe object
    pipe = myMediaPipe('mixed', dir, queue_depth, batch_size, num_threads,
                        img_height, img_width)

    # Build MediaPipe
    pipe.build()

    # Initialize MediaPipe iterator
    pipe.iter_init()

    # Run MediaPipe
    images, labels = pipe.run()

    def as_cpu(tensor):
        if (callable(getattr(tensor, "as_cpu", None))):
            tensor = tensor.as_cpu()
        return tensor

    # Copy data to host from device as numpy array
    images = as_cpu(images).as_nparray()
    labels = as_cpu(labels).as_nparray()

    del pipe

    # Display images
    display_images(images, labels, batch_size, columns)

if  __name__  == "__main__":
    main()

**Decoded, Resized and Cropped Images**[2](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#id4)

[![Image 14: Image1 of decoded batch and cropped.](https://docs.habana.ai/en/latest/_images/img0_resize_crop.png)](https://docs.habana.ai/en/latest/_images/img0_resize_crop.png)

[![Image 15: Image2 of decoded batch and cropped.](https://docs.habana.ai/en/latest/_images/img1_resize_crop.png)](https://docs.habana.ai/en/latest/_images/img1_resize_crop.png)

[![Image 16: Image3 of decoded batch and cropped.](https://docs.habana.ai/en/latest/_images/img2_resize_crop.png)](https://docs.habana.ai/en/latest/_images/img2_resize_crop.png)

[![Image 17: Image3 of decoded batch and cropped.](https://docs.habana.ai/en/latest/_images/img3_resize_crop.png)](https://docs.habana.ai/en/latest/_images/img3_resize_crop.png)

[![Image 18: Image4 of decoded batch and cropped.](https://docs.habana.ai/en/latest/_images/img4_resize_crop.png)](https://docs.habana.ai/en/latest/_images/img4_resize_crop.png)

[![Image 19: Image5 of decoded batch and cropped.](https://docs.habana.ai/en/latest/_images/img5_resize_crop.png)](https://docs.habana.ai/en/latest/_images/img5_resize_crop.png)

2
Licensed under a [CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license. The images used here are taken from [https://data.caltech.edu/records/mzrjq-6wc02](https://data.caltech.edu/records/mzrjq-6wc02).

MediaPipe with CPU Operators Only[¶](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#mediapipe-with-cpu-operators-only "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following code snippet shows MediaPipe with CPU operations. Note that all operators must be defined with `device='cpu'`. The ‘cpu’ device value is also passed to the constructor.

from habana_frameworks.mediapipe import fn
from habana_frameworks.mediapipe.mediapipe import MediaPipe
from habana_frameworks.mediapipe.media_types import dtype as dt
import os

# Create MediaPipe derived class

class myMediaPipe(MediaPipe):
    def  __init__ (self, device, dir, queue_depth, batch_size, num_threads, patch_size):
        super(
            myMediaPipe,
            self). __init__ (
            device,
            queue_depth,
            batch_size,
            num_threads,
            self. __class__ . __name__ )

        self.input = fn.ReadNumpyDatasetFromDir(num_outputs=1,
                                                shuffle=False,
                                                dir=dir,
                                                pattern='case_*_x.npy',
                                                dtype=dt.FLOAT32,
                                                device='cpu')

        self.crop_img = fn.Crop(crop_w=patch_size[0],
                                crop_h=patch_size[1],
                                crop_d=patch_size[2],
                                crop_pos_x=0.5,
                                crop_pos_y=0.5,
                                crop_pos_z=0.5,
                                dtype=dt.FLOAT32,
                                device='cpu')

    def definegraph(self):
        image = self.input()
        image = self.crop_img(image)
        return image

def main():
    batch_size = 2
    queue_depth = 1
    num_threads = 1
    patch_size = [160, 192, 64]
    base_dir = os.environ['DATASET_DIR']
    dir = base_dir + "/npy_data/fp32_4d/"

    # Create MediaPipe object
    pipe = myMediaPipe('cpu', dir, queue_depth,
                    batch_size, num_threads, patch_size)

    # Build MediaPipe
    pipe.build()

    # Initialize MediaPipe iterator
    pipe.iter_init()

    # Run MediaPipe
    image = pipe.run()

    print(image.as_nparray().shape)

if  __name__  == "__main__":
    main()

MediaConst and MediaFunc[¶](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#mediaconst-and-mediafunc "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------

In addition to the above, the Media API allows for defining constant tensors using [MediaConst](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_MediaConst.html#using-mediaconst). These tensors can then be used with operators such as [CropMirrorNorm](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_CMN.html#using-cropmirrornorm) (as shown in the example). If tensors need to be created per batch, [MediaFunc](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Operator_MediaFunc.html#using-mediafunc) should be used. It allows, for example, to introduce random tensors to the operators sequence.

CPU-HPU Operators Ordering Limitation[¶](https://docs.habana.ai/en/latest/Media_Pipeline/Media_Pipeline.html#cpu-hpu-operators-ordering-limitation "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

All CPU operations must be performed prior to HPU operations. Therefore, when implementing the sequence of media processing using `definegraph`, operations need to be processed by CPU first. If operations are processed on the HPU first, no operations performed on the CPU can be processed afterward.

[previous MediaPipe](https://docs.habana.ai/en/latest/Media_Pipeline/index.html "previous page")[next MediaPipe for PyTorch ResNet](https://docs.habana.ai/en/latest/Media_Pipeline/Pytorch_Resnet_Media_Pipe.html "next page")

By Habana Labs

 © Copyright 2026, Habana Labs.
