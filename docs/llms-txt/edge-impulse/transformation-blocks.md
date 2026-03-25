# Source: https://docs.edgeimpulse.com/studio/organizations/transformation-blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Transformation blocks

Transformation blocks are a flexible way to pre-process, i.e. transform, your [organizational data](/studio/organizations/data) through transformation jobs before using it within a project or to create another dataset. They can also be used standalone (not operating on organizational data) as a way to run cloud processing jobs for specific actions.

You can use transformation blocks to fetch external datasets, augment and create variants of your data samples, extract metadata from config files, create helper graphs, align and interpolate measurements across sensors, remove duplicate entries, and more.

<Frame caption="Transformation blocks overview page">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/transformation-blocks-overview.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=2b67d817799d3cf7734529acb369507e" width="1538" height="1000" data-path=".assets/images/transformation-blocks-overview.png" />
</Frame>

## Running a transformation block

Transformation blocks can be run individually through [transformation jobs](/studio/organizations/data-transformation), stacked together to run in series in [data pipelines](/studio/organizations/data-pipelines), or run as a [data source](/studio/projects/data-acquisition/data-sources) (standalone mode only) importing data into a project. Please refer to the respective documentation for details.

## Operating modes

Transformation blocks operate in one of three modes: file, directory, or standalone.

### File

Transformation blocks that have been configured with the file operating mode will only appear in the block dropdown for transformation jobs.

As the name implies, file transformation blocks operate on files. The directory specified in the input data path field for the transformation job is automatically scanned for files. Any files that are found are shown on the right hand side as the selected items.

<Frame caption="Transformation job with 'file' transformation block selected">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/transformation-job-block-file-mode.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=9cdc80a6bf3bc6a8d58948530dcd2900" width="1538" height="1000" data-path=".assets/images/transformation-job-block-file-mode.png" />
</Frame>

### Directory

Transformation blocks that have been configured with the directory operating mode will only appear in the block dropdown for transformation jobs.

As the name implies, directory transformation blocks operate on directories. The directory specified in the input data path field for the transformation job is automatically scanned for directories. Any directories that are found are shown on the right hand side as the selected items.

<Frame caption="Transformation job with 'directory' transformation block selected">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/transformation-job-block-directory-mode.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=aa6575acdbcb76db907843fa0bd44728" width="1538" height="1000" data-path=".assets/images/transformation-job-block-directory-mode.png" />
</Frame>

### Standalone

Transformation blocks that have been configured with the standalone operating mode can appear in the block dropdown for transformation jobs, for project data sources, or both depending on how the block has been set up.

As the name implies, standalone transformation blocks do not operate on any files or directories. No dataset selection fields will be shown for standalone blocks when creating a transformation job. There will be no files or directories shown on the right hand side as the selected items.

<Frame caption="Transformation job with 'standalone' transformation block selected">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/transformation-job-block-standalone-mode.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=7cc47936c1f67bc60f9e630c6f1463b2" width="1538" height="1000" data-path=".assets/images/transformation-job-block-standalone-mode.png" />
</Frame>

## Pre-built transformation blocks

Edge Impulse has the ability to incorporate pre-built transformation blocks into the platform and make these available for all organizations to use. Pre-built transformation blocks may be added over time as recurring needs or interests emerge.

As these blocks are added to the platform, they will be found within your organization by going to the **Transformation** left sidebar menu item under Custom blocks. The pre-built blocks will be listed under the **Public blocks** section at the bottom of the transformation blocks overview page.

## Custom transformation blocks

Please refer to the [custom transformation blocks](/studio/organizations/custom-blocks/custom-transformation-blocks) documentation for details.

## Troubleshooting

<Info>
  No common issues have been identified thus far. If you encounter an issue, please reach out on the [forum](https://forum.edgeimpulse.com) or, if you are on the Enterprise plan, through your support channels.
</Info>

## Additional Resources

* [Data transformation](/studio/organizations/data-transformation)
* [Data pipelines](/studio/organizations/data-pipelines)
* [Data sources](/studio/projects/data-acquisition/data-sources)
* [Custom transformation blocks](/studio/organizations/custom-blocks/custom-transformation-blocks)


Built with [Mintlify](https://mintlify.com).