# Source: https://www.sbert.net/examples/sentence_transformer/training/peft/README.html

# Training with PEFT Adapters[ïƒ?](#training-with-peft-adapters "Link to this heading")

Sentence Transformers has been integrated with [PEFT](https://huggingface.co/docs/peft/en/index) (Parameter-Efficient Fine-Tuning), allowing you to finetune embedding models without fine-tuning all of the model parameters. Instead, with PEFT methods you are only finetuning a fraction of (extra) model parameters with only a minor hit in performance compared to full model finetuning.

PEFT Adapter models can be loaded just like any others, for example [tomaarsen/bert-base-uncased-gooaq-peft](https://huggingface.co/tomaarsen/bert-base-uncased-gooaq-peft) which does not contain a [`model.safetensors`] but only a tiny [`adapter_model.safetensors`]:

    from sentence_transformers import SentenceTransformer

    # Download from the ð¤ Hub
    model = SentenceTransformer("tomaarsen/bert-base-uncased-gooaq-peft")
    # Run inference
    sentences = [
        "is toprol xl the same as metoprolol?",
        "Metoprolol succinate is also known by the brand name Toprol XL. It is the extended-release form of metoprolol. Metoprolol succinate is approved to treat high blood pressure, chronic chest pain, and congestive heart failure.",
        "Metoprolol starts to work after about 2 hours, but it can take up to 1 week to fully take effect. You may not feel any different when you take metoprolol, but this doesn't mean it's not working. It's important to keep taking your medicine"
    ]
    embeddings = model.encode(sentences)
    print(embeddings.shape)
    # [3, 768]

    # Get the similarity scores for the embeddings
    similarities = model.similarity(embeddings[0], embeddings[1:])
    print(similarities)
    # tensor([[0.7913, 0.4976]])

## Compatibility Methods[ïƒ?](#compatibility-methods "Link to this heading")

The [[`SentenceTransformer`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer "sentence_transformers.SentenceTransformer") supports 7 methods for interacting with the PEFT Adapters:

> ::: 
> - [[`add_adapter()`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.add_adapter "sentence_transformers.SentenceTransformer.add_adapter"): Adds a fresh new adapter to the current model for training.
>
> - [[`load_adapter()`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.load_adapter "sentence_transformers.SentenceTransformer.load_adapter"): Load adapter weights from a file or Hugging Face Hub repository.
>
> - [[`active_adapters()`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.active_adapters "sentence_transformers.SentenceTransformer.active_adapters"): Gets the current active adapters.
>
> - [[`set_adapter()`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.set_adapter "sentence_transformers.SentenceTransformer.set_adapter"): Tell your model to use a specific adapter and disable all others.
>
> - [[`enable_adapters()`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.enable_adapters "sentence_transformers.SentenceTransformer.enable_adapters"): Enable all adapters.
>
> - [[`disable_adapters()`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.disable_adapters "sentence_transformers.SentenceTransformer.disable_adapters"): Disable all adapters.
>
> - [[`get_adapter_state_dict()`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.get_adapter_state_dict "sentence_transformers.SentenceTransformer.get_adapter_state_dict"): Get the adapter state dict with the weights.
>
> - [[`delete_adapter()`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.delete_adapter "sentence_transformers.SentenceTransformer.delete_adapter"): Delete an adapter from the model.
> :::

## Adding a New Adapter[ïƒ?](#adding-a-new-adapter "Link to this heading")

Adding a new adapter to a model is as simple as calling [[`add_adapter()`]](../../../../docs/package_reference/sentence_transformer/SentenceTransformer.html#sentence_transformers.SentenceTransformer.add_adapter "sentence_transformers.SentenceTransformer.add_adapter") with a (subclass of) [[`PeftConfig`]](https://huggingface.co/docs/peft/main/en/package_reference/config#peft.PeftConfig "(in peft vmain)") on an initialized Sentence Transformer model. In the following example, we use a [[`LoraConfig`]](https://huggingface.co/docs/peft/main/en/package_reference/lora#peft.LoraConfig "(in peft vmain)") instance.

    from sentence_transformers import SentenceTransformer

    # 1. Load a model to finetune with 2. (Optional) model card data
    model = SentenceTransformer(
        "all-MiniLM-L6-v2",
        model_card_data=SentenceTransformerModelCardData(
            language="en",
            license="apache-2.0",
            model_name="all-MiniLM-L6-v2 adapter finetuned on GooAQ pairs",
        ),
    )

    # 3. Create a LoRA adapter for the model & add it
    peft_config = LoraConfig(
        task_type=TaskType.FEATURE_EXTRACTION,
        inference_mode=False,
        r=64,
        lora_alpha=128,
        lora_dropout=0.1,
    )
    model.add_adapter(peft_config)

    # Proceed as usual... See https://sbert.net/docs/sentence_transformer/training_overview.html

## Loading a Pretrained Adapter[ïƒ?](#loading-a-pretrained-adapter "Link to this heading")

Weâ€™ve created a small adapter model called [tomaarsen/bert-base-uncased-gooaq-peft](https://huggingface.co/tomaarsen/bert-base-uncased-gooaq-peft) on top of the [bert-base-uncased](https://huggingface.co/bert-base-uncased) base model.

The [`adapter_model.safetensors`] is 9.44MB, only 2.14% of the size of the base modelâ€™s [`model.safetensors`]. To load an adapter model like this one, you can either load this adapter directly:

    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer("tomaarsen/bert-base-uncased-gooaq-peft")
    embeddings = model.encode(["This is an example sentence", "Each sentence is converted"])
    print(embeddings.shape)
    # (2, 768)

Or you can load the base model and load the adapter into it:

    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer("bert-base-uncased")
    model.load_adapter("tomaarsen/bert-base-uncased-gooaq-peft")
    embeddings = model.encode(["This is an example sentence", "Each sentence is converted"])
    print(embeddings.shape)
    # (2, 768)

In most cases, the former is easiest, as it will work regardless of whether the model is an adapter model or not.

## Training Script[ïƒ?](#training-script "Link to this heading")

See the following example file for a full example of how PEFT can be used with Sentence Transformers:

- **[[training_gooaq_lora.py]](https://github.com/huggingface/sentence-transformers/tree/master/examples/sentence_transformer/training/peft/training_gooaq_lora.py)**: This is a simple recipe for finetuning [bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) on the GooAQ question-answer dataset with the excellent MultipleNegativesRankingLoss, but it has been adapted to use a [LoRA adapter](https://huggingface.co/docs/peft/en/package_reference/lora) from PEFT.

This script was used to train [tomaarsen/bert-base-uncased-gooaq-peft](https://huggingface.co/tomaarsen/bert-base-uncased-gooaq-peft), which reached 0.4705 NDCG@10 on the NanoBEIR benchmark; only marginally behind [tomaarsen/bert-base-uncased-gooaq](https://huggingface.co/tomaarsen/bert-base-uncased-gooaq) which scores 0.4728 NDCG@10 with a modified script that uses full model finetuning.