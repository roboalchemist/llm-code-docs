# Source: https://unsloth.ai/docs/fr/notions-de-base/inference-and-deployment/saving-to-ollama.md

# Source: https://unsloth.ai/docs/de/grundlagen/inference-and-deployment/saving-to-ollama.md

# Source: https://unsloth.ai/docs/jp/ji-ben/inference-and-deployment/saving-to-ollama.md

# Source: https://unsloth.ai/docs/zh/ji-chu-zhi-shi/inference-and-deployment/saving-to-ollama.md

# Source: https://unsloth.ai/docs/basics/inference-and-deployment/saving-to-ollama.md

# Saving to Ollama

See our guide below for the complete process on how to save to [Ollama](https://github.com/ollama/ollama):

{% content-ref url="../../get-started/fine-tuning-llms-guide/tutorial-how-to-finetune-llama-3-and-use-in-ollama" %}
[tutorial-how-to-finetune-llama-3-and-use-in-ollama](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/tutorial-how-to-finetune-llama-3-and-use-in-ollama)
{% endcontent-ref %}

### Saving on Google Colab

You can save the finetuned model as a small 100MB file called a LoRA adapter like below. You can instead push to the Hugging Face hub as well if you want to upload your model! Remember to get a Hugging Face token via: <https://huggingface.co/settings/tokens> and add your token!

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-8c577103f7c4fe883cabaf35c8437307c6501686%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

After saving the model, we can again use Unsloth to run the model itself! Use `FastLanguageModel` again to call it for inference!

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-1a1be852ca551240bdce47cf99e6ccd7d31c1326%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### Exporting to Ollama

Finally we can export our finetuned model to Ollama itself! First we have to install Ollama in the Colab notebook:

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-24f9429ed4a8b3a630dc8f68dcf81555da0a80ee%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Then we export the finetuned model we have to llama.cpp's GGUF formats like below:

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-56991ea7e2685bb9905af9baf2f3f685123dcdd8%2Fimage%20(52).png?alt=media" alt=""><figcaption></figcaption></figure>

Reminder to convert `False` to `True` for 1 row, and not change every row to `True`, or else you'll be waiting for a very time! We normally suggest the first row getting set to `True`, so we can export the finetuned model quickly to `Q8_0` format (8 bit quantization). We also allow you to export to a whole list of quantization methods as well, with a popular one being `q4_k_m`.

Head over to <https://github.com/ggerganov/llama.cpp> to learn more about GGUF. We also have some manual instructions of how to export to GGUF if you want here: <https://github.com/unslothai/unsloth/wiki#manually-saving-to-gguf>

You will see a long list of text like below - please wait 5 to 10 minutes!!

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-271b392fdafd0e7d01c525d7a11a97ee5c34b713%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

And finally at the very end, it'll look like below:

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-a554bd388fd0394dd8cdef85fd9d208bfd7feee7%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Then, we have to run Ollama itself in the background. We use `subprocess` because Colab doesn't like asynchronous calls, but normally one just runs `ollama serve` in the terminal / command prompt.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-e431609dfc5c742f0b5ab2388dbbd0d8e15c7670%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### Automatic `Modelfile` creation

The trick Unsloth provides is we automatically create a `Modelfile` which Ollama requires! This is a just a list of settings and includes the chat template which we used for the finetune process! You can also print the `Modelfile` generated like below:

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-6945ba10a2e25cfc198848c0e863001375c32c4c%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

We then ask Ollama to create a model which is Ollama compatible, by using the `Modelfile`

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-d431a64613b39d913d1780c22cde37edc6564272%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### Ollama Inference

And we can now call the model for inference if you want to do call the Ollama server itself which is running on your own local machine / in the free Colab notebook in the background. Remember you can edit the yellow underlined part.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fgit-blob-49b93efa192fdd741f3ac8484cef8c3fd7415283%2FInference.png?alt=media" alt=""><figcaption></figcaption></figure>

### Running in Unsloth works well, but after exporting & running on Ollama, the results are poor

You might sometimes encounter an issue where your model runs and produces good results on Unsloth, but when you use it on another platform like Ollama, the results are poor or you might get gibberish, endless/infinite generations *or* repeated output&#x73;**.**

* The most common cause of this error is using an <mark style="background-color:blue;">**incorrect chat template**</mark>**.** It’s essential to use the SAME chat template that was used when training the model in Unsloth and later when you run it in another framework, such as llama.cpp or Ollama. When inferencing from a saved model, it's crucial to apply the correct template.
* You must use the correct `eos token`. If not, you might get gibberish on longer generations.
* It might also be because your inference engine adds an unnecessary "start of sequence" token (or the lack of thereof on the contrary) so ensure you check both hypotheses!
* <mark style="background-color:green;">**Use our conversational notebooks to force the chat template - this will fix most issues.**</mark>
  * Qwen-3 14B Conversational notebook [**Open in Colab**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(14B\)-Reasoning-Conversational.ipynb)
  * Gemma-3 4B Conversational notebook [**Open in Colab**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma3_\(4B\).ipynb)
  * Llama-3.2 3B Conversational notebook [**Open in Colab**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_\(1B_and_3B\)-Conversational.ipynb)
  * Phi-4 14B Conversational notebook [**Open in Colab**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_4-Conversational.ipynb)
  * Mistral v0.3 7B Conversational notebook [**Open in Colab**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_v0.3_\(7B\)-Conversational.ipynb)
  * **More notebooks in our** [**notebooks docs**](https://unsloth.ai/docs/get-started/unsloth-notebooks)
