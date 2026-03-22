# Source: https://docs.wandb.ai/models/integrations/diffusers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Hugging Face Diffusers

> Use W&B autolog with Hugging Face Diffusers to track prompts, generated media, configs, and pipeline architecture.

export const ColabLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="colab-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01.21.03zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z" />
    </svg>
    Try in Colab
  </a>;

<ColabLink url="https://colab.research.google.com/github/wandb/examples/blob/master/colabs/diffusers/lcm-diffusers.ipynb" />

[Hugging Face Diffusers](https://huggingface.co/docs/diffusers/index) is the go-to library for state-of-the-art pre-trained diffusion models for generating images, audio, and even 3D structures of molecules. The W\&B integration adds rich, flexible experiment tracking, media visualization, pipeline architecture, and configuration management to interactive centralized dashboards without compromising that ease of use.

## Next-level logging in just two lines

Log all the prompts, negative prompts, generated media, and configs associated with your experiment by simply including 2 lines of code. Here are the 2 lines of code to begin logging:

```python  theme={null}
# import the autolog function
from wandb.integration.diffusers import autolog

# call the autolog before calling the pipeline
autolog(init=dict(project="diffusers_logging"))
```

<Frame caption="An example of how the results of your experiment are logged.">
  <img src="https://mintcdn.com/wb-21fd5541/mVjDwbx0mC8gYx-b/images/integrations/diffusers-autolog-4.gif?s=8e9d8b2001e9fb16e3cf833e800d6672" alt="Experiment results logging" width="800" height="419" data-path="images/integrations/diffusers-autolog-4.gif" />
</Frame>

## Get started

1. Install `diffusers`, `transformers`, `accelerate`, and `wandb`.

   * Command line:

     ```shell  theme={null}
     pip install --upgrade diffusers transformers accelerate wandb
     ```

   * Notebook:

     ```bash  theme={null}
     !pip install --upgrade diffusers transformers accelerate wandb
     ```

2. Use `autolog` to initialize a W\&B Run and automatically track the inputs and the outputs from [all supported pipeline calls](https://github.com/wandb/wandb/blob/main/wandb/integration/diffusers/autologger.py#L12-L72).

   You can call the `autolog()` function with the `init` parameter, which accepts a dictionary of parameters required by [`wandb.init()`](/models/ref/python/functions/init).

   When you call `autolog()`, it initializes a W\&B Run and automatically tracks the inputs and the outputs from [all supported pipeline calls](https://github.com/wandb/wandb/blob/main/wandb/integration/diffusers/autologger.py#L12-L72).

   * Each pipeline call is tracked into its own [table](/models/tables/) in the workspace, and the configs associated with the pipeline call is appended to the list of workflows in the configs for that run.
   * The prompts, negative prompts, and the generated media are logged in a [`wandb.Table`](/models/tables/).
   * All other configs associated with the experiment including seed and the pipeline architecture are stored in the config section for the run.
   * The generated media for each pipeline call are also logged in [media panels](/models/track/log/media/) in the run.

   <Note>
     You can find a [list of supported pipeline calls](https://github.com/wandb/wandb/blob/main/wandb/integration/diffusers/autologger.py#L12-L72). In case, you want to request a new feature of this integration or report a bug associated with it, open an issue on the [W\&B GitHub issues page](https://github.com/wandb/wandb/issues).
   </Note>

## Examples

### Autologging

Here is a brief end-to-end example of the autolog in action:

<Tabs>
  <Tab title="Script">
    ```python  theme={null}
    import torch
    from diffusers import DiffusionPipeline

    # import the autolog function
    from wandb.integration.diffusers import autolog

    # call the autolog before calling the pipeline
    autolog(init=dict(project="diffusers_logging"))

    # Initialize the diffusion pipeline
    pipeline = DiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-2-1", torch_dtype=torch.float16
    ).to("cuda")

    # Define the prompts, negative prompts, and seed.
    prompt = ["a photograph of an astronaut riding a horse", "a photograph of a dragon"]
    negative_prompt = ["ugly, deformed", "ugly, deformed"]
    generator = torch.Generator(device="cpu").manual_seed(10)

    # call the pipeline to generate the images
    images = pipeline(
        prompt,
        negative_prompt=negative_prompt,
        num_images_per_prompt=2,
        generator=generator,
    )
    ```
  </Tab>

  <Tab title="Notebook">
    ```python  theme={null}
    import torch
    from diffusers import DiffusionPipeline

    import wandb

    # import the autolog function
    from wandb.integration.diffusers import autolog

    run = wandb.init()

    # call the autolog before calling the pipeline
    autolog(init=dict(project="diffusers_logging"))

    # Initialize the diffusion pipeline
    pipeline = DiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-2-1", torch_dtype=torch.float16
    ).to("cuda")

    # Define the prompts, negative prompts, and seed.
    prompt = ["a photograph of an astronaut riding a horse", "a photograph of a dragon"]
    negative_prompt = ["ugly, deformed", "ugly, deformed"]
    generator = torch.Generator(device="cpu").manual_seed(10)

    # call the pipeline to generate the images
    images = pipeline(
        prompt,
        negative_prompt=negative_prompt,
        num_images_per_prompt=2,
        generator=generator,
    )

    # Finish the experiment
    run.finish()
    ```
  </Tab>
</Tabs>

* The results of a single experiment:

  <Frame>
    <img src="https://mintcdn.com/wb-21fd5541/mVjDwbx0mC8gYx-b/images/integrations/diffusers-autolog-2.gif?s=288200006de1764692a7677c7c5dd080" alt="Experiment results logging" width="900" height="508" data-path="images/integrations/diffusers-autolog-2.gif" />
  </Frame>

* The results of multiple experiments:

  <Frame>
    <img src="https://mintcdn.com/wb-21fd5541/mVjDwbx0mC8gYx-b/images/integrations/diffusers-autolog-1.gif?s=b7de1bfc84eb2c624c3e1d79c5a1f371" alt="Experiment results logging" width="888" height="448" data-path="images/integrations/diffusers-autolog-1.gif" />
  </Frame>

* The config of an experiment:

  <Frame>
    <img src="https://mintcdn.com/wb-21fd5541/mVjDwbx0mC8gYx-b/images/integrations/diffusers-autolog-3.gif?s=1080de61acd06bc726162af38844eeba" alt="Experiment config logging" width="600" height="683" data-path="images/integrations/diffusers-autolog-3.gif" />
  </Frame>

<Note>
  You need to explicitly call [`wandb.Run.finish()`](/models/ref/python/functions/finish) when executing the code in IPython notebook environments after calling the pipeline. This is not necessary when executing python scripts.
</Note>

### Tracking multi-pipeline workflows

This section demonstrates the autolog with a typical [Stable Diffusion XL + Refiner](https://huggingface.co/docs/diffusers/using-diffusers/sdxl#base-to-refiner-model) workflow, in which the latents generated by the [`StableDiffusionXLPipeline`](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/stable_diffusion_xl) is refined by the corresponding refiner.

<Tabs>
  <Tab title="Python Script">
    ```python  theme={null}
    import torch
    from diffusers import StableDiffusionXLImg2ImgPipeline, StableDiffusionXLPipeline
    from wandb.integration.diffusers import autolog

    # initialize the SDXL base pipeline
    base_pipeline = StableDiffusionXLPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0",
        torch_dtype=torch.float16,
        variant="fp16",
        use_safetensors=True,
    )
    base_pipeline.enable_model_cpu_offload()

    # initialize the SDXL refiner pipeline
    refiner_pipeline = StableDiffusionXLImg2ImgPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-refiner-1.0",
        text_encoder_2=base_pipeline.text_encoder_2,
        vae=base_pipeline.vae,
        torch_dtype=torch.float16,
        use_safetensors=True,
        variant="fp16",
    )
    refiner_pipeline.enable_model_cpu_offload()

    prompt = "a photo of an astronaut riding a horse on mars"
    negative_prompt = "static, frame, painting, illustration, sd character, low quality, low resolution, greyscale, monochrome, nose, cropped, lowres, jpeg artifacts, deformed iris, deformed pupils, bad eyes, semi-realistic worst quality, bad lips, deformed mouth, deformed face, deformed fingers, deformed toes standing still, posing"

    # Make the experiment reproducible by controlling randomness.
    # The seed would be automatically logged to WandB.
    seed = 42
    generator_base = torch.Generator(device="cuda").manual_seed(seed)
    generator_refiner = torch.Generator(device="cuda").manual_seed(seed)

    # Call WandB Autolog for Diffusers. This would automatically log
    # the prompts, generated images, pipeline architecture and all
    # associated experiment configs to W&B, thus making your
    # image generation experiments easy to reproduce, share and analyze.
    autolog(init=dict(project="sdxl"))

    # Call the base pipeline to generate the latents
    image = base_pipeline(
        prompt=prompt,
        negative_prompt=negative_prompt,
        output_type="latent",
        generator=generator_base,
    ).images[0]

    # Call the refiner pipeline to generate the refined image
    image = refiner_pipeline(
        prompt=prompt,
        negative_prompt=negative_prompt,
        image=image[None, :],
        generator=generator_refiner,
    ).images[0]
    ```
  </Tab>

  <Tab title="Notebook">
    ```python  theme={null}
    import torch
    from diffusers import StableDiffusionXLImg2ImgPipeline, StableDiffusionXLPipeline

    import wandb
    from wandb.integration.diffusers import autolog

    run = wandb.init()

    # initialize the SDXL base pipeline
    base_pipeline = StableDiffusionXLPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0",
        torch_dtype=torch.float16,
        variant="fp16",
        use_safetensors=True,
    )
    base_pipeline.enable_model_cpu_offload()

    # initialize the SDXL refiner pipeline
    refiner_pipeline = StableDiffusionXLImg2ImgPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-refiner-1.0",
        text_encoder_2=base_pipeline.text_encoder_2,
        vae=base_pipeline.vae,
        torch_dtype=torch.float16,
        use_safetensors=True,
        variant="fp16",
    )
    refiner_pipeline.enable_model_cpu_offload()

    prompt = "a photo of an astronaut riding a horse on mars"
    negative_prompt = "static, frame, painting, illustration, sd character, low quality, low resolution, greyscale, monochrome, nose, cropped, lowres, jpeg artifacts, deformed iris, deformed pupils, bad eyes, semi-realistic worst quality, bad lips, deformed mouth, deformed face, deformed fingers, deformed toes standing still, posing"

    # Make the experiment reproducible by controlling randomness.
    # The seed would be automatically logged to WandB.
    seed = 42
    generator_base = torch.Generator(device="cuda").manual_seed(seed)
    generator_refiner = torch.Generator(device="cuda").manual_seed(seed)

    # Call WandB Autolog for Diffusers. This would automatically log
    # the prompts, generated images, pipeline architecture and all
    # associated experiment configs to W&B, thus making your
    # image generation experiments easy to reproduce, share and analyze.
    autolog(init=dict(project="sdxl"))

    # Call the base pipeline to generate the latents
    image = base_pipeline(
        prompt=prompt,
        negative_prompt=negative_prompt,
        output_type="latent",
        generator=generator_base,
    ).images[0]

    # Call the refiner pipeline to generate the refined image
    image = refiner_pipeline(
        prompt=prompt,
        negative_prompt=negative_prompt,
        image=image[None, :],
        generator=generator_refiner,
    ).images[0]

    # Finish the experiment
    run.finish()
    ```
  </Tab>
</Tabs>

* Example of a Stable Diffisuion XL + Refiner experiment:
  <Frame>
    <img src="https://mintcdn.com/wb-21fd5541/mVjDwbx0mC8gYx-b/images/integrations/diffusers-autolog-6.gif?s=17cbafa1416ec671cc78dd36f60915fa" alt="Stable Diffusion XL experiment tracking" width="800" height="418" data-path="images/integrations/diffusers-autolog-6.gif" />
  </Frame>

## More resources

* [A Guide to Prompt Engineering for Stable Diffusion](https://wandb.ai/geekyrakshit/diffusers-prompt-engineering/reports/A-Guide-to-Prompt-Engineering-for-Stable-Diffusion--Vmlldzo1NzY4NzQ3)
* [PIXART-α: A Diffusion Transformer Model for Text-to-Image Generation](https://wandb.ai/geekyrakshit/pixart-alpha/reports/PIXART-A-Diffusion-Transformer-Model-for-Text-to-Image-Generation--Vmlldzo2MTE1NzM3)
