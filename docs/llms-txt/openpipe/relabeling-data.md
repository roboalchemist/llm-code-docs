# Source: https://docs.openpipe.ai/features/datasets/relabeling-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openpipe.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Relabeling Data

> Use powerful models to generate new outputs for your data before training.

After importing rows from request logs or uploading a JSONL file, you can optionally relabel
each row by sending its messages, tools, and other input parameters to a more powerful model,
which will generate an output to replace your row's existing output. If time or cost constraints prevent
you from using the most powerful model available in production, relabeling offers an opportunity to
optimize the quality of your training data before kicking off a job.

<Frame><img src="https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/relabeled-output.png?fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=335be496174ed80e4855fc8ca00107e0" alt="" data-og-width="2420" width="2420" data-og-height="1448" height="1448" data-path="images/features/relabeled-output.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/relabeled-output.png?w=280&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=12f7124b5ae0310713506ef9b5568903 280w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/relabeled-output.png?w=560&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=1d30a74624f45a143c28a0493662badf 560w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/relabeled-output.png?w=840&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=aafd7f0165863bdf681fd59126c559db 840w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/relabeled-output.png?w=1100&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=fd9f4e70a953ee8e14afcbc4caf29ebe 1100w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/relabeled-output.png?w=1650&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=1a5b69d6cb32f3bb9f14cf75f9aa0707 1650w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/relabeled-output.png?w=2500&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=fc7c19d1d6d8c4d1281b7be6514e8bca 2500w" /></Frame>

We provide a number of built-in relabeling options.

Anthropic:

* `claude-3-opus-20240229`
* `claude-sonnet-3-7-20250219`
* `claude-sonnet-3-5-20241022`

OpenAI:

* `gpt-4-5-preview-02-27`
* `o1-2024-12-17`
* `o3-mini-2025-01-31`
* `gpt-4o-2024-08-06`
* `gpt-4o-2024-11-20`
* `gpt-4-turbo-2024-04-09`
* `gpt-4-0125-preview`
* `gpt-4-1106-preview`
* `gpt-4-0613`

Gemini:

* `gemini-2-0-flash`
* `gemini-2-0-pro-exp-02-05`

Meta:

* `meta-llama-3-1-405b-instruct`

DeepSeek:

* `deepseek-v3`
* `deepseek-r1`
