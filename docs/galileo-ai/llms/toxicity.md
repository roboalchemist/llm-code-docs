# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/toxicity.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Toxicity

> Understand Galileo's Toxicity Metric

***Definition:*** Flags whether a response contains hateful or toxic information. Toxicity refers to language that is harmful or inappropriate, typically evaluated based on the following aspects:

* Hate Speech: Statements that demean, dehumanize, or attack individuals or groups based on identity factors like race, gender, or religion.

* Offensive Content: Vulgar, abusive, or overly profane language used to provoke or insult.

* Sexual Content: Explicit or inappropriate sexual statements that may be offensive or unsuitable in context.

* Violence or Harm: Advocacy or description of physical harm, abuse, or violent actions.

* Illegal or Unethical Guidance: Instructions or encouragement for illegal or unethical actions.

* Manipulation or Exploitation: Language intended to deceive, exploit, or manipulate individuals for harmful purposes.

Statements fitting these criteria can be flagged as toxic, harmful, or inappropriate based on context and intent. Output is a binary classification of whether a response is toxic or not.

***Calculation:*** We leverage a Small Language Model (SLM) trained on open-source and internal datasets.

The accuracy on the below open-source datasets averages 96% on the validation set:

* [Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)

* [Jigsaw Unintended Bias in Toxicity Classification](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification)

* [Jigsaw Multilingual Toxic Comment Classification](https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification)

***Usefulness:*** Identify responses that contain toxic comments and take preventative measure such as fine-tuning or implementing guardrails that flag responses to prevent future occurrences.
