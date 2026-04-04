# Source: https://docs.pinecone.io/troubleshooting/unable-to-pip-install.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Unable to pip install

Python `3.x` uses `pip3`. Use the following commands in your terminal to install the latest version of the [Pinecone Python SDK](/reference/sdks/python/overview):

```Shell Shell theme={null}
# If you are connecting to Pinecone via gRPC:
pip3 install -U pinecone[grpc]
```

```Shell Shell theme={null}
# If you are connecting to Pinecone via HTTP:
pip3 install -U pinecone
```
