# Source: https://docs.vllm.ai/en/stable/examples/offline_inference/encoder_decoder_multimodal/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/offline_inference/encoder_decoder_multimodal.md "Edit this page")

# Encoder Decoder Multimodal[¶](#encoder-decoder-multimodal "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/encoder_decoder_multimodal.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    This example shows how to use vLLM for running offline inference with
    the explicit/implicit prompt format on enc-dec LMMs for text generation.
    """

    import os
    import time
    from collections.abc import Sequence
    from dataclasses import asdict
    from typing import NamedTuple

    from vllm import LLM, EngineArgs, PromptType, SamplingParams
    from vllm.assets.audio import AudioAsset
    from vllm.utils.argparse_utils import FlexibleArgumentParser

    class ModelRequestData(NamedTuple):
        engine_args: EngineArgs
        prompts: Sequence[PromptType]

    def run_whisper():
        os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"

        engine_args = EngineArgs(
            model="openai/whisper-large-v3-turbo",
            max_model_len=448,
            max_num_seqs=16,
            limit_mm_per_prompt=,
            dtype="half",
        )

        prompts = [
            ,
            },
            ,
                },
                "decoder_prompt": "<|startoftranscript|>",
            },
        ]

        return ModelRequestData(
            engine_args=engine_args,
            prompts=prompts,
        )

    model_example_map = 

    def parse_args():
        parser = FlexibleArgumentParser(
            description="Demo on using vLLM for offline inference with "
            "vision language models for text generation"
        )
        parser.add_argument(
            "--model-type",
            "-m",
            type=str,
            default="whisper",
            choices=model_example_map.keys(),
            help='Huggingface "model_type".',
        )
        parser.add_argument(
            "--seed",
            type=int,
            default=0,
            help="Set the seed when initializing `vllm.LLM`.",
        )
        return parser.parse_args()

    def main(args):
        model = args.model_type
        if model not in model_example_map:
            raise ValueError(f"Model type  is not supported.")

        req_data = model_example_map[model]()

        # Disable other modalities to save memory
        default_limits = 
        req_data.engine_args.limit_mm_per_prompt = default_limits | dict(
            req_data.engine_args.limit_mm_per_prompt or 
        )

        engine_args = asdict(req_data.engine_args) | 
        llm = LLM(**engine_args)

        prompts = req_data.prompts

        # Create a sampling params object.
        sampling_params = SamplingParams(
            temperature=0,
            top_p=1.0,
            max_tokens=64,
            skip_special_tokens=False,
        )

        start = time.time()

        # Generate output tokens from the prompts. The output is a list of
        # RequestOutput objects that contain the prompt, generated
        # text, and other information.
        outputs = llm.generate(prompts, sampling_params)

        # Print the outputs.
        for output in outputs:
            prompt = output.prompt
            generated_text = output.outputs[0].text
            print(f"Decoder prompt: , Generated text: ")

        duration = time.time() - start

        print("Duration:", duration)
        print("RPS:", len(prompts) / duration)

    if __name__ == "__main__":
        args = parse_args()
        main(args)