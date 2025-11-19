# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/natural-language-inference.md

# Natural Language Inference

> Leverage Galileo NLP Studio for natural language inference (NLI), enabling accurate predictions and model performance monitoring.

[Natural Language Inference (NLI)](http://nlpprogress.com/english/natural_language_inference.html), also known as Recognizing Textual Entailment (RTE), is a sequence classification problem, where given two (short, ordered) documents -- `premise` and `hypothesis`, the task is to determine the inference relation between them.
Samples are classified into one of the three labels depending on whether a `hypothesis` is true (entailment), false (contradiction), or undetermined (neutral) given a `premise`. Here's an example:

```
Premise: A man inspects the uniform of a figure in some East Asian country.
Hypothesis: The man is sleeping.
Label: contradiction


Premise: An older and younger man smiling.
Hypothesis: Two men are smiling and laughing at the cats playing on the floor.
Label: neutral


Premise: A soccer game with multiple males playing.
Hypothesis: Some men are playing a sport.
Label: entailment
```

**Note**: For NLI you must combine the `premise` and `hypothesis` documents for logging. We recommend joining the document text with a separator such as `\<>` to help visualization in the Galileo console.

### Get started with a notebook <Icon icon="book" />

* [PyTorch Notebook](https://colab.research.google.com/github/rungalileo/examples/blob/main/examples/natural_language_inference/Natural_Language_Inference_using_Pytorch_and_%F0%9F%94%AD_Galileo.ipynb)

* [TensorFlow Notebook](https://colab.research.google.com/github/rungalileo/examples/blob/main/examples/natural_language_inference/Natural_Language_Inference_using_TensorFlow_and_%F0%9F%94%AD_Galileo.ipynb)

### Watch our [NLI tutorials](https://www.loom.com/share/4fada6038bd04e5e8e8017d7661aa41d?sid=d2fb9fdd-4845-4bb6-863a-da208985788f) <Icon icon="cassette-vhs" />

###

[](#start-integrating-galileo-with-our-supported-frameworks)

Start integrating Galileo with our supported frameworks <Icon icon="laptop" />

* HuggingFace <Icon icon="face-smiling-hands" />

* PyTorch

* TensorFlow

* Keras
