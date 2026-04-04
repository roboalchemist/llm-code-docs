# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/tone.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Tone

> Understand Galileo's Tone Metric

***Definition:*** Classifies the tone of the response into 9 different emotion categories: neutral, joy, love, fear, surprise, sadness, anger, annoyance, and confusion.

***Calculation:*** We leverage a Small Language Model (SLM) trained on open-source and internal datasets.

Our classifier's accuracy on the [GoEmotions](https://huggingface.co/datasets/go_emotions) (open-source) dataset is about 80% for the validation set.

***Usefulness:*** Recognize and categorize the emotional tone of responses to align with user preferences, allowing for optimization by discouraging undesirable tones and promoting preferred emotional responses.
