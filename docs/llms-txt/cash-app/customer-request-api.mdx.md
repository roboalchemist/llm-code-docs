# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/customer-request-api.mdx

***

## stoplight-id: 138097b2280da

# Customer Request API

The Customer Request API helps developers request permission from customers to perform actions on their accounts. It is accessible from browsers, servers, and point of sale devices to reduce latency, only requiring a client ID as authentication.

In general, most developers should opt to use Pay Kit instead of using the Customer Request API directly. However, if Pay Kit is not able to work with your existing codebase, you can fall back to this API to implement a near-identical experience.

## Visualization

The following figure shows the visualization of the Customer Request API with different entities being involved at various stages:

![customer Request API visualization](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/CustomerRequest-API-visualization.png)

## Endpoints

* Requests
  * [Create request](/cash-app-pay-partner-api/api-reference/customer-request-api/create-request)
  * [Retrieve request](/cash-app-pay-partner-api/api-reference/customer-request-api/retrieve-request)
  * [Update request](/cash-app-pay-partner-api/api-reference/customer-request-api/update-request)
