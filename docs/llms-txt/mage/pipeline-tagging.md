# Source: https://docs.mage.ai/pipelines/pipeline-tagging.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Pipeline filtering and tagging

> How to organize, filter, group, and tag pipelines in Mage.

![Mario pipe](https://github.com/mage-ai/mage-ai/assets/59450879/750168bc-9a42-4083-badd-adc120b5f97b)

A [pipeline](/design/core-abstractions#pipeline) contains references to all the blocks of code you want to run, charts for visualizing data, and organizes the dependency between each block of code.

In the Mage GUI, pipelines can be filtered and grouped to make it easier to find the pipeline you want to run. You can also tag pipelines to make it easier to find pipelines that are related to each other.

![Filtering pipelines](https://user-images.githubusercontent.com/1066980/255380712-3d86d4ac-255b-4894-8a5f-45c10b7c68c8.gif)

To apply a tag, first right click the desired pipeline and select "Add/Remove tags," then, type or select the desired tags, separated by enter.

Mage will populate a list of existing tags for consistency. Once tags have been applied, you can group/filter your pipelines by tag on the "Pipeline" page.

Filters are sticky, so grouping/filtering and navigating away will preserve your filter settings.


Built with [Mintlify](https://mintlify.com).