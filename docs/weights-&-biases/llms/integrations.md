# Source: https://docs.wandb.ai/weave/guides/integrations.md

# Source: https://docs.wandb.ai/models/integrations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrations overview

> Explore W&B integrations with ML frameworks, cloud platforms, and workflow orchestration tools

W\&B integrates with popular machine learning frameworks, cloud platforms, and workflow orchestration tools to help you track experiments, log metrics, and manage models seamlessly.

## Popular ML integrations:

<CardGroup cols={2}>
  <Card title="PyTorch Lightning" href="/models/integrations/lightning">
    Integrate W\&B with your PyTorch Lightning code to add experiment tracking to your pipeline.
  </Card>

  <Card title="HuggingFace Transformers" href="/models/integrations/huggingface">
    Optimize HuggingFace Transformer models with W\&B for experiment tracking and model management.
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="Keras" href="/models/integrations/keras">
    Use W\&B and Keras for machine learning experiment tracking, dataset versioning, and project collaboration.
  </Card>

  <Card title="YOLOv5" href="/models/integrations/yolov5">
    Use the "You Only Look Once" (aka YOLOv5) real-time object detection framework and W\&B to track model metrics, inspect model outputs, and restart interrupted runs.
  </Card>
</CardGroup>

If the library you use is not supported natively, you can still integrate W\&B using the W\&B [Python SDK](/docs/library/integrations/python-sdk). See [Add W\&B to any library](/models/integrations/add-wandb-to-any-library) for best practices and implementation guidance.
