# Source: https://docs.bito.ai/help/bitos-ai-stack/indexing.md

# Indexing

Indexing involves breaking down a source code file into smaller chunks and converting these chunks into [**embeddings**](https://docs.bito.ai/help/bitos-ai-stack/embeddings) that can be stored in a [**vector database**](https://docs.bito.ai/help/bitos-ai-stack/vector-databases). Bito indexes your entire codebase locally (on your machine) to understand it and provide answers tailored to your code.&#x20;

{% hint style="info" %}
Learn more about Bito's [**AI that Understands Your Code**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code) feature.
{% endhint %}

## How Bito Indexes Your Code&#x20;

In the steps below, we'll show you how Bito indexes your code, ensuring that each query you have is met with precise and contextually relevant information. From breaking down code into digestible chunks to leveraging advanced AI models for nuanced understanding, Bito transforms the daunting task of code analysis into a seamless and efficient experience.&#x20;

Here's how the magic happens:&#x20;

### Step 1: Chunk Breakdown&#x20;

*Dividing Code into Pieces*&#x20;

Bito starts by breaking down your source code files into smaller sections, known as 'chunks'. It’s like cutting up a long text into paragraphs to make it more manageable. Each chunk represents a piece of your code that can be individually indexed and analyzed.&#x20;

### Step 2: Indexing Each Chunk&#x20;

*Creating a Searchable Reference*&#x20;

After breaking down the file, each chunk is indexed, similar to creating a catalog entry. This step is crucial as it allows for the efficient location of the code segment later on.&#x20;

### Step 3: Generating Embeddings&#x20;

*Translating Code into Numeric Vectors*&#x20;

For every chunk, Bito generates a numeric vector or [**“embedding”**](https://docs.bito.ai/help/bitos-ai-stack/embeddings). This process, which can be done using OpenAI or alternative open-source embedding models, translates the code into a mathematical representation. The idea is to create a form that can be easily compared and matched with other code chunks.&#x20;

### Step 4: Storing the Vectors&#x20;

*Saving the Essential Data*&#x20;

These embeddings are then stored in an index file on your machine. This index file is like a detailed directory, listing the file name, the location of the chunk within the file (start and end), and the embedding vector for each piece of code.&#x20;

### Step 5: Query Embedding&#x20;

*Understanding Your Questions*&#x20;

When you ask a question in Bito's chatbox, the AI checks whether it has some specific keywords like "my code", "my project", etc. If so, Bito generates a numeric vector for your query, mirroring the process used for code chunks.&#x20;

{% hint style="info" %}
The complete list of these keywords is given on our [**Available Keywords**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/available-keywords) page.&#x20;
{% endhint %}

### Step 6: Finding the Nearest Neighbor&#x20;

*Matching Your Query with Code*&#x20;

Using the query's vector, Bito searches the index to find the code chunk with the closest matching embedding. This step identifies the relevant sections of your codebase that can answer your question.&#x20;

### Step 7: Contextualization&#x20;

*Building a Bigger Picture*&#x20;

Identifying chunks is just part of the process. Bito ensures that these chunks make sense in the broader context of your code. If necessary, it expands the search to include complete functions or related code segments, creating a fuller, more accurate context.&#x20;

### Step 8: Leveraging Language Models&#x20;

*Consulting the AI Experts*&#x20;

With the context in hand, Bito consults with language models – either basic (GPT-4o mini and similar models) or advanced (GPT-4o, Claude Sonnet 3.5, and best in class AI models) – to interpret the code within the context and provide an accurate response to your query.&#x20;

### Step 9: Session Privacy&#x20;

*Keeping Your Data Local*&#x20;

All the indexing and querying happens on your local machine. The index files are stored in the user’s home folder, for example on Windows the path will be something like **C:\Users\Furqan\\.bito\localcodesearch** folder. It ensures that your code and session history remain private and secure.&#x20;

### Step 10: Safeguarding Data&#x20;

*Ensuring Confidentiality*&#x20;

Bito is committed to privacy. All LLM accounts it uses are under strict agreements to prevent your data from being used for training, recorded, or logged.&#x20;

### Step 11: Handling Hallucination&#x20;

*Reducing AI Fabrication*&#x20;

Bito is designed to minimize AI 'hallucinations' or fabrications, ensuring the answers you receive are based on your actual code. Although complete elimination of hallucination isn't feasible, as it sometimes aids in constructing beyond seen data, Bito strives to keep it in check, especially when dealing with your local code.&#x20;

With these steps, Bito provides a robust and privacy-conscious method for indexing and understanding your code, simplifying navigation and enhancing productivity in your development projects.&#x20;
