# Source: https://docs.snowflake.com/en/release-notes/overview.md

# Source: https://docs.snowflake.com/en/migrations/sma-docs/workspace-estimator/overview.md

# Source: https://docs.snowflake.com/en/migrations/sma-docs/user-guide/overview.md

# Source: https://docs.snowflake.com/en/migrations/sma-docs/interactive-assessment-application/overview.md

# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/snowpark/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/native-apps/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/built-in-models/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/streamlit/migrations-and-upgrades/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/native-apps/connector-sdk/reference/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-ml/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-ml/ml-jobs/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-ml/feature-store/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/streamlit-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/stage-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/sql-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/service-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/image-repository-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/image-registry-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/compute-pool-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/snowpark-commands/package-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/snowpark-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/object-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/notebook-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/logs-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/helpers-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/git-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/dbt-commands/execute/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/dbt-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/cortex-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/connection-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/bootstrap-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/auth-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/native-apps-commands/version/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/native-apps-commands/release-directive/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/native-apps-commands/release-channel/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/native-apps-commands/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/streamlit-apps/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/services/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/git/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/native-apps/connector-sdk/flow/ingestion-management/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/native-apps/connector-sdk/using/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/streamlit/getting-started/overview.md

# Source: https://docs.snowflake.com/en/developer-guide/native-apps/connector-sdk/flow/overview.md

# Source: https://docs.snowflake.com/en/user-guide/trust-center/overview.md

# Source: https://docs.snowflake.com/en/user-guide/opencatalog/overview.md

# Source: https://docs.snowflake.com/en/user-guide/client-connectivity-troubleshooting/overview.md

# Source: https://docs.snowflake.com/en/user-guide/views-semantic/overview.md

# Source: https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/overview.md

# Document AI

## What is Document AI

Document AI is a Snowflake AI feature that uses Arctic-TILT, a proprietary large language model (LLM), to extract data from documents.
Document AI processes documents of various formats and extracts information from both text-heavy paragraphs and the content in a
graphical form, such as logos, handwritten text (signatures), tables, or checkmarks. With Document AI, you can prepare pipelines
for continuous processing of new documents of a specific type, such as invoices or finance statements. You can extract information from
entities (in a form of a single value or a list of values), or tables based on the list of specified columns.

Document AI provides both zero-shot extraction and fine-tuning. Zero-shot means that the foundation model can locate
and extract information specific to a document type, even if the model has never seen the document before. This is because the
foundation model is trained on a large volume of various documents, so the model broadly understands the type of document being
processed.

Additionally, you can fine-tune the Snowflake Arctic-TILT model to improve your results by training the model on the documents specific to your
use case. The fine-tuned model (including the training data used) is available only to you and is not shared with other Snowflake customers.

## When to use Document AI

Document AI is best used when:

* You want to turn unstructured data from documents into structured data in tables.
* You want to create pipelines for continuous processing of new documents of a specific type.
* Business users with domain knowledge prepare the model, and the data engineers working with SQL prepare pipelines to automate the
  processing of new documents.

## How Document AI works

Working with Document AI is divided into two phases:

* Preparing a Document AI model build

  You can think of the model build as representing a single type of a document or a use case; for example, a model build for
  extracting information from invoice documents. The Document AI model build includes the model, the data values to be extracted,
  and the documents uploaded to test and train the model.

  You prepare the model build through a Document AI user interface in Snowsight. The interface lets you create a model build,
  upload documents to test and train the model, define data values (information to be extracted) by asking questions using natural
  language, evaluate the model, and publish the model build or fine-tune the model to improve the results.

  For more information, see [Prepare a Document AI model build](prepare-model-build.md).
* Extracting information from documents

  When the model build is ready, you can begin extracting information from documents by running an extracting query,
  which uses the [<model_build_name>!PREDICT](../../../sql-reference/classes/document-intelligence/methods/predict.md) method.
  You can then use the extracting query to create pipelines for continuous processing with streams and tasks.

  For more information, see [Extract information with Document AI](extract-information.md).

  > **Note:**
  >
  > The documents to be processed using the [<model_build_name>!PREDICT](../../../sql-reference/classes/document-intelligence/methods/predict.md) method must be stored in an
  > internal or external stage.

To get started with Document AI, see [Tutorial: Create a document processing pipeline with Document AI](tutorials/create-processing-pipelines.md).

## Document AI model version history

To work with the latest version of the Arctic-TILT model, create a new
Document AI model build.

| Model version release date | Model version improvements |
| --- | --- |
| [May 8, 2025](../../../release-notes/2025/other/2025-05-08-document-ai.md) | * Checkbox identification |
| [April 16, 2025](../../../release-notes/2025/other/2025-04-16-document-ai.md) | *Language support for Spanish, French, German, Portuguese, Italian, and Polish* Language-specific diacritics * Overall model quality |
| [February 14, 2025](../../../release-notes/2025/other/2025-02-14-document-ai.md) | *Checkbox identification* Answers to yes/no questions * Overall model quality |
| [August 6, 2024](../../../release-notes/2024/other/2024-08-06-document-ai.md) | *Doubling length of the answers provided by the model.* Training time. See [Training time estimation](prepare-model-build.md). |
| [June 21, 2024](../../../release-notes/2024/other/2024-06-21-document-ai.md) | *Extraction of lists of values* Checkbox identification * Query paraphrasing recognition to improve recognizing queries built as sentences, such as *Give me the date of the agreement* |

## Legal notices

The data classification of inputs and outputs are as set forth in the following table.

| Input data classification | Output data classification | Designation |
| --- | --- | --- |
| Usage Data | Customer Data | Generally available functions are Covered AI Features. Preview functions are Preview AI Features. [1] |

[1]

Represents the defined term used in the AI Terms and Acceptable Use Policy.

For additional information, refer to [Snowflake AI and ML](../../../guides-overview-ai-features.md).
