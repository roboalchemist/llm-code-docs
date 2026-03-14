# Source: https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/working-with-document-ai.md

# Working with Document AI

This topic provides an overview of working with Document AI.

> **Note:**
>
> Before you begin working with Document AI, confirm that a warehouse, database, and schema are prepared
> and that the required roles and privileges are granted to the users.
>
> For more information, see [Setting up Document AI](setting-up.md).

Working with Document AI consists of the following steps:

1. Prepare your documents.

   The documents you process with Document AI must meet certain requirements.
   For more information, see [Prepare your documents for Document AI](preparing-documents.md).
2. Prepare a Document AI model build in Snowsight.

   Document AI consists of model builds, which include the model, the documents uploaded to test the model, and the data values to be extracted.

   To prepare a Document AI model build:

   1. Upload the documents that will be used to test the model.
   2. Define the data values to be extracted by [asking questions using natural language](optimizing-questions.md).
   3. Review the results provided by the model.
   4. Decide to either publish the model or fine-tune the model to improve the results.

   For more information about working with model builds, see [Prepare a Document AI model build](prepare-model-build.md).
3. Extract information in worksheets by using the [extracting query](extract-information.md).

   Use the extracting query to extract information from staged documents. For more information, see [Extract information with Document AI](extract-information.md).
