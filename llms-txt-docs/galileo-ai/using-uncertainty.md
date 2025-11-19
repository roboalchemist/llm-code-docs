# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-llm-fine-tune/using-uncertainty.md

# Using Uncertainty

> On dataset splits where generations are enabled (e.g. the _Test split_), you'll be seeing Uncertainty Scores and Token-level Uncertainty highlighting

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/finetune-using-uncertainty.png)

*Uncertainty* measures how much the model is deciding randomly between multiple ways of continuing the output.

*Uncertainty* is measured at both the token level and the response level. At the token level:

* Low *Uncertainty* means the model is fairly confident about what to say next, given the preceding tokens

* High *Uncertainty* means the model is unsure what to say next, given the preceding tokens

*Uncertainty* at the response level is simply the maximum token-level *Uncertainty,* over all the tokens in the model's response.

Some types of LLM hallucinations – particularly made-up names, citations, and URLs – are strongly correlated with *Uncertainty.* Monitoring *Uncertainty* can help you pinpoint these types of errors.
