# Source: https://docs.fireflies.ai/schema/input/active-meetings-input.md

# GetActiveMeetingsInput

> Schema for GetActiveMeetingsInput

<ParamField path="email" type="String">
  Filter active meetings by a specific user's email address.

  **Permission requirements:**

  * **Regular users**: Can only query their own active meetings (must pass their own email or omit this field)
  * **Admins**: Can query active meetings for any user in their team

  If this field is omitted, the query returns active meetings for the authenticated user.

  The email must be valid and belong to a user in the same team as the requester.
</ParamField>
