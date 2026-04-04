# Source: https://docs.openpipe.ai/features/fine-tuning/webapp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openpipe.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Fine Tuning via Webapp

>  Fine tune your models on filtered logs or uploaded datasets. Filter by prompt id and exclude requests with an undesirable output.

OpenPipe allows you to train, evaluate, and deploy your models all in the same place. We recommend training your models
through the webapp, which provides more flexibility and a smoother experience than the API. To fine-tune a new model, follow these steps:

1. Create a new dataset or navigate to an existing one.
2. Click "Fine Tune" in the top right.
3. Select a base model.
4. (Optional) Set custom hyperparameters and configure [pruning rules](/features/pruning-rules).
5. Click "Start Training" to kick off the job.

Once started, your model's training job will take at least a few minutes and potentially several hours, depending on the size of the
model and the amount of data. You can check your model's status by navigating to the Fine Tunes page and selecting your model.

For an example of how an OpenPipe model looks once it's trained, see our public [PII Redaction](https://app.openpipe.ai/p/BRZFEx50Pf/fine-tunes/6076ad69-cce5-4892-ae54-e0549bbe107f/general) model. Feel free to hit it with some sample queries!

<Frame><img src="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/fine-tuning.png?fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=9c2ca2e55d30ec9e59213b2381260282" alt="" data-og-width="2330" width="2330" data-og-height="1470" height="1470" data-path="images/features/fine-tuning.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/fine-tuning.png?w=280&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=a8d9b52147a2f9f76b0971f7b65f6687 280w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/fine-tuning.png?w=560&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=f9de2dea7c3c7b8273ac8877115b9dc9 560w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/fine-tuning.png?w=840&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=62878a0c6c3fed3b3b17d9bd8c4f66a6 840w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/fine-tuning.png?w=1100&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=4ec505b5b73683730a4f5bd1f23c1459 1100w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/fine-tuning.png?w=1650&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=bdd3e54e90769aebc7d12af006785a93 1650w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/fine-tuning.png?w=2500&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=c6b49c5acbbf78eb975c397d68d213ee 2500w" /></Frame>
