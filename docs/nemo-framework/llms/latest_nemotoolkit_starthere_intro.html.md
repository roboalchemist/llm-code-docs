# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/starthere/intro.html.md

Title: Introduction — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/starthere/intro.html

Published Time: Fri, 05 Sep 2025 19:00:57 GMT

Markdown Content:
Introduction[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/starthere/intro.html.md#introduction "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

Training generative AI architectures typically requires significant data and computing resources. NeMo utilizes [PyTorch Lightning](https://www.pytorchlightning.ai/) for efficient and performant multi-GPU/multi-node mixed-precision training. NeMo is built on top of NVIDIA’s powerful Megatron Core library and Transformer Engine for its Large Language Models (LLMs) and Multimodal Models (MMs), leveraging cutting-edge advancements in model training and optimization. For Speech AI applications, Automatic Speech Recognition (ASR) and Text-to-Speech (TTS), NeMo is developed with native PyTorch and PyTorch Lightning, ensuring seamless integration and ease of use. Future updates are planned to align Speech AI models with the Megatron framework, enhancing training efficiency and model performance.

[NVIDIA NeMo Framework](https://github.com/NVIDIA/NeMo) features separate collections for Large Language Models (LLMs), Multimodal Models (MMs), Computer Vision (CV), Automatic Speech Recognition (ASR), and Text-to-Speech (TTS) models. Each collection comprises prebuilt modules that include everything needed to train on your data. These modules can be easily customized, extended, and composed to create new generative AI model architectures.

Pre-trained NeMo models are available to download on [NGC](https://catalog.ngc.nvidia.com/models?query=nemo&orderBy=weightPopularDESC) and [HuggingFace Hub](https://huggingface.co/nvidia).

Prerequisites[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/starthere/intro.html.md#prerequisites "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------

Before using NeMo, make sure you meet the following prerequisites:

1.   Python version 3.10 or above.

2.   Pytorch version 1.13.1 or 2.0+.

3.   Access to an NVIDIA GPU for model training.

Installation[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/starthere/intro.html.md#installation "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

Refer to the NeMo Framework [User Guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/installation.html.md) for the latest installation instructions.

Quick Start Guide[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/starthere/intro.html.md#quick-start-guide "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

To explore NeMo’s capabilities in LLM, ASR, and TTS, follow the example below based on the [Audio Translation](https://github.com/NVIDIA/NeMo/blob/stable/tutorials/AudioTranslationSample.ipynb) tutorial. Ensure NeMo is installed before proceeding.

# Import NeMo's ASR, NLP and TTS collections
import nemo.collections.asr as nemo_asr
import nemo.collections.nlp as nemo_nlp
import nemo.collections.tts as nemo_tts

# Download an audio file that we will transcribe, translate, and convert the written translation to speech
import wget
wget.download("https://nemo-public.s3.us-east-2.amazonaws.com/zh-samples/common_voice_zh-CN_21347786.mp3")

# Instantiate a Mandarin speech recognition model and transcribe an audio file.
asr_model = nemo_asr.models.ASRModel.from_pretrained(model_name="stt_zh_citrinet_1024_gamma_0_25")
mandarin_text = asr_model.transcribe(['common_voice_zh-CN_21347786.mp3'])
print(mandarin_text)

# Instantiate Neural Machine Translation model and translate the text
nmt_model = nemo_nlp.models.MTEncDecModel.from_pretrained(model_name="nmt_zh_en_transformer24x6")
english_text = nmt_model.translate(mandarin_text)
print(english_text)

# Instantiate a spectrogram generator (which converts text -> spectrogram)
# and vocoder model (which converts spectrogram -> audio waveform)
spectrogram_generator = nemo_tts.models.FastPitchModel.from_pretrained(model_name="tts_en_fastpitch")
vocoder = nemo_tts.models.HifiGanModel.from_pretrained(model_name="tts_en_hifigan")

# Parse the text input, generate the spectrogram, and convert it to audio
parsed_text = spectrogram_generator.parse(english_text[0])
spectrogram = spectrogram_generator.generate_spectrogram(tokens=parsed_text)
audio = vocoder.convert_spectrogram_to_audio(spec=spectrogram)

# Save the audio to a file
import soundfile as sf
sf.write("output_audio.wav", audio.to('cpu').detach().numpy()[0], 22050)

For detailed tutorials and documentation on specific tasks or to learn more about NeMo, check out the NeMo [tutorials](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/starthere/tutorials.html.md) or dive deeper into the documentation, such as learning about ASR in [here](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/intro.html.md).

Discussion Board[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/starthere/intro.html.md#discussion-board "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------

For additional information and questions, visit the [NVIDIA NeMo Discussion Board](https://github.com/NVIDIA/NeMo/discussions).

Contribute to NeMo[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/starthere/intro.html.md#contribute-to-nemo "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------

Community contributions are welcome! See the [CONTRIBUTING.md](https://github.com/NVIDIA/NeMo/blob/stable/CONTRIBUTING.md) file for how to contribute.

License[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/starthere/intro.html.md#license "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

NeMo is released under the [Apache 2.0 license](https://github.com/NVIDIA/NeMo/blob/stable/LICENSE).

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/starthere/intro.html.md#license)
- [NeMo Framework User Guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/index.html)
- [PyTorch Lightning](https://www.pytorchlightning.ai/)
- [NVIDIA NeMo Framework](https://github.com/NVIDIA/NeMo)
- [NGC](https://catalog.ngc.nvidia.com/models?query=nemo&orderBy=weightPopularDESC)
- [HuggingFace Hub](https://huggingface.co/nvidia)
- [User Guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/installation.html.md)
- [Audio Translation](https://github.com/NVIDIA/NeMo/blob/stable/tutorials/AudioTranslationSample.ipynb)
- [tutorials](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/starthere/tutorials.html.md)
- [here](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/intro.html.md)
- [NVIDIA NeMo Discussion Board](https://github.com/NVIDIA/NeMo/discussions)
- [CONTRIBUTING.md](https://github.com/NVIDIA/NeMo/blob/stable/CONTRIBUTING.md)
- [Apache 2.0 license](https://github.com/NVIDIA/NeMo/blob/stable/LICENSE)
