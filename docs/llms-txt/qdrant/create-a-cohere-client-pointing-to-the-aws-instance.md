# Create a Cohere client pointing to the AWS instance
cohere_client = cohere.Client(...)

```

Next, our connector should be registered. **Please make sure to do it once, and store the id of the connector in the**
**environment variable or in any other way that will be accessible to the application.**

```python
import os

connector_response = cohere_client.connectors.create(
    name="customer-support",
    url=os.environ["RAG_CONNECTOR_URL"],
)