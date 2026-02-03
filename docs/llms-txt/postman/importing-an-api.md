# Import an API into the Postman API Builder

You can import an existing API specification into the Postman API Builder. API specifications can be imported from a local file or directory, a URL, raw text, or an API gateway.

## Import an API specification

1. In Postman, click **Import** in the sidebar.
2. Select an API specification file, enter a link to the API, or paste your raw text.
3. If you import an OpenAPI 3.0 or AsyncAPI 2.0 specification this way, you'll only have the option to [import the specification into Spec Hub](/docs/design-apis/specifications/import-a-specification/). To import an OpenAPI 3.0 or AsyncAPI 2.0 specification into the API Builder, [import the file into your API](/docs/design-apis/api-builder/develop-apis/defining-an-api/#import-an-api-definition).
4. You can choose to import the specification as a collection or as an API along with a collection.
5. Click **Import**.
6. An **Import Complete** message displays in the footer. In the message, select **Open in Postman** icon **View More Actions** to view more actions.
7. Select **Go to Collection** next to a collection or API to open the imported element.

![Import complete message](https://assets.postman.com/postman-docs/v11/import-complete-message-v11-2.jpg)

## Import a multi-file API specification

Multi-file API specifications are supported in OpenAPI 2.0 and 3.0 APIs and protobuf 2.0 and 3.0 APIs.

If you import a multi-file OpenAPI 3.0 specification this way, you'll only have the option to [import the specification into Spec Hub](/docs/design-apis/specifications/import-a-specification/). To import a multi-file OpenAPI 3.0 specification into the API Builder, [import the files into your API](/docs/design-apis/api-builder/develop-apis/defining-an-api/#import-an-api-definition).

1. In Postman, click **Import** in the sidebar.
2. Select **folders**, then select a local folder with your API files.
3. Select the files you want to import into Postman. Select **Postman Collection** to create a collection only. Select **(format) with a Postman Collection** to import the specification as a collection in the **Collections** tab and an API with a collection.
4. Click **Import**.
5. An **Import Complete** message displays in the footer. In the message, select **Open in Postman** icon **View More Actions** to view more actions.
6. Select **Go to Collection** next to a collection or API to open the imported element.

![Import complete message](https://assets.postman.com/postman-docs/v11/import-complete-message-v11-1.jpg)

## Import API specifications from Amazon API Gateway

[Amazon API Gateway](https://aws.amazon.com/api-gateway/) enables developers to publish and manage APIs that access AWS and other web services and data sources. You can import APIs directly from AWS Gateway to Postman. This creates an integration with API Gateway. Once connected, you can view your API deployment status and history from within Postman. You can also view [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics for each stage to get operational insight into your API.

This integration supports importing OpenAPI 3.0 specifications for both HTTP and REST APIs. Importing a specification will create a new API in Postman and will also configure an integration with AWS API Gateway.

To import an API from AWS API Gateway, click **Import** in the sidebar, then select **Other Sources > AWS API Gateway**. When importing an API from AWS API Gateway, you can choose to authenticate by creating an AWS IAM role or by using an AWS access key. Follow the steps for your chosen method:

* [Authenticate with an AWS IAM role](#authenticate-with-an-aws-iam-role)
* [Authenticate with an AWS access key](#authenticate-with-an-aws-access-key)

### Authenticate with an AWS IAM role

To set up a connection to Amazon API Gateway using an AWS IAM role, do the following:

1. Select **IAM** under **AWS Authentication Method**.

    ![Connecting with AWS IAM role](https://assets.postman.com/postman-docs/v11/import-from-api-gateway-with-iam-role-v11.jpg)

1. Select the **AWS API Type** (HTTP or REST).

To create an IAM role for Postman in AWS, do the following:

1. Sign in to the [AWS IAM console](https://console.aws.amazon.com/iam/home#/roles) and select **Create role**.
1. Under **Select type of trusted entity**, select **AWS account**.
1. Under **An AWS account**, select **Another AWS account** and enter Postman's **AWS Account ID**: `258201882842`
1. Under **Options**, select the **Require external ID** checkbox and enter the **External ID** from Postman. You can find the external ID in Postman's **Connect to AWS API Gateway** procedure under **Step 1: Create an IAM role**, as shown in [Authenticating with an AWS IAM role](/docs/integrations/available-integrations/aws-api-gateway/deploying-an-api-aws/#authenticate-with-an-aws-iam-role).

    For more information, refer to the [AWS IAM guide on using external IDs](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html).

1. Click **Next: Permissions**.
1. Select an existing IAM policy or click **Create policy**. If you are creating a policy, use the following JSON code:

    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "Stmt909923626743",
                "Effect": "Allow",
                "Action": [
                    "apigateway:GET",
                    "apigateway:PUT",
                    "apigateway:POST",
                    "cloudwatch:GetMetricData"
                ],
                "Resource": [
                    "*"
                ]
            }
        ]
    }
    ```

    This policy will enable exporting and deploying for HTTP API specifications. (Exporting and deploying aren't supported for REST API specifications.) You can customize the `Action` section in the IAM policy based on your needs:

    * `\"apigateway:GET\"` - (Required) Enables viewing API Gateway deployments for HTTP and REST APIs in Postman.
    * `\"apigateway:PUT\"` - Enables [exporting](/docs/integrations/available-integrations/aws-api-gateway/deploying-an-api-aws/#export-and-deploy-your-api) HTTP API specifications to the API Gateway.
    * `\"apigateway:POST\"` - Enables [deploying](/docs/integrations/available-integrations/aws-api-gateway/deploying-an-api-aws/#export-and-deploy-your-api) HTTP API specifications to a stage on the API Gateway.
    * `\"apigateway:*\"` - Assigns all GET, PUT, POST, PATCH, DELETE permissions to the IAM role.
    * `\"cloudwatch:GetMetricData\"` - Enables [viewing CloudWatch metrics](/docs/integrations/available-integrations/aws-api-gateway/deploying-an-api-aws/#view-cloudwatch-metrics) in Postman.

1. Click **Next: Tags**.
1. Click **Next: Review**.
1. Add a **Role name** and **Role description**, then click **Create role**.

Copy the **Role ARN** from AWS and paste it in Postman under **Step 2: Enter role ARN and region**. Next, enter the **AWS Region** where the API Gateway is located and select the **API Gateway**. Then, enter an **API Name** for the imported API. When you're ready, click **Connect**.

### Authenticate with an AWS access key

To set up a connection to Amazon API Gateway using an AWS access key, select **Access Key** under **AWS Authentication Method**.

![Connecting with AWS access key](https://assets.postman.com/postman-docs/v11/import-from-api-gateway-with-access-key-v11.jpg)

Next, enter information about the connection:

* Select the **AWS API Type** (HTTP or REST).
* Enter the **Access Key ID** and **Secret Access Key** for your AWS account. (Learn how to [find your credentials in AWS](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/getting-your-credentials.html).)
* Enter the **AWS Region** where the API Gateway is located and select the **API Gateway**.
* Enter an **API Name** for the imported API.

When you're ready, click **Import**. After importing your API specification, you can [view API deployments in Postman](/docs/integrations/available-integrations/aws-api-gateway/deploying-an-api-aws/).

## Import API specifications from Azure API Management

You can import a specification from a connected Azure API Management service to an API in Postman. Importing a specification will create a new API in Postman and will also configure an integration with Azure API Management. Learn more about [integrating with Azure API Management](/docs/integrations/available-integrations/azure-api-management/deploying-an-api-azure/).

To import an API specification from Azure API Management, do the following:

1. Click **Import** in the sidebar, then select **Other Sources > Azure API Management**.
2. You'll be prompted to authorize Postman to access your Microsoft Azure account. After you grant access, you can close the browser tab and return to Postman.
3. Enter information about the Azure API Management service you want to import a specification from:

    * **Subscription** - The [subscription](https://docs.microsoft.com/en-us/azure/api-management/api-management-subscriptions) where the service was created.
    * **Resource Group** - The [resource group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal) that has the service.
    * **Service** - The Azure API Management [service instance](https://docs.microsoft.com/en-us/azure/api-management/api-management-key-concepts) used for deploying your API.
    * **Azure API Version** - The Azure API [version](https://docs.microsoft.com/en-us/azure/api-management/api-management-versions) you want to import.
    * **Definition type** - Select the specification for the specification you want to import (OpenAPI 2.0 or OpenAPI 3.0).
    * **API name** - The name to use for the new API that will be created in Postman using the imported specification.

4. Click **Import**.

## Supported API specifications formats

Postman directly supports importing the following formats:

* [OpenAPI 3.0 and 3.1](https://github.com/postmanlabs/openapi-to-postman)
* Swagger [1.2](https://github.com/postmanlabs/swagger1-to-postman) and [2.0](https://github.com/postmanlabs/swagger2-postman2-lambda)
* Protobuf 2 and 3
* [GraphQL](https://github.com/postmanlabs/graphql-to-postman)
* [cURL](https://github.com/postmanlabs/curl-to-postman)
* RAML [0.8](https://github.com/postmanlabs/raml-to-postman) and [1.0](https://github.com/postmanlabs/raml1-to-postman)
* [WSDL 1.1 and 2.0](https://github.com/postmanlabs/wsdl-to-postman)
* [HTTP Archive (HAR)](https://github.com/postmanlabs/har-to-postman)
* Web Application Description Language (WADL)

There are also tools on GitHub to convert different API specifications into a Postman Collection that can be imported:

* [runscope-to-postman](https://github.com/postmanlabs/runscope-to-postman)
* [DHC-to-postman](https://github.com/postmanlabs/dhc-to-postman)