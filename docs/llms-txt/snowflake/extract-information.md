# Source: https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/extract-information.md

# Extract information with Document AI

This topic describes extracting information from documents using Document AI.

If you previously published or trained the Document AI model build, you can now extract information from documents by
running the extracting query in worksheets.
You can also create processing pipelines to continuously process
new documents in a stage.

> **Note:**
>
> Document AI has known limitations, including the number and size of documents you can process in a single query.
> For more information, see [Known limitations to Document AI](limitations.md).

## Prerequisites

Successful information extraction requires the following conditions:

* The documents used for information extraction are stored in either an internal or external stage.
  For more information, see [Setting up Document AI](setting-up.md).
* You are using the database and schema you set up for Document AI. For example:

  ```sqlsyntax
  USE DATABASE doc_ai_db;
  USE SCHEMA doc_ai_schema;
  ```

* You are using an account role that is granted the SNOWFLAKE.DOCUMENT_INTELLIGENCE_CREATOR database role.
  For more information, see [Setting up Document AI](setting-up.md).
* You previously published a Document AI model build or trained a Document AI model.
  For more information, see [Publish a Document AI model build](prepare-model-build.md).

## Use the extracting query

An extracting query is a SQL query based on the PREDICT method. For more information,
see [<model_build_name>!PREDICT](../../../sql-reference/classes/document-intelligence/methods/predict.md).

To extract information from documents, run the extracting query in worksheets. After you publish or train the
Document AI model, you can see the extracting query defined in Snowsight.

To view the extracting query in Snowsight:

1. Sign in to [Snowsight](../../ui-snowsight-gs.md).
2. In the navigation menu, select AI & ML » AI Studio.
3. Next to the Document Processing Playground, select Open. In the Document Processing Playground, to access Document AI, select Go to Document AI model builds.
4. Select a warehouse.

   The list of model builds appears.
5. From the list of model builds, select the name of the model build you want to see the query for.
6. To view the Extracting Query, select the Build Details tab.

> **Important:**
>
> The [<model_build_name>!PREDICT](../../../sql-reference/classes/document-intelligence/methods/predict.md) method is deprecated. Snowflake recommends
> using the [AI_EXTRACT](../../../sql-reference/functions/ai_extract-document-ai.md) function instead. For more information,
> see [Document AI decommission (Pending)](../../../release-notes/bcr-bundles/un-bundled/bcr-2156.md).

## Create document processing pipelines

With Document AI, you can create pipelines that automatically process document files to extract information.
To create a processing pipeline, you need to create both a stream on a stage and a task to continuously process new documents
in the stage.

For more information, see [Tutorial: Create a document processing pipeline with Document AI](tutorials/create-processing-pipelines.md).
