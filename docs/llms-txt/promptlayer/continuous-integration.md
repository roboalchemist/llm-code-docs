# Source: https://docs.promptlayer.com/features/evaluations/continuous-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Continuous Integration

Continuous Integration (CI) of prompt evaluations is the holy grail of prompt engineering. 🏆

CI in the context of prompt engineering involves the automated testing and validation of prompts every time a new version is created or updated. LLMs are a probabilistic technology. It is hard (read: virtually impossible) to ensure a new prompt version doesn't break old user behavior just by eyeballing the prompt. Rigorous testing is the best tool we have.

We believe that it's important to both allow subject-matter experts to write new prompts and provide them with tools to easily test if the prompts broke anything. That's where PromptLayer evaluations comes in.

## Test-driven Prompt Engineering

Similar to test-driven development (TDD) in software engineering, test-driven prompt engineering involves writing and running evaluations against new prompt versions before they are used in production. This proactive testing ensures that new prompts meet predefined criteria and behave as expected, minimizing the risk of unintended consequences.

Setting up automatic evaluations on a specific prompt template is easy. When creating a new version, after adding a commit message, you will be prompted to select an evaluation pipeline to run. After doing this once, every new prompt template you create will run this pipeline by default.

**NOTE**: Make sure your evaluation pipeline uses the "latest" version of the prompt template in its column step. The template is fetched at runtime. If you specify a frozen version, the evaluation report won't reflect your newest prompt template.

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/explain-stocks-scoring.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=ad84ffa191bff41db8391891c61dce32" alt="Scoring a Prompt" data-og-width="1447" width="1447" data-og-height="807" height="807" data-path="images/explain-stocks-scoring.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/explain-stocks-scoring.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=8b9d682e8b3d44e75c5a054f6bfa0efe 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/explain-stocks-scoring.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=8c58637663314de620e2870aa3b5b63a 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/explain-stocks-scoring.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=89c8a1dfae2fdcc57dab7c1bc35c5111 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/explain-stocks-scoring.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=fad09c8b5a00045746f092b02f4bb0c5 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/explain-stocks-scoring.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=ddd3eccd74e0810065f05a928c9ac37a 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/explain-stocks-scoring.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=94055d7c9c1cad88b15b9e0a12f0abf8 2500w" />

## Testing Strategies

### Backtesting

Backtesting involves running new prompt versions against a dataset compiled from historical production data. This strategy provides a real-world context for evaluating prompts, allowing you to assess how new versions would have performed under past conditions. It's an effective way to detect potential regressions and validate improvements, ensuring that updates enhance rather than detract from the user experience.

To set up backtests, follow the steps below:

**1. Create a historical dataset**

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/create-a-new-dataset.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=2e12075b0ca51321766caee5a250cf81" alt="Create a New Dataset" data-og-width="1153" width="1153" data-og-height="730" height="730" data-path="images/create-a-new-dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/create-a-new-dataset.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=07fd7e13b4194abe13be44ca705bb194 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/create-a-new-dataset.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=ef827249715a04b35a9866fe965e21a1 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/create-a-new-dataset.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=83599bff600df7b8b2f8776a38dcfd09 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/create-a-new-dataset.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=45640fedcfcf13c2fc27ed9787734246 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/create-a-new-dataset.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=6111f78af5ac128f2b41a67c0321e29e 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/create-a-new-dataset.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=193a2667305ba16f53e1af9906cc50c3 2500w" />

[Create a dataset](/features/evaluations/datasets) using a search query. For example, I might want to create a dataset using all logged requests:

* That use `my_prompt_template` version 6 or version 5
* That were made in the last 2 months
* That were using the tag `prod`
* That users gave a 👍 response to

This dataset will help you understand if your new prompt version broke any previous versions!

**2. Build an evaluation pipeline**

The next step is to create an evaluation pipeline using our new historical dataset.

In plain English, this evaluation will feed in historical request context into your new prompt version then compare the new results to the old results. You can do a simple string comparison or get fancy with cosine similarities. PromptLayer will even show you a diff view for responses that are different.

**3. Run it when you make a new version**

This is the fun part. Next time you make a new prompt version, just select our new backtesting pipeline to see how the new prompt version fairs.

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/evaluation-diff.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=5d8497176d0b08826206f9f36e129cb4" alt="Diffing evaluation" data-og-width="1636" width="1636" data-og-height="951" height="951" data-path="images/evaluation-diff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/evaluation-diff.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=c5b3484ba8dfe3ab005c3cf9ca228806 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/evaluation-diff.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=73f7c95019f71b3a3189c0b9b81e05d4 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/evaluation-diff.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=0b6622a464faad320243e447dbbfbb3b 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/evaluation-diff.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=7392bc0a75500f34a989cbeb676d96a5 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/evaluation-diff.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=81c29b5bbc906af0ebbfcfbe45decc9c 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/evaluation-diff.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=b689229e2757d6b08a5cb6b7a8dfdfec 2500w" />

### Regression Testing

Regression testing is the continuous refinement of evaluation datasets to include new edge cases and scenarios as they are discovered. This iterative process ensures that prompts remain robust against a growing set of challenges, preventing regressions in areas previously identified as potential failure points. By continually updating evaluations with new edge cases, you maintain a high standard of prompt quality and reliability.

The process of setting up regression tests looks similar to backtesting.

[Create a dataset](/features/evaluations/datasets) containing test cases for every edge case you can think of. The dataset should include context variables that you can input to your prompt template.

### Scoring

The evaluation can result in a single quantitative final score. To configure the score card, all you need to do is make sure that the last step consists entirely of numbers or Booleans. A final objective score makes comparing prompt performance easy, and it will be displayed alongside prompts in the Prompt Registry.

<img src="https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/version-scores.png?fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=1cdcda221e32c09311bf05a9e6e0728e" alt="Version Scoring" data-og-width="387" width="387" data-og-height="482" height="482" data-path="images/version-scores.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/version-scores.png?w=280&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=7d09d12a5d981da213783ad8fc88c2ba 280w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/version-scores.png?w=560&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=e46d40fa576b9d59b476d9e731b8de7f 560w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/version-scores.png?w=840&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=3ae2c2c9c5d275ae1761ea57a927c7ef 840w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/version-scores.png?w=1100&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=be6ca852ef0c9dd3d1c1af12afd0416a 1100w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/version-scores.png?w=1650&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=387a8e664466b344055486ede246b7d1 1650w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/version-scores.png?w=2500&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=ed4d547ef9172e5234d935bb9f03b9c2 2500w" />
