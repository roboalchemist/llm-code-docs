# Source: https://docs.unstructured.io/ui/sources/opensearch.md

# Source: https://docs.unstructured.io/ui/destinations/opensearch.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/opensearch.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/opensearch.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/opensearch.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/opensearch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenSearch

<Note>
  If you're new to Unstructured, read this note first.

  Before you can create a destination connector, you must first sign in to your Unstructured account:

  * If you do not already have an Unstructured account, [sign up for free](https://unstructured.io/?modal=try-for-free).
    After you sign up, you are automatically signed in to your new Unstructured **Let's Go** account, at [https://platform.unstructured.io](https://platform.unstructured.io).
    To sign up for a **Business** account instead, [contact Unstructured Sales](https://unstructured.io/?modal=contact-sales), or [learn more](/api-reference/overview#pricing).
  * If you already have an Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business SaaS** account and are not already signed in, sign in to your account at
    [https://platform.unstructured.io](https://platform.unstructured.io). For other types of **Business** accounts, see your Unstructured account administrator for sign-in instructions,
    or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  After you sign in, the [Unstructured user interface](/ui/overview) (UI) appears, which you use to get your Unstructured API key.

  1. After you sign in to your Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business** account, click **API Keys** on the sidebar.<br />

     For a **Business** account, before you click **API Keys**, make sure you have selected the organizational workspace you want to create an API key
     for. Each API key works with one and only one organizational workspace. [Learn more](/ui/account/workspaces#create-an-api-key-for-a-workspace).

  2. Click **Generate API Key**.<br />

  3. Follow the on-screen instructions to finish generating the key.<br />

  4. Click the **Copy** icon next to your new key to add the key to your system's clipboard. If you lose this key, simply return and click the **Copy** icon again.<br />

  After you create the destination connector, add it along with a
  [source connector](/api-reference/workflow/sources/overview) to a [workflow](/api-reference/workflow/overview#workflows).
  Then run the worklow as a [job](/api-reference/workflow/overview#jobs). To learn how, try out the
  the notebook [Dropbox-To-Pinecone Connector API Quickstart for Unstructured](https://colab.research.google.com/github/Unstructured-IO/notebooks/blob/main/notebooks/Dropbox_To_Pinecone_Connector_Quickstart.ipynb),
  or watch the two 4-minute video tutorials for the [Unstructured Python SDK](/api-reference/workflow/overview#unstructured-python-sdk).

  You can also create destination connectors with the Unstructured user interface (UI).
  [Learn how](/ui/destinations/overview).

  If you need help, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  You are now ready to start creating a destination connector! Keep reading to learn how.
</Note>

Send processed data from Unstructured to OpenSearch.

The requirements are as follows.

* For the [Unstructured UI](/ui/overview) or the [Unstructured API](/api-reference/overview), local OpenSearch instances are not supported.

* For [Unstructured Ingest](/open-source/ingestion/overview), local and non-local OpenSearch instances are supported.

  For example, to set up an [AWS OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html) instance, complete steps similar to the following:

  1. Sign in to your AWS account, and then open your AWS Management Console.

  2. Open your Amazon OpenSearch Service console.

  3. On the sidebar, expand **Managed clusters**, and then click **Dashboard**.

  4. Click **Create domain**.

  5. In the **Name** tile, for **Domain name**, enter some unique domain name for your new OpenSearch instance.

  6. In the **Domain creation method** tile, select a method for creating the domain. For faster setup with sensible
     default settings, this example uses the **Easy create** method.
     [Learn more about the Standard create method](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html).

  7. In the **Engine options** tile, for **Version**, AWS recommends that you select the latest version.

  8. In the **Network** tile, for **Network**, select a network access method.
     For faster setup, this example uses the **Public access** method.
     [Learn more about the VPC access method](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html#prerequisites-vpc-endpoints).

  9. **For IP address type**, select **Dual-stack mode**.

  10. In the **Fine-grained access control** tile, do one of the following:

      * If you want to use an existing AWS IAM user in the AWS account as the domain's master user, then for **Master user**, select **Set IAM ARN as master user**. Then enter the IAM ARN for the master user in the **IAM ARN** box.
      * If you want to create a master user and password as the domain's master user instead, then for **Master user**, select **Create master user**. Then specify some username and password for this
        new master user by filling in the **Master username**, **Master password**, and **Confirm master password** fields. Make
        sure to save the master user's password in a secure location.

  11. Click **Create**.

  12. After the domain is created, you must allow Unstructured to access the domain, as follows:

      a. If the new domain's settings page is not already showing, open it as follows:
      in your Amazon Open Search Service console, on the sidebar, expand **Managed clusters**, and then click **Domains**. Then,
      in the list of available domains, click the name of the newly created domain.<br />
      b. On the **Security configuration** tab, click **Edit**.<br />
      c. In the **Access policy** tile, for **Domain access policy**, select **Only use fine-grained access control**.<br />
      d. Click **Clear policy**.<br />
      e. Click **Save changes**.

  The following video shows how to set up a [local OpenSearch](https://opensearch.org/downloads.html) instance.

  <iframe width="560" height="315" src="https://www.youtube.com/embed/Rew3_pNnYIs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* The instance's host URL, as follows:

  * For an AWS OpenSearch Service instance, do the following:

    1. Sign in to your AWS account, and then open your AWS Management Console.
    2. Open your Amazon OpenSearch Service console.
    3. On the sidebar, expand **Managed clusters**, and then click **Dashboard**.
    4. In the list of available domains, click the name of your domain.
    5. In the **General information** tile, copy the value of **Domain endpoint v2 (dual stack)**.

  * For a local OpenSearch instance, see [Communicate with OpenSearch](https://opensearch.org/docs/latest/getting-started/communicate/).

* The name of the search index on the instance.

  For the destination connector, if you need to create an index and you're using a master user and password as the domain's master user, you can use for example the following `curl` command. Replace the following placeholders:

  * Replace `<host>` with the instance's host URL.
  * Replace `<port>` with the instance's port number, which is typically `443` (for encrypted connections, and less commonly `9200` for unencrypted connections).
  * Replace `<master-username>` with the master user's name, and replace `<master-password>` with the master user's password.
  * Replace `<index-name>` with the name of the new search index on the instance.
  * Replace `<index-schema>` with the schema for the new search index on the instance. A schema is optional; see the explanation
    following this `curl` command for more information.

  ```bash  theme={null}
  curl --request PUT "<host>:<port>/<index-name>" \
  --user "<master-username>:<master-password>" \
  [--header "Content-Type: application/json" \
  --data '<index-schema>']
  ```

  If you're using an existing AWS IAM user as the domain's master user instead, you should use the AWS Command Line Interface (CLI) to create the index instead of using the preceding`curl` command. To learn how, see [create-index](https://docs.aws.amazon.com/cli/latest/reference/opensearch/create-index.html) in the AWS CLI Command Reference.

  For the destination connector, the index does not need to contain a schema beforehand. If Unstructured encounters an index without a schema,
  Unstructured will automatically create a compatible schema for you before inserting items into the index. Nonetheless,
  to reduce possible schema compatibility issues, Unstructured recommends that you create a schema that is compatible with Unstructured's schema.
  Unstructured cannot provide a schema that is guaranteed to work in all
  circumstances. This is because these schemas will vary based on your source files' types; how you
  want Unstructured to partition, chunk, and generate embeddings; any custom post-processing code that you run; and other factors.

  For objects in the `metadata` field that Unstructured produces and that you want to store in an OpenSearch index, you must create fields in your index's schema that
  follows Unstructured's `metadata` field naming convention. For example, if Unstructured produces a `metadata` field with the following
  child objects:

  ```json  theme={null}
  "metadata": {
    "is_extracted": "true",
    "coordinates": {
      "points": [
        [
          134.20055555555555,
          241.36027777777795
        ],
        [
          134.20055555555555,
          420.0269444444447
        ],
        [
          529.7005555555555,
          420.0269444444447
        ],
        [
          529.7005555555555,
          241.36027777777795
        ]
      ],
      "system": "PixelSpace",
      "layout_width": 1654,
      "layout_height": 2339
    },
    "filetype": "application/pdf",
    "languages": [
      "eng"
    ],
    "page_number": 1,
    "image_mime_type": "image/jpeg",
    "filename": "realestate.pdf",
    "data_source": {
      "url": "file:///home/etl/node/downloads/00000000-0000-0000-0000-000000000001/7458635f-realestate.pdf",
      "record_locator": {
        "protocol": "file",
        "remote_file_path": "file:///home/etl/node/downloads/00000000-0000-0000-0000-000000000001/7458635f-realestate.pdf"
      }
    },
    "entities": {
      "items": [
        {
          "entity": "HOME FOR FUTURE",
          "type": "ORGANIZATION"
        },
        {
          "entity": "221 Queen Street, Melbourne VIC 3000",
          "type": "LOCATION"
        }
      ],
      "relationships": [
        {
          "from": "HOME FOR FUTURE",
          "relationship": "based_in",
          "to": "221 Queen Street, Melbourne VIC 3000"
        }
      ]
    }
  }
  ```

  You can adapt the following index schema example for your own needs. Note that outside of `metadata`, the following fields are
  required by Unstructured whenever you create your own index schema:

  * `element_id`
  * `record_id`, which is required by Unstructured for intelligent record updates.
  * `type`, which is not required, but highly recommended.
  * `text`
  * `embeddings` if embeddings are generated; make sure to set `dimension` to the same number of dimensions as the embedding model generates.

  ```json  theme={null}
  {
    "settings": {
      "index": {
        "knn": true,
        "knn.algo_param.ef_search": 100
      }
    },
    "mappings": {
      "properties": {
        "element_id": {
          "type": "keyword"
        },
        "record_id": {
          "type": "text"
        },
        "text": {
          "type": "text"
        },
        "type": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 256
            }
          }
        },
        "embeddings": {
          "type": "knn_vector",
          "dimension": 1536
        },
        "metadata": {
          "properties": {
            "is_extracted": {
              "type": "boolean"
            },
            "coordinates-points": {
              "type": "float"
            },
            "coordinates-system": {
              "type": "text",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "coordinates-layout_width": {
              "type": "long"
            },
            "coordinates-layout_height": {
              "type": "long"
            },
            "filetype": {
              "type": "keyword"
            },
            "languages": {
              "type": "keyword"
            },
            "page_number": {
              "type": "integer"
            },
            "image_mime_type": {
              "type": "keyword"
            },
            "filename": {
              "type": "keyword"
            },
            "data_source-url": {
              "type": "keyword"
            },
            "data_source-record_locator-protocol": {
              "type": "keyword"
            },
            "data_source-record_locator-remote_file_path": {
              "type": "keyword"
            },
            "entities-items": {
              "properties": {
                "entity": {
                  "type": "text",
                  "fields": {
                    "keyword": {
                      "type": "keyword",
                      "ignore_above": 256
                    }
                  }
                },
                "type": {
                  "type": "text",
                  "fields": {
                    "keyword": {
                      "type": "keyword",
                      "ignore_above": 256
                    }
                  }
                }
              }
            },
            "entities-relationships": {
              "properties": {
                "from": {
                  "type": "text",
                  "fields": {
                    "keyword": {
                      "type": "keyword",
                      "ignore_above": 256
                    }
                  }
                },
                "relationship": {
                  "type": "text",
                  "fields": {
                    "keyword": {
                      "type": "keyword",
                      "ignore_above": 256
                    }
                  }
                },
                "to": {
                  "type": "text",
                  "fields": {
                    "keyword": {
                      "type": "keyword",
                      "ignore_above": 256
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  ```

  See also:

  * [Create an index](https://opensearch.org/docs/latest/api-reference/index-apis/create-index/)
  * [Mappings and field types](https://opensearch.org/docs/latest/field-types/)
  * [Explicit mapping](https://opensearch.org/docs/latest/field-types/#explicit-mapping)
  * [Dynamic mapping](https://opensearch.org/docs/latest/field-types/#dynamic-mapping)
  * [Unstructured document elements and metadata](/api-reference/partition/document-elements)

* For non-local OpenSearch instances, or if you're using basic authentication to a local OpenSearch instance, the master user's name and password.

* For local OpenSearch instances, if you're using certificates for authentication instead of basic authentication:

  * The path to the Certificate Authority (CA) bundle, if you use intermediate CAs with your root CA.
  * The path to the combined private key and certificate file, or
  * The paths to the separate private key and certificate file.

  To learn more, see [Authentication backends](https://opensearch.org/docs/latest/security/authentication-backends/authc-index/), [HTTP basic authentication](https://opensearch.org/docs/latest/security/authentication-backends/basic-authc/), and [Client certificate authentication](https://opensearch.org/docs/latest/security/authentication-backends/client-auth/).

To create an OpenSearch destination connector, see the following examples.

<CodeGroup>
  ```python Python SDK theme={null}
  import os

  from unstructured_client import UnstructuredClient
  from unstructured_client.models.operations import CreateDestinationRequest
  from unstructured_client.models.shared import CreateDestinationConnector

  with UnstructuredClient(api_key_auth=os.getenv("UNSTRUCTURED_API_KEY")) as client:
      response = client.destinations.create_destination(
          request=CreateDestinationRequest(
              create_destination_connector=CreateDestinationConnector(
                  name="<name>",
                  type="opensearch",
                  config={
                      "hosts": ["https://<host>:<port>"],
                      "index_name": "<index-name>",
                      "username": "<username>",
                      "password": "<password>",
                      "aws_access_key_id": "<aws-access-key-id>",
                      "aws_secret_access_key": "<aws-secret-access-key>",
                      "aws_session_token": "<aws-session-token>",
                      "use_ssl": <True|False>
                  }
              )
          )
      )

      print(response.destination_connector_information)
  ```

  ```bash curl theme={null}
  curl --request 'POST' --location \
  "$UNSTRUCTURED_API_URL/destinations" \
  --header 'accept: application/json' \
  --header "unstructured-api-key: $UNSTRUCTURED_API_KEY" \
  --header 'content-type: application/json' \
  --data \
  '{
      "name": "<name>",
      "type": "opensearch",
      "config": {
      "hosts": ["https://<host>:<port>"],
          "index_name": "<index-name>",
          "username": "<username>",
          "password": "<password>",
          "aws_access_key_id": "<aws-access-key-id>",
          "aws_secret_access_key": "<aws-secret-access-key>",
          "aws_session_token": "<aws-session-token>",
          "use_ssl": "true|false"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.

* `https://<host>:<port>` (*required*) - The OpenSearch instance's host URL, which typically takes the form of `https://<host>:<port>`.

* `<index-name>` (*required*) - The name of the search index on the instance.

* `<username>` - If you're using basic authentication to the instance, the domain's master user's name.

* `<password>` - If you're using basic authentication to the instance, the domain's master user's password.

* `<aws-access-key-id>` - If you're using an existing AWS IAM user as the domain's master user, the AWS access key ID for the AWS IAM user. If you're also using AWS STS for authentication, this will be a temporary AWS access key ID.

* `<aws-secret-access-key>` - If you're using an existing AWS IAM user as the domain's master user, the AWS secret access key for the AWS IAM user. If you're also using AWS STS for authentication, this will be a temporary AWS secret access key.

* `<aws-session-token>` - If you're using AWS STS for authentication, the temporary AWS STS session token.

  <Warning>
    AWS STS credentials (consisting of a temporary AWS access key, temporary AWS secret access key, and temporary AWS STS session token) can be valid for as little as 15 minutes or as long as 36 hours, depending on how the credentials were initially
    generated. After the expiry time, the credentials are no longer valid and will no longer work with the corresponding OpenSearch connector.
    You must get a new set of AWS STS credentials to replace the expired ones by, which produces
    a new, refreshed temporary AWS access key, temporary AWS secret access key, and temporary AWS STS session token. For more information, see
    [Request temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html).

    After you generate refreshed temporary AWS STS credentials, you must update the OpenSearch connector's settings with the new, refreshed AWS STS credentials.
  </Warning>

* `<field-name>` (*source connectors only*) - Any specific fields to be accessed in the index.

* `<use-ssl>` (*required*) - True if the OpenSearch instance requires an SSL connection; otherwise, false.
