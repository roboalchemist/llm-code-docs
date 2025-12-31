# Source: https://docs.vllm.ai/en/stable/contributing/model/transcription/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/contributing/model/transcription.md "Edit this page")

# Speech-to-Text (Transcription/Translation) Support[¶](#speech-to-text-transcriptiontranslation-support "Permanent link")

This document walks you through the steps to add support for speech-to-text (ASR) models to vLLM's transcription and translation APIs by implementing [SupportsTranscription](../../../api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription "            SupportsTranscription"). Please refer to the [supported models](../../../models/supported_models/#transcription) for further guidance.

## Update the base vLLM model[¶](#update-the-base-vllm-model "Permanent link")

It is assumed you have already implemented your model in vLLM according to the basic model guide. Extend your model with the [SupportsTranscription](../../../api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription "            SupportsTranscription") interface and implement the following class attributes and methods.

### `supported_languages` and `supports_transcription_only`[¶](#supported_languages-and-supports_transcription_only "Permanent link")

Declare supported languages and capabilities:

-   The `supported_languages` mapping is validated at init time.
-   Set `supports_transcription_only=True` if the model should not serve text generation (eg Whisper).

supported_languages and supports_transcription_only

    from typing import ClassVar, Mapping, Literal
    import numpy as np
    import torch
    from torch import nn

    from vllm.config import ModelConfig, SpeechToTextConfig
    from vllm.inputs.data import PromptType
    from vllm.model_executor.models.interfaces import SupportsTranscription

    class YourASRModel(nn.Module, SupportsTranscription):
        # Map of ISO 639-1 language codes to language names
        supported_languages: ClassVar[Mapping[str, str]] = 

        # If your model only supports audio-conditioned generation
        # (no text-only generation), enable this flag.
        supports_transcription_only: ClassVar[bool] = True

Provide an ASR configuration via [get_speech_to_text_config](../../../api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription.get_speech_to_text_config "            get_speech_to_text_config

  
      classmethod
  ").

This is for controlling general behavior of the API when serving your model:

get_speech_to_text_config()

    class YourASRModel(nn.Module, SupportsTranscription):
        ...

        @classmethod
        def get_speech_to_text_config(
            cls,
            model_config: ModelConfig,
            task_type: Literal["transcribe", "translate"],
        ) -> SpeechToTextConfig:
            return SpeechToTextConfig(
                sample_rate=16_000,
                max_audio_clip_s=30,
                # Set to None to disable server-side chunking if your
                # model/processor handles it already
                min_energy_split_window_size=None,
            )

See [Audio preprocessing and chunking](#audio-preprocessing-and-chunking) for what each field controls.

Implement the prompt construction via [get_generation_prompt](../../../api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription.get_generation_prompt "            get_generation_prompt

  
      classmethod
  "). The server passes you the resampled waveform and task parameters; you return a valid [PromptType](../../../api/vllm/inputs/data/#vllm.inputs.data.PromptType "            PromptType

  
      module-attribute
  "). There are two common patterns:

#### Multimodal LLM with audio embeddings (e.g., Voxtral, Gemma3n)[¶](#multimodal-llm-with-audio-embeddings-eg-voxtral-gemma3n "Permanent link") 

Return a dict containing `multi_modal_data` with the audio, and either a `prompt` string or `prompt_token_ids`:

get_generation_prompt()

    class YourASRModel(nn.Module, SupportsTranscription):
        ...

        @classmethod
        def get_generation_prompt(
            cls,
            audio: np.ndarray,
            stt_config: SpeechToTextConfig,
            model_config: ModelConfig,
            language: str | None,
            task_type: Literal["transcribe", "translate"],
            request_prompt: str,
            to_language: str | None,
        ) -> PromptType:
            # Example with a free-form instruction prompt
            task_word = "Transcribe" if task_type == "transcribe" else "Translate"
            prompt = (
                "<start_of_turn>user\n"
                f" this audio: <audio_soft_token>"
                "<end_of_turn>\n<start_of_turn>model\n"
            )

            return ,
                "prompt": prompt,
            }

For further clarification on multi modal inputs, please refer to [Multi-Modal Inputs](../../../features/multimodal_inputs/).

#### Encoder--decoder audio-only (e.g., Whisper)[¶](#encoderdecoder-audio-only-eg-whisper "Permanent link") 

Return a dict with separate `encoder_prompt` and `decoder_prompt` entries:

get_generation_prompt()

    class YourASRModel(nn.Module, SupportsTranscription):
        ...

        @classmethod
        def get_generation_prompt(
            cls,
            audio: np.ndarray,
            stt_config: SpeechToTextConfig,
            model_config: ModelConfig,
            language: str | None,
            task_type: Literal["transcribe", "translate"],
            request_prompt: str,
            to_language: str | None,
        ) -> PromptType:
            if language is None:
                raise ValueError("Language must be specified")

            prompt = ,
                },
                "decoder_prompt": (
                    (f"<|prev|>" if request_prompt else "")
                    + f"<|startoftranscript|><||>"
                    + f"<||><|notimestamps|>"
                ),
            }
            return cast(PromptType, prompt)

### `validate_language` (optional)[¶](#validate_language-optional "Permanent link")

Language validation via [validate_language](../../../api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription.validate_language "            validate_language

  
      classmethod
  ")

If your model requires a language and you want a default, override this method (see Whisper):

validate_language()

    @classmethod
    def validate_language(cls, language: str | None) -> str | None:
        if language is None:
            logger.warning(
                "Defaulting to language='en'. If you wish to transcribe "
                "audio in a different language, pass the `language` field "
                "in the TranscriptionRequest."
            )
            language = "en"
        return super().validate_language(language)

### `get_num_audio_tokens` (optional)[¶](#get_num_audio_tokens-optional "Permanent link")

Token accounting for streaming via [get_num_audio_tokens](../../../api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsTranscription.get_num_audio_tokens "            get_num_audio_tokens

  
      classmethod
  ")

Provide a fast duration→token estimate to improve streaming usage statistics:

get_num_audio_tokens()

    class YourASRModel(nn.Module, SupportsTranscription):
        ...

        @classmethod
        def get_num_audio_tokens(
            cls,
            audio_duration_s: float,
            stt_config: SpeechToTextConfig,
            model_config: ModelConfig,
        ) -> int | None:
            # Return None if unknown; otherwise return an estimate.
            return int(audio_duration_s * stt_config.sample_rate // 320)  # example

## Audio preprocessing and chunking[¶](#audio-preprocessing-and-chunking "Permanent link")

The API server takes care of basic audio I/O and optional chunking before building prompts:

-   Resampling: Input audio is resampled to `SpeechToTextConfig.sample_rate` using `librosa`.
-   Chunking: If `SpeechToTextConfig.allow_audio_chunking` is True and the duration exceeds `max_audio_clip_s`, the server splits the audio into overlapping chunks and generates a prompt per chunk. Overlap is controlled by `overlap_chunk_second`.
-   Energy-aware splitting: When `min_energy_split_window_size` is set, the server finds low-energy regions to minimize cutting within words.

Relevant server logic:

\_preprocess_speech_to_text()

    # vllm/entrypoints/openai/speech_to_text.py
    async def _preprocess_speech_to_text(...):
        language = self.model_cls.validate_language(request.language)
        ...
        y, sr = librosa.load(bytes_, sr=self.asr_config.sample_rate)
        duration = librosa.get_duration(y=y, sr=sr)
        do_split_audio = (self.asr_config.allow_audio_chunking
                        and duration > self.asr_config.max_audio_clip_s)
        chunks = [y] if not do_split_audio else self._split_audio(y, int(sr))
        prompts = []
        for chunk in chunks:
            prompt = self.model_cls.get_generation_prompt(
                audio=chunk,
                stt_config=self.asr_config,
                model_config=self.model_config,
                language=language,
                task_type=self.task_type,
                request_prompt=request.prompt,
                to_language=to_language,
            )
            prompts.append(prompt)
        return prompts, duration

## Exposing tasks automatically[¶](#exposing-tasks-automatically "Permanent link")

vLLM automatically advertises transcription support if your model implements the interface:

    if supports_transcription(model):
        if model.supports_transcription_only:
            return ["transcription"]
        supported_tasks.append("transcription")

When enabled, the server initializes the transcription and translation handlers:

    state.openai_serving_transcription = OpenAIServingTranscription(...) if "transcription" in supported_tasks else None
    state.openai_serving_translation = OpenAIServingTranslation(...) if "transcription" in supported_tasks else None

No extra registration is required beyond having your model class available via the model registry and implementing `SupportsTranscription`.

## Examples in-tree[¶](#examples-in-tree "Permanent link")

-   Whisper encoder--decoder (audio-only): [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] vllm/model_executor/models/whisper.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/whisper.py)
-   Voxtral decoder-only (audio embeddings + LLM): [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] vllm/model_executor/models/voxtral.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/voxtral.py). Make sure to have installed `mistral-common[audio]`.
-   Gemma3n decoder-only with fixed instruction prompt: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] vllm/model_executor/models/gemma3n_mm.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/gemma3n_mm.py)

## Test with the API[¶](#test-with-the-api "Permanent link")

Once your model implements `SupportsTranscription`, you can test the endpoints (API mimics OpenAI):

-   Transcription (ASR):

    ::: 
        curl -s -X POST \
          -H "Authorization: Bearer $VLLM_API_KEY" \
          -H "Content-Type: multipart/form-data" \
          -F "file=@/path/to/audio.wav" \
          -F "model=$MODEL_ID" \
          http://localhost:8000/v1/audio/transcriptions
    :::

-   Translation (source → English unless otherwise supported):

    ::: 
        curl -s -X POST \
          -H "Authorization: Bearer $VLLM_API_KEY" \
          -H "Content-Type: multipart/form-data" \
          -F "file=@/path/to/audio.wav" \
          -F "model=$MODEL_ID" \
          http://localhost:8000/v1/audio/translations
    :::

Or check out more examples in [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/online_serving](https://github.com/vllm-project/vllm/tree/main/examples/online_serving).

Note

-   If your model handles chunking internally (e.g., via its processor or encoder), set `min_energy_split_window_size=None` in the returned `SpeechToTextConfig` to disable server-side chunking.
-   Implementing `get_num_audio_tokens` improves accuracy of streaming usage metrics (`prompt_tokens`) without an extra forward pass.
-   For multilingual behavior, keep `supported_languages` aligned with actual model capabilities.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 7, 2025] ]