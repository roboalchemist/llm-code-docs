# Source: https://llamafactory.readthedocs.io/zh-cn/latest/advanced/acceleration.html

Title: 加速 - LLaMA Factory

URL Source: https://llamafactory.readthedocs.io/zh-cn/latest/advanced/acceleration.html

Markdown Content:
[View this page](https://llamafactory.readthedocs.io/zh-cn/latest/_sources/advanced/acceleration.rst.txt "View this page")

Toggle table of contents sidebar

加速[¶](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/acceleration.html#id1 "此标题的永久链接")
-------------------------------------------------------------------------------------------------

LLaMA-Factory 支持多种加速技术，包括：[FlashAttention](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/acceleration.html#flashattn) 、 [Unsloth](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/acceleration.html#sloth) 、 [Liger Kernel](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/acceleration.html#ligerkernel) 。

FlashAttention[¶](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/acceleration.html#flashattention "此标题的永久链接")
------------------------------------------------------------------------------------------------------------------------

[FlashAttention](https://github.com/Dao-AILab/flash-attention/) 能够加快注意力机制的运算速度，同时减少对内存的使用。

如果您想使用 FlashAttention,请在启动训练时在训练配置文件中添加以下参数：

flash_attn: fa2

Unsloth[¶](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/acceleration.html#unsloth "此标题的永久链接")
----------------------------------------------------------------------------------------------------------

[Unsloth](https://github.com/unslothai/unsloth/) 框架支持 Llama, Mistral, Phi-3, Gemma, Yi, DeepSeek, Qwen等大语言模型并且支持 4-bit 和 16-bit 的 QLoRA/LoRA 微调，该框架在提高运算速度的同时还减少了显存占用。

如果您想使用 Unsloth, 请在启动训练时在训练配置文件中添加以下参数：

use_unsloth: True

Liger Kernel[¶](https://llamafactory.readthedocs.io/zh-cn/latest/advanced/acceleration.html#liger-kernel "此标题的永久链接")
--------------------------------------------------------------------------------------------------------------------

[Liger Kernel](https://github.com/linkedin/Liger-Kernel/) 是一个大语言模型训练的性能优化框架, 可有效地提高吞吐量并减少内存占用。

如果您想使用 Liger Kernel,请在启动训练时在训练配置文件中添加以下参数：

enable_liger_kernel: True
