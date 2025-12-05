# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/best-practices.html.md

Title: Best Practices for NeMo Developers#

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/best-practices.html

Published Time: Fri, 18 Jul 2025 19:29:26 GMT

Markdown Content:
Import Guarding[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/best-practices.html.md#import-guarding "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------

Sometimes, developers have an optional package they would like to use only when it is available. In this case, the developer may want to follow different code paths depending on whether the optional package is present. Other times, a developer may want to require a package for their collection, but they may not want to make that package required for all collections. In either of these cases, it’s important to guard the optional imports.

In [import_utils.py](https://github.com/NVIDIA/NeMo/blob/main/nemo/utils/import_utils.py.md), NeMo provides the utilities required to handle the import of optional packages effectively. This script is adapted from cuML’s [safe_imports module](https://github.com/rapidsai/cuml/blob/e93166ea0dddfa8ef2f68c6335012af4420bc8ac/python/cuml/internals/safe_imports.py.md). The two functions developers should be aware of are:

1.   [safe_import](https://github.com/NVIDIA/NeMo/blob/a9746a654d37d3451bcc33ad58cf8378efe787b7/nemo/utils/import_utils.py.md#L243): A function used to import optional modules. Developers can provide an optional error message to be displayed in the case the module is used after a failed import. Alternatively, they can provide an alternate module to be used if the import of the optional module fails. `safe_import` returns a tuple containing:

    1.   the successfully imported optional module or, if the import fails, the given alternate module or a placeholder `UnavailableMeta` class instance and

    2.   a boolean indicating whether the import of the optional module was successful.

The returned boolean can be used throughout the script to ensure you only use the optional module when it is present. For example, in the LLM collection, we use `safe_import` to determine whether TE is installed. When [creating the default GPT layer spec](https://github.com/NVIDIA/NeMo/blob/a98c5ed2c3027d90cd16b505fecfb54097d0b743/nemo/collections/llm/gpt/model/base.py.md#L115-L119), we use the value of `HAVE_TE` to determine whether the default layer spec uses the transformer engine:

_, HAVE_TE = safe_import("transformer_engine")

...

def default_layer_spec(config: "GPTConfig") -> ModuleSpec:
   if HAVE_TE:
     return transformer_engine_layer_spec(config)
   else:
     return local_layer_spec(config)

2.   [safe_import_from](https://github.com/NVIDIA/NeMo/blob/a9746a654d37d3451bcc33ad58cf8378efe787b7/nemo/utils/import_utils.py.md#L283): A function used to import symbols from modules that may not be available. As in the case of `safe_import`, developers can provide a message to display whenever the symbol is used after a failed import, or they can provide an object to be used in place of the symbol if the import of the symbol fails. `safe_import_from` returns the same tuple containing:

    1.   the successfully imported optional symbol or, if the import fails, the given alternate object or a placeholder `UnavailableMeta` class instance and

    2.   a boolean indicating whether the import of the desired symbol was successful.

`safe_import` and `safe_import_from` are used throughout the NeMo codebase. [megatron_gpt_model.py](https://github.com/NVIDIA/NeMo/blob/e35a6592f53ee34b1ec2fc3f1e009dd1ebc79e65/nemo/collections/nlp/models/language_modeling/megatron_gpt_model.py.md#L131-L136) is one example:

transformer_engine, HAVE_TE = safe_import("transformer_engine")
te_module, HAVE_TE_MODULE = safe_import_from("transformer_engine.pytorch", "module")
get_gpt_layer_with_te_and_hyena_spec, HAVE_HYENA_SPEC = safe_import_from(
   "nemo.collections.nlp.modules.common.hyena.hyena_spec", "get_gpt_layer_with_te_and_hyena_spec"
)
HAVE_TE = HAVE_TE and HAVE_TE_MODULE and HAVE_HYENA_SPEC

Transformer Engine is required for FP8 and Cuda Graphs. The value of `HAVE_TE` is used throughout `megatron_gpt_model.py` to determine whether these features can be enabled and to gracefully handle the case when a user requests these features and they are not present. For example, when a user enables cuda graphs, we use the value of `HAVE_TE` to ensure that Transformer Engine is present. If `HAVE_TE` is False, [a useful message is printed](https://github.com/NVIDIA/NeMo/blob/e35a6592f53ee34b1ec2fc3f1e009dd1ebc79e65/nemo/collections/nlp/models/language_modeling/megatron_gpt_model.py.md#L2143).

One consequence of import guarding is suppose a developer expects a particular module to be present, but the import fails. If the import is guarded, this will cause the execution to continue with a different code path than the developer expects. During development, a user may find it useful to run in `debug` mode. This causes the logger to [report any failed imports](https://github.com/NVIDIA/NeMo/blob/a9746a654d37d3451bcc33ad58cf8378efe787b7/nemo/utils/import_utils.py.md#L271) along with the corresponding traceback, which can help the developer catch any unexpected failed imports and understand why the expected modules are missing. Debug mode can be enabled with the following code:

from nemo.utils import logging
logging.set_verbosity(logging.DEBUG)

Working with Hugging Face Models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/best-practices.html.md#working-with-hugging-face-models "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Some of the NeMo examples require accessing gated Hugging Face models. If you try to run a model and get an error that looks like this:

OSError: You are trying to access a gated repo.
Make sure to have access to it at <URL>

you likely need to set up your `HF_TOKEN` environment variable. You must first request access to the gated model by following the URL provided. After access has been granted, make sure you have a Hugging Face access token (if you do not, follow [this tutorial](https://huggingface.co/docs/hub/en/security-tokens.md#how-to-manage-user-access-tokens) to generate one). Finally, be sure to set the `HF_TOKEN` variable in your environment:

export HF_TOKEN=<your_access_token>

Working with scripts in NeMo 2.0[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/best-practices.html.md#working-with-scripts-in-nemo-2-0 "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When working with any scripts in NeMo 2.0, please make sure you wrap your code in an `if __name__ == "__main__":` block. Otherwise, your code may hang unexpectedly.

The reason for this is that NeMo 2.0 uses Python’s `multiprocessing` module in the backend when running a multi-GPU job. The multiprocessing module will create new Python processes that will import the current module (your script). If you did not add `__name__== "__main__"`, then your module will spawn new processes which import the module and then each spawn new processes. This results in an infinite loop of processing spawning.

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/best-practices.html.md#working-with-scripts-in-nemo-2-0)
- [import_utils.py](https://github.com/NVIDIA/NeMo/blob/main/nemo/utils/import_utils.py.md)
- [safe_imports module](https://github.com/rapidsai/cuml/blob/e93166ea0dddfa8ef2f68c6335012af4420bc8ac/python/cuml/internals/safe_imports.py.md)
- [safe_import](https://github.com/NVIDIA/NeMo/blob/a9746a654d37d3451bcc33ad58cf8378efe787b7/nemo/utils/import_utils.py.md#L243)
- [creating the default GPT layer spec](https://github.com/NVIDIA/NeMo/blob/a98c5ed2c3027d90cd16b505fecfb54097d0b743/nemo/collections/llm/gpt/model/base.py.md#L115-L119)
- [safe_import_from](https://github.com/NVIDIA/NeMo/blob/a9746a654d37d3451bcc33ad58cf8378efe787b7/nemo/utils/import_utils.py.md#L283)
- [megatron_gpt_model.py](https://github.com/NVIDIA/NeMo/blob/e35a6592f53ee34b1ec2fc3f1e009dd1ebc79e65/nemo/collections/nlp/models/language_modeling/megatron_gpt_model.py.md#L131-L136)
- [a useful message is printed](https://github.com/NVIDIA/NeMo/blob/e35a6592f53ee34b1ec2fc3f1e009dd1ebc79e65/nemo/collections/nlp/models/language_modeling/megatron_gpt_model.py.md#L2143)
- [report any failed imports](https://github.com/NVIDIA/NeMo/blob/a9746a654d37d3451bcc33ad58cf8378efe787b7/nemo/utils/import_utils.py.md#L271)
- [this tutorial](https://huggingface.co/docs/hub/en/security-tokens.md#how-to-manage-user-access-tokens)
