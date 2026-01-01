# Source: https://docs.together.ai/docs/deepseek-r1.md

# DeepSeek R1 Quickstart

> How to get the most out of reasoning models like DeepSeek-R1.

Reasoning models like DeepSeek-R1 have been trained to think step-by-step before responding with an answer. As a result they excel at complex reasoning tasks such as coding, mathematics, planning, puzzles, and agent workflows.

Given a question in the form of an input prompt DeepSeek-R1 outputs both its chain of thought/reasoning process in the form of thinking tokens between `<think>` tags and the answer.

Because these models use more computation/tokens to perform better reasoning they produce longer outputs and can be slower and more expensive than their non-reasoning counterparts.

<Frame>
  <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=f6f0a54c08e17e7d3015f4b2840f3cde" data-og-width="2946" width="2946" data-og-height="846" height="846" data-path="images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=a2a20a5084ecf855f6f32d15295f7805 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=79fffaa220583da7c6e63b59dfd13843 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=99521c4258f5bc9c2cff61095b1a6f71 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=06feffe542ddcaa3aa39ee699e5f35a4 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=4f3da12e9eb0145ffe794abf093a0d6b 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/9f4e73cc93d4bc5477375c97d1ff0e4c0ddefaf1466a05223336f2e098784847-image.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=e9e70a0268295c5bb127bbe2e852d1d8 2500w" />
</Frame>

## How to use DeepSeek-R1 API

Since these models produce longer responses we'll stream in tokens instead of waiting for the whole response to complete.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()  # pass in API key to api_key or set a env variable

  stream = client.chat.completions.create(
      model="deepseek-ai/DeepSeek-R1",
      messages=[
          {
              "role": "user",
              "content": "Which number is bigger 9.9 or 9.11?",
          }
      ],
      stream=True,
  )

  for chunk in stream:
      print(chunk.choices[0].delta.content or "", end="", flush=True)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";
  const together = new Together();

  const stream = await together.chat.completions.create({
    model: "deepseek-ai/DeepSeek-R1",
    messages: [{ role: "user", content: "Which number is bigger 9.9 or 9.11?" }],
    stream: true,
  });

  for await (const chunk of stream) {
    // use process.stdout.write instead of console.log to avoid newlines
    process.stdout.write(chunk.choices[0]?.delta?.content || "");
  }
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "deepseek-ai/DeepSeek-R1",
       	"messages": [
            {"role": "user", "content": "Which number is bigger 9.9 or 9.11?"}
       	]
       }'
  ```
</CodeGroup>

This will produce an output that contains both the Chain-of-thought tokens and the answer:

```plain  theme={null}
<think>
Okay, the user is asking which number is bigger between 9.9 and 9.11.

Let me think about how to approach this.
...
</think>

**Answer:** 9.9 is bigger.
```

## Working with DeepSeek-R1

Reasoning models like DeepSeek-R1 should be used differently than standard non-reasoning models to get optimal results.

Here are some usage guides:

* **Temperature**: Use 0.5–0.7 (recommended 0.6) to balance creativity and coherence, avoiding repetitive or nonsensical outputs.
* **System Prompts**: Omit system prompts entirely. Provide all instructions directly in the user query.

Think of DeepSeek-R1 as a senior problem-solver – provide high-level objectives (e.g., "Analyze this data and identify trends") and let it determine the methodology.

* Strengths: Excels at open-ended reasoning, multi-step logic, and inferring unstated requirements.
* Over-prompting (e.g., micromanaging steps) can limit its ability to leverage advanced reasoning.
  Under-prompting (e.g., vague goals like "Help with math") may reduce specificity – balance clarity with flexibility.

For a more detailed guide on DeepSeek-R1 usage please see [Prompting DeepSeek-R1](/docs/prompting-deepseek-r1) .

## DeepSeek-R1 Use-cases

* **Benchmarking other LLMs**: Evaluates LLM responses with contextual understanding, particularly useful in fields requiring critical validation like law, finance and healthcare.
* **Code Review**: Performs comprehensive code analysis and suggests improvements across large codebases
* **Strategic Planning**: Creates detailed plans and selects appropriate AI models based on specific task requirements
* **Document Analysis**: Processes unstructured documents and identifies patterns and connections across multiple sources
* **Information Extraction**: Efficiently extracts relevant data from large volumes of unstructured information, ideal for RAG systems
* **Ambiguity Resolution**: Interprets unclear instructions effectively and seeks clarification when needed rather than making assumptions

## Managing Context and Costs

When working with reasoning models, it's crucial to maintain adequate space in the context window to accommodate the model's reasoning process. The number of reasoning tokens generated can vary based on the complexity of the task - simpler problems may only require a few hundred tokens, while more complex challenges could generate tens of thousands of reasoning tokens.

Cost/Latency management is an important consideration when using these models. To maintain control over resource usage, you can implement limits on the total token generation using the `max_tokens` parameter.

While limiting tokens can reduce costs/latency, it may also impact the model's ability to fully reason through complex problems. Therefore, it's recommended to adjust these parameters based on your specific use case and requirements, finding the optimal balance between thorough reasoning and resource utilization.

## General Limitations

Currently, the capabilities of DeepSeek-R1 fall short of DeepSeek-V3 in general purpose tasks such as:

* Function calling
* Multi-turn conversation
* Complex role-playing
* JSON output.

This is due to the fact that long CoT reinforcement learning training was not optimized for these general purpose tasks and thus for these tasks you should use other models.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt