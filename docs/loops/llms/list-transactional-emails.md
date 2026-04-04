# Source: https://loops.so/docs/api-reference/list-transactional-emails.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List transactional emails

> Retrieve a list of your transactional emails.

## Request

### Query parameters

<ParamField query="perPage" type="string" default={20}>
  How many results to return in each request. Must be between 10 and 50.
</ParamField>

<ParamField query="cursor" type="string">
  A cursor, to return a specific page of results. Cursors can be found from the `pagination.nextCursor` value in each response.
</ParamField>

## Response

This endpoint will return a list of all *published* transactional emails in your account.

<ResponseField name="pagination" type="object">
  <Expandable title="metadata" defaultOpen={false}>
    <ResponseField name="totalResults" type="number">
      Total results found.
    </ResponseField>

    <ResponseField name="returnedResults" type="number">
      The number of results returned in this response.
    </ResponseField>

    <ResponseField name="perPage" type="number">
      The maximum number of results requested.
    </ResponseField>

    <ResponseField name="totalPages" type="number">
      Total number of pages.
    </ResponseField>

    <ResponseField name="nextCursor" type="nullable string">
      The next cursor (for retrieving the next page of results using the `cursor` parameter), or `null` if there are no further pages.
    </ResponseField>

    <ResponseField name="nextPage" type="nullable string">
      The URL of the next page of results, or `null` if there are no further pages.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="data" type="array">
  <Expandable title="properties" defaultOpen={true}>
    <ResponseField name="id" type="string">
      The transactional email's ID.
    </ResponseField>

    <ResponseField name="name" type="string">
      The transactional email's name.
    </ResponseField>

    <ResponseField name="lastUpdated" type="string">
      The date the email was last updated in [ECMA-262 date-time](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-date-time-string-format) format.
    </ResponseField>

    <ResponseField name="dataVariables" type="array">
      Data variables in the transactional email.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Response theme={"dark"}
  {
    "pagination": {
      "totalResults": 23,
      "returnedResults": 20,
      "perPage": 20,
      "totalPages": 2,
      "nextCursor": "clyo0q4wo01p59fsecyxqsh38",
      "nextPage": "https://app.loops.so/api/v1/transactional?cursor=clyo0q4wo01p59fsecyxqsh38&perPage=20"
    },
    "data": [
      {
        "id": "clfn0k1yg001imo0fdeqg30i8",
        "name": "Welcome email",
        "lastUpdated": "2023-11-06T17:48:07.249Z",
        "dataVariables": []
      },
      {
        "id": "cll42l54f20i1la0lfooe3z12",
        "name": "Sign up confirmation",
        "lastUpdated": "2025-02-02T02:56:28.845Z",
        "dataVariables": [
          "confirmationUrl"
        ]
      },
      {
        "id": "clw6rbuwp01rmeiyndm80155l",
        "name": "Invitation",
        "lastUpdated": "2024-05-14T19:02:52.000Z",
        "dataVariables": [
          "firstName",
          "lastName",
          "inviteLink"
        ]
      },
      ...
    ]
  }
  ```
</ResponseExample>
