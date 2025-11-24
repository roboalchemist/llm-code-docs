# Source: https://docs.zapier.com/powered-by-zapier/sponsor-user-automation/user-enrollment.md

# User Enrollment

> Seamlessly enroll users in promotions to unlock exclusive benefits with a single API call.

The Create Promotion Enrollment endpoint allows you to enroll a user into an existing promotion by making a request to the [/v2/promotions endpoint](/powered-by-zapier/api-reference/promotions/create-enrollment). This operation associates a user, identified by their [user access token](/powered-by-zapier/authentication/methods/user-access-token), with a specific promotion.

To enroll a user in a promotion, send a POST request to the [/v2/promotions endpoint](/powered-by-zapier/api-reference/promotions/create-enrollment) with the required parameters in the request body.
Here’s an example request:

```json  theme={null}
// POST /v2/promotions
{
  "promotion_id": "partner_promotion_slug",
  "user_access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

Upon successful enrollment, the endpoint returns a JSON response containing the enrollment details.

```json  theme={null}
{
  "enrollment_id": "partner_promotion_slug:987fcdeb-1a2b-3c4d-5e6f-426614174999"
}
```

The enrollment\_id returned in the response can be used to track or manage the user’s enrollment in subsequent API calls.

### Usage Notes

* Ensure the promotion\_id corresponds to an existing promotion in the system.
* The user\_access\_token must be valid and unexpired to authenticate the user correctly.
* This API is [rate limited](/powered-by-zapier/api-reference/rate-limiting).
