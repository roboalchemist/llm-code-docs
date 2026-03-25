# Source: https://docs.dify.ai/en/use-dify/knowledge/knowledge-pipeline/create-knowledge-pipeline.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Step 1: Create Knowledge Pipeline

<img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/create-knowledge-pipeline-1.png?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=e9e17095e32579d4058931342a3bdda4" alt="Create Knowledge Pipeline" width="1321" height="256" data-path="images/knowledge-base/create-knowledge-pipeline-1.png" />

Navigate to Knowledge at the top, then click Create from Knowledge Pipeline on the left. There're three ways for you to get started.

### Build from Scratch

<img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/create-knowledge-pipeline-2.png?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=485bf88f9cadf10851a1afd1483eebcc" alt="Build from Scratch" width="1280" height="328" data-path="images/knowledge-base/create-knowledge-pipeline-2.png" />

Click Blank Knowledge Pipeline to build a custom pipeline from scratch. Choose this option when you need custom processing strategies based on specific data source and business requirements.

### Templates

Dify offers two types of templates: **Built-in Pipeline** and **Customized**. Both template cards display name of knowledge base, description, and tags (including chunk structure).

<img src="https://mintcdn.com/dify-6c0370d8/6mOfaeljpmK9sOmc/images/knowledge-base/create-knowledge-pipeline-4-1.png?fit=max&auto=format&n=6mOfaeljpmK9sOmc&q=85&s=eb94d19335b57c9fafc8e78bedeba375" alt="" width="3840" height="1176" data-path="images/knowledge-base/create-knowledge-pipeline-4-1.png" />

#### Built-in Pipeline

Built-in pipelines are official knowledge base templates pre-configured by Dify. These templates are optimized for common document structures and use cases. Simply click **Choose** to get started.

<img src="https://mintcdn.com/dify-6c0370d8/6mOfaeljpmK9sOmc/images/knowledge-base/create-knowledge-pipeline-4.png?fit=max&auto=format&n=6mOfaeljpmK9sOmc&q=85&s=3ececc86f5f2f5ef0a01e1e2e6c28863" alt="Built-in Templates" width="1280" height="350" data-path="images/knowledge-base/create-knowledge-pipeline-4.png" />

**Types**

| Name                | Chunk Structure   | Index Method | Retrieval Setting              | Description                                                                                                                                                                                                                  |
| ------------------- | ----------------- | ------------ | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General Mode-ECO    | General           | Economical   | Inverted Index                 | Divide document content into smaller paragraphs, directly used for matching user queries and retrieval.                                                                                                                      |
| Parent-child-HQ     | Parent-Child      | High Quality | Hybrid Search                  | Adopt advanced chunking strategy, dividing document text into larger parent chunks and smaller child chunks. The parent chunks contain child chunks which ensure both retrieval precision and maintain contextual integrity. |
| Simple Q\&A         | Question & Answer | High Quality | Vector Search                  | Convert tabular data into question-answer format, using question matching to quickly hit corresponding answer information.                                                                                                   |
| LLM Generated Q\&A  | Question & Answer | High Quality | Vector Search                  | Generate structured question-answer pairs with large language models based on original text paragraphs. Find relevant answer by using question matching mechanism.                                                           |
| Convert to Markdown | Parent-child      | High Quality | Hybrid Search - Weighted Score | Designed for Office native file formats such as DOCX, XLSX, and PPTX, converting them to Markdown format for better information processing. ⚠️ Note: PDF files are not recommended.                                          |

To preview the selected built-in pipeline, click **Details** on any template card. Then, check information in the popup window, including: orchestration structure, pipeline description, and chunk structure. Click **Use this Knowledge Pipeline** for orchestration.

<img src="https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/create-knowledge-pipeline-5.png?fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=bd1c5e6cefc8b737f59ebc132f01f5be" alt="Template Details" width="1280" height="638" data-path="images/knowledge-base/create-knowledge-pipeline-5.png" />

#### Customized

<img src="https://mintcdn.com/dify-6c0370d8/6mOfaeljpmK9sOmc/images/knowledge-base/create-knowledge-pipeline-6.png?fit=max&auto=format&n=6mOfaeljpmK9sOmc&q=85&s=82420481a0555bb0bdc422a2658ced88" alt="Customized Templates" width="1280" height="511" data-path="images/knowledge-base/create-knowledge-pipeline-6.png" />

Customized templates are user-created and published knowledge pipeline. You can choose a template to start, export the DSL, or view detailed information for any template.

<img src="https://mintcdn.com/dify-6c0370d8/y0OuaOVt1Ats0jeT/images/knowledge-base/create-knowledge-pipeline-7.png?fit=max&auto=format&n=y0OuaOVt1Ats0jeT&q=85&s=5ef6626a2693c1f38a04410b3b361f72" alt="Template Actions" width="741" height="556" data-path="images/knowledge-base/create-knowledge-pipeline-7.png" />

To create a knowledge base from a template, click **Choose** on the template card. You can also create knowledge base by clicking **Use this Knowledge Pipeline** when previewing a template. Click **More** to edit pipeline information, export pipeline, or delete the template.

### Import Pipeline

<img src="https://mintcdn.com/dify-6c0370d8/6mOfaeljpmK9sOmc/images/knowledge-base/create-knowledge-pipeline-3.png?fit=max&auto=format&n=6mOfaeljpmK9sOmc&q=85&s=cdd763e18df70b0663cfbbe138e68126" alt="Import DSL" width="1280" height="693" data-path="images/knowledge-base/create-knowledge-pipeline-3.png" />

Import a pipeline of a previously exported knowledge pipeline to quickly reuse existing configurations and modify them for different scenarios or requirements. Navigate to the bottom left of the page and click **Import from a DSL File**. Dify DSL is a YAML-based standard that defines AI application configurations, including model parameters, prompt design, and workflow orchestration. Similar to workflow DSL, knowledge pipeline uses the same YAML format standard to define processing workflows and configurations within a knowledge base.

What's in a knowledge pipeline DSL:

| Name                    | Description                                                        |
| ----------------------- | ------------------------------------------------------------------ |
| Data Sources            | Local files, websites, online documents, online drive, web crawler |
| Data Processing         | Document extraction, content chunking, cleaning strategies         |
| Knowledge Configuration | Indexing methods, retrieval settings, storage parameters           |
| Node Orchestration      | Arrangement and sequence                                           |
| User Input Form         | Custom parameter fields (if configured)                            |


Built with [Mintlify](https://mintlify.com).