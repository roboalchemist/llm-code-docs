# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/text-classification/model-monitoring-and-data-drift.md

# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/natural-language-inference/model-monitoring-and-data-drift.md

# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/named-entity-recognition/model-monitoring-and-data-drift.md

# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/text-classification/model-monitoring-and-data-drift.md

# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/natural-language-inference/model-monitoring-and-data-drift.md

# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/named-entity-recognition/model-monitoring-and-data-drift.md

# Model Monitoring & Data Drift | Named Entity Recognition

> Learn how to monitor Named Entity Recognition models in production with Galileo NLP Studio, detecting data drift and maintaining model health effectively.

<iframe src="https://cdn.iframe.ly/GFTbcwg" width="100%" height="480px" allowfullscreen="" scrolling="no" allow="encrypted-media *;" />

Production data monitoring with Galileo

> *Is there training\<>production data drift? What unlabeled data should I select for my next training run? Is the model confidence dropping on an existing class in production? ...*

To answer the above questions and more with Galileo, you will need:

1. Your unlabeled production data

2. Your model

### <Icon icon="bolt" />Simply run an inference job on production data to view, inspect and select samples directly in the Galileo UI.

Here is what to expect:

• Get the list of [**drifted data samples**](/galileo/gen-ai-studio-products/galileo-ai-research/data-drift-detection) **out of the box**

• Get the list of [**on-the-class-boundary**](/galileo/gen-ai-studio-products/galileo-ai-research/class-boundary-detection) **samples out of the box**

• Quickly **compare model confidence and class distributions** between production and training runs

• Find **similar samples to low-confidence production data** within less than a second

... and a lot more

## Full Walkthrough Tutorial

Follow our [**example notebook with Pytorch**](https://colab.research.google.com/drive/1t-DL8aGGAWpEOUzBol9CeVDM1CmJibDk) or read the full tutorial below.

<Card title="Google Colaboratory" icon={<img src="https://ssl.gstatic.com/colaboratory-static/common/7a3cffa388d8f658cbf1801b7cbe5352/img/favicon.ico" alt="Google Colaboratory" />} href="https://colab.research.google.com/drive/1t-DL8aGGAWpEOUzBol9CeVDM1CmJibDk" />

After building and training a model, inference allows us to run that model on unseen data, such as deploying that model in production. In text classification, given an unseen set of documents, the task is to predict (as correctly as possible) the class of that document based on the data seen during training.

```
input = "Perfectly works fine after 10 years, would highly recommend. Great buy!!"
# Unknown output label
model.predict(input) --> "positive review"
```

### Logging the Data Inputs

Log your inference dataset. Galileo will join these samples with the model's outputs and present them in the Console. Note that unlike training, where ground truth labels are present for validation, during inference we assume that no ground truth labels exist.

```Py Pytorch

    import torch
    import dataquality
    import pandas as pd
    from transformers import AutoTokenizer

    class InferenceTextDataset(torch.utils.data.Dataset):
        def __init__(
            self, dataset: pd.DataFrame, inference_name: str
        ):
            self.dataset = dataset

            # telescope🌕 Galileo logging
            # Note 1: this works seamlessly because self.dataset has text, label, and
            # id columns. See `help(dq.log_dataset)` for more info
            # Note 2: We can set the inference_name for our run
            dq.log_dataset(self.dataset, split="inference", inference_name=inference_name)

            tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
            self.encodings = tokenizer(
                self.dataset["text"].tolist(), truncation=True, padding=True
            )

        def __getitem__(self, idx):
            x = torch.tensor(self.encodings["input_ids"][idx])
            attention_mask = torch.tensor(self.encodings["attention_mask"][idx])

            return self.dataset["id"][idx], x, attention_mask

        def __len__(self):
            return len(self.dataset)
```

### Logging the Inference Model Outputs

Log model outputs from within your model's forward function.

```py PyTorch

    import torch
    import torch.nn.functional as F
    from torch.nn import Linear
    from transformers import AutoModel


    class TextClassificationModel(torch.nn.Module):
        """Defines a Pytorch text classification bert based model."""

        def __init__(self, num_labels: int):
            super().__init__()
            self.feature_extractor = AutoModel.from_pretrained("distilbert-base-uncased")
            self.classifier = Linear(self.feature_extractor.config.hidden_size, num_labels)

        def forward(self, x, attention_mask, ids):
            """Model forward function."""
            encoded_layers = self.feature_extractor(
                input_ids=x, attention_mask=attention_mask
            ).last_hidden_state
            classification_embedding = encoded_layers[:, 0]
            logits = self.classifier(classification_embedding)

            # telescope🌕 Galileo logging
            dq.log_model_outputs(
                embs=classification_embedding, logits=logits, ids=ids
            )

            return logits
```

### Putting it all together

Login and initialize a *new* project + run name *or* one matching an existing training run (this will add inference to that training run in the console). Then, load and log your inference dataset; load a pre-trained model; set the split to inference and run your inference run; finally call `dq.finish()`!

Note: If you're extending a current training run, the `list_of_labels` logged for your dataset must match exactly that used during training.

```py PyTorch

    import numpy as np
    import io
    import random
    from smart_open import open as smart_open
    import s3fs
    import torch
    import torch.nn.functional as F
    import torchmetrics
    from tqdm.notebook import tqdm

    BATCH_SIZE = 32

    # telescope🌕 Galileo logging - initialize project/run name

    dq.login()
    dq.init(task_type="text_classification", project_name=project_name, run_name=run_name)

    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu"))

    inference_dataset = InferenceTextDataset(inference_df, inference_name="inference_run_1")

    # telescope🌕 Galileo logging
    # Note: if you are adding the inference run to a previous
    # training run, the labels and there order must match that used
    # in training. If you're logging inference in isolation then
    # this order does not matter.
    list_of_labels = ["labels", "ordered", "from", "trianing"]
    dq.set_labels_for_run(list_of_labels)

    inference_dataloader = torch.utils.data.DataLoader(
            inference_dataset,
            batch_size=BATCH_SIZE,
            shuffle=False
    )

    # Load your pre-trained model
    model_path = "path/to/your/model.pt"
    model = TextClassificationModel(num_labels=len(list_of_labels))
    model.load_state_dict(torch.load(model_path))
    model.to(device)

    model.eval()

    # telescope🌕 Galileo logging - naming your inference run
    inference_name = "inference_run_1"
    dq.set_split("inference", inference_name)

    for data in tqdm(inference_dataloader):
        x_idxs, x, attention_mask = data
        x = x.to(device)
        attention_mask = attention_mask.to(device)

        model(x, attention_mask, x_idxs)

    print("Finished Inference")

    # telescope🌕 Galileo logging
    dq.finish()

    print("Finished uploading")
```

To learn more about **Data Drift**, **Class Boundary Detection** or other Model Monitoring features, check out the [Galileo Product Features Guide](/galileo/how-to-and-faq/galileo-product-features).
