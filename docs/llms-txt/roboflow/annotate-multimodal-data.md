# Source: https://docs.roboflow.com/roboflow/roboflow-ko/annotate/annotate-multimodal-data.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/anotto/annotate-multimodal-data.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/annotate/annotate-multimodal-data.md

# Source: https://docs.roboflow.com/annotate/annotate-multimodal-data.md

# Annotate Multimodal Data

If you are labeling a dataset that is part of a Multimodal project, prefixes are used to annotate your images.

A prefix can either be:

* An identifier like `<PREFIX>`, that is used to prompt a [VLM](https://blog.roboflow.com/what-is-a-vision-language-model/) like Florence-2, or;
* A question like "What is in this image?", ideal for use with general VQA models like GPT-4o.

For Florence-2 fine-tuning, for example, the prefix chosen will correspond to the prefix prompt you give to the model. For Florence-2, prefixes should be in the format `<PREFIX>`, like `<TOTAL>`.

For GPT-4o, your prefix may be: "What is the total in this receipt?".

You may want to add different prefixes different features in an object that we want to identify, like total, subtotal, and tax.

### Add Prefixes

To add prefixes, click "Classes & Tags" in the Roboflow sidebar, then click the "Add " button:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-cc730da50a4c28b361532f12fc857c1b2bd6aea9%2FScreenshot%202025-05-19%20at%2012.49.55.png?alt=media" alt=""><figcaption></figcaption></figure>

Then, enter the prefix. This may be a question like "What is in the image?" or a unique ID like "\<RECEIPT>", depending on the model you want to train.

You can add multiple prefixes with the "+" button.

Click “Add Prefixes” to add your prefixes.

Once you have set prefixes, they will be available as questions in your annotation editor:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-4ab4d4da6d88a403f522f08aacb7007c26dc2c2d%2FScreenshot-2024-11-27-at-09.07.07.png?alt=media" alt=""><figcaption></figcaption></figure>
