# Source: https://novita.ai/docs/guides/model-apis-configure-custom-s3-bucket.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure Custom AWS S3 Bucket

By default, Novita AI temporarily stores output results in our private S3 bucket and returns the results to the user through a temporary authorized S3 link.

However, you can set up a **Custom S3 Bucket** to allow us to save the results in your own bucket. Please follow the steps below to enable this.

## 1. Configure S3 Bucket Policy

First, change your S3 Bucket Policy configuration to the following format (replace `${BucketName}` with your bucket name):

```json  theme={"system"}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "CanonicalUser": "e98cde8d11ec7c03ac08688f1a933b08b0f0f7746b21c4f2e7b2c8202cc0532f"
      },
      "Action": [
        "s3:PutObject",
        "s3:PutObjectAcl"
      ],
      "Resource": "arn:aws:s3:::${BucketName}/*"
    }
  ]
}
```

## 2. Enable Custom Storage in V3 APIs

For V3 API endpoints, Novita AI provides the `custom_storage` parameter in the request body, allowing you to configure your custom S3 bucket for storing generated images.

Here's an example using the `txt2img` API endpoint:

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v3/async/txt2img' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data '{
  "extra": {
    "response_image_type": "jpeg",
    "custom_storage": {
      "aws_s3": {
        "region": "us-east-2",
        "bucket": "test_bucket",
        "path": "/"
      }
    }
  },
  "request": {
    "prompt": "a cute dog",
    "model_name": "realisticVisionV51_v51VAE_94301.safetensors",
    "negative_prompt": "",
    "width": 512,
    "height": 384,
    "image_num": 2,
    "steps": 20,
    "seed": 123,
    "clip_skip": 1,
    "sampler_name": "Euler a",
    "guidance_scale": 7.5
  }
}'
```


Built with [Mintlify](https://mintlify.com).