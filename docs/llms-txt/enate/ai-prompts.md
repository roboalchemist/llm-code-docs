# Source: https://docs.enate.net/enate-help/enateai/enateai/enateai-ai-analyst/ai-prompts.md

# AI Prompts

## Sample AI Prompts

#### Enate AI Analyst Sample Prompts

Here are some specific sample business scenarios where EnateAI's AI Analyst can be used. For each, the business scenario is given, along with sample input and detailed prompt texts to add into 'Instructions for AI' in your Prompts:

* [**Bank File Reconciliation**](https://docs.enate.net/enate-help/enateai/enateai/enateai-ai-analyst/ai-prompts/bank-file-reconciliation)
* [**Investment Case Content Creation**](https://docs.enate.net/enate-help/enateai/enateai/enateai-ai-analyst/ai-prompts/investment-case-content-creation)
* [**Credit Card Statement Reconciliation**](https://docs.enate.net/enate-help/enateai/enateai/enateai-ai-analyst/ai-prompts/credit-card-statement-reconciliation)

Many more sample prompts will be added over the coming weeks and months

#### More General AI Prompt samples to explore

Here are some [**more general examples of AI Prompts**](https://platform.openai.com/examples) from OpenAI to explore. These give a much wider view of the possibilities available with AI prompts beyond focused business situations, but may well be useful to explore 'the art of the possible'.

## AI Prompts - Best Practice

For detailed guides to best practice for prompt engineering with OpenAI, check out these resources:

{% embed url="<https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api>" %}

{% embed url="<https://platform.openai.com/docs/guides/prompt-engineering>" %}

Here are some recommendations for creating more effective prompts to get the output you want

1. [**Write Clear Instructions**](#write-clear-instructions-include-details-to-get-more-relevant-answers) - Include details to get more relevant answers
2. Put working into [**defining an accurate persona to adopt**](#put-working-into-defining-an-accurate-persona-to-adopt)
3. [**Use delimiters**](#use-delimiters-to-clearly-indicate-distinct-parts-of-the-input) to clearly indicate distinct parts of the input
4. [**Split Complex tasks into Simpler subtasks**](#split-complex-tasks-into-simpler-subtasks-specify-the-steps-required-to-complete-the-task) - Specify the steps required to complete the task
5. [**Specify the desired length**](#specify-the-desired-length-of-the-output) of the output

### Write Clear Instructions - Include details to get more relevant answers

In order to get a highly relevant response, make sure that requests provide any important details or context. Otherwise you are leaving it up to the model to guess what you mean.

<table><thead><tr><th width="201">Worse</th><th>Better</th></tr></thead><tbody><tr><td>How do I add numbers in Excel?</td><td>How do I add up a row of dollar amounts in Excel? I want to do this automatically for a whole sheet of rows with all the totals ending up on the right in a column called "Total".</td></tr><tr><td>Who’s president?</td><td>Who was the president of Mexico in 2021, and how frequently are elections held?</td></tr><tr><td>Summarize the meeting notes.</td><td>Summarize the meeting notes in a single paragraph. Then write a markdown list of the speakers and each of their key points. Finally, list the next steps or action items suggested by the speakers, if any.</td></tr></tbody></table>

### Put working into defining an accurate persona to adopt

The persona definition goes a long way to helping give context and suggested style to what the AI model will come up. Time spent adding extra layers to the persona is well spent time.

### Use delimiters to clearly indicate distinct parts of the input

Delimiters like triple quotation marks, section titles, etc. can help demarcate sections of text to be treated differently. Example:

```
Summarize the text delimited by triple quotes.

"""insert text here"""
```

### Split Complex tasks into Simpler subtasks - Specify the steps required to complete the task

Just as it is good practice in software engineering to decompose a complex system into a set of modular components, the same is true of tasks submitted to a language model. Complex tasks tend to have higher error rates than simpler tasks. Furthermore, complex tasks can often be re-defined as a workflow of simpler tasks in which the outputs of earlier tasks are used to construct the inputs to later tasks. Example:

{% code overflow="wrap" %}

```
Use the following step-by-step instructions to respond to user inputs.

Step 1 - The user will provide you with text in triple quotes. Summarize this text in one sentence with a prefix that says "Summary: ".

Step 2 - Translate the summary from Step 1 into Spanish, with a prefix that says "Translation: ".
```

{% endcode %}

### Specify the desired length of the output

You can ask the model to produce outputs that are of a given target length. The targeted output length can be specified in terms of the count of words, sentences, paragraphs, bullet points, etc. Note however that instructing the model to generate a specific number of words does not work with high precision. The model can more reliably generate outputs with a specific number of paragraphs or bullet points. Examples:

```
Summarize the text delimited by triple quotes in 2 paragraphs.

"""insert text here"""
```

is better than

```
Summarize the text delimited by triple quotes in 50 words.

"""insert text here"""
```
