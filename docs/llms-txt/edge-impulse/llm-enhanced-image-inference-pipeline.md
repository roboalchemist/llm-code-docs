# Source: https://docs.edgeimpulse.com/projects/expert-network/llm-enhanced-image-inference-pipeline.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Edge Intelligence Pipeline: LLM-Enhanced Interpretation of Embedded ML Inference

Created By: Haziqa Sajid

***

## Introduction

Out of [millions of images from automated wildlife cameras](https://beerys.github.io/assets/papers/EfficientPipeline.pdf), most (∼50–70%) contain no animals. Manually sorting this flood of "false positive" frames is a huge bottleneck. Edge AI models running on a device can incorrectly flag frames as "animal" or "no animal" for a variety of reasons, such as vegetation movement, shadows, or blurry motion for wildlife when confidence scores are low.

To fix this, we will create an **edge intelligence pipeline**: first, run a lightweight image classifier on-device using Edge Impulse to generate binary predictions with confidence. Then, feed each prediction, along with its context, into a local LLM. The LLM "reasoning" uses temporal and spatial clues to decide if a detection is likely real. In practice, this triage frames into high-priority (true wildlife), low-priority (doubtful), or auto-reject, vastly reducing manual review effort.

## Problem Overview

Camera traps are motion- or heat-activated cameras used by biologists to monitor animal populations and behavior. When triggered, they capture image sequences at about one frame per second, but often produce empty frames due to false triggers from wind or ground heat.

* **High false-positive rate**: Camera traps trigger on wind, heat, or moving shadows, so a large majority of images are empty. For example, one survey found \~70% of camera-trap photos contained no animals. Scientists waste many hours scrolling past leaves or grass.

* **Limited signals**: A raw edge inference score (e.g., "animal" at 67% confidence) isn't enough. Low-to-medium confidence cases (e.g, distant or partially seen deer) are ambiguous, and simple thresholds can't distinguish a real animal from, say, rustling bush.

* **No context**: Pure vision classifiers ignore sequence and location patterns. They don't know that the same camera just saw an animal 30 seconds ago, or that it's been triggered every dusk in the past week. These clues could turn a so-so score into a "likely true event" or vice versa.

In short, the traditional workflow (detect on edge, then human reviews everything above a threshold) wastes time on noise. We need an *automated contextual triage layer* that filters out clear false alarms and highlights the truly interesting events for expert review.

## Architecture

The system uses a two-tier inference architecture that processes images captured by the camera. In the first stage, a lightweight edge model classifies each image as either containing an animal or not. Images with confidence scores near the decision threshold are then passed to a second stage, where an LLM evaluates the detection using contextual information and determines whether it represents a genuine animal event or a false positive.

<Frame caption="Architecture of a Two-Tier Inference System for Image Classification">
  <img src="https://mintcdn.com/edgeimpulse/WzdXAJFerapJTBFE/.assets/images/llm-enhanced-image-inference-pipeline/01.jpg?fit=max&auto=format&n=WzdXAJFerapJTBFE&q=85&s=0b310384c022f700cda6dfac1d5bf043" width="2048" height="702" data-path=".assets/images/llm-enhanced-image-inference-pipeline/01.jpg" />
</Frame>

Here's the elaborated workflow:

* **Dataset**: We use the [WCS Camera Traps dataset](https://huggingface.co/datasets/society-ethics/lila_camera_traps) (∼1.4M images, 675 species, 12 countries). It includes every image's timestamp, camera ID/location, and (for many) species labels. Roughly half the images are empty, providing abundant negative examples. This rich metadata lets us simulate and test our pipeline logic on real-world data.

* **Edge Inference Layer**: We train a simple **binary classifier** (animal vs. no-animal) using Edge Impulse. In practice, this runs on the Pi to flag images. For this article, we simulate its outputs: each image gets a "predicted class" and a confidence score. In a real setup, you'd deploy the model to your camera hardware or edge device.

* **LLM Interpretation**: We run a [local LLM](https://ollama.com/library/gemma3:4b#:~:text=Gemma%20is%20a%20lightweight%2C%20family,limited%20devices) (Gemma 3 4B via Ollama) on the same device. Gemma is multimodal and supports long context. For each detection, we send a prompt combining the model's label/confidence *and* the image's metadata (time, camera, recent history). Gemma3 then reasons about it – e.g., if the prediction is uncertain and no animal was seen nearby in time, it may label it a false trigger; if confidence is high and similar frames triggered recently, it flags a genuine event. Using an LLM like this adds temporal/spatial intelligence that fixed ML models lack.

This article focuses on the following aspects and intentionally excludes others.

**In-Scope**: Contextual false-positive filtering; using time/space metadata to spot patterns (e.g., repeated triggers at one camera); and automatically prioritizing images for review. We focus on the software pipeline (data prep, model training, on-device inference, and LLM triage logic).

**Out-of-Scope**: We do not cover specialized hardware or firmware details for actual camera traps (e.g., writing embedded C on a microcontroller). We won't improve the species classifier beyond a simple animal/no-animal model. Also, coordinating inference across multiple cameras or networks is left for future work. Our goal here is to illustrate the core pipeline on one device with one camera's data.

In the next stage, we will prepare our Edge Impulse image classification model and deploy it on a Raspberry Pi.

## Implementation

This section is divided into two parts. The first part is relevant to the simple classifier model using Edge Impulse.  Let's start with the setup:

### Edge Impulse Project Setup

First, create a new Edge Impulse project in the Edge Impulse Studio. Log in to Edge Impulse Studio and make a new project:

<Frame caption="Creating a New Project in Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/WzdXAJFerapJTBFE/.assets/images/llm-enhanced-image-inference-pipeline/02.jpg?fit=max&auto=format&n=WzdXAJFerapJTBFE&q=85&s=fdf805047c7a2b1b77fd0b4027d09ff2" width="600" height="800" data-path=".assets/images/llm-enhanced-image-inference-pipeline/02.jpg" />
</Frame>

Once set up, open the **Data acquisition** tab in the Studio. Here, you define how to upload the dataset.

### Building Your Camera Trap Image Dataset

The WCS Camera Traps dataset contains images captured by motion-triggered wildlife cameras, including both true animal detections and a large number of empty or false-trigger frames. For this work, we use the Hugging Face–hosted **LILA Camera Traps dataset**, which provides structured annotations and direct image URLs, avoiding manual JSON parsing. The dataset is loaded using the `datasets` library with the *Caltech Camera Traps* configuration. Here's the code snippet:

```
from datasets import load_dataset
import os
import requests
from PIL import Image
from io import BytesIO

# Output directories
OUTPUT_DIR = "edge_impulse_dataset"
ANIMAL_DIR = os.path.join(OUTPUT_DIR, "animal")
NO_ANIMAL_DIR = os.path.join(OUTPUT_DIR, "no_animal")

os.makedirs(ANIMAL_DIR, exist_ok=True)
os.makedirs(NO_ANIMAL_DIR, exist_ok=True)

MAX_ANIMAL = 50
MAX_NO_ANIMAL = 50

animal_count = 0
no_animal_count = 0

# Load dataset
dataset = load_dataset("society-ethics/lila_camera_traps",
                       "Caltech Camera Traps",
                       split="train")

def download_image(url):
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return Image.open(BytesIO(r.content)).convert("RGB")

def is_non_animal(taxonomy: dict) -> bool:
    return all(v is None for v in taxonomy.values())

for sample in dataset:
    if animal_count >= MAX_ANIMAL and no_animal_count >= MAX_NO_ANIMAL:
        break

    annotations = sample.get("annotations")
    image_url = sample.get("image")

    if not annotations or not image_url:
        continue

    taxonomy_list = annotations.get("taxonomy")
    if not taxonomy_list or len(taxonomy_list) == 0:
        continue

    taxonomy = taxonomy_list[0]
    try:
        image = download_image(image_url)
    except Exception:
        continue

    if is_non_animal(taxonomy):
        if no_animal_count < MAX_NO_ANIMAL:
            image.save(
                os.path.join(NO_ANIMAL_DIR, f"no_animal_{no_animal_count}.jpg")
            )
            no_animal_count += 1
    else:
        if animal_count < MAX_ANIMAL:
            image.save(
                os.path.join(ANIMAL_DIR, f"animal_{animal_count}.jpg")
            )
            animal_count += 1
```

Each sample includes:

* *image*: URL of the camera trap image
* *annotations.taxonomy*: A taxonomy dictionary describing biological classification
* *seq\_id / frame\_num*: Sequence and temporal metadata (not used at this stage)

The taxonomy field spans multiple biological levels (kingdom → species). These annotations are used to derive binary labels. The dataset does not explicitly label empty frames. Instead, animal presence is inferred from taxonomy annotations:

* *No-animal*: All taxonomy fields are `None`
* *Animal*: At least one taxonomy field is populated

The code above will create a directory including the images of the animal and the non-animal that can then be uploaded to Edge Impulse. Here are some examples of the images:

<Frame caption="The left column shows images of animals, while the right column shows images of non-animals.">
  <img src="https://mintcdn.com/edgeimpulse/WzdXAJFerapJTBFE/.assets/images/llm-enhanced-image-inference-pipeline/03.jpg?fit=max&auto=format&n=WzdXAJFerapJTBFE&q=85&s=22ae815c52e5868bf277b171db0bb55f" width="870" height="658" data-path=".assets/images/llm-enhanced-image-inference-pipeline/03.jpg" />
</Frame>

Now, in your **Data Acquisition** tab, upload the dataset:

<Frame caption="Uploading the Dataset on Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/WzdXAJFerapJTBFE/.assets/images/llm-enhanced-image-inference-pipeline/04.jpg?fit=max&auto=format&n=WzdXAJFerapJTBFE&q=85&s=09e5775bebb0b7838f4883e8e39e0f02" width="1137" height="906" data-path=".assets/images/llm-enhanced-image-inference-pipeline/04.jpg" />
</Frame>

By selecting the label, we can easily assign each image a binary label (Animal / No-animal). Even a partially visible antelope or blurred bird should count as "animal" if the ML is to catch it; adjust your rules consistently.

Since the dataset may contain challenging or ambiguous animal images, these can be filtered out. The model's primary task is to classify images as *animal* or *non-animal*. Any hard-to-classify images can be passed to a second stage for further verification. By iterating on the dataset in Studio, you increase the model's ability to learn clear and reliable distinctions.

### Image Processing Pipeline Design

Once the dataset is prepared and labeled, the next step is to design the Impulse using the **Impulse Design** tab. Here's how our design looks:

<Frame caption="The Image Processing and Classification Impulse Design">
  <img src="https://mintcdn.com/edgeimpulse/WzdXAJFerapJTBFE/.assets/images/llm-enhanced-image-inference-pipeline/05.jpg?fit=max&auto=format&n=WzdXAJFerapJTBFE&q=85&s=d830bd0e98a47ac095077a1637a04e4b" width="1692" height="791" data-path=".assets/images/llm-enhanced-image-inference-pipeline/05.jpg" />
</Frame>

In the first block of the Impulse, we preprocess the image.

* **Processing block**: Configure the input dimensions to balance accuracy and speed: for a Raspberry Pi, 96×96 or 128×128 pixels is a good start. Choose RGB color unless you find that grayscale actually helps by reducing background color noise.

* **Configuration**: Click on the Images block and check the raw input vs. the processed output. You can toggle between RGB and grayscale to compare. In our case, we left color depth at RGB and clicked **Save parameters**.

<Frame caption="Configuring the Color Depth and Saving Parameters">
  <img src="https://mintcdn.com/edgeimpulse/WzdXAJFerapJTBFE/.assets/images/llm-enhanced-image-inference-pipeline/06.jpg?fit=max&auto=format&n=WzdXAJFerapJTBFE&q=85&s=2e8e340b025a6821f71b65778f768324" width="864" height="474" data-path=".assets/images/llm-enhanced-image-inference-pipeline/06.jpg" />
</Frame>

This step ensures that every image will be cropped/resized the same way on the device.

* **Normalization**: The Images block automatically normalizes pixel values (0–1) and resizes the images. You generally don't need custom code here; Edge Impulse handles it.

After configuring the block, click **Generate features**. Edge Impulse will extract the image features for all samples. The *Feature Explorer* (next step) will give you a 3D plot of these features. Here's what it looks like for ours:

<Frame caption="Feature Explorer on the Animal vs Not-Animal Dataset">
  <img src="https://mintcdn.com/edgeimpulse/WzdXAJFerapJTBFE/.assets/images/llm-enhanced-image-inference-pipeline/07.jpg?fit=max&auto=format&n=WzdXAJFerapJTBFE&q=85&s=13ebbafb5eab2bb5bfd8310c57cff0d0" width="848" height="550" data-path=".assets/images/llm-enhanced-image-inference-pipeline/07.jpg" />
</Frame>

Use the resulting plot to review the features generated. You can learn more about the Feature Explorer [here](https://docs.edgeimpulse.com/studio/projects/processing-blocks/feature-explorer). If a feature appears incorrect, go back and adjust the width/height or enable extra processing.

### Neural Network Training and Optimization

After generating the features of the images, we will now train the classifier. Here are the steps:

**Choose a model**: We used transfer learning on MobileNetV2 with a lightweight CNN suited for edge devices. Edge Impulse makes this easy with its *Transfer Learning (Images)* block. These models are already trained on general images, so we only retrain the last layers on "animal vs. not animal."

**Training parameters**: In Edge Impulse's Transfer Learning settings, set a reasonable number of epochs (e.g., 50 cycles) and a learning rate around 0.0005. You can enable **Data augmentation** here to help generalize the dataset if needed. Monitor the training accuracy vs. validation accuracy; if the model quickly overfits (train >> val), try fewer epochs or stronger augmentation.

**Evaluate performance**: After training, Edge Impulse shows the final accuracy and a confusion matrix.

<Frame caption="Results & Confusion Matrix of the Model on the Validation Set">
  <img src="https://mintcdn.com/edgeimpulse/WzdXAJFerapJTBFE/.assets/images/llm-enhanced-image-inference-pipeline/08.jpg?fit=max&auto=format&n=WzdXAJFerapJTBFE&q=85&s=fa4728ee6eb1be76c2ccd4398314f6ae" width="864" height="574" data-path=".assets/images/llm-enhanced-image-inference-pipeline/08.jpg" />
</Frame>

The confusion matrix will tell you if there are still many false positives (no-animal labeled as animal) – if so, consider raising the decision threshold.

**Refine**: If needed, tweak epochs or try a smaller model (Edge Impulse suggests a smaller base if your device is RAM-limited). Check each species or background separately. In short, use the standard ML loop: train, evaluate, analyze errors, and adjust. Edge Impulse's UI helps here by showing mistakes and letting you easily iterate.

In our case, we got a very good accuracy and a bearable loss in our first run. You could further improve this by adding more epochs and data.

### Model Testing and Validation

This is sort of the final test of the model. The test is on the hold-out Testing set. Use Edge Impulse's built-in testing tools to run the trained model on all your test images. It will display overall accuracy and per-class error rates. Focus on the false-positive rate: what percentage of empty frames are still wrongly flagged as "animal"? A high false-positive rate means too much manual review, so our goal is to minimize it, even if it costs a few more false negatives. Here are some tips and features of Edge Impulse to help improve your score:

**Cross-condition checks**: If you have data from different cameras or times, test on those. For instance, take a batch of images from a forest site in the rainy season (the WCS Camera Trap dataset has a lot of images) and see how the model performs. This checks generalization.

**Metrics report**: Record key metrics (precision, recall) for both classes. Edge Impulse provides them in the UI. You might export these or take screenshots of the confusion matrix. This report establishes a baseline.

**Iterate if needed**: If the model misses too many animals or flags too many blanks, go back and improve data/augmentation. For example, increase the animal confidence threshold to reduce false alarms. Retrain and retest until you're satisfied that the on-device model is reasonably solid.

After this step, you will have a simple classification model ready to be deployed on a Raspberry Pi.

## Deployment to Raspberry Pi

For deployment, go to Edge Impulse Studio, go to *Deployment → Linux AARCH64*. Build the "Impulse" for Linux; it will generate a downloadable `.eim` file containing your model.

<Frame caption="Deployment of the Model by Building it for Linux(AARCH64)">
  <img src="https://mintcdn.com/edgeimpulse/WzdXAJFerapJTBFE/.assets/images/llm-enhanced-image-inference-pipeline/09.jpg?fit=max&auto=format&n=WzdXAJFerapJTBFE&q=85&s=ab88151bc74002ed1af36e6f9fb693d2" width="954" height="851" data-path=".assets/images/llm-enhanced-image-inference-pipeline/09.jpg" />
</Frame>

Copy this package to the Pi or use the Edge Impulse Linux runner directly on the Pi to download the model file. Simply open a terminal on the Pi and run:

```
edge-impulse-linux-runner
```

This utility fetches the latest built model from your project and starts inference using an attached camera. As it runs, it will print each image's predicted label and confidence. This uses minimal CPU and no internet, so it runs fully offline.

As we will be using this in our pipeline, we will be using the Linux Python SDK of Edge Impulse. This step is the input to the next stage, the LLM reasoning. So let's work on setting up the LLM part of this pipeline.

## Setting up the LLM

Ensure the Raspberry Pi has Python 3.9+ installed. Install Ollama (a local LLM runner) by running their install script:

```
sudo apt update && sudo apt install -y curl
curl -fsSL https://ollama.com/install.sh | sh
ollama --version  # verify installation
```

This gives you the `ollama` command-line tool and background service. For the model, pull or run the quantized Gemma 4B model. For instance:

```
ollama install gemma3:4b-it-qat
```

Then you can start it with:

```
ollama run gemma3:4b-it-qat
```

The QAT version is crucial: it uses 4-bit quantization and takes only \~3.3 GB of memory, which fits comfortable on an 8GB or 16GB Raspberry Pi 5. Gemma3-4B is "multimodal" (text+image) and has a [128K token context](https://ollama.com/library/gemma3:4b#:~:text=Gemma%20is%20a%20lightweight%2C%20family,limited%20devices), so it's well-suited for our rich prompts.

In your Python environment on the Pi, install the necessary libraries:

```
pip3 install requests pandas
```

We'll use `requests` to talk to Ollama's local API, and `pandas` to handle the metadata.

At this point, the Pi has the LLM ready to serve. Ollama runs an HTTP API on localhost (port 11434 by default) that mimics OpenAI's Chat API. This lets us do [prompt-driven tasks on-device](https://mlsysbook.ai/contents/labs/raspi/llm/llm.html#:~:text=This%20lab%20will%20guide%20you,least%20point%20in%20this%20direction) with privacy and no internet connection. In summary, we have a local ML model (Edge Impulse) producing outputs, and a local LLM (Gemma) ready to process text prompts – all offline.

## Running the Two-Tier Edge–LLM Inference Pipeline

Once the Edge Impulse model is trained and downloaded, inference runs entirely on a Linux device such as a Raspberry Pi using the Edge Impulse Linux Python SDK. The edge model performs fast animal detection, and only uncertain predictions are forwarded to a local LLM running via Ollama.

### Set up for Linux Python SDK

Some libraries required by the SDK (e.g., for audio or cameras) need native Linux packages first. On the Raspberry Pi:

```
sudo apt update
sudo apt install libatlas-base-dev libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev python3-pip
```

After the packages are installed, install `edge-impulse-linux`:

```
pip install edge-impulse-linux
```

This installs the Python package that lets you load and run your `.eim` model in Python. To download the .eim onto your Pi, run the following on the CLI if you did not already do so earlier in this tutorial:

```
edge-impulse-linux-runner --download modelfile.eim
```

The following script shows the complete pipeline in one place: loading the Edge Impulse model, running image classification, and conditionally invoking Gemma-4B through Ollama.

```
from edge_impulse_linux.image import ImageImpulseRunner
from PIL import Image
import requests
import base64
from io import BytesIO

MODEL_PATH = "./modelfile.eim"
IMAGE_PATH = "./test_image.jpg"
OLLAMA_URL = "http://localhost:11434/api/chat"  # Use /api/chat for conversational format

LOW_CONF = 0.45
HIGH_CONF = 0.75

def image_to_base64(image_path):

    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def run_llm_with_image(confidence, label, image_path):

        prompt = f"""An edge ML model detected '{label}' with confidence {confidence:.2f} in this wildlife camera trap image.

CONTEXT: Camera trap images often have challenging conditions like motion blur, partial occlusion by vegetation, low light, animals at image edges, or animals partially hidden behind objects. These are VALID detections.

Your task: Determine if there is actually an animal present in this image, even if barely visible.

Respond with:
1. YES - if you can identify ANY animal presence, including:
   - Blurry or motion-blurred animals
   - Partially visible animals (only head, tail, or body parts visible)
   - Animals obscured by vegetation, branches, or terrain
   - Animals at the edge of the frame
   - Animals in low light or nighttime conditions
   - Distant or small animals in the scene

2. NO - if this is a false positive with NO animal present, such as:
   - Only shadows, light patterns, or lens flares
   - Only vegetation moving in wind
   - Inanimate objects misidentified as animals
   - Empty scenes with no animal indicators

3. UNCERTAIN - only if the image quality is so degraded that you cannot make any determination

IMPORTANT: Err on the side of YES if you detect any animal indicators (shape, eyes, fur texture, limbs, movement patterns) even if unclear.

Provide: Your verdict (YES/NO/UNCERTAIN) followed by a brief explanation of what you observed and why you made that determination."""

    # Encode image as base64
    img_base64 = image_to_base64(image_path)
    
    payload = {
        "model": "gemma3:4b-it-qat",
        "messages": [
            {
                "role": "user",
                "content": prompt,
                "images": [img_base64]
            }
        ],
        "stream": False
    }
    
    r = requests.post(OLLAMA_URL, json=payload, timeout=60)
    return r.json()["message"]["content"]

with ImageImpulseRunner(MODEL_PATH) as runner:
    runner.init()
    image = Image.open(IMAGE_PATH).convert("RGB")
    features, _ = runner.get_features_from_image(image)
    result = runner.classify(features)
    
    scores = result["result"]["classification"]
    label = max(scores, key=scores.get)
    confidence = scores[label]
    
    print(f"Edge result: {label} ({confidence:.2f})")
    
    if confidence < LOW_CONF:
        print("Decision: auto-reject (confidence too low)")
    elif confidence > HIGH_CONF:
        print("Decision: auto-accept (confidence high)")
    else:
        print("Decision: LLM verification needed")
        
        # Try with image first (requires vision model)
        try:
            explanation = run_llm_with_image(confidence, label, IMAGE_PATH)
            print("\n--- LLM Verification ---")
            print(explanation)
        except Exception as e:
            print(f"Vision model failed: {e}")
            print("Could not verify image content.")
```

The edge model produces a confidence score for the animal vs no-animal classification. Clear negatives are rejected immediately, and clear positives are accepted without further processing. Only borderline predictions are passed to the LLM, which interprets the uncertainty and assigns a review priority. Here's the result of the complete pipeline.

For example, for this image, the model gave it a 0.43 chance of being an animal, which is on the borderline:

<Frame caption="False Positive Classification of the Animal">
  <img src="https://mintcdn.com/edgeimpulse/WzdXAJFerapJTBFE/.assets/images/llm-enhanced-image-inference-pipeline/10.jpg?fit=max&auto=format&n=WzdXAJFerapJTBFE&q=85&s=148b0578160eab2298d8ddf4daf094e6" width="864" height="770" data-path=".assets/images/llm-enhanced-image-inference-pipeline/10.jpg" />
</Frame>

The pipeline will send this image to the Gemma-4b model. Here's the response from the model:

```
> YES - There appears to be a small, blurry animal partially obscured by vegetation in the center of the image. While it's difficult to make out specific details, the general shape and some discernible fur texture suggest the presence of an animal, even if it's only partially visible and somewhat blurry due to motion and occlusion.
```

It worked as planned. This completes the pipeline: raw images → edge inference → LLM reasoning → final categorization.

## Conclusion

By adding a local LLM interpretation layer, we transform a simple confidence score into a context-aware decision. The LLM can categorize the image as an animal if the scores are at the borderline. This approach substantially reduced the number of frames flagged for human review.

In practice, this means researchers spend far less time on false alarms and can focus on the genuine wildlife sightings that matter. The metadata (temporal and spatial context) was the key: by leveraging it in prompts, the LLM effectively "understood" the situation.

## Sources

We drew on the [WCS Camera Traps dataset](https://huggingface.co/datasets/society-ethics/lila_camera_traps#:~:text=WCS%20Camera%20Traps) and [prior camera-trap ML research](https://beerys.github.io/CaltechCameraTraps/#:~:text=replace%20the%20batteries%20and%20change,trap%20research%20scalable%20and%20efficient). Edge Impulse documentation guided the [on-device ML setup](https://docs.edgeimpulse.com), and the recent [Gemma 4b model](https://ollama.com/library/gemma3:4b#:~:text=quantization%20Q4_K_M) was used for LLM deployment. All steps were implemented using open-source tools as described above.


Built with [Mintlify](https://mintlify.com).