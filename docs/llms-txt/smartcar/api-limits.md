# Source: https://smartcar.com/docs/help/api-limits.md

# Smartcar Usage Limits

> Learn about limits you may encounter when using Smartcar.

## Overview

There are several types of limits that govern your use of Smartcar. The nature of telematics requires us to carefully manage vehicle connections and traffic to ensure the stability of our platform and those of our upstream providers.

There are two major types of limits - **Billing Limits** and **Operational Rate Limits**.

# Billing Limits

### [BILLING : VEHICLE\_REQUEST\_LIMIT](/errors/api-errors/billing-errors#vehicle-request-limit)

Your Smartcar plan specifies a maximum number of API calls you are permitted to make to each single vehicle in a given month. If you exceed this limit, you will receive the `VEHICLE_REQUEST_LIMIT` error.

For example: you have been allocated 500 API calls per vehicle per month, but you made the 501<sup>st</sup> call to a single vehicle during the billing period.

**This limit can be changed.** If you require more calls per vehicle per month, contact [support@smartcar.com](mailto:support@smartcar.com) or your Account Manager and we can work with you to understand your options.

### [BILLING : VEHICLE\_LIMIT](/errors/api-errors/billing-errors#vehicle-request-limit)

Your Smartcar plan specifies a maximum number of vehicles that you may have connected at any one time. This limit applies to vehicle connections, and is separate from the limit regarding the number of API calls to those vehicles. If you receive this error, you have exceeded your maximum number of connected vehicles.

**This limit can be changed.** Reach out to [support@smartcar.com](mailto:support@smartcar.com) or your Account Manager to discuss your options.

# Operational Rate Limits

### [RATE\_LIMIT : SMARTCAR\_API](/errors/api-errors/rate-limit-errors#smartcar-api)

Smartcar limits the total number of requests a single application can make over a given period of time to ensure platform stability for all customers. The Smartcar API Limit is defined as a "bucket" of requests that refills at a constant rate over time.

The default Smartcar API Limit is a **bucket of 120 requests that refills at a rate of 2 requests per minute.**

If you receive a `RATE_LIMIT:SMARTCAR_API` response, your application has exceeded this limit. You should implement an exponential backoff strategy when retrying requests.

**This limit can be changed.** Reach out to [support@smartcar.com](mailto:support@smartcar.com) or your Account Manager to discuss your options.

### [RATE\_LIMIT : VEHICLE](/errors/api-errors/rate-limit-errors#vehicle)

Sending telematics requests to a vehicle causes it to wake up from its sleep state and consume energy and data resources. Excessive requests to a single vehicle can result in:

* EV battery drain
* 12 volt battery drain
* `UPSTREAM:RATE_LIMIT` errors that prevent you from making requests for a longer period of time

Smartcar enforces a per-vehicle rate limit that governs the rate of requests to a single vehicle and mitigates these potential issues. These limits can differ based on the vehicle manufacturer and a number of other factors, and are set by Smartcar to ensure consistent and timely data can be retrieved from vehicles.

**This limit cannot be changed.** If you receive this response, refer to the `retry-after` header (returned as seconds) for when to retry the request.

### [UPSTREAM : RATE\_LIMIT](/errors/api-errors/upstream-errors#rate-limit)

Vehicle manufacturers sometimes impose rate limits on requests to vehicles. The Smartcar Vehicle Rate Limit will generally prevent those limits from being reached, but outside requests from other providers may cause the upstream limit to be exceeded. If the OEM upstream rate limit is exceeded, you will receive `UPSTREAM:RATE_LIMIT` from the Smartcar API for the affected vehicle until the limit is reset.

**This limit cannot be changed.** Smartcar cannot control rate limits imposed by our upstream providers. If you consistently receive this response for a single vehicle, reach out to [support@smartcar.com](mailto:support@smartcar.com) and we can investigate.
