# Source: https://docs.wandb.ai/weave/tutorial-eval.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Build an evaluation

> Learn how to build an evaluation pipeline with Weave Models and Evaluations

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

export const ColabLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="colab-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01.21.03zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z" />
    </svg>
    Try in Colab
  </a>;

<div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap' }}>
  <ColabLink url="https://colab.research.google.com/github/wandb/docs/blob/main/weave/cookbooks/source/build_an_evaluation_pipeline.ipynb" />

  <GitHubLink url="https://github.com/wandb/docs/blob/main/weave/cookbooks/source/build_an_evaluation_pipeline.ipynb" />
</div>

Evaluations help you iterate and improve your applications by testing them against a set of examples after you make changes. Weave provides first-class support for tracking evaluations with [`Model`](/weave/guides/core-types/models) and [`Evaluation`](/weave/guides/core-types/evaluations) classes. The APIs are designed with minimal assumptions, allowing flexibility for a wide array of use cases.

<img src="https://mintcdn.com/wb-21fd5541/aRvhhwVWqlxBzke5/images/evals-hero.png?fit=max&auto=format&n=aRvhhwVWqlxBzke5&q=85&s=7d7466d666ad412ed3916bfab533d118" alt="Evals hero" width="4100" height="2160" data-path="images/evals-hero.png" />

## What you'll learn:

This guide shows you how to:

* Set up a `Model`
* Create a dataset to test an LLM's responses against
* Define a scoring function to compare model output to expected outputs
* Run an evaluation that tests the model against dataset using the scoring function and an additional built-in scorer
* View the results of the evaluation in the Weave UI

## Prerequisites

* A [W\&B account](https://wandb.ai/signup)
* Python 3.8+ or Node.js 18+
* Required packages installed:
  * **Python**: `pip install weave openai`
  * **TypeScript**: `npm install weave openai`
* An [OpenAI API key](https://platform.openai.com/api-keys) set as an environment variable

## Import the necessary libraries and functions

Import the following libraries into your script:

<Tabs>
  <Tab title="Python">
    ```python lines theme={null}
    import json
    import openai
    import asyncio
    import weave
    from weave.scorers import MultiTaskBinaryClassificationF1
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript lines theme={null}
    import * as weave from 'weave';
    import OpenAI from 'openai';
    ```
  </Tab>
</Tabs>

## Build a `Model`

In Weave, [`Models` are objects](/weave/guides/core-types/models) that capture both the behavior of your model/agent (logic, prompt, parameters) and its versioned metadata (parameters, code, micro-config) so you can track, compare, evaluate and iterate reliably.

When you instantiate a `Model`, Weave automatically captures its configuration and behaviors and updates the version when there are changes. This allows you to track its performance over time as you iterate on it.

`Model`s are declared by subclassing `Model` and implementing a `predict` function definition, which takes one example and returns the response.

The following example model uses OpenAI to extract the names, colors, and flavors of alien fruits from sentences sent to it.

<Tabs>
  <Tab title="Python">
    ```python lines {1,5} theme={null}
    class ExtractFruitsModel(weave.Model):
        model_name: str
        prompt_template: str

        @weave.op()
        async def predict(self, sentence: str) -> dict:
            client = openai.AsyncClient()

            response = await client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": self.prompt_template.format(sentence=sentence)}
                ],
            )
            result = response.choices[0].message.content
            if result is None:
                raise ValueError("No response from model")
            parsed = json.loads(result)
            return parsed
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript lines {9} theme={null}
    // Note: weave.Model is not supported in TypeScript yet.
    // Instead, wrap your model-like function with weave.op

    import * as weave from 'weave';
    import OpenAI from 'openai';

    const openaiClient = new OpenAI();

    const model = weave.op(async function myModel({datasetRow}) {
      const prompt = `Extract fields ("fruit": <str>, "color": <str>, "flavor") from the following text, as json: ${datasetRow.sentence}`;
      const response = await openaiClient.chat.completions.create({
        model: 'gpt-3.5-turbo',
        messages: [{ role: 'user', content: prompt }],
        response_format: { type: 'json_object' }
      });
      return JSON.parse(response.choices[0].message.content);
    });
    ```
  </Tab>
</Tabs>

The `ExtractFruitsModel` class inherits from (or subclasses) `weave.Model` so that Weave can track the instantiated object. `@weave.op` decorates the predict function to track its inputs and outputs.

You can instantiate `Model` objects like this:

<Tabs>
  <Tab title="Python">
    ```python lines theme={null}
    # Set your team and project name
    weave.init('<team-name>/eval_pipeline_quickstart')

    model = ExtractFruitsModel(
        model_name='gpt-3.5-turbo-1106',
        prompt_template='Extract fields ("fruit": <str>, "color": <str>, "flavor": <str>) from the following text, as json: {sentence}'
    )

    sentence = "There are many fruits that were found on the recently discovered planet Goocrux. There are neoskizzles that grow there, which are purple and taste like candy."

    print(asyncio.run(model.predict(sentence)))
    # if you're in a Jupyter Notebook, run:
    # await model.predict(sentence)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    await weave.init('eval_pipeline_quickstart');

    const sentence = "There are many fruits that were found on the recently discovered planet Goocrux. There are neoskizzles that grow there, which are purple and taste like candy.";

    const result = await model({ datasetRow: { sentence } });

    console.log(result);
    ```
  </Tab>
</Tabs>

## Create a dataset

Next, you need a dataset to evaluate your model on. A [`Dataset` is a collection of examples stored as a Weave object](/weave/guides/core-types/datasets).

The following example dataset defines three example input sentences and their correct answers (`labels`), and then formats them in a JSON table format that scoring functions can read.

This example builds a list of examples in code, but you can also log them one at a time from your running application.

<Tabs>
  <Tab title="Python">
    ```python lines theme={null}
    sentences = ["There are many fruits that were found on the recently discovered planet Goocrux. There are neoskizzles that grow there, which are purple and taste like candy.",
    "Pounits are a bright green color and are more savory than sweet.",
    "Finally, there are fruits called glowls, which have a very sour and bitter taste which is acidic and caustic, and a pale orange tinge to them."]
    labels = [
        {'fruit': 'neoskizzles', 'color': 'purple', 'flavor': 'candy'},
        {'fruit': 'pounits', 'color': 'bright green', 'flavor': 'savory'},
        {'fruit': 'glowls', 'color': 'pale orange', 'flavor': 'sour and bitter'}
    ]
    examples = [
        {'id': '0', 'sentence': sentences[0], 'target': labels[0]},
        {'id': '1', 'sentence': sentences[1], 'target': labels[1]},
        {'id': '2', 'sentence': sentences[2], 'target': labels[2]}
    ]
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    const sentences = [
      "There are many fruits that were found on the recently discovered planet Goocrux. There are neoskizzles that grow there, which are purple and taste like candy.",
      "Pounits are a bright green color and are more savory than sweet.",
      "Finally, there are fruits called glowls, which have a very sour and bitter taste which is acidic and caustic, and a pale orange tinge to them."
    ];
    const labels = [
      { fruit: 'neoskizzles', color: 'purple', flavor: 'candy' },
      { fruit: 'pounits', color: 'bright green', flavor: 'savory' },
      { fruit: 'glowls', color: 'pale orange', flavor: 'sour and bitter' }
    ];
    const examples = sentences.map((sentence, i) => ({
      id: i.toString(),
      sentence,
      target: labels[i]
    }));
    ```
  </Tab>
</Tabs>

Then create your dataset using the `weave.Dataset()` class and publish it:

<Tabs>
  <Tab title="Python">
    ```python lines {2} theme={null}
    weave.init('eval_pipeline_quickstart')
    dataset = weave.Dataset(name='fruits', rows=examples)
    weave.publish(dataset)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript lines {3-6} theme={null}
    import * as weave from 'weave';
    await weave.init('eval_pipeline_quickstart');
    const dataset = new weave.Dataset({
      name: 'fruits',
      rows: examples
    });
    await dataset.save();
    ```
  </Tab>
</Tabs>

## Define custom scoring functions

When using Weave evaluations, Weave expects a `target` to compare `output` against. The following scoring function takes two dictionaries (`target` and `output`) and returns a dictionary of boolean values indicating whether the output matches the target. The `@weave.op()` decorator enables Weave to track the scoring function's execution.

<Tabs>
  <Tab title="Python">
    ```python lines theme={null}
    @weave.op()
    def fruit_name_score(target: dict, output: dict) -> dict:
        return {'correct': target['fruit'] == output['fruit']}
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript  theme={null}
    import * as weave from 'weave';

    const fruitNameScorer = weave.op(
      function fruitNameScore({target, output}) {
        return { correct: target.fruit === output.fruit };
      }
    );
    ```
  </Tab>
</Tabs>

To make your own scoring function, learn more in the [Scorers](/weave/guides/evaluation/scorers) guide.

In some applications, you may want to create custom `Scorer` classes. For example, you might create a standardized `LLMJudge` class with specific parameters (such as chat model or prompt), specific row scoring, and aggregate score calculation. See the tutorial on defining a `Scorer` class in the next chapter on [Model-Based Evaluation of RAG applications](/weave/tutorial-rag#optional-defining-a-scorer-class) for more information.

## Use a built-in scorer and run the evaluation

Along with custom scoring functions, you can also use [Weave's built-in scorers](/weave/guides/evaluation/builtin_scorers). In the following evaluation, `weave.Evaluation()` uses the `fruit_name_score` function defined in the previous section and the built-in `MultiTaskBinaryClassificationF1` scorer, which computes [F1 scores](https://en.wikipedia.org/wiki/F-score).

The following example runs an evaluation of `ExtractFruitsModel` on the `fruits` dataset using the scoring the two functions and logs the results to Weave.

<Tabs>
  <Tab title="Python">
    ```python lines {3-10} theme={null}
    weave.init('eval_pipeline_quickstart')

    evaluation = weave.Evaluation(
        name='fruit_eval',
        dataset=dataset, 
        scorers=[
            MultiTaskBinaryClassificationF1(class_names=["fruit", "color", "flavor"]), 
            fruit_name_score
        ],
    )
    print(asyncio.run(evaluation.evaluate(model)))
    # if you're in a Jupyter Notebook, run:
    # await evaluation.evaluate(model)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript lines {5-9} theme={null}
    import * as weave from 'weave';

    await weave.init('eval_pipeline_quickstart');

    const evaluation = new weave.Evaluation({
      name: 'fruit_eval',
      dataset: dataset,
      scorers: [fruitNameScorer],
    });
    const results = await evaluation.evaluate(model);
    console.log(results);
    ```
  </Tab>
</Tabs>

<Note>
  If you're running from a python script, you'll need to use `asyncio.run`. However, if you're running from a Jupyter notebook, you can use `await` directly.
</Note>

### Complete Example

<Accordion title="Complete evaluation pipeline in one script:">
  <Tabs>
    <Tab title="Python">
      ```python lines theme={null}
      import json
      import asyncio
      import openai
      import weave
      from weave.scorers import MultiTaskBinaryClassificationF1

      # Initialize Weave once
      weave.init('eval_pipeline_quickstart')

      # 1. Define Model
      class ExtractFruitsModel(weave.Model):
          model_name: str
          prompt_template: str

          @weave.op()
          async def predict(self, sentence: str) -> dict:
              client = openai.AsyncClient()
              response = await client.chat.completions.create(
                  model=self.model_name,
                  messages=[{"role": "user", "content": self.prompt_template.format(sentence=sentence)}],
              )
              result = response.choices[0].message.content
              if result is None:
                  raise ValueError("No response from model")
              return json.loads(result)

      # 2. Instantiate model
      model = ExtractFruitsModel(
          model_name='gpt-3.5-turbo-1106',
          prompt_template='Extract fields ("fruit": <str>, "color": <str>, "flavor": <str>) from the following text, as json: {sentence}'
      )

      # 3. Create dataset
      sentences = ["There are many fruits that were found on the recently discovered planet Goocrux. There are neoskizzles that grow there, which are purple and taste like candy.",
      "Pounits are a bright green color and are more savory than sweet.",
      "Finally, there are fruits called glowls, which have a very sour and bitter taste which is acidic and caustic, and a pale orange tinge to them."]
      labels = [
          {'fruit': 'neoskizzles', 'color': 'purple', 'flavor': 'candy'},
          {'fruit': 'pounits', 'color': 'bright green', 'flavor': 'savory'},
          {'fruit': 'glowls', 'color': 'pale orange', 'flavor': 'sour and bitter'}
      ]
      examples = [
          {'id': '0', 'sentence': sentences[0], 'target': labels[0]},
          {'id': '1', 'sentence': sentences[1], 'target': labels[1]},
          {'id': '2', 'sentence': sentences[2], 'target': labels[2]}
      ]

      dataset = weave.Dataset(name='fruits', rows=examples)
      weave.publish(dataset)

      # 4. Define scoring function
      @weave.op()
      def fruit_name_score(target: dict, output: dict) -> dict:
          return {'correct': target['fruit'] == output['fruit']}

      # 5. Run evaluation
      evaluation = weave.Evaluation(
          name='fruit_eval',
          dataset=dataset,
          scorers=[
              MultiTaskBinaryClassificationF1(class_names=["fruit", "color", "flavor"]),
              fruit_name_score
          ],
      )
      print(asyncio.run(evaluation.evaluate(model)))
      ```
    </Tab>

    <Tab title="TypeScript">
      ```typescript lines theme={null}
      import * as weave from 'weave';
      import OpenAI from 'openai';

      // Initialize Weave once
      await weave.init('eval_pipeline_quickstart');

      // 1. Define Model
      // Note: weave.Model is not supported in TypeScript yet.
      // Instead, wrap your model-like function with weave.op
      const openaiClient = new OpenAI();

      const model = weave.op(async function myModel({datasetRow}) {
        const prompt = `Extract fields ("fruit": <str>, "color": <str>, "flavor": <str>) from the following text, as json: ${datasetRow.sentence}`;
        const response = await openaiClient.chat.completions.create({
          model: 'gpt-3.5-turbo',
          messages: [{ role: 'user', content: prompt }],
          response_format: { type: 'json_object' }
        });
        return JSON.parse(response.choices[0].message.content);
      });

      // 2. Create dataset
      const sentences = [
        "There are many fruits that were found on the recently discovered planet Goocrux. There are neoskizzles that grow there, which are purple and taste like candy.",
        "Pounits are a bright green color and are more savory than sweet.",
        "Finally, there are fruits called glowls, which have a very sour and bitter taste which is acidic and caustic, and a pale orange tinge to them."
      ];
      const labels = [
        { fruit: 'neoskizzles', color: 'purple', flavor: 'candy' },
        { fruit: 'pounits', color: 'bright green', flavor: 'savory' },
        { fruit: 'glowls', color: 'pale orange', flavor: 'sour and bitter' }
      ];
      const examples = sentences.map((sentence, i) => ({
        id: i.toString(),
        sentence,
        target: labels[i]
      }));

      const dataset = new weave.Dataset({
        name: 'fruits',
        rows: examples
      });
      await dataset.save();

      // 3. Define scoring function
      const fruitNameScorer = weave.op(
        function fruitNameScore({target, output}) {
          return { correct: target.fruit === output.fruit };
        }
      );

      // 4. Run evaluation
      const evaluation = new weave.Evaluation({
        name: 'fruit_eval',
        dataset: dataset,
        scorers: [fruitNameScorer],
      });
      const results = await evaluation.evaluate(model);
      console.log(results);
      ```
    </Tab>
  </Tabs>
</Accordion>

## View your evaluation results

Weave automatically captures traces of each prediction and score. Click on the link printed by the evaluation to view the results in the Weave UI.

<img src="https://mintcdn.com/wb-21fd5541/aRvhhwVWqlxBzke5/images/evals-hero.png?fit=max&auto=format&n=aRvhhwVWqlxBzke5&q=85&s=7d7466d666ad412ed3916bfab533d118" alt="Evaluation results" width="4100" height="2160" data-path="images/evals-hero.png" />

## Learn more about Weave evaluations

* Learn more about how to [build and use scorers](/weave/guides/evaluation/scorers).
* Check out Weave's [built-in scoring functions](/weave/guides/evaluation/builtin_scorers).
* Learn about [Model-Based Evaluation](/weave/guides/evaluation/scorers#model-based-evaluation) for using LLMs as judges.

## Next Steps

[Build a RAG application](/weave/tutorial-rag) to learn about evaluating retrieval-augmented generation.
