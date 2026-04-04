# Source: https://docs.agent.ai/actions/format_text.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Format Text

## Overview

Apply formatting to text, such as changing case, removing characters, or truncating, to prepare it for specific uses.

### Use Cases

* **Text Standardization**: Convert inputs to a consistent format.
* **Data Cleaning**: Remove unwanted characters or HTML from text.

## Configuration Fields

### Format Type

* **Description**: Select the type of formatting to apply.
* **Options**: Make Uppercase, Make Lowercase, Capitalize, Remove Characters, Trim Whitespace, Split Text By Delimiter, Join Text By Delimiter, Remove HTML, Truncate
* **Example**: "Make Uppercase" for standardizing text.
* **Required**: Yes

### Characters/Delimiter/Truncation Length

* **Description**: Specify the characters to remove or delimiter to split/join text, or length for truncation.
* **Example**: "@" to remove mentions or "5" for truncation length.
* **Required**: No

### Input Text

* **Description**: Enter the text to format.
* **Example**: "Hello, World!"
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the formatted text.
* **Example**: "formatted\_text" or "cleaned\_data."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes
