# Source: https://docs.pytorch.org/docs/stable/user_guide/index.html

Title: User Guide

URL Source: https://docs.pytorch.org/docs/stable/user_guide/index.html

Published Time: Aug 13, 2025T00:00:00Z

Markdown Content:
User Guide — PyTorch 2.10 documentation
===============

Opens in a new window Opens an external website Opens an external website in a new window

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences 

[](https://pytorch.org/)

*   [Learn](https://docs.pytorch.org/docs/stable/user_guide/index.html)[Get Started](https://pytorch.org/get-started/locally)[Tutorials](https://docs.pytorch.org/tutorials)[Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html)[PyTorch Recipes](https://pytorch.org/tutorials/recipes/recipes_index.html)[Intro to PyTorch - YouTube Series](https://pytorch.org/tutorials/beginner/introyt.html)[Webinars](https://pytorch.org/webinars/)  
*   [Community](https://docs.pytorch.org/docs/stable/user_guide/index.html)[Landscape](https://landscape.pytorch.org/)[Join the Ecosystem](https://pytorch.org/join-ecosystem)[Community Hub](https://pytorch.org/community-hub/)[Forums](https://discuss.pytorch.org/)[Developer Resources](https://pytorch.org/resources)[Contributor Awards](https://pytorch.org/contributor-awards/)[Community Events](https://pytorch.org/community-events/)[PyTorch Ambassadors](https://pytorch.org/programs/ambassadors/)  
*   [Projects](https://docs.pytorch.org/docs/stable/user_guide/index.html)[PyTorch](https://pytorch.org/projects/pytorch/)[vLLM](https://pytorch.org/projects/vllm/)[DeepSpeed](https://pytorch.org/projects/deepspeed/)[Host Your Project](https://pytorch.org/projects/host-your-project/)[RAY](https://pytorch.org/projects/ray/)  
*   [Docs](https://docs.pytorch.org/docs/stable/user_guide/index.html)[PyTorch](https://docs.pytorch.org/docs/stable/index.html)[Domains](https://pytorch.org/domains)  
*   [Blogs & News](https://docs.pytorch.org/docs/stable/user_guide/index.html)[Blog](https://pytorch.org/blog/)[Announcements](https://pytorch.org/announcements)[Case Studies](https://pytorch.org/case-studies/)[Events](https://pytorch.org/events)[Newsletter](https://pytorch.org/newsletter)  
*   [About](https://docs.pytorch.org/docs/stable/user_guide/index.html)[PyTorch Foundation](https://pytorch.org/foundation)[Members](https://pytorch.org/members)[Governing Board](https://pytorch.org/governing-board)[Technical Advisory Council](https://pytorch.org/tac)[Cloud Credit Program](https://pytorch.org/credits)[Staff](https://pytorch.org/staff)[Contact](https://pytorch.org/contact)[Brand Guidelines](https://pytorch.org/wp-content/uploads/2025/09/pytorch_brand_guide_091925a.pdf)  
*   [JOIN](https://pytorch.org/join) 

[](https://docs.pytorch.org/docs/stable/user_guide/index.html#)

[](https://docs.pytorch.org/docs/stable/user_guide/index.html#)

*   [Learn](https://docs.pytorch.org/docs/stable/user_guide/index.html)

    *   [Get Started](https://pytorch.org/get-started/locally)
    *   [Tutorials](https://docs.pytorch.org/tutorials)
    *   [Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html)
    *   [PyTorch Recipes](https://pytorch.org/tutorials/recipes/recipes_index.html)
    *   [Introduction to PyTorch - YouTube Series](https://pytorch.org/tutorials/beginner/introyt.html)
    *   [Webinars](https://pytorch.org/webinars/)

*   [Community](https://docs.pytorch.org/docs/stable/user_guide/index.html)

    *   [Landscape](https://landscape.pytorch.org/)
    *   [Join the Ecosystem](https://pytorch.org/join-ecosystem)
    *   [Community Hub](https://pytorch.org/community-hub/)
    *   [Forums](https://discuss.pytorch.org/)
    *   [Developer Resources](https://pytorch.org/resources)
    *   [Contributor Awards](https://pytorch.org/contributor-awards/)
    *   [Community Events](https://pytorch.org/community-events/)
    *   [PyTorch Ambassadors](https://pytorch.org/programs/ambassadors/)

*   [Projects](https://docs.pytorch.org/docs/stable/user_guide/index.html)

    *   [PyTorch](https://pytorch.org/projects/pytorch/)
    *   [vLLM](https://pytorch.org/projects/vllm/)
    *   [DeepSpeed](https://pytorch.org/projects/deepspeed/)
    *   [Host Your Project](https://pytorch.org/projects/host-your-project/)

*   [Docs](https://docs.pytorch.org/docs/stable/user_guide/index.html)

    *   [PyTorch](https://docs.pytorch.org/docs/stable/index.html)
    *   [Domains](https://pytorch.org/domains)

*   [Blog & News](https://docs.pytorch.org/docs/stable/user_guide/index.html)

    *   [Blog](https://pytorch.org/blog/)
    *   [Announcements](https://pytorch.org/announcements)
    *   [Case Studies](https://pytorch.org/case-studies/)
    *   [Events](https://pytorch.org/events)
    *   [Newsletter](https://pytorch.org/newsletter)

*   [About](https://docs.pytorch.org/docs/stable/user_guide/index.html)

    *   [PyTorch Foundation](https://pytorch.org/foundation)
    *   [Members](https://pytorch.org/members)
    *   [Governing Board](https://pytorch.org/governing-board)
    *   [Technical Advisory Council](https://pytorch.org/tac)
    *   [Cloud Credit Program](https://pytorch.org/credits)
    *   [Staff](https://pytorch.org/staff)
    *   [Contact](https://pytorch.org/contact)

[Skip to main content](https://docs.pytorch.org/docs/stable/user_guide/index.html#main-content)

Back to top- [x] - [x] 

Ctrl+K

v2.10.0 (stable)

[v2.12.0 (unstable)](https://docs.pytorch.org/docs/main/user_guide/index.html)[v2.11.0 (release candidate)](https://docs.pytorch.org/docs/2.11/user_guide/index.html)[v2.10.0 (stable)](https://docs.pytorch.org/docs/2.10/user_guide/index.html)[v2.9.1](https://docs.pytorch.org/docs/2.9/user_guide/index.html)[v2.8.0](https://docs.pytorch.org/docs/2.8/user_guide/index.html)[v2.7.0](https://docs.pytorch.org/docs/2.7/user_guide/index.html)[v2.6.0](https://docs.pytorch.org/docs/2.6/user_guide/index.html)[v2.5.0](https://docs.pytorch.org/docs/2.5/user_guide/index.html)[v2.4.0](https://docs.pytorch.org/docs/2.4/user_guide/index.html)[v2.3.0](https://docs.pytorch.org/docs/2.3/user_guide/index.html)[v2.2.0](https://docs.pytorch.org/docs/2.2/user_guide/index.html)[v2.1.0](https://docs.pytorch.org/docs/2.1/user_guide/index.html)[v2.0.0](https://docs.pytorch.org/docs/2.0/user_guide/index.html)[v1.13](https://docs.pytorch.org/docs/1.13/user_guide/index.html)[v1.12](https://docs.pytorch.org/docs/1.12/user_guide/index.html)[v1.11](https://docs.pytorch.org/docs/1.11/user_guide/index.html)[v1.10](https://docs.pytorch.org/docs/1.10/user_guide/index.html)[v1.9.1](https://docs.pytorch.org/docs/1.9.1/user_guide/index.html)[v1.9.0](https://docs.pytorch.org/docs/1.9.0/user_guide/index.html)[v1.8.1](https://docs.pytorch.org/docs/1.8.1/user_guide/index.html)[v1.8.0](https://docs.pytorch.org/docs/1.8.0/user_guide/index.html)[v1.7.1](https://docs.pytorch.org/docs/1.7.1/user_guide/index.html)[v1.7.0](https://docs.pytorch.org/docs/1.7.0/user_guide/index.html)[v1.6.0](https://docs.pytorch.org/docs/1.6.0/user_guide/index.html)[v1.5.1](https://docs.pytorch.org/docs/1.5.1/user_guide/index.html)[v1.5.0](https://docs.pytorch.org/docs/1.5.0/user_guide/index.html)[v1.4.0](https://docs.pytorch.org/docs/1.4.0/user_guide/index.html)[v1.3.1](https://docs.pytorch.org/docs/1.3.1/user_guide/index.html)[v1.3.0](https://docs.pytorch.org/docs/1.3.0/user_guide/index.html)[v1.2.0](https://docs.pytorch.org/docs/1.2.0/user_guide/index.html)[v1.1.0](https://docs.pytorch.org/docs/1.1.0/user_guide/index.html)[v1.0.1](https://docs.pytorch.org/docs/1.0.1/user_guide/index.html)[v1.0.0](https://docs.pytorch.org/docs/1.0.0/user_guide/index.html)[v0.4.1](https://docs.pytorch.org/docs/0.4.1/user_guide/index.html)[v0.4.0](https://docs.pytorch.org/docs/0.4.0/user_guide/index.html)[v0.3.1](https://docs.pytorch.org/docs/0.3.1/user_guide/index.html)[v0.3.0](https://docs.pytorch.org/docs/0.3.0/user_guide/index.html)[v0.2.0](https://docs.pytorch.org/docs/0.2.0/user_guide/index.html)[v0.1.12](https://docs.pytorch.org/docs/0.1.12/user_guide/index.html)

[Home](https://docs.pytorch.org/docs/stable/index.html)

*   [Install PyTorch](https://pytorch.org/get-started/locally/)
*   [User Guide](https://docs.pytorch.org/docs/stable/user_guide/index.html#)
*   [Reference API](https://docs.pytorch.org/docs/stable/pytorch-api.html)
*   [Developer Notes](https://docs.pytorch.org/docs/stable/notes.html)
*   [Community](https://docs.pytorch.org/docs/stable/community/index.html)
*   [Tutorials](https://docs.pytorch.org/tutorials/)

Ctrl+K

[×](javascript:void(0) "Clear search box")

Custom Search

Sort by

Relevance

Date

- [x]  

*   [X](https://x.com/PyTorch)
*   [GitHub](https://github.com/pytorch/pytorch)
*   [PyTorch Forum](https://discuss.pytorch.org/)
*   [PyPi](https://pypi.org/project/torch/)

*   [Install PyTorch](https://pytorch.org/get-started/locally/)
*   [User Guide](https://docs.pytorch.org/docs/stable/user_guide/index.html#)
*   [Reference API](https://docs.pytorch.org/docs/stable/pytorch-api.html)
*   [Developer Notes](https://docs.pytorch.org/docs/stable/notes.html)
*   [Community](https://docs.pytorch.org/docs/stable/community/index.html)
*   [Tutorials](https://docs.pytorch.org/tutorials/)

Ctrl+K

[×](javascript:void(0) "Clear search box")

Custom Search

Sort by

Relevance

Date

- [x]  

*   [X](https://x.com/PyTorch)
*   [GitHub](https://github.com/pytorch/pytorch)
*   [PyTorch Forum](https://discuss.pytorch.org/)
*   [PyPi](https://pypi.org/project/torch/)

Section Navigation

Introduction

*   [Pytorch Overview](https://docs.pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)
*   [Get Started](https://pytorch.org/get-started/locally/)
*   [Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)

Core Concepts

*   [PyTorch Main Components](https://docs.pytorch.org/docs/stable/user_guide/pytorch_main_components.html)

Torch Compile

*   [Torch.compile](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler.html)

    *   [Getting Started](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_get_started.html)
    *   [Core Concepts](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/core_concepts.html)

        *   [torch.compile Programming Model](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/programming_model.html)

            *   [Dynamo Core Concepts](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/programming_model.dynamo_core_concepts.html)
            *   [Working with Graph Breaks](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/programming_model.graph_breaks_index.html)
            *   [Non-strict Tracing Programming Model](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/programming_model.non_strict_tracing_model.html)
            *   [Dealing with Recompilations](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/programming_model.recompilation.html)
            *   [tlparse / TORCH_TRACE](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/programming_model.observability.html)
            *   [Reporting Issues](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/programming_model.reporting_issues.html)

        *   [Dynamo Overview](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_dynamo_overview.html)
        *   [PyTorch 2.0 NNModule Support](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_nn_module.html)
        *   [`torch.compile` has different autograd semantics](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_backward.html)

    *   [Performance](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/performance.html)

        *   [PyTorch 2.0 Performance Dashboard](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_performance_dashboard.html)
        *   [TorchInductor GPU Profiling](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_inductor_profiling.html)
        *   [Profiling to understand torch.compile performance](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_profiling_torch_compile.html)
        *   [CUDAGraph Trees](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_cudagraph_trees.html)

    *   [Advanced](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/advanced.html)

        *   [Dynamo Deep-Dive](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_dynamo_deepdive.html)
        *   [Writing Graph Transformations on ATen IR](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_transformations.html)
        *   [Fake tensor](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_fake_tensor.html)
        *   [Custom Backends](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_custom_backends.html)
        *   [Dynamic Shapes](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_dynamic_shapes.html)

            *   [Dynamic Shapes Core Concepts](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/dynamic_shapes_core_concepts.html)
            *   [Troubleshooting Dynamic Shapes](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/dynamic_shapes_troubleshooting.html)
            *   [Advanced Options to Control Dynamic Behavior](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/dynamic_shapes_advanced_control_options.html)
            *   [Beyond the Basics](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/dynamic_shapes_beyond_the_basics.html)

    *   [Troubleshooting FAQs](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/troubleshooting_faqs.html)

        *   [tlparse / TORCH_TRACE](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/programming_model.observability.html)
        *   [Reporting Issues](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/programming_model.reporting_issues.html)
        *   [torch.compile Troubleshooting](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_troubleshooting.html)
        *   [Frequently Asked Questions](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_faq.html)

    *   [Reference/API](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/api_reference.html)

        *   [torch.compiler API reference](https://docs.pytorch.org/docs/stable/torch.compiler_api.html)

            *   [torch.compiler.compile](https://docs.pytorch.org/docs/stable/generated/torch.compiler.compile.html)
            *   [torch.compiler.reset](https://docs.pytorch.org/docs/stable/generated/torch.compiler.reset.html)
            *   [torch.compiler.allow_in_graph](https://docs.pytorch.org/docs/stable/generated/torch.compiler.allow_in_graph.html)
            *   [torch.compiler.substitute_in_graph](https://docs.pytorch.org/docs/stable/generated/torch.compiler.substitute_in_graph.html)
            *   [torch.compiler.assume_constant_result](https://docs.pytorch.org/docs/stable/generated/torch.compiler.assume_constant_result.html)
            *   [torch.compiler.list_backends](https://docs.pytorch.org/docs/stable/generated/torch.compiler.list_backends.html)
            *   [torch.compiler.disable](https://docs.pytorch.org/docs/stable/generated/torch.compiler.disable.html)
            *   [torch.compiler.set_stance](https://docs.pytorch.org/docs/stable/generated/torch.compiler.set_stance.html)
            *   [torch.compiler.set_enable_guard_collectives](https://docs.pytorch.org/docs/stable/generated/torch.compiler.set_enable_guard_collectives.html)
            *   [torch.compiler.cudagraph_mark_step_begin](https://docs.pytorch.org/docs/stable/generated/torch.compiler.cudagraph_mark_step_begin.html)
            *   [torch.compiler.is_compiling](https://docs.pytorch.org/docs/stable/generated/torch.compiler.is_compiling.html)
            *   [torch.compiler.is_dynamo_compiling](https://docs.pytorch.org/docs/stable/generated/torch.compiler.is_dynamo_compiling.html)
            *   [torch.compiler.is_exporting](https://docs.pytorch.org/docs/stable/generated/torch.compiler.is_exporting.html)
            *   [torch.compiler.skip_guard_on_inbuilt_nn_modules_unsafe](https://docs.pytorch.org/docs/stable/generated/torch.compiler.skip_guard_on_inbuilt_nn_modules_unsafe.html)
            *   [torch.compiler.skip_guard_on_all_nn_modules_unsafe](https://docs.pytorch.org/docs/stable/generated/torch.compiler.skip_guard_on_all_nn_modules_unsafe.html)
            *   [torch.compiler.keep_tensor_guards_unsafe](https://docs.pytorch.org/docs/stable/generated/torch.compiler.keep_tensor_guards_unsafe.html)
            *   [torch.compiler.skip_guard_on_globals_unsafe](https://docs.pytorch.org/docs/stable/generated/torch.compiler.skip_guard_on_globals_unsafe.html)
            *   [torch.compiler.skip_all_guards_unsafe](https://docs.pytorch.org/docs/stable/generated/torch.compiler.skip_all_guards_unsafe.html)
            *   [torch.compiler.nested_compile_region](https://docs.pytorch.org/docs/stable/generated/torch.compiler.nested_compile_region.html)

        *   [torch.compiler.config](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler.config.html)
        *   [TorchDynamo APIs for fine-grained tracing](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_fine_grain_apis.html)
        *   [TorchInductor and AOTInductor Provenance Tracking](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_inductor_provenance.html)

*   [Torch.export](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/export.html)

    *   [torch.export API Reference](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/export/api_reference.html)
    *   [torch.export Programming Model](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/export/programming_model.html)
    *   [torch.export IR Specification](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/export/ir_spec.html)
    *   [PT2 Archive Spec](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/export/pt2_archive.html)
    *   [Draft Export](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/export/draft_export.html)
    *   [Joint with descriptors](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/export/joint_with_descriptors.html)
    *   [Control Flow - Cond](https://docs.pytorch.org/docs/stable/cond.html)
    *   [ExportDB](https://docs.pytorch.org/docs/stable/generated/exportdb/index.html)

        *   [torch.escape-hatch](https://docs.pytorch.org/docs/stable/generated/exportdb/torch.escape-hatch.html)
        *   [torch.cond](https://docs.pytorch.org/docs/stable/generated/exportdb/torch.cond.html)
        *   [torch.dynamic-shape](https://docs.pytorch.org/docs/stable/generated/exportdb/torch.dynamic-shape.html)
        *   [python.closure](https://docs.pytorch.org/docs/stable/generated/exportdb/python.closure.html)
        *   [torch.dynamic-value](https://docs.pytorch.org/docs/stable/generated/exportdb/torch.dynamic-value.html)
        *   [python.data-structure](https://docs.pytorch.org/docs/stable/generated/exportdb/python.data-structure.html)
        *   [python.assert](https://docs.pytorch.org/docs/stable/generated/exportdb/python.assert.html)
        *   [python.control-flow](https://docs.pytorch.org/docs/stable/generated/exportdb/python.control-flow.html)
        *   [torch.map](https://docs.pytorch.org/docs/stable/generated/exportdb/torch.map.html)
        *   [python.builtin](https://docs.pytorch.org/docs/stable/generated/exportdb/python.builtin.html)
        *   [python.object-model](https://docs.pytorch.org/docs/stable/generated/exportdb/python.object-model.html)
        *   [python.context-manager](https://docs.pytorch.org/docs/stable/generated/exportdb/python.context-manager.html)
        *   [torch.operator](https://docs.pytorch.org/docs/stable/generated/exportdb/torch.operator.html)
        *   [torch.mutation](https://docs.pytorch.org/docs/stable/generated/exportdb/torch.mutation.html)

    *   [AOTInductor: Ahead-Of-Time Compilation for Torch.Export-ed Models](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_aot_inductor.html)

        *   [torch._logging](https://docs.pytorch.org/docs/stable/logging.html)

            *   [torch._logging.set_logs](https://docs.pytorch.org/docs/stable/generated/torch._logging.set_logs.html)

        *   [AOTInductor Minifier](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_aot_inductor_minifier.html)
        *   [AOTInductor Debugging Guide](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_aot_inductor_debugging_guide.html)

    *   [IRs](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_ir.html)
    *   [Dynamic Shapes](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_dynamic_shapes.html)

        *   [Dynamic Shapes Core Concepts](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/dynamic_shapes_core_concepts.html)
        *   [Troubleshooting Dynamic Shapes](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/dynamic_shapes_troubleshooting.html)

            *   [Debugging with `tlparse` and `TORCH_LOGS=dynamic`](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/dynamic_shapes_debugging_tlparse_torch_logs.html)
            *   [Troubleshooting GuardOnDataDependentSymNode Errors](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/dynamic_shapes_troubleshooting_guardon_errors.html)

        *   [Advanced Options to Control Dynamic Behavior](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/dynamic_shapes_advanced_control_options.html)
        *   [Beyond the Basics](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/dynamic_shapes_beyond_the_basics.html)

            *   [The Zero-One Specialization Problem](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/dynamic_shapes_zero_one_specialization.html)
            *   [Backed vs Unbacked Symints](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/compile/dynamic_shapes_backed_unbacked.html)

    *   [Fake tensor](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_fake_tensor.html)
    *   [Writing Graph Transformations on ATen IR](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_transformations.html)

Developer Notes

*   [Developer Notes](https://docs.pytorch.org/docs/stable/notes.html)

    *   [Automatic Mixed Precision examples](https://docs.pytorch.org/docs/stable/notes/amp_examples.html)
    *   [Autograd mechanics](https://docs.pytorch.org/docs/stable/notes/autograd.html)
    *   [Broadcasting semantics](https://docs.pytorch.org/docs/stable/notes/broadcasting.html)
    *   [CPU threading and TorchScript inference](https://docs.pytorch.org/docs/stable/notes/cpu_threading_torchscript_inference.html)
    *   [CUDA semantics](https://docs.pytorch.org/docs/stable/notes/cuda.html)
    *   [PyTorch Custom Operators Landing Page](https://docs.pytorch.org/docs/stable/notes/custom_operators.html)
    *   [Distributed Data Parallel](https://docs.pytorch.org/docs/stable/notes/ddp.html)
    *   [Extending PyTorch](https://docs.pytorch.org/docs/stable/notes/extending.html)
    *   [Extending torch.func with autograd.Function](https://docs.pytorch.org/docs/stable/notes/extending.func.html)
    *   [Frequently Asked Questions](https://docs.pytorch.org/docs/stable/notes/faq.html)
    *   [Getting Started on Intel GPU](https://docs.pytorch.org/docs/stable/notes/get_start_xpu.html)
    *   [Gradcheck mechanics](https://docs.pytorch.org/docs/stable/notes/gradcheck.html)
    *   [HIP (ROCm) semantics](https://docs.pytorch.org/docs/stable/notes/hip.html)
    *   [Features for large-scale deployments](https://docs.pytorch.org/docs/stable/notes/large_scale_deployments.html)
    *   [LibTorch Stable ABI](https://docs.pytorch.org/docs/stable/notes/libtorch_stable_abi.html)
    *   [MKLDNN backend](https://docs.pytorch.org/docs/stable/notes/mkldnn.html)
    *   [Modules](https://docs.pytorch.org/docs/stable/notes/modules.html)
    *   [MPS backend](https://docs.pytorch.org/docs/stable/notes/mps.html)
    *   [Multiprocessing best practices](https://docs.pytorch.org/docs/stable/notes/multiprocessing.html)
    *   [Numerical accuracy](https://docs.pytorch.org/docs/stable/notes/numerical_accuracy.html)
    *   [Out Notes](https://docs.pytorch.org/docs/stable/notes/out.html)
    *   [Reproducibility](https://docs.pytorch.org/docs/stable/notes/randomness.html)
    *   [Serialization semantics](https://docs.pytorch.org/docs/stable/notes/serialization.html)
    *   [Windows FAQ](https://docs.pytorch.org/docs/stable/notes/windows.html)

Accelerator Integration

*   [Accelerator Integration](https://docs.pytorch.org/docs/stable/accelerator/index.html)

    *   [Device Management](https://docs.pytorch.org/docs/stable/accelerator/device.html)
    *   [Accelerator Hooks](https://docs.pytorch.org/docs/stable/accelerator/hooks.html)
    *   [Guard](https://docs.pytorch.org/docs/stable/accelerator/guard.html)
    *   [Autoload Mechanism](https://docs.pytorch.org/docs/stable/accelerator/autoload.html)
    *   [Operator Registration](https://docs.pytorch.org/docs/stable/accelerator/operators.html)
    *   [Automatic Mixed Precision](https://docs.pytorch.org/docs/stable/accelerator/amp.html)

*   [](https://docs.pytorch.org/docs/stable/index.html)
*   User Guide

 Rate this Page 

★★★★★

User Guide[#](https://docs.pytorch.org/docs/stable/user_guide/index.html#user-guide "Link to this heading")
===========================================================================================================

Created On: Aug 13, 2025 | Last Updated On: Dec 03, 2025

PyTorch provides a flexible and efficient platform for building deep learning models, offering dynamic computation graphs and a rich ecosystem of tools and libraries. This guide will help you harness the power of PyTorch to create and deploy machine learning models effectively.

Note

This guide is a work in progress.

Introduction

*   [Pytorch Overview](https://docs.pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)
*   [Get Started](https://pytorch.org/get-started/locally/)
*   [Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)

Core Concepts

*   [PyTorch Main Components](https://docs.pytorch.org/docs/stable/user_guide/pytorch_main_components.html)

Torch Compile

*   [Torch.compile](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler.html)
*   [Torch.export](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/export.html)

Developer Notes

*   [Developer Notes](https://docs.pytorch.org/docs/stable/notes.html)

Accelerator Integration

*   [Accelerator Integration](https://docs.pytorch.org/docs/stable/accelerator/index.html)

 Rate this Page 

★★★★★

Send Feedback 

[previous PyTorch documentation](https://docs.pytorch.org/docs/stable/index.html "previous page")[next PyTorch Main Components](https://docs.pytorch.org/docs/stable/user_guide/pytorch_main_components.html "next page")

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.

[previous PyTorch documentation](https://docs.pytorch.org/docs/stable/index.html "previous page")[next PyTorch Main Components](https://docs.pytorch.org/docs/stable/user_guide/pytorch_main_components.html "next page")

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/user_guide/index.md)

[Show Source](https://docs.pytorch.org/docs/stable/_sources/user_guide/index.md.txt)

PyTorch Libraries

*   [torchao](https://docs.pytorch.org/ao)
*   [torchrec](https://docs.pytorch.org/torchrec)
*   [torchft](https://docs.pytorch.org/torchft)
*   [TorchCodec](https://docs.pytorch.org/torchcodec)
*   [torchvision](https://docs.pytorch.org/vision)
*   [ExecuTorch](https://docs.pytorch.org/executorch)
*   [PyTorch on XLA Devices](https://docs.pytorch.org/xla)

Docs
----

Access comprehensive developer documentation for PyTorch

[View Docs](https://docs.pytorch.org/docs/stable/index.html)

Tutorials
---------

Get in-depth tutorials for beginners and advanced developers

[View Tutorials](https://docs.pytorch.org/tutorials)

Resources
---------

Find development resources and get your questions answered

[View Resources](https://pytorch.org/resources)

**Stay in touch** for updates, event info, and the latest news

By submitting this form, I consent to receive marketing emails from the LF and its projects regarding their events, training, research, developments, and related announcements. I understand that I can unsubscribe at any time using the links in the footers of the emails I receive. [Privacy Policy](https://www.linuxfoundation.org/legal/privacy-policy?__hstc=132719121.eae0f19b93839bdf90ac5678c3841948.1773275568894.1773275568894.1773275568894.1&__hssc=132719121.1.1773275568895&__hsfp=a9cc2efcfcc506695dc904ec491f705f)

By submitting this form, I consent to receive marketing emails from the LF and its projects regarding their events, training, research, developments, and related announcements. I understand that I can unsubscribe at any time using the links in the footers of the emails I receive. [Privacy Policy](https://www.linuxfoundation.org/privacy/?__hstc=132719121.eae0f19b93839bdf90ac5678c3841948.1773275568894.1773275568894.1773275568894.1&__hssc=132719121.1.1773275568895&__hsfp=a9cc2efcfcc506695dc904ec491f705f).

*   [](https://www.facebook.com/pytorch "PyTorch on Facebook")
*   [](https://twitter.com/pytorch "PyTorch on X")
*   [](https://www.youtube.com/pytorch "PyTorch on YouTube")
*   [](https://www.linkedin.com/company/pytorch "PyTorch on LinkedIn")
*   [](https://pytorch.slack.com/ "PyTorch Slack")
*   [](https://pytorch.org/wechat "PyTorch on WeChat")

© PyTorch. Copyright © The Linux Foundation®. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For more information, including terms of use, privacy policy, and trademark usage, please see our [Policies](https://www.linuxfoundation.org/legal/policies?__hstc=132719121.eae0f19b93839bdf90ac5678c3841948.1773275568894.1773275568894.1773275568894.1&__hssc=132719121.1.1773275568895&__hsfp=a9cc2efcfcc506695dc904ec491f705f) page. [Trademark Usage](https://www.linuxfoundation.org/trademark-usage?__hstc=132719121.eae0f19b93839bdf90ac5678c3841948.1773275568894.1773275568894.1773275568894.1&__hssc=132719121.1.1773275568895&__hsfp=a9cc2efcfcc506695dc904ec491f705f). [Privacy Policy](http://www.linuxfoundation.org/privacy?__hstc=132719121.eae0f19b93839bdf90ac5678c3841948.1773275568894.1773275568894.1773275568894.1&__hssc=132719121.1.1773275568895&__hsfp=a9cc2efcfcc506695dc904ec491f705f).

To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://www.facebook.com/policies/cookies/).

![Image 2](https://docs.pytorch.org/docs/stable/_static/img/pytorch-x.svg)

© Copyright PyTorch Contributors.

Created using [Sphinx](https://www.sphinx-doc.org/) 7.2.6.

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.4.
