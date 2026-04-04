# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_recognition/api.html.md

Title: NeMo Speaker Recognition API — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_recognition/api.html

Published Time: Fri, 18 Jul 2025 19:25:22 GMT

Markdown Content:
NeMo Speaker Recognition API[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_recognition/api.html.md#nemo-speaker-recognition-api "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Model Classes[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_recognition/api.html.md#model-classes "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ nemo.collections.asr.models.label_models.EncDecSpeakerLabelModel(_*args:Any_, _**kwargs:Any_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_recognition/api.html.md#nemo.collections.asr.models.label_models.EncDecSpeakerLabelModel "Link to this definition")
Bases: [`ModelPT`](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT "nemo.core.classes.modelPT.ModelPT"), `ExportableEncDecModel`, `VerificationMixin`

Encoder decoder class for speaker label models. Model class creates training, validation methods for setting up data performing model forward pass. Expects config dict for

> *   preprocessor
> 
> *   Jasper/Quartznet Encoder
> 
> *   Speaker Decoder

get_embedding(_path2audio\_file_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_recognition/api.html.md#nemo.collections.asr.models.label_models.EncDecSpeakerLabelModel.get_embedding "Link to this definition")
Returns the speaker embeddings for a provided audio file.

Parameters:
**path2audio_file** – path to an audio wav file

Returns:
speaker embeddings (Audio representations)

Return type:
emb

verify_speakers(_path2audio\_file1_,_path2audio\_file2_,_threshold=0.7_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_recognition/api.html.md#nemo.collections.asr.models.label_models.EncDecSpeakerLabelModel.verify_speakers "Link to this definition")
Verify if two audio files are from the same speaker or not.

Parameters:
*   **path2audio_file1** – path to audio wav file of speaker 1

*   **path2audio_file2** – path to audio wav file of speaker 2

*   **threshold** – cosine similarity score used as a threshold to distinguish two embeddings (default = 0.7)

Returns:
True if both audio files are from same speaker, False otherwise

verify_speakers_batch(_audio\_files\_pairs_,_threshold=0.7_,_batch\_size=32_,_sample\_rate=16000_,_device='cuda'_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_recognition/api.html.md#nemo.collections.asr.models.label_models.EncDecSpeakerLabelModel.verify_speakers_batch "Link to this definition")
Verify if audio files from the first and second manifests are from the same speaker or not.

Parameters:
*   **audio_files_pairs** – list of tuples with audio_files pairs to be verified

*   **threshold** – cosine similarity score used as a threshold to distinguish two embeddings (default = 0.7)

*   **batch_size** – batch size to perform batch inference

*   **sample_rate** – sample rate of audio files in manifest file

*   **device** – compute device to perform operations.

Returns:
True if both audio pair is from same speaker, False otherwise

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_recognition/api.html.md#nemo.collections.asr.models.label_models.EncDecSpeakerLabelModel.verify_speakers_batch)
- [ModelPT](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT)
