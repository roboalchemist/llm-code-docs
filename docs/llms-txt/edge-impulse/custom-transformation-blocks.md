# Source: https://docs.edgeimpulse.com/studio/organizations/custom-blocks/custom-transformation-blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom transformation blocks

<Info>
  **Only available on the Enterprise plan**

  This feature is only available on the Enterprise plan. Review our [plans and pricing](https://edgeimpulse.com/pricing) or sign up for our free [expert-led trial](https://edgeimpulse.com/expert-led-trial) today.
</Info>

Custom transformation blocks are a way to extend the capabilities of Edge Impulse beyond the [transformation blocks](/studio/organizations/transformation-blocks) built into the platform. If none of the existing blocks created by Edge Impulse fit your needs, you can create custom transformation blocks to integrate your own data pre-processing for unique project requirements.

Ready to dive in and start building? Jump to the [examples](/studio/organizations/custom-blocks/custom-transformation-blocks#examples)!

## Block structure

The transformation block structure is shown below. Please see the [custom blocks](/studio/organizations/custom-blocks) overview page for more details.

<Frame caption="Custom transformation block structure">
  <img src="https://mintcdn.com/edgeimpulse/fGaR6Z5uJaXr3nXE/.assets/images/custom-blocks-structure-transformation.png?fit=max&auto=format&n=fGaR6Z5uJaXr3nXE&q=85&s=9cbfa1c4a05a03d9199367f4f5754cac" width="1600" height="706" data-path=".assets/images/custom-blocks-structure-transformation.png" />
</Frame>

## Block interface

The sections below define the required and optional inputs and the expected outputs for custom transformation blocks.

### Inputs

Transformation blocks have access to environment variables, command line arguments, and mounted storage buckets.

#### Environment variables

The following environment variables are accessible inside of transformation blocks. Environment variable values are always stored as strings.

| Variable                 | Passed      | Description                                                                                            |
| ------------------------ | ----------- | ------------------------------------------------------------------------------------------------------ |
| `EI_API_ENDPOINT`        | Always      | The API base URL: `https://studio.edgeimpulse.com/v1`                                                  |
| `EI_API_KEY`             | Always      | The organization API key with member privileges: `ei_2f7f54...`                                        |
| `EI_INGESTION_HOST`      | Always      | The host for the ingestion API: `edgeimpulse.com`                                                      |
| `EI_LAST_SUCCESSFUL_RUN` | Always      | The last time the block was successfully run, if a part of a data pipeline: `1970-01-01T00:00:00.000Z` |
| `EI_ORGANIZATION_ID`     | Always      | The ID of the organization that the block belongs to: `123456`                                         |
| `EI_PROJECT_ID`          | Conditional | Passed if the transformation block is a data source for a project. The ID of the project: `123456`     |
| `EI_PROJECT_API_KEY`     | Conditional | Passed if the transformation block is a data source for a project. The project API key: `ei_2a1b0e...` |

You can also define your own environment variables to pass to your custom block using the `requiredEnvVariables` property in the `parameters.json` file. You will then be prompted for the associated values for these properties when pushing the block to Edge Impulse using the CLI. Alternatively, these values can be added (or changed) by editing the block in Studio after pushing.

#### Command line arguments

The parameter items defined in your `parameters.json` file will be passed as command line arguments to the script you defined in your Dockerfile as the `ENTRYPOINT` for the Docker image. Please refer to the [parameters.json](/tools/specifications/files/parameters-json) documentation for further details about creating this file, parameter options available, and examples.

In addition to the items defined by you, the following arguments will be automatically passed to your custom transformation block.

| Argument                       | Passed      | Description                                                                                                                                                                                                                           |
| ------------------------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--in-file <file>`             | Conditional | Passed if operation mode is set to `file`. Provides the file path as a string. This is the file to be processed by the block.                                                                                                         |
| `--in-directory <dir>`         | Conditional | Passed if operation mode is set to `directory`. Provides the directory path as a string. This is the directory to be processed by the block.                                                                                          |
| `--out-directory <dir>`        | Conditional | Passed if operation mode is set to either `file` or `directory`. Provides the directory path to the output directory as a string. This is where block output needs to be written.                                                     |
| `--hmac-key <key>`             | Conditional | Passed if operation mode is set to either `file` or `directory`. Provides a project HMAC key as a string, if it exists, otherwise `'0'`.                                                                                              |
| `--metadata <metadata>`        | Conditional | Passed if operation mode is set to either `file` or `directory`, the pass in metadata property (`indMetadata`) is set to true, and the metadata exists. Provides the metadata associated with data item as a stringified JSON object. |
| `--upload-category <category>` | Conditional | Passed if operation mode is set to `file` or `directory` and the transformation job is configured to import the results into a project. Provides the upload category (`split`, `training`, or `testing`) as a string.                 |
| `--upload-label <label>`       | Conditional | Passed if operation mode is set to `file` or `directory` and the transformation job is configured to import the results into a project. Provides the upload label as a string.                                                        |

CLI arguments can also be specified using the `cliArguments` property in the `parameters.json` file. Alternatively, these arguments can be added (or changed) by editing the block in Studio.

Lastly a user can be prompted for extra CLI arguments when configuring a transformation job if the `allowExtraCliArguments` property is set to `true`.

#### Mounted storage buckets

One or more [cloud data storage](/studio/organizations/data/cloud-data-storage) buckets can be mounted inside of your block. If storage buckets exist in your organization, you will be prompted to mount the bucket(s) when initializing the block with the Edge Impulse CLI. The default mount point will be:

```bash  theme={"system"}
/mnt/s3fs/<bucket-name>
```

The mount point can be changed by editing your `parameters.json` file before pushing the block to Edge Impulse or editing the block in Studio after pushing.

### Outputs

There are no required outputs from transformation blocks. In general, for blocks operating in `file` or `directory` mode, new data is written to the directory given by the `--out-directory <dir>` argument. For blocks operating in `standalone` mode, any actions are typically achieved using API calls inside the block itself.

## Understanding operating modes

Transformation blocks can operate in one of three modes: `file`, `directory`, or `standalone`.

### File

As the name implies, file transformation blocks operate on files. When configuring a transformation job, the user will select a list of files to transform. These files will be individually passed to and processed by the script defined in your transformation block. File transformation blocks can be run in multiple processing jobs in parallel.

Each file will be passed to your block using the `--in-file <file>` argument.

### Directory

As the name implies, directory transformation blocks operate on directories. When configuring a transformation job, the user will select a list of directories to transform. These directories will be individually passed to and processed by the script defined in your transformation block. Directory transformation blocks can be run in multiple processing jobs in parallel.

Each directory will be passed to your block using the `--in-directory <dir>` argument.

### Standalone

Standalone transformation blocks are a flexible way to run generic cloud jobs that can be used for a wide variety of tasks. In standalone mode, no data is passed into your block. If you need to access your data, you will need to mount your storage bucket(s) into your block. Standalone transformation blocks are run as a single processing job; they *cannot* be run in multiple processing jobs in parallel.

## Updating data item metadata

If your custom transformation block is operating in `directory` mode and transforming a clinical dataset, you can update the metadata associated with the data item after it is processed.

To do so, your custom transformation block needs to write an `ei-metadata.json` file to the directory specified in the `--out-directory <dir>` argument. Please refer to the [ei-metadata.json](/tools/specifications/files/ei-metadata-json) documentation for further details about this file.

```python  theme={"system"}
with open(os.path.join(args.out_directory, 'ei-metadata.json'), 'w') as f:
    f.write(json.dumps({
        'version': 1,
        'action': 'add',
        'metadata': {
            'now': round(time.time() * 1000)
        }
    }))
```

## Showing the block in Studio

There are two locations within Studio that transformation blocks can be found: transformation jobs and project data sources.

Transformation blocks operating in `file` or `directory` mode will always been shown as an option in the block dropdown for transformation jobs. They cannot be used as a project data source.

Transformation blocks operating in `standalone` mode can optionally be shown in the block dropdown for transformation jobs and/or in the block dropdown for project data sources.

### For transformation jobs

| Operating mode | Shown in block dropdown                                    |
| -------------- | ---------------------------------------------------------- |
| `file`         | Always                                                     |
| `directory`    | Always                                                     |
| `standalone`   | If `showInCreateTransformationJob` property set to `true`. |

### For project data sources

| Operating mode | Shown in block dropdown                        |
| -------------- | ---------------------------------------------- |
| `file`         | Never                                          |
| `directory`    | Never                                          |
| `standalone`   | If `showInDataSources` property set to `true`. |

## Initializing the block

When you are finished developing your block locally, you will want to initialize it. The procedure to initialize your block is described in the [custom blocks](/studio/organizations/custom-blocks) overview page. Please refer to that documentation for details.

## Testing the block locally

To speed up your development process, you can test your custom transformation block locally. There are two ways to achieve this. You will need to have Docker installed on your machine for either approach.

### With blocks runner

For the first method, you can use the CLI `edge-impulse-blocks runner` tool. See [Block runner](/tools/clis/edge-impulse-cli/blocks#block-runner) for additional details.

If your custom transformation block is operating in either `file` or `directory` mode, you will be prompted for information to look up and download data (a file or a directory) for the block to operate on when using the blocks runner. This can be achieved by providing either a data item name (clinical data) or the path within a dataset for a file or directory (clinical or default data). You can also specify some of this information using the blocks runner command line arguments.

| Argument                   | Description                                                                                                                                                                                                                                                                                                        |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--dataset <dataset> `     | Transformation blocks in `file` or `directory` mode. Files and directories will be looked up within this dataset. If not provided, you will be prompted for a dataset name.                                                                                                                                        |
| `--data-item <data-item> ` | Clinical data only. Transformation blocks in `directory` mode. The data item will be looked up, downloaded, and passed to the container when it is run. If not provided, you will be prompted for the information required to look up a data item.                                                                 |
| `--file <filename> `       | Clinical data only. Transformation blocks in `file` mode. Must be used in conjunction with `--data-item <data-item>`. The file will be looked up, downloaded, and passed to the container when it is run. If not provided, you will be prompted for the information required to look up a file within a data item. |
| `--skip-download`          | Skips downloading the data.                                                                                                                                                                                                                                                                                        |
| `--extra-args <args>`      | Additional arguments for your script.                                                                                                                                                                                                                                                                              |

Additional arguments to your script can be provided as a single string using `--extra-args <args>` argument.

```bash  theme={"system"}
 edge-impulse-blocks runner --extra-args "--custom-param-one foo --custom-param-two bar"
```

Using the above approach will create an `ei-block-data` directory within your custom block directory. It will contain subdirectories for the data that has been downloaded.

### With Docker

For the second method, you can build the Docker image and run the container directly. You will need to pass any environment variables or command line arguments required by your script to the container when you run it.

If your transformation block operates in either `file` or `directory` mode, you will also need to create a `data/` directory within your custom block directory and place your data used for testing here.

```bash  theme={"system"}
docker build -t custom-transformation-block .
```

`file` mode:

```bash  theme={"system"}
docker run --rm -v $PWD/data:/data -e CUSTOM_ENV_VAR='<env-value>' custom-transformation-block --in-file /data/<file> --out-directory /data/out --custom-param foo
```

`directory` mode:

```bash  theme={"system"}
docker run --rm -v $PWD/data:/data -e CUSTOM_ENV_VAR='<env-value>' custom-transformation-block --in-directory /data  --out-directory /data/out --custom-param foo
```

`standalone` mode:

```bash  theme={"system"}
docker run --rm -e CUSTOM_ENV_VAR='<env-value>' custom-transformation-block --custom-param foo
```

## Pushing the block to Edge Impulse

When you have initialized and finished testing your block locally, you will want to push it to Edge Impulse. The procedure to push your block to Edge Impulse is described in the [custom blocks](/studio/organizations/custom-blocks) overview page. Please refer to that documentation for details.

## Using the block in Studio

After you have pushed your block to Edge Impulse, it can be used in the same way as any other built-in block.

## Examples

Edge Impulse has developed several transformation blocks, some of which are built into the platform. The code for these blocks can be found in public repositories under the [Edge Impulse GitHub account](https://github.com/edgeimpulse). The repository names typically follow the convention of `example-transform-<description>`. As such, they can be found by going to the Edge Impulse account and searching the repositories for `example-transform`.

Note that when using the above search term you will come across synthetic data blocks as well. Please read the repository description to identify if it is for a transformation block or a synthetic data block.

Further, several example transformation blocks have been gathered into a single repository:

* [Transformation block examples](https://github.com/edgeimpulse/transformation-blocks)

## Troubleshooting

<Accordion title="Files in storage bucket cannot be accessed">
  If you cannot access the files in your storage bucket, make sure that the mount point has been properly configured and that you are referencing this location within your processing script.

  You can double check the mount point by looking at the additional mount point section when editing the block in Studio:

  <Frame caption="Setting up mount point">
    <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/transformation-block-mount-point.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=145e6caf1dc476fc719ce3f41d767ddb" width="1600" height="207" data-path=".assets/images/transformation-block-mount-point.png" />
  </Frame>

  If you do not see your storage bucket, you can mount it here.

  When using the Edge Impulse CLI to initialize your block, it is a common mistake to forget to press the `<space>` key to select the bucket for mounting (and therefore the storage bucket is not added to the parameters.json file).
</Accordion>

<Accordion title="Transformation job runs indefinitely">
  If you notice that your transformation job runs indefinitely, it is probably because of an error with your processing script or the script has not been properly terminated.

  Make sure to exit your script with code 0 (`return 0`, `exit(0)` or `sys.exit(0)`) for success or with any other error code for failure.
</Accordion>

## Additional resources

* [Custom blocks](/studio/organizations/custom-blocks)
* [Transformation blocks](/studio/organizations/transformation-blocks)
* [edge-impulse-blocks](/tools/clis/edge-impulse-cli/blocks)
* [parameters.json](/tools/specifications/files/parameters-json)
* [ei-metadata.json](/tools/specifications/files/ei-metadata-json)


Built with [Mintlify](https://mintlify.com).