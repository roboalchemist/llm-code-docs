# Source: https://docs.together.ai/docs/sequential-agent-workflow.md

# Sequential Workflow

> Coordinating a chain of LLM calls to solve a complex task.

A workflow where the output of one LLM call becomes the input for the next. This sequential design allows for structured reasoning and step-by-step task completion.

## Workflow Architecture

Chain multiple LLM calls sequentially to process complex tasks.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6ba24ee6aded3b4fcbd509d1115b354ee78e414c9edd7f91f19a468c641d9e73-sequential.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=78442d4ddf22839fca77d6e13e0fbea1" alt="" data-og-width="4560" width="4560" data-og-height="1696" height="1696" data-path="images/docs/6ba24ee6aded3b4fcbd509d1115b354ee78e414c9edd7f91f19a468c641d9e73-sequential.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6ba24ee6aded3b4fcbd509d1115b354ee78e414c9edd7f91f19a468c641d9e73-sequential.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=56dbfae0893276ec21bc44ba81ad4db6 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6ba24ee6aded3b4fcbd509d1115b354ee78e414c9edd7f91f19a468c641d9e73-sequential.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=bcef647c7e736d88a0094777216db71e 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6ba24ee6aded3b4fcbd509d1115b354ee78e414c9edd7f91f19a468c641d9e73-sequential.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=2476ae2ffa6857d35a293a74b97cfcbb 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6ba24ee6aded3b4fcbd509d1115b354ee78e414c9edd7f91f19a468c641d9e73-sequential.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=552af104c83e732881245b22fc165621 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6ba24ee6aded3b4fcbd509d1115b354ee78e414c9edd7f91f19a468c641d9e73-sequential.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=266a9a82f4e3b3b80d7151fbbd25b4ad 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6ba24ee6aded3b4fcbd509d1115b354ee78e414c9edd7f91f19a468c641d9e73-sequential.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=842471507d90c733194478e314add630 2500w" />
</Frame>

<Info>
  ### Sequential Workflow Cookbook

  For a more detailed walk-through refer to the [notebook here](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Serial_Chain_Agent_Workflow.ipynb)
</Info>

## Setup Client

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()


  def run_llm(user_prompt: str, model: str, system_prompt: str = None):
      messages = []
      if system_prompt:
          messages.append({"role": "system", "content": system_prompt})

      messages.append({"role": "user", "content": user_prompt})

      response = client.chat.completions.create(
          model=model,
          messages=messages,
          temperature=0.7,
          max_tokens=4000,
      )

      return response.choices[0].message.content
  ```

  ```typescript TypeScript theme={null}
  import assert from "node:assert";
  import Together from "together-ai";

  const client = new Together();

  export async function runLLM(
    userPrompt: string,
    model: string,
    systemPrompt?: string,
  ) {
    const messages: { role: "system" | "user"; content: string }[] = [];
    if (systemPrompt) {
      messages.push({ role: "system", content: systemPrompt });
    }

    messages.push({ role: "user", content: userPrompt });

    const response = await client.chat.completions.create({
      model,
      messages,
      temperature: 0.7,
      max_tokens: 4000,
    });

    const content = response.choices[0].message?.content;
    assert(typeof content === "string");
    return content;
  }
  ```
</CodeGroup>

## Implement Workflow

<CodeGroup>
  ```python Python theme={null}
  from typing import List


  def serial_chain_workflow(
      input_query: str,
      prompt_chain: List[str],
  ) -> List[str]:
      """Run a serial chain of LLM calls to address the `input_query`
      using a list of prompts specified in `prompt_chain`.
      """
      response_chain = []
      response = input_query
      for i, prompt in enumerate(prompt_chain):
          print(f"Step {i+1}")
          response = run_llm(
              f"{prompt}\nInput:\n{response}",
              model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
          )
          response_chain.append(response)
          print(f"{response}\n")
      return response_chain
  ```

  ```typescript TypeScript theme={null}
  /*
    Run a serial chain of LLM calls to address the `inputQuery`
    using a list of prompts specified in `promptChain`.
  */
  async function serialChainWorkflow(inputQuery: string, promptChain: string[]) {
    const responseChain: string[] = [];
    let response = inputQuery;

    for (const prompt of promptChain) {
      console.log(`Step ${promptChain.indexOf(prompt) + 1}`);

      response = await runLLM(
        `${prompt}\nInput:\n${response}`,
        "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
      );
      console.log(`${response}\n`);
      responseChain.push(response);
    }

    return responseChain;
  }
  ```
</CodeGroup>

## Example Usage

<CodeGroup>
  ```python Python theme={null}
  question = "Sally earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?"

  prompt_chain = [
      """Given the math problem, ONLY extract any relevant numerical information and how it can be used.""",
      """Given the numberical information extracted, ONLY express the steps you would take to solve the problem.""",
      """Given the steps, express the final answer to the problem.""",
  ]

  responses = serial_chain_workflow(question, prompt_chain)

  final_answer = responses[-1]
  ```

  ```typescript TypeScript theme={null}
  const question =
    "Sally earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?";

  const promptChain = [
    "Given the math problem, ONLY extract any relevant numerical information and how it can be used.",
    "Given the numberical information extracted, ONLY express the steps you would take to solve the problem.",
    "Given the steps, express the final answer to the problem.",
  ];

  async function main() {
    await serialChainWorkflow(question, promptChain);
  }

  main();
  ```
</CodeGroup>

## Use cases

* Generating Marketing copy, then translating it into a different language.
* Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline.
* Using an LLM to clean and standardize raw data, then passing the cleaned data to another LLM for insights, summaries, or visualizations.
* Generating a set of detailed questions based on a topic with one LLM, then passing those questions to another LLM to produce well-researched answers.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt