# Source: https://docs.picaos.com/api-reference/vault/connections/delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.picaos.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Connection

> Delete a Connection

## Path Parameters

<ParamField path="id" type="string" required>
  The connection ID
</ParamField>

## response

200 OK

<RequestExample>
  ```bash cURL theme={null}
  curl -X DELETE 'https://api.picaos.com/v1/vault/connections/conn_123' \
    -H 'x-pica-secret: YOUR_API_KEY'
  ```
</RequestExample>

<ResponseExample status="200">
  ```json 200 OK theme={null}
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).