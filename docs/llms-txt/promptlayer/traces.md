# Source: https://docs.promptlayer.com/running-requests/traces.md

# Traces

Traces are a powerful feature in PromptLayer that allow you to monitor and analyze the execution flow of your applications, including LLM requests. Built on OpenTelemetry, Traces provide detailed insights into function calls, their durations, inputs, and outputs.

## Overview

Traces in PromptLayer offer a comprehensive view of your application's performance and behavior. They allow you to:

* Visualize the execution flow of your functions
* Track LLM requests and their associated metadata
* Measure function durations and identify performance bottlenecks
* Inspect function inputs and outputs for debugging

**Note:** The left menu in the PromptLayer UI only shows root spans, which represent the entry function of your program. While your program is running, you might not see all spans in the UI immediately, even though child spans are being sent to the backend. The root span, along with all its child spans, will only appear in the UI once the program completes. This behavior is particularly noticeable in long-running programs or those with complex execution flows.

<img src="https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/traces/trace-details.png?fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=5206101845243a0280a6194c86039a76" alt="Traces Overview" data-og-width="2034" width="2034" data-og-height="1150" height="1150" data-path="images/traces/trace-details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/traces/trace-details.png?w=280&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=78397b2005a01f8f43ca8ce909525d26 280w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/traces/trace-details.png?w=560&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=93496396820fe18d18b4df62d56a14b2 560w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/traces/trace-details.png?w=840&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=59f5a78e98b8ae9d7c06affa2a871130 840w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/traces/trace-details.png?w=1100&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=13849da52a6978b14ac5c1346cf694d6 1100w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/traces/trace-details.png?w=1650&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=0adfbda4abaa96a4b1b622e2f8f4c2ed 1650w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/traces/trace-details.png?w=2500&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=abaad9dec0cb13e7c107f9c320e5bd41 2500w" />

## Automatic LLM Request Tracing

When you initialize the PromptLayer class with `enable_tracing` set to `True`, PromptLayer will automatically track any LLM calls made using the PromptLayer library. This allows you to capture detailed information about your LLM requests, including:

* Model used
* Input prompts
* Generated responses
* Request duration
* Associated metadata

<CodeGroup>
  ```python Python theme={null}
  from promptlayer import PromptLayer

  # Initialize PromptLayer with tracing enabled
  pl_client = PromptLayer(enable_tracing=True)
  ```

  ```javascript JavaScript theme={null}
  import { PromptLayer } from "promptlayer";

  // Initialize PromptLayer with tracing enabled
  const promptlayer = new PromptLayer({
      apiKey: process.env.PROMPTLAYER_API_KEY,
      enableTracing: true,
  });
  ```
</CodeGroup>

Once PromptLayer is initialized with tracing enabled, you can use the `run()` method to execute prompts. All LLM calls made through this method will be automatically traced, providing detailed insights into your prompt executions.

<CodeGroup>
  ```python Python theme={null}
  response = pl_client.run(
      prompt_name="simple-greeting",
      input_variables={
          "name": "Alice"
      },
      metadata={
          "user_id": "12345"
      }
  )

  print(response)
  ```

  ```javascript JavaScript theme={null}
  async function runPrompt() {
      try {
          const response = await promptlayer.run({
              promptName: "simple-greeting",
              inputVariables: {
                  name: "Alice"
              },
              metadata: {
                  user_id: "12345"
              }
          });

          console.log(response);
      } catch (error) {
          console.error("Error running prompt:", error);
      }
  }

  runPrompt();
  ```
</CodeGroup>

## Custom Function Tracing

In addition to automatic LLM request tracing, you can also use the `traceable` decorator (for Python) or `wrapWithSpan` (for JavaScript) to explicitly track span data for additional functions. This allows you to gather detailed information about function executions.

<CodeGroup>
  ```python Python theme={null}
  # Use the @pl_client.traceable() decorator to trace a function
  @pl_client.traceable()
  def greet(name):
      return f"Hello, {name}!"

  # Use the decorator with custom attributes
  @pl_client.traceable(attributes={"function_type": "math"})
  def calculate_sum(a, b):
      return a + b

  result1 = greet("Alice")
  print(result1)

  result2 = calculate_sum(5, 3)
  print(result2)
  ```

  ```javascript JavaScript theme={null}
  // Define and wrap a function with PromptLayer tracing
  const greet = promptlayer.wrapWithSpan('greet', (name: string): string => {
      return `Hello, ${name}!`;
  });

  const result = greet("Alice");
  console.log(result);
  ```
</CodeGroup>

## Setting Custom Span Names

When tracing functions, you may want to set custom names for your spans to make them more descriptive. Both Python and JavaScript implementations of PromptLayer allow you to set custom span names.

### Python

In Python, you can set a custom span name by passing the `name` parameter to the `traceable` decorator:

```python  theme={null}
@pl_client.traceable(name="CustomGreeting")
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")
print(result)
```

If you don't provide a name parameter, the span will use the function's name by default.

### JavaScript

In JavaScript, you can set a custom span name by passing it as the first argument to the wrapWithSpan function:

```javascript JavaScript theme={null}
const greet = promptlayer.wrapWithSpan('CustomGreeting', (name) => {
    return `Hello, ${name}!`;
});

const result = greet("Alice");
console.log(result);
```

If you want to use the function's name as the span name, you can simply pass the function name as a string:

```javascript JavaScript theme={null}
const greet = promptlayer.wrapWithSpan('greet', (name) => {
    return `Hello, ${name}!`;
});
```

## Creating Parent Spans and Grouping Function Calls

To create a parent span and group multiple function calls within it, you can use the traceable decorator on a main function that calls other traced functions.
Here's an example that demonstrates this concept:

```python  theme={null}
from promptlayer import PromptLayer

# Initialize PromptLayer with tracing enabled
pl_client = PromptLayer(enable_tracing=True)

@pl_client.traceable(name="custom-span")
def main():
    # This function will be the parent span
    openai_call()
    anthropic_call()
    custom_function()
    run_prompt()

@pl_client.traceable()
def openai_call():
    OpenAI = pl_client.openai.OpenAI
    openai = OpenAI()
    template = pl_client.templates.get("simple-greeting")
    response, pl_request_id = openai.chat.completions.create(
        **template["llm_kwargs"],
        return_pl_id=True
    )
    print("OpenAI response:", response.choices[0].message.content)

@pl_client.traceable()
def anthropic_call():
    anthropic = pl_client.anthropic.Anthropic()
    # Add your Anthropic API call here
    print("Anthropic call executed")

@pl_client.traceable()
def custom_function():
    # This is a custom function that will be traced
    result = "Custom function executed"
    print(result)
    return result

@pl_client.traceable()
def run_prompt():
    response = pl_client.run(
        prompt_name="simple-greeting",
        input_variables={}
    )
    print("Prompt response:", response["prompt_blueprint"]["prompt_template"]["messages"][-1])

if __name__ == "__main__":
    main()
```

<img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/traces/nested-spans.png?fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=23eb15c063fd12669988911e9b044090" alt="Group nests spans" data-og-width="2732" width="2732" data-og-height="1404" height="1404" data-path="images/traces/nested-spans.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/traces/nested-spans.png?w=280&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=4f8d2faffcd3fbf5924b5cda138f6c85 280w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/traces/nested-spans.png?w=560&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=3dcb0258bb5d9cdaacde309ed840830c 560w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/traces/nested-spans.png?w=840&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=6bec685e17aa626196898e5bc88b972b 840w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/traces/nested-spans.png?w=1100&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=dd3e9012d46a0aab1683f324fca7e09d 1100w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/traces/nested-spans.png?w=1650&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=1c721f05dc895ddded7431c0626a9217 1650w, https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/traces/nested-spans.png?w=2500&fit=max&auto=format&n=jUVR1Bx755pIFGwB&q=85&s=2f6e48946fa621c999a0801999674312 2500w" />


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt