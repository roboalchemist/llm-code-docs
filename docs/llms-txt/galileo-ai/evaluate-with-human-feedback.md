# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/evaluate-with-human-feedback.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

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

<img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/hf-1.png?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=610405ee91ad2fa2499520436358df79" alt="Human Ratings configuration." data-og-width="1188" width="1188" data-og-height="1014" height="1014" data-path="images/hf-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/hf-1.png?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=23b29834c88ca8e8a60a9ccb0a218c60 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/hf-1.png?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=2c1cafb95d2c7a19eb93592667f37544 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/hf-1.png?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=7f0c455b796a10b3113996184ef4a056 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/hf-1.png?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=fbe3b7b30734eebc967b8325c6e9d247 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/hf-1.png?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=546595466ce59316307e47dfa95f6a62 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/hf-1.png?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=4891ad1dba4f39e8c8f178226ab22980 2500w" />

#### Adding Ratings

Add your Ratings from the *Feedback* tab of your Trace or Expanded View.

Note: Ratings on Chains or Workflows apply to the entire chain (not just the Node in view).

<img src="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/hf-2.webp?fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=41372dbd92c391e7c1988827078e2e37" alt="Adding Ratings" data-og-width="2304" width="2304" data-og-height="1183" height="1183" data-path="images/hf-2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/hf-2.webp?w=280&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=8d6f549acc0c1abb77e594b12874b6c2 280w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/hf-2.webp?w=560&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=31ffd0dc11513919e9a9edce32d55718 560w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/hf-2.webp?w=840&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=d4e24aa9fbb5ddc99a7c59da10bdc0a1 840w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/hf-2.webp?w=1100&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=4a078313bae1d337fe571ea8a5c7f6cf 1100w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/hf-2.webp?w=1650&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=64bba0081ad3070f790acbf4863b1333 1650w, https://mintcdn.com/galileo/3UGpZ7QaZFb11H8t/images/hf-2.webp?w=2500&fit=max&auto=format&n=3UGpZ7QaZFb11H8t&q=85&s=0fc139671332e5e641d16f7551263389 2500w" />
