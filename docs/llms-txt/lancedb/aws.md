# Source: https://docs.lancedb.com/integrations/embedding/aws.md

# AWS Bedrock

export const PyEmbeddingAwsUsage = "import tempfile\nfrom pathlib import Path\n\nimport lancedb\nimport pandas as pd\nfrom lancedb.embeddings import get_registry\nfrom lancedb.pydantic import LanceModel, Vector\n\nmodel = get_registry().get(\"bedrock-text\").create()\n\nclass TextModel(LanceModel):\n    text: str = model.SourceField()\n    vector: Vector(model.ndims()) = model.VectorField()\n\ndf = pd.DataFrame({\"text\": [\"hello world\", \"goodbye world\"]})\ndb = lancedb.connect(str(Path(tempfile.mkdtemp()) / \"bedrock-demo\"))\ntbl = db.create_table(\"test\", schema=TextModel, mode=\"overwrite\")\n\ntbl.add(df)\nrs = tbl.search(\"hello\").limit(1).to_pandas()\nprint(rs.head())\n";

AWS Bedrock supports multiple base models for generating text embeddings. You need to setup the AWS credentials to use this embedding function.
You can do so by using `awscli` and also add your session\_token:

```shell  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
aws configure
aws configure set aws_session_token "<your_session_token>"
```

to ensure that the credentials are set up correctly, you can run the following command:

```shell  theme={"theme":{"light":"vitesse-light","dark":"catppuccin-mocha"}}
aws sts get-caller-identity
```

Supported Embedding modelIDs are:

* `amazon.titan-embed-text-v1`
* `cohere.embed-english-v3`
* `cohere.embed-multilingual-v3`

Supported parameters (to be passed in `create` method) are:

| Parameter               | Type | Default Value                | Description                                                                                                                                                            |
| ----------------------- | ---- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **name**                | str  | "amazon.titan-embed-text-v1" | The model ID of the bedrock model to use. Supported base models for Text Embeddings: amazon.titan-embed-text-v1, cohere.embed-english-v3, cohere.embed-multilingual-v3 |
| **region**              | str  | "us-east-1"                  | Optional name of the AWS Region in which the service should be called (e.g., "us-east-1").                                                                             |
| **profile\_name**       | str  | None                         | Optional name of the AWS profile to use for calling the Bedrock service. If not specified, the default profile will be used.                                           |
| **assumed\_role**       | str  | None                         | Optional ARN of an AWS IAM role to assume for calling the Bedrock service. If not specified, the current active credentials will be used.                              |
| **role\_session\_name** | str  | "lancedb-embeddings"         | Optional name of the AWS IAM role session to use for calling the Bedrock service. If not specified, a "lancedb-embeddings" name will be used.                          |
| **runtime**             | bool | True                         | Optional choice of getting different client to perform operations with the Amazon Bedrock service.                                                                     |
| **max\_retries**        | int  | 7                            | Optional number of retries to perform when a request fails.                                                                                                            |

Usage Example:

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {PyEmbeddingAwsUsage}
  </CodeBlock>
</CodeGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt