# Source: https://dev.writer.com/home/prompting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Write effective prompts

> Master prompting fundamentals and advanced techniques. Learn directive writing, context inclusion, few-shot prompting, and chain-of-thought reasoning.

export const PromptComponent = ({prompt}) => <div>
    <p class="prompts">{prompt}</p>
  </div>;

This guide covers the [fundamentals](/home/prompting#fundamentals) behind prompting strategies and discusses some [advanced techniques](/home/prompting#advanced-techniques).

For in-depth information on prompting, see the Writer [prompt crafting guide](https://writer.com/guides/prompt-crafting/).

## Fundamentals

<CardGroup cols={2}>
  <Card title="Directive writing" icon="pencil" color="currentcolor">
    Be direct and to the point:

    <br />

    <br />

    <PromptComponent prompt={`Write a short summary of the article titled "The Impact of Artificial Intelligence on Employment"`} />
  </Card>

  <Card title="Inclusive prompts" icon="users" color="currentcolor">
    Include your audience in your prompt:

    <br />

    <br />

    <PromptComponent prompt={`Explain the implications of the recent changes in tax laws for small business owners in California.`} />
  </Card>

  <Card title="Structured formatting" icon="hashtag" color="currentcolor">
    Format your prompt with *### Instruction ###*, followed by *### Question
    \###*:

    <br />

    <br />

    <p class="prompts">
      <strong>### Instruction ###</strong> <br />Write a poem in the style of
      Robert Frost. <br />

      <br />

      <strong>### Question ###</strong>
      <br /> What's the poem about?
    </p>
  </Card>

  <Card title="Task breakdown" icon="list-check" color="currentcolor">
    Break down complicated tasks into multiple prompts:

    <br />

    <br />

    <PromptComponent prompt={`First, provide a brief overview of derivatives. Then, explain how it's related to credit risk.`} />
  </Card>

  <Card title="Positive language" icon="thumbs-up" color="currentcolor">
    Use directives like "do" instead of "don't":

    <br />

    <br />

    <PromptComponent prompt={`Do provide an analysis of the potential benefits and drawbacks of using renewable energy sources in the manufacturing industry, focusing on the economic, environmental, and social impacts.`} />
  </Card>

  <Card title="Mandatory instructions" icon="triangle-exclamation" color="currentcolor">
    Use phrases like *You MUST*:

    <br />

    <br />

    <PromptComponent prompt={`You must provide a step-by-step guide to setting up a WordPress website, including domain registration, web hosting, and content creation.`} />
  </Card>

  <Card title="Penalty warning" icon="gavel" color="currentcolor">
    Use phrases like *You'll be penalized*:

    <br />

    <br />

    <PromptComponent prompt={`You’ll be penalized if you don't include at least three different methods for solving the following math problem: Find the area of a circle with a radius of 5 units.`} />
  </Card>

  <Card title="Natural responses" icon="comments" color="currentcolor">
    Request a simple response:

    <br />

    <br />

    <PromptComponent prompt={`Please provide a brief explanation of the difference between a virus and a bacterium, answering in a natural, human-like manner.`} />
  </Card>

  <Card title="Unbiased descriptions" icon="scale-balanced" color="currentcolor">
    Make sure that your answer is unbiased and doesn’t rely on stereotype:

    <br />

    <br />

    <PromptComponent prompt={`Please describe the cultural significance of sushi in Japan, making sure that your answer is unbiased.`} />
  </Card>

  <Card title="Educational writing" icon="book-open" color="currentcolor">
    To write an essay, text, paragraph, article, or any detailed text:

    <br />

    <br />

    <PromptComponent prompt={`Write a detailed essay for me on the history of the monetary policy.`} />
  </Card>

  <Card title="Style consistency" icon="typewriter" color="currentcolor">
    Improve the tone of the text to make the writing style more
    professional:

    <br />

    <br />

    <PromptComponent prompt={`Revise the following paragraph to improve its grammar and vocabulary, but make sure that the writing style remains formal.`} />
  </Card>

  <Card title="Creative writing" icon="pen-fancy" color="currentcolor">
    I'll give you the beginning of a story. Finish it and keep the flow
    consistent:

    <br />

    <br />

    <PromptComponent prompt={`As the sun began to set, the sky turned a deep shade of orange. The birds returned to their nests, and the crickets started to chirp.`} />
  </Card>

  <Card title="Linguistic mimicry" icon="copy" color="currentcolor">
    Use the same language as the following paragraph to explain the importance
    of exercise:

    <br />

    <br />

    <PromptComponent prompt={`The practice of meditation has been around for thousands of years. It's a way to calm the mind and body, and it can be done almost anywhere.`} />
  </Card>

  <Card title="Precise instructions" icon="ruler" color="currentcolor">
    Clearly state the requirements that the model must follow to produce
    content, in the form of keywords or instructions. <br />

    <br />

    <PromptComponent prompt={`Write a short summary of the article titled 'The Impact of AI on Employment'. Ensure that the summary is no longer than 150 words and includes the main arguments.`} />
  </Card>
</CardGroup>

## Advanced techniques

<CardGroup cols={1}>
  <Card title="Example driven prompts" icon="check" color="currentcolor">
    Use example-driven (few-shot) prompting:

    <br />

    <p class="prompts">
      Provide a list of idioms in English, along with their meanings and example
      sentences.

      <br />

      Here is an example for the output: <br />

      <br />

      <strong>An idiom</strong>: 'Break a leg' <br />
      <strong>Meaning</strong>: Good luck <br />
      <strong>Example sentence</strong>: 'I'm sure you'll do great in your interview.
      Break a leg!'
    </p>
  </Card>

  <Card title="Chain-of-thought Prompts" icon="thought-bubble" color="currentcolor">
    Combine chain-of-thought (CoT) prompts with few-shot prompts:

    <br />

    <p class="prompts">
      <strong>System instruction:</strong> Create a product detail page for a
      fictional innovative smartphone by a retailer known as "TechTrend
      Electronics."

      <br />

      <strong>Prompt 1:</strong> Start by describing the unique features of the smartphone,
      such as its solar-powered battery, triple-lens camera system, and foldable
      screen technology.

      <br />

      <strong>Prompt 2:</strong> Next, outline the benefits of these features
      for users, like extended battery life, exceptional photo quality, and
      enhanced device portability.

      <br />

      <strong>Prompt 3:</strong> Conclude with crafting compelling product descriptions
      and a call-to-action that entices customers to make a purchase during the upcoming
      holiday sale.
    </p>
  </Card>

  <Card title="Delimited prompts" icon="text" color="currentcolor">
    Use delimiters to structure text:

    <br />

    <p class="prompts">
      Summarize a series of healthcare claims documents for a fictional
      healthcare company, 'HealthFirst Solutions', using the following delimiter `\n`
      to separate different sections of the summary:

      <br />

      <strong>Claim Number:</strong> 123456789 `\n` <br />
      <strong>Date of Service:</strong> January 1, 2024 `\n` <br />
      <strong>Diagnosis:</strong> Acute sinusitis `\n` <br />
      <strong>Total Claimed:</strong> \$300 `\n` <br />
      <strong>Status:</strong> Pending review `\n` <br />
    </p>
  </Card>
</CardGroup>
