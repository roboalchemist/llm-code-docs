# Source: https://resend.com/docs/send-with-aws-lambda.md

# Send emails with AWS Lambda

> Learn how to send your first email using AWS Lambda.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Create a AWS Lambda function

Go to [aws.amazon.com](https://aws.amazon.com) and create a new Lambda function using the Node.js 18.x runtime.

<img alt="AWS Lambda - New Function" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/aws-lambda-new-function.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=324a1181f685affebb1f50b18765538c" data-og-width="3414" width="3414" data-og-height="1886" height="1886" data-path="images/aws-lambda-new-function.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/aws-lambda-new-function.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=a3182c8eb1966d9636f31456e00e2ec9 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/aws-lambda-new-function.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=d797f2e3768184703be6627c29d23273 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/aws-lambda-new-function.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=050e88c52777b8d38ce95bf8df426e95 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/aws-lambda-new-function.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=21f874a49461776f1c187428c8282ee0 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/aws-lambda-new-function.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=c2df9c56cf87833cbfb7358e8d6fcbc1 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/aws-lambda-new-function.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=b3fa3c2f80d29249d1aab8ae837b17bd 2500w" />

## 2. Edit the handler function

Paste the following code into the browser editor:

```js index.mjs theme={null}
const RESEND_API_KEY = 're_xxxxxxxxx';

export const handler = async (event) => {
  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${RESEND_API_KEY}`,
    },
    body: JSON.stringify({
      from: 'Acme <onboarding@resend.dev>',
      to: ['delivered@resend.dev'],
      subject: 'hello world',
      html: '<strong>it works!</strong>',
    }),
  });

  if (res.ok) {
    const data = await res.json();

    return {
      statusCode: 200,
      body: data,
    };
  }
};
```

## 3. Deploy and send email

Click on `Deploy` and then `Test` at the top of the screen.

<img alt="AWS Lambda - Edit Function" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/aws-lambda-edit-function.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=0393dc19bce3c93881bf4b433024c40b" data-og-width="3414" width="3414" data-og-height="1886" height="1886" data-path="images/aws-lambda-edit-function.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/aws-lambda-edit-function.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=a0e20c73afe50bb014377b782795ca66 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/aws-lambda-edit-function.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=65843732a55e50eed22c683b34fe7416 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/aws-lambda-edit-function.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=e2eca4ce6ae102824f7f6d8fabb2cd53 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/aws-lambda-edit-function.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=916affe26c33065b698a9ad542e72a46 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/aws-lambda-edit-function.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=89ceedcf272892ec14424394826abfc4 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/aws-lambda-edit-function.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=d1fabd5e1e6e4f5dfcd0ba513f197144 2500w" />

## 4. Try it yourself

<Card title="AWS Lambda Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-aws-lambda-example">
  See the full source code.
</Card>
