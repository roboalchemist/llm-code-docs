# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-llm-fine-tune/using-uncertainty.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Uncertainty

> On dataset splits where generations are enabled (e.g. the _Test split_), you'll be seeing Uncertainty Scores and Token-level Uncertainty highlighting

<img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-using-uncertainty.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=4c44f6eec1f522253860728d2bf7df6b" alt="" data-og-width="978" width="978" data-og-height="318" height="318" data-path="images/finetune-using-uncertainty.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-using-uncertainty.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=0146d23456eeb77051ad76acee9398f9 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-using-uncertainty.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=dbce0e601bd6e378e969564d981d461d 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-using-uncertainty.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=aac340dd096543c0c927329efcda4c3e 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-using-uncertainty.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=5e526dff60ce45ae549335c358591fe4 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-using-uncertainty.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=f28d8b0f5a2d1fe4ab71989d213b28a7 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-using-uncertainty.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=feffc21b7785143f116b3fa22109f78e 2500w" />

*Uncertainty* measures how much the model is deciding randomly between multiple ways of continuing the output.

*Uncertainty* is measured at both the token level and the response level. At the token level:

* Low *Uncertainty* means the model is fairly confident about what to say next, given the preceding tokens

* High *Uncertainty* means the model is unsure what to say next, given the preceding tokens

*Uncertainty* at the response level is simply the maximum token-level *Uncertainty,* over all the tokens in the model's response.

Some types of LLM hallucinations – particularly made-up names, citations, and URLs – are strongly correlated with *Uncertainty.* Monitoring *Uncertainty* can help you pinpoint these types of errors.
