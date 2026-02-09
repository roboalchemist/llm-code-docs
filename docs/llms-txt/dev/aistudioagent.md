# Source: https://dev.writer.com/blueprints/aistudioagent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AI Studio Agent

Runs a Writer AI Studio agent app by ID.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-block.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=e0eb9481a50bca31956d08f8141afa51" alt="" data-og-width="2310" width="2310" data-og-height="1490" height="1490" data-path="images/agent-builder/blueprints/ai-studio-agent-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-block.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=5e3876b2a54cca7d802481492f32092f 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-block.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=aafa6e36255a59e6206ce6d0f385de79 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-block.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=9da17b9e90d225b41521585c8a9f20ef 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-block.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=57f8351879d732b62e1d8e49d83a9d63 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-block.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=341ccb90a97ca54daeacd73edf31da6f 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-block.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=bc291c5ede6c905ebbf2e390cf19d306 2500w" />

## Overview

The **AI Studio Agent** block runs a [deployed no-code AI Studio agent](/no-code/introduction). Only agents with [text generation](/no-code/text-generation) and [research](/no-code/research) capabilities are supported.

Under `App Id`, you can select the no-code agent you'd like to run from a pre-populated list of your deployed no-code agents.

<Warning>No-code agents with [chat capabilities](/no-code/chat) are not supported with this blueprint block. See the [Agent Builder chatbot tutorial](/agent-builder/chatbot-tutorial) for an example of how to create a chatbot with Agent Builder.</Warning>

## Inputs

The **AI Studio Agent** block takes key-value pairs in the `App inputs` field. The inputs should match the inputs of the no-code agent you're running. The key is the name of the input and the value is the value you'd like to pass to the agent.

If the no-code agent is a research assistant, it takes a single input with the key `query`. The value is the query you'd like the agent to run.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-research-agent-inputs.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=6b8d9215b349c3a00d6547daa88f54ae" alt="" data-og-width="1822" width="1822" data-og-height="580" height="580" data-path="images/agent-builder/blueprints/ai-studio-agent-research-agent-inputs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-research-agent-inputs.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=996579e5b70e6655432f53c8f3014240 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-research-agent-inputs.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=a0ce41693bfa44cbc60f4315b7675915 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-research-agent-inputs.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=9acbedc751e6be8a7c3c7c6a2993c3c2 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-research-agent-inputs.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=5215f7c5a6f97cf7394bb2bf584e7816 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-research-agent-inputs.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=e5b2de4f1901b7ebebc12b99fb53b117 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-research-agent-inputs.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=119235798b0f99641b0c01503dce70f4 2500w" />

### File and image inputs

If the input is a file or an image, you must upload the file to Writer first and then pass the ID to the agent. You can't pass the file or image directly to the agent.

See the [Upload, parse, and summarize PDFs](/agent-builder/summarize-pdfs#first-blueprint%3A-upload-file-to-writer-cloud) tutorial for more information on how to upload files to the Writer cloud.

If the no-code agent accepts URLs to a file or image as input, you can pass a URL to the agent as a value rather than uploading the file to the Writer cloud.

## Output

The **AI Studio Agent** block returns the output of the no-code agent as a string.

You can access the output of an **AI Studio Agent** block using the `@{result}` variable in the block that follows it in a blueprint.

## Example

The following example shows an **AI Studio Agent** block that runs a no-code AI Studio agent.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-blueprint.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=737a0097cca4a7981c9ebb1f09136dd7" alt="" data-og-width="2606" width="2606" data-og-height="1084" height="1084" data-path="images/agent-builder/blueprints/ai-studio-agent-blueprint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-blueprint.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=a46dfd53a418b32367c55276a1ccefb6 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-blueprint.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=edad1abdb65fa0d10e6b33a098915328 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-blueprint.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=5f57090365ac05f11bb4cbce8b9ca0e9 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-blueprint.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=6f5d9ddc3c197d662bf34405d7d3ccd4 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-blueprint.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=7f8e48f69d89d4d3644236848a2c33c2 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-blueprint.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=fe643611db6d9da4c5064b2c0757ea8b 2500w" />

The no-code agent is an NDA review assistant that accepts a file input with the name `NDA` and runs a text generation workflow. It returns the analysis from the workflow in the `Output formatting` field.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-example.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=dc25a67c23e6d3d51b56c5578e60f8b4" alt="" data-og-width="3456" width="3456" data-og-height="1804" height="1804" data-path="images/agent-builder/blueprints/ai-studio-agent-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-example.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=421aed661d21bb7eaeee2337afaa5667 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-example.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=8f382a7606d07b743cfbb7019b1e72e9 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-example.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=8b0ee2974bd268b60f5e3b27870f9a49 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-example.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=67bf3e714a6ff0483cc8baf5e76c6d4f 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-example.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=89877828f697e46b608d6887add16724 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/blueprints/ai-studio-agent-example.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=9c33e6c7747c7c343de7ba6b5d668dcd 2500w" />

In this example blueprint, the **AI Studio Agent** block provides a file ID for an uploaded file, which is stored in the agent's state as `nda_file_id`. The file must already be uploaded to the Writer cloud.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-file-input.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=124ad6e47668cd41f7c4ad5144bf7dfe" alt="" data-og-width="1946" width="1946" data-og-height="740" height="740" data-path="images/agent-builder/blueprints/ai-studio-agent-file-input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-file-input.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=e615c2a31c65a1fcaf20a144a4c27c42 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-file-input.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=3c96d0d87d7b13305656df8072b80dcc 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-file-input.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=de3197143456ceb5c468e6f40669616f 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-file-input.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=efaeb33ee16ea3f4b18e52a3bfacb3d2 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-file-input.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=e746f58c766a0a6132ef594956770b1a 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-file-input.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=13cdfc1bfa332503c6c99c4c51cebc85 2500w" />

The **AI Studio Agent** block returns the output of the no-code agent and proceeds to the next block, which stores the `@{result}` in a state variable.

## Errors

If the AI Studio Agent block fails with the error `Failed to acquire proper response for completion from data`, ensure that your no-code agent in AI Studio returns a value in the `Output formatting` field and that you are passing the correct inputs to the agent.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-output-formatting.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=ffdf336a049d782d6f40d23dec078934" alt="" data-og-width="812" width="812" data-og-height="398" height="398" data-path="images/agent-builder/blueprints/ai-studio-agent-output-formatting.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-output-formatting.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=f865f988e5b63f3a400a509e682347e5 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-output-formatting.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=ba743256f1f5ee11da696e81e082fbad 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-output-formatting.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=030c3568a012542345682c9c89cb41fc 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-output-formatting.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=03e37938af31f881fc77bded1f49971e 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-output-formatting.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=b09e9ce15d798b4efd5bf3991f3b5110 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ai-studio-agent-output-formatting.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=643c49f3f0fb1c09cf13725c7bbf5e84 2500w" />

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
      <td>App Id</td>
      <td>App Id</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>The agent id can be found in the agent's URL. It has a UUID format.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        Format: uuid
      </td>
    </tr>

    <tr>
      <td>App inputs</td>
      <td>Key-Value</td>
      <td>-</td>

      <td>
        <code>
          {"{}"}
        </code>
      </td>

      <td>-</td>

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
      <td>The agent ran successfully.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>There was an error running the agent.</td>
    </tr>
  </tbody>
</table>

Access the output of an **AI Studio Agent** block using the `@{result}` variable in the block that follows it in a blueprint.
