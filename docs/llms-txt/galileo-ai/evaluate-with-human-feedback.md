# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-with-human-feedback.md

# Evaluate with Human Feedback

> Galileo allows you to do qualitative human evaluations of your prompts and responses.

#### Configure your Human Ratings settings

You can configure your Human Ratings settings by clicking on "Configure Human Ratings" from your Project or Run view. Your configuration is applied to all runs in the Project, to allow you to compare all runs on the same rating dimensions.

You can configure multiple dimensions or "Rating Types" to rate your run on. Each Rating Type will be used to rate your responses on a different dimension (e.g. quality, conciseness, hallucination potential, etc).

Types are Name and have a Format. We support 5 formats:

* <Icon icon="thumbs-up" solid /> / <Icon icon="thumbs-down" solid />

* 1 - 5 <Icon icon="star" solid />s

* Numerical ratings

* Categorical ratings (self-defined categories)

* Free-form text

Along with each rating, you can also allow raters to provide a rationale.

To align everyone on the Rating Criteria or rubric, you can define it as part of your Human Ratings configuration.

![Human Ratings configuration.](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/hf-1.png)

#### Adding Ratings

Add your Ratings from the *Feedback* tab of your Trace or Expanded View.

Note: Ratings on Chains or Workflows apply to the entire chain (not just the Node in view).

![Adding Ratings](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/hf-2.webp)
