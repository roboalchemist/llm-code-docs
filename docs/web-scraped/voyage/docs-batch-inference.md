# Source: https://docs.voyageai.com/docs/batch-inference

## GET STARTED 

- [[[Introduction]]](/docs/introduction)
- [[[API Key and Python Client]]](/docs/api-key-and-installation)
- [[[Quickstart Tutorial]]](/docs/quickstart-tutorial)

## CAPABILITIES 

- [[[Text Embeddings]]](/docs/embeddings)
- [[[Contextualized Chunk Embeddings]]](/docs/contextualized-chunk-embeddings)
- [[[Multimodal Embeddings]]](/docs/multimodal-embeddings)
- [[[Rerankers]]](/docs/reranker)

## GUIDES 

- [[[Tokenization]]](/docs/tokenization)
- [[[Flexible Dimensions and Quantization]]](/docs/flexible-dimensions-and-quantization)
- [[[Batch Inference]]](/docs/batch-inference)
- [[[Error Codes]]](/docs/error-codes)
- [[[Rate Limits]]](/docs/rate-limits)
- [[[Pricing]]](/docs/pricing)
- [[[Organizations and Projects]]](/docs/organizations-and-projects)
- [[[Service Level Objectives]]](/docs/service-level-objectives)

## DEPLOYMENT ON VPC 

- [[AWS Marketplace Model Package]]
  - [[[MongoDB Voyage AI Models in AWS]]](/docs/aws-marketplace-mongodb-voyage)
  - [[[Voyage AI Models in AWS]]](/docs/aws-marketplace-voyage)
- [[Azure Marketplace Managed Application]]
  - [[[MongoDB Voyage AI Models in Azure]]](/docs/azure-marketplace-mongodb-voyage)
  - [[[Voyage AI Models in Azure]]](/docs/azure-marketplace-voyage)

## ACCESS VIA DATA PLATFORMS 

- [[[Snowflake]]](/docs/snowflake)

## Community 

- [[[Integrations]]](/docs/integrations-and-other-libraries)
- [[[Community SDKs]]](/docs/community-sdks)

## HELP 

- [[[FAQ]]](/docs/faq)
- [[[Contact Email]]](/docs/contact-email)
- [[[Discord]]](/docs/discord)

Powered by [](https://readme.com?ref_src=hub&project=voyage-ai)

# Batch Inference

> [🚧]
>
> This feature is in Public Preview. The feature and the corresponding documentation might change at any time during the Preview period. To learn more, see [Preview Features](https://www.mongodb.com/docs/preview-features/).

Real-time API responses are unnecessary in some scenarios, such as when embedding large corpora for vector databases or running large-scale evaluations. In these cases, the **Batch API** provides a simple way to process multiple requests efficiently. It handles retries and threading automatically, ensuring high throughput and reliable results. You bundle requests into a single file, initiate a batch job, track its status as it runs, and retrieve results once complete. Our Batch API offers a **12-hour completion window** and is more cost-effective than standard endpoints, providing a **33% discount**.

You can also explore the API reference directly [here](/reference/batch).

#  

Getting Started

[](#getting-started)

You can create batch jobs for the following endpoints: `/v1/embeddings` ([Text embedding models](https://docs.voyageai.com/reference/embeddings-api)), `/v1/contextualizedembeddings` ([Contextualized chunk embedding models](https://docs.voyageai.com/reference/contextualized-embeddings-api)), and `v1/rerank` ([Rerankers](https://docs.voyageai.com/reference/reranker-api)).

**Projects**. Batch jobs are tied to specific projects and can only be viewed or managed within the projects linked to the API keys used to create them.

##  

1\. Create Batch Input File

[](#1-create-batch-input-file)

The input data for batch requests are bundled in a JSONL file. This separation of input data from other request parameters allows for reuse of the batch input file \-- supporting experimentation, evaluation, and re-vectorizing use cases over the same data. The details, including an example of the batch request input object, are in the following collapsed section.

Batch request input object

A batch request input object requires two keys: `custom_id` and `body`.

- `custom_id`. This is a user-provided ID used to match outputs to inputs since the ordering of output results will not necessarily be aligned with the ordering of input requests. The
  `custom_id` values must be unique for each request in a batch.
- `body`. This is the input data of the underlying endpoint. The model and other other parameters are specified at the batch level will be used for all requests in the batch. How the input data is specified depends on the endpoint:
  `input` for
  `v1/embeddings`,
  `inputs` for
  `v1/contextualizedembeddings`, and
  `query` and
  `documents` for
  `v1/rerank`.

**Examples**

JSONL snippet for v1/embeddings

JSONL snippet for v1/contextualizedembeddings

JSONL snippet for v1/rerank

    }
    }

    }
    }

    }
    }

**100K inputs per batch maximum**. Each batch can contain up to 100K inputs. Each request may include multiple examples. For instance, a single request to the `v1/embeddings` endpoint can contain up to 1,000 examples. Each request is still subject to the context length (e.g., 32K tokens for `voyage-3.5`) and total token limit (e.g., 320K tokens for `voyage-3.5`) of the target model and endpoint.

##  

2\. Upload Batch Input File

[](#2-upload-batch-input-file)

In order for batch jobs to access the batch input file, it must be uploaded using our [Files API](/reference/files). The following example uploads a batch input file named `foo.jsonl`:

cURL

Example cURL response

    curl https://api.voyageai.com/v1/files \
      -H "Authorization: Bearer $VOYAGE_API_KEY" \
      -F purpose="batch" \
      -F file="@foo.jsonl"

    

When you successfully upload your batch input file, the input file will be given a file ID that can be referenced when creating a batch job.

Listing files

You can always verify your files by listing them. The following example lists your available files:

cURL

Example cURL response

    curl https://api.voyageai.com/v1/files \
      -H "Authorization: Bearer $VOYAGE_API_KEY"

    ,
      
    ],
    "first_id": "file-abc123",
    "last_id": "file-def456",
    "has_more": false

##  

3\. Create the Batch

[](#3-create-the-batch)

When creating a batch, you must specify the batch input file, endpoint, completion window, and model. Optionally, you can provide up to 16 custom key-value pairs to associate with the batch job using the `metadata` parameter. For example, you could provide a custom `corpus` key to associate the corpus you may be vectorizing.

A `Batch` object containing metadata about the batch job, such as an assigned batch id, will be created and returned.

**Example**

cURL

    curl -X POST https://api.voyageai.com/v1/batches \
      -H "Authorization: Bearer $VOYAGE_API_KEY" \
      -H "content-type: application/json" \
      -d ' 
      ,
        "input_file_id": "file-abc123",
        "metadata": 
      }'

The `request_params` parameter specifies all endpoint parameters for requests, except for the input data, which is provided in the batch input JSONL file. The only required endpoint parameter---and the only mandatory key in `request_params`---is `model`. Essentially, the batch job combines the input data from the batch input JSONL file with the endpoint parameters in `request_params` to form the inference requests that are ultimately processed. Any endpoint parameter not explicitly set will default to the endpoint's default value. Below is an example of a batch job created with multiple endpoint parameters specified in `request_params`.

cURL

    curl -X POST https://api.voyageai.com/v1/batches \
      -H "Authorization: Bearer $VOYAGE_API_KEY" \
      -H "content-type: application/json" \
      -d ' 
      ,
        "input_file_id": "file-abc123",
        "metadata": 
      }'

##  

4\. Check Batch Status

[](#4-check-batch-status)

Once created, batch jobs have an **12-hour completion window**. If a batch job cannot be finished within this time, the job will process as many requests as possible. Completed results will be provided in an output file, and users will only be charged for tokens used in these requests.

As the batch job progresses through its lifecycle, the Batch object will be updated, and it can be queried to check on the status of the batch job. More on the batch lifecycle in a [section below](/docs/batch-inference#batch-lifecycle) .

###  

Example: Retrieve batch for status

[](#example-retrieve-batch-for-status)

To check the status of a batch, you need to specify its batch id.

cURL

Example cURL response

    curl https://api.voyageai.com/v1/batches/batch-abc123 \
      -H "Authorization: Bearer $VOYAGE_API_KEY" \
      -H "Content-Type: application/json"

    ,
      "metadata": 
    }

##  

5\. Retrieve Results

[](#5-retrieve-results)

Once a batch job successfully completes, a JSONL output file will be created with the results, where there will be one response line for every successful request from the batch input file.

> [🚧]
>
> Note that the output line order may not match the input line order. Instead of relying on order to process your results, use the `custom_id` field, which will be present in each line of your output results file and allow you to map requests in your input to results in your output.

You can retrieve and download the output file using the [Files API](/reference/files). The Batch object will provide the file id of the output file in the `output_file_id` field.

For failed requests, error information will be written to an error file specified by the `error_file_id` field of the Batch object.

**Example**

cURL

Example cURL response

    curl https://api.voyageai.com/v1/batches/batch-def456 \
      -H "Authorization: Bearer $VOYAGE_API_KEY" \
      -H "Content-Type: application/json"

    ,
      "metadata": 
    }

The following code snippets show you how to retrieve the actual contents of your output file.

cURL

Python

    curl https://api.voyageai.com/v1/files/file-xyz987/content \
      -H "Authorization: Bearer $VOYAGE_API_KEY" > foo_batch_results.jsonl

    import voyageai
    vo = voyageai.Client()

    output_file = vo.files.content(file_id='file_xyz987')
    output_file.write_to_file(file='foo_batch_results.jsonl')

##  

6\. Cancel a Batch

[](#6-cancel-a-batch)

You can cancel an ongoing batch at any time. The batch\'s status will change to `cancelling` until in-flight requests are complete (up to 10 minutes), after which the status will change to `cancelled`.

Any completed results before cancelation will be available in the output file, and users will be charged for the tokens consumed from completed requests. There is no penalty for cancellation.

**Example**

cURL

Example cURL response cancelling

Example cURL response cancelled

    curl https://api.voyageai.com/v1/batches/batch-abc123/cancel \
      -H "Authorization: Bearer $VOYAGE_API_KEY" \
      -H "Content-Type: application/json" \
      -X POST

    ,
      "metadata": ,
      "created_at": "2025-11-19T02:46:44.547607+00:00",
      "in_progress_at": "2025-11-19T02:46:45.992553+00:00",
      "finalizing_at": null,
      "completed_at": null,
      "failed_at": null,
      "expected_completion_at": "2025-11-19T10:46:44.547607+00:00",
      "cancelling_at": "2025-11-19T02:46:46.202515+00:00",
      "cancelled_at": null
    }

    ,
      "metadata": ,
      "created_at": "2025-11-19T02:46:44.547607+00:00",
      "in_progress_at": "2025-11-19T02:46:45.992553+00:00",
      "finalizing_at": null,
      "completed_at": null,
      "failed_at": null,
      "expected_completion_at": "2025-11-19T10:46:44.547607+00:00",
      "cancelling_at": "2025-11-19T02:46:46.202515+00:00",
      "cancelled_at": "2025-11-19T02:46:48.970135+00:00"
    }

##  

7\. Get a List of Batches

[](#7-get-a-list-of-batches)

At any time, you can see all your batches. For users with many batches, you can use the `limit` and `after` parameters to paginate your results.

cURL

Example cURL response

    curl https://api.voyageai.com/v1/batches \
      -H "Authorization: Bearer $VOYAGE_API_KEY" \
      -H "Content-Type: application/json"

    ,
          "metadata": ,
          "created_at": "2025-11-19T02:47:42.031781+00:00",
          "in_progress_at": "2025-11-19T02:47:46.166042+00:00",
          "finalizing_at": "2025-11-19T02:48:00.101059+00:00",
          "completed_at": "2025-11-19T02:48:09.221885+00:00",
          "failed_at": null,
          "expected_completion_at": "2025-11-19T10:47:42.031781+00:00",
          "cancelling_at": null,
          "cancelled_at": null
        },
        ,
          "metadata": ,
          "created_at": "2025-11-19T02:46:44.547607+00:00",
          "in_progress_at": "2025-11-19T02:46:45.992553+00:00",
          "finalizing_at": null,
          "completed_at": null,
          "failed_at": null,
          "expected_completion_at": "2025-11-19T10:46:44.547607+00:00",
          "cancelling_at": "2025-11-19T02:46:46.202515+00:00",
          "cancelled_at": "2025-11-19T02:46:48.970135+00:00"
        }
      ]
    }

#  

Batch lifecycle

[](#batch-lifecycle)

The following diagram illustrates the batch lifecycle, showing state transitions from one status to another.

[[![Batch Lifecycle](https://files.readme.io/96601ff80bf6cca1d14136a34bad5b72ade4f5a5a1370d5fe37c6c6122e73783-batch-api-Batch_Lifecycle.png)]]

All jobs start by validating the input (i.e., their status is `validating`).

**Standard, successful batch job.** A standard, successful job is ready to process after input validation is complete, moving into the `in_progress` status. The results are prepared once the job is completed and the job is in the `finalizing` status. Once the results are ready, the job is marked as `completed`.

**Failed job.** Jobs not properly validated will have a `failed` status.

**Cancelled jobs.** Users can cancel jobs at any time. If a cancellation is initiated, the job enters the `cancelling` status, which can take up to 10 minutes until the job is actually cancelled. Once cancelled, the job is marked as `cancelled`.

**Partially complete jobs.** If the job has not been completed within the completion window, it will prepare the results that it has completed. The unfinished requests will be written in your error file with the message shown below. You can use the `custom_id` to retrieve the request data for unfinished requests. You will only be charged for tokens consumed from any completed requests.

**Lifecycle tracking.** The batch lifecycle is tracked in the Batch object, storing the timestamps of when the batch enters various statuses. See the [Batch API reference](/reference/batch) for details.

The table below summarizes and describes the various batch statuses.

  Status                                                       Description
  ------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `validating`    The input file is being validated before the batch can begin. This checks that the requests in the input file are valid, such as adhering to the input request schema and valid schema keys.
  `failed`        Input validation has failed.
  `in_progress`   The batch is currently being run.
  `finalizing`    The batch has been completed, and the results are being prepared.
  `completed`     The batch has been completed, and the results are ready
  `cancelling`    The batch is being canceled (it may take up to 10 minutes).
  `cancelled`     The batch was canceled.

#  

Organization Limits

[](#organization-limits)

**In-flight batch jobs** are those with the following statuses: `validating`, `in_progress`, `finalizing`, and `cancelling`. An organization must not have more than **10 in-flight batch jobs** or **exceed 500M tokens** across all of them. Additionally, each batch job may contain no more than **100K inputs**.

#  

Batch Results

[](#batch-results)

As mentioned earlier, once a batch job successfully completes, a JSONL output file will be created with the results, where there will be one response line for every successful request from the batch input file.

Batch output file object

    
          ],
          "model": "voyage-3.5",
          "usage": 
        }
      },
      "error": null
    }

#  

Batch Errors

[](#batch-errors)

For failed requests, error information will be written to an error file, a JSONL file where there will be one line for every failed requests.

JSON

    ,
      "error": null
    }

JSON

    
    }

#  

Model Availability

[](#model-availability)

The Batch API can currently be used to execute queries against the following models: `voyage-3-large`, `voyage-3.5`, `voyage-3.5-lite`, `voyage-context-3`, `voyage-code-3`, `voyage-code-2`, `rerank-2.5`, and `rerank-2.5-lite`.

Updated 3 days ago

------------------------------------------------------------------------

[[]](/docs/flexible-dimensions-and-quantization)

Flexible Dimensions and Quantization

[](/docs/error-codes)

Error Codes

[]

- [Table of Contents](#)
- - [Getting Started](#getting-started)
  - - [1. Create Batch Input File](#1-create-batch-input-file)
    - [2. Upload Batch Input File](#2-upload-batch-input-file)
    - [3. Create the Batch](#3-create-the-batch)
    - [4. Check Batch Status](#4-check-batch-status)
    - [5. Retrieve Results](#5-retrieve-results)
    - [6. Cancel a Batch](#6-cancel-a-batch)
    - [7. Get a List of Batches](#7-get-a-list-of-batches)
  - [Batch lifecycle](#batch-lifecycle)
  - [Organization Limits](#organization-limits)
  - [Batch Results](#batch-results)
  - [Batch Errors](#batch-errors)
  - [Model Availability](#model-availability)