# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/multi-label-text-classification.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Multi Label Text Classification

> Implement multi-label text classification in Galileo NLP Studio to accurately label datasets, streamline workflows, and enhance model training.

[Multi-label text classification](https://en.wikipedia.org/wiki/Multi-label_classification) (MLTC), also known as multi-output text classification is a variant of the text classification problem, where multiple labels are assigned to each sample. It is a generalization of [multiclass text classification](https://github.com/rungalileo/docs/blob/main/supported-ml-use-cases/broken-reference/README.md), where a single label is assigned to each sample.

Samples are assigned a subset of the available label classes, where there are no constraints on how many classes a sample can be assigned. We refer to the set of available label classes as tasks and behind the scenes, Galileo treats assigning each class (a task) as a binary prediction problem - 1 if the given class is assigned, 0 otherwise. Here's an example:

```
Input: Now I'm wondering on what I've been missing out. Again thank you for this.
Output: Curosity, Gratitude

Input: That is odd.
Output: Disappointment, Disgust
```

## Get started with a notebook <Icon icon="book" />

* [PyTorch Notebook](https://colab.research.google.com/github/rungalileo/examples/blob/main/examples/multi_label_text_classification/Multi_Label_Text_Classification_using_Pytorch_and_%F0%9F%94%AD_Galileo.ipynb)

* [TensorFlow Notebook](https://colab.research.google.com/github/rungalileo/examples/blob/main/examples/multi_label_text_classification/Multi_Label_Text_Classification_using_TensorFlow_and_%F0%9F%94%AD_Galileo.ipynb)

## Start integrating Galileo with our supported frameworks <Icon icon="laptop" />

* HuggingFace <Icon icon="face-smiling-hands" />

* PyTorch

* TensorFlow

* Keras
