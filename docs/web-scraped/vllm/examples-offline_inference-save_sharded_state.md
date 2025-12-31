# Source: https://docs.vllm.ai/en/stable/examples/offline_inference/save_sharded_state/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/offline_inference/save_sharded_state.md "Edit this page")

# Save Sharded State[¶](#save-sharded-state "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/save_sharded_state.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """
    Saves each worker's model state dict directly to a checkpoint, which enables a
    fast load path for large tensor-parallel models where each worker only needs to
    read its own shard rather than the entire checkpoint.

    Example usage:

    python save_sharded_state.py \
        --model /path/to/load \
        --quantization deepspeedfp \
        --tensor-parallel-size 8 \
        --output /path/to/save

    Then, the model can be loaded with

    llm = LLM(
        model="/path/to/save",
        load_format="sharded_state",
        quantization="deepspeedfp",
        tensor_parallel_size=8,
    )
    """

    import dataclasses
    import os
    import shutil
    from pathlib import Path

    from vllm import LLM, EngineArgs
    from vllm.model_executor.model_loader import ShardedStateLoader
    from vllm.utils.argparse_utils import FlexibleArgumentParser

    def parse_args():
        parser = FlexibleArgumentParser()
        EngineArgs.add_cli_args(parser)
        parser.add_argument(
            "--output", "-o", required=True, type=str, help="path to output checkpoint"
        )
        parser.add_argument(
            "--file-pattern",
            type=str,
            default=ShardedStateLoader.DEFAULT_PATTERN,
            help="string pattern of saved filenames",
        )
        parser.add_argument(
            "--max-file-size",
            type=int,
            default=5 * 1024**3,
            help="max size (in bytes) of each safetensors file",
        )
        return parser.parse_args()

    def main(args):
        engine_args = EngineArgs.from_cli_args(args)
        if engine_args.enable_lora:
            raise ValueError("Saving with enable_lora=True is not supported!")
        model_path = engine_args.model
        if not Path(model_path).is_dir():
            raise ValueError("model path must be a local directory")
        # Create LLM instance from arguments
        llm = LLM(**dataclasses.asdict(engine_args))
        # Prepare output directory
        Path(args.output).mkdir(exist_ok=True)
        # Dump worker states to output directory

        llm.llm_engine.engine_core.save_sharded_state(
            path=args.output, pattern=args.file_pattern, max_size=args.max_file_size
        )

        # Copy metadata files to output directory
        for file in os.listdir(model_path):
            if os.path.splitext(file)[1] not in (".bin", ".pt", ".safetensors"):
                if os.path.isdir(os.path.join(model_path, file)):
                    shutil.copytree(
                        os.path.join(model_path, file), os.path.join(args.output, file)
                    )
                else:
                    shutil.copy(os.path.join(model_path, file), args.output)

    if __name__ == "__main__":
        args = parse_args()
        main(args)