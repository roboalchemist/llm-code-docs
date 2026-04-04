# Source: https://docs.aws.amazon.com/clean-rooms/latest/userguide/llms.txt

# AWS Clean Rooms User Guide

> Provides a conceptual overview of AWS Clean Rooms and offers step-by-step instructions for creating collaborations and analyzing datasets.

- [Troubleshooting](https://docs.aws.amazon.com/clean-rooms/latest/userguide/troubleshooting.html)
- [AWS CloudFormation resources](https://docs.aws.amazon.com/clean-rooms/latest/userguide/creating-resources-with-cloudformation.html)
- [Document history](https://docs.aws.amazon.com/clean-rooms/latest/userguide/doc-history.html)
- [Glossary](https://docs.aws.amazon.com/clean-rooms/latest/userguide/glossary.html)

## [What is AWS Clean Rooms?](https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html)

### [Analysis rules](https://docs.aws.amazon.com/clean-rooms/latest/userguide/analysis-rules.html)

Learn how to use analysis rules in AWS Clean Rooms.

- [Aggregation analysis rule](https://docs.aws.amazon.com/clean-rooms/latest/userguide/analysis-rules-aggregation.html): Learn how to use the aggregation analysis rule type in AWS Clean Rooms.
- [List analysis rule](https://docs.aws.amazon.com/clean-rooms/latest/userguide/analysis-rules-list.html): Learn how to use the list analysis rule type in AWS Clean Rooms.
- [Custom analysis rule](https://docs.aws.amazon.com/clean-rooms/latest/userguide/analysis-rules-custom.html): Learn how to use the custom analysis rule type in AWS Clean Rooms.
- [ID mapping table analysis rule](https://docs.aws.amazon.com/clean-rooms/latest/userguide/analysis-rules-id-mapping-table.html): Learn how to use the ID mapping table analysis rule type in AWS Clean Rooms.

### [AWS Clean Rooms Differential Privacy](https://docs.aws.amazon.com/clean-rooms/latest/userguide/differential-privacy.html)

Learn about how AWS Clean Rooms Differential Privacy protects your data.

- [Differential privacy policy](https://docs.aws.amazon.com/clean-rooms/latest/userguide/dp-settings.html): Learn about the different controls available for your differential privacy policy.
- [SQL capabilities](https://docs.aws.amazon.com/clean-rooms/latest/userguide/dp-sql-capabilities.html): Learn about the SQL capabilities of AWS Clean Rooms Differential Privacy.
- [SQL query tips and examples](https://docs.aws.amazon.com/clean-rooms/latest/userguide/dp-query-tips-examples.html): Learn about the general-purpose query structure that AWS Clean Rooms Differential Privacy uses to protect user data.
- [Limitations](https://docs.aws.amazon.com/clean-rooms/latest/userguide/dp-limitations.html): Learn about the limitations of AWS Clean Rooms Differential Privacy.

### [AWS Clean Rooms ML](https://docs.aws.amazon.com/clean-rooms/latest/userguide/machine-learning.html)

Learn about how AWS Clean Rooms uses machine learning to create lookalike models.

### [AWS models in Clean Rooms ML](https://docs.aws.amazon.com/clean-rooms/latest/userguide/aws-models.html)

Learn the concepts and requirements for AWS ML models in Clean Rooms ML.

- [Privacy protections of AWS Clean Rooms ML](https://docs.aws.amazon.com/clean-rooms/latest/userguide/ml-privacy.html): Learn how Clean Rooms ML protects your data from user-identification attempts using differential privacy.
- [Training data requirements](https://docs.aws.amazon.com/clean-rooms/latest/userguide/ml-training-data-requirements.html): Provides information about the training data requirements to use AWS Clean Rooms ML.
- [Seed data requirements](https://docs.aws.amazon.com/clean-rooms/latest/userguide/ml-seed-data-requirements.html): Provides information about the seed data requirements to use AWS Clean Rooms ML.
- [Model metrics](https://docs.aws.amazon.com/clean-rooms/latest/userguide/ml-metrics.html): Recall and relevance are measures of how well your model performs.

### [Custom models in Clean Rooms ML](https://docs.aws.amazon.com/clean-rooms/latest/userguide/custom-models.html)

Learn the concepts and requirements for custom ML models in Clean Rooms ML.

- [Custom ML prerequisites](https://docs.aws.amazon.com/clean-rooms/latest/userguide/custom-model-prerequisites.html): Before you can perform custom ML modeling, you should consider the following:
- [ML model guidelines](https://docs.aws.amazon.com/clean-rooms/latest/userguide/custom-model-guidelines.html): This section details the guidelines that model providers should follow when creating a custom ML model algorithm for Clean Rooms ML.
- [Data inference guidelines](https://docs.aws.amazon.com/clean-rooms/latest/userguide/inference-model-guidelines.html): This section details the guidelines that model providers should follow when creating an inference algorithm for Clean Rooms ML.
- [Model logs and metrics](https://docs.aws.amazon.com/clean-rooms/latest/userguide/custom-model-logs.html): To receive logs and metrics from custom model training or inference, members must have created an ML Configuration with a valid role that provides the necessary CloudWatch permissions (see Create a service role for custom ML modeling - ML Configuration).

### [Cryptographic computing](https://docs.aws.amazon.com/clean-rooms/latest/userguide/crypto-computing.html)

Learn about Cryptographic Computing for Clean Rooms.

- [Considerations](https://docs.aws.amazon.com/clean-rooms/latest/userguide/crypto-computing-considerations.html): Learn about the tradeoffs to consider when using Cryptographic Computing for Clean Rooms.
- [Supported file and data types](https://docs.aws.amazon.com/clean-rooms/latest/userguide/crypto-computing-file-types.html): Learn about supported file types and data types in Cryptographic Computing for Clean Rooms.
- [Column names](https://docs.aws.amazon.com/clean-rooms/latest/userguide/crypto-computing-column-names.html): Learn about column names in Cryptographic Computing for Clean Rooms.
- [Column types](https://docs.aws.amazon.com/clean-rooms/latest/userguide/crypto-computing-column-types.html): Learn about column types in Cryptographic Computing for Clean Rooms.
- [Parameters](https://docs.aws.amazon.com/clean-rooms/latest/userguide/crypto-computing-parameters.html): Learn about parameters in Cryptographic Computing for Clean Rooms.
- [Optional flags](https://docs.aws.amazon.com/clean-rooms/latest/userguide/crypto-computing-optional-flags.html): Learn about optional flags in Cryptographic Computing for Clean Rooms.
- [Queries with C3R](https://docs.aws.amazon.com/clean-rooms/latest/userguide/crypto-computing-queries.html): Learn about running queries with Cryptographic Computing for Clean Rooms.
- [Guidelines](https://docs.aws.amazon.com/clean-rooms/latest/userguide/crypto-computing-guidelines.html): Learn about how to tune C3R in order to balance performance and cryptographic assurances.


## [Setting up AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/setting-up.html)

- [Sign up for AWS](https://docs.aws.amazon.com/clean-rooms/latest/userguide/setting-up-aws-sign-up.html): To use AWS Clean Rooms, you must sign up for AWS.
- [Set up service roles for AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/setting-up-roles.html): To use AWS Clean Rooms, you must set up IAM roles.
- [Set up service roles for AWS Clean Rooms ML](https://docs.aws.amazon.com/clean-rooms/latest/userguide/ml-roles.html): Learn how to set up IAM roles to use AWS Clean Rooms ML.


## [Collaborations and memberships](https://docs.aws.amazon.com/clean-rooms/latest/userguide/working-with-collaborations.html)

### [Creating a collaboration](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-collaboration.html)

Learn how to create a collaboration in AWS Clean Rooms.

- [Creating a collaboration for queries](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-collab-queries.html): Learn how to create a collaboration for queries in AWS Clean Rooms.
- [Creating a collaboration for queries and jobs](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-collab-queries-and-jobs.html): Learn how to create a collaboration for jobs in AWS Clean Rooms.
- [Creating a collaboration for ML modeling](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-collab-ml-modeling.html): Learn how to create a collaboration for machine learning modeling in AWS Clean Rooms, including setting up member abilities, configuring payment, and specifying results destinations.
- [Creating a membership and joining a collaboration](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-membership.html): Learn how to create a membership and join a collaboration in AWS Clean Rooms.
- [Editing collaborations](https://docs.aws.amazon.com/clean-rooms/latest/userguide/edit-collaboration.html): Learn how to edit various aspects of an AWS Clean Rooms collaboration, including name, description, tags, logs settings, and associated resources.
- [Change requests](https://docs.aws.amazon.com/clean-rooms/latest/userguide/change-requests.html): Learn how to use change requests to propose and approve changes to collaboration settings.
- [Deleting collaborations](https://docs.aws.amazon.com/clean-rooms/latest/userguide/delete-collaboration.html): Learn how to delete a collaboration in AWS Clean Rooms.
- [Viewing collaborations](https://docs.aws.amazon.com/clean-rooms/latest/userguide/review-collab-console.html): Learn how to view the collaborations you have created in AWS Clean Rooms.
- [Inviting members](https://docs.aws.amazon.com/clean-rooms/latest/userguide/invite-members.html): Learn how to invite members to an AWS Clean Rooms collaboration by copying and sharing an invitation link.
- [Monitoring members](https://docs.aws.amazon.com/clean-rooms/latest/userguide/monitor-status.html): Monitor collaboration members, check their status, review member abilities, and verify payment configurations using the AWS Management Console.
- [Adding members](https://docs.aws.amazon.com/clean-rooms/latest/userguide/add-member.html): Learn how to add members to an existing collaboration using the AWS Management Console.
- [Removing members](https://docs.aws.amazon.com/clean-rooms/latest/userguide/remove-member.html): Remove a member and their associated datasets from a collaboration in AWS Clean Rooms using the AWS Management Console.
- [Leaving a collaboration](https://docs.aws.amazon.com/clean-rooms/latest/userguide/leave-collab.html): Learn how to leave a collaboration in AWS Clean Rooms.


## [Data tables](https://docs.aws.amazon.com/clean-rooms/latest/userguide/working-with-data-tables.html)

- [Data formats](https://docs.aws.amazon.com/clean-rooms/latest/userguide/data-formats.html): Learn about the data formats and data types you can use for queries in AWS Clean Rooms.
- [Apache Iceberg tables](https://docs.aws.amazon.com/clean-rooms/latest/userguide/iceberg-tables.html): Learn about the Apache Iceberg table format and data types that you can use for queries in AWS Clean Rooms.

### [Preparing data tables](https://docs.aws.amazon.com/clean-rooms/latest/userguide/prepare-data.html)

Learn how to prepare data tables to be analyzed in AWS Clean Rooms.

- [Preparing data tables in Amazon S3](https://docs.aws.amazon.com/clean-rooms/latest/userguide/prepare-data-S3.html): Learn how to prepare data tables in S3 to be analyzed in AWS Clean Rooms.
- [Preparing data tables in Amazon Athena](https://docs.aws.amazon.com/clean-rooms/latest/userguide/prepare-data-athena.html): Learn how to prepare data tables in Amazon Athena to be queried in AWS Clean Rooms.
- [Preparing data tables in Snowflake](https://docs.aws.amazon.com/clean-rooms/latest/userguide/prepare-data-snowflake.html): Learn how to prepare data tables in Snowflake to be queried in AWS Clean Rooms.

### [Preparing encrypted data tables](https://docs.aws.amazon.com/clean-rooms/latest/userguide/prepare-encrypted-data.html)

Learn to encrypt data before using it in a collaboration.

- [Step 1: Complete the prerequisites](https://docs.aws.amazon.com/clean-rooms/latest/userguide/prerequisites.html): Learn how to complete the prerequisites for C3R.
- [Step 2: Download the C3R encryption client](https://docs.aws.amazon.com/clean-rooms/latest/userguide/download-client.html)
- [Step 3: (Optional) View available commands in the C3R encryption client](https://docs.aws.amazon.com/clean-rooms/latest/userguide/view-commands.html): Use this procedure to familiarize yourself with the available commands in the C3R encryption client.
- [Step 4: Generate an encryption schema for a tabular file](https://docs.aws.amazon.com/clean-rooms/latest/userguide/gen-encryption-schema-csv.html): To encrypt data, an encryption schema describing how the data will be used is required.
- [Step 5: Create a shared secret key](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-SSK.html): To encrypt the data tables, the collaboration participants must agree upon and securely share a shared secret key.
- [Step 6: Store the shared secret key in an environment variable](https://docs.aws.amazon.com/clean-rooms/latest/userguide/store-key.html): An environment variable is a convenient and extensible way for users to provide a secret key from various key stores like AWS Secrets Manager and pass it to the C3R encryption client.
- [Step 7: Encrypt data](https://docs.aws.amazon.com/clean-rooms/latest/userguide/encrypt-data.html): To perform this step, you must acquire the AWS Clean Rooms collaboration ID and the shared secret key.
- [Step 8: Verify data encryption](https://docs.aws.amazon.com/clean-rooms/latest/userguide/verify-encryption.html)
- [(Optional) Create a schema (advanced users)](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-schema.html): Creating a schema manually is for advanced users.
- [Decrypting data tables](https://docs.aws.amazon.com/clean-rooms/latest/userguide/decrypt-data.html): Learn to decrypt encrypted data tables with the C3R encryption client.


## [Configured tables](https://docs.aws.amazon.com/clean-rooms/latest/userguide/working-with-configured-tables.html)

### [Creating a configured table](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-configured-table.html)

Learn how to create a configured table in AWS Clean Rooms.

- [Amazon S3 data source](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-config-table-s3.html): Learn how to create a configured table in AWS Clean Rooms.
- [Amazon Athena data source](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-config-table-athena.html): Learn how to create a configured table in AWS Clean Rooms.
- [Snowflake data source](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-config-table-snowflake.html): Learn how to create a configured table in AWS Clean Rooms.
- [Adding an analysis rule to a configured table](https://docs.aws.amazon.com/clean-rooms/latest/userguide/add-analysis-rule.html): Learn how to add an analysis rule to a configured table.
- [Associating a configured table to a collaboration](https://docs.aws.amazon.com/clean-rooms/latest/userguide/associate-configured-table.html): Learn how to associate a configured table to a collaboration.

### [Configuring a data access budget](https://docs.aws.amazon.com/clean-rooms/latest/userguide/configure-data-access-budget.html)

Configure, view, edit, and delete data access budgets to control how many times tables can be used in AWS Clean Rooms collaborations.

- [Viewing a data access budget](https://docs.aws.amazon.com/clean-rooms/latest/userguide/view-access-budget.html): View and monitor data access budgets for tables in AWS Clean Rooms collaborations using the AWS Management Console.
- [Adding a data access budget to an existing associated table](https://docs.aws.amazon.com/clean-rooms/latest/userguide/add-access-budget-to-existing-associated-table.html): As a collaboration member, you can add a data access budget to an existing associated table.
- [Editing a data access budget](https://docs.aws.amazon.com/clean-rooms/latest/userguide/edit-access-budget.html): As a collaboration member, you can edit the data access budget.
- [Deleting a data access budget](https://docs.aws.amazon.com/clean-rooms/latest/userguide/delete-access-budget.html): You can delete a data access budget from the Tables tab or from the table details page.
- [Adding a collaboration analysis rule to a configured table](https://docs.aws.amazon.com/clean-rooms/latest/userguide/add-collaboration-analysis-rule.html): Learn how to add a collaboration analysis rule to a configured table that has been associated to a collaboration.
- [Configuring differential privacy policy (optional)](https://docs.aws.amazon.com/clean-rooms/latest/userguide/configure-differential-privacy.html): Learn how to configure differential privacy rules to protect against user re-identification attempts.
- [Viewing tables and analysis rules](https://docs.aws.amazon.com/clean-rooms/latest/userguide/view-tables.html): View and manage tables associated with collaborations, including table details and analysis rules in AWS Clean Rooms.
- [Editing a configured table](https://docs.aws.amazon.com/clean-rooms/latest/userguide/edit-configured-table.html): Learn how to edit the name, description, and configuration details of tables in AWS Clean Rooms for Amazon S3, Amazon Athena, and Snowflake data sources.
- [Editing configured table tags](https://docs.aws.amazon.com/clean-rooms/latest/userguide/edit-config-table-tags.html): Learn how to add, remove, and manage resource tags for configured tables in AWS Clean Rooms.
- [Editing the configured table analysis rule](https://docs.aws.amazon.com/clean-rooms/latest/userguide/edit-config-table-analysis-rule.html): Learn how to edit table analysis rules by modifying rule definitions, previewing collaboration members, and importing rule definitions in AWS Clean Rooms.
- [Deleting the configured table analysis rule](https://docs.aws.amazon.com/clean-rooms/latest/userguide/delete-config-table-analysis-rule.html): Learn how to delete a configured table analysis rule and understand the impact on related resources in your AWS Clean Rooms collaboration.
- [Configured table disallowed columns](https://docs.aws.amazon.com/clean-rooms/latest/userguide/disallowed-columns.html): Learn how to configure disallowed output columns in AWS Clean Rooms custom analysis rules to control which table columns can appear in query results.
- [Editing configured table associations](https://docs.aws.amazon.com/clean-rooms/latest/userguide/edit-config-table-assoc.html): Edit table association details, including descriptions and service access information, for tables that you have configured in AWS Clean Rooms collaborations.
- [Disassociating configured tables](https://docs.aws.amazon.com/clean-rooms/latest/userguide/disassociate-config-table.html): Learn how to disassociate a configured table from a collaboration to remove query permissions for collaboration members.


## [AWS Entity Resolution in AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/working-with-entity-resolution.html)

### [ID namespaces](https://docs.aws.amazon.com/clean-rooms/latest/userguide/working-with-id-namespaces.html)

Learn to create and manage an ID namespace in AWS Clean Rooms.

- [Creating and associating a new ID namespace](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-new-id-namespace.html): Learn how to create and associate a new ID namespace in AWS Clean Rooms.
- [Associating an existing ID namespace](https://docs.aws.amazon.com/clean-rooms/latest/userguide/associate-existing-id-namespace.html): Learn how to associate an existing ID namespace in AWS Clean Rooms.
- [Editing ID namespace associations](https://docs.aws.amazon.com/clean-rooms/latest/userguide/edit-id-namespace-association.html): Edit ID namespace associations in AWS Clean Rooms to modify association details and configure ID mapping table protections for collaboration members.
- [Disassociating ID namespace associations](https://docs.aws.amazon.com/clean-rooms/latest/userguide/disassociate-id-namespace-association.html): Learn how to disassociate ID namespace associations from an AWS Clean Rooms collaboration and understand the impact on ID mapping tables and query capabilities.

### [ID mapping tables](https://docs.aws.amazon.com/clean-rooms/latest/userguide/working-with-id-mapping-tables.html)

Learn to create and manage an ID mapping table in AWS Clean Rooms.

- [Creating and populating a new ID mapping table](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-id-mapping-table.html): Learn how to create and populate a new ID mapping table in AWS Clean Rooms.
- [Populating an existing ID mapping table](https://docs.aws.amazon.com/clean-rooms/latest/userguide/populate-id-mapping-table.html): Learn how to populate an existing ID mapping table in AWS Clean Rooms.
- [Editing an ID mapping table](https://docs.aws.amazon.com/clean-rooms/latest/userguide/edit-id-mapping-table.html): As a collaboration member, you can edit the ID mapping table that you have created.
- [Deleting an ID mapping table](https://docs.aws.amazon.com/clean-rooms/latest/userguide/delete-id-mapping-table.html): As a collaboration member, you can delete an ID mapping table that you have created.


## [Analysis templates](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-analysis-template.html)

### [SQL analysis templates](https://docs.aws.amazon.com/clean-rooms/latest/userguide/sql-analysis-templates.html)

Learn to create a SQL analysis template in AWS Clean Rooms.

- [Creating a SQL analysis template](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-sql-analysis-template.html): Learn to create a SQL analysis template in AWS Clean Rooms.
- [Reviewing a SQL analysis template](https://docs.aws.amazon.com/clean-rooms/latest/userguide/review-analysis-template.html): Learn how to review a SQL analysis template in AWS Clean Rooms.

### [PySpark analysis templates](https://docs.aws.amazon.com/clean-rooms/latest/userguide/pyspark-analysis-templates.html)

Learn to create a PySpark analysis template in AWS Clean Rooms.

- [Creating a user script](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-user-script.html): Learn to create a PySpark analysis template in AWS Clean Rooms.
- [Working with parameters in PySpark analysis templates](https://docs.aws.amazon.com/clean-rooms/latest/userguide/pyspark-parameter-handling.html): Learn how to safely access and use parameters in your PySpark user scripts.
- [Creating a virtual environment (optional)](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-virtual-environment.html): Learn to create a virtual environment in AWS Clean Rooms.
- [Storing a user script and virtual environment in S3](https://docs.aws.amazon.com/clean-rooms/latest/userguide/store-artifacts-in-s3.html): Learn to store a user script and virtual environment in Amazon S3.
- [Creating a PySpark analysis template](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-pyspark-analysis-template.html): Learn to create a PySpark analysis template in AWS Clean Rooms.
- [Reviewing a PySpark analysis template](https://docs.aws.amazon.com/clean-rooms/latest/userguide/review-pyspark-analysis-template.html): Learn how to review a PySpark analysis template in AWS Clean Rooms.
- [Troubleshooting PySpark analysis templates](https://docs.aws.amazon.com/clean-rooms/latest/userguide/troubleshooting-pyspark-analysis-templates.html): This topic helps you resolve common issues when running PySpark analysis templates in AWS Clean Rooms.


## [Analysis](https://docs.aws.amazon.com/clean-rooms/latest/userguide/analyze-data.html)

### [Running SQL queries](https://docs.aws.amazon.com/clean-rooms/latest/userguide/running-sql-queries.html)

Learn how to query data in an AWS Clean Rooms collaboration.

- [Querying configured tables](https://docs.aws.amazon.com/clean-rooms/latest/userguide/use-sql-editor.html): Learn how to query configured tables using the SQL code editor in AWS Clean Rooms.
- [Querying ID mapping tables](https://docs.aws.amazon.com/clean-rooms/latest/userguide/query-id-mapping-tables.html): Learn how to query configured tables using the SQL code editor in AWS Clean Rooms.
- [Querying configured tables using an analysis template](https://docs.aws.amazon.com/clean-rooms/latest/userguide/use-analysis-template.html): Learn how to query configured tables using an analysis template.
- [Querying with the analysis builder](https://docs.aws.amazon.com/clean-rooms/latest/userguide/query-data-analysis-builder.html): Learn how to query configured tables using the analysis builder in AWS Clean Rooms.
- [Viewing the impact of differential privacy](https://docs.aws.amazon.com/clean-rooms/latest/userguide/query-data-with-diff-privacy.html): Learn how to view the impact of differential privacy when it's turned on in AWS Clean Rooms.
- [Viewing recent queries](https://docs.aws.amazon.com/clean-rooms/latest/userguide/view-queries-console.html): Learn how to view recent queries in AWS Clean Rooms.
- [Viewing query details](https://docs.aws.amazon.com/clean-rooms/latest/userguide/view-query-details.html): Learn how to view query details in AWS Clean Rooms.

### [Running PySpark jobs](https://docs.aws.amazon.com/clean-rooms/latest/userguide/run-jobs.html)

Learn how to run PySpark jobs in an AWS Clean Rooms collaboration.

- [Running a job using an analysis template](https://docs.aws.amazon.com/clean-rooms/latest/userguide/run-jobs-with-analysis-template.html): Learn how to query configured tables using an analysis template.
- [Viewing recent jobs](https://docs.aws.amazon.com/clean-rooms/latest/userguide/view-recent-jobs.html): Learn how to view recent jobs in AWS Clean Rooms.
- [Viewing job details](https://docs.aws.amazon.com/clean-rooms/latest/userguide/view-job-details.html): Learn how to view job details in AWS Clean Rooms.


## [Analysis results](https://docs.aws.amazon.com/clean-rooms/latest/userguide/receive-query-results.html)

- [Receiving query results](https://docs.aws.amazon.com/clean-rooms/latest/userguide/receive-results.html): Learn how to receive query results in AWS Clean Rooms.
- [Receiving job results](https://docs.aws.amazon.com/clean-rooms/latest/userguide/receive-job-results.html): Learn how to receive query results in AWS Clean Rooms.
- [Editing default values for query results settings](https://docs.aws.amazon.com/clean-rooms/latest/userguide/edit-query-results-settings.html): Learn how to edit the default values for query results settings in AWS Clean Rooms.
- [Editing default values for job results settings](https://docs.aws.amazon.com/clean-rooms/latest/userguide/edit-job-results-settings.html): Learn how to edit the default values for job results settings in AWS Clean Rooms.
- [Using query output in other AWS services](https://docs.aws.amazon.com/clean-rooms/latest/userguide/using-query-output.html): Learn how to use query output in other AWS services.


## [Custom modeling](https://docs.aws.amazon.com/clean-rooms/latest/userguide/working-with-custom-models.html)

### [Privacy-enhanced synthetic dataset generation](https://docs.aws.amazon.com/clean-rooms/latest/userguide/synthetic-data-generation.html)

Learn how to generate synthetic data in AWS Clean Rooms.

- [Considerations for synthetic data generation](https://docs.aws.amazon.com/clean-rooms/latest/userguide/considerations-for-data-generation.html): Learn to create a SQL analysis template in AWS Clean Rooms.
- [Creating and joining the collaboration](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-custom-ml-collaboration.html): Learn how collaboration creators and invited members set up roles, permissions, and ML configurations in AWS Clean Rooms to enable secure data collaboration and model training.
- [Contributing training data](https://docs.aws.amazon.com/clean-rooms/latest/userguide/custom-model-training-data.html): Learn how to contribute training data to an AWS Clean Rooms ML collaboration by configuring tables, setting up analysis rules, and managing data access permissions.
- [Configuring a model algorithm](https://docs.aws.amazon.com/clean-rooms/latest/userguide/configure-model-algorithm.html): Configure a custom machine learning model algorithm in AWS Clean Rooms by specifying training and inference image containers from Amazon ECR repositories.
- [Associating the configured model algorithm](https://docs.aws.amazon.com/clean-rooms/latest/userguide/associate-model-algorithm.html): Associate a configured model algorithm with a collaboration in AWS Clean Rooms to make it available to collaboration members.
- [Creating an ML input channel](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-ml-input-channel.html): Create an ML input channel in AWS Clean Rooms to prepare data streams for machine learning model training and inference using SQL queries or analysis templates.

### [Creating a trained model](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-trained-model.html)

Create a trained model in AWS Clean Rooms ML to enable collaboration members to jointly analyze their data using machine learning algorithms.

- [Using incremental training](https://docs.aws.amazon.com/clean-rooms/latest/userguide/use-incremental-training.html): Learn how to use incremental training in AWS Clean Rooms ML to create new models from existing model artifacts and updated datasets, saving time and resources.
- [Using distributed training](https://docs.aws.amazon.com/clean-rooms/latest/userguide/use-distributed-training.html): Learn how to use distributed training in AWS Clean Rooms ML to train models across many computing nodes, configure training modes, and distribute data across instances.
- [Exporting model artifacts](https://docs.aws.amazon.com/clean-rooms/latest/userguide/export-model-artifacts.html): Export trained model artifacts to collaboration members in AWS Clean Rooms ML and configure who can receive model output after training completion.
- [Running inference on a trained model](https://docs.aws.amazon.com/clean-rooms/latest/userguide/run-inference-jobs.html): Create and run inference jobs with trained models in AWS Clean Rooms ML to generate predictions using your collaboration data.


## [ML modeling for training data providers](https://docs.aws.amazon.com/clean-rooms/latest/userguide/working-with-machine-learning-tdp.html)

- [Importing training data](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-ml-model-training-data.html)
- [Creating a lookalike model](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-ml-model-create-model.html): After you have created a training dataset, you are ready to create a lookalike model.
- [Configuring a lookalike model](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-ml-model-configure-model.html): After you have created a lookalike model, you are ready to configure it for use in a collaboration.
- [Associating a configured lookalike model](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-ml-model-associate-model.html): After you have configured a lookalike model, you can associate it to a collaboration.
- [Updating a configured lookalike model](https://docs.aws.amazon.com/clean-rooms/latest/userguide/update-ml-model-configured-model.html): After you have associated a configured a lookalike model, you can update it to change information such as the name, metrics to share, or output Amazon S3 location.


## [ML modeling for seed data providers](https://docs.aws.amazon.com/clean-rooms/latest/userguide/working-with-machine-learning-sdp.html)

- [Creating a lookalike segment](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-ml-segment-create.html)
- [Exporting a lookalike segment](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-ml-segment-export.html): After you have created a lookalike segment, you can export that data to an Amazon S3 bucket.


## [Security](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/clean-rooms/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS Clean Rooms.
- [Using service-linked roles](https://docs.aws.amazon.com/clean-rooms/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give AWS Clean Rooms access to resources in your AWS account.
- [Data retention](https://docs.aws.amazon.com/clean-rooms/latest/userguide/data-retention.html): Learn how AWS Clean Rooms and AWS Clean Rooms ML handles data retention.
- [Best practices](https://docs.aws.amazon.com/clean-rooms/latest/userguide/best-practices.html): Learn about the best practices for conducting data collaborations in AWS Clean Rooms.

### [Identity and Access Management](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html)

Learn how to authenticate requests and manage access to your AWS Clean Rooms resources.

- [How AWS Clean Rooms works with IAM](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security_iam_service-with-iam.html): Learn how AWS Clean Rooms works with IAM to protect your data.
- [Identity-based policy examples](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security_iam_id-based-policy-examples.html): Learn how AWS Clean Rooms uses identity-based policies to grant users permission to perform actions.
- [AWS managed policies](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS Clean Rooms and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security_iam_troubleshoot.html): Learn how to troubleshoot certain identity and access issues in AWS Clean Rooms.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/clean-rooms/latest/userguide/cross-service-confused-deputy-prevention.html): Learn how AWSÂ Clean Rooms handles the cross-service confused deputy problem.
- [IAM behaviors for AWS Clean Rooms ML](https://docs.aws.amazon.com/clean-rooms/latest/userguide/ml-behaviors.html): Learn about how AWS Clean Rooms ML handles cross-account jobs, logs, and collaborations.
- [IAM behaviors for Clean Rooms ML Custom Models](https://docs.aws.amazon.com/clean-rooms/latest/userguide/ml-behaviors-byom.html): Learn about how AWS Clean Rooms ML Custom Models handles cross-account jobs.
- [Compliance validation](https://docs.aws.amazon.com/clean-rooms/latest/userguide/SERVICE-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/clean-rooms/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Clean Rooms features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/clean-rooms/latest/userguide/infrastructure-security.html): Learn how AWS Clean Rooms isolates service traffic.
- [AWS PrivateLink](https://docs.aws.amazon.com/clean-rooms/latest/userguide/vpc-interface-endpoints.html): You can use AWS PrivateLink to create a private connection between your VPC and AWS Clean Rooms or AWS Clean Rooms ML.


## [Monitoring](https://docs.aws.amazon.com/clean-rooms/latest/userguide/monitoring-overview.html)

### [Analysis logging in AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/query-logs.html)

Learn how to create, store, and monitor query and job logs in AWS Clean Rooms to verify analysis compliance and support auditing requirements.

- [Receive query and job logs](https://docs.aws.amazon.com/clean-rooms/latest/userguide/receiving-query-logs.html): Learn how AWS Clean Rooms automatically creates and manages query and job logs for collaboration members, including log delivery rules and troubleshooting information.
- [Recommended actions for query and job logs](https://docs.aws.amazon.com/clean-rooms/latest/userguide/using-query-logs.html): Learn how to monitor and verify queries, jobs, and table configurations in your collaboration to ensure compliance with agreed-upon use cases.
- [Detailed monitoring with CloudWatch in AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/cloudwatch-metrics.html): CloudWatch is a monitoring and observability service.
- [CloudTrail logs](https://docs.aws.amazon.com/clean-rooms/latest/userguide/logging-using-cloudtrail.html): Learn about logging AWS Clean Rooms with AWS CloudTrail.

### [Integrating AWS Clean Rooms into EDAs](https://docs.aws.amazon.com/clean-rooms/latest/userguide/eventbridge-integration-full.html)

Receive notifications when specific AWS Clean Rooms events such as object creation or deletion occur in an AWS Clean Rooms with EventBridge.

- [Events detail reference](https://docs.aws.amazon.com/clean-rooms/latest/userguide/events-detail-reference-full.html): All events from AWS services have a common set of fields containing metadata about the event, such as the AWS service that is the source of the event, the time the event was generated, the account and region in which the event took place, and others.
- [Cost Allocation Tagging](https://docs.aws.amazon.com/clean-rooms/latest/userguide/cost-allocation-tagging.html): AWS Clean Rooms supports using Cost Allocation Tags to track your AWS costs.


## [Quotas](https://docs.aws.amazon.com/clean-rooms/latest/userguide/quotas.html)

- [AWS Clean Rooms quotas](https://docs.aws.amazon.com/clean-rooms/latest/userguide/clean-rooms-quotas.html): Learn about AWS Clean Rooms service quotas, including limits on collaborations, configured tables, queries, and API request rates.
- [AWS Clean Rooms ML quotas](https://docs.aws.amazon.com/clean-rooms/latest/userguide/clean-rooms-ml-quotas.html): Learn about the service quotas and limits for Clean Rooms ML, including dataset constraints, API throttling rates, and maximum durations for various operations.
