# Source: https://docs.bito.ai/help/bitos-ai-stack/llm-tokens.md

# LLM tokens

At the heart of every LLM, from GPT-3.5 Turbo to the latest GPT-4o, are tokens. These are not your arcade game coins but the fundamental units of language that these models understand and process. Imagine tokens as the DNA of digital language—their sequence dictates how an LLM interprets and responds to text.&#x20;

A token is created when we break down a massive text corpus into digestible bits. Think of it like slicing a cake into pieces; each slice, or token, can vary from a single word to a punctuation mark or even a part of a word. The process of creating tokens, known as **tokenization**, simplifies complex input text, making it manageable for LLMs to analyze.&#x20;

**Here’s a quick reference to understand token equivalents:**&#x20;

* 1 token ≈ 4 characters in English&#x20;
* 1 token ≈ ¾ of a word&#x20;
* 100 tokens ≈ 75 words or about 1–2 sentences&#x20;

## Tokenization Methods&#x20;

Imagine you have a sentence: **"The quick brown fox jumps over the lazy dog."** An LLM would use tokenization to chop this sentence into manageable pieces. Depending on the chosen method (we’ve discussed it in the next section below), this could result in a variety of tokens, such as:&#x20;

* **Word-level:** \["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]&#x20;
* **Subword-level:** \["The", "quick", "brown", "fox", "jumps", "over", "the", "la", "zy", "dog"]&#x20;
* **Character-level:** \["T", "h", "e", " ", "q", "u", "i", "c", "k", " ", ...]&#x20;

Each method has its own advantages and disadvantages.&#x20;

**Word-level tokenization** is straightforward and aligns with the way humans naturally read and write text. It is effective for languages with clear word boundaries and for tasks where the meaning is heavily dependent on the use of specific words. However, this method can lead to very large vocabularies, especially in languages with rich morphology or in cases where the text contains a lot of different proper nouns or technical terms. This large vocabulary can become a problem when trying to manage memory and computational efficiency.&#x20;

**Subword-level tokenization**, often implemented through methods like Byte Pair Encoding (BPE) or SentencePiece, addresses some of the issues of word-level tokenization. By breaking down words into more frequently occurring subunits, this method allows the model to handle rare or out-of-vocabulary (OOV) words more gracefully. It balances the vocabulary size and the ability to represent the full range of text seen during training. It can also be more effective for agglutinative languages (like Turkish or Finnish), where you can combine many suffixes with a base word, leading to an explosion of possible word forms if using word-level tokenization.&#x20;

**Character-level tokenization** has the advantage of the smallest possible vocabulary. Since it deals with characters, it is very robust to misspellings and OOV words. However, because it operates at such a fine-grained level, it may require more complex models to understand higher-level abstractions in the text. Models may need to be larger or more complex to learn the same concepts that could be learned with fewer parameters at higher levels of tokenization.&#x20;

Beyond these, there are other tokenization methods such as:&#x20;

* **Byte-level:** Similar to character-level, but treats the text as a sequence of bytes, which can be useful for handling multilingual text uniformly.&#x20;
* **Morpheme-level:** Breaks words down into morphemes, which are the smallest meaningful units of language. This can be useful for capturing linguistic nuances but requires sophisticated algorithms to implement effectively.&#x20;
* **Hybrid approaches:** Some models use a combination of the above methods, often starting with a larger unit and then falling back to smaller units when the first approach does not work.&#x20;

The choice of tokenization can affect not just the performance of an LLM but also its understanding of the text. For example, using a subword tokenizer that never breaks down "dog" into smaller pieces ensures that the model always considers "dog" as a semantic unit. In contrast, if "dog" could be broken down into "d" and "og", the model might lose the understanding that "dog" represents an animal.&#x20;

## Tokens and Model Costs&#x20;

The complexity and number of tokens directly impact the computational horsepower needed to run AI models. More tokens generally mean more memory and processing power, which translates to higher costs.&#x20;

When you use services like OpenAI's GPT models, you're charged based on the number of tokens processed. With different rates for different models (like Davinci or Ada), budgeting for AI usage can get tricky. This makes the choice of tokenization method not just a technical decision but also a financial one.&#x20;

## Overcoming the Token Limit Challenge&#x20;

A crucial point about LLMs is that they can only handle a limited number of tokens at once—this is their **token limit**. The more tokens they can process, the more complex the tasks they can handle.&#x20;

Imagine asking an AI to write a novel in one go. If the token limit is low, it might only manage a chapter. If it's high, you could get a full book, but it might take ages to write. It's all about finding the balance between performance and practicality.&#x20;

**Here’s the token limits chart of popular LLMs.**&#x20;

| Model Name             | Context Window | Max Output Tokens |
| ---------------------- | -------------- | ----------------- |
| GPT-3.5 Turbo          | 16,385 tokens  | 4,096 tokens      |
| GPT-3.5 Turbo Instruct | 4,096 tokens   | 4,096 tokens      |
| GPT-4                  | 8,192 tokens   | 8,192 tokens      |
| GPT-4o                 | 128,000 tokens | 4,096 tokens      |
| GPT-4o mini            | 128,000 tokens | 16,384 tokens     |
| Claude Sonnet 3.5      | 200,000 tokens | 8192 tokens       |

&#x20;But what happens when you have more to say than the token limit allows?&#x20;

## 5 Strategies to Beat Token Limits&#x20;

1. **Truncation:** The most straightforward approach is to cut the text down until it fits the token budget. However, this is like trimming a picture; you lose some of the scenes.
2. **Chunk Processing:** Break your text into smaller pieces, process each chunk separately, and stitch the results together. It's like watching a series of short clips instead of a full movie.
3. **Summarization:** Distill your text to its essence. For example, "It's sunny today. What will the weather be like tomorrow?" can be shortened to "Tell me tomorrow's weather."
4. **Remove Redundant Terms:** Cut out the fluff—words that don't add significant meaning (like "the" or "and"). This streamlines the text but beware, over-pruning can alter the message.
5. **Fine-Tuning Language Models:** Custom-train your model on specific data to get better results with fewer tokens. It’s like prepping a chef to make a dish they can cook blindfolded.&#x20;

## Conclusion&#x20;

Tokens are much more than jargon—they're central to how language models process and understand our queries and commands. &#x20;

Understanding tokens and their role in AI language processing is fundamental for anyone looking to leverage the power of LLMs in their work or business. By grasping the basics of tokenization and its impact on computational requirements and costs, users can make informed decisions to balance performance with budget.&#x20;
