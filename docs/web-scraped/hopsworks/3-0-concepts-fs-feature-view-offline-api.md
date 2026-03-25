# Source: https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/

Title: Offline API - Hopsworks Documentation

URL Source: https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/

Markdown Content:
Offline API - Hopsworks Documentation
===============

- [x] - [x]

[Skip to content](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/#training-data)

[![Image 3: logo](https://docs.hopsworks.ai/3.0/assets/images/hops-logo.png)](https://docs.hopsworks.ai/3.0/ "Hopsworks Documentation")

 Hopsworks Documentation

 Offline API

 Initializing search

[logicalclocks/hopsworks](https://github.com/logicalclocks/hopsworks "Go to repository")

- [Home](https://docs.hopsworks.ai/3.0/)
- [Getting Started ↗](https://colab.research.google.com/github/logicalclocks/hopsworks-tutorials/blob/master/quickstart.ipynb)
- [Tutorials](https://docs.hopsworks.ai/3.0/tutorials/)
- [Concepts](https://docs.hopsworks.ai/3.0/concepts/hopsworks/)
- [Guides](https://docs.hopsworks.ai/3.0/user_guides/)
- [Setup and Installation](https://docs.hopsworks.ai/3.0/setup_installation/)
- [Administration](https://docs.hopsworks.ai/3.0/admin/)
- [](https://docs.hopsworks.ai/)[API](https://docs.hopsworks.ai/)[](https://docs.hopsworks.ai/)[Hopsworks API](https://docs.hopsworks.ai/hopsworks-api/dev)[Feature Store API](https://docs.hopsworks.ai/feature-store-api/dev)[MLOps API](https://docs.hopsworks.ai/machine-learning-api/dev)  
- [Community ↗](https://community.hopsworks.ai/)

[![Image 4: logo](https://docs.hopsworks.ai/3.0/assets/images/hops-logo.png)](https://docs.hopsworks.ai/3.0/ "Hopsworks Documentation") Hopsworks Documentation  

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
      - [Feature Pipelines](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/feature_pipelines/)
      - [External Feature Groups](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/external_fg/)
      - [Data Validation/Stats/Alerts](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/fg_statistics/)
      - [Versioning](https://docs.hopsworks.ai/3.0/concepts/fs/feature_group/versioning/)

    - - [x]  Feature Views   Feature Views  
      - [Overview](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/fv_overview/)
      - - [x]  Offline API  [Offline API](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/) Table of contents  
        - [Training Data](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/#training-data)
          - [Point-in-time Correct Training Data](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/#point-in-time-correct-training-data)
          - [Splitting Training Data](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/#splitting-training-data)
          - [Evaluation Sets](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/#evaluation-sets)

        - [Batch (Scoring) Data](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/#batch-scoring-data)

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
- [Training Data](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/#training-data)
  - [Point-in-time Correct Training Data](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/#point-in-time-correct-training-data)
  - [Splitting Training Data](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/#splitting-training-data)
  - [Evaluation Sets](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/#evaluation-sets)

- [Batch (Scoring) Data](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/#batch-scoring-data)

Offline API
===========

The feature view provides an _Offline API_ for

- creating training data
- creating batch (scoring) data

Training Data[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/#training-data "Permanent link")
--------------------------------------------------------------------------------------------------------------------

Training data is created using a feature view. You can create training data as either:

- in-memory Pandas DataFrames, useful when you have a small amount of training data;
- materialized training data in files, in a file format of your choice (such as .tfrecord, .csv, or .parquet).

You can apply filters when creating training data from a feature view:

- start-time and end-time, for example, to create the train-set from an earlier time range, and the test-set from a later (unseen) time range;
- feature value features, for example, only train a model on customers from a particular country.

Note that filters are not applied when retrieving feature vectors using feature views, as we only look up features for a specific entity, like a customer. In this case, the application should know that predictions for this customer should be made on the model trained on customers in USA, for example.

### Point-in-time Correct Training Data[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/#point-in-time-correct-training-data "Permanent link")

When you create training data from features in different feature groups, it is possible that the feature groups are updated at different cadences. For example, maybe one feature group is updated hourly, while another feature group is updated daily. It is very complex to write code that joins features together from such feature groups and ensures there is no data leakage in the resultant training data. HSFS hides this complexity by performing the point-in-time JOIN transparently, similar to the illustration below:

![Image 5](https://docs.hopsworks.ai/3.0/assets/images/concepts/fs/feature-view-training-data.svg)

HSFS uses the event_time columns on both feature groups to determine the most recent (but not newer) feature values that are joined together with the feature values from the feature group containing the label. That is, the features in the feature group containing the label are the observation times for the features in the resulting training data, and we want feature values from the other feature groups that have the most recent timestamps, but not newer than the timestamp in the label-containing feature group.

### Splitting Training Data[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/#splitting-training-data "Permanent link")

You can create random train/validation/test splits of your training data using the HSFS API. You can also time-based splits with the HSFS API.

### Evaluation Sets[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/#evaluation-sets "Permanent link")

Test data can also be split into evaluation sets to help evaluate a model for potential bias. First, you have to identify the classes of samples that could be at risk of bias, and generate _evaluation sets_ from your unseen test set - one evaluation set for each group of samples at risk of bias. For example, if you have a feature group of users, where one of the features is gender, and you want to evaluate the risk of bias due to gender, you can use filters to generate 3 evaluation sets from your test set - one for male, female, and non-binary. Then you score your model against all 3 evaluation sets to ensure that the prediction performance is comparable and non-biased across all 3 gender.

Batch (Scoring) Data[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/#batch-scoring-data "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------

Batch data for scoring models is created using a feature view. Similar to training data, you can create batch data as either:

- in-memory Pandas DataFrames, useful when you have a small amount of data to score;
- materialized data in files, in a file format of your choice (such as .tfrecord, .csv, or .parquet)

Batch data requires specification of a `start_time` for the start of the batch scoring data. You can also specify the `end_time` (default is the current date).

![Image 6](https://docs.hopsworks.ai/3.0/assets/images/concepts/fs/batch-scoring-data.svg)

[Previous Overview](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/fv_overview/)[Next Online API](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/online_api/)

[](https://twitter.com/hopsworks "twitter.com")[](https://github.com/logicalclocks/hopsworks "github.com")[](https://community.hopsworks.ai/ "community.hopsworks.ai")[](https://www.linkedin.com/company/hopsworks/ "www.linkedin.com")[](https://bit.ly/publichopsworks "bit.ly")
