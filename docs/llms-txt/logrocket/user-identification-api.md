# Source: https://docs.logrocket.com/docs/user-identification-api.md

# User Identification API

An API for sending user demographic, financial, and engagement data to LogRocket. 

## Summary

Leverage the User Identification API to send relevant user information from any backend system to LogRocket in order to contextualize user behavior and breakdown business metrics by revenue, subscription type, or product interest. This information supplements the identity information you capture clientside using our [identify method,](https://docs.logrocket.com/reference/identify) `logrocket.identify()`.

For example:

* Post revenue information for each customer and use this information to understand the revenue impact of a particular issue or poor user experience.
* Send subscription information in order to understand how engagement in the platform differs based on a user's subscription.
* Track product interest from social media campaigns in LogRocket in order to understand how many conversions each campaign is driving over time.
* While watching a session, peruse a detailed overview of the user in the session info tab of the replay.

**This feature is available for Pro and Enterprise plans.**

## PUT User Information

`PUT - https://api.logrocket.com/v1/orgs/<your_org_id>/apps/<your_app_id>/users/<user_id>`

### Authentication

To make user identification requests, you'll need your API key. You can find your API key in the dashboard under Settings > General Settings. Once you have your API key, you can include this as a header in requests to the LogRocket User Identification API as such:

```shell shell
curl https://api.logrocket.com/v1/orgs/<your_org_id>/apps/<your_app_id>/users/<user_id> \
  -H 'Authorization: token <your-api-key>' -d <request body>
```

<br />

### Example request bodies

**Create or update user traits**

Method: `PUT`

Endpoint: `/users/<user_id>`

```json
{
  "name": "John Smith",
  "email": "john.smith@gmail.com",
  "traits": {
    "age": 43,
    "favoriteColor": "blue",
    "plan": "free"
  }
}
```

This API request will update a user's traits with the new value for all traits that are present in the request. If a trait is not present in the request, it will maintain its previous value. To remove a trait, the trait should be provided in the request and set to a blank value.

## API Specification

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Optional or Required
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        name
      </td>

      <td>
        Optional
      </td>

      <td>
        A string that represents the user's name. Max: 1024 characters
      </td>
    </tr>

    <tr>
      <td>
        email
      </td>

      <td>
        Optional
      </td>

      <td>
        A string containing the user's email. Max: 1024 characters
      </td>
    </tr>

    <tr>
      <td>
        timestamp
      </td>

      <td>
        Optional
      </td>

      <td>
        Unix timestamp in ms indicating the timestamp of the submitted data. This timestamp will be used when determining when the user was first and last seen.
      </td>
    </tr>

    <tr>
      <td>
        traits
      </td>

      <td>
        Optional
      </td>

      <td>
        Object containing user trait names (as key) and user trait values (as values).

        Ex: \{ "plan": "FREE" }
      </td>
    </tr>
  </tbody>
</Table>

## Result Payload

When a request is successful, the API will return a 200 and a body containing the new user object. Any user trait values submitted as integers or booleans will be converted to strings in the result payload.

```json
{
  "userID": "1234",
  "name": "John Smith",
  "email": "john.smith@gmail.com",
  "traits": {
    "age": "43",
    "favoriteColor": "blue",
    "plan": "free"
  }
}
```

<br />

## Failures

If the request was not successful, the API will return an error status code and, if possible, a message that explains the error.

| Error Message                                      | Status | Description                                                                     |
| :------------------------------------------------- | :----- | :------------------------------------------------------------------------------ |
| "Missing request body"                             | 400    | PUT request is missing a body                                                   |
| "Malformed request"                                | 400    | PUT body doesn't conform to the schema                                          |
| "userID too large (max 1024 characters)"           | 400    | Validation error, all string keys and values must be less than 1024 characters. |
| "email too large (max 1024 characters)"            | 400    | Validation error, all string keys and values must be less than 1024 characters. |
| "name too large (max 1024 characters)"             | 400    | Validation error, all string keys and values must be less than 1024 characters. |
| "user trait value too large (max 1024 characters)" | 400    | Validation error, all string keys and values must be less than 1024 characters. |
| "user trait key too large"                         | 400    | Validation error, all string keys and values must be less than 1024 characters. |
| "Error processing user data"                       | 500    | LogRocket internal error, please contact support if this persists.              |