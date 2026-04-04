# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/customer-request-api/schemas/request.mdx

<EndpointSchemaSnippet endpoint="POST /requests" selector="response.body" />

<Aside>
  ```json Example
  {
    "id": "GRR_1hrxhz136krcq6ezdte2ha5q",
    "status": "PENDING",
    "actions": [
      {
        "amount": 2500,
        "currency": "USD",
        "scope_id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
        "type": "ONE_TIME_PAYMENT"
      }
    ],
    "auth_flow_triggers": {
      "qr_code_image_url": "https://api.cash.app/qr/f/GRANTLY_MANAGED_GRANT%3Frequest_id=GRR_1hrxhz136krcq6ezdte2ha5q-k21srg&method=qr?rounded=0&format=png",
      "qr_code_svg_url": "https://api.cash.app/qr/f/GRANTLY_MANAGED_GRANT%3Frequest_id=GRR_1hrxhz136krcq6ezdte2ha5q-k21srg&method=qr?rounded=0&format=svg",
      "mobile_url": "https://cash.app/f/GRANTLY_MANAGED_GRANT%3Frequest_id=GRR_1hrxhz136krcq6ezdte2ha5q-k21srg&method=mobile_url",
      "refreshes_at": "2019-08-24T14:15:22Z",
      "desktop_url": "https://pay.cash.app?customerRequestId={request_id}"
    },
    "redirect_url": "https://example.com",
    "created_at": "2022-01-01T12:09:00Z",
    "updated_at": "2022-01-01T12:10:00Z",
    "expires_at": "2033-01-01T12:20:00Z",
    "origin": {
      "type": "DIRECT",
      "id": "string"
    },
    "channel": "ONLINE",
    "grants": [
      {
        "id": "GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50",
        "customer_id": "CST_AQmxh4y_QGoNNIG5NUw0jttqyYedL1LklACQdyJ3H-Vs6WmLtP6A_C7XjQNohvY",
        "action": {
          "amount": 2500,
          "currency": "USD",
          "scope_id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
          "type": "ONE_TIME_PAYMENT"
        },
        "status": "ACTIVE",
        "type": "ONE_TIME",
        "channel": "ONLINE",
        "created_at": "2019-08-24T14:15:22Z",
        "updated_at": "2019-08-24T14:15:22Z",
        "expires_at": "2022-04-01T12:00:00Z"
      }
    ],
    "reference_id": "external-id",
    "requester_profile": {
      "name": "A Brand",
      "logo_url": "https://picsum.photos/200"
    },
    "customer_profile": {
      "id": "CST_AQmxh4y_QGoNNIG5NUw0jttqyYedL1LklACQdyJ3H-Vs6WmLtP6A_C7XjQNohvY",
      "cashtag": "$CashTag"
    },
    "metadata": {},
    "customer_metadata": {
      "reference_id": "string"
    }
  }
  ```
</Aside>
