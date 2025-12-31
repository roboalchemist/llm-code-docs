# Aws Powertools Typescript Documentation

Source: https://docs.aws.amazon.com/powertools/typescript/latest/llms-full.txt

---

# Powertools for AWS Lambda (TypeScript)

> Powertools for AWS Lambda (TypeScript)

Powertools for AWS Lambda (TypeScript) is a developer toolkit to implement Serverless best practices and increase developer velocity. It provides a suite of utilities for AWS Lambda Functions that makes tracing with AWS X-Ray, structured logging and creating custom metrics asynchronously easier.

# Getting Started

You can use Powertools for AWS Lambda (TypeScript) by installing it with your favorite dependency management, or via [Lambda Layers](https://docs.aws.amazon.com/powertools/typescript/latest/getting-started/lambda-layers/index.md).

The toolkit is compatible with both TypeScript and JavaScript code bases, and supports both CommonJS and ES modules.

All features are available as individual packages, so you can install only the ones you need, for example:

- **Logger**: `npm i @aws-lambda-powertools/logger`
- **Event Handler**: `npm i @aws-lambda-powertools/event-handler`
- **Metrics**: `npm i @aws-lambda-powertools/metrics`
- **Tracer**: `npm i @aws-lambda-powertools/tracer`

See the [Features](https://docs.aws.amazon.com/powertools/typescript/latest/features/index.md) page for a complete list of available utilities.

## Extra dependencies

Some features use additional dependencies like the AWS SDK for JavaScript v3, which might you need to install separately. Below is a list of utilities that use external dependencies, and the packages you need to install to use them.

||Feature |Install |Default dependency || | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------- | ||**[Tracer](https://docs.aws.amazon.com/powertools/typescript/latest/features/tracer/index.md)** |**`npm i @aws-lambda-powertools/tracer`** |`aws-xray-sdk-core` || ||**[Idempotency](https://docs.aws.amazon.com/powertools/typescript/latest/features/idempotency/index.md)** |**`npm i @aws-lambda-powertools/idempotency @aws-sdk/client-dynamodb @aws-sdk/lib-dynamodb`** | || ||**[Parameters (SSM)](https://docs.aws.amazon.com/powertools/typescript/latest/features/parameters/index.md)** |**`npm i @aws-lambda-powertools/parameters @aws-sdk/client-ssm`** | || ||**[Parameters (Secrets Manager)](https://docs.aws.amazon.com/powertools/typescript/latest/features/parameters/index.md)** |**`npm i @aws-lambda-powertools/parameters @aws-sdk/client-secrets-manager`** | || ||**[Parameters (AppConfig)](https://docs.aws.amazon.com/powertools/typescript/latest/features/parameters/index.md)** |**`npm i @aws-lambda-powertools/parameters @aws-sdk/client-appconfigdata`** | || ||**[Parser](https://docs.aws.amazon.com/powertools/typescript/latest/features/parser/index.md)** |**`npm i @aws-lambda-powertools/parser zod`** | || ||**[Validation](https://docs.aws.amazon.com/powertools/typescript/latest/features/validation/index.md)** |**`npm i @aws-lambda-powertools/validation`** |`ajv` || ||**[Kafka (Protocol Buffers)](https://docs.aws.amazon.com/powertools/typescript/latest/features/kafka/index.md)** |**`npm i @aws-lambda-powertools/kafka protobufjs`** | || ||**[Kafka (Avro)](https://docs.aws.amazon.com/powertools/typescript/latest/features/kafka/index.md)** |**`npm i @aws-lambda-powertools/kafka avro-js`** | ||

Powertools for AWS Lambda (TypeScript) is a collection of utilities designed to help you build serverless applications on AWS.

The toolkit is modular, so you can pick and choose the utilities you need for your application, but also combine them for a complete solution for your serverless applications.

## Patterns

Many of the utilities provided can be used with different patterns, depending on your preferences and the structure of your code.

### Class Method Decorator

If you prefer writing your business logic using Object-Oriented Programming (OOP) and TypeScript Classes, the Class Method decorator pattern is a good fit. This approach lets you decorate class methods with Powertools utilities, applying their functionality with minimal code changes.

This pattern works well when you want to integrate Powertools for AWS into an existing codebase without significant refactoring and with no additional runtime dependencies.

Note

This approach relies on TypeScript's experimental decorator feature, see [TypeScript Settings](https://docs.aws.amazon.com/powertools/typescript/latest/getting-started/typescript-settings/index.md) for more information.

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Logger } from '@aws-lambda-powertools/logger';
import { Metrics } from '@aws-lambda-powertools/metrics';
import { Tracer } from '@aws-lambda-powertools/tracer';
import type { Context } from 'aws-lambda';

const logger = new Logger();
const tracer = new Tracer();
const metrics = new Metrics();

class Lambda implements LambdaInterface {
  @tracer.captureLambdaHandler()
  @logger.injectLambdaContext()
  @metrics.logMetrics()
  async handler(_event: unknown, _context: Context) {
    // Your business logic here
  }
}
const lambda = new Lambda();
export const handler = lambda.handler.bind(lambda);

```

All our decorators assume that the method they are decorating is asynchronous. This means that even when decorating a synchronous method, they will return a promise. If this is not the desired behavior, you can use one of the other patterns.

### Middy.js Middleware

If your existing codebase relies on the [Middy.js](https://middy.js.org/docs/) middleware engine, you can use the Powertools for AWS Lambda (TypeScript) middleware to integrate with your existing code. This approach is similar to the Class Method decorator pattern but uses the Middy.js middleware engine to apply Powertools utilities.

Note

We guarantee support for Middy.js `v5.x` and `v6.x`. Check Middy.js docs to learn more about [best practices](https://middy.js.org/docs/integrations/lambda-powertools#best-practices) when working with Powertools for AWS middlewares.

```
import { Logger } from '@aws-lambda-powertools/logger';
import { injectLambdaContext } from '@aws-lambda-powertools/logger/middleware';
import { Metrics } from '@aws-lambda-powertools/metrics';
import { logMetrics } from '@aws-lambda-powertools/metrics/middleware';
import { Tracer } from '@aws-lambda-powertools/tracer';
import { captureLambdaHandler } from '@aws-lambda-powertools/tracer/middleware';
import middy from '@middy/core';

const logger = new Logger();
const tracer = new Tracer();
const metrics = new Metrics();

export const handler = middy()
  .use(captureLambdaHandler(tracer))
  .use(injectLambdaContext(logger))
  .use(logMetrics(metrics))
  .handler(async (_event: unknown) => {
    // Your business logic here
  });

```

### Functional Approach

If you prefer a more functional programming style, you can use the Powertools for AWS Lambda (TypeScript) utilities directly in your code without decorators or middleware. This approach is more verbose but provides the most control over how the utilities are applied.

```
import { Logger } from '@aws-lambda-powertools/logger';
import { Metrics } from '@aws-lambda-powertools/metrics';
import { Tracer } from '@aws-lambda-powertools/tracer';
import type { Context } from 'aws-lambda';

const logger = new Logger();
const tracer = new Tracer();
const metrics = new Metrics();

export const handler = async (event: unknown, context: Context) => {
  logger.addContext(context);
  logger.logEventIfEnabled(event);

  const subsegment = tracer.getSegment()?.addNewSubsegment('#### handler');

  try {
    // Your business logic here
    throw new Error('An error occurred');
  } catch (error) {
    logger.error('Error occurred', { error });
    tracer.addErrorAsMetadata(error as Error);
    throw error;
  } finally {
    subsegment?.close();
    metrics.publishStoredMetrics();
  }
};

```

While you can use the toolkit with JavaScript, using TypeScript is recommended.

The toolkit is written in TypeScript with bundled type definitions. We officially support TypeScript 5.0+ and recommend using the latest version to benefit from all features and improvements.

## TypeScript Configuration

If you use class method decorators, you must set `experimentalDecorators: true` in your tsconfig.json. This is because we currently support only the legacy decorator syntax. Support for the new decorator syntax will come in our next major release.

The following `tsconfig.json` file is a good place to start and includes the recommended settings along with some modern TypeScript features.

```
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": [
      "es2022"
    ],
    "declaration": true,
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "noImplicitThis": true,
    "alwaysStrict": true,
    "noUnusedLocals": false,
    "noUnusedParameters": false,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": false,
    "inlineSourceMap": true,
    "inlineSources": true,
    "experimentalDecorators": true,
    "strictPropertyInitialization": false
  },
  "exclude": [
    "node_modules"
  ]
}

```

A [Lambda Layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) is a `.zip` file archive that can contain additional code, pre-packaged dependencies, data, or configuration files. We provide a Lambda Layer for Powertools for AWS Lambda (TypeScript) to help you get started quickly with the library.

You can add our layer both in the [AWS Lambda Console *(under `Layers`)*](https://docs.aws.amazon.com/lambda/latest/dg/adding-layers.html), or via your favorite infrastructure as code framework with the ARN value. You can use the Lambda Layer both with CommonJS and ESM (ECMAScript modules).

## Layer ARNs

We publish the Lambda Layer for Powertools for AWS Lambda in all commercial regions and AWS GovCloud (US) regions.

Spotted a missing region?

Open an [issue](https://github.com/aws-powertools/powertools-lambda-typescript/issues/new?template=feature_request.yml&title=Feature%20request%3A%20missing%20Lambda%20layer%20region) in our GitHub repository to request it.

| Region           | Layer ARN                                                                                      |
| ---------------- | ---------------------------------------------------------------------------------------------- |
| `us-east-1`      | [arn:aws:lambda:us-east-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)            |
| `us-east-2`      | [arn:aws:lambda:us-east-2:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)            |
| `us-west-1`      | [arn:aws:lambda:us-west-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)            |
| `us-west-2`      | [arn:aws:lambda:us-west-2:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)            |
| `ap-south-1`     | [arn:aws:lambda:ap-south-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)           |
| `ap-south-2`     | [arn:aws:lambda:ap-south-2:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)           |
| `ap-east-1`      | [arn:aws:lambda:ap-east-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)            |
| `ap-northeast-1` | [arn:aws:lambda:ap-northeast-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)       |
| `ap-northeast-2` | [arn:aws:lambda:ap-northeast-2:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)       |
| `ap-northeast-3` | [arn:aws:lambda:ap-northeast-3:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)       |
| `ap-southeast-1` | [arn:aws:lambda:ap-southeast-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)       |
| `ap-southeast-2` | [arn:aws:lambda:ap-southeast-2:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)       |
| `ap-southeast-3` | [arn:aws:lambda:ap-southeast-3:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)       |
| `ap-southeast-4` | [arn:aws:lambda:ap-southeast-4:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)       |
| `ap-southeast-5` | [arn:aws:lambda:ap-southeast-5:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)       |
| `ap-southeast-7` | [arn:aws:lambda:ap-southeast-7:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)       |
| `eu-central-1`   | [arn:aws:lambda:eu-central-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)         |
| `eu-central-2`   | [arn:aws:lambda:eu-central-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)         |
| `eu-west-1`      | [arn:aws:lambda:eu-west-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)            |
| `eu-west-2`      | [arn:aws:lambda:eu-west-2:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)            |
| `eu-west-3`      | [arn:aws:lambda:eu-west-3:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)            |
| `eu-north-1`     | [arn:aws:lambda:eu-north-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)           |
| `eu-south-1`     | [arn:aws:lambda:eu-south-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)           |
| `eu-south-2`     | [arn:aws:lambda:eu-south-2:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)           |
| `ca-central-1`   | [arn:aws:lambda:ca-central-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)         |
| `ca-west-1`      | [arn:aws:lambda:ca-west-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)            |
| `sa-east-1`      | [arn:aws:lambda:sa-east-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)            |
| `af-south-1`     | [arn:aws:lambda:af-south-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)           |
| `me-south-1`     | [arn:aws:lambda:me-south-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)           |
| `me-central-1`   | [arn:aws:lambda:me-central-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)         |
| `il-central-1`   | [arn:aws:lambda:il-central-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)         |
| `mx-central-1`   | [arn:aws:lambda:mx-central-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)         |
| `us-gov-west-1`  | [arn:aws-us-gov:lambda:us-gov-west-1:165093116878:layer:AWSLambdaPowertoolsTypeScriptV2:41](#) |
| `us-gov-east-1`  | [arn:aws-us-gov:lambda:us-gov-east-1:165087284144:layer:AWSLambdaPowertoolsTypeScriptV2:41](#) |
| `cn-north-1`     | [arn:aws-aws-cn:lambda:cn-north-1:498634801083:layer:AWSLambdaPowertoolsTypeScriptV2:41](#)    |

### Lookup Layer ARN via AWS SSM Parameter Store

You can also use AWS SSM Parameter Store to dynamically add Powertools for AWS Lambda. The `{version}` placeholder is the semantic version number (e,g. 2.1.0) for a release or `_latest_`.

For example, to get the ARN for version `2.14.0` in the `eu-west-1` region, run the following command:

```
aws ssm get-parameter --name /aws/service/powertools/typescript/generic/all/2.14.0 --region eu-west-1

# output
Parameter:
  ARN: arn:aws:ssm:eu-west-1::parameter/aws/service/powertools/typescript/generic/all/2.14.0
  DataType: text
  LastModifiedDate: '2025-02-11T11:08:45.070000+01:00'
  Name: /aws/service/powertools/typescript/generic/all/2.14.0
  Type: String
  Value: arn:aws:lambda:eu-west-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41
  Version: 1

```

We currently publish SSM parameters for the following Powertools for AWS Lambda versions in all commercial regions:

- `/aws/service/powertools/typescript/generic/all/latest`: for the latest version of Powertools for AWS Lambda
- `/aws/service/powertools/typescript/generic/all/{version}`: for a specific version of Powertools for AWS Lambda (e.g. `2.14.0`)

See the [examples below](#how-to-use-with-infrastructure-as-code) for how to use the SSM parameter in your infrastructure as code.

### Want to inspect the contents of the Layer?

The pre-signed URL to download this Lambda Layer will be within `Location` key in the CLI output. The CLI output will also contain the Powertools for AWS Lambda version it contains.

Change `{aws::region}` to your AWS region, e.g. `eu-west-1`, and run the following command:

```
aws lambda get-layer-version-by-arn --arn arn:aws:lambda:{aws::region}:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41 --region {aws::region}

```

```
{  
    "Content": {
        "Location": "https://awslambda-eu-west-1-layers.s3.eu-west-1.amazonaws.com/...",
        "CodeSha256": "gwGIE8w0JckdDeDCTX6FbWObb2uIDwgiaAq78gMWDyA=",
        "CodeSize": 3548324
    },
    "LayerArn": "arn:aws:lambda:eu-west-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2",
    "LayerVersionArn": "arn:aws:lambda:eu-west-1:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41",
    "Description": "Powertools for AWS Lambda (TypeScript) version 2.18.0",
    "CreatedDate": "2025-04-08T07:38:30.424+0000",
    "Version": 24,
    "CompatibleRuntimes": [
        "nodejs20.x",
        "nodejs22.x",
        "nodejs24.x"
    ],
    "LicenseInfo": "MIT-0",
    "CompatibleArchitectures": [
        "arm64",
        "x86_64"
    ]
}

```

### How to use with Infrastructure as Code

```
import { Stack } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { LayerVersion, Function, Runtime, Code } from 'aws-cdk-lib/aws-lambda';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';

export class SampleFunctionWithLayer extends Construct {
  constructor(scope: Construct, id: string) {
    super(scope, id);

    // Create a Layer with Powertools for AWS Lambda (TypeScript)
    const powertoolsLayer = LayerVersion.fromLayerVersionArn(
      this,
      'PowertoolsLayer',
      `arn:aws:lambda:${Stack.of(this).region}:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41`
    );

    new NodejsFunction(this, 'Function', {
      runtime: Runtime.NODEJS_24_X,
      // Add the Layer to a Lambda function
      layers: [powertoolsLayer],
      code: Code.fromInline(`...`),
      handler: 'index.handler',
    });
  }
}

```

If you use `esbuild` to bundle your code, make sure to exclude `@aws-lambda-powertools/*` and `@aws-sdk/*` from being bundled since the packages are already present the layer:

```
new NodejsFunction(this, 'Function', {
  ...
  bundling: {
    externalModules: [
      '@aws-lambda-powertools/*',
      '@aws-sdk/*',
    ],
  }
});

```

Check the AWS CDK `NodeJsFunction` [documentation](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda_nodejs.BundlingOptions.html#externalmodules) for more details.

You can also use AWS SSM Parameter Store to dynamically resolve the Layer ARN from SSM Parameter Store and add the toolkit in your code, allowing you to pin to `latest` or a specific Powertools for AWS version.

```
import { Stack } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { LayerVersion, Function, Runtime, Code } from 'aws-cdk-lib/aws-lambda';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { StringParameter } from 'aws-cdk-lib/aws-ssm';

export class SampleFunctionWithLayer extends Construct {
  constructor(scope: Construct, id: string) {
    super(scope, id);

    // Create a Layer with Powertools for AWS Lambda (TypeScript)
    const powertoolsLayer = LayerVersion.fromLayerVersionArn(
      this,
      'PowertoolsLayer',
      StringParameter.valueForStringParameter(this, 'PowertoolsLayer', {
        parameterName: '/aws/service/powertools/typescript/generic/all/latest',
      })
    );

    new NodejsFunction(this, 'Function', {
      runtime: Runtime.NODEJS_24_X,
      // Add the Layer to a Lambda function
      layers: [powertoolsLayer],
      code: Code.fromInline(`...`),
      handler: 'index.handler',
    });
  }
}

```

```
MyLambdaFunction:
  Type: AWS::Serverless::Function
    Properties:
      Layers:
        - !Sub arn:aws:lambda:${AWS::Region}:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41

```

You can also use AWS SSM Parameter Store to dynamically add Powertools for AWS Lambda and resolve the Layer ARN from SSM Parameter Store in your code, allowing you to pin to `latest` or a specific Powertools for AWS Lambda version.

```
MyLambdaFunction:
  Type: AWS::Serverless::Function
    Properties:
      Layers:
        - {{resolve:ssm:/aws/service/powertools/typescript/generic/all/latest}}

```

If you use `esbuild` to bundle your code, make sure to exclude `@aws-lambda-powertools/*` and `@aws-sdk/*` from being bundled since the packages are already present the layer:

```
MyLambdaFunction:
  Type: AWS::Serverless::Function
  Properties:
    ...
    Metadata: 
      # Manage esbuild properties
      BuildMethod: esbuild
      BuildProperties:
      Minify: true
      External:
        - '@aws-lambda-powertools/*'
        - '@aws-sdk/*'

```

Check the [documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-build-typescript.html) for more details.

```
functions:
  hello:
    handler: lambda_function.lambda_handler
    layers:
      - arn:aws:lambda:${aws:region}:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41

```

If you use `esbuild` to bundle your code, make sure to exclude `@aws-lambda-powertools/*` and `@aws-sdk/*` from being bundled since the packages are already present the layer:

```
custom:
  esbuild:
    external:
      - '@aws-lambda-powertools/*'
      - '@aws-sdk/*'

```

Check the [documentation](https://floydspace.github.io/serverless-esbuild/) for more details.

```
terraform {
  required_version = "~> 1.0.5"
  required_providers {
    aws = "~> 3.50.0"
  }
}

provider "aws" {
  region  = "{aws::region}"
}

resource "aws_lambda_function" "test_lambda" {
  filename      = "lambda_function_payload.zip"
  function_name = "lambda_function_name"
  role          = ...
  handler       = "index.handler"
  runtime       = "nodejs24.x"
  layers        = ["arn:aws:lambda:{aws::region}:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41"]
  source_code_hash = filebase64sha256("lambda_function_payload.zip")
}

```

You can use [data sources](https://developer.hashicorp.com/terraform/language/data-sources) to resolve the SSM Parameter Store in your code, allowing you to pin to `latest` or a specific Powertools for AWS Lambda version.

```
  data "aws_ssm_parameter" "powertools_version" {
    # Replace {version} with your chosen Powertools for AWS Lambda version or latest
    name = "/aws/service/powertools/python/generic/all/latest"
  }

  resource "aws_lambda_function" "test_lambda" {
    ...

    runtime = "nodejs24.x"

    layers = [data.aws_ssm_parameter.powertools_version.value]
  }

```

```
import * as pulumi from '@pulumi/pulumi';
import * as aws from '@pulumi/aws';

const role = new aws.iam.Role('role', {
    assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal(aws.iam.Principals.LambdaPrincipal),
    managedPolicyArns: [aws.iam.ManagedPolicies.AWSLambdaBasicExecutionRole]
});

const lambdaFunction = new aws.lambda.Function('function', {
    layers: [
        pulumi.interpolate`arn:aws:lambda:${aws.getRegionOutput().name}:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41`
    ],
    code: new pulumi.asset.FileArchive('lambda_function_payload.zip'),
    tracingConfig: {
        mode: 'Active'
    },
    runtime: aws.lambda.Runtime.NodeJS24dX,
    handler: 'index.handler',
    role: role.arn,
    architectures: ['x86_64']
});

```

Remember to replace the region with your AWS region, e.g., `eu-west-1`. Amplify Gen 2 currently does not support obtaining the region dynamically.

```
import { defineFunction } from "@aws-amplify/backend";

export const myFunction = defineFunction({
  name: "my-function",
  layers: {
    "@aws-lambda-powertools/*":
      "arn:aws:lambda:${AWS::Region}:094274105915:layer:AWSLambdaPowertoolsTypeScriptV2:41",
  },
});

```

### Dependency management

When using the Lambda Layer, the Powertools for AWS Lambda packages are already included in your Lambda runtime environment. However, you still need to [install these packages](https://docs.aws.amazon.com/powertools/typescript/latest/getting-started/installation/index.md) locally for development, testing, and IDE support.

Since the packages are provided by the Lambda Layer at runtime, install them as `devDependencies` in your `package.json` file:

```
npm i -D @aws-lambda-powertools/logger

```

**Important considerations:**

- **Exclude from bundling**: Ensure your build process excludes these packages from your deployment bundle since they're provided by the layer
- **Version synchronization**: Keep your local development dependencies in sync with the Lambda Layer version to maintain consistency

Following these practices prevents version conflicts that can cause unexpected behavior, such as failed `instanceof` checks or inconsistent behavior between your local development environment and the Lambda execution environment.
# Features

Tracer is an opinionated thin wrapper for [AWS X-Ray SDK for Node.js](https://github.com/aws/aws-xray-sdk-node).

## Key features

- Auto-capturing cold start and service name as annotations, and responses or full exceptions as metadata.
- Automatically tracing HTTP(S) clients including `fetch` and generating segments for each request.
- Supporting tracing functions via decorators, middleware, and manual instrumentation.
- Supporting tracing AWS SDK v2 and v3 via AWS X-Ray SDK for Node.js.
- Auto-disable tracing when not running in the Lambda environment.

Tracer showcase - Handler Annotations

## Getting started

Tracer relies on AWS X-Ray SDK over [OpenTelemetry Distro (ADOT)](https://aws-otel.github.io/docs/getting-started/lambda) for optimal cold start (lower latency).

### Installation

Install the library in your project:

```
npm install @aws-lambda-powertools/tracer

```

### Usage

The `Tracer` utility must always be instantiated outside of the Lambda handler. In doing this, subsequent invocations processed by the same instance of your function can reuse these resources. This saves cost by reducing function run time. In addition, `Tracer` can track cold start and annotate the traces accordingly.

```
import { Tracer } from '@aws-lambda-powertools/tracer';

const tracer = new Tracer({ serviceName: 'serverlessAirline' });

export const handler = async () => {
  const segment = tracer.getSegment();
  const subsegment = segment?.addNewSubsegment('subsegment');
  subsegment?.addAnnotation('annotationKey', 'annotationValue');
  subsegment?.addMetadata('metadataKey', { foo: 'bar' });
  subsegment?.close();
};

```

#### Using with ESM?

Tracer relies on the AWS X-Ray SDK for Node.js, which is distributed as a CommonJS module and uses `require`.

To use it in an ESM project, you can instruct your bundler to use the `require` syntax for specific dependencies while using ESM for everything else. This is commonly known as [polyfill](https://developer.mozilla.org/en-US/docs/Glossary/Polyfill).

Code snippets for AWS CDK and AWS SAM CLI with `esbuild`

```
import { Stack, type StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { NodejsFunction, OutputFormat } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Runtime } from 'aws-cdk-lib/aws-lambda';

export class MyStack extends Stack {
public constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const handler = new NodejsFunction(this, 'helloWorldFunction', {
    runtime: Runtime.NODEJS_24_X,
    handler: 'handler',
    entry: 'src/index.ts',
    bundling: {
        format: OutputFormat.ESM,
        minify: true,
        esbuildArgs: {
        "--tree-shaking": "true",
        },
        banner: 
        "import { createRequire } from 'module';const require = createRequire(import.meta.url);", // (1)!
    },
    });
}
}

```

1. `esbuild` will include this arbitrary code at the top of your bundle to maximize CommonJS compatibility *(`require` keyword)*.

```
Transform: AWS::Serverless-2016-10-31
Resources:
HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
    Runtime: nodejs24.x
    Handler: src/index.handler
    Metadata:
    BuildMethod: esbuild
    BuildProperties:
        Minify: true
        Target: 'ES2020'
        Sourcemap: true
        Format: esm
        EntryPoints:
        - src/index.ts
        Banner:
        js: "import { createRequire } from 'module';const require = createRequire(import.meta.url);"  # (1)!

```

1. `esbuild` will include this arbitrary code at the top of your bundle to maximize CommonJS compatibility *(`require` keyword)*.

### Utility settings

The library has three optional settings. You can set them as environment variables, or pass them in the constructor:

| Setting                    | Description                                                           | Environment variable                       | Default             | Allowed Values    | Example             | Constructor parameter  |
| -------------------------- | --------------------------------------------------------------------- | ------------------------------------------ | ------------------- | ----------------- | ------------------- | ---------------------- |
| **Service name**           | Sets an annotation with the **name of the service** across all traces | `POWERTOOLS_SERVICE_NAME`                  | `service_undefined` | Any string        | `serverlessAirline` | `serviceName`          |
| **Tracing enabled**        | Enables or disables tracing.                                          | `POWERTOOLS_TRACE_ENABLED`                 | `true`              | `true` or `false` | `false`             | `enabled`              |
| **Capture HTTPs Requests** | Defines whether HTTPs requests will be traced or not                  | `POWERTOOLS_TRACER_CAPTURE_HTTPS_REQUESTS` | `true`              | `true` or `false` | `false`             | `captureHTTPsRequests` |
| **Capture Response**       | Defines whether functions responses are serialized as metadata        | `POWERTOOLS_TRACER_CAPTURE_RESPONSE`       | `true`              | `true` or `false` | `false`             | `captureResult`        |
| **Capture Errors**         | Defines whether functions errors are serialized as metadata           | `POWERTOOLS_TRACER_CAPTURE_ERROR`          | `true`              | `true` or `false` | `false`             | N/A                    |

Note

Before you use this utility, your AWS Lambda function must have [Active Tracing enabled](https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html) as well as [have permissions](https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html#services-xray-permissions) to send traces to AWS X-Ray

#### Example using AWS Serverless Application Model (SAM)

The `Tracer` utility is instantiated outside of the Lambda handler. In doing this, the same instance can be used across multiple invocations inside the same execution environment. This allows `Tracer` to be aware of things like whether or not a given invocation had a cold start or not.

```
import { Tracer } from '@aws-lambda-powertools/tracer';

// Tracer parameter fetched from the environment variables (see template.yaml tab)
const tracer = new Tracer();
tracer.getSegment();

// You can also pass the parameter in the constructor
// const tracer = new Tracer({
//     serviceName: 'serverlessAirline'
// });

```

```
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      Runtime: nodejs24.x
      Tracing: Active
      Environment:
        Variables:
          POWERTOOLS_SERVICE_NAME: serverlessAirline

```

### Lambda handler

You can quickly start by importing the `Tracer` class, initialize it outside the Lambda handler, and instrument your function.

```
import { Tracer } from '@aws-lambda-powertools/tracer';
import { captureLambdaHandler } from '@aws-lambda-powertools/tracer/middleware';
import middy from '@middy/core';

const tracer = new Tracer({ serviceName: 'serverlessAirline' });

const lambdaHandler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  tracer.putAnnotation('successfulBooking', true);
};

// Wrap the handler with middy
export const handler = middy(lambdaHandler)
  // Use the middleware by passing the Tracer instance as a parameter
  .use(captureLambdaHandler(tracer));

```

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Tracer } from '@aws-lambda-powertools/tracer';

const tracer = new Tracer({ serviceName: 'serverlessAirline' });

class Lambda implements LambdaInterface {
  // Decorate your handler class method
  @tracer.captureLambdaHandler()
  public async handler(_event: unknown, _context: unknown): Promise<void> {
    tracer.getSegment();
  }
}

const handlerClass = new Lambda();
export const handler = handlerClass.handler.bind(handlerClass); // (1)

```

1. Binding your handler method allows your handler to access `this`.

```
import { Tracer } from '@aws-lambda-powertools/tracer';
import type { Subsegment } from 'aws-xray-sdk-core';

const tracer = new Tracer({ serviceName: 'serverlessAirline' });

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<unknown> => {
  const segment = tracer.getSegment(); // This is the facade segment (the one that is created by AWS Lambda)
  let subsegment: Subsegment | undefined;
  if (segment) {
    // Create subsegment for the function & set it as active
    subsegment = segment.addNewSubsegment(`## ${process.env._HANDLER}`);
    tracer.setSegment(subsegment);
  }

  // Annotate the subsegment with the cold start & serviceName
  tracer.annotateColdStart();
  tracer.addServiceNameAnnotation();

  try {
    // Add the response as metadata
    tracer.addResponseAsMetadata({}, process.env._HANDLER);
  } catch (err) {
    // Add the error as metadata
    tracer.addErrorAsMetadata(err as Error);
    throw err;
  } finally {
    if (segment && subsegment) {
      // Close subsegment (the AWS Lambda one is closed automatically)
      subsegment.close();
      // Set back the facade segment as active again
      tracer.setSegment(segment);
    }
  }

  return {};
};

```

When using the `captureLambdaHandler` decorator or middleware, Tracer performs these additional tasks to ease operations:

- Handles the lifecycle of the subsegment
- Creates a `ColdStart` annotation to easily filter traces that have had an initialization overhead
- Creates a `Service` annotation to easily filter traces that have a specific service name
- Captures any response, or full exceptions generated by the handler, and includes them as tracing metadata

### Annotations & Metadata

**Annotations** are key-values associated with traces and indexed by AWS X-Ray. You can use them to filter traces and to create [Trace Groups](https://aws.amazon.com/about-aws/whats-new/2018/11/aws-xray-adds-the-ability-to-group-traces/) to slice and dice your transactions.

**Metadata** are key-values also associated with traces but not indexed by AWS X-Ray. You can use them to add additional context for an operation using any native object.

You can add annotations using `putAnnotation` method.

```
import { Tracer } from '@aws-lambda-powertools/tracer';

const tracer = new Tracer({ serviceName: 'serverlessAirline' });

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  const handlerSegment = tracer.getSegment()?.addNewSubsegment('### handler');
  handlerSegment && tracer.setSegment(handlerSegment); // (1)!

  tracer.putAnnotation('successfulBooking', true);

  handlerSegment?.close();
  handlerSegment && tracer.setSegment(handlerSegment?.parent); // (2)!
};

```

1. When Lambda starts an invocation [the X-Ray SDk creates a segment called `facade`](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-nodejs-subsegments.html#xray-sdk-nodejs-subsegments-lambda). This segment cannot be annotated or modified by your code, so you need to create a new subsegment. This is done automatically by Tracer when using the [decorator or middleware patterns](https://docs.aws.amazon.com/powertools/typescript/latest/features/tracer/#lambda-handler)
1. To correctly trace the current and subsequent invocations you need to restore the original segment, this is done automatically by Tracer when using the [decorator or middleware patterns](https://docs.aws.amazon.com/powertools/typescript/latest/features/tracer/#lambda-handler).

You can add metadata using `putMetadata` method.

```
import { Tracer } from '@aws-lambda-powertools/tracer';

const tracer = new Tracer({ serviceName: 'serverlessAirline' });

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  const handlerSegment = tracer.getSegment()?.addNewSubsegment('### handler');
  handlerSegment && tracer.setSegment(handlerSegment); // (1)!

  tracer.putMetadata('paymentResponse', {
    foo: 'bar',
  });

  handlerSegment?.close();
  handlerSegment && tracer.setSegment(handlerSegment?.parent); // (2)!
};

```

1. When Lambda starts an invocation [the X-Ray SDk creates a segment called `facade`](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-nodejs-subsegments.html#xray-sdk-nodejs-subsegments-lambda). This segment cannot be modified by your code, so you need to create a new subsegment. This is done automatically by Tracer when using the [decorator or middleware patterns](https://docs.aws.amazon.com/powertools/typescript/latest/features/tracer/#lambda-handler)
1. To correctly trace the current and subsequent invocations you need to restore the original segment, this is done automatically by Tracer when using the [decorator or middleware patterns](https://docs.aws.amazon.com/powertools/typescript/latest/features/tracer/#lambda-handler).

Tracer showcase - Handler Metadata

### Methods

You can trace other class methods using the `captureMethod` decorator or any arbitrary asynchronous function using manual instrumentation.

Note

The class method decorators in this project follow the experimental implementation enabled via the [`experimentalDecorators` compiler option](https://www.typescriptlang.org/tsconfig#experimentalDecorators) in TypeScript.

Additionally, they are implemented to decorate async methods. When decorating a synchronous one, the decorator replaces its implementation with an async one causing the caller to have to `await` the now decorated method.

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Tracer } from '@aws-lambda-powertools/tracer';

const tracer = new Tracer({ serviceName: 'serverlessAirline' });

class Lambda implements LambdaInterface {
  // Decorate your class method
  @tracer.captureMethod() // (1)
  public async getChargeId(): Promise<string> {
    /* ... */
    return 'foo bar';
  }

  public async handler(_event: unknown, _context: unknown): Promise<void> {
    await this.getChargeId();
  }
}

const handlerClass = new Lambda();
export const handler = handlerClass.handler.bind(handlerClass); // (2)

```

1. You can set a custom name for the subsegment by passing `subSegmentName` to the decorator, like: `@tracer.captureMethod({ subSegmentName: '### myCustomMethod' })`.
1. Binding your handler method allows your handler to access `this`.

```
import { Tracer } from '@aws-lambda-powertools/tracer';
import type { Subsegment } from 'aws-xray-sdk-core';

const tracer = new Tracer({ serviceName: 'serverlessAirline' });

const getChargeId = async (): Promise<unknown> => {
  const parentSubsegment = tracer.getSegment(); // This is the subsegment currently active
  let subsegment: Subsegment | undefined;
  subsegment = parentSubsegment?.addNewSubsegment('### chargeId');
  subsegment && tracer.setSegment(subsegment);

  try {
    const res = { chargeId: '1234' };

    // Add the response as metadata
    tracer.addResponseAsMetadata(res, 'chargeId');

    return res;
  } catch (err) {
    // Add the error as metadata
    tracer.addErrorAsMetadata(err as Error);
    throw err;
  } finally {
    // Close subsegment
    subsegment?.close();
    // Set the facade segment as active again, it'll be closed automatically
    parentSubsegment && tracer.setSegment(parentSubsegment);
  }
};

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  await getChargeId();
};

```

### Patching AWS SDK clients

Tracer can patch any [AWS SDK clients](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-nodejs-awssdkclients.html) and create traces when your application makes calls to AWS services.

Info

The following snippet assumes you are using the [**AWS SDK v3** for JavaScript](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/)

You can patch any AWS SDK clients by calling the `captureAWSv3Client` method:

```
import { Tracer } from '@aws-lambda-powertools/tracer';
import { SecretsManagerClient } from '@aws-sdk/client-secrets-manager';

const tracer = new Tracer({ serviceName: 'serverlessAirline' });
// Instrument the AWS SDK client
const client = tracer.captureAWSv3Client(new SecretsManagerClient({}));

export default client;

```

Info

The following two snippets assume you are using the [**AWS SDK v2** for JavaScript](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/welcome.html)

You can patch all AWS SDK v2 clients by calling the `captureAWS` method:

```
import { Tracer } from '@aws-lambda-powertools/tracer';
import AWS from 'aws-sdk';

const tracer = new Tracer({ serviceName: 'serverlessAirline' });

// Instrument all AWS SDK clients created from this point onwards
tracer.captureAWS(AWS);

// Create a new client which will be automatically instrumented
const client = new AWS.SecretsManager();
export default client;

```

If you're looking to shave a few microseconds, or milliseconds depending on your function memory configuration, you can patch only specific AWS SDK v2 clients using `captureAWSClient`:

```
import { Tracer } from '@aws-lambda-powertools/tracer';
import { S3 } from 'aws-sdk';

const tracer = new Tracer({ serviceName: 'serverlessAirline' });
// Instrument the AWS SDK client
const client = tracer.captureAWSClient(new S3());

export default client;

```

### Tracing HTTP requests

When your function makes outgoing requests to APIs, Tracer automatically traces those calls and adds the API to the service graph as a downstream service.

You can opt-out from this feature by setting the **`POWERTOOLS_TRACER_CAPTURE_HTTPS_REQUESTS=false`** environment variable or by passing the `captureHTTPsRequests: false` option to the `Tracer` constructor.

Info

The following snippet shows how to trace [`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/fetch) requests, but you can use any HTTP client library built on top it, or on [http](https://nodejs.org/api/http.html), and [https](https://nodejs.org/api/https.html). Support to 3rd party HTTP clients is provided on a best effort basis.

```
import { Tracer } from '@aws-lambda-powertools/tracer';
import { captureLambdaHandler } from '@aws-lambda-powertools/tracer/middleware';
import middy from '@middy/core';

const tracer = new Tracer({ serviceName: 'serverlessAirline' });

export const handler = middy(
  async (_event: unknown, _context: unknown): Promise<void> => {
    await fetch('https://httpbin.org/status/200');
  }
).use(captureLambdaHandler(tracer));

```

```
{
    "id": "22883fbc730e3a0b",
    "name": "## index.handler",
    "start_time": 1647956168.22749,
    "end_time": 1647956169.0679862,
    "subsegments": [
        {
            "id": "ab82ab2b7d525d8f",
            "name": "httpbin.org",
            "start_time": 1647956168.407,
            "end_time": 1647956168.945,
            "http": {
                "request": {
                    "url": "https://httpbin.org/status/200",
                    "method": "GET"
                },
                "response": {
                    "status": 200,
                    "content_length": 0
                }
            },
            "namespace": "remote"
        }
    ]
}

```

## Advanced

### Disabling response auto-capture

Use **`POWERTOOLS_TRACER_CAPTURE_RESPONSE=false`** environment variable to instruct Tracer **not** to serialize function responses as metadata.

This is commonly useful in three scenarios

1. You might **return sensitive** information you don't want it to be added to your traces
1. You might manipulate **streaming objects that can be read only once**; this prevents subsequent calls from being empty
1. You might return **more than 64K** of data *e.g., `message too long` error*

Alternatively, use the `captureResponse: false` option in both `tracer.captureLambdaHandler()` and `tracer.captureMethod()` decorators, or use the same option in the Middy `captureLambdaHandler` middleware to instruct Tracer **not** to serialize function responses as metadata.

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Tracer } from '@aws-lambda-powertools/tracer';

const tracer = new Tracer({ serviceName: 'serverlessAirline' });

class Lambda implements LambdaInterface {
  @tracer.captureMethod({ captureResponse: false })
  public async getChargeId(): Promise<string> {
    /* ... */
    return 'foo bar';
  }

  public async handler(_event: unknown, _context: unknown): Promise<void> {
    /* ... */
  }
}

const handlerClass = new Lambda();
export const handler = handlerClass.handler.bind(handlerClass);

```

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Tracer } from '@aws-lambda-powertools/tracer';

const tracer = new Tracer({ serviceName: 'serverlessAirline' });

class Lambda implements LambdaInterface {
  @tracer.captureLambdaHandler({ captureResponse: false })
  public async handler(_event: unknown, _context: unknown): Promise<void> {
    tracer.getSegment();
  }
}

const handlerClass = new Lambda();
export const handler = handlerClass.handler.bind(handlerClass);

```

```
import { Tracer } from '@aws-lambda-powertools/tracer';
import { captureLambdaHandler } from '@aws-lambda-powertools/tracer/middleware';
import middy from '@middy/core';

const tracer = new Tracer({ serviceName: 'serverlessAirline' });

const lambdaHandler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  /* ... */
};

// Wrap the handler with middy
export const handler = middy(lambdaHandler)
  // Use the middleware by passing the Tracer instance as a parameter,
  // but specify the captureResponse option as false.
  .use(captureLambdaHandler(tracer, { captureResponse: false }));

```

### Disabling errors auto-capture

Use **`POWERTOOLS_TRACER_CAPTURE_ERROR=false`** environment variable to instruct Tracer **not** to serialize errors as metadata.

Commonly useful in one scenario

1. You might **return sensitive** information from errors, stack traces you might not control

### Access AWS X-Ray Root Trace ID

Tracer exposes a `getRootXrayTraceId()` method that allows you to retrieve the [AWS X-Ray Root Trace ID](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-traces) corresponds to the current function execution.

This is commonly useful in two scenarios

1. By including the root trace id in your response, consumers can use it to correlate requests
1. You might want to surface the root trace id to your end users so that they can reference it while contacting customer service

```
import { Logger } from '@aws-lambda-powertools/logger';
import { Tracer } from '@aws-lambda-powertools/tracer';

const tracer = new Tracer({ serviceName: 'serverlessAirline' });
const logger = new Logger({ serviceName: 'serverlessAirline' });

export const handler = async (): Promise<unknown> => {
  try {
    throw new Error('Something went wrong');
  } catch (error) {
    logger.error('An error occurred', { error });

    const rootTraceId = tracer.getRootXrayTraceId();

    // Example of returning an error response
    return {
      statusCode: 500,
      body: `Internal Error - Please contact support and quote the following id: ${rootTraceId}`,
      headers: { _X_AMZN_TRACE_ID: rootTraceId },
    };
  }
};

```

### Escape hatch mechanism

You can use `tracer.provider` attribute to access [a subset of the methods provided](https://docs.aws.amazon.com/powertools/typescript/latest/api/classes/_aws-lambda-powertools_tracer.provider_ProviderService.ProviderService.html) by the [AWS X-Ray SDK](https://docs.aws.amazon.com/xray-sdk-for-nodejs/latest/reference/AWSXRay.html).

This is useful when you need a feature available in X-Ray that is not available in the Tracer utility, for example [SQL queries tracing](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-nodejs-sqlclients.html), or [a custom logger](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-nodejs-configuration.html#xray-sdk-nodejs-configuration-logging).

```
import { Logger } from '@aws-lambda-powertools/logger';
import { Tracer } from '@aws-lambda-powertools/tracer';

const serviceName = 'serverlessAirline';
const logger = new Logger({ serviceName: serviceName });
const tracer = new Tracer({ serviceName: serviceName });
tracer.provider.setLogger(logger);

```

If you need to access a method that is not available you can import it directly from the AWS X-Ray SDK for Node.js. Compatibility with the Tracer utility is not guaranteed.

## Testing your code

Tracer is disabled by default when not running in the AWS Lambda environment - This means no code changes or environment variables to be set.

## Tips

- Use annotations on key operations to slice and dice traces, create unique views, and create metrics from it via Trace Groups
- Use a namespace when adding metadata to group data more easily
- Annotations and metadata are added to the currently open subsegment. If you want them in a specific subsegment, [create one](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-nodejs-subsegments.html#xray-sdk-nodejs-subsegments-lambda) via the escape hatch mechanism

Logger provides an opinionated logger with output structured as JSON.

## Key features

- Capturing key fields from the Lambda context, cold starts, and structure logging output as JSON.
- Logging Lambda invocation events when instructed (disabled by default).
- Switch log level to `DEBUG` for a percentage of invocations (sampling).
- Buffering logs for a specific request or invocation, and flushing them automatically on error or manually as needed.
- Appending additional keys to structured logs at any point in time.
- Providing a custom log formatter (Bring Your Own Formatter) to output logs in a structure compatible with your organizationâs Logging RFC.

Logger showcase - Log attributes

## Getting started

### Installation

Install the library in your project:

```
npm install @aws-lambda-powertools/logger

```

### Usage

The `Logger` utility must always be instantiated outside the Lambda handler. By doing this, subsequent invocations processed by the same instance of your function can reuse these resources. This saves cost by reducing function run time. In addition, `Logger` can keep track of a cold start and inject the appropriate fields into logs.

```
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger({ serviceName: 'serverlessAirline' });

export const handler = async () => {
  logger.info('Hello World');
};

```

### Utility settings

The library has three optional settings, which can be set via environment variables or passed in the constructor.

These settings will be used across all logs emitted:

| Setting           | Description                                                                                                      | Environment variable            | Default Value       | Allowed Values                                         | Example Value       | Constructor parameter |
| ----------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------------------- | ------------------------------------------------------ | ------------------- | --------------------- |
| **Service name**  | Sets the name of service of which the Lambda function is part of, that will be present across all log statements | `POWERTOOLS_SERVICE_NAME`       | `service_undefined` | Any string                                             | `serverlessAirline` | `serviceName`         |
| **Logging level** | Sets how verbose Logger should be, from the most verbose to the least verbose (no logs)                          | `POWERTOOLS_LOG_LEVEL`          | `INFO`              | `DEBUG`, `INFO`, `WARN`, `ERROR`, `CRITICAL`, `SILENT` | `ERROR`             | `logLevel`            |
| **Sample rate**   | Probability that a Lambda invocation will print all the log items regardless of the log level setting            | `POWERTOOLS_LOGGER_SAMPLE_RATE` | `0`                 | `0.0` to `1.0`                                         | `0.1`               | `sampleRateValue`     |

Info

When `POWERTOOLS_DEV` environment variable is present and set to `"true"` or `"1"`, Logger will pretty-print log messages for easier readability. We recommend to use this setting only when debugging on local environments.

See all environment variables in the [Environment variables](https://docs.aws.amazon.com/powertools/typescript/latest/environment-variables/index.md) section.

Check API docs to learn more about [Logger constructor options](https://docs.aws.amazon.com/powertools/typescript/latest/api/types/_aws-lambda-powertools_logger.types.ConstructorOptions.html).

#### Example using AWS Serverless Application Model (SAM)

```
import { Logger } from '@aws-lambda-powertools/logger';

// Logger parameters fetched from the environment variables (see template.yaml tab)
const logger = new Logger();
logger.info('Hello World');

// You can also pass the parameters in the constructor
// const logger = new Logger({
//     logLevel: 'WARN',
//     serviceName: 'serverlessAirline'
// });

```

```
Resources:
  ShoppingCartApiFunction:
    Type: AWS::Serverless::Function
    Properties:
      Runtime: nodejs24.x
      Environment:
        Variables:
          POWERTOOLS_LOG_LEVEL: WARN
          POWERTOOLS_SERVICE_NAME: serverlessAirline

```

### Standard structured keys

Your Logger will include the following keys to your structured logging (default log formatter):

| Key                         | Example                                                                                                          | Note                                                                                                                                                                                                           |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **level**: `string`         | `INFO`                                                                                                           | Logging level set for the Lambda function's invocation                                                                                                                                                         |
| **message**: `string`       | `Query performed to DynamoDB`                                                                                    | A descriptive, human-readable representation of this log item                                                                                                                                                  |
| **sampling_rate**: `float`  | `0.1`                                                                                                            | When enabled, it prints all the logs of a percentage of invocations, e.g. 10%                                                                                                                                  |
| **service**: `string`       | `serverlessAirline`                                                                                              | A unique name identifier of the service this Lambda function belongs to, by default `service_undefined`                                                                                                        |
| **timestamp**: `string`     | `2011-10-05T14:48:00.000Z`                                                                                       | Timestamp string in simplified extended ISO format (ISO 8601)                                                                                                                                                  |
| **xray_trace_id**: `string` | `1-5759e988-bd862e3fe1be46a994272793`                                                                            | X-Ray Trace ID. This value is always presented in Lambda environment, whether [tracing is enabled](https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html) or not. Logger will always log this value. |
| **error**: `Object`         | `{ name: "Error", location: "/my-project/handler.ts:18", message: "Unexpected error #1", stack: "[stacktrace]"}` | Optional - An object containing information about the Error passed to the logger                                                                                                                               |

Note

If you emit a log message with a key that matches one of `level`, `message`, `sampling_rate`, `service`, or `timestamp`, the Logger will log a warning message and ignore the key.

### Capturing Lambda context info

You can enrich your structured logs with key Lambda context information in multiple ways.

This functionality will include the following keys in your structured logs:

| Key                                | Example                                                                                  |
| ---------------------------------- | ---------------------------------------------------------------------------------------- |
| **cold_start**: `bool`             | `false`                                                                                  |
| **function_name** `string`         | `shopping-cart-api-lambda-prod-eu-west-1`                                                |
| **function_memory_size**: `number` | `128`                                                                                    |
| **function_arn**: `string`         | `arn:aws:lambda:eu-west-1:123456789012:function:shopping-cart-api-lambda-prod-eu-west-1` |
| **function_request_id**: `string`  | `c6af9ac6-7b61-11e6-9a41-93e812345678`                                                   |

```
import { Logger } from '@aws-lambda-powertools/logger';
import { injectLambdaContext } from '@aws-lambda-powertools/logger/middleware';
import middy from '@middy/core';

const logger = new Logger();

const lambdaHandler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  logger.info('This is an INFO log with some context');
};

export const handler = middy(lambdaHandler).use(injectLambdaContext(logger));

```

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger();

class Lambda implements LambdaInterface {
  // Decorate your handler class method
  @logger.injectLambdaContext()
  public async handler(_event: unknown, _context: unknown): Promise<void> {
    logger.info('This is an INFO log with some context');
  }
}

const myFunction = new Lambda();
export const handler = myFunction.handler.bind(myFunction); // (1)

```

1. Binding your handler method allows your handler to access `this` within the class methods.

```
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';

const logger = new Logger();

export const handler = async (
  _event: unknown,
  context: Context
): Promise<void> => {
  logger.addContext(context);

  logger.info('This is an INFO log with some context');
};

```

In each case, the printed log will look like this:

```
{
    "level": "INFO",
    "message": "This is an INFO log with some context",
    "timestamp": "2021-12-12T21:21:08.921Z",
    "service": "serverlessAirline",
    "cold_start": true,
    "function_arn": "arn:aws:lambda:eu-west-1:123456789012:function:shopping-cart-api-lambda-prod-eu-west-1",
    "function_memory_size": 128,
    "function_request_id": "c6af9ac6-7b61-11e6-9a41-93e812345678",
    "function_name": "shopping-cart-api-lambda-prod-eu-west-1",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456"
}

```

### Log incoming event

When debugging in non-production environments, you can log the incoming event using the `logEventIfEnabled()` method or by setting the `logEvent` option in the `injectLambdaContext()` Middy.js middleware or class method decorator.

Warning

This is disabled by default to prevent sensitive info being logged

```
process.env.POWERTOOLS_LOGGER_LOG_EVENT = 'true';

import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger();

export const handler = async (event: unknown) => {
  logger.logEventIfEnabled(event); // (1)
  // ... your logic here
};

```

1. You can control the event logging via the `POWERTOOLS_LOGGER_LOG_EVENT` environment variable.

```
import { Logger } from '@aws-lambda-powertools/logger';
import { injectLambdaContext } from '@aws-lambda-powertools/logger/middleware';
import middy from '@middy/core';

const logger = new Logger();

export const handler = middy(async () => {
  // ... your logic here
}).use(
  injectLambdaContext(logger, { logEvent: true }) // (1)
);

```

1. The `logEvent` option takes precedence over the `POWERTOOLS_LOGGER_LOG_EVENT` environment variable.

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger();

class Lambda implements LambdaInterface {
  @logger.injectLambdaContext({ logEvent: true }) // (1)
  public async handler(_event: unknown, _context: unknown): Promise<void> {
    // ... your logic here
  }
}

const myFunction = new Lambda();
export const handler = myFunction.handler.bind(myFunction);

```

1. The `logEvent` option takes precedence over the `POWERTOOLS_LOGGER_LOG_EVENT` environment variable.

```
{
  "foo": "bar"
}

```

```
{
  "cold_start": true,
  "function_arn": "arn:aws:lambda:eu-west-1:123456789012:function:LogEventFn",
  "function_memory_size": "128",
  "function_name": "LogEventFn",
  "function_request_id": "0a9df60d-e2de-447d-ba3e-45f149eae6c9",
  "level": "INFO",
  "message": "Lambda invocation event",
  "sampling_rate": 0,
  "service": "service_undefined",
  "timestamp": "2024-08-14T10:08:06.199Z",
  "xray_trace_id": "1-66bc8205-21f8b5190da519d22b2b0533",
  "event": {
    "foo": "bar"
  }
}

```

Use `POWERTOOLS_LOGGER_LOG_EVENT` environment variable to enable or disable (`true`/`false`) this feature. When using Middy.js middleware or class method decorator, the `logEvent` option will take precedence over the environment variable.

### Setting a Correlation ID

To get started, install the `@aws-lambda-powertools/jmespath` package, and pass the search function using the `correlationIdSearchFn` constructor parameter:

```
import { Logger } from '@aws-lambda-powertools/logger';
import { search } from '@aws-lambda-powertools/logger/correlationId';

const _logger = new Logger({
  correlationIdSearchFn: search,
});

```

Tip

You can retrieve correlation IDs via `getCorrelationId` method.

You can set a correlation ID using `correlationIdPath` parameter by passing a JMESPath expression, including our custom JMESPath functions or set it manually by calling `setCorrelationId` function.

```
import { Logger } from '@aws-lambda-powertools/logger';
import type { APIGatewayProxyEvent } from 'aws-lambda';

const logger = new Logger();

export const handler = async (event: APIGatewayProxyEvent) => {
  logger.setCorrelationId(event.requestContext.requestId); // (1)!

  logger.info('log with correlation_id');
};

```

1. Alternatively, if the payload is more complex you can use a JMESPath expression as second parameter when prividing a search function in the constructor.

```
import { Logger } from '@aws-lambda-powertools/logger';
import { search } from '@aws-lambda-powertools/logger/correlationId';
import { injectLambdaContext } from '@aws-lambda-powertools/logger/middleware';
import middy from '@middy/core';

const logger = new Logger({
  correlationIdSearchFn: search,
});

export const handler = middy()
  .use(
    injectLambdaContext(logger, {
      correlationIdPath: 'headers.my_request_id_header',
    })
  )
  .handler(async () => {
    logger.info('log with correlation_id');
  });

```

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Logger } from '@aws-lambda-powertools/logger';
import { search } from '@aws-lambda-powertools/logger/correlationId';

const logger = new Logger({
  correlationIdSearchFn: search,
});

class Lambda implements LambdaInterface {
  @logger.injectLambdaContext({
    correlationIdPath: 'headers.my_request_id_header',
  })
  public async handler(_event: unknown, _context: unknown): Promise<void> {
    logger.info('This is an INFO log with some context');
  }
}

const myFunction = new Lambda();
export const handler = myFunction.handler.bind(myFunction);

```

```
{
  "headers": {
    "my_request_id_header": "correlation_id_value"
  }
}

```

```
{
  "level": "INFO",
  "message": "This is an INFO log with some context",
  "timestamp": "2021-05-03 11:47:12,494+0000",
  "service": "payment",
  "correlation_id": "correlation_id_value"
}

```

To ease routine tasks like extracting correlation ID from popular event sources, we provide built-in JMESPath expressions.

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Logger } from '@aws-lambda-powertools/logger';
import {
  correlationPaths,
  search,
} from '@aws-lambda-powertools/logger/correlationId';

const logger = new Logger({
  correlationIdSearchFn: search,
});

class Lambda implements LambdaInterface {
  @logger.injectLambdaContext({
    correlationIdPath: correlationPaths.API_GATEWAY_REST,
  })
  public async handler(_event: unknown, _context: unknown): Promise<void> {
    logger.info('This is an INFO log with some context');
  }
}

const myFunction = new Lambda();
export const handler = myFunction.handler.bind(myFunction);

```

Note: Any object key named with `-` must be escaped

For example, **`request.headers."x-amzn-trace-id"`**.

| Name                          | Expression                            | Description                     |
| ----------------------------- | ------------------------------------- | ------------------------------- |
| **API_GATEWAY_REST**          | `'requestContext.requestId'`          | API Gateway REST API request ID |
| **API_GATEWAY_HTTP**          | `'requestContext.requestId'`          | API Gateway HTTP API request ID |
| **APPSYNC_AUTHORIZER**        | `'requestContext.requestId'`          | AppSync resolver request ID     |
| **APPSYNC_RESOLVER**          | `'request.headers."x-amzn-trace-id"'` | AppSync X-Ray Trace ID          |
| **APPLICATION_LOAD_BALANCER** | `'headers."x-amzn-trace-id"'`         | ALB X-Ray Trace ID              |
| **EVENT_BRIDGE**              | `'id'`                                | EventBridge Event ID            |
| **LAMBDA_FUNCTION_URL**       | `'requestContext.requestId'`          | Lambda Function URL request ID  |
| **S3_OBJECT_LAMBDA**          | `'xAmzRequestId'`                     | S3 Object trigger request ID    |
| **VPC_LATTICE**               | `'headers."x-amzn-trace-id'`          | VPC Lattice X-Ray Trace ID      |

### Appending additional keys

You can append additional keys using either mechanism:

- Add **extra keys** to a single log message by passing them to the log method directly
- Append **temporary keys** to all future log messages via the `appendKeys()` method until `resetKeys()` is called
- Set **Persistent keys** for the logger instance via the `persistentKeys` constructor option or the `appendPersistentKeys()` method

To prevent you from accidentally overwriting some of the [standard keys](#standard-structured-keys), we will log a warning message and ignore the key if you try to overwrite them.

#### Extra keys

You can append additional data to a single log item by passing objects as additional parameters.

- Pass a simple string for logging it with default key name `extra`
- Pass one or multiple objects containing arbitrary data to be logged. Each data object should be placed in an enclosing object as a single property value, you can name this property as you need: `{ myData: arbitraryObjectToLog }`
- If you already have an object containing a `message` key and an additional property, you can pass this object directly

```
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger();

export const handler = async (
  event: unknown,
  _context: unknown
): Promise<unknown> => {
  const myImportantVariable = {
    foo: 'bar',
  };

  // Log additional data in single log items

  // As second parameter
  logger.info('This is a log with an extra variable', {
    data: myImportantVariable,
  });

  // You can also pass multiple parameters containing arbitrary objects
  logger.info(
    'This is a log with 3 extra objects',
    { data: myImportantVariable },
    { correlationIds: { myCustomCorrelationId: 'foo-bar-baz' } },
    { lambdaEvent: event }
  );

  // Simply pass a string for logging additional data
  logger.info('This is a log with additional string value', 'string value');

  // Directly passing an object containing both the message and the additional info
  const logObject = {
    message: 'This is a log message',
    additionalValue: 42,
  };

  logger.info(logObject);

  return {
    foo: 'bar',
  };
};

```

```
{
    "level": "INFO",
    "message": "This is a log with an extra variable",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T22:06:17.463Z",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456",
    "data": { "foo": "bar" }
}
{
    "level": "INFO",
    "message": "This is a log with 3 extra objects",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T22:06:17.466Z",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456",
    "data": { "foo": "bar" },
    "correlationIds": { "myCustomCorrelationId": "foo-bar-baz" },
    "lambdaEvent": { 
        "exampleEventData": {
            "eventValue": 42
        }
    }
}
{
    "level": "INFO",
    "message": "This is a log with additional string value",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T22:06:17.463Z",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456",
    "extra": "string value"
}
{
    "level": "INFO",
    "message": "This is a log message",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T22:06:17.463Z",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456",
    "additionalValue": 42
}

```

#### Temporary keys

You can append additional keys to all future log messages by using the `appendKeys()` method.

When is this useful?

This is helpful to contextualize log messages emitted during a specific function.

```
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger({
  serviceName: 'serverlessAirline',
});

const processTransaction = async (customerId: string): Promise<void> => {
  try {
    logger.appendKeys({
      customerId,
    });

    // ... your business logic

    logger.info('transaction processed');
  } finally {
    logger.resetKeys(); // (1)!
  }
};

export const handler = async (
  event: { customerId: string },
  _context: unknown
): Promise<void> => {
  await processTransaction(event.customerId);

  // .. other business logic

  logger.info('other business logic processed');
};

```

1. You can also remove specific keys by calling the `removeKeys()` method.

```
{
    "level": "INFO",
    "message": "transaction processed",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T21:49:58.084Z",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456",
    "customerId": "123456789012"
}
{
    "level": "INFO",
    "message": "other business logic processed",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T21:49:58.088Z",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456"
}

```

#### Persistent keys

You can persist keys across Lambda invocations by using the `persistentKeys` constructor option or the `appendPersistentKeys()` method. These keys will persist even if you call the [`resetKeys()` method](#resetting-keys).

A common use case is to set keys about your environment or application version, so that you can easily filter logs in CloudWatch Logs.

```
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger({
  serviceName: 'serverlessAirline',
  persistentKeys: {
    environment: 'prod',
    version: process.env.BUILD_VERSION,
  },
});

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  logger.info('processing transaction');

  // ... your business logic
};

```

```
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger({
  serviceName: 'serverlessAirline',
});

declare const getRemoteConfig: (env: string) => {
  environment: string;
  version: string;
};
const { environment, version } = getRemoteConfig('prod');

logger.appendPersistentKeys({ environment, version });

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  logger.info('processing transaction');

  // .. your business logic
};

```

```
{
    "level": "INFO",
    "message": "processing transaction",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T21:49:58.084Z",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456",
    "environment": "prod",
    "version": "1.2.0",
}

```

### Removing additional keys

You can remove additional keys from the logger instance at any time:

- Remove temporary keys added via the `appendKeys()` method by using the `removeKeys()` method
- Remove persistent keys added via the `persistentKeys` constructor option or the `appendPersistentKeys()` method by using the `removePersistentKeys()` method

```
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger({
  serviceName: 'serverlessAirline',
});

const processTransaction = async (customerId: string): Promise<void> => {
  try {
    logger.appendKeys({
      customerId,
    });

    // ... your business logic

    logger.info('transaction processed');
  } finally {
    logger.removeKeys(['customerId']);
  }
};

export const handler = async (
  event: { customerId: string },
  _context: unknown
): Promise<void> => {
  await processTransaction(event.customerId);

  // .. other business logic

  logger.info('other business logic processed');
};

```

```
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger({
  serviceName: 'serverlessAirline',
  persistentKeys: {
    foo: true,
  },
});

declare const getRemoteConfig: (env: string) => {
  isFoo: boolean;
};

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  const { isFoo } = getRemoteConfig('prod');
  if (isFoo) logger.removePersistentKeys(['foo']);

  logger.info('processing transaction');

  // ... your business logic
};

```

#### Resetting keys

Logger is commonly initialized in the global scope. Due to [Lambda Execution Context](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html) reuse, this means that custom keys can be persisted across invocations.

Resetting the state allows you to clear all the temporary keys you have added.

Tip: When is this useful?

This is useful when you add multiple custom keys conditionally or when you use canonical or wide logs.

```
import { Logger } from '@aws-lambda-powertools/logger';

// Persistent attributes will be cached across invocations
const logger = new Logger({
  logLevel: 'info',
  persistentKeys: {
    environment: 'prod',
  },
});

// Enable the clear state flag
export const handler = async (
  event: { userId: string },
  _context: unknown
): Promise<void> => {
  try {
    // This temporary key will be included in the log & cleared after the invocation
    logger.appendKeys({
      details: { userId: event.userId },
    });

    // ... your business logic
  } finally {
    logger.info('WIDE');
    logger.resetKeys();
  }
};

```

```
import { Logger } from '@aws-lambda-powertools/logger';
import { injectLambdaContext } from '@aws-lambda-powertools/logger/middleware';
import middy from '@middy/core';

// Persistent attributes will be cached across invocations
const logger = new Logger({
  logLevel: 'info',
  persistentKeys: {
    environment: 'prod',
  },
});

export const handler = middy(
  async (event: { userId: string }, _context: unknown): Promise<void> => {
    // This temporary key will be included in the log & cleared after the invocation
    logger.appendKeys({
      details: { userId: event.userId },
    });

    // ... your business logic

    logger.info('WIDE');
  }
).use(injectLambdaContext(logger, { resetKeys: true }));

```

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Logger } from '@aws-lambda-powertools/logger';

// Persistent attributes will be cached across invocations
const logger = new Logger({
  logLevel: 'info',
  persistentKeys: {
    environment: 'prod',
  },
});

class Lambda implements LambdaInterface {
  @logger.injectLambdaContext({ resetKeys: true })
  public async handler(
    event: { userId: string },
    _context: unknown
  ): Promise<void> {
    // This temporary key will be included in the log & cleared after the invocation
    logger.appendKeys({
      details: { userId: event.userId },
    });

    // ... your business logic

    logger.info('WIDE');
  }
}

const myFunction = new Lambda();
export const handler = myFunction.handler.bind(myFunction); // (1)!

```

1. Binding your handler method allows your handler to access `this` within the class methods.

```
{
    "environment": "prod",
    "cold_start": true,
    "userId": "123456789012",
    "foo": "bar",
    "function_arn": "arn:aws:lambda:eu-west-1:123456789012:function:foo-bar-function",
    "function_memory_size": 128,
    "function_name": "foo-bar-function",
    "function_request_id": "abcdef123456abcdef123456",
    "level": "INFO",
    "message": "WIDE",
    "service": "hello-world",
    "timestamp": "2021-12-12T22:32:54.670Z",
    "xray_trace_id": "1-5759e988-bd862e3fe1be46a994272793"
}

```

```
{
    "environment": "prod",
    "cold_start": false,
    "userId": "210987654321",
    "function_arn": "arn:aws:lambda:eu-west-1:123456789012:function:foo-bar-function",
    "function_memory_size": 128,
    "function_name": "foo-bar-function",
    "function_request_id": "abcdef123456abcdef123456",
    "level": "INFO",
    "message": "WIDE",
    "service": "hello-world",
    "timestamp": "2021-12-12T22:40:23.120Z",
    "xray_trace_id": "1-5759e988-bd862e3fe1be46a994272793"
}

```

### Logging errors

You can log errors by using the `error` method and pass the error object as parameter. The error will be logged with default key name `error`, but you can also pass your own custom key name.

```
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger();

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  try {
    throw new Error('Unexpected error #1');
  } catch (error) {
    // Log information about the error using the default "error" key
    logger.error('This is the first error', error as Error);
  }

  try {
    throw new Error('Unexpected error #2');
  } catch (error) {
    // Log information about the error using a custom "myCustomErrorKey" key
    logger.error('This is the second error', {
      myCustomErrorKey: error as Error,
    });
  }
};

```

```
{
    "level": "ERROR",
    "message": "This is the first error",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T22:12:39.345Z",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456",
    "error": {
        "name": "Error",
        "location": "/path/to/my/source-code/my-service/handler.ts:18",
        "message": "Unexpected error #1",
        "stack": "Error: Unexpected error #1    at lambdaHandler (/path/to/my/source-code/my-service/handler.ts:18:11)    at Object.<anonymous> (/path/to/my/source-code/my-service/handler.ts:35:1)    at Module._compile (node:internal/modules/cjs/loader:1108:14)    at Module.m._compile (/path/to/my/source-code/node_modules/ts-node/src/index.ts:1371:23)    at Module._extensions..js (node:internal/modules/cjs/loader:1137:10)    at Object.require.extensions.<computed> [as .ts] (/path/to/my/source-code/node_modules/ts-node/src/index.ts:1374:12)    at Module.load (node:internal/modules/cjs/loader:973:32)    at Function.Module._load (node:internal/modules/cjs/loader:813:14)    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:76:12)    at main (/path/to/my/source-code/node_modules/ts-node/src/bin.ts:331:12)"
    }
}
{
    "level": "ERROR",
    "message": "This is the second error",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T22:12:39.377Z",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456",
    "myCustomErrorKey": {
        "name": "Error",
        "location": "/path/to/my/source-code/my-service/handler.ts:24",
        "message": "Unexpected error #2",
        "stack": "Error: Unexpected error #2    at lambdaHandler (/path/to/my/source-code/my-service/handler.ts:24:11)    at Object.<anonymous> (/path/to/my/source-code/my-service/handler.ts:35:1)    at Module._compile (node:internal/modules/cjs/loader:1108:14)    at Module.m._compile (/path/to/my/source-code/node_modules/ts-node/src/index.ts:1371:23)    at Module._extensions..js (node:internal/modules/cjs/loader:1137:10)    at Object.require.extensions.<computed> [as .ts] (/path/to/my/source-code/node_modules/ts-node/src/index.ts:1374:12)    at Module.load (node:internal/modules/cjs/loader:973:32)    at Function.Module._load (node:internal/modules/cjs/loader:813:14)    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:76:12)    at main (/path/to/my/source-code/node_modules/ts-node/src/bin.ts:331:12)"
    }
}

```

Logging errors and log level

You can also log errors using the `warn`, `info`, and `debug` methods. Be aware of the log level though, you might miss those errors when analyzing the log later depending on the log level configuration.

## Advanced

### Log levels

The default log level is `INFO` and can be set using the `logLevel` constructor option or by using the `POWERTOOLS_LOG_LEVEL` environment variable.

We support the following log levels:

| Level      | Numeric value |
| ---------- | ------------- |
| `TRACE`    | 6             |
| `DEBUG`    | 8             |
| `INFO`     | 12            |
| `WARN`     | 16            |
| `ERROR`    | 20            |
| `CRITICAL` | 24            |
| `SILENT`   | 28            |

You can access the current log level by using the `getLevelName()` method. This method returns the name of the current log level as a string. If you want to change the log level at runtime, you can use the `setLogLevel()` method. This method accepts a string value that represents the log level you want to set, both lower and upper case values are supported.

```
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger();

logger.getLevelName(); // returns "INFO"
logger.setLogLevel('DEBUG');

```

If you want to access the numeric value of the current log level, you can use the `level` property. For example, if the current log level is `INFO`, `logger.level` property will return `12`.

#### Silencing logs

The `SILENT` log level provides a simple and efficient way to suppress all log messages without the need to modify your code. When you set this log level, all log messages, regardless of their severity, will be silenced.

This feature is useful when you want to have your code instrumented to produce logs, but due to some requirement or business decision, you prefer to not emit them.

By setting the log level to `SILENT`, which can be done either through the `logLevel` constructor option or by using the `POWERTOOLS_LOG_LEVEL` environment variable, you can easily suppress all logs as needed.

Note

Use the `SILENT` log level with care, as it can make it more challenging to monitor and debug your application. Therefore, we advise using this log level judiciously.

#### AWS Lambda Advanced Logging Controls (ALC)

With [AWS Lambda Advanced Logging Controls (ALC)](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html#monitoring-cloudwatchlogs-advanced), you can control the output format of your logs as either `TEXT` or `JSON` and specify the minimum accepted log level for your application.

Regardless of the output format setting in Lambda, we will always output JSON formatted logging messages.

When you have this feature enabled, log messages that donât meet the configured log level are discarded by Lambda. For example, if you set the minimum log level to `WARN`, you will only receive `WARN` and `ERROR` messages in your AWS CloudWatch Logs, all other log levels will be discarded by Lambda.

```
sequenceDiagram
    title Lambda ALC allows WARN logs only
    participant Lambda service
    participant Lambda function
    participant Application Logger

    Note over Lambda service: AWS_LAMBDA_LOG_LEVEL="WARN"
    Lambda service->>Lambda function: Invoke (event)
    Lambda function->>Lambda function: Calls handler
    Lambda function->>Application Logger: logger.warn("Something happened")
    Lambda function-->>Application Logger: logger.debug("Something happened")
    Lambda function-->>Application Logger: logger.info("Something happened")

    Lambda service->>Lambda service: DROP INFO and DEBUG logs

    Lambda service->>CloudWatch Logs: Ingest error logs
```

**Priority of log level settings in Powertools for AWS Lambda**

When the Advanced Logging Controls feature is enabled, we are unable to increase the minimum log level below the `AWS_LAMBDA_LOG_LEVEL` environment variable value, see [AWS Lambda service documentation](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html#monitoring-cloudwatchlogs-log-level) for more details.

We prioritise log level settings in this order:

1. `AWS_LAMBDA_LOG_LEVEL` environment variable
1. Setting the log level in code using the `logLevel` constructor option, or by calling the `logger.setLogLevel()` method
1. `POWERTOOLS_LOG_LEVEL` environment variable

In the event you have set a log level in Powertools to a level that is lower than the ACL setting, we will output a warning log message informing you that your messages will be discarded by Lambda.

### Buffering logs

Log buffering enables you to buffer logs for a specific request or invocation. Enable log buffering by passing `logBufferOptions` when initializing a Logger instance. You can buffer logs at the `WARNING`, `INFO`, `DEBUG`, or `TRACE` level, and flush them automatically on error or manually as needed.

This is useful when you want to reduce the number of log messages emitted while still having detailed logs when needed, such as when troubleshooting issues.

```
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger({
  logBufferOptions: {
    maxBytes: 20480,
    flushOnErrorLog: true,
  },
});

logger.debug('This is a debug message'); // This is NOT buffered

export const handler = async () => {
  logger.debug('This is a debug message'); // This is buffered
  logger.info('This is an info message');

  // your business logic here

  logger.error('This is an error message'); // This also flushes the buffer
  // or logger.flushBuffer(); // to flush the buffer manually
};

```

#### Configuring the buffer

When configuring the buffer, you can set the following options to fine-tune how logs are captured, stored, and emitted. You can configure the following options in the `logBufferOptions` constructor parameter:

| Parameter           | Description                                      | Configuration                       | Default |
| ------------------- | ------------------------------------------------ | ----------------------------------- | ------- |
| `enabled`           | Enable or disable log buffering                  | `true`, `false`                     | `false` |
| `maxBytes`          | Maximum size of the log buffer in bytes          | `number`                            | `20480` |
| `bufferAtVerbosity` | Minimum log level to buffer                      | `TRACE`, `DEBUG`, `INFO`, `WARNING` | `DEBUG` |
| `flushOnErrorLog`   | Automatically flush buffer when logging an error | `true`, `false`                     | `true`  |

```
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger({
  logBufferOptions: {
    bufferAtVerbosity: 'warn', // (1)!
  },
});

export const handler = async () => {
  // All logs below are buffered
  logger.debug('This is a debug message');
  logger.info('This is an info message');
  logger.warn('This is a warn message');

  logger.clearBuffer(); // (2)!
};

```

1. Setting `bufferAtVerbosity: 'warn'` configures log buffering for `WARNING` and all lower severity levels like `INFO`, `DEBUG`, and `TRACE`.
1. Calling `logger.clearBuffer()` will clear the buffer without emitting the logs.

```
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger({
  logBufferOptions: {
    maxBytes: 20480,
    flushOnErrorLog: false, // (1)!
  },
});

export const handler = async () => {
  logger.debug('This is a debug message'); // This is buffered

  try {
    throw new Error('a non fatal error');
  } catch (error) {
    logger.error('A non fatal error occurred', { error }); // This does NOT flush the buffer
  }

  logger.debug('This is another debug message'); // This is buffered

  try {
    throw new Error('a fatal error');
  } catch (error) {
    logger.error('A fatal error occurred', { error }); // This does NOT flush the buffer
    logger.flushBuffer();
  }
};

```

1. Disabling `flushOnErrorLog` will not flush the buffer when logging an error. This is useful when you want to control when the buffer is flushed by calling the `logger.flushBuffer()` method.

#### Flushing on errors

When using the `logger.injectLambdaContext()` class method decorator or the `injectLambdaContext()` middleware, you can configure the logger to automatically flush the buffer when an error occurs. This is done by setting the `flushBufferOnUncaughtError` option to `true` in the decorator or middleware options.

```
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';

const logger = new Logger({
  logLevel: 'DEBUG',
  logBufferOptions: { enabled: true },
});

class Lambda {
  @logger.injectLambdaContext({
    flushBufferOnUncaughtError: true,
  })
  async handler(_event: unknown, _context: Context) {
    // Both logs below are buffered
    logger.debug('a debug log');
    logger.debug('another debug log');

    throw new Error('an error log'); // This causes the buffer to flush
  }
}

const lambda = new Lambda();
export const handler = lambda.handler.bind(lambda);

```

```
import { Logger } from '@aws-lambda-powertools/logger';
import { injectLambdaContext } from '@aws-lambda-powertools/logger/middleware';
import middy from '@middy/core';

const logger = new Logger({
  logLevel: 'DEBUG',
  logBufferOptions: { enabled: true },
});

export const handler = middy()
  .use(injectLambdaContext(logger, { flushBufferOnUncaughtError: true }))
  .handler(async (_event: unknown) => {
    // Both logs below are buffered
    logger.debug('a debug log');
    logger.debug('another debug log');

    throw new Error('an error log'); // This causes the buffer to flush
  });

```

#### Buffering workflows

##### Manual flush

```
sequenceDiagram
    participant Client
    participant Lambda
    participant Logger
    participant CloudWatch
    Client->>Lambda: Invoke Lambda
    Lambda->>Logger: Initialize with DEBUG level buffering
    Logger-->>Lambda: Logger buffer ready
    Lambda->>Logger: logger.debug("First debug log")
    Logger-->>Logger: Buffer first debug log
    Lambda->>Logger: logger.info("Info log")
    Logger->>CloudWatch: Directly log info message
    Lambda->>Logger: logger.debug("Second debug log")
    Logger-->>Logger: Buffer second debug log
    Lambda->>Logger: logger.flush_buffer()
    Logger->>CloudWatch: Emit buffered logs to stdout
    Lambda->>Client: Return execution result
```

*Flushing buffer manually*

##### Flushing when logging an error

```
sequenceDiagram
    participant Client
    participant Lambda
    participant Logger
    participant CloudWatch
    Client->>Lambda: Invoke Lambda
    Lambda->>Logger: Initialize with DEBUG level buffering
    Logger-->>Lambda: Logger buffer ready
    Lambda->>Logger: logger.debug("First log")
    Logger-->>Logger: Buffer first debug log
    Lambda->>Logger: logger.debug("Second log")
    Logger-->>Logger: Buffer second debug log
    Lambda->>Logger: logger.debug("Third log")
    Logger-->>Logger: Buffer third debug log
    Lambda->>Lambda: Exception occurs
    Lambda->>Logger: logger.error("Error details")
    Logger->>CloudWatch: Emit buffered debug logs
    Logger->>CloudWatch: Emit error log
    Lambda->>Client: Raise exception
```

*Flushing buffer when an error happens*

##### Flushing on error

This works only when using the `logger.injectLambdaContext()` class method decorator or the `injectLambdaContext()` middleware. You can configure the logger to automatically flush the buffer when an error occurs by setting the `flushBufferOnUncaughtError` option to `true` in the decorator or middleware options.

```
sequenceDiagram
    participant Client
    participant Lambda
    participant Logger
    participant CloudWatch
    Client->>Lambda: Invoke Lambda
    Lambda->>Logger: Using decorator
    Logger-->>Lambda: Logger context injected
    Lambda->>Logger: logger.debug("First log")
    Logger-->>Logger: Buffer first debug log
    Lambda->>Logger: logger.debug("Second log")
    Logger-->>Logger: Buffer second debug log
    Lambda->>Lambda: Uncaught Exception
    Lambda->>CloudWatch: Automatically emit buffered debug logs
    Lambda->>Client: Raise uncaught exception
```

*Flushing buffer when an uncaught exception happens*

#### Buffering FAQs

1. **Does the buffer persist across Lambda invocations?** No, each Lambda invocation has its own buffer. The buffer is initialized when the Lambda function is invoked and is cleared after the function execution completes or when flushed manually.
1. **Are my logs buffered during cold starts?** No, we never buffer logs during cold starts. This is because we want to ensure that logs emitted during this phase are always available for debugging and monitoring purposes. The buffer is only used during the execution of the Lambda function.
1. **How can I prevent log buffering from consuming excessive memory?** You can limit the size of the buffer by setting the `maxBytes` option in the `logBufferOptions` constructor parameter. This will ensure that the buffer does not grow indefinitely and consume excessive memory.
1. **What happens if the log buffer reaches its maximum size?** Older logs are removed from the buffer to make room for new logs. This means that if the buffer is full, you may lose some logs if they are not flushed before the buffer reaches its maximum size. When this happens, we emit a warning when flushing the buffer to indicate that some logs have been dropped.
1. **How is the log size of a log line calculated?** The log size is calculated based on the size of the stringified log line in bytes. This includes the size of the log message, the size of any additional keys, and the size of the timestamp.
1. **What timestamp is used when I flush the logs?** The timestamp preserves the original time when the log record was created. If you create a log record at 11:00:10 and flush it at 11:00:25, the log line will retain its original timestamp of 11:00:10.
1. **What happens if I try to add a log line that is bigger than max buffer size?** The log will be emitted directly to standard output and not buffered. When this happens, we emit a warning to indicate that the log line was too big to be buffered.
1. **What happens if Lambda times out without flushing the buffer?** Logs that are still in the buffer will be lost. If you are using the log buffer to log asynchronously, you should ensure that the buffer is flushed before the Lambda function times out. You can do this by calling the `logger.flushBuffer()` method at the end of your Lambda function.
1. **Do child loggers inherit the buffer?** No, child loggers do not inherit the buffer from their parent logger but only the buffer configuration. This means that if you create a child logger, it will have its own buffer and will not share the buffer with the parent logger.

### Reordering log keys position

You can change the order of [standard Logger keys](#standard-structured-keys) or any keys that will be appended later at runtime via the `logRecordOrder` parameter.

Note

This feature is available only in the default log formatter and not with custom log formatters.

```
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger({
  serviceName: 'serverlessAirline',
  logRecordOrder: ['timestamp', 'additionalKey'],
});

export const handler = async (): Promise<void> => {
  logger.info('Hello, World!', {
    additionalKey: 'additionalValue',
  });
};

```

```
{
  "level": "INFO",
  "message": "Hello, World!",
  "timestamp": "2024-09-03T02:59:06.603Z",
  "service": "serverlessAirline",
  "additionalKey": "additionalValue",
  "sampling_rate": 0,
  "xray_trace_id": "1-66d67b7a-79bc7b2346b32af01b437cf8"
}

```

### Setting timestamp to custom timezone

By default, Logger emits records with the default Lambda timestamp in **UTC**, i.e. `2016-06-20T12:08:10.000Z`

If you prefer to log in a specific timezone, you can configure it by setting the `TZ` environment variable. You can do this either as an environment variable or directly within your Lambda function settings.

See the [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-runtime) for a comprehensive list of available Lambda environment variables.

```
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger({ serviceName: 'serverlessAirline' });

export const handler = async (): Promise<void> => {
  logger.info('Hello, World!');

  process.env.TZ = 'Europe/Rome';

  const childLogger = logger.createChild();

  childLogger.info('Ciao, Mondo!');
};

```

```
[
  {
    "level": "INFO",
    "message": "Hello, World!",
    "timestamp": "2024-07-01T11:00:37.886Z",
    "service": "serverlessAirline",
    "sampling_rate": 0,
    "xray_trace_id": "1-66828c55-2bb635c65eb609c820ebe7bc"
  },
  {
    "level": "INFO",
    "message": "Ciao, Mondo!",
    "timestamp": "2024-07-01T13:00:37.934+02:00",
    "service": "serverlessAirline",
    "sampling_rate": 0,
    "xray_trace_id": "1-66828c55-2bb635c65eb609c820ebe7bc"
  }
]

```

### Creating child loggers

The `createChild` method allows you to create a child instance of the Logger, which inherits all of the attributes from its parent. You have the option to override any of the settings and attributes from the parent logger, including [its settings](#utility-settings), any [extra keys](#appending-additional-keys), and [the log formatter](#custom-log-formatter).

Once a child logger is created, the logger and its parent will act as separate instances of the Logger class, and as such any change to one won't be applied to the other.

The following example shows how to create multiple Loggers that share service name and persistent attributes while specifying different logging levels within a single Lambda invocation. As the result, only ERROR logs with all the inherited attributes will be displayed in CloudWatch Logs from the child logger, but all logs emitted will have the same service name and persistent attributes.

```
import { Logger } from '@aws-lambda-powertools/logger';

// This logger has a service name, some persistent attributes
// and log level set to INFO
const logger = new Logger({
  serviceName: 'serverlessAirline',
  logLevel: 'INFO',
  persistentLogAttributes: {
    aws_account_id: '123456789012',
    aws_region: 'eu-west-1',
  },
});

// This other logger inherits all the parent's attributes
// but the log level, which is now set to ERROR
const childLogger = logger.createChild({
  logLevel: 'ERROR',
});

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  logger.info('This is an INFO log, from the parent logger');
  logger.error('This is an ERROR log, from the parent logger');

  childLogger.info('This is an INFO log, from the child logger');
  childLogger.error('This is an ERROR log, from the child logger');
};

```

```
{
    "level": "INFO",
    "message": "This is an INFO log, from the parent logger",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T22:32:54.667Z",
    "aws_account_id":"123456789012",
    "aws_region":"eu-west-1",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456"
}
{
    "level": "ERROR",
    "message": "This is an ERROR log, from the parent logger",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T22:32:54.670Z",
    "aws_account_id":"123456789012",
    "aws_region":"eu-west-1",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456"
}
{
    "level": "ERROR",
    "message": "This is an ERROR log, from the child logger",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T22:32:54.670Z",
    "aws_account_id":"123456789012",
    "aws_region":"eu-west-1",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456"
}

```

### Sampling debug logs

Use sampling when you want to dynamically change your log level to **DEBUG** based on a **percentage of your invocations**.

You can use values ranging from `0` to `1` (100%) when setting the `sampleRateValue` constructor option or `POWERTOOLS_LOGGER_SAMPLE_RATE` env var.

When is this useful?

Let's imagine a sudden spike increase in concurrency triggered a transient issue downstream. When looking into the logs you might not have enough information, and while you can adjust log levels it might not happen again.

This feature takes into account transient issues where additional debugging information can be useful.

Sampling decision happens at the Logger initialization. When using the `injectLambdaContext` method either as a decorator or Middy.js middleware, the sampling decision is refreshed at the beginning of each Lambda invocation for you, except for cold starts.

If you're not using either of these, you'll need to manually call the `refreshSamplingRate()` function at the start of your handler to refresh the sampling decision for each invocation.

```
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger({
  logLevel: 'ERROR', // (1)!
  sampleRateValue: 0.5,
});

export const handler = async () => {
  logger.refreshSampleRateCalculation(); // (2)!

  logger.error('This log is always emitted');

  logger.debug('This log has ~50% chance of being emitted');
  logger.info('This log has ~50% chance of being emitted');
  logger.warn('This log has ~50% chance of being emitted');
};

```

1. The log level must be set to a more verbose level than `DEBUG` for log sampling to kick in.
1. You need to call `logger.refreshSamplingRate()` at the start of your handler **only** if you're not using the `injectLambdaContext()` class method decorator or Middy.js middleware.

```
{
  "level": "ERROR",
  "message": "This log is always emitted",
  "sampling_rate": "0.5",
  "service": "serverlessAirline",
  "timestamp": "2021-12-12T22:59:06.334Z",
  "xray_trace_id": "abcdef123456abcdef123456abcdef123456"
}

```

```
[
  {
    "level": "ERROR",
    "message": "This log is always emitted",
    "sampling_rate": "0.5",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T22:59:06.334Z",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456"
  },
  {
    "level": "DEBUG",
    "message": "This log has ~50% chance of being emitted",
    "sampling_rate": "0.5",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T22:59:06.337Z",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456"
  },
  {
    "level": "INFO",
    "message": "This log has ~50% chance of being emitted",
    "sampling_rate": "0.5",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T22:59:06.338Z",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456"
  },
  {
    "level": "WARN",
    "message": "This log has ~50% chance of being emitted",
    "sampling_rate": "0.5",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T22:59:06.338Z",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456"
  }
]

```

```
[
  {
    "level": "ERROR",
    "message": "This log is always emitted",
    "sampling_rate": "0.5",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T22:59:06.334Z",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456"
  },
  {
    "level": "DEBUG",
    "message": "This log has ~50% chance of being emitted",
    "sampling_rate": "0.5",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T22:59:06.337Z",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456"
  },
  {
    "level": "INFO",
    "message": "This log has ~50% chance of being emitted",
    "sampling_rate": "0.5",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T22:59:06.338Z",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456"
  },
  {
    "level": "WARN",
    "message": "This log has ~50% chance of being emitted",
    "sampling_rate": "0.5",
    "service": "serverlessAirline",
    "timestamp": "2021-12-12T22:59:06.338Z",
    "xray_trace_id": "abcdef123456abcdef123456abcdef123456"
  }
]

```

```
{
  "level": "ERROR",
  "message": "This log is always emitted",
  "sampling_rate": "0.5",
  "service": "serverlessAirline",
  "timestamp": "2021-12-12T22:59:06.334Z",
  "xray_trace_id": "abcdef123456abcdef123456abcdef123456"
}

```

### Custom Log formatter

You can customize the structure (keys and values) of your logs by passing a custom log formatter, a class that implements the `LogFormatter` interface, to the `Logger` constructor.

When working with custom log formatters, you take full control over the structure of your logs. This allows you to optionally drop or transform keys, add new ones, or change the format to suit your company's logging standards or use Logger with a third-party logging service.

```
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';
import { MyCompanyLogFormatter } from './bringYourOwnFormatterClass';

const logger = new Logger({
  logFormatter: new MyCompanyLogFormatter(),
  logLevel: 'DEBUG',
  serviceName: 'serverlessAirline',
  sampleRateValue: 0.5,
  persistentLogAttributes: {
    awsAccountId: process.env.AWS_ACCOUNT_ID,
    logger: {
      name: '@aws-lambda-powertools/logger',
      version: '0.0.1',
    },
  },
});

export const handler = async (
  _event: unknown,
  context: Context
): Promise<void> => {
  logger.addContext(context);

  logger.info('This is an INFO log', {
    correlationIds: { myCustomCorrelationId: 'foo-bar-baz' },
  });
};

```

```
import { LogFormatter, LogItem } from '@aws-lambda-powertools/logger';
import type {
  LogAttributes,
  UnformattedAttributes,
} from '@aws-lambda-powertools/logger/types';

// Replace this line with your own type
type MyCompanyLog = LogAttributes;

class MyCompanyLogFormatter extends LogFormatter {
  public formatAttributes(
    attributes: UnformattedAttributes,
    additionalLogAttributes: LogAttributes
  ): LogItem {
    const baseAttributes: MyCompanyLog = {
      message: attributes.message,
      service: attributes.serviceName,
      environment: attributes.environment,
      awsRegion: attributes.awsRegion,
      correlationIds: {
        awsRequestId: attributes.lambdaContext?.awsRequestId,
        xRayTraceId: attributes.xRayTraceId,
      },
      lambdaFunction: {
        name: attributes.lambdaContext?.functionName,
        arn: attributes.lambdaContext?.invokedFunctionArn,
        memoryLimitInMB: attributes.lambdaContext?.memoryLimitInMB,
        version: attributes.lambdaContext?.functionVersion,
        coldStart: attributes.lambdaContext?.coldStart,
      },
      logLevel: attributes.logLevel,
      timestamp: this.formatTimestamp(attributes.timestamp), // You can extend this function
      logger: {
        sampleRateValue: attributes.sampleRateValue,
      },
    };

    const logItem = new LogItem({ attributes: baseAttributes });
    logItem.addAttributes(additionalLogAttributes); // add any attributes not explicitly defined

    return logItem;
  }
}

export { MyCompanyLogFormatter };

```

```
{
    "message": "This is an INFO log",
    "service": "serverlessAirline",
    "awsRegion": "eu-west-1",
    "correlationIds": {
        "awsRequestId": "c6af9ac6-7b61-11e6-9a41-93e812345678",
        "xRayTraceId": "abcdef123456abcdef123456abcdef123456",
        "myCustomCorrelationId": "foo-bar-baz"
    },
    "lambdaFunction": {
        "name": "shopping-cart-api-lambda-prod-eu-west-1",
        "arn": "arn:aws:lambda:eu-west-1:123456789012:function:shopping-cart-api-lambda-prod-eu-west-1",
        "memoryLimitInMB": 128,
        "version": "$LATEST",
        "coldStart": true
    },
    "logLevel": "INFO",
    "timestamp": "2021-12-12T23:13:53.404Z",
    "logger": {
        "sampleRateValue": "0.5",
        "name": "aws-lambda-powertools-typescript",
        "version": "0.0.1"
    },
    "awsAccountId": "123456789012"
}

```

Note that when implementing this method, you should avoid mutating the `attributes` and `additionalLogAttributes` objects directly. Instead, create a new object with the desired structure and return it. If mutation is necessary, you can create a [`structuredClone`](https://developer.mozilla.org/en-US/docs/Web/API/Window/structuredClone) of the object to avoid side effects.

### Extend JSON replacer function

You can extend the default JSON serializer by passing a custom serializer function to the `Logger` constructor, using the `jsonReplacerFn` option. This is useful when you want to customize the serialization of specific values.

```
import { Logger } from '@aws-lambda-powertools/logger';
import type { CustomJsonReplacerFn } from '@aws-lambda-powertools/logger/types';

const jsonReplacerFn: CustomJsonReplacerFn = (_: string, value: unknown) =>
  value instanceof Set ? [...value] : value;

const logger = new Logger({ serviceName: 'serverlessAirline', jsonReplacerFn });

export const handler = async () => {
  logger.info('Serialize with custom serializer', {
    serializedValue: new Set([1, 2, 3]),
  });
};

```

```
{
  "level": "INFO",
  "message": "Serialize with custom serializer",
  "timestamp": "2024-07-07T09:52:14.212Z",
  "service": "serverlessAirline",
  "sampling_rate": 0,
  "xray_trace_id": "1-668a654d-396c646b760ee7d067f32f18",
  "serializedValue": [1, 2, 3]
}

```

By default, Logger uses `JSON.stringify()` to serialize log items and a [custom replacer function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#the_replacer_parameter) to serialize common unserializable values such as `BigInt`, circular references, and `Error` objects.

When you extend the default JSON serializer, we will call your custom serializer function before the default one. This allows you to customize the serialization while still benefiting from the default behavior.

## Testing your code

### Inject Lambda Context

When unit testing your code that makes use of `logger.addContext()` or `injectLambdaContext` middleware and decorator, you can optionally pass a dummy Lambda Context if you want your logs to contain this information.

This is a sample that provides the minimum information necessary for Logger to inject context data:

```
import type { Context } from 'aws-lambda';
import { describe, expect, it } from 'vitest';

declare const handler: (event: unknown, context: Context) => Promise<true>;

const context = {
  callbackWaitsForEmptyEventLoop: true,
  functionVersion: '$LATEST',
  functionName: 'foo-bar-function',
  memoryLimitInMB: '128',
  logGroupName: '/aws/lambda/foo-bar-function-123456abcdef',
  logStreamName: '2021/03/09/[$LATEST]abcdef123456abcdef123456abcdef123456',
  invokedFunctionArn:
    'arn:aws:lambda:eu-west-1:123456789012:function:foo-bar-function',
  awsRequestId: 'c6af9ac6-7b61-11e6-9a41-93e812345678',
  getRemainingTimeInMillis: () => 1234,
  done: () => console.log('Done!'),
  fail: () => console.log('Failed!'),
  succeed: () => console.log('Succeeded!'),
} satisfies Context;

describe('MyUnitTest', () => {
  it('invokes the handler successfully', async () => {
    // Prepare
    const testEvent = { test: 'test' };

    // Act
    const result = await handler(testEvent, context);

    // Assert
    expect(result).toBe(true);
  });
});

```

### Suppress logs

When unit testing your code with [Jest](https://jestjs.io) or [Vitest](http://vitest.dev) you can use the `POWERTOOLS_DEV` environment variable in conjunction with the `--silent` CLI option to suppress logs from Logger.

```
export POWERTOOLS_DEV=true && npx vitest --silent

```

Alternatively, you can also set the `POWERTOOLS_DEV` environment variable to `true` in your test setup file, or in a hoisted block at the top of your test file.

Metrics creates custom metrics asynchronously by logging metrics to standard output following [Amazon CloudWatch Embedded Metric Format (EMF)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html).

These metrics can be visualized through [Amazon CloudWatch Console](https://console.aws.amazon.com/cloudwatch/).

## Key features

- Aggregating up to 100 metrics using a single CloudWatch EMF object (large JSON blob).
- Validating your metrics against common metric definitions mistakes (for example, metric unit, values, max dimensions, max metrics).
- Metrics are created asynchronously by the CloudWatch service. You do not need any custom stacks, and there is no impact to Lambda function latency.
- Creating a one-off metric with different dimensions.

Metrics showcase - Metrics Explorer

## Terminologies

If you're new to Amazon CloudWatch, there are two terminologies you must be aware of before using this utility:

- **Namespace**. It's the highest level container that will group multiple metrics from multiple services for a given application, for example `ServerlessEcommerce`.
- **Dimensions**. Metrics metadata in key-value format. They help you slice and dice metrics visualization, for example `ColdStart` metric by Payment `service`.
- **Metric**. It's the name of the metric, for example: SuccessfulBooking or UpdatedBooking.
- **Unit**. It's a value representing the unit of measure for the corresponding metric, for example: Count or Seconds.
- **Resolution**. It's a value representing the storage resolution for the corresponding metric. Metrics can be either [Standard or High resolution](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Resolution_definition).

Metric terminology, visually explained

## Getting started

### Installation

Install the library in your project:

```
npm install @aws-lambda-powertools/metrics

```

Caution

When using the Lambda [Advanced Logging Controls](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html#monitoring-cloudwatchlogs-advanced) feature you must install version of Powertools for AWS Lambda (TypeScript) v1.15.0 or newer.

### Usage

The `Metrics` utility must always be instantiated outside of the Lambda handler. In doing this, subsequent invocations processed by the same instance of your function can reuse these resources. This saves cost by reducing function run time. In addition, `Metrics` can track cold start and emit the appropriate metrics.

```
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  metrics.addMetric('successfulBooking', MetricUnit.Count, 1);
};

```

### Utility settings

The library requires two settings. You can set them as environment variables, or pass them in the constructor.

These settings will be used across all metrics emitted:

| Setting              | Description                                                      | Environment variable               | Default                                                  | Allowed Values | Example             | Constructor parameter |
| -------------------- | ---------------------------------------------------------------- | ---------------------------------- | -------------------------------------------------------- | -------------- | ------------------- | --------------------- |
| **Service**          | Optionally, sets **service** metric dimension across all metrics | `POWERTOOLS_SERVICE_NAME`          | `service_undefined`                                      | Any string     | `serverlessAirline` | `serviceName`         |
| **Metric namespace** | Logical container where all metrics will be placed               | `POWERTOOLS_METRICS_NAMESPACE`     | `default_namespace`                                      | Any string     | `serverlessAirline` | `default_namespace`   |
| **Function Name**    | Function name used as dimension for the `ColdStart` metric       | `POWERTOOLS_METRICS_FUNCTION_NAME` | [See docs](#capturing-a-cold-start-invocation-as-metric) | Any string     | `my-function-name`  | `functionName`        |
| **Disabled**         | Whether to disable the log of metrics to standard output or not  | `POWERTOOLS_METRICS_DISABLED`      | `false`                                                  | Boolean        | `true`              |                       |

Tip

Use your application name or main service as the metric namespace to easily group all metrics

#### Example using AWS Serverless Application Model (SAM)

The `Metrics` utility is instantiated outside of the Lambda handler. In doing this, the same instance can be used across multiple invocations inside the same execution environment. This allows `Metrics` to be aware of things like whether or not a given invocation had a cold start or not.

```
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';

// Metrics parameters fetched from the environment variables (see template.yaml tab)
const metrics = new Metrics();
metrics.addMetric('successfulBooking', MetricUnit.Count, 1);

// You can also pass the parameters in the constructor
// const metrics = new Metrics({
//   namespace: 'serverlessAirline',
//   serviceName: 'orders'
// });

```

```
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      Runtime: nodejs24.x
      Environment:
      Variables:
        POWERTOOLS_SERVICE_NAME: orders
        POWERTOOLS_METRICS_NAMESPACE: serverlessAirline
        POWERTOOLS_METRICS_FUNCTION_NAME: my-function-name

```

You can initialize Metrics anywhere in your code - It'll keep track of your aggregate metrics in memory.

### Creating metrics

You can create metrics using the `addMetric` method. Metrics are automatically associated with your configured namespace and dimensions.

```
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  metrics.addMetric('successfulBooking', MetricUnit.Count, 1);
  metrics.publishStoredMetrics();
};

```

```
{
  "_aws": {
    "Timestamp": 1763409658885,
    "CloudWatchMetrics": [
      {
        "Namespace": "serverlessAirline",
        "Dimensions": [["service"]],
        "Metrics": [
          {
            "Name": "successfulBooking",
            "Unit": "Count"
          }
        ]
      }
    ]
  },
  "service": "orders",
  "successfulBooking": 1
}

```

### Adding dimensions

By default, Powertools adds a `service` dimension in a [DimensionSet](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html). You can append additional dimensions for all your aggregate metrics using the `addDimension` method.

Note

The `addDimension` method appends the dimension to the first `DimensionSet` in the `DimensionSet` array. To create a new `DimensionSet`, use the `addDimensions` method.

```
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  metrics.addDimension('environment', 'prod');
  metrics.addMetric('successfulBooking', MetricUnit.Count, 1);
  metrics.publishStoredMetrics();
};

```

```
{
  "_aws": {
    "Timestamp": 1763409658885,
    "CloudWatchMetrics": [
      {
        "Namespace": "serverlessAirline",
        "Dimensions": [["service", "environment"]],
        "Metrics": [
          {
            "Name": "successfulBooking",
            "Unit": "Count"
          }
        ]
      }
    ]
  },
  "service": "orders",
  "environment": "prod",
  "successfulBooking": 1
}

```

### Creating a `DimensionSet`

You can create a separate `DimensionSet` for your metrics using the `addDimensions` method. This allows you to group metrics by different dimension combinations.

When you call `addDimensions()`, it creates a new `DimensionSet` rather than adding to the first set. This is useful when you want to track the same metric across different dimension combinations.

```
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  // Add a single dimension
  metrics.addDimension('environment', 'prod');

  // Add a new dimension set
  metrics.addDimensions({
    dimension1: '1',
    dimension2: '2',
  });

  // Add another dimension set
  metrics.addDimensions({
    region: 'us-east-1',
    category: 'books',
  });

  // Add metrics
  metrics.addMetric('successfulBooking', MetricUnit.Count, 1);
  metrics.publishStoredMetrics();
};

```

```
{
  "_aws": {
    "Timestamp": 1763409658885,
    "CloudWatchMetrics": [
      {
        "Namespace": "serverlessAirline",
        "Dimensions": [
          ["service", "environment"],
          ["dimension1", "dimension2"],
          ["region", "category"]
        ],
        "Metrics": [
          {
            "Name": "successfulBooking",
            "Unit": "Count"
          }
        ]
      }
    ]
  },
  "service": "orders",
  "environment": "prod",
  "dimension1": "1",
  "dimension2": "2",
  "region": "us-east-1",
  "category": "books",
  "successfulBooking": 1
}

```

Autocomplete Metric Units

Use the `MetricUnit` enum to easily find a supported metric unit by CloudWatch. Alternatively, you can pass the value as a string if you already know them e.g. "Count".

Metrics overflow

CloudWatch EMF supports a max of 100 metrics per batch. Metrics will automatically propagate all the metrics when adding the 100th metric. Subsequent metrics, e.g. 101th, will be aggregated into a new EMF object, for your convenience.

Do not create metrics or dimensions outside the handler

Metrics or dimensions added in the global scope will only be added during cold start. Disregard if that's the intended behavior.

### Adding high-resolution metrics

You can create [high-resolution metrics](https://aws.amazon.com/about-aws/whats-new/2023/02/amazon-cloudwatch-high-resolution-metric-extraction-structured-logs/) passing `resolution` as parameter to `addMetric`.

When is it useful?

High-resolution metrics are data with a granularity of one second and are very useful in several situations such as telemetry, time series, real-time incident management, and others.

```
import {
  MetricResolution,
  Metrics,
  MetricUnit,
} from '@aws-lambda-powertools/metrics';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  metrics.addMetric(
    'successfulBooking',
    MetricUnit.Count,
    1,
    MetricResolution.High
  );
};

```

Autocomplete Metric Resolutions

Use the `MetricResolution` type to easily find a supported metric resolution by CloudWatch. Alternatively, you can pass the allowed values of 1 or 60 as an integer.

### Adding multi-value metrics

You can call `addMetric()` with the same name multiple times. The values will be grouped together in an array.

```
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  metrics.addMetric('performedActionA', MetricUnit.Count, 2);
  // do something else...
  metrics.addMetric('performedActionA', MetricUnit.Count, 1);
};

```

```
{
  "performedActionA": [2, 1],
  "_aws": {
    "Timestamp": 1592234975665,
    "CloudWatchMetrics": [
      {
        "Namespace": "serverlessAirline",
        "Dimensions": [["service"]],
        "Metrics": [
          {
            "Name": "performedActionA",
            "Unit": "Count"
          }
        ]
      }
    ]
  },
  "service": "orders"
}

```

### Adding default dimensions

You can add default dimensions to your metrics by passing them as parameters in 4 ways:

- in the constructor
- in the [Middy-compatible](https://github.com/middyjs/middy) middleware
- using the `setDefaultDimensions` method
- in the decorator

```
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
  defaultDimensions: { environment: 'prod', foo: 'bar' },
});

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  metrics.addMetric('successfulBooking', MetricUnit.Count, 1);
};

```

```
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';
import { logMetrics } from '@aws-lambda-powertools/metrics/middleware';
import middy from '@middy/core';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});

const lambdaHandler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  metrics.addMetric('successfulBooking', MetricUnit.Count, 1);
};

// Wrap the handler with middy
export const handler = middy(lambdaHandler)
  // Use the middleware by passing the Metrics instance as a parameter
  .use(
    logMetrics(metrics, {
      defaultDimensions: { environment: 'prod', foo: 'bar' },
    })
  );

```

```
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});
metrics.setDefaultDimensions({ environment: 'prod', foo: 'bar' });

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  metrics.addMetric('successfulBooking', MetricUnit.Count, 1);
};

```

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});
const DEFAULT_DIMENSIONS = { environment: 'prod', foo: 'bar' };

export class Lambda implements LambdaInterface {
  // Decorate your handler class method
  @metrics.logMetrics({ defaultDimensions: DEFAULT_DIMENSIONS })
  public async handler(_event: unknown, _context: unknown): Promise<void> {
    metrics.addMetric('successfulBooking', MetricUnit.Count, 1);
  }
}

const handlerClass = new Lambda();
export const handler = handlerClass.handler.bind(handlerClass); // (1)

```

1. Binding your handler method allows your handler to access `this` within the class methods.

If you'd like to remove them at some point, you can use the `clearDefaultDimensions` method.

### Changing default timestamp

When creating metrics, we use the current timestamp. If you want to change the timestamp of all the metrics you create, utilize the `setTimestamp` function. You can specify a datetime object or an integer representing an epoch timestamp in milliseconds.

Note that when specifying the timestamp using an integer, it must adhere to the epoch timezone format in milliseconds.

```
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  const metricTimestamp = new Date(Date.now() - 24 * 60 * 60 * 1000); // 24 hours ago
  metrics.setTimestamp(metricTimestamp);
  metrics.addMetric('successfulBooking', MetricUnit.Count, 1);
};

```

### Flushing metrics

As you finish adding all your metrics, you need to serialize and "flush them" by calling `publishStoredMetrics()`. This will print the metrics to standard output.

You can flush metrics automatically using one of the following methods:

- manually
- [Middy-compatible](https://github.com/middyjs/middy) middleware
- class decorator

Using the Middy middleware or decorator will **automatically validate, serialize, and flush** all your metrics. During metrics validation, if no metrics are provided then a warning will be logged, but no exception will be thrown. If you do not use the middleware or decorator, you have to flush your metrics manually.

Metric validation

If metrics are provided, and any of the following criteria are not met, a **`RangeError`** error will be thrown:

- Maximum of 29 dimensions
- Namespace is set only once (or none)
- Metric units must be [supported by CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html)

#### Middy middleware

See below an example of how to automatically flush metrics with the Middy-compatible `logMetrics` middleware.

```
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';
import { logMetrics } from '@aws-lambda-powertools/metrics/middleware';
import middy from '@middy/core';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});

const lambdaHandler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  metrics.addMetric('successfulBooking', MetricUnit.Count, 1);
};

export const handler = middy(lambdaHandler).use(logMetrics(metrics));

```

```
{
  "successfulBooking": 1.0,
  "_aws": {
    "Timestamp": 1592234975665,
    "CloudWatchMetrics": [
      {
        "Namespace": "serverlessAirline",
        "Dimensions": [["service"]],
        "Metrics": [
          {
            "Name": "successfulBooking",
            "Unit": "Count"
          }
        ]
      }
    ]
  },
  "service": "orders"
}

```

#### Using the class decorator

Note

The class method decorators in this project follow the experimental implementation enabled via the [`experimentalDecorators` compiler option](https://www.typescriptlang.org/tsconfig#experimentalDecorators) in TypeScript.

Additionally, they are implemented to decorate async methods. When decorating a synchronous one, the decorator replaces its implementation with an async one causing the caller to have to `await` the now decorated method.

If this is not the desired behavior, you can use the `logMetrics` middleware instead.

The `logMetrics` decorator of the metrics utility can be used when your Lambda handler function is implemented as method of a Class.

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});

class Lambda implements LambdaInterface {
  @metrics.logMetrics()
  public async handler(_event: unknown, _context: unknown): Promise<void> {
    metrics.addMetric('successfulBooking', MetricUnit.Count, 1);
  }
}

const handlerClass = new Lambda();
export const handler = handlerClass.handler.bind(handlerClass); // (1)

```

1. Binding your handler method allows your handler to access `this` within the class methods.

```
{
  "successfulBooking": 1.0,
  "_aws": {
    "Timestamp": 1592234975665,
    "CloudWatchMetrics": [
      {
        "Namespace": "successfulBooking",
        "Dimensions": [["service"]],
        "Metrics": [
          {
            "Name": "successfulBooking",
            "Unit": "Count"
          }
        ]
      }
    ]
  },
  "service": "orders"
}

```

#### Manually

You can manually flush the metrics with `publishStoredMetrics` as follows:

Warning

Metrics, dimensions and namespace validation still applies.

```
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  metrics.addMetric('successfulBooking', MetricUnit.Count, 10);
  metrics.publishStoredMetrics();
};

```

```
{
  "successfulBooking": 1.0,
  "_aws": {
    "Timestamp": 1592234975665,
    "CloudWatchMetrics": [
      {
        "Namespace": "successfulBooking",
        "Dimensions": [["service"]],
        "Metrics": [
          {
            "Name": "successfulBooking",
            "Unit": "Count"
          }
        ]
      }
    ]
  },
  "service": "orders"
}

```

#### Throwing a RangeError when no metrics are emitted

If you want to ensure that at least one metric is emitted before you flush them, you can use the `throwOnEmptyMetrics` parameter and pass it to the middleware or decorator:

```
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';
import { logMetrics } from '@aws-lambda-powertools/metrics/middleware';
import middy from '@middy/core';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});

const lambdaHandler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  metrics.addMetric('successfulBooking', MetricUnit.Count, 1);
};

export const handler = middy(lambdaHandler).use(
  logMetrics(metrics, { throwOnEmptyMetrics: true })
);

```

### Capturing a cold start invocation as metric

You can optionally capture cold start metrics with the `logMetrics` middleware or decorator via the `captureColdStartMetric` param.

```
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';
import { logMetrics } from '@aws-lambda-powertools/metrics/middleware';
import middy from '@middy/core';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});

const lambdaHandler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  metrics.addMetric('successfulBooking', MetricUnit.Count, 1);
};

export const handler = middy(lambdaHandler).use(
  logMetrics(metrics, { captureColdStartMetric: true })
);

```

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});

export class MyFunction implements LambdaInterface {
  @metrics.logMetrics({ captureColdStartMetric: true })
  public async handler(_event: unknown, _context: unknown): Promise<void> {
    metrics.addMetric('successfulBooking', MetricUnit.Count, 1);
  }
}

```

If it's a cold start invocation, this feature will:

- Create a separate EMF blob solely containing a metric named `ColdStart`
- Add the `function_name`, `service` and default dimensions

This has the advantage of keeping cold start metric separate from your application metrics, where you might have unrelated dimensions.

We do not emit 0 as a value for the ColdStart metric for cost-efficiency reasons. [Let us know](https://github.com/aws-powertools/powertools-lambda-typescript/issues/new?assignees=&labels=feature-request%2C+triage&template=feature_request.md&title=) if you'd prefer a flag to override it.

#### Setting function name

When emitting cold start metrics, the `function_name` dimension defaults to `context.functionName`. If you want to change the value you can set the `functionName` parameter in the metrics constructor, define the environment variable `POWERTOOLS_METRICS_FUNCTION_NAME`, or pass a value to `captureColdStartMetric`.

The priority of the `function_name` dimension value is defined as:

1. `functionName` constructor option
1. `POWERTOOLS_METRICS_FUNCTION_NAME` environment variable
1. The value passed in the `captureColdStartMetric` call, or `context.functionName` if using logMetrics decorator or Middy middleware

```
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
  functionName: 'my-function-name',
});

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  metrics.captureColdStartMetric();

  metrics.addMetric('successfulBooking', MetricUnit.Count, 1);

  metrics.publishStoredMetrics();
};

```

```
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  metrics.captureColdStartMetric('my-function-name');

  metrics.addMetric('successfulBooking', MetricUnit.Count, 1);

  metrics.publishStoredMetrics();
};

```

## Advanced

### Adding metadata

You can add high-cardinality data as part of your Metrics log with the `addMetadata` method. This is useful when you want to search highly contextual information along with your metrics in your logs.

Info

**This will not be available during metrics visualization** - Use **dimensions** for this purpose

```
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';
import { logMetrics } from '@aws-lambda-powertools/metrics/middleware';
import middy from '@middy/core';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});

const lambdaHandler = async (
  _event: unknown,
  _context: unknown
): Promise<void> => {
  metrics.addMetric('successfulBooking', MetricUnit.Count, 1);
  metrics.addMetadata('bookingId', '7051cd10-6283-11ec-90d6-0242ac120003');
};

export const handler = middy(lambdaHandler).use(logMetrics(metrics));

```

```
{
  "successfulBooking": 1.0,
  "_aws": {
    "Timestamp": 1592234975665,
    "CloudWatchMetrics": [
      {
        "Namespace": "serverlessAirline",
        "Dimensions": [["service"]],
        "Metrics": [
          {
            "Namespace": "exampleApplication",
            "Dimensions": [["service"]],
            "Metrics": [
              {
                "Name": "successfulBooking",
                "Unit": "Count"
              }
            ]
          }
        ]
      }
    ]
  },
  "service": "orders",
  "bookingId": "7051cd10-6283-11ec-90d6-0242ac120003"
}

```

### Single metric with different dimensions

CloudWatch EMF uses the same dimensions across all your metrics. Use `singleMetric` if you have a metric that should have different dimensions.

Generally, using different dimensions would be an edge case since you [pay for unique metric](https://aws.amazon.com/cloudwatch/pricing).

Keep the following formula in mind: `unique metric = (metric_name + dimension_name + dimension_value)`.

```
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'orders',
});

export const handler = async (event: { orderId: string }) => {
  const singleMetric = metrics.singleMetric();
  singleMetric.addDimension('metricType', 'business');
  singleMetric.addMetadata('orderId', event.orderId); // (1)!
  singleMetric.addMetric('successfulBooking', MetricUnit.Count, 1); // (2)!
};

```

1. Metadata should be added before calling `addMetric()` to ensure it's included in the same EMF blob.
1. Single metrics are emitted as soon as `addMetric()` is called, so you don't need to call `publishStoredMetrics()`.

### Customizing the logger

You can customize how Metrics logs warnings and debug messages to standard output by passing a custom logger as a constructor parameter. This is useful when you want to silence warnings or debug messages, or when you want to log them to a different output.

```
import { Logger, LogLevel } from '@aws-lambda-powertools/logger';
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';

const logger = new Logger({ logLevel: LogLevel.CRITICAL });
const metrics = new Metrics({
  serviceName: 'serverless-airline',
  namespace: 'orders',
  singleMetric: true,
  logger,
});

metrics.addMetric('successfulBooking', MetricUnit.Count, 1);

```

## Testing your code

When unit testing your code that uses the Metrics utility, you may want to silence the logs emitted by the utility. To do so, you can set the `POWERTOOLS_DEV` environment variable to `true`. This instructs the utility to not emit any logs to standard output.

If instead you want to spy on the logs emitted by the utility, you must set the `POWERTOOLS_DEV` environment variable to `true` in conjunction with the `POWERTOOLS_METRICS_DISABLED` environment variable set to `false`.

When `POWERTOOLS_DEV` is enabled, Metrics uses the global `console` to emit metrics to standard out. This allows you to easily spy on the logs emitted and make assertions on them.

```
import { describe, expect, it, vi } from 'vitest';

vi.hoisted(() => {
  process.env.POWERTOOLS_DEV = 'true';
  process.env.POWERTOOLS_METRICS_DISABLED = 'false';
});

describe('Metrics tests', () => {
  it('emits metrics properly', async () => {
    // Prepare
    const metricsEmittedSpy = vi
      .spyOn(console, 'log')
      .mockImplementation(() => {});

    // Act
    // ...

    // Assess
    expect(metricsEmittedSpy).toHaveBeenCalledOnce();
  });
});

```

Event handler for Amazon API Gateway REST and HTTP APIs, Application Loader Balancer (ALB), and Lambda Function URLs.

## Key Features

- Lightweight routing to reduce boilerplate for API Gateway REST/HTTP API, ALB and Lambda Function URLs.
- Built-in middleware engine for request/response transformation (validation coming soon).
- Works with micro function (one or a few routes) and monolithic functions (see [Considerations](#considerations)).

## Getting started

### Install

```
npm install @aws-lambda-powertools/event-handler

```

### Required resources

The event handler works with different types of events. It can process events from API Gateway REST APIs, HTTP APIs, ALB, Lambda Function URLs, and will soon support VPC Lattice as well.

You must have an existing integration configured to invoke your Lambda function depending on what you are using:

| Integration               | Documentation                                                                                                               |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| API Gateway REST API      | [Proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html)     |
| API Gateway HTTP API      | [Proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html) |
| Application Load Balancer | [ALB configuration](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html)              |
| Lambda Function URL       | [Function URL configuration](https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html)                          |

This is the sample infrastructure for the different integrations we are using for the examples in this documentation. There is no additional permissions or dependencies required to use this utility.

See Infrastructure as Code (IaC) examples

```
AWSTemplateFormatVersion: "2010-09-09"
Transform: AWS::Serverless-2016-10-31
Description: Hello world event handler API Gateway REST API

Globals:
  Api:
    TracingEnabled: true
    Cors: # see CORS section
      AllowOrigin: "'https://example.com'"
      AllowHeaders: "'Content-Type,Authorization,X-Amz-Date'"
      MaxAge: "'300'"
    BinaryMediaTypes: # see Binary responses section
      - "*~1*" # converts to */* for any binary type
      # NOTE: use this stricter version if you're also using CORS; */* doesn't work with CORS
      # see: https://github.com/aws-powertools/powertools-lambda-python/issues/3373#issuecomment-1821144779
      # - "image~1*" # converts to image/*
      # - "*~1csv" # converts to */csv, eg text/csv, application/csv

  Function:
    Timeout: 5
    MemorySize: 256
    Runtime: nodejs24.x
    Tracing: Active
    Environment:
      Variables:
        POWERTOOLS_LOG_LEVEL: INFO
        POWERTOOLS_SERVICE_NAME: hello

Resources:
  ApiFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.handler
      CodeUri: hello_world
      Description: API handler function
      Events:
        AnyApiEvent:
          Type: Api
          Properties:
            # NOTE: this is a catch-all rule to simplify the documentation.
            # explicit routes and methods are recommended for prod instead (see below)
            Path: /{proxy+} # Send requests on any path to the lambda function
            Method: ANY # Send requests using any http method to the lambda function
        GetAllTodos:
           Type: Api
           Properties:
             Path: /todos
             Method: GET
        GetTodoById:
           Type: Api
           Properties:
             Path: /todos/{todo_id}
             Method: GET

```

```
AWSTemplateFormatVersion: "2010-09-09"
Transform: AWS::Serverless-2016-10-31
Description: Hello world event handler API Gateway HTTP API

Globals:
  HttpApi:
    CorsConfiguration:
      AllowOrigins:
        - https://example.com
      AllowHeaders:
        - Content-Type
        - Authorization
        - X-Amz-Date
      MaxAge: 300

  Function:
    Timeout: 5
    MemorySize: 256
    Runtime: nodejs22.x
    Tracing: Active
    Environment:
      Variables:
        POWERTOOLS_LOG_LEVEL: INFO
        POWERTOOLS_SERVICE_NAME: hello

Resources:
  ApiFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.handler
      CodeUri: hello_world
      Description: API handler function
      Events:
        AnyApiEvent:
          Type: HttpApi
          Properties:
            Path: /{proxy+}
            Method: ANY
        GetAllTodos:
           Type: HttpApi
           Properties:
             Path: /todos
             Method: GET
        GetTodoById:
           Type: HttpApi
           Properties:
             Path: /todos/{todo_id}
             Method: GET

```

```
AWSTemplateFormatVersion: "2010-09-09"
Transform: AWS::Serverless-2016-10-31
Description: Hello world event handler Lambda Function URL

Globals:
  Function:
    Timeout: 5
    MemorySize: 256
    Runtime: nodejs24.x
    Tracing: Active
    Environment:
      Variables:
        POWERTOOLS_LOG_LEVEL: INFO
        POWERTOOLS_SERVICE_NAME: hello
    FunctionUrlConfig:
      Cors: # see CORS section
        # Notice that values here are Lists of Strings, vs comma-separated values on API Gateway
        AllowOrigins: ["https://example.com"]
        AllowHeaders: ["Content-Type", "Authorization", "X-Amz-Date"]
        MaxAge: 300

Resources:
  ApiFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.handler
      CodeUri: hello_world
      Description: API handler function
      FunctionUrlConfig:
        AuthType: NONE # AWS_IAM for added security beyond sample documentation

```

### Route events

When a request is received, the event handler automatically detects the event type and converts it into a [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) object.

You get access to headers, query parameters, request body, and path parameters via typed arguments. The response type is determined automatically based on the event.

#### Response auto-serialization

Want full control over the response, headers, and status code? Read how to [return `Response` objects](#returning-response-objects) directly.

For your convenience, when you return a JavaScript object from your route handler, we automatically perform these actions:

- Auto-serialize the response to JSON
- Include the response under the appropriate equivalent of a `body`
- Set the `Content-Type` header to `application/json`
- Set the HTTP status code to 200 (OK)

```
import { Router } from '@aws-lambda-powertools/event-handler/http';
import type { Context } from 'aws-lambda';

const app = new Router();

app.get('/ping', async () => {
  return { message: 'pong' }; // (1)!
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

1. This object will be serialized and included under the `body` key

```
{
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json"
  },
  "body": "{'message':'pong'}",
  "isBase64Encoded": false
}

```

Automatic response format transformation

The event handler automatically ensures the correct response format is returned based on the event type received. For example, if your handler returns an API Gateway v1 proxy response but processes an ALB event, we'll automatically transform it into an ALB-compatible response. This allows you to swap integrations with little to no code changes.

### Dynamic routes

You can use `/todos/:todoId` to configure dynamic URL paths, where `:todoId` will be resolved at runtime.

All dynamic route parameters will be available as typed object properties in the first argument of your route handler.

```
import { Router } from '@aws-lambda-powertools/event-handler/http';
import { Logger } from '@aws-lambda-powertools/logger';
import {
  correlationPaths,
  search,
} from '@aws-lambda-powertools/logger/correlationId';
import type { Context } from 'aws-lambda/handler';

const logger = new Logger({
  correlationIdSearchFn: search,
});
const app = new Router({ logger });

app.get('/todos/:todoId', async ({ params: { todoId } }) => {
  const todo = await getTodoById(todoId);
  return { todo };
});

export const handler = async (event: unknown, context: Context) => {
  // You can continue using other utilities just as before
  logger.addContext(context);
  logger.setCorrelationId(event, correlationPaths.API_GATEWAY_REST);
  return app.resolve(event, context);
};

```

```
{
  "resource": "/todos/{id}",
  "path": "/todos/1",
  "httpMethod": "GET"
}

```

You can also nest dynamic paths, for example `/todos/:todoId/comments/:commentId`, where both `:todoId` and `:commentId` will be resolved at runtime.

#### Catch-all routes

For scenarios where you need to handle arbitrary or deeply nested paths, you can use regex patterns directly in your route definitions. These are particularly useful for proxy routes or when dealing with file paths.

**We recommend** having explicit routes whenever possible; use catch-all routes sparingly.

##### Using Regex Patterns

You can use standard [regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions) in your route definitions, for example:

| Pattern   | Description                              | Examples                                                    |
| --------- | ---------------------------------------- | ----------------------------------------------------------- |
| `/.+/`    | Matches one or more characters (greedy)  | `/\/proxy\/.+/` matches `/proxy/any/deep/path`              |
| `/.*/`    | Matches zero or more characters (greedy) | `/\/files\/.*/` matches `/files/` and `/files/deep/path`    |
| `/[^/]+/` | Matches one or more non-slash characters | `/\/api\/[^\/]+/` matches `/api/v1` but not `/api/v1/users` |
| `/\w+/`   | Matches one or more word characters      | `/\/users\/\w+/` matches `/users/john123`                   |

```
import { Router } from '@aws-lambda-powertools/event-handler/http';
import type { APIGatewayProxyEvent, Context } from 'aws-lambda';

const app = new Router();

// File path proxy
app.get(/\/files\/.+/, () => 'Catch any GET method under /files');

// API versioning with any format
app.get(/\/api\/v\d+\/.*/, () => 'Catch any GET method under /api/vX');

// Mixed: dynamic parameter + regex catch-all
app.get(/\/users\/:userId\/files\/.+/, (reqCtx) => {
  return {
    userId: reqCtx.params.userId,
  };
});

// Catch all route
app.get(/.+/, () => 'Catch any GET method');

export const handler = async (event: APIGatewayProxyEvent, context: Context) =>
  app.resolve(event, context);

```

Route Matching Priority

- For non-regex routes, routes are matched in **order of specificity**, not registration order
- More specific routes (exact matches) take precedence over regex patterns
- Among regex routes, registration order determines matching precedence, therefore, always place catch-all routes `/.*/` last

### HTTP Methods

You can use dedicated methods to specify the HTTP method that should be handled in each resolver. That is, `app.<httpMethod>()`, where the HTTP method could be `delete`, `get`, `head`, `patch`, `post`, `put`, `options`.

```
import { Router } from '@aws-lambda-powertools/event-handler/http';
import { Logger } from '@aws-lambda-powertools/logger';
import {
  correlationPaths,
  search,
} from '@aws-lambda-powertools/logger/correlationId';
import type { Context } from 'aws-lambda/handler';

const logger = new Logger({
  correlationIdSearchFn: search,
});
const app = new Router({ logger });

app.post('/todos', async ({ req }) => {
  const body = await req.json();
  const todo = await putTodo(body);

  return todo;
});

export const handler = async (event: unknown, context: Context) => {
  // You can continue using other utilities just as before
  logger.addContext(context);
  logger.setCorrelationId(event, correlationPaths.API_GATEWAY_REST);
  return app.resolve(event, context);
};

```

```
{
  "resource": "/todos",
  "path": "/todos",
  "httpMethod": "POST",
  "body": "{\"title\": \"foo\", \"userId\": 1, \"completed\": false}"
}

```

If you need to accept multiple HTTP methods in a single function, or support an HTTP method for which no dedicated method exists (i.e. [`TRACE`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/TRACE)), you can use the `route()` method and pass a list of HTTP methods.

```
import { Router } from '@aws-lambda-powertools/event-handler/http';
import { Logger } from '@aws-lambda-powertools/logger';
import {
  correlationPaths,
  search,
} from '@aws-lambda-powertools/logger/correlationId';
import type { Context } from 'aws-lambda/handler';

const logger = new Logger({
  correlationIdSearchFn: search,
});
const app = new Router({ logger });

app.route(
  async ({ req }) => {
    const body = await req.json();
    const todo = await putTodo(body);

    return todo;
  },
  {
    path: '/todos',
    method: ['POST', 'PUT'],
  }
);

export const handler = async (event: unknown, context: Context) => {
  // You can continue using other utilities just as before
  logger.addContext(context);
  logger.setCorrelationId(event, correlationPaths.API_GATEWAY_REST);
  return app.resolve(event, context);
};

```

Tip

We recommend defining separate route handlers for each HTTP method within your Lambda function, as the functionality typically differs between operations such as `GET`, `POST`, `PUT`, `DELETE` etc

### Data validation

Coming soon

We plan to add built-in support for request and response validation using [Standard Schema](https://standardschema.dev) in a future release. For the time being, you can use any validation library of your choice in your route handlers or middleware.

Please [check this issue](https://github.com/aws-powertools/powertools-lambda-typescript/issues/4516) for more details and examples, and add ð if you would like us to prioritize it.

### Accessing request details

You can access request details such as headers, query parameters, and body using the `Request` object provided to your route handlers and middleware functions via `reqCtx.req`.

### Error handling

You can use the `errorHandler()` method as a higher-order function or class method decorator to define a custom error handler for errors thrown in your route handlers or middleware.

This allows you to catch and return custom error responses, or perform any other error handling logic you need.

Error handlers receive the error object and the request context as arguments, and can return a [`Response` object](#returning-response-objects) or a JavaScript object that will be auto-serialized as per the [response auto-serialization](#response-auto-serialization) section.

You can also pass a list of error classes to the `errorHandler()` method.

```
import {
  HttpStatusCodes,
  Router,
} from '@aws-lambda-powertools/event-handler/http';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda/handler';

const logger = new Logger();
const app = new Router({ logger });

app.errorHandler(GetTodoError, async (error, reqCtx) => {
  logger.error('Unable to get todo', { error });

  return {
    statusCode: HttpStatusCodes.BAD_REQUEST,
    message: `Bad request: ${error.message} - ${reqCtx.req.headers.get('x-correlation-id')}`,
  };
});

app.get('/todos/:todoId', async ({ params: { todoId } }) => {
  const todo = await getTodoById(todoId); // May throw GetTodoError
  return { todo };
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

### Built-in Error Handlers

We provide built-in error handlers for common routing errors so you don't have to specify the Error type explicitly.

You can use the `notFound()` and `methodNotAllowed()` methods as higher-order functions or class method decorators to customize error responses for unmatched routes and unsupported HTTP methods.

By default, we return a `404 Not Found` response for unmatched routes.

```
import {
  HttpStatusCodes,
  Router,
} from '@aws-lambda-powertools/event-handler/http';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda/handler';

const logger = new Logger();
const app = new Router({ logger });

app.notFound(async (error, reqCtx) => {
  logger.error('Unable to get todo', { error });

  return {
    statusCode: HttpStatusCodes.IM_A_TEAPOT,
    body: "I'm a teapot!",
    headers: {
      'x-correlation-id': reqCtx.req.headers.get('x-correlation-id'),
    },
  };
});

app.methodNotAllowed(async (error) => {
  logger.error('Method not allowed', { error });

  return {
    body: 'This method is not allowed',
  };
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

### Throwing HTTP errors

You can throw HTTP errors in your route handlers to stop execution and return specific HTTP status codes and messages. Event Handler provides a set of built-in HTTP error classes that you can use to throw common HTTP errors.

This ensures that your Lambda function doesn't fail but returns a well-defined HTTP error response to the client.

If you need to send custom headers or a different response structure/code, you can use the [Response](#returning-response-objects) object instead.

You can throw HTTP errors in your route handlers, middleware, or custom error handlers!

```
import {
  Router,
  UnauthorizedError,
} from '@aws-lambda-powertools/event-handler/http';
import type { Context } from 'aws-lambda';

const app = new Router();

app.use(async ({ reqCtx, next }) => {
  if (!isAuthenticated(reqCtx.req.headers.get('Authorization') ?? '')) {
    throw new UnauthorizedError(); // This will return a 401 Unauthorized response
  }
  await next();
});

app.get('/secure', async () => {
  return { message: 'super important data' };
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

#### Available HTTP error classes

The following HTTP error classes are available for use in your route handlers:

| Error Class                  | HTTP Status Code | Description                                                                            |
| ---------------------------- | ---------------- | -------------------------------------------------------------------------------------- |
| `BadRequestError`            | 400              | Bad Request - The request cannot be fulfilled due to bad syntax                        |
| `UnauthorizedError`          | 401              | Unauthorized - Authentication is required and has failed or not been provided          |
| `ForbiddenError`             | 403              | Forbidden - The request is valid but the server is refusing action                     |
| `NotFoundError`              | 404              | Not Found - The requested resource could not be found                                  |
| `MethodNotAllowedError`      | 405              | Method Not Allowed - The request method is not supported for the requested resource    |
| `RequestTimeoutError`        | 408              | Request Timeout - The server timed out waiting for the request                         |
| `RequestEntityTooLargeError` | 413              | Request Entity Too Large - The request is larger than the server is willing to process |
| `InternalServerError`        | 500              | Internal Server Error - A generic error message for unexpected server conditions       |
| `ServiceUnavailableError`    | 503              | Service Unavailable - The server is currently unavailable                              |

All error classes accept optional parameters for custom messages and additional details:

- `message` - Custom error message
- `options` - Standard JavaScript `ErrorOptions`
- `details` - Additional structured data to include in the error response

### Route prefixes

When defining multiple routes related to a specific resource, it's common to have a shared prefix. For example, you might have several routes that all start with `/todos`.

For example, if you have a custom domain `api.example.com` and you want to map it to the `/v1` base path of your API. In this case, all the requests will contain `/v1/<resource>` in the path, requiring you to repeat the `/v1` prefix in all your route definitions.

To avoid repeating the prefix in each route definition, you can use the `prefix` constructor parameter when creating a new `Router` instance, and we'll automatically strip it from the request path before matching routes. After mapping a path prefix, the new root path will automatically be mapped to the path argument of `/`.

```
import { Router } from '@aws-lambda-powertools/event-handler/http';
import type { Context } from 'aws-lambda';

const app = new Router({ prefix: '/todos' });

// matches POST /todos
app.post('/', async ({ req: { headers } }) => {
  const todos = await getUserTodos(headers.get('Authorization'));
  return { todos };
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

This is also useful when splitting routes into separate files (see [Split routers](#split-routers) section) or when using [API mappings](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-mappings.html) to map custom domains to specific base paths.

For example, when using `prefix: '/pay'`, there is no difference between a request path of `/pay` and `/pay/`; and the path argument would be defined as `/`.

## Advanced

### Middleware

Middleware are functions that execute during the request-response cycle, sitting between the incoming request and your route handler. They provide a way to implement cross-cutting concerns like authentication, logging, validation, and response transformation without cluttering your route handlers.

Each middleware function receives two arguments:

- **reqCtx** - Request context containing the event, Lambda context, request, and response objects
- **next** - A function to pass control to the next middleware in the chain

Middleware can be applied on specific routes, globally on all routes, or a combination of both.

Middleware execution follows an onion pattern where global middleware runs first in pre-processing, then route-specific middleware. After the handler executes, the order reverses for post-processing. When middleware modify the same response properties, the middleware that executes last in post-processing wins.

```
sequenceDiagram
    participant Request
    participant Router
    participant GM as Global Middleware
    participant RM as Route Middleware
    participant Handler as Route Handler

    Request->>Router: Incoming Request
    Router->>GM: Execute ({ reqCtx, next })
    Note over GM: Pre-processing
    GM->>RM: Call await next()
    Note over RM: Pre-processing
    RM->>Handler: Call await next()
    Note over Handler: Execute handler
    Handler-->>RM: Return
    Note over RM: Post-processing
    RM-->>GM: Return
    Note over GM: Post-processing
    GM-->>Router: Return
    Router-->>Request: Response

```

#### Registering middleware

You can use `app.use()` to register middleware that should always run regardless of the route and you can apply middleware to specific routes by passing them as arguments before the route handler.

```
import { Router } from '@aws-lambda-powertools/event-handler/http';
import type { Middleware } from '@aws-lambda-powertools/event-handler/types';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';

const logger = new Logger();
const app = new Router({ logger });

// Global middleware - executes first in pre-processing, last in post-processing
app.use(async ({ reqCtx, next }) => {
  reqCtx.res.headers.set('x-pre-processed-by', 'global-middleware');
  await next();
  reqCtx.res.headers.set('x-post-processed-by', 'global-middleware');
});

// Route-specific middleware - executes second in pre-processing, first in post-processing
const routeMiddleware: Middleware = async ({ reqCtx, next }) => {
  reqCtx.res.headers.set('x-pre-processed-by', 'route-middleware');
  await next();
  reqCtx.res.headers.set('x-post-processed-by', 'route-middleware');
};

app.get('/todos', async () => {
  const todos = await getAllTodos();
  return { todos };
});

// This route will have:
// x-pre-processed-by: route-middleware (route middleware overwrites global)
// x-post-processed-by: global-middleware (global middleware executes last)
app.post('/todos', [routeMiddleware], async ({ req }) => {
  const body = await req.json();
  const todo = await putTodo(body);
  return todo;
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

```
{
  "statusCode": 200,
  "body": "{\"id\":\"123\",\"title\":\"New todo\"}",
  "headers": {
    "content-type": "application/json",
    "x-pre-processed-by": "route-middleware",
    "x-post-processed-by": "global-middleware"
  },
  "isBase64Encoded": false
}

```

#### Returning early

There are cases where you may want to terminate the execution of the middleware chain early. To do so, middleware can short-circuit processing by returning a `Response` or JSON object instead of calling `await next()`.

Neither the handler nor any subsequent middleware will run but the post-processing of already executed middleware will.

```
sequenceDiagram
    participant Request
    participant Router
    participant M1 as Middleware 1
    participant M2 as Middleware 2
    participant M3 as Middleware 3
    participant Handler as Route Handler

    Request->>Router: Incoming Request
    Router->>M1: Execute ({ reqCtx, next })
    Note over M1: Pre-processing
    M1->>M2: Call await next()
    Note over M2: Pre-processing
    M2->>M2: Return Response (early return)
    Note over M2: Post-processing
    M2-->>M1: Return Response
    Note over M1: Post-processing
    M1-->>Router: Return Response
    Router-->>Request: Response
    Note over M3,Handler: Never executed
```

```
import { Router } from '@aws-lambda-powertools/event-handler/http';
import type { Middleware } from '@aws-lambda-powertools/event-handler/types';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';

const logger = new Logger();
const app = new Router({ logger });

// Authentication middleware - returns early if no auth header
const authMiddleware: Middleware = async ({ reqCtx, next }) => {
  const authHeader = reqCtx.req.headers.get('authorization');

  if (!authHeader) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), {
      status: 401,
      headers: { 'Content-Type': 'application/json' },
    });
  }

  await next();
};

// Logging middleware - never executes when auth fails
const loggingMiddleware: Middleware = async ({ next }) => {
  logger.info('Request processed');
  await next();
};

app.use(authMiddleware);
app.use(loggingMiddleware);

app.get('/todos', async () => {
  const todos = await getAllTodos();
  return { todos };
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

```
{
  "statusCode": 401,
  "body": "{\"error\":\"Unauthorized\"}",
  "headers": {
    "Content-Type": "application/json"
  },
  "isBase64Encoded": false
}

```

#### Error Handling

By default, any unhandled error in the middleware chain will be propagated as a HTTP 500 back to the client. As you would expect, unlike early return, this stops the middleware chain entirely and no post-processing steps for any previously executed middleware will occur.

```
sequenceDiagram
    participant Request
    participant Router
    participant EH as Error Handler
    participant M1 as Middleware 1
    participant M2 as Middleware 2
    participant Handler as Route Handler

    Request->>Router: Incoming Request
    Router->>M1: Execute ({ reqCtx, next })
    Note over M1: Pre-processing
    M1->>M2: Call await next()
    Note over M2: Throws Error
    M2-->>M1: Error propagated
    M1-->>Router: Error propagated
    Router->>EH: Handle error
    EH-->>Router: HTTP 500 Response
    Router-->>Request: HTTP 500 Error
    Note over Handler: Never executed
```

*Unhandled errors*

You can handle errors in middleware as you would anywhere else, simply surround your code in a `try`/`catch` block and processing will occur as usual.

```
sequenceDiagram
    participant Request
    participant Router
    participant M1 as Middleware 1
    participant M2 as Middleware 2
    participant Handler as Route Handler

    Request->>Router: Incoming Request
    Router->>M1: Execute ({ reqCtx, next })
    Note over M1: Pre-processing
    M1->>M2: Call await next()
    Note over M2: Error thrown & caught
    Note over M2: Handle error gracefully
    M2->>Handler: Call await next()
    Note over Handler: Execute handler
    Handler-->>M2: Return
    Note over M2: Post-processing
    M2-->>M1: Return
    Note over M1: Post-processing
    M1-->>Router: Return
    Router-->>Request: Response
```

*Handled errors*

Similarly, you can choose to stop processing entirely by throwing an error in your middleware. Event handler provides many [built-in HTTP errors](#throwing-http-errors) that you can use or you can throw a custom error of your own. As noted above, this means that no post-processing of your request will occur.

```
sequenceDiagram
    participant Request
    participant Router
    participant EH as Error Handler
    participant M1 as Middleware 1
    participant M2 as Middleware 2
    participant Handler as Route Handler

    Request->>Router: Incoming Request
    Router->>M1: Execute ({ reqCtx, next })
    Note over M1: Pre-processing
    M1->>M2: Call await next()
    Note over M2: Intentionally throws error
    M2-->>M1: Error propagated
    M1-->>Router: Error propagated
    Router->>EH: Handle error
    EH-->>Router: HTTP Error Response
    Router-->>Request: HTTP Error Response
    Note over Handler: Never executed

```

*Intentional errors*

#### Custom middleware

A common pattern to create reusable middleware is to implement a factory functions that accepts configuration options and returns a middleware function.

Always `await next()` unless returning early

Middleware functions must always call `await next()` to pass control to the next middleware in the chain, unless you are intentionally returning early by returning a `Response` or JSON object.

```
import { getStringFromEnv } from '@aws-lambda-powertools/commons/utils/env';
import {
  Router,
  UnauthorizedError,
} from '@aws-lambda-powertools/event-handler/http';
import type { Middleware } from '@aws-lambda-powertools/event-handler/types';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';

const jwtSecret = getStringFromEnv({
  key: 'JWT_SECRET',
  errorMessage: 'JWT_SECRET is not set',
});

const logger = new Logger({});
const app = new Router();
const store: { userId: string; roles: string[] } = { userId: '', roles: [] };

// Factory function that returns middleware
const verifyToken = (options: { jwtSecret: string }): Middleware => {
  return async ({ reqCtx: { req }, next }) => {
    const auth = req.headers.get('Authorization');
    if (!auth || !auth.startsWith('Bearer '))
      throw new UnauthorizedError('Missing or invalid Authorization header');

    const token = auth.slice(7);
    try {
      const payload = jwt.verify(token, options.jwtSecret);
      store.userId = payload.sub;
      store.roles = payload.roles;
    } catch (error) {
      logger.error('Token verification failed', { error });
      throw new UnauthorizedError('Invalid token');
    }

    await next();
  };
};

// Use custom middleware globally
app.use(verifyToken({ jwtSecret }));

app.post('/todos', async () => {
  const { userId } = store;
  const todos = await getUserTodos(userId);
  return { todos };
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

In this example we have a middleware that acts only in the post-processing stage as all the logic occurs after the `next` function has been called. This is so as to ensure that the handler has run and we have access to request body.

#### Avoiding destructuring pitfalls

Never destructure the response object

When writing middleware, always access the response through `reqCtx.res` rather than destructuring `{ res }` from the request context. Destructuring captures a reference to the original response object, which becomes stale when middleware replaces the response.

```
import type { Context } from 'aws-lambda';

const app = new Router();

// â WRONG: Using destructuring captures a reference to the original response
const _badMiddleware: Middleware = async ({ reqCtx: { res }, next }) => {
  res.headers.set('X-Before', 'Before');
  await next();
  // This header will NOT be added because 'res' is a stale reference
  res.headers.set('X-After', 'After');
};

// â CORRECT: Always access response through reqCtx
const goodMiddleware: Middleware = async ({ reqCtx, next }) => {
  reqCtx.res.headers.set('X-Before', 'Before');
  await next();
  // This header WILL be added because we get the current response
  reqCtx.res.headers.set('X-After', 'After');
};

app.use(goodMiddleware);

app.get('/test', async () => {
  return { message: 'Hello World!' };
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

During the middleware execution chain, the response object (`reqCtx.res`) can be replaced by other middleware or the route handler. When you destructure the request context, you capture a reference to the response object as it existed at that moment, not the current response.

#### Composing middleware

You can create reusable middleware stacks by using the `composeMiddleware` function to combine multiple middleware into a single middleware function. This is useful for creating standardized middleware combinations that can be shared across different routes or applications.

```
import { composeMiddleware } from '@aws-lambda-powertools/event-handler/http';
import { cors } from '@aws-lambda-powertools/event-handler/http/middleware';
import type { Middleware } from '@aws-lambda-powertools/event-handler/types';
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger();

const logging: Middleware = async ({ reqCtx, next }) => {
  logger.info(`Request: ${reqCtx.req.method} ${reqCtx.req.url}`);
  await next();
  logger.info(`Response: ${reqCtx.res.status}`);
};

const rateLimit: Middleware = async ({ reqCtx, next }) => {
  // Rate limiting logic would go here
  reqCtx.res.headers.set('X-RateLimit-Limit', '100');
  await next();
};

// Reusable composed middleware
const apiMiddleware = composeMiddleware([logging, cors(), rateLimit]);

export { apiMiddleware };

```

```
import { Router } from '@aws-lambda-powertools/event-handler/http';
import type { Context } from 'aws-lambda';
import { apiMiddleware } from './advanced_mw_compose_middleware_shared.js';

const app = new Router();

app.use(apiMiddleware);

app.get('/todos', async () => {
  const todos = await getAllTodos();
  return { todos };
});

app.post('/todos', async ({ req }) => {
  const body = await req.json();
  const todo = await putTodo(body);
  return todo;
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

The `composeMiddleware` function maintains the same execution order as if you had applied the middleware individually, following the onion pattern where middleware execute in order during pre-processing and in reverse order during post-processing.

Composition order

Unlike traditional function composition which typically works right-to-left, `composeMiddleware` follows the convention used by most web frameworks and executes middleware left-to-right (first to last in the array). This means `composeMiddleware([a, b, c])` executes middleware `a` first, then `b`, then `c`.

#### Being a good citizen

Middleware can add subtle improvements to request/response processing, but also add significant complexity if you're not careful.

Keep the following in mind when authoring middleware for Event Handler:

- **Call the next middleware.** If you are not returning early by returning a `Response` object or JSON object, always ensure you call the `next` function.
- **Keep a lean scope.** Focus on a single task per middleware to ease composability and maintenance.
- **Catch your own errors.** Catch and handle known errors to your logic, unless you want to raise HTTP Errors, or propagate specific errors to the client.
- **Avoid destructuring the response object.** As mentioned in the [destructuring pitfalls](#avoiding-destructuring-pitfalls) section, always access the response through `reqCtx.res` rather than destructuring to avoid stale references.

### Returning `Response` objects

You can use the Web API's `Response` object to have full control over the response. For example, you might want to add additional headers, cookies, or set a custom content type.

```
import { Router } from '@aws-lambda-powertools/event-handler/http';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';

const logger = new Logger();
const app = new Router({ logger });

app.get('/todos', async () => {
  const todos = await getAllTodos();

  return new Response(JSON.stringify({ todos }), {
    status: 200,
    headers: {
      'Content-Type': 'application/json',
      'Cache-Control': 'max-age=300',
      'X-Custom-Header': 'custom-value',
    },
  });
});

app.post('/todos', async ({ req }) => {
  const body = await req.json();
  const todo = await createTodo(body.title);

  return new Response(JSON.stringify(todo), {
    status: 201,
    headers: {
      Location: `/todos/${todo.id}`,
      'Content-Type': 'application/json',
    },
  });
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

```
{
  "statusCode": 201,
  "body": "{\"id\":\"123\",\"title\":\"Learn TypeScript\"}",
  "headers": {
    "Content-Type": "application/json",
    "Location": "/todos/123"
  },
  "isBase64Encoded": false
}

```

### CORS

You can configure CORS (Cross-Origin Resource Sharing) by using the `cors` middleware.

This will ensure that CORS headers are returned as part of the response when your functions match the path invoked and the Origin matches one of the allowed values.

```
import { Router } from '@aws-lambda-powertools/event-handler/http';
import { cors } from '@aws-lambda-powertools/event-handler/http/middleware';
import type { Context } from 'aws-lambda';

const app = new Router();

app.use(
  cors({
    origin: 'https://example.com',
    maxAge: 300,
  })
);

app.get('/todos/:todoId', async ({ params: { todoId } }) => {
  const todo = await getTodoById(todoId);
  return { todo };
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

```
{
  "statusCode": 200,
  "headers": {
    "access-control-allow-credentials": "false",
    "access-control-allow-origin": "https://example.com",
    "content-type": "application/json"
  },
  "multiValueHeaders": {
    "access-control-allow-headers": [
      "Authorization",
      "Content-Type",
      "X-Amz-Date",
      "X-Api-Key",
      "X-Amz-Security-Token"
    ],
    "access-control-allow-methods": [
      "DELETE",
      "GET",
      "HEAD",
      "PATCH",
      "POST",
      "PUT"
    ]
  },
  "body": "{\"todoId\":\"123\",\"task\":\"Example task\",\"completed\":false}",
  "isBase64Encoded": false
}

```

#### Pre-flight

Pre-flight (`OPTIONS`) requests are typically handled at the API Gateway or Lambda Function URL as per our [sample infrastructure](#required-resources), no Lambda integration is necessary. However, ALB expects you to handle pre-flight requests in your function.

For convenience, when you register the `cors` middleware, we automatically handle these requests for you as long as the path matches and the `Origin` header is present and valid.

#### Defaults

For convenience, these are the default CORS settings applied when you register the `cors` middleware without any options:

Security consideration

Always set the `origin` option to a specific domain or list of domains in production environments to avoid security risks associated with allowing all origins.

| Key             | Default Value                                                                | Description                                                                                                                                              |
| --------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `origin`        | `*`                                                                          | Specifies the allowed origin(s) that can access the resource. Use `*` to allow all origins.                                                              |
| `methods`       | `['DELETE', 'GET', 'HEAD', 'PATCH', 'POST', 'PUT']`                          | Specifies the allowed HTTP methods.                                                                                                                      |
| `allowHeaders`  | `[Authorization, Content-Type, X-Amz-Date, X-Api-Key, X-Amz-Security-Token]` | Specifies the allowed headers that can be used in the actual request.                                                                                    |
| `exposeHeaders` | `[]`                                                                         | Any additional header beyond the [safe listed by CORS specification](https://developer.mozilla.org/en-US/docs/Glossary/CORS-safelisted_response_header). |
| `credentials`   | `false`                                                                      | Only necessary when you need to expose cookies, authorization headers or TLS client certificates.                                                        |

#### Per-route overrides

You can override the global CORS settings on a per-route basis by passing options to the `cors` middleware when applying it to a specific route.

```
import { Router } from '@aws-lambda-powertools/event-handler/http';
import { cors } from '@aws-lambda-powertools/event-handler/http/middleware';
import type { Context } from 'aws-lambda';

const app = new Router();

app.use(
  cors({
    origin: 'https://example.com',
    maxAge: 300,
  })
);

app.get('/todos/:todoId', async ({ params: { todoId } }) => {
  const todo = await getTodoById(todoId);
  return { todo };
});

app.get('/health', [cors({ origin: '*' })], async () => {
  return { status: 'ok' };
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

```
{
  "statusCode": 200,
  "headers": {
    "access-control-allow-origin": "*",
    "content-type": "application/json"
  },
  "body": "{\"status\":\"ok\"}",
  "isBase64Encoded": false
}

```

### Compress

You can enable response compression by using the `compress` middleware. This will automatically compress responses using gzip and base64 encode them when the client indicates support via the `Accept-Encoding` header.

```
import { Router } from '@aws-lambda-powertools/event-handler/http';
import { compress } from '@aws-lambda-powertools/event-handler/http/middleware';
import type { Context } from 'aws-lambda';

const app = new Router();

app.use(compress());

app.get('/todos/:todoId', async ({ params: { todoId } }) => {
  const todo = await getTodoById(todoId);
  return { todo };
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

```
{
  "headers": {
    "Accept-Encoding": "gzip"
  },
  "resource": "/todos/1",
  "path": "/todos/1",
  "httpMethod": "GET"
}

```

```
{
  "statusCode": 200,
  "multiValueHeaders": {
    "Content-Type": ["application/json"],
    "Content-Encoding": ["gzip"]
  },
  "body": "H4sIAAAAAAACE42STU4DMQyFrxJl3QXln96AMyAW7sSDLCVxiJ0Kqerd8TCCUOgii1EmP/783pOPXjmw+N3L0TfB+hz8brvxtC5KGtHvfMCIkzZx0HT5MPmNnziViIr2dIYoeNr8Q1x3xHsjcVadIbkZJoq2RXU8zzQROLseQ9505NzeCNQdMJNBE+UmY4zbzjAJhWtlZ57sB84BWtul+rteH2HPlVgWARwjqXkxpklK5gmEHAQqJBMtFsGVygcKmNVRjG0wxvuzGF2L0dpVUOKMC3bfJNjJgWMrCuZk7cUp02AiD72D6WKHHwUDKbiJs6AZ0VZXKOUx4uNvzdxT+E4mLcMA+6G8nzrLQkaxkNEVrFKW2VGbJCoCY7q2V3+tiv5kGThyxfTecDWbgGz/NfYXhL6ePgF9PnFdPgMAAA==",
  "isBase64Encoded": true
}

```

### Binary responses

If you need to return binary data, there are several ways you can do so based on how much control you require.

#### Auto serialization

As described in the [response auto serialization](#response-auto-serialization) section, when you return a JavaScript object from your route handler, we automatically serialize it to JSON and set the `Content-Type` header to `application/json`.

A similar pattern applies to binary data where you can return an `ArrayBuffer`, a [Nodejs stream](https://nodejs.org/api/stream.html), or a [Web stream](https://developer.mozilla.org/en-US/docs/Web/API/Streams_API#browser_compatibility) directly from your handler. We will automatically serialize the response by setting the `isBase64Encoded` flag to `true` and `base64` encoding the binary data.

Content types

The default header will be set to `application/json`. If you wish to change this, e.g., in the case of images, PDFs, videos, etc, then you should use the `reqCtx.res.headers` object to set the appropriate header.

```
import { createReadStream } from 'node:fs';
import { Router } from '@aws-lambda-powertools/event-handler/http';
import type { Context } from 'aws-lambda';

const app = new Router();

app.get('/logo', async (reqCtx) => {
  reqCtx.res.headers.set('Content-Type', 'image/png');
  return createReadStream(`${process.env.LAMBDA_TASK_ROOT}/logo.png`);
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

```
{
  "resource": "/logo",
  "path": "/logo",
  "httpMethod": "GET"
}

```

```
{
  "body": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMjU2cHgiIGhlaWdodD0iMjU2cHgiIHZpZXdCb3g9IjAgMCAyNTYgMjU2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaWRZTWlkIj4KICAgIDx0aXRsZT5BV1MgTGFtYmRhPC90aXRsZT4KICAgIDxkZWZzPgogICAgICAgIDxsaW5lYXJHcmFkaWVudCB4MT0iMCUiIHkxPSIxMDAlIiB4Mj0iMTAwJSIgeTI9IjAlIiBpZD0ibGluZWFyR3JhZGllbnQtMSI+CiAgICAgICAgICAgIDxzdG9wIHN0b3AtY29sb3I9IiNDODUxMUIiIG9mZnNldD0iMCUiPjwvc3RvcD4KICAgICAgICAgICAgPHN0b3Agc3RvcC1jb2xvcj0iI0ZGOTkwMCIgb2Zmc2V0PSIxMDAlIj48L3N0b3A+CiAgICAgICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDwvZGVmcz4KICAgIDxnPgogICAgICAgIDxyZWN0IGZpbGw9InVybCgjbGluZWFyR3JhZGllbnQtMSkiIHg9IjAiIHk9IjAiIHdpZHRoPSIyNTYiIGhlaWdodD0iMjU2Ij48L3JlY3Q+CiAgICAgICAgPHBhdGggZD0iTTg5LjYyNDExMjYsMjExLjIgTDQ5Ljg5MDMyNzcsMjExLjIgTDkzLjgzNTQ4MzIsMTE5LjM0NzIgTDExMy43NDcyOCwxNjAuMzM5MiBMODkuNjI0MTEyNiwyMTEuMiBaIE05Ni43MDI5MzU3LDExMC41Njk2IEM5Ni4xNjQwODU4LDEwOS40NjU2IDk1LjA0MTQ4MTMsMTA4Ljc2NDggOTMuODE2MjM4NCwxMDguNzY0OCBMOTMuODA2NjE2MywxMDguNzY0OCBDOTIuNTcxNzUxNCwxMDguNzY4IDkxLjQ0OTE0NjYsMTA5LjQ3NTIgOTAuOTE5OTE4NywxMTAuNTg1NiBMNDEuOTEzNDIwOCwyMTMuMDIwOCBDNDEuNDM4NzE5NywyMTQuMDEyOCA0MS41MDYwNzU4LDIxNS4xNzc2IDQyLjA5NjI0NTEsMjE2LjEwODggQzQyLjY3OTk5OTQsMjE3LjAzNjggNDMuNzA2MzgwNSwyMTcuNiA0NC44MDY1MzMxLDIxNy42IEw5MS42NTQ0MjMsMjE3LjYgQzkyLjg5NTcwMjcsMjE3LjYgOTQuMDIxNTE0OSwyMTYuODg2NCA5NC41NTM5NTAxLDIxNS43Njk2IEwxMjAuMjAzODU5LDE2MS42ODk2IEMxMjAuNjE3NjE5LDE2MC44MTI4IDEyMC42MTQ0MTIsMTU5Ljc5ODQgMTIwLjE4NzgyMiwxNTguOTI4IEw5Ni43MDI5MzU3LDExMC41Njk2IFogTTIwNy45ODUxMTcsMjExLjIgTDE2OC41MDc5MjgsMjExLjIgTDEwNS4xNzM3ODksNzguNjI0IEMxMDQuNjQ0NTYxLDc3LjUxMDQgMTAzLjUxNTU0MSw3Ni44IDEwMi4yNzc0NjksNzYuOCBMNzYuNDQ3OTQzLDc2LjggTDc2LjQ3NjgwOTksNDQuOCBMMTI3LjEwMzA2Niw0NC44IEwxOTAuMTQ1MzI4LDE3Ny4zNzI4IEMxOTAuNjc0NTU2LDE3OC40ODY0IDE5MS44MDM1NzUsMTc5LjIgMTkzLjA0MTY0NywxNzkuMiBMMjA3Ljk4NTExNywxNzkuMiBMMjA3Ljk4NTExNywyMTEuMiBaIE0yMTEuMTkyNTU4LDE3Mi44IEwxOTUuMDcxOTU4LDE3Mi44IEwxMzIuMDI5Njk2LDQwLjIyNzIgQzEzMS41MDA0NjgsMzkuMTEzNiAxMzAuMzcxNDQ5LDM4LjQgMTI5LjEzMDE2OSwzOC40IEw3My4yNzI1NzYsMzguNCBDNzEuNTA1Mjc1OCwzOC40IDcwLjA2ODM0MjEsMzkuODMwNCA3MC4wNjUxMzQ0LDQxLjU5NjggTDcwLjAyOTg1MjgsNzkuOTk2OCBDNzAuMDI5ODUyOCw4MC44NDggNzAuMzYzNDI2Niw4MS42NjA4IDcwLjk2OTYzMyw4Mi4yNjI0IEM3MS41Njk0MjQ2LDgyLjg2NCA3Mi4zODQxMTQ2LDgzLjIgNzMuMjM3Mjk0MSw4My4yIEwxMDAuMjUzNTczLDgzLjIgTDE2My41OTA5MiwyMTUuNzc2IEMxNjQuMTIzMzU1LDIxNi44ODk2IDE2NS4yNDU5NiwyMTcuNiAxNjYuNDg0MDMyLDIxNy42IEwyMTEuMTkyNTU4LDIxNy42IEMyMTIuOTY2Mjc0LDIxNy42IDIxNC40LDIxNi4xNjY0IDIxNC40LDIxNC40IEwyMTQuNCwxNzYgQzIxNC40LDE3NC4yMzM2IDIxMi45NjYyNzQsMTcyLjggMjExLjE5MjU1OCwxNzIuOCBMMjExLjE5MjU1OCwxNzIuOCBaIiBmaWxsPSIjRkZGRkZGIj48L3BhdGg+CiAgICA8L2c+Cjwvc3ZnPg==",
  "headers": {
    "Content-Type": "image/png"
  },
  "isBase64Encoded": true,
  "statusCode": 200
}

```

#### Set `isBase64Encoded` parameter

You can indicate that you wish to `base64` encode any response, regardless of type, by setting the `isBase64Encoded` field in `reqCtx` to `true`.

```
import { Router } from '@aws-lambda-powertools/event-handler/http';
import type { Context } from 'aws-lambda';

const app = new Router();

app.get('/json64', async (reqCtx) => {
  reqCtx.isBase64Encoded = true;
  return { message: 'Hello World!' };
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

```
{
  "resource": "/json64",
  "path": "/json64",
  "httpMethod": "GET"
}

```

```
{
  "body": "eyJtZXNzYWdlIjoiSGVsbG8gV29ybGQifQ==",
  "headers": {
    "Content-Type": "application/json"
  },
  "isBase64Encoded": true,
  "statusCode": 200
}

```

#### Manual serialization

For complete control you can return an `APIGatewayProxyEvent` (`v1` or `v2`) and this will be handled transparently by the resolver.

```
import { readFile } from 'node:fs/promises';
import { Router } from '@aws-lambda-powertools/event-handler/http';
import type { Context } from 'aws-lambda';

const app = new Router();

app.get('/logo', async () => {
  const logoFile = await readFile(`${process.env.LAMBDA_TASK_ROOT}/logo.png`);
  return {
    body: logoFile.toString('base64'),
    isBase64Encoded: true,
    headers: {
      'Content-Type': 'image/png',
    },
    statusCode: 200,
  };
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

```
{
  "resource": "/logo",
  "path": "/logo",
  "httpMethod": "GET"
}

```

```
{
  "body": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMjU2cHgiIGhlaWdodD0iMjU2cHgiIHZpZXdCb3g9IjAgMCAyNTYgMjU2IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaWRZTWlkIj4KICAgIDx0aXRsZT5BV1MgTGFtYmRhPC90aXRsZT4KICAgIDxkZWZzPgogICAgICAgIDxsaW5lYXJHcmFkaWVudCB4MT0iMCUiIHkxPSIxMDAlIiB4Mj0iMTAwJSIgeTI9IjAlIiBpZD0ibGluZWFyR3JhZGllbnQtMSI+CiAgICAgICAgICAgIDxzdG9wIHN0b3AtY29sb3I9IiNDODUxMUIiIG9mZnNldD0iMCUiPjwvc3RvcD4KICAgICAgICAgICAgPHN0b3Agc3RvcC1jb2xvcj0iI0ZGOTkwMCIgb2Zmc2V0PSIxMDAlIj48L3N0b3A+CiAgICAgICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDwvZGVmcz4KICAgIDxnPgogICAgICAgIDxyZWN0IGZpbGw9InVybCgjbGluZWFyR3JhZGllbnQtMSkiIHg9IjAiIHk9IjAiIHdpZHRoPSIyNTYiIGhlaWdodD0iMjU2Ij48L3JlY3Q+CiAgICAgICAgPHBhdGggZD0iTTg5LjYyNDExMjYsMjExLjIgTDQ5Ljg5MDMyNzcsMjExLjIgTDkzLjgzNTQ4MzIsMTE5LjM0NzIgTDExMy43NDcyOCwxNjAuMzM5MiBMODkuNjI0MTEyNiwyMTEuMiBaIE05Ni43MDI5MzU3LDExMC41Njk2IEM5Ni4xNjQwODU4LDEwOS40NjU2IDk1LjA0MTQ4MTMsMTA4Ljc2NDggOTMuODE2MjM4NCwxMDguNzY0OCBMOTMuODA2NjE2MywxMDguNzY0OCBDOTIuNTcxNzUxNCwxMDguNzY4IDkxLjQ0OTE0NjYsMTA5LjQ3NTIgOTAuOTE5OTE4NywxMTAuNTg1NiBMNDEuOTEzNDIwOCwyMTMuMDIwOCBDNDEuNDM4NzE5NywyMTQuMDEyOCA0MS41MDYwNzU4LDIxNS4xNzc2IDQyLjA5NjI0NTEsMjE2LjEwODggQzQyLjY3OTk5OTQsMjE3LjAzNjggNDMuNzA2MzgwNSwyMTcuNiA0NC44MDY1MzMxLDIxNy42IEw5MS42NTQ0MjMsMjE3LjYgQzkyLjg5NTcwMjcsMjE3LjYgOTQuMDIxNTE0OSwyMTYuODg2NCA5NC41NTM5NTAxLDIxNS43Njk2IEwxMjAuMjAzODU5LDE2MS42ODk2IEMxMjAuNjE3NjE5LDE2MC44MTI4IDEyMC42MTQ0MTIsMTU5Ljc5ODQgMTIwLjE4NzgyMiwxNTguOTI4IEw5Ni43MDI5MzU3LDExMC41Njk2IFogTTIwNy45ODUxMTcsMjExLjIgTDE2OC41MDc5MjgsMjExLjIgTDEwNS4xNzM3ODksNzguNjI0IEMxMDQuNjQ0NTYxLDc3LjUxMDQgMTAzLjUxNTU0MSw3Ni44IDEwMi4yNzc0NjksNzYuOCBMNzYuNDQ3OTQzLDc2LjggTDc2LjQ3NjgwOTksNDQuOCBMMTI3LjEwMzA2Niw0NC44IEwxOTAuMTQ1MzI4LDE3Ny4zNzI4IEMxOTAuNjc0NTU2LDE3OC40ODY0IDE5MS44MDM1NzUsMTc5LjIgMTkzLjA0MTY0NywxNzkuMiBMMjA3Ljk4NTExNywxNzkuMiBMMjA3Ljk4NTExNywyMTEuMiBaIE0yMTEuMTkyNTU4LDE3Mi44IEwxOTUuMDcxOTU4LDE3Mi44IEwxMzIuMDI5Njk2LDQwLjIyNzIgQzEzMS41MDA0NjgsMzkuMTEzNiAxMzAuMzcxNDQ5LDM4LjQgMTI5LjEzMDE2OSwzOC40IEw3My4yNzI1NzYsMzguNCBDNzEuNTA1Mjc1OCwzOC40IDcwLjA2ODM0MjEsMzkuODMwNCA3MC4wNjUxMzQ0LDQxLjU5NjggTDcwLjAyOTg1MjgsNzkuOTk2OCBDNzAuMDI5ODUyOCw4MC44NDggNzAuMzYzNDI2Niw4MS42NjA4IDcwLjk2OTYzMyw4Mi4yNjI0IEM3MS41Njk0MjQ2LDgyLjg2NCA3Mi4zODQxMTQ2LDgzLjIgNzMuMjM3Mjk0MSw4My4yIEwxMDAuMjUzNTczLDgzLjIgTDE2My41OTA5MiwyMTUuNzc2IEMxNjQuMTIzMzU1LDIxNi44ODk2IDE2NS4yNDU5NiwyMTcuNiAxNjYuNDg0MDMyLDIxNy42IEwyMTEuMTkyNTU4LDIxNy42IEMyMTIuOTY2Mjc0LDIxNy42IDIxNC40LDIxNi4xNjY0IDIxNC40LDIxNC40IEwyMTQuNCwxNzYgQzIxNC40LDE3NC4yMzM2IDIxMi45NjYyNzQsMTcyLjggMjExLjE5MjU1OCwxNzIuOCBMMjExLjE5MjU1OCwxNzIuOCBaIiBmaWxsPSIjRkZGRkZGIj48L3BhdGg+CiAgICA8L2c+Cjwvc3ZnPg==",
  "headers": {
    "Content-Type": "image/png"
  },
  "isBase64Encoded": true,
  "statusCode": 200
}

```

Compression

If you wish to use binary responses together with the [`compress`](#compress) feature, the client must send the `Accept` header with the correct media type.

### Response streaming

Compatibility

Response streaming is only available for [API Gateway REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode.html) and [Lambda function URLs](https://docs.aws.amazon.com/lambda/latest/dg/configuration-response-streaming.html).

You can send responses to the client using HTTP streaming by wrapping your router with the `streamify` function to turn all the associated route handlers into stream compatible handlers. This is useful when you need to send large payloads or want to start sending data before the entire response is ready.

In order to gain the most benefit, you should return either a readable [Nodejs stream](https://nodejs.org/api/stream.html#readable-streams), a duplex [Nodejs stream](https://nodejs.org/api/stream.html#class-streamduplex), or a [Web stream](https://developer.mozilla.org/en-US/docs/Web/API/Streams_API) from your handlers. However, you can also return other types and these will also be delivered via HTTP streaming.

```
import { Router, streamify } from '@aws-lambda-powertools/event-handler/http';

const app = new Router();

app.get('/video-stream', async (reqCtx) => {
  reqCtx.res.headers.set('content-type', 'video/mp4');
  return createVideoStream();
});

app.get('/hello', () => {
  return { message: 'Hello World' };
});

export const handler = streamify(app);

```

When to use streaming

Consider response streaming when:

- Returning large payloads (> 6MB)
- Processing data that can be sent incrementally
- Reducing time-to-first-byte for long-running operations is a requirement

For most use cases, the standard `resolve` method is sufficient.

### Debug mode

You can enable debug mode via the `POWERTOOLS_DEV` environment variable.

When set to `true`, debug mode enhances error responses with detailed information to aid in debugging and testing.

Security consideration

Never enable debug mode in production environments as it exposes sensitive error details that could be exploited by attackers.

Only use it during development and testing.

#### Enhanced error responses

When an unhandled error occurs in your route handler or middleware, Event Handler will return a HTTP 500 response by default.

```
{
  "statusCode": 500,
  "error": "Internal Server Error",
  "message": "Internal Server Error"
}

```

```
{
  "statusCode": 500,
  "error": "Internal Server Error",
  "message": "Actual error message from the exception",
  "stack": "Full stack trace of the error",
  "details": {
    "errorName": "Name of the error class"
  }
}

```

#### Logging requests and responses

Coming soon

Please [check this issue](https://github.com/aws-powertools/powertools-lambda-typescript/issues/4482) and add ð if you would like us to prioritize this feature.

### OpenAPI

Coming soon

Currently, Event Handler does not support automatic generation of OpenAPI documentation from your route definitions.

We plan to add this feature in a future release with an experience similar to what described in the [utility's RFC](https://github.com/aws-powertools/powertools-lambda-typescript/discussions/3500) and to what available in [Powertools for AWS Lambda (Python)](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway/#openapi).

Please [check this issue](https://github.com/aws-powertools/powertools-lambda-typescript/issues/4515) for more details, and add ð if you would like us to prioritize it.

### Split routers

As applications grow and the number of routes a Lambda function handles increases, it becomes natural to either break it into smaller Lambda functions or split routes into separate files to ease maintenance.

The `Router` class provide an `includeRouter` method to compose multiple router instances allowing developers to define routes in multiple files and merge route definitions. You will be able to define routes in separate files and import them into a main router file, improving code organization and maintainability.

Merging with Global Middleware

When merging two `Router` instances together, if you have a global middleware defined in one of your instances, the global middleware gets applied to the all the merged routes.

Let's assume you have `index.ts` as your Lambda function entrypoint and routes in `split_route.ts`. This is how you'd use the `includeRouter` feature.

```
import { Router } from '@aws-lambda-powertools/event-handler/http';

const router = new Router();
router.get('/todos', () => 'Get all todos');
router.get('/todos/:id', () => 'Get a single todo item');

export { router };

```

```
import { Router } from '@aws-lambda-powertools/event-handler/http';
import type { APIGatewayProxyEvent, Context } from 'aws-lambda';
import { router } from './split_route';

const app = new Router();

// Split Routers
app.includeRouter(router);

export const handler = async (event: APIGatewayProxyEvent, context: Context) =>
  app.resolve(event, context);

```

#### Route Prefix

In the previous example, `split_route.ts` routes had a `/todos` prefix. This might grow over time and become repetitive.

When necessary, you can set a prefix when including a `Router` instance. This means you can remove `/todos` prefix altogether.

```
import { Router } from '@aws-lambda-powertools/event-handler/http';

const router = new Router();
router.get('/', () => 'Get all todos');
router.get('/:id', () => 'Get a single todo item');

export { router };

```

```
import { Router } from '@aws-lambda-powertools/event-handler/http';
import type { APIGatewayProxyEvent, Context } from 'aws-lambda';
import { router } from './split_route';

const app = new Router();

// Split Routers
app.includeRouter(router, { prefix: '/todos' });

export const handler = async (event: APIGatewayProxyEvent, context: Context) =>
  app.resolve(event, context);

```

### Considerations

This utility is optimized for AWS Lambda computing model and prioritizes fast startup, minimal feature set, and quick onboarding for triggers supported by Lambda.

Event Handler naturally leads to a single Lambda function handling multiple routes for a given service, which can be eventually broken into multiple functions.

Both single (monolithic) and multiple functions (micro) offer different set of trade-offs worth knowing.

TL;DR;

Start with a monolithic function, add additional functions with new handlers, and possibly break into micro functions if necessary.

#### Monolithic function

A monolithic function means that your final code artifact will be deployed to a single function. This is generally the best approach to start.

***Benefits***

- **Code reuse.** It's easier to reason about your service, modularize it and reuse code as it grows. Eventually, it can be turned into a standalone library.
- **No custom tooling.** Monolithic functions are treated just like normal Typescript packages; no upfront investment in tooling.
- **Faster deployment and debugging.** Whether you use all-at-once, linear, or canary deployments, a monolithic function is a single deployable unit. IDEs like WebStorm and VSCode have tooling to quickly profile, visualize, and step through debug any Typescript package.

***Downsides***

- **Cold starts.** Frequent deployments and/or high load can diminish the benefit of monolithic functions depending on your latency requirements, due to the [Lambda scaling model](https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html). Always load test to find a pragmatic balance between customer experience and developer cognitive load.
- **Granular security permissions.** The micro function approach enables you to use fine-grained permissions and access controls, separate external dependencies and code signing at the function level. Conversely, you could have multiple functions while duplicating the final code artifact in a monolithic approach. Regardless, least privilege can be applied to either approaches.
- **Higher risk per deployment.** A misconfiguration or invalid import can cause disruption if not caught early in automated testing. Multiple functions can mitigate misconfigurations but they will still share the same code artifact. You can further minimize risks with multiple environments in your CI/CD pipeline.

#### Micro function

A micro function means that your final code artifact will be different to each function deployed. This is generally the approach to start if you're looking for fine-grain control and/or high load on certain parts of your service.

***Benefits***

- **Granular scaling.** A micro function can benefit from the [Lambda scaling model](https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html) to scale differently depending on each part of your application. Concurrency controls and provisioned concurrency can also be used at a granular level for capacity management.
- **Discoverability.** Micro functions are easier to visualize when using distributed tracing. Their high-level architectures can be self-explanatory, and complexity is highly visible â assuming each function is named after the business purpose it serves.
- **Package size.** An independent function can be significantly smaller (KB vs MB) depending on the external dependencies it requires to perform its purpose. Conversely, a monolithic approach can benefit from [Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/invocation-layers.html) to optimize builds for external dependencies.

***Downsides***

- **Upfront investment.** You need custom build tooling to bundle assets, including [native bindings for runtime compatibility](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html). Operations become more elaborate â you need to standardize tracing labels/annotations, structured logging, and metrics to pinpoint root causes.
- **Engineering discipline** is necessary for both approaches. However, the micro-function approach requires further attention to consistency as the number of functions grow, just like any distributed system.
- **Harder to share code.** Shared code must be carefully evaluated to avoid unnecessary deployments when this code changes. Equally, if shared code isn't a library, your development, building, deployment tooling need to accommodate the distinct layout.
- **Slower safe deployments.** Safely deploying multiple functions require coordination â AWS CodeDeploy deploys and verifies each function sequentially. This increases lead time substantially (minutes to hours) depending on the deployment strategy you choose. You can mitigate it by selectively enabling it in prod-like environments only, and where the risk profile is applicable. Automated testing, operational and security reviews are essential to stability in either approaches.

## Testing your code

You can use any testing framework of your choice to test Lambda functions using Event Handler.

Since Event Handler doesn't require any server or socket to run, you can test your code as you would any other JavaScript/TypeScript function.

Below is an example using [Vitest](https://vitest.dev), including a helper function to create mock API Gateway events that you can copy and adapt to your needs.

```
import type { Context } from 'aws-lambda';
import { expect, test } from 'vitest';
import { handler } from './advanced_cors_simple.js';
import { createTestEvent } from './advanced_testing_helper.js';

test('returns CORS headers', async () => {
  // Preapare
  const event = createTestEvent({
    httpMethod: 'GET',
    headers: {
      Origin: 'https://example.com',
    },
    path: '/todos/123',
  });

  // Act
  const result = await handler(event, {} as Context);

  // Assess
  expect(result.statusCode).toEqual(200);
  expect(result.body).toEqual(JSON.stringify({ todo: { id: '123' } }));
  expect(result.headers?.['access-control-allow-origin']).toEqual(
    'https://example.com'
  );
  expect(
    result.multiValueHeaders?.['access-control-allow-methods'].sort()
  ).toEqual(['DELETE', 'GET', 'HEAD', 'PATCH', 'POST', 'PUT'].sort());
  expect(
    result.multiValueHeaders?.['access-control-allow-headers'].sort()
  ).toEqual(
    [
      'Authorization',
      'Content-Type',
      'X-Amz-Date',
      'X-Amz-Security-Token',
      'X-Api-Key',
    ].sort()
  );
});

```

```
import type { APIGatewayProxyEvent } from 'aws-lambda';

const createTestEvent = (options: {
  path: string;
  httpMethod: string;
  headers?: Record<string, string>;
}): APIGatewayProxyEvent => ({
  path: options.path,
  httpMethod: options.httpMethod,
  headers: options.headers ?? {},
  body: null,
  multiValueHeaders: {},
  isBase64Encoded: false,
  pathParameters: null,
  queryStringParameters: null,
  multiValueQueryStringParameters: null,
  stageVariables: null,
  requestContext: {
    httpMethod: options.httpMethod,
    path: options.path,
    domainName: 'localhost',
  } as APIGatewayProxyEvent['requestContext'],
  resource: '',
});

export { createTestEvent };

```

```
import { Router } from '@aws-lambda-powertools/event-handler/http';
import { cors } from '@aws-lambda-powertools/event-handler/http/middleware';
import type { Context } from 'aws-lambda';

const app = new Router();

app.use(
  cors({
    origin: 'https://example.com',
    maxAge: 300,
  })
);

app.get('/todos/:todoId', async ({ params: { todoId } }) => {
  const todo = await getTodoById(todoId);
  return { todo };
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

Event Handler for AWS AppSync real-time events.

```
stateDiagram-v2
    direction LR
    EventSource: AppSync Events
    EventHandlerResolvers: Publish & Subscribe events
    LambdaInit: Lambda invocation
    EventHandler: Event Handler
    EventHandlerResolver: Route event based on namespace/channel
    YourLogic: Run your registered handler function
    EventHandlerResolverBuilder: Adapts response to AppSync contract
    LambdaResponse: Lambda response

    state EventSource {
        EventHandlerResolvers
    }

    EventHandlerResolvers --> LambdaInit

    LambdaInit --> EventHandler
    EventHandler --> EventHandlerResolver

    state EventHandler {
        [*] --> EventHandlerResolver: app.resolve(event, context)
        EventHandlerResolver --> YourLogic
        YourLogic --> EventHandlerResolverBuilder
    }

    EventHandler --> LambdaResponse
```

## Key Features

- Easily handle publish and subscribe events with dedicated handler methods
- Automatic routing based on namespace and channel patterns
- Support for wildcard patterns to create catch-all handlers
- Process events in parallel and control aggregation for batch processing
- Graceful error handling for individual events

## Terminology

**[AWS AppSync Events](https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-welcome.html)**. A service that enables you to quickly build secure, scalable real-time WebSocket APIs without managing infrastructure or writing API code.

It handles connection management, message broadcasting, authentication, and monitoring, reducing time to market and operational costs.

## Getting started

Tip: New to AppSync Real-time API?

Visit [AWS AppSync Real-time documentation](https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-getting-started.html) to understand how to set up subscriptions and pub/sub messaging.

### Required resources

You must have an existing AppSync Events API with real-time capabilities enabled and IAM permissions to invoke your AWS Lambda function. That said, there are no additional permissions required to use Event Handler as routing requires no dependency.

Additionally, if you want the result of your handler to be used by AppSync you must set the integration type to `REQUEST_RESPONSE`.

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Globals:
  Function:
    Timeout: 5
    MemorySize: 256
    Runtime: nodejs24.x
    Tracing: Active
    Environment:
      Variables:
        POWERTOOLS_LOG_LEVEL: INFO
        POWERTOOLS_SERVICE_NAME: hello

Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.handler
      CodeUri: hello_world

  WebsocketAPI:
    Type: AWS::AppSync::Api
    Properties:
      EventConfig:
        AuthProviders:
          - AuthType: API_KEY
        ConnectionAuthModes:
          - AuthType: API_KEY
        DefaultPublishAuthModes:
          - AuthType: API_KEY
        DefaultSubscribeAuthModes:
          - AuthType: API_KEY
      Name: RealTimeEventAPI

  WebsocketApiKey:
    Type: AWS::AppSync::ApiKey
    Properties:
      ApiId: !GetAtt WebsocketAPI.ApiId

  WebsocketAPINamespace:
    Type: AWS::AppSync::ChannelNamespace
    Properties:
      ApiId: !GetAtt WebsocketAPI.ApiId
      Name: powertools
      HandlerConfigs:
        OnPublish:
          Behavior: DIRECT
          Integration:
            DataSourceName: powertools_lambda
            LambdaConfig:
              InvokeType: REQUEST_RESPONSE
        OnSubscribe:
          Behavior: DIRECT
          Integration:
            DataSourceName: powertools_lambda
            LambdaConfig:
              InvokeType: REQUEST_RESPONSE

  DataSourceIAMRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: appsync.amazonaws.com
            Action: sts:AssumeRole
      Policies:
        - PolicyName: LambdaInvokePolicy
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - lambda:InvokeFunction
                Resource: !GetAtt HelloWorldFunction.Arn

  NameSpaceDataSource:
    Type: AWS::AppSync::DataSource
    Properties:
      ApiId: !GetAtt WebsocketAPI.ApiId
      LambdaConfig: 
        LambdaFunctionArn: !GetAtt HelloWorldFunction.Arn
      Name: powertools_lambda
      ServiceRoleArn: !GetAtt DataSourceIAMRole.Arn
      Type: AWS_LAMBDA

```

### AppSync request and response format

AppSync Events uses a specific event format for Lambda requests and responses. In most scenarios, Powertools for AWS simplifies this interaction by automatically formatting resolver returns to match the expected AppSync response structure.

```
{
  "identity": "None",
  "result": "None",
  "request": {
    "headers": {
      "x-forwarded-for": "1.1.1.1, 2.2.2.2",
      "cloudfront-viewer-country": "US"
    },
    "domainName": "None"
  },
  "info": {
    "channel": {
      "path": "/default/channel",
      "segments": ["default", "channel"]
    },
    "channelNamespace": {
      "name": "default"
    },
    "operation": "PUBLISH"
  },
  "error": "None",
  "prev": "None",
  "stash": {},
  "outErrors": [],
  "events": [
    {
      "payload": {
        "data": "data_1"
      },
      "id": "1"
    },
    {
      "payload": {
        "data": "data_2"
      },
      "id": "2"
    }
  ]
}

```

```
{
  "events": [
    {
      "payload": {
        "data": "data_1"
      },
      "id": "1"
    },
    {
      "payload": {
        "data": "data_2"
      },
      "id": "2"
    }
  ]
}

```

```
{
  "events": [
    {
      "error": "Error message",
      "id": "1"
    },
    {
      "payload": {
        "data": "data_2"
      },
      "id": "2"
    }
  ]
}

```

#### Events response with error

When processing events with Lambda, you can return errors to AppSync in three ways:

- **Item specific error:** Return an `error` key within each individual item's response. AppSync Events expects this format for item-specific errors.
- **Fail entire request:** Return a JSON object with a top-level `error` key. This signals a general failure, and AppSync treats the entire request as unsuccessful.
- **Unauthorized exception**: Throw an **UnauthorizedException** exception to reject a subscribe or publish request with HTTP 403.

### Route handlers

The event handler automatically parses the incoming event data and invokes the appropriate handler based on the namespace/channel pattern you register.

You can define your handlers for different event types using the `onPublish()` and `onSubscribe()` methods and pass a function to handle the event.

```
import { AppSyncEventsResolver } from '@aws-lambda-powertools/event-handler/appsync-events';
import type { Context } from 'aws-lambda';

const app = new AppSyncEventsResolver();

app.onPublish('/default/foo', (payload) => {
  return {
    processed: true,
    original_payload: payload,
  };
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

```
import { AppSyncEventsResolver } from '@aws-lambda-powertools/event-handler/appsync-events';
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';
import type { Context } from 'aws-lambda';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'chat',
  singleMetric: true,
});
const app = new AppSyncEventsResolver();

app.onSubscribe('/default/foo', (event) => {
  metrics.addDimension('channel', event.info.channel.path);
  metrics.addMetric('connections', MetricUnit.Count, 1);
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

If you prefer to use the decorator syntax, you can instead use the same methods on a class method to register your handlers.

```
import { AppSyncEventsResolver } from '@aws-lambda-powertools/event-handler/appsync-events';
import type { AppSyncEventsPublishEvent } from '@aws-lambda-powertools/event-handler/types';
import type { Context } from 'aws-lambda';

const app = new AppSyncEventsResolver();

class Lambda {
  @app.onPublish('/default/foo')
  async fooHandler(payload: AppSyncEventsPublishEvent) {
    return {
      processed: true,
      original_payload: payload,
    };
  }

  async handler(event: unknown, context: Context) {
    return app.resolve(event, context, { scope: this });
  }
}

const lambda = new Lambda();
export const handler = lambda.handler.bind(lambda);

```

```
import { AppSyncEventsResolver } from '@aws-lambda-powertools/event-handler/appsync-events';
import type { AppSyncEventsSubscribeEvent } from '@aws-lambda-powertools/event-handler/types';
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';
import type { Context } from 'aws-lambda';

const metrics = new Metrics({
  namespace: 'serverlessAirline',
  serviceName: 'chat',
  singleMetric: true,
});
const app = new AppSyncEventsResolver();

class Lambda {
  @app.onSubscribe('/default/foo')
  async fooHandler(event: AppSyncEventsSubscribeEvent) {
    metrics.addDimension('channel', event.info.channel.path);
    metrics.addMetric('connections', MetricUnit.Count, 1);
  }

  async handler(event: unknown, context: Context) {
    return app.resolve(event, context, { scope: this });
  }
}

const lambda = new Lambda();
export const handler = lambda.handler.bind(lambda);

```

## Advanced

### Wildcard patterns and handler precedence

You can use wildcard patterns to create catch-all handlers for multiple channels or namespaces. This is particularly useful for centralizing logic that applies to multiple channels.

When an event matches with multiple handler, the most specific pattern takes precedence.

Supported wildcard patterns

Only the following patterns are supported:

- `/namespace/*` - Matches all channels in the specified namespace
- `/*` - Matches all channels in all namespaces

Patterns like `/namespace/channel*` or `/namespace/*/subpath` are not supported.

More specific handlers will always take precedence over less specific ones. For example, `/default/channel1` will take precedence over `/default/*`, which will take precedence over `/*`.

```
import { AppSyncEventsResolver } from '@aws-lambda-powertools/event-handler/appsync-events';
import type { Context } from 'aws-lambda';

const app = new AppSyncEventsResolver();

app.onPublish('/default/*', (_payload) => {
  // your logic here
});

app.onSubscribe('/*', (_payload) => {
  // your logic here
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

If the event doesn't match any registered handler, the Event Handler will log a warning and skip processing the event.

### Aggregated processing

In some scenarios, you might want to process all messages published to a channel as a batch rather than individually.

This is useful when you want to for example:

- Optimize database operations by making a single batch query
- Ensure all events are processed together or not at all
- Apply custom error handling logic for the entire batch

You can enable this with the `aggregate` parameter:

```
import { AppSyncEventsResolver } from '@aws-lambda-powertools/event-handler/appsync-events';
import {
  BatchWriteItemCommand,
  DynamoDBClient,
  type WriteRequest,
} from '@aws-sdk/client-dynamodb';
import { marshall } from '@aws-sdk/util-dynamodb';
import type { Context } from 'aws-lambda';

const ddbClient = new DynamoDBClient();
const app = new AppSyncEventsResolver();

app.onPublish(
  '/default/foo/*',
  async (payloads) => {
    const writeOperations: WriteRequest[] = [];
    for (const payload of payloads) {
      writeOperations.push({
        PutRequest: {
          Item: marshall(payload),
        },
      });
    }
    await ddbClient.send(
      new BatchWriteItemCommand({
        RequestItems: {
          'your-table-name': writeOperations,
        },
      })
    );

    return payloads;
  },
  { aggregate: true }
);

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

When enabling `aggregate`, your handler receives a list of all the events, requiring you to manage the response format. Ensure your response includes results for each event in the expected [AppSync Request and Response Format](#appsync-request-and-response-format).

If you want to omit one or more events from the response, you can do so by excluding them from the returned array. Likewise, if you want to discard the entire batch and prevent subscribers from receiving it, you can return an empty array.

```
import { AppSyncEventsResolver } from '@aws-lambda-powertools/event-handler/appsync-events';
import type { AppSyncEventsPublishEvent } from '@aws-lambda-powertools/event-handler/types';
import type { Context } from 'aws-lambda';

const app = new AppSyncEventsResolver();

app.onPublish(
  '/default/foo/*',
  async (events) => {
    const payloadsToReturn: AppSyncEventsPublishEvent['events'] = [];

    for (const event of events) {
      if (event.payload.includes('foo')) continue;
      payloadsToReturn.push(event);
    }

    return payloadsToReturn; // (1)!
  },
  { aggregate: true }
);

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

1. You can also return an empty array `[]` to discard the entire batch and prevent subscribers from receiving it.

### Handling errors

You can filter or reject events by throwing exceptions in your resolvers or by formatting the payload according to the expected response structure. This instructs AppSync not to propagate that specific message, so subscribers will not receive it.

#### Handling errors with individual items

When processing items individually, you can throw an exception to fail a specific message. When this happens, the Event Handler will catch it and include the exception name and message in the response.

```
import { AppSyncEventsResolver } from '@aws-lambda-powertools/event-handler/appsync-events';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';

const logger = new Logger({
  serviceName: 'appsync-events',
  logLevel: 'DEBUG',
});
const app = new AppSyncEventsResolver();

app.onPublish('/default/foo', (payload) => {
  try {
    return payload;
  } catch (error) {
    logger.error('Error processing event', { error });
    throw error;
  }
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

```
{
  "events": [
    {
      "error": "Error message",
      "id": "1"
    },
    {
      "payload": {
        "data": "data_2"
      },
      "id": "2"
    }
  ]
}

```

#### Handling errors with aggregate

When processing batch of items with `aggregate` enabled, you must format the payload according the expected response.

```
import { AppSyncEventsResolver } from '@aws-lambda-powertools/event-handler/appsync-events';
import type { OnPublishAggregateOutput } from '@aws-lambda-powertools/event-handler/types';
import type { Context } from 'aws-lambda';

const app = new AppSyncEventsResolver();

app.onPublish(
  '/default/foo/*',
  async (payloads) => {
    const returnValues: OnPublishAggregateOutput<{
      processed: boolean;
      original_payload: unknown;
    }> = [];
    for (const payload of payloads) {
      try {
        returnValues.push({
          id: payload.id,
          payload: { processed: true, original_payload: payload },
        });
      } catch (error) {
        const errorString =
          error instanceof Error
            ? `${error.name} - ${error.message}`
            : 'Unknown error';
        returnValues.push({
          id: payload.id,
          error: errorString,
        });
      }
    }

    return returnValues;
  },
  { aggregate: true }
);

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

```
{
  "events": [
    {
      "error": "SyntaxError - Invalid item",
      "id": "1"
    },
    {
      "payload": {
        "processed": true,
        "original_payload": {
          "event_2": "data_2"
        }
      },
      "id": "2"
    }
  ]
}

```

If instead you want to fail the entire batch, you can throw an exception. This will cause the Event Handler to return an error response to AppSync and fail the entire batch.

```
import { AppSyncEventsResolver } from '@aws-lambda-powertools/event-handler/appsync-events';
import type { OnPublishAggregateOutput } from '@aws-lambda-powertools/event-handler/types';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';

const logger = new Logger({
  serviceName: 'serverlessAirline',
  logLevel: 'INFO',
});
const app = new AppSyncEventsResolver();

app.onPublish(
  '/default/foo/*',
  async (payloads) => {
    const returnValues: OnPublishAggregateOutput<{
      processed: boolean;
      original_payload: unknown;
    }> = [];
    try {
      for (const payload of payloads) {
        returnValues.push({
          id: payload.id,
          payload: { processed: true, original_payload: payload },
        });
      }
    } catch (error) {
      logger.error('Error processing payloads', { error });
      throw error;
    }

    return returnValues;
  },
  { aggregate: true }
);

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

```
{
  "error": "Error - An unexpected error occurred"
}

```

#### Authorization control

Throwing `UnauthorizedException` will cause the Lambda invocation to fail.

You can also do content-based authorization for channel by throwing an `UnauthorizedException` error. This can cause two situations:

- **When working with publish events**, Powertools for AWS stops processing messages and prevents subscribers from receiving messages.
- **When working with subscribe events** it'll prevent the subscription from being created.

```
import {
  AppSyncEventsResolver,
  UnauthorizedException,
} from '@aws-lambda-powertools/event-handler/appsync-events';
import type { Context } from 'aws-lambda';

const app = new AppSyncEventsResolver();

app.onPublish('/default/foo', (payload) => {
  return payload;
});

app.onPublish('/*', () => {
  throw new UnauthorizedException('You can only publish to /default/foo');
});

app.onSubscribe('/private/*', async (info) => {
  const userGroups =
    info.identity?.groups && Array.isArray(info.identity?.groups)
      ? info.identity?.groups
      : [];
  const channelGroup = 'premium-users';

  if (!userGroups.includes(channelGroup)) {
    throw new UnauthorizedException(
      `Subscription requires ${channelGroup} group membership`
    );
  }
});

export const handler = async (event: unknown, context: Context) =>
  await app.resolve(event, context);

```

### Accessing Lambda context and event

You can access to the original Lambda event or context for additional information. These are passed to the handler function as optional arguments.

```
import { AppSyncEventsResolver } from '@aws-lambda-powertools/event-handler/appsync-events';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';

const logger = new Logger({
  serviceName: 'serverlessAirline',
});
const app = new AppSyncEventsResolver();

app.onPublish('/*', (payload, event, context) => {
  const { headers } = event.request; // (1)!
  const { awsRequestId } = context;
  logger.info('headers', { headers, awsRequestId });

  // your business logic here

  return payload;
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

1. The `event` parameter contains the original AppSync event and has type `AppSyncEventsPublishEvent` or `AppSyncEventsSubscribeEvent` from the `@aws-lambda-powertools/event-handler/types`.

### Logging

By default, the `AppSyncEventsResolver` uses the global `console` logger and emits only warnings and errors.

You can change this behavior by passing a custom logger instance to the `AppSyncEventsResolver` and setting the log level for it, or by enabling [Lambda Advanced Logging Controls](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs-advanced.html) and setting the log level to `DEBUG`.

When debug logging is enabled, the resolver will emit logs that show the underlying handler resolution process. This is useful for understanding how your handlers are being resolved and invoked and can help you troubleshoot issues with your event processing.

For example, when using the [Powertools for AWS Lambda logger](https://docs.aws.amazon.com/powertools/typescript/latest/features/logger/index.md), you can set the `LOG_LEVEL` to `DEBUG` in your environment variables or at the logger level and pass the logger instance to the `AppSyncEventsResolver` constructor to enable debug logging.

```
import { AppSyncEventsResolver } from '@aws-lambda-powertools/event-handler/appsync-events';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';

const logger = new Logger({
  serviceName: 'serverlessAirline',
  logLevel: 'DEBUG',
});
const app = new AppSyncEventsResolver({ logger });

app.onPublish('/default/foo', (payload) => {
  return payload;
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

```
[
  {
    "level": "DEBUG",
    "message": "Registering onPublish route handler for path '/default/foo' with aggregate 'false'",
    "timestamp": "2025-04-22T13:24:34.762Z",
    "service": "serverlessAirline",
    "sampling_rate": 0
  },
  {
    "level": "DEBUG",
    "message": "Resolving handler for path '/default/foo'",
    "timestamp": "2025-04-22T13:24:34.775Z",
    "service": "serverlessAirline",
    "sampling_rate": 0,
    "xray_trace_id": "1-68079892-6a1723770bc0b1f348d9a7ad"
  }
]

```

## Flow diagrams

### Working with single items

```
sequenceDiagram
    participant Client
    participant AppSync
    participant Lambda
    participant EventHandler
    note over Client,EventHandler: Individual Event Processing (aggregate=False)
    Client->>+AppSync: Send multiple events to channel
    AppSync->>+Lambda: Invoke Lambda with batch of events
    Lambda->>+EventHandler: Process events with aggregate=False
    loop For each event in batch
        EventHandler->>EventHandler: Process individual event
    end
    EventHandler-->>-Lambda: Return array of processed events
    Lambda-->>-AppSync: Return event-by-event responses
    AppSync-->>-Client: Report individual event statuses
```

### Working with aggregated items

```
sequenceDiagram
    participant Client
    participant AppSync
    participant Lambda
    participant EventHandler
    note over Client,EventHandler: Aggregate Processing Workflow
    Client->>+AppSync: Send multiple events to channel
    AppSync->>+Lambda: Invoke Lambda with batch of events
    Lambda->>+EventHandler: Process events with aggregate=True
    EventHandler->>EventHandler: Batch of events
    EventHandler->>EventHandler: Process entire batch at once
    EventHandler->>EventHandler: Format response for each event
    EventHandler-->>-Lambda: Return aggregated results
    Lambda-->>-AppSync: Return success responses
    AppSync-->>-Client: Confirm all events processed
```

### Unauthorized publish

```
sequenceDiagram
    participant Client
    participant AppSync
    participant Lambda
    participant EventHandler
    note over Client,EventHandler: Publish Event Authorization Flow
    Client->>AppSync: Publish message to channel
    AppSync->>Lambda: Invoke Lambda with publish event
    Lambda->>EventHandler: Process publish event
    alt Authorization Failed
        EventHandler->>EventHandler: Authorization check fails
        EventHandler->>Lambda: Raise UnauthorizedException
        Lambda->>AppSync: Return error response
        AppSync--xClient: Message not delivered
        AppSync--xAppSync: No distribution to subscribers
    else Authorization Passed
        EventHandler->>Lambda: Return successful response
        Lambda->>AppSync: Return processed event
        AppSync->>Client: Acknowledge message
        AppSync->>AppSync: Distribute to subscribers
    end
```

### Unauthorized subscribe

```
sequenceDiagram
    participant Client
    participant AppSync
    participant Lambda
    participant EventHandler
    note over Client,EventHandler: Subscribe Event Authorization Flow
    Client->>AppSync: Request subscription to channel
    AppSync->>Lambda: Invoke Lambda with subscribe event
    Lambda->>EventHandler: Process subscribe event
    alt Authorization Failed
        EventHandler->>EventHandler: Authorization check fails
        EventHandler->>Lambda: Raise UnauthorizedException
        Lambda->>AppSync: Return error response
        AppSync--xClient: Subscription denied (HTTP 403)
    else Authorization Passed
        EventHandler->>Lambda: Return successful response
        Lambda->>AppSync: Return authorization success
        AppSync->>Client: Subscription established
    end
```

## Testing your code

You can test your event handlers by passing a mock payload with the expected structure.

For example, when working with `PUBLISH` events, you can use the `OnPublishOutput` to easily cast the output of your handler to the expected type and assert the expected values.

```
import { readFileSync } from 'node:fs';
import type { OnPublishOutput } from '@aws-lambda-powertools/event-handler/types';
import type { Context } from 'aws-lambda';
import { describe, expect, it } from 'vitest';
import { handler } from './gettingStartedOnPublish.js'; // (1)!

describe('On publish', () => {
  it('handles publish on /default/foo', async () => {
    // Prepare
    const event = structuredClone(
      JSON.parse(readFileSync('./samples/onPublishEvent.json', 'utf-8'))
    );

    // Act
    const result = (await handler(event, {} as Context)) as OnPublishOutput;

    // Assess
    expect(result.events).toHaveLength(3);
    expect(result.events[0].payload).toEqual({
      processed: true,
      original_payload: event.events[0].payload,
    });
    expect(result.events[1].payload).toEqual({
      processed: true,
      original_payload: event.events[1].payload,
    });
    expect(result.events[2].payload).toEqual({
      processed: true,
      original_payload: event.events[2].payload,
    });
  });
});

```

1. See [here](#route-handlers) to see the implementation of this handler.

```
{
  "identity": null,
  "result": null,
  "request": {
    "headers": {
      "key": "value"
    },
    "domainName": null
  },
  "info": {
    "channel": {
      "path": "/default/foo",
      "segments": ["default", "foo"]
    },
    "channelNamespace": {
      "name": "default"
    },
    "operation": "PUBLISH"
  },
  "error": null,
  "prev": null,
  "stash": {},
  "outErrors": [],
  "events": [
    {
      "payload": {
        "event_1": "data_1"
      },
      "id": "5f7dfbd1-b8ff-4c20-924e-23b42db467a0"
    },
    {
      "payload": {
        "event_2": "data_2"
      },
      "id": "ababdf65-a3e6-4c1d-acd3-87466eab433c"
    },
    {
      "payload": {
        "event_3": "data_3"
      },
      "id": "8bb2983a-0967-45a0-8243-0aeb8c83d80e"
    }
  ]
}

```

You can also assert that a handler throws an exception when processing a specific event.

```
import { readFileSync } from 'node:fs';
import { UnauthorizedException } from '@aws-lambda-powertools/event-handler/appsync-events';
import type { Context } from 'aws-lambda';
import { describe, expect, it } from 'vitest';
import { handler } from './unauthorizedException.js'; // (1)!

describe('On publish', () => {
  it('rejects subscriptions on /default/bar', async () => {
    // Prepare
    const event = structuredClone(
      JSON.parse(readFileSync('./samples/onSubscribeEvent.json', 'utf-8'))
    );

    // Act & Assess
    await expect(() => handler(event, {} as Context)).rejects.toThrow(
      UnauthorizedException
    );
  });
});

```

1. See [here](#authorization-control) to see the implementation of this handler.

```
{
  "identity": null,
  "result": null,
  "request": {
    "headers": {
      "key": "value"
    },
    "domainName": null
  },
  "info": {
    "channel": {
      "path": "/default/bar",
      "segments": ["default", "bar"]
    },
    "channelNamespace": {
      "name": "default"
    },
    "operation": "SUBSCRIBE"
  },
  "error": null,
  "prev": null,
  "stash": {},
  "outErrors": [],
  "events": null
}

```

Event Handler for AWS AppSync GraphQL APIs simplifies routing and processing of events in AWS Lambda functions. It allows you to define resolvers for GraphQL types and fields, making it easier to handle GraphQL requests without the need for complex VTL or JavaScript templates.

```
stateDiagram-v2
    direction LR
    EventSource: AWS Lambda Event Sources
    EventHandlerResolvers: AWS AppSync invocation
    LambdaInit: Lambda invocation
    EventHandler: Event Handler
    EventHandlerResolver: Route event based on GraphQL type/field keys
    YourLogic: Run your registered resolver function
    EventHandlerResolverBuilder: Adapts response to Event Source contract
    LambdaResponse: Lambda response

    state EventSource {
        EventHandlerResolvers
    }

    EventHandlerResolvers --> LambdaInit

    LambdaInit --> EventHandler
    EventHandler --> EventHandlerResolver

    state EventHandler {
        [*] --> EventHandlerResolver: app.resolve(event, context)
        EventHandlerResolver --> YourLogic
        YourLogic --> EventHandlerResolverBuilder
    }

    EventHandler --> LambdaResponse
```

## Key Features

- Route events based on GraphQL type and field keys
- Automatically parse API arguments to function parameters
- Handle GraphQL responses and errors in the expected format

## Terminology

**[Direct Lambda Resolver](https://docs.aws.amazon.com/appsync/latest/devguide/direct-lambda-reference.html)**. A custom AppSync Resolver that bypasses Apache Velocity Template (VTL) and JavaScript templates, and automatically maps your function's response to a GraphQL field.

**[Batching resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/tutorial-lambda-resolvers.html#advanced-use-case-batching)**. A technique that allows you to batch multiple GraphQL requests into a single Lambda function invocation, reducing the number of calls and improving performance.

## Getting started

Tip: Designing GraphQL Schemas for the first time?

Visit [AWS AppSync schema documentation](https://docs.aws.amazon.com/appsync/latest/devguide/designing-your-schema.html) to understand how to define types, nesting, and pagination.

### Required resources

You must have an existing AppSync GraphQL API and IAM permissions to invoke your Lambda function. That said, there is no additional permissions to use Event Handler as routing requires no dependency (*standard library*).

This is the sample infrastructure we will be using for the initial examples with an AppSync Direct Lambda Resolver.

```
schema {
  query: Query
  mutation: Mutation
}

type Query {
  # these are fields you can attach resolvers to (type_name: Query, field_name: getTodo)
  getTodo(id: ID!): Todo
  listTodos: [Todo]
}

type Mutation {
  createTodo(title: String!): Todo
}

type Todo {
  id: ID!
  userId: String
  title: String
  completed: Boolean
}

```

```
AWSTemplateFormatVersion: "2010-09-09"
Transform: AWS::Serverless-2016-10-31
Description: Hello world Direct Lambda Resolver

Globals:
  Function:
    Timeout: 5
    MemorySize: 256
    Runtime: nodejs24.x
    Environment:
      Variables:
        # Powertools for AWS Lambda (TypeScript) env vars: https://docs.aws.amazon.com/powertools/typescript/latest/environment-variables/
        POWERTOOLS_LOG_LEVEL: INFO
        POWERTOOLS_LOGGER_SAMPLE_RATE: 0.1
        POWERTOOLS_LOGGER_LOG_EVENT: true
        POWERTOOLS_SERVICE_NAME: example

Resources:
  TodosFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.handler
      CodeUri: hello_world

  # IAM Permissions and Roles

  AppSyncServiceRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: "Allow"
            Principal:
              Service:
                - "appsync.amazonaws.com"
            Action:
              - "sts:AssumeRole"

  InvokeLambdaResolverPolicy:
    Type: "AWS::IAM::Policy"
    Properties:
      PolicyName: "DirectAppSyncLambda"
      PolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: "Allow"
            Action: "lambda:invokeFunction"
            Resource:
              - !GetAtt TodosFunction.Arn
      Roles:
        - !Ref AppSyncServiceRole

  # GraphQL API

  TodosApi:
    Type: "AWS::AppSync::GraphQLApi"
    Properties:
      Name: TodosApi
      AuthenticationType: "API_KEY"
      XrayEnabled: true

  TodosApiKey:
    Type: AWS::AppSync::ApiKey
    Properties:
      ApiId: !GetAtt TodosApi.ApiId

  TodosApiSchema:
    Type: "AWS::AppSync::GraphQLSchema"
    Properties:
      ApiId: !GetAtt TodosApi.ApiId
      DefinitionS3Location: ../src/getting_started_schema.graphql
    Metadata:
      cfn-lint:
        config:
          ignore_checks:
            - W3002 # allow relative path in DefinitionS3Location

  # Lambda Direct Data Source and Resolver

  TodosFunctionDataSource:
    Type: "AWS::AppSync::DataSource"
    Properties:
      ApiId: !GetAtt TodosApi.ApiId
      Name: "HelloWorldLambdaDirectResolver"
      Type: "AWS_LAMBDA"
      ServiceRoleArn: !GetAtt AppSyncServiceRole.Arn
      LambdaConfig:
        LambdaFunctionArn: !GetAtt TodosFunction.Arn

  ListTodosResolver:
    Type: "AWS::AppSync::Resolver"
    Properties:
      ApiId: !GetAtt TodosApi.ApiId
      TypeName: "Query"
      FieldName: "listTodos"
      DataSourceName: !GetAtt TodosFunctionDataSource.Name

  GetTodoResolver:
    Type: "AWS::AppSync::Resolver"
    Properties:
      ApiId: !GetAtt TodosApi.ApiId
      TypeName: "Query"
      FieldName: "getTodo"
      DataSourceName: !GetAtt TodosFunctionDataSource.Name

  CreateTodoResolver:
    Type: "AWS::AppSync::Resolver"
    Properties:
      ApiId: !GetAtt TodosApi.ApiId
      TypeName: "Mutation"
      FieldName: "createTodo"
      DataSourceName: !GetAtt TodosFunctionDataSource.Name

Outputs:
  TodosFunction:
    Description: "Hello World Lambda Function ARN"
    Value: !GetAtt TodosFunction.Arn

  TodosApi:
    Value: !GetAtt TodosApi.GraphQLUrl

```

### Registering a resolver

You can register functions to match GraphQL types and fields with one of three methods:

- `onQuery()` - Register a function to handle a GraphQL Query type.
- `onMutation()` - Register a function to handle a GraphQL Mutation type.
- `resolver()` - Register a function to handle a GraphQL type and field.

What is a type and field?

A type would be a top-level **GraphQL Type** like `Query`, `Mutation`, `Todo`. A **GraphQL Field** would be `listTodos` under `Query`, `createTodo` under `Mutation`, etc.

The function receives the parsed arguments from the GraphQL request as its first parameter. We also take care of parsing the response or catching errors and returning them in the expected format.

#### Query resolver

When registering a resolver for a `Query` type, you can use the `onQuery()` method. This method allows you to define a function that will be invoked when a GraphQL Query is made.

```
import { AppSyncGraphQLResolver } from '@aws-lambda-powertools/event-handler/appsync-graphql';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';

const logger = new Logger({
  serviceName: 'TodoManager',
});
const app = new AppSyncGraphQLResolver({ logger });

app.onQuery<{ id: string }>('getTodo', async ({ id }) => {
  logger.debug('Resolving todo', { id });
  // Simulate fetching a todo from a database or external service
  return {
    id,
    title: 'Todo Title',
    completed: false,
  };
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

#### Mutation resolver

Similarly, you can register a resolver for a `Mutation` type using the `onMutation()` method. This method allows you to define a function that will be invoked when a GraphQL Mutation is made.

```
import {
  AppSyncGraphQLResolver,
  makeId,
} from '@aws-lambda-powertools/event-handler/appsync-graphql';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';

const logger = new Logger({
  serviceName: 'TodoManager',
});
const app = new AppSyncGraphQLResolver({ logger });

app.onMutation<{ title: string }>('createTodo', async ({ title }) => {
  logger.debug('Creating todo', { title });
  const todoId = makeId();
  // Simulate creating a todo in a database or external service
  return {
    id: todoId,
    title,
    completed: false,
  };
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

#### Generic resolver

When you want to have more control over the type and field, you can use the `resolver()` method. This method allows you to register a function for a specific GraphQL type and field including custom types.

```
import { AppSyncGraphQLResolver } from '@aws-lambda-powertools/event-handler/appsync-graphql';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';

const logger = new Logger({
  serviceName: 'TodoManager',
});
const app = new AppSyncGraphQLResolver({ logger });

app.resolver(
  async () => {
    logger.debug('Resolving todos');
    // Simulate fetching a todo from a database or external service
    return [
      {
        id: 'todo-id',
        title: 'Todo Title',
        completed: false,
      },
      {
        id: 'todo-id-2',
        title: 'Todo Title 2',
        completed: true,
      },
    ];
  },
  {
    fieldName: 'listTodos',
    typeName: 'Query',
  }
);

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

#### Using decorators

If you prefer to use the decorator syntax, you can instead use the same methods on a class method to register your handlers. Learn more about how Powertools for TypeScript supports [decorators](https://docs.aws.amazon.com/powertools/typescript/latest/getting-started/usage-patterns/index.md).

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import {
  AppSyncGraphQLResolver,
  makeId,
} from '@aws-lambda-powertools/event-handler/appsync-graphql';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';

const logger = new Logger({
  serviceName: 'TodoManager',
});
const app = new AppSyncGraphQLResolver({ logger });

class Lambda implements LambdaInterface {
  @app.onMutation('createTodo')
  public async createTodo({ title }: { title: string }) {
    logger.debug('Creating todo', { title });
    const todoId = makeId();
    // Simulate creating a todo in a database or external service
    return {
      id: todoId,
      title,
      completed: false,
    };
  }

  @app.onQuery('getTodo')
  public async getTodo({ id }: { id: string }) {
    logger.debug('Resolving todo', { id });
    // Simulate fetching a todo from a database or external service
    return {
      id,
      title: 'Todo Title',
      completed: false,
    };
  }

  @app.resolver({
    fieldName: 'listTodos',
    typeName: 'Query',
  })
  public async listTodos() {
    logger.debug('Resolving todos');
    // Simulate fetching a todo from a database or external service
    return [
      {
        id: 'todo-id',
        title: 'Todo Title',
        completed: false,
      },
      {
        id: 'todo-id-2',
        title: 'Todo Title 2',
        completed: true,
      },
    ];
  }

  async handler(event: unknown, context: Context) {
    return app.resolve(event, context, { scope: this }); // (1)!
  }
}

const lambda = new Lambda();
export const handler = lambda.handler.bind(lambda);

```

1. It's recommended to pass a refernce of `this` to ensure the correct class scope is propageted to the route handler functions.

### Scalar functions

When working with [AWS AppSync Scalar types](https://docs.aws.amazon.com/appsync/latest/devguide/scalars.html), you might want to generate the same values for data validation purposes.

For convenience, the most commonly used values are available as helper functions within the module.

```
import {
  AppSyncGraphQLResolver,
  awsDate,
  awsDateTime,
  awsTime,
  awsTimestamp,
  makeId,
} from '@aws-lambda-powertools/event-handler/appsync-graphql';
import type { Context } from 'aws-lambda';

const app = new AppSyncGraphQLResolver();

app.resolver(
  async ({ title, content }) => {
    // your business logic here
    return {
      title,
      content,
      id: makeId(),
      createdAt: awsDateTime(),
      updatedAt: awsDateTime(),
      timestamp: awsTimestamp(),
      time: awsTime(),
      date: awsDate(),
    };
  },
  {
    fieldName: 'createTodo',
    typeName: 'Mutation',
  }
);

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

Here's a table with their related scalar as a quick reference:

| Scalar type      | Scalar function | Sample value                           |
| ---------------- | --------------- | -------------------------------------- |
| **ID**           | `makeId`        | `e916c84d-48b6-484c-bef3-cee3e4d86ebf` |
| **AWSDate**      | `awsDate`       | `2022-07-08Z`                          |
| **AWSTime**      | `awsTime`       | `15:11:00.189Z`                        |
| **AWSDateTime**  | `awsDateTime`   | `2022-07-08T15:11:00.189Z`             |
| **AWSTimestamp** | `awsTimestamp`  | `1657293060`                           |

## Advanced

### Split operations with Router

As you grow the number of related GraphQL operations a given Lambda function should handle, it is natural to split them into separate files to ease maintenance - That's when the `Router` feature comes handy.

Let's assume you have `app.ts` as your Lambda function entrypoint and routes in `postRouter.ts` and `userRouter.ts`. This is how you'd use the `Router` feature.

We import **Router** instead of **AppSyncGraphQLResolver**; syntax wise is exactly the same.

```
import { Router } from '@aws-lambda-powertools/event-handler/appsync-graphql';

const postRouter = new Router();

postRouter.onQuery('getPosts', async () => {
  return [{ id: 1, title: 'First post', content: 'Hello world!' }];
});

postRouter.onMutation('createPost', async ({ title, content }) => {
  return {
    id: Date.now(),
    title,
    content,
    createdAt: new Date().toISOString(),
  };
});

export { postRouter };

```

We import **Router** instead of **AppSyncGraphQLResolver**; syntax wise is exactly the same.

```
import { Router } from '@aws-lambda-powertools/event-handler/appsync-graphql';

const userRouter = new Router();

userRouter.onQuery('getUsers', async () => {
  return [{ id: 1, name: 'John Doe', email: 'john@example.com' }];
});

export { userRouter };

```

We use `includeRouter` method and include all operations registered in the router instances.

```
import { AppSyncGraphQLResolver } from '@aws-lambda-powertools/event-handler/appsync-graphql';
import type { Context } from 'aws-lambda';
import { postRouter } from './postRouter';
import { userRouter } from './userRouter';

const app = new AppSyncGraphQLResolver();

app.includeRouter([postRouter, userRouter]);

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

### Nested mappings

Note

The following examples use a more advanced schema. These schemas differ from the [initial sample infrastructure we used earlier](#required-resources).

You can register the same route handler multiple times to resolve fields with the same return value.

```
import { AppSyncGraphQLResolver } from '@aws-lambda-powertools/event-handler/appsync-graphql';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';

const logger = new Logger({
  serviceName: 'TodoManager',
});
const app = new AppSyncGraphQLResolver({ logger });

type Location = {
  id: string;
  name: string;
  description?: string;
};

const locationsResolver = async (): Promise<Location[]> => {
  logger.debug('Resolving locations');
  // Simulate fetching locations from a database or external service
  return [
    {
      id: 'loc1',
      name: 'Location One',
      description: 'First location description',
    },
    {
      id: 'loc2',
      name: 'Location Two',
      description: 'Second location description',
    },
  ];
};

app.resolver(locationsResolver, {
  fieldName: 'locations',
  typeName: 'Merchant',
});
app.resolver(locationsResolver, {
  fieldName: 'listLocations', // (1)!
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

1. If omitted, the `typeName` defaults to `Query`.

```
schema {
  query: Query
}

type Query {
  listLocations: [Location]
}

type Location {
  id: ID!
  name: String!
  description: String
  address: String
}

type Merchant {
  id: String!
  name: String!
  description: String
  locations: [Location]
}

```

### Accessing Lambda context and event

You can access the original Lambda event or context for additional information. These are passed to the handler function as optional arguments.

```
import { AppSyncGraphQLResolver } from '@aws-lambda-powertools/event-handler/appsync-graphql';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';

const logger = new Logger({
  serviceName: 'TodoManager',
});
const app = new AppSyncGraphQLResolver({ logger });

app.onQuery<{ id: string }>('getTodo', async ({ id }, { event, context }) => {
  const { headers } = event.request; // (1)!
  const { awsRequestId } = context;
  logger.info('headers', { headers, awsRequestId });

  return {
    id,
    title: 'Todo Title',
    completed: false,
  };
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

1. The `event` parameter contains the original AppSync event and has type `AppSyncResolverEvent` from the `@types/aws-lambda`.

### Exception Handling

You can use the `exceptionHandler` method to handle any exception. This allows you to handle common errors outside your resolver and return a custom response.

The `exceptionHandler` method also supports passing an array of exceptions that you wish to handle with a single handler.

You can use an AppSync JavaScript resolver or a VTL response mapping template to detect these custom responses and forward them to the client gracefully.

```
import { AssertionError } from 'node:assert';
import { AppSyncGraphQLResolver } from '@aws-lambda-powertools/event-handler/appsync-graphql';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';

const logger = new Logger({
  serviceName: 'MyService',
});
const app = new AppSyncGraphQLResolver({ logger });

app.exceptionHandler(AssertionError, async (error) => {
  return {
    error: {
      message: error.message,
      type: error.name,
    },
  };
});

app.onQuery('createSomething', async () => {
  throw new AssertionError({
    message: 'This is an assertion error',
  });
});

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

```
import { util } from '@aws-appsync/utils';

export function request(ctx) {
  return {
    operation: 'Invoke',
    payload: ctx,
  };
}

export function response(ctx) {
  if (ctx.result.error) {
    return util.error(ctx.result.error.message, ctx.result.error.type);
  }
  return ctx.result;
}

```

```
#if (!$util.isNull($ctx.result.error))
  $util.error($ctx.result.error.message, $ctx.result.error.type)
#end

$utils.toJson($ctx.result)

```

```
{
  "data": {
    "createSomething": null
  },
  "errors": [
    {
      "path": ["createSomething"],
      "data": null,
      "errorType": "AssertionError",
      "errorInfo": null,
      "locations": [
        {
          "line": 2,
          "column": 3,
          "sourceName": null
        }
      ],
      "message": "This is an assertion Error"
    }
  ]
}

```

### Logging

By default, the utility uses the global `console` logger and emits only warnings and errors.

You can change this behavior by passing a custom logger instance to the `AppSyncGraphQLResolver` or `Router` and setting the log level for it, or by enabling [Lambda Advanced Logging Controls](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs-advanced.html) and setting the log level to `DEBUG`.

When debug logging is enabled, the resolver will emit logs that show the underlying handler resolution process. This is useful for understanding how your handlers are being resolved and invoked and can help you troubleshoot issues with your event processing.

For example, when using the [Powertools for AWS Lambda logger](https://docs.aws.amazon.com/powertools/typescript/latest/features/logger/index.md), you can set the `LOG_LEVEL` to `DEBUG` in your environment variables or at the logger level and pass the logger instance to the constructor to enable debug logging.

```
import { AppSyncGraphQLResolver } from '@aws-lambda-powertools/event-handler/appsync-graphql';
import { Logger } from '@aws-lambda-powertools/logger';
import {
  correlationPaths,
  search,
} from '@aws-lambda-powertools/logger/correlationId';
import type { Context } from 'aws-lambda';

const logger = new Logger({
  serviceName: 'TodoManager',
  logLevel: 'DEBUG',
  correlationIdSearchFn: search,
});
const app = new AppSyncGraphQLResolver({ logger });

app.onQuery<{ id: string }>('getTodo', async ({ id }) => {
  logger.debug('Resolving todo', { id });
  // Simulate fetching a todo from a database or external service
  return {
    id,
    title: 'Todo Title',
    completed: false,
  };
});

export const handler = async (event: unknown, context: Context) => {
  logger.setCorrelationId(event, correlationPaths.APPSYNC_RESOLVER);
  return app.resolve(event, context);
};

```

```
[
  {
    "level": "DEBUG",
    "message": "Adding resolver for field Query.getTodo",
    "timestamp": "2025-07-02T13:39:36.017Z",
    "service": "service_undefined",
    "sampling_rate": 0
  },
  {
    "level": "DEBUG",
    "message": "Looking for resolver for type=Query, field=getTodo",
    "timestamp": "2025-07-02T13:39:36.033Z",
    "service": "service_undefined",
    "sampling_rate": 0,
    "xray_trace_id": "1-68653697-0f1223120d19409c38812f01",
    "correlation_id": "Root=1-68653697-3623822a02e171272e2ecfe4"
  },
  {
    "level": "DEBUG",
    "message": "Resolving todo",
    "timestamp": "2025-07-02T13:39:36.033Z",
    "service": "service_undefined",
    "sampling_rate": 0,
    "xray_trace_id": "1-68653697-0f1223120d19409c38812f01",
    "correlation_id": "Root=1-68653697-3623822a02e171272e2ecfe4",
    "id": "42"
  }
]

```

## Testing your code

You can test your resolvers by passing an event with the shape expected by the AppSync GraphQL API resolver.

Here's an example of how you can test your resolvers that uses a factory function to create the event shape:

```
import type { Context } from 'aws-lambda';
import { describe, expect, it } from 'vitest';
import { handler } from './advancedNestedMappings.js';

const createEventFactory = (
  fieldName: string,
  args: Record<string, unknown>,
  parentTypeName: string
) => ({
  arguments: { ...args },
  identity: null,
  source: null,
  request: {
    headers: {
      key: 'value',
    },
    domainName: null,
  },
  info: {
    fieldName,
    parentTypeName,
    selectionSetList: [],
    variables: {},
  },
  prev: null,
  stash: {},
});

const onGraphqlEventFactory = (
  fieldName: string,
  typeName: 'Query' | 'Mutation',
  args: Record<string, unknown> = {}
) => createEventFactory(fieldName, args, typeName);

describe('Unit test for AppSync GraphQL Resolver', () => {
  it('returns the location', async () => {
    // Prepare
    const event = onGraphqlEventFactory('listLocations', 'Query');

    // Act
    const result = (await handler(event, {} as Context)) as unknown[];

    // Assess
    expect(result).toHaveLength(2);
    expect(result[0]).toEqual({
      id: 'loc1',
      name: 'Location One',
      description: 'First location description',
    });
    expect(result[1]).toEqual({
      id: 'loc2',
      name: 'Location Two',
      description: 'Second location description',
    });
  });
});

```

Create [Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html#agents-how) and focus on building your agent's logic without worrying about parsing and routing requests.

```
flowchart LR
    Bedrock[LLM] <-- uses --> Agent
    You[User input] --> Agent
    Agent[Bedrock Agent] <-- tool use --> Lambda

    subgraph Agent[Bedrock Agent]
        ToolDescriptions[Tool Definitions]
    end

    subgraph Lambda[Lambda Function]
        direction TB
        Parsing[Parameter Parsing] --> Routing
        Routing --> Code[Your code]
        Code --> ResponseBuilding[Response Building]
    end

    style You stroke:#0F0,stroke-width:2px
```

## Key Features

- Easily expose tools for your Large Language Model (LLM) agents
- Automatic routing based on tool name and function details
- Graceful error handling and response formatting

## Terminology

**Event handler** is a Powertools for AWS feature that processes an event, runs data parsing and validation, routes the request to a specific function, and returns a response to the caller in the proper format.

**Function details** consist of a list of parameters, defined by their name, data type, and whether or not they are required. The agent uses these configurations to determine what information it needs to elicit from the user.

**Action group** is a collection of two resources where you define the actions that the agent should carry out: an OpenAPI schema to define the APIs that the agent can invoke to carry out its tasks, and a Lambda function to execute those actions.

**Large Language Models (LLM)** are very large deep learning models that are pre-trained on vast amounts of data, capable of extracting meanings from a sequence of text and understanding the relationship between words and phrases within that text.

**Amazon Bedrock Agent** is an Amazon Bedrock feature to build and deploy conversational agents that can interact with your customers using Large Language Models (LLM) and AWS Lambda functions.

## Getting Started

```
npm i @aws-lambda-powertools/event-handler

```

### Required resources

You must create an Amazon Bedrock Agent with at least one action group. Each action group can contain up to 5 tools, which in turn need to match the ones defined in your Lambda function. Bedrock must have permission to invoke your Lambda function.

Click to see example IaC templates

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Globals:
  Function:
    Timeout: 30
    MemorySize: 256
    Runtime: nodejs24.x

Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.handler
      CodeUri: hello_world

  AirlineAgentRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Sub '${AWS::StackName}-AirlineAgentRole'
      Description: 'Role for Bedrock Airline agent'
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: bedrock.amazonaws.com
            Action: sts:AssumeRole
      Policies:
        - PolicyName: bedrock
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action: 'bedrock:*'
                Resource:
                  - !Sub 'arn:aws:bedrock:us-*::foundation-model/*'
                  - !Sub 'arn:aws:bedrock:us-*:*:inference-profile/*'

  BedrockAgentInvokePermission:
    Type: AWS::Lambda::Permission
    Properties:
      FunctionName: !Ref HelloWorldFunction
      Action: lambda:InvokeFunction
      Principal: bedrock.amazonaws.com
      SourceAccount: !Ref 'AWS::AccountId'
      SourceArn: !Sub 'arn:aws:bedrock:${AWS::Region}:${AWS::AccountId}:agent/${AirlineAgent}'

  # Bedrock Agent
  AirlineAgent:
    Type: AWS::Bedrock::Agent
    Properties:
      AgentName: AirlineAgent
      Description: 'A simple Airline agent'
      FoundationModel: !Sub 'arn:aws:bedrock:us-west-2:${AWS::AccountId}:inference-profile/us.amazon.nova-pro-v1:0'
      Instruction: |
        You are an airport traffic control agent. You will be given a city name and you will return the airport code for that city.
      AgentResourceRoleArn: !GetAtt AirlineAgentRole.Arn
      AutoPrepare: true
      ActionGroups:
        - ActionGroupName: AirlineActionGroup
          ActionGroupExecutor:
            Lambda: !GetAtt AirlineAgentFunction.Arn
          FunctionSchema:
            Functions:
              - Name: getAirportCodeForCity
                Description: 'Get the airport code for a given city'
                Parameters:
                  city:
                    Type: string
                    Description: 'The name of the city to get the airport code for'
                    Required: true

```

```
import { Arn, RemovalPolicy, Stack, type StackProps } from 'aws-cdk-lib';
import { CfnAgent } from 'aws-cdk-lib/aws-bedrock';
import {
  PolicyDocument,
  PolicyStatement,
  Role,
  ServicePrincipal,
} from 'aws-cdk-lib/aws-iam';
import { Runtime } from 'aws-cdk-lib/aws-lambda';
import { NodejsFunction, OutputFormat } from 'aws-cdk-lib/aws-lambda-nodejs';
import { LogGroup, RetentionDays } from 'aws-cdk-lib/aws-logs';
import type { Construct } from 'constructs';

export class BedrockAgentsStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const fnName = 'BedrockAgentsFn';
    const logGroup = new LogGroup(this, 'AirlineAgentLogGroup', {
      logGroupName: `/aws/lambda/${fnName}`,
      removalPolicy: RemovalPolicy.DESTROY,
      retention: RetentionDays.ONE_DAY,
    });
    const fn = new NodejsFunction(this, 'AirlineAgentFunction', {
      functionName: fnName,
      logGroup,
      runtime: Runtime.NODEJS_24_X,
      entry: './src/index.ts',
      handler: 'handler',
      bundling: {
        minify: true,
        mainFields: ['module', 'main'],
        sourceMap: true,
        format: OutputFormat.ESM,
      },
    });

    const agentRole = new Role(this, 'AirlineAgentRole', {
      assumedBy: new ServicePrincipal('bedrock.amazonaws.com'),
      description: 'Role for Bedrock Airline agent',
      inlinePolicies: {
        bedrock: new PolicyDocument({
          statements: [
            new PolicyStatement({
              actions: ['bedrock:*'],
              resources: [
                Arn.format(
                  {
                    service: 'bedrock',
                    resource: 'foundation-model/*',
                    region: 'us-*',
                    account: '',
                  },
                  Stack.of(this)
                ),
                Arn.format(
                  {
                    service: 'bedrock',
                    resource: 'inference-profile/*',
                    region: 'us-*',
                    account: '*',
                  },
                  Stack.of(this)
                ),
              ],
            }),
          ],
        }),
      },
    });

    const agent = new CfnAgent(this, 'AirlineAgent', {
      agentName: 'AirlineAgent',
      actionGroups: [
        {
          actionGroupName: 'AirlineActionGroup',
          actionGroupExecutor: {
            lambda: fn.functionArn,
          },
          functionSchema: {
            functions: [
              {
                name: 'getAirportCodeForCity',
                description: 'Get the airport code for a given city',
                parameters: {
                  city: {
                    type: 'string',
                    description:
                      'The name of the city to get the airport code for',
                    required: true,
                  },
                },
              },
            ],
          },
        },
      ],
      agentResourceRoleArn: agentRole.roleArn,
      autoPrepare: true,
      description: 'A simple Airline agent',
      foundationModel: `arn:aws:bedrock:us-west-2:${Stack.of(this).account}:inference-profile/us.amazon.nova-pro-v1:0`,
      instruction:
        'You are an airport traffic control agent. You will be given a city name and you will return the airport code for that city.',
    });
    fn.addPermission('BedrockAgentInvokePermission', {
      principal: new ServicePrincipal('bedrock.amazonaws.com'),
      action: 'lambda:InvokeFunction',
      sourceAccount: this.account,
      sourceArn: `arn:aws:bedrock:${this.region}:${this.account}:agent/${agent.attrAgentId}`,
    });
  }
}

```

### Usage

Use the `BedrockAgentFunctionResolver` to register your tools and handle the requests to your Lambda function. The resolver will automatically parse the request, route it to the appropriate function, and return a well-formed response that includes the tool's output and any existing session attributes.

When passing the tool parameters to your handler, we will automatically cast them to the appropriate type based on the `type` field defined in the action group. This means you can use native JavaScript types like `string`, `number`, `boolean` without worrying about parsing them yourself.

Currently, we don't support parsing `array` types, so you will receive them as strings.

```
import { BedrockAgentFunctionResolver } from '@aws-lambda-powertools/event-handler/bedrock-agent';
import type { Context } from 'aws-lambda';

const app = new BedrockAgentFunctionResolver();

app.tool<{ city: string }>(
  async ({ city }) => {
    return {
      city,
      airportCode: 'XYZ',
    };
  },
  {
    name: 'getAirportCodeForCity',
    description: 'Get the airport code for a given city', // (1)!
  }
);

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

1. The `description` field is optional, but highly recommended in the action group definition so that the LLM can understand what the tool does and how to use it.

## Advanced

### Handling errors

By default, we will handle errors gracefully and return a well-formed response to the agent so that it can continue the conversation with the user.

When an error occurs, we send back an error message in the response body that includes the error type and message. The agent will then use this information to let the user know that something went wrong.

If you want to handle errors differently, you can return a `BedrockFunctionResponse` with a custom `body` and `responseState` set to `FAILURE`. This is useful when you want to abort the conversation.

Tip

You can use the same technique to reprompt the user for missing information or for them to correct their input. Just return a `BedrockFunctionResponse` with a custom message and `responseState` set to `REPROMPT`.

```
import {
  BedrockAgentFunctionResolver,
  BedrockFunctionResponse,
} from '@aws-lambda-powertools/event-handler/bedrock-agent';
import type { Context } from 'aws-lambda';

const app = new BedrockAgentFunctionResolver();

app.tool<{ city: string }>(
  async ({ city }, { event }) => {
    try {
      throw new Error('Simulated error for demonstration purposes');
    } catch {
      const {
        sessionAttributes,
        promptSessionAttributes,
        knowledgeBasesConfiguration,
      } = event;
      return new BedrockFunctionResponse({
        body: `An error occurred while fetching the airport code for ${city}`,
        responseState: 'FAILURE',
        sessionAttributes,
        promptSessionAttributes,
        knowledgeBasesConfiguration,
      });
    }
  },
  {
    name: 'getAirportCodeForCity',
    description: 'Get the airport code for a given city',
  }
);

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

### Accessing Lambda context and event

You can access to the original Lambda event or context for additional information. These are passed to the handler function as optional arguments.

```
import { BedrockAgentFunctionResolver } from '@aws-lambda-powertools/event-handler/bedrock-agent';
import type { Context } from 'aws-lambda';

const app = new BedrockAgentFunctionResolver();

app.tool<{ city: string }>(
  async ({ city }, { event, context }) => {
    const { sessionAttributes } = event;
    sessionAttributes.requestId = context.awsRequestId;

    return {
      city,
      airportCode: 'XYZ', // Simulated airport code for the city
    };
  },
  {
    name: 'getAirportCodeForCity',
    description: 'Get the airport code for a given city',
  }
);

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

### Setting session attributes

When Bedrock Agents invoke your Lambda function, it can pass session attributes that you can use to store information across multiple interactions with the user. You can access these attributes in your handler function and modify them as needed.

```
import {
  BedrockAgentFunctionResolver,
  BedrockFunctionResponse,
} from '@aws-lambda-powertools/event-handler/bedrock-agent';
import type { Context } from 'aws-lambda';

const app = new BedrockAgentFunctionResolver();

app.tool<{ city: string }>(
  async ({ city }, { event }) => {
    const {
      sessionAttributes,
      promptSessionAttributes,
      knowledgeBasesConfiguration,
    } = event;

    // your logic to fetch airport code for the city

    return new BedrockFunctionResponse({
      body: JSON.stringify({
        city,
        airportCode: 'XYZ',
      }),
      sessionAttributes: {
        ...sessionAttributes,
        isCommercialAirport: true,
      },
      promptSessionAttributes,
      knowledgeBasesConfiguration,
    });
  },
  {
    name: 'getAirportCodeForCity',
    description: 'Get the airport code for a given city',
  }
);

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

### Logging

By default, the `BedrockAgentFunctionResolver` uses the global `console` logger and emits only warnings and errors.

You can change this behavior by passing a custom logger instance to the `BedrockAgentFunctionResolver` constructor and setting its log level. Alternatively, you can also enable [Lambda Advanced Logging Controls](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs-advanced.html) and setting the log level to `DEBUG`.

When debug logging is enabled, the resolver will emit logs that show the underlying handler registration and the routing process. This is useful for understanding how the agent resolves the tools and routes the requests.

For example, when using the [Powertools for AWS Lambda logger](https://docs.aws.amazon.com/powertools/typescript/latest/features/logger/index.md), you can set the `LOG_LEVEL` to `DEBUG` in your environment variables or at the logger level and pass the logger instance to the `BedrockAgentFunctionResolver` constructor to enable debug logging.

```
import { BedrockAgentFunctionResolver } from '@aws-lambda-powertools/event-handler/bedrock-agent';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context } from 'aws-lambda';

const logger = new Logger({
  serviceName: 'serverlessAirline',
  logLevel: 'DEBUG',
});
const app = new BedrockAgentFunctionResolver({ logger });

app.tool<{ city: string }>(
  async ({ city }) => {
    return {
      city,
      airportCode: 'XYZ', // Simulated airport code for the city
    };
  },
  {
    name: 'getAirportCodeForCity',
    description: 'Get the airport code for a given city',
  }
);

export const handler = async (event: unknown, context: Context) =>
  app.resolve(event, context);

```

The Parameters utility provides high-level functions to retrieve one or multiple parameter values from [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html), [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html), [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html), [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html), or your own parameter store.

## Key features

- Retrieve one or multiple parameters from the underlying provider
- Cache parameter values for a given amount of time (defaults to 5 seconds)
- Transform parameter values from JSON or base64 encoded strings
- Bring Your Own Parameter Store Provider

## Getting started

The Parameters Utility helps to retrieve parameters from the System Manager Parameter Store (SSM), secrets from the Secrets Manager, and application configuration from AppConfig. Additionally, the utility also offers support for a DynamoDB provider, enabling the retrieval of arbitrary parameters from specified tables.

### Installation

Note

This utility supports **[AWS SDK for JavaScript v3](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) only**. This allows the utility to be modular, and you to install only the SDK packages you need and keep your bundle size small.

Depending on the provider you want to use, install the library and the corresponding AWS SDK package:

```
npm install @aws-lambda-powertools/parameters @aws-sdk/client-ssm

```

```
npm install @aws-lambda-powertools/parameters @aws-sdk/client-secrets-manager

```

```
npm install @aws-lambda-powertools/parameters @aws-sdk/client-appconfigdata

```

```
npm install @aws-lambda-powertools/parameters @aws-sdk/client-dynamodb @aws-sdk/util-dynamodb

```

Tip

If you are using the `nodejs18.x` runtime or newer, the AWS SDK for JavaScript v3 is already installed and you can install the utility only.

### IAM Permissions

This utility requires additional permissions to work as expected.

Note

Different parameter providers require different permissions.

| Provider  | Function/Method                                                  | IAM Permission                                                                       |
| --------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| SSM       | **`getParameter`**, **`SSMProvider.get`**                        | **`ssm:GetParameter`**                                                               |
| SSM       | **`getParameters`**, **`SSMProvider.getMultiple`**               | **`ssm:GetParametersByPath`**                                                        |
| SSM       | **`getParametersByName`**, **`SSMProvider.getParametersByName`** | **`ssm:GetParameter`** and **`ssm:GetParameters`**                                   |
| SSM       | If using **`decrypt: true`**                                     | You must add an additional permission **`kms:Decrypt`**                              |
| SSM       | **`setParameter`**, **`SSMProvider.set`**                        | **`ssm:PutParameter`**                                                               |
| Secrets   | **`getSecret`**, **`SecretsProvider.get`**                       | **`secretsmanager:GetSecretValue`**                                                  |
| DynamoDB  | **`DynamoDBProvider.get`**                                       | **`dynamodb:GetItem`**                                                               |
| DynamoDB  | **`DynamoDBProvider.getMultiple`**                               | **`dynamodb:Query`**                                                                 |
| AppConfig | **`getAppConfig`**, **`AppConfigProvider.getAppConfig`**         | **`appconfig:GetLatestConfiguration`** and **`appconfig:StartConfigurationSession`** |

### Fetching parameters

You can retrieve a single parameter using the `getParameter` high-level function.

```
import { getParameter } from '@aws-lambda-powertools/parameters/ssm';

export const handler = async (): Promise<void> => {
  // Retrieve a single parameter
  const parameter = await getParameter('/my/parameter');
  console.log(parameter);
};

```

For multiple parameters, you can use either:

- `getParameters` to recursively fetch all parameters by path.
- `getParametersByName` to fetch distinct parameters by their full name. It also accepts custom caching, transform, decrypt per parameter.

```
import { getParameters } from '@aws-lambda-powertools/parameters/ssm';

export const handler = async (): Promise<void> => {
  /**
   * Retrieve multiple parameters from a path prefix recursively.
   * This returns an object with the parameter name as key
   */
  const parameters = await getParameters('/my/path/prefix');
  for (const [key, value] of Object.entries(parameters || {})) {
    console.log(`${key}: ${value}`);
  }
};

```

```
import { Transform } from '@aws-lambda-powertools/parameters';
import { getParametersByName } from '@aws-lambda-powertools/parameters/ssm';
import type { SSMGetParametersByNameOptions } from '@aws-lambda-powertools/parameters/ssm/types';

const props: Record<string, SSMGetParametersByNameOptions> = {
  '/develop/service/commons/telemetry/config': {
    maxAge: 300,
    transform: Transform.JSON,
  },
  '/no_cache_param': { maxAge: 0 },
  '/develop/service/payment/api/capture/url': {}, // When empty or undefined, it uses default values
};

export const handler = async (): Promise<void> => {
  // This returns an object with the parameter name as key
  const parameters = await getParametersByName(props, { maxAge: 60 });
  for (const [key, value] of Object.entries(parameters)) {
    console.log(`${key}: ${value}`);
  }
};

```

`getParametersByName` supports graceful error handling

By default, the provider will throw a `GetParameterError` when any parameter fails to be fetched. You can override it by setting `throwOnError: false`.

When disabled, instead the provider will take the following actions:

- Add failed parameter name in the `_errors` key, *e.g.*, `{ _errors: [ '/param1', '/param2' ] }`
- Keep only successful parameter names and their values in the response
- Throw `GetParameterError` if any of your parameters is named `_errors`

```
import { getParametersByName } from '@aws-lambda-powertools/parameters/ssm';
import type { SSMGetParametersByNameOptions } from '@aws-lambda-powertools/parameters/ssm/types';

const props: Record<string, SSMGetParametersByNameOptions> = {
  '/develop/service/commons/telemetry/config': {
    maxAge: 300,
    transform: 'json',
  },
  '/this/param/does/not/exist': {}, // <- Example of non-existent parameter
};

export const handler = async (): Promise<void> => {
  const { _errors: errors, ...parameters } = await getParametersByName(props, {
    throwOnError: false,
  });

  // Handle gracefully, since `/this/param/does/not/exist` will only be available in `_errors`
  if (errors?.length) {
    console.error(`Unable to retrieve parameters: ${errors.join(',')}`);
  }

  for (const [key, value] of Object.entries(parameters)) {
    console.log(`${key}: ${value}`);
  }
};

```

### Storing parameters

You can store parameters in the System Manager Parameter Store using `setParameter`.

```
import { setParameter } from '@aws-lambda-powertools/parameters/ssm';

export const handler = async (): Promise<void> => {
  // Store a string parameter
  const parameter = await setParameter('/my/parameter', { value: 'my-value' });
  console.log(parameter);
};

```

If the parameter is already existent, it needs to have the `overwrite` parameter set to `true` to update the value.

```
import { setParameter } from '@aws-lambda-powertools/parameters/ssm';

export const handler = async (): Promise<void> => {
  // Overwrite a string parameter
  const parameter = await setParameter('/my/parameter', {
    value: 'my-value',
    overwrite: true,
  });
  console.log(parameter);
};

```

### Fetching secrets

You can fetch secrets stored in Secrets Manager using `getSecret`.

```
import { getSecret } from '@aws-lambda-powertools/parameters/secrets';

export const handler = async (): Promise<void> => {
  // Retrieve a single secret
  const secret = await getSecret('my-secret');
  console.log(secret);
};

```

### Fetching app configurations

You can fetch application configurations in AWS AppConfig using `getAppConfig`.

The following will retrieve the latest version and store it in the cache.

```
import { getAppConfig } from '@aws-lambda-powertools/parameters/appconfig';

export const handler = async (): Promise<void> => {
  // Retrieve a configuration, latest version
  const config = await getAppConfig('my-configuration', {
    environment: 'my-env',
    application: 'my-app',
  });
  console.log(config);
};

```

When using `getAppConfig`, the [underlying provider](#appconfigprovider) is cached. To fetch from different applications or environments, create separate `AppConfigProvider` instances for each application/environment combination.

## Advanced

### Adjusting cache TTL

By default, the provider will cache parameters retrieved in-memory for 5 seconds.

You can adjust how long values should be kept in cache by using the param `maxAge`, when using `get()` or `getMultiple()` methods across all providers.

Tip

If you want to set the same TTL for all parameters, you can set the `POWERTOOLS_PARAMETERS_MAX_AGE` environment variable. **This will override the default TTL of 5 seconds but can be overridden by the `maxAge` parameter**.

```
import { SSMProvider } from '@aws-lambda-powertools/parameters/ssm';

const parametersProvider = new SSMProvider();

export const handler = async (): Promise<void> => {
  // Retrieve a single parameter and cache it for 1 minute
  const parameter = await parametersProvider.get('/my/parameter', {
    maxAge: 60,
  }); // (1)
  console.log(parameter);

  // Retrieve multiple parameters from a path prefix and cache them for 2 minutes
  const parameters = await parametersProvider.getMultiple('/my/path/prefix', {
    maxAge: 120,
  });
  for (const [key, value] of Object.entries(parameters || {})) {
    console.log(`${key}: ${value}`);
  }
};

```

1. Options passed to `get()`, `getMultiple()`, and `getParametersByName()` will override the values set in `POWERTOOLS_PARAMETERS_MAX_AGE` environment variable.

Info

The `maxAge` parameter is also available in high level functions like `getParameter`, `getSecret`, etc.

### Always fetching the latest

If you'd like to always ensure you fetch the latest parameter from the store regardless if already available in cache, use the `forceFetch` parameter.

```
import { getParameter } from '@aws-lambda-powertools/parameters/ssm';

export const handler = async (): Promise<void> => {
  // Retrieve a single parameter
  const parameter = await getParameter('/my/parameter', { forceFetch: true });
  console.log(parameter);
};

```

### Built-in provider class

For greater flexibility such as configuring the underlying SDK client used by built-in providers, you can use their respective Provider Classes directly.

Tip

This can be used to retrieve values from other regions, change the retry behavior, etc.

#### SSMProvider

```
import { SSMProvider } from '@aws-lambda-powertools/parameters/ssm';
import type { SSMClientConfig } from '@aws-sdk/client-ssm';

const clientConfig: SSMClientConfig = { region: 'us-east-1' };
const parametersProvider = new SSMProvider({ clientConfig });

export const handler = async (): Promise<void> => {
  // Retrieve a single parameter
  const parameter = await parametersProvider.get('/my/parameter');
  console.log(parameter);

  // Retrieve multiple parameters from a path prefix
  const parameters = await parametersProvider.getMultiple('/my/path/prefix');
  for (const [key, value] of Object.entries(parameters || {})) {
    console.log(`${key}: ${value}`);
  }
};

```

The AWS Systems Manager Parameter Store provider supports two additional arguments for the `get()` and `getMultiple()` methods:

| Parameter     | Default | Description                                                                                   |
| ------------- | ------- | --------------------------------------------------------------------------------------------- |
| **decrypt**   | `false` | Will automatically decrypt the parameter (see required [IAM Permissions](#iam-permissions)).  |
| **recursive** | `true`  | For `getMultiple()` only, will fetch all parameter values recursively based on a path prefix. |

Tip

If you want to always decrypt parameters, you can set the `POWERTOOLS_PARAMETERS_SSM_DECRYPT=true` environment variable. **This will override the default value of `false` but can be overridden by the `decrypt` parameter**.

```
import { SSMProvider } from '@aws-lambda-powertools/parameters/ssm';

const parametersProvider = new SSMProvider();

export const handler = async (): Promise<void> => {
  const decryptedValue = await parametersProvider.get(
    '/my/encrypted/parameter',
    { decrypt: true }
  ); // (1)
  console.log(decryptedValue);

  const noRecursiveValues = await parametersProvider.getMultiple(
    '/my/path/prefix',
    { recursive: false }
  );
  for (const [key, value] of Object.entries(noRecursiveValues || {})) {
    console.log(`${key}: ${value}`);
  }
};

```

1. Options passed to `get()`, `getMultiple()`, and `getParametersByName()` will override the values set in `POWERTOOLS_PARAMETERS_SSM_DECRYPT` environment variable.

#### SecretsProvider

```
import { SecretsProvider } from '@aws-lambda-powertools/parameters/secrets';
import type { SecretsManagerClientConfig } from '@aws-sdk/client-secrets-manager';

const clientConfig: SecretsManagerClientConfig = { region: 'us-east-1' };
const secretsProvider = new SecretsProvider({ clientConfig });

export const handler = async (): Promise<void> => {
  // Retrieve a single secret
  const secret = await secretsProvider.get('my-secret');
  console.log(secret);
};

```

#### AppConfigProvider

The AWS AppConfig provider requires two arguments when initialized:

| Parameter       | Mandatory in constructor | Alternative                            | Description                                              |
| --------------- | ------------------------ | -------------------------------------- | -------------------------------------------------------- |
| **application** | No                       | `POWERTOOLS_SERVICE_NAME` env variable | The application in which your config resides.            |
| **environment** | Yes                      | *(N/A)*                                | The environment that corresponds to your current config. |

```
import { AppConfigProvider } from '@aws-lambda-powertools/parameters/appconfig';
import type { AppConfigDataClientConfig } from '@aws-sdk/client-appconfigdata';

const clientConfig: AppConfigDataClientConfig = { region: 'us-east-1' };
const configsProvider = new AppConfigProvider({
  application: 'my-app',
  environment: 'my-env',
  clientConfig,
});

export const handler = async (): Promise<void> => {
  // Retrieve a config
  const config = await configsProvider.get('my-config');
  console.log(config);
};

```

#### DynamoDBProvider

The DynamoDB Provider does not have any high-level functions and needs to know the name of the DynamoDB table containing the parameters.

**DynamoDB table structure for single parameters**

For single parameters, you must use `id` as the [partition key](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey) for that table.

Example

DynamoDB table with `id` partition key and `value` as attribute

| id           | value    |
| ------------ | -------- |
| my-parameter | my-value |

With this table, `await dynamoDBProvider.get('my-param')` will return `my-value`.

```
import { DynamoDBProvider } from '@aws-lambda-powertools/parameters/dynamodb';

const dynamoDBProvider = new DynamoDBProvider({ tableName: 'my-table' });

export const handler = async (): Promise<void> => {
  // Retrieve a value from DynamoDB
  const value = await dynamoDBProvider.get('my-parameter');
  console.log(value);
};

```

You can initialize the DynamoDB provider pointing to [DynamoDB Local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html) using the `endpoint` field in the `clientConfig` parameter:

```
import { DynamoDBProvider } from '@aws-lambda-powertools/parameters/dynamodb';

const dynamoDBProvider = new DynamoDBProvider({
  tableName: 'my-table',
  clientConfig: {
    endpoint: 'http://localhost:8000',
  },
});

export const handler = async (): Promise<void> => {
  // Retrieve a value from DynamoDB
  const value = await dynamoDBProvider.get('my-parameter');
  console.log(value);
};

```

**DynamoDB table structure for multiple values parameters**

You can retrieve multiple parameters sharing the same `id` by having a sort key named `sk`.

Example

DynamoDB table with `id` primary key, `sk` as sort key and `value` as attribute

| id          | sk      | value      |
| ----------- | ------- | ---------- |
| my-hash-key | param-a | my-value-a |
| my-hash-key | param-b | my-value-b |
| my-hash-key | param-c | my-value-c |

With this table, `await dynamoDBProvider.getMultiple('my-hash-key')` will return a dictionary response in the shape of `sk:value`.

```
import { DynamoDBProvider } from '@aws-lambda-powertools/parameters/dynamodb';

const dynamoDBProvider = new DynamoDBProvider({ tableName: 'my-table' });

export const handler = async (): Promise<void> => {
  /**
   * Retrieve multiple values by performing a Query on the DynamoDB table.
   * This returns a dict with the sort key attribute as dict key.
   */
  const values = await dynamoDBProvider.getMultiple('my-hash-key');
  for (const [key, value] of Object.entries(values || {})) {
    // key: param-a
    // value: my-value-a
    console.log(`${key}: ${value}`);
  }
};

```

```
{
  "param-a": "my-value-a",
  "param-b": "my-value-b",
  "param-c": "my-value-c"
}

```

**Customizing DynamoDBProvider**

DynamoDB provider can be customized at initialization to match your table structure:

| Parameter     | Mandatory | Default | Description                                                                                               |
| ------------- | --------- | ------- | --------------------------------------------------------------------------------------------------------- |
| **tableName** | **Yes**   | *(N/A)* | Name of the DynamoDB table containing the parameter values.                                               |
| **keyAttr**   | No        | `id`    | Hash key for the DynamoDB table.                                                                          |
| **sortAttr**  | No        | `sk`    | Range key for the DynamoDB table. You don't need to set this if you don't use the `getMultiple()` method. |
| **valueAttr** | No        | `value` | Name of the attribute containing the parameter value.                                                     |

```
import { DynamoDBProvider } from '@aws-lambda-powertools/parameters/dynamodb';

const dynamoDBProvider = new DynamoDBProvider({
  tableName: 'my-table',
  keyAttr: 'key',
  sortAttr: 'sort',
  valueAttr: 'val',
});

export const handler = async (): Promise<void> => {
  const value = await dynamoDBProvider.get('my-parameter');
  console.log(value);
};

```

### Create your own provider

You can create your own custom parameter store provider by extending the `BaseProvider` class, and implementing the `get()` and `getMultiple()` methods, as well as its respective `_get()` and `_getMultiple()` private methods to retrieve a single, or multiple parameters from your custom store.

All caching logic is handled by the `BaseProvider`, and provided that the return types of your store are compatible with the ones used in the `BaseProvider`, all transformations will also work as expected.

Here's an example of implementing a custom parameter store using an external service like HashiCorp Vault, a widely popular key-value secret storage.

```
import { Logger } from '@aws-lambda-powertools/logger';
import { HashiCorpVaultProvider } from './customProviderVault.js';

const logger = new Logger({ serviceName: 'serverless-airline' });
const secretsProvider = new HashiCorpVaultProvider({
  url: 'https://vault.example.com:8200/v1',
  token: process.env.ROOT_TOKEN ?? '',
  rootPath: 'kv',
});

// Retrieve a secret from HashiCorp Vault
const secret = await secretsProvider.get<{ foo: 'string' }>('my-secret');

const res = await fetch('https://example.com/api', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${secret?.foo}`,
  },
  body: JSON.stringify({ data: 'example' }),
});
logger.debug('res status', { status: res.status });

```

```
import { BaseProvider } from '@aws-lambda-powertools/parameters/base';
import { GetParameterError } from '@aws-lambda-powertools/parameters/errors';
import type {
  HashiCorpVaultGetOptions,
  HashiCorpVaultProviderOptions,
} from './customProviderVaultTypes.js';

class HashiCorpVaultProvider extends BaseProvider {
  readonly #baseUrl: string;
  readonly #token: string;
  readonly #rootPath?: string;
  readonly #timeout: number;
  readonly #abortController: AbortController;

  /**
   * It initializes the HashiCorpVaultProvider class.
   *
   * @param config - The configuration object.
   */
  public constructor(config: HashiCorpVaultProviderOptions) {
    super({});

    const { url, token, rootPath, timeout } = config;
    this.#baseUrl = url;
    this.#rootPath = rootPath ?? 'secret';
    this.#timeout = timeout ?? 5000;
    this.#token = token;
    this.#abortController = new AbortController();
  }

  /**
   * Retrieve a secret from HashiCorp Vault.
   *
   * @param name - The name of the secret
   * @param options - Options to customize the retrieval of the secret
   * @param options.maxAge - The maximum age of the value in cache before fetching a new one (in seconds) (default: 5)
   * @param options.forceFetch - Whether to always fetch a new value from the store regardless if already available in cache
   * @param options.sdkOptions - Extra options to pass to the HashiCorp Vault SDK, e.g. `mount` or `version`
   */
  public async get<T extends Record<string, unknown>>(
    name: string,
    options?: HashiCorpVaultGetOptions
  ): Promise<T | undefined> {
    return super.get(name, options) as Promise<
      Record<string, unknown> | undefined
    > as Promise<T | undefined>;
  }

  /**
   * Retrieving multiple parameter values is not supported with HashiCorp Vault.
   */
  public async getMultiple(path: string, _options?: unknown): Promise<void> {
    await super.getMultiple(path);
  }

  /**
   * Retrieve a secret from HashiCorp Vault.
   *
   * @param name - The name of the secret
   * @param options - Options to customize the retrieval of the secret
   */
  protected async _get(
    name: string,
    options?: HashiCorpVaultGetOptions
  ): Promise<Record<string, unknown>> {
    const { sdkOptions } = options ?? {};
    const mount = sdkOptions?.mount ?? this.#rootPath;
    const version = sdkOptions?.version
      ? `?version=${sdkOptions?.version}`
      : '';

    setTimeout(() => {
      this.#abortController.abort();
    }, this.#timeout);

    const res = await fetch(
      `${this.#baseUrl}/${mount}/data/${name}${version}`,
      {
        headers: { 'X-Vault-Token': this.#token },
        method: 'GET',
        signal: this.#abortController.signal,
      }
    );
    if (!res.ok) {
      throw new GetParameterError(`Failed to fetch secret ${res.statusText}`);
    }
    const response = await res.json();
    return response.data.data;
  }

  /**
   * Retrieving multiple parameter values from HashiCorp Vault is not supported.
   *
   * @throws Not Implemented Error.
   */
  protected async _getMultiple(
    _path: string,
    _options?: unknown
  ): Promise<Record<string, unknown> | undefined> {
    throw new GetParameterError('Method not implemented.');
  }
}

export { HashiCorpVaultProvider };

```

```
import type { GetOptionsInterface } from '@aws-lambda-powertools/parameters/base/types';

/**
 * Options for the HashiCorpVaultProvider class constructor.
 *
 * @param {string} url - Indicate the server name/IP, port and API version for the Vault instance, all paths are relative to this one.
 * @param {string} token - The Vault token to use for authentication.
 *
 */
interface HashiCorpVaultProviderOptions {
  /**
   * Indicate the server name/IP, port and API version for the Vault instance, all paths are relative to this one.
   * @example 'https://vault.example.com:8200/v1'
   */
  url: string;
  /**
   * The Vault token to use for authentication.
   */
  token: string;
  /**
   * The root path to use for the secret engine. Defaults to `secret`.
   */
  rootPath?: string;
  /**
   * The timeout in milliseconds for the HTTP requests. Defaults to `5000`.
   * @example 10000
   * @default 5000
   */
  timeout?: number;
}

type HashiCorpVaultReadKVSecretOptions = {
  /**
   * The mount point of the secret engine to use. Defaults to `secret`.
   * @example 'kv'
   */
  mount?: string;
  /**
   * The version of the secret to retrieve. Defaults to `undefined`.
   * @example 1
   */
  version?: number;
};

interface HashiCorpVaultGetOptions extends GetOptionsInterface {
  /**
   * The Parameters utility does not support transforming `Record<string, unknown>` values as returned by the HashiCorp Vault SDK.
   */
  transform?: never;
  sdkOptions?: HashiCorpVaultReadKVSecretOptions;
}

export type { HashiCorpVaultProviderOptions, HashiCorpVaultGetOptions };

```

### Deserializing values with transform parameter

For parameters stored in JSON or Base64 format, you can use the `transform` argument for deserialization.

Info

The `transform` argument is available across all providers, including the high level functions.

```
import { getParameter } from '@aws-lambda-powertools/parameters/ssm';

export const handler = async (): Promise<void> => {
  const valueFromJson = await getParameter('/my/json/parameter', {
    transform: 'json',
  });
  console.log(valueFromJson);
};

```

```
import { SecretsProvider } from '@aws-lambda-powertools/parameters/secrets';

const secretsProvider = new SecretsProvider();

export const handler = async (): Promise<void> => {
  // Transform a JSON string
  const json = await secretsProvider.get('my-secret-json', {
    transform: 'json',
  });
  console.log(json);

  // Transform a Base64 encoded string (e.g. binary)
  const binary = await secretsProvider.getMultiple('my-secret-binary', {
    transform: 'binary',
  });
  console.log(binary);
};

```

#### Partial transform failures with `getMultiple()`

If you use `transform` with `getMultiple()`, you can have a single malformed parameter value. To prevent failing the entire request, the method will return an `undefined` value for the parameters that failed to transform.

You can override this by setting the `throwOnTransformError` argument to `true`. If you do so, a single transform error will throw a **`TransformParameterError`** error.

For example, if you have three parameters, */param/a*, */param/b* and */param/c*, but */param/c* is malformed:

```
import { SSMProvider } from '@aws-lambda-powertools/parameters/ssm';

const parametersProvider = new SSMProvider();

export const handler = async (): Promise<void> => {
  /**
   * This will display:
   * /param/a: [some value]
   * /param/b: [some value]
   * /param/c: undefined
   */
  const parameters = await parametersProvider.getMultiple('/param', {
    transform: 'json',
  });
  for (const [key, value] of Object.entries(parameters || {})) {
    console.log(`${key}: ${value}`);
  }

  try {
    // This will throw a TransformParameterError
    const parameters2 = await parametersProvider.getMultiple('/param', {
      transform: 'json',
      throwOnTransformError: true,
    });
    for (const [key, value] of Object.entries(parameters2 || {})) {
      console.log(`${key}: ${value}`);
    }
  } catch (err) {
    console.error(err);
  }
};

```

#### Auto-transform values on suffix

If you use `transform` with `getMultiple()`, you might want to retrieve and transform parameters encoded in different formats.

You can do this with a single request by using `transform: 'auto'`. This will instruct any provider to infer its type based on the suffix and transform it accordingly.

Info

`transform: 'auto'` feature is available across all providers, including the high level functions.

```
import { SSMProvider } from '@aws-lambda-powertools/parameters/ssm';

const parametersProvider = new SSMProvider();

export const handler = async (): Promise<void> => {
  const values = await parametersProvider.getMultiple('/param', {
    transform: 'auto',
  });
  for (const [key, value] of Object.entries(values || {})) {
    console.log(`${key}: ${value}`);
  }
};

```

For example, if you have three parameters: two with the following suffixes `.json` and `.binary` and one without any suffix:

| Parameter name  | Parameter value      |
| --------------- | -------------------- |
| /param/a        | [some encoded value] |
| /param/a.json   | [some encoded value] |
| /param/a.binary | [some encoded value] |

The return of `await parametersProvider.getMultiple('/param', transform: 'auto');` call will be an object like:

```
{
  "a": [some encoded value],
  "a.json": [some decoded value],
  "b.binary": [some decoded value]
}

```

The two parameters with a suffix will be decoded, while the one without a suffix will be returned as is.

### Passing additional SDK arguments

You can use a special `sdkOptions` object argument to pass any supported option directly to the underlying SDK method.

```
import { SecretsProvider } from '@aws-lambda-powertools/parameters/secrets';
import type { GetSecretValueCommandInput } from '@aws-sdk/client-secrets-manager';

const secretsProvider = new SecretsProvider();

export const handler = async (): Promise<void> => {
  const sdkOptions: Partial<GetSecretValueCommandInput> = {
    VersionId: 'e62ec170-6b01-48c7-94f3-d7497851a8d2',
  };
  /**
   * The 'VersionId' argument will be passed to the underlying
   * `GetSecretValueCommand` call.
   */
  const secret = await secretsProvider.get('my-secret', { sdkOptions });
  console.log(secret);
};

```

Here is the mapping between this utility's functions and methods and the underlying SDK:

| Provider            | Function/Method                | Client name                       | Function name                                                                                                                                                                                                                                                                                                   |
| ------------------- | ------------------------------ | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSM Parameter Store | `getParameter`                 | `@aws-sdk/client-ssm`             | [GetParameterCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/ssm/command/GetParameterCommand/)                                                                                                                                                                                           |
| SSM Parameter Store | `getParameters`                | `@aws-sdk/client-ssm`             | [GetParametersByPathCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/ssm/command/GetParametersByPathCommand/)                                                                                                                                                                             |
| SSM Parameter Store | `SSMProvider.get`              | `@aws-sdk/client-ssm`             | [GetParameterCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/ssm/command/GetParameterCommand/)                                                                                                                                                                                           |
| SSM Parameter Store | `SSMProvider.getMultiple`      | `@aws-sdk/client-ssm`             | [GetParametersByPathCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/ssm/command/GetParametersByPathCommand)                                                                                                                                                                              |
| SSM Parameter Store | `setParameter`                 | `@aws-sdk/client-ssm`             | [PutParameterCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/ssm/command/PutParameterCommand/)                                                                                                                                                                                           |
| SSM Parameter Store | `SSMProvider.set`              | `@aws-sdk/client-ssm`             | [PutParameterCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/ssm/command/PutParameterCommand/)                                                                                                                                                                                           |
| Secrets Manager     | `getSecret`                    | `@aws-sdk/client-secrets-manager` | [GetSecretValueCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/secrets-manager/command/GetSecretValueCommand/)                                                                                                                                                                           |
| Secrets Manager     | `SecretsProvider.get`          | `@aws-sdk/client-secrets-manager` | [GetSecretValueCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/secrets-manager/command/GetSecretValueCommand/)                                                                                                                                                                           |
| AppConfig           | `AppConfigProvider.get`        | `@aws-sdk/client-appconfigdata`   | [StartConfigurationSessionCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/appconfigdata/command/StartConfigurationSessionCommand/) & [GetLatestConfigurationCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/appconfigdata/command/GetLatestConfigurationCommand/) |
| AppConfig           | `getAppConfig`                 | `@aws-sdk/client-appconfigdata`   | [StartConfigurationSessionCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/appconfigdata/command/StartConfigurationSessionCommand/) & [GetLatestConfigurationCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/appconfigdata/command/GetLatestConfigurationCommand/) |
| DynamoDB            | `DynamoDBProvider.get`         | `@aws-sdk/client-dynamodb`        | [GetItemCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/dynamodb/command/GetItemCommand/)                                                                                                                                                                                                |
| DynamoDB            | `DynamoDBProvider.getMultiple` | `@aws-sdk/client-dynamodb`        | [QueryCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/dynamodb/command/QueryCommand/)                                                                                                                                                                                                    |

### Bring your own AWS SDK v3 client

You can use the `awsSdkV3Client` parameter via any of the available [Provider Classes](#built-in-provider-class).

| Provider                                | Client                        |
| --------------------------------------- | ----------------------------- |
| [SSMProvider](#ssmprovider)             | `new SSMClient();`            |
| [SecretsProvider](#secretsprovider)     | `new SecretsManagerClient();` |
| [AppConfigProvider](#appconfigprovider) | `new AppConfigDataClient();`  |
| [DynamoDBProvider](#dynamodbprovider)   | `new DynamoDBClient();`       |

When is this useful?

Injecting a custom AWS SDK v3 client allows you to [apply tracing](https://docs.aws.amazon.com/powertools/typescript/latest/features/tracer/#patching-aws-sdk-clients) or make unit/snapshot testing easier, including SDK customizations.

```
import { SSMProvider } from '@aws-lambda-powertools/parameters/ssm';
import { SSMClient } from '@aws-sdk/client-ssm';

// construct your clients with any custom configuration
const ssmClient = new SSMClient({ region: 'us-east-1' });
// pass the client to the provider
const parametersProvider = new SSMProvider({ awsSdkV3Client: ssmClient });

export const handler = async (): Promise<void> => {
  // Retrieve a single parameter
  const parameter = await parametersProvider.get('/my/parameter');
  console.log(parameter);
};

```

```
import { SecretsProvider } from '@aws-lambda-powertools/parameters/secrets';
import { SecretsManagerClient } from '@aws-sdk/client-secrets-manager';

// construct your clients with any custom configuration
const secretsManagerClient = new SecretsManagerClient({ region: 'us-east-1' });
// pass the client to the provider
const secretsProvider = new SecretsProvider({
  awsSdkV3Client: secretsManagerClient,
});

export const handler = async (): Promise<void> => {
  // Retrieve a single secret
  const secret = await secretsProvider.get('my-secret');
  console.log(secret);
};

```

```
import { AppConfigProvider } from '@aws-lambda-powertools/parameters/appconfig';
import { AppConfigDataClient } from '@aws-sdk/client-appconfigdata';

// construct your clients with any custom configuration
const appConfigClient = new AppConfigDataClient({ region: 'us-east-1' });
// pass the client to the provider
const configsProvider = new AppConfigProvider({
  application: 'my-app',
  environment: 'my-env',
  awsSdkV3Client: appConfigClient,
});

export const handler = async (): Promise<void> => {
  const config = await configsProvider.get('my-config');
  console.log(config);
};

```

```
import { DynamoDBProvider } from '@aws-lambda-powertools/parameters/dynamodb';
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';

// construct your clients with any custom configuration
const dynamoDBClient = new DynamoDBClient({ region: 'us-east-1' });
// pass the client to the provider
const valuesProvider = new DynamoDBProvider({
  tableName: 'my-table',
  awsSdkV3Client: dynamoDBClient,
});

export const handler = async (): Promise<void> => {
  // Retrieve a single value
  const value = await valuesProvider.get('my-value');
  console.log(value);
};

```

### Customizing AWS SDK v3 configuration

The **`clientConfig`** parameter enables you to pass in a custom [config object](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/configuring-the-jssdk.html) when constructing any of the built-in provider classes.

Tip

You can use a custom session for retrieving parameters cross-account/region and for snapshot testing.

When using VPC private endpoints, you can pass a custom client altogether. It's also useful for testing when injecting fake instances.

```
import { SSMProvider } from '@aws-lambda-powertools/parameters/ssm';
import type { SSMClientConfig } from '@aws-sdk/client-ssm';

const clientConfig: SSMClientConfig = { region: 'us-east-1' };
const parametersProvider = new SSMProvider({ clientConfig });

export const handler = async (): Promise<void> => {
  // Retrieve a single parameter
  const value = await parametersProvider.get('/my/parameter');
  console.log(value);
};

```

## Testing your code

### Mocking parameter values

For unit testing your applications, you can mock the calls to the parameters utility to avoid calling AWS APIs. This can be achieved in a number of ways - in this example, we mock the module import to patch the `getParameters` function.

```
import { afterEach, describe, expect, it, vi } from 'vitest';
import { handler } from './testingYourCodeFunctionsHandler.js';

const mocks = vi.hoisted(() => ({
  getParameter: vi.fn(),
}));

vi.mock('@aws-lambda-powertools/parameters/ssm', async (importOriginal) => ({
  ...(await importOriginal<
    typeof import('@aws-lambda-powertools/parameters/ssm')
  >()),
  getParameter: mocks.getParameter,
}));

describe('Function tests', () => {
  afterEach(() => {
    vi.clearAllMocks();
  });

  it('returns the correct response', async () => {
    // Prepare
    mocks.getParameter.mockResolvedValueOnce('my/param');

    // Act
    const result = await handler({}, {});

    // Assess
    expect(result).toEqual({
      value: 'my/param',
    });
  });
});

```

```
import { getParameter } from '@aws-lambda-powertools/parameters/ssm';

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<Record<string, unknown>> => {
  const parameter = await getParameter('my/param');

  return {
    value: parameter,
  };
};

```

With this pattern in place, you can customize the return values of the mocked function to test different scenarios without calling AWS APIs.

A similar pattern can be applied also to any of the built-in provider classes - in this other example, we use spies to patch the `get` function of the `AppConfigProvider` class. This is useful also when you want to test that the correct arguments are being passed to the Parameters utility.

```
import { AppConfigProvider } from '@aws-lambda-powertools/parameters/appconfig';
import { Uint8ArrayBlobAdapter } from '@smithy/util-stream';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { handler } from './testingYourCodeFunctionsHandler.js';

describe('Function tests', () => {
  const providerSpy = vi.spyOn(AppConfigProvider.prototype, 'get');

  afterEach(() => {
    vi.clearAllMocks();
  });

  it('retrieves the config once and uses the correct name', async () => {
    // Prepare
    const expectedConfig = {
      feature: {
        enabled: true,
        name: 'paywall',
      },
    };
    providerSpy.mockResolvedValueOnce(
      Uint8ArrayBlobAdapter.fromString(JSON.stringify(expectedConfig))
    );

    // Act
    const result = await handler({}, {});

    // Assess
    expect(result).toStrictEqual({ value: expectedConfig });
    expect(providerSpy).toHaveBeenCalledTimes(1);
    expect(providerSpy).toHaveBeenCalledWith('my-config');
  });
});

```

```
import { AppConfigProvider } from '@aws-lambda-powertools/parameters/appconfig';

const provider = new AppConfigProvider({
  environment: 'dev',
  application: 'my-app',
});

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<Record<string, unknown>> => {
  const config = await provider.get('my-config');

  return {
    value: config,
  };
};

```

For when you want to mock the AWS SDK v3 client directly, we recommend using the [`aws-sdk-client-mock`](https://www.npmjs.com/package/aws-sdk-client-mock) and [`aws-sdk-client-mock-vitest`](https://www.npmjs.com/package/aws-sdk-client-mock-vitest) libraries. This is useful when you want to test how your code behaves when the AWS SDK v3 client throws an error or a specific response.

```
import {
  GetSecretValueCommand,
  ResourceNotFoundException,
  SecretsManagerClient,
} from '@aws-sdk/client-secrets-manager';
import { mockClient } from 'aws-sdk-client-mock';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { handler } from './testingYourCodeFunctionsHandler.js';
import 'aws-sdk-client-mock-vitest';

describe('Function tests', () => {
  const client = mockClient(SecretsManagerClient);

  afterEach(() => {
    vi.clearAllMocks();
    client.reset();
  });

  it('returns the correct error message', async () => {
    // Prepare
    client.on(GetSecretValueCommand).rejectsOnce(
      new ResourceNotFoundException({
        $metadata: {
          httpStatusCode: 404,
        },
        message: 'Unable to retrieve secret',
      })
    );

    // Act
    const result = await handler({}, {});

    // Assess
    expect(result).toStrictEqual({ message: 'Unable to retrieve secret' });
  });
});

```

```
import { getSecret } from '@aws-lambda-powertools/parameters/secrets';

export const handler = async (
  _event: unknown,
  _context: unknown
): Promise<Record<string, unknown>> => {
  try {
    const parameter = await getSecret('my-secret');

    return {
      value: parameter,
    };
  } catch (error) {
    console.error('Unable to retrieve secret: ', error);
    return {
      message: 'Unable to retrieve secret',
    };
  }
};

```

### Clearing cache

Parameters utility caches all parameter values for performance and cost reasons. However, this can have unintended interference in tests using the same parameter name.

Within your tests, you can use `clearCache` method available in [every provider](#built-in-provider-class). When using multiple providers or higher level functions like `getParameter`, use the `clearCaches` standalone function to clear cache globally.

```
import { clearCaches } from '@aws-lambda-powertools/parameters';
import { afterEach, describe } from 'vitest';

describe('Function tests', () => {
  afterEach(() => {
    clearCaches();
  });

  // ...
});

```

The idempotency utility provides a simple solution to convert your Lambda functions into idempotent operations which are safe to retry.

## Key features

- Prevent Lambda handler from executing more than once on the same event payload during a time window
- Ensure Lambda handler returns the same result when called with the same payload
- Select a subset of the event as the idempotency key using JMESPath expressions
- Set a time window in which records with the same payload should be considered duplicates
- Expires in-progress executions if the Lambda function times out halfway through
- Support for Amazon DynamoDB, Valkey, Redis OSS, or any Redis-compatible cache as the persistence layer

## Terminology

The property of idempotency means that an operation does not cause additional side effects if it is called more than once with the same input parameters.

**Idempotent operations will return the same result when they are called multiple times with the same parameters**. This makes idempotent operations safe to retry.

**Idempotency key** is a hash representation of either the entire event or a specific configured subset of the event, and invocation results are **JSON serialized** and stored in your persistence storage layer.

**Idempotency record** is the data representation of an idempotent request saved in your preferred storage layer. We use it to coordinate whether a request is idempotent, whether it's still valid or expired based on timestamps, etc.

```
classDiagram
    direction LR
    class IdempotencyRecord {
        idempotencyKey string
        status Status
        expiryTimestamp number
        inProgressExpiryTimestamp number
        responseData Json~string~
        payloadHash string
    }
    class Status {
        <<Enumeration>>
        INPROGRESS
        COMPLETE
        EXPIRED internal_only
    }
    IdempotencyRecord -- Status
```

*Idempotency record representation*

## Getting started

Tip

Throughout the documentation we use Amazon DynamoDB as the default persistence layer. If you prefer to use a cache based persistence layer, you can learn more in the [cache database](#cache-database) and [`CachePersistenceLayer`](#cachepersistencelayer) sections.

### Amazon DynamoDB

```
npm i @aws-lambda-powertools/idempotency @aws-sdk/client-dynamodb @aws-sdk/lib-dynamodb

```

#### IAM Permissions

Your Lambda function IAM Role must have `dynamodb:GetItem`, `dynamodb:PutItem`, `dynamodb:UpdateItem` and `dynamodb:DeleteItem` IAM permissions before using this feature. If you're using one of our examples below the required permissions are already included.

#### Table configuration

Unless you're looking to use an [existing table or customize each attribute](#dynamodbpersistencelayer), you only need the following:

| Configuration      | Default value | Notes                                                                                  |
| ------------------ | ------------- | -------------------------------------------------------------------------------------- |
| Partition key      | `id`          | The id of each idempotency record which a combination of `functionName#hashOfPayload`. |
| TTL attribute name | `expiration`  | This can only be configured after your table is created if you're using AWS Console.   |

You **can** use a single DynamoDB table for all functions using this utility. We use the function name in addition to the idempotency key as a hash key.

```
import { Stack, type StackProps } from 'aws-cdk-lib';
import { AttributeType, BillingMode, Table } from 'aws-cdk-lib/aws-dynamodb';
import { Runtime } from 'aws-cdk-lib/aws-lambda';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import type { Construct } from 'constructs';

export class IdempotencyStack extends Stack {
  public constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const table = new Table(this, 'idempotencyTable', {
      partitionKey: {
        name: 'id',
        type: AttributeType.STRING,
      },
      timeToLiveAttribute: 'expiration',
      billingMode: BillingMode.PAY_PER_REQUEST,
    });

    const fnHandler = new NodejsFunction(this, 'helloWorldFunction', {
      runtime: Runtime.NODEJS_20_X,
      handler: 'handler',
      entry: 'src/index.ts',
      environment: {
        IDEMPOTENCY_TABLE_NAME: table.tableName,
      },
    });
    table.grantReadWriteData(fnHandler);
  }
}

```

```
Transform: AWS::Serverless-2016-10-31
Resources:
  IdempotencyTable:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      TimeToLiveSpecification:
        AttributeName: expiration
        Enabled: true
      BillingMode: PAY_PER_REQUEST

  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      Runtime: nodejs24.x
      Handler: index.js
      Policies:
        - Statement:
            - Sid: AllowDynamodbReadWrite
              Effect: Allow
              Action:
                - dynamodb:PutItem
                - dynamodb:GetItem
                - dynamodb:UpdateItem
                - dynamodb:DeleteItem
              Resource: !GetAtt IdempotencyTable.Arn

```

```
terraform {
    required_providers {
        aws = {
        source  = "hashicorp/aws"
        version = "~> 4.0"
        }
    }
}

provider "aws" {
    region = "us-east-1" # Replace with your desired AWS region
}

resource "aws_dynamodb_table" "IdempotencyTable" {
    name         = "IdempotencyTable"
    billing_mode = "PAY_PER_REQUEST"
    hash_key     = "id"
    attribute {
        name = "id"
        type = "S"
    }
    ttl {
        attribute_name = "expiration"
        enabled        = true
    }
}

resource "aws_lambda_function" "IdempotencyFunction" {
    function_name = "IdempotencyFunction"
    role          = aws_iam_role.IdempotencyFunctionRole.arn
    runtime       = "nodejs20.x"
    handler       = "index.handler"
    filename      = "lambda.zip"
}

resource "aws_iam_role" "IdempotencyFunctionRole" {
    name = "IdempotencyFunctionRole"

    assume_role_policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
        {
            Sid    = ""
            Effect = "Allow"
            Principal = {
            Service = "lambda.amazonaws.com"
            }
            Action = "sts:AssumeRole"
        },
        ]
    })
}

resource "aws_iam_policy" "LambdaDynamoDBPolicy" {
    name        = "LambdaDynamoDBPolicy"
    description = "IAM policy for Lambda function to access DynamoDB"
    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
        {
            Sid    = "AllowDynamodbReadWrite"
            Effect = "Allow"
            Action = [
            "dynamodb:PutItem",
            "dynamodb:GetItem",
            "dynamodb:UpdateItem",
            "dynamodb:DeleteItem",
            ]
            Resource = aws_dynamodb_table.IdempotencyTable.arn
        },
        ]
    })
}

resource "aws_iam_role_policy_attachment" "IdempotencyFunctionRoleAttachment" {
    role       = aws_iam_role.IdempotencyFunctionRole.name
    policy_arn = aws_iam_policy.LambdaDynamoDBPolicy.arn
}

```

##### Limitations

- **DynamoDB restricts [item sizes to 400KB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html#limits-items)**. This means that your idempotent function's response must be smaller than 400KB, otherwise your function will fail. Consider using the [cache persistence layer](#cache-database) if you need to store larger responses.
- **Expect 2 WCUs per non-idempotent call**. During the first invocation, we use `PutItem` for locking and `UpdateItem` for completion. Consider reviewing [DynamoDB pricing documentation](https://aws.amazon.com/dynamodb/pricing/) to estimate cost.
- **Expect 1 RCU per idempotent calls**. On subsequent invocations, we use `PutItem` to optimistically attempt to lock the record using `ConditionExpression` and `ReturnValuesOnConditionCheckFailure` to return the record if it exists. This is a single read operation.

### Cache database

Depending on the persistence layer you want to use, install the library and the corresponding peer dependencies.

```
npm i @aws-lambda-powertools/idempotency @valkey/valkey-glide

```

```
npm i @aws-lambda-powertools/idempotency @redis/client

```

We recommend starting with a managed cache service, such as [Amazon ElastiCache for Valkey and for Redis OSS](https://aws.amazon.com/elasticache/redis/) or [Amazon MemoryDB](https://aws.amazon.com/memorydb/).

In both services, you'll need to configure [VPC access](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html) to your AWS Lambda and permissions for writing and reading from the cache.

#### Cache configuration

```
import { Duration, RemovalPolicy, Stack, type StackProps } from 'aws-cdk-lib';
import { Port, SecurityGroup, Vpc } from 'aws-cdk-lib/aws-ec2';
import { CfnServerlessCache } from 'aws-cdk-lib/aws-elasticache';
import {
  Architecture,
  Code,
  LayerVersion,
  Runtime,
} from 'aws-cdk-lib/aws-lambda';
import { NodejsFunction, OutputFormat } from 'aws-cdk-lib/aws-lambda-nodejs';
import { LogGroup, RetentionDays } from 'aws-cdk-lib/aws-logs';
import type { Construct } from 'constructs';

export class ValkeyStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const vpc = Vpc.fromLookup(this, 'MyVpc', {
      vpcId: 'vpc-{your_vpc_id}', // (1)!
    });

    const fnSecurityGroup = new SecurityGroup(this, 'ValkeyFnSecurityGroup', {
      vpc,
      allowAllOutbound: true,
      description: 'Security group for Valkey function',
    });

    const idempotencyCacheSG = SecurityGroup.fromSecurityGroupId(
      this,
      'IdempotencyCacheSG',
      'security-{your_sg_id}' // (2)!
    );
    idempotencyCacheSG.addIngressRule(
      fnSecurityGroup,
      Port.tcp(6379),
      'Allow Lambda to connect to serverless cache'
    );

    const serverlessCache = new CfnServerlessCache(
      this,
      'MyCfnServerlessCache',
      {
        engine: 'valkey', // (3)!
        majorEngineVersion: '8',
        serverlessCacheName: 'idempotency-cache',
        subnetIds: [
          vpc.privateSubnets[0].subnetId,
          vpc.privateSubnets[1].subnetId,
        ],
        securityGroupIds: [idempotencyCacheSG.securityGroupId],
      }
    );

    const valkeyLayer = new LayerVersion(this, 'ValkeyLayer', {
      removalPolicy: RemovalPolicy.DESTROY,
      compatibleArchitectures: [Architecture.ARM_64],
      compatibleRuntimes: [Runtime.NODEJS_22_X, Runtime.NODEJS_24_X],
      code: Code.fromAsset('./lib/layers/valkey-glide'),
    });

    const fnName = 'ValkeyFn';
    const logGroup = new LogGroup(this, 'MyLogGroup', {
      logGroupName: `/aws/lambda/${fnName}`,
      removalPolicy: RemovalPolicy.DESTROY,
      retention: RetentionDays.ONE_DAY,
    });
    const fn = new NodejsFunction(this, 'MyFunction', {
      functionName: fnName,
      logGroup,
      runtime: Runtime.NODEJS_24_X,
      architecture: Architecture.ARM_64,
      memorySize: 512,
      timeout: Duration.seconds(30),
      entry: './src/idempotency.ts',
      handler: 'handler',
      layers: [valkeyLayer],
      bundling: {
        minify: true,
        mainFields: ['module', 'main'],
        sourceMap: true,
        format: OutputFormat.ESM,
        externalModules: ['@valkey/valkey-glide'],
        metafile: true,
        banner:
          "import { createRequire } from 'module';const require = createRequire(import.meta.url);",
      },
      vpc,
      securityGroups: [fnSecurityGroup],
    });
    fn.addEnvironment(
      'CACHE_ENDPOINT',
      serverlessCache.getAtt('Endpoint.Address').toString()
    );
    fn.addEnvironment(
      'CACHE_PORT',
      serverlessCache.getAtt('Endpoint.Port').toString()
    );
  }
}

```

1. Replace the VPC ID to match your VPC settings.
1. Replace the Security Group ID to match your VPC settings.
1. You can use the same template for Redis OSS, just replace the engine to `redis`.

```
AWSTemplateFormatVersion: "2010-09-09"
Transform: AWS::Serverless-2016-10-31

Resources:
  CacheIdempotency:
    Type: AWS::ElastiCache::ServerlessCache
    Properties:
      Engine: valkey # (1)!
      ServerlessCacheName: idempotency-cache
      SecurityGroupIds: # (2)!
        - security-{your_sg_id}
      SubnetIds:
        - subnet-{your_subnet_id_1}
        - subnet-{your_subnet_id_2}

  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      Runtime: nodejs24.x
      Handler: index.js
      VpcConfig: # (3)!
        SecurityGroupIds:
          - security-{your_sg_id}
        SubnetIds:
          - subnet-{your_subnet_id_1}
          - subnet-{your_subnet_id_2}
      Environment:
        Variables:
          CACHE_ENDPOINT: !GetAtt CacheIdempotency.Endpoint.Address
          CACHE_PORT: !GetAtt CacheIdempotency.Endpoint.Port

```

1. You can use the same template for Redis OSS, just replace the engine to `redis`.
1. Replace the Security Group ID and Subnet ID to match your VPC settings.
1. Replace the Security Group ID and Subnet ID to match your VPC settings.

### MakeIdempotent function wrapper

You can quickly start by initializing the `DynamoDBPersistenceLayer` class and using it with the `makeIdempotent` function wrapper on your Lambda handler.

```
import { randomUUID } from 'node:crypto';
import { makeIdempotent } from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import type { Context } from 'aws-lambda';
import type { Request, Response, SubscriptionResult } from './types.js';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
});

const createSubscriptionPayment = async (
  event: Request
): Promise<SubscriptionResult> => {
  // ... create payment
  return {
    id: randomUUID(),
    productId: event.productId,
  };
};

export const handler = makeIdempotent(
  async (event: Request, _context: Context): Promise<Response> => {
    const payment = await createSubscriptionPayment(event);

    return {
      paymentId: payment.id,
      message: 'success',
      statusCode: 200,
    };
  },
  {
    persistenceStore,
  }
);

```

```
export type Request = {
  user: string;
  productId: string;
};

export type Response = {
  [key: string]: unknown;
};

export type SubscriptionResult = {
  id: string;
  productId: string;
};

```

After processing this request successfully, a second request containing the exact same payload above will now return the same response, ensuring our customer isn't charged twice.

Note

In this example, the entire Lambda handler is treated as a single idempotent operation. If your Lambda handler can cause multiple side effects, or you're only interested in making a specific logic idempotent, use the `makeIdempotent` high-order function only on the function that needs to be idempotent.

See [Choosing a payload subset for idempotency](#choosing-a-payload-subset-for-idempotency) for more elaborate use cases.

You can also use the `makeIdempotent` function wrapper on any method that returns a response to make it idempotent. This is useful when you want to make a specific logic idempotent, for example when your Lambda handler performs multiple side effects and you only want to make a specific one idempotent.

Limitation

Make sure to return a JSON serializable response from your function, otherwise you'll get an error.

When using `makeIdempotent` on arbitrary functions, you can tell us which argument in your function signature has the data we should use via **`dataIndexArgument`**. If you don't specify this argument, we'll use the first argument in the function signature.

```
import { randomUUID } from 'node:crypto';
import {
  IdempotencyConfig,
  makeIdempotent,
} from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import type { Context } from 'aws-lambda';
import type { Request, Response, SubscriptionResult } from './types.js';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
});
const config = new IdempotencyConfig({});

const reportSubscriptionMetrics = async (
  _transactionId: string,
  _user: string
): Promise<void> => {
  // ... send notification
};

const createSubscriptionPayment = makeIdempotent(
  async (
    transactionId: string,
    event: Request
  ): Promise<SubscriptionResult> => {
    // ... create payment
    return {
      id: transactionId,
      productId: event.productId,
    };
  },
  {
    persistenceStore,
    dataIndexArgument: 1,
    config,
  }
);

export const handler = async (
  event: Request,
  context: Context
): Promise<Response> => {
  config.registerLambdaContext(context);

  const transactionId = randomUUID();
  const payment = await createSubscriptionPayment(transactionId, event);

  await reportSubscriptionMetrics(transactionId, event.user);

  return {
    paymentId: payment.id,
    message: 'success',
    statusCode: 200,
  };
};

```

```
export type Request = {
  user: string;
  productId: string;
};

export type Response = {
  [key: string]: unknown;
};

export type SubscriptionResult = {
  id: string;
  productId: string;
};

```

The function this example has two arguments, note that while wrapping it with the `makeIdempotent` high-order function, we specify the `dataIndexArgument` as `1` to tell the decorator that the second argument is the one with the data we should use to make the function idempotent. Remember that arguments are zero-indexed, so the first argument is `0`, the second is `1`, etc.

### Idempotent Decorator

You can also use the `@idempotent` decorator to make your Lambda handler idempotent, similar to the `makeIdempotent` function wrapper.

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import {
  IdempotencyConfig,
  idempotent,
} from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import type { Context } from 'aws-lambda';
import type { Request, Response } from './types.js';

const dynamoDBPersistenceLayer = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
});

const config = new IdempotencyConfig({});

class MyLambda implements LambdaInterface {
  @idempotent({ persistenceStore: dynamoDBPersistenceLayer, config: config })
  public async handler(_event: Request, _context: Context): Promise<Response> {
    // ... process your event
    return {
      message: 'success',
      statusCode: 200,
    };
  }
}

const defaultLambda = new MyLambda();
export const handler = defaultLambda.handler.bind(defaultLambda);

```

```
import type { IdempotencyRecordStatusValue } from '@aws-lambda-powertools/idempotency/types';

export type Request = {
  user: string;
  productId: string;
};

export type Response = {
  [key: string]: unknown;
};

export type SubscriptionResult = {
  id: string;
  productId: string;
};

export type ApiSecret = {
  apiKey: string;
  refreshToken: string;
  validUntil: number;
  restEndpoint: string;
};

export type ProviderItem = {
  validation?: string;
  in_progress_expiration?: number;
  status: IdempotencyRecordStatusValue;
  data: string;
};

```

### MakeHandlerIdempotent Middy middleware

If you are using [Middy.js](https://middy.js.org) as your middleware engine, you can use the `makeHandlerIdempotent` middleware to make your Lambda handler idempotent.

Similar to the `makeIdempotent` function wrapper, you can quickly make your Lambda handler idempotent by initializing the `DynamoDBPersistenceLayer` class and using it with the `makeHandlerIdempotent` middleware.

```
import { randomUUID } from 'node:crypto';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import { makeHandlerIdempotent } from '@aws-lambda-powertools/idempotency/middleware';
import middy from '@middy/core';
import type { Context } from 'aws-lambda';
import type { Request, Response, SubscriptionResult } from './types.js';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
});

const createSubscriptionPayment = async (
  event: Request
): Promise<SubscriptionResult> => {
  // ... create payment
  return {
    id: randomUUID(),
    productId: event.productId,
  };
};

export const handler = middy(
  async (event: Request, _context: Context): Promise<Response> => {
    const payment = await createSubscriptionPayment(event);

    return {
      paymentId: payment.id,
      message: 'success',
      statusCode: 200,
    };
  }
).use(
  makeHandlerIdempotent({
    persistenceStore,
  })
);

```

```
export type Request = {
  user: string;
  productId: string;
};

export type Response = {
  [key: string]: unknown;
};

export type SubscriptionResult = {
  id: string;
  productId: string;
};

```

For the middleware to work, your Lambda function handler must return a value different from `undefined`. This is a [known limitation of the early return feature in Middy.js](https://github.com/middyjs/middy/issues/1236). If your use case requires early returns, you can use the `makeIdempotent` function wrapper instead.

### Choosing a payload subset for idempotency

Use [`IdempotencyConfig`](#customizing-the-default-behavior) to instruct the idempotent decorator to only use a portion of your payload to verify whether a request is idempotent, and therefore it should not be retried. When dealing with a more elaborate payload, where parts of the payload always change, you should use the **`eventKeyJmesPath`** parameter.

**Payment scenario**

In this example, we have a Lambda handler that creates a payment for a user subscribing to a product. We want to ensure that we don't accidentally charge our customer by subscribing them more than once.

Imagine the function executes successfully, but the client never receives the response due to a connection issue. It is safe to retry in this instance, as the idempotent decorator will return a previously saved response.

**What we want here** is to instruct Idempotency to use the `user` and `productId` fields from our incoming payload as our idempotency key. If we were to treat the entire request as our idempotency key, a simple HTTP header or timestamp change would cause our customer to be charged twice.

Deserializing JSON strings in payloads for increased accuracy.

The payload extracted by the `eventKeyJmesPath` is treated as a string by default. This means there could be differences in whitespace even when the JSON payload itself is identical.

To alter this behaviour, we can use the [JMESPath built-in function `powertools_json()`](https://docs.aws.amazon.com/powertools/typescript/latest/features/jmespath/#powertools_json-function) to treat the payload as a JSON object rather than a string.

```
import { randomUUID } from 'node:crypto';
import {
  IdempotencyConfig,
  makeIdempotent,
} from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import type { Context } from 'aws-lambda';
import type { Request, Response, SubscriptionResult } from './types.js';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
});

const createSubscriptionPayment = async (
  _user: string,
  productId: string
): Promise<SubscriptionResult> => {
  // ... create payment
  return {
    id: randomUUID(),
    productId: productId,
  };
};

// Deserialize JSON string under the "body" key, then extract the "user" and "productId" keys
const config = new IdempotencyConfig({
  eventKeyJmesPath: 'powertools_json(body).["user", "productId"]',
});

export const handler = makeIdempotent(
  async (event: Request, _context: Context): Promise<Response> => {
    const payment = await createSubscriptionPayment(
      event.user,
      event.productId
    );

    return {
      paymentId: payment.id,
      message: 'success',
      statusCode: 200,
    };
  },
  {
    persistenceStore,
    config,
  }
);

```

```
{
  "version": "2.0",
  "routeKey": "ANY /createpayment",
  "rawPath": "/createpayment",
  "rawQueryString": "",
  "headers": {
    "Header1": "value1",
    "X-Idempotency-Key": "abcdefg"
  },
  "requestContext": {
    "accountId": "123456789012",
    "apiId": "api-id",
    "domainName": "id.execute-api.us-east-1.amazonaws.com",
    "domainPrefix": "id",
    "http": {
      "method": "POST",
      "path": "/createpayment",
      "protocol": "HTTP/1.1",
      "sourceIp": "ip",
      "userAgent": "agent"
    },
    "requestId": "id",
    "routeKey": "ANY /createpayment",
    "stage": "$default",
    "time": "10/Feb/2021:13:40:43 +0000",
    "timeEpoch": 1612964443723
  },
  "body": "{\"user\":\"xyz\",\"productId\":\"123456789\"}",
  "isBase64Encoded": false
}

```

```
export type Request = {
  user: string;
  productId: string;
};

export type Response = {
  [key: string]: unknown;
};

export type SubscriptionResult = {
  id: string;
  productId: string;
};

```

### Lambda timeouts

To prevent against extended failed retries when a [Lambda function times out](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-verify-invocation-timeouts/), Powertools for AWS Lambda calculates and includes the remaining invocation available time as part of the idempotency record. This is automatically done when you wrap your Lambda handler with the [makeIdempotent](#makeidempotent-function-wrapper) function wrapper, or use the [`makeHandlerIdempotent`](#makehandleridempotent-middy-middleware) Middy middleware.

Example

If a second invocation happens **after** this timestamp, and the record is marked as `INPROGRESS`, we will execute the invocation again as if it was in the `EXPIRED` state (e.g, `expire_seconds` field elapsed).

This means that if an invocation expired during execution, it will be quickly executed again on the next retry.

Important

If you are only using the [makeIdempotent function wrapper](#makeidempotent-function-wrapper) to guard isolated parts of your code outside of your handler, you must use `registerLambdaContext` available in the [idempotency config object](#customizing-the-default-behavior) to benefit from this protection.

Here is an example on how you register the Lambda context in your handler:

```
import { randomUUID } from 'node:crypto';
import {
  IdempotencyConfig,
  makeIdempotent,
} from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import type { Context } from 'aws-lambda';
import type { Request, Response, SubscriptionResult } from './types.js';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
});
const config = new IdempotencyConfig({});

const createSubscriptionPayment = makeIdempotent(
  async (
    transactionId: string,
    event: Request
  ): Promise<SubscriptionResult> => {
    // ... create payment
    return {
      id: transactionId,
      productId: event.productId,
    };
  },
  {
    persistenceStore,
    dataIndexArgument: 1,
    config,
  }
);

export const handler = async (
  event: Request,
  context: Context
): Promise<Response> => {
  // Register the Lambda context to the IdempotencyConfig instance
  config.registerLambdaContext(context);

  const transactionId = randomUUID();
  const payment = await createSubscriptionPayment(transactionId, event);

  return {
    paymentId: payment.id,
    message: 'success',
    statusCode: 200,
  };
};

```

### Handling exceptions

If you are making on your entire Lambda handler idempotent, any unhandled exceptions that are raised during the code execution will cause **the record in the persistence layer to be deleted**. This means that new invocations will execute your code again despite having the same payload. If you don't want the record to be deleted, you need to catch exceptions within the idempotent function and return a successful response.

```
sequenceDiagram
    autonumber
    participant Client
    participant Lambda
    participant Persistence Layer
    Client->>Lambda: Invoke (event)
    Lambda->>Persistence Layer: Get or set (id=event.search(payload))
    activate Persistence Layer
    Note right of Persistence Layer: Locked during this time. Prevents multiple<br/>Lambda invocations with the same<br/>payload running concurrently.
    Lambda--xLambda: Call handler (event).<br/>Raises exception
    Lambda->>Persistence Layer: Delete record (id=event.search(payload))
    deactivate Persistence Layer
    Lambda-->>Client: Return error response
```

*Idempotent sequence exception*

If you are using `makeIdempotent` on any other function, any unhandled exceptions that are thrown *inside* the wrapped function will cause the record in the persistence layer to be deleted, and allow the function to be executed again if retried.

If an error is thrown *outside* the scope of the decorated function and after your function has been called, the persistent record will not be affected. In this case, idempotency will be maintained for your decorated function. Example:

```
import { randomUUID } from 'node:crypto';
import {
  IdempotencyConfig,
  makeIdempotent,
} from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import type { Context } from 'aws-lambda';
import type { Request, Response, SubscriptionResult } from './types.js';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
});
const config = new IdempotencyConfig({});

const createSubscriptionPayment = makeIdempotent(
  async (
    transactionId: string,
    event: Request
  ): Promise<SubscriptionResult> => {
    // ... create payment
    return {
      id: transactionId,
      productId: event.productId,
    };
  },
  {
    persistenceStore,
    dataIndexArgument: 1,
    config,
  }
);

export const handler = async (
  event: Request,
  context: Context
): Promise<Response> => {
  config.registerLambdaContext(context);
  /**
   * If an exception is thrown before the wrapped function is called,
   * no idempotency record is created.
   */
  try {
    const transactionId = randomUUID();
    const payment = await createSubscriptionPayment(transactionId, event);

    /**
     * If an exception is thrown after the wrapped function is called,
     * the idempotency record won't be affected so it's safe to retry.
     */

    return {
      paymentId: payment.id,
      message: 'success',
      statusCode: 200,
    };
  } catch (error) {
    throw new Error('Error creating payment', { cause: error });
  }
};

```

Warning

**We will throw `IdempotencyPersistenceLayerError`** if any of the calls to the persistence layer fail unexpectedly.

As this happens outside the scope of your decorated function, you are not able to catch it when making your Lambda handler idempotent.

### Idempotency request flow

The following sequence diagrams explain how the Idempotency feature behaves under different scenarios.

#### Successful request

```
sequenceDiagram
    autonumber
    participant Client
    participant Lambda
    participant Persistence Layer
    alt initial request
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set idempotency_key=hash(payload)
        activate Persistence Layer
        Note over Lambda,Persistence Layer: Set record status to INPROGRESS. <br> Prevents concurrent invocations <br> with the same payload
        Lambda-->>Lambda: Call your function
        Lambda->>Persistence Layer: Update record with result
        deactivate Persistence Layer
        Persistence Layer-->>Persistence Layer: Update record
        Note over Lambda,Persistence Layer: Set record status to COMPLETE. <br> New invocations with the same payload <br> now return the same result
        Lambda-->>Client: Response sent to client
    else retried request
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set idempotency_key=hash(payload)
        activate Persistence Layer
        Persistence Layer-->>Lambda: Already exists in persistence layer.
        deactivate Persistence Layer
        Note over Lambda,Persistence Layer: Record status is COMPLETE and not expired
        Lambda-->>Client: Same response sent to client
    end
```

*Idempotent successful request*

#### Successful request with cache enabled

[In-memory cache is disabled by default](#using-in-memory-cache).

```
sequenceDiagram
    autonumber
    participant Client
    participant Lambda
    participant Persistence Layer
    alt initial request
      Client->>Lambda: Invoke (event)
      Lambda->>Persistence Layer: Get or set idempotency_key=hash(payload)
      activate Persistence Layer
      Note over Lambda,Persistence Layer: Set record status to INPROGRESS. <br> Prevents concurrent invocations <br> with the same payload
      Lambda-->>Lambda: Call your function
      Lambda->>Persistence Layer: Update record with result
      deactivate Persistence Layer
      Persistence Layer-->>Persistence Layer: Update record
      Note over Lambda,Persistence Layer: Set record status to COMPLETE. <br> New invocations with the same payload <br> now return the same result
      Lambda-->>Lambda: Save record and result in memory
      Lambda-->>Client: Response sent to client
    else retried request
      Client->>Lambda: Invoke (event)
      Lambda-->>Lambda: Get idempotency_key=hash(payload)
      Note over Lambda,Persistence Layer: Record status is COMPLETE and not expired
      Lambda-->>Client: Same response sent to client
    end
```

*Idempotent successful request cached*

#### Successful request with responseHook configured

```
sequenceDiagram
    participant Client
    participant Lambda
    participant Response hook
    participant Persistence Layer
    alt initial request
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set idempotency_key=hash(payload)
        activate Persistence Layer
        Note over Lambda,Persistence Layer: Set record status to INPROGRESS. <br> Prevents concurrent invocations <br> with the same payload
        Lambda-->>Lambda: Call your function
        Lambda->>Persistence Layer: Update record with result
        deactivate Persistence Layer
        Persistence Layer-->>Persistence Layer: Update record
        Note over Lambda,Persistence Layer: Set record status to COMPLETE. <br> New invocations with the same payload <br> now return the same result
        Lambda-->>Client: Response sent to client
    else retried request
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set idempotency_key=hash(payload)
        activate Persistence Layer
        Persistence Layer-->>Response hook: Already exists in persistence layer.
        deactivate Persistence Layer
        Note over Response hook,Persistence Layer: Record status is COMPLETE and not expired
        Response hook->>Lambda: Response hook invoked
        Lambda-->>Client: Manipulated idempotent response sent to client
    end
```

*Successful idempotent request with a response hook*

#### Expired idempotency records

```
sequenceDiagram
    autonumber
    participant Client
    participant Lambda
    participant Persistence Layer
    alt initial request
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set idempotency_key=hash(payload)
        activate Persistence Layer
        Note over Lambda,Persistence Layer: Set record status to INPROGRESS. <br> Prevents concurrent invocations <br> with the same payload
        Lambda-->>Lambda: Call your function
        Lambda->>Persistence Layer: Update record with result
        deactivate Persistence Layer
        Persistence Layer-->>Persistence Layer: Update record
        Note over Lambda,Persistence Layer: Set record status to COMPLETE. <br> New invocations with the same payload <br> now return the same result
        Lambda-->>Client: Response sent to client
    else retried request
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set idempotency_key=hash(payload)
        activate Persistence Layer
        Persistence Layer-->>Lambda: Already exists in persistence layer.
        deactivate Persistence Layer
        Note over Lambda,Persistence Layer: Record status is COMPLETE but expired hours ago
        loop Repeat initial request process
            Note over Lambda,Persistence Layer: 1. Set record to INPROGRESS, <br> 2. Call your function, <br> 3. Set record to COMPLETE
        end
        Lambda-->>Client: Same response sent to client
    end
```

*Previous Idempotent request expired*

#### Concurrent identical in-flight requests

```
sequenceDiagram
    autonumber
    participant Client
    participant Lambda
    participant Persistence Layer
    Client->>Lambda: Invoke (event)
    Lambda->>Persistence Layer: Get or set idempotency_key=hash(payload)
    activate Persistence Layer
    Note over Lambda,Persistence Layer: Set record status to INPROGRESS. <br> Prevents concurrent invocations <br> with the same payload
      par Second request
          Client->>Lambda: Invoke (event)
          Lambda->>Persistence Layer: Get or set idempotency_key=hash(payload)
          Lambda--xLambda: IdempotencyAlreadyInProgressError
          Lambda->>Client: Error sent to client if unhandled
      end
    Lambda-->>Lambda: Call your function
    Lambda->>Persistence Layer: Update record with result
    deactivate Persistence Layer
    Persistence Layer-->>Persistence Layer: Update record
    Note over Lambda,Persistence Layer: Set record status to COMPLETE. <br> New invocations with the same payload <br> now return the same result
    Lambda-->>Client: Response sent to client
```

*Concurrent identical in-flight requests*

#### Lambda request timeout

```
sequenceDiagram
    autonumber
    participant Client
    participant Lambda
    participant Persistence Layer
    alt initial request
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set idempotency_key=hash(payload)
        activate Persistence Layer
        Note over Lambda,Persistence Layer: Set record status to INPROGRESS. <br> Prevents concurrent invocations <br> with the same payload
        Lambda-->>Lambda: Call your function
        Note right of Lambda: Time out
        Lambda--xLambda: Time out error
        Lambda-->>Client: Return error response
        deactivate Persistence Layer
    else retry after Lambda timeout elapses
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set idempotency_key=hash(payload)
        activate Persistence Layer
        Note over Lambda,Persistence Layer: Set record status to INPROGRESS. <br> Reset in_progress_expiry attribute
        Lambda-->>Lambda: Call your function
        Lambda->>Persistence Layer: Update record with result
        deactivate Persistence Layer
        Persistence Layer-->>Persistence Layer: Update record
        Lambda-->>Client: Response sent to client
    end
```

*Idempotent request during and after Lambda timeouts*

#### Optional idempotency key

```
sequenceDiagram
    autonumber
    participant Client
    participant Lambda
    participant Persistence Layer
    alt request with idempotency key
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set idempotency_key=hash(payload)
        activate Persistence Layer
        Note over Lambda,Persistence Layer: Set record status to INPROGRESS. <br> Prevents concurrent invocations <br> with the same payload
        Lambda-->>Lambda: Call your function
        Lambda->>Persistence Layer: Update record with result
        deactivate Persistence Layer
        Persistence Layer-->>Persistence Layer: Update record
        Note over Lambda,Persistence Layer: Set record status to COMPLETE. <br> New invocations with the same payload <br> now return the same result
        Lambda-->>Client: Response sent to client
    else request(s) without idempotency key
        Client->>Lambda: Invoke (event)
        Note over Lambda: Idempotency key is missing
        Note over Persistence Layer: Skips any operation to fetch, update, and delete
        Lambda-->>Lambda: Call your function
        Lambda-->>Client: Response sent to client
    end
```

*Optional idempotency key*

#### Race condition with Cache

```
graph TD;
    A(Existing orphan record in cache)-->A1;
    A1[Two Lambda invoke at same time]-->B1[Lambda handler1];
    B1-->B2[Fetch from Cache];
    B2-->B3[Handler1 got orphan record];
    B3-->B4[Handler1 acquired lock];
    B4-->B5[Handler1 overwrite orphan record]
    B5-->B6[Handler1 continue to execution];
    A1-->C1[Lambda handler2];
    C1-->C2[Fetch from Cache];
    C2-->C3[Handler2 got orphan record];
    C3-->C4[Handler2 failed to acquire lock];
    C4-->C5[Handler2 wait and fetch from Cache];
    C5-->C6[Handler2 return without executing];
    B6-->D(Lambda handler executed only once);
    C6-->D;
```

*Race condition with Cache*

### Persistence layers

#### DynamoDBPersistenceLayer

This persistence layer is built-in, and you can either use an existing DynamoDB table or create a new one dedicated for idempotency state (recommended).

```
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import { makeHandlerIdempotent } from '@aws-lambda-powertools/idempotency/middleware';
import middy from '@middy/core';
import type { Context } from 'aws-lambda';
import type { Request, Response } from './types.js';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
  keyAttr: 'idempotencyKey',
  expiryAttr: 'expiresAt',
  inProgressExpiryAttr: 'inProgressExpiresAt',
  statusAttr: 'currentStatus',
  dataAttr: 'resultData',
  validationKeyAttr: 'validationKey',
});

export const handler = middy(
  async (_event: Request, _context: Context): Promise<Response> => {
    // ... create payment

    return {
      paymentId: '1234567890',
      message: 'success',
      statusCode: 200,
    };
  }
).use(
  makeHandlerIdempotent({
    persistenceStore,
  })
);

```

When using DynamoDB as a persistence layer, you can alter the attribute names by passing these parameters when initializing the persistence layer:

||Parameter |Required |Default |Description || | ------------------------ | ------------------ | ------------------------------------ | -------------------------------------------------------------------------------------------------------- | ||**tableName** | | |Table name to store state || ||**keyAttr** | |`id` |Partition key of the table. Hashed representation of the payload (unless **sort_key_attr** is specified) || ||**expiryAttr** | |`expiration` |Unix timestamp of when record expires || ||**inProgressExpiryAttr** | |`in_progress_expiration` |Unix timestamp of when record expires while in progress (in case of the invocation times out) || ||**statusAttr** | |`status` |Stores status of the lambda execution during and after invocation || ||**dataAttr** | |`data` |Stores results of successfully executed Lambda handlers || ||**validationKeyAttr** | |`validation` |Hashed representation of the parts of the event used for validation || ||**sortKeyAttr** | | |Sort key of the table (if table is configured with a sort key). || ||**staticPkValue** | |`idempotency#{LAMBDA_FUNCTION_NAME}` |Static value to use as the partition key. Only used when **sort_key_attr** is set. ||

#### CachePersistenceLayer

The `CachePersistenceLayer` enables you to use Valkey, Redis OSS, or any Redis-compatible cache as the persistence layer for idempotency state. You need to provide your own cache client.

We recommend using [`@valkey/valkey-glide`](https://www.npmjs.com/package/@valkey/valkey-glide) for Valkey or [`@redis/client`](https://www.npmjs.com/package/@redis/client) for Redis. However, any Redis OSS-compatible client should work.

Info

Make sure your cache client is configured and connected before using it with `CachePersistenceLayer`.

```
import { CachePersistenceLayer } from '@aws-lambda-powertools/idempotency/cache';
import { makeHandlerIdempotent } from '@aws-lambda-powertools/idempotency/middleware';
import middy from '@middy/core';
import { GlideClient } from '@valkey/valkey-glide';
import type { Context } from 'aws-lambda';

const client = await GlideClient.createClient({
  addresses: [
    {
      host: String(process.env.CACHE_ENDPOINT),
      port: Number(process.env.CACHE_PORT),
    },
  ],
  useTLS: true,
  requestTimeout: 2000,
});

const persistenceStore = new CachePersistenceLayer({
  client,
});

export const handler = middy(async (_event: unknown, _context: Context) => {
  const payment = await processPayment();

  return {
    paymentId: payment?.paymentId,
    message: 'success',
    statusCode: 200,
  };
}).use(
  makeHandlerIdempotent({
    persistenceStore,
  })
);

```

```
import { CachePersistenceLayer } from '@aws-lambda-powertools/idempotency/cache';
import { makeHandlerIdempotent } from '@aws-lambda-powertools/idempotency/middleware';
import middy from '@middy/core';
import { createClient } from '@redis/client';
import type { Context } from 'aws-lambda';

const client = await createClient({
  url: `rediss://${process.env.CACHE_ENDPOINT}:${process.env.CACHE_PORT}`,
  username: 'default',
}).connect();

const persistenceStore = new CachePersistenceLayer({
  client,
});

export const handler = middy(async (_event: unknown, _context: Context) => {
  const payment = await processPayment();

  return {
    paymentId: payment?.paymentId,
    message: 'success',
    statusCode: 200,
  };
}).use(
  makeHandlerIdempotent({
    persistenceStore,
  })
);

```

When using Cache as a persistence layer, you can alter the attribute names by passing these parameters when initializing the persistence layer:

||Parameter |Required |Default |Description || | ------------------------ | ------------------ | ------------------------------------ | -------------------------------------------------------------------------------------------------------- | ||**client** | | |A connected Redis-compatible client instance || ||**expiryAttr** | |`expiration` |Unix timestamp of when record expires || ||**inProgressExpiryAttr** | |`in_progress_expiration` |Unix timestamp of when record expires while in progress (in case of the invocation times out) || ||**statusAttr** | |`status` |Stores status of the lambda execution during and after invocation || ||**dataAttr** | |`data` |Stores results of successfully executed Lambda handlers || ||**validationKeyAttr** | |`validation` |Hashed representation of the parts of the event used for validation ||

```
import { CachePersistenceLayer } from '@aws-lambda-powertools/idempotency/cache';
import { makeHandlerIdempotent } from '@aws-lambda-powertools/idempotency/middleware';
import middy from '@middy/core';
import { GlideClient } from '@valkey/valkey-glide';
import type { Context } from 'aws-lambda';

const client = await GlideClient.createClient({
  addresses: [
    {
      host: String(process.env.CACHE_ENDPOINT),
      port: Number(process.env.CACHE_PORT),
    },
  ],
  useTLS: true,
  requestTimeout: 5000,
});

const persistenceStore = new CachePersistenceLayer({
  client,
  expiryAttr: 'expiresAt',
  inProgressExpiryAttr: 'inProgressExpiresAt',
  statusAttr: 'currentStatus',
  dataAttr: 'resultData',
  validationKeyAttr: 'validationKey',
});

export const handler = middy(async (_event: unknown, _context: Context) => {
  const payment = await processPayment();

  return {
    paymentId: payment?.paymentId,
    message: 'success',
    statusCode: 200,
  };
}).use(
  makeHandlerIdempotent({
    persistenceStore,
  })
);

```

## Advanced

### Customizing the default behavior

Idempotent decorator can be further configured with **`IdempotencyConfig`** as seen in the previous examples. These are the available options for further configuration

||Parameter |Default |Description || | ----------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ||**eventKeyJmespath** |`''` |JMESPath expression to extract the idempotency key from the event record using [built-in functions](https://docs.aws.amazon.com/powertools/typescript/latest/features/jmespath/#built-in-jmespath-functions){target="*blank"} || ||**payloadValidationJmespath** |`''` |JMESPath expression to validate that the specified fields haven't changed across requests for the same idempotency key \_e.g., payload tampering.* || ||**jmesPathOptions** |`undefined` |Custom JMESPath functions to use when parsing the JMESPath expressions. See [Custom JMESPath Functions](https://docs.aws.amazon.com/powertools/typescript/latest/features/idempotency/#custom-jmespath-functions) || ||**throwOnNoIdempotencyKey** |`false` |Throw an error if no idempotency key was found in the request || ||**expiresAfterSeconds** |3600 |The number of seconds to wait before a record is expired, allowing a new transaction with the same idempotency key || ||**useLocalCache** |`false` |Whether to cache idempotency results in-memory to save on persistence storage latency and costs || ||**localCacheMaxItems** |256 |Max number of items to store in local cache || ||**hashFunction** |`md5` |Function to use for calculating hashes, as provided by the [crypto](https://nodejs.org/api/crypto.html#cryptocreatehashalgorithm-options) module in the standard library. || ||**responseHook** |`undefined` |Function to use for processing the stored Idempotent response. This function hook is called when an existing idempotent response is found. See [Manipulating The Idempotent Response](https://docs.aws.amazon.com/powertools/typescript/latest/features/idempotency/#manipulating-the-idempotent-response) ||

### Handling concurrent executions with the same payload

This utility will throw an **`IdempotencyAlreadyInProgressError`** error if you receive **multiple invocations with the same payload while the first invocation hasn't completed yet**.

Info

If you receive `IdempotencyAlreadyInProgressError`, you can safely retry the operation.

This is a locking mechanism for correctness. Since we don't know the result from the first invocation yet, we can't safely allow another concurrent execution.

### Using in-memory cache

**By default, in-memory local caching is disabled**, since we don't know how much memory you consume per invocation compared to the maximum configured in your Lambda function.

Note: This in-memory cache is local to each Lambda execution environment

This means it will be effective in cases where your function's concurrency is low in comparison to the number of "retry" invocations with the same payload, because cache might be empty.

You can enable in-memory caching with the **`useLocalCache`** parameter:

```
import { IdempotencyConfig } from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import { makeHandlerIdempotent } from '@aws-lambda-powertools/idempotency/middleware';
import middy from '@middy/core';
import type { Context } from 'aws-lambda';
import type { Request, Response } from './types.js';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
});
const config = new IdempotencyConfig({
  useLocalCache: true,
  maxLocalCacheSize: 512,
});

export const handler = middy(
  async (_event: Request, _context: Context): Promise<Response> => {
    // ... create payment

    return {
      paymentId: '1234567890',
      message: 'success',
      statusCode: 200,
    };
  }
).use(
  makeHandlerIdempotent({
    persistenceStore,
    config,
  })
);

```

When enabled, the default is to cache a maximum of 256 records in each Lambda execution environment - You can change it with the **`maxLocalCacheSize`** parameter.

### Expiring idempotency records

By default, we expire idempotency records after **an hour** (3600 seconds).

In most cases, it is not desirable to store the idempotency records forever. Rather, you want to guarantee that the same payload won't be executed within a period of time.

You can change this window with the **`expiresAfterSeconds`** parameter:

```
import {
  IdempotencyConfig,
  makeIdempotent,
} from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import type { Context } from 'aws-lambda';
import type { Request, Response } from './types.js';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
});

const config = new IdempotencyConfig({
  expiresAfterSeconds: 300,
});

export const handler = makeIdempotent(
  async (_event: Request, _context: Context): Promise<Response> => {
    // ... create payment

    return {
      paymentId: '12345',
      message: 'success',
      statusCode: 200,
    };
  },
  {
    persistenceStore,
    config,
  }
);

```

This will mark any records older than 5 minutes as expired, and [your function will be executed as normal if it is invoked with a matching payload](#expired-idempotency-records).

Idempotency record expiration vs DynamoDB time-to-live (TTL)

[DynamoDB TTL is a feature](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/howitworks-ttl.html) to remove items after a certain period of time, it may occur within 48 hours of expiration.

We don't rely on DynamoDB or any persistence storage layer to determine whether a record is expired to avoid eventual inconsistency states.

Instead, Idempotency records saved in the storage layer contain timestamps that can be verified upon retrieval and double checked within Idempotency feature.

**Why?**

A record might still be valid (`COMPLETE`) when we retrieved, but in some rare cases it might expire a second later. A record could also be [cached in memory](#using-in-memory-cache). You might also want to have idempotent transactions that should expire in seconds.

### Payload validation

Question: What if your function is invoked with the same payload except some outer parameters have changed?

Example: A payment transaction for a given productID was requested twice for the same customer, **however the amount to be paid has changed in the second transaction**.

By default, we will return the same result as it returned before, however in this instance it may be misleading; we provide a fail fast payload validation to address this edge case.

With **`payloadValidationJmesPath`**, you can provide an additional JMESPath expression to specify which part of the event body should be validated against previous idempotent invocations

```
import { randomUUID } from 'node:crypto';
import {
  IdempotencyConfig,
  makeIdempotent,
} from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import type { Context } from 'aws-lambda';
import type { Request, Response, SubscriptionResult } from './types.js';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
});
const config = new IdempotencyConfig({
  eventKeyJmesPath: '["userId", "productId"]',
  payloadValidationJmesPath: 'amount',
});

const fetchProductAmount = async (_transactionId: string): Promise<number> => {
  // ... fetch product amount
  return 42;
};

const createSubscriptionPayment = makeIdempotent(
  async (event: Request & { amount: number }): Promise<SubscriptionResult> => {
    // ... create payment
    return {
      id: randomUUID(),
      productId: event.productId,
    };
  },
  {
    persistenceStore,
    dataIndexArgument: 1,
    config,
  }
);

export const handler = async (
  event: Request,
  context: Context
): Promise<Response> => {
  config.registerLambdaContext(context);

  const productAmount = await fetchProductAmount(event.productId);
  const payment = await createSubscriptionPayment({
    ...event,
    amount: productAmount,
  });

  return {
    paymentId: payment.id,
    message: 'success',
    statusCode: 200,
  };
};

```

In this example, the **`userId`** and **`productId`** keys are used as the payload to generate the idempotency key, as per **`eventKeyJmespath`** parameter.

Note

If we try to send the same request but with a different amount, we will raise **`IdempotencyValidationError`**.

Without payload validation, we would have returned the same result as we did for the initial request. Since we're also returning an amount in the response, this could be quite confusing for the client.

By using **`payloadValidationJmesPath="amount"`**, we prevent this potentially confusing behavior and instead throw an error.

### Custom JMESPath Functions

You can provide custom JMESPath functions for evaluating JMESPath expressions by passing them through the **`jmesPathOptions`** parameter. In this example, we use a custom function, `my_fancy_function`, to parse the payload as a JSON object instead of a string.

```
import type { JSONValue } from '@aws-lambda-powertools/commons/types';
import {
  IdempotencyConfig,
  makeIdempotent,
} from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import {
  Functions,
  PowertoolsFunctions,
} from '@aws-lambda-powertools/jmespath/functions';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
});

class MyFancyFunctions extends PowertoolsFunctions {
  @Functions.signature({
    argumentsSpecs: [['string']],
  })
  public funcMyFancyFunction(value: string): JSONValue {
    return JSON.parse(value);
  }
}

export const handler = makeIdempotent(async () => true, {
  persistenceStore,
  config: new IdempotencyConfig({
    eventKeyJmesPath: 'my_fancy_function(body).["user", "productId"]',
    jmesPathOptions: new MyFancyFunctions(),
  }),
});

```

### Making idempotency key required

If you want to enforce that an idempotency key is required, you can set **`throwOnNoIdempotencyKey`** to `true`.

This means that we will raise **`IdempotencyKeyError`** if the evaluation of **`eventKeyJmesPath`** results in an empty subset.

Warning

To prevent errors, transactions will not be treated as idempotent if **`throwOnNoIdempotencyKey`** is set to `false` and the evaluation of **`eventKeyJmesPath`** is an empty result. Therefore, no data will be fetched, stored, or deleted in the idempotency storage layer.

```
import {
  IdempotencyConfig,
  makeIdempotent,
} from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import type { Context } from 'aws-lambda';
import type { Request, Response } from './types.js';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
});

const config = new IdempotencyConfig({
  throwOnNoIdempotencyKey: true,
  eventKeyJmesPath: '["user.uid", "productId"]',
});

export const handler = makeIdempotent(
  async (_event: Request, _context: Context): Promise<Response> => {
    // ... create payment

    return {
      paymentId: '12345',
      message: 'success',
      statusCode: 200,
    };
  },
  {
    persistenceStore,
    config,
  }
);

```

```
{
  "user": {
    "uid": "BB0D045C-8878-40C8-889E-38B3CB0A61B1",
    "name": "Foo"
  },
  "productId": 10000
}

```

```
{
  "user": {
    "uid": "BB0D045C-8878-40C8-889E-38B3CB0A61B1",
    "name": "foo",
    "productId": 10000
  }
}

```

### Customizing the idempotency key prefix

Warning

Changing the idempotency key generation will invalidate existing idempotency records

You can use the `keyPrefix` parameter in any of the idempotency configurations to define a custom prefix for your idempotency key. This allows you to decouple the idempotency key from the function name, which is especially useful during application refactorings.

```
import { randomUUID } from 'node:crypto';
import { makeIdempotent } from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
});

export const handler = makeIdempotent(
  async () => {
    // ... create payment

    return {
      paymentId: randomUUID(),
      message: 'success',
      statusCode: 200,
    };
  },
  {
    persistenceStore,
    keyPrefix: 'createSubscriptionPayment',
  }
);

```

```
import { randomUUID } from 'node:crypto';
import { idempotent } from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import type { Context } from 'aws-lambda';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
});

class Lambda {
  @idempotent({
    persistenceStore,
    keyPrefix: 'createSubscriptionPayment',
  })
  async handler(_event: unknown, _context: Context) {
    // ... create payment

    return {
      paymentId: randomUUID(),
      message: 'success',
      statusCode: 200,
    };
  }
}

const lambda = new Lambda();
export const handler = lambda.handler.bind(lambda);

```

```
import { randomUUID } from 'node:crypto';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import { makeHandlerIdempotent } from '@aws-lambda-powertools/idempotency/middleware';
import middy from '@middy/core';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
});

export const handler = middy()
  .use(
    makeHandlerIdempotent({
      persistenceStore,
      keyPrefix: 'createSubscriptionPayment',
    })
  )
  .handler(async () => {
    // ... create payment

    return {
      paymentId: randomUUID(),
      message: 'success',
      statusCode: 200,
    };
  });

```

### Batch integration

You can easily integrate with [Batch](https://docs.aws.amazon.com/powertools/typescript/latest/features/batch/index.md) utility by using idempotency wrapper around your processing function. This ensures that you process each record in an idempotent manner, and guard against a [Lambda timeout](#lambda-timeouts) idempotent situation.

Choosing a unique batch record attribute

In this example, we choose `messageId` as our idempotency key since we know it'll be unique. Depending on your use case, it might be more accurate [to choose another field](#choosing-a-payload-subset-for-idempotency) your producer intentionally set to define uniqueness.

```
import {
  BatchProcessor,
  EventType,
  processPartialResponse,
} from '@aws-lambda-powertools/batch';
import {
  IdempotencyConfig,
  makeIdempotent,
} from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import type {
  Context,
  SQSBatchResponse,
  SQSEvent,
  SQSRecord,
} from 'aws-lambda';

const processor = new BatchProcessor(EventType.SQS);

const dynamoDBPersistence = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTable',
});
const idempotencyConfig = new IdempotencyConfig({
  eventKeyJmesPath: 'messageId',
});

const processIdempotently = makeIdempotent(
  async (_record: SQSRecord) => {
    // process your event
  },
  {
    persistenceStore: dynamoDBPersistence,
    config: idempotencyConfig,
  }
);

export const handler = async (
  event: SQSEvent,
  context: Context
): Promise<SQSBatchResponse> => {
  idempotencyConfig.registerLambdaContext(context);

  return processPartialResponse(event, processIdempotently, processor, {
    context,
  });
};

```

```
{
  "Records": [
    {
      "messageId": "059f36b4-87a3-44ab-83d2-661975830a7d",
      "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a...",
      "body": "Test message.",
      "attributes": {
        "ApproximateReceiveCount": "1",
        "SentTimestamp": "1545082649183",
        "SenderId": "AIDAIENQZJOLO23YVJ4VO",
        "ApproximateFirstReceiveTimestamp": "1545082649185"
      },
      "messageAttributes": {
        "testAttr": {
          "stringValue": "100",
          "binaryValue": "base64Str",
          "dataType": "Number"
        }
      },
      "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:my-queue",
      "awsRegion": "us-east-2"
    }
  ]
}

```

### Customizing AWS SDK configuration

The **`clientConfig`** and **`awsSdkV3Client`** parameters enable you to pass in custom configurations or your own [DynamoDBClient](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/dynamodb/) when constructing the persistence store.

```
import { makeIdempotent } from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import type { Context } from 'aws-lambda';
import type { Request, Response } from './types.js';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
  clientConfig: {
    region: 'us-east-1',
  },
});

export const handler = makeIdempotent(
  async (_event: Request, _context: Context): Promise<Response> => {
    // ... create payment

    return {
      paymentId: '12345',
      message: 'success',
      statusCode: 200,
    };
  },
  {
    persistenceStore,
  }
);

```

```
import { makeIdempotent } from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import type { Context } from 'aws-lambda';
import type { Request, Response } from './types.js';

const customDynamoDBClient = new DynamoDBClient({
  endpoint: 'http://localhost:8000',
});
const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
  awsSdkV3Client: customDynamoDBClient,
});

export const handler = makeIdempotent(
  async (_event: Request, _context: Context): Promise<Response> => {
    // ... create payment

    return {
      paymentId: '12345',
      message: 'success',
      statusCode: 200,
    };
  },
  {
    persistenceStore,
  }
);

```

### Using a DynamoDB table with a composite primary key

When using a composite primary key table (hash+range key), use `sortKeyAttr` parameter when initializing your persistence layer.

With this setting, we will save the idempotency key in the sort key instead of the primary key. By default, the primary key will now be set to `idempotency#{LAMBDA_FUNCTION_NAME}`.

You can optionally set a static value for the partition key using the `staticPkValue` parameter.

```
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import { makeHandlerIdempotent } from '@aws-lambda-powertools/idempotency/middleware';
import middy from '@middy/core';
import type { Context } from 'aws-lambda';
import type { Request, Response } from './types.js';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
  sortKeyAttr: 'sort_key',
});

export const handler = middy(
  async (_event: Request, _context: Context): Promise<Response> => {
    // ... create payment

    return {
      paymentId: '12345',
      message: 'success',
      statusCode: 200,
    };
  }
).use(
  makeHandlerIdempotent({
    persistenceStore,
  })
);

```

The example function above would cause data to be stored in DynamoDB like this:

||id |sort_key |expiration |status |data || | ---------------------------- | -------------------------------- | ---------- | ----------- | ---------------------------------------------------------------- | ||idempotency#MyLambdaFunction |1e956ef7da78d0cb890be999aecc0c9e |1636549553 |COMPLETED |{"paymentId": "12345, "message": "success", "statusCode": 200} || ||idempotency#MyLambdaFunction |2b2cdb5f86361e97b4383087c1ffdf27 |1636549571 |COMPLETED |{"paymentId": "527212", "message": "success", "statusCode": 200} || ||idempotency#MyLambdaFunction |f091d2527ad1c78f05d54cc3f363be80 |1636549585 |IN_PROGRESS | ||

### Bring your own persistent store

This utility provides an abstract base class (ABC), so that you can implement your choice of persistent storage layer.

You can create your own persistent store from scratch by inheriting the `BasePersistenceLayer` class, and implementing `_getRecord()`, `_putRecord()`, `_updateRecord()` and `_deleteRecord()`.

- `_getRecord()` â Retrieves an item from the persistence store using an idempotency key and returns it as a `IdempotencyRecord` instance.
- `_putRecord()` â Adds a `IdempotencyRecord` to the persistence store if it doesn't already exist with that key. Throws an `IdempotencyItemAlreadyExistsError` error if a non-expired entry already exists.
- `_updateRecord()` â Updates an item in the persistence store.
- `_deleteRecord()` â Removes an item from the persistence store.

Below an example implementation of a custom persistence layer backed by a generic key-value store.

```
import {
  IdempotencyItemAlreadyExistsError,
  IdempotencyItemNotFoundError,
  IdempotencyRecordStatus,
} from '@aws-lambda-powertools/idempotency';
import {
  BasePersistenceLayer,
  IdempotencyRecord,
} from '@aws-lambda-powertools/idempotency/persistence';
import type { IdempotencyRecordOptions } from '@aws-lambda-powertools/idempotency/types';
import { Transform } from '@aws-lambda-powertools/parameters';
import { getSecret } from '@aws-lambda-powertools/parameters/secrets';
import {
  ProviderClient,
  ProviderItemAlreadyExists,
} from './advancedBringYourOwnPersistenceLayerProvider';
import type { ApiSecret, ProviderItem } from './types';

class CustomPersistenceLayer extends BasePersistenceLayer {
  #collectionName: string;
  #client?: ProviderClient;

  public constructor(config: { collectionName: string }) {
    super();
    this.#collectionName = config.collectionName;
  }

  protected async _deleteRecord(record: IdempotencyRecord): Promise<void> {
    await (await this.#getClient()).delete(
      this.#collectionName,
      record.idempotencyKey
    );
  }

  protected async _getRecord(
    idempotencyKey: string
  ): Promise<IdempotencyRecord> {
    try {
      const item = await (await this.#getClient()).get(
        this.#collectionName,
        idempotencyKey
      );

      return new IdempotencyRecord({
        ...(item as unknown as IdempotencyRecordOptions),
      });
    } catch (error) {
      throw new IdempotencyItemNotFoundError('Item not found in store', {
        cause: error,
      });
    }
  }

  protected async _putRecord(record: IdempotencyRecord): Promise<void> {
    const item: Partial<ProviderItem> = {
      status: record.getStatus(),
    };

    if (record.inProgressExpiryTimestamp !== undefined) {
      item.in_progress_expiration = record.inProgressExpiryTimestamp;
    }

    if (this.isPayloadValidationEnabled() && record.payloadHash !== undefined) {
      item.validation = record.payloadHash;
    }

    const ttl = record.expiryTimestamp
      ? Math.floor(new Date(record.expiryTimestamp * 1000).getTime() / 1000) -
        Math.floor(Date.now() / 1000)
      : this.getExpiresAfterSeconds();

    let existingItem: ProviderItem | undefined;
    try {
      existingItem = await (await this.#getClient()).put(
        this.#collectionName,
        record.idempotencyKey,
        item,
        {
          ttl,
        }
      );
    } catch (error) {
      if (error instanceof ProviderItemAlreadyExists) {
        if (
          existingItem &&
          existingItem.status !== IdempotencyRecordStatus.INPROGRESS &&
          (existingItem.in_progress_expiration || 0) < Date.now()
        ) {
          throw new IdempotencyItemAlreadyExistsError(
            `Failed to put record for already existing idempotency key: ${record.idempotencyKey}`
          );
        }
      }
    }
  }

  protected async _updateRecord(record: IdempotencyRecord): Promise<void> {
    const value: Partial<ProviderItem> = {
      data: JSON.stringify(record.responseData),
      status: record.getStatus(),
    };

    if (this.isPayloadValidationEnabled()) {
      value.validation = record.payloadHash;
    }

    await (await this.#getClient()).update(
      this.#collectionName,
      record.idempotencyKey,
      value
    );
  }

  async #getClient(): Promise<ProviderClient> {
    if (this.#client) return this.#client;

    const secretName = process.env.API_SECRET;
    if (!secretName) {
      throw new Error('API_SECRET environment variable is not set');
    }

    const apiSecret = await getSecret<ApiSecret>(secretName, {
      transform: Transform.JSON,
    });

    if (!apiSecret) {
      throw new Error(`Could not retrieve secret ${secretName}`);
    }

    this.#client = new ProviderClient({
      apiKey: apiSecret.apiKey,
      defaultTtlSeconds: this.getExpiresAfterSeconds(),
    });

    return this.#client;
  }
}

export { CustomPersistenceLayer };

```

```
import { randomUUID } from 'node:crypto';
import {
  IdempotencyConfig,
  makeIdempotent,
} from '@aws-lambda-powertools/idempotency';
import type { Context } from 'aws-lambda';
import { CustomPersistenceLayer } from './advancedBringYourOwnPersistenceLayer';
import type { Request, Response, SubscriptionResult } from './types.js';

const persistenceStore = new CustomPersistenceLayer({
  collectionName: 'powertools',
});
const config = new IdempotencyConfig({
  expiresAfterSeconds: 60,
});

const createSubscriptionPayment = makeIdempotent(
  async (
    _transactionId: string,
    event: Request
  ): Promise<SubscriptionResult> => {
    // ... create payment
    return {
      id: randomUUID(),
      productId: event.productId,
    };
  },
  {
    persistenceStore,
    dataIndexArgument: 1,
    config,
  }
);

export const handler = async (
  event: Request,
  context: Context
): Promise<Response> => {
  config.registerLambdaContext(context);

  const transactionId = randomUUID();
  const payment = await createSubscriptionPayment(transactionId, event);

  return {
    paymentId: payment.id,
    message: 'success',
    statusCode: 200,
  };
};

```

```
import type { IdempotencyRecordStatusValue } from '@aws-lambda-powertools/idempotency/types';

export type Request = {
  user: string;
  productId: string;
};

export type Response = {
  [key: string]: unknown;
};

export type SubscriptionResult = {
  id: string;
  productId: string;
};

export type ApiSecret = {
  apiKey: string;
  refreshToken: string;
  validUntil: number;
  restEndpoint: string;
};

export type ProviderItem = {
  validation?: string;
  in_progress_expiration?: number;
  status: IdempotencyRecordStatusValue;
  data: string;
};

```

Danger

Pay attention to the documentation for each - you may need to perform additional checks inside these methods to ensure the idempotency guarantees remain intact.

For example, the `_putRecord()` method needs to throw an error if a non-expired record already exists in the data store with a matching key.

### Manipulating the Idempotent Response

You can set up a `responseHook` in the `IdempotentConfig` class to manipulate the returned data when an operation is idempotent. The hook function will be called with the current deserialized response object and the Idempotency record.

```
import { randomUUID } from 'node:crypto';
import type { JSONValue } from '@aws-lambda-powertools/commons/types';
import {
  IdempotencyConfig,
  makeIdempotent,
} from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import type { IdempotencyRecord } from '@aws-lambda-powertools/idempotency/persistence';
import type { Context } from 'aws-lambda';
import type { Request, Response, SubscriptionResult } from './types.js';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'idempotencyTableName',
});

const responseHook = (response: JSONValue, record: IdempotencyRecord) => {
  // Return inserted Header data into the Idempotent Response
  (response as Response).headers = {
    'x-idempotency-key': record.idempotencyKey,
  };

  // Must return the response here
  return response as JSONValue;
};

const config = new IdempotencyConfig({
  responseHook,
});

const createSubscriptionPayment = async (
  event: Request
): Promise<SubscriptionResult> => {
  // ... create payment
  return {
    id: randomUUID(),
    productId: event.productId,
  };
};

export const handler = makeIdempotent(
  async (event: Request, _context: Context): Promise<Response> => {
    const payment = await createSubscriptionPayment(event);

    return {
      paymentId: payment.id,
      message: 'success',
      statusCode: 200,
    };
  },
  {
    persistenceStore,
    config,
  }
);

```

```
{
  "user": "John Doe",
  "productId": "123456"
}

```

```
{
  "message": "success",
  "paymentId": "31a964eb-7477-4fe1-99fe-7f8a6a351a7e",
  "statusCode": 200,
  "headers": {
    "x-idempotency-key": "function-name#mHfGv2vJ8h+ZvLIr/qGBbQ=="
  }
}

```

Info: Using custom de-serialization?

The responseHook is called after the custom de-serialization so the payload you process will be the de-serialized version.

#### Being a good citizen

When using response hooks to manipulate returned data from idempotent operations, it's important to follow best practices to avoid introducing complexity or issues. Keep these guidelines in mind:

1. **Response hook works exclusively when operations are idempotent.** The hook will not be called when an operation is not idempotent, or when the idempotent logic fails.
1. **Catch and Handle Exceptions.** Your response hook code should catch and handle any exceptions that may arise from your logic. Unhandled exceptions will cause the Lambda function to fail unexpectedly.
1. **Keep Hook Logic Simple** Response hooks should consist of minimal and straightforward logic for manipulating response data. Avoid complex conditional branching and aim for hooks that are easy to reason about.

## Testing your code

The idempotency utility provides several routes to test your code.

### Disabling the idempotency utility

When testing your code, you may wish to disable the idempotency logic altogether and focus on testing your business logic. To do this, you can set the environment variable `POWERTOOLS_IDEMPOTENCY_DISABLED` with a truthy value.

### Testing with local DynamoDB

When testing your Lambda function locally, you can use a local DynamoDB instance to test the idempotency feature. You can use [DynamoDB Local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html) or [LocalStack](https://localstack.cloud/).

```
import { makeIdempotent } from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import type { Context } from 'aws-lambda';
import { describe, expect, it } from 'vitest';
import { handler } from './workingWithLocalDynamoDB.js';

const context = {
  functionName: 'foo-bar-function',
  memoryLimitInMB: '128',
  invokedFunctionArn:
    'arn:aws:lambda:eu-west-1:123456789012:function:foo-bar-function',
  awsRequestId: 'c6af9ac6-7b61-11e6-9a41-93e812345678',
  getRemainingTimeInMillis: () => 1234,
} as Context;

const mockPersistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'IdempotencyTable',
  clientConfig: { endpoint: 'http://localhost:8000' }, // 8000 for local DynamoDB and 4566 for LocalStack
});

describe('Idempotent handler', () => {
  it('returns the same response', async () => {
    // Prepare
    const idempotentHandler = makeIdempotent(handler, {
      persistenceStore: mockPersistenceStore,
    });

    // Act
    const response = await idempotentHandler(
      {
        foo: 'bar',
      },
      context
    );

    // Assess
    expect(response).toEqual({
      statusCode: 200,
      body: JSON.stringify({
        paymentId: '123',
        message: 'Payment created',
      }),
    });
  });
});

```

```
import { makeIdempotent } from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import type { Context } from 'aws-lambda';

const ddbPersistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'IdempotencyTable',
});

const handler = async (_event: unknown, _context: Context) => {
  return {
    statusCode: 200,
    body: JSON.stringify({
      paymentId: '123',
      message: 'Payment created',
    }),
  };
};

const idempotentHandler = makeIdempotent(handler, {
  persistenceStore: ddbPersistenceStore,
});

export { idempotentHandler, handler };

```

### Testing with local cache

Likewise, when using a cache database, you can use a local Valkey or Redis-OSS instance as a local server and replace the endpoint and port in the environment variables.

```
import type { Context } from 'aws-lambda';
import { describe, expect, it, vi } from 'vitest';
import { handler } from './cachePersistenceLayerValkey.js';

vi.hoisted(() => {
  process.env.CACHE_ENDPOINT = 'localhost';
  process.env.CACHE_PORT = '6379';
});

const context = {
  functionName: 'foo-bar-function',
  memoryLimitInMB: '128',
  invokedFunctionArn:
    'arn:aws:lambda:eu-west-1:123456789012:function:foo-bar-function',
  awsRequestId: 'c6af9ac6-7b61-11e6-9a41-93e812345678',
  getRemainingTimeInMillis: () => 1234,
} as Context;

describe('Idempotent handler', () => {
  it('returns the same response', async () => {
    // Act
    const response = await handler(
      {
        foo: 'bar',
      },
      context
    );

    // Assess
    expect(response).toEqual({
      paymentId: expect.any(String),
      message: 'success',
      statusCode: 200,
    });
  });
});

```

```
import { CachePersistenceLayer } from '@aws-lambda-powertools/idempotency/cache';
import { makeHandlerIdempotent } from '@aws-lambda-powertools/idempotency/middleware';
import middy from '@middy/core';
import { GlideClient } from '@valkey/valkey-glide';
import type { Context } from 'aws-lambda';

const client = await GlideClient.createClient({
  addresses: [
    {
      host: String(process.env.CACHE_ENDPOINT),
      port: Number(process.env.CACHE_PORT),
    },
  ],
  useTLS: true,
  requestTimeout: 2000,
});

const persistenceStore = new CachePersistenceLayer({
  client,
});

export const handler = middy(async (_event: unknown, _context: Context) => {
  const payment = await processPayment();

  return {
    paymentId: payment?.paymentId,
    message: 'success',
    statusCode: 200,
  };
}).use(
  makeHandlerIdempotent({
    persistenceStore,
  })
);

```

## Extra resources

If you're interested in a deep dive on how Amazon uses idempotency when building our APIs, check out [this article](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).

The batch processing utility handles partial failures when processing batches from Amazon SQS, Amazon Kinesis Data Streams, and Amazon DynamoDB Streams.

```
stateDiagram-v2
    direction LR
    BatchSource: Amazon SQS <br/><br/> Amazon Kinesis Data Streams <br/><br/> Amazon DynamoDB Streams <br/><br/>
    LambdaInit: Lambda invocation
    BatchProcessor: Batch Processor
    RecordHandler: Record Handler function
    YourLogic: Your logic to process each batch item
    LambdaResponse: Lambda response

    BatchSource --> LambdaInit

    LambdaInit --> BatchProcessor
    BatchProcessor --> RecordHandler

    state BatchProcessor {
        [*] --> RecordHandler: Your function
        RecordHandler --> YourLogic
    }

    RecordHandler --> BatchProcessor: Collect results
    BatchProcessor --> LambdaResponse: Report items that failed processing
```

## Key features

- Reports batch item failures to reduce number of retries for a record upon errors
- Simple interface to process each batch record
- Build your own batch processor by extending primitives

## Background

When using SQS, Kinesis Data Streams, or DynamoDB Streams as a Lambda event source, your Lambda functions are triggered with a batch of messages.

If your function fails to process any message from the batch, the entire batch returns to your queue or stream. This same batch is then retried until either condition happens first: **a)** your Lambda function returns a successful response, **b)** record reaches maximum retry attempts, or **c)** when records expire.

```
journey
  section Conditions
    Successful response: 5: Success
    Maximum retries: 3: Failure
    Records expired: 1: Failure
```

This behavior changes when you enable the [ReportBatchItemFailures feature](https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-errorhandling.html#services-sqs-batchfailurereporting) in your Lambda function event source configuration:

- [**SQS queues**](#sqs-standard). Only messages reported as failure will return to the queue for a retry, while successful ones will be deleted.
- [**Kinesis data streams**](#kinesis-and-dynamodb-streams) and [**DynamoDB streams**](#kinesis-and-dynamodb-streams). Single reported failure will use its sequence number as the stream checkpoint. Multiple reported failures will use the lowest sequence number as the checkpoint.

Warning: This utility lowers the chance of processing records more than once; it does not guarantee it

We recommend implementing processing logic in an [idempotent manner](https://docs.aws.amazon.com/powertools/typescript/latest/features/idempotency/index.md) whenever possible.

You can find more details on how Lambda works with either [SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html), [Kinesis](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html), or [DynamoDB](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html) in the AWS Documentation.

## Getting started

### Installation

Install the library in your project

```
npm i @aws-lambda-powertools/batch

```

For this feature to work, you need to **(1)** configure your Lambda function event source to use `ReportBatchItemFailures`, so that the response from the Batch Processing utility can inform the service which records failed to be processed.

Use your preferred deployment framework to set the correct configuration while this utility handles the correct response to be returned.

### Required resources

The remaining sections of the documentation will rely on these samples. For completeness, this demonstrates IAM permissions and Dead Letter Queue where batch records will be sent after 2 retries.

You do not need any additional IAM permissions to use this utility, except for what each event source requires.

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: partial batch response sample

Globals:
  Function:
    Timeout: 5
    MemorySize: 256
    Runtime: nodejs24.x
    Tracing: Active
    Environment:
      Variables:
        POWERTOOLS_LOG_LEVEL: INFO
        POWERTOOLS_SERVICE_NAME: hello

Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.handler
      CodeUri: hello_world
      Policies:
        - SQSPollerPolicy:
            QueueName: !GetAtt SampleQueue.QueueName
      Events:
        Batch:
          Type: SQS
          Properties:
            Queue: !GetAtt SampleQueue.Arn
            FunctionResponseTypes:
              - ReportBatchItemFailures

  SampleDLQ:
    Type: AWS::SQS::Queue

  SampleQueue:
    Type: AWS::SQS::Queue
    Properties:
      VisibilityTimeout: 30 # Fn timeout * 6
      SqsManagedSseEnabled: true
      RedrivePolicy:
        maxReceiveCount: 2
        deadLetterTargetArn: !GetAtt SampleDLQ.Arn

```

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: partial batch response sample

Globals:
  Function:
    Timeout: 5
    MemorySize: 256
    Runtime: nodejs24.x
    Tracing: Active
    Environment:
      Variables:
        LOG_LEVEL: INFO
        POWERTOOLS_SERVICE_NAME: hello

Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.handler
      CodeUri: hello_world
      Policies:
        # Lambda Destinations require additional permissions
        # to send failure records to DLQ from Kinesis/DynamoDB
        - Version: '2012-10-17'
          Statement:
            Effect: 'Allow'
            Action:
              - sqs:GetQueueAttributes
              - sqs:GetQueueUrl
              - sqs:SendMessage
            Resource: !GetAtt SampleDLQ.Arn
      Events:
        KinesisStream:
          Type: Kinesis
          Properties:
            Stream: !GetAtt SampleStream.Arn
            BatchSize: 100
            StartingPosition: LATEST
            MaximumRetryAttempts: 2
            DestinationConfig:
              OnFailure:
                Destination: !GetAtt SampleDLQ.Arn
            FunctionResponseTypes:
              - ReportBatchItemFailures

  SampleDLQ:
    Type: AWS::SQS::Queue

  SampleStream:
    Type: AWS::Kinesis::Stream
    Properties:
      ShardCount: 1
      StreamEncryption:
        EncryptionType: KMS
        KeyId: alias/aws/kinesis

```

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: partial batch response sample

Globals:
  Function:
    Timeout: 5
    MemorySize: 256
    Runtime: nodejs24.x
    Tracing: Active
    Environment:
      Variables:
        POWERTOOLS_LOG_LEVEL: INFO
        POWERTOOLS_SERVICE_NAME: hello

Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.handler
      CodeUri: hello_world
      Policies:
        # Lambda Destinations require additional permissions
        # to send failure records from Kinesis/DynamoDB
        - Version: '2012-10-17'
          Statement:
            Effect: 'Allow'
            Action:
              - sqs:GetQueueAttributes
              - sqs:GetQueueUrl
              - sqs:SendMessage
            Resource: !GetAtt SampleDLQ.Arn
      Events:
        DynamoDBStream:
          Type: DynamoDB
          Properties:
            Stream: !GetAtt SampleTable.StreamArn
            StartingPosition: LATEST
            MaximumRetryAttempts: 2
            DestinationConfig:
              OnFailure:
                Destination: !GetAtt SampleDLQ.Arn
            FunctionResponseTypes:
              - ReportBatchItemFailures

  SampleDLQ:
    Type: AWS::SQS::Queue

  SampleTable:
    Type: AWS::DynamoDB::Table
    Properties:
      BillingMode: PAY_PER_REQUEST
      AttributeDefinitions:
        - AttributeName: pk
          AttributeType: S
        - AttributeName: sk
          AttributeType: S
      KeySchema:
        - AttributeName: pk
          KeyType: HASH
        - AttributeName: sk
          KeyType: RANGE
      SSESpecification:
        SSEEnabled: true
      StreamSpecification:
        StreamViewType: NEW_AND_OLD_IMAGES

```

### Processing messages from SQS

Processing batches from SQS works in three stages:

1. Instantiate **`BatchProcessor`** and choose **`EventType.SQS`** for the event type
1. Define your function to handle each batch record, and use the `SQSRecord` type annotation for autocompletion
1. Use **`processPartialResponse`** to kick off processing

Note

By default, the batch processor will process messages in parallel, which does not guarantee the order of processing. If you need to process messages in order, set the [`processInParallel` option to `false`](#sequential-processing), or use [`SqsFifoPartialProcessor` for SQS FIFO queues](#fifo-queues).

```
 import {
   BatchProcessor,
   EventType,
   processPartialResponse,
 } from '@aws-lambda-powertools/batch';
 import { Logger } from '@aws-lambda-powertools/logger';
 import type { SQSHandler, SQSRecord } from 'aws-lambda';

 const processor = new BatchProcessor(EventType.SQS); // (1)!
 const logger = new Logger();

 const recordHandler = async (record: SQSRecord): Promise<void> => { // (2)!
   const payload = record.body;
   if (payload) {
     const item = JSON.parse(payload);
     logger.info('Processed item', { item });
   }
 };

 export const handler: SQSHandler = async (event, context) =>
   processPartialResponse(event, recordHandler, processor, { // (3)!
     context,
   });

```

1. **Step 1**. Creates a partial failure batch processor for SQS queues. See [partial failure mechanics for details](#partial-failure-mechanics)
1. **Step 2**. Defines a function to receive one record at a time from the batch
1. **Step 3**. Kicks off processing

The second record failed to be processed, therefore the processor added its message ID in the response.

```
{
  "batchItemFailures": [
    {
      "itemIdentifier": "244fc6b4-87a3-44ab-83d2-361172410c3a"
    }
  ]
}

```

```
{
  "Records": [
    {
      "messageId": "059f36b4-87a3-44ab-83d2-661975830a7d",
      "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a",
      "body": "{\"Message\": \"success\"}",
      "attributes": {
        "ApproximateReceiveCount": "1",
        "SentTimestamp": "1545082649183",
        "SenderId": "AIDAIENQZJOLO23YVJ4VO",
        "ApproximateFirstReceiveTimestamp": "1545082649185"
      },
      "messageAttributes": {},
      "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-2: 123456789012:my-queue",
      "awsRegion": "us-east-1"
    },
    {
      "messageId": "244fc6b4-87a3-44ab-83d2-361172410c3a",
      "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a",
      "body": "SGVsbG8sIHRoaXMgaXMgYSB0ZXN0Lg==",
      "attributes": {
        "ApproximateReceiveCount": "1",
        "SentTimestamp": "1545082649183",
        "SenderId": "AIDAIENQZJOLO23YVJ4VO",
        "ApproximateFirstReceiveTimestamp": "1545082649185"
      },
      "messageAttributes": {},
      "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-2: 123456789012:my-queue",
      "awsRegion": "us-east-1"
    }
  ]
}

```

#### FIFO queues

When using [SQS FIFO queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fifo-queues.html), a batch may include messages from different group IDs.

By default, we will stop processing at the first failure and mark unprocessed messages as failed to preserve ordering. However, this behavior may not be optimal for customers who wish to proceed with processing messages from a different group ID.

Enable the `skipGroupOnError` option for seamless processing of messages from various group IDs. This setup ensures that messages from a failed group ID are sent back to SQS, enabling uninterrupted processing of messages from the subsequent group ID.

```
import {
  processPartialResponse,
  SqsFifoPartialProcessorAsync,
} from '@aws-lambda-powertools/batch';
import { Logger } from '@aws-lambda-powertools/logger';
import type { SQSHandler, SQSRecord } from 'aws-lambda';

const processor = new SqsFifoPartialProcessorAsync();
const logger = new Logger();

const recordHandler = async (record: SQSRecord): Promise<void> => {
  const payload = record.body;
  if (payload) {
    const item = JSON.parse(payload);
    logger.info('Processed item', { item });
  }
};

export const handler: SQSHandler = async (event, context) =>
  processPartialResponse(event, recordHandler, processor, {
    context,
  });

```

```
import {
  processPartialResponse,
  SqsFifoPartialProcessorAsync,
} from '@aws-lambda-powertools/batch';
import { Logger } from '@aws-lambda-powertools/logger';
import type {
  Context,
  SQSBatchResponse,
  SQSEvent,
  SQSRecord,
} from 'aws-lambda';

const processor = new SqsFifoPartialProcessorAsync();
const logger = new Logger();

const recordHandler = (record: SQSRecord): void => {
  const payload = record.body;
  if (payload) {
    const item = JSON.parse(payload);
    logger.info('Processed item', { item });
  }
};

export const handler = async (
  event: SQSEvent,
  context: Context
): Promise<SQSBatchResponse> => {
  return processPartialResponse(event, recordHandler, processor, {
    context,
    skipGroupOnError: true,
  });
};

```

### Processing messages from Kinesis

Processing batches from Kinesis works in three stages:

1. Instantiate **`BatchProcessor`** and choose **`EventType.KinesisDataStreams`** for the event type
1. Define your function to handle each batch record, and use the `KinesisStreamRecord` type annotation for autocompletion
1. Use **`processPartialResponse`** to kick off processing

```
import {
  BatchProcessor,
  EventType,
  processPartialResponse,
} from '@aws-lambda-powertools/batch';
import { Logger } from '@aws-lambda-powertools/logger';
import type { KinesisStreamHandler, KinesisStreamRecord } from 'aws-lambda';

const processor = new BatchProcessor(EventType.KinesisDataStreams); // (1)!
const logger = new Logger();

const recordHandler = async (record: KinesisStreamRecord): Promise<void> => {
  logger.info('Processing record', { record: record.kinesis.data });
  const payload = JSON.parse(record.kinesis.data);
  logger.info('Processed item', { item: payload });
};

export const handler: KinesisStreamHandler = async (event, context) =>
  processPartialResponse(event, recordHandler, processor, {
    context,
  });

```

1. Creates a partial failure batch processor for Kinesis Data Streams. See [partial failure mechanics for details](#partial-failure-mechanics)

The second record failed to be processed, therefore the processor added its sequence number in the response.

```
{
  "Records": [
    {
      "kinesis": {
        "kinesisSchemaVersion": "1.0",
        "partitionKey": "1",
        "sequenceNumber": "4107859083838847772757075850904226111829882106684065",
        "data": "eyJNZXNzYWdlIjogInN1Y2Nlc3MifQ==",
        "approximateArrivalTimestamp": 1545084650.987
      },
      "eventSource": "aws:kinesis",
      "eventVersion": "1.0",
      "eventID": "shardId-000000000006:4107859083838847772757075850904226111829882106684065",
      "eventName": "aws:kinesis:record",
      "invokeIdentityArn": "arn:aws:iam::123456789012:role/lambda-role",
      "awsRegion": "us-east-2",
      "eventSourceARN": "arn:aws:kinesis:us-east-2:123456789012:stream/lambda-stream"
    },
    {
      "kinesis": {
        "kinesisSchemaVersion": "1.0",
        "partitionKey": "1",
        "sequenceNumber": "6006958808509702859251049540584488075644979031228738",
        "data": "c3VjY2Vzcw==",
        "approximateArrivalTimestamp": 1545084650.987
      },
      "eventSource": "aws:kinesis",
      "eventVersion": "1.0",
      "eventID": "shardId-000000000006:6006958808509702859251049540584488075644979031228738",
      "eventName": "aws:kinesis:record",
      "invokeIdentityArn": "arn:aws:iam::123456789012:role/lambda-role",
      "awsRegion": "us-east-2",
      "eventSourceARN": "arn:aws:kinesis:us-east-2:123456789012:stream/lambda-stream"
    }
  ]
}

```

```
{
  "batchItemFailures": [
    {
      "itemIdentifier": "6006958808509702859251049540584488075644979031228738"
    }
  ]
}

```

### Processing messages from DynamoDB

Processing batches from DynamoDB Streams works in three stages:

1. Instantiate **`BatchProcessor`** and choose **`EventType.DynamoDBStreams`** for the event type
1. Define your function to handle each batch record, and use the `DynamoDBRecord` type annotation for autocompletion
1. Use **`processPartialResponse`** to kick off processing

Info

This code example optionally uses Logger for completion.

```
import {
  BatchProcessor,
  EventType,
  processPartialResponse,
} from '@aws-lambda-powertools/batch';
import { Logger } from '@aws-lambda-powertools/logger';
import type { DynamoDBRecord, DynamoDBStreamHandler } from 'aws-lambda';

const processor = new BatchProcessor(EventType.DynamoDBStreams); // (1)!
const logger = new Logger();

const recordHandler = async (record: DynamoDBRecord): Promise<void> => {
  if (record.dynamodb?.NewImage) {
    logger.info('Processing record', { record: record.dynamodb.NewImage });
    const message = record.dynamodb.NewImage.Message.S;
    if (message) {
      const payload = JSON.parse(message);
      logger.info('Processed item', { item: payload });
    }
  }
};

export const handler: DynamoDBStreamHandler = async (event, context) =>
  processPartialResponse(event, recordHandler, processor, {
    context,
  });

```

1. Creates a partial failure batch processor for DynamoDB Streams. See [partial failure mechanics for details](#partial-failure-mechanics)

The second record failed to be processed, therefore the processor added its sequence number in the response.

```
{
  "batchItemFailures": [
    {
      "itemIdentifier": "8640712661"
    }
  ]
}

```

```
{
  "Records": [
    {
      "eventID": "1",
      "eventVersion": "1.0",
      "dynamodb": {
        "Keys": {
          "Id": {
            "N": "101"
          }
        },
        "NewImage": {
          "Message": {
            "S": "failure"
          }
        },
        "StreamViewType": "NEW_AND_OLD_IMAGES",
        "SequenceNumber": "3275880929",
        "SizeBytes": 26
      },
      "awsRegion": "us-west-2",
      "eventName": "INSERT",
      "eventSourceARN": "eventsource_arn",
      "eventSource": "aws:dynamodb"
    },
    {
      "eventID": "1",
      "eventVersion": "1.0",
      "dynamodb": {
        "Keys": {
          "Id": {
            "N": "101"
          }
        },
        "NewImage": {
          "SomethingElse": {
            "S": "success"
          }
        },
        "StreamViewType": "NEW_AND_OLD_IMAGES",
        "SequenceNumber": "8640712661",
        "SizeBytes": 26
      },
      "awsRegion": "us-west-2",
      "eventName": "INSERT",
      "eventSourceARN": "eventsource_arn",
      "eventSource": "aws:dynamodb"
    }
  ]
}

```

### Error handling

By default, we catch any exception raised by your record handler function. This allows us to **(1)** continue processing the batch, **(2)** collect each batch item that failed processing, and **(3)** return the appropriate response correctly without failing your Lambda function execution.

```
 import {
   BatchProcessor,
   EventType,
   processPartialResponse,
 } from '@aws-lambda-powertools/batch';
 import { Logger } from '@aws-lambda-powertools/logger';
 import type { SQSHandler, SQSRecord } from 'aws-lambda';

 const processor = new BatchProcessor(EventType.SQS);
 const logger = new Logger();

 class InvalidPayload extends Error {
   public constructor(message: string) {
     super(message);
     this.name = 'InvalidPayload';
   }
 }

 const recordHandler = async (record: SQSRecord): Promise<void> => {
   const payload = record.body;
   if (payload) {
     const item = JSON.parse(payload);
     logger.info('Processed item', { item });
   } else {
     throw new InvalidPayload('Payload does not contain minimum required fields'); // (1)!
   }
 };

 export const handler: SQSHandler = async (event, context) =>
   processPartialResponse(event, recordHandler, processor, { // (2)!
     context,
   });

```

1. Any exception works here. See [extending `BatchProcessor` section, if you want to override this behavior.](#extending-batchprocessor)

1. Errors raised in `recordHandler` will propagate to `processPartialResponse`.

   We catch them and include each failed batch item identifier in the response object (see `Sample response` tab).

```
{
  "batchItemFailures": [
    {
      "itemIdentifier": "244fc6b4-87a3-44ab-83d2-361172410c3a"
    }
  ]
}

```

### Partial failure mechanics

All records in the batch will be passed to this handler for processing, even if exceptions are thrown - Here's the behaviour after completing the batch:

- **All records successfully processed**. We will return an empty list of item failures `{'batchItemFailures': []}`
- **Partial success with some exceptions**. We will return a list of all item IDs/sequence numbers that failed processing
- **All records failed to be processed**. We will throw a `FullBatchFailureError` error with a list of all the errors thrown while processing unless `throwOnFullBatchFailure` is disabled.

The following sequence diagrams explain how each Batch processor behaves under different scenarios.

#### SQS Standard

> Read more about [Batch Failure Reporting feature in AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#services-sqs-batchfailurereporting).

Sequence diagram to explain how [`BatchProcessor` works](#processing-messages-from-sqs) with SQS Standard queues.

```
sequenceDiagram
    autonumber
    participant SQS queue
    participant Lambda service
    participant Lambda function
    Lambda service->>SQS queue: Poll
    Lambda service->>Lambda function: Invoke (batch event)
    Lambda function->>Lambda service: Report some failed messages
    activate SQS queue
    Lambda service->>SQS queue: Delete successful messages
    SQS queue-->>SQS queue: Failed messages return
    Note over SQS queue,Lambda service: Process repeat
    deactivate SQS queue
```

*SQS mechanism with Batch Item Failures*

#### SQS FIFO

> Read more about [Batch Failure Reporting feature in AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#services-sqs-batchfailurereporting).

Sequence diagram to explain how [`SqsFifoPartialProcessor` works](#fifo-queues) with SQS FIFO queues without `skipGroupOnError` flag.

```
sequenceDiagram
    autonumber
    participant SQS queue
    participant Lambda service
    participant Lambda function
    Lambda service->>SQS queue: Poll
    Lambda service->>Lambda function: Invoke (batch event)
    activate Lambda function
    Lambda function-->Lambda function: Process 2 out of 10 batch items
    Lambda function--xLambda function: Fail on 3rd batch item
    Lambda function->>Lambda service: Report 3rd batch item and unprocessed messages as failure
    deactivate Lambda function
    activate SQS queue
    Lambda service->>SQS queue: Delete successful messages (1-2)
    SQS queue-->>SQS queue: Failed messages return (3-10)
    deactivate SQS queue
```

*SQS FIFO mechanism with Batch Item Failures*

Sequence diagram to explain how [`SqsFifoPartialProcessor` works](#fifo-queues) with SQS FIFO queues with `skipGroupOnError` flag.

```
sequenceDiagram
    autonumber
    participant SQS queue
    participant Lambda service
    participant Lambda function
    Lambda service->>SQS queue: Poll
    Lambda service->>Lambda function: Invoke (batch event)
    activate Lambda function
    Lambda function-->Lambda function: Process 2 out of 10 batch items
    Lambda function--xLambda function: Fail on 3rd batch item
    Lambda function-->Lambda function: Process messages from another MessageGroupID
    Lambda function->>Lambda service: Report 3rd batch item and all messages within the same MessageGroupID as failure
    deactivate Lambda function
    activate SQS queue
    Lambda service->>SQS queue: Delete successful messages processed
    SQS queue-->>SQS queue: Failed messages return
    deactivate SQS queue
```

*SQS FIFO mechanism with Batch Item Failures*

#### Kinesis and DynamoDB Streams

> Read more about [Batch Failure Reporting feature](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-batchfailurereporting).

Sequence diagram to explain how `BatchProcessor` works with both [Kinesis Data Streams](#processing-messages-from-kinesis) and [DynamoDB Streams](#processing-messages-from-dynamodb).

For brevity, we will use `Streams` to refer to either services. For theory on stream checkpoints, see this [blog post](https://aws.amazon.com/blogs/compute/optimizing-batch-processing-with-custom-checkpoints-in-aws-lambda/)

```
sequenceDiagram
    autonumber
    participant Streams
    participant Lambda service
    participant Lambda function
    Lambda service->>Streams: Poll latest records
    Lambda service->>Lambda function: Invoke (batch event)
    activate Lambda function
    Lambda function-->Lambda function: Process 2 out of 10 batch items
    Lambda function--xLambda function: Fail on 3rd batch item
    Lambda function-->Lambda function: Continue processing batch items (4-10)
    Lambda function->>Lambda service: Report batch item as failure (3)
    deactivate Lambda function
    activate Streams
    Lambda service->>Streams: Checkpoints to sequence number from 3rd batch item
    Lambda service->>Streams: Poll records starting from updated checkpoint
    deactivate Streams
```

*Kinesis and DynamoDB streams mechanism with single batch item failure*

The behavior changes slightly when there are multiple item failures. Stream checkpoint is updated to the lowest sequence number reported.

Note that the batch item sequence number could be different from batch item number in the illustration.

```
sequenceDiagram
    autonumber
    participant Streams
    participant Lambda service
    participant Lambda function
    Lambda service->>Streams: Poll latest records
    Lambda service->>Lambda function: Invoke (batch event)
    activate Lambda function
    Lambda function-->Lambda function: Process 2 out of 10 batch items
    Lambda function--xLambda function: Fail on 3-5 batch items
    Lambda function-->Lambda function: Continue processing batch items (6-10)
    Lambda function->>Lambda service: Report batch items as failure (3-5)
    deactivate Lambda function
    activate Streams
    Lambda service->>Streams: Checkpoints to lowest sequence number
    Lambda service->>Streams: Poll records starting from updated checkpoint
    deactivate Streams
```

*Kinesis and DynamoDB streams mechanism with multiple batch item failures*

## Advanced

### Parser integration

The Batch Processing utility integrates with the [Parser utility](https://docs.aws.amazon.com/powertools/typescript/latest/features/parser/index.md) to automatically validate and parse each batch record before processing. This ensures your record handler receives properly typed and validated data, eliminating the need for manual parsing and validation.

To enable parser integration, import the `parser` function from `@aws-lambda-powertools/batch/parser` and pass it along with a schema when instantiating the `BatchProcessor`. This requires you to also [install the Parser utility](https://docs.aws.amazon.com/powertools/typescript/latest/features/parser/#getting-started).

```
import { parser } from '@aws-lambda-powertools/batch/parser';

```

You have two approaches for schema validation:

1. **Item schema only** (`innerSchema`) - Focus on your payload schema, we handle extending the base event structure
1. **Full event schema** (`schema`) - Validate the entire event record structure with complete control

#### Benefits of parser integration

Parser integration eliminates runtime errors from malformed data and provides compile-time type safety, making your code more reliable and easier to maintain. Invalid records are automatically marked as failed and won't reach your handler, reducing defensive coding.

```
const recordHandler = async (record: SQSRecord) => {
  // Manual parsing with no type safety
  const payload = JSON.parse(record.body); // any type
  console.log(payload.name); // No autocomplete, runtime errors possible
};

```

```
const mySchema = z.object({ name: z.string(), age: z.number() });

const recordHandler = async (record: ParsedRecord<SQSRecord, z.infer<typeof mySchema>>) => {
  // Automatic validation and strong typing
  console.log(record.body.name); // Full type safety and autocomplete
};

```

#### Using item schema only

When you want to focus on validating your payload without dealing with the full event structure, use `innerSchema`. We automatically extend the base event schema for you, reducing boilerplate code while still validating the entire record.

Available transformers by event type:

| Event Type | Base Schema               | Available Transformers | When to use transformer                                        |
| ---------- | ------------------------- | ---------------------- | -------------------------------------------------------------- |
| SQS        | `SqsRecordSchema`         | `json`, `base64`       | `json` for stringified JSON, `base64` for encoded data         |
| Kinesis    | `KinesisDataStreamRecord` | `base64`               | Required for Kinesis data (always base64 encoded)              |
| DynamoDB   | `DynamoDBStreamRecord`    | `unmarshall`           | Required to convert DynamoDB attribute values to plain objects |

```
import {
  BatchProcessor,
  EventType,
  processPartialResponse,
} from '@aws-lambda-powertools/batch';
import { parser } from '@aws-lambda-powertools/batch/parser';
import type { ParsedRecord } from '@aws-lambda-powertools/batch/types';
import { Logger } from '@aws-lambda-powertools/logger';
import type { SQSHandler, SQSRecord } from 'aws-lambda';
import { z } from 'zod';

const myItemSchema = z.object({
  name: z.string(),
  age: z.number(),
});

const logger = new Logger();
const processor = new BatchProcessor(EventType.SQS, {
  parser,
  innerSchema: myItemSchema,
  transformer: 'json',
  logger,
});

const recordHandler = async ({
  messageId,
  body: { name, age },
}: ParsedRecord<SQSRecord, z.infer<typeof myItemSchema>>) => {
  logger.info(`Processing record ${messageId}`, { name, age });
};

export const handler: SQSHandler = async (event, context) =>
  processPartialResponse(event, recordHandler, processor, {
    context,
  });

```

```
{
  "Records": [
    {
      "messageId": "059f36b4-87a3-44ab-83d2-661975830a7d",
      "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a",
      "body": "{\"name\": \"test-1\",\"age\": 20}",
      "attributes": {
        "ApproximateReceiveCount": "1",
        "SentTimestamp": "1545082649183",
        "SenderId": "AIDAIENQZJOLO23YVJ4VO",
        "ApproximateFirstReceiveTimestamp": "1545082649185"
      },
      "messageAttributes": {},
      "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-2: 123456789012:my-queue",
      "awsRegion": "us-east-1"
    },
    {
      "messageId": "244fc6b4-87a3-44ab-83d2-361172410c3a",
      "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a",
      "body": "{\"name\": \"test-2\",\"age\": 30}",
      "attributes": {
        "ApproximateReceiveCount": "1",
        "SentTimestamp": "1545082649183",
        "SenderId": "AIDAIENQZJOLO23YVJ4VO",
        "ApproximateFirstReceiveTimestamp": "1545082649185"
      },
      "messageAttributes": {},
      "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-2: 123456789012:my-queue",
      "awsRegion": "us-east-1"
    }
  ]
}

```

Note

If `innerSchema` is used with DynamoDB streams, the schema will be applied to both the `NewImage` and the `OldImage` by default. If you want to have dedicated schemas, see the section below.

#### Using full event schema

For complete control over validation, extend the built-in schemas with your custom payload schema. This approach gives you full control over the entire event structure.

```
import {
  BatchProcessor,
  EventType,
  processPartialResponse,
} from '@aws-lambda-powertools/batch';
import { parser } from '@aws-lambda-powertools/batch/parser';
import type { ParsedRecord } from '@aws-lambda-powertools/batch/types';
import { Logger } from '@aws-lambda-powertools/logger';
import { JSONStringified } from '@aws-lambda-powertools/parser/helpers';
import { SqsRecordSchema } from '@aws-lambda-powertools/parser/schemas';
import type { SqsRecord } from '@aws-lambda-powertools/parser/types';
import type { SQSHandler } from 'aws-lambda';
import { z } from 'zod';

const myItemSchema = JSONStringified(
  z.object({ name: z.string(), age: z.number() })
);

const logger = new Logger();
const processor = new BatchProcessor(EventType.SQS, {
  parser,
  schema: SqsRecordSchema.extend({
    body: myItemSchema,
  }),
  logger,
});

const recordHandler = async ({
  messageId,
  body: { name, age },
}: ParsedRecord<SqsRecord, z.infer<typeof myItemSchema>>) => {
  logger.info(`Processing record ${messageId}`, { name, age });
};

export const handler: SQSHandler = async (event, context) =>
  processPartialResponse(event, recordHandler, processor, {
    context,
  });

```

```
import {
  BatchProcessor,
  EventType,
  processPartialResponse,
} from '@aws-lambda-powertools/batch';
import { parser } from '@aws-lambda-powertools/batch/parser';
import type { ParsedRecord } from '@aws-lambda-powertools/batch/types';
import { Logger } from '@aws-lambda-powertools/logger';
import { Base64Encoded } from '@aws-lambda-powertools/parser/helpers';
import {
  KinesisDataStreamRecord,
  KinesisDataStreamRecordPayload,
} from '@aws-lambda-powertools/parser/schemas/kinesis';
import type { KinesisDataStreamRecordEvent } from '@aws-lambda-powertools/parser/types';
import type { KinesisStreamHandler } from 'aws-lambda';
import { z } from 'zod';

const myItemSchema = Base64Encoded(
  z.object({
    name: z.string(),
    age: z.number(),
  })
);

const logger = new Logger();
const processor = new BatchProcessor(EventType.KinesisDataStreams, {
  parser,
  schema: KinesisDataStreamRecord.extend({
    kinesis: KinesisDataStreamRecordPayload.extend({
      data: myItemSchema,
    }),
  }),
  logger,
});

const recordHandler = async ({
  kinesis: {
    sequenceNumber,
    data: { name, age },
  },
}: ParsedRecord<
  KinesisDataStreamRecordEvent,
  z.infer<typeof myItemSchema>
>) => {
  logger.info(`Processing record: ${sequenceNumber}`, {
    name,
    age,
  });
};

export const handler: KinesisStreamHandler = async (event, context) =>
  processPartialResponse(event, recordHandler, processor, {
    context,
  });

```

```
import {
  BatchProcessor,
  EventType,
  processPartialResponse,
} from '@aws-lambda-powertools/batch';
import { parser } from '@aws-lambda-powertools/batch/parser';
import type { ParsedRecord } from '@aws-lambda-powertools/batch/types';
import { Logger } from '@aws-lambda-powertools/logger';
import { DynamoDBMarshalled } from '@aws-lambda-powertools/parser/helpers/dynamodb';
import {
  DynamoDBStreamChangeRecordBase,
  DynamoDBStreamRecord,
} from '@aws-lambda-powertools/parser/schemas/dynamodb';
import type { DynamoDBRecord, DynamoDBStreamHandler } from 'aws-lambda';
import { z } from 'zod';

const myItemSchema = DynamoDBMarshalled(
  z.object({ name: z.string(), age: z.number() })
);

const logger = new Logger();
const processor = new BatchProcessor(EventType.SQS, {
  parser,
  schema: DynamoDBStreamRecord.extend({
    dynamodb: DynamoDBStreamChangeRecordBase.extend({
      NewImage: myItemSchema,
    }),
  }),
  logger,
});

const recordHandler = async ({
  eventID,
  dynamodb: {
    NewImage: { name, age },
  },
}: ParsedRecord<DynamoDBRecord, z.infer<typeof myItemSchema>>) => {
  logger.info(`Processing record ${eventID}`, { name, age });
};

export const handler: DynamoDBStreamHandler = async (event, context) =>
  processPartialResponse(event, recordHandler, processor, {
    context,
  });

```

#### Typed record handlers with ParsedRecord

To get full type safety in your record handlers, use the `ParsedRecord` utility type:

```
import type { ParsedRecord } from '@aws-lambda-powertools/batch';

// For most cases - single schema
type MyRecord = ParsedRecord<SQSRecord, z.infer<typeof mySchema>>;

// For DynamoDB - separate schemas for NewImage and OldImage
type MyDynamoRecord = ParsedRecord<DynamoDBRecord, z.infer<typeof newSchema>, z.infer<typeof oldSchema>>;

```

This eliminates verbose type annotations and provides clean autocompletion for your parsed data.

### Accessing processed messages

Use the `BatchProcessor` directly in your function to access a list of all returned values from your `recordHandler` function.

- **When successful**. We will include a tuple with `success`, the result of `recordHandler`, and the batch record
- **When failed**. We will include a tuple with `fail`, exception as a string, and the batch record

```
import { BatchProcessor, EventType } from '@aws-lambda-powertools/batch';
import { Logger } from '@aws-lambda-powertools/logger';
import type { SQSHandler, SQSRecord } from 'aws-lambda';

const processor = new BatchProcessor(EventType.SQS);
const logger = new Logger();

const recordHandler = (record: SQSRecord): void => {
  const payload = record.body;
  if (payload) {
    const item = JSON.parse(payload);
    logger.info('Processed item', { item });
  }
};

export const handler: SQSHandler = async (event, context) => {
  const batch = event.Records; // (1)!

  processor.register(batch, recordHandler, { context }); // (2)!
  const processedMessages = await processor.process();

  for (const message of processedMessages) {
    const [status, error, record] = message;

    logger.info('Processed record', { status, record, error });
  }

  return processor.response();
};

```

1. The processor requires the records array. This is typically handled by `processPartialResponse`.
1. You need to register the `batch`, the `recordHandler` function, and optionally the `context` to access the Lambda context.

### Accessing Lambda Context

Within your `recordHandler` function, you might need access to the Lambda context to determine how much time you have left before your function times out.

We can automatically inject the [Lambda context](https://docs.aws.amazon.com/lambda/latest/dg/typescript-context.html) into your `recordHandler` as optional second argument if you pass it to the `processPartialResponse` function.

```
import {
  BatchProcessor,
  EventType,
  processPartialResponse,
} from '@aws-lambda-powertools/batch';
import { Logger } from '@aws-lambda-powertools/logger';
import type { Context, SQSHandler, SQSRecord } from 'aws-lambda';

const processor = new BatchProcessor(EventType.SQS);
const logger = new Logger();

const recordHandler = (record: SQSRecord, lambdaContext?: Context): void => {
  const payload = record.body;
  if (payload) {
    const item = JSON.parse(payload);
    logger.info('Processed item', { item });
  }
  if (lambdaContext) {
    logger.info('Remaining time', {
      time: lambdaContext.getRemainingTimeInMillis(),
    });
  }
};

export const handler: SQSHandler = async (event, context) =>
  processPartialResponse(event, recordHandler, processor, {
    context,
  });

```

### Working with full batch failures

By default, the `BatchProcessor` will throw a `FullBatchFailureError` if all records in the batch fail to process, we do this to reflect the failure in your operational metrics.

When working with functions that handle batches with a small number of records, or when you use errors as a flow control mechanism, this behavior might not be desirable as your function might generate an unnaturally high number of errors. When this happens, the [Lambda service will scale down the concurrency of your function](https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-errorhandling.html#services-sqs-backoff-strategy), potentially impacting performance.

For these scenarios, you can set the `throwOnFullBatchFailure` option to `false` when calling.

```
import {
  BatchProcessor,
  EventType,
  processPartialResponse,
} from '@aws-lambda-powertools/batch';
import type { SQSHandler, SQSRecord } from 'aws-lambda';

const processor = new BatchProcessor(EventType.SQS);

const recordHandler = async (_record: SQSRecord): Promise<void> => {
  // Process the record
};

export const handler: SQSHandler = async (event, context) =>
  processPartialResponse(event, recordHandler, processor, {
    context,
    throwOnFullBatchFailure: false,
  });

```

### Extending BatchProcessor

You might want to bring custom logic to the existing `BatchProcessor` to slightly override how we handle successes and failures.

For these scenarios, you can subclass `BatchProcessor` and quickly override `successHandler` and `failureHandler` methods:

- **`successHandler()`** â Keeps track of successful batch records
- **`failureHandler()`** â Keeps track of failed batch records

Let's suppose you'd like to add a metric named `BatchRecordFailures` for each batch record that failed processing

```
import {
  BatchProcessor,
  EventType,
  processPartialResponse,
} from '@aws-lambda-powertools/batch';
import type {
  EventSourceDataClassTypes,
  FailureResponse,
} from '@aws-lambda-powertools/batch/types';
import { Logger } from '@aws-lambda-powertools/logger';
import { Metrics, MetricUnit } from '@aws-lambda-powertools/metrics';
import type { SQSHandler, SQSRecord } from 'aws-lambda';

class MyProcessor extends BatchProcessor {
  #metrics: Metrics;

  public constructor(eventType: keyof typeof EventType) {
    super(eventType);
    this.#metrics = new Metrics({ namespace: 'test' });
  }

  public failureHandler(
    record: EventSourceDataClassTypes,
    error: Error
  ): FailureResponse {
    this.#metrics.addMetric('BatchRecordFailures', MetricUnit.Count, 1);

    return super.failureHandler(record, error);
  }
}

const processor = new MyProcessor(EventType.SQS);
const logger = new Logger();

const recordHandler = (record: SQSRecord): void => {
  const payload = record.body;
  if (payload) {
    const item = JSON.parse(payload);
    logger.info('Processed item', { item });
  }
};

export const handler: SQSHandler = async (event, context) =>
  processPartialResponse(event, recordHandler, processor, {
    context,
  });

```

### Sequential processing

By default, the `BatchProcessor` processes records in parallel using `Promise.all()`. However, if you need to preserve the order of records, you can set the `processInParallel` option to `false` to process records sequentially.

If the `processInParallel` option is not provided, the `BatchProcessor` will process records in parallel.

When processing records from SQS FIFO queues, we recommend using the [`SqsFifoPartialProcessor`](#fifo-queues) class, which guarantees ordering of records and implements a short-circuit mechanism to skip processing records from a different message group ID.

```
import {
  BatchProcessor,
  EventType,
  processPartialResponse,
} from '@aws-lambda-powertools/batch';
import type { SQSHandler, SQSRecord } from 'aws-lambda';

const processor = new BatchProcessor(EventType.SQS);

const recordHandler = async (_record: SQSRecord): Promise<void> => {
  // Process the record
};

export const handler: SQSHandler = async (event, context) =>
  processPartialResponse(event, recordHandler, processor, {
    context,
    processInParallel: false,
  });

```

### Create your own partial processor

You can create your own partial batch processor from scratch by inheriting the `BasePartialProcessor` class, and implementing the `prepare()`, `clean()`, `processRecord()` and `processRecordSync()` abstract methods.

```
classDiagram
    direction LR
    class BasePartialProcessor {
        <<interface>>
        +prepare()
        +clean()
        +processRecord(record: BaseRecord)
        +processRecordSync(record: BaseRecord)
    }
    class YourCustomProcessor {
        +prepare()
        +clean()
        +processRecord(record: BaseRecord)
        +processRecordSyc(record: BaseRecord)
    }
    BasePartialProcessor <|-- YourCustomProcessor : extends
```

*Visual representation to bring your own processor*

- **`prepare()`** â called once as part of the processor initialization
- **`clean()`** â teardown logic called once after `processRecord` completes
- **`processRecord()`** â If you need to implement asynchronous logic, use this method, otherwise define it in your class with empty logic
- **`processRecordSync()`** â handles all processing logic for each individual message of a batch, including calling the `recordHandler` (`this.handler`)

You can then pass this class to `processPartialResponse` to process the records in your Lambda handler function.

```
import { randomInt } from 'node:crypto';
import {
  BasePartialBatchProcessor,
  EventType,
  processPartialResponse,
} from '@aws-lambda-powertools/batch';
import type {
  BaseRecord,
  FailureResponse,
  SuccessResponse,
} from '@aws-lambda-powertools/batch/types';
import {
  BatchWriteItemCommand,
  DynamoDBClient,
} from '@aws-sdk/client-dynamodb';
import { marshall } from '@aws-sdk/util-dynamodb';
import type { SQSHandler } from 'aws-lambda';

const tableName = process.env.TABLE_NAME || 'table-not-found';

class MyPartialProcessor extends BasePartialBatchProcessor {
  #tableName: string;
  #client?: DynamoDBClient;

  public constructor(tableName: string) {
    super(EventType.SQS);
    this.#tableName = tableName;
  }

  /**
   * It's called once, **after** processing the batch.
   *
   * Here we are writing all the processed messages to DynamoDB.
   */
  public clean(): void {
    // biome-ignore lint/style/noNonNullAssertion: We know that the client is defined because clean() is called after prepare()
    this.#client!.send(
      new BatchWriteItemCommand({
        RequestItems: {
          [this.#tableName]: this.successMessages.map((message) => ({
            PutRequest: {
              Item: marshall(message),
            },
          })),
        },
      })
    );
  }

  /**
   * It's called once, **before** processing the batch.
   *
   * It initializes a new client and cleans up any existing data.
   */
  public prepare(): void {
    this.#client = new DynamoDBClient({});
    this.successMessages = [];
  }

  public async processRecord(
    _record: BaseRecord
  ): Promise<SuccessResponse | FailureResponse> {
    throw new Error('Not implemented');
  }

  /**
   * It handles how your record is processed.
   *
   * Here we are keeping the status of each run, `this.handler` is
   * the function that is passed when calling `processor.register()`.
   */
  public processRecordSync(
    record: BaseRecord
  ): SuccessResponse | FailureResponse {
    try {
      const result = this.handler(record);

      return this.successHandler(record, result);
    } catch (error) {
      return this.failureHandler(record, error as Error);
    }
  }
}

const processor = new MyPartialProcessor(tableName);

const recordHandler = (): number => {
  return Math.floor(randomInt(1, 10));
};

export const handler: SQSHandler = async (event, context) =>
  processPartialResponse(event, recordHandler, processor, {
    context,
  });

```

## Tracing with AWS X-Ray

You can use Tracer to create subsegments for each batch record processed. To do so, you can open a new subsegment for each record, and close it when you're done processing it. When adding annotations and metadata to the subsegment, you can do so directly without calling `tracer.setSegment(subsegment)`. This allows you to work with the subsegment directly and avoid having to either pass the parent subsegment around or have to restore the parent subsegment at the end of the record processing.

```
import {
  BatchProcessor,
  EventType,
  processPartialResponse,
} from '@aws-lambda-powertools/batch';
import { Tracer } from '@aws-lambda-powertools/tracer';
import { captureLambdaHandler } from '@aws-lambda-powertools/tracer/middleware';
import middy from '@middy/core';
import type { SQSEvent, SQSHandler, SQSRecord } from 'aws-lambda';

const processor = new BatchProcessor(EventType.SQS);
const tracer = new Tracer({ serviceName: 'serverlessAirline' });

const recordHandler = async (record: SQSRecord): Promise<void> => {
  const subsegment = tracer.getSegment()?.addNewSubsegment('### recordHandler'); // (1)!
  subsegment?.addAnnotation('messageId', record.messageId); // (2)!

  const payload = record.body;
  if (payload) {
    try {
      const item = JSON.parse(payload);
      // do something with the item
      subsegment?.addMetadata('item', item);
    } catch (error) {
      subsegment?.addError(error as Error);
      throw error;
    }
  }

  subsegment?.close(); // (3)!
};

export const handler: SQSHandler = middy(async (event: SQSEvent, context) =>
  processPartialResponse(event, recordHandler, processor, {
    context,
  })
).use(captureLambdaHandler(tracer));

```

1. Retrieve the current segment, then create a subsegment for the record being processed
1. You can add annotations and metadata to the subsegment directly without calling `tracer.setSegment(subsegment)`
1. Close the subsegment when you're done processing the record

## Testing your code

As there is no external calls, you can unit test your code with `BatchProcessor` quite easily.

**Example**:

Given a SQS batch where the first batch record succeeds and the second fails processing, we should have a single item reported in the function response.

```
import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';
import { handler, processor } from './gettingStartedSQS.js';

const context = {
  callbackWaitsForEmptyEventLoop: true,
  functionVersion: '$LATEST',
  functionName: 'foo-bar-function',
  memoryLimitInMB: '128',
  logGroupName: '/aws/lambda/foo-bar-function-123456abcdef',
  logStreamName: '2021/03/09/[$LATEST]abcdef123456abcdef123456abcdef123456',
  invokedFunctionArn:
    'arn:aws:lambda:eu-west-1:123456789012:function:foo-bar-function',
  awsRequestId: 'c6af9ac6-7b61-11e6-9a41-93e812345678',
  getRemainingTimeInMillis: () => 1234,
  done: () => console.log('Done!'),
  fail: () => console.log('Failed!'),
  succeed: () => console.log('Succeeded!'),
};

describe('Function tests', () => {
  it('returns one failed message', async () => {
    // Prepare
    const event = JSON.parse(
      readFileSync('./samples/sampleSQSEvent.json', 'utf8')
    );
    const processorResult = processor; // access processor for additional assertions
    const successfulRecord = event.Records[0];
    const failedRecord = event.Records[1];
    const expectedResponse = {
      batchItemFailures: [
        {
          itemIdentifier: failedRecord.messageId,
        },
      ],
    };

    // Act
    const response = await handler(event, context, () => {});

    // Assess
    expect(response).toEqual(expectedResponse);
    expect(processorResult.failureMessages).toHaveLength(1);
    expect(processorResult.successMessages[0]).toEqual(successfulRecord);
  });
});

```

```
import {
  BatchProcessor,
  EventType,
  processPartialResponse,
} from '@aws-lambda-powertools/batch';
import { Logger } from '@aws-lambda-powertools/logger';
import type { SQSHandler, SQSRecord } from 'aws-lambda';

const processor = new BatchProcessor(EventType.SQS); // (1)!
const logger = new Logger();

// biome-ignore format: we need the comment in the next line to stay there to annotate the code snippet in the docs
const recordHandler = async (record: SQSRecord): Promise<void> => { // (2)!
  const payload = record.body;
  if (payload) {
    const item = JSON.parse(payload);
    logger.info('Processed item', { item });
  }
};

export const handler: SQSHandler = async (event, context) =>
  // biome-ignore format: we need the comment in the next line to stay there to annotate the code snippet in the docs
  processPartialResponse(event, recordHandler, processor, { // (3)!
    context,
  });

export { processor };

```

```
{
  "Records": [
    {
      "messageId": "059f36b4-87a3-44ab-83d2-661975830a7d",
      "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a",
      "body": "{\"Message\": \"success\"}",
      "attributes": {
        "ApproximateReceiveCount": "1",
        "SentTimestamp": "1545082649183",
        "SenderId": "AIDAIENQZJOLO23YVJ4VO",
        "ApproximateFirstReceiveTimestamp": "1545082649185"
      },
      "messageAttributes": {},
      "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-2: 123456789012:my-queue",
      "awsRegion": "us-east-1"
    },
    {
      "messageId": "244fc6b4-87a3-44ab-83d2-361172410c3a",
      "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a",
      "body": "SGVsbG8sIHRoaXMgaXMgYSB0ZXN0Lg==",
      "attributes": {
        "ApproximateReceiveCount": "1",
        "SentTimestamp": "1545082649183",
        "SenderId": "AIDAIENQZJOLO23YVJ4VO",
        "ApproximateFirstReceiveTimestamp": "1545082649185"
      },
      "messageAttributes": {},
      "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-2: 123456789012:my-queue",
      "awsRegion": "us-east-1"
    }
  ]
}

```

Built-in [JMESPath](https://jmespath.org/) functions to easily deserialize common encoded JSON payloads in Lambda functions.

## Key features

- Deserialize JSON from JSON strings, base64, and compressed data
- Use JMESPath to extract and combine data recursively
- Provides commonly used JMESPath expressions with popular event sources

## Getting started

### Installation

Install the utility in your project:

```
npm install @aws-lambda-powertools/jmespath

```

You might have events that contain encoded JSON payloads as string, base64, or even in compressed format. It is a common use case to decode and extract them partially or fully as part of your Lambda function invocation.

Powertools for AWS Lambda (TypeScript) also have utilities like [idempotency](https://docs.aws.amazon.com/powertools/typescript/latest/features/idempotency/index.md) where you might need to extract a portion of your data before using them.

Terminology

**Envelope** is the terminology we use for the **JMESPath expression** to extract your JSON object from your data input. We might use those two terms interchangeably.

### Extracting data

You can use the `extractDataFromEnvelope` function with any [JMESPath expression](https://jmespath.org/tutorial.html).

Tip

Another common use case is to fetch deeply nested data, filter, flatten, and more.

```
import { extractDataFromEnvelope } from '@aws-lambda-powertools/jmespath/envelopes';

type MyEvent = {
  body: string; // "{\"customerId\":\"dd4649e6-2484-4993-acb8-0f9123103394\"}"
  deeplyNested: Array<{ someData: number[] }>;
};

type MessageBody = {
  customerId: string;
};

export const handler = async (event: MyEvent): Promise<unknown> => {
  const payload = extractDataFromEnvelope<MessageBody>(
    event,
    'powertools_json(body)'
  );
  const { customerId } = payload; // now deserialized

  // also works for fetching and flattening deeply nested data
  const someData = extractDataFromEnvelope<number[]>(
    event,
    'deeplyNested[*].someData[]'
  );

  return {
    customerId,
    message: 'success',
    context: someData,
    statusCode: 200,
  };
};

```

```
{
  "body": "{\"customerId\":\"dd4649e6-2484-4993-acb8-0f9123103394\"}",
  "deeplyNested": [
    {
      "someData": [1, 2, 3]
    }
  ]
}

```

### Built-in envelopes

We provide built-in envelopes for popular AWS Lambda event sources to easily decode and/or deserialize JSON objects.

```
import {
  extractDataFromEnvelope,
  SQS,
} from '@aws-lambda-powertools/jmespath/envelopes';
import { Logger } from '@aws-lambda-powertools/logger';
import type { SQSEvent } from 'aws-lambda';

const logger = new Logger();

type MessageBody = {
  customerId: string;
};

export const handler = async (event: SQSEvent): Promise<void> => {
  const records = extractDataFromEnvelope<Array<MessageBody>>(event, SQS);
  for (const record of records) {
    // records is now a list containing the deserialized body of each message
    const { customerId } = record;
    logger.appendKeys({ customerId });
  }
};

```

```
{
  "Records": [
    {
      "messageId": "19dd0b57-b21e-4ac1-bd88-01bbb068cb78",
      "receiptHandle": "MessageReceiptHandle",
      "body": "{\"customerId\":\"dd4649e6-2484-4993-acb8-0f9123103394\",\"booking\":{\"id\":\"5b2c4803-330b-42b7-811a-c68689425de1\",\"reference\":\"ySz7oA\",\"outboundFlightId\":\"20c0d2f2-56a3-4068-bf20-ff7703db552d\"},\"payment\":{\"receipt\":\"https://pay.stripe.com/receipts/acct_1Dvn7pF4aIiftV70/ch_3JTC14F4aIiftV700iFq2CHB/rcpt_K7QsrFln9FgFnzUuBIiNdkkRYGxUL0X\",\"amount\":100}}",
      "attributes": {
        "ApproximateReceiveCount": "1",
        "SentTimestamp": "1523232000000",
        "SenderId": "123456789012",
        "ApproximateFirstReceiveTimestamp": "1523232000001"
      },
      "messageAttributes": {},
      "md5OfBody": "7b270e59b47ff90a553787216d55d91d",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-1:123456789012:MyQueue",
      "awsRegion": "us-east-1"
    }
  ]
}

```

These are all built-in envelopes you can use along with their expression as a reference:

| Envelope                          | JMESPath expression                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------- |
| **`API_GATEWAY_HTTP`**            | `powertools_json(body)`                                                                   |
| **`API_GATEWAY_REST`**            | `powertools_json(body)`                                                                   |
| **`CLOUDWATCH_EVENTS_SCHEDULED`** | `detail`                                                                                  |
| **`CLOUDWATCH_LOGS`**             | \`awslogs.powertools_base64_gzip(data)                                                    |
| **`EVENTBRIDGE`**                 | `detail`                                                                                  |
| **`KINESIS_DATA_STREAM`**         | `Records[*].kinesis.powertools_json(powertools_base64(data))`                             |
| **`S3_EVENTBRIDGE_SQS`**          | `Records[*].powertools_json(body).detail`                                                 |
| **`S3_KINESIS_FIREHOSE`**         | `records[*].powertools_json(powertools_base64(data)).Records[0]`                          |
| **`S3_SNS_KINESIS_FIREHOSE`**     | `records[*].powertools_json(powertools_base64(data)).powertools_json(Message).Records[0]` |
| **`S3_SNS_SQS`**                  | `Records[*].powertools_json(body).powertools_json(Message).Records[0]`                    |
| **`S3_SQS`**                      | `Records[*].powertools_json(body).Records[0]`                                             |
| **`SNS`**                         | \`Records[0].Sns.Message                                                                  |
| **`SQS`**                         | `Records[*].powertools_json(body)`                                                        |

Using SNS?

If you don't require SNS metadata, enable [raw message delivery](https://docs.aws.amazon.com/sns/latest/dg/sns-large-payload-raw-message-delivery.html). It will reduce multiple payload layers and size, when using SNS in combination with other services (*e.g., SQS, S3, etc*).

## Advanced

### Built-in JMESPath functions

You can use our built-in JMESPath functions within your envelope expression. They handle deserialization for common data formats found in AWS Lambda event sources such as JSON strings, base64, and uncompress gzip data.

#### `powertools_json` function

Use `powertools_json` function to decode any JSON string anywhere a JMESPath expression is allowed.

> **Idempotency scenario**

This sample will deserialize the JSON string within the `body` key before [Idempotency](https://docs.aws.amazon.com/powertools/typescript/latest/features/idempotency/index.md) processes it.

```
import { randomUUID } from 'node:crypto';
import {
  IdempotencyConfig,
  makeIdempotent,
} from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import type { APIGatewayEvent } from 'aws-lambda';

const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'IdempotencyTable',
});

export const handler = makeIdempotent(
  async (event: APIGatewayEvent) => {
    const body = JSON.parse(event.body || '{}');
    const { user, productId } = body;

    const result = await createSubscriptionPayment(user, productId);

    return {
      statusCode: 200,
      body: JSON.stringify({
        paymentId: result.id,
        message: 'success',
      }),
    };
  },
  {
    persistenceStore,
    config: new IdempotencyConfig({
      eventKeyJmesPath: 'powertools_json(body)',
    }),
  }
);

const createSubscriptionPayment = async (
  user: string,
  productId: string
): Promise<{ id: string; message: string }> => {
  const payload = { user, productId };
  const response = await fetch('https://httpbin.org/anything', {
    method: 'POST',
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error('Failed to create subscription payment');
  }

  return { id: randomUUID(), message: 'paid' };
};

```

```
{
  "version": "2.0",
  "routeKey": "ANY /createpayment",
  "rawPath": "/createpayment",
  "rawQueryString": "",
  "headers": {
    "Header1": "value1",
    "Header2": "value2"
  },
  "requestContext": {
    "accountId": "123456789012",
    "apiId": "api-id",
    "domainName": "id.execute-api.us-east-1.amazonaws.com",
    "domainPrefix": "id",
    "http": {
      "method": "POST",
      "path": "/createpayment",
      "protocol": "HTTP/1.1",
      "sourceIp": "ip",
      "userAgent": "agent"
    },
    "requestId": "id",
    "routeKey": "ANY /createpayment",
    "stage": "$default",
    "time": "10/Feb/2021:13:40:43 +0000",
    "timeEpoch": 1612964443723
  },
  "body": "{\"user\":\"xyz\",\"product_id\":\"123456789\"}",
  "isBase64Encoded": false
}

```

#### `powertools_base64` function

Use `powertools_base64` function to decode any base64 data.

This sample will decode the base64 value within the `data` key, and deserialize the JSON string before processing.

```
import { extractDataFromEnvelope } from '@aws-lambda-powertools/jmespath/envelopes';
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger();

export const handler = async (event: { payload: string }): Promise<void> => {
  const data = extractDataFromEnvelope<string>(
    event,
    'powertools_json(powertools_base64(payload))'
  );

  logger.info('Decoded payload', { data }); // (1)!
};

```

1. The `data` variable contains the decoded object that looks like this:

   ```
   {
       user_id: 123,
       product_id: 1,
       quantity: 2,
       price: 10.4,
       currency: 'USD',
   }

   ```

```
{
  "payload": "eyJ1c2VyX2lkIjogMTIzLCAicHJvZHVjdF9pZCI6IDEsICJxdWFudGl0eSI6IDIsICJwcmljZSI6IDEwLjQwLCAiY3VycmVuY3kiOiAiVVNEIn0="
}

```

#### `powertools_base64_gzip` function

Use `powertools_base64_gzip` function to decompress and decode base64 data.

This sample will decompress and decode base64 data from Cloudwatch Logs, then use JMESPath pipeline expression to pass the result for decoding its JSON string.

```
import { extractDataFromEnvelope } from '@aws-lambda-powertools/jmespath/envelopes';
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger();

export const handler = async (event: { payload: string }): Promise<void> => {
  const logGroup = extractDataFromEnvelope<string>(
    event, // (1)!
    'powertools_base64_gzip(payload) | powertools_json(@).logGroup'
  );

  logger.info('Log group name', { logGroup }); // (2)!
};

```

1. The `payload` key contains a JSON object that once decompressed and decoded looks like this:

   ```
   {
       "owner": "123456789012",
       "logGroup": "/aws/lambda/powertools-example",
       "logStream": "2020/09/02/[$LATEST]d3a8dcaffc7f4de2b8db132e3e106660",
       "subscriptionFilters": ["Destination"],
       "messageType": "DATA_MESSAGE",
       "logEvents": [
           {
               "id": "eventId1",
               "message": {
                   "username": "lessa",
                   "message": "hello world"
               },
               "timestamp": 1440442987000
           },
           {
               "id": "eventId2",
               "message": {
                   "username": "dummy",
                   "message": "hello world"
               },
               "timestamp": 1440442987001
           }
       ]
   }

   ```

1. The `logGroup` variable contains the string `"/aws/lambda/powertools-example"`.

```
{
  "payload": "H4sIACZAXl8C/52PzUrEMBhFX2UILpX8tPbHXWHqIOiq3Q1F0ubrWEiakqTWofTdTYYB0YWL2d5zvnuTFellBIOedoiyKH5M0iwnlKH7HZL6dDB6ngLDfLFYctUKjie9gHFaS/sAX1xNEq525QxwFXRGGMEkx4Th491rUZdV3YiIZ6Ljfd+lfSyAtZloacQgAkqSJCGhxM6t7cwwuUGPz4N0YKyvO6I9WDeMPMSo8Z4Ca/kJ6vMEYW5f1MX7W1lVxaG8vqX8hNFdjlc0iCBBSF4ERT/3Pl7RbMGMXF2KZMh/C+gDpNS7RRsp0OaRGzx0/t8e0jgmcczyLCWEePhni/23JWalzjdu0a3ZvgEaNLXeugEAAA=="
}

```

### Bring your own JMESPath function

Warning

This should only be used for advanced use cases where you have special formats not covered by the built-in functions.

For special binary formats that you want to decode before processing, you can bring your own JMESPath function by extending the `PowertoolsFunctions` class.

Here is an example of how to decompress messages compressed using the [Brotli compression algorithm](https://nodejs.org/api/zlib.html#zlibbrotlidecompressbuffer-options-callback):

```
 import { brotliDecompressSync } from 'node:zlib';
 import { fromBase64 } from '@aws-lambda-powertools/commons/utils/base64';
 import { extractDataFromEnvelope } from '@aws-lambda-powertools/jmespath/envelopes';
 import { PowertoolsFunctions } from '@aws-lambda-powertools/jmespath/functions';
 import { Logger } from '@aws-lambda-powertools/logger';

 const logger = new Logger();

 class CustomFunctions extends PowertoolsFunctions {
   @PowertoolsFunctions.signature({ // (1)!
     argumentsSpecs: [['string']],
     variadic: false,
   })
   public funcDecodeBrotliCompression(value: string): string { // (2)!
     const encoded = fromBase64(value, 'base64');
     const uncompressed = brotliDecompressSync(encoded);

     return uncompressed.toString();
   }
 }

 export const handler = async (event: { payload: string }): Promise<void> => {
   const message = extractDataFromEnvelope<string>(
     event,
     'Records[*].decode_brotli_compression(notification) | [*].powertools_json(@).message',
     { customFunctions: new CustomFunctions() }
   );

   logger.info('Decoded message', { message });
 };

```

1. The function signature can be enforced at runtime by using the `@Functions.signature` decorator.
1. The name of the function must start with the `func` prefix.

```
{
  "Records": [
    {
      "application": "app",
      "datetime": "2022-01-01T00:00:00.000Z",
      "notification": "GyYA+AXhZKk/K5DkanoQSTYpSKMwwxXh8DRWVo9A1hLqAQ=="
    }
  ]
}

```

This utility provides data validation and parsing for [Standard Schema](https://github.com/standard-schema/standard-schema), together with a collection of built-in [Zod](https://zod.dev) schemas and envelopes to parse and unwrap popular AWS event sources payloads.

## Key features

- Accept a [Standard Schema](https://github.com/standard-schema/standard-schema) and parse incoming payloads
- Built-in Zod schemas and envelopes to unwrap and validate popular AWS event sources payloads
- Extend and customize built-in Zod schemas to fit your needs
- Safe parsing option to avoid throwing errors and allow custom error handling
- Available as Middy.js middleware and TypeScript class method decorator

## Getting started

```
npm install @aws-lambda-powertools/parser zod

```

## Parse events

You can parse inbound events using `parser` decorator, Middy.js middleware, or [manually](#manual-parsing) using built-in envelopes and schemas.

When using the decorator or middleware, you can specify a schema to parse the event, this can be a [built-in Zod schema](#built-in-schemas) or a custom schema you defined. Custom schemas can be defined using Zod or any other [Standard Schema compatible library](https://standardschema.dev/#what-schema-libraries-implement-the-spec).

```
import { Logger } from '@aws-lambda-powertools/logger';
import { parser } from '@aws-lambda-powertools/parser/middleware';
import middy from '@middy/core';
import { z } from 'zod';

const logger = new Logger();

const orderSchema = z.object({
  id: z.number().positive(),
  description: z.string(),
  items: z.array(
    z.object({
      id: z.number().positive(),
      quantity: z.number().positive(),
      description: z.string(),
    })
  ),
  optionalField: z.string().optional(),
});

export const handler = middy()
  .use(parser({ schema: orderSchema }))
  .handler(async (event): Promise<void> => {
    for (const item of event.items) {
      // item is parsed as OrderItem
      logger.info('Processing item', { item });
    }
  });

```

```
import { Logger } from '@aws-lambda-powertools/logger';
import { parser } from '@aws-lambda-powertools/parser/middleware';
import middy from '@middy/core';
import {
  array,
  number,
  object,
  optional,
  pipe,
  string,
  toMinValue,
} from 'valibot';

const logger = new Logger();

const orderSchema = object({
  id: pipe(number(), toMinValue(0)),
  description: string(),
  items: array(
    object({
      id: pipe(number(), toMinValue(0)),
      quantity: pipe(number(), toMinValue(1)),
      description: string(),
    })
  ),
  optionalField: optional(string()),
});

export const handler = middy()
  .use(parser({ schema: orderSchema }))
  .handler(async (event): Promise<void> => {
    for (const item of event.items) {
      // item is parsed as OrderItem
      logger.info('Processing item', { item });
    }
  });

```

Warning

The decorator and middleware will replace the event object with the parsed schema if successful. Be cautious when using multiple decorators that expect an event to have a specific structure, the order of evaluation for decorators is from the inner to the outermost decorator.

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Logger } from '@aws-lambda-powertools/logger';
import { parser } from '@aws-lambda-powertools/parser';
import type { Context } from 'aws-lambda';
import { z } from 'zod';

const logger = new Logger();

const orderSchema = z.object({
  id: z.number().positive(),
  description: z.string(),
  items: z.array(
    z.object({
      id: z.number().positive(),
      quantity: z.number(),
      description: z.string(),
    })
  ),
  optionalField: z.string().optional(),
});

type Order = z.infer<typeof orderSchema>;

class Lambda implements LambdaInterface {
  @parser({ schema: orderSchema })
  public async handler(event: Order, _context: Context): Promise<void> {
    // event is now typed as Order
    for (const item of event.items) {
      logger.info('Processing item', { item });
    }
  }
}

const myFunction = new Lambda();
export const handler = myFunction.handler.bind(myFunction);

```

## Built-in schemas

**Parser** comes with the following built-in Zod schemas:

Looking for other libraries?

The built-in schemas are defined using Zod, if you would like us to support other libraries like [valibot](https://valibot.dev) please [open an issue](https://github.com/aws-powertools/powertools-lambda-typescript/issues/new?template=feature_request.yml) and we will consider it based on the community's feedback.

| Model name                                   | Description                                                                           |
| -------------------------------------------- | ------------------------------------------------------------------------------------- |
| **AlbSchema**                                | Lambda Event Source payload for Amazon Application Load Balancer                      |
| **APIGatewayProxyEventSchema**               | Lambda Event Source payload for Amazon API Gateway                                    |
| **APIGatewayRequestAuthorizerEventSchema**   | Lambda Event Source payload for Amazon API Gateway Request Authorizer                 |
| **APIGatewayTokenAuthorizerEventSchema**     | Lambda Event Source payload for Amazon API Gateway Token Authorizer                   |
| **APIGatewayProxyEventV2Schema**             | Lambda Event Source payload for Amazon API Gateway v2 payload                         |
| **APIGatewayProxyWebsocketEventSchema**      | Lambda Event Source payload for Amazon API Gateway WebSocket events                   |
| **APIGatewayRequestAuthorizerEventV2Schema** | Lambda Event Source payload for Amazon API Gateway v2 Authorizer                      |
| **AppSyncResolverSchema**                    | Lambda Event Source payload for AWS AppSync GraphQL API resolver                      |
| **AppSyncBatchResolverSchema**               | Lambda Event Source payload for AWS AppSync GraphQL API batch resolver                |
| **AppSyncEventsPublishSchema**               | Lambda Event Source payload for AWS AppSync Events API `PUBLISH` operation            |
| **AppSyncEventsSubscribeSchema**             | Lambda Event Source payload for AWS AppSync Events API `SUBSCRIBE` operation          |
| **CloudFormationCustomResourceCreateSchema** | Lambda Event Source payload for AWS CloudFormation `CREATE` operation                 |
| **CloudFormationCustomResourceUpdateSchema** | Lambda Event Source payload for AWS CloudFormation `UPDATE` operation                 |
| **CloudFormationCustomResourceDeleteSchema** | Lambda Event Source payload for AWS CloudFormation `DELETE` operation                 |
| **CloudwatchLogsSchema**                     | Lambda Event Source payload for Amazon CloudWatch Logs                                |
| **PreSignupTriggerSchema**                   | Lambda Event Source payload for Amazon Cognito Pre Sign-up trigger                    |
| **PostConfirmationTriggerSchema**            | Lambda Event Source payload for Amazon Cognito Post Confirmation trigger              |
| **PreTokenGenerationTriggerSchema**          | Lambda Event Source payload for Amazon Cognito Pre Token Generation trigger           |
| **CustomMessageTriggerSchema**               | Lambda Event Source payload for Amazon Cognito Custom Message trigger                 |
| **MigrateUserTriggerSchema**                 | Lambda Event Source payload for Amazon Cognito User Migration trigger                 |
| **CustomSMSTriggerSchema**                   | Lambda Event Source payload for Amazon Cognito Custom SMS trigger                     |
| **CustomEmailTriggerSchema**                 | Lambda Event Source payload for Amazon Cognito Custom Email trigger                   |
| **DefineAuthChallengeTriggerSchema**         | Lambda Event Source payload for Amazon Cognito Define Auth Challenge trigger          |
| **CreateAuthChallengeTriggerSchema**         | Lambda Event Source payload for Amazon Cognito Create Auth Challenge trigger          |
| **VerifyAuthChallengeResponseTriggerSchema** | Lambda Event Source payload for Amazon Cognito Verify Auth Challenge Response trigger |
| **PreTokenGenerationTriggerSchemaV1**        | Lambda Event Source payload for Amazon Cognito Pre Token Generation trigger v1        |
| **PreTokenGenerationTriggerSchemaV2AndV3**   | Lambda Event Source payload for Amazon Cognito Pre Token Generation trigger v2 and v3 |
| **DynamoDBStreamSchema**                     | Lambda Event Source payload for Amazon DynamoDB Streams                               |
| **EventBridgeSchema**                        | Lambda Event Source payload for Amazon EventBridge                                    |
| **KafkaMskEventSchema**                      | Lambda Event Source payload for AWS MSK payload                                       |
| **KafkaSelfManagedEventSchema**              | Lambda Event Source payload for self managed Kafka payload                            |
| **KinesisDataStreamSchema**                  | Lambda Event Source payload for Amazon Kinesis Data Streams                           |
| **KinesisFirehoseSchema**                    | Lambda Event Source payload for Amazon Kinesis Firehose                               |
| **KinesisDynamoDBStreamSchema**              | Lambda Event Source payload for DynamodbStream record wrapped in Kinesis Data stream  |
| **KinesisFirehoseSqsSchema**                 | Lambda Event Source payload for SQS messages wrapped in Kinesis Firehose records      |
| **LambdaFunctionUrlSchema**                  | Lambda Event Source payload for Lambda Function URL payload                           |
| **S3EventNotificationEventBridgeSchema**     | Lambda Event Source payload for Amazon S3 Event Notification to EventBridge.          |
| **S3Schema**                                 | Lambda Event Source payload for Amazon S3                                             |
| **S3ObjectLambdaEvent**                      | Lambda Event Source payload for Amazon S3 Object Lambda                               |
| **S3SqsEventNotificationSchema**             | Lambda Event Source payload for S3 event notifications wrapped in SQS event (S3->SQS) |
| **SesSchema**                                | Lambda Event Source payload for Amazon Simple Email Service                           |
| **SnsSchema**                                | Lambda Event Source payload for Amazon Simple Notification Service                    |
| **SqsSchema**                                | Lambda Event Source payload for Amazon SQS                                            |
| **TransferFamilySchema**                     | Lambda Event Source payload for AWS Transfer Family events                            |
| **VpcLatticeSchema**                         | Lambda Event Source payload for Amazon VPC Lattice                                    |
| **VpcLatticeV2Schema**                       | Lambda Event Source payload for Amazon VPC Lattice v2 payload                         |

### Extend built-in schemas

You can extend every built-in schema to include your own schema, and yet have all other known fields parsed along the way.

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Logger } from '@aws-lambda-powertools/logger';
import { parser } from '@aws-lambda-powertools/parser';
import { EventBridgeSchema } from '@aws-lambda-powertools/parser/schemas/eventbridge';
import type { Context } from 'aws-lambda';
import { z } from 'zod';

const logger = new Logger();

const orderSchema = z.object({
  id: z.number().positive(),
  description: z.string(),
  items: z.array(
    z.object({
      id: z.number().positive(),
      quantity: z.number(),
      description: z.string(),
    })
  ),
  optionalField: z.string().optional(),
});

const orderEventSchema = EventBridgeSchema.extend({
  detail: orderSchema, // (1)!
});

type OrderEvent = z.infer<typeof orderEventSchema>;

class Lambda implements LambdaInterface {
  @parser({ schema: orderEventSchema }) // (2)!
  public async handler(event: OrderEvent, _context: Context): Promise<void> {
    for (const item of event.detail.items) {
      // process OrderItem
      logger.info('Processing item', { item }); // (3)!
    }
  }
}

const myFunction = new Lambda();
export const handler = myFunction.handler.bind(myFunction);

```

1. Extend built-in `EventBridgeSchema` with your own detail schema
1. Pass the extended schema to `parser` decorator or middy middleware
1. `event` is validated including your custom schema and now available in your handler

```
{
  "version": "0",
  "id": "6a7e8feb-b491-4cf7-a9f1-bf3703467718",
  "detail-type": "OrderPurchased",
  "source": "OrderService",
  "account": "111122223333",
  "time": "2020-10-22T18:43:48Z",
  "region": "us-west-1",
  "resources": ["some_additional"],
  "detail": {
    "id": 10876546789,
    "description": "My order",
    "items": [
      {
        "id": 1015938732,
        "quantity": 1,
        "description": "item xpto"
      }
    ]
  }
}

```

### JSON stringified payloads

If you want to extend a schema and transform a JSON stringified payload to an object, you can use helper function `JSONStringified`:

```
import { JSONStringified } from '@aws-lambda-powertools/parser/helpers';
import { AlbSchema } from '@aws-lambda-powertools/parser/schemas/alb';
import { z } from 'zod';

const customSchema = z.object({
  name: z.string(),
  age: z.number(),
});

const extendedSchema = AlbSchema.extend({
  body: JSONStringified(customSchema), // (1)!
});

type _ExtendedAlbEvent = z.infer<typeof extendedSchema>;

```

1. Extend built-in `AlbSchema` using JSONStringified function to transform your payload

```
{
  "requestContext": {
    "elb": {
      "targetGroupArn": "arn:aws:elasticloadbalancing:us-east-2:123456789012:targetgroup/lambda-279XGJDqGZ5rsrHC2Fjr/49e9d65c45c6791a"
    }
  },
  "httpMethod": "GET",
  "path": "/lambda",
  "queryStringParameters": {
    "query": "1234ABCD"
  },
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "host": "lambda-alb-123578498.us-east-2.elb.amazonaws.com",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "x-amzn-trace-id": "Root=1-5c536348-3d683b8b04734faae651f476",
    "x-forwarded-for": "72.12.164.125",
    "x-forwarded-port": "80",
    "x-forwarded-proto": "http",
    "x-imforwards": "20"
  },
  "body": "{\"name\":\"Walter\", \"age\": 50}",
  "isBase64Encoded": false
}

```

```
 import { JSONStringified } from '@aws-lambda-powertools/parser/helpers';
 import { APIGatewayProxyEventV2Schema } from '@aws-lambda-powertools/parser/schemas/api-gatewayv2';
 import { z } from 'zod';

 const extendedSchema = APIGatewayProxyEventV2Schema.extend({ // (1)!
   body: JSONStringified(
     z.object({
       name: z.string(),
       age: z.number(),
     })
   ),
 });
 type _ExtendedAPIGatewayEvent = z.infer<typeof extendedSchema>;

```

1. This is compatible also with API Gateway REST API schemas

```
{
  "version": "2.0",
  "routeKey": "POST /lambda",
  "rawPath": "/lambda",
  "rawQueryString": "",
  "headers": {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate",
    "authorization": "Bearer foo",
    "content-length": "0",
    "host": "lsw1ro4ipb.execute-api.eu-west-1.amazonaws.com",
    "user-agent": "HTTPie/3.2.2",
    "x-amzn-trace-id": "Root=1-66705bc7-2b4257df30cbee696ef2cf28",
    "x-forwarded-for": "15.248.3.126",
    "x-forwarded-port": "443",
    "x-forwarded-proto": "https"
  },
  "requestContext": {
    "accountId": "123456789012",
    "apiId": "lsw1ro4ipb",
    "authorizer": {
      "lambda": null
    },
    "domainName": "lsw1ro4ipb.execute-api.eu-west-1.amazonaws.com",
    "domainPrefix": "lsw1ro4ipb",
    "http": {
      "method": "POST",
      "path": "/lambda",
      "protocol": "HTTP/1.1",
      "sourceIp": "15.248.3.126",
      "userAgent": "HTTPie/3.2.2"
    },
    "requestId": "ZhNHJhhLjoEEPiw=",
    "routeKey": "POST /lambda",
    "stage": "$default",
    "time": "17/Jun/2024:15:52:39 +0000",
    "timeEpoch": 1718639559080
  },
  "body": "{\"name\":\"John\",\"age\":42}",
  "isBase64Encoded": false
}

```

```
import { JSONStringified } from '@aws-lambda-powertools/parser/helpers';
import {
  SqsRecordSchema,
  SqsSchema,
} from '@aws-lambda-powertools/parser/schemas/sqs';
import { z } from 'zod';

const customSchema = z.object({
  name: z.string(),
  age: z.number(),
});

const extendedSchema = SqsSchema.extend({
  Records: z.array(
    SqsRecordSchema.extend({
      body: JSONStringified(customSchema),
    })
  ),
});

type _ExtendedSqsEvent = z.infer<typeof extendedSchema>;

```

```
{
  "Records": [
    {
      "messageId": "059f36b4-87a3-44ab-83d2-661975830a7d",
      "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a...",
      "body": "{\"name\": \"John Doe\", \"age\": 30}",
      "attributes": {
        "ApproximateReceiveCount": "1",
        "SentTimestamp": "1545082649183",
        "SenderId": "AIDAIENQZJOLO23YVJ4VO",
        "ApproximateFirstReceiveTimestamp": "1545082649185"
      },
      "messageAttributes": {
        "testAttr": {
          "stringValue": "100",
          "binaryValue": "base64Str",
          "dataType": "Number"
        }
      },
      "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:my-queue",
      "awsRegion": "us-east-2"
    },
    {
      "messageId": "2e1424d4-f796-459a-8184-9c92662be6da",
      "receiptHandle": "AQEBzWwaftRI0KuVm4tP+/7q1rGgNqicHq...",
      "body": "{\"name\": \"foo\", \"age\": 10}",
      "attributes": {
        "ApproximateReceiveCount": "1",
        "SentTimestamp": "1545082650636",
        "SenderId": "AIDAIENQZJOLO23YVJ4VO",
        "ApproximateFirstReceiveTimestamp": "1545082650649",
        "DeadLetterQueueSourceArn": "arn:aws:sqs:us-east-2:123456789012:my-queue-dead"
      },
      "messageAttributes": {},
      "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:my-queue",
      "awsRegion": "us-east-2"
    }
  ]
}

```

### DynamoDB Stream event parsing

If you want to parse a DynamoDB stream event with unmarshalling, you can use the helper function `DynamoDBMarshalled`:

```
import { DynamoDBMarshalled } from '@aws-lambda-powertools/parser/helpers/dynamodb';
import {
  DynamoDBStreamChangeRecordBase,
  DynamoDBStreamRecord,
  DynamoDBStreamSchema,
} from '@aws-lambda-powertools/parser/schemas/dynamodb';
import { z } from 'zod';

const customSchema = z.object({
  id: z.string(),
  message: z.string(),
});

const extendedSchema = DynamoDBStreamSchema.extend({
  Records: z.array(
    DynamoDBStreamRecord.extend({
      dynamodb: DynamoDBStreamChangeRecordBase.extend({
        NewImage: DynamoDBMarshalled(customSchema).optional(),
      }),
    })
  ),
});

type _ExtendedDynamoDBStreamEvent = z.infer<typeof extendedSchema>;

```

```
{
  "Records": [
    {
      "eventID": "1",
      "eventVersion": "1.0",
      "dynamodb": {
        "ApproximateCreationDateTime": 1693997155.0,
        "Keys": {
          "Id": {
            "N": "101"
          }
        },
        "NewImage": {
          "Message": {
            "S": "New item!"
          },
          "Id": {
            "N": "101"
          }
        },
        "StreamViewType": "NEW_AND_OLD_IMAGES",
        "SequenceNumber": "111",
        "SizeBytes": 26
      },
      "awsRegion": "us-west-2",
      "eventName": "INSERT",
      "eventSourceARN": "eventsource_arn",
      "eventSource": "aws:dynamodb"
    },
    {
      "eventID": "2",
      "eventVersion": "1.0",
      "dynamodb": {
        "OldImage": {
          "Message": {
            "S": "New item!"
          },
          "Id": {
            "N": "101"
          }
        },
        "SequenceNumber": "222",
        "Keys": {
          "Id": {
            "N": "101"
          }
        },
        "SizeBytes": 59,
        "NewImage": {
          "Message": {
            "S": "This item has changed"
          },
          "Id": {
            "N": "101"
          }
        },
        "StreamViewType": "NEW_AND_OLD_IMAGES"
      },
      "awsRegion": "us-west-2",
      "eventName": "MODIFY",
      "eventSourceARN": "source_arn",
      "eventSource": "aws:dynamodb"
    }
  ]
}

```

## Envelopes

When trying to parse your payload you might encounter the following situations:

- Your actual payload is wrapped around a known structure, for example Lambda Event Sources like EventBridge
- You're only interested in a portion of the payload, for example parsing the detail of custom events in EventBridge, or body of SQS records
- You can either solve these situations by creating a schema of these known structures, parsing them, then extracting and parsing a key where your payload is.

This can become difficult quite quickly. Parser simplifies the development through a feature named Envelope. Envelopes can be used via envelope parameter available in middy and decorator. Here's an example of parsing a custom schema in an event coming from EventBridge, where all you want is what's inside the detail key.

```
import { Logger } from '@aws-lambda-powertools/logger';
import { EventBridgeEnvelope } from '@aws-lambda-powertools/parser/envelopes/eventbridge';
import { parser } from '@aws-lambda-powertools/parser/middleware';
import middy from '@middy/core';
import { z } from 'zod';

const logger = new Logger();

const orderSchema = z.object({
  id: z.number().positive(),
  description: z.string(),
  items: z.array(
    z.object({
      id: z.number().positive(),
      quantity: z.number(),
      description: z.string(),
    })
  ),
  optionalField: z.string().optional(),
});

export const handler = middy()
  .use(parser({ schema: orderSchema, envelope: EventBridgeEnvelope }))
  .handler(async (event): Promise<void> => {
    for (const item of event.items) {
      // item is parsed as OrderItem
      logger.info('Processing item', { item });
    }
  });

```

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Logger } from '@aws-lambda-powertools/logger';
import { parser } from '@aws-lambda-powertools/parser';
import { EventBridgeEnvelope } from '@aws-lambda-powertools/parser/envelopes/eventbridge';
import type { Context } from 'aws-lambda';
import { z } from 'zod';

const logger = new Logger();

const orderSchema = z.object({
  id: z.number().positive(),
  description: z.string(),
  items: z.array(
    z.object({
      id: z.number().positive(),
      quantity: z.number(),
      description: z.string(),
    })
  ),
  optionalField: z.string().optional(),
});

type Order = z.infer<typeof orderSchema>;

class Lambda implements LambdaInterface {
  @parser({ schema: orderSchema, envelope: EventBridgeEnvelope }) // (1)!
  public async handler(event: Order, _context: Context): Promise<void> {
    // event is now typed as Order
    for (const item of event.items) {
      logger.info('Processing item', item); // (2)!
    }
  }
}

const myFunction = new Lambda();
export const handler = myFunction.handler.bind(myFunction);

```

1. Pass `eventBridgeEnvelope` to `parser` decorator
1. `event` is parsed and replaced as `Order` object

The envelopes are functions that take an event and the schema to parse, and return the result of the inner schema. Depending on the envelope it can be something simple like extracting a key. We have also complex envelopes that parse the payload from a string, decode base64, uncompress gzip, etc.

Envelopes vs schema extension

Use envelopes if you want to extract only the inner part of an event payload and don't use the information from the Lambda event. Otherwise, extend built-in schema to parse the whole payload and use the metadata from the Lambda event.

### Built-in envelopes

Parser comes with the following built-in Zod envelopes:

Looking for other libraries?

The built-in schemas are defined using Zod, if you would like us to support other libraries like [valibot](https://valibot.dev) please [open an issue](https://github.com/aws-powertools/powertools-lambda-typescript/issues/new?template=feature_request.yml) and we will consider it based on the community's feedback.

| Envelope name                 | Behaviour                                                                                                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ApiGatewayEnvelope**        | 1. Parses data using `APIGatewayProxyEventSchema`. 2. Parses `body` key using your schema and returns it.                                                                                         |
| **ApiGatewayV2Envelope**      | 1. Parses data using `APIGatewayProxyEventV2Schema`. 2. Parses `body` key using your schema and returns it.                                                                                       |
| **CloudWatchEnvelope**        | 1. Parses data using `CloudwatchLogsSchema` which will base64 decode and decompress it. 2. Parses records in `message` key using your schema and return them in a list.                           |
| **DynamoDBStreamEnvelope**    | 1. Parses data using `DynamoDBStreamSchema`. 2. Parses records in `NewImage` and `OldImage` keys using your schema. 3. Returns a list with a dictionary containing `NewImage` and `OldImage` keys |
| **EventBridgeEnvelope**       | 1. Parses data using `EventBridgeSchema`. 2. Parses `detail` key using your schema and returns it.                                                                                                |
| **KafkaEnvelope**             | 1. Parses data using `KafkaRecordSchema`. 2. Parses `value` key using your schema and returns it.                                                                                                 |
| **KinesisEnvelope**           | 1. Parses data using `KinesisDataStreamSchema` which will base64 decode it. 2. Parses records in `Records` key using your schema and returns them in a list.                                      |
| **KinesisFirehoseEnvelope**   | 1. Parses data using `KinesisFirehoseSchema` which will base64 decode it. 2. Parses records in `Records` key using your schema and returns them in a list.                                        |
| **LambdaFunctionUrlEnvelope** | 1. Parses data using `LambdaFunctionUrlSchema`. 2. Parses `body` key using your schema and returns it.                                                                                            |
| **SnsEnvelope**               | 1. Parses data using `SnsSchema`. 2. Parses records in `body` key using your schema and return them in a list.                                                                                    |
| **SnsSqsEnvelope**            | 1. Parses data using `SqsSchema`. 2. Parses SNS records in `body` key using `SnsNotificationSchema`. 3. Parses data in `Message` key using your schema and return them in a list.                 |
| **SnsEnvelope**               | 1. Parses data using `SqsSchema`. 2. Parses records in `body` key using your schema and return them in a list.                                                                                    |
| **VpcLatticeEnvelope**        | 1. Parses data using `VpcLatticeSchema`. 2. Parses `value` key using your schema and returns it.                                                                                                  |
| **VpcLatticeV2Envelope**      | 1. Parses data using `VpcLatticeSchema`. 2. Parses `value` key using your schema and returns it.                                                                                                  |

## Safe parsing

If you want to parse the event without throwing an error, use the `safeParse` option. The handler `event` object will be replaced with `ParsedResult<Input?, Oputput?>`, for example `ParsedResult<SqsEvent, Order>`, where `SqsEvent` is the original event and `Order` is the parsed schema.

The `ParsedResult` object will have `success`, `data`, or `error` and `originalEvent` fields, depending on the outcome. If the parsing is successful, the `data` field will contain the parsed event, otherwise you can access the `error` field and the `originalEvent` to handle the error and recover the original event.

```
import { Logger } from '@aws-lambda-powertools/logger';
import { parser } from '@aws-lambda-powertools/parser/middleware';
import middy from '@middy/core';
import { z } from 'zod';

const logger = new Logger();

const orderSchema = z.object({
  id: z.number().positive(),
  description: z.string(),
  items: z.array(
    z.object({
      id: z.number().positive(),
      quantity: z.number(),
      description: z.string(),
    })
  ),
  optionalField: z.string().optional(),
});

export const handler = middy()
  .use(
    parser({ schema: orderSchema, safeParse: true }) // (1)!
  )
  .handler(async (event): Promise<void> => {
    if (event.success) {
      for (const item of event.data.items) {
        logger.info('Processing item', { item }); // (2)!
      }
    } else {
      logger.error('Error parsing event', { event: event.error }); // (3)!
      logger.error('Original event', { event: event.originalEvent }); // (4)!
    }
  });

```

1. Use `safeParse` option to parse the event without throwing an error
1. Use `data` to access the parsed event when successful
1. Use `error` to handle the error message
1. Use `originalEvent` to get the original event and recover

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Logger } from '@aws-lambda-powertools/logger';
import { parser } from '@aws-lambda-powertools/parser';
import { EventBridgeEnvelope } from '@aws-lambda-powertools/parser/envelopes/eventbridge';
import type {
  EventBridgeEvent,
  ParsedResult,
} from '@aws-lambda-powertools/parser/types';
import type { Context } from 'aws-lambda';
import { z } from 'zod';

const logger = new Logger();

const orderSchema = z.object({
  id: z.number().positive(),
  description: z.string(),
  items: z.array(
    z.object({
      id: z.number().positive(),
      quantity: z.number(),
      description: z.string(),
    })
  ),
  optionalField: z.string().optional(),
});

type Order = z.infer<typeof orderSchema>;

class Lambda implements LambdaInterface {
  @parser({
    schema: orderSchema,
    envelope: EventBridgeEnvelope,
    safeParse: true, // (1)!
  })
  public async handler(
    event: ParsedResult<EventBridgeEvent, Order>,
    _context: Context
  ): Promise<void> {
    if (event.success) {
      for (const item of event.data.items) {
        logger.info('Processing item', { item }); // (2)!
      }
    } else {
      logger.error('Failed to parse event', { error: event.error }); // (3)!
      logger.error('Original event is ', { original: event.originalEvent }); // (4)!
    }
  }
}

const myFunction = new Lambda();
export const handler = myFunction.handler.bind(myFunction);

```

1. Use `safeParse` option to parse the event without throwing an error
1. Use `data` to access the parsed event when successful
1. Use `error` to handle the error message
1. Use `originalEvent` to get the original event and recover

## Manual parsing

You can use built-in envelopes and schemas to parse the incoming events manually, without using middy or decorator.

```
import { Logger } from '@aws-lambda-powertools/logger';
import { EventBridgeEnvelope } from '@aws-lambda-powertools/parser/envelopes/eventbridge';
import { EventBridgeSchema } from '@aws-lambda-powertools/parser/schemas/eventbridge';
import type { EventBridgeEvent } from '@aws-lambda-powertools/parser/types';
import type { Context } from 'aws-lambda';
import { z } from 'zod';

const logger = new Logger();

const orderSchema = z.object({
  id: z.number().positive(),
  description: z.string(),
  items: z.array(
    z.object({
      id: z.number().positive(),
      quantity: z.number(),
      description: z.string(),
    })
  ),
  optionalField: z.string().optional(),
});
type Order = z.infer<typeof orderSchema>;

export const handler = async (
  event: EventBridgeEvent,
  _context: Context
): Promise<void> => {
  const parsedEvent = EventBridgeSchema.parse(event); // (1)!
  logger.info('Parsed event', parsedEvent);

  const orders: Order = EventBridgeEnvelope.parse(event, orderSchema); // (2)!
  logger.info('Parsed orders', orders);
};

```

1. Use `EventBridgeSchema` to parse the event, the `details` fields will be parsed as a generic record.
1. Use `eventBridgeEnvelope` with a combination of `orderSchema` to get `Order` object from the `details` field.

```
import { Logger } from '@aws-lambda-powertools/logger';
import { EventBridgeEnvelope } from '@aws-lambda-powertools/parser/envelopes/eventbridge';
import { EventBridgeSchema } from '@aws-lambda-powertools/parser/schemas/eventbridge';
import type { EventBridgeEvent } from '@aws-lambda-powertools/parser/types';
import type { Context } from 'aws-lambda';
import { z } from 'zod';

const logger = new Logger();

const orderSchema = z.object({
  id: z.number().positive(),
  description: z.string(),
  items: z.array(
    z.object({
      id: z.number().positive(),
      quantity: z.number(),
      description: z.string(),
    })
  ),
  optionalField: z.string().optional(),
});

export const handler = async (
  event: EventBridgeEvent,
  _context: Context
): Promise<void> => {
  const parsedEvent = EventBridgeSchema.safeParse(event); // (1)!
  parsedEvent.success
    ? logger.info('Event parsed successfully', parsedEvent.data)
    : logger.error('Event parsing failed', parsedEvent.error);
  const parsedEvenlope = EventBridgeEnvelope.safeParse(event, orderSchema); // (2)!
  parsedEvenlope.success
    ? logger.info('Event envelope parsed successfully')
    : logger.error('Event envelope parsing failed', parsedEvenlope.error);
};

```

1. Use `safeParse` option to parse the event without throwing an error
1. `safeParse` is also available for envelopes

## Custom validation

Because Parser uses Zod, you can use all the features of Zod to validate your data. For example, you can use `refine` to validate a field or a combination of fields:

```
import { z } from 'zod';

const orderItemSchema = z.object({
  id: z.number().positive(),
  quantity: z.number(),
  description: z.string(),
});

export const orderSchema = z
  .object({
    id: z.number().positive(),
    description: z.string(),
    items: z.array(orderItemSchema).refine((items) => items.length > 0, {
      message: 'Order must have at least one item', // (1)!
    }),
    optionalField: z.string().optional(),
  })
  .refine((order) => order.id > 100 && order.items.length > 100, {
    message:
      'All orders with more than 100 items must have an id greater than 100', // (2)!
  });

```

1. validate a single field
1. validate an object with multiple fields

Zod provides a lot of other features and customization, see [Zod documentation](https://zod.dev) for more details.

## Types

### Schema and Type inference

Use `z.infer` to extract the type of the schema, so you can use types during development and avoid type errors.

```
import { Logger } from '@aws-lambda-powertools/logger';
import { parser } from '@aws-lambda-powertools/parser/middleware';
import middy from '@middy/core';
import type { Context } from 'aws-lambda';
import { z } from 'zod';

const logger = new Logger();

const orderSchema = z.object({
  id: z.number().positive(),
  description: z.string(),
  items: z.array(
    z.object({
      id: z.number().positive(),
      quantity: z.number(),
      description: z.string(),
    })
  ),
  optionalField: z.string().optional(),
});

type Order = z.infer<typeof orderSchema>; // (1)!

const lambdaHandler = async (
  event: Order, // (2)!
  _context: Context
): Promise<void> => {
  for (const item of event.items) {
    // item is parsed as OrderItem
    logger.info('Processing item', { item }); // (3)!
  }
};

export const handler = middy(lambdaHandler).use(
  parser({ schema: orderSchema })
);

```

1. Use `z.infer` to extract the type of the schema, also works for nested schemas
1. `event` is of type `Order`
1. infer types from deeply nested schemas

### Compatibility with `@types/aws-lambda`

The package `@types/aws-lambda` is a popular project that contains type definitions for many AWS service event invocations, support for these types is provided on a best effort basis.

We recommend using the types provided by the Parser utility under `@aws-powertools/parser/types` when using the built-in schemas and envelopes, as they are inferred directly from the Zod schemas and are more accurate.

If you encounter any type compatibility issues with `@types/aws-lambda`, please [submit an issue](https://github.com/aws-powertools/powertools-lambda-typescript/issues/new/choose).

## Testing your code

When testing your handler with [**parser decorator**](#parse-events) you need to use double assertion to bypass TypeScript type checking in your tests. This is useful when you want to test the handler for invalid payloads or when you want to test the error handling. If you are you use middy middleware, you don't need to do this.

```
import type { Context } from 'aws-lambda';
import { describe, expect, it } from 'vitest';
import { handler } from './decorator.js';
import type { Order } from './schema.js';

describe('Test handler', () => {
  it('should parse event successfully', async () => {
    const testEvent = {
      id: 123,
      description: 'test',
      items: [
        {
          id: 1,
          quantity: 1,
          description: 'item1',
        },
      ],
    };

    await expect(handler(testEvent, {} as Context)).resolves.toEqual(123);
  });

  it('should throw error if event is invalid', async () => {
    const testEvent = { foo: 'bar' };
    await expect(
      handler(
        testEvent as unknown as Order, // (1)!
        {} as Context
      )
    ).rejects.toThrow();
  });
});

```

1. Use double assertion `as unknown as X` to bypass TypeScript type checking in your tests

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Logger } from '@aws-lambda-powertools/logger';
import { parser } from '@aws-lambda-powertools/parser';
import type { Context } from 'aws-lambda';
import { type Order, orderSchema } from './schema.js';

const logger = new Logger();

class Lambda implements LambdaInterface {
  @parser({ schema: orderSchema })
  public async handler(event: Order, _context: Context): Promise<number> {
    logger.info('Processing event', { event });

    // ... business logic
    return event.id;
  }
}

const myFunction = new Lambda();
export const handler = myFunction.handler.bind(myFunction);

```

```
import { z } from 'zod';

const orderSchema = z.object({
  id: z.number().positive(),
  description: z.string(),
  items: z.array(
    z.object({
      id: z.number().positive(),
      quantity: z.number(),
      description: z.string(),
    })
  ),
  optionalField: z.string().optional(),
});

type Order = z.infer<typeof orderSchema>;

export { orderSchema, type Order };

```

This also works when using `safeParse` option.

```
import type {
  EventBridgeEvent,
  ParsedResult,
} from '@aws-lambda-powertools/parser/types';
import type { Context } from 'aws-lambda';
import { describe, expect, it } from 'vitest';
import { handler } from './safeParseDecorator.js';
import type { Order } from './schema.js';

describe('Test handler', () => {
  it('should parse event successfully', async () => {
    const testEvent = {
      version: '0',
      id: '6a7e8feb-b491-4cf7-a9f1-bf3703467718',
      'detail-type': 'OrderPurchased',
      source: 'OrderService',
      account: '111122223333',
      time: '2020-10-22T18:43:48Z',
      region: 'us-west-1',
      resources: ['some_additional'],
      detail: {
        id: 10876546789,
        description: 'My order',
        items: [
          {
            id: 1015938732,
            quantity: 1,
            description: 'item xpto',
          },
        ],
      },
    };

    await expect(
      handler(
        testEvent as unknown as ParsedResult<EventBridgeEvent, Order>, // (1)!
        {} as Context
      )
    ).resolves.toEqual(10876546789);
  });

  it('should throw error if event is invalid', async () => {
    const testEvent = { foo: 'bar' };
    await expect(
      handler(
        testEvent as unknown as ParsedResult<EventBridgeEvent, Order>,
        {} as Context
      )
    ).rejects.toThrow();
  });
});

```

1. Use double assertion to pass expected types to the handler

```
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Logger } from '@aws-lambda-powertools/logger';
import { parser } from '@aws-lambda-powertools/parser';
import { EventBridgeEnvelope } from '@aws-lambda-powertools/parser/envelopes/eventbridge';
import type {
  EventBridgeEvent,
  ParsedResult,
} from '@aws-lambda-powertools/parser/types';
import type { Context } from 'aws-lambda';
import { type Order, orderSchema } from './schema.js';

const logger = new Logger();

class Lambda implements LambdaInterface {
  @parser({
    schema: orderSchema,
    envelope: EventBridgeEnvelope,
    safeParse: true,
  })
  public async handler(
    event: ParsedResult<EventBridgeEvent, Order>,
    _context: Context
  ): Promise<number> {
    logger.info('Processing event', { event });
    if (event.success) {
      // ... business logic
      return event.data.id;
    }
    logger.error('Failed to parse event', { event });
    throw new Error('Failed to parse event');
  }
}

const myFunction = new Lambda();
export const handler = myFunction.handler.bind(myFunction);

```

```
import { z } from 'zod';

const orderSchema = z.object({
  id: z.number().positive(),
  description: z.string(),
  items: z.array(
    z.object({
      id: z.number().positive(),
      quantity: z.number(),
      description: z.string(),
    })
  ),
  optionalField: z.string().optional(),
});

type Order = z.infer<typeof orderSchema>;

export { orderSchema, type Order };

```

## Should I use this or Validation?

One of Powertools for AWS Lambda [tenets](https://docs.aws.amazon.com/powertools/typescript/latest/#tenets) is to be progressive. This means that our utilities are designed to be incrementally adopted by customers at any stage of their serverless journey.

For new projects, especially those using TypeScript, we recommend using the Parser utility. Thanks to its integration with [Zod](http://zod.dev), it provides an expressive and type-safe way to validate and parse payloads.

If instead you are already using JSON Schema, or simply feel more comfortable with it, the [Validation](https://docs.aws.amazon.com/powertools/typescript/latest/features/validation/index.md) utility is a great choice. It provides an opinionated thin layer on top of the popular [ajv](https://ajv.js.org) library, with built-in support for JMESPath and AWS service envelopes.

When it comes to feature set, besides the type-safe parsing, the Parser utility also provides a rich collection of built-in schemas and envelopes for AWS services. The Validation utility, on the other hand, follows a more bring-your-own-schema approach, with built-in support for JMESPath and AWS service envelopes to help you unwrap events before validation.

Additionally, while both utilities serve specific use cases, understanding your project requirements will help you choose the right tool for your validation needs.

Finally, in terms of bundle size, the Validation utility is slightly heavier than the Parser utility primarily due to ajv not providing ESM builds. However, even with this, the Validation utility still clocks in at under ~100KB when minified and bundled.

This utility provides [JSON Schema](https://json-schema.org) validation for events and responses, including JMESPath support to unwrap events before validation.

## Should I use this or Parser?

One of Powertools for AWS Lambda [tenets](https://docs.aws.amazon.com/powertools/typescript/latest/#tenets) is to be progressive. This means that our utilities are designed to be incrementally adopted by customers at any stage of their serverless journey.

For new projects, especially those using TypeScript, we recommend using the [Parser](https://docs.aws.amazon.com/powertools/typescript/latest/features/parser/index.md) utility. Thanks to its integration with [Zod](http://zod.dev), it provides an expressive and type-safe way to validate and parse payloads.

If instead you are already using JSON Schema, or simply feel more comfortable with it, the Validation utility is a great choice. It provides an opinionated thin layer on top of the popular [ajv](https://ajv.js.org) library, with built-in support for JMESPath and AWS service envelopes.

When it comes to feature set, besides the type-safe parsing, the Parser utility also provides a rich collection of built-in schemas and envelopes for AWS services. The Validation utility, on the other hand, follows a more bring-your-own-schema approach, with built-in support for JMESPath and AWS service envelopes to help you unwrap events before validation.

Additionally, while both utilities serve specific use cases, understanding your project requirements will help you choose the right tool for your validation needs.

Finally, in terms of bundle size, the Validation utility is slightly heavier than the Parser utility primarily due to ajv not providing ESM builds. However, even with this, the Validation utility still clocks in at under ~100KB when minified and bundled.

## Key features

- Validate incoming event and response payloads
- JMESPath support to unwrap events before validation
- Built-in envelope to unwrap popular AWS service events
- TypeScript support with type-safe validation

## Getting started

```
npm install @aws-lambda-powertools/validation

```

You can validate inbound and outbound payloads using the validator class method decorator or Middy.js middleware.

You can also use the standalone `validate` function, if you want more control over the validation process such as handling a validation error.

Using JSON Schemas for the first time?

Check this step-by-step guide on [how to create JSON Schemas](https://json-schema.org/learn/getting-started-step-by-step.html). By default, we support JSON Schema draft-07.

### Validator decorator

The `@validator` decorator is a class method decorator that you can use to validate both the incoming event and the response payload.

If the validation fails, we will throw a `SchemaValidationError`.

```
import { validator } from '@aws-lambda-powertools/validation/decorator';
import type { Context } from 'aws-lambda';
import {
  type InboundSchema,
  inboundSchema,
  type OutboundSchema,
  outboundSchema,
} from './schemas.js';

class Lambda {
  @validator({
    inboundSchema,
    outboundSchema,
  })
  async handler(
    event: InboundSchema,
    _context: Context
  ): Promise<OutboundSchema> {
    return {
      statusCode: 200,
      body: `Hello from ${event.userId}`,
    };
  }
}

const lambda = new Lambda();
export const handler = lambda.handler.bind(lambda);

```

```
const inboundSchema = {
  type: 'object',
  properties: {
    userId: {
      type: 'string',
    },
  },
  required: ['userId'],
} as const;

type InboundSchema = {
  userId: string;
};

const outboundSchema = {
  type: 'object',
  properties: {
    body: {
      type: 'string',
    },
    statusCode: {
      type: 'number',
    },
  },
  required: ['body', 'statusCode'],
} as const;

type OutboundSchema = {
  body: string;
  statusCode: number;
};

export {
  inboundSchema,
  outboundSchema,
  type InboundSchema,
  type OutboundSchema,
};

```

It's not mandatory to validate both the inbound and outbound payloads. You can either use one, the other, or both.

### Validator middleware

If you are using Middy.js, you can use the `validator` middleware to validate the incoming event and response payload.

A note on Middy.js

We officially support versions of Middy.js `v4.x` through `v6.x`

Check their docs to learn more about [Middy.js and its middleware stack](https://middy.js.org/docs/intro/getting-started) as well as [best practices when working with Powertools for AWS](https://middy.js.org/docs/integrations/lambda-powertools#best-practices).

Like the class method decorator, if the validation fails, we will throw a `SchemaValidationError`, and you don't need to use both the inbound and outbound schemas if you don't need to.

```
import { validator } from '@aws-lambda-powertools/validation/middleware';
import middy from '@middy/core';
import {
  type InboundSchema,
  inboundSchema,
  type OutboundSchema,
  outboundSchema,
} from './schemas.js';

export const handler = middy()
  .use(
    validator({
      inboundSchema,
      outboundSchema,
    })
  )
  .handler(
    async (event: InboundSchema): Promise<OutboundSchema> => ({
      statusCode: 200,
      body: `Hello from ${event.userId}`,
    })
  );

```

```
const inboundSchema = {
  type: 'object',
  properties: {
    userId: {
      type: 'string',
    },
  },
  required: ['userId'],
} as const;

type InboundSchema = {
  userId: string;
};

const outboundSchema = {
  type: 'object',
  properties: {
    body: {
      type: 'string',
    },
    statusCode: {
      type: 'number',
    },
  },
  required: ['body', 'statusCode'],
} as const;

type OutboundSchema = {
  body: string;
  statusCode: number;
};

export {
  inboundSchema,
  outboundSchema,
  type InboundSchema,
  type OutboundSchema,
};

```

### Standalone validation

The `validate` function gives you more control over the validation process, and is typically used within the Lambda handler, or any other function that performs validation.

You can also gracefully handle schema validation errors by catching `SchemaValidationError` errors.

```
import { Logger } from '@aws-lambda-powertools/logger';
import { validate } from '@aws-lambda-powertools/validation';
import { SchemaValidationError } from '@aws-lambda-powertools/validation/errors';
import { type InboundSchema, inboundSchema } from './schemas.js';

const logger = new Logger();

export const handler = async (event: InboundSchema) => {
  try {
    validate({
      payload: event,
      schema: inboundSchema,
    });

    return {
      message: 'ok', // (1)!
    };
  } catch (error) {
    if (error instanceof SchemaValidationError) {
      logger.error('Schema validation failed', error);
      throw new Error('Invalid event payload');
    }

    throw error;
  }
};

```

1. Since we are not validating the output, we can return anything

```
const inboundSchema = {
  type: 'object',
  properties: {
    userId: {
      type: 'string',
    },
  },
  required: ['userId'],
} as const;

type InboundSchema = {
  userId: string;
};

const outboundSchema = {
  type: 'object',
  properties: {
    body: {
      type: 'string',
    },
    statusCode: {
      type: 'number',
    },
  },
  required: ['body', 'statusCode'],
} as const;

type OutboundSchema = {
  body: string;
  statusCode: number;
};

export {
  inboundSchema,
  outboundSchema,
  type InboundSchema,
  type OutboundSchema,
};

```

### Unwrapping events prior to validation

In some cases you might want to validate only a portion of the event payload - this is what the `envelope` option is for.

Envelopes are [JMESPath expressions](https://jmespath.org/tutorial.html) to extract the part of the JSON you want before applying the JSON Schema validation.

Here is a sample custom EventBridge event, where we only want to validate the `detail` part of the event:

```
import { validator } from '@aws-lambda-powertools/validation/decorator';
import type { Context } from 'aws-lambda';
import { type InboundSchema, inboundSchema } from './schemas.js';

class Lambda {
  @validator({
    inboundSchema,
    envelope: 'detail',
  })
  async handler(event: InboundSchema, _context: Context) {
    return {
      message: `processed ${event.userId}`,
      success: true,
    };
  }
}

const lambda = new Lambda();
export const handler = lambda.handler.bind(lambda);

```

```
const inboundSchema = {
  type: 'object',
  properties: {
    userId: {
      type: 'string',
    },
  },
  required: ['userId'],
} as const;

type InboundSchema = {
  userId: string;
};

const outboundSchema = {
  type: 'object',
  properties: {
    body: {
      type: 'string',
    },
    statusCode: {
      type: 'number',
    },
  },
  required: ['body', 'statusCode'],
} as const;

type OutboundSchema = {
  body: string;
  statusCode: number;
};

export {
  inboundSchema,
  outboundSchema,
  type InboundSchema,
  type OutboundSchema,
};

```

```
{
  "version": "0",
  "id": "12345678-1234-1234-1234-123456789012",
  "detail-type": "myDetailType",
  "source": "myEventSource",
  "account": "123456789012",
  "time": "2017-12-22T18:43:48Z",
  "region": "us-west-2",
  "resources": [],
  "detail": {
    "userId": "123"
  }
}

```

This is quite powerful as it allows you to validate only the part of the event that you are interested in, and thanks to JMESPath, you can extract records from [arrays](https://jmespath.org/tutorial.html#list-and-slice-projections), combine [pipe](https://jmespath.org/tutorial.html#pipe-expressions) and filter expressions, and more.

When combined, these features allow you to extract and validate the exact part of the event you actually care about.

### Built-in envelopes

We provide built-in envelopes to easily extract payloads from popular AWS event sources.

Here is an example of how you can use the built-in envelope for SQS events:

```
import { SQS } from '@aws-lambda-powertools/jmespath/envelopes';
import { Logger } from '@aws-lambda-powertools/logger';
import { validator } from '@aws-lambda-powertools/validation/middleware';
import middy from '@middy/core';
import { type InboundSchema, inboundSchema } from './schemas.js';

const logger = new Logger();

export const handler = middy()
  .use(
    validator({
      inboundSchema,
      envelope: SQS,
    })
  )
  .handler(async (event: Array<InboundSchema>) => {
    for (const record of event) {
      logger.info(`Processing message ${record.userId}`);
    }
  });

```

```
const inboundSchema = {
  type: 'object',
  properties: {
    userId: {
      type: 'string',
    },
  },
  required: ['userId'],
} as const;

type InboundSchema = {
  userId: string;
};

const outboundSchema = {
  type: 'object',
  properties: {
    body: {
      type: 'string',
    },
    statusCode: {
      type: 'number',
    },
  },
  required: ['body', 'statusCode'],
} as const;

type OutboundSchema = {
  body: string;
  statusCode: number;
};

export {
  inboundSchema,
  outboundSchema,
  type InboundSchema,
  type OutboundSchema,
};

```

```
{
  "Records": [
    {
      "messageId": "c80e8021-a70a-42c7-a470-796e1186f753",
      "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a...",
      "body": "{\"userId\":\"123\"}",
      "attributes": {
        "ApproximateReceiveCount": "3",
        "SentTimestamp": "1529104986221",
        "SenderId": "AIDAIC6K7FJUZ7Q",
        "ApproximateFirstReceiveTimestamp": "1529104986230"
      },
      "messageAttributes": {},
      "md5OfBody": "098f6bcd4621d373cade4e832627b4f6",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-west-2:123456789012:my-queue",
      "awsRegion": "us-west-2"
    },
    {
      "messageId": "c80e8021-a70a-42c7-a470-796e1186f753",
      "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a...",
      "body": "{\"userId\":\"456\"}",
      "attributes": {
        "ApproximateReceiveCount": "3",
        "SentTimestamp": "1529104986221",
        "SenderId": "AIDAIC6K7FJUZ7Q",
        "ApproximateFirstReceiveTimestamp": "1529104986230"
      },
      "messageAttributes": {},
      "md5OfBody": "098f6bcd4621d373cade4e832627b4f6",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-west-2:123456789012:my-queue",
      "awsRegion": "us-west-2"
    }
  ]
}

```

For a complete list of built-in envelopes, check the [built-in envelopes section](https://docs.aws.amazon.com/powertools/typescript/latest/features/jmespath/#built-in-envelopes).

## Advanced

### Validating custom formats

While JSON Schema draft-07 has many new built-in formats such as date, time, and specifically a regex format which can be used in place of custom formats, you can also define your own custom formats.

This is useful when you have a specific format that is not covered by the built-in formats or when you don't control the schema.

JSON Schemas with custom formats like `awsaccountid` will fail validation if the format is not defined. You can define custom formats using the `formats` option to any of the validation methods.

```
{
  "type": "object",
  "properties": {
    "accountId": {
      "type": "string",
      "format": "awsaccountid"
    },
    "creditCard": {
      "type": "string",
      "format": "creditcard"
    }
  },
  "required": ["accountId"]
}

```

For each one of these custom formats, you need to tell us how to validate them. To do so, you can either pass a `RegExp` object or a function that receives the value and returns a boolean.

For example, to validate using the schema above, you can define a custom format for `awsaccountid` like this:

```
import { Logger } from '@aws-lambda-powertools/logger';
import { validate } from '@aws-lambda-powertools/validation';
import { SchemaValidationError } from '@aws-lambda-powertools/validation/errors';
import schemaWithCustomFormat from './samples/schemaWithCustomFormat.json';

const logger = new Logger();

const customFormats = {
  awsaccountid: /^\d{12}$/,
  creditcard: (value: string) => {
    // Luhn algorithm (for demonstration purposes only - do not use in production)
    const sum = value
      .split('')
      .reverse()
      .reduce((acc, digit, index) => {
        const num = Number.parseInt(digit, 10);
        return acc + (index % 2 === 0 ? num : num < 5 ? num * 2 : num * 2 - 9);
      }, 0);

    return sum % 10 === 0;
  },
};

export const handler = async (event: unknown) => {
  try {
    await validate({
      payload: event,
      schema: schemaWithCustomFormat,
      formats: customFormats,
    });

    return {
      message: 'ok',
    };
  } catch (error) {
    if (error instanceof SchemaValidationError) {
      logger.error('Schema validation failed', error);
      throw new Error('Invalid event payload');
    }

    throw error;
  }
};

```

### Built-in JMESpath functions

In some cases, your payloads might require some transformation before validation. For example, you might want to parse a JSON string or decode a base64 string before validating the payload.

For this, you can use our buil-in JMESPath functions within your expressions. We have a few built-in functions that you can use:

- [`powertools_json()`](https://docs.aws.amazon.com/powertools/typescript/latest/features/jmespath/#powertools_json-function): Parses a JSON string
- [`powertools_base64()`](https://docs.aws.amazon.com/powertools/typescript/latest/features/jmespath/#powertools_base64-function): Decodes a base64 string
- [`powertools_base64_gzip()`](https://docs.aws.amazon.com/powertools/typescript/latest/features/jmespath/#powertools_base64_gzip-function): Decodes a base64 string and unzips it

We use these functions for [built-in envelopes](#built-in-envelopes) to easily decode and unwrap events from sources like Kinesis, SQS, S3, and more.

### Validating with external references

JSON Schema allows schemas to reference other schemas using the `$ref` keyword. This is useful when you have a common schema that you want to reuse across multiple schemas.

You can use the `externalRefs` option to pass a list of schemas that you want to reference in your inbound and outbound schemas.

```
import { validator } from '@aws-lambda-powertools/validation/decorator';
import type { Context } from 'aws-lambda';
import {
  defsSchema,
  type InboundSchema,
  inboundSchema,
  outboundSchema,
} from './schemasWithExternalRefs.js';

class Lambda {
  @validator({
    inboundSchema,
    outboundSchema,
    externalRefs: [defsSchema],
  })
  async handler(event: InboundSchema, _context: Context) {
    return {
      message: `processed ${event.userId}`,
      success: true,
    };
  }
}

const lambda = new Lambda();
export const handler = lambda.handler.bind(lambda);

```

```
const defsSchema = {
  $id: 'http://example.com/schemas/defs.json',
  definitions: {
    int: { type: 'integer' },
    str: { type: 'string' },
  },
} as const;

const inboundSchema = {
  $id: 'http://example.com/schemas/inbound.json',
  type: 'object',
  properties: {
    userId: { $ref: 'defs.json#/definitions/str' },
  },
  required: ['userId'],
} as const;

type InboundSchema = {
  userId: string;
};

const outboundSchema = {
  $id: 'http://example.com/schemas/outbound.json',
  type: 'object',
  properties: {
    body: { $ref: 'defs.json#/definitions/str' },
    statusCode: { $ref: 'defs.json#/definitions/int' },
  },
  required: ['body', 'statusCode'],
} as const;

type OutboundSchema = {
  body: string;
  statusCode: number;
};

export {
  defsSchema,
  inboundSchema,
  outboundSchema,
  type InboundSchema,
  type OutboundSchema,
};

```

### Bringing your own `ajv` instance

By default, we use JSON Schema draft-07. If you want to use a different draft, you can pass your own `ajv` instance to any of the validation methods.

This is also useful if you want to configure `ajv` with custom options like keywords and more.

```
import { Logger } from '@aws-lambda-powertools/logger';
import { validate } from '@aws-lambda-powertools/validation';
import { SchemaValidationError } from '@aws-lambda-powertools/validation/errors';
import Ajv2019 from 'ajv/dist/2019';
import { inboundSchema } from './schemas.js';

const logger = new Logger();

const ajv = new Ajv2019();

export const handler = async (event: unknown) => {
  try {
    await validate({
      payload: event,
      schema: inboundSchema,
      ajv, // (1)!
    });

    return {
      message: 'ok',
    };
  } catch (error) {
    if (error instanceof SchemaValidationError) {
      logger.error('Schema validation failed', error);
      throw new Error('Invalid event payload');
    }

    throw error;
  }
};

```

1. You can pass your own `ajv` instance to any of the validation methods. This is useful if you want to configure `ajv` with custom options like keywords and more.

The Kafka Consumer utility transparently handles message deserialization, provides an intuitive developer experience, and integrates seamlessly with the rest of the Powertools for AWS Lambda ecosystem.

```
flowchart LR
  KafkaTopic["Kafka Topic"] --> MSK["Amazon MSK"]
  KafkaTopic --> MSKServerless["Amazon MSK Serverless"]
  KafkaTopic --> SelfHosted["Self-hosted Kafka"]
  MSK --> EventSourceMapping["Event Source Mapping"]
  MSKServerless --> EventSourceMapping
  SelfHosted --> EventSourceMapping
  EventSourceMapping --> Lambda["Lambda Function"]
  Lambda --> KafkaConsumer["Kafka Consumer Utility"]
  KafkaConsumer --> Deserialization["Deserialization"]
  Deserialization --> YourLogic["Your Business Logic"]
```

## Key features

- Automatic deserialization of Kafka messages (JSON, Avro, and Protocol Buffers)
- Simplified event record handling with intuitive interface
- Support for key and value deserialization
- Support for [Standard Schema](https://github.com/standard-schema/standard-schema) output parsing (e.g., Zod, Valibot, ArkType)
- Support for Event Source Mapping (ESM) with and without Schema Registry integration
- Out of the box error handling for deserialization issues

## Terminology

**Event Source Mapping (ESM)** A Lambda feature that reads from streaming sources (like Kafka) and invokes your Lambda function. It manages polling, batching, and error handling automatically, eliminating the need for consumer management code.

**Record Key and Value** A Kafka messages contain two important parts: an optional key that determines the partition and a value containing the actual message data. Both are base64-encoded in Lambda events and can be independently deserialized.

**Deserialization** The process of converting binary data (base64-encoded in Lambda events) into usable Python objects according to a specific format like JSON, Avro, or Protocol Buffers. Powertools handles this conversion automatically.

**SchemaConfig class** Contains parameters that tell Powertools how to interpret message data, including the format type (JSON, Avro, Protocol Buffers) and optional schema definitions needed for binary formats.

**Output parsing** A [Standard Schema](https://github.com/standard-schema/standard-schema) used to parse your data at runtime, allowing you to define how the deserialized data should be structured and validated.

**Schema Registry** A centralized service that stores and validates schemas, ensuring producers and consumers maintain compatibility when message formats evolve over time.

## Moving from traditional Kafka consumers

Lambda processes Kafka messages as discrete events rather than continuous streams, requiring a different approach to consumer development that Powertools for AWS helps standardize.

| Aspect                | Traditional Kafka Consumers         | Lambda Kafka Consumer                                          |
| --------------------- | ----------------------------------- | -------------------------------------------------------------- |
| **Model**             | Pull-based (you poll for messages)  | Push-based (Lambda invoked with messages)                      |
| **Scaling**           | Manual scaling configuration        | Automatic scaling to partition count                           |
| **State**             | Long-running application with state | Stateless, ephemeral executions                                |
| **Offsets**           | Manual offset management            | Automatic offset commitment                                    |
| **Schema Validation** | Client-side schema validation       | Optional Schema Registry integration with Event Source Mapping |
| **Error Handling**    | Per-message retry control           | Batch-level retry policies                                     |

## Getting started

### Installation

Depending on the schema types you want to use, install the library and the corresponding libraries:

```
npm install @aws-lambda-powertools/kafka

```

```
npm install @aws-lambda-powertools/kafka avro-js

```

```
npm install @aws-lambda-powertools/kafka protobufjs

```

Additionally, if you want to use output parsing with [Standard Schema](https://github.com/standard-schema/standard-schema), you can install [any of the supported libraries](https://standardschema.dev/#what-schema-libraries-implement-the-spec), for example: Zod, Valibot, or ArkType.

### Required resources

To use the Kafka consumer utility, you need an AWS Lambda function configured with a Kafka event source. This can be Amazon MSK, MSK Serverless, or a self-hosted Kafka cluster.

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Resources:
  KafkaConsumerFunction:
    Type: AWS::Serverless::Function
    Properties:
      Runtime: nodejs24.x
      Handler: index.js
      Timeout: 30
      Events:
        MSKEvent:
          Type: MSK
          Properties:
            StartingPosition: LATEST
            Stream: !GetAtt MyMSKCluster.Arn
            Topics:
              - my-topic-1
              - my-topic-2
      Policies:
        - AWSLambdaMSKExecutionRole

```

### Using ESM with Schema Registry

The Event Source Mapping configuration determines which mode is used. With `JSON`, Lambda converts all messages to JSON before invoking your function. With `SOURCE` mode, Lambda preserves the original format, requiring you function to handle the appropriate deserialization.

Powertools for AWS supports both Schema Registry integration modes in your Event Source Mapping configuration.

For simplicity, we will use a simple schema containing `name` and `age` in most of our examples. You can also copy the payload example with the expected Kafka event to test your code.

```
{
  "name": "...",
  "age": "..."
}

```

```
{
  "eventSource": "aws:kafka",
  "eventSourceArn": "arn:aws:kafka:eu-west-3:123456789012:cluster/powertools-kafka-esm/f138df86-9253-4d2a-b682-19e132396d4f-s3",
  "bootstrapServers": "boot-z3majaui.c3.kafka-serverless.eu-west-3.amazonaws.com:9098",
  "records": {
    "python-with-avro-doc-5": [
      {
        "topic": "python-with-avro-doc",
        "partition": 5,
        "offset": 0,
        "timestamp": 1750547462087,
        "timestampType": "CREATE_TIME",
        "key": "MTIz",
        "value": "eyJuYW1lIjogIlBvd2VydG9vbHMiLCAiYWdlIjogNX0=",
        "headers": []
      }
    ]
  }
}

```

```
{
    "type": "record",
    "name": "User",
    "namespace": "com.example",
    "fields": [
        {"name": "name", "type": "string"},
        {"name": "age", "type": "int"}
    ]
}

```

```
{
  "eventSource": "aws:kafka",
  "eventSourceArn": "arn:aws:kafka:eu-west-3:123456789012:cluster/powertools-kafka-esm/f138df86-9253-4d2a-b682-19e132396d4f-s3",
  "bootstrapServers": "boot-z3majaui.c3.kafka-serverless.eu-west-3.amazonaws.com:9098",
  "records": {
    "python-with-avro-doc-3": [
      {
        "topic": "python-with-avro-doc",
        "partition": 3,
        "offset": 0,
        "timestamp": 1750547105187,
        "timestampType": "CREATE_TIME",
        "key": "MTIz",
        "value": "AwBXT2qalUhN6oaj2CwEeaEWFFBvd2VydG9vbHMK",
        "headers": []
      }
    ]
  }
}

```

```
syntax = "proto3";

package com.example;

message User {
  string name = 1;
  int32 age = 2;
}

```

```
{
  "eventSource": "aws:kafka",
  "eventSourceArn": "arn:aws:kafka:eu-west-3:992382490249:cluster/powertools-kafka-esm/f138df86-9253-4d2a-b682-19e132396d4f-s3",
  "bootstrapServers": "boot-z3majaui.c3.kafka-serverless.eu-west-3.amazonaws.com:9098",
  "records": {
    "python-with-avro-doc-5": [
      {
        "topic": "python-with-avro-doc",
        "partition": 5,
        "offset": 1,
        "timestamp": 1750624373324,
        "timestampType": "CREATE_TIME",
        "key": "MTIz",
        "value": "Cgpwb3dlcnRvb2xzEAU=",
        "headers": []
      }
    ]
  }
}

```

### Processing Kafka events

The Kafka consumer utility transforms raw Kafka events into an intuitive format for processing. To handle messages effectively, you'll need to configure a schema that matches your data format.

Using Avro is recommended

We recommend Avro for production Kafka implementations due to its schema evolution capabilities, compact binary format, and integration with Schema Registry. This offers better type safety and forward/backward compatibility compared to JSON.

```
import { readFileSync } from 'node:fs';
import { kafkaConsumer, SchemaType } from '@aws-lambda-powertools/kafka';
import type { SchemaConfig } from '@aws-lambda-powertools/kafka/types';
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger({ serviceName: 'kafka-consumer' });

const schemaConfig = {
  value: {
    type: SchemaType.AVRO,
    schema: readFileSync(new URL('./user.avsc', import.meta.url), 'utf8'),
  },
} satisfies SchemaConfig;

export const handler = kafkaConsumer(async (event, _context) => {
  for (const { value } of event.records) {
    logger.info('received value', { value });
  }
}, schemaConfig);

```

```
import { kafkaConsumer, SchemaType } from '@aws-lambda-powertools/kafka';
import type { SchemaConfig } from '@aws-lambda-powertools/kafka/types';
import { Logger } from '@aws-lambda-powertools/logger';
import { com } from './samples/user.generated.js'; // protobuf generated class

const logger = new Logger({ serviceName: 'kafka-consumer' });

const schemaConfig = {
  value: {
    type: SchemaType.PROTOBUF,
    schema: com.example.User,
  },
} satisfies SchemaConfig;

export const handler = kafkaConsumer(async (event, _context) => {
  for (const { value } of event.records) {
    logger.info('received value', { value });
  }
}, schemaConfig);

```

```
import { kafkaConsumer, SchemaType } from '@aws-lambda-powertools/kafka';
import type { SchemaConfig } from '@aws-lambda-powertools/kafka/types';
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger({ serviceName: 'kafka-consumer' });

const schemaConfig = {
  value: {
    type: SchemaType.JSON,
  },
} satisfies SchemaConfig;

export const handler = kafkaConsumer(async (event, _context) => {
  for (const { value } of event.records) {
    logger.info('received value', { value });
  }
}, schemaConfig);

```

### Deserializing key and value

The `kafkaConsumer` function can deserialize both key and value independently based on your schema configuration. This flexibility allows you to work with different data formats in the same message.

```
import { readFileSync } from 'node:fs';
import { kafkaConsumer, SchemaType } from '@aws-lambda-powertools/kafka';
import type { SchemaConfig } from '@aws-lambda-powertools/kafka/types';
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger({ serviceName: 'kafka-consumer' });

const schemaConfig = {
  key: {
    type: SchemaType.AVRO,
    schema: readFileSync(new URL('./ProductKey.avsc', import.meta.url), 'utf8'),
  },
  value: {
    type: SchemaType.AVRO,
    schema: readFileSync(
      new URL('./productInfo.avsc', import.meta.url),
      'utf8'
    ),
  },
} satisfies SchemaConfig;

export const handler = kafkaConsumer<ProductKey, ProductInfo>(
  async (event, _context) => {
    for (const { key, value } of event.records) {
      logger.info('processing product ID', { productId: key.productId });
      logger.info('product', { name: value.name, price: value.price });
    }
  },
  schemaConfig
);

```

```
type ProductKey = {
  productId: string;
};

type ProductInfo = {
  name: string;
  price: number;
  inStock: boolean;
};

```

```
{
  "type": "record",
  "name": "ProductKey",
  "fields": [
    {"name": "product_id", "type": "string"}
  ]
}

```

```
{
  "type": "record",
  "name": "ProductInfo",
  "fields": [
    {"name": "name", "type": "string"},
    {"name": "price", "type": "double"},
    {"name": "in_stock", "type": "boolean"}
  ]
}

```

You can configure the `kafkaConsumer` to handle only the value. This allows you to optimize your Lambda function for the specific data structure of your Kafka messages.

### Handling primitive types

When working with primitive data types (strings, integers, etc.) rather than structured objects, you can simplify your configuration by omitting the schema specification for that component. Powertools for AWS will deserialize the value always as a string.

Common pattern: Keys with primitive values

Using primitive types (strings, integers) as Kafka message keys is a common pattern for partitioning and identifying messages. The Kafka consumer automatically handles these primitive keys without requiring special configuration, making it easy to implement this popular design pattern.

```
import { kafkaConsumer } from '@aws-lambda-powertools/kafka';
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger({ serviceName: 'kafka-consumer' });

export const handler = kafkaConsumer<string, { name: string; age: number }>(
  async (event, _context) => {
    for (const record of event.records) {
      // Key is automatically decoded as UTF-8 string
      const { key } = record;
      // Value is parsed as JSON object
      const { value } = record;

      logger.info('received value', {
        key,
        product: {
          name: value.name,
          age: value.age,
        },
      });
    }
  }
);

```

### Message format support and comparison

The Kafka consumer utility supports multiple serialization formats to match your existing Kafka implementation. Choose the format that best suits your needs based on performance, schema evolution requirements, and ecosystem compatibility.

Selecting the right format

For new applications, consider Avro or Protocol Buffers over JSON. Both provide schema validation, evolution support, and significantly better performance with smaller message sizes. Avro is particularly well-suited for Kafka due to its built-in schema evolution capabilities.

| Format               | Schema Type  | Description                       | Required Parameters                  |
| -------------------- | ------------ | --------------------------------- | ------------------------------------ |
| **JSON**             | `"JSON"`     | Human-readable text format        | None                                 |
| **Avro**             | `"AVRO"`     | Compact binary format with schema | `value.schema` (Avro schema string)  |
| **Protocol Buffers** | `"PROTOBUF"` | Efficient binary format           | `value.schema` (Proto message class) |

| Feature                       | JSON     | Avro                 | Protocol Buffers        |
| ----------------------------- | -------- | -------------------- | ----------------------- |
| **Schema Definition**         | Optional | Required JSON schema | Required Protobuf class |
| **Schema Evolution**          | None     | Strong support       | Strong support          |
| **Size Efficiency**           | Low      | High                 | Highest                 |
| **Processing Speed**          | Slower   | Fast                 | Fastest                 |
| **Human Readability**         | High     | Low                  | Low                     |
| **Implementation Complexity** | Low      | Medium               | Medium                  |
| **Additional Dependencies**   | None     | `avro-js` module     | `protobufjs` module     |

Choose the serialization format that best fits your needs:

- **JSON**: Best for simplicity and when schema flexibility is important
- **Avro**: Best for systems with evolving schemas and when compatibility is critical
- **Protocol Buffers**: Best for performance-critical systems with structured data

## Advanced

### Accessing record metadata

Each Kafka record contains important metadata that you can access alongside the deserialized message content. This metadata helps with message processing, troubleshooting, and implementing advanced patterns like exactly-once processing.

```
import { kafkaConsumer, SchemaType } from '@aws-lambda-powertools/kafka';
import { Logger } from '@aws-lambda-powertools/logger';
import { com } from './samples/user.generated.js'; // protobuf generated class

const logger = new Logger({ serviceName: 'kafka-consumer' });

export const handler = kafkaConsumer<unknown, com.example.IUser>(
  async (event, _context) => {
    for (const record of event.records) {
      const { value, topic, partition, offset, timestamp, headers } = record;
      logger.info(`processing message from topic ${topic}`, {
        partition,
        offset,
        timestamp,
      });

      if (headers) {
        for (const header of headers) {
          logger.debug(`Header: ${header.key}`, {
            value: header.value,
          });
        }
      }

      // Process the deserialized value
      logger.info('User data', {
        userName: value.name,
        userAge: value.age,
      });
    }
  },
  {
    value: {
      type: SchemaType.PROTOBUF,
      schema: com.example.User,
    },
  }
);

```

For debugging purposes, you can also access the original key, value, and headers in their base64-encoded form, these are available in the `originalValue`, `originalKey`, and `originalHeaders` properties of the `record`.

#### Available metadata properties

| Property              | Description                                                      | Example Use Case                                                    |
| --------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------- |
| `topic`               | Topic name the record was published to                           | Routing logic in multi-topic consumers                              |
| `partition`           | Kafka partition number                                           | Tracking message distribution                                       |
| `offset`              | Position in the partition                                        | De-duplication, exactly-once processing                             |
| `timestamp`           | Unix timestamp when record was created                           | Event timing analysis                                               |
| `timestamp_type`      | Timestamp type (`CREATE_TIME` or `LOG_APPEND_TIME`)              | Data lineage verification                                           |
| `headers`             | Key-value pairs attached to the message                          | Cross-cutting concerns like correlation IDs                         |
| `key`                 | Deserialized message key                                         | Customer ID or entity identifier                                    |
| `value`               | Deserialized message content                                     | The actual business data                                            |
| `originalValue`       | Base64-encoded original message value                            | Debugging or custom deserialization                                 |
| `originalKey`         | Base64-encoded original message key                              | Debugging or custom deserialization                                 |
| `originalHeaders`     | Base64-encoded original message headers                          | Debugging or custom deserialization                                 |
| `valueSchemaMetadata` | Metadata about the value schema like `schemaId` and `dataFormat` | Used by `kafkaConsumer` to process Protobuf, data format validation |
| `keySchemaMetadata`   | Metadata about the key schema like `schemaId` and `dataFormat`   | Used by `kafkaConsumer` to process Protobuf, data format validation |

### Additional Parsing

You can parse deserialized data using your preferred parsing library. This can help you integrate Kafka data with your domain schemas and application architecture, providing type hints, runtime parsing and validation, and advanced data transformations.

```
import { kafkaConsumer, SchemaType } from '@aws-lambda-powertools/kafka';
import type { SchemaConfig } from '@aws-lambda-powertools/kafka/types';
import { Logger } from '@aws-lambda-powertools/logger';
import { z } from 'zod/v4';

const logger = new Logger({ serviceName: 'kafka-consumer' });

const OrderItemSchema = z.object({
  productId: z.string(),
  quantity: z.number().int().positive(),
  price: z.number().positive(),
});

const OrderSchema = z.object({
  id: z.string(),
  customerId: z.string(),
  items: z.array(OrderItemSchema).min(1, 'Order must have at least one item'),
  createdAt: z.iso.datetime(),
  totalAmount: z.number().positive(),
});

const schemaConfig = {
  value: {
    type: SchemaType.JSON,
    parserSchema: OrderSchema,
  },
} satisfies SchemaConfig;

export const handler = kafkaConsumer<unknown, z.infer<typeof OrderSchema>>(
  async (event, _context) => {
    for (const record of event.records) {
      const {
        value: { id, items },
      } = record;
      logger.setCorrelationId(id);
      logger.debug(`order includes ${items.length} items`);
    }
  },
  schemaConfig
);

```

```
import { kafkaConsumer, SchemaType } from '@aws-lambda-powertools/kafka';
import type { SchemaConfig } from '@aws-lambda-powertools/kafka/types';
import { Logger } from '@aws-lambda-powertools/logger';
import * as v from 'valibot';

const logger = new Logger({ serviceName: 'kafka-consumer' });

const OrderItemSchema = v.object({
  productId: v.string(),
  quantity: v.pipe(v.number(), v.integer(), v.toMinValue(1)),
  price: v.pipe(v.number(), v.integer()),
});

const OrderSchema = v.object({
  id: v.string(),
  customerId: v.string(),
  items: v.pipe(
    v.array(OrderItemSchema),
    v.minLength(1, 'Order must have at least one item')
  ),
  createdAt: v.pipe(v.string(), v.isoDateTime()),
  totalAmount: v.pipe(v.number(), v.toMinValue(0)),
});

const schemaConfig = {
  value: {
    type: SchemaType.JSON,
    parserSchema: OrderSchema,
  },
} satisfies SchemaConfig;

export const handler = kafkaConsumer<unknown, v.InferInput<typeof OrderSchema>>(
  async (event, _context) => {
    for (const record of event.records) {
      const {
        value: { id, items },
      } = record;
      logger.setCorrelationId(id);
      logger.debug(`order includes ${items.length} items`);
    }
  },
  schemaConfig
);

```

```
import { kafkaConsumer, SchemaType } from '@aws-lambda-powertools/kafka';
import type { SchemaConfig } from '@aws-lambda-powertools/kafka/types';
import { Logger } from '@aws-lambda-powertools/logger';
import { type } from 'arktype';

const logger = new Logger({ serviceName: 'kafka-consumer' });

const OrderItemSchema = type({
  productId: 'string',
  quantity: 'number.integer >= 1',
  price: 'number.integer',
});

const OrderSchema = type({
  id: 'string',
  customerId: 'string',
  items: OrderItemSchema.array().moreThanLength(0),
  createdAt: 'string.date',
  totalAmount: 'number.integer >= 0',
});

const schemaConfig = {
  value: {
    type: SchemaType.JSON,
    parserSchema: OrderSchema,
  },
} satisfies SchemaConfig;

export const handler = kafkaConsumer<unknown, typeof OrderSchema.infer>(
  async (event, _context) => {
    for (const record of event.records) {
      const {
        value: { id, items },
      } = record;
      logger.setCorrelationId(id);
      logger.debug(`order includes ${items.length} items`);
    }
  },
  schemaConfig
);

```

### Error handling

Handle errors gracefully when processing Kafka messages to ensure your application maintains resilience and provides clear diagnostic information. The Kafka consumer utility provides specific exception types to help you identify and handle deserialization issues effectively.

Tip

Fields like `value`, `key`, and `headers` are decoded lazily, meaning they are only deserialized when accessed. This allows you to handle deserialization errors at the point of access rather than when the record is first processed.

```
import { readFileSync } from 'node:fs';
import { kafkaConsumer, SchemaType } from '@aws-lambda-powertools/kafka';
import { KafkaConsumerDeserializationError } from '@aws-lambda-powertools/kafka/errors';
import type {
  ConsumerRecord,
  SchemaConfig,
} from '@aws-lambda-powertools/kafka/types';
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger({ serviceName: 'kafka-consumer' });

const schemaConfig = {
  value: {
    type: SchemaType.AVRO,
    schema: readFileSync(new URL('./user.avsc', import.meta.url), 'utf8'),
  },
} satisfies SchemaConfig;

export const handler = kafkaConsumer(async (event, _context) => {
  const results: {
    successful: number;
    failed: Array<ConsumerRecord<unknown, unknown>>;
  } = {
    successful: 0,
    failed: [],
  };
  for (const record of event.records) {
    try {
      const { value, partition, offset, topic } = record; // (1)!
      logger.setCorrelationId(`${topic}-${partition}-${offset}`);

      await processRecord(value);

      results.successful += 1;
    } catch (error) {
      if (error instanceof KafkaConsumerDeserializationError) {
        results.failed.push(record);
        logger.error('Error deserializing message', { error });
      } else {
        logger.error('Error processing message', { error });
      }
    }

    if (results.failed.length > 0) {
      // Handle failed records, e.g., send to a dead-letter queue
    }

    logger.info('Successfully processed records', {
      successful: results.successful,
    });
  }
}, schemaConfig);

```

1. If you want to handle deserialization and parsing errors, you should destructure or access the `value`, `key`, or `headers` properties of the record within the `for...of` loop.

```
import { readFileSync } from 'node:fs';
import { kafkaConsumer, SchemaType } from '@aws-lambda-powertools/kafka';
import { KafkaConsumerParserError } from '@aws-lambda-powertools/kafka/errors';
import type {
  ConsumerRecord,
  SchemaConfig,
} from '@aws-lambda-powertools/kafka/types';
import { Logger } from '@aws-lambda-powertools/logger';
import { z } from 'zod/v4';

const logger = new Logger({ serviceName: 'kafka-consumer' });

const schemaConfig = {
  value: {
    type: SchemaType.AVRO,
    schema: readFileSync(new URL('./user.avsc', import.meta.url), 'utf8'),
    parserSchema: z.object({
      id: z.number(),
      name: z.string(),
      email: z.email(),
    }),
  },
} satisfies SchemaConfig;

export const handler = kafkaConsumer(async (event, _context) => {
  const results: {
    successful: number;
    failed: Array<ConsumerRecord<unknown, unknown>>;
  } = {
    successful: 0,
    failed: [],
  };
  for (const record of event.records) {
    try {
      const { value, partition, offset, topic } = record;
      logger.setCorrelationId(`${topic}-${partition}-${offset}`);

      await processRecord(value);
      results.successful += 1;
    } catch (error) {
      if (error instanceof KafkaConsumerParserError) {
        results.failed.push(record);
        logger.error(
          `Error deserializing message - ${z.prettifyError({ issues: error.cause } as z.ZodError)}`,
          { error } // (1)!
        );
      } else {
        logger.error('Error processing message', { error });
      }
    }

    if (results.failed.length > 0) {
      // Handle failed records, e.g., send to a dead-letter queue
    }

    logger.info('Successfully processed records', {
      successful: results.successful,
    });
  }
}, schemaConfig);

```

1. The `cause` property of the error is populated with the original Standard Schema parsing error, allowing you to access detailed information about the parsing failure.

#### Error types

| Exception                            | Description                                   | Common Causes                                                               |
| ------------------------------------ | --------------------------------------------- | --------------------------------------------------------------------------- |
| `KafkaConsumerError`.                | Base class for all Kafka consumer errors      | General unhandled errors                                                    |
| `KafkaConsumerDeserializationError`  | Thrown when message deserialization fails     | Corrupted message data, schema mismatch, or wrong schema type configuration |
| `KafkaConsumerMissingSchemaError`    | Thrown when a required schema is not provided | Missing schema for AVRO or PROTOBUF formats (required parameter)            |
| `KafkaConsumerOutputSerializerError` | Thrown when additional schema parsing fails   | Parsing failures in Standard Schema models                                  |

### Integrating with Idempotency

When processing Kafka messages in Lambda, failed batches can result in message reprocessing. The [Idempotency utility](https://docs.aws.amazon.com/powertools/typescript/latest/features/idempotency/index.md) prevents duplicate processing by tracking which messages have already been handled, ensuring each message is processed exactly once.

The Idempotency utility automatically stores the result of each successful operation, returning the cached result if the same message is processed again, which prevents potentially harmful duplicate operations like double-charging customers or double-counting metrics.

Tip

By using the Kafka record's unique coordinates (topic, partition, offset) as the idempotency key, you ensure that even if a batch fails and Lambda retries the messages, each message will be processed exactly once.

```
import {
  IdempotencyConfig,
  makeIdempotent,
} from '@aws-lambda-powertools/idempotency';
import { DynamoDBPersistenceLayer } from '@aws-lambda-powertools/idempotency/dynamodb';
import { kafkaConsumer, SchemaType } from '@aws-lambda-powertools/kafka';
import type { SchemaConfig } from '@aws-lambda-powertools/kafka/types';
import { Logger } from '@aws-lambda-powertools/logger';
import { com } from './samples/user.generated.js'; // protobuf generated class

const logger = new Logger({ serviceName: 'kafka-consumer' });
const persistenceStore = new DynamoDBPersistenceLayer({
  tableName: 'IdempotencyTable',
});

const schemaConfig = {
  value: {
    type: SchemaType.PROTOBUF,
    schema: com.example.User,
  },
} satisfies SchemaConfig;

const processRecord = makeIdempotent(
  async (user, topic, partition, offset) => {
    logger.info('processing user', {
      user,
      meta: {
        topic,
        partition,
        offset,
      },
    });

    // ...your business logic here

    return {
      success: true,
      user,
    };
  },
  {
    persistenceStore,
    config: new IdempotencyConfig({
      eventKeyJmesPath: `topic & '-' & partition & '-' & offset`,
    }),
  }
);

export const handler = kafkaConsumer(async (event, _context) => {
  for (const { value, topic, partition, offset } of event.records) {
    await processRecord(value, topic, partition, offset);
  }
}, schemaConfig);

```

### Best practices

#### Handling large messages

When processing large Kafka messages in Lambda, be mindful of memory limitations. Although the Kafka consumer utility optimizes memory usage, large deserialized messages can still exhaust the function resources.

```
import { kafkaConsumer } from '@aws-lambda-powertools/kafka';
import { Logger } from '@aws-lambda-powertools/logger';
import { object, safeParse, string } from 'valibot';

const logger = new Logger({ serviceName: 'kafka-consumer' });

const LargeMessage = object({
  key: string(),
  bucket: string(),
});

export const handler = kafkaConsumer(async (event, _context) => {
  for (const record of event.records) {
    const { topic, value, originalValue } = record;
    const valueSize = Buffer.byteLength(originalValue, 'utf8');
    const parsedValue = safeParse(LargeMessage, value);
    if (
      topic === 'product-catalog' &&
      valueSize > 3_000_000 &&
      parsedValue.success
    ) {
      logger.info('Large message detected, processing from S3', {
        size: valueSize,
      });

      const { key, bucket } = parsedValue.output;
      await processRecordFromS3({ key, bucket });

      logger.info('Processed large message from S3', {
        key,
        bucket,
      });
    }

    // regular processing of the record
  }
});

```

For large messages, consider these proven approaches:

- **Store the data:** use Amazon S3 and include only the S3 reference in your Kafka message
- **Split large payloads:** use multiple smaller messages with sequence identifiers
- **Increase memory:** Increase your Lambda function's memory allocation, which also increases CPU capacity

#### Batch size configuration

The number of Kafka records processed per Lambda invocation is controlled by your Event Source Mapping configuration. Properly sized batches optimize cost and performance.

```
Resources:
OrderProcessingFunction:
    Type: AWS::Serverless::Function
    Properties:
    Runtime: nodejs24.x
    Handler: index.js
    Events:
        KafkaEvent:
        Type: MSK
        Properties:
            Stream: !GetAtt OrdersMSKCluster.Arn
            Topics:
            - order-events
            - payment-events
            # Configuration for optimal throughput/latency balance
            BatchSize: 100
            MaximumBatchingWindowInSeconds: 5
            StartingPosition: LATEST
            # Enable partial batch success reporting
            FunctionResponseTypes:
            - ReportBatchItemFailures

```

Different workloads benefit from different batch configurations:

- **High-volume, simple processing:** Use larger batches (100-500 records) with short timeout
- **Complex processing with database operations:** Use smaller batches (10-50 records)
- **Mixed message sizes:** Set appropriate batching window (1-5 seconds) to handle variability

#### Cross-language compatibility

When using binary serialization formats across multiple programming languages, ensure consistent schema handling to prevent deserialization failures.

Common cross-language challenges to address:

- **Field naming conventions:** camelCase in Java vs snake_case in Python
- **Date/time:** representation differences
- **Numeric precision handling:** especially decimals, doubles, and floats

### Troubleshooting

#### Deserialization failures

When encountering deserialization errors with your Kafka messages, follow this systematic troubleshooting approach to identify and resolve the root cause.

First, check that your schema definition exactly matches the message format. Even minor discrepancies can cause deserialization failures, especially with binary formats like Avro and Protocol Buffers.

For binary messages that fail to deserialize, examine the raw encoded data:

```
// DO NOT include this code in production handlers
// For troubleshooting purposes only
import base64

const rawBytes = Buffer.from(record.originalValue, 'base64');
console.log(`Message size: ${rawBytes.length} bytes`);
console.log(`First 50 bytes (hex): ${rawBytes.slice(0, 50).toString('hex')}`);

```

#### Schema compatibility issues

Schema compatibility issues often manifest as successful connections but failed deserialization. Common causes include:

- **Schema evolution without backward compatibility**: New producer schema is incompatible with consumer schema
- **Field type mismatches**: For example, a field changed from string to integer across systems
- **Missing required fields**: Fields required by the consumer schema but absent in the message
- **Default value discrepancies**: Different handling of default values between languages

When using Schema Registry, verify schema compatibility rules are properly configured for your topics and that all applications use the same registry.

#### Memory and timeout optimization

Lambda functions processing Kafka messages may encounter resource constraints, particularly with large batches or complex processing logic.

For memory errors:

- Increase Lambda memory allocation, which also provides more CPU resources
- Process fewer records per batch by adjusting the `BatchSize` parameter in your event source mapping
- Consider optimizing your message format to reduce memory footprint

For timeout issues:

- Extend your Lambda function timeout setting to accommodate processing time
- Implement chunked or asynchronous processing patterns for time-consuming operations
- Monitor and optimize database operations, external API calls, or other I/O operations in your handler

Monitoring memory usage

Use CloudWatch metrics to track your function's memory utilization. If it consistently exceeds 80% of allocated memory, consider increasing the memory allocation or optimizing your code.

## Kafka consumer workflow

### Using ESM with Schema Registry validation (SOURCE)

```
sequenceDiagram
  participant Kafka
  participant ESM as Event Source Mapping
  participant SchemaRegistry as Schema Registry
  participant Lambda
  participant KafkaConsumer
  participant YourCode
  Kafka->>+ESM: Send batch of records
  ESM->>+SchemaRegistry: Validate schema
  SchemaRegistry-->>-ESM: Confirm schema is valid
  ESM->>+Lambda: Invoke with validated records (still encoded)
  Lambda->>+KafkaConsumer: Pass Kafka event
  KafkaConsumer->>KafkaConsumer: Parse event structure
  loop For each record
      KafkaConsumer->>KafkaConsumer: Decode base64 data
      KafkaConsumer->>KafkaConsumer: Deserialize based on schema_type
      alt Output serializer provided
          KafkaConsumer->>KafkaConsumer: Apply output serializer
      end
  end
  KafkaConsumer->>+YourCode: Provide ConsumerRecords
  YourCode->>YourCode: Process records
  YourCode-->>-KafkaConsumer: Return result
  KafkaConsumer-->>-Lambda: Pass result back
  Lambda-->>-ESM: Return response
  ESM-->>-Kafka: Acknowledge processed batch
```

### Using ESM with Schema Registry deserialization (JSON)

```
sequenceDiagram
  participant Kafka
  participant ESM as Event Source Mapping
  participant SchemaRegistry as Schema Registry
  participant Lambda
  participant KafkaConsumer
  participant YourCode
  Kafka->>+ESM: Send batch of records
  ESM->>+SchemaRegistry: Validate and deserialize
  SchemaRegistry->>SchemaRegistry: Deserialize records
  SchemaRegistry-->>-ESM: Return deserialized data
  ESM->>+Lambda: Invoke with pre-deserialized JSON records
  Lambda->>+KafkaConsumer: Pass Kafka event
  KafkaConsumer->>KafkaConsumer: Parse event structure
  loop For each record
      KafkaConsumer->>KafkaConsumer: Record is already deserialized
      alt Output serializer provided
          KafkaConsumer->>KafkaConsumer: Apply output serializer
      end
  end
  KafkaConsumer->>+YourCode: Provide ConsumerRecords
  YourCode->>YourCode: Process records
  YourCode-->>-KafkaConsumer: Return result
  KafkaConsumer-->>-Lambda: Pass result back
  Lambda-->>-ESM: Return response
  ESM-->>-Kafka: Acknowledge processed batch
```

### Using ESM without Schema Registry integration

```
sequenceDiagram
  participant Kafka
  participant Lambda
  participant KafkaConsumer
  participant YourCode
  Kafka->>+Lambda: Invoke with batch of records (direct integration)
  Lambda->>+KafkaConsumer: Pass raw Kafka event
  KafkaConsumer->>KafkaConsumer: Parse event structure
  loop For each record
      KafkaConsumer->>KafkaConsumer: Decode base64 data
      KafkaConsumer->>KafkaConsumer: Deserialize based on schema_type
      alt Output serializer provided
          KafkaConsumer->>KafkaConsumer: Apply output serializer
      end
  end
  KafkaConsumer->>+YourCode: Provide ConsumerRecords
  YourCode->>YourCode: Process records
  YourCode-->>-KafkaConsumer: Return result
  KafkaConsumer-->>-Lambda: Pass result back
  Lambda-->>-Kafka: Acknowledge processed batch
```

## Testing your code

Testing Kafka consumer code requires simulating Lambda events with Kafka messages. You can create simple test cases using local JSON files without needing a live Kafka cluster. Below an example of how to simulate a JSON message.

```
import type { MSKEvent } from '@aws-lambda-powertools/kafka/types';
import type { Context } from 'aws-lambda';
import { expect, it } from 'vitest';
import { handler } from './gettingStartedPrimitiveValues.js';

it('handles complex protobuf messages from Glue Schema Registry', async () => {
  // Prepare
  const event = {
    eventSource: 'aws:kafka',
    eventSourceArn:
      'arn:aws:kafka:us-east-1:123456789012:cluster/MyCluster/12345678-1234-1234-1234-123456789012-1',
    bootstrapServers:
      'b-1.mskcluster.abcde12345.us-east-1.kafka.amazonaws.com:9092',
    records: {
      'orders-topic': [
        {
          topic: 'orders-topic',
          partition: 0,
          offset: 15,
          timestamp: 1545084650987,
          timestampType: 'CREATE_TIME',
          headers: [],
          key: undefined,
          keySchemaMetadata: {
            dataFormat: 'JSON',
          },
          valueSchemaMetadata: {
            dataFormat: 'JSON',
            schemaId: undefined,
          },
          value: Buffer.from(
            JSON.stringify({ order_id: '12345', amount: 99.95 })
          ).toString('base64'),
        },
      ],
    },
  } as MSKEvent;

  // Act
  const result = await handler(event, {} as Context);

  // Assess
  expect(result).toBeDefined();
  // You can add more specific assertions based on your handler's logic
});

```
# Environment variables

You can configure Powertools for AWS Lambda using environment variables. This is useful when you want to set configuration values in your Infrastructure as Code (IaC) templates or when you want to override default values without changing your code.

Info

Explicit parameters in your code take precedence over environment variables

| Environment variable                         | Description                                                                              | Utility                                                                                               | Default                                                                                                      |
| -------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **POWERTOOLS_SERVICE_NAME**                  | Set service name used for tracing namespace, metrics dimension and structured logging    | All                                                                                                   | `service_undefined`                                                                                          |
| **POWERTOOLS_METRICS_NAMESPACE**             | Set namespace used for metrics                                                           | [Metrics](https://docs.aws.amazon.com/powertools/typescript/latest/features/metrics/index.md)         | `default_namespace`                                                                                          |
| **POWERTOOLS_METRICS_FUNCTION_NAME**         | Function name used as dimension for the `ColdStart` metric                               | [Metrics](https://docs.aws.amazon.com/powertools/typescript/latest/features/metrics/index.md)         | [See docs](https://docs.aws.amazon.com/powertools/typescript/latest/features/metrics/#setting-function-name) |
| **POWERTOOLS_METRICS_DISABLED**              | Explicitly disables emitting metrics to stdout                                           | [Metrics](https://docs.aws.amazon.com/powertools/typescript/latest/features/metrics/index.md)         | `false`                                                                                                      |
| **POWERTOOLS_TRACE_ENABLED**                 | Explicitly disables tracing                                                              | [Tracer](https://docs.aws.amazon.com/powertools/typescript/latest/features/tracer/index.md)           | `true`                                                                                                       |
| **POWERTOOLS_TRACER_CAPTURE_RESPONSE**       | Capture Lambda or method return as metadata.                                             | [Tracer](https://docs.aws.amazon.com/powertools/typescript/latest/features/tracer/index.md)           | `true`                                                                                                       |
| **POWERTOOLS_TRACER_CAPTURE_ERROR**          | Capture Lambda or method exception as metadata.                                          | [Tracer](https://docs.aws.amazon.com/powertools/typescript/latest/features/tracer/index.md)           | `true`                                                                                                       |
| **POWERTOOLS_TRACER_CAPTURE_HTTPS_REQUESTS** | Capture HTTP(s) requests as segments.                                                    | [Tracer](https://docs.aws.amazon.com/powertools/typescript/latest/features/tracer/index.md)           | `true`                                                                                                       |
| **POWERTOOLS_LOGGER_LOG_EVENT**              | Log incoming event                                                                       | [Logger](https://docs.aws.amazon.com/powertools/typescript/latest/features/logger/index.md)           | `false`                                                                                                      |
| **POWERTOOLS_LOGGER_SAMPLE_RATE**            | Debug log sampling                                                                       | [Logger](https://docs.aws.amazon.com/powertools/typescript/latest/features/logger/index.md)           | `0`                                                                                                          |
| **POWERTOOLS_DEV**                           | Pretty-print logs, disable metrics flushing, and disable traces - use for dev only       | See section below                                                                                     | `false`                                                                                                      |
| **POWERTOOLS_LOG_LEVEL**                     | Sets how verbose Logger should be, from the most verbose to the least verbose (no logs)  | [Logger](https://docs.aws.amazon.com/powertools/typescript/latest/features/logger/index.md)           | `INFO`                                                                                                       |
| **POWERTOOLS_PARAMETERS_MAX_AGE**            | Adjust how long values are kept in cache (in seconds)                                    | [Parameters](https://docs.aws.amazon.com/powertools/typescript/latest/features/parameters/index.md)   | `5`                                                                                                          |
| **POWERTOOLS_PARAMETERS_SSM_DECRYPT**        | Set whether to decrypt or not values retrieved from AWS Systems Manager Parameters Store | [Parameters](https://docs.aws.amazon.com/powertools/typescript/latest/features/parameters/index.md)   | `false`                                                                                                      |
| **POWERTOOLS_IDEMPOTENCY_DISABLED**          | Disable the Idempotency logic without changing your code, useful for testing             | [Idempotency](https://docs.aws.amazon.com/powertools/typescript/latest/features/idempotency/index.md) | `false`                                                                                                      |

Each Utility page provides information on example values and allowed values.

## Dev Mode

Whether you're prototyping locally or against a non-production environment, you can use `POWERTOOLS_DEV` to increase verbosity across multiple utilities or disable certain features.

When `POWERTOOLS_DEV` is set to a truthy value (`1`, `true`, `on`), it'll have the following effects:

| Utility     | Effect                                                                                                               |
| ----------- | -------------------------------------------------------------------------------------------------------------------- |
| **Logger**  | Increase JSON indentation to 4, uses global `console` to emit logs, and format stack traces                          |
| **Tracer**  | Disable tracing operations. This already happens automatically when running in non-Lambda environments               |
| **Metrics** | Disable emitting metrics to stdout. Can be overridden by explicitly setting `POWERTOOLS_METRICS_DISABLED` to `false` |
# Upgrade guide

## End of support v1

On March 13th, 2024, Powertools for AWS Lambda (TypeScript) v1 entered maintenance mode, and has reached End-of-Life on September 1st, 2024. If you are still using v1, we strongly recommend you to upgrade to the latest version.

Given our commitment to all of our customers using Powertools for AWS Lambda (TypeScript), we will keep npm v1 releases and documentation 1.x versions to prevent any disruption.

## Migrate from v1 to v2

V2 is focused on official support for ESM (ECMAScript modules). We've made other minimal breaking changes to make your transition to v2 as smooth as possible.

### Quick summary

||Area |Change |Code change required || | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ||**ESM support** |Added ESM support via dual CommonJS and ESM bundling, enabling top-level `await` and tree-shaking. |- || ||**Middy.js** |Updated import path for Middy.js middlewares to leverage subpath exports - i.e. `@aws-lambda-powertools/tracer/middleware`. |Yes || ||**Types imports** |Updated import path for TypeScript types to leverage subpath exports - i.e. `@aws-lambda-powertools/logger/types`. |Yes || ||**Logger** |Changed [log sampling](https://docs.aws.amazon.com/powertools/typescript/latest/features/logger/#sampling-debug-logs) to dynamically switch log level to `DEBUG` on a percentage of requests. |- || ||**Logger** |Updated [custom log formatter](#custom-log-formatter) to include standard as well as persistent keys. |Yes || ||**Logger** |Removed `ContextExamples` from `@aws-lambda-powertools/commons` package. |Yes || ||**Logger and Tracer** |Removed deprecated `createLogger` and `createTracer` helper functions in favor of direct instantiation. |Yes ||

### First steps

Before you start, we suggest making a copy of your current working project or create a new git branch.

1. Upgrade Node.js to v18 or higher, Node.js v20 is recommended.
1. Ensure that you have the latest Powertools for AWS Lambda (TypeScript) version via [Lambda Layer](https://docs.aws.amazon.com/powertools/typescript/latest/getting-started/lambda-layers/index.md) or npm.
1. Review the following sections to confirm whether they apply to your codebase.

## ESM support

With support for ES Modules in v2, you can now use `import` instead of `require` syntax.

This is especially useful when you want to run asynchronous code during the initialization phase by using top-level `await`.

```
import { getSecret } from '@aws-lambda-powertools/parameters/secrets';

// This code will run during the initialization phase of your Lambda function
const myApiKey = await getSecret('my-api-key', { transform: 'json' });

export const handler = async (_event: unknown, _context: unknown) => {
    // ...
};

```

In v2, we improved tree-shaking support to help you reduce your function bundle size. We would love to hear your feedback on further improvements we could make.

### Unable to use ESM?

We recommend using ESM for the best experience *(top-level await, smaller bundle size etc.)*.

If you're unable to use ESM, you can still use the `require` syntax to import the package. We will continue to support it by shipping CommonJS modules alongside ESM.

You might still need the `require` syntax when using a dependency or a transitive dependency that doesn't support ESM. For example, Tracer *(`@aws-lambda-powertools/tracer`)* relies on the AWS X-Ray SDK for Node.js which uses `require`.

When that happens, you can instruct your bundler to use the `require` syntax for specific dependencies while using ESM for everything else. This is commonly known as [polyfill](https://developer.mozilla.org/en-US/docs/Glossary/Polyfill). Here is an example using `esbuild` bundler.

```
import { Stack, type StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { NodejsFunction, OutputFormat } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Runtime } from 'aws-cdk-lib/aws-lambda';

export class MyStack extends Stack {
  public constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const handler = new NodejsFunction(this, 'helloWorldFunction', {
      runtime: Runtime.NODEJS_24_X,
      handler: 'handler',
      entry: 'src/index.ts',
      bundling: {
        format: OutputFormat.ESM,
        minify: true,
        esbuildArgs: {
          "--tree-shaking": "true",
        },
        banner: 
          "import { createRequire } from 'module';const require = createRequire(import.meta.url);", // (1)!
      },
    });
  }
}

```

1. `esbuild` will include this arbitrary code at the top of your bundle to maximize CommonJS compatibility *(`require` keyword)*.

```
Transform: AWS::Serverless-2016-10-31
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      Runtime: nodejs24.x
      Handler: src/index.handler
    Metadata:
      BuildMethod: esbuild
      BuildProperties:
        Minify: true
        Target: 'ES2020'
        Sourcemap: true
        Format: esm
        EntryPoints:
          - src/index.ts
        Banner:
          js: "import { createRequire } from 'module';const require = createRequire(import.meta.url);"  # (1)!

```

1. `esbuild` will include this arbitrary code at the top of your bundle to maximize CommonJS compatibility *(`require` keyword)*.

## Scoped imports

### Middy.js middleware imports

Disregard if you are not using Middy.js middlewares.

In v2, we've added support for subpath exports. This means if you don't import Middy.js middlewares, you will benefit from a smaller bundle size.

In v1, you could import Middy.js middlewares from the default export of a package *(e.g., `logger`)*. For example, you'd import `injectLambdaContext` Logger middleware from `@aws-lambda-powertools/logger`.

In v2, you can now import only the Middy.js middlewares you want to use from a subpath export, *e.g., `@aws-lambda-powertools/logger/middleware`*, leading to a smaller bundle size.

```
import { Logger, injectLambdaContext } from '@aws-lambda-powertools/logger';
import { Tracer, captureLambdaHandler } from '@aws-lambda-powertools/tracer';
import { Metrics, logMetrics } from '@aws-lambda-powertools/metrics';

```

```
import { Logger } from '@aws-lambda-powertools/logger';
import { injectLambdaContext } from '@aws-lambda-powertools/logger/middleware';

import { Tracer } from '@aws-lambda-powertools/tracer';
import { captureLambdaHandler } from '@aws-lambda-powertools/tracer/middleware';

import { Metrics } from '@aws-lambda-powertools/metrics';
import { logMetrics } from '@aws-lambda-powertools/metrics/middleware';

```

### Types imports

In v1, you could import package types from each package under `/lib`, for example `@aws-lambda-powertools/logger/lib/types`.

In v2, you can now directly import from the `types` subpath export, e.g., `@aws-lambda-powertools/logger/types`. This will optimize your bundle size, standardize types import across packages, future-proofing growth.

```
import { LogAttributes, UnformattedAttributes } from '@aws-lambda-powertools/logger/lib/types';

```

```
import { LogAttributes, UnformattedAttributes } from '@aws-lambda-powertools/logger/types';

```

### Using eslint?

When using `eslint`, you might need to use [`@typescript-eslint/parser`](https://github.com/typescript-eslint/typescript-eslint/tree/HEAD/packages/parser) and [`eslint-plugin-import`](https://www.npmjs.com/package/eslint-import-resolver-typescript) to resolve the new subpath imports.

Below is an example of how to configure your `.eslintrc.json` file:

```
{
  "parser": "@typescript-eslint/parser",
  "settings": {
    "import/resolver": {
      "node": {},
      "typescript": {
        "project": "./tsconfig.json",
        "alwaysTryTypes": true,
      },
    },
  },
}

```

## Logger

### Log sampling

Disregard if you are not using the [log sampling feature](https://docs.aws.amazon.com/powertools/typescript/latest/features/logger/#sampling-debug-logs).

In v1, log sampling implementation was inconsistent from other Powertools for AWS Lambda languages *(Python, .NET, and Java)*.

In v2, we changed these behaviors for consistency across languages:

||Behavior |v1 |v2 || | ----------------------- | ------------------------------------------------------------ | --------------------------------------------- | ||Log Level |Log level remains unchanged but any log statement is printed |Log level changes to `DEBUG` || ||Log sampling indication |No indication |Debug message indicates sampling is in effect ||

Logger `sampleRateValue` **continues** to determine the percentage of concurrent/cold start invocations that logs will be sampled, *e.g., log level set to `DEBUG`*.

### Custom log formatter

Disregard if you are not customizing log output with a [custom log formatter](https://docs.aws.amazon.com/powertools/typescript/latest/features/logger/#custom-log-formatter).

In v1, `Logger` exposed the [standard](https://docs.aws.amazon.com/powertools/typescript/latest/features/logger/#standard-structured-keys) as a single argument, *e.g., `formatAttributes(attributes: UnformattedAttributes)`*. It expected a plain object with keys and values you wanted in the final log output.

In v2, you have more control over **standard** (`attributes`) and [**custom keys**](https://docs.aws.amazon.com/powertools/typescript/latest/features/logger/#appending-additional-keys) (`additionalLogAttributes`) in the `formatAttributes` method. Also, you now return a `LogItem` object to increase type safety when defining the final log output.

```
import { LogFormatter } from '@aws-lambda-powertools/logger';
import {
  LogAttributes,
  UnformattedAttributes,
} from '@aws-lambda-powertools/logger/lib/types';

class MyCompanyLogFormatter extends LogFormatter {
  public formatAttributes(attributes: UnformattedAttributes): LogAttributes {
    return {
      message: attributes.message,
      service: attributes.serviceName,
      environment: attributes.environment,
      awsRegion: attributes.awsRegion,
      correlationIds: {
        awsRequestId: attributes.lambdaContext?.awsRequestId,
        xRayTraceId: attributes.xRayTraceId,
      },
      lambdaFunction: {
        name: attributes.lambdaContext?.functionName,
        arn: attributes.lambdaContext?.invokedFunctionArn,
        memoryLimitInMB: attributes.lambdaContext?.memoryLimitInMB,
        version: attributes.lambdaContext?.functionVersion,
        coldStart: attributes.lambdaContext?.coldStart,
      },
      logLevel: attributes.logLevel,
      timestamp: this.formatTimestamp(attributes.timestamp),
      logger: {
        sampleRateValue: attributes.sampleRateValue,
      },
    };
  }
}

export { MyCompanyLogFormatter };

```

```
import { LogFormatter, LogItem } from '@aws-lambda-powertools/logger';
import type { LogAttributes, UnformattedAttributes } from '@aws-lambda-powertools/logger/types';

class MyCompanyLogFormatter extends LogFormatter {
  public formatAttributes(
    attributes: UnformattedAttributes,
    additionalLogAttributes: LogAttributes  // (1)!
  ): LogItem {  // (2)!
    const baseAttributes = {
        message: attributes.message,
        service: attributes.serviceName,
        environment: attributes.environment,
        awsRegion: attributes.awsRegion,
        correlationIds: {
            awsRequestId: attributes.lambdaContext?.awsRequestId,
            xRayTraceId: attributes.xRayTraceId,
        },
        lambdaFunction: {
            name: attributes.lambdaContext?.functionName,
            arn: attributes.lambdaContext?.invokedFunctionArn,
            memoryLimitInMB: attributes.lambdaContext?.memoryLimitInMB,
            version: attributes.lambdaContext?.functionVersion,
            coldStart: attributes.lambdaContext?.coldStart,
        },
        logLevel: attributes.logLevel,
        timestamp: this.formatTimestamp(attributes.timestamp),
        logger: {
            sampleRateValue: attributes.sampleRateValue,
        },
    };

    // Create a new LogItem with the base attributes
    const logItem = new LogItem({ attributes: baseAttributes });

    // Merge additional attributes
    logItem.addAttributes(additionalLogAttributes); // (3)!

    return logItem;
  }
}

export { MyCompanyLogFormatter };

```

1. This new argument contains all [your custom keys](https://docs.aws.amazon.com/powertools/typescript/latest/features/logger/#appending-additional-keys).

1. `LogItem` is the new return object instead of a plain object.

1. If you prefer adding at the initialization, use:

   **`LogItem({persistentAttributes: additionalLogAttributes, attributes: baseAttributes})`**

### ContextExamples for testing

In v1, we have provided a `ContextExamples` object to help you with testing.

In v2, we have removed the `ContextExamples` from the `@aws-lambda-powertools/commons` package, so you need to create it in your tests:

```
import { ContextExamples as dummyContext } from '@aws-lambda-powertools/commons';

describe('MyUnitTest', () => {
  test('Lambda invoked successfully', async () => {
    const testEvent = { test: 'test' };
    await handler(testEvent, dummyContext);
  });
});

```

```
declare const handler: (event: unknown, context: unknown) => Promise<void>;

const context = {
  callbackWaitsForEmptyEventLoop: true,
  functionVersion: '$LATEST',
  functionName: 'foo-bar-function',
  memoryLimitInMB: '128',
  logGroupName: '/aws/lambda/foo-bar-function-123456abcdef',
  logStreamName: '2021/03/09/[$LATEST]abcdef123456abcdef123456abcdef123456',
  invokedFunctionArn:
  'arn:aws:lambda:eu-west-1:123456789012:function:foo-bar-function',
  awsRequestId: 'c6af9ac6-7b61-11e6-9a41-93e812345678',
  getRemainingTimeInMillis: () => 1234,
  done: () => console.log('Done!'),
  fail: () => console.log('Failed!'),
  succeed: () => console.log('Succeeded!'),
};

describe('MyUnitTest', () => {
  test('Lambda invoked successfully', async () => {
    const testEvent = { test: 'test' };
    await handler(testEvent, context);
  });
});

```

## Helper functions

We removed the deprecated `createLogger` and `createTracer` helper functions.

```
import { createLogger } from '@aws-lambda-powertools/logger';
import { createTracer } from '@aws-lambda-powertools/tracer';

const logger = createLogger({ logLevel: 'info' });
const tracer = createTracer({ serviceName: 'my-service' });

```

You can migrate to instantiating the `Logger` and `Tracer` classes directly with no additional changes.

```
import { Logger } from '@aws-lambda-powertools/logger';
import { Tracer } from '@aws-lambda-powertools/tracer';

const logger = new Logger({ logLevel: 'info' });
const tracer = new Tracer({ serviceName: 'my-service' });

```
