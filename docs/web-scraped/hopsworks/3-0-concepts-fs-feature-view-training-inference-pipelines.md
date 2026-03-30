# Source: https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/

Title: Consistent Transformations - Hopsworks Documentation

URL Source: https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/

Markdown Content:
Consistent Transformations - Hopsworks Documentation
===============

- [x] - [x]

[Skip to content](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/#transformations)

[![Image 2: logo](https://docs.hopsworks.ai/3.0/assets/images/hops-logo.png)](https://docs.hopsworks.ai/3.0/ "Hopsworks Documentation")

 Hopsworks Documentation

 Consistent Transformations

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

[![Image 3: logo](https://docs.hopsworks.ai/3.0/assets/images/hops-logo.png)](https://docs.hopsworks.ai/3.0/ "Hopsworks Documentation") Hopsworks Documentation  

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
      - [Offline API](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/offline_api/)
      - [Online API](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/online_api/)
      - - [x]  Consistent Transformations  [Consistent Transformations](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/) Table of contents  
        - [Transformations](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/#transformations)
        - [Training Serving Skew](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/#training-serving-skew)
          - [Transformations as Pre-Processing Layers in Models](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/#transformations-as-pre-processing-layers-in-models)
          - [Transformation Pipelines in Scikit-Learn/TensorFlow/PyTorch](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/#transformation-pipelines-in-scikit-learntensorflowpytorch)
          - [Transformations as Python UDFs in HSFS](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/#transformations-as-python-udfs-in-hsfs)

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
- [Transformations](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/#transformations)
- [Training Serving Skew](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/#training-serving-skew)
  - [Transformations as Pre-Processing Layers in Models](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/#transformations-as-pre-processing-layers-in-models)
  - [Transformation Pipelines in Scikit-Learn/TensorFlow/PyTorch](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/#transformation-pipelines-in-scikit-learntensorflowpytorch)
  - [Transformations as Python UDFs in HSFS](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/#transformations-as-python-udfs-in-hsfs)

Consistent Transformations
==========================

A _training pipeline_ is a program that orchestrates the training of a machine learning model. For supervised machine learning, a training pipeline requires both features and labels, and these can typically be retrieved from the feature store as either in-memory Pandas DataFrames or read as training data files, created from the feature store. An _inference pipeline_ is a program that takes user input, optionally enriches it with features from the feature store, and builds a feature vector (or batch of feature vectors) with with it uses a model to make a prediction.

Transformations[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/#transformations "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------

Feature transformations are mathematical operations that change feature values with the goal of improving model convergence or performance properties. Transformation functions take as input a single value (or small number of values), they often require state (such as the mean value of a feature to normalize the input), and they output a single value or a list of values.

Training Serving Skew[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/#training-serving-skew "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

It is crucial that the transformations performed when creating features (for training or serving) are consistent - use the same code - to avoid training/serving skew. In the image below, you can see that transformations happen after the Feature Store, but that the implementation of the transformation functions need to be consistent between the training and inference pipelines.

![Image 4](https://docs.hopsworks.ai/3.0/assets/images/concepts/fs/no-training-serving-skew.svg)

There are 3 main approaches to prevent training/serving skew that we support in Hopsworks. These are (1) perform transformations in models, (2) perform transformations in pipelines (sklearn, TF, PyTorch) and use the model registry to save the transformation pipeline so that the same transformation is used in your inference pipeline, and (3) use HSFS transformations, defined as UDFs in Python.

### Transformations as Pre-Processing Layers in Models[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/#transformations-as-pre-processing-layers-in-models "Permanent link")

Transformation functions can be implemented as preprocessing steps within a model. For example, you can write a transformation function as a pre-processing layer in Keras/TensorFlow. When you save the model, the preprocessing steps will also be saved as part of the model. Any state required to compute the transformation, such as the arithmetic mean of a numerical feature in the train set, is also stored with the function, enabling consistent transformations during inference. When data preprocessing is part of the model, users can just send the untransformed feature values to the model and the model itself will apply any transformation functions as preprocessing layers (such as encoding categorical variables or normalizing numerical variables).

### Transformation Pipelines in Scikit-Learn/TensorFlow/PyTorch[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/#transformation-pipelines-in-scikit-learntensorflowpytorch "Permanent link")

You have to save your transformation pipeline (serialize the object or the parameters) and make sure you apply exactly the same transformations in your inference pipeline. This means you should version the transformations. In Hopsworks, you can store the transformations with your versioned models in the Model Registry, helping you to ensure the same transformation pipeline is applied to both training/serving for the same model version.

### Transformations as Python UDFs in HSFS[#](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/training_inference_pipelines/#transformations-as-python-udfs-in-hsfs "Permanent link")

Hopsworks feature store also supports consistent transformation functions by enabling a Python UDF, that implements a transformation, to be attached a to feature in a feature view. When training data is created with a feature view or when a feature vector is retrieved from a feature view, HSFS ensures that any transformation functions defined over any features will be applied before returning feature values. You can use built-in transformation objects in HSFS or write your own custom transformation functions as Python UDFs. The benefit of this approach is that transformations are applied consistently when creating training data and when retrieving feature data from the online feature store. Transformations no longer need to be included in either your training pipeline or inference pipeline, as they are applied transparently when creating training data and retrieving feature vectors. Hopsworks uses Spark to create training data as files, and any transformation functions for features are executed as Python UDFs in Spark - enabling transformation functions to be applied on large volumes of data and removing potentially CPU-intensive transformations from training pipelines.

[Previous Online API](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/online_api/)[Next Statistics](https://docs.hopsworks.ai/3.0/concepts/fs/feature_view/statistics/)

[](https://twitter.com/hopsworks "twitter.com")[](https://github.com/logicalclocks/hopsworks "github.com")[](https://community.hopsworks.ai/ "community.hopsworks.ai")[](https://www.linkedin.com/company/hopsworks/ "www.linkedin.com")[](https://bit.ly/publichopsworks "bit.ly")
