# Source: https://www.sbert.net/examples/cross_encoder/training/quora_duplicate_questions/README.html

# Quora Duplicate Questions[ïƒ?](#quora-duplicate-questions "Link to this heading")

This folder contains scripts that demonstrate how to train SentenceTransformers for **Information Retrieval**. As a simple example, we will use the [Quora Duplicate Questions dataset](https://huggingface.co/datasets/sentence-transformers/quora-duplicates). It contains over 500,000 sentences with over 400,000 pairwise annotations whether two questions are a duplicate or not.

Models trained on this dataset can be used for mining duplicate questions, i.e., given a large set of sentences (in this case questions), identify all pairs that are duplicates. Due to how [[`CrossEncoder`]](../../../../docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder") models work only on pairs of texts, they are best deployed after an initial filtering using a [[`SentenceTransformer`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") model. See [Sentence Transformer \> Usage \> Paraphrase Mining](../../../sentence_transformer/applications/paraphrase-mining/README.html) for an example how to use sentence transformers to mine for duplicate questions / paraphrases across hundred thousands of sentences.

After the initial filtering, a [[`CrossEncoder`]](../../../../docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder") model can be used to rerank the top e.g. 100 candidates into the top e.g. 10. Because a [[`CrossEncoder`]](../../../../docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder") can apply attention across the sentences from the pairs, the model can give better scores than the [[`SentenceTransformer`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") can.

To train a CrossEncoder on the Quora Duplicate Questions dataset, see the following example file:

- **[[training_quora_duplicate_questions.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/cross_encoder/training/quora_duplicate_questions/training_quora_duplicate_questions.py)**:

  This example uses [[`BinaryCrossEntropyLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss "sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss") to train the CrossEncoder model to give high scores for identical questions and low scores for different questions.

You can also train and use [[`SentenceTransformer`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") models for this task. See [Sentence Transformer \> Training Examples \> Quora Duplicate Questions](../../../sentence_transformer/training/quora_duplicate_questions/README.html) for more details.

## Training[ïƒ?](#training "Link to this heading")

Choosing the right loss function is crucial for finetuning useful models. [[`BinaryCrossEntropyLoss`]](../../../../docs/package_reference/cross_encoder/losses.html#sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss "sentence_transformers.cross_encoder.losses.BinaryCrossEntropyLoss") remains a very solid loss for training any [[`CrossEncoder`]](../../../../docs/package_reference/cross_encoder/cross_encoder.html#sentence_transformers.cross_encoder.CrossEncoder "sentence_transformers.cross_encoder.CrossEncoder") model that has just one output class, i.e. if it just outputs one score.

![CrossEncoder architecture](https://raw.githubusercontent.com/UKPLab/sentence-transformers/master/docs/img/CrossEncoder.png)

For each question pair, we pass question A and question B through the BERT-based model, after which a classifier head converts the intermediary representation from the BERT-based model into a similarity score. With this loss, we apply [[`torch.nn.BCEWithLogitsLoss`]](https://docs.pytorch.org/docs/stable/generated/torch.nn.BCEWithLogitsLoss.html#torch.nn.BCEWithLogitsLoss "(in PyTorch v2.9)") which accepts logits (a.k.a. outputs, raw predictions) and gold similarity scores (1 if duplicate, 0 if not duplicate) to compute a loss denoting how well the model has done. This loss is then minimized to improve the performance of the model.

## Inference[ïƒ?](#inference "Link to this heading")

You can perform inference using any of the [[pre-trained CrossEncoder models for Duplicate Question detection]](../../../../docs/cross_encoder/pretrained_models.html#quora-duplicate-questions) like so:

    from sentence_transformers import CrossEncoder

    model = CrossEncoder('cross-encoder/quora-distilroberta-base')
    scores = model.predict([
        ('What do apples consist of?', 'What are in Apple devices?'),
        ('How do I get good at programming?', 'How to become a good programmer?')
    ])
    print(scores)
    # [0.00056, 0.97536]