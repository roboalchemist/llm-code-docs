# Source: https://dev.writer.com/agent-builder/summarize-pdfs.md

# Upload, parse, and summarize PDFs

> Build a PDF research paper summarizer with Agent Builder. Upload PDFs, parse content, and generate summaries for specific personas.

This tutorial follows a similar format to the [Agent Builder Quickstart](/agent-builder/quickstart) use case of summarizing text; in this case, it adds the ability to upload and parse PDFs with Agent Builder and summarize the content.

This tutorial use case is a research paper summarizer that summarizes papers for a specific persona.

If you haven't completed the Agent Builder Quickstart, you may want to do that first to familiarize yourself with the mechanics of Agent Builder.

## Build the UI

The UI for the agent contains:

* A file input block
* A select input to choose the persona to summarize the file for
* A button to start the summarization process
* A message block to indicate that the file is in progress
* A text block to display the results

<Steps>
  <Step title="Add a File Input block">
    First, add a File Input block to the canvas. In the block's configuration panel, update the following fields:

    * **Label**: `Research paper PDF`
    * **Allowed file types**: `.pdf`
    * **Allow multiple files**: `no`

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/file-input-block.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=3fe8e96ebc1c942cc5011c2b08e209b4" alt="File Input block" data-og-width="3456" width="3456" data-og-height="1808" height="1808" data-path="images/agent-builder/parse-pdf-tutorial/file-input-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/file-input-block.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=aa9e5390efdaa349008e853f8bf8a923 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/file-input-block.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=6bd10135f818b5894f6a1c745a329897 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/file-input-block.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=e0eb9a190aad3241d0c3718050a34c28 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/file-input-block.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=91cf475a934c0aa1847eaa399f017ec4 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/file-input-block.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=5ecd7f262b7ee58b2eb69737f34f10d5 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/file-input-block.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=c65e36ea1171ee7fac5d277a8c37c944 2500w" />
  </Step>

  <Step title="Add a select input to choose the persona">
    Next, add a **Select input** block to the canvas, which creates a dropdown. In the block's configuration panel, update the following fields:

    * **Label**: `Persona`
    * **Options**: add the personas you want to summarize the file for. This example uses the personas `Sales`, `Marketing`, `Product`, and `Engineering`.
    * **Link variable** under **Binding**: `persona`. You use this variable name in the blueprint when asking the text generation block to generate a summary for the selected persona.

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/persona-dropdown.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=a6a3884b0d73feb8ec3c626946d586d3" alt="Persona dropdown" data-og-width="3456" width="3456" data-og-height="1816" height="1816" data-path="images/agent-builder/parse-pdf-tutorial/persona-dropdown.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/persona-dropdown.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=b58022a5b2c332361dce43bb21fad932 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/persona-dropdown.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=3bfb24dd55e4b38ebe406eadb85ddc62 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/persona-dropdown.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=c22d10afe400b9953d1f5594cc0a0a3e 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/persona-dropdown.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=fe680f0103ea7a42d00f7a20c1dfc4e5 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/persona-dropdown.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=8a5c9783aa5ed50ae4098dbb77690835 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/persona-dropdown.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=d309b5acf352c42f1db5215dc0b5f546 2500w" />
  </Step>

  <Step title="Add a button to start the summarization process">
    Add a **Button** block to the canvas. In the block's configuration panel, update the following fields:

    * **Text**: `Summarize`

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/summarize-button.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=572c59eb855183817afa84eae959e4d8" alt="Start button" data-og-width="3456" width="3456" data-og-height="1798" height="1798" data-path="images/agent-builder/parse-pdf-tutorial/summarize-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/summarize-button.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=17fff27c87424f53d63d33f0363ee8fc 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/summarize-button.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=548581ca48a1d57903326152cb604339 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/summarize-button.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=acf572599ade57b1f3d756ee45d088e7 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/summarize-button.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=402621b479eb4f7813d78961dff7d2b0 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/summarize-button.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=97d7eff091eea6706410776aaf94e106 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/summarize-button.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=a224beacb2e8ce00e395733087c58e0f 2500w" />
  </Step>

  <Step title="Add a message block to indicate that the file is in progress">
    Add a **Message** block to the canvas, which will display a message to the user indicating that the summarization is in progress. In the block's configuration panel, update the following fields:

    * **Message**: `@{status}`. This will display the status message from the agent's state. You use this variable name in the blueprint to update the status message in the UI.

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/status-message.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=1a5e469712a8f15e6f1563ff0df14201" alt="In progress message" data-og-width="3456" width="3456" data-og-height="1806" height="1806" data-path="images/agent-builder/parse-pdf-tutorial/status-message.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/status-message.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=272c082f358fce0b4b65cac4a99a3175 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/status-message.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=9871b96eca824c8fc20035eb6f885d18 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/status-message.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=5e77dffd9814ff5d32ab38d2d4946283 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/status-message.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=ead8b9b0fb090e609e1f620b47d08e62 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/status-message.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=245f5f58f231bda79e2686111d166c65 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/status-message.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=61cacf60e8bbbcd8eb706c5fa708c33f 2500w" />
  </Step>

  <Step title="Add a text block to display the results">
    Finally, add a **Text** block to the canvas, which will display the summary results. In the block's configuration panel, update the following fields:

    * **Text**: `@{summary}`. This will display the summary results from the agent's state. You use this  name in the blueprint to display the summary results in the UI.
    * **Use markdown**: `yes`

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/summary-text-block.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=c0628ca41d9369735591fdbfdace1a71" alt="Results text block" data-og-width="3456" width="3456" data-og-height="1808" height="1808" data-path="images/agent-builder/parse-pdf-tutorial/summary-text-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/summary-text-block.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=15037891cd67b49894a5ef5b24259a48 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/summary-text-block.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=c1030e30743d3d6f734d28fe80bd5788 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/summary-text-block.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=becddd0689b670429d47180703efde99 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/summary-text-block.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=64369fbaf6dd6d2609b43d33e1fb3b6a 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/summary-text-block.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=3706e31751f04b0a1be0efcfbf7256c8 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/summary-text-block.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=9f4759143b70968604ff4c0b500d5393 2500w" />
  </Step>
</Steps>

## Build the blueprints

The agent has two blueprints:

* [One for uploading a file to Writer cloud](#first-blueprint-upload-file-to-writer-cloud) when a user adds a file to the file input block
* [One for parsing the file and summarizing it](#second-blueprint-parse-and-summarize-the-file) when a user clicks the button to start summarizing

The agent's logic is segmented into two blueprints so that the file uploading can complete before the parsing and summarizing begins.

### First blueprint: Upload file to Writer cloud

Before you can work with the content of a PDF file in a blueprint, you need to upload it to the Writer Cloud with the **Add files to Writer Cloud** block. Once you've uploaded the file, you can access it in the blueprint using the uploaded file's ID and perform operations like parsing the PDF and providing that information to a text generation block.

<Steps>
  <Step title="Add a UI trigger for file input">
    Add a **UI trigger** block to the canvas. This triggers the blueprint when a user adds or changes the file in the file input block.

    In the block's configuration panel, update the following fields:

    * **Alias**: `File upload`. This is optional, but helps to identify the trigger in the blueprint.
    * **Component Id**: Select the `File Input` component from the dropdown of UI blocks
    * **Event type**: `wf-file-change`

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/file-input-trigger.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=9d43933e62f7a24a99a6cf6979c2bb2b" alt="File input trigger" data-og-width="3456" width="3456" data-og-height="1810" height="1810" data-path="images/agent-builder/parse-pdf-tutorial/file-input-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/file-input-trigger.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=e85a02538db1fc23732ac9d0093af06c 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/file-input-trigger.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=6f49d1cc3b3d82b1b773942e1fae6da9 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/file-input-trigger.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=ce308fe3d9c309c90841efe9ca9781a3 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/file-input-trigger.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=5f4282e45f5b3a3dd45d8f6b459b23c8 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/file-input-trigger.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=fa101493cec36a4d1c80ded92f79dc74 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/file-input-trigger.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=7cb862b91fafdffdeb14a0efbcd39b77 2500w" />
  </Step>

  <Step title="Add a block to add files to Writer Cloud">
    Add a **Add files to Writer Cloud** block to the canvas. This block uploads the file to Writer Cloud.

    In the block's configuration panel, update the following fields:

    * **Files**: `@{payload}`. This references the payload provided by the preceding UI trigger. The payload contains the file that was uploaded to the file input block.

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/add-files-to-writer-cloud-block.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=0f40f2cc19b00e3f36bbcf67824e8a3e" alt="Add files to Writer Cloud" data-og-width="3456" width="3456" data-og-height="1808" height="1808" data-path="images/agent-builder/parse-pdf-tutorial/add-files-to-writer-cloud-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/add-files-to-writer-cloud-block.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=17ccd17fc00cf4955a5d4cd155a6c19d 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/add-files-to-writer-cloud-block.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=808ac07a20f0ac49c982e91662cce8c7 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/add-files-to-writer-cloud-block.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=65f4f18263f2ed32a31c07cf29f04825 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/add-files-to-writer-cloud-block.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=a1445dfd72b178664685fac35ec961ec 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/add-files-to-writer-cloud-block.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=47ed37eb67228854fa25999e8e2c7578 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/add-files-to-writer-cloud-block.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=0072c61ddc5ec2055151f63e20aba9b1 2500w" />
  </Step>

  <Step title="Add the uploaded file information to the state">
    Finally, add a **Set state** block to the canvas. This block takes the results from the **Add files to Writer Cloud** block and stores it in the state as the `file_info` state variable. This is the information about the uploaded file, specifically the `id` of the file in Writer Cloud, that will be used in the next blueprint.

    In the block's configuration panel, update the following fields:

    * **Link variable**: `file_info`
    * **Value type**: `text`
    * **Value**: `@{result}`. This references the `result` from the previous block, which is the information about the uploaded file.

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/set-state-file-info.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=329481258b83d0213751714be3be5c5a" alt="Upload files to Writer Cloud" data-og-width="3456" width="3456" data-og-height="1806" height="1806" data-path="images/agent-builder/parse-pdf-tutorial/set-state-file-info.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/set-state-file-info.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=86b013c4a66c3fdb202c2b8247c1b0f1 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/set-state-file-info.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=ff341fe91c3ffb190deb6bf59ee1d89e 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/set-state-file-info.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=1dfcdf9a374bb4b6d1cab1bc50302bc1 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/set-state-file-info.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=d1234896dbb707c68bc6ffa9fc2ef0aa 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/set-state-file-info.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=fa8fec2fb4e123a3de8477c151213e3c 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/set-state-file-info.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=3068e3b665eb1222142a6193f4eb65ad 2500w" />
  </Step>
</Steps>

### Second blueprint: Parse and summarize the file

Once you've uploaded the file to the Writer Cloud, you can parse the PDF and provide the file's content to a text generation block.

<Steps>
  <Step title="Add a new blueprint">
    First, add a new blueprint to the canvas. Navigate to the Blueprint Layers section in the sidebar and click **+ Add blueprint** at the bottom of the blueprint layers outline.

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/add-blueprint.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=f083c9ae85a52c996402889fa0eeabb9" alt="Add blueprint" data-og-width="3456" width="3456" data-og-height="1806" height="1806" data-path="images/agent-builder/parse-pdf-tutorial/add-blueprint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/add-blueprint.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=ab584779c47efd96f080f405e8b8b3b9 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/add-blueprint.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=30955f8e7ac274cff22eea64c6a9d7d9 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/add-blueprint.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=cf3c74a8c83d1bd8c169fc7e0652b846 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/add-blueprint.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=fd32d89ee8bfc1556428d59d0dfce1a9 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/add-blueprint.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=31333cf04c3cc6136f4a923ec32661aa 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/add-blueprint.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=22f43e332fa480f48bc9708821818c1d 2500w" />
  </Step>

  <Step title="Add a UI trigger for the button to start summarizing">
    Navigate back to the Add Block section of the Agent Builder and add a **UI trigger** block to the new blueprint. This triggers the blueprint when a user clicks the button to start summarizing.

    In the block's configuration panel, update the following fields:

    * **Alias**: `Start summary` (optional, to make the trigger easier to identify)
    * **Component Id**: Select the `Summarize` button component from the dropdown of UI blocks
    * **Event type**: `wf-click`

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/start-summary-trigger.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=14a153c76c8ad3e1257557a7ae951011" alt="Start summary trigger" data-og-width="3456" width="3456" data-og-height="1812" height="1812" data-path="images/agent-builder/parse-pdf-tutorial/start-summary-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/start-summary-trigger.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=72f1f19f00a2a4593f188d52f7cc2e81 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/start-summary-trigger.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=5a180acfa216a24ec204eb3ca9864f90 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/start-summary-trigger.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=05186493138eb2ee593b8c39129f6537 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/start-summary-trigger.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=b99531454f8d4f2bc9f57b41607b6974 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/start-summary-trigger.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=f49b457c184c68450f6dd9dc632d4a2b 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/start-summary-trigger.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=e7fc6fe4b8b80cd5e451e9f197fa7440 2500w" />
  </Step>

  <Step title="Update the status message">
    Add a **Set state** block to the canvas. This block updates the status message in the state to indicate that the summarization is in progress. The message will appear in the UI message block.

    In the block's configuration panel, update the following fields:

    * **Link variable**: `status`
    * **Value type**: `text`
    * **Value**: `%Summarizing...`. The `%` symbol creates an animated spinning icon when the message appears in the UI.

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/update-status-message.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=3e13aab9c2f9f6a817cef8db1d178a97" alt="Update status message" data-og-width="3456" width="3456" data-og-height="1814" height="1814" data-path="images/agent-builder/parse-pdf-tutorial/update-status-message.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/update-status-message.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=d3b3dbd604f5c77c487fa7bb3c2157f1 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/update-status-message.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=3ce3d66159b7139c321eeace03e6523e 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/update-status-message.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=4620cd1390c25e0a8ce1ad018fbf8ff9 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/update-status-message.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=33fc31ac36c82e034ed657826df77dce 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/update-status-message.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=5bfeb239527bdf0b948e86e440749106 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/update-status-message.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=10f5f2f92a2baf676a846ea428bcdd61 2500w" />
  </Step>

  <Step title="Add a block to parse the uploaded PDF file">
    Add a **Parse PDF Tool** block to the canvas. This block parses the uploaded PDF file so that the agent can generate a summary of the file.

    In the block's configuration panel, update the following fields:

    * **File**: `@{file_info.0.id}`. This references the `file_info` state variable you defined in the first blueprint and specifically access the `id` of the uploaded file.

    <Tip>
      The `file_info` state variable is an array of objects, containing one object with information from the **Add files to Writer Cloud** block. You can see the values of state variables by clicking the **State Explorer** (`<>`) icon at the top of the canvas. Learn more about [nested state variables](/agent-builder/state#nested-state-variables).
    </Tip>

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/parse-pdf-tool-block.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=1a647f453a1dd18501468dbf3d0d9ceb" alt="Parse file" data-og-width="3456" width="3456" data-og-height="1808" height="1808" data-path="images/agent-builder/parse-pdf-tutorial/parse-pdf-tool-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/parse-pdf-tool-block.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=d309ec84b759813c7c36793a7c73af42 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/parse-pdf-tool-block.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=6be65ae658894740f9c424d7f7cb08a0 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/parse-pdf-tool-block.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=9464cd1e3d88fdd080f139acf0dfe2e0 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/parse-pdf-tool-block.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=bfd384be60fadb0c6139a675c80b05b4 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/parse-pdf-tool-block.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=71fabecf9ae5c203470ce495a7a8eca1 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/parse-pdf-tool-block.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=83a254a8a27cb56156ce838ab1df9a80 2500w" />
  </Step>

  <Step title="Add a block to generate a summary of the parsed file">
    Add a **Text generation** block to the canvas. This block generates text with a Palmyra LLM based on a prompt.

    In the block's configuration panel, update the following fields:

    * **Prompt**: `Provide a one-paragraph summary and a list of the three most important takeaways from this research paper: @{result}. Provide the summary for the user persona @{persona}.`
      * `@{result}` references the `result` from the previous block, which is the parsed PDF file.
      * `@{persona}` references the `persona` state variable you defined in the UI.
    * **Model**: `Palmyra X5`

    You can also update the additional fields **Temperature** and **Max tokens** to further control the output of the text generation.

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/generate-summary-block.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=884e9ec231163e2a4d64aa5a82b9e6d8" alt="Generate summary" data-og-width="3456" width="3456" data-og-height="1816" height="1816" data-path="images/agent-builder/parse-pdf-tutorial/generate-summary-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/generate-summary-block.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=0eb191bb895d54fbb75addb6e659f20b 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/generate-summary-block.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=6e5fa8927dfd58e569979beb32ea0f79 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/generate-summary-block.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=a030f80b8bfb3246aaf6057bc37d3627 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/generate-summary-block.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=4afa62227506f90b5f4e590ea5fe338a 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/generate-summary-block.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=622bbe0c52cea69479b9d9f0c708d4e5 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/generate-summary-block.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=8b6179287e9f7bf063cafd7dd5e89bde 2500w" />
  </Step>

  <Step title="Add the summary results to the state">
    Add a **Set state** block to the canvas. This block takes the results from the previous text generation block and stores it in the state as the `summary` state variable.

    In the block's configuration panel, update the following fields:

    * **Link variable**: `summary`
    * **Value type**: `text`
    * **Value**: `@{result}`. This references the `result` from the previous block, which is the summary of the parsed PDF file.

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/set-state-summary.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=c80888ca3d215112661ca2a2bbbe92e1" alt="Set state summary" data-og-width="3456" width="3456" data-og-height="1810" height="1810" data-path="images/agent-builder/parse-pdf-tutorial/set-state-summary.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/set-state-summary.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=4674f55741c03dd8ddc19a25213cdfb6 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/set-state-summary.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=ee0dba4f7b2332fd4c51d6e616dc2a34 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/set-state-summary.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=501dfffc2523cf82c12b3484d7955ce0 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/set-state-summary.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=cb2074099789cfb031cb4efe11fc2bf1 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/set-state-summary.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=9d5c0cb8a06ead8e43062cf785679f70 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/set-state-summary.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=6924d2f11eb8b90261d1f8e3b4e77ff1 2500w" />
  </Step>

  <Step title="Clear the status message from the state">
    Finally, add a **Set state** block to the canvas to clear the status message from the state.

    In the block's configuration panel, update the following fields:

    * **Link variable**: `status`
    * **Value type**: `text`
    * **Value**: Leave blank. This clears the status message from the state.

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/clear-status-message.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=7370708791e2f351c1e1937d4fd77d6f" alt="Clear status message" data-og-width="3456" width="3456" data-og-height="1808" height="1808" data-path="images/agent-builder/parse-pdf-tutorial/clear-status-message.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/clear-status-message.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=1883651aa62702af946bc7c09e8a9d7a 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/clear-status-message.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=2942e88bec8b054794571724138d7411 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/clear-status-message.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=2a9d387fc603247873e930f842e0f1f1 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/clear-status-message.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=16bd5ba4f42884206a434932200b1fc4 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/clear-status-message.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=3534e4df1905337ad19b553824b89aab 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/clear-status-message.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=0973981a0f66360236530cc4c6095b82 2500w" />
  </Step>
</Steps>

## Preview the agent

Now that you've built the agent, you can preview it.

1. Navigate to the **Preview** tab in the Agent Builder.
2. Add a PDF file to the file input block and select a persona from the dropdown.
3. Click the **Summarize** button to start the summarization process.
4. You should see the status message update to `%Summarizing...` and the summary results appear in the text block.

The results take a few seconds to generate. You can see the progress of the Agent Builder by going to the **Blueprints** tab. The blueprint blocks that have already run will be highlighted in green, and the one that's currently running will have an animated blue border.

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/blueprint-progress.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=f4213ab4084c828a555723aa85a84a49" alt="Blueprint in progress" data-og-width="3456" width="3456" data-og-height="1796" height="1796" data-path="images/agent-builder/parse-pdf-tutorial/blueprint-progress.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/blueprint-progress.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=0ba61d4c42c8d61b2a8d658765ed3c5f 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/blueprint-progress.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=b2517593f52e6caa8c88ac9d02e96d05 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/blueprint-progress.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=db5f2d3d44a7e87d2bc29245deb0bee2 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/blueprint-progress.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=bfd12e807fa0f820291a108bca526a43 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/blueprint-progress.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=e77294494ac8731601c76d0dfd572524 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/parse-pdf-tutorial/blueprint-progress.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=3c9dbd995b7ab600114ffff490b78fdd 2500w" />

If you encounter any issues, refer to the [Troubleshooting](/agent-builder/troubleshooting) guide for debugging information.

<feedback />
