# Source: https://docs.edgeimpulse.com/tutorials/topics/data/generate-image-data-dall-e.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate image data using Dall-E

<a href="https://colab.research.google.com/github/edgeimpulse/notebooks/blob/main/notebooks/generate-dall-e-image-dataset.ipynb" target="_blank">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Google Colab" noZoom />
</a>

This notebook explores how we can use generative AI to create datasets which don't exist yet. This can be a good starting point for your project if you have not collected or cannot collect the data required. It is important to note the limitations of generative AI still apply here, biases can be introduced through your prompts, results can include "hallucinations" and quality control is important.

This example uses the OpenAI API to call the Dall-E image generation tool, it explores both generation and variation but there are other tools such as editing which could also be useful for augmenting an existing dataset.

There is also a video version of this tutorial:

<iframe src="https://www.youtube.com/embed/PVDqlTuBzLc" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

We have wrapped this example into a [Transformation Block](/knowledge/guides/reference-designs/health-reference-design/transforming-clinical-data) (Enterprise Feature) to make it even easier to generate images and upload them to your organization. See: [https://github.com/edgeimpulse/example-transform-Dall-E-images](https://github.com/edgeimpulse/example-transform-Dall-E-images)

### Local Software Requirements

* Python 3
* Pip package manager
* Jupyter Notebook: [https://jupyter.org/install](https://jupyter.org/install)
* pip packages (install with `pip install`*`packagename`*):
  * openai [https://pypi.org/project/openai/](https://pypi.org/project/openai/)

```python  theme={"system"}
! pip install openai
```

```python  theme={"system"}
# Imports
import openai
import os
import requests

# Notebook Imports
from IPython.display import Image
from IPython.display import display
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
```

## Set up OpenAI API

First off you will need to set up and Edge Impulse account and create your first project.

You will also need to create an API Key for OpenAI: [https://platform.openai.com/docs/api-reference/authentication](https://platform.openai.com/docs/api-reference/authentication)

```python  theme={"system"}

# You can set your API key and org as environment variables in your system like this:
# os.environ['OPENAI_API_KEY'] = 'api string'

# Set up OpenAI API key and organization
openai.api_key = os.getenv("OPENAI_API_KEY")
```

### Generate your first image

The API takes in a prompt, number of images and a size

```python  theme={"system"}
image_prompt = "A webcam image of a human 1m from the camera sitting at a desk showing that they are wearing gloves with their hands up to the camera."
# image_prompt = "A webcam image of a person 1m from the camera sitting at a desk with their bare hands up to the camera."
# image_prompt = "A webcam image of a human 1m from the camera sitting at a desk showing that they are wearing wool gloves with their hands up to the camera."

response = openai.Image.create(
    prompt=image_prompt,
    n=1,
    size="256x256",
)
Image(url=response["data"][0]["url"])
```

### Generate some variations of this image

The API also has a variations call which takes in an existing images and creates variations of it. This could also be used to modify existing images.

```python  theme={"system"}
response2 = openai.Image.create_variation(
  image=requests.get(response['data'][0]['url']).content,
  n=3,
  size="256x256"
)
imgs = []
for img in response2['data']:
  imgs.append(Image(url=img['url']))

display(*imgs)
```

## Generate a dataset:

Here we are iterate through a number of images and variations to generate a dataset based on the prompts/labels given.

```python  theme={"system"}
labels = [{"prompt": "A webcam image of a human 1m from the camera sitting at a desk showing that they are wearing wool gloves with their hands up to the camera.",
          "label": "gloves"},
          {"prompt": "A webcam image of a person 1m from the camera sitting at a desk with their bare hands up to the camera.",
          "label": "no-gloves"}
        ]
output_folder = "output"
base_images_number = 10
variation_per_image = 3
# Check if output directory for noisey files exists and create it if it doesn't
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for option in labels:
    for i in range(base_images_number):
        response = openai.Image.create(
            prompt=option["prompt"],
            n=1,
            size="256x256",
        )
        try:
            img = response["data"][0]["url"]
            with open(f'{output_folder}/{option["label"]}.{img.split("/")[-1]}.png', 'wb+') as f:
                f.write(requests.get(img).content)
            response2 = openai.Image.create_variation(
                image=requests.get(img).content,
                n=variation_per_image,
                size="256x256"
            )
        except Exception as e:
            print(e)
        for img in response2['data']:
            try:
                with open(f'{output_folder}/{option["label"]}.{img["url"].split("/")[-1]}.png', 'wb') as f:
                    f.write(requests.get(img["url"]).content)
            except Exception as e:
                print(e)
```

### Plot all the output images:

```python  theme={"system"}
import os


# Define the folder containing the images
folder_path = './output'

# Get a list of all the image files in the folder
image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.png')]

# Set up the plot
fig, axs = plt.subplots(nrows=20, ncols=20, figsize=(10, 10))

# Loop through each image and plot it in a grid cell
for i in range(20):
    for j in range(20):
        img = mpimg.imread(os.path.join(folder_path, image_files[i*10+j]))
        axs[i,j].imshow(img)
        axs[i,j].axis('off')

# Make the plot look clean
fig.subplots_adjust(hspace=0, wspace=0)
plt.tight_layout()
plt.show()

```

<Frame caption="Images generated from the script">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/tutorial-generate-image-datasets.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=a5e41332d7ef2031216a816ef97bf428" alt="" width="989" height="990" data-path=".assets/images/tutorial-generate-image-datasets.png" />
</Frame>

These files can then be uploaded to a project with these commands (run in a separate terminal window):

```python  theme={"system"}
! cd output
! edge-impulse-uploader .
```

(run edge-impulse-uploader --clean if you have used the CLI before to reset the target project)

## What next?

Now you can use your images to create an image classification model on Edge Impulse.

Why not try some other OpenAI calls, 'edit' could be used to take an existing image and translate it into different environments or add different humans to increase the variety of your dataset. [https://platform.openai.com/docs/guides/images/usage](https://platform.openai.com/docs/guides/images/usage)


Built with [Mintlify](https://mintlify.com).