# Source: https://docs.vllm.ai/en/stable/examples/offline_inference/openai_batch/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/offline_inference/openai_batch.md "Edit this page")

# Offline Inference with the OpenAI Batch file format[¶](#offline-inference-with-the-openai-batch-file-format "Permanent link")

Source <https://github.com/vllm-project/vllm/tree/main/examples/offline_inference/openai_batch>.

    This is a guide to performing batch inference using the OpenAI batch file format, **not** the complete Batch (REST) API.

## File Format[¶](#file-format "Permanent link")

The OpenAI batch file format consists of a series of json objects on new lines.

[See here for an example file.](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/openai_batch/openai_example_batch.jsonl)

Each line represents a separate request. See the [OpenAI package reference](https://platform.openai.com/docs/api-reference/batch/requestInput) for more details.

    We currently support `/v1/chat/completions`, `/v1/embeddings`, and `/v1/score` endpoints (completions coming soon).

## Pre-requisites[¶](#pre-requisites "Permanent link")

-   The examples in this document use `meta-llama/Meta-Llama-3-8B-Instruct`.
    -   Create a [user access token](https://huggingface.co/docs/hub/en/security-tokens)
    -   Install the token on your machine (Run `huggingface-cli login`).
    -   Get access to the gated model by [visiting the model card](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) and agreeing to the terms and conditions.

## Example 1: Running with a local file[¶](#example-1-running-with-a-local-file "Permanent link")

### Step 1: Create your batch file[¶](#step-1-create-your-batch-file "Permanent link")

To follow along with this example, you can download the example batch, or create your own batch file in your working directory.

    wget https://raw.githubusercontent.com/vllm-project/vllm/main/examples/offline_inference/openai_batch/openai_example_batch.jsonl

Once you\'ve created your batch file it should look like this

    cat offline_inference/openai_batch/openai_example_batch.jsonl
    ,],"max_completion_tokens": 1000}}
    ,],"max_completion_tokens": 1000}}

### Step 2: Run the batch[¶](#step-2-run-the-batch "Permanent link")

The batch running tool is designed to be used from the command line.

You can run the batch with the following command, which will write its results to a file called `results.jsonl`

    python -m vllm.entrypoints.openai.run_batch \
        -i offline_inference/openai_batch/openai_example_batch.jsonl \
        -o results.jsonl \
        --model meta-llama/Meta-Llama-3-8B-Instruct

or use command-line:

    vllm run-batch \
        -i offline_inference/openai_batch/openai_example_batch.jsonl \
        -o results.jsonl \
        --model meta-llama/Meta-Llama-3-8B-Instruct

### Step 3: Check your results[¶](#step-3-check-your-results "Permanent link")

You should now have your results at `results.jsonl`. You can check your results by running `cat results.jsonl`

    cat results.jsonl
    ,"logprobs":null,"finish_reason":"stop","stop_reason":null}],"usage":},"error":null}
    ,"logprobs":null,"finish_reason":"stop","stop_reason":null}],"usage":},"error":null}

## Example 2: Using remote files[¶](#example-2-using-remote-files "Permanent link")

The batch runner supports remote input and output urls that are accessible via http/https.

For example, to run against our example input file located at `https://raw.githubusercontent.com/vllm-project/vllm/main/examples/offline_inference/openai_batch/openai_example_batch.jsonl`, you can run

    python -m vllm.entrypoints.openai.run_batch \
        -i https://raw.githubusercontent.com/vllm-project/vllm/main/examples/offline_inference/openai_batch/openai_example_batch.jsonl \
        -o results.jsonl \
        --model meta-llama/Meta-Llama-3-8B-Instruct

or use command-line:

    vllm run-batch \
        -i https://raw.githubusercontent.com/vllm-project/vllm/main/examples/offline_inference/openai_batch/openai_example_batch.jsonl \
        -o results.jsonl \
        --model meta-llama/Meta-Llama-3-8B-Instruct

## Example 3: Integrating with AWS S3[¶](#example-3-integrating-with-aws-s3 "Permanent link")

To integrate with cloud blob storage, we recommend using presigned urls.

\[Learn more about S3 presigned urls here\]

### Additional prerequisites[¶](#additional-prerequisites "Permanent link")

-   [Create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
-   The `awscli` package (Run `pip install awscli`) to configure your credentials and interactively use s3.
    -   [Configure your credentials](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html).
-   The `boto3` python package (Run `pip install boto3`) to generate presigned urls.

### Step 1: Upload your input script[¶](#step-1-upload-your-input-script "Permanent link")

To follow along with this example, you can download the example batch, or create your own batch file in your working directory.

    wget https://raw.githubusercontent.com/vllm-project/vllm/main/examples/offline_inference/openai_batch/openai_example_batch.jsonl

Once you\'ve created your batch file it should look like this

    cat offline_inference/openai_batch/openai_example_batch.jsonl
    ,],"max_completion_tokens": 1000}}
    ,],"max_completion_tokens": 1000}}

Now upload your batch file to your S3 bucket.

    aws s3 cp offline_inference/openai_batch/openai_example_batch.jsonl s3://MY_BUCKET/MY_INPUT_FILE.jsonl

### Step 2: Generate your presigned urls[¶](#step-2-generate-your-presigned-urls "Permanent link")

Presigned urls can only be generated via the SDK. You can run the following python script to generate your presigned urls. Be sure to replace the `MY_BUCKET`, `MY_INPUT_FILE.jsonl`, and `MY_OUTPUT_FILE.jsonl` placeholders with your bucket and file names.

(The script is adapted from <https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/s3/s3_basics/presigned_url.py>)

    import boto3
    from botocore.exceptions import ClientError

    def generate_presigned_url(s3_client, client_method, method_parameters, expires_in):
        """
        Generate a presigned Amazon S3 URL that can be used to perform an action.

        :param s3_client: A Boto3 Amazon S3 client.
        :param client_method: The name of the client method that the URL performs.
        :param method_parameters: The parameters of the specified client method.
        :param expires_in: The number of seconds the presigned URL is valid for.
        :return: The presigned URL.
        """
        try:
            url = s3_client.generate_presigned_url(
                ClientMethod=client_method,
                Params=method_parameters,
                ExpiresIn=expires_in,
            )
        except ClientError:
            raise
        return url

    s3_client = boto3.client("s3")
    input_url = generate_presigned_url(
        s3_client,
        "get_object",
        ,
        expires_in=3600,
    )
    output_url = generate_presigned_url(
        s3_client,
        "put_object",
        ,
        expires_in=3600,
    )
    print(f"")
    print(f"")

This script should output

    input_url='https://s3.us-west-2.amazonaws.com/MY_BUCKET/MY_INPUT_FILE.jsonl?AWSAccessKeyId=ABCDEFGHIJKLMNOPQRST&Signature=abcdefghijklmnopqrstuvwxyz12345&Expires=1715800091'
    output_url='https://s3.us-west-2.amazonaws.com/MY_BUCKET/MY_OUTPUT_FILE.jsonl?AWSAccessKeyId=ABCDEFGHIJKLMNOPQRST&Signature=abcdefghijklmnopqrstuvwxyz12345&Expires=1715800091'

### Step 3: Run the batch runner using your presigned urls[¶](#step-3-run-the-batch-runner-using-your-presigned-urls "Permanent link")

You can now run the batch runner, using the urls generated in the previous section.

    python -m vllm.entrypoints.openai.run_batch \
        -i "https://s3.us-west-2.amazonaws.com/MY_BUCKET/MY_INPUT_FILE.jsonl?AWSAccessKeyId=ABCDEFGHIJKLMNOPQRST&Signature=abcdefghijklmnopqrstuvwxyz12345&Expires=1715800091" \
        -o "https://s3.us-west-2.amazonaws.com/MY_BUCKET/MY_OUTPUT_FILE.jsonl?AWSAccessKeyId=ABCDEFGHIJKLMNOPQRST&Signature=abcdefghijklmnopqrstuvwxyz12345&Expires=1715800091" \
        --model --model meta-llama/Meta-Llama-3-8B-Instruct

or use command-line:

    vllm run-batch \
        -i "https://s3.us-west-2.amazonaws.com/MY_BUCKET/MY_INPUT_FILE.jsonl?AWSAccessKeyId=ABCDEFGHIJKLMNOPQRST&Signature=abcdefghijklmnopqrstuvwxyz12345&Expires=1715800091" \
        -o "https://s3.us-west-2.amazonaws.com/MY_BUCKET/MY_OUTPUT_FILE.jsonl?AWSAccessKeyId=ABCDEFGHIJKLMNOPQRST&Signature=abcdefghijklmnopqrstuvwxyz12345&Expires=1715800091" \
        --model --model meta-llama/Meta-Llama-3-8B-Instruct

### Step 4: View your results[¶](#step-4-view-your-results "Permanent link")

Your results are now on S3. You can view them in your terminal by running

    aws s3 cp s3://MY_BUCKET/MY_OUTPUT_FILE.jsonl -

## Example 4: Using embeddings endpoint[¶](#example-4-using-embeddings-endpoint "Permanent link")

### Additional prerequisites[¶](#additional-prerequisites_1 "Permanent link") 

-   Ensure you are using `vllm >= 0.5.5`.

### Step 1: Create your batch file[¶](#step-1-create-your-batch-file_1 "Permanent link") 

Add embedding requests to your batch file. The following is an example:

    }
    }

You can even mix chat completion and embedding requests in the batch file, as long as the model you are using supports both chat completion and embeddings (note that all requests must use the same model).

### Step 2: Run the batch[¶](#step-2-run-the-batch_1 "Permanent link") 

You can run the batch using the same command as in earlier examples.

### Step 3: Check your results[¶](#step-3-check-your-results_1 "Permanent link") 

You can check your results by running `cat results.jsonl`

    cat results.jsonl
    ],"usage":}},"error":null}
    ...

## Example 5: Using score endpoint[¶](#example-5-using-score-endpoint "Permanent link")

### Additional prerequisites[¶](#additional-prerequisites_2 "Permanent link") 

-   Ensure you are using `vllm >= 0.7.0`.

### Step 1: Create your batch file[¶](#step-1-create-your-batch-file_2 "Permanent link") 

Add score requests to your batch file. The following is an example:

    }
    }

You can mix chat completion, embedding, and score requests in the batch file, as long as the model you are using supports them all (note that all requests must use the same model).

### Step 2: Run the batch[¶](#step-2-run-the-batch_2 "Permanent link") 

You can run the batch using the same command as in earlier examples.

### Step 3: Check your results[¶](#step-3-check-your-results_2 "Permanent link") 

You can check your results by running `cat results.jsonl`

    cat results.jsonl
    ,],"usage":}},"error":null}
    ,],"usage":}},"error":null}

## Example materials[¶](#example-materials "Permanent link")

openai_example_batch.jsonl

    ,],"max_completion_tokens": 1000}}
    ,],"max_completion_tokens": 1000}}