# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/autogen-metrics.md

# Auto-generating an LLM-as-a-judge

> Learn how to use Galileo's Autogen feature to generate LLM-as-a-judge metrics.

Creating an LLM-as-a-judge metric is really easy with Galileo's Autogen feature. You can simply enter
a description of what you want to measure or detect, and Galileo auto-generates a metric for you.

## How it works

When you enter a description of your metric (e.g. "detect any toxic language in the inputs"), your description
is converted into a prompt and few-shot examples for your metric. This prompt and few-shot examples are used
to power an LLM-as-a-judge that uses chain-of-thought and majority voting (see [Chainpoll paper](/galileo-ai-research/chainpoll)) to calculate a metric.

You can customize the model that gets used or the number of judges used to calculate your metric.

<Note>Currently, auto-generated metrics are restricted to binary (yes/no) measurements. Multiple choice or numerical ratings are coming soon.</Note>

## How to use it

<iframe src="https://www.loom.com/embed/7219af823044488090ced9cfea19a645?sid=84af27d0-70ff-4eee-be77-9d6d579ad32f" width="100%" height="480px" allowfullscreen="" scrolling="no" allow="encrypted-media *;" />

## Editing and Iterating on your auto-generated LLM-as-a-judge

You can always go back and edit your prompt or examples. Additionally, you can use [Continuous Learning via Human Feedback (CLHF)](/galileo/gen-ai-studio-products/galileo-evaluate/how-to/continuous-learning-via-human-feedback) to improve and adapt your metric.
