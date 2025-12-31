# Source: https://docs.vllm.ai/en/stable/features/multimodal_inputs/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/features/multimodal_inputs.md "Edit this page")

# Multimodal Inputs[¶](#multimodal-inputs "Permanent link")

This page teaches you how to pass multi-modal inputs to [multi-modal models](../../models/supported_models/#list-of-multimodal-language-models) in vLLM.

Note

We are actively iterating on multi-modal support. See [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] this RFC](https://github.com/vllm-project/vllm/issues/4194) for upcoming changes, and [open an issue on GitHub](https://github.com/vllm-project/vllm/issues/new/choose) if you have any feedback or feature requests.

Tip

When serving multi-modal models, consider setting `--allowed-media-domains` to restrict domain that vLLM can access to prevent it from accessing arbitrary endpoints that can potentially be vulnerable to Server-Side Request Forgery (SSRF) attacks. You can provide a list of domains for this arg. For example: `--allowed-media-domains upload.wikimedia.org github.com www.bogotobogo.com`

Also, consider setting `VLLM_MEDIA_URL_ALLOW_REDIRECTS=0` to prevent HTTP redirects from being followed to bypass domain restrictions.

This restriction is especially important if you run vLLM in a containerized environment where the vLLM pods may have unrestricted access to internal networks.

## Offline Inference[¶](#offline-inference "Permanent link")

To input multi-modal data, follow this schema in [vllm.inputs.PromptType](../../api/vllm/inputs/#vllm.inputs.PromptType "            PromptType

  
      module-attribute
  "):

-   `prompt`: The prompt should follow the format that is documented on HuggingFace.
-   `multi_modal_data`: This is a dictionary that follows the schema defined in [vllm.multimodal.inputs.MultiModalDataDict](../../api/vllm/multimodal/inputs/#vllm.multimodal.inputs.MultiModalDataDict "            MultiModalDataDict

      
          module-attribute
      ").

### Stable UUIDs for Caching (multi_modal_uuids)[¶](#stable-uuids-for-caching-multi_modal_uuids "Permanent link")

When using multi-modal inputs, vLLM normally hashes each media item by content to enable caching across requests. You can optionally pass `multi_modal_uuids` to provide your own stable IDs for each item so caching can reuse work across requests without rehashing the raw content.

Code

    from vllm import LLM
    from PIL import Image

    # Qwen2.5-VL example with two images
    llm = LLM(model="Qwen/Qwen2.5-VL-3B-Instruct")

    prompt = "USER: <image><image>\nDescribe the differences.\nASSISTANT:"
    img_a = Image.open("/path/to/a.jpg")
    img_b = Image.open("/path/to/b.jpg")

    outputs = llm.generate(,
        # Provide stable IDs for caching.
        # Requirements (matched by this example):
        #  - Include every modality present in multi_modal_data.
        #  - For lists, provide the same number of entries.
        #  - Use None to fall back to content hashing for that item.
        "multi_modal_uuids": ,
    })

    for o in outputs:
        print(o.outputs[0].text)

Using UUIDs, you can also skip sending media data entirely if you expect cache hits for respective items. Note that the request will fail if the skipped media doesn\'t have a corresponding UUID, or if the UUID fails to hit the cache.

Code

    from vllm import LLM
    from PIL import Image

    # Qwen2.5-VL example with two images
    llm = LLM(model="Qwen/Qwen2.5-VL-3B-Instruct")

    prompt = "USER: <image><image>\nDescribe the differences.\nASSISTANT:"
    img_b = Image.open("/path/to/b.jpg")

    outputs = llm.generate(,
        # Since img_a is expected to be cached, we can skip sending the actual
        # image entirely.
        "multi_modal_uuids": ,
    })

    for o in outputs:
        print(o.outputs[0].text)

Warning

If both multimodal processor caching and prefix caching are disabled, user-provided `multi_modal_uuids` are ignored.

### Image Inputs[¶](#image-inputs "Permanent link")

You can pass a single image to the `'image'` field of the multi-modal dictionary, as shown in the following examples:

Code

    from vllm import LLM

    llm = LLM(model="llava-hf/llava-1.5-7b-hf")

    # Refer to the HuggingFace repo for the correct format to use
    prompt = "USER: <image>\nWhat is the content of this image?\nASSISTANT:"

    # Load the image using PIL.Image
    image = PIL.Image.open(...)

    # Single prompt inference
    outputs = llm.generate(,
    })

    for o in outputs:
        generated_text = o.outputs[0].text
        print(generated_text)

    # Batch inference
    image_1 = PIL.Image.open(...)
    image_2 = PIL.Image.open(...)
    outputs = llm.generate(
        [
            ,
            },
            ,
            }
        ]
    )

    for o in outputs:
        generated_text = o.outputs[0].text
        print(generated_text)

Full example: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/offline_inference/vision_language.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/vision_language.py)

To substitute multiple images inside the same text prompt, you can pass in a list of images instead:

Code

    from vllm import LLM

    llm = LLM(
        model="microsoft/Phi-3.5-vision-instruct",
        trust_remote_code=True,  # Required to load Phi-3.5-vision
        max_model_len=4096,  # Otherwise, it may not fit in smaller GPUs
        limit_mm_per_prompt=,  # The maximum number to accept
    )

    # Refer to the HuggingFace repo for the correct format to use
    prompt = "<|user|>\n<|image_1|>\n<|image_2|>\nWhat is the content of each image?<|end|>\n<|assistant|>\n"

    # Load the images using PIL.Image
    image1 = PIL.Image.open(...)
    image2 = PIL.Image.open(...)

    outputs = llm.generate(,
    })

    for o in outputs:
        generated_text = o.outputs[0].text
        print(generated_text)

Full example: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/offline_inference/vision_language_multi_image.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/vision_language_multi_image.py)

If using the [LLM.chat](../../models/generative_models/#llmchat) method, you can pass images directly in the message content using various formats: image URLs, PIL Image objects, or pre-computed embeddings:

    from vllm import LLM
    from vllm.assets.image import ImageAsset

    llm = LLM(model="llava-hf/llava-1.5-7b-hf")
    image_url = "https://picsum.photos/id/32/512/512"
    image_pil = ImageAsset('cherry_blossom').pil_image
    image_embeds = torch.load(...)

    conversation = [
        ,
        ,
        ,
        ,
                },
                ,
                ,
                ,
            ],
        },
    ]

    # Perform inference and log output.
    outputs = llm.chat(conversation)

    for o in outputs:
        generated_text = o.outputs[0].text
        print(generated_text)

Multi-image input can be extended to perform video captioning. We show this with [Qwen2-VL](https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct) as it supports videos:

Code

    from vllm import LLM

    # Specify the maximum number of frames per video to be 4. This can be changed.
    llm = LLM("Qwen/Qwen2-VL-2B-Instruct", limit_mm_per_prompt=)

    # Create the request payload.
    video_frames = ... # load your video making sure it only has the number of frames specified earlier.
    message = ,
        ],
    }
    for i in range(len(video_frames)):
        base64_image = encode_image(video_frames[i]) # base64 encoding.
        new_image = "}}
        message["content"].append(new_image)

    # Perform inference and log output.
    outputs = llm.chat([message])

    for o in outputs:
        generated_text = o.outputs[0].text
        print(generated_text)

#### Custom RGBA Background Color[¶](#custom-rgba-background-color "Permanent link")

When loading RGBA images (images with transparency), vLLM converts them to RGB format. By default, transparent pixels are replaced with white background. You can customize this background color using the `rgba_background_color` parameter in `media_io_kwargs`.

Code

    from vllm import LLM

    # Default white background (no configuration needed)
    llm = LLM(model="llava-hf/llava-1.5-7b-hf")

    # Custom black background for dark theme
    llm = LLM(
        model="llava-hf/llava-1.5-7b-hf",
        media_io_kwargs=},
    )

    # Custom brand color background (e.g., blue)
    llm = LLM(
        model="llava-hf/llava-1.5-7b-hf",
        media_io_kwargs=},
    )

Note

-   The `rgba_background_color` accepts RGB values as a list `[R, G, B]` or tuple `(R, G, B)` where each value is 0-255
-   This setting only affects RGBA images with transparency; RGB images are unchanged
-   If not specified, the default white background `(255, 255, 255)` is used for backward compatibility

### Video Inputs[¶](#video-inputs "Permanent link")

You can pass a list of NumPy arrays directly to the `'video'` field of the multi-modal dictionary instead of using multi-image input.

Instead of NumPy arrays, you can also pass `'torch.Tensor'` instances, as shown in this example using Qwen2.5-VL:

Code

    from transformers import AutoProcessor
    from vllm import LLM, SamplingParams
    from qwen_vl_utils import process_vision_info

    model_path = "Qwen/Qwen2.5-VL-3B-Instruct"
    video_path = "https://content.pexels.com/videos/free-videos.mp4"

    llm = LLM(
        model=model_path,
        gpu_memory_utilization=0.8,
        enforce_eager=True,
        limit_mm_per_prompt=,
    )

    sampling_params = SamplingParams(max_tokens=1024)

    video_messages = [
        ,
        ,
                ,
            ]
        },
    ]

    messages = video_messages
    processor = AutoProcessor.from_pretrained(model_path)
    prompt = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    image_inputs, video_inputs = process_vision_info(messages)
    mm_data = 
    if video_inputs is not None:
        mm_data["video"] = video_inputs

    llm_inputs = 

    outputs = llm.generate([llm_inputs], sampling_params=sampling_params)
    for o in outputs:
        generated_text = o.outputs[0].text
        print(generated_text)

Note

\'process_vision_info\' is only applicable to Qwen2.5-VL and similar models.

Full example: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/offline_inference/vision_language.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/vision_language.py)

### Audio Inputs[¶](#audio-inputs "Permanent link")

You can pass a tuple `(array, sampling_rate)` to the `'audio'` field of the multi-modal dictionary.

Full example: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/offline_inference/audio_language.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/audio_language.py)

### Embedding Inputs[¶](#embedding-inputs "Permanent link")

To input pre-computed embeddings belonging to a data type (i.e. image, video, or audio) directly to the language model, pass a tensor of shape `(num_items, feature_size, hidden_size of LM)` to the corresponding field of the multi-modal dictionary.

You must enable this feature via `enable_mm_embeds=True`.

Warning

The vLLM engine may crash if incorrect shape of embeddings is passed. Only enable this flag for trusted users!

#### Image Embeddings[¶](#image-embeddings "Permanent link")

Code

    from vllm import LLM

    # Inference with image embeddings as input
    llm = LLM(model="llava-hf/llava-1.5-7b-hf", enable_mm_embeds=True)

    # Refer to the HuggingFace repo for the correct format to use
    prompt = "USER: <image>\nWhat is the content of this image?\nASSISTANT:"

    # Embeddings for single image
    # torch.Tensor of shape (1, image_feature_size, hidden_size of LM)
    image_embeds = torch.load(...)

    outputs = llm.generate(,
    })

    for o in outputs:
        generated_text = o.outputs[0].text
        print(generated_text)

For Qwen2-VL and MiniCPM-V, we accept additional parameters alongside the embeddings:

Code

    # Construct the prompt based on your model
    prompt = ...

    # Embeddings for multiple images
    # torch.Tensor of shape (num_images, image_feature_size, hidden_size of LM)
    image_embeds = torch.load(...)

    # Qwen2-VL
    llm = LLM(
        "Qwen/Qwen2-VL-2B-Instruct",
        limit_mm_per_prompt=,
        enable_mm_embeds=True,
    )
    mm_data = 
    }

    # MiniCPM-V
    llm = LLM(
        "openbmb/MiniCPM-V-2_6",
        trust_remote_code=True,
        limit_mm_per_prompt=,
        enable_mm_embeds=True,
    )
    mm_data = 
    }

    outputs = llm.generate()

    for o in outputs:
        generated_text = o.outputs[0].text
        print(generated_text)

For Qwen3-VL, the `image_embeds` should contain both the base image embedding and deepstack features.

#### Audio Embedding Inputs[¶](#audio-embedding-inputs "Permanent link")

You can pass pre-computed audio embeddings similar to image embeddings:

Code

    from vllm import LLM
    import torch

    # Enable audio embeddings support
    llm = LLM(model="fixie-ai/ultravox-v0_5-llama-3_2-1b", enable_mm_embeds=True)

    # Refer to the HuggingFace repo for the correct format to use
    prompt = "USER: <audio>\nWhat is in this audio?\nASSISTANT:"

    # Load pre-computed audio embeddings
    # torch.Tensor of shape (1, audio_feature_size, hidden_size of LM)
    audio_embeds = torch.load(...)

    outputs = llm.generate(,
    })

    for o in outputs:
        generated_text = o.outputs[0].text
        print(generated_text)

## Online Serving[¶](#online-serving "Permanent link")

Our OpenAI-compatible server accepts multi-modal data via the [Chat Completions API](https://platform.openai.com/docs/api-reference/chat). Media inputs also support optional UUIDs users can provide to uniquely identify each media, which is used to cache the media results across requests.

Important

A chat template is **required** to use Chat Completions API. For HF format models, the default chat template is defined inside `chat_template.json` or `tokenizer_config.json`.

If no default chat template is available, we will first look for a built-in fallback in [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] vllm/transformers_utils/chat_templates/registry.py](https://github.com/vllm-project/vllm/blob/main/vllm/transformers_utils/chat_templates/registry.py). If no fallback is available, an error is raised and you have to provide the chat template manually via the `--chat-template` argument.

For certain models, we provide alternative chat templates inside [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples](https://github.com/vllm-project/vllm/tree/main/examples). For example, VLM2Vec uses [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/template_vlm2vec_phi3v.jinja](https://github.com/vllm-project/vllm/blob/main/examples/template_vlm2vec_phi3v.jinja) which is different from the default one for Phi-3-Vision.

### Image Inputs[¶](#image-inputs_1 "Permanent link") 

Image input is supported according to [OpenAI Vision API](https://platform.openai.com/docs/guides/vision). Here is a simple example using Phi-3.5-Vision.

First, launch the OpenAI-compatible server:

    vllm serve microsoft/Phi-3.5-vision-instruct --runner generate \
      --trust-remote-code --max-model-len 4096 --limit-mm-per-prompt ''

Then, you can use the OpenAI client as follows:

Code

    from openai import OpenAI

    openai_api_key = "EMPTY"
    openai_api_base = "http://localhost:8000/v1"

    client = OpenAI(
        api_key=openai_api_key,
        base_url=openai_api_base,
    )

    # Single-image input inference
    image_url = "https://vllm-public-assets.s3.us-west-2.amazonaws.com/vision_model_images/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"

    chat_response = client.chat.completions.create(
        model="microsoft/Phi-3.5-vision-instruct",
        messages=[
            ,
                    ,
                        "uuid": image_url,  # Optional
                    },
                ],
            }
        ],
    )
    print("Chat completion output:", chat_response.choices[0].message.content)

    # Multi-image input inference
    image_url_duck = "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/duck.jpg"
    image_url_lion = "https://vllm-public-assets.s3.us-west-2.amazonaws.com/multimodal_asset/lion.jpg"

    chat_response = client.chat.completions.create(
        model="microsoft/Phi-3.5-vision-instruct",
        messages=[
            ,
                    ,
                        "uuid": image_url_duck,  # Optional
                    },
                    ,
                        "uuid": image_url_lion,  # Optional
                    },
                ],
            }
        ],
    )
    print("Chat completion output:", chat_response.choices[0].message.content)

Full example: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/online_serving/openai_chat_completion_client_for_multimodal.py](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_client_for_multimodal.py)

Tip

Loading from local file paths is also supported on vLLM: You can specify the allowed local media path via `--allowed-local-media-path` when launching the API server/engine, and pass the file path as `url` in the API request.

Tip

There is no need to place image placeholders in the text content of the API request - they are already represented by the image content. In fact, you can place image placeholders in the middle of the text by interleaving text and image content.

Note

By default, the timeout for fetching images through HTTP URL is `5` seconds. You can override this by setting the environment variable:

    export VLLM_IMAGE_FETCH_TIMEOUT=<timeout>

### Video Inputs[¶](#video-inputs_1 "Permanent link") 

Instead of `image_url`, you can pass a video file via `video_url`. Here is a simple example using [LLaVA-OneVision](https://huggingface.co/llava-hf/llava-onevision-qwen2-0.5b-ov-hf).

First, launch the OpenAI-compatible server:

    vllm serve llava-hf/llava-onevision-qwen2-0.5b-ov-hf --runner generate --max-model-len 8192

Then, you can use the OpenAI client as follows:

Code

    from openai import OpenAI

    openai_api_key = "EMPTY"
    openai_api_base = "http://localhost:8000/v1"

    client = OpenAI(
        api_key=openai_api_key,
        base_url=openai_api_base,
    )

    video_url = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4"

    ## Use video url in the payload
    chat_completion_from_url = client.chat.completions.create(
        messages=[
            ,
                    ,
                        "uuid": video_url,  # Optional
                    },
                ],
            }
        ],
        model=model,
        max_completion_tokens=64,
    )

    result = chat_completion_from_url.choices[0].message.content
    print("Chat completion output from image url:", result)

Full example: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/online_serving/openai_chat_completion_client_for_multimodal.py](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_client_for_multimodal.py)

Note

By default, the timeout for fetching videos through HTTP URL is `30` seconds. You can override this by setting the environment variable:

    export VLLM_VIDEO_FETCH_TIMEOUT=<timeout>

#### Custom RGBA Background Color[¶](#custom-rgba-background-color_1 "Permanent link") 

To use a custom background color for RGBA images, pass the `rgba_background_color` parameter via `--media-io-kwargs`:

    # Example: Black background for dark theme
    vllm serve llava-hf/llava-1.5-7b-hf \
      --media-io-kwargs '}'

    # Example: Custom gray background
    vllm serve llava-hf/llava-1.5-7b-hf \
      --media-io-kwargs '}'

### Audio Inputs[¶](#audio-inputs_1 "Permanent link") 

Audio input is supported according to [OpenAI Audio API](https://platform.openai.com/docs/guides/audio?audio-generation-quickstart-example=audio-in). Here is a simple example using Ultravox-v0.5-1B.

First, launch the OpenAI-compatible server:

    vllm serve fixie-ai/ultravox-v0_5-llama-3_2-1b

Then, you can use the OpenAI client as follows:

Code

    import base64
    import requests
    from openai import OpenAI
    from vllm.assets.audio import AudioAsset

    def encode_base64_content_from_url(content_url: str) -> str:
        """Encode a content retrieved from a remote url to base64 format."""

        with requests.get(content_url) as response:
            response.raise_for_status()
            result = base64.b64encode(response.content).decode('utf-8')

        return result

    openai_api_key = "EMPTY"
    openai_api_base = "http://localhost:8000/v1"

    client = OpenAI(
        api_key=openai_api_key,
        base_url=openai_api_base,
    )

    # Any format supported by librosa is supported
    audio_url = AudioAsset("winning_call").url
    audio_base64 = encode_base64_content_from_url(audio_url)

    chat_completion_from_base64 = client.chat.completions.create(
        messages=[
            ,
                    ,
                        "uuid": audio_url,  # Optional
                    },
                ],
            },
        ],
        model=model,
        max_completion_tokens=64,
    )

    result = chat_completion_from_base64.choices[0].message.content
    print("Chat completion output from input audio:", result)

Alternatively, you can pass `audio_url`, which is the audio counterpart of `image_url` for image input:

Code

    chat_completion_from_url = client.chat.completions.create(
        messages=[
            ,
                    ,
                        "uuid": audio_url,  # Optional
                    },
                ],
            }
        ],
        model=model,
        max_completion_tokens=64,
    )

    result = chat_completion_from_url.choices[0].message.content
    print("Chat completion output from audio url:", result)

Full example: [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] examples/online_serving/openai_chat_completion_client_for_multimodal.py](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_client_for_multimodal.py)

Note

By default, the timeout for fetching audios through HTTP URL is `10` seconds. You can override this by setting the environment variable:

    export VLLM_AUDIO_FETCH_TIMEOUT=<timeout>

### Embedding Inputs[¶](#embedding-inputs_1 "Permanent link") 

To input pre-computed embeddings belonging to a data type (i.e. image, video, or audio) directly to the language model, pass a tensor of shape `(num_items, feature_size, hidden_size of LM)` to the corresponding field of the multi-modal dictionary.

You must enable this feature via the `--enable-mm-embeds` flag in `vllm serve`.

Warning

The vLLM engine may crash if incorrect shape of embeddings is passed. Only enable this flag for trusted users!

#### Image Embedding Inputs[¶](#image-embedding-inputs "Permanent link")

For image embeddings, you can pass the base64-encoded tensor to the `image_embeds` field. The following example demonstrates how to pass image embeddings to the OpenAI server:

Code

    from vllm.utils.serial_utils import tensor2base64

    image_embedding = torch.load(...)
    grid_thw = torch.load(...) # Required by Qwen/Qwen2-VL-2B-Instruct

    base64_image_embedding = tensor2base64(image_embedding)

    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=openai_api_key,
        base_url=openai_api_base,
    )

    # Basic usage - this is equivalent to the LLaVA example for offline inference
    model = "llava-hf/llava-1.5-7b-hf"
    embeds = ",
        "uuid": image_url,  # Optional
    }

    # Pass additional parameters (available to Qwen2-VL and MiniCPM-V)
    model = "Qwen/Qwen2-VL-2B-Instruct"
    embeds = ",  # Required
            "image_grid_thw": f"",  # Required by Qwen/Qwen2-VL-2B-Instruct
        },
        "uuid": image_url,  # Optional
    }
    model = "openbmb/MiniCPM-V-2_6"
    embeds = ",  # Required
            "image_sizes": f"",  # Required by openbmb/MiniCPM-V-2_6
        },
        "uuid": image_url,  # Optional
    }
    chat_completion = client.chat.completions.create(
        messages=[
            ,
            ,
                    embeds,
                ],
            },
        ],
        model=model,
    )

For Online Serving, you can also skip sending media if you expect cache hits with provided UUIDs. You can do so by sending media like this:

    ```python
        # Image/video/audio URL:
        ,

        # image_embeds
        ,

        # input_audio:
        ,

        # PIL Image:
        ,

    ```

Note

Multiple messages can now contain ``, enabling you to pass multiple image embeddings in a single request (similar to regular images). The number of embeddings is limited by `--limit-mm-per-prompt`.

**Important**: The embedding shape format differs based on the number of embeddings:

-   **Single embedding**: 3D tensor of shape `(1, feature_size, hidden_size)`
-   **Multiple embeddings**: List of 2D tensors, each of shape `(feature_size, hidden_size)`

If used with a model that requires additional parameters, you must also provide a tensor for each of them, e.g. `image_grid_thw`, `image_sizes`, etc.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 7, 2025] ]