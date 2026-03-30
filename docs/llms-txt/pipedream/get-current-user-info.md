# Source: https://pipedream.com/docs/rest-api/api-reference/users/get-current-user-info.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Current User Info

Retrieve information on the authenticated user.

#### Endpoint

```
GET /users/me
```

#### Parameters

*No parameters*

<RequestExample>
  ```bash  theme={null}
  curl 'https://api.pipedream.com/v1/users/me' \
    -H 'Authorization: Bearer <token>'
  ```
</RequestExample>

<ResponseExample>
  ```json Free user theme={null}
  {
    "data": {
      "id": "u_abc123",
      "username": "dylburger",
      "email": "dylan@pipedream.com",
      "daily_compute_time_quota": 95400000,
      "daily_compute_time_used": 8420300,
      "daily_invocations_quota": 27344,
      "daily_invocations_used": 24903
      "orgs": [
        {
          "name": "MyWorkspace",
          "id": "o_abc123",
          "orgname": "myworkspace",
          "email": "workspace@pipedream.com",
          "daily_credits_quota": 100,
          "daily_credits_used": 0
        },
        {
          "name": "MyTeam",
          "id": "o_edf456",
          "orgname": "myteam",
          "email": "team@pipedream.com",
          "daily_credits_quota": 100,
          "daily_credits_used": 0,
          "daily_compute_time_quota": 1800000,
          "daily_compute_time_used": 0,
          "daily_invocations_quota": 100,
          "daily_invocations_used": 0
        }
      ],

    }
  }

  ```

  ```json Paid user theme={null}
  {
    "data": {
      "id": "u_abc123",
      "username": "user-35b7389db9e5222d42df6b3f0cfa8143"
      "email": "dylan@pipedream.com",
      "billing_period_start_ts": 1610154978,
      "billing_period_end_ts": 1612833378,
      "billing_period_credits": 12345
    }
  }
  ```

</ResponseExample>

Built with [Mintlify](https://mintlify.com).
