# Source: https://docs.aporia.com/nlp/example-question-answering.md

# Source: https://docs.aporia.com/v1/nlp/example-question-answering.md

# Source: https://docs.aporia.com/nlp/example-question-answering.md

# Source: https://docs.aporia.com/v1/nlp/example-question-answering.md

# Example: Question Answering

**Question answering models can retrieve the answer to a question from a given text**, which is useful for searching for an answer in a document.&#x20;

Throughout the guide, we will use a simple question answering model based on 🤗 [HuggingFace](https://huggingface.co/):thumbsup:

```python
>>> from transformers import pipeline

>>> qa_model = pipeline("question-answering")
```

This downloads a default pretrained model and tokenizer for Questioning Answering. Now you can use the `qa_model` on your target question / context:

```python
qa_model(
    question="Where are the best cookies?",
    context="The best cookies are in Aporia's office."
)

# ==> {'score': 0.8362494111061096,
#      'start': 24,
#      'end': 39,
#      'answer': "Aporia's office"}
```

## Extract Embeddings&#x20;

To extract embeddings from the model, we'll first need to do two things:

1. Pass `output_hidden_states=True` to our model params.
2. When we call `pipeline(...)` it does a lot of things for us - preprocessing, inference, and postprocessing. **We'll need to break all this**, so we can interfere in the middle and get embeddings [😉](https://emojipedia.org/winking-face/)

In other words:

```python
qa_model = pipeline("question-answering", model_kwargs={"output_hidden_states": True})

# Preprocess
model_inputs = next(qa_model.preprocess(QuestionAnsweringPipeline.create_sample(
    question="Where are the best cookies?", 
    context="The best cookies are in Aporia's office."
)))

# Inference
model_output = qa_model.model(input_ids=model_inputs["input_ids"])

# Postprocessing
start, end = model_output[:2]
qa_model.postprocess([{"start": start, "end": end, **model_inputs}])
  # ==> {'score': 0.8362494111061096, 'start': 24, 'end': 39, 'answer': "Aporia's office"}
```

And finally, to extract embeddings for this prediction:

```python
embeddings = torch.mean(model_output.hidden_states[-1], dim=1).squeeze()
```

## Storing your Predictions

The next step would be to store your predictions in a data store, including the embeddings themselves. For more information on storing your predictions, please check out the [Storing Your Predictions](https://docs.aporia.com/v1/storing-your-predictions) section.

For example, you could use a Parquet file on S3 or a Postgres table that looks like this:

<table><thead><tr><th width="88.33333333333331">id</th><th width="291">question</th><th width="227">context</th><th width="263">embeddings</th><th width="187.66666666666674">answer</th><th width="186">score</th><th width="207">timestamp</th></tr></thead><tbody><tr><td>1</td><td>Where are the best cookies?</td><td>The best cookies are in...</td><td><code>[0.77, 0.87, 0.94, ...]</code></td><td><code>Aporia's Office</code></td><td>0.982</td><td>2021-11-20 13:41:00</td></tr><tr><td>2</td><td>Where is the best hummus?</td><td>The best hummus is in...</td><td><code>[0.97, 0.82, 0.13, ...]</code></td><td><code>Another Place</code></td><td>0.881</td><td>2021-11-20 13:45:00</td></tr><tr><td>3</td><td>Where is the best burger?</td><td>The best burger is in...</td><td><code>[0.14, 0.55, 0.66, ...]</code></td><td><code>Blablabla</code></td><td>0.925</td><td>2021-11-20 13:49:00</td></tr></tbody></table>

## Integrate to Aporia

Now let’s add some monitoring to this model 🚀 To monitor this model in Aporia, the first step is to create a model version:

```python
apr_model = aporia.create_model_version(
  model_id="<MODEL_ID>",
  model_version="v1",
  model_type="multiclass"
  raw_inputs={
    "question": "text",
    "context": "text"
  },
  features={
     "embeddings": {"type": "tensor", "dimensions": [768]}
  },
  predictions={
    "answer": "string",
    "score": "numeric"
  },
)
```

Next, we can log predictions directly to Aporia:

```python
qa_model = pipeline(
    task="question-answering",
    model_kwargs={"output_hidden_states": True}
)


def predict(question: str, answer: str):
    # Preprocess
    model_inputs = next(qa_model.preprocess(QuestionAnsweringPipeline.create_sample(
        question="Where are the best cookies?", 
        context="The best cookies are in Aporia's office."
    )))
    
    # Inference
    model_output = qa_model.model(input_ids=model_inputs["input_ids"])
    
    # Postprocessing
    start, end = model_output[:2]
    result = qa_model.postprocess([{"start": start, "end": end, **model_inputs}])
    
    # Log prediction to Aporia
    apr_model.log_prediction(
        id=str(uuid.uuid4()),
        raw_inputs={
            "question": question,
            "context": context
        },
        features={
            "embeddings": embeddings
        },
        predictions={
            "answer": result["answer"],
            "score": result["score"]
        }
    )
    
    return result
```

Alternatively, connect Aporia to a data source. For more information, see [Data Sources - Overview:](https://docs.aporia.com/v1/data-sources)

```python
apr_model.connect_serving(
    data_source=<DATA_SOURCE>,
    
    id_column="id",
    timestamp_column="timestamp"
)
```

Your model should now be integrated to Aporia! 🎉
