# Source: https://docs.mystic.ai/docs/how-to-deploy-a-huggingface-model.md

# How to deploy a Hugging Face model

We outline how to deploy a HuggingFace pretrained transformers model. For this example, we use a text classification sentiment analysis model.

# Initialise a new pipeline

In an empty directory, you can initialise a new project by running the following command:

```shell
pipeline container init
```

You should see 2 new files appear, `my_new_pipeline.py` and `pipeline.yaml`, with some initial content that we will later update. The `.py` file should contain the code that should be executed at runtime while the `.yaml` file is a configuration file for the pipeline.

# The pipeline graph

Substitute the following code into `my_new_pipeline.py`:

```python my_new_pipeline.py
import numpy as np  
import preprocessor  
import torch  
from transformers import AutoConfig, AutoModelForSequenceClassification, AutoTokenizer

from pipeline import Pipeline, Variable, entity, pipe

def softmax(x):  
    """Used to convert raw model output scores into probabilities."""  
    x_max = np.amax(x, keepdims=True)  
    exp_x_shifted = np.exp(x - x_max)  
    return exp_x_shifted / np.sum(exp_x_shifted, keepdims=True)

#: The HuggingFace source model  
HF_MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"

@entity  
class RobertaPipeline:  
    def __init__(self) -> None:  
        self.tokenizer = None  
        self.config = None  
        self.model = None  
        self.device = None

    @pipe(on_startup=True, run_once=True)
    def load(self) -> None:
        """Load the model, tokenizer and config"""
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model = AutoModelForSequenceClassification.from_pretrained(
            HF_MODEL_NAME
        ).to(self.device)

        self.tokenizer = AutoTokenizer.from_pretrained(HF_MODEL_NAME)
        # Used in postprocessing to map IDs to labels
        self.config = AutoConfig.from_pretrained(HF_MODEL_NAME)

    @pipe
    def preprocess(self, raw_text: str) -> str:
        """Preprocesses the input text by filtering out unwanted strings.
        for further details, see https://github.com/s/preprocessor"""
        options = [
            preprocessor.OPT.URL,
            preprocessor.OPT.MENTION,
            preprocessor.OPT.ESCAPE_CHAR,
            preprocessor.OPT.RESERVED,
        ]
        preprocessor.set_options(*options)
        return preprocessor.clean(raw_text)

    @pipe
    def predict(self, input_text: str) -> list[float]:
        """Tokenize the input and feed it to the model"""
        encoded_input = self.tokenizer(input_text, return_tensors="pt").to(self.device)
        output = self.model(**encoded_input)
        # Detatch scores from the computation graph and converted into a numpy array.
        scores = output[0][0].detach().cpu().numpy()
        return scores

    @pipe
    def postprocess(self, scores: list[float]) -> list[dict[str, float]]:
        """The raw scores from the model are passed through the softmax
        function to convert them into probabilities.
        The final output represents the model's confidence for each class
        (positive, negative, neutral)."""
        probablities = softmax(scores)
        ranking = np.argsort(probablities)
        ranking = ranking[::-1]
        result = [
            dict(
                label=self.config.id2label[ranking[i]],
                score=np.round(float(probablities[ranking[i]]), 4),
            )
            for i in range(probablities.shape[0])
        ]
        return result
  
  
# : Define the computational graph for the pipeline
with Pipeline() as builder:  
    input_text = Variable(  
        str,  
        title="input_text",  
        description="The text that sentiment analysis will be performed on.",  
        max_length=512,  
    )  
    roberta_pipeline = RobertaPipeline()  
    roberta_pipeline.load()  
    text = roberta_pipeline.preprocess(input_text)  
    scores = roberta_pipeline.predict(text)  
    output = roberta_pipeline.postprocess(scores)  
    builder.output(output)

# Get the computational graph
my_new_pipeline = builder.get_pipeline()
```

# The pipeline config

Substitute the following configuration into `pipeline.yaml`:

```yaml pipeline.yaml
runtime:
  container_commands:
    - apt-get update
    - apt-get install -y git
  python:
    version: "3.10"
    requirements:
      - pipeline-ai
      - tweet-preprocessor==0.6.0
      - torch==2.0.1
      - transformers==4.32.0
    cuda_version: "11.4"
accelerators: ["nvidia_t4"]
accelerator_memory: null
pipeline_graph: new_pipeline:my_new_pipeline
pipeline_name: twitter-roberta-base-sentiment
description: null
readme: null
extras: {}
```

## Build pipeline docker image

To build a docker image of the pipeline, run the following command from the same directory containing the files:

```shell
pipeline container build
```

## Run container locally

Before uploading your pipeline, we strongly encourage to test your pipeline locally, to ensure it behaves as expected. To do so, run:

```shell
pipeline container up
```

It will take a little while for the model to be downloaded from HuggingFace. The container comes with [an API](http;//localhost:14300), allowing you to make local inference requests. Check out the [play form ](http://localhost:14300/play) to quickly start testing out the pipeline.

## Push pipeline docker image

To upload the pipeline, or push the docker image of the pipeline to the Mystic docker registry, run the following command:

```shell
pipeline container push
```