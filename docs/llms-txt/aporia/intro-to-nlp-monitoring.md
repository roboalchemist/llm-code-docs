# Source: https://docs.aporia.com/nlp/intro-to-nlp-monitoring.md

# Source: https://docs.aporia.com/v1/nlp/intro-to-nlp-monitoring.md

# Intro to NLP Monitoring

This guide will walk you through the core concepts of NLP model monitoring. Before soon, you'll be able to detect drift and measure model performance for your NLP models 🚀

Throughout the guide, we will use a simple sentiment analysis model based on 🤗 [HuggingFace](https://huggingface.co/):

```python
>>> from transformers import pipeline

>>> classifier = pipeline("sentiment-analysis")
```

This downloads a default pretrained model and tokenizer for Sentiment Analysis. Now you can use the `classifier` on your target text:

```python
>>> classifier("I love cookies and Aporia")
[{'label': 'POSITIVE', 'score': 0.9997883439064026}]
```

## Extract Embeddings&#x20;

To effectively detect drift in NLP models, we use *embeddings*.

{% hint style="info" %}
**But... what are embeddings?**

Textual data is complex, high-dimensional, and free-form. Embeddings represent text as *low-dimensional vectors*.&#x20;

Various language models, such as [Word2Vec](https://en.wikipedia.org/wiki/Word2vec) and transformer-based models like [BERT](https://en.wikipedia.org/wiki/BERT_\(language_model\)), are used obtain embeddings for NLP models. In case of BERT, embeddings are usually vectors of size 768.
{% endhint %}

To get embeddings for our HuggingFace model, we'll need to do two things:

1. Pass `output_hidden_states=True` to our model params.
2. When we call `pipeline(...)` it does a lot of things for us - preprocessing, inference, and postprocessing. **We'll need to break all this**, so we can interfere in the middle and get embeddings [😉](https://emojipedia.org/winking-face/)

In other words:

```python
classifier = pipeline(
    task="sentiment-analysis",
    model_kwargs={"output_hidden_states": True}
)

# Preprocessing
model_input = classifier.preprocess("I love cookies and Aporia")

# Inference
model_output = classifier.forward(model_input)

# Postprocessing
classifier.postprocess(model_output)
  # ==> {'label': 'POSITIVE', 'score': 0.9998340606689453} 
```

And finally, to extract embeddings for this prediction:

```python
embeddings = torch.mean(model_output.hidden_states[-1], dim=1).squeeze()
```

## Storing your Predictions

The next step would be to store your predictions in a data store, including the embeddings themselves. For more information on storing your predictions, please check out the [Storing Your Predictions](https://docs.aporia.com/v1/storing-your-predictions) section.

For example, you could use a Parquet file on S3 or a Postgres table that looks like this:

<table><thead><tr><th width="88.33333333333331">id</th><th width="297">raw_text</th><th width="263">embeddings</th><th width="162.66666666666674">prediction</th><th width="186">score</th><th width="207">timestamp</th></tr></thead><tbody><tr><td>1</td><td>I love cookies and Aporia</td><td><code>[0.77, 0.87, 0.94, ...]</code></td><td><code>POSITIVE</code></td><td>0.98</td><td>2021-11-20 13:41:00</td></tr><tr><td>2</td><td>This restaurant was really bad</td><td><code>[0.97, 0.82, 0.13, ...]</code></td><td><code>NEGATIVE</code></td><td>0.88</td><td>2021-11-20 13:45:00</td></tr><tr><td>3</td><td>Hummus is the tastiest thing ever</td><td><code>[0.14, 0.55, 0.66, ...]</code></td><td><code>POSITIVE</code></td><td>0.92</td><td>2021-11-20 13:49:00</td></tr></tbody></table>

## Integrate to Aporia

Now let’s add some monitoring to this model 🚀 To monitor this model in Aporia, the first step is to create a model version:

```python
apr_model = aporia.create_model_version(
  model_id="<MODEL_ID>",
  model_version="v1",
  model_type="multiclass"
  raw_inputs={
    "raw_text": "text",
  },
  features={
     "embeddings": {"type": "tensor", "dimensions": [768]}
  },
  predictions={
    "prediction": "string",
    "score": "numeric"
  },
)
```

Next, we can log predictions directly to Aporia:

```python
classifier = pipeline(
    task="sentiment-analysis",
    model_kwargs={"output_hidden_states": True}
)


def predict(raw_text: str):
    # Run model pipeline
    model_input = classifier.preprocess(raw_text)
    model_output = classifier.forward(model_input)
    result = classifier.postprocess(model_output)
    
    # Extract embeddings
    embeddings = torch.mean(model_output.hidden_states[-1], dim=1).squeeze().tolist()
    
    # Log prediction to Aporia
    apr_model.log_prediction(
        id=str(uuid.uuid4()),
        raw_inputs={
            "raw_text": raw_text
        },
        features={
            "embeddings": embeddings
        },
        predictions={
            "prediction": result["prediction"],
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

## Next steps

* **Create a custom dashboard for your model in Aporia** - Drag & drop widgets to show different performance metrics, top drifted features, etc.
* **Visualize NLP drift using Aporia's Embeddings Projector** - Use the UMap tool to visually see drift between different datasets in production.
* **Set up alerts to get notified for ML issues** - Including data integrity issues, model performance degradation, and model drift.
