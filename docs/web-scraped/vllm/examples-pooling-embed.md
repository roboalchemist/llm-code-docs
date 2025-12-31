# Source: https://docs.vllm.ai/en/stable/examples/pooling/embed/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/pooling/embed.md "Edit this page")

# Embed[¶](#embed "Permanent link")

Source <https://github.com/vllm-project/vllm/tree/main/examples/pooling/embed>.

## Embed Jina Embeddings V3[¶](#embed-jina-embeddings-v3 "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    from argparse import Namespace

    from vllm import LLM, EngineArgs
    from vllm.utils.argparse_utils import FlexibleArgumentParser

    def parse_args():
        parser = FlexibleArgumentParser()
        parser = EngineArgs.add_cli_args(parser)
        # Set example specific arguments
        parser.set_defaults(
            model="jinaai/jina-embeddings-v3",
            runner="pooling",
            trust_remote_code=True,
        )
        return parser.parse_args()

    def main(args: Namespace):
        # Sample prompts.
        prompts = [
            "Follow the white rabbit.",  # English
            "Sigue al conejo blanco.",  # Spanish
            "Suis le lapin blanc.",  # French
            "跟着白兔走。",  # Chinese
            "اتبع الأرنب الأبيض.",  # Arabic
            "Folge dem weißen Kaninchen.",  # German
        ]

        # Create an LLM.
        # You should pass runner="pooling" for embedding models
        llm = LLM(**vars(args))

        # Generate embedding. The output is a list of EmbeddingRequestOutputs.
        # Only text matching task is supported for now. See #16120
        outputs = llm.embed(prompts)

        # Print the outputs.
        print("\nGenerated Outputs:")
        print("Only text matching task is supported for now. See #16120")
        print("-" * 60)
        for prompt, output in zip(prompts, outputs):
            embeds = output.outputs.embedding
            embeds_trimmed = (
                (str(embeds[:16])[:-1] + ", ...]") if len(embeds) > 16 else embeds
            )
            print(
                f"Prompt:  \n"
                f"Embeddings for text matching:  "
                f"(size=)"
            )
            print("-" * 60)

    if __name__ == "__main__":
        args = parse_args()
        main(args)

## Embed Matryoshka Fy[¶](#embed-matryoshka-fy "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    from argparse import Namespace

    from vllm import LLM, EngineArgs, PoolingParams
    from vllm.utils.argparse_utils import FlexibleArgumentParser

    def parse_args():
        parser = FlexibleArgumentParser()
        parser = EngineArgs.add_cli_args(parser)
        # Set example specific arguments
        parser.set_defaults(
            model="jinaai/jina-embeddings-v3",
            runner="pooling",
            trust_remote_code=True,
        )
        return parser.parse_args()

    def main(args: Namespace):
        # Sample prompts.
        prompts = [
            "Follow the white rabbit.",  # English
            "Sigue al conejo blanco.",  # Spanish
            "Suis le lapin blanc.",  # French
            "跟着白兔走。",  # Chinese
            "اتبع الأرنب الأبيض.",  # Arabic
            "Folge dem weißen Kaninchen.",  # German
        ]

        # Create an LLM.
        # You should pass runner="pooling" for embedding models
        llm = LLM(**vars(args))

        # Generate embedding. The output is a list of EmbeddingRequestOutputs.
        outputs = llm.embed(prompts, pooling_params=PoolingParams(dimensions=32))

        # Print the outputs.
        print("\nGenerated Outputs:")
        print("-" * 60)
        for prompt, output in zip(prompts, outputs):
            embeds = output.outputs.embedding
            embeds_trimmed = (
                (str(embeds[:16])[:-1] + ", ...]") if len(embeds) > 16 else embeds
            )
            print(f"Prompt:  \nEmbeddings:  (size=)")
            print("-" * 60)

    if __name__ == "__main__":
        args = parse_args()
        main(args)

## Embedding Requests Base64 Client[¶](#embedding-requests-base64-client "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """Example Python client for embedding API using vLLM API server
    NOTE:
        start a supported embeddings model server with `vllm serve`, e.g.
        vllm serve intfloat/e5-small
    """

    import argparse
    import base64

    import requests
    import torch

    from vllm.utils.serial_utils import (
        EMBED_DTYPE_TO_TORCH_DTYPE,
        ENDIANNESS,
        binary2tensor,
    )

    def post_http_request(prompt: dict, api_url: str) -> requests.Response:
        headers = 
        response = requests.post(api_url, headers=headers, json=prompt)
        return response

    def parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("--host", type=str, default="localhost")
        parser.add_argument("--port", type=int, default=8000)
        parser.add_argument("--model", type=str, default="intfloat/e5-small")

        return parser.parse_args()

    def main(args):
        api_url = f"http://:/v1/embeddings"
        model_name = args.model

        # The OpenAI client does not support the embed_dtype and endianness parameters.
        for embed_dtype in EMBED_DTYPE_TO_TORCH_DTYPE:
            for endianness in ENDIANNESS:
                prompt = 
                response = post_http_request(prompt=prompt, api_url=api_url)

                embedding = []
                for data in response.json()["data"]:
                    binary = base64.b64decode(data["embedding"])
                    tensor = binary2tensor(binary, (-1,), embed_dtype, endianness)
                    embedding.append(tensor.to(torch.float32))
                embedding = torch.cat(embedding)
                print(embed_dtype, endianness, embedding.shape)

    if __name__ == "__main__":
        args = parse_args()
        main(args)

## Embedding Requests Bytes Client[¶](#embedding-requests-bytes-client "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """Example Python client for embedding API using vLLM API server
    NOTE:
        start a supported embeddings model server with `vllm serve`, e.g.
        vllm serve intfloat/e5-small
    """

    import argparse
    import json

    import requests
    import torch

    from vllm.utils.serial_utils import (
        EMBED_DTYPE_TO_TORCH_DTYPE,
        ENDIANNESS,
        MetadataItem,
        build_metadata_items,
        decode_pooling_output,
    )

    def post_http_request(prompt: dict, api_url: str) -> requests.Response:
        headers = 
        response = requests.post(api_url, headers=headers, json=prompt)
        return response

    def parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("--host", type=str, default="localhost")
        parser.add_argument("--port", type=int, default=8000)
        parser.add_argument("--model", type=str, default="intfloat/e5-small")

        return parser.parse_args()

    def main(args):
        api_url = f"http://:/v1/embeddings"
        model_name = args.model
        embedding_size = 0

        input_texts = [
            "The best thing about vLLM is that it supports many different models",
        ] * 2

        # The OpenAI client does not support the bytes encoding_format.
        # The OpenAI client does not support the embed_dtype and endianness parameters.
        for embed_dtype in EMBED_DTYPE_TO_TORCH_DTYPE:
            for endianness in ENDIANNESS:
                prompt = 
                response = post_http_request(prompt=prompt, api_url=api_url)
                metadata = json.loads(response.headers["metadata"])
                body = response.content
                items = [MetadataItem(**x) for x in metadata["data"]]

                embedding = decode_pooling_output(items=items, body=body)
                embedding = [x.to(torch.float32) for x in embedding]
                embedding = torch.stack(embedding)
                embedding_size = embedding.shape[-1]
                print(embed_dtype, endianness, embedding.shape)

        # The vllm server always sorts the returned embeddings in the order of input. So
        # returning metadata is not necessary. You can set encoding_format to bytes_only
        # to let the server not return metadata.
        for embed_dtype in EMBED_DTYPE_TO_TORCH_DTYPE:
            for endianness in ENDIANNESS:
                prompt = 
                response = post_http_request(prompt=prompt, api_url=api_url)
                body = response.content

                items = build_metadata_items(
                    embed_dtype=embed_dtype,
                    endianness=endianness,
                    shape=(embedding_size,),
                    n_request=len(input_texts),
                )
                embedding = decode_pooling_output(items=items, body=body)
                embedding = [x.to(torch.float32) for x in embedding]
                embedding = torch.stack(embedding)
                print(embed_dtype, endianness, embedding.shape)

    if __name__ == "__main__":
        args = parse_args()
        main(args)

## OpenAI Chat Embedding Client For Multimodal[¶](#openai-chat-embedding-client-for-multimodal "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    # ruff: noqa: E501
    """Example Python client for multimodal embedding API using vLLM API server.

    Refer to each `run_*` function for the command to run the server for that model.
    """

    import argparse
    import base64
    import io
    from typing import Literal

    from openai import OpenAI
    from openai._types import NOT_GIVEN, NotGiven
    from openai.types.chat import ChatCompletionMessageParam
    from openai.types.create_embedding_response import CreateEmbeddingResponse
    from PIL import Image

    # Modify OpenAI's API key and API base to use vLLM's API server.
    openai_api_key = "EMPTY"
    openai_api_base = "http://localhost:8000/v1"

    image_url = "https://vllm-public-assets.s3.us-west-2.amazonaws.com/vision_model_images/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"

    def create_chat_embeddings(
        client: OpenAI,
        *,
        messages: list[ChatCompletionMessageParam],
        model: str,
        encoding_format: Literal["base64", "float"] | NotGiven = NOT_GIVEN,
    ) -> CreateEmbeddingResponse:
        """
        Convenience function for accessing vLLM's Chat Embeddings API,
        which is an extension of OpenAI's existing Embeddings API.
        """
        return client.post(
            "/embeddings",
            cast_to=CreateEmbeddingResponse,
            body=,
        )

    def run_clip(client: OpenAI, model: str):
        """
        Start the server using:

        vllm serve openai/clip-vit-base-patch32 \
            --runner pooling
        """

        response = create_chat_embeddings(
            client,
            messages=[
                },
                    ],
                }
            ],
            model=model,
            encoding_format="float",
        )

        print("Image embedding output:", response.data[0].embedding)

        response = create_chat_embeddings(
            client,
            messages=[
                ,
                    ],
                }
            ],
            model=model,
            encoding_format="float",
        )

        print("Text embedding output:", response.data[0].embedding)

    def run_dse_qwen2_vl(client: OpenAI, model: str):
        """
        Start the server using:

        vllm serve MrLight/dse-qwen2-2b-mrl-v1 \
            --runner pooling \
            --trust-remote-code \
            --max-model-len 8192 \
            --chat-template examples/template_dse_qwen2_vl.jinja
        """
        response = create_chat_embeddings(
            client,
            messages=[
                ,
                        },
                        ,
                    ],
                }
            ],
            model=model,
            encoding_format="float",
        )

        print("Image embedding output:", response.data[0].embedding)

        # MrLight/dse-qwen2-2b-mrl-v1 requires a placeholder image
        # of the minimum input size
        buffer = io.BytesIO()
        image_placeholder = Image.new("RGB", (56, 56))
        image_placeholder.save(buffer, "png")
        buffer.seek(0)
        image_placeholder = base64.b64encode(buffer.read()).decode("utf-8")
        response = create_chat_embeddings(
            client,
            messages=[
                ",
                            },
                        },
                        ,
                    ],
                }
            ],
            model=model,
            encoding_format="float",
        )

        print("Text embedding output:", response.data[0].embedding)

    def run_siglip(client: OpenAI, model: str):
        """
        Start the server using:

        vllm serve google/siglip-base-patch16-224 \
            --runner pooling \
            --chat-template template_basic.jinja
        """

        response = create_chat_embeddings(
            client,
            messages=[
                },
                    ],
                }
            ],
            model=model,
            encoding_format="float",
        )

        print("Image embedding output:", response.data[0].embedding)

        response = create_chat_embeddings(
            client,
            messages=[
                ,
                    ],
                }
            ],
            model=model,
            encoding_format="float",
        )

        print("Text embedding output:", response.data[0].embedding)

    def run_vlm2vec(client: OpenAI, model: str):
        """
        Start the server using:

        vllm serve TIGER-Lab/VLM2Vec-Full \
            --runner pooling \
            --trust-remote-code \
            --max-model-len 4096 \
            --chat-template examples/template_vlm2vec_phi3v.jinja
        """

        response = create_chat_embeddings(
            client,
            messages=[
                },
                        ,
                    ],
                }
            ],
            model=model,
            encoding_format="float",
        )

        print("Image embedding output:", response.data[0].embedding)

        response = create_chat_embeddings(
            client,
            messages=[
                },
                        ,
                    ],
                }
            ],
            model=model,
            encoding_format="float",
        )

        print("Image+Text embedding output:", response.data[0].embedding)

        response = create_chat_embeddings(
            client,
            messages=[
                ,
                    ],
                }
            ],
            model=model,
            encoding_format="float",
        )

        print("Text embedding output:", response.data[0].embedding)

    model_example_map = 

    def parse_args():
        parser = argparse.ArgumentParser(
            "Script to call a specified VLM through the API. Make sure to serve "
            "the model with `--runner pooling` before running this."
        )
        parser.add_argument(
            "--model",
            type=str,
            choices=model_example_map.keys(),
            required=True,
            help="The name of the embedding model.",
        )
        return parser.parse_args()

    def main(args):
        client = OpenAI(
            # defaults to os.environ.get("OPENAI_API_KEY")
            api_key=openai_api_key,
            base_url=openai_api_base,
        )

        models = client.models.list()
        model_id = models.data[0].id

        model_example_map[args.model](client, model_id)

    if __name__ == "__main__":
        args = parse_args()
        main(args)

## OpenAI Embedding Client[¶](#openai-embedding-client "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """Example Python client for embedding API using vLLM API server
    NOTE:
        start a supported embeddings model server with `vllm serve`, e.g.
        vllm serve intfloat/e5-small
    """

    from openai import OpenAI

    # Modify OpenAI's API key and API base to use vLLM's API server.
    openai_api_key = "EMPTY"
    openai_api_base = "http://localhost:8000/v1"

    def main():
        client = OpenAI(
            # defaults to os.environ.get("OPENAI_API_KEY")
            api_key=openai_api_key,
            base_url=openai_api_base,
        )

        models = client.models.list()
        model = models.data[0].id

        responses = client.embeddings.create(
            # ruff: noqa: E501
            input=[
                "Hello my name is",
                "The best thing about vLLM is that it supports many different models",
            ],
            model=model,
        )

        for data in responses.data:
            print(data.embedding)  # List of float of len 4096

    if __name__ == "__main__":
        main()

## OpenAI Embedding Long Text - Readme[¶](#openai-embedding-long-text-readme "Permanent link") 

    # Long Text Embedding with Chunked Processing

    This directory contains examples for using vLLM's **chunked processing** feature to handle long text embedding that exceeds the model's maximum context length.

    ## 🚀 Quick Start

    ### Start the Server

    Use the provided script to start a vLLM server with chunked processing enabled:

    ```bash
    # Basic usage (supports very long texts up to ~3M tokens)
    ./service.sh

    # Custom configuration with different models
    MODEL_NAME="jinaai/jina-embeddings-v3" \
    MAX_EMBED_LEN=1048576 \
    ./service.sh

    # For extremely long documents
    MODEL_NAME="intfloat/multilingual-e5-large" \
    MAX_EMBED_LEN=3072000 \
    ./service.sh
    ```

    ### Test Long Text Embedding

    Run the comprehensive test client:

    ```bash
    python client.py
    ```

    ## 📁 Files

    | File | Description |
    |------|-------------|
    | `service.sh` | Server startup script with chunked processing enabled |
    | `client.py` | Comprehensive test client for long text embedding |

    ## ⚙️ Configuration

    ### Server Configuration

    The key parameters for chunked processing are in the `--pooler-config`:

    ```json
    
    ```

    !!! note
        `pooling_type` sets the model's own pooling strategy for processing within each chunk. The cross-chunk aggregation automatically uses MEAN strategy when input exceeds the model's native maximum length.

    #### Chunked Processing Behavior

    Chunked processing uses **MEAN aggregation** for cross-chunk combination when input exceeds the model's native maximum length:

    | Component | Behavior | Description |
    |-----------|----------|-------------|
    | **Within chunks** | Model's native pooling | Uses the model's configured pooling strategy |
    | **Cross-chunk aggregation** | Always MEAN | Weighted averaging based on chunk token counts |
    | **Performance** | Optimal | All chunks processed for complete semantic coverage |

    ### Environment Variables

    | Variable | Default | Description |
    |----------|---------|-------------|
    | `MODEL_NAME` | `intfloat/multilingual-e5-large` | Embedding model to use (supports multiple models) |
    | `PORT` | `31090` | Server port |
    | `GPU_COUNT` | `1` | Number of GPUs to use |
    | `MAX_EMBED_LEN` | `3072000` | Maximum embedding input length (supports very long documents) |
    | `POOLING_TYPE` | `auto` | Model's native pooling type: `auto`, `MEAN`, `CLS`, `LAST` (only affects within-chunk pooling, not cross-chunk aggregation) |
    | `API_KEY` | `EMPTY` | API key for authentication |

    ## 🔧 How It Works

    1. **Enhanced Input Validation**: `max_embed_len` allows accepting inputs longer than `max_model_len` without environment variables
    2. **Smart Chunking**: Text is split based on `max_position_embeddings` to maintain semantic integrity
    3. **Unified Processing**: All chunks processed separately through the model using its configured pooling strategy
    4. **MEAN Aggregation**: When input exceeds model's native length, results combined using token count-based weighted averaging across all chunks
    5. **Consistent Output**: Final embeddings maintain the same dimensionality as standard processing

    ### Input Length Handling

    - **Within max_embed_len**: Input is accepted and processed (up to 3M+ tokens)
    - **Exceeds max_position_embeddings**: Chunked processing is automatically triggered
    - **Exceeds max_embed_len**: Input is rejected with clear error message
    - **No environment variables required**: Works without `VLLM_ALLOW_LONG_MAX_MODEL_LEN`

    ### Extreme Long Text Support

    With `MAX_EMBED_LEN=3072000`, you can process:

    - **Academic papers**: Full research papers with references
    - **Legal documents**: Complete contracts and legal texts  
    - **Books**: Entire chapters or small books
    - **Code repositories**: Large codebases and documentation

    ## 📊 Performance Characteristics

    ### Chunked Processing Performance

    | Aspect | Behavior | Performance |
    |--------|----------|-------------|
    | **Chunk Processing** | All chunks processed with native pooling | Consistent with input length |
    | **Cross-chunk Aggregation** | MEAN weighted averaging | Minimal overhead |
    | **Memory Usage** | Proportional to number of chunks | Moderate, scalable |
    | **Semantic Quality** | Complete text coverage | Optimal for long documents |

    ## 🧪 Test Cases

    The test client demonstrates:

    - ✅ **Short text**: Normal processing (baseline)
    - ✅ **Medium text**: Single chunk processing
    - ✅ **Long text**: Multi-chunk processing with aggregation
    - ✅ **Very long text**: Many chunks processing
    - ✅ **Extreme long text**: Document-level processing (100K+ tokens)
    - ✅ **Batch processing**: Mixed-length inputs in one request
    - ✅ **Consistency**: Reproducible results across runs

    ## 🐛 Troubleshooting

    ### Common Issues

    1. **Chunked processing not enabled**:

       ```log
       ValueError: This model's maximum position embeddings length is 4096 tokens...
       ```

       **Solution**: Ensure `enable_chunked_processing: true` in pooler config

    2. **Input exceeds max_embed_len**:

       ```log
       ValueError: This model's maximum embedding input length is 3072000 tokens...
       ```

       **Solution**: Increase `max_embed_len` in pooler config or reduce input length

    3. **Memory errors**:

       ```log
       RuntimeError: CUDA out of memory
       ```

       **Solution**: Reduce chunk size by adjusting model's `max_position_embeddings` or use fewer GPUs

    4. **Slow processing**:
       **Expected**: Long text takes more time due to multiple inference calls

    ### Debug Information

    Server logs show chunked processing activity:

    ```log
    INFO: Input length 150000 exceeds max_position_embeddings 4096, will use chunked processing
    INFO: Split input of 150000 tokens into 37 chunks (max_chunk_size: 4096)
    ```

    ## 🤝 Contributing

    To extend chunked processing support to other embedding models:

    1. Check model compatibility with the pooling architecture
    2. Test with various text lengths
    3. Validate embedding quality compared to single-chunk processing
    4. Submit PR with test cases and documentation updates

    ## 🆕 Enhanced Features

    ### max_embed_len Parameter

    The new `max_embed_len` parameter provides:

    - **Simplified Configuration**: No need for `VLLM_ALLOW_LONG_MAX_MODEL_LEN` environment variable
    - **Flexible Input Validation**: Accept inputs longer than `max_model_len` up to `max_embed_len`
    - **Extreme Length Support**: Process documents with millions of tokens
    - **Clear Error Messages**: Better feedback when inputs exceed limits
    - **Backward Compatibility**: Existing configurations continue to work

## OpenAI Embedding Long Text - Client[¶](#openai-embedding-long-text-client "Permanent link") 

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    """
    Example script demonstrating long text embedding with chunked processing in vLLM.

    This example shows how to use vLLM's chunked processing feature to handle text
    inputs that exceed the model's maximum token length. The feature automatically
    splits long text into chunks and handles different pooling types optimally.

    Prerequisites:
    1. Start vLLM server with chunked processing enabled:

       # MEAN pooling (processes all chunks, recommended for complete coverage)
       vllm serve intfloat/multilingual-e5-large \
         --pooler-config \
          '' \
         --served-model-name multilingual-e5-large \
         --trust-remote-code \
         --port 31090 \
         --api-key your-api-key

       # OR CLS pooling (native CLS within chunks, MEAN aggregation across chunks)
       vllm serve BAAI/bge-large-en-v1.5 \
         --pooler-config \
          '' \
         --served-model-name bge-large-en-v1.5 \
         --trust-remote-code \
         --port 31090 \
         --api-key your-api-key

    2. Install required dependencies:
       pip install openai requests
    """

    import time

    import numpy as np
    from openai import OpenAI

    # Configuration
    API_KEY = "your-api-key"  # Replace with your actual API key
    BASE_URL = "http://localhost:31090/v1"
    MODEL_NAME = "multilingual-e5-large"

    def generate_long_text(base_text: str, repeat_count: int) -> str:
        """Generate long text by repeating base text."""
        return base_text * repeat_count

    def test_embedding_with_different_lengths():
        """Test embedding generation with different text lengths."""
        client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

        # Test cases with different text lengths
        test_cases = [
            ,
            ,
            ,
            ,
        ]

        print("🧪 Testing vLLM Long Text Embedding with Chunked Processing")
        print("=" * 70)

        for i, test_case in enumerate(test_cases, 1):
            print(f"\n📝 Test : ")
            print(f"Text length:  characters")

            try:
                start_time = time.time()

                response = client.embeddings.create(
                    input=test_case["text"], model=MODEL_NAME, encoding_format="float"
                )

                end_time = time.time()
                processing_time = end_time - start_time

                # Extract embedding data
                embedding = response.data[0].embedding
                embedding_dim = len(embedding)

                print("✅ Success!")
                print(f"   - Embedding dimension: ")
                print(f"   - Processing time: s")
                print(f"   - Expected chunks: ~")
                print(f"   - First 5 values: ")

            except Exception as e:
                print(f"❌ Failed: ")

    def test_batch_embedding():
        """Test batch embedding with mixed-length inputs."""
        client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

        print("\n🔄 Testing Batch Embedding with Mixed Lengths")
        print("=" * 50)

        # Mix of short and long texts
        batch_inputs = [
            "Short text 1",
            generate_long_text("Medium length text that fits in one chunk. " * 20, 1),
            "Another short text",
            generate_long_text("Long text requiring chunked processing. " * 100, 5),
        ]

        try:
            start_time = time.time()

            response = client.embeddings.create(
                input=batch_inputs, model=MODEL_NAME, encoding_format="float"
            )

            end_time = time.time()
            processing_time = end_time - start_time

            print("✅ Batch processing successful!")
            print(f"   - Number of inputs: ")
            print(f"   - Number of embeddings: ")
            print(f"   - Total processing time: s")
            print(
                f"   - Average time per input: s"
            )

            for i, data in enumerate(response.data):
                input_length = len(batch_inputs[i])
                embedding_dim = len(data.embedding)
                print(
                    f"   - Input :  chars → D embedding"
                )

        except Exception as e:
            print(f"❌ Batch processing failed: ")

    def test_multiple_long_texts_batch():
        """Test batch processing with multiple long texts to verify chunk ID uniqueness."""
        client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

        print("\n🔧 Testing Multiple Long Texts in Batch (Chunk ID Fix Verification)")
        print("=" * 70)

        # Create multiple distinct long texts that will all require chunking
        # Note: All pooling types now use MEAN aggregation across chunks:
        # - Native pooling (MEAN/CLS/LAST) is used within each chunk
        # - MEAN aggregation combines results across all chunks
        # - Full semantic coverage for all pooling types
        long_texts = [
            generate_long_text(
                "First long document about artificial intelligence and machine learning. "
                * 80,
                6,
            ),
            generate_long_text(
                "Second long document about natural language processing and transformers. "
                * 80,
                6,
            ),
            generate_long_text(
                "Third long document about computer vision and neural networks. " * 80, 6
            ),
        ]

        # Add some short texts to mix things up
        batch_inputs = [
            "Short text before long texts",
            long_texts[0],
            "Short text between long texts",
            long_texts[1],
            long_texts[2],
            "Short text after long texts",
        ]

        print("📊 Batch composition:")
        for i, text in enumerate(batch_inputs):
            length = len(text)
            text_type = "Long (will be chunked)" if length > 5000 else "Short"
            print(f"   - Input :  chars ()")

        try:
            start_time = time.time()

            response = client.embeddings.create(
                input=batch_inputs, model=MODEL_NAME, encoding_format="float"
            )

            end_time = time.time()
            processing_time = end_time - start_time

            print("\n✅ Multiple long texts batch processing successful!")
            print(f"   - Number of inputs: ")
            print(f"   - Number of embeddings returned: ")
            print(f"   - Total processing time: s")

            # Verify each embedding is different (no incorrect aggregation)
            embeddings = [data.embedding for data in response.data]

            if len(embeddings) >= 3:
                import numpy as np

                # Compare embeddings of the long texts (indices 1, 3, 4)
                long_embeddings = [
                    np.array(embeddings[1]),  # First long text
                    np.array(embeddings[3]),  # Second long text
                    np.array(embeddings[4]),  # Third long text
                ]

                print("\n🔍 Verifying embedding uniqueness:")
                for i in range(len(long_embeddings)):
                    for j in range(i + 1, len(long_embeddings)):
                        cosine_sim = np.dot(long_embeddings[i], long_embeddings[j]) / (
                            np.linalg.norm(long_embeddings[i])
                            * np.linalg.norm(long_embeddings[j])
                        )
                        print(
                            f"   - Similarity between long text  and : "
                            f""
                        )

                        if (
                            cosine_sim < 0.9
                        ):  # Different content should have lower similarity
                            print("     ✅ Good: Embeddings are appropriately different")
                        else:
                            print(
                                "     ⚠️ High similarity - may indicate chunk "
                                "aggregation issue"
                            )

            print("\n📋 Per-input results:")
            for i, data in enumerate(response.data):
                input_length = len(batch_inputs[i])
                embedding_dim = len(data.embedding)
                embedding_norm = np.linalg.norm(data.embedding)
                print(
                    f"   - Input :  chars → D "
                    f"embedding (norm: )"
                )

            print(
                "\n✅ This test verifies the fix for chunk ID collisions in "
                "batch processing"
            )
            print("   - Before fix: Multiple long texts would have conflicting chunk IDs")
            print("   - After fix: Each prompt's chunks have unique IDs with prompt index")

        except Exception as e:
            print(f"❌ Multiple long texts batch test failed: ")
            print("   This might indicate the chunk ID collision bug is present!")

    def test_embedding_consistency():
        """Test that chunked processing produces consistent results."""
        client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

        print("\n🔍 Testing Embedding Consistency")
        print("=" * 40)

        # Use the same long text multiple times
        long_text = generate_long_text(
            "Consistency test text for chunked processing validation. " * 50, 3
        )

        embeddings = []

        try:
            for i in range(3):
                response = client.embeddings.create(
                    input=long_text, model=MODEL_NAME, encoding_format="float"
                )
                embeddings.append(response.data[0].embedding)
                print(f"   - Generated embedding ")

            # Check consistency (embeddings should be identical)
            if len(embeddings) >= 2:
                # Calculate similarity between first two embeddings

                emb1 = np.array(embeddings[0])
                emb2 = np.array(embeddings[1])

                # Cosine similarity
                cosine_sim = np.dot(emb1, emb2) / (
                    np.linalg.norm(emb1) * np.linalg.norm(emb2)
                )

                print("✅ Consistency test completed!")
                print(f"   - Cosine similarity between runs: ")
                print("   - Expected: ~1.0 (identical embeddings)")

                if cosine_sim > 0.999:
                    print("   - ✅ High consistency achieved!")
                else:
                    print("   - ⚠️ Consistency may vary due to numerical precision")

        except Exception as e:
            print(f"❌ Consistency test failed: ")

    def main():
        """Main function to run all tests."""
        print("🚀 vLLM Long Text Embedding Client")
        print(f"📡 Connecting to: ")
        print(f"🤖 Model: ")
        masked_key = "*" * (len(API_KEY) - 4) + API_KEY[-4:] if len(API_KEY) > 4 else "****"
        print(f"🔑 API Key: ")

        # Run all test cases
        test_embedding_with_different_lengths()
        test_batch_embedding()
        test_multiple_long_texts_batch()
        test_embedding_consistency()

        print("\n" + "=" * 70)
        print("🎉 All tests completed!")
        print("\n💡 Key Features Demonstrated:")
        print("   - ✅ Automatic chunked processing for long text")
        print("   - ✅ Seamless handling of mixed-length batches")
        print("   - ✅ Multiple long texts in single batch (chunk ID fix)")
        print("   - ✅ Unified chunked processing:")
        print("     • Native pooling used within each chunk")
        print("     • MEAN aggregation across all chunks")
        print("     • Complete semantic coverage for all pooling types")
        print("   - ✅ Consistent embedding generation")
        print("   - ✅ Backward compatibility with short text")
        print("\n📚 For more information, see:")
        print(
            "   - Documentation: https://docs.vllm.ai/en/latest/models/pooling_models.html"
        )
        print("   - Chunked Processing Guide: openai_embedding_long_text.md")

    if __name__ == "__main__":
        main()

## OpenAI Embedding Long Text - Service[¶](#openai-embedding-long-text-service "Permanent link") 

    #!/bin/bash

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project

    # vLLM Embedding Server with Enhanced Chunked Processing
    # This script starts a vLLM server with chunked processing enabled for long text embedding.
    # Now supports proper pooling type validation and model-specific configurations.

    set -euo pipefail

    # Configuration
    MODEL_NAME=$
    MODEL_CODE=$

    PORT=$
    GPU_COUNT=$
    MAX_EMBED_LEN=$
    API_KEY=$

    # Enhanced pooling configuration with model-specific defaults
    POOLING_TYPE=$  # auto, MEAN, CLS, LAST
    export VLLM_ENABLE_CHUNKED_PROCESSING=true
    export CUDA_VISIBLE_DEVICES=2,3,4,5

    echo "🚀 Starting vLLM Embedding Server with Enhanced Chunked Processing"
    echo "=================================================================="

    # Environment variables for optimization
    export VLLM_WORKER_MULTIPROC_METHOD=spawn

    # Function to determine optimal pooling type for known models
    get_optimal_pooling_type() 

    # Auto-detect pooling type if not explicitly set
    if [ "$POOLING_TYPE" = "auto" ]; then
        POOLING_TYPE=$(get_optimal_pooling_type "$MODEL_NAME")
        echo "🔍 Auto-detected pooling type: $POOLING_TYPE for model $MODEL_NAME"
    fi

    # Display configuration
    echo "📋 Configuration:"
    echo "   - Model: $MODEL_NAME"
    echo "   - Port: $PORT"
    echo "   - GPU Count: $GPU_COUNT"
    echo "   - Enhanced Chunked Processing: $"
    echo "   - Max Embed Length: $ tokens"
    echo "   - Native Pooling Type: $POOLING_TYPE + Normalization"
    echo "   - Cross-chunk Aggregation: MEAN (automatic)"
    echo ""

    # Validate GPU availability
    if command -v nvidia-smi &> /dev/null; then
        gpu_count=$(nvidia-smi --list-gpus | wc -l)
        echo "🖥️  Available GPUs: $gpu_count"
        if [ "$GPU_COUNT" -gt "$gpu_count" ]; then
            echo "⚠️  Warning: Requested $GPU_COUNT GPUs but only $gpu_count available"
            echo "   Adjusting to use $gpu_count GPUs"
            GPU_COUNT=$gpu_count
        fi
    else
        echo "⚠️  Warning: nvidia-smi not found. GPU detection skipped."
    fi

    # Chunked processing uses unified MEAN aggregation
    echo "ℹ️  Chunked Processing: Using $POOLING_TYPE pooling within chunks, MEAN aggregation across chunks"
    echo "   - All chunks processed for complete semantic coverage"
    echo "   - Weighted averaging based on chunk token counts"

    echo ""
    echo "🔧 Starting server with enhanced chunked processing configuration..."

    # Build pooler config JSON
    POOLER_CONFIG=", \"max_embed_len\": $}"

    # Start vLLM server with enhanced chunked processing
    vllm serve "$MODEL_NAME" \
      --tensor-parallel-size "$GPU_COUNT" \
      --enforce-eager \
      --pooler-config "$POOLER_CONFIG" \
      --served-model-name $ \
      --api-key "$API_KEY" \
      --trust-remote-code \
      --port "$PORT" \
      --host 0.0.0.0

    echo ""
    echo "✅ vLLM Embedding Server started successfully!"
    echo ""
    echo "📡 Server Information:"
    echo "   - Base URL: http://localhost:$PORT"
    echo "   - Model Code: $"
    echo "   - API Key: $API_KEY"
    echo "   - Native Pooling: $POOLING_TYPE | Cross-chunk: MEAN"
    echo ""
    echo "🧪 Test the server with:"
    echo "   python examples/online_serving/openai_embedding_long_text/client.py"
    echo ""
    echo "📚 Enhanced features enabled:"
    echo "   ✅ Intelligent native pooling type detection"
    echo "   ✅ Unified MEAN aggregation for chunked processing"
    echo "   ✅ Model-specific native pooling optimization"
    echo "   ✅ Enhanced max embedding length ($ tokens)"
    echo "   ✅ Complete semantic coverage for all pooling types"
    echo "   ✅ OpenAI-compatible API"
    echo "   ✅ GPU acceleration"
    echo ""
    echo "🔧 Advanced usage:"
    echo "   - Set POOLING_TYPE=MEAN|CLS|LAST to override auto-detection"
    echo "   - Set MAX_EMBED_LEN to adjust maximum input length"
    echo "   - All pooling types use MEAN aggregation across chunks" 

## OpenAI Embedding Matryoshka Fy[¶](#openai-embedding-matryoshka-fy "Permanent link")

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    """Example Python client for embedding API dimensions using vLLM API server
    NOTE:
        start a supported Matryoshka Embeddings model server with `vllm serve`, e.g.
        vllm serve jinaai/jina-embeddings-v3 --trust-remote-code
    """

    from openai import OpenAI

    # Modify OpenAI's API key and API base to use vLLM's API server.
    openai_api_key = "EMPTY"
    openai_api_base = "http://localhost:8000/v1"

    def main():
        client = OpenAI(
            # defaults to os.environ.get("OPENAI_API_KEY")
            api_key=openai_api_key,
            base_url=openai_api_base,
        )

        models = client.models.list()
        model = models.data[0].id

        responses = client.embeddings.create(
            input=["Follow the white rabbit."],
            model=model,
            dimensions=32,
        )

        for data in responses.data:
            print(data.embedding)  # List of float of len 32

    if __name__ == "__main__":
        main()