# Source: https://docs.together.ai/docs/language-overview.md

# Code/Language

> Learn how to create completions from language and code models.

## Creating a completion

Use `client.completions.create` to create a completion for a code or language models:

<CodeGroup>
  ```py Python theme={null}
  import os
  from together import Together

  client = Together()

  response = client.completions.create(
      model="meta-llama/Llama-2-70b-hf",
      prompt="def fibonacci(n): ",
      stream=True,
  )

  for chunk in response:
      print(chunk.choices[0].text or "", end="", flush=True)
  ```

  ```ts TypeScript theme={null}
  import Together from 'together-ai';

  const together = new Together();

  const response = await together.completions.create({
    model: "meta-llama/Llama-2-70b-hf",
    prompt: 'def bubbleSort(): ',
    stream: true
  });

  for chunk in response:
      console.log(chunk.choices[0].text)
  ```
</CodeGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt