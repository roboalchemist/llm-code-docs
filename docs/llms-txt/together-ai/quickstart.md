# Source: https://docs.together.ai/docs/quickstart.md

# Quickstart

> Get up to speed with our API in one minute.

Together AI makes it easy to run leading open-source models using only a few lines of code.

## 1. Register for an account

First, [register for an account](https://api.together.xyz/settings/api-keys) to get an API key.

Once you've registered, set your account's API key to an environment variable named `TOGETHER_API_KEY`:

```shell Shell theme={null}
export TOGETHER_API_KEY=xxxxx
```

## 2. Install your preferred library

Together provides an official library for Python and TypeScript, or you can call our HTTP API in any language you want:

<CodeGroup>
  ```sh Python theme={null}
  pip install together
  ```

  ```sh TypeScript theme={null}
  npm install together-ai
  ```
</CodeGroup>

## 3. Run your first query against a model

Choose a model to query. In this example, we'll choose GPT OSS 20B with streaming:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  stream = client.chat.completions.create(
      model="openai/gpt-oss-20b",
      messages=[
          {
              "role": "user",
              "content": "What are the top 3 things to do in New York?",
          }
      ],
      stream=True,
  )

  for chunk in stream:
      print(chunk.choices[0].delta.content or "", end="", flush=True)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai"

  async function main() {
    const together = new Together()
    const stream = await together.chat.completions.create({
      model: "openai/gpt-oss-20b",
      messages: [
        { role: "user", content: "What are the top 3 things to do in New York?" },
      ],
      stream: true,
    })

    for await (const chunk of stream) {
      process.stdout.write(chunk.choices[0]?.delta?.content || "")
    }
  }

  main()
  ```

  ```curl cURL theme={null}
  curl -N -X POST "https://api.together.xyz/v1/chat/completions" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "google/gemma-3n-E4B-it",
      "messages": [
        {"role": "user", "content": "Tell me a joke about programmers."}
      ],
      "max_tokens": 100,
      "temperature": 0.8,
      "stream": true
    }'
  ```
</CodeGroup>

Congratulations –you've just made your first query to Together AI!

## Next steps

* Explore [our cookbook](https://github.com/togethercomputer/together-cookbook) for Python recipes with Together AI
* Explore [our demos](https://together.ai/demos) for full-stack open source example apps.
* Check out the [Together AI playground](https://api.together.xyz/playground) to try out different models.
* See [our integrations](/docs/integrations) with leading LLM frameworks.

## Resources

* [Discord](https://discord.com/invite/9Rk6sSeWEG)
* [Pricing](https://www.together.ai/pricing)
* [Support](https://www.together.ai/contact)

***


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt