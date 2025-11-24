# Source: https://docs.agent.ai/actions/use_genai.md

# Use GenAI (LLM)

## Overview

Invoke a language model (LLM) to generate text based on input instructions, enabling creative and dynamic text outputs.

### Use Cases

* **Content Generation**: Draft blog posts, social media captions, or email templates.
* **Summarization**: Generate concise summaries of complex documents.
* **Customer Support**: Create personalized responses or FAQs.

## Configuration Fields

### LLM Engine

* **Description**: Select the language model to use for generating text.
* **Options**: Auto Optimized, GPT-4o, Claude Opus, Gemini 2.0 Flash, and more.
* **Example**: "GPT-4o" for detailed responses or "Claude Opus" for creative writing.
* **Required**: Yes

### Instructions

* **Description**: Enter detailed instructions for the language model.
* **Example**: "Write a summary of this document" or "Generate a persuasive email."
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the generated text.
* **Example**: "llm\_output" or "ai\_generated\_text."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes
