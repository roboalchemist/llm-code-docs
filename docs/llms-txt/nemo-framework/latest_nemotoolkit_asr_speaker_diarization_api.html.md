# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html.md

Title: NeMo Speaker Diarization API — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html

Published Time: Fri, 18 Jul 2025 19:25:08 GMT

Markdown Content:
NeMo Speaker Diarization API[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html.md#nemo-speaker-diarization-api "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Model Classes[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html.md#model-classes "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------

Mixins[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html.md#mixins "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

_class_ nemo.collections.asr.parts.mixins.DiarizationMixin[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html.md#nemo.collections.asr.parts.mixins.DiarizationMixin "Link to this definition")
Bases: `VerificationMixin`

_abstract_ diarize(_paths2audio\_files:List[str]_,_batch\_size:int=1_,)→List[str][#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html.md#nemo.collections.asr.parts.mixins.DiarizationMixin.diarize "Link to this definition")
Takes paths to audio files and returns speaker labels :param paths2audio_files: paths to audio fragment to be transcribed

Returns:
Speaker labels

_class_ nemo.collections.asr.parts.mixins.diarization.SpkDiarizationMixin[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html.md#nemo.collections.asr.parts.mixins.diarization.SpkDiarizationMixin "Link to this definition")
Bases: `ABC`

An abstract class for diarize-able models.

Creates a template function diarize() that provides an interface to perform transcription of audio tensors or filepaths.

The following abstract classes must be implemented by the subclass:

> *   _setup_diarize_dataloader():
> Setup the dataloader for diarization. Receives the output from _diarize_input_manifest_processing().
> 
> *   _diarize_forward():
> Implements the model’s custom forward pass to return outputs that are processed by _diarize_output_processing().
> 
> *   _diarize_output_processing():
> Implements the post processing of the model’s outputs to return the results to the user. The result can be a list of objects, list of list of objects, tuple of objects, tuple of list of objects, or a dict of list of objects.

_abstract_ _diarize_forward(_batch:Any_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html.md#nemo.collections.asr.parts.mixins.diarization.SpkDiarizationMixin._diarize_forward "Link to this definition")
Internal function to perform the model’s custom forward pass to return outputs that are processed by _diarize_output_processing(). This function is called by diarize() and diarize_generator() to perform the model’s forward pass.

Parameters:
**batch** – A batch of input data from the data loader that is used to perform the model’s forward pass.

Returns:
The model’s outputs that are processed by _diarize_output_processing().

_diarize_input_manifest_processing(_audio\_files:List[str]_,_temp\_dir:str_,_diarcfg:DiarizeConfig_,)→Dict[str,Any][#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html.md#nemo.collections.asr.parts.mixins.diarization.SpkDiarizationMixin._diarize_input_manifest_processing "Link to this definition")
Internal function to process the input audio filepaths and return a config dict for the dataloader.

Parameters:
*   **audio_files** – A list of string filepaths for audio files.

*   **temp_dir** – A temporary directory to store intermediate files.

*   **diarcfg** – The diarization config dataclass. Subclasses can change this to a different dataclass if needed.

Returns:
A config dict that is used to setup the dataloader for diarization.

_diarize_input_processing(_audio_,_diarcfg:DiarizeConfig_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html.md#nemo.collections.asr.parts.mixins.diarization.SpkDiarizationMixin._diarize_input_processing "Link to this definition")
Internal function to process the input audio data and return a DataLoader. This function is called by diarize() and diarize_generator() to setup the input data for diarization.

Parameters:
*   **audio** – Of type GenericDiarizationType

*   **diarcfg** – The diarization config dataclass. Subclasses can change this to a different dataclass if needed.

Returns:
A DataLoader object that is used to iterate over the input audio data.

_diarize_on_begin(_audio:str|List[str]_,_diarcfg:DiarizeConfig_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html.md#nemo.collections.asr.parts.mixins.diarization.SpkDiarizationMixin._diarize_on_begin "Link to this definition")
Internal function to setup the model for diarization. Perform all setup and pre-checks here.

Parameters:
*   **audio** (_Union_ _[_ _str_ _,_ _List_ _[_ _str_ _]_ _]_) – Of type GenericDiarizationType

*   **diarcfg** (_DiarizeConfig_) – An instance of DiarizeConfig.

_diarize_on_end(_diarcfg:DiarizeConfig_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html.md#nemo.collections.asr.parts.mixins.diarization.SpkDiarizationMixin._diarize_on_end "Link to this definition")
Internal function to teardown the model after transcription. Perform all teardown and post-checks here.

Parameters:
**diarcfg** – The diarization config dataclass. Subclasses can change this to a different dataclass if needed.

_abstract_ _diarize_output_processing(_outputs_,_uniq\_ids_,_diarcfg:DiarizeConfig_,)→List[Any]|List[List[Any]]|Tuple[Any]|Tuple[List[Any]][#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html.md#nemo.collections.asr.parts.mixins.diarization.SpkDiarizationMixin._diarize_output_processing "Link to this definition")
Internal function to process the model’s outputs to return the results to the user. This function is called by diarize() and diarize_generator() to process the model’s outputs.

Parameters:
*   **outputs** – The model’s outputs that are processed by _diarize_forward().

*   **uniq_ids** – List of unique recording identificators in batch

*   **diarcfg** – The diarization config dataclass. Subclasses can change this to a different dataclass if needed.

Returns:
The output can be a list of objects, list of list of objects, tuple of objects, tuple of list of objects. Its type is defined in GenericDiarizationType.

_input_audio_to_rttm_processing(_audio\_files:List[str]_,)→List[Dict[str,str|float]][#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html.md#nemo.collections.asr.parts.mixins.diarization.SpkDiarizationMixin._input_audio_to_rttm_processing "Link to this definition")
Generate manifest style dict if audio is a list of paths to audio files.

Parameters:
**audio_files** – A list of paths to audio files.

Returns:
audio_rttm_map_dict A list of manifest style dicts.

_abstract_ _setup_diarize_dataloader(_config:Dict_,)→torch.utils.data.DataLoader[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html.md#nemo.collections.asr.parts.mixins.diarization.SpkDiarizationMixin._setup_diarize_dataloader "Link to this definition")
Internal function to setup the dataloader for diarization. This function is called by diarize() and diarize_generator() to setup the input data for diarization.

Parameters:
**config** – A config dict that is used to setup the dataloader for diarization. It can be generated by _diarize_input_manifest_processing().

Returns:
A DataLoader object that is used to iterate over the input audio data.

diarize(_audio:str|List[str]|numpy.ndarray|torch.utils.data.DataLoader_,_batch\_size:int=1_,_include\_tensor\_outputs:bool=False_,_postprocessing\_yaml:str|None=None_,_num\_workers:int=1_,_verbose:bool=False_,_override\_config:DiarizeConfig|None=None_,_**config\_kwargs_,)→List[Any]|List[List[Any]]|Tuple[Any]|Tuple[List[Any]][#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html.md#nemo.collections.asr.parts.mixins.diarization.SpkDiarizationMixin.diarize "Link to this definition")
Takes paths to audio files and returns speaker labels

diarize_generator(_audio_,_override\_config:DiarizeConfig|None_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html.md#nemo.collections.asr.parts.mixins.diarization.SpkDiarizationMixin.diarize_generator "Link to this definition")
A generator version of diarize function.

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/speaker_diarization/api.html.md#nemo.collections.asr.parts.mixins.diarization.SpkDiarizationMixin.diarize_generator)
