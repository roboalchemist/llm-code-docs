# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-llm-fine-tune/using-data-error-potential.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Data Error Potential

> Learn about Galileo LLM Fine-Tune's Data Error Potential (DEP) score to identify and address errors in your training data, improving overall data quality.

The **Galileo Data Error Potential (DEP)** score has been built to provide a per-sample holistic data quality score to identify samples in the dataset contributing to low or high model performance, i.e., pulling the model's performance up or down respectively. In other words, the DEP score measures the potential for a "misfit" of an observation to the given model.

When fine-tuning generative models, it's useful to look at DEP at a sample level as well as at the token level. Token-level DEP can tell you exactly what parts of your Target Output your model is struggling to learn.

<img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-using-dep.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=762cb2243fa9dc981afe0a55b1a8fa04" alt="" data-og-width="652" width="652" data-og-height="301" height="301" data-path="images/finetune-using-dep.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-using-dep.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=f248f63e5095dd131f2859d8462914be 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-using-dep.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=726ecdc400a145f7c9e4f81e7450be1d 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-using-dep.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=16acb5ae4cef24b5bc76c76ca4d16b38 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-using-dep.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=dbf58be639c78a59502981093c6a36c2 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-using-dep.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=8b13b10e647c79685e236b83ef70d9f1 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/finetune-using-dep.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=74124b306e13c8c3161a162a9db46edd 2500w" />

Data Error Potential (DEP) scores are shown throughout the product. Token-level highlighting of DEP can be turned on wherever the Target Output is shown. Red indicates high DEP, orange medium DEP, and green low DEP.

**How to use DEP?**

Look for patterns in groups of High DEP samples (e.g. a High DEP cluster). A High Data Error Potential might be due to a mistake in the annotation (e.g. expecting an answer that the model couldn't possibly infer from the input), due to there not being enough "similar samples" (something the model could learn but you need to feed it more samples like it) or it simply being garbage sample which needs to be removed.

Determine whether you need to *Edit Target* and change your Target Output, *Remove* your samples, or Find Similar Data to include in your dataset, and [take action](/galileo/gen-ai-studio-products/galileo-llm-fine-tune/taking-action).
