# Source: https://docs.dify.ai/en/use-dify/knowledge/knowledge-pipeline/upload-files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Step 4: Upload Files

After publishing knowledge pipeline, there're two ways to upload files as below:

A: Click **Go to Documents** in the success notification to add or manage documents. After entering Documents page, click **Add File** to upload.

<div style={{display: 'flex', flexWrap: 'wrap', gap: '30px'}}>
  <div style={{flex: 1, minWidth: '200px'}}>
        <img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/create-knowledge-pipeline-14.png?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=26a955606af6f3e9d17a398e91dbf266" alt="Option A-1" width="1093" height="793" data-path="images/knowledge-base/create-knowledge-pipeline-14.png" />
  </div>

  <div style={{flex: 2, minWidth: '300px'}}>
        <img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/create-knowledge-pipeline-15.png?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=5a1a76ba5a62ebbedacd4cd0be0a9332" alt="Option A-2" width="1280" height="545" data-path="images/knowledge-base/create-knowledge-pipeline-15.png" />
  </div>
</div>

B: Click **Go to Add Documents** to add documents.

<div style={{display: 'flex', flexWrap: 'wrap', gap: '30px'}}>
  <div style={{flex: 1, minWidth: '200px'}}>
        <img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/create-knowledge-pipeline-16.png?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=727b47cb0a59eba682d5da911d0ecf46" alt="Option B-1" width="669" height="620" data-path="images/knowledge-base/create-knowledge-pipeline-16.png" />
  </div>

  <div style={{flex: 2, minWidth: '300px'}}>
        <img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/create-knowledge-pipeline-17.png?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=452d99aa7a2e37b849d95b4ceef67f67" alt="Option B-2" width="1280" height="521" data-path="images/knowledge-base/create-knowledge-pipeline-17.png" />
  </div>
</div>

### Upload Process

1. **Select Data Source**\
   Choose from the data source types configured in your pipeline. Dify currently supports 4 types of data sources: File Upload (pdf, docx, etc.), Online Drive (Google Drive, OneDrive, etc.), Online Doc (Notion), and Web Crawler (Jina Reader, Firecrawl).
   Please visit [Dify Marketplace](https://marketplace.dify.ai/) to install additional data sources.

2. **Fill in Processing Parameters and Preview**\
   If you configured user input fields during pipeline orchestration, users will need to fill in the required parameters and variables at this step. After completing the form, click **Preview** to see chunking results. Click **Save & Process** to complete knowledge base creation and start data processing.
   <Warning>
     Important reminder: Chunk structure remains consistent with the pipeline configuration and won't change with user input parameters.
   </Warning>
   <img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/create-knowledge-pipeline-18.png?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=3faf5eb32a3dd69da5b1105eeaf4d89a" alt="Parameter Input" width="1280" height="601" data-path="images/knowledge-base/create-knowledge-pipeline-18.png" />

3. **Process Documents**\
   Track the progress of document processing. After embedding is completed, click **Go to Document**.
   <img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/create-knowledge-pipeline-19.png?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=bfb68cd8a2e812d9d32de2670862fecc" alt="Processing Progress" width="1280" height="468" data-path="images/knowledge-base/create-knowledge-pipeline-19.png" />

4. **Access Documents List**\
   Click **Go to Documents** to view the Documents page, where you can browse all uploaded file, processing status, etc.
   <img src="https://mintcdn.com/dify-6c0370d8/zkT6R8Ak-WmNYVSe/images/knowledge-base/create-knowledge-pipeline-20.png?fit=max&auto=format&n=zkT6R8Ak-WmNYVSe&q=85&s=2c9b7c1f251744f5ba82262e04269a4b" alt="Documents List" width="1280" height="831" data-path="images/knowledge-base/create-knowledge-pipeline-20.png" />


Built with [Mintlify](https://mintlify.com).