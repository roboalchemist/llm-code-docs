# Source: https://docs.pentaho.com/pdc-use/ldc-explore-your-data-cp/pdc-processing-data/pdc-processing-collections.md

# Processing collections

In Data Catalog, you can process Datasets to understand better their structure, quality, and consistency across files or tables. Processing is an essential part of preparing a Dataset for sharing, governance, or publication as a Data Product. The two main processing jobs available for Datasets are **Data Profiling** and **Data Aggregation**. These jobs help generate statistical summaries and quality insights at both the individual file level and the collection level.

**Note:** Processing is supported only for Datasets. Data Collections, which are a group of heterogeneous data, do not support profiling or aggregation jobs in the current release (PDC 10.2.5).

## **Data Profile**

The **Data Profile** job analyzes the structure and content of each file or table within the Dataset. It runs automatically using default profiling options and generates detailed statistics, including data types, null value percentages, distinct counts, and pattern distributions.

You should run a Data Profile job on a Dataset immediately after creating it or making significant updates. Profiling helps validate the structure and quality of the data, making it an essential step before sharing the Dataset with others or publishing it as a Data Product. To learn more about running a Data Profiling job, see [Run Data Profile job](https://docs.pentaho.com/pdc-use/ldc-explore-your-data-cp/pdc-processing-data/broken-reference).

When a Dataset is profiled, each file or table is evaluated independently. The system captures key metrics for each column and generates a profile report that helps you assess the overall quality and structure of the data. These insights are helpful in identifying inconsistencies, anomalies, or potential data issues before proceeding with further analysis or publication.

Profiling also enables the Columns canvas in the Dataset view. This canvas shows a visual representation of the common columns found across all included tables, along with their individual and aggregated statistics.

## **Data Aggregation**

The **Data Aggregation** job computes summary statistics across common columns shared by the profiled tables. Unlike profiling, which operates at the file or table level, aggregation works at the collection level to provide a consolidated view of the data. It helps you understand your dataset at a broader level by summarizing key statistics across all the files or tables it contains.

You should run **Data Aggregation** after the profiling process is complete. Aggregation is useful when you need summary insights across the entire Dataset, especially for identifying patterns, trends, or outliers at the collection level.

When you run this job, Data Catalog calculates overall values such as minimum, maximum, and average for each column that is common across the dataset. In addition to numerical summaries, aggregation helps you assess the consistency of the dataset’s structure. You can quickly identify whether all files follow the same column definitions and formats, or if there are structural differences that need attention. Aggregation results can also reveal trends and potential outliers in the data, helping you spot anomalies or irregular patterns across the dataset.

## Run Data Profile job

Perform the following steps to run the Data Profile job on the Dataset in Data Catalog:

**Note:** When you run a **Data Profiling** job on a Dataset, it automatically runs the **Data Aggregation** job as well. You do not need to run it separately.

1. In the left navigation menu, click **Data Canvas** and click the **Collections** tab.

   The list of collections appears.
2. Select a Dataset for which you want to run the Data Profile job.

   The summary page of the selected Dataset appears.
3. Click **Actions** and select **Process**.

   The **Choose Process** page appears, displaying the **Data Aggregation** and **Data Profiling** cards.
4. Under the Data Profile card, click **Start**.

   It initiates the data profiling job of the Dataset. You can see the status of the job in the **Workers** page.

You have successfully profiled the dataset in Data Catalog. When the Data Profile job is complete, you can view the results on the various tabs in the Content pane of the profiled dataset.

You can perform various actions, such as assigning business terms, trust scores, and sensitivity levels, and so on. For more information, see [Content pane](https://docs.pentaho.com/pdc-use/pdc-data-canvas-explore-your-data#content-pane).

## Run Data Aggregation job

Perform the following steps to run the Data Profile job on the Dataset in Data Catalog:

1. In the left navigation menu, click **Data Canvas** and click the **Collections** tab.

   The list of collections appears.
2. Select a Dataset for which you want to run the Data Profile job.

   The summary page of the selected Dataset appears.
3. Click **Actions** and select **Process**.

   The **Choose Process** page appears, displaying the **Data Aggregation** and **Data Profiling** cards.
4. Under the **Data Aggregation** card, click **Start**.

   It initiates the **Data Aggregation** job of the Dataset. You can see the status of the job in the **Workers** page.

You have successfully profiled the dataset in Data Catalog. When the Data Profile job is complete, you can view the aggregation results at the column level too. The following image is an example of data aggregation results that appear on the Statistics section under the **Summary** tab.

![PDC Data Aggregation Job Result](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-da9f8193b92b144ac823b2ffe6478194212d7f50%2FPDC%20Data%20Aggregation%20Job%20Results.png?alt=media)
