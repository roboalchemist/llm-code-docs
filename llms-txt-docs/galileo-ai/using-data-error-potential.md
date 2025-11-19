# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-llm-fine-tune/using-data-error-potential.md

# Using Data Error Potential

> Learn about Galileo LLM Fine-Tune's Data Error Potential (DEP) score to identify and address errors in your training data, improving overall data quality.

The **Galileo Data Error Potential (DEP)** score has been built to provide a per-sample holistic data quality score to identify samples in the dataset contributing to low or high model performance, i.e., pulling the model's performance up or down respectively. In other words, the DEP score measures the potential for a "misfit" of an observation to the given model.

When fine-tuning generative models, it's useful to look at DEP at a sample level as well as at the token level. Token-level DEP can tell you exactly what parts of your Target Output your model is struggling to learn.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/finetune-using-dep.png)

Data Error Potential (DEP) scores are shown throughout the product. Token-level highlighting of DEP can be turned on wherever the Target Output is shown. Red indicates high DEP, orange medium DEP, and green low DEP.

**How to use DEP?**

Look for patterns in groups of High DEP samples (e.g. a High DEP cluster). A High Data Error Potential might be due to a mistake in the annotation (e.g. expecting an answer that the model couldn't possibly infer from the input), due to there not being enough "similar samples" (something the model could learn but you need to feed it more samples like it) or it simply being garbage sample which needs to be removed.

Determine whether you need to *Edit Target* and change your Target Output, *Remove* your samples, or Find Similar Data to include in your dataset, and [take action](/galileo/gen-ai-studio-products/galileo-llm-fine-tune/taking-action).
