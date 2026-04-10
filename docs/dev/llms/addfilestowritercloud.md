# Source: https://dev.writer.com/blueprints/addfilestowritercloud.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add files to Writer Cloud

Uploads files to the Writer platform.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-block.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=46ec31b2b07e69e33047416a967aa5a6" alt="" data-og-width="2310" width="2310" data-og-height="1490" height="1490" data-path="images/agent-builder/blueprints/add-files-to-writer-cloud-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-block.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=8390e7d102ff0e2f4e7c16215c7e2664 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-block.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=1edcb79d677b77c08def9144b6efb4db 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-block.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=bbe59c19922152f7a1939d4f1aef4ab3 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-block.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=2de7e79d53643df3fd6cd0a71f6203a3 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-block.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=eb86c5f63cdb7bdbeda7149e6c084841 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-block.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=b0cc271a9fa1dbd76ae61c725b991d91 2500w" />

## Overview

The **Add files to Writer Cloud** block uploads files to the Writer cloud so you can use them in your workflows. It accepts a list of file objects as inputs.

## File inputs

The **Add files to Writer Cloud** block accepts a list of file objects as inputs. Each file object must have the following fields:

| Field  | Type   | Description                                                                                                    |
| ------ | ------ | -------------------------------------------------------------------------------------------------------------- |
| `name` | string | The name of the file.                                                                                          |
| `data` | bytes  | The content of the file as bytes.                                                                              |
| `type` | string | The [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types/Common_types) of the file. |

### Adding files from the file input block

If you upload a file with the **File input** interface block, the list of file objects is automatically created for you, so all you have to do is pass the list to the **Add files to Writer Cloud** block. See the [example below](#example%3A-upload-files-to-writer-cloud-from-the-file-input-block) for how to do this.

You can retrieve the file objects list from the **File input** interface block in two ways:

* Connect a UI Trigger to the **File input** block's `wf-file-change` event. Then, use the `@{payload}` environment variable to access the file objects. The trigger will fire when a user adds or removes files from the file input block.
* Under **Binding** in the **File input** interface block, define a state variable that contains the list of file objects. Then reference that variable in the **Add files to Writer Cloud** block.

## Output

Once the files are uploaded to the Writer cloud, the **Add files to Writer Cloud** block returns a list containing the uploaded file IDs and other information about the files.

You can access the output of an **Add files to Writer Cloud** block using the `@{result}` variable in the block that follows it in a blueprint.

Each file object has the following fields:

| Field        | Type   | Description                                                             |
| ------------ | ------ | ----------------------------------------------------------------------- |
| `id`         | string | The ID of the file.                                                     |
| `name`       | string | The name of the file.                                                   |
| `status`     | string | The status of the file. Can be `in_progress`, `completed`, or `failed`. |
| `created_at` | string | The date and time the file was created.                                 |
| `graph_ids`  | array  | The IDs of any Knowledge Graphs that the file is associated with.       |

```json  theme={null}
[
    {
        "id": "701118ae",
        "name": "research_paper.pdf",
        "status": "in_progress",
        "created_at": "2025-06-17T16:18:42.672407+00:00",
        "graph_ids": []
    }
]
```

### File processing status

If the uploaded file's status is `in_progress`, the file is being processed and is not ready to be used in a workflow.

Some files are processed quickly, such as PDFs and images, and are ready to be used in a workflow within seconds. Others, such as Word documents, may take a few minutes to process.

There are a few ways you can handle files that are still being processed:

* Split the blueprint into two parts: one that uploads the files when a user adds them to the file input block, and another that uses the files when a user clicks a button in the UI. This way, you can use the files in the workflow as soon as they're uploaded, and wait for the user to click a button to use the files in the second part of the blueprint. See an example in the [Upload, parse, and summarize PDFs](/agent-builder/summarize-pdfs#build-the-blueprints) tutorial.
* Add a Python block that introduces a few seconds of delay before the workflow continues.
* Add a [**Tool calling** block](/agent-builder/tool-calling) that can check the status of the file [using the Writer API](/api-reference/file-api/get-file) and wait for the file to be processed before continuing.

## Example: Upload files to Writer Cloud from the file input block

This example shows how to upload files to Writer Cloud that are stored in a state variable. In this example, the interface contains a file input block that's bound to the state variable `files`. After the UI Trigger fires, the **Add files to Writer Cloud** block uploads the files to Writer Cloud by accessing the `@{files}` state variable.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-example.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=f34f6e8d3f07c6f5678f7ff34ce5e1b5" alt="" data-og-width="2140" width="2140" data-og-height="940" height="940" data-path="images/agent-builder/blueprints/add-files-to-writer-cloud-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-example.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=81140f17c9651a99eb78957a4fc972a6 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-example.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=b337526f958550756a0ea1368a5d5080 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-example.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=e49d37b7f1a7d5539995bc4d5901254a 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-example.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=92c6d139a656b6a51cec27370554058c 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-example.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=168fdd400ee37b30c877485e36fef4ae 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-example.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=62c00920ae7edea87bf6e21a6b6406e3 2500w" />

The `@{files}` state variable looks like this:

```json  theme={null}
[
    {
        "name": "research_paper.pdf",
        "data": "...",
        "type": "application/pdf"
    }
]
```

## Example: Create and upload files from Python processing

This example shows how to manually create file objects in a **Python code** block and then upload them to Writer Cloud. In this scenario, a Python block generates a CSV report from data processing and creates the file object programmatically.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-example-python.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=2cadb6231212ce4fdf5013147b457f28" alt="" data-og-width="2406" width="2406" data-og-height="1202" height="1202" data-path="images/agent-builder/blueprints/add-files-to-writer-cloud-example-python.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-example-python.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=c9785e96df66f8d2e974e86dcacaf602 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-example-python.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=48e173027ac18c5595fa95aa9e1977c5 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-example-python.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=6f850d373f70264b0cbc625df3160545 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-example-python.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=f729631e3475060e58d0cd0668fc5eb0 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-example-python.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=b748df52fca30a3785a952569df2fd5e 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/add-files-to-writer-cloud-example-python.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=c3482aec1fe379de080fb46988cad3da 2500w" />

The **Python code** block contains the following code, which creates a CSV file object and returns it as a list for the **Add files to Writer Cloud** block to access.

```python  theme={null}
import csv
import io

# Sample data processing
data = [
    ["Name", "Score", "Category"],
    ["Product A", 85, "Electronics"],
    ["Product B", 92, "Home & Garden"],
    ["Product C", 78, "Electronics"]
]

# Create CSV content
csv_buffer = io.StringIO()
writer = csv.writer(csv_buffer)
writer.writerows(data)
csv_content = csv_buffer.getvalue()

# Convert to bytes
csv_bytes = csv_content.encode('utf-8')

# Create file object
file_object = {
    "name": "product_analysis.csv",
    "data": csv_bytes,
    "type": "text/csv"
}

# Return the file object as a list (required by Add files to Writer Cloud block)
set_output([file_object])
```

The Python block outputs `[file_object]`, which the **Add files to Writer Cloud** block then accesses using `@{result}` to upload the CSV file.

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
      <td>Files</td>
      <td>Object</td>
      <td>-</td>

      <td>
        <code>\[]</code>
      </td>

      <td>A list of files to be uploaded to the Writer platform. You can use files uploaded via the File input component or specify dictionaries with data, type and name.</td>

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
      <td>File successfully uploaded.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>There was an error uploading the files.</td>
    </tr>
  </tbody>
</table>

Access the output of a **Add files to Writer Cloud** block using the `@{result}` variable in the block that follows it in a blueprint.
