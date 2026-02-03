# Source: https://docs.agent.ai/lists-in-for-loops.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Use Lists in For Loops

> How to transform multi-select values into a usable format in Agent.ai workflows

<iframe width="560" height="315" src="https://www.youtube.com/embed/qy84PxZPFhw?si=eNa6AxbJavt7EbiE" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## **Overview**

When using **for loop** actions in [Agent.ai](http://Agent.ai), you might run into issues if you're working with multi-select dropdowns. The problem usually comes down to format: **for loop** expects a very specific type of input, and the raw output from a multi-dropdown list might not be an exact match.

This guide walks you through how to inspect your input, transform it using a built-in LLM, and successfully run a loop with multi-dropdown values.

## **Required Format for for loop**

[Agent.ai](http://Agent.ai)'s **for loop** requires a **plain list of strings** in the following format:

```
["item1", "item2", "item3"]
```

Unspecified

* Must include square brackets **\[]**
* Each item must be in quotes
* Items must be separated by commas

Structured JSON (e.g., objects with ) will not work directly.

## **Step 1: Inspect Multi-Dropdown Output**

Multi-dropdown inputs do not return a list of strings. Instead, you'll get a list of objects that looks like this:

```
[  
  {"label": "LinkedIn", "value": "LinkedIn"},
  {"label": "Twitter", "value": "Twitter"}
]
```

To verify this, add a **Create Output** action immediately after your multi-dropdown input and display the variable. This lets you confirm the exact format before using it in a loop.

## **Step 2: Transform the Input**

To convert this into a usable format, insert an **LLM** **action** before the the loop action. Use a prompt that extracts only the **value** fields and returns a plain list of strings.

### **Example Prompt**

You will receive a JSON array of objects. Each object has a "label" and "value."

Your task:

* Extract the "value" from each object
* Return a plain Python list of strings
* No extra text, no code block formatting, no JSON structure
* Only output something like: \["LinkedIn", "Twitter"]

## **Step 3: Use the Transformed List**

Once the LLM returns the cleaned-up list, pass it into your **for loop** action. The loop should now work as expected.

Have questions or need help with your agent? Reach out to our [support team](https://agent.ai/feedback) or [community](https://community.agent.ai/feed).
