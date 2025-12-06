# Source: https://www.sbert.net/examples/cross_encoder/training/nli/README.html

# Natural Language Inference[ïƒ?](#natural-language-inference "Link to this heading")

Given two sentence (premise and hypothesis), Natural Language Inference (NLI) is the task of deciding if the premise entails the hypothesis, if they are contradiction, or if they are neutral. Commonly used NLI dataset are [SNLI](https://huggingface.co/datasets/stanfordnlp/snli) and [MultiNLI](https://huggingface.co/datasets/nyu-mll/multi_nli).

To train a CrossEncoder on NLI, see the following example file:

- **[[training_nli.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/nli/training_nli.py)**:

  This example uses [[`CrossEntropyLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.CrossEntropyLoss "sentence_transformers.cross_encoder.losses.CrossEntropyLoss") to train the CrossEncoder model to predict the highest logit for the correct class out of â€œcontradictionâ€?, â€œentailmentâ€?, and â€œneutralâ€?.

You can also train and use [[`SentenceTransformer`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") models for this task. See [Sentence Transformer \> Training Examples \> Natural Language Inference](../../../sentence_transformer/training/nli/README.html) for more details.

## Data[ïƒ?](#data "Link to this heading")

We combine [SNLI](https://huggingface.co/datasets/stanfordnlp/snli) and [MultiNLI](https://huggingface.co/datasets/nyu-mll/multi_nli) into a dataset we call [AllNLI](https://huggingface.co/datasets/sentence-transformers/all-nli). These two datasets contain sentence pairs and one of three labels: entailment, neutral, contradiction:

  Sentence A (Premise)                                                 Sentence B (Hypothesis)                                              Label
  -------------------------------------------------------------------- -------------------------------------------------------------------- ---------------
  A soccer game with multiple males playing.                           Some men are playing a sport.                                        entailment
  An older and younger man smiling.                                    Two men are smiling and laughing at the cats playing on the floor.   neutral
  A man inspects the uniform of a figure in some East Asian country.   The man is sleeping.                                                 contradiction

We format AllNLI in a few different subsets, compatible with different loss functions. See for example the [pair-class subset of AllNLI](https://huggingface.co/datasets/sentence-transformers/all-nli/viewer/pair-class).

## CrossEntropyLoss[ïƒ?](#crossentropyloss "Link to this heading")

The [[`CrossEntropyLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.CrossEntropyLoss "sentence_transformers.cross_encoder.losses.CrossEntropyLoss") is a rather elementary loss that applies the common [[`torch.nn.CrossEntropyLoss`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html#torch.nn.CrossEntropyLoss "(in PyTorch v2.9)") on the logits (a.k.a. outputs, raw predictions) produced after 1) passing the tokenized text pairs through the model and 2) applying the optional activation function over the logits. Itâ€™s very commonly used if the CrossEncoder model has to predict more than just 1 class.

## Inference[ïƒ?](#inference "Link to this heading")

You can perform inference using any of the [[pre-trained CrossEncoder models for NLI]](../../../../docs/cross_encoder/pretrained_models.html#nli) like so:

    from sentence_transformers import CrossEncoder

    model = CrossEncoder("cross-encoder/nli-deberta-v3-base")
    scores = model.predict([
        ("A man is eating pizza", "A man eats something"),
        ("A black race car starts up in front of a crowd of people.", "A man is driving down a lonely road."),
    ])

    # Convert scores to labels
    label_mapping = ["contradiction", "entailment", "neutral"]
    labels = [label_mapping[score_max] for score_max in scores.argmax(axis=1)]
    # => ['entailment', 'contradiction']