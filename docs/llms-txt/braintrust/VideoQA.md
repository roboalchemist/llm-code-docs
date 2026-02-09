# Source: https://braintrust.dev/docs/cookbook/recipes/VideoQA.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Evaluating video QA

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/VideoQA/VideoQA.ipynb) by [Adrian Barbir](https://www.linkedin.com/in/adrianbarbir/) on 2025-02-18</div>

Large language models have gotten extremely good at interpreting text, but understanding and answering questions about video content is a newer area of focus. It's especially difficult for domain-specific tasks, like sports broadcasts or educational videos, where specific visual details can completely change the answer.

In this cookbook, we'll explore how to evaluate an LLM-based video question-answering (Video QA) system using the [MMVU dataset](https://mmvu-benchmark.github.io/). The MMVU dataset includes multi-disciplinary videos paired with questions and ground-truth answers, spanning many different topics.

By the end, you'll have a repeatable workflow for quantitatively evaluating video QA performance, which you can adapt to different datasets or use cases.

## Getting started

To follow along, start by installing the required packages:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
pip install opencv-python requests datasets braintrust autoevals openai
```

Next, make sure you have a [Braintrust](https://www.braintrust.dev/signup) account, along with an [OpenAI API key](https://platform.openai.com/). To authenticate with Braintrust, export your `BRAINTRUST_API_KEY` as an environment variable:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
export BRAINTRUST_API_KEY="YOUR_API_KEY_HERE"
```

<Callout type="info">
  Exporting your API key is a best practice, but to make it easier to follow along with this cookbook, you can also hardcode it into the code below.
</Callout>

We'll import our modules, define constants, and initialize the OpenAI client using the Braintrust proxy:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import os
import base64
from typing import List, Dict, Any, Optional

import cv2
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from datasets import load_dataset

import braintrust
import autoevals
from openai import OpenAI


NUM_FRAMES = 32
TARGET_DIMENSIONS = (512, 512)
JPEG_QUALITY = 80

RETRY_TOTAL = 3
RETRY_BACKOFF = 0.5
STATUS_FORCELIST = [502, 503, 504]

# Uncomment the following line to hardcode your API key
# os.environ["BRAINTRUST_API_KEY"] = "YOUR_API_KEY_HERE"

client = braintrust.wrap_openai(
    OpenAI(
        api_key=os.environ["BRAINTRUST_API_KEY"],
        base_url="https://api.braintrust.dev/v1/proxy",
    )
)
```

## Extracting frames as base64

To give the LLM visual context, we'll extract up to `NUM_FRAMES` frames from each video, resize them to `TARGET_DIMENSIONS`, and encode each frame as a base64 string. This lets us include key snapshots of the video in the prompt:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def extract_frames_b64(video_path: str) -> List[str]:
    base64_frames = []
    count = 0
    video_capture = cv2.VideoCapture(video_path)

    try:
        while video_capture.isOpened() and count < NUM_FRAMES:
            ret, frame = video_capture.read()
            if not ret:
                break

            frame = cv2.resize(frame, TARGET_DIMENSIONS)
            success, encoded_img = cv2.imencode(
                ".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), JPEG_QUALITY]
            )
            if success:
                b64_str = base64.b64encode(encoded_img).decode("utf-8")
                base64_frames.append(b64_str)
            count += 1
    finally:
        # Ensure the capture is always released
        video_capture.release()

    return base64_frames
```

## Downloading or reading raw video data

Storing the raw video file as an attachment in Braintrust can simplify debugging by allowing you to easily reference the original source. The helper function `get_video_data` retrieves a video file either from a local path or URL:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def get_video_data(video_path: str, session: requests.Session) -> Optional[bytes]:
    try:
        if video_path.startswith("http"):
            response = session.get(video_path, timeout=10)
            response.raise_for_status()
            return response.content
        else:
            with open(video_path, "rb") as f:
                return f.read()
    except Exception as e:
        print(f"Error retrieving video data from {video_path}: {e}")
        return None
```

## Loading the data

We'll work with the first 20 samples from the MMVU validation split. Each sample contains a video, a question, and an expected answer. We'll convert the video frames to base64, attach the raw video bytes, and include the question-answer pair:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def load_data_subset() -> List[Dict[str, Any]]:
    ds = load_dataset("yale-nlp/MMVU", split="validation[:20]")

    session = requests.Session()
    retry = Retry(
        total=RETRY_TOTAL,
        backoff_factor=RETRY_BACKOFF,
        status_forcelist=STATUS_FORCELIST,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    data_list = []
    for row in ds:
        question_type = row["question_type"]
        video_path = row["video"]

        frames_b64 = extract_frames_b64(video_path)
        raw_video = get_video_data(video_path, session)

        choices_data = (
            row.get("choices") if question_type == "multiple-choice" else None
        )

        data_list.append(
            {
                "input": {
                    "frames_b64": frames_b64,
                    "question": row["question"],
                    "question_type": question_type,
                    "choices": choices_data,
                    "video_attachment": braintrust.Attachment(
                        filename=os.path.basename(video_path),
                        content_type="video/mp4",
                        data=raw_video,
                    ),
                },
                "expected": {"answer": row["answer"]},
                "metadata": {
                    "subject": row["metadata"]["subject"],
                    "textbook": row["metadata"]["textbook"],
                    "question_type": question_type,
                },
            }
        )

    session.close()
    return data_list
```

<img src="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/VideoQA/attachments.gif?s=fc5c4f5962b61a01e8c42ed3aac49e01" alt="attachments" data-og-width="1671" width="1671" data-og-height="959" height="959" data-path="cookbook/assets/VideoQA/attachments.gif" data-optimize="true" data-opv="3" />
In the Braintrust UI, you'll be able to see the raw video attachment, the base64 frames, and a preview of the analyzed frames.

## Prompting the LLM

Next, we'll define a `video_qa` function to prompt the LLM for answers. It constructs a prompt with the base64-encoded frames, the question, and, for multiple-choice questions, the available options:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def video_qa(input_dict: Dict[str, Any]) -> str:
    frames_b64 = input_dict["frames_b64"]
    question = input_dict["question"]
    question_type = input_dict.get("question_type", "open-ended")
    choices_data = input_dict.get("choices")

    content_blocks = [
        {
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{b64}", "detail": "low"},
        }
        for b64 in frames_b64
    ]

    if question_type == "multiple-choice" and choices_data:
        if isinstance(choices_data, dict):
            options_text = "\n".join(
                f"{key}: {value}" for key, value in choices_data.items()
            )
        else:
            options_text = "\n".join(
                f"{chr(65 + i)}: {option}" for i, option in enumerate(choices_data)
            )
        prompt_text = (
            f"You just saw {NUM_FRAMES} frames from a video. Based on what you see, "
            f"answer the following question: {question}.\n\n"
            f"Here are your options:\n{options_text}\n"
            "Choose the correct option in the format 'answer: X'. If uncertain, guess. You MUST pick something."
        )
    else:
        prompt_text = (
            f"You just saw {NUM_FRAMES} frames from a video. "
            f"Answer the following question: {question}.\n"
            "If uncertain, guess. Provide the best possible answer. You MUST answer to the best of your ability."
        )

    content_blocks.append({"type": "text", "text": prompt_text})

    messages = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": (
                        "You are a helpful assistant. Provide an answer even if you are uncertain."
                    ),
                }
            ],
        },
        {"role": "user", "content": content_blocks},
    ]

    response = client.chat.completions.create(model="gpt-4o", messages=messages)
    return response.choices[0].message.content
```

## Evaluating the model's answers

To evaluate the model's answers, we'll define a function called `evaluator` that uses the `LLMClassifier` from the [autoevals](https://github.com/braintrustdata/autoevals?tab=readme-ov-file#custom-evaluation-prompts) library as a starting point. This scorer compares the model's output with the expected answer, assigning 1 if they match and 0 otherwise.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
evaluator = autoevals.LLMClassifier(
    name="evaluator",
    prompt_template=(
        "You are a judge evaluating a model's ability to answer a question "
        f"based on {NUM_FRAMES} frames in a video.\n\n"
        "Model's answer:\n{{output}}\n\n"
        "Expected answer:\n{{expected.answer}}\n\n"
        "Is the model's answer correct? (Y/N)? Only Y or N."
    ),
    choice_scores={"Y": 1, "N": 0},
    use_cot=True,
)
```

### Running the evaluation

Now that we have the three required components (a dataset, task, and prompt), we can run the eval. It loads data using`load_data_subset`, uses `video_qa` to get answers from the LLM, and scores each response with `evaluator`:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
await braintrust.EvalAsync(
    "mmvu_eval_32images",
    data=load_data_subset,
    task=video_qa,
    scores=[evaluator],
    metadata={"model": "gpt-4o"},
    experiment_name="mmvu_eval_32images",
)
```

## Analyzing results

After running the evaluation, head over to **Evaluations** in the Braintrust UI to see your results. Select your most recent experiment to review the video frames included in the prompt, the model's answer for each sample, and the scoring by our LLM-based judge. We also attached metadata like `subject` and `question_type`, which you can use to filter in the Braintrust UI. This makes it easy to see whether the model underperforms on a certain type of question or domain. If you discover specific weaknesses, consider refining your prompt with more context or switching models.

<img src="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/VideoQA/filters.gif?s=43eb3da05c020003181673540b7b90f4" alt="Filtering" data-og-width="1671" width="1671" data-og-height="959" height="959" data-path="cookbook/assets/VideoQA/filters.gif" data-optimize="true" data-opv="3" />

## Next steps

* Learn more about the [MMVU dataset](https://mmvu-benchmark.github.io/)
* Add [custom scorers](/evaluate/write-scorers#custom-scorers) to get more granular feedback (like partial credit, or domain-specific checks)
* Check out our [prompt chaining agents cookbook](/cookbook/recipes/PromptChaining) if you're building complex AI systems where video classification is just one component
