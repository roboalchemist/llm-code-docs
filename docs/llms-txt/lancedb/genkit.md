# Source: https://docs.lancedb.com/integrations/ai/genkit.md

# GenKit

export const TsFrameworksGenkitUsage = "import { lancedbIndexerRef, lancedb, lancedbRetrieverRef, WriteMode } from \"genkitx-lancedb\";\nimport { textEmbedding004, vertexAI } from \"@genkit-ai/vertexai\";\nimport { gemini } from \"@genkit-ai/vertexai\";\nimport { z, genkit } from \"genkit\";\nimport { Document } from \"genkit/retriever\";\nimport { chunk } from \"llm-chunk\";\nimport { readFile } from \"fs/promises\";\nimport path from \"path\";\nimport pdf from \"pdf-parse/lib/pdf-parse\";\n\nconst ai = genkit({\n  plugins: [\n    // vertexAI provides the textEmbedding004 embedder\n    vertexAI(),\n\n    // the local vector store requires an embedder to translate from text to vector\n    lancedb([\n      {\n        dbUri: \".db\", // optional lancedb uri, default to .db\n        tableName: \"table\", // optional table name, default to table\n        embedder: textEmbedding004,\n      },\n    ]),\n  ],\n});\n";

export const TsFrameworksGenkitCustomRetriever = "export const menuRetriever = lancedbRetrieverRef({\n  tableName: \"table\", // Use the same table name as the indexer.\n  displayName: \"Menu\", // Use a custom display name.\n});\n\nexport const menuQAFlow = ai.defineFlow(\n  { name: \"Menu\", inputSchema: z.string(), outputSchema: z.string() },\n  async (input: string) => {\n    // retrieve relevant documents\n    const docs = await ai.retrieve({\n      retriever: menuRetriever,\n      query: input,\n      options: {\n        k: 3,\n      },\n    });\n\n    const extractedContent = docs.map((doc) => {\n      if (doc.content && Array.isArray(doc.content) && doc.content.length > 0) {\n        if (doc.content[0].media && doc.content[0].media.url) {\n          return doc.content[0].media.url;\n        }\n      }\n      return \"No content found\";\n    });\n\n    console.log(\"Extracted content:\", extractedContent);\n\n    const { text } = await ai.generate({\n      model: gemini(\"gemini-2.0-flash\"),\n      prompt: `\nYou are acting as a helpful AI assistant that can answer \nquestions about the food available on the menu at Genkit Grub Pub.\n\nUse only the context provided to answer the question.\nIf you don't know, do not make up an answer.\nDo not add or change items on the menu.\n\nContext:\n${extractedContent.join(\"\\n\\n\")}\n\nQuestion: ${input}`,\n      docs,\n    });\n\n    return text;\n  },\n);\n";

export const TsFrameworksGenkitCustomIndexer = "export const menuPdfIndexer = lancedbIndexerRef({\n  // Using all defaults, for dbUri, tableName, and embedder, etc\n});\n\nconst chunkingConfig = {\n  minLength: 1000,\n  maxLength: 2000,\n  splitter: \"sentence\",\n  overlap: 100,\n  delimiters: \"\",\n} as any;\n\nasync function extractTextFromPdf(filePath: string) {\n  const pdfFile = path.resolve(filePath);\n  const dataBuffer = await readFile(pdfFile);\n  const data = await pdf(dataBuffer);\n  return data.text;\n}\n\nexport const indexMenu = ai.defineFlow(\n  {\n    name: \"indexMenu\",\n    inputSchema: z.string().describe(\"PDF file path\"),\n    outputSchema: z.void(),\n  },\n  async (filePath: string) => {\n    filePath = path.resolve(filePath);\n\n    // Read the pdf.\n    const pdfTxt = await ai.run(\"extract-text\", () => extractTextFromPdf(filePath));\n\n    // Divide the pdf text into segments.\n    const chunks = await ai.run(\"chunk-it\", async () => chunk(pdfTxt, chunkingConfig));\n\n    // Convert chunks of text into documents to store in the index.\n    const documents = chunks.map((text) => {\n      return Document.fromText(text, { filePath });\n    });\n\n    // Add documents to the index.\n    await ai.index({\n      indexer: menuPdfIndexer,\n      documents,\n      options: {\n        writeMode: WriteMode.Overwrite,\n      } as any,\n    });\n  },\n);\n";

### genkitx-lancedb

Genkit is an open-source framework for building end-to-end AI and RAG pipelines with a clean, TypeScript-first
developer experience. The genkitx-lancedb plugin lets you use LanceDB as a high-performance vector store
inside your Genkit flows, so you can index, search, and retrieve data efficiently as part of your AI
applications.

### Installation

```bash  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
pnpm install genkitx-lancedb
```

### Usage

Adding LanceDB plugin to your genkit instance.

<CodeBlock filename="TypeScript" language="TypeScript" icon="square-js">
  {TsFrameworksGenkitUsage}
</CodeBlock>

You can run this app with the following command:

```bash  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
genkit start -- tsx --watch src/index.ts
```

This'll add LanceDB as a retriever and indexer to the genkit instance. You can see it in the GUI view

<img width="1710" alt="Screenshot 2025-05-11 at 7 21 05 PM" src="https://github.com/user-attachments/assets/e752f7f4-785b-4797-a11e-72ab06a531b7" />

**Testing retrieval on a sample table**
Let's see the raw retrieval results

<img width="1710" alt="Screenshot 2025-05-11 at 7 21 05 PM" src="https://github.com/user-attachments/assets/b8d356ed-8421-4790-8fc0-d6af563b9657" />

On running this query, you'll 5 results fetched from the lancedb table, where each result looks something like this:

<img width="1417" alt="Screenshot 2025-05-11 at 7 21 18 PM" src="https://github.com/user-attachments/assets/77429525-36e2-4da6-a694-e58c1cf9eb83" />

## Creating a custom RAG flow

Now that we've seen how you can use LanceDB for in a genkit pipeline, let's refine the flow and create a RAG. A RAG flow will consist of an index and a retreiver with its outputs postprocessed an fed into an LLM for final response

### Creating custom indexer flows

You can also create custom indexer flows, utilizing more options and features provided by LanceDB.

<CodeBlock filename="TypeScript" language="TypeScript" icon="square-js">
  {TsFrameworksGenkitCustomIndexer}
</CodeBlock>

<img width="1316" alt="Screenshot 2025-05-11 at 8 35 56 PM" src="https://github.com/user-attachments/assets/e2a20ce4-d1d0-4fa2-9a84-f2cc26e3a29f" />

In your console, you can see the logs

<img width="511" alt="Screenshot 2025-05-11 at 7 19 14 PM" src="https://github.com/user-attachments/assets/243f26c5-ed38-40b6-b661-002f40f0423a" />

### Creating custom retriever flows

You can also create custom retriever flows, utilizing more options and features provided by LanceDB.

<CodeBlock filename="TypeScript" language="TypeScript" icon="square-js">
  {TsFrameworksGenkitCustomRetriever}
</CodeBlock>

Now using our retrieval flow, we can ask question about the ingsted PDF

<img width="1306" alt="Screenshot 2025-05-11 at 7 18 45 PM" src="https://github.com/user-attachments/assets/86c66b13-7c12-4d5f-9d81-ae36bfb1c346" />


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt