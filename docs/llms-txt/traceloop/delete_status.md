# Source: https://www.traceloop.com/docs/api-reference/privacy/delete_status.md

# Status of user deletion request

Get the status of your user deletion request.

## Request Query Parameter

<ParamField query="requestId" type="string">
  The request ID from the user deletion request.
</ParamField>

## Response

<ResponseField name="completed" type="boolean">
  `true` if the process was completed, `false` otherwise.
</ResponseField>

<ResponseField name="deleted" type="string">
  The number of spans that were deleted.
</ResponseField>

<ResponseField name="total" type="string">
  The number of spans that needs to be deleted in total.
</ResponseField>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.traceloop.com/docs/llms.txt