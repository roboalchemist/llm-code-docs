# Source: https://docs.together.ai/docs/parallel-workflows.md

# Parallel Workflow

> Execute multiple LLM calls in parallel and aggregate afterwards.

Parallelization takes advantage of tasks that can broken up into discrete independent parts. The user's prompt is passed to multiple LLMs simultaneously. Once all the LLMs respond, their answers are all sent to a final LLM call to be aggregated for the final answer.

## Parallel Architecture

Run multiple LLMs in parallel and aggregate their solutions.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=563f3308591ef0da8d01a05de0cf83ed" alt="" data-og-width="3856" width="3856" data-og-height="1792" height="1792" data-path="images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c41987be307115e06c9f92515c7067ce 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=9671d4da9e5a5ca9bceb7f94ce5089f6 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ab1c7b3726580483dafd0b3aa21f74b6 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d10471ea6b7f34d639117129a5e9250c 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a077c1f04ec3bbb35626abcb6d46fce7 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=4500e603783ef5326b1d6548383aa701 2500w" />
</Frame>

<Info>
  Notice that the same user prompt goes to each parallel LLM for execution. An alternate parallel workflow where this main prompt task is broken in sub-tasks is presented later.
</Info>

<Info>
  ### Parallel Workflow Cookbook

  For a more detailed walk-through refer to the [notebook here](https://togetherai.link/agent-recipes-deep-dive-parallelization) .
</Info>

## Setup Client & Helper Functions

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import together
  from together import AsyncTogether, Together

  client = Together()
  async_client = AsyncTogether()


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


  # The function below will call the reference LLMs in parallel
  async def run_llm_parallel(
      user_prompt: str,
      model: str,
      system_prompt: str = None,
  ):
      """Run a single LLM call with a reference model."""
      for sleep_time in [1, 2, 4]:
          try:
              messages = []
              if system_prompt:
                  messages.append({"role": "system", "content": system_prompt})

              messages.append({"role": "user", "content": user_prompt})

              response = await async_client.chat.completions.create(
                  model=model,
                  messages=messages,
                  temperature=0.7,
                  max_tokens=2000,
              )
              break
          except together.error.RateLimitError as e:
              print(e)
              await asyncio.sleep(sleep_time)
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
  import asyncio
  from typing import List


  async def parallel_workflow(
      prompt: str,
      proposer_models: List[str],
      aggregator_model: str,
      aggregator_prompt: str,
  ):
      """Run a parallel chain of LLM calls to address the `input_query`
      using a list of models specified in `models`.

      Returns output from final aggregator model.
      """

      # Gather intermediate responses from proposer models
      proposed_responses = await asyncio.gather(
          *[run_llm_parallel(prompt, model) for model in proposer_models]
      )

      # Aggregate responses using an aggregator model
      final_output = run_llm(
          user_prompt=prompt,
          model=aggregator_model,
          system_prompt=aggregator_prompt
          + "\n"
          + "\n".join(
              f"{i+1}. {str(element)}"
              for i, element in enumerate(proposed_responses)
          ),
      )

      return final_output, proposed_responses
  ```

  ```typescript TypeScript theme={null}
  import dedent from "dedent";

  /*
    Run a parallel chain of LLM calls to address the `inputQuery`
    using a list of models specified in `proposerModels`.

    Returns output from final aggregator model.
  */
  async function parallelWorkflow(
    inputQuery: string,
    proposerModels: string[],
    aggregatorModel: string,
    aggregatorSystemPrompt: string,
  ) {
    // Gather intermediate responses from proposer models
    const proposedResponses = await Promise.all(
      proposerModels.map((model) => runLLM(inputQuery, model)),
    );

    // Aggregate responses using an aggregator model
    const aggregatorSystemPromptWithResponses = dedent`
      ${aggregatorSystemPrompt}

      ${proposedResponses.map((response, i) => `${i + 1}. response`)}
    `;

    const finalOutput = await runLLM(
      inputQuery,
      aggregatorModel,
      aggregatorSystemPromptWithResponses,
    );

    return [finalOutput, proposedResponses];
  }
  ```
</CodeGroup>

## Example Usage

<CodeGroup>
  ```python Python theme={null}
  reference_models = [
      "microsoft/WizardLM-2-8x22B",
      "Qwen/Qwen2.5-72B-Instruct-Turbo",
      "google/gemma-2-27b-it",
      "meta-llama/Llama-3.3-70B-Instruct-Turbo",
  ]

  user_prompt = """Jenna and her mother picked some apples from their apple farm.
  Jenna picked half as many apples as her mom. If her mom got 20 apples, how many apples did they both pick?"""

  aggregator_model = "deepseek-ai/DeepSeek-V3"

  aggregator_system_prompt = """You have been provided with a set of responses from various open-source models to the latest user query.
  Your task is to synthesize these responses into a single, high-quality response. It is crucial to critically evaluate the information
  provided in these responses, recognizing that some of it may be biased or incorrect. Your response should not simply replicate the
  given answers but should offer a refined, accurate, and comprehensive reply to the instruction. Ensure your response is well-structured,
  coherent, and adheres to the highest standards of accuracy and reliability.

  Responses from models:"""


  async def main():
      answer, intermediate_reponses = await parallel_workflow(
          prompt=user_prompt,
          proposer_models=reference_models,
          aggregator_model=aggregator_model,
          aggregator_prompt=aggregator_system_prompt,
      )

      for i, response in enumerate(intermediate_reponses):
          print(f"Intermetidate Response {i+1}:\n\n{response}\n")

      print(f"Final Answer: {answer}\n")


  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}
  const referenceModels = [
    "microsoft/WizardLM-2-8x22B",
    "Qwen/Qwen2.5-72B-Instruct-Turbo",
    "google/gemma-2-27b-it",
    "meta-llama/Llama-3.3-70B-Instruct-Turbo",
  ];

  const userPrompt = dedent`
    Jenna and her mother picked some apples from their apple farm.
    Jenna picked half as many apples as her mom.

    If her mom got 20 apples, how many apples did they both pick?
  `;

  const aggregatorModel = "deepseek-ai/DeepSeek-V3";

  const aggregatorSystemPrompt = dedent`
    You have been provided with a set of responses from various
    open-source models to the latest user query. Your task is to
    synthesize these responses into a single, high-quality response.
    It is crucial to critically evaluate the information provided in
    these responses, recognizing that some of it may be biased or incorrect.
    Your response should not simply replicate the given answers but
    should offer a refined, accurate, and comprehensive reply to the
    instruction. Ensure your response is well-structured, coherent, and
    adheres to the highest standards of accuracy and reliability.

    Responses from models:
  `;

  async function main() {
    const [answer, intermediateResponses] = await parallelWorkflow(
      userPrompt,
      referenceModels,
      aggregatorModel,
      aggregatorSystemPrompt,
    );
    for (const response of intermediateResponses) {
      console.log(
        `## Intermediate Response: ${intermediateResponses.indexOf(response) + 1}:\n`,
      );
      console.log(`${response}\n`);
    }
    console.log(`## Final Answer:`);
    console.log(`${answer}\n`);
  }

  main();
  ```
</CodeGroup>

## Use cases

* Using one LLM to answer a user's question, while at the same time using another to screen the question for inappropriate content or requests.
* Reviewing a piece of code for both security vulnerabilities and stylistic improvements at the same time.
* Analyzing a lengthy document by dividing it into sections and assigning each section to a separate LLM for summarization, then combining the summaries into a comprehensive overview.
* Simultaneously analyzing a text for emotional tone, intent, and potential biases, with each aspect handled by a dedicated LLM.
* Translating a document into multiple languages at the same time by assigning each language to a separate LLM, then aggregating the results for multilingual output.

## Subtask Agent Workflow

An alternate and useful parallel workflow. This workflow begins with an LLM breaking down the task into subtasks that are dynamically determined based on the input. These subtasks are then processed in parallel by multiple worker LLMs. Finally, the orchestrator LLM synthesizes the workers' outputs into the final result.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=3033de4327c6f5acedc35d5ff47290c4" alt="" data-og-width="4118" width="4118" data-og-height="1793" height="1793" data-path="images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5759ca55b49d3542d6c156be30ce9424 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a262112478ac7b9e3c8743aae475412d 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=fac6dd08237e1ac86ef86aa6e5d1c0e6 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=93838a2ed1523e39f29aeb8bdfa6fda9 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=74ed0c8802e44e210036ef08dbfdbd95 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=bdf28b0ebd4db4539215318034cec012 2500w" />
</Frame>

<Info>
  ### Subtask Workflow Cookbook

  For a more detailed walk-through refer to the [notebook here](https://togetherai.link/agent-recipes-deep-dive-orchestrator) .
</Info>

## Setup Client & Helper Functions

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import json
  import together
  from pydantic import ValidationError
  from together import AsyncTogether, Together

  client = Together()
  async_client = AsyncTogether()


  # The function below will call the reference LLMs in parallel
  async def run_llm_parallel(
      user_prompt: str,
      model: str,
      system_prompt: str = None,
  ):
      """Run a single LLM call with a reference model."""
      for sleep_time in [1, 2, 4]:
          try:
              messages = []
              if system_prompt:
                  messages.append({"role": "system", "content": system_prompt})

              messages.append({"role": "user", "content": user_prompt})

              response = await async_client.chat.completions.create(
                  model=model,
                  messages=messages,
                  temperature=0.7,
                  max_tokens=2000,
              )
              break
          except together.error.RateLimitError as e:
              print(e)
              await asyncio.sleep(sleep_time)
      return response.choices[0].message.content


  def JSON_llm(user_prompt: str, schema, system_prompt: str = None):
      try:
          messages = []
          if system_prompt:
              messages.append({"role": "system", "content": system_prompt})

          messages.append({"role": "user", "content": user_prompt})

          extract = client.chat.completions.create(
              messages=messages,
              model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
              response_format={
                  "type": "json_object",
                  "schema": schema.model_json_schema(),
              },
          )
          return json.loads(extract.choices[0].message.content)

      except ValidationError as e:
          error_message = f"Failed to parse JSON: {e}"
          print(error_message)
  ```

  ```typescript TypeScript theme={null}
  import assert from "node:assert";
  import Together from "together-ai";
  import { Schema } from "zod";
  import zodToJsonSchema from "zod-to-json-schema";

  const client = new Together();

  export async function runLLM(userPrompt: string, model: string) {
    const response = await client.chat.completions.create({
      model,
      messages: [{ role: "user", content: userPrompt }],
      temperature: 0.7,
      max_tokens: 4000,
    });

    const content = response.choices[0].message?.content;
    assert(typeof content === "string");
    return content;
  }

  export async function jsonLLM<T>(
    userPrompt: string,
    schema: Schema<T>,
    systemPrompt?: string,
  ) {
    const messages: { role: "system" | "user"; content: string }[] = [];
    if (systemPrompt) {
      messages.push({ role: "system", content: systemPrompt });
    }

    messages.push({ role: "user", content: userPrompt });

    const response = await client.chat.completions.create({
      model: "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
      messages,
      response_format: {
        type: "json_object",
        // @ts-expect-error Expected error
        schema: zodToJsonSchema(schema, {
          target: "openAi",
        }),
      },
    });

    const content = response.choices[0].message?.content;
    assert(typeof content === "string");

    return schema.parse(JSON.parse(content));
  }
  ```
</CodeGroup>

## Implement Workflow

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import json
  from pydantic import BaseModel, Field
  from typing import Literal, List

  ORCHESTRATOR_PROMPT = """
  Analyze this task and break it down into 2-3 distinct approaches:

  Task: {task}

  Provide an Analysis:

  Explain your understanding of the task and which variations would be valuable.
  Focus on how each approach serves different aspects of the task.

  Along with the analysis, provide 2-3 approaches to tackle the task, each with a brief description:

  Formal style: Write technically and precisely, focusing on detailed specifications
  Conversational style: Write in a friendly and engaging way that connects with the reader
  Hybrid style: Tell a story that includes technical details, combining emotional elements with specifications

  Return only JSON output.
  """

  WORKER_PROMPT = """
  Generate content based on:
  Task: {original_task}
  Style: {task_type}
  Guidelines: {task_description}

  Return only your response:
  [Your content here, maintaining the specified style and fully addressing requirements.]
  """

  task = """Write a product description for a new eco-friendly water bottle.
  The target_audience is environmentally conscious millennials and key product features are: plastic-free, insulated, lifetime warranty
  """


  class Task(BaseModel):
      type: Literal["formal", "conversational", "hybrid"]
      description: str


  class TaskList(BaseModel):
      analysis: str
      tasks: List[Task] = Field(..., default_factory=list)


  async def orchestrator_workflow(
      task: str,
      orchestrator_prompt: str,
      worker_prompt: str,
  ):
      """Use a orchestrator model to break down a task into sub-tasks and then use worker models to generate and return responses."""

      # Use orchestrator model to break the task up into sub-tasks
      orchestrator_response = JSON_llm(
          orchestrator_prompt.format(task=task),
          schema=TaskList,
      )

      # Parse orchestrator response
      analysis = orchestrator_response["analysis"]
      tasks = orchestrator_response["tasks"]

      print("\n=== ORCHESTRATOR OUTPUT ===")
      print(f"\nANALYSIS:\n{analysis}")
      print(f"\nTASKS:\n{json.dumps(tasks, indent=2)}")

      worker_model = ["meta-llama/Llama-3.3-70B-Instruct-Turbo"] * len(tasks)

      # Gather intermediate responses from worker models
      return tasks, await asyncio.gather(
          *[
              run_llm_parallel(
                  user_prompt=worker_prompt.format(
                      original_task=task,
                      task_type=task_info["type"],
                      task_description=task_info["description"],
                  ),
                  model=model,
              )
              for task_info, model in zip(tasks, worker_model)
          ]
      )
  ```

  ````bash Bash theme={null}
  import dedent from "dedent";
  import { z } from "zod";

  function ORCHESTRATOR_PROMPT(task: string) {
    return dedent`
      Analyze this task and break it down into 2-3 distinct approaches:

      Task: ${task}

      Provide an Analysis:

      Explain your understanding of the task and which variations would be valuable.
      Focus on how each approach serves different aspects of the task.

      Along with the analysis, provide 2-3 approaches to tackle the task, each with a brief description:

      Formal style: Write technically and precisely, focusing on detailed specifications
      Conversational style: Write in a friendly and engaging way that connects with the reader
      Hybrid style: Tell a story that includes technical details, combining emotional elements with specifications

      Return only JSON output.
    `;
  }

  function WORKER_PROMPT(
    originalTask: string,
    taskType: string,
    taskDescription: string,
  ) {
    return dedent`
      Generate content based on:
      Task: ${originalTask}
      Style: ${taskType}
      Guidelines: ${taskDescription}

      Return only your response:
      [Your content here, maintaining the specified style and fully addressing requirements.]
    `;
  }

  const taskListSchema = z.object({
    analysis: z.string(),
    tasks: z.array(
      z.object({
        type: z.enum(["formal", "conversational", "hybrid"]),
        description: z.string(),
      }),
    ),
  });

  /*
    Use an orchestrator model to break down a task into sub-tasks,
    then use worker models to generate and return responses.
  */
  async function orchestratorWorkflow(
    originalTask: string,
    orchestratorPrompt: (task: string) => string,
    workerPrompt: (
      originalTask: string,
      taskType: string,
      taskDescription: string,
    ) => string,
  ) {
    // Use orchestrator model to break the task up into sub-tasks
    const { analysis, tasks } = await jsonLLM(
      orchestratorPrompt(originalTask),
      taskListSchema,
    );

    console.log(dedent`
      ## Analysis:
      ${analysis}

      ## Tasks:
    `);
    console.log("```json", JSON.stringify(tasks, null, 2), "\n```\n");

    const workerResponses = await Promise.all(
      tasks.map(async (task) => {
        const response = await runLLM(
          workerPrompt(originalTask, task.type, task.description),
          "meta-llama/Llama-3.3-70B-Instruct-Turbo",
        );

        return { task, response };
      }),
    );

    return workerResponses;
  }
  ````
</CodeGroup>

## Example Usage

<CodeGroup>
  ```typescript TypeScript theme={null}
  async function main() {
    const task = `Write a product description for a new eco-friendly water bottle.
      The target_audience is environmentally conscious millennials and key product
      features are: plastic-free, insulated, lifetime warranty
    `;

    const workerResponses = await orchestratorWorkflow(
      task,
      ORCHESTRATOR_PROMPT,
      WORKER_PROMPT,
    );

    console.log(
      workerResponses
        .map((w) => `## WORKER RESULT (${w.task.type})\n${w.response}`)
        .join("\n\n"),
    );
  }

  main();
  ```

  ```typescript typescript theme={null}
  async function main() {
    const task = `Write a product description for a new eco-friendly water bottle.
      The target_audience is environmentally conscious millennials and key product
      features are: plastic-free, insulated, lifetime warranty
    `;

    const workerResponses = await orchestratorWorkflow(
      task,
      ORCHESTRATOR_PROMPT,
      WORKER_PROMPT,
    );

    console.log(
      workerResponses
        .map((w) => `## WORKER RESULT (${w.task.type})\n${w.response}`)
        .join("\n\n"),
    );
  }

  main();
  ```
</CodeGroup>

## Use cases

* Breaking down a coding problem into subtasks, using an LLM to generate code for each subtask, and making a final LLM call to combine the results into a complete solution.
* Searching for data across multiple sources, using an LLM to identify relevant sources, and synthesizing the findings into a cohesive answer.
* Creating a tutorial by splitting each section into subtasks like writing an introduction, outlining steps, and generating examples. Worker LLMs handle each part, and the orchestrator combines them into a polished final document.
* Dividing a data analysis task into subtasks like cleaning the data, identifying trends, and generating visualizations. Each step is handled by separate worker LLMs, and the orchestrator integrates their findings into a complete analytical report.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt