# Source: https://docs.edgeimpulse.com/studio/organizations/data-pipelines.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data pipelines

<Info>
  **Only available on the Enterprise plan**

  This feature is only available on the Enterprise plan. Review our [plans and pricing](https://edgeimpulse.com/pricing) or sign up for our free [expert-led trial](https://edgeimpulse.com/expert-led-trial) today.
</Info>

Building data pipelines is a very useful feature where you can stack several transformation blocks similar to the [Data sources pipelines](/studio/projects/data-acquisition/data-sources). They can be used in a standalone mode (just execute several transformation jobs in a pipeline), to feed a dataset or to feed a project.

<Frame caption="clinical data pipelines example">
  <img src="https://mintcdn.com/edgeimpulse/rTWxVUHegAMX0AbN/.assets/images/research-data-pipelines.png?fit=max&auto=format&n=rTWxVUHegAMX0AbN&q=85&s=24f8e78f2d3fa99ce4a0c9356c07456e" width="1600" height="738" data-path=".assets/images/research-data-pipelines.png" />
</Frame>

The examples in the screenshots below shows how to create and use a pipeline to create the 'AMS Activity 2022' dataset.

## Create a pipeline

To create a new pipeline, click on '**+Add a new pipeline**:

<Frame caption="Add a new clinical data pipeline">
  <img src="https://mintcdn.com/edgeimpulse/rTWxVUHegAMX0AbN/.assets/images/research-data-create-new-pipeline.png?fit=max&auto=format&n=rTWxVUHegAMX0AbN&q=85&s=c81e02f16c5cc31c76bb7a69dac88ea2" width="1201" height="1000" data-path=".assets/images/research-data-create-new-pipeline.png" />
</Frame>

### Get the steps from your transformation blocks

In your organization workspace, go to **Custom blocks -> Transformation** and select **Run job** on the job you want to add.

<Frame caption="Transformation blocks">
  <img src="https://mintcdn.com/edgeimpulse/rTWxVUHegAMX0AbN/.assets/images/research-data-run-job-transformation-block.png?fit=max&auto=format&n=rTWxVUHegAMX0AbN&q=85&s=c69a8476612160d41ce9882b748805b4" width="1600" height="645" data-path=".assets/images/research-data-run-job-transformation-block.png" />
</Frame>

Select **Copy as pipeline step** and paste it to the configuration json file.

<Frame caption="Copy">
  <img src="https://mintcdn.com/edgeimpulse/rTWxVUHegAMX0AbN/.assets/images/research-data-copy-pipeline-step.png?fit=max&auto=format&n=rTWxVUHegAMX0AbN&q=85&s=33bb3a4991112eedec41d1116353ddf6" width="1600" height="838" data-path=".assets/images/research-data-copy-pipeline-step.png" />
</Frame>

You can then paste the copied step directly to the respected field.

Below, you have an option to feed the data to either a **organisation dataset** or an **Edge Impulse project**

### Schedule and notify

By default, your pipeline will run every day. To schedule your pipeline jobs, click on the `⋮` button and select **Edit pipeline**.

<Frame caption="Edit pipeline">
  <img src="https://mintcdn.com/edgeimpulse/rTWxVUHegAMX0AbN/.assets/images/research-data-schedule-pipeline.png?fit=max&auto=format&n=rTWxVUHegAMX0AbN&q=85&s=86b80a60ff9e4b68d980725c5b780b08" width="1600" height="675" data-path=".assets/images/research-data-schedule-pipeline.png" />
</Frame>

Once the pipeline has successfully finished, it can send an email to the **Users to notify**.

## Run the pipeline

Once your pipeline is set, you can run it directly from the UI, from external sources or by scheduling the task.

### Run the pipeline from the UI

To run your pipeline from Edge Impulse studio, click on the `⋮` button and select **Run pipeline now**.

### Run the pipeline from code

To run your pipeline from Edge Impulse studio, click on the `⋮` button and select **Run pipeline from code**. This will display an overlay with `curl`, `Node.js` and `Python` code samples.

<Info>
  You will need to create an **API key** to run the pipeline from code.
</Info>

<Frame caption="Run the pipeline from code">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-data-sources-run-from-code.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=5475f438fff946deffe30322f736c26d" width="1303" height="1000" data-path=".assets/images/studio-data-sources-run-from-code.png" />
</Frame>

### Webhooks

Another useful feature is to create a **webhook** to call a URL when the pipeline has ran. It will run a POST request containing the following information:

```
{
    "organizationId":XX,
    "pipelineId":XX,
    "pipelineName":"Fetch, sort, validate and combine",
    "projectId":XXXXX,
    "success":true,
    "newItems":0,
    "newChecklistOK":0,
    "newChecklistFail":0
}
```

<Frame caption="Data sources webhooks">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-data-sources-webhooks.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=b469396a4e3771880ebe285a0f9cb026" width="1600" height="741" data-path=".assets/images/studio-data-sources-webhooks.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).