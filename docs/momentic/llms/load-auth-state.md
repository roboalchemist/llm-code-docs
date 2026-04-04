# Source: https://momentic.ai/docs/steps/load-auth-state.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Load auth state

> Load session data in JSON form into the current browser context

Load or clear session state using a JSON snapshot including cookies,
`localstorage`, and IndexDB entries.

## Inputs

<ResponseField name="Authentication state function" type="string" required>
  JavaScript code returning an object containing cookies and local storage to
  load into the session. The object should be in the same format returned by the
  [Save auth state](/steps/save-auth-state) step. Leave the function blank or
  return an empty object to clear the current session state instead.
</ResponseField>


Built with [Mintlify](https://mintlify.com).