# Source: https://braintrust.dev/docs/cookbook/recipes/PromptVersioning.md

# Prompt versioning and deployment

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/PromptVersioning/PromptVersioning.ipynb) by [Adrian Barbir](https://www.linkedin.com/in/adrianbarbir/) on 2025-02-24</div>

Large language models can sometimes feel unpredictable, where small changes to a prompt can dramatically change the quality and tone of generated responses. In customer support, this is especially important, since customer satisfaction, brand tone, and the clarity of solutions offered all rely on consistent, high-quality prompts. Optimizing this process involves creating a couple variations, measuring their effectiveness, and sometimes returning to previous versions that performed better.

In this cookbook, we'll build a support chatbot and walk through the complete cycle of prompt development. Starting with a basic implementation, we'll create increasingly sophisticated prompts, keep track of different versions, evaluate their performance, and switch back to earlier versions when necessary.

## Getting started

Before getting started, make sure you have a [Braintrust account](https://www.braintrust.dev/signup) and an API key for [OpenAI](https://platform.openai.com/signup). Make sure to plug the OpenAI key into your Braintrust account's [AI provider configuration](https://www.braintrust.dev/app/settings?subroute=secrets).

Once you have your Braintrust account set up with an OpenAI API key, install the following dependencies:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
pip install braintrust autoevals openai
```

To authenticate with Braintrust, export your `BRAINTRUST_API_KEY` as an environment variable:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
export BRAINTRUST_API_KEY="YOUR_API_KEY_HERE"
```

<Callout type="info">
  Exporting your API key is a best practice, but to make it easier to follow along with this cookbook, you can also hardcode it into the code below.
</Callout>

Once the API key is set, we can import our modules and initialize the OpenAI client using the AI proxy:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import os
import subprocess
from openai import OpenAI
from braintrust import Eval, wrap_openai, invoke
from autoevals import LLMClassifier

# Uncomment the following line to hardcode your API key
# os.environ["BRAINTRUST_API_KEY"] = "YOUR_API_KEY_HERE"

# Initialize OpenAI client with Braintrust wrapper
client = wrap_openai(
    OpenAI(
        base_url="https://api.braintrust.dev/v1/proxy",
        api_key=os.environ["BRAINTRUST_API_KEY"],
    )
)

project_name = "SupportChatbot"
```

## Creating a dataset

We'll create a small dataset of sample customer complaints and inquiries to evaluate our prompts. In a production application, you'd want to use real customer interactions from your logs to create a representative dataset.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
dataset = [
    {
        "input": "Why did my package disappear after tracking showed it was delivered?",
        "metadata": {"category": "shipping"},
    },
    {
        "input": "Your product smells like burnt rubber - what’s wrong with it?",
        "metadata": {"category": "product"},
    },
    {
        "input": "I ordered 3 items but only got 1, where’s the rest?",
        "metadata": {"category": "shipping"},
    },
    {
        "input": "Why does your app crash every time I try to check out?",
        "metadata": {"category": "tech"},
    },
    {
        "input": "My refund was supposed to be here 2 weeks ago - what’s the holdup?",
        "metadata": {"category": "returns"},
    },
    {
        "input": "Your instructions say ‘easy setup’ but it took me 3 hours!",
        "metadata": {"category": "product"},
    },
    {
        "input": "Why does your delivery guy keep leaving packages at the wrong house?",
        "metadata": {"category": "shipping"},
    },
    {
        "input": "The discount code you sent me doesn’t work - fix it!",
        "metadata": {"category": "sales"},
    },
    {
        "input": "Your support line hung up on me twice - what’s going on?",
        "metadata": {"category": "support"},
    },
    {
        "input": "Why is your website saying my account doesn’t exist when I just made it?",
        "metadata": {"category": "tech"},
    },
]
```

## Creating a scoring function

When evaluating support responses, we care about tone, helpfulness, and professionalism, not just accuracy. To do this, we use an [LLMClassifier](https://github.com/braintrustdata/autoevals?tab=readme-ov-file#python-3) that checks for alignment with brand guidelines:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
brand_alignment_scorer = LLMClassifier(
    name="BrandAlignment",
    prompt_template="""
    Evaluate if the response aligns with our brand guidelines (Y/N):
    1. **Positive Tone**: Uses upbeat language, avoids negativity (e.g., "We’re thrilled to help!" vs. "That’s your problem").
    2. **Proactive Approach**: Offers a clear next step or solution (e.g., "We’ll track it now!" vs. vague promises).
    3. **Apologetic When Appropriate**: Acknowledges issues with empathy (e.g., "So sorry for the mix-up!" vs. ignoring the complaint).
    4. **Solution-Oriented**: Focuses on fixing the issue for the customer (e.g., "Here’s how we’ll make it right!" vs. excuses).
    5. **Professionalism**: There should be no profanity, or emojis.

    Response: {{output}}


    Only give a Y if all the criteria are met. If one is missing and it should be there, give a N.
    """,
    choice_scores={
        "Y": 1,
        "N": 0,
    },  # This scorer will return a 1 if the response fully matches all brand guidelines, and a 0 otherwise.
    use_cot=True,
)
```

## Creating a prompt

To push a prompt to Braintrust, we need to create a new Python file `prompt_v1.py` that defines the prompt. Once we've created the file, we can push it to Braintrust via the CLI. Let's start with a basic prompt that provides a direct response to customer inquiries:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
# Create a prompt_v1.py file

import braintrust

project = braintrust.projects.create(name="SupportChatbot")

prompt_v1 = project.prompts.create(
    name="Brand Support V1",
    slug="brand-support-v1",
    description="Simple support prompt",
    model="gpt-4o",
    messages=[{"role": "user", "content": "{{{input}}}"}],
    if_exists="replace",
)
```

To push the prompt to Braintrust, run:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
braintrust push prompt_v1.py
```

After pushing the prompt, you'll see it in the Braintrust UI.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/promptv1.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=6be68bb447cba0ea1ca4973135c4b300" alt="promptv1" data-og-width="3374" width="3374" data-og-height="1936" height="1936" data-path="cookbook/assets/PromptVersioning/promptv1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/promptv1.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=56ebc9e300693a808befad0629240c59 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/promptv1.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=82f894cf4f79d0076b1222a2f72e1cd3 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/promptv1.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=54ec7716f0bc57acede355a05f874efa 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/promptv1.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=e1a17eca2525e27694966ad82f7aea3c 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/promptv1.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=5545ec1f4c0362166bbad67987cf2f4f 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/promptv1.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=b63af47f69ae06fb8596d339b91b9578 2500w" />

### Evaluating prompt v1

Now that our first prompt is ready, we'll define a task function that calls this prompt. Then, we'll run an evaluation with our `brand_alignment_scorer`:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
# Define task using invoke with correct input
def task_v1(input):
    result = invoke(
        project_name=project_name,
        slug="brand-support-v1",
        input={"input": input},  # Matches {{{input}}} in our prompt
    )
    return result


eval_task = Eval(
    project_name,
    data=lambda: dataset,
    task=task_v1,
    scores=[brand_alignment_scorer],
    experiment_name="prompt_v1",
)
```

After running the evaluation, you'll see the results in the Braintrust UI:

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v1results1.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=19a0c5c2d96087a00e69ea036363a955" alt="v1results1" data-og-width="3368" width="3368" data-og-height="1886" height="1886" data-path="cookbook/assets/PromptVersioning/v1results1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v1results1.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=9916a4557d4cb60611ce673ed5cc46ae 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v1results1.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=988cace58e375aebf27f47a384d24592 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v1results1.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=e334cefe6648da90912e58fc38f33703 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v1results1.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=cc7fccc87f5effb1bfd204f8f7c78ff1 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v1results1.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=09a18362dcee143b6b92070634c73119 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v1results1.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=5989c3843d1e4ea85764389b57ed7c9c 2500w" />

## Improving our prompt

Our initial evaluation showed that there is room for improvement. Let's create a more sophisticated prompt that incorporates our brand guidelines to encourage a positive, proactive tone and clear solutions. Like before, we'll create a new Python file called `prompt_v2.py` and push it to Braintrust.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
# Create a prompt_v2.py file

import braintrust

project = braintrust.projects.create(name="SupportChatbot")

prompt_v2 = project.prompts.create(
    name="Brand Support V2",
    slug="brand-support-v2",
    description="Brand-aligned support prompt",
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You’re a cheerful, proactive assistant for Sunshine Co. Always use a positive tone, apologize for issues with empathy, and offer clear solutions to delight customers! No emojis or profanity.",
        },
        {"role": "user", "content": "{{{input}}}"},
    ],
    if_exists="replace",
)
```

To push the prompt to Braintrust, run:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
braintrust push prompt_v2.py
```

### Evaluating prompt v2

We now point our task function to the slug of our second prompt:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def task_v2(input):
    result = invoke(
        project_name=project_name,
        slug="brand-support-v2",
        input={"input": input},
    )
    return result


eval_task = Eval(
    project_name,
    data=lambda: dataset,
    task=task_v2,
    scores=[brand_alignment_scorer],
    experiment_name="prompt_v2",
)
```

There is a clear improvement in brand alignment.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v2results1.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=5028138770e81a48d84a1d58ade4aa62" alt="v2results1" data-og-width="3312" width="3312" data-og-height="1882" height="1882" data-path="cookbook/assets/PromptVersioning/v2results1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v2results1.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=8b6fb7ca2b364876c5a7303208432a3a 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v2results1.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=7ba5b506bc31fc0fbb1f8c60f97d77b9 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v2results1.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=ea8f24f1d35bae9061f30db5ff24da8e 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v2results1.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=0cfc19d488a18e8ee801627486aeb43c 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v2results1.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=f841b93b7ba28849538210d370df5767 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v2results1.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=20d24e36eadf8e88f216e1f7a355b472 2500w" />

## Experimenting with tone

For our third prompt, let's create `prompt_v3.py` and exaggerate the brand voice further. This example is intentionally over the top to show how brand alignment might fail if the tone is too extreme or vague in offering solutions. In practice, you'd likely use more subtle variations.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
# Create a prompt_v3.py file

import braintrust

project = braintrust.projects.create(name="SupportChatbot")

prompt_v3 = project.prompts.create(
    name="Brand Support V3",
    slug="brand-support-v3",
    description="Over-enthusiastic support prompt with middling performance",
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You’re a SUPER EXCITED Sunshine Co. assistant! SHOUT IN ALL CAPS WITH LOTS OF EXCLAMATIONS!!!! SAY SORRY IF SOMETHING’S WRONG BUT KEEP IT VAGUE AND FUN!!! Make customers HAPPY with BIG ENERGY, even if solutions are UNCLEAR!!!!",
        },
        {"role": "user", "content": "{{{input}}}"},
    ],
    if_exists="replace",
)
```

To push the prompt to Braintrust, run:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
braintrust push prompt_v3.py
```

### Evaluating prompt v3

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def task_v3(input):
    result = invoke(
        project_name=project_name,
        slug="brand-support-v3",
        input={"input": input},
    )
    return result


eval_task = Eval(
    project_name,
    data=lambda: dataset,
    task=task_v3,
    scores=[brand_alignment_scorer],
    experiment_name="prompt_v3",
)
```

You might notice a lower brand alignment score here. This highlights why controlled tone adjustments are crucial in real-world scenarios, and how you might need several iterations to find an optimal prompt.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v3results.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=f654390cb69920a378d114d7a343a9f8" alt="v3results" data-og-width="3364" width="3364" data-og-height="1888" height="1888" data-path="cookbook/assets/PromptVersioning/v3results.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v3results.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=dcd31c6018284edf0ca131d0b0a2200d 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v3results.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=28413d30ff5e2729112ad8d810ba4e8e 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v3results.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=8255231f652b9067cd02e38604c2e8cc 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v3results.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=fc206aae9847ac7f715fc0032a79ad25 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v3results.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=3f8c18a68089d830451b8f7ffececa90 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/v3results.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=6e8b217854e8066612a8e8684571c586 2500w" />

## Managing prompt versions

After evaluating all three versions, we found that our second prompt achieved the highest score.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/scores.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=1e6f59a6fae241c9bc93e6e5be1bac4e" alt="scores" data-og-width="3350" width="3350" data-og-height="1872" height="1872" data-path="cookbook/assets/PromptVersioning/scores.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/scores.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=7b25744857d8a1649b8651a218a61c6e 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/scores.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=f9e038e30fdd358e3617b1119e776a8e 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/scores.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=b657937e701ef14712abeb636ff1e392 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/scores.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=71306fc76f6be66009114ab3950ae7fd 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/scores.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=8b0db0c8a59065d3e8df2d31858406e2 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/scores.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=09f1bbabce43ca007fdf848db8d0ddfb 2500w" />

Although we've iterated on the prompt, Braintrust makes it simple to revert to this high-performing version:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
def task_reverted(input):
    result = invoke(
        project_name=project_name,
        slug="brand-support-v2",
        input={"input": input},
    )
    return result


eval_task = Eval(
    project_name,
    data=lambda: dataset,
    task=task_reverted,
    scores=[brand_alignment_scorer],
    experiment_name="prompt_v2_reverted",
)
```

If you keep the same slug for multiple changes, Braintrust’s built-in versioning allows you to revert within the UI. See the docs on [prompt versioning](/core/functions/prompts#in-code) for more information.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/versions1.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=5fd64bed4778bbd703657b5e8241e8fe" alt="versions1" data-og-width="3306" width="3306" data-og-height="1886" height="1886" data-path="cookbook/assets/PromptVersioning/versions1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/versions1.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=ce97f814de268dcfb7f3c69accd7b506 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/versions1.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=732ff8f0e2e1a728a07c69b2c01d4bcd 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/versions1.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=3ead527193153233cd8355511f7570f2 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/versions1.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=f0d27d9e6534a08e830f519dbcb7534f 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/versions1.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=99a299e3e724d702ead61209c9cbbb58 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/PromptVersioning/versions1.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=f776d2cb7276c138574d29263aa3d22e 2500w" />

## Next steps

* Now that you have some prompts saved, you can rapidly test them with new models in our [prompt playground](/core/playground).
* Learn more about [evaluating a chat assistant](/cookbook/recipes/EvaluatingChatAssistant).
* Think about how you might add more sophisticated [scoring functions](/core/experiments/write#scorers) to your evals.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt