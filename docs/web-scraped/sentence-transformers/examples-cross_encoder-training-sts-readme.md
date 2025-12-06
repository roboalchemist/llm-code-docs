# Source: https://www.sbert.net/examples/cross_encoder/training/sts/README.html

# Semantic Textual Similarity[ïƒ?](#semantic-textual-similarity "Link to this heading")

Semantic Textual Similarity (STS) assigns a score on the similarity of two texts. In this example, we use the [stsb](https://huggingface.co/datasets/sentence-transformers/stsb) dataset as training data to fine-tune a [[`CrossEncoder`]](../../../../docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder") model. See the following example script how to tune [[`CrossEncoder`]](../../../../docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder") models on STS data:

- **[[training_stsbenchmark.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/sts/training_stsbenchmark.py)** - This example shows how to create and finetune a CrossEncoder model from a pre-trained transformer model (e.g. [[`distilroberta-base`]](https://huggingface.co/distilbert/distilroberta-base)).

You can also train and use [[`SentenceTransformer`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") models for this task. See [Sentence Transformer \> Training Examples \> Semantic Textual Similarity](../../../sentence_transformer/training/sts/README.html) for more details.

## Training data[ïƒ?](#training-data "Link to this heading")

In STS, we have sentence pairs annotated together with a score indicating the similarity. In the original STSbenchmark dataset, the scores range from 0 to 5. We have normalized these scores to range between 0 and 1 in [stsb](https://huggingface.co/datasets/sentence-transformers/stsb), as that is required for [[`BinaryCrossEntropyLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss "sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss") as you can see in the [Loss Overiew](../../../../docs/cross_encoder/loss_overview.html).

Here is a simplified version of our training data:

    from datasets import Dataset

    sentence1_list = ["My first sentence", "Another pair"]
    sentence2_list = ["My second sentence", "Unrelated sentence"]
    labels_list = [0.8, 0.3]
    train_dataset = Dataset.from_dict()
    # => Dataset()
    print(train_dataset[0])
    # => 
    print(train_dataset[1])
    # => 

In the aforementioned scripts, we directly load the [stsb](https://huggingface.co/datasets/sentence-transformers/stsb) dataset:

    from datasets import load_dataset

    train_dataset = load_dataset("sentence-transformers/stsb", split="train")
    # => Dataset()

## Loss Function[ïƒ?](#loss-function "Link to this heading")

We use [[`BinaryCrossEntropyLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss "sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss") as our loss function.

![CrossEncoder architecture](https://raw.githubusercontent.com/UKPLab/sentence-transformers/master/docs/img/CrossEncoder.png)

For each sentence pair, we pass sentence A and sentence B through the BERT-based model, after which a classifier head converts the intermediary representation from the BERT-based model into a similarity score. With this loss, we apply [[`torch.nn.BCEWithLogitsLoss`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.BCEWithLogitsLoss.html#torch.nn.BCEWithLogitsLoss "(in PyTorch v2.9)") which accepts logits (a.k.a. outputs, raw predictions) and gold similarity scores to compute a loss denoting how well the model has done on this batch. This loss can be minimized to improve the performance of the model.

## Inference[ïƒ?](#inference "Link to this heading")

You can perform inference using any of the [[pre-trained CrossEncoder models for STS]](../../../../docs/cross_encoder/pretrained_models.html#stsbenchmark) like so:

    from sentence_transformers import CrossEncoder

    model = CrossEncoder("cross-encoder/stsb-roberta-base")
    scores = model.predict([("It's a wonderful day outside.", "It's so sunny today!"), ("It's a wonderful day outside.", "He drove to work earlier.")])
    # => array([0.60443085, 0.00240758], dtype=float32)