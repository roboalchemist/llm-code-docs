# Source: https://docs.edgeimpulse.com/studio/organizations/custom-blocks/custom-ai-labeling-blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom AI labeling blocks

<Info>
  **Only available on the Enterprise plan**

  This feature is only available on the Enterprise plan. Review our [plans and pricing](https://edgeimpulse.com/pricing) or sign up for our free [expert-led trial](https://edgeimpulse.com/expert-led-trial) today.
</Info>

Custom AI labeling blocks are a way to extend the [AI labeling](/studio/projects/data-acquisition/ai-labeling) feature within Edge Impulse. If none of the blocks created by Edge Impulse that are built into the platform fit your needs, you can modify them or develop from scratch to create a custom AI labeling block. This allows you to integrate your own models or prompts for unique project requirements.

Ready to dive in and start building? Jump to the [examples](/studio/organizations/custom-blocks/custom-ai-labeling-blocks#examples)!

## Block structure

AI labeling blocks are an extension of transformation blocks operating in `standalone` mode and, as such, follow the same structure without being able to pass a directory or file directly to your scripts. Please see the [custom blocks](/studio/organizations/custom-blocks) overview page for more details.

<Frame caption="Custom AI labeling block structure">
  <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/custom-blocks-structure-ai-labeling.png?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=fc1531891a47059567d8830f023a45a1" width="1600" height="706" data-path=".assets/images/custom-blocks-structure-ai-labeling.png" />
</Frame>

## Block interface

The sections below define the required and optional inputs and the expected outputs for custom AI labeling blocks.

### Inputs

AI labeling blocks have access to environment variables, command line arguments, and mounted storage buckets.

#### Environment variables

The following environment variables are accessible inside of AI labeling blocks. Environment variable values are always stored as strings.

| Variable             | Passed | Description                                                     |
| -------------------- | ------ | --------------------------------------------------------------- |
| `EI_API_ENDPOINT`    | Always | The API base URL: `https://studio.edgeimpulse.com/v1`           |
| `EI_API_KEY`         | Always | The organization API key with member privileges: `ei_2f7f54...` |
| `EI_INGESTION_HOST`  | Always | The host for the ingestion API: `edgeimpulse.com`               |
| `EI_ORGANIZATION_ID` | Always | The ID of the organization that the block belongs to: `123456`  |
| `EI_PROJECT_ID`      | Always | The ID of the project: `123456`                                 |
| `EI_PROJECT_API_KEY` | Always | The project API key: `ei_2a1b0e...`                             |

You can also define your own environment variables to pass to your custom block using the `requiredEnvVariables` key in the metadata section of the `parameters.json` file. You will then be prompted for the associated values for these keys when pushing the block to Edge Impulse using the CLI. Alternatively, these values can be added (or changed) by editing the block in Studio.

#### Command line arguments

The parameter items defined in your `parameters.json` file will be passed as command line arguments to the script you defined in your Dockerfile as the `ENTRYPOINT` for the Docker image. Please refer to the [parameters.json](/tools/specifications/files/parameters-json) documentation for further details about creating this file, parameter options available, and examples.

In addition to the items defined by you, specific arguments will be automatically passed to your AI labeling block.

AI labeling blocks are an extension of transformation blocks operating in `standalone` mode, the arguments that are automatically passed to transformation blocks in this mode are also automatically passed to AI labeling blocks. Please refer to the [custom transformation blocks](/studio/organizations/custom-blocks/custom-transformation-blocks) documentation for further details on those parameters.

Along with the transformation block arguments, the following AI labeling specific arguments are passed as well.

| Argument                     | Passed      | Description                                                                                                                                                                                                                                                                 |
| ---------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--data-ids-file <file>`     | Always      | Provides the file path for `id.json` as a string. The `ids.json` file lists the data sample IDs to operate on as integers. See [ids.json](/tools/specifications/files/ids-json).                                                                                            |
| `--propose-actions <job-id>` | Conditional | Only passed when the user wants to preview label changes. If passed, label changes should be staged and not directly applied. Provides the job ID as an integer. See [preview mode](/studio/organizations/custom-blocks/custom-ai-labeling-blocks#running-in-preview-mode). |

Additional CLI arguments can also be specified using the CLI arguments field when editing the block in Studio.

#### Mounted storage buckets

One or more [cloud data storage](/studio/organizations/data/cloud-data-storage) buckets can be mounted inside of your block. If storage buckets exist in your organization, you will be prompted to mount the bucket(s) when initializing the block with the Edge Impulse CLI. The default mount point will be:

```bash  theme={"system"}
/mnt/s3fs/<bucket-name>
```

The mount point can be changed by editing the block in Studio after pushing.

### Outputs

There are no required outputs from AI labeling blocks. In general, all changes are applied to data using API calls inside the block itself.

## Running in preview mode

AI labeling blocks can run in "preview" mode, which is triggered when a user clicks `Label preview data` within an AI labeling action configuration. When a user is previewing label changes, the changes are *staged* and not applied directly.

For preview mode, the `--propose-actions <job-id>` argument is passed into your block. When you see this option, you should not apply changes directly to the data samples (e.g. via `raw_data_api.set_sample_bounding_boxes` or `raw_data_api.set_sample_structured_labels`) but rather use the `raw_data_api.set_sample_proposed_changes` API call.

<CodeGroup>
  ```python Python theme={"system"}
  if args.propose_actions:
      raw_data_api.set_sample_proposed_changes(project_id=project_id, sample_id=sample.id, set_sample_proposed_changes_request={
          'jobId': args.propose_actions,
          'proposedChanges': {
              'structuredLabels': structured_labels,
              'metadata': new_metadata
          }
      })
  else:
      raw_data_api.set_sample_structured_labels(
          project_id, sample.id, set_sample_structured_labels_request={
              'structuredLabels': structured_labels
          }
      )
      raw_data_api.set_sample_metadata(project_id=project_id, sample_id=sample.id, set_sample_metadata_request={
          'metadata': new_metadata
      })
  ```

  ```typescript Typescript theme={"system"}
  if (proposeActionsJobId) {
        await api.rawData.setSampleProposedChanges(project.id, sample.id, {
            jobId: proposeActionsJobId,
            proposedChanges: {
                boundingBoxes: newBbs,
            },
        });
    }
  else {
        await api.rawData.setSampleBoundingBoxes(project.id, sample.id, {
            boundingBoxes: newBbs,
        });
  }
  ```
</CodeGroup>

## Initializing the block

When you are finished developing your block locally, you will want to initialize it. The procedure to initialize your block is described in the [custom blocks](/studio/organizations/custom-blocks) overview page. Please refer to that documentation for details.

## Testing the block locally

<Warning>
  **AI labeling blocks are not supported by the** `edge-impulse-blocks runner` **CLI tool**
</Warning>

AI labeling blocks are not currently supported by the blocks runner in the Edge Impulse CLI. To test you custom AI labeling block, you will need to build the Docker image and run the container directly. You will need to pass any environment variables or command line arguments required by your script to the container when you run it.

```bash  theme={"system"}
docker build -t custom-ai-labeling-block .
docker run --rm -e EI_PROJECT_API_KEY='ei_...' -e CUSTOM_ENV_VAR='<env-value>' custom-ai-labeling-block --data-ids-file ids.json --custom-param-one foo --custom-param-two bar
```

## Pushing the block to Edge Impulse

When you have initialized and finished testing your block locally, you will want to push it to Edge Impulse. The procedure to push your block to Edge Impulse is described in the [custom blocks](/studio/organizations/custom-blocks) overview page. Please refer to that documentation for details.

## Using the block in a project

After you have pushed your block to Edge Impulse, it can be used in the same way as any other built-in block.

## Examples

Edge Impulse has developed several AI labeling blocks that are built into the platform. The code for these blocks can be found in public repositories under the [Edge Impulse GitHub account](https://github.com/edgeimpulse). The repository names typically follow the convention of `ai-labeling-<description>`. As such, they can be found by going to the Edge Impulse account and searching the repositories for `ai-labeling`.

Below are direct links to some examples:

* [Bounding box labeling with OWL-ViT](https://github.com/edgeimpulse/ai-labeling-zero-shot-object-detector-owl-vit)
* [Bounding box re-labeling with GPT-4o](https://github.com/edgeimpulse/ai-labeling-bounding-box-relabeling-gpt4o)
* [Image labeling with GPT-4o](https://github.com/edgeimpulse//ai-labeling-images-gpt4o)
* [Image labeling with pretrained models](https://github.com/edgeimpulse/ai-labeling-using-existing-ei-project)
* [Audio labeling with Audio Spectrogram Transformer](https://github.com/edgeimpulse/ai-labeling-audio-spectrogram-transformer)

## Troubleshooting

<Info>
  No common issues have been identified thus far. If you encounter an issue, please reach out on the [forum](https://forum.edgeimpulse.com) or, if you are on the Enterprise plan, through your support channels.
</Info>

## Additional resources

* [Custom blocks](/studio/organizations/custom-blocks)
* [AI labeling](/studio/projects/data-acquisition/ai-labeling)
* [edge-impulse-blocks](/tools/clis/edge-impulse-cli/blocks)
* [parameters.json](/tools/specifications/files/parameters-json)
* [ids.json](/tools/specifications/files/ids-json)


Built with [Mintlify](https://mintlify.com).