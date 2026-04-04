# Source: https://braintrust.dev/docs/best-practices/scorers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Writing scorers

To accurately evaluate the quality of your AI systems, you need to write good scorers. Scorers allow you to evaluate the output of LLMs based on a set of criteria. These can include both heuristics (expressed as code) or prompts (expressed as LLM-as-a-judge). Scorers help you assign a performance score between 0 and 100% to assess how well the AI outputs match expected results. While many scorers are available out of the box through the open-source [autoevals](https://github.com/braintrustdata/autoevals) library, most create their own custom scorers based on their specific use case.

This guide outlines a structured approach and best practices, based on [insights from Loom's implementation](https://www.braintrust.dev/blog/loom), to help you build reliable scorers tailored to your AI features.

## Mental models

Scorers are a crucial element of both offline and online evaluations:

* Offline evaluations are used to proactively identify and resolve issues before deployment.
* Online evaluation involves running scorers on live requests to diagnose problems, monitor performance, and capture user feedback in real-time.

Writing good scorers is important for both parts of the LLM software development lifecycle. Any scorer you create for offline evaluation can also [be run on a live request](/core/experiments/write#online-evaluation).

<Steps>
  <Step title="Define clear criteria">
    Before beginning to write scorers, clearly identify the criteria users will use to evaluate the generated output.
    You can start by defining:

    * **Input**: The data or prompt given to the model.
    * **Output**: The expected result from the model.

    Then, specify traits that users would expect and value in the output. Think of this like the product requirements you put together when developing a new feature in your product. Common traits might include:

    * Accuracy of information
    * Conciseness
    * Clarity and readability
    * Appropriate tone
    * Correct grammar and spelling
    * Bias and safety
    * Adherence to specific formatting

    <Note>
      In more complex, agentic workflows, it's possible that each step will have its own inputs and outputs. This just means that you might have different criteria, and therefore different scorers, for each step. Braintrust will automatically aggregate scores across spans for each trace.
    </Note>
  </Step>

  <Step title="Apply common quality checks">
    You will certainly have success criteria that are unique to your product and use case, but many evaluation scenarios also benefit from common quality checks. Check out this list of common checks, and verify if they apply to your use case:

    * **Relevance**: Does the output reflect the source input accurately?
    * **Readability**: Is the language clear and easy to understand?
    * **Structure and formatting**: Does the output follow required formats, such as structured lists or JSON schemas?
    * **Factuality**: Is the provided information correct and verifiable?
    * **Safety**: Is the content free from biased or offensive language?
    * **Language accuracy**: Does the output match the requested language?

    Then, consider if you'd need to tailor any of these checks specifically for your application. For example, you might want a specific structure or formatting, or be pulling information from an external resource. Getting as specific as possible in determining what you're looking for improves the reliability of your application.
  </Step>

  <Step title="Automate with code-based checks">
    Where possible, implement deterministic quality checks through code-based scoring functions. Code-based scorers are reliable and consistent, execute quickly and efficiently, and reduce variability from human or model judgments. Code-based scorers in Braintrust can be written in either TypeScript or Python, via either the UI or SDK. They return a score between `0` and `1`.

    Some examples of code-based checks include:

    * Verifying valid JSON structure

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      // Returns 1 if output is valid JSON, else 0
      function handler({
        output,
        expected,
      }: {
        output: string;
        expected: string | null;
      }): number {
        if (expected == null) return 0;
        try {
          JSON.parse(output);
          return 1;
        } catch {
          return 0;
        }
      }
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import json
      from typing import Optional

      # Returns 1.0 if output is valid JSON, else 0.0
      def handler(
          output: str,
          expected: Optional[str],
      ) -> float:
          if expected is None:
              return 0.0
          try:
              json.loads(output)
              return 1.0
          except json.JSONDecodeError:
              return 0.0
      ```
    </CodeGroup>

    * Checking text length constraints (for example, less than 100 characters)

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      // Enter handler function that returns a score between 0 and 1
      function handler({
        output,
        expected,
      }: {
        output: string;
        expected: string | null;
      }): number {
        if (expected === null) return 0;
        return output.length <= 100 ? 1 : 0;
      }
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      from typing import Optional

      # Enter handler function that returns a score between 0 and 1
      def handler(
          output: str,
          expected: Optional[str],
      ) -> float:
          if expected is None:
              return 0.0
          return 1.0 if len(output) <= 100 else 0.0
      ```
    </CodeGroup>

    * Ensuring outputs match predefined patterns (for example, a bullet-point list of exactly three items)

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      // Enter handler function that returns a score between 0 and 1
      function handler({
        output,
        expected,
      }: {
        output: string;
        expected: string | null;
      }): number {
        if (expected === null) return 0;
        const bullets = output.match(/^- .+/gm) || [];
        return bullets.length === 3 ? 1 : 0;
      }
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import re
      from typing import Optional

      # Enter handler function that returns a score between 0 and 1
      def handler(
          output: str,
          expected: Optional[str],
      ) -> float:
          if expected is None:
              return 0.0
          bullets = re.findall(r"^- .+", output, flags=re.MULTILINE)
          return 1.0 if len(bullets) == 3 else 0.0
      ```
    </CodeGroup>

    <Note>
      Schema validation libraries like `pydantic` or `jsonschema` are useful for formatting requirements.
    </Note>
  </Step>

  <Step title="Develop and align LLM-based scorers">
    For more subjective and nuanced criteria that code can not capture, like tone appropriateness or creativity, you can use LLM-based scorers.

    When building these, it's important to:

    * Design judge prompts with explicit instructions, examples of good vs. bad outputs, and a clear scoring rubric
    * Use chain of thought to understand why the model is assigning a specific score
    * Use more granular scoring when necessary
    * Choose the model that is best suited for the evaluation, which may be different from the model used in the task

    For example:

    ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    const promptTemplate: string = `
    You are an expert technical writer who helps assess how effectively an open source product team generates a changelog based on git commits since the last release. Analyze commit messages and determine if the changelog is comprehensive, accurate, and informative.

    Assess the comprehensiveness of the changelog and select one of the following options. List out which commits are missing from the changelog if it is not comprehensive.
    a) The changelog is comprehensive and includes all relevant commits
    b) The changelog is mostly comprehensive but is missing a few commits
    c) The changelog includes changes that are not in commit messages
    d) The changelog is incomplete and not informative

    Output format: Return your evaluation as a JSON object with the following four keys:
    1. Score: A score between 0 and 1 based on how well the input meets the criteria defined in the rubric above.
    2. Missing commits: A list of all missing information.
    3. Extra entries: A list of any extra information that isn't part of the commit
    4. Rationale: A brief 1-2 sentence explanation for your scoring decision.

    ---
    EXAMPLE 1
    Input commits:
    - abc123: fix typo in README
    - def456: add JSON parser

    Changelog:
    - Fixed typo in README
    - Added JSON parser

    Evaluation:
    {
      "Score": 1.00,
      "Missing commits": [],
      "Extra entries": [],
      "Rationale": "The changelog covers both commits accurately and includes no unrelated entries."
    }

    ---
    EXAMPLE 2
    Input commits:
    - abc123: fix typo in README
    - def456: add JSON parser
    - ghi789: update CI config

    Changelog:
    - Fixed typo in README
    - Added JSON parser

    Evaluation:
    {
      "Score": 0.75,
      "Missing commits": [
        "ghi789: update CI config"
      ],
      "Extra entries": [],
      "Rationale": "The changelog captures two of three commits but omits the CI config update, making it mostly comprehensive."
    }

    ---
    Now evaluate:
    Input:
    {{input}}

    Changelog:
    {{output}}
    `;
    ```

    When you create your LLM-based scorer, you will assign each choice in the rubric to a specific score between 0 and 1. Binary scoring is often recommended as it's easier to define and creates less confusion among human reviewers during alignment. However, when you need more nuanced evaluation, be sure to clearly explain what each choice score corresponds to like in the example above.

    <Note>
      LLMs can also help you generate good scorer prompts.
    </Note>

    To calibrate your LLM-based scorer, test it on a small but representative dataset that covers edge cases, different user personas, and a good variety of inputs. Compare the results with human spot checks to make sure they are aligned.

    <Note>
      In Braintrust, you can enable [chain of thought](/core/functions/scorers#llm-as-a-judge-scorers) (CoT) with a toggle or flag from the UI or SDK, respectively.
    </Note>
  </Step>

  <Step title="Iterate on your initial set of criteria">
    Scorer development is an ongoing process. After assessing your initial scorers, you should review low-score outputs to identify missing criteria or edge-case behaviors. Based on what you find, you can refine your definitions and add new scorers for uncovered aspects. You can also rerun the calibration step on an expanded example set, and adjust prompts, model providers, or code as needed.

    By tightly coupling development, evaluation, and refinement, you can make sure that your scorers stay aligned with evolving product needs and user inputs.
  </Step>
</Steps>

## Best practices for scorer design

* **Provide clear rationale**: When using language-model-based scorers, enable detailed rationale explanations to understand scoring decisions and refine scorer behavior.
* **Single-aspect scorers**: Create separate scorers for each distinct evaluation aspect, such as accuracy versus style.
* **Weighted scoring**: Use weighted averages when combining scores, prioritizing critical criteria over less important ones.
* **Appropriate scoring scales**: Match the scoring scale to evaluation complexity. Use binary scoring (yes/no) for simple checks and multi-point scales for nuanced assessments.

## Evaluating agents

When evaluating agents, scorers should assess not only individual responses but also overall agent behavior and performance:

* **Goal completion**: Did the agent accomplish the assigned task?
* **Efficiency**: Did the agent complete the task within acceptable resource or time constraints?
* **Interaction quality**: Was the interaction coherent, helpful, and aligned with user expectations?
* **Error handling**: Did the agent handle unexpected situations gracefully and recover effectively?

Consider using simulations or controlled scenarios to thoroughly evaluate agent performance across these dimensions.

<Tip>
  For more information on evaluating agents, check out the [full guide](https://www.braintrust.dev/blog/evaluating-agents).
</Tip>

## Benefits of effective scorers

By following a structured evaluation cycle (define, implement, evaluate, refine), you can:

* Get closer to deterministic model behavior
* Quickly iterate and improve AI features
* Scale evaluations without manual overhead

Reliable scorers are the backbone of high‑quality, user‑aligned AI products.
