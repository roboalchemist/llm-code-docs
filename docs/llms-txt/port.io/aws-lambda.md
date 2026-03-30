# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws-v3/resource-and-property-reference/aws-lambda.md

# AWS Lambda

<!-- -->

## AWS::Lambda::Function[â](#awslambdafunction "Direct link to AWS::Lambda::Function")

The following example demonstrates how to ingest your AWS Lambda functions to Port.

#### Lambda Function supported actions[â](#lambda-function-supported-actions "Direct link to Lambda Function supported actions")

The table below summarizes the available actions for ingesting AWS Lambda Function resources in Port:

| Action                                                                                      | Description                                            | Type     | Required AWS Permission |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------ | -------- | ----------------------- |
| [ListFunctionsAction](https://docs.aws.amazon.com/lambda/latest/api/API_ListFunctions.html) | Discover all Lambda functions across your AWS account. | Default  | `lambda:ListFunctions`  |
| [ListTagsAction](https://docs.aws.amazon.com/lambda/latest/api/API_ListTags.html)           | Retrieve tags for each function.                       | Optional | `lambda:ListTags`       |

Optional Properties Note

Properties of optional actions will not appear in the response unless you explicitly include the action that provides them in your configuration.

You can use the following Port blueprint definitions and integration configuration:

**Lambda Function blueprint (click to expand)**

Create in Port

```
{
  "identifier": "lambdaFunction",
  "title": "Lambda Function",
  "icon": "AWS",
  "schema": {
    "properties": {
      "FunctionName": {
        "type": "string",
        "title": "Function Name",
        "description": "The name of the Lambda function"
      },
      "FunctionArn": {
        "type": "string",
        "title": "Function ARN",
        "description": "The Amazon Resource Name (ARN) of the Lambda function"
      },
      "Runtime": {
        "type": "string",
        "title": "Runtime",
        "description": "The runtime environment for the Lambda function"
      },
      "Handler": {
        "type": "string",
        "title": "Handler",
        "description": "The function entry point"
      },
      "MemorySize": {
        "type": "number",
        "title": "Memory Size",
        "description": "The amount of memory available to the function in MB"
      },
      "Timeout": {
        "type": "number",
        "title": "Timeout",
        "description": "The function execution time limit in seconds"
      },
      "State": {
        "type": "string",
        "title": "State",
        "description": "The current state of the function"
      },
      "LastModified": {
        "type": "string",
        "title": "Last Modified",
        "description": "The date and time the function was last modified"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": false,
      "many": false
    }
  }
}
```

**Lambda Function mapping configuration (click to expand)**

```
resources:
  - kind: AWS::Lambda::Function
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .Properties.FunctionArn
          title: .Properties.FunctionName
          blueprint: '"lambdaFunction"'
          properties:
            FunctionName: .Properties.FunctionName
            FunctionArn: .Properties.FunctionArn
            Runtime: .Properties.Runtime
            Handler: .Properties.Handler
            MemorySize: .Properties.MemorySize
            Timeout: .Properties.Timeout
            State: .Properties.State
            LastModified: .Properties.LastModified
          relations:
            account: .__ExtraContext.AccountId
```

For more details about Lambda function properties, refer to the [AWS Lambda API documentation](https://docs.aws.amazon.com/lambda/latest/api/welcome.html).
