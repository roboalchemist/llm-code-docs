# Source: https://www.promptfoo.dev/docs/guides/testing-guardrails/

# Testing and Validating Guardrails

Guardrails are security filters that help protect your AI applications from misuse. This guide explains how to test and validate guardrails with Promptfoo to ensure they're working effectively.

## Overview of Guardrails Testing

There are two primary approaches to testing guardrails:

1. **Test your application directly** - Test your application with guardrails enabled as part of your HTTP endpoint
2. **Test guardrails separately** - Test the guardrail service directly if it has a dedicated endpoint

Either way, Promptfoo provides powerful tools to validate that your guardrails are properly preventing harmful content, detecting PII, blocking prompt injections, and more.

## Testing Application with Integrated Guardrails

### HTTP Provider Configuration

If your application includes guardrails as part of its API, you can test it using the [HTTP provider](/docs/providers/http/):

```yaml
promptfooconfig.yaml
```

```python
import boto3
import json
from botocore.exceptions import ClientError
import logging

def call_api(prompt, options, context):
    """AWS Bedrock Guardrails provider for image content analysis.
    Supports image input through ApplyGuardrail API with comprehensive error handling.
    """
    config = options.get("config", {})
    guardrail_id = config.get("guardrail_id")
    guardrail_version = config.get("guardrail_version", "DRAFT")
    region = config.get("region", "us-east-1")
    log_requests = config.get("log_requests", False)

    try:
        # Get variables from context
        vars_dict = context.get("vars", {})

        # Initialize content array
        content = []

        # Process image input
        image_data = vars_dict.get("image")
        image_format = vars_dict.get("format", "jpeg")

        if not image_data:
            return {"output": None, "error": "No image data provided in context variables"}

        # Handle image input processing
        if log_requests:
            logger.info(f"Processing image input (format: {image_format})")
            logger.info(f"Image data length: {len(image_data) if image_data else 0}")

        try:
            if isinstance(image_data, str):
                # Remove any data URL prefix if present
                if image_data.startswith("data:"):
                    image_data = image_data.split(":", 1)[1] if "," in image_data else image_data

                # Strict base64 decode
                image_bytes = base64.b64decode(image_data, validate=True)

            elif isinstance(image_data, (bytes, bytearray)):
                # If bytes are provided, assume already-decoded content
                image_bytes = bytes(image_data)

            else:
                raise ValueError("Unsupported image data type; expected base64 string or bytes")

            content.append({
                "image": {
                    "format": image_format.lower(),
                    "source": {
                        "bytes": image_bytes
                    }
                }
            })

        except Exception as e:
            logger.error(f"Failed to decode base64 image for AWS: {e}")
            return {"output": None, "error": f"Failed to decode base64 image: {str(e)}"}

        if log_requests:
            logger.info(f"Calling ApplyGuardrail with {len(content)} content items")
            logger.info(f"Guardrail ID: {guardrail_id}, Version: {guardrail_version}")

        # Call the ApplyGuardrail API
        response = bedrock_runtime.apply_guardrail(
            guardrailIdentifier=guardrail_id,
            guardrailVersion=guardrail_version,
            source="INPUT",  # Test input content
            content=content
        )

        if log_requests:
            logger.info(f"Guardrail response: {json.dumps(response, indent=2)}")

        # Check the action taken by the guardrail
        action = response.get("action", "")

        # Extract assessment details
        assessments = response.get("assessments", [])
        detailed_reasons = []
        for assessment in assessments:
            if "topicPolicy" in assessment:
                for topic in assessment["topicPolicy"].get("topics", []):
                    if topic.get("action") == "BLOCKED":
                        detailed_reasons.append(f"Topic: {topic.get('name', 'Unknown')}")

            if "contentPolicy" in assessment:
                filters = assessment["contentPolicy"].get("filters", [])
                for filter_item in filters:
                    if filter_item.get("action") == "BLOCKED":
                        filter_type = filter_item.get("type", "Unknown")
                        confidence = filter_item.get("confidence", "N/A")
                        detailed_reasons.append(f"Content Filter: {filter_type} (Confidence: {confidence})")

            if "wordPolicy" in assessment:
                custom_words = assessment["wordPolicy"].get("customWords", [])
                managed_words = assessment["wordPolicy"].get("managedWordLists", [])
                if custom_words:
                    detailed_reasons.append(f"Custom words detected: {", ".join(custom_words)}")
                if managed_words:
                    detailed_reasons.append(f"Managed word lists: {", ".join(managed_words)}")

        # Get the actual AWS blocked message from outputs
        outputs = response.get("outputs", [])
        aws_blocked_message = ""

        if outputs and len(outputs) > 0:
            aws_blocked_message = outputs[0].get("text", "")

        if action == "GUARDRAIL_INTERVENED":
            if detailed_reasons:
                blocked_message = f"Image content blocked. Categories: {", ".join(detailed_reasons)}. "
            else:
                blocked_message = "Image content blocked by guardrails."

            if aws_blocked_message:
                blocked_message += f" AWS Response: '{aws_blocked_message}'"

            return {"output": blocked_message, "guardrails": {
                "flagged": True,  # Content was flagged (blocked)
                "blocked": True,  # Explicitly indicate blocking
                "reason": aws_blocked_message or "Guardrail intervened",
                "detailed_reasons": detailed_reasons,
                "action": action,
                "assessments": assessments,
                "aws_message": aws_blocked_message,
                "details": response
            }}

        else:
            return {"output": "Image content passed guardrails check", "guardrails": {
                "flagged": False,  # Content was not flagged
                "blocked": False,  # Content was not blocked
                "reason": "Image content passed guardrails check",
                "action": action,
                "details": response
            }}

    except ClientError as e:
        error_code = e.response["Error"]["Code"]
        error_message = e.response["Error"]["Message"]

        logger.error(f"AWS ClientError: {error_code} - {error_message}")

        # Provide specific error messages for common issues
        if error_code == "ValidationException":
            if "image format" in error_message.lower():
                return {
                    "output": None,
                    "error": f"Invalid image format. Supported formats: JPEG, PNG. Error: {error_message}"
                }
            elif "size" in error_message.lower():
                return {
                    "output": None,
                    "error": f"Image size exceeds limits. Maximum size: 5MB. Error: {error_message}"
                }

        return {
            "output": None,
            "error": f"AWS Error ({error_code}): {error_message}"
        }

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {
            "output": None,
            "error": f"Unexpected error: {str(e)}"
        }
```

Configure image testing with a dedicated configuration file:

```yaml
promptfooconfig_bedrock_images.yaml
```

```yaml
# Image-only configuration for AWS Bedrock Guardrails
targets:
  - id: file://aws_bedrock_guardrails_with_images.py
    config:
      region: us-east-1
      guardrail_id: your-guardrail-id
      guardrail_version: DRAFT  # Set your version
      log_requests: false  # Set to true for debugging

prompts:
  - Check image safety

defaultTest:
  options:
    transformVars: |
      // Clean image data for AWS Bedrock
      if (vars.image && typeof vars.image === 'string') {
        // Remove any data URL prefix
        if (vars.image.includes('base64',)) {
          vars.image = vars.image.split('base64',)[1];
        }
        // Set format (default to jpeg)
        vars.format = vars.format || 'jpeg';
      }
      return vars;

redteam:
  purpose: Test AWS Bedrock Guardrails ability to detect harmful visual content
  injectVar: image  # Critical: tells Promptfoo to inject images, not text
  numTests: 10
  plugins:
    - id: unsafebench
      config:
        categories: 
          - Violence
          - Sexual
          - Hate
          # Additional available categories:
          # - Deception
          # - Harassment
          # - Illegal activity
          # - Political
          # - Public and personal health
          # - Self-harm
          # - Shocking
          # - Spam
```

Run image-only tests with:

```bash
promptfoo redteam run -c promptfooconfig_bedrock_images.yaml
```

The Promptfoo UI will properly render the images and show which ones were blocked by your guardrails.

## Testing NVIDIA NeMo Guardrails

For NVIDIA NeMo Guardrails, you'd implement a similar approach. We implement `call_api` with a `{output, guardrails, error}` return dictionary:

```python
import nemoguardrails as ng

def call_api(prompt, options, context):
    # Load NeMo Guardrails config
    config_path = options.get("config", {}).get("config_path", "./nemo_config.yml")

    try:
        # Initialize the guardrails
        rails = ng.RailsConfig.from_path(config_path)
        app = ng.LLMRails(rails)

        # Process the user input with guardrails
        result = app.generate(messages=[{"role": "user", "content": prompt}])

        # Check if guardrails were triggered
        flagged = result.get("blocked", False)
        explanation = result.get("explanation", "")

        return {
            "output": result.get("content", ""),
            "guardrails": {
                "flagged": flagged,
                "reason": explanation if flagged else "Passed guardrails"
            }
        }
    except Exception as e:
        return {
            "output": None,
            "error": str(e)
        }
```

Then configure the red team:

```yaml
targets:
  - id: file://nemo_guardrails.py
    config:
      config_path: ./nemo_config.yml

redteam:
  plugins:
    - harmful
    - ...
```

For more information on running the red team, see [red team setup](/docs/red-team/quickstart/).

## Comparing Guardrail Performance

You can set multiple guardrail targets using [red teaming](/docs/red-team/quickstart/) to probe for vulnerabilities:

```yaml
promptfooconfig.yaml
```

```yaml
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
targets:
  - id: file://azure_content_filter.py
    config:
      endpoint: {{env.CONTENT_SAFETY_ENDPOINT}}
      key: {{env.CONTENT_SAFETY_KEY}}
  - id: file://nemo_guardrails.py
  # - And others...

redteam:
  plugins:
    - harmful:hate
    - harmful:self-harm
    - harmful:sexual
    - harmful:violence
    - prompt-injection
    - jailbreak
  strategies:
    - id: prompt-injection
    - id: jailbreak
    - id: translation  # Test evasion through different languages
    - id: misspelling  # Test evasion through character substitution

  numTests: 20
  purpose: Evaluate the effectiveness of content moderation guardrails
```

## Things to think about

When testing guardrails, consider these best practices:

1. **Balance true and false positives** - Don't focus solely on catching harmful content; also measure how often your guardrails incorrectly flag benign content. This is a common problem with guardrails. You can implement additional metrics like [F1-score](/docs/configuration/expected-outputs/deterministic/#f-score) to measure the balance between true and false positives.
2. **Test evasion tactics** - Use misspellings, coded language, and other techniques attackers might use to bypass filters
3. **Test multilingual content** - Guardrails often perform differently across languages
4. **Compare across providers** - Test the same content across different guardrail implementations to compare effectiveness

## What's next

Guardrails are just another endpoint that you can red team. They are a commodity - there are hundreds of guardrails solutions out there.

Choosing a guardrail could be as simple as just going with whatever is offered by your preferred inference provider. But for very serious applications, it's necessary to benchmark and compare.

Learn more about [automated red teaming](/docs/red-team/quickstart/) to conduct these benchmarks.