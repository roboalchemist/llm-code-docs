# Source: https://docs.bito.ai/help/bitos-ai-stack/embeddings.md

# Embeddings

Bito leverages the power of embeddings to [understand your entire codebase](https://docs.bito.ai/feature-guides/ai-that-understands-your-code). But WTF are these embeddings, and how do they help Bito understand your code?&#x20;

If you are curious to know, this guide is for you!&#x20;

## What is Embedding?

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FsFApPUNBNyvz2x8EtZnM%2Fembeddings.gif?alt=media&#x26;token=a336faca-fa2a-429e-9e0b-8b64a86f681f" alt=""><figcaption></figcaption></figure>

Embeddings, at their essence, are like magic translators. They convert data—whether words, images, or, in Bito's case, code—into vectors in a dense numerical space. These vectors encapsulate meaning or semantics. Basically, these vectors help computers understand and work with data more efficiently.&#x20;

Imagine an embedding as a vector (list) of floating-point numbers. If two vectors are close, they're similar. If they're far apart, they're different. Simple as that!&#x20;

{% hint style="info" %}
**A vector embedding looks something like this:** \[0.02362240, -0.01716885, 0.00493248, ..., 0.01665339]
{% endhint %}

## Why Embeddings?&#x20;

In this section, we'll explore the most common and impactful ways embeddings are used in everyday tech and applications.&#x20;

**Word Similarity & Semantics:** Word embeddings, like Word2Vec, map words to vectors such that semantically similar words are closer in the vector space. This allows algorithms to discern synonyms, antonyms, and more based on their vector representations.&#x20;

**Sentiment Analysis:** By converting text into embeddings, machine learning models can be trained to detect and classify the sentiment of a text, such as determining if a product review is positive or negative.&#x20;

**Recommendation Systems:** Embeddings can represent items (like movies, books, or products) and users. By comparing these embeddings, recommendation systems can suggest items similar to a user's preferences. For example, by converting audio or video data into embeddings, systems can recommend content based on similarity in the embedded space, leading to personalized user recommendations.&#x20;

**Document Clustering & Categorization:** Text documents can be turned into embeddings using models like Doc2Vec. These embeddings can then be used to cluster or categorize documents based on their content.&#x20;

**Translation & Language Models:** Models like BERT and GPT use embeddings to understand the context within sentences. This contextual understanding aids in tasks like translation and text generation.&#x20;

**Image Recognition:** Images can be converted into embeddings using convolutional neural networks (CNNs). These embeddings can then be used to recognize and classify objects within the images.&#x20;

**Anomaly Detection:** By converting data points into embeddings, algorithms can identify outliers or anomalies by measuring the distance between data points in the embedded space.&#x20;

**Chatbots & Virtual Assistants:** Conversational models turn user inputs into embeddings to understand intent and context, enabling more natural and relevant responses.&#x20;

**Search Engines:** Text queries can be converted into embeddings, which are then used to find relevant documents or information in a database by comparing embeddings.

## Let’s look at an example&#x20;

Suppose you have two functions in your codebase:&#x20;

**Function # 1:**&#x20;

```python
def add(x, y):
    return x + y
```

**Function # 2:**&#x20;

```python
def subtract(x, y):
    return x - y
```

Using embeddings, Bito might convert these functions into two vectors. Because these functions perform different operations, their embeddings would be at a certain distance apart. Now, if you had another function that also performed addition but with a slight variation, its embedding would be closer to the `add` function than the `subtract` function.&#x20;

Let's oversimplify and imagine these embeddings visually:&#x20;

**Embedding for Function # 1 (add):**&#x20;

\[0.9, 0.2, 0.1]

**Embedding for Function # 2 (subtract):**&#x20;

\[0.2, 0.9, 0.1]

Notice the numbers? The first positions in these lists are quite different: **0.9** for addition and **0.2** for subtraction. This difference signifies the varied operations these functions perform.&#x20;

Now, let's add a twist. Suppose you wrote another addition function, but with an extra print statement:

**Function # 3:**&#x20;

```python
def add_and_print(x, y):
    result = x + y
    print(result)
    return result
```

**Bito might give an embedding like:**&#x20;

\[0.85, 0.3, 0.15]

If you compare, this new list is more similar to the `add` function's list than the `subtract` one, especially in the first position. But it's not exactly the same as the pure `add` function because of the added print operation.&#x20;

This distance or difference between lists is what Bito uses to determine how similar functions or chunks of code are to one another. So, when you ask Bito about a piece of code, it quickly checks these number lists, finds the closest match, and guides you accordingly!&#x20;

## How Bito Uses Embeddings&#x20;

When you ask Bito a question or seek assistance with a certain piece of code, Bito doesn't read the code the way we do. Instead, it refers to these vector representations (embeddings). By doing so, it can quickly find related pieces of code in your repository or understand the essence of your query.&#x20;

For example, if you ask Bito, "Where did I implement addition logic?", Bito will convert your question into an embedding and then look for the most related (or closest) embeddings in its index. Since it already knows the `add` function's embedding represents addition, it can swiftly point you to that function.

## Models for Generating Embeddings&#x20;

When we talk about turning data into these nifty lists of numbers (embeddings), several models and techniques come into play. These models have been designed to extract meaningful patterns from vast amounts of data and represent them as compact vectors. Here are some of the standout models:&#x20;

**Word2Vec:** One of the pioneers in the world of embeddings, this model, developed by researchers at Google, primarily focuses on words. Given a large amount of text, Word2Vec can produce a vector for each word, capturing its context and meaning.&#x20;

**Doc2Vec:** An extension of Word2Vec, this model is designed to represent entire documents or paragraphs as vectors, making it suitable for larger chunks of text.&#x20;

**GloVe (Global Vectors for Word Representation):** Developed by Stanford, GloVe is another method to generate word embeddings. It stands out because it combines both global statistical information and local semantic details from a text.&#x20;

**BERT (Bidirectional Encoder Representations from Transformers):** A more recent and advanced model from Google, BERT captures context from both left and right (hence, bidirectional) of a word in all layers. This deep understanding allows for more accurate embeddings, especially in complex linguistic scenarios.&#x20;

**FastText:** Developed by Facebook’s AI Research lab, FastText enhances Word2Vec by considering sub-words. This means it can generate embeddings even for misspelled words or words not seen during training by breaking them into smaller chunks.&#x20;

**ELMo (Embeddings from Language Models):** This model dynamically generates embeddings based on the context in which words appear, allowing for richer representations.&#x20;

**Universal Sentence Encoder:** This model, developed by Google, is designed to embed entire sentences, making it especially useful for tasks that deal with larger text chunks or require understanding the nuances of entire sentences.&#x20;

**GPT (Generative Pre-trained Transformer):** Developed by OpenAI, GPT is a series of models (from GPT-1 to GPT-4o) that use the Transformer architecture to generate text. While GPT models are famous for generating text, they can also produce vector embeddings. Their latest embeddings model is **text-embedding-ada-002** which can generate embeddings for text search, code search, sentence similarity, and text classification tasks.&#x20;

{% hint style="info" %}
Bito uses **text-embedding-ada-002** from **OpenAI** and we’re also trying out some open-source embedding models for our [AI that Understands Your Code](https://docs.bito.ai/feature-guides/ai-that-understands-your-code) feature.
{% endhint %}

These models, among many others, power a wide range of applications, from natural language processing tasks like sentiment analysis and machine translation to aiding assistants like Bito in understanding and processing code or any other form of data.

## Embeddings: More Than Just Numbers&#x20;

While embeddings might seem like just another technical term or a mere list of numbers, they are crucial bridges that connect human logic and machine understanding. The ability to convert complex data, be it code, images, or even human language, into such vectors, and then use the 'distance' between these vectors to find relatedness, is nothing short of magic.&#x20;

In the context of Bito, embeddings aren't just a feature—it's the core that powers its deep understanding of your code, making it an indispensable tool for developers. So, the next time you think of Bito's answers as magical, remember, it's the power of embeddings at work!&#x20;
