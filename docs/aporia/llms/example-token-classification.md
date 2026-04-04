# Source: https://docs.aporia.com/nlp/example-token-classification.md

# Source: https://docs.aporia.com/v1/nlp/example-token-classification.md

# Example: Token Classification

Token classification is a natural language understanding task in which a label is assigned to some tokens in a text&#x20;

**Named Entity Recognition (NER)** and **Part-of-Speech (PoS)** tagging are two popular token classification subtasks. NER models could be trained to recognize specific entities in a text, such as dates, individuals, and locations, while PoS tagging would identify which words in a text are verbs, nouns, and punctuation marks.

This guide will walk you through an example of NER model monitoring using spacy. Let's start by creating a dummy model:

```python
import spacy

NER = spacy.load("en_core_web_sm")
```

And let’s assume this is how our prediction function looks like (maybe it’s a part of an http server, for example):

```python
def predict(request_id: str, raw_text: str):
  return {
    entity.text: entity.label_ 
    for entity in NER(raw_text).ents
  }
```

Now let’s add some monitoring to this function 🚀  But before that, let’s create a new model in Aporia:

```python
apr_model = aporia.create_model_version(
    model_id="<MODEL_ID>",
    model_version="v1",
    model_type="multiclass",
    raw_inputs={
        "entity_text": "text",
    },
    features={
        "embeddings": {"type": "tensor", "dimensions": [96]},
    },
    predictions={
        "entity_label": "string"
    }
)
```

This is a `multiclass` model, as each entity can be classified to one of two or more entities.

Now, we can change the `predict` function to log predictions to Aporia:

```python
def predict(request_id: str, raw_text: str):
    entities = NER(raw_text).ents

    for i, entity in enumerate(entities):
        apr_model.log_prediction(
            id=f"{request_id}_{i}",
            raw_inputs={"entity_text": entity.text},
            features={"embeddings": entity.vector},
            predictions={"entity_label": entity.label_},
        )

      return {
        entity.text: entity.label_ 
        for entity in entities
      }
```

Now, here are some sample monitors you can define:

* Make sure the distribution of the different entity labels doesn’t drift across time
* Make sure the distribution of the embedding vector doesn’t drift across time

**General Metadata**

But this is just the very beginning. Here, you can get really creative and start adding more information to each Aporia prediction.

First, if you have any general metadata of your prediction request (unrelated to the NER model itself), you can go ahead and log this metadata as raw inputs. This will let you make sure the model doesn’t drift or bias specific segments of your data (e.g gender, company type, etc.).

**Entity-specific Metadata**

Let’s start with an example. For each entity, you can log the word count of that entity. Then, you’ll be able to monitor drift in the word count between different labels.

For example, you might expect `country` entities to be 1-2 words, but `organization` entities to have a distribution of 1-5 words, with most organizations having 2-3 words. If suddenly you see an `organization` with 10 words - it is an outlier and probably not really an organization :)

But word count is just a simple example, and depending on your application, you can add various types of metadata to make monitoring really great :tada:<br>
