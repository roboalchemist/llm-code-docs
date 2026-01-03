# Source: https://braintrust.dev/docs/cookbook/recipes/WebAgent.md

# Evaluating a web agent

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/WebAgent/WebAgent.ipynb) by [Ornella Altunyan](https://twitter.com/ornelladotcom), [Adrian Barbir](https://www.linkedin.com/in/adrianbarbir/) on 2025-03-08</div>

Web navigation can be tricky for AI agents because they need to understand webpage layouts, visual elements, and remember previous steps to take the right actions. This cookbook focuses on how models decide what to do next, like clicking buttons, entering text, or choosing dropdown options.

We'll use the [Multimodal-Mind2Web dataset](https://osu-nlp-group.github.io/Mind2Web/), which combines screenshots and HTML, to help models make better decisions. We'll also discuss how to apply these lessons beyond just this dataset. By the end, you'll have a clear framework for testing how well your AI navigates websites and finding ways to improve it.

## Getting started

To follow along, start by installing the required packages:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
%pip install lxml openai datasets pillow braintrust autoevals
```

Next, make sure you have a [Braintrust](https://www.braintrust.dev/signup) account, along with an [OpenAI API key](https://platform.openai.com/). To authenticate with Braintrust, export your `BRAINTRUST_API_KEY` as an environment variable:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
export BRAINTRUST_API_KEY="YOUR_API_KEY_HERE"
```

<Callout type="info">
  Exporting your API key is a best practice, but to make it easier to follow along with this cookbook, you can also hardcode it into the code below.
</Callout>

We'll import our modules and initialize the OpenAI client using the Braintrust proxy:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import os
import json
import base64
import re
import time
from typing import Dict, Any, List, Optional, Tuple

from lxml import etree
import openai
from datasets import load_dataset
from PIL import Image
from io import BytesIO

from braintrust import (
    Eval,
    Attachment,
    start_span,
    wrap_openai,
)

# Constants
MAX_SAMPLES = 50
HTML_MAX_ELEMENTS = 50
MAX_PREVIOUS_ACTIONS = 3

# Uncomment the following line to hardcode your API key
# os.environ["BRAINTRUST_API_KEY"] = "YOUR_API_KEY_HERE"

client = wrap_openai(
    openai.OpenAI(
        api_key=os.environ.get("BRAINTRUST_API_KEY"),
        base_url="https://api.braintrust.dev/v1/proxy",
    )
)
```

## Approaches to web navigation

There are a few ways AI models can navigate websites:

* HTML-only: Uses page structure but misses visual details.
* Screenshot-only: Captures visuals but misses interaction details.
* Multimodal: Combines HTML structure and screenshots for better decisions.

In this cookbook, we'll use the multimodal approach, combining HTML DOM structure and screenshots.

## Processing screenshots

First, let's write a function that converts screenshots of a given webpage into a format that we can use to pass to our model and [attach to our eval](/core/experiments/write#attachments).

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def process_screenshot(screenshot_input: Any) -> Optional[Attachment]:
    with start_span(name="process_screenshot") as span:
        try:
            # Handle PIL Image
            if isinstance(screenshot_input, Image.Image):
                img_byte_arr = BytesIO()
                screenshot_input.save(img_byte_arr, format="PNG")
                image_data = img_byte_arr.getvalue()

            # Handle file path
            elif isinstance(screenshot_input, str) and os.path.exists(screenshot_input):
                with open(screenshot_input, "rb") as f:
                    image_data = f.read()

            # Handle bytes
            elif isinstance(screenshot_input, bytes):
                image_data = screenshot_input

            # Handle dictionary with base64 data
            elif isinstance(screenshot_input, dict) and "data" in screenshot_input:
                data = screenshot_input["data"]
                if not isinstance(data, str):
                    return None

                # Process base64 data
                if data.startswith("data:image"):
                    base64_data = data.split(",", 1)[1]
                elif data.startswith("/9j/") or data.startswith("iVBOR"):
                    base64_data = data
                else:
                    return None

                image_data = base64.b64decode(base64_data)
            else:
                return None

            # Create attachment
            result = Attachment(
                data=image_data,
                filename="screenshot.png",
                content_type="image/png",
            )

            return result

        except Exception:
            return None
```

Next, we'll identify and summarize important HTML elements on the webpage, making it easier for the model to quickly understand page structure:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def get_enhanced_tree_summary(
    html_content: str, max_items: int = HTML_MAX_ELEMENTS
) -> str:
    with start_span(name="html_parsing") as span:
        if not html_content:
            return "No HTML content provided"

        try:
            # Parse HTML
            parser = etree.HTMLParser()
            dom_tree = etree.fromstring(html_content, parser)

            # XPath for interactive elements, sorted by relevance
            xpath_queries = [
                "//button | //input[@type='submit'] | //input[@type='button']",
                "//a[@href] | //*[@role='button'] | //*[@onclick]",
                "//input[not(@type='hidden')] | //select | //textarea",
                "//label | //form",
                "//h1 | //h2 | //h3 | //nav | //*[@role='navigation']",
            ]

            # Collect elements by priority until max_items is reached
            important_elements = []
            for query in xpath_queries:
                if len(important_elements) >= max_items:
                    break
                elements = dom_tree.xpath(query)
                remaining_slots = max_items - len(important_elements)
                important_elements.extend(elements[:remaining_slots])

            # Create a concise representation
            summary = []
            for elem in important_elements:
                tag = elem.tag

                # Get text content, limited to 30 chars
                text = elem.text.strip() if elem.text else ""
                if not text:
                    for child in elem.xpath(".//text()"):
                        if child.strip():
                            text += " " + child.strip()
                text = text.strip()[:30]

                # Get key attributes
                key_attrs = [
                    "id",
                    "type",
                    "placeholder",
                    "href",
                    "role",
                    "aria-label",
                    "value",
                    "name",
                ]
                attrs = []
                for k in key_attrs:
                    if k in elem.attrib:
                        attrs.append(f'{k}="{elem.attrib[k]}"')

                # Format element representation
                elem_repr = f"<{tag} {' '.join(attrs)}>{text}</{tag}>"
                summary.append(elem_repr)

            return "\n".join(summary)

        except Exception as e:
            return f"Error parsing HTML: {str(e)}"
```

## Keeping track of actions

Models perform better if they have context from previous steps. Without historical context, an agent might repeat actions or select incorrect next steps.

This function takes the latest few actions (up to `MAX_PREVIOUS_ACTIONS`) and neatly formats them for easy reference:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def format_previous_actions(
    actions: List[str], max_actions: int = MAX_PREVIOUS_ACTIONS
) -> str:
    if not actions:
        return "None"

    # Only take the most recent actions
    recent_actions = actions[-max_actions:]

    # Format with numbering
    formatted = "\n".join(
        [f"{i+1}. {action}" for i, action in enumerate(recent_actions)]
    )

    # Indicate if there were more actions before these
    if len(actions) > max_actions:
        formatted = (
            f"Showing {max_actions} most recent of {len(actions)} total actions\n"
            + formatted
        )

    return formatted
```

We also need a reliable way to convert raw action descriptions from our dataset into structured data our program can use. This function parses a provided action description and figures out the action type (`CLICK`, `TYPE`, or `SELECT`), and any associated values (like text typed):

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def parse_operation_string(operation_str: str) -> Dict[str, str]:
    with start_span(name="parse_operation") as span:
        # Default values
        operation = {"op": "CLICK", "value": ""}

        if not operation_str:
            return operation

        try:
            # Try parsing as JSON first
            if operation_str.strip().startswith("{"):
                parsed = json.loads(operation_str)
                if isinstance(parsed, dict):
                    operation["op"] = parsed.get("op", "CLICK")
                    operation["value"] = parsed.get("value", "")
            else:
                # Fallback to regex parsing
                import re

                match_op = re.search(r"(CLICK|TYPE|SELECT)", operation_str)
                if match_op:
                    operation["op"] = match_op.group(1)
                    match_value = re.search(
                        r'value\s*[:=]\s*["\']?([^"\']+)["\']?', operation_str
                    )
                    if match_value:
                        operation["value"] = match_value.group(1)
        except Exception:
            pass

        return operation
```

## Loading and preparing the dataset

Now that we've set up our helper functions, we can we load and process samples from the [Multimodal-Mind2Web dataset](https://huggingface.co/datasets/osunlp/Multimodal-Mind2Web):

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def load_mind2web_samples(
    max_samples: int = MAX_SAMPLES, use_smaller_subset: bool = True
) -> List[Dict[str, Any]]:

    # Load the dataset with streaming to conserve memory
    split = "test_domain" if use_smaller_subset else "train"
    dataset = load_dataset("osunlp/Multimodal-Mind2Web", split=split, streaming=True)

    processed_samples = []
    successful_samples = 0

    # Process samples
    for item in dataset:
        if successful_samples >= max_samples:
            break

        try:
            with start_span(name="process_sample") as sample_span:
                # Extract basic fields
                annotation_id = item.get(
                    "annotation_id", f"sample_{successful_samples}"
                )
                website = item.get("website", "unknown")
                confirmed_task = item.get("confirmed_task", "Navigate the website")
                cleaned_html = item.get("cleaned_html", "<html></html>")
                operation_str = item.get("operation", '{"op": "CLICK", "value": ""}')

                # Process operation
                operation = parse_operation_string(operation_str)

                # Process screenshot
                screenshot_attachment = None
                screenshot_dict = item.get("screenshot")
                if screenshot_dict:
                    screenshot_attachment = process_screenshot(screenshot_dict)

                # Process HTML summary
                html_summary = get_enhanced_tree_summary(
                    cleaned_html, max_items=HTML_MAX_ELEMENTS
                )

                # Process previous actions
                action_reprs = item.get("action_reprs", [])
                previous_actions_str = format_previous_actions(
                    action_reprs, max_actions=MAX_PREVIOUS_ACTIONS
                )

                # Map operation type to the correct option letter
                expected_option = "A"  # Default to CLICK
                if operation["op"] == "TYPE":
                    expected_option = "B"
                elif operation["op"] == "SELECT":
                    expected_option = "C"

                # Create a focused prompt
                formatted_prompt = f"""
                    Task: {confirmed_task}

                    Key webpage elements:
                    {html_summary}

                    Previous actions:
                    {previous_actions_str}

                    What should be the next action? Select from:
                    A. Click the appropriate element based on the task
                    B. Type text into an input field
                    C. Select an option from a dropdown
                    """

                # Build complete sample
                sample = {
                    "annotation_id": annotation_id,
                    "website": website,
                    "confirmed_task": confirmed_task,
                    "html_summary": html_summary,
                    "operation": operation,
                    "previous_actions_str": previous_actions_str,
                    "formatted_prompt": formatted_prompt,
                    "expected_option": expected_option,
                    "expected_action": operation["op"],
                    "expected_value": operation["value"],
                    "screenshot_attachment": screenshot_attachment,
                }

                processed_samples.append(sample)
                successful_samples += 1

        except Exception:
            continue

    return processed_samples
```

We'll transform these samples to a format that your model can easily use during evaluation. This function creates structured samples clearly separating inputs (task, screenshot) from expected actions for comparison during evaluation:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def create_braintrust_dataset(samples: List[Dict[str, Any]]) -> List[Dict[str, Any]]:

    dataset_samples = []

    for sample in samples:
        if not isinstance(sample, dict):
            continue

        # Extract operation details
        operation = sample.get("operation", {})
        operation_type = (
            operation.get("op", "CLICK") if isinstance(operation, dict) else "CLICK"
        )
        operation_value = (
            operation.get("value", "") if isinstance(operation, dict) else ""
        )

        # Create dataset entry
        dataset_entry = {
            "input": {
                "prompt": sample.get("formatted_prompt", ""),
                "task": sample.get("confirmed_task", ""),
                "website": sample.get("website", ""),
                "previous_actions": sample.get("previous_actions_str", "None"),
            },
            "expected": {
                "option": sample.get("expected_option", ""),
                "action": operation_type,
                "value": operation_value,
            },
            "metadata": {
                "annotation_id": sample.get("annotation_id", ""),
                "website": sample.get("website", ""),
                "operation_type": operation_type,
            },
        }

        # Add screenshot attachment if available
        if sample.get("screenshot_attachment"):
            dataset_entry["input"]["screenshot"] = sample["screenshot_attachment"]

        dataset_samples.append(dataset_entry)

    return dataset_samples
```

## Building the prediction function

Next, we'll build the prediction function that will send each formatted input to the model (`gpt-4o`) and retrieve the predicted action:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def predict_with_gpt4o(input_data: Dict[str, Any]) -> Dict[str, Any]:
    with start_span(name="model_prediction") as predict_span:
        try:
            # Extract input components
            prompt = input_data.get("prompt", "")
            screenshot_attachment = input_data.get("screenshot")

            # Create system message requesting JSON output
            system_message = """You are a web navigation assistant that helps users complete tasks online.
                Analyze the webpage and determine the best action to take next based on the task.

                You MUST respond with a valid JSON object with the following structure:
                {
                "option": "A, B, or C",
                "op": "CLICK, TYPE, or SELECT",
                "value": "Only provide value for TYPE/SELECT actions"
                }

                Option A corresponds to CLICK, B to TYPE, and C to SELECT.
                For CLICK operations, include an empty value field.

                Example for clicking:
                {"option": "A", "op": "CLICK", "value": ""}

                Example for typing:
                {"option": "B", "op": "TYPE", "value": "search query text"}

                Example for selecting:
                {"option": "C", "op": "SELECT", "value": "dropdown option"}
                """

            # Create messages array
            messages = [{"role": "system", "content": system_message}]

            # Add screenshot if available
            if screenshot_attachment and hasattr(screenshot_attachment, "data"):
                try:
                    image_data = screenshot_attachment.data
                    base64_image = base64.b64encode(image_data).decode("utf-8")

                    messages.append(
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/png;base64,{base64_image}"
                                    },
                                },
                                {"type": "text", "text": prompt},
                            ],
                        }
                    )
                except Exception:
                    messages.append({"role": "user", "content": prompt})
            else:
                messages.append({"role": "user", "content": prompt})

            # Request JSON output format
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                max_tokens=150,
                temperature=0.2,
                response_format={"type": "json_object"},  # This is critical!
            )

            result = response.choices[0].message.content

            # Parse JSON response
            try:
                structured_response = json.loads(result)

                # Ensure the required fields exist
                if "option" not in structured_response:
                    structured_response["option"] = ""
                if "op" not in structured_response:
                    structured_response["op"] = ""
                if "value" not in structured_response:
                    structured_response["value"] = ""

                return structured_response

            except json.JSONDecodeError as e:
                # If JSON parsing fails, try to extract data from text
                option_match = re.search(r"Answer:\s*([ABC])", result, re.IGNORECASE)
                action_match = re.search(
                    r"Action:\s*(CLICK|TYPE|SELECT)", result, re.IGNORECASE
                )
                value_match = re.search(r"Value:\s*(.+?)(?:\n|$)", result)

                option = option_match.group(1).upper() if option_match else ""
                action = action_match.group(1).upper() if action_match else ""
                value = value_match.group(1).strip() if value_match else ""

                # Convert to structured format
                return {
                    "option": option,
                    "op": action,
                    "value": value,
                    "error": f"JSON parsing failed: {str(e)}",
                }

        except Exception as e:
            # Return error information in JSON format
            return {"option": "", "op": "ERROR", "value": str(e), "error": str(e)}
```

## Defining our scorers

To evaluate how accurate the predictions are against the ground truth, we'll use two different scoring metrics. For web navigation tasks, we need metrics that can pinpoint specific strengths and weaknesses in our agent. We'll create two simple code-based scorers.

The first scorer checks if the predicted action matches the expected action type:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def option_selection_scorer(output: Dict[str, str], expected: Dict[str, Any]) -> int:
    return int(output["op"] == expected["action"])
```

The second evaluates whether the details of the action were correct:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def action_correctness_scorer(output: Dict[str, str], expected: Dict[str, Any]) -> int:
    # First, check if both action types match (note output uses "op" key)
    action_matches = output["op"] == expected["action"]

    # If the actions don't match, return 0 immediately
    if not action_matches:
        return 0

    # If we're dealing with a CLICK action, we've already confirmed they match
    if expected["action"] == "CLICK":
        return 1

    # For TYPE or SELECT, check if values match too
    return int(output["value"] == expected["value"])
```

Using two different scorers will help us identify whether errors come from misunderstanding the task context or from incorrectly formulating the action details.

## Running the evaluation

Now that we've set up the task, dataset, and evaluation criteria, we're ready to run our evaluation. This function will load and process each dataset sample, generate predictions, and assess how accurately the model identifies the correct action type and associated details. All results will be captured in Braintrust, allowing us to analyze performance and pinpoint areas for improvement.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def run_mind2web_evaluation(sample_size: int = MAX_SAMPLES) -> None:
    try:
        # Load samples
        samples = load_mind2web_samples(max_samples=sample_size)

        if not samples:
            return

        # Create Braintrust dataset
        dataset = create_braintrust_dataset(samples)

        # Run the evaluation
        experiment_name = f"mind2web-{int(time.time())}"
        Eval(
            "multimodal-mind2web-eval",  # Project name
            data=dataset,
            task=predict_with_gpt4o,
            scores=[option_selection_scorer, action_correctness_scorer],
            experiment_name=experiment_name,
            metadata={
                "model": "gpt-4o",
            },
        )

    except Exception as e:
        print(f"Evaluation failed: {e}")


if __name__ == "__main__":
    # Run evaluation with a smaller sample size for testing. Adjust this number to run on more or less samples.
    run_mind2web_evaluation(sample_size=10)
```

## Analyzing the results

Web agents have many configuration options that can impact their performance. In Braintrust, you can dig deeper into each trace to see each step the agent takes, including attachments and intermediate processing steps. This makes it easier to identify issues, debug quickly, and iterate.

<img src="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/WebAgent/trace.png?fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=e4e59bf794da13a35454dd4ce520f512" alt="attachment" data-og-width="2650" width="2650" data-og-height="1568" height="1568" data-path="cookbook/assets/WebAgent/trace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/WebAgent/trace.png?w=280&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=6749d45da4ec05655b9810c0cfb08284 280w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/WebAgent/trace.png?w=560&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=00430e27c6e8b6a4e2b4b820d241912d 560w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/WebAgent/trace.png?w=840&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=f6b388476a9c10ac2721f20cb3696f15 840w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/WebAgent/trace.png?w=1100&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=ed8d1462a3ed11f803ab107c0b29b928 1100w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/WebAgent/trace.png?w=1650&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=436de465ac294510465138ccae0b5686 1650w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/WebAgent/trace.png?w=2500&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=e3b57fe5b9610baa1a98a169f25373a6 2500w" />

Performance can also vary depending on context. For example, your agent might perform well on some websites but struggle with others, or handle certain action types better. In Braintrust, you can group and filter evaluation results by metadata, helping you quickly pinpoint patterns and identify areas for improvement.

<img src="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/WebAgent/grouping.png?fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=b004a8806256a6dba38dd589ab106521" alt="grouping" data-og-width="2656" width="2656" data-og-height="1546" height="1546" data-path="cookbook/assets/WebAgent/grouping.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/WebAgent/grouping.png?w=280&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=005a530514f3f3ffa89acaffe6c76bd9 280w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/WebAgent/grouping.png?w=560&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=1850df791d7f78d352b220b1e5d2855d 560w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/WebAgent/grouping.png?w=840&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=013c79349aff8f2039ee6382b9927ec2 840w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/WebAgent/grouping.png?w=1100&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=bc654e7e9cbc8604a7c4bec922a4e40e 1100w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/WebAgent/grouping.png?w=1650&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=4176995affa8588b41eafe119db4d470 1650w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/cookbook/assets/WebAgent/grouping.png?w=2500&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=41ab794bbe2a6aff3e38173711d66294 2500w" />

### Learning from the data

Taking the time to analyze your results in Braintrust will help you discover clear opportunities to improve your agent. For example, you might find that certain HTML preprocessing techniques perform better on form-intensive websites, or that providing more detailed historical context improves accuracy on complex tasks. By tracing each action, filtering results, and comparing different approaches systematically, you can make targeted improvements instead of relying on guesswork.

## Next steps

Now that you've explored how to evaluate the decision making ability of a web agent, you can:

* Learn more about [how to evaluate agents](https://braintrust.dev/blog/evaluating-agents)
* Check out the [guide to what you should do after running an eval](https://braintrust.dev/blog/after-evals)
* Try out another [agent cookbook](/cookbook/recipes/PromptChaining)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt