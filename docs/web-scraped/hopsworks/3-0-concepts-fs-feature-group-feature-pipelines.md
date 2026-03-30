# Source: https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/

Title: Feature Pipelines - Hopsworks Documentation

URL Source: https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/

Published Time: Thu, 12 Mar 2026 10:23:35 GMT

Markdown Content:
Feature Pipelines - Hopsworks Documentation
===============

- [x] - [x]

[Skip to content](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#data-sources)

[![Image 1: logo](https://docs.hopsworks.ai/3.0/assets/images/hops-logo.png)](https://docs.hopsworks.ai/3.0/ "Hopsworks Documentation")

 Hopsworks Documentation

 Feature Pipelines

 Initializing search

[logicalclocks/hopsworks](https://github.com/logicalclocks/hopsworks "Go to repository")

- [Home](https://docs.hopsworks.ai/3.0/)
- [Getting Started ↗](https://colab.research.google.com/github/logicalclocks/hopsworks-tutorials/blob/master/quickstart.ipynb)
- [Tutorials](https://docs.hopsworks.ai/3.0/tutorials/)
- [Concepts](https://docs.hopsworks.ai/3.0/concepts/hopsworks/)
- [Guides](https://docs.hopsworks.ai/3.0/user_guides/)
- [Setup and Installation](https://docs.hopsworks.ai/3.0/setup_installation/)
- [Administration](https://docs.hopsworks.ai/3.0/admin/)
- [API [Hopsworks API](https://docs.hopsworks.ai/hopsworks-api/dev)[Feature Store API](https://docs.hopsworks.ai/feature-store-api/dev)[MLOps API](https://docs.hopsworks.ai/machine-learning-api/dev)](https://docs.hopsworks.ai/)
- [Community ↗](https://community.hopsworks.ai/)

[![Image 2: logo](https://docs.hopsworks.ai/3.0/assets/images/hops-logo.png)](https://docs.hopsworks.ai/3.0/ "Hopsworks Documentation") Hopsworks Documentation  

[logicalclocks/hopsworks](https://github.com/logicalclocks/hopsworks "Go to repository")

- [Home](https://docs.hopsworks.ai/3.0/)
- [Getting Started ↗](https://colab.research.google.com/github/logicalclocks/hopsworks-tutorials/blob/master/quickstart.ipynb)
- - [x] [Tutorials](https://docs.hopsworks.ai/3.0/tutorials/)  Tutorials  

- - [x]  Concepts   Concepts  
  - [Hopsworks Platform](https://docs.hopsworks.ai/3.0/concepts/hopsworks/)
  - [MLOps Dictionary ↗](https://www.hopsworks.ai/mlops-dictionary?utm_source=web&utm_medium=docs)
  - - [x] [Feature Store](https://docs.hopsworks.ai/3.0/concepts/fs/)  Feature Store  
    - - [x]  Feature Groups   Feature Groups  
      - [Overview](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/fg_overview/)
      - [Write APIs](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/write_apis/)
      - - [x]  Feature Pipelines  [Feature Pipelines](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/) Table of contents  
        - [Data Sources](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#data-sources)
        - [Data Validation](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#data-validation)
        - [Aggregations](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#aggregations)
        - [Dimensionality Reduction](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#dimensionality-reduction)
        - [Transformations](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#transformations)
        - [Feature Engineering in Python](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#feature-engineering-in-python)
        - [Feature Engineering in Spark/PySpark](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#feature-engineering-in-sparkpyspark)
        - [Feature Engineering in SQL](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#feature-engineering-in-sql)
        - [Feature Engineering in Flink](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#feature-engineering-in-flink)

      - [External Feature Groups](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/external_fg/)
      - [Data Validation/Stats/Alerts](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/fg_statistics/)
      - [Versioning](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/versioning/)

    - - [x]  Feature Views   Feature Views  
      - [Overview](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/fv_overview/)
      - [Offline API](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/)
      - [Online API](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/online_api/)
      - [Consistent Transformations](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/)
      - [Statistics](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/statistics/)
      - [Versioning](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/versioning/)

  - - [x]  Projects   Projects  
    - [Governance](https://docs.hopsworks.ai/3.0/concepts/projects/governance/)
    - [Data Storage/Sharing](https://docs.hopsworks.ai/3.0/concepts/projects/storage/)
    - [Tags/Search/Lineage](https://docs.hopsworks.ai/3.0/concepts/projects/search/)
    - [CI/CD](https://docs.hopsworks.ai/3.0/concepts/projects/cicd/)

  - - [x]  MLOps   MLOps  
    - [Prediction Services](https://docs.hopsworks.ai/3.0/concepts/mlops/prediction_services/)
    - [Model Training](https://docs.hopsworks.ai/3.0/concepts/mlops/training/)
    - [Model Registry](https://docs.hopsworks.ai/3.0/concepts/mlops/registry/)
    - [Model Serving](https://docs.hopsworks.ai/3.0/concepts/mlops/kserve/)
    - [Vector Database](https://docs.hopsworks.ai/3.0/concepts/mlops/opensearch/)
    - [BI Tools](https://docs.hopsworks.ai/3.0/concepts/mlops/bi_tools/)

  - - [x]  Development   Development  
    - [Outside Hopsworks](https://docs.hopsworks.ai/3.0/concepts/dev/outside/)
    - [Inside Hopsworks](https://docs.hopsworks.ai/3.0/concepts/dev/inside/)

- - [x] [Guides](https://docs.hopsworks.ai/3.0/user_guides/)  Guides  
  - - [x] [Feature Store](https://docs.hopsworks.ai/3.0/user_guides/fs/)  Feature Store  
    - - [x] [Storage Connector](https://docs.hopsworks.ai/3.0/user_guides/fs/storage_connector/)  Storage Connector  
      - - [x]  Configuration and Creation   Configuration and Creation  
        - [JDBC](https://docs.hopsworks.ai/3.0/user_guides/fs/storage_connector/creation/jdbc/)
        - [Snowflake](https://docs.hopsworks.ai/3.0/user_guides/fs/storage_connector/creation/snowflake/)
        - [Kafka](https://docs.hopsworks.ai/3.0/user_guides/fs/storage_connector/creation/kafka/)
        - [HopsFS](https://docs.hopsworks.ai/3.0/user_guides/fs/storage_connector/creation/hopsfs/)
        - [S3](https://docs.hopsworks.ai/3.0/user_guides/fs/storage_connector/creation/s3/)
        - [Redshift](https://docs.hopsworks.ai/3.0/user_guides/fs/storage_connector/creation/redshift/)
        - [ADLS](https://docs.hopsworks.ai/3.0/user_guides/fs/storage_connector/creation/adls/)
        - [BigQuery](https://docs.hopsworks.ai/3.0/user_guides/fs/storage_connector/creation/bigquery/)
        - [GCS](https://docs.hopsworks.ai/3.0/user_guides/fs/storage_connector/creation/gcs/)

      - [Usage](https://docs.hopsworks.ai/3.0/user_guides/fs/storage_connector/usage/)

    - - [x] [Feature Group](https://docs.hopsworks.ai/3.0/user_guides/fs/feature_group/)  Feature Group  
      - [Create](https://docs.hopsworks.ai/3.0/user_guides/fs/feature_group/create/)
      - [Create External](https://docs.hopsworks.ai/3.0/user_guides/fs/feature_group/create_external/)
      - [Data Types and Schema management](https://docs.hopsworks.ai/3.0/user_guides/fs/feature_group/data_types/)
      - [Statistics](https://docs.hopsworks.ai/3.0/user_guides/fs/feature_group/statistics/)
      - [Data Validation](https://docs.hopsworks.ai/3.0/user_guides/fs/feature_group/data_validation/)

    - - [x] [Feature View](https://docs.hopsworks.ai/3.0/user_guides/fs/feature_view/)  Feature View  
      - [Feature View](https://docs.hopsworks.ai/3.0/user_guides/fs/feature_view/overview/)
      - [Training data](https://docs.hopsworks.ai/3.0/user_guides/fs/feature_view/training-data/)
      - [Batch data](https://docs.hopsworks.ai/3.0/user_guides/fs/feature_view/batch-data/)
      - [Feature vectors](https://docs.hopsworks.ai/3.0/user_guides/fs/feature_view/feature-vectors/)
      - [Query](https://docs.hopsworks.ai/3.0/user_guides/fs/feature_view/query/)
      - [Transformation Functions](https://docs.hopsworks.ai/3.0/user_guides/fs/feature_view/transformation-function/)

    - [Compute Engines](https://docs.hopsworks.ai/3.0/user_guides/fs/compute_engines/)
    - - [x] [Client Integrations](https://docs.hopsworks.ai/3.0/user_guides/integrations/)  Client Integrations  
      - [Python](https://docs.hopsworks.ai/3.0/user_guides/integrations/python/)
      - - [x]  Databricks   Databricks  
        - [Networking](https://docs.hopsworks.ai/3.0/user_guides/integrations/databricks/networking/)
        - [Hopsworks API Key](https://docs.hopsworks.ai/3.0/user_guides/integrations/databricks/api_key/)
        - [Configuration](https://docs.hopsworks.ai/3.0/user_guides/integrations/databricks/configuration/)

      - [AWS Sagemaker](https://docs.hopsworks.ai/3.0/user_guides/integrations/sagemaker/)
      - - [x]  AWS EMR   AWS EMR  
        - [Networking](https://docs.hopsworks.ai/3.0/user_guides/integrations/emr/networking/)
        - [Configure EMR for the Hopsworks Feature Store](https://docs.hopsworks.ai/3.0/user_guides/integrations/emr/emr_configuration/)

      - [Azure HDInsight](https://docs.hopsworks.ai/3.0/user_guides/integrations/hdinsight/)
      - - [x]  Azure Machine Learning   Azure Machine Learning  
        - [Designer](https://docs.hopsworks.ai/3.0/user_guides/integrations/mlstudio_designer/)
        - [Notebooks](https://docs.hopsworks.ai/3.0/user_guides/integrations/mlstudio_notebooks/)

      - [Apache Spark](https://docs.hopsworks.ai/3.0/user_guides/integrations/spark/)

    - [Sharing](https://docs.hopsworks.ai/3.0/user_guides/fs/sharing/sharing/)
    - [Tags](https://docs.hopsworks.ai/3.0/user_guides/fs/tags/tags/)

  - - [x] [Projects](https://docs.hopsworks.ai/3.0/user_guides/projects/)  Projects  
    - - [x]  Authentication   Authentication  
      - [Registration](https://docs.hopsworks.ai/3.0/user_guides/projects/auth/registration/)
      - [Login](https://docs.hopsworks.ai/3.0/user_guides/projects/auth/login/)
      - [Password Recovery](https://docs.hopsworks.ai/3.0/user_guides/projects/auth/recovery/)
      - [OAuth2 Authentication](https://docs.hopsworks.ai/3.0/user_guides/projects/auth/oauth/)
      - [LDAP Authentication](https://docs.hopsworks.ai/3.0/user_guides/projects/auth/ldap/)
      - [Kerberos Authentication](https://docs.hopsworks.ai/3.0/user_guides/projects/auth/krb/)
      - [Update Profile](https://docs.hopsworks.ai/3.0/user_guides/projects/auth/profile/)

    - - [x]  Projects   Projects  
      - [Create Project](https://docs.hopsworks.ai/3.0/user_guides/projects/project/create_project/)
      - [Add Members](https://docs.hopsworks.ai/3.0/user_guides/projects/project/add_members/)

    - - [x]  Python   Python  
      - [Install Library](https://docs.hopsworks.ai/3.0/user_guides/projects/python/python_install/)
      - [Export environment](https://docs.hopsworks.ai/3.0/user_guides/projects/python/python_env_export/)
      - [Recreate environment](https://docs.hopsworks.ai/3.0/user_guides/projects/python/python_env_recreate/)

    - - [x]  Jupyter   Jupyter  
      - [Run Spark Notebook](https://docs.hopsworks.ai/3.0/user_guides/projects/jupyter/spark_notebook/)
      - [Run Python Notebook](https://docs.hopsworks.ai/3.0/user_guides/projects/jupyter/python_notebook/)

    - - [x]  Jobs   Jobs  
      - [Run PySpark Job](https://docs.hopsworks.ai/3.0/user_guides/projects/jobs/pyspark_job/)
      - [Run Spark Job](https://docs.hopsworks.ai/3.0/user_guides/projects/jobs/spark_job/)
      - [Run Python Job](https://docs.hopsworks.ai/3.0/user_guides/projects/jobs/python_job/)

    - - [x]  OpenSearch   OpenSearch  
      - [Connect](https://docs.hopsworks.ai/3.0/user_guides/projects/opensearch/connect/)

    - - [x]  Kafka   Kafka  
      - [Create Schema](https://docs.hopsworks.ai/3.0/user_guides/projects/kafka/create_schema/)
      - [Create Topic](https://docs.hopsworks.ai/3.0/user_guides/projects/kafka/create_topic/)
      - [Produce messages](https://docs.hopsworks.ai/3.0/user_guides/projects/kafka/produce_messages/)
      - [Consume messages](https://docs.hopsworks.ai/3.0/user_guides/projects/kafka/consume_messages/)

    - - [x]  Git   Git  
      - [Configure Git Provider](https://docs.hopsworks.ai/3.0/user_guides/projects/git/configure_git_provider/)
      - [Clone Repository](https://docs.hopsworks.ai/3.0/user_guides/projects/git/clone_repo/)

    - - [x]  Secrets   Secrets  
      - [Create Secret](https://docs.hopsworks.ai/3.0/user_guides/projects/secrets/create_secret/)

    - - [x]  Api Keys   Api Keys  
      - [Create API Key](https://docs.hopsworks.ai/3.0/user_guides/projects/api_key/create_api_key/)

    - [AWS IAM Roles](https://docs.hopsworks.ai/3.0/user_guides/projects/iam_role/iam_role_chaining/)

  - - [x] [MLOps](https://docs.hopsworks.ai/3.0/user_guides/mlops/)  MLOps  
    - - [x] [Model Registry](https://docs.hopsworks.ai/3.0/user_guides/mlops/registry/)  Model Registry  
      - - [x]  Frameworks   Frameworks  
        - [TensorFlow](https://docs.hopsworks.ai/3.0/user_guides/mlops/registry/frameworks/tf/)
        - [Scikit-learn](https://docs.hopsworks.ai/3.0/user_guides/mlops/registry/frameworks/skl/)
        - [Python](https://docs.hopsworks.ai/3.0/user_guides/mlops/registry/frameworks/python/)

      - [Model Schema](https://docs.hopsworks.ai/3.0/user_guides/mlops/registry/model_schema/)
      - [Input Example](https://docs.hopsworks.ai/3.0/user_guides/mlops/registry/input_example/)

    - - [x] [Model Serving](https://docs.hopsworks.ai/3.0/user_guides/mlops/serving/)  Model Serving  
      - [Deployment](https://docs.hopsworks.ai/3.0/user_guides/mlops/serving/deployment/)
      - [Predictor](https://docs.hopsworks.ai/3.0/user_guides/mlops/serving/predictor/)
      - [Transformer](https://docs.hopsworks.ai/3.0/user_guides/mlops/serving/transformer/)
      - [Resource Allocation](https://docs.hopsworks.ai/3.0/user_guides/mlops/serving/resources/)
      - [Inference Logger](https://docs.hopsworks.ai/3.0/user_guides/mlops/serving/inference-logger/)
      - [Inference Batcher](https://docs.hopsworks.ai/3.0/user_guides/mlops/serving/inference-batcher/)

    - [Vector Database](https://docs.hopsworks.ai/3.0/user_guides/mlops/vector_database/)

  - - [x]  Migration   Migration  
    - [3.0](https://docs.hopsworks.ai/3.0/user_guides/migration/30_migration/)

- - [x] [Setup and Installation](https://docs.hopsworks.ai/3.0/setup_installation/)  Setup and Installation  
  - - [x] [Client Installation](https://docs.hopsworks.ai/3.0/user_guides/client_installation/)  Client Installation  

  - - [x]  AWS   AWS  
    - [Getting Started](https://docs.hopsworks.ai/3.0/setup_installation/aws/getting_started/)
    - [Cluster Creation](https://docs.hopsworks.ai/3.0/setup_installation/aws/cluster_creation/)
    - [EKS/ECR integration](https://docs.hopsworks.ai/3.0/setup_installation/aws/eks_ecr_integration/)
    - [Limiting Permissions](https://docs.hopsworks.ai/3.0/setup_installation/aws/restrictive_permissions/)
    - - [x]  Cluster upgrade   Cluster upgrade  
      - [Version 2.4 or newer](https://docs.hopsworks.ai/3.0/setup_installation/aws/upgrade_2.4/)
      - [Version 2.2 or older](https://docs.hopsworks.ai/3.0/setup_installation/aws/upgrade/)

    - [Troubleshooting](https://docs.hopsworks.ai/3.0/setup_installation/aws/troubleshooting/)

  - - [x]  Azure   Azure  
    - [Getting Started](https://docs.hopsworks.ai/3.0/setup_installation/azure/getting_started/)
    - [Cluster Creation](https://docs.hopsworks.ai/3.0/setup_installation/azure/cluster_creation/)
    - [AKS/ACR integration](https://docs.hopsworks.ai/3.0/setup_installation/azure/aks_acr_integration/)
    - [Limiting Permissions](https://docs.hopsworks.ai/3.0/setup_installation/azure/restrictive_permissions/)
    - - [x]  Cluster upgrade   Cluster upgrade  
      - [Version 2.4 or newer](https://docs.hopsworks.ai/3.0/setup_installation/azure/upgrade_2.4/)
      - [Version 2.2 or older](https://docs.hopsworks.ai/3.0/setup_installation/azure/upgrade/)

  - - [x]  GCP   GCP  
    - [Getting Started](https://docs.hopsworks.ai/3.0/setup_installation/gcp/getting_started/)
    - [Cluster Creation](https://docs.hopsworks.ai/3.0/setup_installation/gcp/cluster_creation/)
    - [Limiting Permissions](https://docs.hopsworks.ai/3.0/setup_installation/gcp/restrictive_permissions/)

  - - [x]  Common   Common  
    - [The dashboard](https://docs.hopsworks.ai/3.0/setup_installation/common/dashboard/)
    - [Settings](https://docs.hopsworks.ai/3.0/setup_installation/common/settings/)
    - [Services](https://docs.hopsworks.ai/3.0/setup_installation/common/services/)
    - [Adding and Removing workers](https://docs.hopsworks.ai/3.0/setup_installation/common/adding_removing_workers/)
    - [Autoscaling](https://docs.hopsworks.ai/3.0/setup_installation/common/autoscaling/)
    - [Backup](https://docs.hopsworks.ai/3.0/setup_installation/common/backup/)
    - [Scaling up](https://docs.hopsworks.ai/3.0/setup_installation/common/scalingup/)
    - [GPU support](https://docs.hopsworks.ai/3.0/setup_installation/common/gpu_support/)
    - [User management](https://docs.hopsworks.ai/3.0/setup_installation/common/user_management/)
    - [Managed RonDB](https://docs.hopsworks.ai/3.0/setup_installation/common/rondb/)
    - - [x]  Single Sign On   Single Sign On  
      - - [x]  Hopsworks   Hopsworks  
        - [OAuth2](https://docs.hopsworks.ai/3.0/setup_installation/common/sso/oauth/)
        - [LDAP](https://docs.hopsworks.ai/3.0/setup_installation/common/sso/ldap/)

    - [API Key](https://docs.hopsworks.ai/3.0/setup_installation/common/api_key/)
    - [Terraform](https://docs.hopsworks.ai/3.0/setup_installation/common/terraform/)

  - - [x]  On-Prem   On-Prem  
    - [Hopsworks Installer](https://docs.hopsworks.ai/3.0/setup_installation/on_prem/hopsworks_installer/)

- - [x] [Administration](https://docs.hopsworks.ai/3.0/admin/)  Administration  
  - [Cluster Configuration](https://docs.hopsworks.ai/3.0/admin/variables/)
  - [User Management](https://docs.hopsworks.ai/3.0/admin/user/)
  - [Configure Alerts](https://docs.hopsworks.ai/3.0/admin/alert/)
  - [Manage Services](https://docs.hopsworks.ai/3.0/admin/services/)
  - [IAM Role Chaining](https://docs.hopsworks.ai/3.0/admin/roleChaining/)
  - - [x]  Monitoring   Monitoring  
    - [Services Dashboards](https://docs.hopsworks.ai/3.0/admin/monitoring/grafana/)
    - [Services Logs](https://docs.hopsworks.ai/3.0/admin/monitoring/services-logs/)

  - - [x]  Authentication   Authentication  
    - [Configure Authentication](https://docs.hopsworks.ai/3.0/admin/auth/)
    - - [x]  Configure OAuth2   Configure OAuth2  
      - [Register an Identity Provider](https://docs.hopsworks.ai/3.0/admin/oauth2/create-client/)
      - [Create Okta Client](https://docs.hopsworks.ai/3.0/admin/oauth2/create-okta-client/)
      - [Create Azure Client](https://docs.hopsworks.ai/3.0/admin/oauth2/create-azure-client/)

    - - [x]  Configure LDAP/Kerberos   Configure LDAP/Kerberos  
      - [Configure LDAP](https://docs.hopsworks.ai/3.0/admin/ldap/configure-ldap/)
      - [Configure Kerberos](https://docs.hopsworks.ai/3.0/admin/ldap/configure-krb/)
      - [Configure server for LDAP and Kerberos](https://docs.hopsworks.ai/3.0/admin/ldap/configure-server/)

  - - [x]  High availability / Disaster Recovery   High availability / Disaster Recovery  
    - [Overview](https://docs.hopsworks.ai/3.0/admin/ha-dr/intro/)
    - [High Availability](https://docs.hopsworks.ai/3.0/admin/ha-dr/ha/)
    - [Disaster Recovery](https://docs.hopsworks.ai/3.0/admin/ha-dr/dr/)

- [API [Hopsworks API](https://docs.hopsworks.ai/hopsworks-api/dev)[Feature Store API](https://docs.hopsworks.ai/feature-store-api/dev)[MLOps API](https://docs.hopsworks.ai/machine-learning-api/dev)](https://docs.hopsworks.ai/)
- [Community ↗](https://community.hopsworks.ai/)

 Table of contents  
- [Data Sources](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#data-sources)
- [Data Validation](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#data-validation)
- [Aggregations](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#aggregations)
- [Dimensionality Reduction](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#dimensionality-reduction)
- [Transformations](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#transformations)
- [Feature Engineering in Python](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#feature-engineering-in-python)
- [Feature Engineering in Spark/PySpark](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#feature-engineering-in-sparkpyspark)
- [Feature Engineering in SQL](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#feature-engineering-in-sql)
- [Feature Engineering in Flink](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#feature-engineering-in-flink)

Feature Pipelines
=================

A feature pipeline is a program that orchestrates the execution of a dataflow graph of data validation, aggregation, dimensionality reduction, transformation, and other feature engineering steps on input data to create and/or update feature data. With HSFS, you can write feature pipelines in different languages as shown in the figure below.

![Image 3](https://docs.hopsworks.ai/3.0/assets/images/concepts/fs/feature-pipelines.svg)

### Data Sources[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#data-sources "Permanent link")

Your feature pipeline needs to connect to some (external) data source to read the data to be processed. Python, Spark, and Flink have connectors to a huge number of different data sources, while SQL feature pipelines are often restricted to a single data source (for example, your connector to SnowFlake only runs SQL on SnowFlake). SparkSQL, in contrast, can be used over tables that originate in different data sources.

### Data Validation[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#data-validation "Permanent link")

In order to be able to train and serve models that you can rely on, you need clean, high quality features. Data validation operations include removing bad data, removing or imputing missing values, and identifying problems such as feature shift. HSFS supports Great Expectations to specify data validation rules that are executed in the client before features are written to the Feature Store. The validation results are collected and shown in Hopsworks.

### Aggregations[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#aggregations "Permanent link")

Aggregations are used to summarize large datasets into more concise, signal-rich features. Popular aggregations include count(), sum(), mean(), median(), stddev(), min(), and max(). These aggregations produce a single number (a numerical feature) that captures information about a potentially large dataset. Both numerical and categorical features are often transformed before being used to train or serve models.

### Dimensionality Reduction[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#dimensionality-reduction "Permanent link")

If input data is impractically large or if it has a significant amount of redundancy, it can often be transformed into a reduced set of features with dimensionality reduction (often called feature extraction). Popular dimensionality algorithms include embedding algorithms, PCA, and TSNE.

### Transformations[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#transformations "Permanent link")

Transformations are covered in more detail in [training/inference pipelines](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/), as transformations typically happen after the feature store. If you store transformed features in feature groups, the feature data is no longer useful for EDA (as it near to impossible for Data Scientists to understand the transformed values). It also makes it impossible for inference pipelines to log untransformed feature values and predictions for an operational model. There is one use case for storing transformed features in feature groups - when you need to have ultra low latency when reading precomputed features (and online transformations when reading features add too much latency for your use case). The figure below shows to include transformations in your feature pipelines.

![Image 4](https://docs.hopsworks.ai/3.0/assets/images/concepts/fs/feature-pipelines-with-transformations.svg)

### Feature Engineering in Python[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#feature-engineering-in-python "Permanent link")

Python is the most widely used framework for feature engineering due to its extensive library support for aggregations (Pandas), data validation (Great Expectations), and dimensionality reduction (embeddings, PCA), and transformations (in Scikit-Learn, TensorFlow, PyTorch). Python also supports open-source feature engineering frameworks used for automated feature engineering, such as [featuretools](https://www.featuretools.com/) that supports relational and temporal sources.

### Feature Engineering in Spark/PySpark[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#feature-engineering-in-sparkpyspark "Permanent link")

Spark is popular as a feature engineering framework as it can scale to process larger volumes of data than Python, and provides native support for aggregations, and it supports many of the same data validation (Great Expectations), and dimensionality reduction algorithms (embeddings, PCA) as Python. Spark also has native support for transformations, which are useful for analytical models (batch scoring), but less useful for operational models, where online transformations are required, and Spark environments are less common. Online model serving environments typically only support online transformations in Python.

### Feature Engineering in SQL[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#feature-engineering-in-sql "Permanent link")

SQL has grown in popularity for performing heavy lifting in feature pipelines - computing aggregates on data - when the input data already resides in a data warehouse. Data warehouses also support data validation, for example, through Great Expectations in DBT. However, SQL is not mature as a platform for transformations and dimensionality reductions, where UDFs are applied row-wise.

You can do aggregation in SQL for data in your data warehouse or database.

### Feature Engineering in Flink[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/#feature-engineering-in-flink "Permanent link")

Flink is used for feature engineering when you need very fresh features computed in real-time. Flink pipelines are often written in Java, and provide native support for aggregations, with dimensionality reduction algorithms and transformations also possible in Java.

[Previous Write APIs](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/write_apis/)[Next External Feature Groups](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/external_fg/)

[](https://twitter.com/hopsworks "twitter.com")[](https://github.com/logicalclocks/hopsworks "github.com")[](https://community.hopsworks.ai/ "community.hopsworks.ai")[](https://www.linkedin.com/company/hopsworks/ "www.linkedin.com")[](https://bit.ly/publichopsworks "bit.ly")
