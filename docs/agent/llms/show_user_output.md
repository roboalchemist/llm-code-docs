# Source: https://docs.agent.ai/actions/show_user_output.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Show User Output

## Overview

The "Show User Output" action displays information to users in a visually organized way. It lets you present data, results, or messages in different formats to make them easy to read and understand.

### Use Cases

* **Real-time Feedback**: Display data summaries or workflow outputs to users.

* **Interactive Reports**: Present results in a structured format like tables or markdown.

## **How to Configure**

### **Step 1: Add the Action**

1. In the Actions tab, click "Add action"

2. Select "Show User Output" from the options

## Step 2: Configuration Fields

### Heading

* **Description**: Provide a heading for the output display.

* **Example**: "User Results" or "Analysis Summary."

* **Required**: No

### Output Formatted

* **Description**: Enter the formatted output in HTML, JSON, or Markdown.

* **Example**:&#x20;

1. Can be text: "Here are your results"

2. Or a variable: \{\{analysis\_results}}

3. Or a mix of both: "Analysis complete: \{\{analysis\_results}}"

* **Required**: Yes

### Format

* **Description**: Choose the format for output display.

* **Options**: Auto, HTML, JSON, Table, Markdown, Audio, Text, JSX

* **Example**: "HTML" for web-based formatting.

* **Required**: Yes

## **Output Formats Explained**

### **Auto**

Agent.AI will try to detect the best format automatically based on your content. Use this when you're unsure which format to choose.

### **HTML**

Displays content with web formatting (like colors, spacing, and styles).

* Example: \<h1>Results\</h1>\<p>Your information is ready.\</p>

* Good for: Creating visually structured content with different text sizes, colors, or layouts

* Tip: When using AI tools like Claude or GPT, you can ask them to format their responses in HTML

### **Markdown**

A simple way to format text with headings, lists, and emphasis.

* Example: # Results\n\n- First item\n- Second item

* Good for: Creating organized content with simple formatting needs

* Tip: You can ask AI models to output their responses in Markdown format for easier display

### **JSON**

Displays data in a structured format with keys and values.

* Example: \{"name": "John", "age": 30, "email": "[john@example.com](mailto:john@example.com)"}

* Good for: Displaying data in an organized, hierarchical structure

* To get a specific part of a JSON string, use dot notation:

  * \{\{user\_data.name}} to display just the name

  * \{\{weather.forecast.temperature}} to display a nested value

  * For array items, use: \{\{items.0}} for the first item, \{\{items.1}} for the second, etc.

* Tip: You can request AI models to respond in JSON format when you need structured data

### **Table**

Shows information in rows and columns, like a spreadsheet.

* **Important**: Tables requires a very specific format:

1\) A JSON array of arrays:

```
[
  ["Column 1", "Column 2", "Column 3"],
  ["Row 1 Data", "More Data", "Even More"],
  ["Row 2 Data", "More Data", "Even More"]
]
```

2\) Or a CSV:

```
Column 1,Column 2,Column 3
Row 1 Data,More Data,Even More
Row 2 Data,More Data,Even More
```

See [<u>this example agent</u>](https://agent.ai/agent/Table-Creator) for table output format.

### **Text**

Simple plain text without any special formatting. What you type is exactly what the user sees.

* Good for: Simple messages or information that doesn't need special formatting

### **Audio**

Displays an audio player to play sound files. See [<u>this agent</u>](https://agent.ai/agent/autio-template) as an example. 

### **JSX**

For technical users who need to create complex, interactive displays.

* Good for: Interactive components with special styling needs

* Requires knowledge of React JSX formatting
