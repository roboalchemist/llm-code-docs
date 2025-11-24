# Source: https://upstash.com/docs/qstash/quickstarts/aws-lambda/nodejs.md

# AWS Lambda (Node)

## Setting up a Lambda

The [AWS CDK](https://aws.amazon.com/cdk/) is the most convenient way to create a new project on AWS Lambda. For example, it lets you directly define integrations such as APIGateway, a tool to make our lambda publicly available as an API, in your code.

```bash Terminal theme={"system"}
mkdir my-app
cd my-app
cdk init app -l typescript
npm i esbuild @upstash/qstash
mkdir lambda
touch lambda/index.ts
```

## Webhook verification

### Using the SDK (recommended)

Edit `lambda/index.ts`, the file containing our core lambda logic:

```ts lambda/index.ts theme={"system"}
import { Receiver } from "@upstash/qstash"
import type { APIGatewayProxyEvent, APIGatewayProxyResult } from "aws-lambda"

const receiver = new Receiver({
  currentSigningKey: process.env.QSTASH_CURRENT_SIGNING_KEY ?? "",
  nextSigningKey: process.env.QSTASH_NEXT_SIGNING_KEY ?? "",
})

export const handler = async (
  event: APIGatewayProxyEvent
): Promise<APIGatewayProxyResult> => {
  const signature = event.headers["upstash-signature"]
  const lambdaFunctionUrl = `https://${event.requestContext.domainName}`

  if (!signature) {
    return {
      statusCode: 401,
      body: JSON.stringify({ message: "Missing signature" }),
    }
  }

  try {
    await receiver.verify({
      signature: signature,
      body: event.body ?? "",
      url: lambdaFunctionUrl,
    })
  } catch (err) {
    return {
      statusCode: 401,
      body: JSON.stringify({ message: "Invalid signature" }),
    }
  }

  // Request is valid, perform business logic

  return {
    statusCode: 200,
    body: JSON.stringify({ message: "Request processed successfully" }),
  }
}
```

We'll set the `QSTASH_CURRENT_SIGNING_KEY` and `QSTASH_NEXT_SIGNING_KEY` environment variables together when deploying our Lambda.

### Manual Verification

In this section, we'll manually verify our incoming QStash requests without additional packages. Also see our [manual verification example](https://github.com/upstash/qstash-examples/tree/main/aws-lambda).

1. Implement the handler function

```ts lambda/index.ts theme={"system"}
import type { APIGatewayEvent, APIGatewayProxyResult } from "aws-lambda"
import { createHash, createHmac } from "node:crypto"

export const handler = async (
  event: APIGatewayEvent,
): Promise<APIGatewayProxyResult> => {
  const signature = event.headers["upstash-signature"] ?? ""
  const currentSigningKey = process.env.QSTASH_CURRENT_SIGNING_KEY ?? ""
  const nextSigningKey = process.env.QSTASH_NEXT_SIGNING_KEY ?? ""

  const url = `https://${event.requestContext.domainName}`

  try {
    // Try to verify the signature with the current signing key and if that fails, try the next signing key
    // This allows you to roll your signing keys once without downtime
    await verify(signature, currentSigningKey, event.body, url).catch((err) => {
      console.error(
        `Failed to verify signature with current signing key: ${err}`
      )

      return verify(signature, nextSigningKey, event.body, url)
    })
  } catch (err) {
    const message = err instanceof Error ? err.toString() : err

    return {
      statusCode: 400,
      body: JSON.stringify({ error: message }),
    }
  }

  // Add your business logic here

  return {
    statusCode: 200,
    body: JSON.stringify({ message: "Request processed successfully" }),
  }
}
```

2. Implement the `verify` function:

```ts lambda/index.ts theme={"system"}
/**
 * @param jwt - The content of the `upstash-signature` header (JWT)
 * @param signingKey - The signing key to use to verify the signature (Get it from Upstash Console)
 * @param body - The raw body of the request
 * @param url - The public URL of the lambda function
 */
async function verify(
  jwt: string,
  signingKey: string,
  body: string | null,
  url: string
): Promise<void> {
  const split = jwt.split(".")
  if (split.length != 3) {
    throw new Error("Invalid JWT")
  }
  const [header, payload, signature] = split

  if (
    signature !=
    createHmac("sha256", signingKey)
      .update(`${header}.${payload}`)
      .digest("base64url")
  ) {
    throw new Error("Invalid JWT signature")
  }

  // JWT is verified, start looking at payload claims
  const p: {
    sub: string
    iss: string
    exp: number
    nbf: number
    body: string
  } = JSON.parse(Buffer.from(payload, "base64url").toString())

  if (p.iss !== "Upstash") {
    throw new Error(`invalid issuer: ${p.iss}, expected "Upstash"`)
  }
  if (p.sub !== url) {
    throw new Error(`invalid subject: ${p.sub}, expected "${url}"`)
  }

  const now = Math.floor(Date.now() / 1000)
  if (now > p.exp) {
    throw new Error("token has expired")
  }
  if (now < p.nbf) {
    throw new Error("token is not yet valid")
  }

  if (body != null) {
    if (
      p.body.replace(/=+$/, "") !=
      createHash("sha256").update(body).digest("base64url")
    ) {
      throw new Error("body hash does not match")
    }
  }
}
```

You can find the complete example
[here](https://github.com/upstash/qstash-examples/blob/main/aws-lambda/typescript-example/index.ts).

## Deploying a Lambda

### Using the AWS CDK (recommended)

Because we used the AWS CDK to initialize our project, deployment is straightforward. Edit the `lib/<your-stack-name>.ts` file the CDK created when bootstrapping the project. For example, if our lambda webhook does video processing, it could look like this:

```ts lib/<your-stack-name>.ts theme={"system"}
import * as cdk from "aws-cdk-lib";
import * as lambda from "aws-cdk-lib/aws-lambda";
import { NodejsFunction } from "aws-cdk-lib/aws-lambda-nodejs";
import { Construct } from "constructs";
import path from "path";
import * as apigateway from 'aws-cdk-lib/aws-apigateway';

export class VideoProcessingStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    // Create the Lambda function
    const videoProcessingLambda = new NodejsFunction(this, 'VideoProcessingLambda', {
      runtime: lambda.Runtime.NODEJS_20_X,
      handler: 'handler',
      entry: path.join(__dirname, '../lambda/index.ts'),
    });

    // Create the API Gateway
    const api = new apigateway.RestApi(this, 'VideoProcessingApi', {
      restApiName: 'Video Processing Service',
      description: 'This service handles video processing.',
      defaultMethodOptions: {
        authorizationType: apigateway.AuthorizationType.NONE,
      },
    });

    api.root.addMethod('POST', new apigateway.LambdaIntegration(videoProcessingLambda));
  }
}
```

Every time we now run the following deployment command in our terminal, our changes are going to be deployed right to a publicly available API, authorized by our QStash webhook logic from before.

```bash Terminal theme={"system"}
cdk deploy
```

You may be prompted to confirm the necessary AWS permissions during this process, for example allowing APIGateway to invoke your lambda function.

Once your code has been deployed to Lambda, you'll receive a live URL to your endpoint via the CLI and can see the new APIGateway connection in your AWS dashboard:

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/api-gateway.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f07b1c8472eec7faff846c05dabf5f6d" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="img/qstash/aws/api-gateway.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/api-gateway.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=058d384f8e63bd1c5ffb53ee9c56a521 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/api-gateway.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=ccf60c328fb20a8275494169228369ef 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/api-gateway.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=9aa4a9694db70a918ee5790811ae5abc 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/api-gateway.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=eb2e309a525baee49722fabe084bb1dc 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/api-gateway.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=a41d328f4a909e95a3358c42bdb02b51 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/api-gateway.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=44e80904cad9bb76988e82377ecbcd2e 2500w" />
</Frame>

The URL you use to invoke your function typically follows this format, especially if you follow the same stack configuration as shown above:

`https://<API-GATEWAY-ID>.execute-api.<API-REGION>.amazonaws.com/prod/`

To provide our `QSTASH_CURRENT_SIGNING_KEY` and `QSTASH_NEXT_SIGNING_KEY` environment variables, navigate to your QStash dashboard:

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=80587de8e955411f9c092d3348056af3" data-og-width="1211" width="1211" data-og-height="833" height="833" data-path="img/qstash-workflow/qstash_signing_keys.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=9aff13ae1e92d8e869d002ed08a9da07 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=796060edf979b7ce1e6710b9a4cdf78b 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=185f283f737442f131d8f3de95f88cc8 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=773c19bc5a6f25f3fa5f3616c7f7919f 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=cf56a1e230831d2bfdd539d8118df910 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=e42354e5503790f53e952804d7ca0ead 2500w" />
</Frame>

and make these two variables available to your Lambda in your function configuration:

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=8bc62c641000e9e128a9b37198d1906d" data-og-width="1919" width="1919" data-og-height="1080" height="1080" data-path="img/qstash/aws/environment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=71cbd9ef3b59d2548192de531eb1595d 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=ea9d015c40cad5e2cc8582553ec09754 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f162de686cf6ef6f7984d8fe553d33ed 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=e4181a1e22541d08903375e3f59d67aa 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=591592bbcc823643cdb5fcb8a9d467ef 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=ced801202130219f8c75ed907c931cb0 2500w" />
</Frame>

Tada, we just deployed a live Lambda with the AWS CDK! 🎉

### Manual Deployment

1. Create a new Lambda function by going to the [AWS dashboard](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/create/function) for your desired lambda region. Give your new function a name and select `Node.js 20.x` as runtime, then create the function.

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_lambda.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=3582c906c9bd8316714abd84cfc36d7a" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="img/qstash/aws/create_lambda.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_lambda.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=cc123cbcec268d316e9c9c0df1f18dfe 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_lambda.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=1d4707c9406ba6493b85d19820df4330 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_lambda.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=616fa0ff8b3ba1d5390535ab4a1b4cc8 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_lambda.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=3f23acd71afa860a8eb89e80903025b4 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_lambda.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=d321923e425b60e7caa62f44c53947a5 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_lambda.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=ebf5b50e8ac995899825aed7a44956f9 2500w" />
</Frame>

2. To make this Lambda available under a public URL, navigate to the `Configuration` tab and click `Function URL`:

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_url.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f4f927ec6e24d6309406a53874b37c53" data-og-width="1919" width="1919" data-og-height="1080" height="1080" data-path="img/qstash/aws/create_url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_url.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=0d3d39f60f188ecd0551852ff0d916af 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_url.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=89e086b38e2f965514586a687dff234b 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_url.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=76b1e5f09bd966a99968cac2b640631e 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_url.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=5a00bcb5625d71deda3b2b7eba61c318 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_url.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=a72303771729bc260c0633ec61b562e3 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_url.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=13a5a1547d723fb2296710e738dfd7db 2500w" />
</Frame>

3. In the following dialog, you'll be asked to select one of two authentication types. Select `NONE`, because we are handling authentication ourselves. Then, click `Save`.

   You'll see the function URL on the right side of your function overview:

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/overview.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=94d488280830a5843d265040a7e8842d" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="img/qstash/aws/overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/overview.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=2abfa43675d0a24c01282b5ef7f50a25 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/overview.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=8707939c6fe6f98d2286358a7473c2a8 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/overview.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=a07632d24f62047f83995bdb527e1431 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/overview.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=7d7cddc5865e3ce07eda28ac247e47b0 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/overview.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=2f16c346e178fcadb5ef4fca6ab4f9bc 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/overview.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=57715f8c175f946456661920f91ce292 2500w" />
</Frame>

4. Get your current and next signing key from the
   [Upstash Console](https://console.upstash.com/qstash).

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=80587de8e955411f9c092d3348056af3" data-og-width="1211" width="1211" data-og-height="833" height="833" data-path="img/qstash-workflow/qstash_signing_keys.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=9aff13ae1e92d8e869d002ed08a9da07 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=796060edf979b7ce1e6710b9a4cdf78b 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=185f283f737442f131d8f3de95f88cc8 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=773c19bc5a6f25f3fa5f3616c7f7919f 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=cf56a1e230831d2bfdd539d8118df910 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=e42354e5503790f53e952804d7ca0ead 2500w" />
</Frame>

5. Still under the `Configuration` tab, set the `QSTASH_CURRENT_SIGNING_KEY` and `QSTASH_NEXT_SIGNING_KEY`
   environment variables:

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=8bc62c641000e9e128a9b37198d1906d" data-og-width="1919" width="1919" data-og-height="1080" height="1080" data-path="img/qstash/aws/environment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=71cbd9ef3b59d2548192de531eb1595d 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=ea9d015c40cad5e2cc8582553ec09754 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f162de686cf6ef6f7984d8fe553d33ed 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=e4181a1e22541d08903375e3f59d67aa 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=591592bbcc823643cdb5fcb8a9d467ef 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=ced801202130219f8c75ed907c931cb0 2500w" />
</Frame>

6. Add the following script to your `package.json` file to build and zip your code:

```json package.json theme={"system"}
{
  "scripts": {
    "build": "rm -rf ./dist; esbuild index.ts --bundle --minify --sourcemap --platform=node --target=es2020 --outfile=dist/index.js && cd dist && zip -r index.zip index.js*"
  }
}
```

7. Click the `Upload from` button for your Lambda and
   deploy the code to AWS. Select `./dist/index.zip` as the upload file.

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/upload.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=04c254761fc6695610e756635a41ccc0" data-og-width="1918" width="1918" data-og-height="1080" height="1080" data-path="img/qstash/aws/upload.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/upload.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=fccd08e6810f18706d56aa6b7ab3cd1b 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/upload.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=546e032f292909dca00c7df011cb1e44 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/upload.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=65e76cbea01afcdfdbd2c616adda1fe2 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/upload.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=4c8a3e6ecb1a67b80e7e7c0e5f39900b 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/upload.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=b31331ce2c780a2aed9df74802b503ac 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/upload.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=043a7652099f9c97ca4f3dcbf0f3ccc1 2500w" />
</Frame>

Tada, you've manually deployed a zip file to AWS Lambda! 🎉

## Testing the Integration

To make sure everything works as expected, navigate to your QStash request builder and send a request to your freshly deployed Lambda function:

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/verify-integration.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=21446d89f9624bc1a32b9d66a227368b" data-og-width="1253" width="1253" data-og-height="752" height="752" data-path="img/qstash/aws/verify-integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/verify-integration.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=7ba80e9eee665c3434aa445c046df602 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/verify-integration.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=bbfd54dc0d771368d4365f8e1359b5b0 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/verify-integration.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=5b7db6102b578a20729c7a0caac693dd 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/verify-integration.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=398676b5df8e4f78a565b8f528255650 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/verify-integration.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=cbadedc9f3a0a52b4239e144b1614227 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/verify-integration.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=9253d2e5f2a1e331415f033beb222b2f 2500w" />
</Frame>

Alternatively, you can also send a request via CURL:

```bash Terminal theme={"system"}
curl --request POST "https://qstash.upstash.io/v2/publish/<YOUR-LAMBDA-URL>" \
-H "Authorization: Bearer <QSTASH_TOKEN>" \
-H "Content-Type: application/json" \
-d "{ \"hello\": \"world\"}"
```
