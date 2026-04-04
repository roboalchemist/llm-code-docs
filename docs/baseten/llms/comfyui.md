# Source: https://docs.baseten.co/examples/comfyui.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy a ComfyUI project

> Deploy your ComfyUI workflow as an API endpoint

<Card title="View example on GitHub" horizontal icon="github" iconType="light" href="https://github.com/basetenlabs/truss-examples/tree/main/comfyui-truss" />

In this example, we'll deploy an **anime style transfer** ComfyUI workflow using truss.
This example won't require any Python code, but there are a few pre-requisites in order to get started.

Pre-Requisites:

1. Convert your ComfyUI workflow to an **API compatible JSON format**. The regular JSON format that is used to export Comfy workflows will not work here.
2. Have a list of the models your workflow requires along with URLs to where each model can be downloaded

## Setup

Clone the truss-examples repository and navigate to the `comfyui-truss` directory

```bash  theme={"system"}
git clone https://github.com/basetenlabs/truss-examples.git
cd truss-examples/comfyui-truss
```

This repository already contains all the files we need to deploy our ComfyUI workflow.
There are just two files we need to modify:

1. `config.yaml`
2. `data/comfy_ui_workflow.json`

## Setting up the `config.yaml`

```yaml  theme={"system"}
build_commands:
- git clone https://github.com/comfyanonymous/ComfyUI.git
- cd ComfyUI && git checkout b1fd26fe9e55163f780bf9e5f56bf9bf5f035c93 && pip install -r requirements.txt
- cd ComfyUI/custom_nodes && git clone https://github.com/LykosAI/ComfyUI-Inference-Core-Nodes --recursive && cd ComfyUI-Inference-Core-Nodes && pip install -e .[cuda12]
- cd ComfyUI/custom_nodes && git clone https://github.com/ZHO-ZHO-ZHO/ComfyUI-Gemini --recursive && cd ComfyUI-Gemini && pip install -r requirements.txt
- cd ComfyUI/custom_nodes && git clone https://github.com/kijai/ComfyUI-Marigold --recursive && cd ComfyUI-Marigold && pip install -r requirements.txt
- cd ComfyUI/custom_nodes && git clone https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92 --recursive
- cd ComfyUI/custom_nodes && git clone https://github.com/Fannovel16/comfyui_controlnet_aux --recursive && cd comfyui_controlnet_aux && pip install -r requirements.txt
- cd ComfyUI/models/controlnet && wget -O control-lora-canny-rank256.safetensors https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-canny-rank256.safetensors
- cd ComfyUI/models/controlnet && wget -O control-lora-depth-rank256.safetensors https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-depth-rank256.safetensors
- cd ComfyUI/models/checkpoints && wget -O dreamshaperXL_v21TurboDPMSDE.safetensors https://civitai.com/api/download/models/351306
- cd ComfyUI/models/loras && wget -O StudioGhibli.Redmond-StdGBRRedmAF-StudioGhibli.safetensors https://huggingface.co/artificialguybr/StudioGhibli.Redmond-V2/resolve/main/StudioGhibli.Redmond-StdGBRRedmAF-StudioGhibli.safetensors
environment_variables: {}
external_package_dirs: []
model_metadata: {}
model_name: Anime Style Transfer
python_version: py310
requirements:
  - websocket-client
  - accelerate
  - opencv-python
resources:
  accelerator: H100
  use_gpu: true
secrets: {}
system_packages:
  - wget
  - ffmpeg
  - libgl1-mesa-glx
```

The main part that needs to get filled out is under `build_commands`. Build commands are shell commands that get run during the build stage of the docker image.

In this example, the first two lines clone the ComfyUI repository and install the python requirements.
The latter commands install various custom nodes and models and place them in their respective directory within the ComfyUI repository.

## Modifying `data/comfy_ui_workflow.json`

The `comfy_ui_workflow.json` contains the entire ComfyUI workflow in an API compatible format. This is the workflow that will get executed by the ComfyUI server.

Here is the workflow we will be using for this example.

<Accordion title="Anime Style Transfer Workflow">
  ```json  theme={"system"}
  {
      "1": {
        "inputs": {
          "ckpt_name": "dreamshaperXL_v21TurboDPMSDE.safetensors"
        },
        "class_type": "CheckpointLoaderSimple",
        "_meta": {
          "title": "Load Checkpoint"
        }
      },
      "3": {
        "inputs": {
          "image": "{{input_image}}",
          "upload": "image"
        },
        "class_type": "LoadImage",
        "_meta": {
          "title": "Load Image"
        }
      },
      "4": {
        "inputs": {
          "text": [
            "160",
            0
          ],
          "clip": [
            "154",
            1
          ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
          "title": "CLIP Text Encode (Prompt)"
        }
      },
      "12": {
        "inputs": {
          "strength": 0.8,
          "conditioning": [
            "131",
            0
          ],
          "control_net": [
            "13",
            0
          ],
          "image": [
            "71",
            0
          ]
        },
        "class_type": "ControlNetApply",
        "_meta": {
          "title": "Apply ControlNet"
        }
      },
      "13": {
        "inputs": {
          "control_net_name": "control-lora-canny-rank256.safetensors"
        },
        "class_type": "ControlNetLoader",
        "_meta": {
          "title": "Load ControlNet Model"
        }
      },
      "15": {
        "inputs": {
          "strength": 0.8,
          "conditioning": [
            "12",
            0
          ],
          "control_net": [
            "16",
            0
          ],
          "image": [
            "18",
            0
          ]
        },
        "class_type": "ControlNetApply",
        "_meta": {
          "title": "Apply ControlNet"
        }
      },
      "16": {
        "inputs": {
          "control_net_name": "control-lora-depth-rank256.safetensors"
        },
        "class_type": "ControlNetLoader",
        "_meta": {
          "title": "Load ControlNet Model"
        }
      },
      "18": {
        "inputs": {
          "seed": 995352869972963,
          "denoise_steps": 4,
          "n_repeat": 10,
          "regularizer_strength": 0.02,
          "reduction_method": "median",
          "max_iter": 5,
          "tol": 0.001,
          "invert": true,
          "keep_model_loaded": true,
          "n_repeat_batch_size": 2,
          "use_fp16": true,
          "scheduler": "LCMScheduler",
          "normalize": true,
          "model": "marigold-lcm-v1-0",
          "image": [
            "3",
            0
          ]
        },
        "class_type": "MarigoldDepthEstimation",
        "_meta": {
          "title": "MarigoldDepthEstimation"
        }
      },
      "19": {
        "inputs": {
          "images": [
            "71",
            0
          ]
        },
        "class_type": "PreviewImage",
        "_meta": {
          "title": "Preview Image"
        }
      },
      "20": {
        "inputs": {
          "images": [
            "18",
            0
          ]
        },
        "class_type": "PreviewImage",
        "_meta": {
          "title": "Preview Image"
        }
      },
      "21": {
        "inputs": {
          "seed": 358881677137626,
          "steps": 20,
          "cfg": 7,
          "sampler_name": "dpmpp_2m_sde",
          "scheduler": "karras",
          "denoise": 0.7000000000000001,
          "model": [
            "154",
            0
          ],
          "positive": [
            "15",
            0
          ],
          "negative": [
            "4",
            0
          ],
          "latent_image": [
            "25",
            0
          ]
        },
        "class_type": "KSampler",
        "_meta": {
          "title": "KSampler"
        }
      },
      "25": {
        "inputs": {
          "pixels": [
            "70",
            0
          ],
          "vae": [
            "1",
            2
          ]
        },
        "class_type": "VAEEncode",
        "_meta": {
          "title": "VAE Encode"
        }
      },
      "27": {
        "inputs": {
          "samples": [
            "21",
            0
          ],
          "vae": [
            "1",
            2
          ]
        },
        "class_type": "VAEDecode",
        "_meta": {
          "title": "VAE Decode"
        }
      },
      "70": {
        "inputs": {
          "upscale_method": "lanczos",
          "megapixels": 1,
          "image": [
            "3",
            0
          ]
        },
        "class_type": "ImageScaleToTotalPixels",
        "_meta": {
          "title": "ImageScaleToTotalPixels"
        }
      },
      "71": {
        "inputs": {
          "low_threshold": 50,
          "high_threshold": 150,
          "resolution": 1024,
          "image": [
            "3",
            0
          ]
        },
        "class_type": "CannyEdgePreprocessor",
        "_meta": {
          "title": "Canny Edge"
        }
      },
      "123": {
        "inputs": {
          "images": [
            "27",
            0
          ]
        },
        "class_type": "PreviewImage",
        "_meta": {
          "title": "Preview Image"
        }
      },
      "131": {
        "inputs": {
          "text": [
            "159",
            0
          ],
          "clip": [
            "154",
            1
          ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
          "title": "CLIP Text Encode (Prompt)"
        }
      },
      "152": {
        "inputs": {
          "text": "{{prompt}}"
        },
        "class_type": "Text _O",
        "_meta": {
          "title": "Text_1"
        }
      },
      "154": {
        "inputs": {
          "lora_name": "StudioGhibli.Redmond-StdGBRRedmAF-StudioGhibli.safetensors",
          "strength_model": 0.6,
          "strength_clip": 1,
          "model": [
            "1",
            0
          ],
          "clip": [
            "1",
            1
          ]
        },
        "class_type": "LoraLoader",
        "_meta": {
          "title": "Load LoRA"
        }
      },
      "156": {
        "inputs": {
          "text_1": [
            "152",
            0
          ],
          "text_2": [
            "158",
            0
          ]
        },
        "class_type": "ConcatText_Zho",
        "_meta": {
          "title": "✨ConcatText_Zho"
        }
      },
      "157": {
        "inputs": {
          "text": "StdGBRedmAF,Studio Ghibli,"
        },
        "class_type": "Text _O",
        "_meta": {
          "title": "Text _2"
        }
      },
      "158": {
        "inputs": {
          "text": "looking at viewer, anime artwork, anime style, key visual, vibrant, studio anime, highly detailed"
        },
        "class_type": "Text _O",
        "_meta": {
          "title": "Text _O"
        }
      },
      "159": {
        "inputs": {
          "text_1": [
            "156",
            0
          ],
          "text_2": [
            "157",
            0
          ]
        },
        "class_type": "ConcatText_Zho",
        "_meta": {
          "title": "✨ConcatText_Zho"
        }
      },
      "160": {
        "inputs": {
          "text": "photo, deformed, black and white, realism, disfigured, low contrast"
        },
        "class_type": "Text _O",
        "_meta": {
          "title": "Text _O"
        }
      }
    }
  ```
</Accordion>

**Important:**
If you look at the JSON file above, you'll notice we have templatized a few items using the **`{{handlebars}}`** templating style.

If there are any inputs in your ComfyUI workflow that should be variables such as input prompts, images, etc, you should templatize them using the handlebars format.

In this example workflow, there are two inputs:  **`{{input_image}}`** and **`{{prompt}}`**

When making an API call to this workflow, we will be able to pass in any variable for these two inputs.

## Deploying the Workflow to Baseten

Once you have both your `config.yaml` and `data/comfy_ui_workflow.json` filled out we can deploy this workflow just like any other model on Baseten.

1. `pip install truss --upgrade`
2. `truss push --publish`

## Running Inference

When you deploy the truss, it will spin up a new deployment in your Baseten account. Each deployment will expose a REST API endpoint which we can use to call this workflow.

```python  theme={"system"}
import requests
import os
import base64
from PIL import Image
from io import BytesIO

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]
BASE64_PREAMBLE = "data:image/png;base64,"

def pil_to_b64(pil_img):
   buffered = BytesIO()
   pil_img.save(buffered, format="PNG")
   img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
   return img_str

def b64_to_pil(b64_str):
   return Image.open(BytesIO(base64.b64decode(b64_str.replace(BASE64_PREAMBLE, ""))))

values = {
 "prompt": "american Shorthair",
 "input_image": {"type": "image", "data": pil_to_b64(Image.open("/path/to/cat.png"))}
}

resp = requests.post(
   f"https://model-{model_id}.api.baseten.co/production/predict",
   headers={"Authorization": f"Api-Key {baseten_api_key}"},
   json={"workflow_values": values}
)

res = resp.json()
results = res.get("result")

for item in results:
   if item.get("format") == "png":
       data = item.get("data")
       img = b64_to_pil(data)
       img.save(f"pet-style-transfer-1.png")
```

If you recall, we templatized two variables in our workflow: `prompt` and `input_image`. In our API call we can specify the values for these two variables like so:

```json  theme={"system"}
values = {
 "prompt": "Maltipoo",
 "input_image": {"type": "image", "data": pil_to_b64(Image.open("/path/to/dog.png"))}
}
```

If your workflow contains more variables, simply add them to the dictionary above.

The API call returns an image in the form of a base64 string, which we convert to a PNG image.

<Frame>
  <img src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/pic-to-anime.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=2c74f510d7b1c09d20a6ed1a189ee94f" data-og-width="2400" width="2400" data-og-height="981" height="981" data-path="images/pic-to-anime.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/pic-to-anime.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=64cc5319254a073201e30a7eaf8c1711 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/pic-to-anime.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=15d8f0484852d14155a190b5a21b7d32 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/pic-to-anime.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=155d16198263c8afe5bca85a97437455 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/pic-to-anime.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=8b53df3d76801809aa7e6fe04feade1c 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/pic-to-anime.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=1d6892ab6b39a445bdea9f4b9597ba41 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/pic-to-anime.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=130e8c15418e8c78f103c3a3ee453ffc 2500w" />
</Frame>
