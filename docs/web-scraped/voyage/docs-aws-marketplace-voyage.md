# Source: https://docs.voyageai.com/docs/aws-marketplace-voyage

## GET STARTED 

- [[[Introduction]]](/docs/introduction)
- [[[API Key and Python Client]]](/docs/api-key-and-installation)
- [[[Quickstart Tutorial]]](/docs/quickstart-tutorial)

## CAPABILITIES 

- [[[Text Embeddings]]](/docs/embeddings)
- [[[Contextualized Chunk Embeddings]]](/docs/contextualized-chunk-embeddings)
- [[[Multimodal Embeddings]]](/docs/multimodal-embeddings)
- [[[Rerankers]]](/docs/reranker)

## GUIDES 

- [[[Tokenization]]](/docs/tokenization)
- [[[Flexible Dimensions and Quantization]]](/docs/flexible-dimensions-and-quantization)
- [[[Batch Inference]]](/docs/batch-inference)
- [[[Error Codes]]](/docs/error-codes)
- [[[Rate Limits]]](/docs/rate-limits)
- [[[Pricing]]](/docs/pricing)
- [[[Organizations and Projects]]](/docs/organizations-and-projects)
- [[[Service Level Objectives]]](/docs/service-level-objectives)

## DEPLOYMENT ON VPC 

- [[AWS Marketplace Model Package]]
  - [[[MongoDB Voyage AI Models in AWS]]](/docs/aws-marketplace-mongodb-voyage)
  - [[[Voyage AI Models in AWS]]](/docs/aws-marketplace-voyage)
- [[Azure Marketplace Managed Application]]
  - [[[MongoDB Voyage AI Models in Azure]]](/docs/azure-marketplace-mongodb-voyage)
  - [[[Voyage AI Models in Azure]]](/docs/azure-marketplace-voyage)

## ACCESS VIA DATA PLATFORMS 

- [[[Snowflake]]](/docs/snowflake)

## Community 

- [[[Integrations]]](/docs/integrations-and-other-libraries)
- [[[Community SDKs]]](/docs/community-sdks)

## HELP 

- [[[FAQ]]](/docs/faq)
- [[[Contact Email]]](/docs/contact-email)
- [[[Discord]]](/docs/discord)

Powered by [](https://readme.com?ref_src=hub&project=voyage-ai)

# Voyage AI Models in AWS

Deploy Voyage AI models using AWS Marketplace

> [🚧]
>
> Models published under Voyage AI are no longer updated and will be removed in the future. For the latest models and all future updates, use the official MongoDB listing. To learn more, see [MongoDB Voyage AI Models in AWS](aws-marketplace-mongodb-voyage).

AWS Marketplace model packages are containerized solutions that include the model and inference code, designed to be deployed in a customer account and virtual private cloud (VPC). Model packages offer several benefits to customers:

1.  **Data flow and access control**. Because models are deployed into their account and VPC, customers maintain full control over data flow and API access, effectively addressing data privacy risks associated with third-party or multi-tenant serving.
2.  **Reliability and compliance backed by AWS**. AWS will be the customer sub-processor, and customers inherit all the reliability and compliance guarantees of AWS.
3.  **Billing and payment through AWS**. By transacting through a marketplace listing, customers can utilize their existing AWS billing information and credits to procure Voyage models. This streamlined process eliminates the need to manage a separate third-party payment and billing system.

A model package can be deployed in two ways --- as a [real-time inference API endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html) or a [batch transform job](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html). A real-time inference API endpoint is a persistent, fully managed API endpoint designed for request-by-request inference. In contrast, a batch transform job is a finite execution process intended for bulk inference on a dataset, with predictions written to a file. In both cases, the model packages are running on some underlying hardware, such as GPUs, which are called AWS instances.

**Pricing.** Pricing for the use of a Voyage model package consists of software pricing and infrastructure pricing, both at an hourly rate. Software pricing covers the cost of model usage, while your total hourly cost is the sum of the software pricing (e.g., \$5.71 per hour for [`voyage-multilingual-2`](https://aws.amazon.com/marketplace/pp/prodview-ebotgiywtalec?sr=0-4&ref_=beagle&applicationId=AWSMPContessa) ) and the infrastructure pricing (e.g., \$1.408 per hour for a single ml.g5.xlarge). Pricing rates vary based on deployment type (i.e., real-time inference API endpoint versus batch transform job), instance type, and region. All Voyage AI models come with a free trial.

Below, we present a short tutorial on subscribing to and deploying the models. Then, we will discuss advanced deployment options and provide information on latency and throughput.

#  

Model Package Subscription

[](#model-package-subscription)

You will need the following AWS identity access management (IAM) permission to subscribe to an AWS Marketplace listing. To add them, [sign into your AWS account console](https://console.aws.amazon.com/iam/) and see this [page](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#add-policies-console) for instructions.

- [AmazonSageMakerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.html) (AWS Managed Policy)
- aws-marketplace:ViewSubscriptions
- aws-marketplace:Subscribe
- aws-marketplace:Unsubscribe

To subscribe via the AWS Marketplace:

1.  Select the Voyage model package you would like to subscribe to in the [AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=seller-snt4gb6fd7ljg).

2.  Click **Continue to Subscribe**.

    [[![](https://files.readme.io/a961efdfd4d005d154197aed321fc1c52a1df6bc8e324e5d25702222fcbe7d4f-image.png)]]

3.  Click **Accept Offer**.

    [[![](https://files.readme.io/36ea2d0d6696e815311c34119a2a30e98054d2b45bd74223664b38311fa18a0b-image.png)]]

4.  Confirm you have successfully subscribed (see confirmation toast in the figure below). You can now safely close the window.

    [[![](https://files.readme.io/207453ae5fc0c0e2ae5415b7f527cb43d061353384e648de73380b83ae6b5e85-image.png)]]

You can also confirm and manage your AWS Marketplace subscriptions through the console's [manage subscription page](https://aws.amazon.com/marketplace/library/ref=gtw_navgno_library). You can [cancel your subscription](https://docs.aws.amazon.com/marketplace/latest/buyerguide/cancel-machine-learning-subscription.html) at any time, but note that canceling your subscription [***does not***](https://docs.aws.amazon.com/marketplace/latest/buyerguide/cancel-machine-learning-subscription.html) terminate your existing real-time inference endpoints or batch transform jobs (see [Delete Real-Time Inference Endpoints](#delete-real-time-inference-endpoints)).

Model package deployment requires specific SageMaker instances (e.g., ml.g5.xlarge). The exact quota names for these instances end with "endpoint usage" and "transform job usage" (e.g., "ml.g5.2xlarge for endpoint usage", and "ml.g5.2xlarge for transform job usage". These [quotas](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html#limits_sagemaker) are often set to zero by default. Please go to the [SageMaker Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/sagemaker/quotas) to [request quota increases](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) if needed.

#  

Model Package Deployment

[](#model-package-deployment)

This section covers the mechanics of how to deploy a model package using Amazon SageMaker Studio and our example Jupyter Notebooks.

##  

Amazon SageMaker Studio

[](#amazon-sagemaker-studio)

[Amazon SageMaker Studio](https://aws.amazon.com/sagemaker/studio/) is a web-based interface for ML and AI development that includes a hosted notebook environment already authenticated to your AWS account. You can skip this section if you have another preferred Jupyter notebook execution environment, such as your local machine, and you know how to properly authenticate to your AWS account from that environment. Follow the SageMaker documentation to first [launch SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html), and then [launch a JupyterLab environment](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-user-guide.html).

[[![Amazon SageMaker Studio](https://files.readme.io/97ce1bf372af3f435910e8c98c38405d61ddf7fffa37c98eee82fd522c581fd0-image.png)]]

##  

Jupyter Notebook

[](#jupyter-notebook)

We provide an [example Jupyter notebook](https://github.com/voyage-ai/voyageai-aws/blob/main/deploy_voyage_model_package_sagemaker.ipynb) to get started with Python using the AWS SDK ([Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)) and the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/). You can clone the notebook into SageMaker Studio, or your preferred Jupyter notebook execution environment, by cloning the [Voyage AI AWS repo](https://github.com/voyage-ai/voyageai-aws/tree/main) (i.e., `git clone https://github.com/voyage-ai/voyageai-aws.git`).

[[![JupyterLab git clone](https://files.readme.io/f7669bb78111a58f7dca9326090a48332eb2a33676b1521e00ed043447515d36-image.png)]]

Alternatively, you can directly download the notebook from GitHub and move it to your notebook execution environment (e.g., upload it to SageMaker Studio).

Once accessible to SageMaker Studio or your preferred execution environment, you can open the notebook and follow the steps in it to deploy the models.

##  

Delete Real-Time Inference Endpoints

[](#delete-real-time-inference-endpoints)

Be careful to not have real-time inference endpoints running unnecessarily. They will incur wasteful costs, potentially leading to unexpected charges. If you are using a provided example Jupyter notebook, be sure to run the "Clean-up" section, which deletes the endpoint and associated endpoint configuration. You can manage and delete endpoints through SageMaker Studio or the SageMaker console (see [here](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-manage.html) for instructions).

#  

Advanced Deployment

[](#advanced-deployment)

The Jupyter notebook described in the previous section is meant to get you started and build your understanding of deploying model packages. However, we'd like to make you aware of several other ways to deploy model packages, such as CloudFormation, the SageMaker Console, and the AWS CLI, though the details are beyond the scope of this documentation. These alternative methods may better suit the existing production workflow you have: CloudFormation for declarative infrastructure specification, SageMaker Console for interactive UI-based deployment, and AWS CLI for programmatic shell orchestration. A subscribed listing **Configure and launch** page provides instructions and resources for the aforementioned deployment methods, which you can return to by:

1.  Returning to the product listing page for your subscribed model of interest from the [AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=seller-snt4gb6fd7ljg).

2.  Clicking on **Continue to Subscribe** (upper right), which will take you to the **Subscribe to this software** page.

    [[![Voyage AI model package AWS marketplace continue to subscribe](https://files.readme.io/381d847f8dee6e615388cac16325459edef2de3f540de0ed1f0122710dd54b22-image.png)]]

3.  In the **Subscribe to this software** page, you should notice an "Already Subscribed" indicator. Click on the **Continue to configuration** button (upper right).

    [[![Voyage AI model package AWS marketplace already subscribed](https://files.readme.io/15d7c516c24758984e31704e30f43e3cadb3e2fa82e17346bb4a53826ead82e1-image.png)]]

4.  You are now back at the **Configure and launch** page. You can select your desired launch method, and the user interface will change with the appropriate instructions and resources for that method.

    [[![Voyage AI model package AWS marketplace configure and launch](https://files.readme.io/4a33160c71a2daae8ee71a10887bc3fdeb976fcdf9c51801b3edbb9be928a78c-image.png)]]

#  

Latency and Throughput

[](#latency-and-throughput)

The following table provides representative latency and throughput numbers for a deployed real-time inference endpoint running on an ml.g6.xlarge.

  Model                                                                                                                                                                                                                                                                                                                                                                                                Latency                                                                  Throughput
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------ ------------------------
  `voyage-3`                                                                                                                                                                                                                                                                                                                                              75 ms for a single query with at most 200 tokens.                        57M tokens per hour.
  `voyage-3-lite`                                                                                                                                                                                                                                                                                                                                         20 ms for a single query with at most 200 tokens.                        182M tokens per hour.
  `voyage-large-2` `voyage-large-2-instruct` `voyage-code-2` `voyage-law-2` `voyage-multilingual-2` `voyage-finance-2`   90 ms for single query with at most 100 tokens. 185 ms for 500 tokens.   12.6M tokens per hour.
  `voyage-2`                                                                                                                                                                                                                                                                                                                                              75 ms for single query with at most 200 tokens 90 ms for 500 tokens.     36M tokens per hour.
  `rerank-2`                                                                                                                                                                                                                                                                                                                                              For 25K tokens: 1.5 s (1 GPU), 415 ms (4 GPUs), and 245 ms (8 GPUs).     60M tokens per hour.
  `rerank-2-lite`                                                                                                                                                                                                                                                                                                                                         For 25K tokens: 565 ms (1 GPU), 170 ms (4 GPUs), and 120 ms (8 GPUs).    160M tokens per hour.
  `rerank-lite-1`                                                                                                                                                                                                                                                                                                                                         For 25K tokens: 445 ms (1 GPU), 135 ms (4 GPUs), and 90 ms (8 GPUs).     202M tokens per hour.

If you need assistance subscribing and deploying a Voyage model package from the AWS Marketplace, please send an email to [[\[email protected\]]](/cdn-cgi/l/email-protection#ccafa3a2b8adafb88cbaa3b5adaba9ada5e2afa3a1) or join our [Discord](https://discord.gg/zAU7GQEmvT).

Updated 24 days ago

------------------------------------------------------------------------

[[]](/docs/aws-marketplace-mongodb-voyage)

MongoDB Voyage AI Models in AWS

[](/docs/azure-marketplace)

Azure Marketplace Managed Application

[]

- [Table of Contents](#)
- - [Model Package Subscription](#model-package-subscription)
  - [Model Package Deployment](#model-package-deployment)
  - - [Amazon SageMaker Studio](#amazon-sagemaker-studio)
    - [Jupyter Notebook](#jupyter-notebook)
    - [Delete Real-Time Inference Endpoints](#delete-real-time-inference-endpoints)
  - [Advanced Deployment](#advanced-deployment)
  - [Latency and Throughput](#latency-and-throughput)