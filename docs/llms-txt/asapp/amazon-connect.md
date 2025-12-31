# Source: https://docs.asapp.com/generativeagent/integrate/amazon-connect.md

# Source: https://docs.asapp.com/ai-productivity/ai-transcribe/amazon-connect.md

# Source: https://docs.asapp.com/generativeagent/integrate/amazon-connect.md

# Source: https://docs.asapp.com/ai-productivity/ai-transcribe/amazon-connect.md

# Source: https://docs.asapp.com/generativeagent/integrate/amazon-connect.md

# Source: https://docs.asapp.com/ai-productivity/ai-transcribe/amazon-connect.md

# Source: https://docs.asapp.com/generativeagent/integrate/amazon-connect.md

# Source: https://docs.asapp.com/autotranscribe/amazon-connect.md

# Source: https://docs.asapp.com/generativeagent/integrate/amazon-connect.md

# Amazon Connect

> Learn how to integrate GenerativeAgent into Amazon Connect

The Amazon Connect integration with ASAPP's GenerativeAgent allows callers to have conversations with GenerativeAgent while maintaining the call entirely with in your Amazon Connect contact center.

This guide demonstrates an example integration using AWS's basic building blocks and ASAPP-provided flows. It showcases how the various components work together, but you can adapt or replace any part of the integration to match your organization's requirements.

<Note>
  **Want to skip the manual setup?**

  You can automatically deploy this integration using our QuickStart in the **[GenerativeAgent Amazon Connect - Code Samples](https://github.com/asappinc/generativeagent-amazon-connect)** on GitHub.
</Note>

## How it works

At a high level, the Amazon Connect integration with GenerativeAgent works by handing off the conversation between your Amazon Connect flow and GenerativeAgent:

1. **Hand off the conversation** to GenerativeAgent through your Amazon Connect Flows.
2. **GenerativeAgent handles the conversation** using Lambda functions to communicate with ASAPP's APIs, and respond to the caller using AWS's Text to Speech (TTS) service.
3. **Return control back** to your Amazon Connect Flow when:
   * The conversation is successfully completed
   * The caller requests a human agent
   * An error occurs

<Accordion title="Detailed Flow">
  Here's how a GenerativeAgent call will work in detail within your Amazon Connect:

  1. Your Amazon Connect Flow receives an incoming call
  2. When the flow engages GenerativeAgent, the Flow:
     * Sets required contact attributes
     * Starts media streaming
     * Calls ASAPP's API to initiate the conversation
  3. During the conversation:
     * Live audio streams through Kinesis Video Streams
     * Lambda functions coordinate between Amazon Connect and GenerativeAgent including using AWS's Text to Speech (TTS) service to respond to the caller.
     * Valkey manages the conversation state
  4. When the conversation ends, GenerativeAgent returns control to your Flow with:
     * The conversation outcome
     * Any error messages
     * Instructions for next steps (e.g., transfer to agent)

  <Frame>
    <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/AmazonConnectDiagram.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=e8a062923c9244d23d9bf405ca21d764" data-og-width="1600" width="1600" data-og-height="1015" height="1015" data-path="images/generativeagent/AmazonConnectDiagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/AmazonConnectDiagram.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=2443dd179fc2ebdfd5ffdf7ef561f74c 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/AmazonConnectDiagram.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=0e25deb42aa39fffaab9ebde13fbef70 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/AmazonConnectDiagram.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=dc67bc24951cd1b9e2c26f944d7031f0 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/AmazonConnectDiagram.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=7056af0993bd98d1ce443615fd45a5fb 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/AmazonConnectDiagram.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=cf71d4be37941516ce738e0eb8642668 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/AmazonConnectDiagram.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=3b2c98b7bc365dee925d7612898ecbe9 2500w" />
  </Frame>

  <Note>
    You are free to choose the moment when GenerativeAgent is invoked by Amazon Connect in your Contact Flow.

    You can add GenerativeAgent to any or all of your Amazon Contact Phone Numbers.
  </Note>
</Accordion>

## Before you Begin

Before using the GenerativeAgent integration with Amazon Connect, you need to:

* [Get your API Key Id and Secret](/getting-started/developers#access-api-credentials)
  * Ensure your API key has been configured to access GenerativeAgent APIs. Reach out to your ASAPP team if you need access enabled.
* Have an existing Amazon Connect instance:
  * Have claimed phone numbers.
  * Access to an Amazon Connect admin account.
* Have a AWS administrator account with the permissions for the following:
  * Creating/managing IAM roles/policies: create a policy permitting list/read operations on the Kinesis Video Streams associated with the Amazon Connect Flow
  * Managing Amazon Connect instance
  * Create/manage Lambda functions
  * Create/manage CloudWatch Log Groups
  * Create/manage ElastiCache for Valkey
  * Create/manage VPC
* Be familiar with AWS including Amazon Connect, IAM roles, and more:

  <Accordion title="AWS Components">
    You will set up and configure the following AWS services:

    * **Amazon Connect** - Handles call flow and audio streaming
    * **Valkey ElastiCache** - Manages conversation state and actions
    * **Virtual Private Cloud (VPC)** - Provides network isolation
    * **Kinesis Video Streams** - Handles real-time audio streaming
    * **IAM Roles and Permissions** - Controls access between services
    * **Lambda functions** - These functions will handle communication between Amazon Connect and GenerativeAgent
  </Accordion>
* Receive the GenerativeAgent Connect Flow and Prompts from your ASAPP team.

The components used in the example integration are **intended for testing environments**. You can use your own components in Production when you integrate GenerativeAgent.

<Note>
  This guide uses files from the [GenerativeAgent Amazon Connect - Code Samples](https://github.com/asappinc/generativeagent-amazon-connect) repository.
</Note>

## Step 1: Set up your AWS Account and Amazon Connect instance

You need to set up your AWS Account and configure AWS services that will be used for an Amazon Connect flow that engages GenerativeAgent. You will configure the flow in a future step.

### Provide a dedicated VPC

All components of the GenerativeAgent Amazon Connect integration must be in the same VPC.

You can use an existing VPC or create a new one:

* **To use an existing VPC:** Verify it has at least two subnets in different Availability Zones, and that the subnets are private and isolated (not connected to the Internet).
* **To create a new VPC:** In the AWS Console, go to **VPC > Your VPCs**, click **Create VPC**, and follow the prompts to set up a VPC with at least two private isolated subnets in different Availability Zones.

### Configure your Amazon Connect instance

To connect your Amazon Connect instance with an Amazon Kinesis Video Stream service, follow these steps:

1. **Navigate to Live Media Storage**
   * In the AWS Console, navigate to **Amazon Connect** and select your Amazon Connect instance by clicking on the Instance alias.
   * On the left menu, go to **Data storage > Live Media Storage**.

2. **Enable Live Media Streaming**
   * Under Data Storage options, enable **Live Media Streaming**.

3. **Set Retention Period**
   * Set a retention period of at least **1 hour**.

4. **Save the Kinesis Video Stream Instance Prefix**
   * Copy the **Kinesis video stream instance prefix**; you will need this when you [Configure IAM Roles and Policies](#step-3%3A-configure-iam-roles-and-policies).

<Frame>
  <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LiveMediaStreaming.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=38c801eeebc335c69e19de04c9dc6eea" data-og-width="1293" width="1293" data-og-height="647" height="647" data-path="images/generativeagent/LiveMediaStreaming.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LiveMediaStreaming.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=dbcb3607595cd1041bb1e8aa8780aa0d 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LiveMediaStreaming.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=96c79cb75d3fad160bcc6eefd0ef4149 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LiveMediaStreaming.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=583c9bb872942626405e850e494f3547 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LiveMediaStreaming.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=40e74946c476e39bff66655756112a50 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LiveMediaStreaming.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=b10d5fc8debd5222c62ea4c643b78139 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LiveMediaStreaming.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=fff4e32aa3e8d4db7ae59c379830986b 2500w" />
</Frame>

<Note>
  The access to the Kinesis Video Streams service is [controlled by IAM policies](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-iam).

  GenerativeAgent uses an IAM role in the ASAPP account to assume the IAM role you configure as part of this guide.
  The IAM role you configure must trust GenerativeAgent IAM role and provide permissions to access Kinesis Video Streams.
  See more in [Configuring IAM Roles and Policies](#step-3%3A-configure-iam-roles-and-policies)
</Note>

### Create security groups

You will need three security groups: one for Valkey ElastiCache, one for the PullAction Lambda function, and one for the PushAction Lambda function.

1. **Create all three security groups**
   * In the AWS Console, navigate to **VPC > Security Groups**.
   * For each of the following, click **Create security group**, using these names (or similar):
     * `ValkeyElastiCacheSecurityGroup`
     * `PullActionLambdaSecurityGroup`
     * `PushActionLambdaSecurityGroup`
   * Associate each security group with your VPC.
   * Save the security group IDs for later use.

2. **Configure security group rules**
   * **Valkey ElastiCache security group:**
     * **Inbound rules:**
       * Allow TCP traffic on port 6379 from the PullAction Lambda security group.
       * Allow TCP traffic on port 6379 from the PushAction Lambda security group.
     * **Outbound rules:**
       * No outbound rules are required. Remove any default outbound rules.

   * **PullAction Lambda security group:**
     * **Outbound rules:**
       * Allow TCP traffic on port 6379 to the Valkey ElastiCache security group.
       * Remove any other default outbound rules.

   * **PushAction Lambda security group:**
     * **Outbound rules:**
       * Allow TCP traffic on port 6379 to the Valkey ElastiCache security group.
       * Remove any other default outbound rules.

<Tip>
  You will use these security groups when setting up the [Lambda functions](#step-2-create-lambda-functions-to-call-generativeagent).
</Tip>

### Create the Valkey ElastiCache

The Amazon Connect Flow uses ElastiCache (Valkey engine) to store ordered list of actions for each call.
Follow these steps to create and configure your Valkey Cache in AWS ElastiCache:

1. **Create a subnet group**

   * In the AWS Console, navigate to **ElastiCache > Subnet groups**.
   * Click **Create subnet group**.
   * Enter a name and description for your subnet group (e.g., `ValkeySubnetGroup`).
   * Select your VPC.
   * Add both of your private isolated subnets (each in a different Availability Zone) to the group.
   * Save the subnet group.

2. **Create a Valkey ElastiCache**

   * In the AWS Console, navigate to **ElastiCache**.
   * In the left menu, select **Valkey caches**.
   * Click the **Create cache** button at the top right.

3. **Configure Settings**

   3.1 **Configuration**

   * **Engine:** Select **Valkey**.
   * **Deployment option:** Choose **Design your own cache**.
   * **Creation method:** Select **Cluster cache**.
   * **Cluster mode:** Set to **Disabled**.
   * **Cluster info:** Enter a name (e.g., `asapp-generativeagent`), up to 40 characters.
   * **Location:** Choose **AWS Cloud**.
   * **Multi-AZ:** Leave **Enabled**.

   3.2 **Cache settings**

   * **Engine version, Port, Parameter groups:** Leave default values.
   * **Node type:** For testing, select `cache.t4g.micro`. Adjust sizing based on your expected call volume before production.
   * **Number of replicas:** Set to **1**.

   3.3. **Connectivity**

   * **Subnet group:** Choose the existing subnet group you created previously.

   3.4. **Availability Zone placements**

   * **Availability Zone placements**: Select **No preference**.

   Click **Next** to proceed to Advanced settings.

4. **Configure Advanced Settings**

   4.1 **Security**

   * **Encryption at rest:** Enable
   * **Encryption in transit:** Disable
   * **Selected security groups:** Click **Manage** and select the security groups created earlier in the [Create security groups](#create-security-groups) section.
   * **Backups:** Uncheck **Enable automatic backups**.
   * **Maintenance:** Leave default options.
   * **Logs:** Leave default options.

   Click **Next** to review your configuration.

5. **Review and Create**

   * Review all settings.
   * Click **Create** to provision your Valkey Cache.

   Once created, save the **Primary endpoint**—you will use this value as `PRIMARY_VALKEY_HOST` and `PRIMARY_VALKEY_PORT` when configuring your [Lambda functions](#step-2%3A-create-lambda-functions-to-call-generativeagent).

   <Frame>
     <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ClusterDetails.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=3987b194d390f6c2cdffc426e6a571c2" data-og-width="1077" width="1077" data-og-height="570" height="570" data-path="images/generativeagent/ClusterDetails.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ClusterDetails.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=dfbf121844cc33696586d73982633bd1 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ClusterDetails.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=514e380515530af3c297c78baa42a710 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ClusterDetails.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=34d694a155703fb48385d430be8b5f2f 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ClusterDetails.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=fff5cd2b3bbc66fe24356d58f5cb7c94 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ClusterDetails.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=8d1bf0898dc953a25dbb78f54f3aad6b 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ClusterDetails.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=eb0fb5d9d94223b8ab51e09691de7fef 2500w" />
   </Frame>

<Tip>
  This guide provides setup suggestions, but the final configuration is up to you.

  [Learn more about Amazon ElastiCache for Valkey here](https://aws.amazon.com/elasticache/what-is-valkey/)
</Tip>

## Step 2: Create Lambda functions to call GenerativeAgent

The GenerativeAgent Flow Module expects certain Lambda functions to exist to interact with GenerativeAgent.

You will need to create the following Lambda functions:

* Engage
* PushAction
* PullAction

<Note>
  Lambda functions are delivered in `Node.js 22.x`.

  For other languages such as Go or Python, contact your ASAPP team.
</Note>

### Engage Lambda Function

This Lambda function sends REST API requests to ASAPP and engages GenerativeAgent into a conversation.

To create a Lambda function from the AWS Console:

<Steps>
  <Step title="Create the Lambda function">
    Navigate to **AWS Console > Lambda > Create function**.

    Choose **Author from scratch** and fill in the required fields as described below.

    <Tabs>
      <Tab title="Basic Information">
        * **Function name:** Choose a name (e.g., `asapp-generativeagent-engage`)
        * **Runtime:** The Lambda sample is delivered in `Node.js 22.x`.
        * **Architecture:** `x86_64`.
      </Tab>

      <Tab title="Execution Role">
        * Under **Change default execution role**, select **"Create a new role with basic Lambda permissions"**. This option automatically adds the necessary permissions for basic Lambda execution and CloudWatch logging.
        * If you are creating the Lambda function using infrastructure-as-code tools (such as Terraform), you must ensure the following permissions are included in the execution role:
          * Allow `logs:CreateLogStream` and `logs:PutLogEvents` for all streams under your CloudWatch Log Group.
          * Allow `lambda:InvokeFunction` action in your resource base policy.
          * List `connect.amazonaws.com` as the Principal Service in your resource policy. Also list `AWS:SourceArn` as the ARN of your Amazon Connect in the Conditions table.
      </Tab>

      <Tab title="VPC and Security Groups">
        * Under **Additional configurations**, ensure that **Enable VPC** is **disabled**. `Engage` only connects to Internet endpoints, so **do not attach it to a VPC**.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Create and Save ARN">
    Click **Create function**.

    Once the `Engage` Lambda function is created, **Save the ARN** of the Lambda function.

    You will need this ARN when editing the GenerativeAgent Flow Module JSON in the [Create GenerativeAgent Flow Module](#create-generativeagent-flow-module) section.
  </Step>

  <Step title="Upload the code">
    With the Lambda function created, go to the **Code** tab, click **Upload from**, and upload the `.zip` file containing the Lambda function code.

    You can find the Lambda function code for Engage in the repository at:\
    [Engage Lambda function code](https://github.com/asappinc/generativeagent-amazon-connect/tree/main/lambdas/engage)

    <Note>
      If you need to pass additional [`input variables`](https://docs.asapp.com/generativeagent/configuring/tasks-and-functions/input-variables) from Amazon Connect to GenerativeAgent, update the [`attributesToInputVariables.mjs`](https://github.com/asappinc/generativeagent-amazon-connect/blob/main/lambdas/engage/attributesToInputVariables.mjs) file in the Engage Lambda function **before uploading your Lambda code**.\
      This file controls how Amazon Connect Contact Attribute names are mapped to GenerativeAgent input variable names.\
      You can find a sample mapping in the [Engage Lambda README](https://github.com/asappinc/generativeagent-amazon-connect/tree/main/lambdas/engage#sample-attributestoinputvariablesmjs-contents), which is part of the repository.
    </Note>
  </Step>

  <Step title="Add environment variables">
    After uploading the code, go to the **Configuration** tab, then select **Environment variables** from the left menu.\
    Add the required environment variables for the Lambda function.

    | Name               | Description            | Value                                          |
    | :----------------- | :--------------------- | :--------------------------------------------- |
    | ASAPP\_API\_HOST   | Base URL for ASAPP API | [https://api.asapp.com](https://api.asapp.com) |
    | ASAPP\_API\_ID     | App-Id credential      | Provided by ASAPP                              |
    | ASAPP\_API\_SECRET | App-Secret credential  | Provided by ASAPP                              |
  </Step>
</Steps>

### PullAction Lambda Function

This Lambda function is called by the Amazon Connect Flow and queries Valkey for the next actions of a specific call.\
The call identifier is the `contactId` taken from the `Event.ContactData`.

<Tip>
  When the `PullAction` Lambda function is created, **Save the ARN** of the Lambda function.

  You will need this ARN when editing the GenerativeAgent Flow Module JSON in the [Create GenerativeAgent Flow Module](#create-generativeagent-flow-module) section.
</Tip>

<Steps>
  <Step title="Create the Lambda function">
    Navigate to **AWS Console > Lambda > Create function**.

    Choose **Author from scratch** and fill in the required fields as described below.

    <Tabs>
      <Tab title="Basic Information">
        * **Function name:** Choose a name (e.g., `asapp-generativeagent-pullaction`)
        * **Runtime:** The Lambda sample is delivered in `Node.js 22.x`.
        * **Architecture:** `x86_64`.
      </Tab>

      <Tab title="Execution Role">
        * Under **Change default execution role**, select **"Create a new role with basic Lambda permissions"**.
        * This option automatically adds the necessary permissions for basic Lambda execution and CloudWatch logging.
        * If you are creating the Lambda function manually or using infrastructure-as-code tools (such as Terraform), you must ensure the following permissions are included in the execution role:
          * Allow `logs:CreateLogStream` and `logs:PutLogEvents` for all streams under your CloudWatch Log Group.
          * Allow `lambda:InvokeFunction` action in your resource base policy.
          * For VPC access, proper permissions should be part of the execution role as described in the [AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html).
          * Generally, using the `AWSLambdaVPCAccessExecutionRole` managed policy is enough.
      </Tab>

      <Tab title="VPC and Security Groups">
        * Under **Additional configurations**, enable **VPC** and select the VPC where your Valkey ElastiCache is deployed.
        * Assign the `PullActionLambdaSecurityGroup` you created earlier to this Lambda function.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Create and Save ARN">
    Click **Create function**.

    Once the `PullAction` Lambda function is created, **Save the ARN** of the Lambda function.

    You will need this ARN when editing the GenerativeAgent Flow Module JSON in the [Create GenerativeAgent Flow Module](#create-generativeagent-flow-module) section.
  </Step>

  <Step title="Upload the code">
    With the Lambda function created, go to the **Code** tab, click **Upload from**, and upload the `.zip` file containing the Lambda function code.

    You can find the Lambda function code for PullAction in the repository at:\
    [PullAction Lambda function code](https://github.com/asappinc/generativeagent-amazon-connect/tree/main/lambdas/pullaction)
  </Step>

  <Step title="Add environment variables">
    After uploading the code, go to the **Configuration** tab, then select **Environment variables** from the left menu.\
    Add the required environment variables for the Lambda function:

    | Name         | Description                                 | Value                   |
    | :----------- | :------------------------------------------ | :---------------------- |
    | VALKEY\_HOST | Hostname of the Valkey Cache (primary node) | `[PRIMARY_VALKEY_HOST]` |
    | VALKEY\_PORT | Port of the Valkey Cache (primary node)     | `[PRIMARY_VALKEY_PORT]` |

    <Note>
      Use the primary endpoint created in the [Valkey ElastiCache](#create-the-valkey-elasticache-cache) for the `VALKEY_HOST` and `VALKEY_HOST`.

      Be sure to enter only the hostname part for `VALKEY_HOST` and only the port number for `VALKEY_PORT`.
    </Note>
  </Step>
</Steps>

### PushAction Lambda Function

ASAPP calls this Lambda function to communicate a further action for each call GenerativeAgent is engaging.\
This function also pushes next actions into Valkey for `PullAction` to query at the next opportunity.

<Tip>
  When the `PushAction` Lambda function is created, **Save the ARN** of the Lambda function.

  You will need this ARN when editing the GenerativeAgent Flow Module JSON in the [Create GenerativeAgent Flow Module](#create-generativeagent-flow-module) section.
</Tip>

<Steps>
  <Step title="Create the Lambda function">
    Navigate to **AWS Console > Lambda > Create function**.

    Choose **Author from scratch** and fill in the required fields as described below.

    <Tabs>
      <Tab title="Basic Information">
        * **Function name:** Choose a name (e.g., `asapp-generativeagent-pushaction`)
        * **Runtime:** The Lambda sample is delivered in `Node.js 22.x`.
        * **Architecture:** Default (`x86_64`)
      </Tab>

      <Tab title="Execution Role">
        * Under **Change default execution role**, select **"Create a new role with basic Lambda permissions"**. This option automatically adds the necessary permissions for basic Lambda execution and CloudWatch logging.
        * If you are creating the Lambda function manually or using infrastructure-as-code tools (such as Terraform), you must ensure the following permissions are included in the execution role:
          * Allow `logs:CreateLogStream` and `logs:PutLogEvents` for all streams under your CloudWatch Log Group.
          * Allow `lambda:InvokeFunction` action in your resource base policy.
          * For VPC access, proper permissions should be part of the execution role as described in the [AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html).
          * Generally, using the `AWSLambdaVPCAccessExecutionRole` managed policy is enough.
      </Tab>

      <Tab title="VPC and Security Groups">
        * Under **Additional configurations**, enable **VPC** and select the VPC where your Valkey ElastiCache is deployed.
        * Assign the `PushActionLambdaSecurityGroup` you created earlier to this Lambda function.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Create and Save ARN">
    Click **Create function**.

    Once the `PushAction` Lambda function is created, **Save the ARN** of the Lambda function.

    You will need this ARN when editing the GenerativeAgent Flow Module JSON in the [Create GenerativeAgent Flow Module](#create-generativeagent-flow-module) section.
  </Step>

  <Step title="Upload the code">
    With the Lambda function created, go to the **Code** tab, click **Upload from**, and upload the `.zip` file containing the Lambda function code.

    You can find the Lambda function code for PushAction in the repository at:\
    [PushAction Lambda function](https://github.com/asappinc/generativeagent-amazon-connect/tree/main/lambdas/pushaction)
  </Step>

  <Step title="Add environment variables">
    After uploading the code, go to the **Configuration** tab, then select **Environment variables** from the left menu.\
    Add the required environment variables for the Lambda function:

    | Name         | Description                                 | Value                   |
    | :----------- | :------------------------------------------ | :---------------------- |
    | VALKEY\_HOST | Hostname of the Valkey Cache (primary node) | `[PRIMARY_VALKEY_HOST]` |
    | VALKEY\_PORT | Port of the Valkey Cache (primary node)     | `[PRIMARY_VALKEY_PORT]` |

    <Note>
      Use the primary endpoint created in the [Valkey ElastiCache](#create-the-valkey-elasticache-cache) for the `VALKEY_HOST` and `VALKEY_HOST`.

      Be sure to enter only the hostname part for `VALKEY_HOST` and only the port number for `VALKEY_PORT`.
    </Note>
  </Step>
</Steps>

## Step 3: Configure IAM Roles and Policies

As part of this integration, ASAPP services will reach out to your AWS account to invoke the Lambda functions and access the Kinesis Video Streams.

ASAPP will need to assume a role in your AWS account to access these services.

We will provide you with the ARN of ASAPP's GenerativeAgent role. You need to create an IAM role for ASAPP to assume and specify the ARN of the IAM role in the trust policy.

To create an IAM role from the AWS Console:

<Steps>
  <Step title="Create the IAM role">
    1. Navigate to **IAM > Roles > Create role**.
    2. Choose **Custom trust policy** and paste the following policy:

       ```json  theme={null}
       {
           "Version": "2012-10-17",
           "Statement": [
               {
                   "Sid": "TrustASAPPRole",
                   "Effect": "Allow",
                   "Principal": {
                       "AWS": "[asapp-assuming-role-arn]"
                   },
                   "Action": "sts:AssumeRole"
               }
           ]
       }

       ```

       <Note>
         Replace the `[asapp-assuming-role-arn]` placeholder with the value provided by ASAPP.

         If there are multiple ARNs to trust, create multiple statements with unique Sid values and ASAPP provided ARN values in each statement.
       </Note>

       Click **Next**.
    3. Skip the **Permissions** screen, don't immediately add permissions, instead you will add them after creation.

       Click **Next** again.
    4. In the **Name, review, and create** screen, enter a role name (for example, `ASAPPGenerativeAgentRole`).

       Review your settings, and click **Create role**.
  </Step>

  <Step title="Add Kinesis Video Stream access">
    Add Kinesis Video Stream access to the IAM role by creating the following inline permissions policy:

    ```json  theme={null}
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "ReadAmazonConnectStreams",
                "Effect": "Allow",
                "Action": [
                    "kinesisvideo:GetDataEndpoint",
                    "kinesisvideo:GetMedia",
                    "kinesisvideo:DescribeStream"
                ],
                "Resource": "arn:aws:kinesisvideo:*:[customer-account-id]:stream/[kinesis-video-streams-prefix]*/*"
            },
            {
                "Sid": "ListAllStreams",
                "Effect": "Allow",
                "Action": "kinesisvideo:ListStreams",
                "Resource": "*"
            }
        ]
    }
    ```

    <Note>
      Replace the `[customer-account-id]` with your AWS Account number and `[kinesis-video-streams-prefix]` with the value saved in the [Configure your Amazon Connect instance](#configure-your-amazon-connect-instance) step.
    </Note>
  </Step>

  <Step title="Add Lambda function access">
    Add Lambda function access to the IAM role by creating the following inline permissions policy.
    This will allow the ASAPP service to invoke Lambda functions:

    ```json  theme={null}
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "Stmt1",
                "Effect": "Allow",
                "Action": [
                    "lambda:InvokeFunction"
                ],
                "Resource": [
                    "[lambda-pushaction-arn]"
                ]
            }
        ]
    }
    ```

    <Note>
      Replace the `[lambda-pushaction-arn]` placeholder with the ARN of the [`PushAction` Lambda function](#pushaction).
    </Note>
  </Step>

  <Step title="Share the IAM role ARN with ASAPP">
    ASAPP will use the ARN to interact with the `PushAction` Lambda function and Kinesis Video Streams.
  </Step>
</Steps>

## Step 4: Add Prompts and the GenerativeAgent Flow Module

With the relevant components in place, you need to create or update a flow to use the GenerativeAgent Flow Module to engage GenerativeAgent.

### Upload the Prompts

The GenerativeAgent Flow Module requires specific prompts during the conversation.

To upload the prompts:

1. **Download the prompt files**

   Download the required `.wav` prompt files from the following repository:
   [Prompt audio files](https://github.com/asappinc/generativeagent-amazon-connect/tree/main/flow-modules/prompts)

   ```
     asappBeepBop.wav
     asappSilence1second.wav
     asappSilence400ms.wav
   ```

2. **Upload and name each prompt in Amazon Connect**

   In your Amazon Connect instance, navigate to **Routing > Prompts**.

   For each `.wav` file:

   * Click **Add prompt**.
   * Upload the file.
   * When prompted for the name, enter the file name without the `.wav` extension:
     ```
       asappBeepBop
       asappSilence1second
       asappSilence400ms
     ```

3. **Save the prompt ARNs**

   After uploading each prompt, save the ARN for each prompt.

   You will need these ARNs when editing the GenerativeAgent Flow Module JSON in the [Create GenerativeAgent Flow Module](#create-generativeagent-flow-module) section.

### Create GenerativeAgent Flow Module

The GenerativeAgent Flow Module will handle the conversation between the customer and GenerativeAgent.

To create the GenerativeAgent Flow Module in your Amazon Connect instance:

1. **Download the Module JSON**
   * Download the `ASAPPGenerativeAgent.json` flow module json from the repository: [ASAPP GenerativeAgent Flow Module](https://github.com/asappinc/generativeagent-amazon-connect/blob/main/flow-modules/template/ASAPPGenerativeAgent.json)

2. **Edit the Module JSON**
   Open the `.json` file and update the ARNs to reference your own Lambda functions:
   * Replace the ARN for the `Engage` Lambda function with the ARN you created in [Step 2: Engage](#engage-lambda-function).
   * Replace the ARN for the `PullAction` Lambda function with the ARN you created in [Step 2: PullAction](#pullaction-lambda-function).
   * Locate the section with `"Identifier": "Wait1sPrompt"` and, within its `"Parameters"`, replace the `"PromptId"` string value with your `asappSilence1second` prompt ARN.
   * Locate the section with `"Identifier": "Wait400msPrompt"` and, within its `"Parameters"`, replace the `"PromptId"` string value with your `asappSilence400ms` prompt ARN.
   * Locate the section with `"Identifier": "PlayBeepBopShort"` and, within its `"Parameters"`, replace the `"PromptId"` string value with your `asappBeepBop` prompt ARN.

3. **Import the Module**
   * In your Amazon Connect instance, navigate to **Routing > Flows > Modules**.
   * Click **Create flow module**.
   * Expand the **Save** dropdown and select **Import**.
   * Upload your edited `.json` file and click **Import**.

4. **Verify the Module**
   * Ensure the imported module appears in your list and references the correct Lambda ARNs.

### Invoke the GenerativeAgent Flow Module

To hand off a conversation to GenerativeAgent, you need to invoke the GenerativeAgent Flow Module.

Most companies have many flows with nuanced logic and it is entirely up to you on when you engage the GenerativeAgent Flow Module.

Once you have determined where within your flows you want to hand off a conversation to GenerativeAgent, you need to:

<Steps>
  <Step title="Configure Contact Attributes">
    Before invoking the module, you must set up the required contact attributes:

    1. **Add a "Set contact attributes" block** to your flow
    2. **Configure the following attributes**:

    | Contact Attribute     | Required | Description                                                                                                                                                                                                                                           |
    | :-------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `ASAPP_companyMarker` | Yes      | Your company's unique identifier in GenerativeAgent                                                                                                                                                                                                   |
    | Custom attributes     | No       | The additional attributes to pass to GenerativeAgent for the [task to enter](/generativeagent/configuring/tasks-and-functions/enter-specific-task) and additional [input variables](/generativeagent/configuring/tasks-and-functions/input-variables) |

    <Note>
      The `ASAPP_companyMarker` is provided by ASAPP along with your API credentials. Contact your ASAPP team if you need this value.
    </Note>

    <Accordion title="Mapping Custom Attributes">
      To pass custom data to GenerativeAgent:

      1. **Add the attributes** to your "Set contact attributes" block
      2. **Update the mapping** in the `Engage` Lambda function:

         * The mapping between Amazon Connect Contact Attribute names and GenerativeAgent input variable names is defined in the [`attributesToInputVariables.mjs`](https://github.com/asappinc/generativeagent-amazon-connect/blob/main/lambdas/engage/attributesToInputVariables.mjs) file in the `Engage` Lambda function.
         * In this file, add a mapping of the contact attribute name to the GenerativeAgent input variable name.
           * The key is the attribute name in Amazon Connect, the value is the input variable name passed to generative GenerativeAgent.
         * Providing a value of `taskName` will be set as the [task](/generativeagent/configuring/tasks-and-functions/enter-specific-task) for GenerativeAgent to enter.

           * All other fields will be added as [input variables](/generativeagent/configuring/tasks-and-functions/input-variables).

      As an example, here contact attributes of `InitialTask` is mapped to `taskName` and `AccountNumber` is mapped to `CustomerAccountNumber` for input variables.

      ```javascript  theme={null}
      export default 
      {
          "InitialTask": "taskName",
          "CustomerAccountNumber": "AccountNumber"
      }
      ```
    </Accordion>
  </Step>

  <Step title="Invoke the GenerativeAgent Flow Module">
    Create an "Invoke module" block and select the GenerativeAgent Flow Module. This is where the conversation is handed off to GenerativeAgent.

    <Frame>
      <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InvokeModule.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=4825356aece341e0d692c1618d9315b8" data-og-width="1378" width="1378" data-og-height="691" height="691" data-path="images/generativeagent/InvokeModule.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InvokeModule.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=2ece0788fe0bfaacc8477afcd03a3931 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InvokeModule.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=791cf1314388243cd6eb426686a0ea15 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InvokeModule.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=7ac174df245a143a16db319a08bd36d2 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InvokeModule.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=ebc61d3774e8bdcc24ebe841897a6c19 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InvokeModule.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=60e2108373bc9d3b15111f0aece3cca6 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InvokeModule.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=d9c29dab3a1af719fe435804626c2e33 2500w" />
    </Frame>

    Within the GenerativeAgent Flow Module, the flow will use the various components you created in previous steps to engage ASAPP's GenerativeAgent to the end user.

    Once the conversation is complete, GenerativeAgent will exit the Module and return control to your flow.
  </Step>

  <Step title="Handle the result">
    The GenerativeAgent Flow Module will exit for one of four reasons, and will output the `ASAPP_Disposition` contact attribute with one of the following values:

    * `transferToAgent`: when the conversation needs to be transferred to an agent
    * `transferToSystem`: when the conversation needs to be transferred to an external system
    * `disengage`: when the conversation is completed
    * `error`: when an error has occurred
  </Step>

  <Step title="Map output Variables">
    After importing the Flow Module, you may want to extract `transferVariables` from the [system transfer](/generativeagent/configuring/tasks-and-functions/system-transfer) from GenerativeAgent for use in your flow.

    <Note>As of now, only `transferVariables` from system transfer are supported.</Note>

    To use the `transferVariables` in your flow:

    * In the imported Flow Module, locate the block named `ExtractOutputVariables`.
    * For each output variable, specify the key as `$.External.outputVariables.<variableName>` where `<variableName>` is the name of the output variable you want to extract.

      * As an example, if the transfer variable is `CustomerAccountNumber`, the key would be `$.External.outputVariables.CustomerAccountNumber`.
    * Save the flow.
    * In the flow invoking the GenerativeAgent Flow Module, the variables are available in the flow as contact attributes. Use them in your flow as needed.
  </Step>
</Steps>

## Step 5: Engage GenerativeAgent

Now you are ready to make a call and engage GenerativeAgent.

Call the phone number configured in your Contact Flow and follow the prompts until you reach the point where GenerativeAgent is engaged. You should see the conversation transition to GenerativeAgent based on where you placed the GenerativeAgent Flow Module in your flow.

Verify that:

1. You are handed off to GenerativeAgent
2. GenerativeAgent responds appropriately to your inputs
3. You are returned to your flow when the conversation ends

<Note>
  This integration is a good starting point for your integration with GenerativeAgent. You need to further configure the integration to meet your organization's requirements.
</Note>

## Next Steps

Now that you have integrated GenerativeAgent with Amazon Connect, here are some important next steps to consider:

<CardGroup>
  <Card title="Configuration Overview" href="/generativeagent/configuring">
    Learn how to configure GenerativeAgent's behaviors, tasks, and communication style
  </Card>

  <Card title="Connect your APIs" href="/generativeagent/configuring/connect-apis">
    Configure your APIs to allow GenerativeAgent to access necessary data and perform actions
  </Card>

  <Card title="Review Knowledge Base" href="/generativeagent/configuring/connecting-your-knowledge-base">
    Connect and optimize your knowledge base to improve GenerativeAgent's responses
  </Card>

  <Card title="Go Live" href="/generativeagent/go-live">
    Follow the deployment checklist to launch GenerativeAgent in your production environment
  </Card>
</CardGroup>
