# Source: https://braintrust.dev/docs/cookbook/recipes/SpamClassifier.md

# Classifying spam using structured outputs

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/SpamClassifier/SpamClassifier.mdx) by [Ornella Altunyan](https://twitter.com/ornelladotcom) on 2025-02-08</div>

When building AI applications that require consistent, structured responses, you have to decide how to implement structured outputs based on the LLM provider you're using.
Generally, if you're using a model from OpenAI, you'd just use [structured outputs](https://platform.openai.com/docs/guides/structured-outputs).
If you want to use models from Anthropic, however, you'd need to take a different approach and use their [Tool](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) feature, or use prompt engineering to get the desired response.

In the [Braintrust Playground](/core/playground), it's easy to use either AI provider with structured outputs by simply selecting **Structured output** from the output dropdown menu and defining a JSON schema. If you use the [AI proxy](/guides/proxy), you can also use OpenAI SDKs in your code to speak structured outputs to Anthropic models. Structured outputs work in Braintrust for most LLMs.

In this cookbook, we'll explore how to use structured outputs and Anthropic models in the playground to classify spam in text messages.

## Getting started

Before getting started, make sure you have a [Braintrust account](https://www.braintrust.dev/signup) and an API key for [Anthropic](https://console.anthropic.com/). Make sure to plug the Anthropic key into your Braintrust account's [AI providers](https://www.braintrust.dev/app/settings?subroute=secrets) configuration. In this cookbook, we'll be working entirely in the Braintrust UI, so there's no need for a separate code editor.

## Setting up the playground

The first thing you'll need to do is create a new project. Name your project "Spam classifier." Then, navigate to **Evaluations** > **Playgrounds** and create a new playground. In Braintrust, a playground is a tool for exploring, comparing, and evaluating prompts.

## Importing a dataset

Download the [dataset](https://github.com/braintrustdata/braintrust-cookbook/tree/main/examples/SpamClassifier/spam-dataset.csv) of text messages from GitHub– it is a `.csv` file with two columns, **message** and **is\_spam**. Inside your playground, select **Dataset**, then **Upload dataset**, and upload the CSV file. Using drag and drop, assign the CSV columns to dataset fields. The input column corresponds to **message**, and the expected column should be **is\_spam**. Then, select **Import**.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/import-dataset.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=1aee792bfbfe20b66bd945dc96d7c52f" alt="Import dataset" data-og-width="2402" width="2402" data-og-height="1648" height="1648" data-path="cookbook/assets/SpamClassifier/import-dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/import-dataset.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=78ca2ec20700c45fd623354f390f8b4f 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/import-dataset.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=5cda57784103b4aa1fea774d2391fdca 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/import-dataset.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=1913d7c944e622fb8608a41b21a38095 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/import-dataset.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=7f8092a60cb52210f84d6b5135df89e4 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/import-dataset.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=cb0bfaf700c73fdf07ce86f3fbf1783d 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/import-dataset.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=9a1261cc76001bbd326591ecaa8ed32a 2500w" />

## Writing a prompt

Recall that for this cookbook, we're going to be using Anthropic models. Choose **Claude 3.5 Sonnet Latest** or your favorite Anthropic model from the model dropdown.

Then, type this for your system prompt:

```
Identify whether or not the {{input}} is spam.
```

Prompts can use [mustache](https://mustache.github.io/mustache.5.html) templating syntax to refer to variables. In this case, the input corresponds to the text in the text message.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/write-prompt.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=4e888ad1a6c32031d717de9b36c3472a" alt="Write prompt" data-og-width="2396" width="2396" data-og-height="1556" height="1556" data-path="cookbook/assets/SpamClassifier/write-prompt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/write-prompt.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=4a7cbd45017e2b6426b1fd7fa19729dd 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/write-prompt.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=406a5a0ce4697e6cc4353fb2c7c0c130 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/write-prompt.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=6ec732a292b3348f74ced332ce64bf64 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/write-prompt.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=5c27f85a38a291c69f77ffe57c7c1048 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/write-prompt.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=6e2c9df7e19dac89f0adbc3338c1ab13 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/write-prompt.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=c9c23585f2419a6c533e74226f8ce292 2500w" />

### Defining a structured output

Select **Structured output** from the output dropdown menu and define the JSON schema `isSpam` for the structured output of the prompt, using this code for the schema definition:

```YAML  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
type: object
required:
  - is_spam
properties:
  is_spam:
    type: boolean
    description: Returns true if the text message is spam, otherwise false.
additionalProperties: false
```

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/structured-output.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=68462e03fc74a96b3a80ab9bee7f1bc3" alt="Define structured output" data-og-width="2396" width="2396" data-og-height="1656" height="1656" data-path="cookbook/assets/SpamClassifier/structured-output.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/structured-output.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=36359901e5f8098862446fe2e4291ef7 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/structured-output.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=10d48c902eab5d4481109aefabf6af93 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/structured-output.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=5377b90319cd2afa71619bf5feb4a824 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/structured-output.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=15970edff52325dfd68298e5cf1d0317 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/structured-output.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=4af4cdeb5b2ddbcb085cc5b42a8e1965 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/structured-output.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=bacd345f9da2e24992f4452acf892780 2500w" />

## Running the prompt

Selecting **Run** will run the LLM call on each input and generate an output. The output of each call will be in the format we created:

```JSON  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{"is_spam": false}
```

or

```JSON  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{"is_spam": true}
```

At this point, we've successfully generated a structured output response from an Anthropic model without using Tools!

## Running an eval

To close the loop, let's run an evaluation. To run an eval, you need three things:

* **Data**: a set of examples to test your application on
* **Task**: the AI function you want to test (any function that takes in an input and returns an output)
* **Scores**: a set of scoring functions that take an input, output, and optional expected value and compute a score

In this example, the Data is the dataset you uploaded, and the Task is the prompt you created, so all we need is a scoring function.

### Creating a custom scorer

A scoring function allows you to compare the expected output of a task to the actual output and produce a score between 0 and 1. Inside your playground, select **Scorers** to choose from several types of scoring functions. For this example, since we have the expected classifications from the dataset, we can create a scoring function that measures whether or not the LLM output matches the expected classification.

Select **Scorers**, then **Create custom scorer**. We'll create a custom TypeScript scorer called "Correctness" that compares the value of `output.is_spam` to the expected classification:

```TypeScript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
function handler({
  output,
  expected
}: {
  output: boolean;
  expected: boolean | string;
}): number {
  if (expected === null) return 0;

  // Convert 'expected' to a boolean if it's a string
  const expectedBool = (expected === 'true') ? true : (expected === 'false') ? false : expected;

  return output.is_spam === expectedBool ? 1 : 0;
}
```

Now that you have your dataset, prompt, and scoring function set up, you can select **+ Experiment** to run a full evaluation.

<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/create-experiment.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=fae3103e10a22f196c60489ca6f8d55f" alt="Create experiment" data-og-width="2374" width="2374" data-og-height="1394" height="1394" data-path="cookbook/assets/SpamClassifier/create-experiment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/create-experiment.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=b8ff5539b9dc3b5bf27f287c56d779b3 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/create-experiment.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=deaec0874a5f61b20a0f7e4e4a66f0b5 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/create-experiment.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=43ab24c6701b8bee136fa4dbb31de4a3 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/create-experiment.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=7a49d97d25b84a3ec1ae3543a7a09197 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/create-experiment.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=f7e369ddf985cec0991de38cc9bac2b3 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/create-experiment.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=f8f432e27a2b3e8da1f4c1d04dfd6285 2500w" />

### Interpreting your results

Navigate to the **Experiments** page to view your evaluation.
<img src="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/eval.png?fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=0d356c0adc04088311b795aee057adb5" alt="Eval" data-og-width="2394" width="2394" data-og-height="1748" height="1748" data-path="cookbook/assets/SpamClassifier/eval.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/eval.png?w=280&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=cfb1aeb54f91b737289abe5cefbf01b1 280w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/eval.png?w=560&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=1f8e66c4a64fad65e941dc333e6c1d00 560w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/eval.png?w=840&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=0df47cdfe0f4ba6f3a8ba5074ecb1cb1 840w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/eval.png?w=1100&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=b24c3ffa593307577af183d6ad1c35fa 1100w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/eval.png?w=1650&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=4e4296fd30e48388ba411f370de93e94 1650w, https://mintcdn.com/braintrust/cnpybiCnmDJAdQWI/cookbook/assets/SpamClassifier/eval.png?w=2500&fit=max&auto=format&n=cnpybiCnmDJAdQWI&q=85&s=b221dfcc8283de254a7c1c1f2f9975ba 2500w" />

Examine the scores generated by your evals. If you notice that some of your outputs did not match what was expected, you can tweak your prompt directly in the UI until it consistently produces high-quality outputs.

If changing the prompt doesn't yield the desired results, you can experiment with different models. Since most models have structured output capabilities in Braintrust, this is as simple as choosing a different model from the dropdown menu in a prompt. As you iterate on your prompt, you can run more experiments and compare results.

## Next steps

In addition to changing your prompt definition and model, you can also:

* Add more [custom scorers](/core/functions/scorers#custom-scorers)
* Use a larger or more custom [dataset](/core/datasets)
* Write more complex [structured output](/core/functions/prompts#structured-outputs) JSON schema


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt