# Source: https://docs.edgeimpulse.com/knowledge/guides/reference-designs/health-reference-design.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Health reference design

In this section, you will find a health reference design that describes an end-to-end machine learning workflow for building a wearable health product using Edge Impulse.

We will utilize a publicly available dataset of PPG and accelerometer data that was collected from 15 subjects performing various activities, and emulate a clinical study to train a machine learning model that can classify activities.

## Overview

The dataset selected to use in this example is the **PPG-DaLiA dataset**, which includes 15 subjects performing 9 activities, resulting in a total of 15 recordings. See the CSV file summary [here](/knowledge/guides/reference-designs/health-reference-design/synchronizing-clinical-data), and read more about it in the publishers website [here](https://archive.ics.uci.edu/dataset/495/ppg+dalia),

This dataset covers an activity study where data is recorded from a wearable end device (PPG + accelerometer), along with labels such as **Stairs, Soccer, Cycling, Driving, Lunch, Walking, Working, Clean Baseline,** and **No Activity**. The data is collected and validated, then written to a clinical dataset in an Edge Impulse organization, and finally imported into an Edge Impulse project where we train a classifier.

The health reference design builds transformation blocks that [sync](/knowledge/guides/reference-designs/health-reference-design/synchronizing-clinical-data) clinical data, [validate](/knowledge/guides/reference-designs/health-reference-design/validating-clinical-data) the dataset, [query](/knowledge/guides/reference-designs/health-reference-design/querying-clinical-data) the dataset, and [transform](/knowledge/guides/reference-designs/health-reference-design/transforming-clinical-data) the data to process raw data files into a unified dataset.

<Frame caption="Data Pipeline">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/healthref-block-diagram.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=9b4f9e564ad773f7299c04fb140a1e63" width="1151" height="561" data-path=".assets/images/healthref-block-diagram.png" />
</Frame>

The design culminates in a [data pipeline](/studio/organizations/data-pipelines) that handles data coming from multiple sources, data alignment, and a multi-stage pipeline before the data is imported into an Edge Impulse project.

We won't cover in detail all the code snippets, it should be straightforward to follow through, if issues are encountered our solution engineers can help you set this end-to-end ML workflow.

## Health Reference Design Sections

This **health reference design** section helps you understand how to create a full clinical data pipeline by:

* [Synchronizing clinical data with a bucket](/knowledge/guides/reference-designs/health-reference-design/synchronizing-clinical-data): Collect and organize data from multiple sources into a sorted dataset.
* [Validating clinical data](/knowledge/guides/reference-designs/health-reference-design/validating-clinical-data): Ensure the integrity and consistency of the dataset by applying checklists.
* [Querying clinical data](/knowledge/guides/reference-designs/health-reference-design/querying-clinical-data): Explore and slice data using a query system.
* [Transforming clinical data](/knowledge/guides/reference-designs/health-reference-design/transforming-clinical-data): Process and transform raw data into a format suitable for machine learning.

## Bringing it all together

After you have completed the health reference design, you can go further by combining the individual transformation steps into a data pipeline.

Refer to the following guide to learn how to build data pipelines:

* [Building data pipelines](/studio/organizations/data-pipelines): Build pipelines to automate data processing steps.

The Health Reference Design pipeline consists of the following steps:

* [DataProcessor](https://github.com/edgeimpulse/health-reference-design-public-data): Processes raw data files for each subject.
* [MetadataGenerator](https://github.com/edgeimpulse/health-reference-design-public-data): Extracts and attaches metadata to each subject's data.
* [DataCombiner](https://github.com/edgeimpulse/health-reference-design-public-data): Merges all processed data into a unified dataset.

Repository containing the blocks used in this health reference design:

[https://github.com/edgeimpulse/health-reference-design-public-data](https://github.com/edgeimpulse/health-reference-design-public-data)

### Data Pipeline Workflow

The data pipeline workflow for the Health Reference Design is as follows:

<Frame caption="Data Pipeline - workflow">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/healthref-block-diagram.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=9b4f9e564ad773f7299c04fb140a1e63" width="1151" height="561" data-path=".assets/images/healthref-block-diagram.png" />
</Frame>

### Creating and Running the Pipeline in Edge Impulse

Now that all transformation blocks are pushed to Edge Impulse, you can create a pipeline to chain them together.

#### Steps:

1. **Access Pipelines:**

* In Edge Impulse Studio, navigate to your organization.
* Go to Data > Pipelines.

2. **Add a New Pipeline:**

* Click on + Add a new pipeline.
* Name: PPG-DaLiA Data Processing Pipeline
* Description: Processes PPG-DaLiA data from raw files to a combined dataset.

3. **Configure Pipeline Steps:**

* Paste the following JSON configuration into the pipeline steps:

```json  theme={"system"}
[
  {
   "name": "Process Subject Data",
   "filter": "name LIKE '%S%_E4%'",
   "uploadType": "dataset",
   "inputDatasetId": "raw-dataset",
   "outputDatasetId": "processed-dataset",
   "transformationBlockId": 1234, // Replace 1234 with your DataProcessor block ID
   "transformationParallel": 3,
   "parameters": {
    "in-directory": "."
   }
  },
  {
   "name": "Generate Metadata",
   "filter": "name LIKE '%S%_E4%'",
   "uploadType": "dataset",
   "inputDatasetId": "processed-dataset",
   "outputDatasetId": "processed-dataset",
   "transformationBlockId": 5678, // Replace 5678 with your MetadataGenerator block ID
   "transformationParallel": 3,
   "parameters": {
    "in-directory": "."
   }
  },
  {
   "name": "Combine Processed Data",
   "filter": "name LIKE '%'",
   "uploadType": "dataset",
   "inputDatasetId": "processed-dataset",
   "outputDatasetId": "combined-dataset",
   "transformationBlockId": 9101, // Replace 9101 with your DataCombiner block ID
   "transformationParallel": 1,
   "parameters": {
    "dataset-name": "ppg_dalia_combined.parquet"
   }
  }
]
```

<Info>
  Replace the transformationBlockId values with the actual IDs of your transformation blocks.
</Info>

4. **Save the Pipeline.**

5. **Run the Pipeline:**

* Click on the ⋮ (ellipsis) next to your pipeline.
* Select Run pipeline now.

6. **Monitor Execution:**

* Check the pipeline logs to ensure each step runs successfully.
* Address any errors that may occur.

7. **Verify Output:**

* After completion, verify that the datasets (processed-dataset and combined-dataset) have been created and populated.

### Next Steps

After the pipeline has successfully run, you can import the combined dataset into an Edge Impulse project to train a machine learning model.

If you didn't complete the pipeline, don't worry, this is just a demonstration. However, you can still import the processed dataset from our [HRV Analysis](/tutorials/end-to-end/hr-hrv-estimation) tutorial to train a model.

Refer to the following guides to learn how to import datasets into Edge Impulse:

* [HRV Analysis](/tutorials/end-to-end/hr-hrv-estimation): Analyze Heart Rate Variability (HRV) data.
* [Activity Recognition](/tutorials/end-to-end/motion-recognition): Classify activities using accelerometer data.
* [MLOps](/knowledge/concepts/lifecycle/lifecycle-management): Implement MLOps practices in your workflow.

### Conclusion

The Health Reference Design provides a comprehensive overview of building a wearable health product using Edge Impulse. By following the steps outlined in this guide, you will gain a practical understanding of a real-world machine learning workflow for processing and analyzing clinical data.

If you have any questions or need assistance with implementing the Health Reference Design, feel free to reach out to our [sales team](https://edgeimpulse.com/contact-sales) for product development, or share your work on our [forum](https://forum.edgeimpulse.com).


Built with [Mintlify](https://mintlify.com).