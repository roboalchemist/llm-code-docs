# Source: https://loops.so/docs/api-reference/list-mailing-lists.md

# List mailing lists

> Retrieve a list of your account's mailing lists.

## Request

No parameters.

## Response

This endpoint will return a list of mailing list objects.

If your account has no mailing lists, an empty list will be returned.

<ResponseField name="Lists" type="array">
  <Expandable title="properties" defaultOpen={true}>
    <ResponseField name="id" type="string">
      The ID of the list.
    </ResponseField>

    <ResponseField name="name" type="string">
      The name of the list.
    </ResponseField>

    <ResponseField name="description" type="string">
      The list's description. Will be `null` if no description has been added to the list.
    </ResponseField>

    <ResponseField name="isPublic" type="boolean">
      Whether the list is public (`true`) or private (`false`). [Read more](/contacts/mailing-lists#list-types)
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Response theme={"dark"}
  [
      {
          "id": "clxf1nxlb000t0ml79ajwcsj0",
          "name": "Mailing List Beta",
          "description": null,
          "isPublic": true
      },
      {
          "id": "clxf2q43u00010mlh12q9ggx1",
          "name": "Product B Launch",
          "description": "Get pre-launch updates about Product B.",
          "isPublic": true
      }
  ]
  ```
</ResponseExample>
