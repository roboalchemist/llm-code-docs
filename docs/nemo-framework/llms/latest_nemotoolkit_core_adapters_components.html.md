# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/components.html.md

Title: Adapter Components — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/components.html

Published Time: Fri, 18 Jul 2025 19:25:38 GMT

Markdown Content:
Adapter Components[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/components.html.md#adapter-components "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Adapters can be considered as any set of parameters that are added to a pre-existing module/model. In our case, we currently support the standard adapter in literature, more advanced adapter modules are being researched and can potentially be supported by NeMo.

An adapter module can be any pytorch module, but it must follow certain straightforward requirements -

1.   The model accepts an input of some input dimension, and its output must match this dimension.

2.   Ideally, the module is initialized such that the output of the adapter when initialized is such that it does not modify the original input. This allows the model to produce the same output results, even when additional parameters have been added.

According to Junxian et al [[1](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/components.html.md#id6 "Junxian He, Chunting Zhou, Xuezhe Ma, Taylor Berg-Kirkpatrick, and Graham Neubig. Towards a unified view of parameter-efficient transfer learning. 2021. URL: https://arxiv.org/abs/2110.04366, doi:10.48550/ARXIV.2110.04366.")], we can consider an adapter being represented as three components -

1.   Functional form - the trainable parameters that will modify the input

2.   Insertion form - Where the adapter outputs are integrated with the original input. The input to the adapters can be the last output of the layer, the input to some attention layer, or even the original input to the module itself (before even the modules forward pass).

3.   Composition function - How the adapters outputs are integrated with the inputs. It can be as simple as residual addition connection, or concatenation, or point-wise multiplication etc.

Functional Form - Adapter Networks[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/components.html.md#functional-form-adapter-networks "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Adapter modules represent the functional form of the adapter. We discuss an example of a most commonly used adapter module found in literature, titled the `LinearAdapter` (or Houlsby Adapter) [[2](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/components.html.md#id5 "Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, Bruna Morrone, Quentin De Laroussilhe, Andrea Gesmundo, Mona Attariyan, and Sylvain Gelly. Parameter-efficient transfer learning for nlp. In International Conference on Machine Learning, 2790–2799. PMLR, 2019.")].

Note

All adapter modules must extend `AdapterModuleUtil` and should ideally have an equivalent DataClass config for easy instantiation !

_class_ nemo.collections.common.parts.adapter_modules.AdapterModuleUtil
Bases: [`AccessMixin`](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.mixins.access_mixins.AccessMixin "nemo.core.classes.mixins.access_mixins.AccessMixin")

Base class of Adapter Modules, providing common functionality to all Adapter Modules.

setup_adapter_strategy(_adapter\_strategy:AbstractAdapterStrategy|None_,)
Setup adapter strategy of this class, enabling dynamic change in the way the adapter output is merged with the input.

When called successfully, will assign the variable adapter_strategy to the module.

Parameters:
**adapter_strategy** – Can be a None or an implementation of AbstractAdapterStrategy.

get_default_strategy_config()→dataclass
Returns a default adapter module strategy.

adapter_unfreeze()
Sets the requires grad for all parameters in the adapter to True. This method should be overridden for any custom unfreeze behavior that is required. For example, if not all params of the adapter should be unfrozen.

* * *

_class_ nemo.collections.common.parts.adapter_modules.LinearAdapter(_*args:Any_, _**kwargs:Any_)
Bases: `Module`, `AdapterModuleUtil`

Simple Linear Feedforward Adapter module with LayerNorm and singe hidden layer with activation function. Note: The adapter explicitly initializes its final layer with all zeros in order to avoid affecting the original model when all adapters are disabled.

Parameters:
*   **in_features** – Input dimension of the module. Note that for adapters, input_dim == output_dim.

*   **dim** – Hidden dimension of the feed forward network.

*   **activation** – Str name for an activation function.

*   **norm_position** – Str, can be pre or post. Defaults to pre. Determines whether the normalization will occur in the first layer or the last layer. Certain architectures may prefer one over the other.

*   **dropout** – float value, whether to perform dropout on the output of the last layer of the adapter.

*   **adapter_strategy** – By default, ResidualAddAdapterStrategyConfig. An adapter composition function object.

Insertion Form - Module Adapters[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/components.html.md#insertion-form-module-adapters "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Adapter modules can be integrated into many different locations of a given module. For example, it is possible to have an adapter that affects only the outputs of the final layer in each module. We can also have a `Parallel Adapter`[[1](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/components.html.md#id6 "Junxian He, Chunting Zhou, Xuezhe Ma, Taylor Berg-Kirkpatrick, and Graham Neubig. Towards a unified view of parameter-efficient transfer learning. 2021. URL: https://arxiv.org/abs/2110.04366, doi:10.48550/ARXIV.2110.04366.")] that operates at the input of the module itself, in parallel to the forward pass of the module. Yet another insertion location is inside the Multi Head Attention Layers.

On top of this, while adapters are commonly used only in the layers containing the most parameters (say the Encoder of a network), some models can support adapters in multiple locations (Encoder-Decoder architecture for Language Models, Machine Translation, or even Encoder-Decoder-Joint for ASR with Transducer Loss). As such, NeMo utilizes the concept of `Module Adapters`.

`Module Adapters` are very simply defined when adding an adapter - by specifying the module that the adapter should be inserted into.

# Get the list of supported modules / locations in a adapter compatible Model
print(model.adapter_module_names)  # assume ['', 'encoder', 'decoder']

# When calling add_adapter, specify the module name in the left of the colon symbol, and the adapter name afterwords.
# The adapter is then directed to the decoder module instead of the default / encoder module.
model.add_adapter("decoder:first_adapter", cfg=...)

You might note that `model.adapter_module_names` can sometimes return `''` as one of the supported module names - this refers to the “default module”. Generally we try to provide the default as the most commonly used adapter in literature - for example, Encoder adapters in NLP/NMT/ASR.

Composition Function - Adapter Strategies[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/components.html.md#composition-function-adapter-strategies "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Finally, we discuss how to compose the input and output of adapter modules. In order to generalize this step, we construct `Adapter Strategies`. A strategy is any class (not torch.nn.Module!) that extends `AbstractAdapterStrategy`, and provides a `forward()` method that accepts a specific signature of the inputs and produces an output tensor which combines the input and output with some specific method.

We discuss a simple residual additional connection strategy below - that accepts an input to the adapter and an adapters output and simply adds them together. It also supports `stochastic_depth` which enables adapters to be dynamically switched off during training, making training more robust.

_class_ nemo.core.classes.mixins.adapter_mixin_strategies.AbstractAdapterStrategy
Bases: `ABC`

forward(_input:torch.Tensor_,_adapter:torch.nn.Module_,_*_,_module:[AdapterModuleMixin](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/intro.html.md#nemo.core.adapter\_mixins.AdapterModuleMixin "nemo.core.adapter\_mixins.AdapterModuleMixin")_,)
Forward method that defines how the output of the adapter should be merged with the input, or if it should be merged at all.

Also provides the module that called this strategy - thereby allowing access to all other adapters in the calling module. This can be useful if one adapter is a meta adapter, that combines the outputs of various adapters. In such a case, the input can be forwarded across all other adapters, collecting their outputs, and those outputs can then be merged via some strategy. For example, refer to :

*   [AdapterFusion: Non-Destructive Task Composition for Transfer Learning]([https://arxiv.org/abs/2005.00247](https://arxiv.org/abs/2005.00247.md))

*   [Exploiting Adapters for Cross-lingual Low-resource Speech Recognition]([https://arxiv.org/abs/2105.11905](https://arxiv.org/abs/2105.11905.md))

Parameters:
*   **input** – Original output tensor of the module, or the output of the previous adapter (if more than one adapters are enabled).

*   **adapter** – The adapter module that is currently required to perform the forward pass.

*   **module** – The calling module, in its entirety. It is a module that implements AdapterModuleMixin, therefore the strategy can access all other adapters in this module via module.adapter_layer.

Returns:
The result tensor, after one of the active adapters has finished its forward passes.

* * *

_class_ nemo.core.classes.mixins.adapter_mixin_strategies.ResidualAddAdapterStrategy(_stochastic\_depth:float=0.0_,_l2\_lambda:float=0.0_,)
Bases: `AbstractAdapterStrategy`

An implementation of residual addition of an adapter module with its input. Supports stochastic depth regularization.

forward(_input:torch.Tensor_,_adapter:torch.nn.Module_,_*_,_module:[AdapterModuleMixin](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/intro.html.md#nemo.core.adapter\_mixins.AdapterModuleMixin "nemo.core.adapter\_mixins.AdapterModuleMixin")_,)
A basic strategy, comprising of a residual connection over the input, after forward pass by the underlying adapter.

Parameters:
*   **input** – Original output tensor of the module, or the output of the previous adapter (if more than one adapters are enabled).

*   **adapter** – The adapter module that is currently required to perform the forward pass.

*   **module** – The calling module, in its entirety. It is a module that implements AdapterModuleMixin, therefore the strategy can access all other adapters in this module via module.adapter_layer.

Returns:
The result tensor, after one of the active adapters has finished its forward passes.

compute_output(_input:torch.Tensor_,_adapter:torch.nn.Module_,_*_,_module:[AdapterModuleMixin](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/intro.html.md#nemo.core.adapter\_mixins.AdapterModuleMixin "nemo.core.adapter\_mixins.AdapterModuleMixin")_,)→torch.Tensor
Compute the output of a single adapter to some input.

Parameters:
*   **input** – Original output tensor of the module, or the output of the previous adapter (if more than one adapters are enabled).

*   **adapter** – The adapter module that is currently required to perform the forward pass.

*   **module** – The calling module, in its entirety. It is a module that implements AdapterModuleMixin, therefore the strategy can access all other adapters in this module via module.adapter_layer.

Returns:
The result tensor, after one of the active adapters has finished its forward passes.

apply_stochastic_depth(_output:torch.Tensor_,_input:torch.Tensor_,_adapter:torch.nn.Module_,_*_,_module:[AdapterModuleMixin](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/intro.html.md#nemo.core.adapter\_mixins.AdapterModuleMixin "nemo.core.adapter\_mixins.AdapterModuleMixin")_,)
Compute and apply stochastic depth if probability is greater than 0.

Parameters:
*   **output** – The result tensor, after one of the active adapters has finished its forward passes.

*   **input** – Original output tensor of the module, or the output of the previous adapter (if more than one adapters are enabled).

*   **adapter** – The adapter module that is currently required to perform the forward pass.

*   **module** – The calling module, in its entirety. It is a module that implements AdapterModuleMixin, therefore the strategy can access all other adapters in this module via module.adapter_layer.

Returns:
The result tensor, after stochastic depth has been potentially applied to it.

compute_auxiliary_losses(_output:torch.Tensor_,_input:torch.Tensor_,_adapter:torch.nn.Module_,_*_,_module:[AdapterModuleMixin](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/intro.html.md#nemo.core.adapter\_mixins.AdapterModuleMixin "nemo.core.adapter\_mixins.AdapterModuleMixin")_,)
Compute any auxiliary losses and preserve it in the tensor registry.

Parameters:
*   **output** – The result tensor, after one of the active adapters has finished its forward passes.

*   **input** – Original output tensor of the module, or the output of the previous adapter (if more than one adapters are enabled).

*   **adapter** – The adapter module that is currently required to perform the forward pass.

*   **module** – The calling module, in its entirety. It is a module that implements AdapterModuleMixin, therefore the strategy can access all other adapters in this module via module.adapter_layer.

* * *

References[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/components.html.md#references "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------

[[2](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/components.html.md#id2)]

Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, Bruna Morrone, Quentin De Laroussilhe, Andrea Gesmundo, Mona Attariyan, and Sylvain Gelly. Parameter-efficient transfer learning for nlp. In _International Conference on Machine Learning_, 2790–2799. PMLR, 2019.

Links/Buttons:
- [1](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/components.html.md#id1)
- [2](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/components.html.md#id2)
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/components.html.md#references)
- [AccessMixin](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.mixins.access_mixins.AccessMixin)
- [AdapterModuleMixin](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/adapters/intro.html.md#nemo.core.adapter_mixins.AdapterModuleMixin)
- [https://arxiv.org/abs/2005.00247](https://arxiv.org/abs/2005.00247.md)
- [https://arxiv.org/abs/2105.11905](https://arxiv.org/abs/2105.11905.md)
- [https://arxiv.org/abs/2110.04366](https://arxiv.org/abs/2110.04366.md)
- [doi:10.48550/ARXIV.2110.04366](https://doi.org/10.48550/ARXIV.2110.04366.md)
