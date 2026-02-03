# Source: https://docs.promptlayer.com/why-promptlayer/fine-tuning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Fine-Tuning

Fine-tuning is incredibly powerful. PromptLayer lets you build and iterate models in a few clicks.

If you are already logging your `gpt-4` requests in PromptLayer, it only takes a few clicks to fine-tune a `gpt-3.5-turbo` model on those requests! ✨

## What is fine-tuning?

Fine-tuning is a technique to specialize a pre-trained large language model (LLM) for a specific task. It involves training the LLM on a small dataset of examples, where the input is the text to be processed and the output is the desired output, such as a classification label, a translation, or a generated text.

Fine-tuning is powerful because it allows developers to create a model that is tailored to their specific needs. This could be used to improve model output quality, shorten a system prompt without degrading performance, or to decrease latency by building off of a smaller model.

Here are some examples of how fine-tuning can be used:

* **Reduce latency and cost:** Fine-tune `gpt-3.5-turbo` on `gpt-4` outputs to achieve `gpt-4`-quality results on a faster and cheaper model.
* **Save on tokens:** Generate training data using a long and complex prompt. When fine-tuning, change the prompt to something shorter and save on tokens.
* **Improve output format:** Generate synthetic training data to teach a base model to only output text in JSON.

## Create training data

The first step to fine-tuning is preparing the training data you want the model to learn from. Training data in this case are just LLM requests.

### Log in the background

The simplest way to do this is to just connect your application to PromptLayer and start logging requests. Just wait a week and your production users will have created tons of training data for you!

### Batch run prompts

Alternatively, you can use PromptLayer to generate these training requests. Visit the [Evaluations page](/why-promptlayer/evaluation-page) to run batch jobs of your prompts.

For example, to generate fine-tuning data you can run a prompt template from the [Prompt Registry](/features/prompt-registry) against 200 test cases on `gpt-4`. Then just filter the sidebar based its specific test run tag.

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/generate.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=26745383e78ffa98ebecec334e7b17c2" alt="Generate Training Data" data-og-width="2114" width="2114" data-og-height="1554" height="1554" data-path="images/fine-tuning/generate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/generate.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=8e2c44ff6b388a96ce45432813e14f70 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/generate.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=b9d04c5af9a07c86f92348b157ef8b5e 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/generate.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=44b5610f6db25f6e54b8cc7bb721e82f 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/generate.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=d010759351335ecab2d46f82d38b11d4 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/generate.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=a79b082111e94341a0346f1fb6d15d9d 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/generate.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=47533bd924f4bdeaf5d0af3e1b6aa701 2500w" />

## Select training data

Use the sidebar search area to filter for your training data. All the data that appears from that search query will be used to fine-tune.

[Learn more about search filters](/why-promptlayer/advanced-search)

<div style={{width: '70%'}}>
    <img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/select-training.gif?s=2892dfbf1ff25e5c72dcd1984cde4b58" alt="Select Training Data" data-og-width="800" width="800" data-og-height="720" height="720" data-path="images/fine-tuning/select-training.gif" data-optimize="true" data-opv="3" />
</div>

## Start the fine-tune job

Click "Fine-Tune" in the sidebar, follow the steps, and kick off a job.

## Test out your new model

**Success!** 🎉 Now you have a new fine-tuned model. Let's see if it's any good...

<div style={{width: '70%'}}>
    <img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/success.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=3be76ebaa27e1fff8060a9c5ec347f8d" alt="Successful fine-tuning" data-og-width="1156" width="1156" data-og-height="1468" height="1468" data-path="images/fine-tuning/success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/success.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=b3e7818245285322474cb6c1db756c94 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/success.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=20db40296e3bf71c46342d8a2a2aafa1 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/success.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=c857984db9620809c9beaf10b9218041 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/success.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=761db85c3586cfa28355472aa49508ac 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/success.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=bef49919858922e5dd8aca0f041567bc 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/success.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=1b746fcc36f49537bc616fd36103808f 2500w" />
</div>

### Try it in Playground

Copy the model name and navigate to the PromptLayer Playground. There you can run an arbitrary request on the new model. See how it does!

<div style={{width: '70%'}}>
    <img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/request.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=de4eaff35eba350bf92bf02c48cd97f4" alt="Try out Fine-Tuned Model" data-og-width="728" width="728" data-og-height="406" height="406" data-path="images/fine-tuning/request.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/request.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=3a113a5f0ab54359a2df1d932f52df44 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/request.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=9352f1797f85633904c1d92c6cb4ccbf 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/request.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=7be65b7d5a0ad3230eb9d9f17118374d 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/request.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=3edd484b6cc4de17c2c8d4ea2c8f0e17 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/request.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=cc696606987349c42d04036a103ed483 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/request.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=8038c13a2d6b5dd0273f9048e4439b05 2500w" />
</div>

### Try it in Evaluations

It's important to test your fine-tune model a little more rigorously than one-off Playground requests. Navigate to the [Evaluations page](/why-promptlayer/evaluation-page) and run some batch tests. See how the fine-tuned candidate compares to a standard `gpt-4` candidate.

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/evaluate.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=f0f72722d47c2c422abeb108aa08a9bc" alt="Evaluate fine-tuned model" data-og-width="2014" width="2014" data-og-height="1428" height="1428" data-path="images/fine-tuning/evaluate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/evaluate.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=8740d221d6afe207a27e406d41c6e187 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/evaluate.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=7c45140613c8236fe9765b0777a36576 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/evaluate.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=e225d66d885c40f3422ca818cd4fa541 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/evaluate.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=937728fed682b27d5278dcb2e9566e84 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/evaluate.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=ce82062621dd2dbc8bb588d2acad8ffc 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/fine-tuning/evaluate.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=33ece3b7c5c7aa61802842ab89ba55fc 2500w" />
