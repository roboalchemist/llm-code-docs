# Source: https://docs.aws.amazon.com/step-functions/latest/dg/llms.txt

# AWS Step Functions Developer Guide

> Describes how to build workflows and orchestrate services with AWS Step Functions.

- [What is Step Functions?](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- [Use cases](https://docs.aws.amazon.com/step-functions/latest/dg/use-cases.html)
- [Getting started tutorial](https://docs.aws.amazon.com/step-functions/latest/dg/getting-started.html)
- [State machines](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-statemachines.html)
- [Activities](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-activities.html)
- [Choosing workflow type](https://docs.aws.amazon.com/step-functions/latest/dg/choosing-workflow-type.html)
- [Handling errors](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html)
- [Troubleshooting](https://docs.aws.amazon.com/step-functions/latest/dg/troubleshooting.html)
- [Best practices](https://docs.aws.amazon.com/step-functions/latest/dg/sfn-best-practices.html)
- [Service quotas](https://docs.aws.amazon.com/step-functions/latest/dg/service-quotas.html)
- [Recent feature launches](https://docs.aws.amazon.com/step-functions/latest/dg/recent-launches.html)
- [Document history](https://docs.aws.amazon.com/step-functions/latest/dg/document-history.html)

## [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html)

- [State machine structure](https://docs.aws.amazon.com/step-functions/latest/dg/statemachine-structure.html): Learn about the common fields to define state machines in Step Functions using Amazon States Language.
- [Intrinsic functions](https://docs.aws.amazon.com/step-functions/latest/dg/intrinsic-functions.html): Learn about using intrinsic functions to perform basic data processing tasks in Step Functions workflows.


## [Workflow states](https://docs.aws.amazon.com/step-functions/latest/dg/workflow-states.html)

- [Task](https://docs.aws.amazon.com/step-functions/latest/dg/state-task.html): Learn how to use the Task workflow state to represent a single unit of work performed by a state machine in your Step Functions workflows.
- [Choice](https://docs.aws.amazon.com/step-functions/latest/dg/state-choice.html): Learn how to use the Choice workflow state to add conditional logic to a state machine in your Step Functions workflows.
- [Parallel](https://docs.aws.amazon.com/step-functions/latest/dg/state-parallel.html): Learn how to use the Parallel workflow state to add separate branches of execution in your Step Functions workflows.

### [Map](https://docs.aws.amazon.com/step-functions/latest/dg/state-map.html)

Learn how to use the Map workflow state to run a set of steps in your Step Functions workflows.

- [Inline mode](https://docs.aws.amazon.com/step-functions/latest/dg/state-map-inline.html): Learn how to use the Map state in Inline mode, a low-concurrency mode that runs in the context as its parent Step Functions workflow.
- [Distributed mode](https://docs.aws.amazon.com/step-functions/latest/dg/state-map-distributed.html): Use the Map state in Distributed mode to orchestrate large-scale parallel workloads in your state machines to perform tasks in Step Functions.
- [Pass](https://docs.aws.amazon.com/step-functions/latest/dg/state-pass.html): Learn how to use the Pass workflow state to pass its input to its output, without performing work, in your Step Functions state machine workflows.
- [Wait](https://docs.aws.amazon.com/step-functions/latest/dg/state-wait.html): Learn how to use the Wait workflow state to delay the state machine from continuing for a specified time in your Step Functions workflows.
- [Succeed](https://docs.aws.amazon.com/step-functions/latest/dg/state-succeed.html): Learn how to use the Succeed workflow state to successfully stop the execution of the state machine in your Step Functions workflows.
- [Fail](https://docs.aws.amazon.com/step-functions/latest/dg/state-fail.html): Learn how to use the Fail workflow state to stop the execution of the state machine and marks it as a failure in your Step Functions workflows.


## [Tutorials and Workshops](https://docs.aws.amazon.com/step-functions/latest/dg/learning-resources.html)

- [Handle error conditions](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-handling-error-conditions.html): Create an AWS Step Functions state machine to handle error conditions using a Catch field for a Task states.
- [Create a state machine using AWS SAM](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-state-machine-using-sam.html): Download, build, and deploy a sample AWS SAM application that contains an AWS Step Functions state machine.
- [Examine executions](https://docs.aws.amazon.com/step-functions/latest/dg/debug-sm-exec-using-ui.html): Examine a failed state machine execution using the information available on the Execution Details page of the Step Functions console.
- [Create a state machine that uses Lambda](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-creating-lambda-state-machine.html): Create a single-step workflow using AWS Step Functions to invoke an AWS Lambda function.
- [Wait for human approval](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-human-approval.html): Deploy a AWS CloudFormation stack that shows an example human approval Step Functions workflow that pauses during a task and waits for a user to respond.
- [Repeat actions with Inline Map](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-map-inline.html): Use the Map state in Inline mode to repeatedly perform an action.
- [Copy large-scale CSV using Distributed Map](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-map-distributed.html): Learn how to use the Map state in Distributed mode to iteratively process large volumes of data.
- [Iterate a loop with Lambda](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-create-iterate-pattern-section.html): Learn how to create a Step Functions state machine that uses an AWS Lambda function to iterate a count during a loop.
- [Process batch data with Lambda](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-itembatcher-param-task.html): Learn how to process an entire batch of data with a Lambda function in a Step Functions workflow.
- [Process individual items with Lambda](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-itembatcher-single-item-process.html): Learn how to iterate over individual items in a batch with each invocation of a Lambda function in a Step Functions workflow.
- [Start a workflow from EventBridge](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-cloudwatch-events-s3.html): Learn how to start an AWS Step Functions state machine execution using an Amazon EventBridge rule that reacts to AWS service events.
- [Create an API using API Gateway](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-api-gateway.html): Associate your Step Functions APIs with an API Gateway API, so that when an HTTPS request is sent to an API method, API Gateway invokes Step Functions API actions.
- [Create an Activity state machine](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-creating-activity-state-machine.html): Learn how to create an activity-based state machine using Java and AWS Step Functions.
- [View X-Ray traces](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-xray-traces.html): Learn how to use X-Ray to trace errors that occur when running a Step Functions state machine.
- [Gather Amazon S3 bucket info](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-gather-s3-info.html): Learn how to perform an AWS SDK integration to gather information about your Amazon S3 buckets and their versioning information.
- [Continue long-running workflows using Step Functions API (recommended)](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-continue-new.html): Learn how to continue long-running executions from a Step Functions Task state to avoid exceeding quotas.
- [Using Lambda to continue a workflow](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-use-lambda-cont-exec.html): Learn how to start executions of a state machine with a Lambda function.
- [Access cross-account resources](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-access-cross-acct-resources.html): Learn the steps to access AWS resources available across multiple AWS accounts.


## [Starter templates](https://docs.aws.amazon.com/step-functions/latest/dg/starter-templates.html)

- [Manage a container task](https://docs.aws.amazon.com/step-functions/latest/dg/sample-project-container-task-notification.html): Deploy a state machine that runs an AWS Fargate task and sends an Amazon SNS notification.
- [Transfer data records](https://docs.aws.amazon.com/step-functions/latest/dg/sample-project-transfer-data-sqs.html): Deploy a state machine that reads items from an Amazon DynamoDB table and sends them to an Amazon SQS queue.
- [Job poller](https://docs.aws.amazon.com/step-functions/latest/dg/sample-project-job-poller.html): Deploy a state machine that submits an AWS Batch job and uses Lambda to check on the job status.
- [Task timer](https://docs.aws.amazon.com/step-functions/latest/dg/task-timer-sample.html): Deploy a state machine that sends an Amazon SNS notification using Lambda after waiting for a specific period of time.
- [Callback pattern example](https://docs.aws.amazon.com/step-functions/latest/dg/callback-task-sample-sqs.html): Deploy a state machine that sends a message to Amazon SQS and pauses the workflow until it receives a callback from an external caller.
- [Manage an Amazon EMR job](https://docs.aws.amazon.com/step-functions/latest/dg/sample-emr-job.html): Deploy a state machine that creates an Amazon EMR cluster and then terminates the cluster.
- [Run an EMR Serverless job](https://docs.aws.amazon.com/step-functions/latest/dg/sample-emr-serverless-job.html): Create and start an Amazon EMR Serverless application, and then run two jobs in that application.
- [Start a workflow within a workflow](https://docs.aws.amazon.com/step-functions/latest/dg/sample-start-workflow.html): Deploy a sample project that creates a state machine which starts the execution of another state machine.
- [Process data with a Map](https://docs.aws.amazon.com/step-functions/latest/dg/sample-map-state.html): Deploy a sample project that creates a state machine which demonstrates dynamic parallelism using a Map state.
- [Distributed Map to process a CSV file in S3](https://docs.aws.amazon.com/step-functions/latest/dg/sample-dist-map-csv-process.html): Learn how to use the Distributed Map state to iterate over the rows of a CSV file with a sample project.
- [Distributed Map to process files in S3](https://docs.aws.amazon.com/step-functions/latest/dg/sample-dist-map-s3data-process.html): Learn how to use the Distributed Map state to process large amounts of data stored in an Amazon S3 bucket.
- [Train a machine learning model](https://docs.aws.amazon.com/step-functions/latest/dg/sample-train-model.html): Learn how to train a machine learning model in SageMaker AI and batch transform a test dataset.
- [Tune a machine learning model](https://docs.aws.amazon.com/step-functions/latest/dg/sample-hyper-tuning.html): Learn how to tune the hyperparameters of a machine learning model and batch transform a test dataset.
- [Perform AI prompt-chaining with Amazon Bedrock](https://docs.aws.amazon.com/step-functions/latest/dg/sample-bedrock-prompt-chaining.html): Learn how to use AI prompt chaining with Amazon Bedrock to build high-quality chatbots.
- [Process high-volume messages from SQS](https://docs.aws.amazon.com/step-functions/latest/dg/sample-project-express-high-volume-sqs.html): Learn how to use an Express workflow state machine to process Amazon SQS message at a very high rate
- [Selective checkpointing example](https://docs.aws.amazon.com/step-functions/latest/dg/sample-project-express-selective-checkpointing.html): Learn how to combine Standard and Express state machines to run an e-commerce workflow with selective checkpointing
- [Start a CodeBuild build](https://docs.aws.amazon.com/step-functions/latest/dg/sample-project-codebuild.html): Learn how to build a CodeBuild project and send a notification using Amazon SNS based on the results
- [Preprocess data and train a machine learning model](https://docs.aws.amazon.com/step-functions/latest/dg/sample-preprocess-feature-transform.html): Learn how to apply feature standardization on training data and train a machine learning model with SageMaker AI
- [Orchestrate Lambda functions](https://docs.aws.amazon.com/step-functions/latest/dg/sample-lambda-orchestration.html): Learn how to orchestrate serverless functions using a stock-trading workflow with a human approval step.
- [Start an Athena query](https://docs.aws.amazon.com/step-functions/latest/dg/sample-athena-query.html): Learn how to start an Athena query and send a notification with the results using Amazon SNS.
- [Execute queries in sequence and parallel using Athena](https://docs.aws.amazon.com/step-functions/latest/dg/run-multiple-queries.html): Learn how to execute Athena queries in sequence and parallel with error handling and notifications
- [Query large datasets](https://docs.aws.amazon.com/step-functions/latest/dg/sample-query-large-datasets.html): Learn how to use an AWS Glue crawler to ingest data to Amazon S3 then submit an Athena query and send results to Amazon SNS
- [Keep data up to date](https://docs.aws.amazon.com/step-functions/latest/dg/sample-keep-data-updated.html): Learn how to use a Step Functions state machine to keep a target table up to date using AWS Glue catalog and Athena
- [Manage an Amazon EKS cluster](https://docs.aws.amazon.com/step-functions/latest/dg/sample-eks-cluster.html): Learn how to create an Amazon EKS cluster with a node group, run a job, and then delete the node group and cluster.
- [Make a call to API Gateway](https://docs.aws.amazon.com/step-functions/latest/dg/sample-apigateway-workflow.html): Learn how to interact with an API managed by API Gateway using Step Functions
- [Call a microservice with API Gateway](https://docs.aws.amazon.com/step-functions/latest/dg/sample-apigateway-ecs-workflow.html): Learn how to make a call to an API Gateway endpoint that fronts an Amazon ECS container microservice
- [Send a custom event to EventBridge](https://docs.aws.amazon.com/step-functions/latest/dg/sample-eventbridge-custom-event.html): Learn how to send a custom event to an EventBridge event bus that matches with a rule with multiple targets
- [Invoke Synchronous Express Workflows through API Gateway](https://docs.aws.amazon.com/step-functions/latest/dg/synchronous-execution.html): Learn how to invoke Synchronous Express Workflows through API Gateway to manage an employee database
- [ETL job in Amazon Redshift](https://docs.aws.amazon.com/step-functions/latest/dg/sample-etl-orchestration.html): Learn how to use Step Functions and the Amazon Redshift Data API to run an ETL/ELT workflow that loads data into the Amazon Redshift data warehouse
- [Manage a batch job](https://docs.aws.amazon.com/step-functions/latest/dg/batch-job-notification.html): Deploy a state machine that submits an AWS Batch job and sends an Amazon SNS notification.
- [Fan out a batch job](https://docs.aws.amazon.com/step-functions/latest/dg/sample-batch-fan-out.html): Learn how to fan out a batch job with Map state using Step Functions, AWS Batch, and Lambda
- [Batch job with Lambda](https://docs.aws.amazon.com/step-functions/latest/dg/sample-batch-lambda.html): Learn how to use Step Functions to run a batch job with Lambda for pre-processing input data


## [Developing workflows](https://docs.aws.amazon.com/step-functions/latest/dg/developing-workflows.html)

### [Using Workflow Studio](https://docs.aws.amazon.com/step-functions/latest/dg/workflow-studio.html)

Learn how to use Step Functions Workflow Studio to build workflows with a visual editor.

- [Create a workflow](https://docs.aws.amazon.com/step-functions/latest/dg/workflow-studio-create.html): Using Workflow Studio to create a workflow in Step Functions
- [Configure input and output](https://docs.aws.amazon.com/step-functions/latest/dg/workflow-studio-process.html): Configure inputs and outputs for Step Functions workflow states in Workflow Studio.
- [Set up execution roles](https://docs.aws.amazon.com/step-functions/latest/dg/manage-state-machine-permissions.html): You can use Workflow Studio to set up execution roles for your workflows.
- [Configure error handling](https://docs.aws.amazon.com/step-functions/latest/dg/workflow-studio-process-error.html): Configure error handling with the Workflow Studio visual editor in Step Functions
- [Using Workflow Studio in Infrastructure Composer](https://docs.aws.amazon.com/step-functions/latest/dg/use-wfs-in-app-composer.html): Use Workflow Studio in Infrastructure Composer to build serverless workflows using AWS CloudFormation templates.
- [Using AWS SAM](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-sam-sfn.html): You can use AWS Serverless Application Model for a unified infrastructure and code experience to build and deploy state machines in Step Functions.
- [Create a state machine with CloudFormation](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-lambda-state-machine-cloudformation.html): Learn how to create an Step Functions AWS Lambda state machine with CloudFormation.
- [Using CDK to create a Standard workflow](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-lambda-state-machine-cdk.html): Learn how to create an Step Functions workflow that integrates with an AWS Lambda function using AWS CDK.
- [Using CDK to create an Express workflow](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-step-functions-rest-api-integration-cdk.html): Learn how to create an Amazon API Gateway REST API with synchronous express state machine as backend integration using AWS CDK.
- [Using Terraform to deploy workflows](https://docs.aws.amazon.com/step-functions/latest/dg/terraform-sfn.html): Describes the development lifecycle for using Terraform to create and deploy a Step Functions state machine.
- [Exporting to IaC templates](https://docs.aws.amazon.com/step-functions/latest/dg/exporting-iac-templates.html): The AWS Step Functions console can export a saved workflow as an IaC template file in either a CloudFormation or AWS SAM template.


## [Starting state machines](https://docs.aws.amazon.com/step-functions/latest/dg/statemachine-starting.html)

- [Start from a Task](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-nested-workflows.html): Learn how to use Step Functions to start a new Step Functions workflow execution from a task state of a state machine.
- [Using EventBridge Scheduler](https://docs.aws.amazon.com/step-functions/latest/dg/using-eventbridge-scheduler.html): Use Amazon EventBridge Scheduler to create a schedule that invokes a state machine execution in Step Functions.
- [Viewing workflow runs](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-view-execution-details.html): View and debug in-progress and past executions for workflows using the information displayed in the Step Functions console.
- [Redriving state machines](https://docs.aws.amazon.com/step-functions/latest/dg/redrive-executions.html): Continue unsuccessful state machine executions from their point of failure using redrive in Step Functions.
- [Viewing Map Runs](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html): Learn about the information displayed on a Map Run Details page.
- [Redriving Map Runs](https://docs.aws.amazon.com/step-functions/latest/dg/redrive-map-run.html): Restart unsuccessful child workflow executions in a Map Run using redrive.


## [Processing input and output](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-input-output-filtering.html)

- [Passing data with variables](https://docs.aws.amazon.com/step-functions/latest/dg/workflow-variables.html): With state output and variables, you can pass information across the lifecycle of your workflow.
- [Transforming data with JSONata](https://docs.aws.amazon.com/step-functions/latest/dg/transforming-data.html): With JSONata, you can transform data from state to state.
- [Context object](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-contextobject.html): Use the Context object to enable your workflow to access information about their specific execution in Step Functions.
- [Using JSONPath paths](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-paths.html): Use paths to access subsets of input when specifying values for InputPath, ResultPath, and OutputPath in Step Functions workflows.
- [Manipulate parameters with paths](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html): Use the InputPath, Parameters and ResultSelector fields to manipulate JSON data as it flows through workflow states.
- [Example: Manipulating state data with paths](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-example.html): See an example of how to manipulate state input and output JSON using InputPath, ResultPath, and OutputPath in Step Functions workflows.
- [Specify state output with paths](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-resultpath.html): Use the ResultPath field to control the combination of input and result that is passed to the state output in Step Functions workflows.

### [Map state configuration](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-fields-dist-map.html)

Learn how to use Map fields configure the input and output for Distributed Map state in Step Functions.

- [ItemReader](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-itemreader.html): Learn how to override the input values for each Map state iteration using the ItemReader field in Step Functions.
- [ItemsPath (JSONPath)](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-itemspath.html): Use the ItemsPath field to select an array within a JSON input provided to a Map state in a Step Functions workflow.
- [ItemSelector](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-itemselector.html): Learn how to override the input values for each Map state iteration using the ItemSelector field in Step Functions.
- [ItemBatcher](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-itembatcher.html): Learn how to process a group of items in each child workflow execution using the ItemBatcher field in Step Functions.
- [ResultWriter](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-resultwriter.html): Learn how to export the Map state results to an Amazon S3 bucket using ResultWriter in Step Functions.
- [Parsing input CSV files](https://docs.aws.amazon.com/step-functions/latest/dg/example-csv-parse-dist-map.html): Learn how Step Functions parses a CSV file provided as an input dataset.


## [Integrating services](https://docs.aws.amazon.com/step-functions/latest/dg/integrate-services.html)

- [AWS SDK integrations](https://docs.aws.amazon.com/step-functions/latest/dg/supported-services-awssdk.html): AWS Step Functions integrates with AWS services, so you can call service's API actions from your workflows.
- [Service integration patterns](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html): Discover the Step Functions integration patterns to use services directly in Amazon States Language.
- [Call HTTPS APIs](https://docs.aws.amazon.com/step-functions/latest/dg/call-https-apis.html): Learn how to call any HTTPS API, including SaaS applications, in your state machines using the HTTP Task.
- [Pass parameters](https://docs.aws.amazon.com/step-functions/latest/dg/connect-parameters.html): Use the Parameters field in a Task state to control what is passed to a service API in Step Functions


## [Integrating optimized services](https://docs.aws.amazon.com/step-functions/latest/dg/integrate-optimized.html)

- [Amazon API Gateway](https://docs.aws.amazon.com/step-functions/latest/dg/connect-api-gateway.html): Learn how to integrate Step Functions with API Gateway using a Task state to create REST APIs
- [Amazon Athena](https://docs.aws.amazon.com/step-functions/latest/dg/connect-athena.html): Learn how to integrate Step Functions with Amazon Athena to start and stop queries and get results
- [AWS Batch](https://docs.aws.amazon.com/step-functions/latest/dg/connect-batch.html): Learn how to integrate Step Functions with AWS Batch to run batch computing workloads in the AWS cloud
- [Amazon Bedrock](https://docs.aws.amazon.com/step-functions/latest/dg/connect-bedrock.html): Learn how to integrate Step Functions with Amazon Bedrock to invoke and customize models
- [AWS CodeBuild](https://docs.aws.amazon.com/step-functions/latest/dg/connect-codebuild.html): Learn how to integrate Step Functions with AWS CodeBuild to trigger, stop, and manage builds
- [Amazon DynamoDB](https://docs.aws.amazon.com/step-functions/latest/dg/connect-ddb.html): Learn how to integrate Step Functions with DynamoDB to perform CRUD operations on a table
- [Amazon ECS/Fargate](https://docs.aws.amazon.com/step-functions/latest/dg/connect-ecs.html): Learn how to integrate Step Functions with Amazon ECS or Fargate to run and manage tasks.
- [Amazon EKS](https://docs.aws.amazon.com/step-functions/latest/dg/connect-eks.html): Learn how to integrate Step Functions with Amazon EKS to manage Kubernetes clusters.
- [Amazon EMR](https://docs.aws.amazon.com/step-functions/latest/dg/connect-emr.html): Learn how to integrate Step Functions with Amazon EMR to manage clusters.
- [Amazon EMR on EKS](https://docs.aws.amazon.com/step-functions/latest/dg/connect-emr-eks.html): Learn how to integrate Step Functions with Amazon EMR on EKS to manage clusters.
- [Amazon EMR Serverless](https://docs.aws.amazon.com/step-functions/latest/dg/connect-emr-serverless.html): Learn to create and manage EMR Serverless applications using Step Functions
- [Amazon EventBridge](https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html): Learn how to integrate Step Functions with EventBridge to add EventBridge events using PutEvents API.
- [AWS Glue](https://docs.aws.amazon.com/step-functions/latest/dg/connect-glue.html): Learn how to integrate Step Functions with AWS Glue to start a job run.
- [AWS Glue DataBrew](https://docs.aws.amazon.com/step-functions/latest/dg/connect-databrew.html): Learn how to start an AWS Glue DataBrew job using Step Functions.
- [AWS Lambda](https://docs.aws.amazon.com/step-functions/latest/dg/connect-lambda.html): Learn how to integrate Step Functions with Lambda to invoke Lambda functions
- [AWS Elemental MediaConvert](https://docs.aws.amazon.com/step-functions/latest/dg/connect-mediaconvert.html): Learn how to integrate Step Functions with AWS Elemental MediaConvert to create a MediaConvert job
- [Amazon SageMaker AI](https://docs.aws.amazon.com/step-functions/latest/dg/connect-sagemaker.html): Learn how to integrate Step Functions with SageMaker AI to create and manage jobs
- [Amazon SNS](https://docs.aws.amazon.com/step-functions/latest/dg/connect-sns.html): Learn how to integrate Step Functions with Amazon SNS to publish messages to a topic
- [Amazon SQS](https://docs.aws.amazon.com/step-functions/latest/dg/connect-sqs.html): Learn how to integrate Step Functions with Amazon SQS to send messages to a queue
- [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-stepfunctions.html): Learn how to start a new execution of a Step Functions state machine from a running execution


## [Securing state machines](https://docs.aws.amazon.com/step-functions/latest/dg/security.html)

### [Data protection](https://docs.aws.amazon.com/step-functions/latest/dg/data-protection.html)

Learn how to configure encryption at rest with customer managed AWS KMS keys in AWS Step Functions.

- [Data at rest encryption](https://docs.aws.amazon.com/step-functions/latest/dg/encryption-at-rest.html): Adding a layer of encryption by choosing a customer managed key to encrypt workflows, activities, and logs.
- [Data in transit encryption](https://docs.aws.amazon.com/step-functions/latest/dg/encryption-in-transit.html): Step Functions encrypts data in transit between the service and other integrated AWS services (see ).

### [Identity and Access Management](https://docs.aws.amazon.com/step-functions/latest/dg/auth-and-access-control-sfn.html)

Learn how to write a policy and how AWS evaluates policies to decide to grant requester access to resources.

- [How AWS Step Functions works with IAM](https://docs.aws.amazon.com/step-functions/latest/dg/security_iam_service-with-iam.html): Before you use IAM to manage access to Step Functions, learn what IAM features are available to use with Step Functions.
- [Identity-based policy examples](https://docs.aws.amazon.com/step-functions/latest/dg/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Step Functions resources.
- [AWS managed policies](https://docs.aws.amazon.com/step-functions/latest/dg/security-iam-awsmanpol.html): Learn about AWS managed policies for Step Functions and recent changes to those policies.
- [Creating a state machine IAM role](https://docs.aws.amazon.com/step-functions/latest/dg/procedure-create-iam-role.html): Learn how to create an IAM role for your state machine in AWS Step Functions.
- [Creating granular permissions for non-admin users](https://docs.aws.amazon.com/step-functions/latest/dg/concept-create-iam-advanced.html): Creating granular IAM permissions for non-admin users in Step Functions
- [Accessing cross-account AWS resources](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-access-cross-acct-resources.html): Learn how to access AWS resources available across multiple AWS accounts in Step Functions
- [Create VPC endpoints](https://docs.aws.amazon.com/step-functions/latest/dg/vpc-endpoints.html): Access your AWS Step Functions resources directly from Amazon Virtual Private Cloud endpoints.
- [IAM Policies for integrated services](https://docs.aws.amazon.com/step-functions/latest/dg/service-integration-iam-templates.html): Learn about how Step Functions creates IAM policies for services that integrate with AWS Step Functions.
- [IAM policies for Distributed Maps](https://docs.aws.amazon.com/step-functions/latest/dg/iam-policies-eg-dist-map.html): View examples of IAM policies with least privileges necessary that allow Step Functions to run a Distributed Map state and access Amazon S3 resources.
- [Creating tag-based policies](https://docs.aws.amazon.com/step-functions/latest/dg/tag-based-policies.html): Create tag-based IAM policies to allow or deny access to Step Functions resources.
- [Troubleshooting identity and access](https://docs.aws.amazon.com/step-functions/latest/dg/security_iam_troubleshoot.html): Find information for troubleshooting issues around permissions, policies, and other identity and access control problems in Step Functions.


## [Logging and monitoring](https://docs.aws.amazon.com/step-functions/latest/dg/monitoring-logging.html)

- [Metrics in CloudWatch](https://docs.aws.amazon.com/step-functions/latest/dg/procedure-cw-metrics.html): Learn how to monitor Step Functions reliability, availability, and performance using metrics available to Amazon CloudWatch.
- [Automate event delivery](https://docs.aws.amazon.com/step-functions/latest/dg/eventbridge-integration.html): With EventBridge, you can select events from Step Functions, such as resource creation or deletion, to send to other services for additional processing.
- [API calls in CloudTrail](https://docs.aws.amazon.com/step-functions/latest/dg/procedure-cloud-trail.html): Learn about logging AWS Step Functions API calls with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service.
- [Logging in CloudWatch Logs](https://docs.aws.amazon.com/step-functions/latest/dg/cw-logs.html): Learn how to configure logging execution history for Standard and Express Workflows in Step Functions using Amazon CloudWatch Logs.
- [Trace data in X-Ray](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-xray-tracing.html): Use AWS X-Ray to trace requests as they are executed in Step Functions, including viewing service maps and searchable trace summaries.
- [Events using User Notifications](https://docs.aws.amazon.com/step-functions/latest/dg/using-user-notifications-sfn.html): Learn how to get notifications for AWS Step Functions using AWS User Notifications.


## [Testing and debugging](https://docs.aws.amazon.com/step-functions/latest/dg/test-and-debug.html)

- [Testing with TestState](https://docs.aws.amazon.com/step-functions/latest/dg/test-state-isolation.html): Use the TestState API to test and debug a Step Functions workflow state without creating a state machine or updating an existing state machine.

### [Step Functions Local (unsupported)](https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local.html)

Learn how to use Step Functions test Step Functions state machines in a local development environment.

- [Tutorial: Testing using Step Functions and AWS SAM CLI Local](https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local-lambda.html): Learn how to set up and test a state machine and Lambda function using AWS Step Functions and AWS Lambda on your local machine.
- [Testing with mocked service integrations](https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local-test-sm-exec.html): Learn how to test AWS Step Functions state machine executions locally without relying on the real AWS service endpoints by using mocked service integrations.


## [Versions and aliases](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-cd-aliasing-versioning.html)

- [Versions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html): Create and test versions of your state machine definition and gradually deploy them to the production environment i Step Functions.
- [Aliases](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html): Manage gradual, rolling, or canary deployment of your state machines using traffic shifting mechanism in Step Functions.
- [Versions and alias authorization](https://docs.aws.amazon.com/step-functions/latest/dg/auth-version-alias.html): Learn how authorization works for state machine versions and aliases in Step Functions, including how to scope down permissions for a version and/or alias.
- [Associating executions with a version or alias](https://docs.aws.amazon.com/step-functions/latest/dg/execution-alias-version-associate.html): Learn how Step Functions associates state machine executions with a version or an alias.
- [Deployment example](https://docs.aws.amazon.com/step-functions/latest/dg/example-alias-version-deployment.html): See an example of how to rollout a new state machine version with AWS CLI commands using Canary deployment technique.
- [Gradual deployment of versions](https://docs.aws.amazon.com/step-functions/latest/dg/version-rolling-deployment.html): Deploy a new state machine version by gradually shifting execution traffic from a previous state machine version to the new version.
