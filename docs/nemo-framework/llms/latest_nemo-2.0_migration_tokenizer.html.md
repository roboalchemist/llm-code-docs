# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/tokenizer.html.md

Title: Tokenizers — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/tokenizer.html

Published Time: Fri, 18 Jul 2025 19:26:15 GMT

Markdown Content:
Tokenizers[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/tokenizer.html.md#tokenizers "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

NeMo 1.0 (Previous Release)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/tokenizer.html.md#nemo-1-0-previous-release "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In NeMo 1.0, tokenizers were configured in the [tokenizer section](https://github.com/NVIDIA/NeMo/blob/54458fa9c1c913b2b0ea80f072b32d011c063e67/examples/nlp/language_modeling/conf/megatron_gpt_config.yaml.md#L130-L137) of the YAML configuration file.

NeMo 2.0 (New Release)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/tokenizer.html.md#nemo-2-0-new-release "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

In NeMo 2.0, tokenizers can be initialized directly in Python. [get_nmt_tokenizer](https://github.com/NVIDIA/NeMo/blob/54458fa9c1c913b2b0ea80f072b32d011c063e67/nemo/collections/nlp/modules/common/tokenizer_utils.py.md#L148) is a utility function used in NeMo to instantiate many of the common tokenizers used for llm and multimodal training. For example, the following code will construct a `GPT2BPETokenizer`:

from nemo.collections.nlp.modules.common.tokenizer_utils import get_nmt_tokenizer

tokenizer = get_nmt_tokenizer(
    library="megatron",
    model_name="GPT2BPETokenizer",
    vocab_file="/path/to/vocab",
    merges_file="/path/to/merges",
)

The following will construct a `SentencePiece` tokenizer:

from nemo.collections.nlp.modules.common.tokenizer_utils import get_nmt_tokenizer

tokenizer = get_nmt_tokenizer(
    library="sentencepiece",
    tokenizer_model='/path/to/sentencepiece/model'
)

The following will construct a `Hugging Face` tokenizer:

from nemo.collections.nlp.modules.common.tokenizer_utils import get_nmt_tokenizer

tokenizer = get_nmt_tokenizer(
    library="huggingface",
    model_name='nvidia/Minitron-4B-Base',
    use_fast=True,
)

Refer to the `get_nmt_tokenizer` code for a full list of supported arguments.

To set up the tokenizer using nemo_run, use the following code:

> import nemo_run as run
> from nemo.collections.common.tokenizers import SentencePieceTokenizer
> from nemo.collections.common.tokenizers.huggingface.auto_tokenizer import AutoTokenizer
> 
> # Set up Sentence Piece tokenizer
> tokenizer = run.Config(SentencePieceTokenizer, model_path="/path/to/tokenizer.model")
> 
> # Set up Hugging Face tokenizer
> tokenizer = run.Config(AutoTokenizer, pretrained_model_name="/path/to/tokenizer/model")

Refer to the [SentencePieceTokenizer](https://github.com/NVIDIA/NeMo/blob/45f35240a608c295ce199fb50b7336c346099617/nemo/collections/common/tokenizers/sentencepiece_tokenizer.py.md#L35) or [AutoTokenizer](https://github.com/NVIDIA/NeMo/blob/45f35240a608c295ce199fb50b7336c346099617/nemo/collections/common/tokenizers/huggingface/auto_tokenizer.py.md#L28) code for a full list of supported arguments.

To change the tokenizer path for model recipe, use the following code:

from nemo.collections import llm

recipe = partial(llm.llama3_8b)()

# Change path for Hugging Face tokenizer
recipe.data.tokenizer.pretrained_model_name = "/path/to/tokenizer/model"

# Change tokenizer path for Sentence Piece tokenizer
recipe.data.tokenizer.model_path = "/path/to/tokenizer.model"

Basic NeMo 2.0 recipes can contain predefined tokenizers. Visit [this page](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/mamba2_8b.py.md#L38) to see an example of setting up the tokenizer in the recipe.

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/tokenizer.html.md#nemo-2-0-new-release)
- [tokenizer section](https://github.com/NVIDIA/NeMo/blob/54458fa9c1c913b2b0ea80f072b32d011c063e67/examples/nlp/language_modeling/conf/megatron_gpt_config.yaml.md#L130-L137)
- [get_nmt_tokenizer](https://github.com/NVIDIA/NeMo/blob/54458fa9c1c913b2b0ea80f072b32d011c063e67/nemo/collections/nlp/modules/common/tokenizer_utils.py.md#L148)
- [SentencePieceTokenizer](https://github.com/NVIDIA/NeMo/blob/45f35240a608c295ce199fb50b7336c346099617/nemo/collections/common/tokenizers/sentencepiece_tokenizer.py.md#L35)
- [AutoTokenizer](https://github.com/NVIDIA/NeMo/blob/45f35240a608c295ce199fb50b7336c346099617/nemo/collections/common/tokenizers/huggingface/auto_tokenizer.py.md#L28)
- [this page](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/recipes/mamba2_8b.py.md#L38)
