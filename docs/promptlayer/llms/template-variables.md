# Source: https://docs.promptlayer.com/features/prompt-registry/template-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Template Variables

Creating flexible, dynamic prompts is essential to getting the most out of LLMs. PromptLayer's template system allows you to build reusable prompts where values can be inserted at runtime. This guide explains the two formatting options available in our platform: `f-string` and `jinja2`.

<Info>
  Looking to save and reuse variable values? Check out [Input Variable Sets](/features/prompt-registry/input-variable-sets) to learn how to create named collections of variables that can be applied across prompts, playground, and agents.
</Info>

## What are input variables?

Input variables make your prompts dynamic by creating placeholders that get replaced with actual values when the prompt is used. This allows you to:

* Personalize prompts with user information
* Insert specific context or data
* Create reusable prompt templates for different scenarios
* Conditionally include or exclude sections based on available data

PromptLayer supports two popular templating systems, each with their own strengths:

1. **F-strings**: Simple, straightforward variable replacement
2. **Jinja2**: Advanced templating with conditional logic, loops, and filters

## F-string Variables

F-strings (formatted string literals) offer a straightforward way to insert variables into your prompts using simple curly braces.

### Basic Syntax

```
Tell me about {topic} in a way that {audience} would understand.
```

### How It Works

When you use this template, you provide values for each variable:

<CodeGroup>
  ```python Python theme={null}
  input_variables = {
      "topic": "quantum computing",
      "audience": "high school students"
  }

  template = promptlayer_client.templates.get("educational_prompt", {
      "input_variables": input_variables
  })
  ```

  ```js JavaScript theme={null}
  const input_variables = {
      topic: "quantum computing",
      audience: "high school students"
  };

  const template = await promptLayerClient.templates.get("educational_prompt", {
      input_variables
  });
  ```
</CodeGroup>

The resulting prompt would be:

```
Tell me about quantum computing in a way that high school students would understand.
```

### F-string Best Practices

* Use descriptive variable names that clearly indicate their purpose
* Keep variable names simple and avoid special characters
* Make sure all variables in your template have corresponding values at runtime
* Use f-strings when you need simple variable substitution without complex logic

## Jinja2 Templates

Jinja2 is a more powerful templating engine that extends beyond basic variable replacement. It's ideal for complex prompt structures that require conditionals, loops, or data transformations.

PromptLayer supports the full Jinja2 spec. Read more about best practices for using Jinja2 [here](https://blog.promptlayer.com/prompt-templates-with-jinja2-2/).

### When to Use Jinja2

Consider using Jinja2 instead of f-strings when:

* You need conditional sections in your prompts
* You're working with lists or JSON data that needs to be formatted
* Your prompt requires loops to handle multiple items
* You want to transform variables (uppercase, lowercase, etc.)
* You're using nested data structures

<Warning>
  If your templates contain JSON, always use Jinja2 instead of f-strings, as the curly braces in JSON can conflict with f-string syntax.
</Warning>

### Basic Variable Replacement

Jinja2 uses double curly braces for variable insertion:

```
Hello, {{ user_name }}! Let's discuss {{ topic }} today.
```

### Conditional Logic

Include or exclude sections based on whether variables exist or meet certain conditions:

```
Let's analyze this text:
{{ text }}

{% if key_points %}
Focus on these key points:
{% for point in key_points %}
- {{ point }}
{% endfor %}
{% else %}
Provide a general summary.
{% endif %}
```

### Loops for Lists and Collections

Iterate through lists of items to include multiple elements:

```
Please analyze the following products:
{% for product in products %}
- {{ product.name }}: priced at ${{ product.price }}, category: {{ product.category }}
{% endfor %}
```

### Working with JSON Data

Jinja2 excels at handling structured JSON inputs:

```
{% if customer.history %}
Based on your purchase history:
{% for purchase in customer.history %}
- {{ purchase.item }} (purchased on {{ purchase.date }})
{% endfor %}

Here are our recommendations:
{% for item in recommendations %}
- {{ item.name }}: {{ item.description }}
{% endfor %}
{% else %}
Welcome new customer! Here are our popular items:
{% for item in popular_items %}
- {{ item.name }}: {{ item.description }}
{% endfor %}
{% endif %}
```

### Text Transformation with Filters

Apply transformations to your variables using filters:

```
Original query: {{ query }}
Searching for: {{ query | lower }}
Categories: {{ categories | join(", ") }}
```

### Advanced Jinja2 Techniques

#### Default Values

Provide fallbacks for optional variables:

```
Hello, {{ user.name | default("valued customer") }}!
```

#### Macro Definitions

Create reusable template components:

```
{% macro format_product(item) %}
- {{ item.name }} (${{ item.price }}): {{ item.description }}
{% endmacro %}

Our featured products:
{% for product in featured %}
{{ format_product(product) }}
{% endfor %}
```

#### Working with Conditionals

Make templates adaptable to different inputs:

```
{% if user.experience == "beginner" %}
Let me explain {{ topic }} in simple terms...
{% elif user.experience == "intermediate" %}
As you're familiar with the basics of {{ topic }}...
{% else %}
Given your advanced understanding of {{ topic }}...
{% endif %}
```

By leveraging these formatting options, you can create versatile prompt templates that adapt to different scenarios, making your PromptLayer workflows more flexible and powerful.

## Setting Template Format

When creating a template in PromptLayer, select the appropriate format based on your needs:

<img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/template-format.png?fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=e09c2dfb0eefd0548043d67b51b3c8c7" data-og-width="2880" width="2880" data-og-height="1800" height="1800" data-path="images/template-format.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/template-format.png?w=280&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=f75c1be03395698686a0048fde36eb23 280w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/template-format.png?w=560&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=a011d728c86d9365e452b1a4a21fc0cf 560w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/template-format.png?w=840&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=45de0d00ee0b3a3efc562ac95fed5f73 840w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/template-format.png?w=1100&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=21de7c13c31e084e24c3cd82f5b5e6f2 1100w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/template-format.png?w=1650&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=91b85783460bf20f16e892928ed91e9f 1650w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/template-format.png?w=2500&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=6180e00715d8008edb3ec790e1de07dc 2500w" />

## Input Variable Examples

### F-string Example

<CodeGroup>
  ```python Python theme={null}
  input_variables = {
      "product_name": "Smart Home Hub",
      "customer_segment": "tech enthusiasts",
      "pain_points": "complex setup process, compatibility issues"
  }
  ```

  ```js JavaScript theme={null}
  const input_variables = {
      product_name: "Smart Home Hub",
      customer_segment: "tech enthusiasts",
      pain_points: "complex setup process, compatibility issues"
  };
  ```
</CodeGroup>

### Jinja2 Example with Structured Data

<CodeGroup>
  ```python Python theme={null}
  input_variables = {
      "user": {
          "name": "Alex",
          "role": "Marketing Manager",
          "experience_level": "intermediate"
      },
      "topics": ["SEO optimization", "content strategy", "social media"],
      "show_advanced": True
  }
  ```

  ```js JavaScript theme={null}
  const input_variables = {
      user: {
          name: "Alex",
          role: "Marketing Manager",
          experience_level: "intermediate"
      },
      topics: ["SEO optimization", "content strategy", "social media"],
      show_advanced: true
  };
  ```
</CodeGroup>

## Structured Outputs

Template variables can also be used within structured output schemas to create dynamic validation rules and response formats. For more information, see our [Structured Outputs documentation](/features/prompt-registry/structured-outputs).
