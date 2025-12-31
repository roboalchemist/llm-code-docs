# Source: https://docs.vllm.ai/en/stable/examples/offline_inference/kv_load_failure_recovery/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/offline_inference/kv_load_failure_recovery.md "Edit this page")

# KV Load Failure Recovery Test[¶](#kv-load-failure-recovery-test "Permanent link")

Source <https://github.com/vllm-project/vllm/tree/main/examples/offline_inference/kv_load_failure_recovery>.

This example builds upon the `disaggregated-prefill-v1` example in `examples/offline_inference`.

It demonstrates vLLM\'s ability to recover from KV load failures in both synchronous and asynchronous loading modes. The goal is to verify that vLLM correctly identifies invalid KV blocks, reschedules the affected requests, and ensures successful and consistent output.

## Files[¶](#files "Permanent link")

-   `prefill_example.py` -- performs the prefill stage and saves KV data (same as in `disaggregated-prefill-v1`).

-   `decode_example.py` -- performs the decode stage. Accepts:
    -   `--simulate-failure`: simulates KV load failure using a custom connector.
    -   `--async-load`: enables asynchronous KV loading mode.

-   `load_recovery_example_connector.py` -- defines `LoadRecoveryExampleConnector`, a subclass of `ExampleConnector`, that simulates missing or corrupted external KV blocks by failing to load blocks for the first decode request.

-   `run.sh` -- orchestrates the test: runs the prefill stage, then three decode stages:

    1.  Normal decode (baseline).
    2.  Decode with simulated sync KV load failure.
    3.  Decode with simulated async KV load failure.

    Finally, it compares the output of the baseline with the recovered outputs to verify correctness.

## How It Works[¶](#how-it-works "Permanent link")

-   The test dynamically loads `LoadRecoveryExampleConnector` via `KVTransferConfig.kv_connector_module_path`, enabling controlled simulation of load failures without modifying the original connector.
-   The decode stages that simulate failure are expected to trigger recovery logic in vLLM, resulting in the same output as the baseline decode.
-   If recovery fails, the script prints a unified diff of the output mismatch and exits with error.

## Usage[¶](#usage "Permanent link")

\`\`\`bash ./run.sh

## Example materials[¶](#example-materials "Permanent link")

decode_example.py

\`\`\`\`\`\`py

# SPDX-License-Identifier: Apache-2.0[¶](#spdx-license-identifier-apache-20 "Permanent link") 

# SPDX-FileCopyrightText: Copyright contributors to the vLLM project[¶](#spdx-filecopyrighttext-copyright-contributors-to-the-vllm-project "Permanent link")

import argparse

from vllm import LLM, SamplingParams from vllm.config import KVTransferConfig

def read_prompts(): \"\"\"Read prompts from prefill_output.txt\"\"\" prompts = \[\] try: with open(\"prefill_output.txt\") as f: for line in f: prompts.append(line.strip()) print(f\"Loaded  prompts from prefill_output.txt\") return prompts except FileNotFoundError: print(\"Error: prefill_output.txt file not found\") exit(-1)

def main(): prompts = read_prompts() sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=10)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--simulate-failure", action="store_true", help="Simulate KV load failure."
    )
    parser.add_argument(
        "--async-load", action="store_true", help="Simulate async KV load"
    )
    args = parser.parse_args()

    if args.simulate_failure:
        ktc = KVTransferConfig(
            kv_connector="LoadRecoveryExampleConnector",
            kv_role="kv_both",
            kv_connector_extra_config=,
            kv_connector_module_path="load_recovery_example_connector",
        )
        out_file = (
            "async_decode_recovered_output.txt"
            if args.async_load
            else "sync_decode_recovered_output.txt"
        )
    else:
        ktc = KVTransferConfig(
            kv_connector="ExampleConnector",
            kv_role="kv_both",
            kv_connector_extra_config=,
        )
        out_file = "decode_output.txt"

    llm = LLM(
        model="meta-llama/Llama-3.2-1B-Instruct",
        enforce_eager=True,
        gpu_memory_utilization=0.8,
        max_num_batched_tokens=64,
        max_num_seqs=16,
        kv_transfer_config=ktc,
    )

    outputs = llm.generate(prompts, sampling_params)

    sep_str = "-" * 30
    with open(out_file, "w", encoding="utf-8") as f:
        for output in outputs:
            prompt = output.prompt
            generated_text = output.outputs[0].text
            out_str = f"Prompt: \nGenerated text: "
            print(out_str)
            print(sep_str)
            f.write(out_str)
            f.write(sep_str)

if **name** == \"**main**\": main()

\`\`\`\`\`\`

load_recovery_example_connector.py

\`\`\`\`\`\`py

# SPDX-License-Identifier: Apache-2.0[¶](#spdx-license-identifier-apache-20_1 "Permanent link") 

# SPDX-FileCopyrightText: Copyright contributors to the vLLM project[¶](#spdx-filecopyrighttext-copyright-contributors-to-the-vllm-project_1 "Permanent link") 

# ruff: noqa: E501[¶](#ruff-noqa-e501 "Permanent link")

import logging from dataclasses import dataclass, field from typing import TYPE_CHECKING

from vllm.config import VllmConfig from vllm.distributed.kv_transfer.kv_connector.v1.base import ( KVConnectorMetadata, KVConnectorRole, ) from vllm.distributed.kv_transfer.kv_connector.v1.example_connector import ( ExampleConnector, ExampleConnectorMetadata, ) from vllm.forward_context import ForwardContext from vllm.v1.core.kv_cache_manager import KVCacheBlocks from vllm.v1.request import Request

if TYPE_CHECKING: from vllm.v1.core.sched.output import SchedulerOutput

logger = logging.getLogger() logging.basicConfig(level=logging.INFO)

\@dataclass class LoadRecoveryExampleConnectorMetadata(ExampleConnectorMetadata): req_to_block_ids: dict\[str, set\[int\]\] = field(default_factory=dict)

    @classmethod
    def from_base(cls, base: ExampleConnectorMetadata):
        return cls(requests=base.requests)

class LoadRecoveryExampleConnector(ExampleConnector): def **init**(self, vllm_config: \"VllmConfig\", role: KVConnectorRole): super().**init**(vllm_config=vllm_config, role=role) self.\_async_load = vllm_config.kv_transfer_config.get_from_extra_config( \"async_load\", False ) self.\_invalid_block_ids: set = None self.\_seen_requests: set = set() self.\_req_to_block_ids: dict\[str, list\[int\]\] = dict()

    def bind_connector_metadata(self, connector_metadata: KVConnectorMetadata) -> None:
        assert isinstance(connector_metadata, LoadRecoveryExampleConnectorMetadata)
        index, failed_request = next(
            (
                (i, x)
                for i, x in enumerate(connector_metadata.requests)
                if not x.is_store
            ),
            (None, None),
        )
        if index is not None:
            del connector_metadata.requests[index]
            self._invalid_block_ids = set(
                (
                    failed_request.slot_mapping[:: self._block_size] // self._block_size
                ).tolist()
            )
            logger.info(
                "Simulating failure to load all KV blocks for the "
                "first load request. Total blocks: %d",
                len(self._invalid_block_ids),
            )
        super().bind_connector_metadata(connector_metadata)

    def clear_connector_metadata(self) -> None:
        self._invalid_block_ids = None
        super().clear_connector_metadata()

    def start_load_kv(self, forward_context: ForwardContext, **kwargs) -> None:
        if self._async_load and forward_context.attn_metadata is None:
            # Bypass  sanity check in super().start_load_kv
            forward_context.attn_metadata = "None"

        super().start_load_kv(forward_context, **kwargs)

    def get_finished(
        self, finished_req_ids: set[str]
    ) -> tuple[set[str] | None, set[str] | None]:
        if self._async_load:
            meta = self._get_connector_metadata()
            assert isinstance(meta, LoadRecoveryExampleConnectorMetadata)
            if meta.req_to_block_ids:
                return None, set(meta.req_to_block_ids)

        return None, None

    def get_block_ids_with_load_errors(self) -> set[int]:
        return self._invalid_block_ids

    def get_num_new_matched_tokens(
        self,
        request: Request,
        num_computed_tokens: int,
    ) -> tuple[int, bool]:
        if request.request_id in self._seen_requests:
            return 0, False

        self._seen_requests.add(request.request_id)

        num_tokens, _ = super().get_num_new_matched_tokens(request, num_computed_tokens)
        return num_tokens, self._async_load and num_tokens > 0

    def update_state_after_alloc(
        self, request: Request, blocks: KVCacheBlocks, num_external_tokens: int
    ):
        """
        Update KVConnector state after block allocation.

        If blocks were allocated, add to _requests_need_load,
        such that we load the KVs in the next forward pass.
        """
        super().update_state_after_alloc(request, blocks, num_external_tokens)

        if num_external_tokens > 0:
            self._req_to_block_ids[request.request_id] = blocks.get_block_ids()[0]

    def build_connector_meta(
        self,
        scheduler_output: "SchedulerOutput",
    ) -> KVConnectorMetadata:
        if not self._async_load:
            base = super().build_connector_meta(scheduler_output)
            meta = LoadRecoveryExampleConnectorMetadata.from_base(base)
        else:
            meta = LoadRecoveryExampleConnectorMetadata()
            if self._requests_need_load:
                for req_id, request in self._requests_need_load.items():
                    meta.add_request(
                        token_ids=request.prompt_token_ids,
                        block_ids=self._req_to_block_ids[req_id],
                        block_size=self._block_size,
                        is_store=False,
                        mm_hashes=[],
                    )
                # Clear state
                self._requests_need_load.clear()
        meta.req_to_block_ids = self._req_to_block_ids
        self._req_to_block_ids = dict()
        return meta

\`\`\`\`\`\`

prefill_example.py

\`\`\`\`\`\`py

# SPDX-License-Identifier: Apache-2.0[¶](#spdx-license-identifier-apache-20_2 "Permanent link") 

# SPDX-FileCopyrightText: Copyright contributors to the vLLM project[¶](#spdx-filecopyrighttext-copyright-contributors-to-the-vllm-project_2 "Permanent link") 

from vllm import LLM, SamplingParams from vllm.config import KVTransferConfig

def read_prompts(): context = \"Hi \" \* 1000 context2 = \"Hey \" \* 500 return \[ context + \"Hello, my name is\", context + \"The capital of France is\", context2 + \"Your name is\", context2 + \"The capital of China is\", \]

def main(): prompts = read_prompts()

    sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=1)

    llm = LLM(
        model="meta-llama/Llama-3.2-1B-Instruct",
        enforce_eager=True,
        gpu_memory_utilization=0.8,
        kv_transfer_config=KVTransferConfig(
            kv_connector="ExampleConnector",
            kv_role="kv_both",
            kv_connector_extra_config=,
        ),
    )  # , max_model_len=2048, max_num_batched_tokens=2048)

    # 1ST generation (prefill instance)
    outputs = llm.generate(
        prompts,
        sampling_params,
    )

    new_prompts = []
    print("-" * 30)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        new_prompts.append(prompt + generated_text)
        print(f"Prompt: \nGenerated text: ")
        print("-" * 30)

    # Write new_prompts to prefill_output.txt
    with open("prefill_output.txt", "w") as f:
        for prompt in new_prompts:
            f.write(prompt + "\n")
    print(f"Saved  prompts to prefill_output.txt")

if **name** == \"**main**\": main()

\`\`\`\`\`\`

run.sh

\`\`\`\`\`\`sh

# !/bin/bash[¶](#binbash "Permanent link")

# Constants[¶](#constants "Permanent link")

SHARED_STORAGE_DIR=\"local_storage\" PREFILL_OUTPUT=\"prefill_output.txt\" DECODE_OUTPUT=\"decode_output.txt\" SYNC_DECODE_RECOVERED_OUTPUT=\"sync_decode_recovered_output.txt\" ASYNC_DECODE_RECOVERED_OUTPUT=\"async_decode_recovered_output.txt\"

# Cleanup[¶](#cleanup "Permanent link")

rm -rf \"[\\(SHARED_STORAGE_DIR\" rm -f \"\\)]PREFILL_OUTPUT\" \"[\\(DECODE_OUTPUT\" \"\\)]SYNC_DECODE_RECOVERED_OUTPUT\" \"\$ASYNC_DECODE_RECOVERED_OUTPUT\"

# Run inference examples[¶](#run-inference-examples "Permanent link")

VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=0 python3 prefill_example.py VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=0 python3 decode_example.py VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=0 python3 decode_example.py \--simulate-failure VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=0 python3 decode_example.py \--simulate-failure \--async-load

# Compare outputs[¶](#compare-outputs "Permanent link")

if ! cmp -s \"[\\(DECODE_OUTPUT\" \"\\)]SYNC_DECODE_RECOVERED_OUTPUT\"; then echo \"❌ Outputs differ: sync recovery failed.\" diff -u \"[\\(DECODE_OUTPUT\" \"\\)]SYNC_DECODE_RECOVERED_OUTPUT\" exit 1 fi

if ! cmp -s \"[\\(DECODE_OUTPUT\" \"\\)]ASYNC_DECODE_RECOVERED_OUTPUT\"; then echo \"❌ Outputs differ: async recovery failed.\" diff -u \"[\\(DECODE_OUTPUT\" \"\\)]ASYNC_DECODE_RECOVERED_OUTPUT\" exit 1 fi

echo \"✅ Outputs match: recovery successful.\"

\`\`\`\`\`\`