# Source: https://docs.vllm.ai/en/stable/examples/offline_inference/qwen2_5_omni/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/offline_inference/qwen2_5_omni.md "Edit this page")

# Qwen2.5-Omni Offline Inference Examples[¶](#qwen25-omni-offline-inference-examples "Permanent link") 

Source <https://github.com/vllm-project/vllm/tree/main/examples/offline_inference/qwen2_5_omni>.

This folder provides several example scripts on how to inference Qwen2.5-Omni offline.

## Thinker Only[¶](#thinker-only "Permanent link")

    # Audio + image + video
    python examples/offline_inference/qwen2_5_omni/only_thinker.py \
        -q mixed_modalities

    # Read vision and audio inputs from a single video file
    # NOTE: V1 engine does not support interleaved modalities yet.
    python examples/offline_inference/qwen2_5_omni/only_thinker.py \
        -q use_audio_in_video

    # Multiple audios
    python examples/offline_inference/qwen2_5_omni/only_thinker.py \
        -q multi_audios

This script will run the thinker part of Qwen2.5-Omni, and generate text response.

You can also test Qwen2.5-Omni on a single modality:

    # Process audio inputs
    python examples/offline_inference/audio_language.py \
        --model-type qwen2_5_omni

    # Process image inputs
    python examples/offline_inference/vision_language.py \
        --modality image \
        --model-type qwen2_5_omni

    # Process video inputs
    python examples/offline_inference/vision_language.py \
        --modality video \
        --model-type qwen2_5_omni

## Example materials[¶](#example-materials "Permanent link")

only_thinker.py

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    This example shows how to use vLLM for running offline inference
    with the correct prompt format on Qwen2.5-Omni (thinker only).
    """

    from typing import NamedTuple

    from vllm import LLM, SamplingParams
    from vllm.assets.audio import AudioAsset
    from vllm.assets.image import ImageAsset
    from vllm.assets.video import VideoAsset
    from vllm.multimodal.image import convert_image_mode
    from vllm.utils.argparse_utils import FlexibleArgumentParser

    class QueryResult(NamedTuple):
        inputs: dict
        limit_mm_per_prompt: dict[str, int]

    # NOTE: The default `max_num_seqs` and `max_model_len` may result in OOM on
    # lower-end GPUs.
    # Unless specified, these settings have been tested to work on a single L4.

    default_system = (
        "You are Qwen, a virtual human developed by the Qwen Team, Alibaba "
        "Group, capable of perceiving auditory and visual inputs, as well as "
        "generating text and speech."
    )

    def get_mixed_modalities_query() -> QueryResult:
        question = (
            "What is recited in the audio? "
            "What is the content of this image? Why is this video funny?"
        )
        prompt = (
            f"<|im_start|>system\n<|im_end|>\n"
            "<|im_start|>user\n<|audio_bos|><|AUDIO|><|audio_eos|>"
            "<|vision_bos|><|IMAGE|><|vision_eos|>"
            "<|vision_bos|><|VIDEO|><|vision_eos|>"
            f"<|im_end|>\n"
            f"<|im_start|>assistant\n"
        )
        return QueryResult(
            inputs=,
            },
            limit_mm_per_prompt=,
        )

    def get_use_audio_in_video_query() -> QueryResult:
        question = (
            "Describe the content of the video, then convert what the baby say into text."
        )
        prompt = (
            f"<|im_start|>system\n<|im_end|>\n"
            "<|im_start|>user\n<|vision_bos|><|VIDEO|><|vision_eos|>"
            f"<|im_end|>\n"
            f"<|im_start|>assistant\n"
        )
        asset = VideoAsset(name="baby_reading", num_frames=16)
        audio = asset.get_audio(sampling_rate=16000)

        return QueryResult(
            inputs=,
                "mm_processor_kwargs": ,
            },
            limit_mm_per_prompt=,
        )

    def get_multi_audios_query() -> QueryResult:
        question = "Are these two audio clips the same?"
        prompt = (
            f"<|im_start|>system\n<|im_end|>\n"
            "<|im_start|>user\n<|audio_bos|><|AUDIO|><|audio_eos|>"
            "<|audio_bos|><|AUDIO|><|audio_eos|>"
            f"<|im_end|>\n"
            f"<|im_start|>assistant\n"
        )
        return QueryResult(
            inputs=,
            },
            limit_mm_per_prompt=,
        )

    query_map = 

    def main(args):
        model_name = "Qwen/Qwen2.5-Omni-7B"
        query_result = query_map[args.query_type]()

        llm = LLM(
            model=model_name,
            max_model_len=5632,
            max_num_seqs=5,
            limit_mm_per_prompt=query_result.limit_mm_per_prompt,
            seed=args.seed,
        )

        # We set temperature to 0.2 so that outputs can be different
        # even when all prompts are identical when running batch inference.
        sampling_params = SamplingParams(temperature=0.2, max_tokens=64)

        outputs = llm.generate(query_result.inputs, sampling_params=sampling_params)

        for o in outputs:
            generated_text = o.outputs[0].text
            print(generated_text)

    def parse_args():
        parser = FlexibleArgumentParser(
            description="Demo on using vLLM for offline inference with "
            "audio language models"
        )
        parser.add_argument(
            "--query-type",
            "-q",
            type=str,
            default="mixed_modalities",
            choices=query_map.keys(),
            help="Query type.",
        )
        parser.add_argument(
            "--seed",
            type=int,
            default=0,
            help="Set the seed when initializing `vllm.LLM`.",
        )

        return parser.parse_args()

    if __name__ == "__main__":
        args = parse_args()
        main(args)