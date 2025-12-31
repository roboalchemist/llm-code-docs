# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md

Title: Checkpoints — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html

Published Time: Fri, 18 Jul 2025 19:26:53 GMT

Markdown Content:
Checkpoints[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md#checkpoints "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

There are two main ways to load pretrained checkpoints in NeMo as described in [Checkpoints](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/results.html.md).

*   Using the `restore_from()` method to load a local checkpoint file (`.nemo`), or

*   Using the `from_pretrained()` method to download and set up a checkpoint from NGC.

Note that these instructions are for loading fully trained checkpoints for evaluation or fine-tuning. For resuming an unfinished training experiment, use the Experiment Manager to do so by setting the `resume_if_exists` flag to `True`.

Local Checkpoints[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md#local-checkpoints "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

*   **Save Model Checkpoints**: NeMo automatically saves final model checkpoints with `.nemo` suffix. You could also manually save any model checkpoint using `model.save_to(<checkpoint_path>.nemo)`.

*   **Load Model Checkpoints**: if you’d like to load a checkpoint saved at `<path/to/checkpoint/file.nemo>`, use the `restore_from()` method below, where `<MODEL_BASE_CLASS>` is the TTS model class of the original checkpoint.

import nemo.collections.tts as nemo_tts
model = nemo_tts.models.<MODEL_BASE_CLASS>.restore_from(restore_path="<path/to/checkpoint/file.nemo>")

NGC Pretrained Checkpoints[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md#ngc-pretrained-checkpoints "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The NGC [NeMo Text to Speech collection](https://catalog.ngc.nvidia.com/orgs/nvidia/collections/nemo_tts.md) aggregates model cards that contain detailed information about checkpoints of various models trained on various datasets. The tables below in [Checkpoints](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md#ngc-tts-models) list part of available TTS models from NGC including speech/text aligners, acoustic models, and vocoders.

### Load Model Checkpoints[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md#load-model-checkpoints "Link to this heading")

The models can be accessed via the `from_pretrained()` method inside the TTS Model class. In general, you can load any of these models with code in the following format,

import nemo.collections.tts as nemo_tts
model = nemo_tts.models.<MODEL_BASE_CLASS>.from_pretrained(model_name="<MODEL_NAME>")

where `<MODEL_NAME>` is the value in `Model Name` column in the tables in [Checkpoints](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md#ngc-tts-models). These names are predefined in the each model’s member function `self.list_available_models()`. For example, the available NGC FastPitch model names can be found,

In [1]: import nemo.collections.tts as nemo_tts

In [2]: nemo_tts.models.FastPitchModel.list_available_models()
Out[2]:
[PretrainedModelInfo(
 pretrained_model_name=tts_en_fastpitch,
 description=This model is trained on LJSpeech sampled at 22050Hz with and can be used to generate female English voices with an American accent. It is ARPABET-based.,
 location=https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_en_fastpitch/versions/1.8.1/files/tts_en_fastpitch_align.nemo,
 class_=<class 'nemo.collections.tts.models.fastpitch.FastPitchModel'>
 ),
 PretrainedModelInfo(
 pretrained_model_name=tts_en_fastpitch_ipa,
 description=This model is trained on LJSpeech sampled at 22050Hz with and can be used to generate female English voices with an American accent. It is IPA-based.,
 location=https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_en_fastpitch/versions/IPA_1.13.0/files/tts_en_fastpitch_align_ipa.nemo,
 class_=<class 'nemo.collections.tts.models.fastpitch.FastPitchModel'>
 ),
 PretrainedModelInfo(
 pretrained_model_name=tts_en_fastpitch_multispeaker,
 description=This model is trained on HiFITTS sampled at 44100Hz with and can be used to generate male and female English voices with an American accent.,
 location=https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_en_multispeaker_fastpitchhifigan/versions/1.10.0/files/tts_en_fastpitch_multispeaker.nemo,
 class_=<class 'nemo.collections.tts.models.fastpitch.FastPitchModel'>
 ),
 PretrainedModelInfo(
 pretrained_model_name=tts_de_fastpitch_singlespeaker,
 description=This model is trained on a single male speaker data in OpenSLR Neutral German Dataset sampled at 22050Hz and can be used to generate male German voices.,
 location=https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_de_fastpitchhifigan/versions/1.10.0/files/tts_de_fastpitch_align.nemo,
 class_=<class 'nemo.collections.tts.models.fastpitch.FastPitchModel'>
 ),
 PretrainedModelInfo(
 pretrained_model_name=tts_de_fastpitch_multispeaker_5,
 description=This model is trained on 5 speakers in HUI-Audio-Corpus-German clean subset sampled at 44100Hz with and can be used to generate male and female German voices.,
 location=https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_de_fastpitch_multispeaker_5/versions/1.11.0/files/tts_de_fastpitch_multispeaker_5.nemo,
 class_=<class 'nemo.collections.tts.models.fastpitch.FastPitchModel'>
 )]

From the above key-value pair `pretrained_model_name=tts_en_fastpitch`, you could get the model name `tts_en_fastpitch` and load it by running,

model = nemo_tts.models.FastPitchModel.from_pretrained(model_name="tts_en_fastpitch")

If you would like to programmatically list the models available for a particular base class, you can use the `list_available_models()` method,

nemo_tts.models.<MODEL_BASE_CLASS>.list_available_models()

### Inference and Audio Generation[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md#inference-and-audio-generation "Link to this heading")

NeMo TTS supports both cascaded and end-to-end models to synthesize audios. Most of steps in between are the same except that cascaded models need to load an extra vocoder model before generating audios. Below code snippet demonstrates steps of generating a audio sample from a text input using a cascaded FastPitch and HiFiGAN models. Please refer to NeMo TTS Collection API for detailed implementation of model classes.

import nemo.collections.tts as nemo_tts
# Load mel spectrogram generator
spec_generator = nemo_tts.models.FastPitchModel.from_pretrained("tts_en_fastpitch")
# Load vocoder
vocoder = nemo_tts.models.HifiGanModel.from_pretrained(model_name="tts_en_hifigan")
# Generate audio
import soundfile as sf
parsed = spec_generator.parse("You can type your sentence here to get nemo to produce speech.")
spectrogram = spec_generator.generate_spectrogram(tokens=parsed)
audio = vocoder.convert_spectrogram_to_audio(spec=spectrogram)
# Save the audio to disk in a file called speech.wav
sf.write("speech.wav", audio.to('cpu').numpy(), 22050)

### Fine-Tuning on Different Datasets[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md#fine-tuning-on-different-datasets "Link to this heading")

There are multiple TTS tutorials provided in the directory of [tutorials/tts/](https://github.com/NVIDIA/NeMo/tree/stable/tutorials/tts.md). Most of these tutorials demonstrate how to instantiate a pre-trained model, and prepare the model for fine-tuning on datasets with the same language or different languages, the same speaker or different speakers.

*   **cross-lingual fine-tuning**: [NVIDIA/NeMo](https://github.com/NVIDIA/NeMo/tree/stable/tutorials/tts/FastPitch_GermanTTS_Training.ipynb.md)

*   **cross-speaker fine-tuning**: [NVIDIA/NeMo](https://github.com/NVIDIA/NeMo/tree/stable/tutorials/tts/FastPitch_Finetuning.ipynb.md)

NGC TTS Models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md#ngc-tts-models "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

This section summarizes a full list of available NeMo TTS models that have been released in [NGC NeMo Text to Speech Collection](https://catalog.ngc.nvidia.com/orgs/nvidia/collections/nemo_tts/entities.md). You can download model checkpoints of your interest via either way below,

*   `wget '<CHECKPOINT_URL_IN_THE_TABLE>'`

*   `curl -LO '<CHECKPOINT_URL_IN_THE_TABLE>'`

### Speech/Text Aligners[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md#speech-text-aligners "Link to this heading")

| Locale | Model Name | Dataset | Sampling Rate | #Spk | Phoneme Unit | Model Class | Overview | Checkpoint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| en-US | tts_en_radtts_aligner | LJSpeech | 22050Hz | 1 | ARPABET | nemo.collections.tts.models.aligner.AlignerModel | [tts_en_radtts_aligner](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_radtts_aligner.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_en_radtts_aligner/versions/ARPABET_1.11.0/files/Aligner.nemo` |
| en-US | tts_en_radtts_aligner_ipa | LJSpeech | 22050Hz | 1 | IPA | nemo.collections.tts.models.aligner.AlignerModel | [tts_en_radtts_aligner](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_radtts_aligner.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_en_radtts_aligner/versions/IPA_1.13.0/files/Aligner.nemo` |

### Mel-Spectrogram Generators[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md#mel-spectrogram-generators "Link to this heading")

| Locale | Model Name | Dataset | Sampling Rate | #Spk | Symbols | Model Class | Overview | Checkpoint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| en-US | tts_en_fastpitch | LJSpeech | 22050Hz | 1 | ARPABET | nemo.collections.tts.models.fastpitch.FastPitchModel | [tts_en_fastpitch](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_fastpitch.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_en_fastpitch/versions/1.8.1/files/tts_en_fastpitch_align.nemo` |
| en-US | tts_en_fastpitch_ipa | LJSpeech | 22050Hz | 1 | IPA | nemo.collections.tts.models.fastpitch.FastPitchModel | [tts_en_fastpitch](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_fastpitch.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_en_fastpitch/versions/IPA_1.13.0/files/tts_en_fastpitch_align_ipa.nemo` |
| en-US | tts_en_fastpitch_multispeaker | HiFiTTS | 44100Hz | 10 | ARPABET | nemo.collections.tts.models.fastpitch.FastPitchModel | [tts_en_multispeaker_fastpitchhifigan](https://ngc.nvidia.com/models/nvidia:nemo:tts_en_multispeaker_fastpitchhifigan.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_en_multispeaker_fastpitchhifigan/versions/1.10.0/files/tts_en_fastpitch_multispeaker.nemo` |
| en-US | tts_en_lj_mixertts | LJSpeech | 22050Hz | 1 | ARPABET | nemo.collections.tts.models.mixer_tts.MixerTTSModel | [tts_en_lj_mixertts](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_lj_mixertts.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_en_lj_mixertts/versions/1.6.0/files/tts_en_lj_mixertts.nemo` |
| en-US | tts_en_lj_mixerttsx | LJSpeech | 22050Hz | 1 | ARPABET | nemo.collections.tts.models.mixer_tts.MixerTTSModel | [tts_en_lj_mixerttsx](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_lj_mixerttsx.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_en_lj_mixerttsx/versions/1.6.0/files/tts_en_lj_mixerttsx.nemo` |
| en-US | RAD-TTS | TBD | TBD | TBD | ARPABET | nemo.collections.tts.models.radtts.RadTTSModel | TBD |  |
| en-US | tts_en_tacotron2 | LJSpeech | 22050Hz | 1 | ARPABET | nemo.collections.tts.models.tacotron2.Tacotron2Model | [tts_en_tacotron2](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_tacotron2.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_en_tacotron2/versions/1.10.0/files/tts_en_tacotron2.nemo` |
| de-DE | tts_de_fastpitch_multispeaker_5 | HUI Audio Corpus German | 44100Hz | 5 | ARPABET | nemo.collections.tts.models.fastpitch.FastPitchModel | [tts_de_fastpitch_multispeaker_5](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_de_fastpitch_multispeaker_5.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_de_fastpitch_multispeaker_5/versions/1.11.0/files/tts_de_fastpitch_multispeaker_5.nemo` |
| de-DE | tts_de_fastpitch_singleSpeaker_thorstenNeutral_2102 | Thorsten Müller Neutral 21.02 dataset | 22050Hz | 1 | Graphemes | nemo.collections.tts.models.fastpitch.FastPitchModel | [tts_de_fastpitchhifigan](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_de_fastpitchhifigan.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_de_fastpitchhifigan/versions/1.15.0/files/tts_de_fastpitch_thorstens2102.nemo` |
| de-DE | tts_de_fastpitch_singleSpeaker_thorstenNeutral_2210 | Thorsten Müller Neutral 22.10 dataset | 22050Hz | 1 | Graphemes | nemo.collections.tts.models.fastpitch.FastPitchModel | [tts_de_fastpitchhifigan](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_de_fastpitchhifigan.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_de_fastpitchhifigan/versions/1.15.0/files/tts_de_fastpitch_thorstens2210.nemo` |
| es | tts_es_fastpitch_multispeaker | OpenSLR crowdsourced Latin American Spanish | 44100Hz | 174 | IPA | nemo.collections.tts.models.fastpitch.FastPitchModel | [tts_es_multispeaker_fastpitchhifigan](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/tts_es_multispeaker_fastpitchhifigan.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_es_multispeaker_fastpitchhifigan/versions/1.15.0/files/tts_es_fastpitch_multispeaker.nemo` |
| zh-CN | tts_zh_fastpitch_sfspeech | SFSpeech Chinese/English Bilingual Speech | 22050Hz | 1 | pinyin | nemo.collections.tts.models.fastpitch.FastPitchModel | [tts_zh_fastpitch_hifigan_sfspeech](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_zh_fastpitch_hifigan_sfspeech.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_zh_fastpitch_hifigan_sfspeech/versions/1.15.0/files/tts_zh_fastpitch_sfspeech.nemo` |

### Vocoders[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md#vocoders "Link to this heading")

| Locale | Model Name | Spectrogram Generator | Dataset | Sampling Rate | #Spk | Model Class | Overview | Checkpoint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| en-US | tts_en_hifigan | librosa.filters.mel | LJSpeech | 22050Hz | 1 | nemo.collections.tts.models.hifigan.HifiGanModel | [tts_en_hifigan](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_hifigan.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_hifigan/versions/1.0.0rc1/files/tts_hifigan.nemo` |
| en-US | tts_en_lj_hifigan_ft_mixertts | Mixer-TTS | LJSpeech | 22050Hz | 1 | nemo.collections.tts.models.hifigan.HifiGanModel | [tts_en_lj_hifigan](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_lj_hifigan.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_en_lj_hifigan/versions/1.6.0/files/tts_en_lj_hifigan_ft_mixertts.nemo` |
| en-US | tts_en_lj_hifigan_ft_mixerttsx | Mixer-TTS-X | LJSpeech | 22050Hz | 1 | nemo.collections.tts.models.hifigan.HifiGanModel | [tts_en_lj_hifigan](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_lj_hifigan.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_en_lj_hifigan/versions/1.6.0/files/tts_en_lj_hifigan_ft_mixerttsx.nemo` |
| en-US | tts_en_hifitts_hifigan_ft_fastpitch | FastPitch | HiFiTTS | 44100Hz | 10 | nemo.collections.tts.models.hifigan.HifiGanModel | [tts_en_multispeaker_fastpitchhifigan](https://ngc.nvidia.com/models/nvidia:nemo:tts_en_multispeaker_fastpitchhifigan.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_en_multispeaker_fastpitchhifigan/versions/1.10.0/files/tts_en_hifitts_hifigan_ft_fastpitch.nemo` |
| en-US | tts_en_lj_univnet | librosa.filters.mel | LJSpeech | 22050Hz | 1 | nemo.collections.tts.models.univnet.UnivNetModel | [tts_en_lj_univnet](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_lj_univnet.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_en_lj_univnet/versions/1.7.0/files/tts_en_lj_univnet.nemo` |
| en-US | tts_en_libritts_univnet | librosa.filters.mel | LibriTTS | 24000Hz | 1 | nemo.collections.tts.models.univnet.UnivNetModel | [tts_en_libritts_univnet](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_libritts_univnet.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_en_libritts_univnet/versions/1.7.0/files/tts_en_libritts_multispeaker_univnet.nemo` |
| en-US | tts_en_waveglow_88m | librosa.filters.mel | LJSpeech | 22050Hz | 1 | nemo.collections.tts.models.waveglow.WaveGlowModel | [tts_en_waveglow_88m](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_waveglow_88m.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_waveglow_88m/versions/1.0.0/files/tts_waveglow.nemo` |
| de-DE | tts_de_hui_hifigan_ft_fastpitch_multispeaker_5 | FastPitch | HUI Audio Corpus German | 44100Hz | 5 | nemo.collections.tts.models.hifigan.HifiGanModel | [tts_de_fastpitch_multispeaker_5](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_de_fastpitch_multispeaker_5.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_de_fastpitch_multispeaker_5/versions/1.11.0/files/tts_de_hui_hifigan_ft_fastpitch_multispeaker_5.nemo` |
| de-DE | tts_de_hifigan_singleSpeaker_thorstenNeutral_2102 | FastPitch | Thorsten Müller Neutral 21.02 dataset | 22050Hz | 1 | nemo.collections.tts.models.hifigan.HifiGanModel | [tts_de_fastpitchhifigan](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_de_fastpitchhifigan.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_de_fastpitchhifigan/versions/1.15.0/files/tts_de_hifigan_thorstens2102.nemo` |
| de-DE | tts_de_hifigan_singleSpeaker_thorstenNeutral_2210 | FastPitch | Thorsten Müller Neutral 22.10 dataset | 22050Hz | 1 | nemo.collections.tts.models.hifigan.HifiGanModel | [tts_de_fastpitchhifigan](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_de_fastpitchhifigan.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_de_fastpitchhifigan/versions/1.15.0/files/tts_de_hifigan_thorstens2210.nemo` |
| es | tts_es_hifigan_ft_fastpitch_multispeaker | FastPitch | OpenSLR crowdsourced Latin American Spanish | 44100Hz | 174 | nemo.collections.tts.models.hifigan.HifiGanModel | [tts_es_multispeaker_fastpitchhifigan](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/tts_es_multispeaker_fastpitchhifigan.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_es_multispeaker_fastpitchhifigan/versions/1.15.0/files/tts_es_hifigan_ft_fastpitch_multispeaker.nemo` |
| zh-CN | tts_zh_hifigan_sfspeech | FastPitch | SFSpeech Chinese/English Bilingual Speech | 22050Hz | 1 | nemo.collections.tts.models.hifigan.HifiGanModel | [tts_zh_fastpitch_hifigan_sfspeech](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_zh_fastpitch_hifigan_sfspeech.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_zh_fastpitch_hifigan_sfspeech/versions/1.15.0/files/tts_zh_hifigan_sfspeech.nemo` |

### End2End models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md#end2end-models "Link to this heading")

| Locale | Model Name | Dataset | Sampling Rate | #Spk | Phoneme Unit | Model Class | Overview | Checkpoint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| en-US | tts_en_lj_vits | LJSpeech | 22050Hz | 1 | IPA | nemo.collections.tts.models.vits.VitsModel | [tts_en_lj_vits](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_lj_vits.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_en_lj_vits/versions/1.13.0/files/vits_ljspeech_fp16_full.nemo` |
| en-US | tts_en_hifitts_vits | HiFiTTS | 44100Hz | 10 | IPA | nemo.collections.tts.models.vits.VitsModel | [tts_en_hifitts_vits](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_hifitts_vits.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/tts_en_hifitts_vits/versions/r1.15.0/files/vits_en_hifitts.nemo` |

### Codec models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md#codec-models "Link to this heading")

| Model Name | Dataset | Sampling Rate | Model Class | Overview | Checkpoint |
| --- | --- | --- | --- | --- | --- |
| audio_codec_16khz_small | Libri-Light | 16000Hz | nemo.collections.tts.models.AudioCodecModel | [audio_codec_16khz_small](https://ngc.nvidia.com/catalog/models/nvidia:nemo:audio_codec_16khz_small.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/audio_codec_16khz_small/versions/v1/files/audio_codec_16khz_small.nemo` |
| mel_codec_22khz_medium | LibriVox and Common Voice | 22050Hz | nemo.collections.tts.models.AudioCodecModel | [mel_codec_22khz_medium](https://ngc.nvidia.com/catalog/models/nvidia:nemo:mel_codec_22khz_medium.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/mel_codec_22khz_medium/versions/v1/files/mel_codec_22khz_medium.nemo` |
| mel_codec_44khz_medium | LibriVox and Common Voice | 44100Hz | nemo.collections.tts.models.AudioCodecModel | [mel_codec_44khz_medium](https://ngc.nvidia.com/catalog/models/nvidia:nemo:mel_codec_44khz_medium.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/mel_codec_44khz_medium/versions/v1/files/mel_codec_44khz_medium.nemo` |
| mel_codec_22khz_fullband_medium | LibriVox and Common Voice | 22050Hz | nemo.collections.tts.models.AudioCodecModel | [mel_codec_22khz_fullband_medium](https://ngc.nvidia.com/catalog/models/nvidia:nemo:mel_codec_22khz_fullband_medium.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/mel_codec_22khz_fullband_medium/versions/v1/files/mel_codec_22khz_fullband_medium.nemo` |
| mel_codec_44khz_fullband_medium | LibriVox and Common Voice | 44100Hz | nemo.collections.tts.models.AudioCodecModel | [mel_codec_44khz_fullband_medium](https://ngc.nvidia.com/catalog/models/nvidia:nemo:mel_codec_44khz_fullband_medium.md) | `https://api.ngc.nvidia.com/v2/models/nvidia/nemo/mel_codec_44khz_fullband_medium/versions/v1/files/mel_codec_44khz_fullband_medium.nemo` |
| nvidia/low-frame-rate-speech-codec-22khz | LibriVox and Common Voice | 22050Hz | nemo.collections.tts.models.AudioCodecModel | [audio_codec_low_frame_rate_22khz](https://huggingface.co/nvidia/low-frame-rate-speech-codec-22khz.md) | `https://huggingface.co/nvidia/low-frame-rate-speech-codec-22khz/resolve/main/low-frame-rate-speech-codec-22khz.nemo` |
| nvidia/audio-codec-22khz | LibriVox and Common Voice | 22050Hz | nemo.collections.tts.models.AudioCodecModel | [audio-codec-22khz](https://huggingface.co/nvidia/audio-codec-22khz.md) | `https://huggingface.co/nvidia/audio-codec-22khz/resolve/main/audio-codec-22khz.nemo` |
| nvidia/audio-codec-44khz | LibriVox and Common Voice | 44100Hz | nemo.collections.tts.models.AudioCodecModel | [audio-codec-44khz](https://huggingface.co/nvidia/audio-codec-44khz.md) | `https://huggingface.co/nvidia/audio-codec-44khz/resolve/main/audio-codec-44khz.nemo` |
| nvidia/mel-codec-22khz | LibriVox and Common Voice | 22050Hz | nemo.collections.tts.models.AudioCodecModel | [mel-codec-22khz](https://huggingface.co/nvidia/mel-codec-22khz.md) | `https://huggingface.co/nvidia/mel-codec-22khz/resolve/main/mel-codec-22khz.nemo` |
| nvidia/mel-codec-44khz | LibriVox and Common Voice | 44100Hz | nemo.collections.tts.models.AudioCodecModel | [mel-codec-44khz](https://huggingface.co/nvidia/mel-codec-44khz.md) | `https://huggingface.co/nvidia/mel-codec-44khz/resolve/main/mel-codec-44khz.nemo` |

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md#codec-models)
- [Checkpoints](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/checkpoints.html.md#ngc-tts-models)
- [NeMo Text to Speech collection](https://catalog.ngc.nvidia.com/orgs/nvidia/collections/nemo_tts.md)
- [tutorials/tts/](https://github.com/NVIDIA/NeMo/tree/stable/tutorials/tts.md)
- [NVIDIA/NeMo](https://github.com/NVIDIA/NeMo/tree/stable/tutorials/tts/FastPitch_Finetuning.ipynb.md)
- [NGC NeMo Text to Speech Collection](https://catalog.ngc.nvidia.com/orgs/nvidia/collections/nemo_tts/entities.md)
- [tts_en_radtts_aligner](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_radtts_aligner.md)
- [tts_en_fastpitch](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_fastpitch.md)
- [tts_en_multispeaker_fastpitchhifigan](https://ngc.nvidia.com/models/nvidia:nemo:tts_en_multispeaker_fastpitchhifigan.md)
- [tts_en_lj_mixertts](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_lj_mixertts.md)
- [tts_en_lj_mixerttsx](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_lj_mixerttsx.md)
- [tts_en_tacotron2](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_tacotron2.md)
- [tts_de_fastpitch_multispeaker_5](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_de_fastpitch_multispeaker_5.md)
- [tts_de_fastpitchhifigan](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_de_fastpitchhifigan.md)
- [tts_es_multispeaker_fastpitchhifigan](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/tts_es_multispeaker_fastpitchhifigan.md)
- [tts_zh_fastpitch_hifigan_sfspeech](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_zh_fastpitch_hifigan_sfspeech.md)
- [tts_en_hifigan](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_hifigan.md)
- [tts_en_lj_hifigan](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_lj_hifigan.md)
- [tts_en_lj_univnet](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_lj_univnet.md)
- [tts_en_libritts_univnet](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_libritts_univnet.md)
- [tts_en_waveglow_88m](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_waveglow_88m.md)
- [tts_en_lj_vits](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_lj_vits.md)
- [tts_en_hifitts_vits](https://ngc.nvidia.com/catalog/models/nvidia:nemo:tts_en_hifitts_vits.md)
- [audio_codec_16khz_small](https://ngc.nvidia.com/catalog/models/nvidia:nemo:audio_codec_16khz_small.md)
- [mel_codec_22khz_medium](https://ngc.nvidia.com/catalog/models/nvidia:nemo:mel_codec_22khz_medium.md)
- [mel_codec_44khz_medium](https://ngc.nvidia.com/catalog/models/nvidia:nemo:mel_codec_44khz_medium.md)
- [mel_codec_22khz_fullband_medium](https://ngc.nvidia.com/catalog/models/nvidia:nemo:mel_codec_22khz_fullband_medium.md)
- [mel_codec_44khz_fullband_medium](https://ngc.nvidia.com/catalog/models/nvidia:nemo:mel_codec_44khz_fullband_medium.md)
- [audio_codec_low_frame_rate_22khz](https://huggingface.co/nvidia/low-frame-rate-speech-codec-22khz.md)
- [audio-codec-22khz](https://huggingface.co/nvidia/audio-codec-22khz.md)
- [audio-codec-44khz](https://huggingface.co/nvidia/audio-codec-44khz.md)
- [mel-codec-22khz](https://huggingface.co/nvidia/mel-codec-22khz.md)
- [mel-codec-44khz](https://huggingface.co/nvidia/mel-codec-44khz.md)
