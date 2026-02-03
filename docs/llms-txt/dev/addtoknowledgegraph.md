# Source: https://dev.writer.com/blueprints/addtoknowledgegraph.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add to Knowledge Graph

Adds structured information to the knowledge graph. Use for storing facts AI can reference.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-knowledge-graph-block.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=cb8e3d7d668e0748a96e90d710cdd44c" alt="" data-og-width="2310" width="2310" data-og-height="1490" height="1490" data-path="images/agent-builder/blueprints/add-to-knowledge-graph-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-knowledge-graph-block.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=14b994531c702b60d3fb3f0b06de9ddd 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-knowledge-graph-block.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=de3f72fa92d1d3605feb19e08c8f722d 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-knowledge-graph-block.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=8538a7d3b6972fb75c456f1d23a55bf7 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-knowledge-graph-block.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=a28c7e32a15f1397d45904ff910586f2 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-knowledge-graph-block.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=335cea5e76e123beaa30110cfbaeb42b 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-knowledge-graph-block.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=8792d7721886fb459ad988bdd02ea0c3 2500w" />

## Overview

The **Add to Knowledge Graph** block ingests files into a Writer Knowledge Graph, making the information available for AI-powered search, retrieval, and question answering. You can use this block to build enterprise AI applications that need to reference company documents, policies, or structured data.

<Tip>
  The Add to Knowledge Graph block only works for Knowledge Graphs that support file uploads. You can't add files to Knowledge Graphs that support data connectors, like Google Drive or Notion, or URLs.
</Tip>

**Supported file types:** You can upload `PDF`, `TXT`, `DOC/DOCX`, `PPT/PPTX`, `EML`, `HTML`, `SRT`, `CSV`, or `XLS/XLSX` files to a Knowledge Graph.

## How it works

1. **File selection**: Choose the files to ingest into the Knowledge Graph.
2. **Graph specification**: Select the target Knowledge Graph for ingestion.
3. **Processing**: The block processes and indexes the file content.
4. **Integration**: Files become available for AI-powered queries and retrieval.

The block handles the complete process of uploading files to Writer and adding them to the Knowledge Graph, including file validation, content extraction, and indexing. You don't need to upload the files separately or provide file IDs. Once processed, the information becomes searchable through Knowledge Graph queries.

## Examples

### Ingest company policies

The following example shows how to add documents to a Knowledge Graph. In this example, the user uploads one or more documents via the [**File Input** interface block](/components/fileinput), which sets the `@{files}` state variable to the user's uploaded files.

**Blueprint flow:**

1. **UI Trigger** → User initiates document ingestion with a button click. The **File Input** interface block set the `@{files}` state variable to the user's uploaded file.
2. **Add to Knowledge Graph** → Ingest and add the files from the `@{files}` state variable to the Knowledge Graph.
3. **Set state** → Store whether the files were successfully ingested so the UI can display feedback to the user.

**Add to Knowledge Graph block configuration:**

* **Graph Id:** `Support KB`
* **Files:** `@{files}`

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-knowledge-graph-example.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=25af8b3438a193bbde15733f46f3226e" alt="" data-og-width="2360" width="2360" data-og-height="1122" height="1122" data-path="images/agent-builder/blueprints/add-to-knowledge-graph-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-knowledge-graph-example.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=ec97fad6c1c57a6809fe0e02c3cd0e43 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-knowledge-graph-example.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=9e111608fec4c6b892f53cdf76d90110 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-knowledge-graph-example.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=f24ca6181953d9e16a971b0d856d6239 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-knowledge-graph-example.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=359bbc40df218e8ed5cc90ec7b8ce75f 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-knowledge-graph-example.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=87c22efdb2bfeccfd1e29a83dfcd4b3a 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-to-knowledge-graph-example.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=32461a2da21dae648f9066cb1d4ef724 2500w" />

## Fields

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Type</th>
    <th>Control</th>
    <th>Default</th>
    <th>Description</th>
    <th>Options</th>
    <th>Validation</th>
  </thead>

  <tbody>
    <tr>
      <td>Graph Id</td>
      <td>Graph Id</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>The id for an existing knowledge graph. It has a UUID format.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        Format: uuid
      </td>
    </tr>

    <tr>
      <td>Files</td>
      <td>Object</td>
      <td>-</td>

      <td>
        <code>\[]</code>
      </td>

      <td>A list of files to be uploaded and added to the knowledge graph. You can use files uploaded via the File input component or specify dictionaries with data, type and name.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>URLs</td>
      <td>Object</td>
      <td>-</td>

      <td>
        <code>\[]</code>
      </td>

      <td>A list of URLs to be added to the knowledge graph. Web content from these URLs will be indexed.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>

## End states

Below are the possible end states of the block call.

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </thead>

  <tbody>
    <tr>
      <td>Success</td>
      <td>-</td>
      <td>success</td>
      <td>Content was added to the knowledge graph.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>There was an error adding content to the knowledge graph.</td>
    </tr>
  </tbody>
</table>

The **Add to Knowledge Graph** block does not return any output.
