# Source: https://upstash.com/docs/qstash/quickstarts/aws-lambda/python.md

# AWS Lambda (Python)

[Source Code](https://github.com/upstash/qstash-examples/tree/main/aws-lambda/python-example)

This is a step by step guide on how to receive webhooks from QStash in your
Lambda function on AWS.

### 1. Create a new project

Let's create a new folder called `aws-lambda` and initialize a new project by
creating `lambda_function.py` This example uses Makefile, but the scripts can
also be written for `Pipenv`.

```bash  theme={"system"}
mkdir aws-lambda
cd aws-lambda
touch lambda_function.py
```

### 2. Dependencies

We are using `PyJwt` for decoding the JWT token in our code. We will install the
package in the zipping stage.

### 3. Creating the handler function

In this example we will show how to receive a webhook from QStash and verify the
signature.

First, let's import everything we need:

```python  theme={"system"}
import json
import os
import hmac
import hashlib
import base64
import time
import jwt
```

Now, we create the handler function. In the handler we will prepare all
necessary variables that we need for verification. This includes the signature,
the signing keys and the url of the lambda function. Then we try to verify the
request using the current signing key and if that fails we will try the next
one. If the signature could be verified, we can start processing the request.

```python  theme={"system"}
def lambda_handler(event, context):

    # parse the inputs
    current_signing_key = os.environ['QSTASH_CURRENT_SIGNING_KEY']
    next_signing_key = os.environ['QSTASH_NEXT_SIGNING_KEY']

    headers = event['headers']
    signature = headers['upstash-signature']
    url = "https://{}{}".format(event["requestContext"]["domainName"], event["rawPath"])
    body = None
    if 'body' in event:
        body = event['body']


    # check verification now
    try:
        verify(signature, current_signing_key, body, url)
    except Exception as e:
        print("Failed to verify signature with current signing key:", e)
        try:
            verify(signature, next_signing_key, body, url)
        except Exception as e2:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": str(e2),
                }),
            }


    # Your logic here...

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "ok",
        }),
    }
```

The `verify` function will handle the actual verification of the signature. The
signature itself is actually a [JWT](https://jwt.io) and includes claims about
the request. See [here](/qstash/features/security#claims).

```python  theme={"system"}
# @param jwt_token - The content of the `upstash-signature` header
# @param signing_key - The signing key to use to verify the signature (Get it from Upstash Console)
# @param body - The raw body of the request
# @param url - The public URL of the lambda function
def verify(jwt_token, signing_key, body, url):
    split = jwt_token.split(".")
    if len(split) != 3:
        raise Exception("Invalid JWT.")

    header, payload, signature = split

    message = header + '.' + payload
    generated_signature = base64.urlsafe_b64encode(hmac.new(bytes(signing_key, 'utf-8'), bytes(message, 'utf-8'), digestmod=hashlib.sha256).digest()).decode()

    if generated_signature != signature and signature + "=" != generated_signature :
        raise Exception("Invalid JWT signature.")

    decoded = jwt.decode(jwt_token, options={"verify_signature": False})
    sub = decoded['sub']
    iss = decoded['iss']
    exp = decoded['exp']
    nbf = decoded['nbf']
    decoded_body = decoded['body']

    if iss != "Upstash":
        raise Exception("Invalid issuer: {}".format(iss))

    if sub.rstrip("/") != url.rstrip("/"):
        raise Exception("Invalid subject: {}".format(sub))

    now = time.time()
    if now > exp:
        raise Exception("Token has expired.")

    if now < nbf:
        raise Exception("Token is not yet valid.")


    if body != None:
        while decoded_body[-1] == "=":
            decoded_body = decoded_body[:-1]

        m = hashlib.sha256()
        m.update(bytes(body, 'utf-8'))
        m = m.digest()
        generated_hash = base64.urlsafe_b64encode(m).decode()

        if generated_hash != decoded_body and generated_hash != decoded_body + "=" :
                raise Exception("Body hash doesn't match.")
```

You can find the complete file
[here](https://github.com/upstash/qstash-examples/tree/main/aws-lambda/python-example/lambda_function.py).

That's it, now we can create the function on AWS and test it.

### 4. Create a Lambda function on AWS

Create a new Lambda function from scratch by going to the
[AWS console](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/create/function).
(Make sure you select your desired region)

Give it a name and select `Python 3.8` as runtime, then create the function.

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/python/create_lambda.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=ef006f177bb6ac267678a2ef2218d685" data-og-width="1904" width="1904" data-og-height="907" height="907" data-path="img/qstash/aws/python/create_lambda.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/python/create_lambda.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=bb218a9b61e74e0d93db42640d0479ac 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/python/create_lambda.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=0288d0ae3f89efc0d8a707188e0194a3 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/python/create_lambda.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=1d8b14e68171cd9c5266bf16275782ea 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/python/create_lambda.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=e5c5f5fad35aab353c2a8adad0246f02 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/python/create_lambda.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=ca22c3f689ad2dc75e43f200ebca92d2 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/python/create_lambda.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=2d0a68794faea77685f65455cd383e14 2500w" />
</Frame>

Afterwards we will add a public URL to this lambda by going to the
`Configuration` tab:

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_url.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f4f927ec6e24d6309406a53874b37c53" data-og-width="1919" width="1919" data-og-height="1080" height="1080" data-path="img/qstash/aws/create_url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_url.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=0d3d39f60f188ecd0551852ff0d916af 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_url.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=89e086b38e2f965514586a687dff234b 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_url.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=76b1e5f09bd966a99968cac2b640631e 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_url.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=5a00bcb5625d71deda3b2b7eba61c318 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_url.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=a72303771729bc260c0633ec61b562e3 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/create_url.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=13a5a1547d723fb2296710e738dfd7db 2500w" />
</Frame>

Select `Auth Type = NONE` because we are handling authentication ourselves.

After creating the url, you should see it on the right side of the overview of
your function:

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/python/overview.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=e9eda18e87d98ebc1057e15b21abcc2a" data-og-width="1904" width="1904" data-og-height="906" height="906" data-path="img/qstash/aws/python/overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/python/overview.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=8a74d2186aab480704bbcf058e6d291e 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/python/overview.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=03949c0baba2a516294fab5403bb9e33 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/python/overview.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=048ca2d00cef212ce2d9ea42cf78ccbf 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/python/overview.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=982c0650915c75b771aaa3f487894a1a 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/python/overview.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=08dd85b062fab8d46a216584ea46ef13 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/python/overview.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=27aab10a9c48121f29654ee47d41ffca 2500w" />
</Frame>

### 5. Set Environment Variables

Get your current and next signing key from the
[Upstash Console](https://console.upstash.com/qstash)

On the same `Configuration` tab from earlier, we will now set the required
environment variables:

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=8bc62c641000e9e128a9b37198d1906d" data-og-width="1919" width="1919" data-og-height="1080" height="1080" data-path="img/qstash/aws/environment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=71cbd9ef3b59d2548192de531eb1595d 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=ea9d015c40cad5e2cc8582553ec09754 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f162de686cf6ef6f7984d8fe553d33ed 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=e4181a1e22541d08903375e3f59d67aa 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=591592bbcc823643cdb5fcb8a9d467ef 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/environment.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=ced801202130219f8c75ed907c931cb0 2500w" />
</Frame>

### 6. Deploy your Lambda function

We need to bundle our code and zip it to deploy it to AWS.

Add the following script to your `Makefile` file (or corresponding pipenv
script):

```yaml  theme={"system"}
zip:
    rm -rf dist
	pip3 install --target ./dist pyjwt
	cp lambda_function.py ./dist/lambda_function.py
	cd dist && zip -r lambda.zip .
	mv ./dist/lambda.zip ./
```

When calling `make zip` this will install PyJwt and zip the code.

Afterwards we can click the `Upload from` button in the lower right corner and
deploy the code to AWS. Select `lambda.zip` as upload file.

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/upload.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=04c254761fc6695610e756635a41ccc0" data-og-width="1918" width="1918" data-og-height="1080" height="1080" data-path="img/qstash/aws/upload.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/upload.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=fccd08e6810f18706d56aa6b7ab3cd1b 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/upload.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=546e032f292909dca00c7df011cb1e44 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/upload.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=65e76cbea01afcdfdbd2c616adda1fe2 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/upload.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=4c8a3e6ecb1a67b80e7e7c0e5f39900b 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/upload.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=b31331ce2c780a2aed9df74802b503ac 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/aws/upload.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=043a7652099f9c97ca4f3dcbf0f3ccc1 2500w" />
</Frame>

### 7. Publish a message

Open a different terminal and publish a message to QStash. Note the destination
url is the URL from step 4.

```bash  theme={"system"}
curl --request POST "https://qstash.upstash.io/v2/publish/https://urzdbfn4et56vzeasu3fpcynym0zerme.lambda-url.eu-west-1.on.aws" \
     -H "Authorization: Bearer <QSTASH_TOKEN>" \
     -H "Content-Type: application/json" \
     -d "{ \"hello\": \"world\"}"
```

## Next Steps

That's it, you have successfully created a secure AWS lambda function, that
receives and verifies incoming webhooks from qstash.

Learn more about publishing a message to qstash [here](/qstash/howto/publishing)
