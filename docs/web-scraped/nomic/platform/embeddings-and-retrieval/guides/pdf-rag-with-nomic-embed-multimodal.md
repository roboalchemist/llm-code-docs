# Nomic Documentation

Source: https://docs.nomic.ai/platform/embeddings-and-retrieval/guides/pdf-rag-with-nomic-embed-multimodal

Nomic Embed Multimodal is an embedding model that processes both text and images. It can directly process the visual content in PDFs without requiring preprocessing steps like OCR or image captioning.

In this guide, we'll demonstrate how to build multimodal RAG that can answer questions from PDFs containing both text and visual elements.

## Installation​

First, let's install the required dependencies, including poppler for PDF to image conversion:

```
poppler
```

- Linux
- macOS
- Windows
```
sudo apt-get install --quiet -y poppler-utils
```

```
brew install poppler
```

Read the docs here

- pip
- uv
```
pip install -q colpali-engine transformers qwen-vl-utils accelerate flash-attn matplotlib numpy pillow scikit-learn torch pdf2image requests
```

```
uv pip install -q colpali-engine transformers qwen-vl-utils accelerate flash-attn matplotlib numpy pillow scikit-learn torch pdf2image requests
```

## Loading and Previewing the PDFs​

We'll use a collection of arxiv papers as our example dataset:

```
import requestsPDFs = [    {'title': "Attention Is All You Need", 'file': "https://arxiv.org/pdf/1706.03762"},    {'title': "Deep Residual Learning", 'file': "https://arxiv.org/pdf/1512.03385"},    {'title': "BERT", 'file': "https://arxiv.org/pdf/1810.04805"},    {'title': "GPT-3", 'file': "https://arxiv.org/pdf/2005.14165"},    {'title': "Adam Optimizer", 'file': "https://arxiv.org/pdf/1412.6980"},    {'title': "GANs", 'file': "https://arxiv.org/pdf/1406.2661"},    {'title': "U-Net", 'file': "https://arxiv.org/pdf/1505.04597"},    {'title': "DALL-E 2", 'file': "https://arxiv.org/pdf/2204.06125"},    {'title': "Stable Diffusion", 'file': "https://arxiv.org/pdf/2112.10752"}]for pdf in PDFs:    with open(f"{pdf['title']}.pdf", 'wb') as f:        f.write(requests.get(pdf['file']).content)
```

Let's create a helper function to display PDF pages:

```
import matplotlib.pyplot as pltfrom pdf2image import convert_from_pathdef display_pdf_images(images_list):    """Display all images in the provided list as subplots with 5 images per row."""    num_images = len(images_list)    num_rows = num_images // 5 + (1 if num_images % 5 > 0 else 0)    fig, axes = plt.subplots(num_rows, 5, figsize=(20, 4 * num_rows))    axes = axes.flatten()    for i, img in enumerate(images_list):        if i < len(axes):            ax = axes[i]            ax.imshow(img)            ax.set_title(f"Page {i+1}")            ax.axis('off')    for j in range(num_images, len(axes)):        axes[j].axis('off')    plt.tight_layout()    plt.show()for pdf in PDFs:    pdf["images"] = convert_from_path(f"{pdf['title']}.pdf")display_pdf_images(PDFs[0]["images"][:10])
```

## Embedding the PDFs​

We'll use Nomic Embed Multimodal to create embeddings for each page of our PDFs:

```
from colpali_engine.models import BiQwen2_5, BiQwen2_5_Processorimport torchnomic_model = BiQwen2_5.from_pretrained(    "nomic-ai/nomic-embed-multimodal-3b",    torch_dtype=torch.bfloat16,    device_map="cuda",    attn_implementation="flash_attention_2" # remove if no compatible GPU available).eval()nomic_processor = BiQwen2_5_Processor.from_pretrained("nomic-ai/nomic-embed-multimodal-3b")
```

```
image_counter = 0for pdf_idx, pdf in enumerate(PDFs):    print(f"Generating embeddings for {len(pdf['images'])} pages in {pdf['title']}")    pdf['page_embeddings'] = []    batch_size = 4    for i in range(0, len(pdf["images"]), batch_size):        batch_images = pdf["images"][i:i+batch_size]        inputs = nomic_processor.process_images(batch_images)        inputs = {k: v.to(nomic_model.device) for k, v in inputs.items()}        with torch.no_grad():            embeddings = nomic_model(**inputs)        embeddings = embeddings.cpu()        embeddings = embeddings / torch.norm(embeddings, dim=1, keepdim=True)        for j, emb in enumerate(embeddings):            if i+j < len(pdf["images"]):                if 'page_embeddings' not in pdf:                    pdf['page_embeddings'] = []                pdf['page_embeddings'].append(emb)                image_counter += 1print(f"Generated embeddings for {image_counter} PDF pages")
```

```
Generating embeddings for 15 pages in Attention Is All You NeedGenerating embeddings for 12 pages in Deep Residual LearningGenerating embeddings for 16 pages in BERTGenerating embeddings for 75 pages in GPT-3Generating embeddings for 15 pages in Adam OptimizerGenerating embeddings for 9 pages in GANsGenerating embeddings for 8 pages in U-NetGenerating embeddings for 27 pages in DALL-E 2Generating embeddings for 45 pages in Stable DiffusionGenerated embeddings for 222 PDF pages
```

## Setting Up Retrieval​

Let's set up our retrieval function that uses Nomic Embed Multimodal embeddings to find relevant PDF pages:

```
import numpy as npfrom sklearn.metrics.pairwise import cosine_similarityembeddings = np.stack([    embedding.float().numpy()    for pdf in PDFs for embedding in pdf["page_embeddings"]])data = []page_count = 0for pdf in PDFs:    for page_idx in range(len(pdf["images"])):        data.append({            "title": pdf["title"],            "file": pdf["file"],            "page_number": page_idx + 1,            "image": pdf["images"][page_idx],            "id": page_count        })        page_count += 1def retrieve(query: str, k: int = 3) -> list:    """Retrieve semantically similar items from data based on embeddings"""    query = nomic_processor.process_queries([query])    with torch.no_grad():        query = {k: v.to(nomic_model.device) for k, v in query.items()}        query_embedding = nomic_model(**query).float().cpu().numpy()    query_embedding = query_embedding / np.linalg.norm(query_embedding)    cos_sim = cosine_similarity(query_embedding, embeddings)[0]    idx_sorted_by_cosine_sim = np.argsort(cos_sim)[::-1]    sorted_data = [data[i] for i in idx_sorted_by_cosine_sim]    return sorted_data[:k]
```

## Setting Up the VLM​

We'll use Qwen 2.5 VL 7B Instruct as our vision-language model to answer questions about the retrieved PDF pages:

```
from transformers import Qwen2_5_VLForConditionalGeneration, AutoProcessorfrom qwen_vl_utils import process_vision_infofrom PIL.Image import Imagemodel = Qwen2_5_VLForConditionalGeneration.from_pretrained(    "Qwen/Qwen2.5-VL-7B-Instruct",    torch_dtype=torch.bfloat16,    device_map="auto")processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct")def query_vlm(query: str, images: list[Image]) -> str:    """Queries Qwen VLM with text and images"""    system_prompt = "You are an expert professional PDF analyst who gives rigorous in-depth answers."    message_content = [        {"type": "image", "image": image}        for image in images    ] + [{"type": "text", "text": query}]    messages = [        {            "role": "system",            "content": [{"type": "text", "text": system_prompt}]        },        {            "role": "user",            "content": message_content        }    ]    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)    image_inputs, video_inputs = process_vision_info(messages)    inputs = processor(        text=[text],        images=image_inputs,        videos=video_inputs,        padding=True,        return_tensors="pt"    ).to(model.device)    generated_ids = model.generate(**inputs, max_new_tokens=1000)    generated_ids_trimmed = generated_ids[0][len(inputs.input_ids[0]):]    return processor.decode(generated_ids_trimmed, skip_special_tokens=True)
```

## Example Usage​

### Single-Document Retrieval​

Let's try a query retrieving a single page:

```
query = "How does the transformer architecture work?"results = retrieve(query, k=1)image = results[0]["image"]single_doc_answer = query_vlm(query, [image])print(single_doc_answer)
```

```
image
```

```
single_doc_answer
```

The Transformer architecture, as depicted in Figure 1 and described in the text, is a neural network model that uses stacked self-attention mechanisms and point-wise fully connected layers for both the encoder and decoder. Here's a detailed breakdown of how it works:

Encoder:

- Input Embedding: The input sequence is first converted into a sequence of vectors using an embedding layer.
- Positional Encoding: Positional encoding is added to the embedded input to provide information about the relative or absolute position of each token within the sequence. This helps the model understand the order of elements.
- Encoder Stack:

The encoder consists of multiple identical layers (N = 6).
Each layer contains two sub-layers:
Multi-Head Self-Attention: This mechanism allows the model to focus on different parts of the input sequence simultaneously by dividing the attention mechanism into multiple heads. Each head computes its own attention scores independently, and the outputs are concatenated and passed through a linear projection.
Feed-Forward Network: A simple, point-wise fully connected feed-forward network that processes the output of the multi-head self-attention mechanism. It typically consists of two linear transformations with a ReLU activation function in between.
- The encoder consists of multiple identical layers (N = 6).
- Each layer contains two sub-layers:
- Multi-Head Self-Attention: This mechanism allows the model to focus on different parts of the input sequence simultaneously by dividing the attention mechanism into multiple heads. Each head computes its own attention scores independently, and the outputs are concatenated and passed through a linear projection.
- Feed-Forward Network: A simple, point-wise fully connected feed-forward network that processes the output of the multi-head self-attention mechanism. It typically consists of two linear transformations with a ReLU activation function in between.
- Residual Connections and Layer Normalization: To facilitate learning across deep networks, residual connections are used around each sub-layer. This means the output of each sub-layer is added to the input before normalization. Layer normalization is applied after the addition to ensure stable training.
Decoder:

- Output Embedding: The output from the encoder is fed into the decoder, which also starts with an embedding layer.
- Positional Encoding: Similar to the encoder, positional encoding is added to the embedded output.
- Decoder Stack:

The decoder also consists of multiple identical layers (N = 6).
Each layer contains three sub-layers:
Multi-Head Self-Attention: This mechanism is used to attend to the previous output of the decoder itself, allowing the model to generate a response based on previously generated tokens.
Multi-Head Attention over Encoder Output: This mechanism allows the decoder to attend to the entire encoded input sequence, enabling it to incorporate information from the source context.
Feed-Forward Network: A simple, point-wise fully connected feed-forward network similar to the one in the encoder.
- The decoder also consists of multiple identical layers (N = 6).
- Each layer contains three sub-layers:
- Multi-Head Self-Attention: This mechanism is used to attend to the previous output of the decoder itself, allowing the model to generate a response based on previously generated tokens.
- Multi-Head Attention over Encoder Output: This mechanism allows the decoder to attend to the entire encoded input sequence, enabling it to incorporate information from the source context.
- Feed-Forward Network: A simple, point-wise fully connected feed-forward network similar to the one in the encoder.
- Residual Connections and Layer Normalization: Again, residual connections are used around each sub-layer, followed by layer normalization.
Attention Mechanism:

- Self-Attention: In the encoder and decoder, the self-attention mechanism allows each element in the sequence to attend to all other elements. This helps the model capture long-range dependencies in the data.
- Masked Multi-Head Attention: In the decoder, the self-attention mechanism is masked to prevent the decoder from attending to future positions in the sequence. This ensures that the predictions for position (i) can only depend on the known outputs at positions less than (i).
Output:

- After passing through the decoder stack, the final output is processed through a linear layer and a softmax function to produce probabilities over the target vocabulary.
In summary, the Transformer architecture leverages self-attention mechanisms to capture long-range dependencies and point-wise fully connected layers to process the information efficiently. The use of residual connections and layer normalization helps in stable training, even for deep networks.

### Multi-Document Retrieval​

For more complex queries that might require looking at multiple pages:

```
query = "What does the forward pass of a diffusion model look like?"k = 2results = retrieve(query, k=k)images = [x["image"] for x in results]multi_doc_answer = query_vlm(query, images)print(multi_doc_answer)
```

```
images
```

```
multi_doc_answer
```

The forward pass of a diffusion model, as described in the text, involves gradually adding noise to the input data over time steps t from 1 to T. This process is defined by a sequence of parameters:

where

represents the probability distribution at each step t, which is a normal distribution centered around αtx0α_t x_0αt​x0​ with variance σt2σ_t^2σt2​.

The Markov structure ensures that the noise added at each step depends only on the previous state:

where

In summary, the forward pass of a diffusion model starts with an initial clean image x0x_0x0​ and iteratively adds noise to it, with the noise level controlled by the parameters αtα_tαt​ and σtσ_tσt​.

## Run This Guide As A Notebook​

### Google Colab​

You can run this guide as a Google Colab notebook.

### GitHub​

You can download this guide as a Jupyter notebook from our cookbook repo.

- Installation
- Loading and Previewing the PDFs
- Embedding the PDFs
- Setting Up Retrieval
- Setting Up the VLM
- Example UsageSingle-Document RetrievalMulti-Document Retrieval
- Single-Document Retrieval
- Multi-Document Retrieval
- Run This Guide As A NotebookGoogle ColabGitHub
- Google Colab
- GitHub
