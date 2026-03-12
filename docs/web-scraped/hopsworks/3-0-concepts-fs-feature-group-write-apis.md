# Source: https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/write_apis/

Title: Write APIs - Hopsworks Documentation

URL Source: https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/write_apis/

Markdown Content:
Write APIs - Hopsworks Documentation
===============

- [x] - [x]

[Skip to content](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/write_apis/#stream-api)

[![Image 4: logo](https://docs.hopsworks.ai/3.0/assets/images/hops-logo.png)](https://docs.hopsworks.ai/3.0/ "Hopsworks Documentation")

 Hopsworks Documentation

3.0
- [dev](https://docs.hopsworks.ai/dev/)
- [4.7](https://docs.hopsworks.ai/4.7/)
- [4.6](https://docs.hopsworks.ai/4.6/)
- [4.4](https://docs.hopsworks.ai/4.4/)
- [4.3](https://docs.hopsworks.ai/4.3/)
- [4.2](https://docs.hopsworks.ai/4.2/)
- [4.1](https://docs.hopsworks.ai/4.1/)
- [4.0](https://docs.hopsworks.ai/4.0/)
- [3.9](https://docs.hopsworks.ai/3.9/)
- [3.8](https://docs.hopsworks.ai/3.8/)
- [3.7](https://docs.hopsworks.ai/3.7/)
- [3.5](https://docs.hopsworks.ai/3.5/)
- [3.4](https://docs.hopsworks.ai/3.4/)
- [3.3](https://docs.hopsworks.ai/3.3/)
- [3.2](https://docs.hopsworks.ai/3.2/)
- [3.1](https://docs.hopsworks.ai/3.1/)
- [3.0](https://docs.hopsworks.ai/3.0/)
- [2.5](https://docs.hopsworks.ai/2.5/)

 Write APIs

 Initializing search

[logicalclocks/hopsworks * v3.7.0 * 1.3k * 154](https://github.com/logicalclocks/hopsworks "Go to repository")

- [Home](https://docs.hopsworks.ai/3.0/)
- [Getting Started ↗](https://colab.research.google.com/github/logicalclocks/hopsworks-tutorials/blob/master/quickstart.ipynb)
- [Tutorials](https://docs.hopsworks.ai/3.0/tutorials/)
- [Concepts](https://docs.hopsworks.ai/3.0/concepts/hopsworks/)
- [Guides](https://docs.hopsworks.ai/3.0/user_guides/)
- [Setup and Installation](https://docs.hopsworks.ai/3.0/setup_installation/)
- [Administration](https://docs.hopsworks.ai/3.0/admin/)
- [](https://docs.hopsworks.ai/)[API](https://docs.hopsworks.ai/)[](https://docs.hopsworks.ai/)[Hopsworks API](https://docs.hopsworks.ai/hopsworks-api/3.0/generated/api/login/)[Feature Store API](https://docs.hopsworks.ai/feature-store-api/3.0/generated/api/connection_api/)[MLOps API](https://docs.hopsworks.ai/machine-learning-api/3.0/generated/connection_api/)  
- [Community ↗](https://community.hopsworks.ai/)

[![Image 5: logo](https://docs.hopsworks.ai/3.0/assets/images/hops-logo.png)](https://docs.hopsworks.ai/3.0/ "Hopsworks Documentation") Hopsworks Documentation  

[logicalclocks/hopsworks * v3.7.0 * 1.3k * 154](https://github.com/logicalclocks/hopsworks "Go to repository")

- [Home](https://docs.hopsworks.ai/3.0/)
- [Getting Started ↗](https://colab.research.google.com/github/logicalclocks/hopsworks-tutorials/blob/master/quickstart.ipynb)
- - [x] [Tutorials](https://docs.hopsworks.ai/3.0/tutorials/)  Tutorials  

- - [x]  Concepts   Concepts  
  - [Hopsworks Platform](https://docs.hopsworks.ai/3.0/concepts/hopsworks/)
  - [MLOps Dictionary ↗](https://www.hopsworks.ai/mlops-dictionary?utm_source=web&utm_medium=docs)
  - - [x] [Feature Store](https://docs.hopsworks.ai/3.0/concepts/fs/)  Feature Store  
    - - [x]  Feature Groups   Feature Groups  
      - [Overview](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/fg_overview/)
      - - [x]  Write APIs  [Write APIs](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/write_apis/) Table of contents  
        - [Stream API](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/write_apis/#stream-api)
        - [Batch API](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/write_apis/#batch-api)
        - [Connector API](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/write_apis/#connector-api)

      - [Feature Pipelines](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/)
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

- [](https://docs.hopsworks.ai/)[API](https://docs.hopsworks.ai/)[](https://docs.hopsworks.ai/)[Hopsworks API](https://docs.hopsworks.ai/hopsworks-api/dev)[Feature Store API](https://docs.hopsworks.ai/feature-store-api/dev)[MLOps API](https://docs.hopsworks.ai/machine-learning-api/dev)  
- [Community ↗](https://community.hopsworks.ai/)

 Table of contents  
- [Stream API](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/write_apis/#stream-api)
- [Batch API](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/write_apis/#batch-api)
- [Connector API](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/write_apis/#connector-api)

Write APIs
==========

You write to feature groups, and read from feature views.

There are 3 APIs for writing to feature groups, as shown in the table below:

|  | Stream API | Batch API | Connector API |
| --- | --- | --- | --- |
| Python | X | - | - |
| Spark | X | X | - |
| Flink | X | - | - |
| External Table | - | - | X |

Stream API[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/write_apis/#stream-api "Permanent link")
--------------------------------------------------------------------------------------------------------------

The Stream API is the only API for Python and Flink clients, and is the preferred API for Spark, as it ensures consistent features between offline and online feature stores. The Stream API first writes data to be ingested to a Kafka topic, and then Hopsworks ensures that the data is synchronized to the Online and Offline Feature Groups through the OnlineFS service and Hudi DeltaStreamer jobs, respectively. The data in the feature groups is guaranteed to arrive at-most-once, through idempotent writes to the online feature group (only the latest values of features are stored there, and duplicates in Kafka only cause idempotent updates) and duplicate removal by Apache Hudi for the offline feature group.

![Image 6](https://docs.hopsworks.ai/3.0/assets/images/concepts/fs/fg-stream-api.svg)

Batch API[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/write_apis/#batch-api "Permanent link")
------------------------------------------------------------------------------------------------------------

For very large updates to feature groups, such as when you are backfilling large amounts of data to an offline feature group, it is often preferential to write directly to the Hudi tables in Hopsworks, instead of via Kafka - thus reducing write amplification. Spark clients can write directly to Hudi tables on Hopsworks with Hopsworks libraries and certificates using a HDFS API. This requires network connectivity between the Spark clients and the datanodes in Hopsworks.

![Image 7](https://docs.hopsworks.ai/3.0/assets/images/concepts/fs/fg-batch-api.svg)

Connector API[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/write_apis/#connector-api "Permanent link")
--------------------------------------------------------------------------------------------------------------------

Hopsworks supports external tables as feature groups. You can mount a table from an external database as an offline feature group using the Connector API - you create an external table using the connector. This enables you to use features from your external data source (Snowflake, Redshift, Delta Lake, etc) as you would any feature in an offline feature group in Hopsworks. You can, for example, join features from different feature groups (external or not) together to create feature views and training data for models.

![Image 8](https://docs.hopsworks.ai/3.0/assets/images/concepts/fs/fg-connector-api.svg)

[Previous Overview](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/fg_overview/)[Next Feature Pipelines](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/)

[](https://twitter.com/hopsworks "twitter.com")[](https://github.com/logicalclocks/hopsworks "github.com")[](https://community.hopsworks.ai/ "community.hopsworks.ai")[](https://www.linkedin.com/company/hopsworks/ "www.linkedin.com")[](https://bit.ly/publichopsworks "bit.ly")
