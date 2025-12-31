# Source: https://developer.mastercard.com/user-account-management-service/documentation/use-cases/cls-offer-activation/index.md

# CLS Offer Activations
source: https://developer.mastercard.com/user-account-management-service/documentation/use-cases/cls-offer-activation/index.md

## Add Card Linked Services (CLS) Offer Activation {#add-card-linked-services-cls-offer-activation}

This use case provides the ability for clients using CLS to add a new CLS offer activation, in real time, as cardholders pick and link their card to specific offers.

### Sequence Diagram {#sequence-diagram}

Diagram add-cls-activation

##### Following are the execution steps: {#following-are-the-execution-steps}

1. The cardholder signs into the customer application.
2. The customer authenticates the cardholder.
3. The customer sends a signed request to the User Account Management to add CLS account activations.
   * The request to add a mapping record requires the following mandatory input parameters:
     * userId - Unique identifier of the user.
     * userIdType - Identifier type for the given user.
     * transactionFilterCode - Used to filter transaction for eligibility rules. These codes are created by Mastercard during partner onboarding.
     * activationStatus - The status of the activation, valid values are A (ACTIVE) and I (INACTIVE).
4. The Mastercard API Gateway validates the customer's information and routes the request to the User Account Management in the case of a valid customer.
5. The User Account Management Service validates the signed request received through the `/cls/accounts/activations` endpoint.
6. The User Account Management Service creates the CLS offer activation.
7. The User Account Management Service sends a response with the activation ID (200).
8. The User Account Management Service sends a response with a status code of 4xx/5xx in case of an invalid request.

You will receive an error response for an invalid request or any missing request parameter. In that case, you need to update the input and perform step 3 again.

### Endpoint {#endpoint}


API Reference: `GET /cls/accounts/activations`

## Update Card Linked Services(CLS) Offer Activation {#update-card-linked-servicescls-offer-activation}

This use case is used when a customer wants to update an existing CLS offer activation of an account.

### Sequence Diagram {#sequence-diagram-1}

Diagram update-cls-activation

##### Following are the execution steps: {#following-are-the-execution-steps-1}

1. The cardholder signs into the customer application.
2. The customer authenticates the cardholder.
3. The customer sends a signed request to the User Account Management to update the CLS activations.
   * The request for updating the mapping record requires the following mandatory input parameters:
     * accountId - The unique identifier for the given account.
     * activationId - The unique identifier for the given account.
4. The Mastercard API Gateway validates the customer's information and routes the request to the User Account Management in the case of a valid customer.
5. The User Account Management Service validates the signed request received through the `/cls/accounts/{account_id}/activations/{activation_id}` endpoint.
6. The User Account Management Service updates the CLS offer activation.
7. The User Account Management Service sends a response with a status code of (200).
8. The User Account Management Service sends a response with a status code of 4xx/5xx in case of an invalid request.

You will receive an error response for an invalid request or any missing request parameter. In that case, you need to update the input and perform step 3 again.

### Endpoint {#endpoint-1}


API Reference: `GET /cls/accounts/{account_id}/activations/{activation_id}`

## Retrieve Card Linked Services(CLS) Offer Activations {#retrieve-card-linked-servicescls-offer-activations}

This use case is used when a customer wants to retrieve a list of all CLS offer activations of an account or filter based on search criteria in the request.

### Sequence Diagram {#sequence-diagram-2}

Diagram get-cls-activation

##### Following are the execution steps: {#following-are-the-execution-steps-2}

1. The cardholder signs into the customer application.
2. The customer authenticates the cardholder.
3. The customer sends a signed request to the User Account Management for CLS activation details.
   * The request for mapping record details requires the following mandatory request parameters:
     * accountId - The unique identifier for the given account.
4. Mastercard Network API Gateway authenticates and authorizes the customer and routes the request to the User Account Management in the case of a valid customer.
5. The User Account Management Service validates the request parameters received through the `/cls/accounts/{account_id}/activations` endpoint.
6. The User Account Management Service retrieves the CLS offer activation details.
7. The User Account Management Service sends a response with the CLS offer Activation details (200).
8. The User Account Management Service sends a response with a status code of 4xx/5xx in case of an invalid request.

You will receive an error response for an invalid request or any missing request parameter. In that case, you need to update the input and perform step 3 again.

### Endpoint {#endpoint-2}


API Reference: `GET /cls/accounts/{account_id}/activations`

Note: For more information about the error codes, refer to the [Code and Formats](https://developer.mastercard.com/user-account-management-service/documentation/code-and-formats/index.md) section.
