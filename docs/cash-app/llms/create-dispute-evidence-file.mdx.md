# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/create-dispute-evidence-file.mdx

# Create dispute evidence file

POST https://api.cash.app/network/v1/disputes/{dispute_id}/evidence-file
Content-Type: multipart/form-data

Uploads a binary file as a piece of evidence for the given dispute, which can then be submitted with the [challenge dispute](Network-API.v1.yaml/paths/~1disputes~1{dispute_id}~1challenge) endpoint.

The file must be one of the supported formats, or else it may not be usable to challenge the dispute:

- `JPEG`
- `HEIC`
- `HEIF`
- `PNG`
- `PDF`
- `TIFF`

<Note> 
Uploading evidence does not challenge the dispute. Make sure to call the [challenge dispute](Network-API.v1.yaml/paths/~1disputes~1{dispute_id}~1challenge) endpoint before the `response_due_at` timestamp, or else the merchant will automatically "lose" the dispute.
</Note>

**This endpoint is not rate limited.**

Scopes: `DISPUTES_WRITE`

---

### Example request payload (cURL)

The following example shows how to make a request to upload a dispute file. There are two "parts" of the request:

- `request`, a JSON blob that contains details about the file to upload
- `file`, which contains the binary data for the file to be uploaded.

Using `cURL` to make the request, the request would look like the example below. Please refer to documentation for your particular language / framework and `multipart/form-data` requests to see how you should implement it in your own codebase.

Please refer to [Signing Multipart Requests](https://developers.cash.app/docs/partner/technical-documentation/api-fundamentals/requests/signing-requests) to compute a signature for the request.

```curl
curl --request POST 'https://sandbox.api.cash.app/network/v1/disputes/DSPT_ztqn5hd8wmrzjzavmf60pjbzf/evidence-file' \
--header 'Accept: application/json' \
--header 'Authorization: Client CLIENT_ID API_KEY_ID' \
--header 'Content-Type: multipart/form-data' \
--header 'X-Region: PDX' \
--form 'request={
  "idempotency_key": "e445c3fb-2caa-46fd-b0d3-aa7c7b00ab41",
  "evidence": {
    "category": "AUTHORIZATION_DOCUMENTATION",
    "file": {
      "filename": "evidence.pdf",
      "content_type": "application/pdf"
    }
  }
}' \
--form 'signature=SIGNATURE' \
--form 'file=path-to-file.pdf' 
```

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/create-dispute-evidence-file

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /disputes/{dispute_id}/evidence-file:
    post:
      operationId: create-dispute-evidence-file
      summary: Create dispute evidence file
      description: >-
        Uploads a binary file as a piece of evidence for the given dispute,
        which can then be submitted with the [challenge
        dispute](Network-API.v1.yaml/paths/~1disputes~1{dispute_id}~1challenge)
        endpoint.


        The file must be one of the supported formats, or else it may not be
        usable to challenge the dispute:


        - `JPEG`

        - `HEIC`

        - `HEIF`

        - `PNG`

        - `PDF`

        - `TIFF`


        <Note> 

        Uploading evidence does not challenge the dispute. Make sure to call the
        [challenge
        dispute](Network-API.v1.yaml/paths/~1disputes~1{dispute_id}~1challenge)
        endpoint before the `response_due_at` timestamp, or else the merchant
        will automatically "lose" the dispute.

        </Note>


        **This endpoint is not rate limited.**


        Scopes: `DISPUTES_WRITE`


        ---


        ### Example request payload (cURL)


        The following example shows how to make a request to upload a dispute
        file. There are two "parts" of the request:


        - `request`, a JSON blob that contains details about the file to upload

        - `file`, which contains the binary data for the file to be uploaded.


        Using `cURL` to make the request, the request would look like the
        example below. Please refer to documentation for your particular
        language / framework and `multipart/form-data` requests to see how you
        should implement it in your own codebase.


        Please refer to [Signing Multipart
        Requests](https://developers.cash.app/docs/partner/technical-documentation/api-fundamentals/requests/signing-requests)
        to compute a signature for the request.


        ```curl

        curl --request POST
        'https://sandbox.api.cash.app/network/v1/disputes/DSPT_ztqn5hd8wmrzjzavmf60pjbzf/evidence-file'
        \

        --header 'Accept: application/json' \

        --header 'Authorization: Client CLIENT_ID API_KEY_ID' \

        --header 'Content-Type: multipart/form-data' \

        --header 'X-Region: PDX' \

        --form 'request={
          "idempotency_key": "e445c3fb-2caa-46fd-b0d3-aa7c7b00ab41",
          "evidence": {
            "category": "AUTHORIZATION_DOCUMENTATION",
            "file": {
              "filename": "evidence.pdf",
              "content_type": "application/pdf"
            }
          }
        }' \

        --form 'signature=SIGNATURE' \

        --form 'file=path-to-file.pdf' 

        ```
      tags:
        - subpackage_disputes
      parameters:
        - name: dispute_id
          in: path
          required: true
          schema:
            type: string
        - name: Accept
          in: header
          required: true
          schema:
            type: string
        - name: X-Region
          in: header
          required: true
          schema:
            type: string
        - name: X-Signature
          in: header
          required: true
          schema:
            type: string
        - name: User-Agent
          in: header
          required: true
          schema:
            type: string
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Disputes_create-dispute-evidence-file_Response_201
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      requestBody:
        description: ''
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                request:
                  $ref: >-
                    #/components/schemas/DisputesDisputeIdEvidenceFilePostRequestBodyContentMultipartFormDataSchemaRequest
                  description: >-
                    JSON-encoded payload describing the contents of the file
                    uploaded
                file:
                  type: string
                  format: binary
                  description: |-
                    Binary file to upload

                    Min size: `1 byte`
                    Max size: `5 megabytes`
              required:
                - request
                - file
servers:
  - url: https://api.cash.app/network/v1
  - url: https://sandbox.api.cash.app/network/v1
components:
  schemas:
    IdempotencyKey:
      type: string
      description: >-
        A unique identifier which can be used by Cash App to de-duplicate
        retries of this request, making it idempotent. Learn more about
        idempotency in the API.
      title: IdempotencyKey
    DisputesDisputeIdEvidenceFilePostRequestBodyContentMultipartFormDataSchemaRequestEvidenceCategory:
      type: string
      enum:
        - GENERIC_EVIDENCE
        - ONLINE_OR_APP_ACCESS_LOG
        - AUTHORIZATION_DOCUMENTATION
        - CANCELLATION_OR_REFUND_DOCUMENTATION
        - CARDHOLDER_COMMUNICATION
        - CARDHOLDER_INFORMATION
        - PURCHASE_ACKNOWLEDGEMENT
        - DUPLICATE_CHARGE_DOCUMENTATION
        - PRODUCT_OR_SERVICE_DESCRIPTION
        - RECEIPT
        - SERVICE_RECEIVED_DOCUMENTATION
        - PROOF_OF_DELIVERY_DOCUMENTATION
        - RELATED_TRANSACTION_DOCUMENTATION
        - REBUTTAL_EXPLANATION
        - TRACKING_NUMBER
      description: >-
        Describes what type of information is contained in this piece of
        evidence.


        Current values:


        - `GENERIC_EVIDENCE`: Default evidence type used if no other category
        applies.

        - `ONLINE_OR_APP_ACCESS_LOG`: Server or activity logs that show proof of
        the cardholder’s identity and that the cardholder successfully ordered
        and received the goods (digitally or otherwise). Example evidence
        includes IP addresses, corresponding timestamps/dates, cardholder’s name
        and email address linked to a cardholder profile held by the seller,
        proof the same device and card (used in dispute) were previously used in
        prior undisputed transaction, and any related detailed activity.

        - `AUTHORIZATION_DOCUMENTATION`: **[File Only]** Evidence that the
        cardholder did provide authorization for the charge. Example evidence
        includes a signed credit card authorization.

        - `CANCELLATION_OR_REFUND_DOCUMENTATION`: Evidence that the cardholder
        acknowledged your refund or cancellation policy. Example evidence
        includes a signature or checkbox showing the cardholder’s
        acknowledgement of your refund or cancellation policy.

        - `CARDHOLDER_COMMUNICATION`: **[File Only]** Evidence that shows
        relevant communication with the cardholder. Example evidence includes
        emails or texts that show the cardholder received goods/services or
        demonstrate cardholder satisfaction.

        - `CARDHOLDER_INFORMATION`: Evidence that validates the customer's
        identity. Example evidence includes personally identifiable details such
        as name, email address, purchaser IP address, and a copy of the
        cardholder ID.

        - `PURCHASE_ACKNOWLEDGEMENT`: Evidence that shows proof of the
        sale/transaction. Example evidence includes an invoice, contract, or
        other item showing the customer’s acknowledgement of the purchase and
        your terms.

        - `DUPLICATE_CHARGE_DOCUMENTATION`: **[File Only]** Evidence that shows
        the charges in question are valid and distinct from one another. Example
        evidence includes receipts, shipping labels, and invoices along with
        their distinct payment IDs.

        - `PRODUCT_OR_SERVICE_DESCRIPTION`: A description of the product or
        service sold.

        - `RECEIPT`: A receipt or message sent to the cardholder detailing the
        charge. Note: You do not need to upload the Square receipt; Square
        submits the receipt on your behalf.

        - `SERVICE_RECEIVED_DOCUMENTATION`: Evidence that the service was
        provided to the cardholder or the expected date that services will be
        rendered. Example evidence includes a signed delivery form, work order,
        expected delivery date, or other written agreements.

        - `PROOF_OF_DELIVERY_DOCUMENTATION`: Evidence that shows the product was
        provided to the cardholder or the expected date of delivery. Example
        evidence includes a signed delivery form or written agreement
        acknowledging receipt of the goods or services.

        - `RELATED_TRANSACTION_DOCUMENTATION`: Evidence that shows the
        cardholder previously processed transactions on the same card and did
        not dispute them.

        - `REBUTTAL_EXPLANATION`: An explanation of why the cardholder’s claim
        is invalid. Example evidence includes an explanation of why each
        distinct charge is a legitimate purchase, why the cardholder’s claim for
        credit owed due to their attempt to cancel, return, or refund is invalid
        per your stated policy and cardholder agreement, or an explanation of
        how the cardholder did not attempt to remedy the issue with you first to
        receive credit.

        - `TRACKING_NUMBER`: The tracking number for the order provided by the
        shipping carrier. If you have multiple numbers, they need to be
        submitted individually as separate pieces of evidence.
      title: >-
        DisputesDisputeIdEvidenceFilePostRequestBodyContentMultipartFormDataSchemaRequestEvidenceCategory
    DisputesDisputeIdEvidenceFilePostRequestBodyContentMultipartFormDataSchemaRequestEvidenceFileContentType:
      type: string
      enum:
        - application/pdf
        - image/png
        - image/jpeg
        - image/heic
        - image/heif
        - image/tiff
      description: |-
        The MIME type of the uploaded file.

        Current values:

        - `application/pdf`
        - `image/heic`
        - `image/heif`
        - `image/jpeg`
        - `image/png`
        - `image/tiff`
      title: >-
        DisputesDisputeIdEvidenceFilePostRequestBodyContentMultipartFormDataSchemaRequestEvidenceFileContentType
    DisputesDisputeIdEvidenceFilePostRequestBodyContentMultipartFormDataSchemaRequestEvidenceFile:
      type: object
      properties:
        filename:
          type: string
          description: >-
            Name of the uploaded file. It should be descriptive enough to
            indicate what type of information is contained in the uploaded file.
        content_type:
          $ref: >-
            #/components/schemas/DisputesDisputeIdEvidenceFilePostRequestBodyContentMultipartFormDataSchemaRequestEvidenceFileContentType
          description: |-
            The MIME type of the uploaded file.

            Current values:

            - `application/pdf`
            - `image/heic`
            - `image/heif`
            - `image/jpeg`
            - `image/png`
            - `image/tiff`
      required:
        - filename
        - content_type
      description: Metadata about the uploaded file.
      title: >-
        DisputesDisputeIdEvidenceFilePostRequestBodyContentMultipartFormDataSchemaRequestEvidenceFile
    Metadata:
      type: object
      additionalProperties:
        type: string
      description: >-
        Freeform key-value pairs of arbitrary data associated with this
        resource.


        Keys and values must be passed as strings and not contain any personally
        identifiable information (PII).


        Min keys: `0`

        Max keys: `50`



        > Note: Nested keys are not supported.
      title: Metadata
    DisputesDisputeIdEvidenceFilePostRequestBodyContentMultipartFormDataSchemaRequestEvidence:
      type: object
      properties:
        category:
          $ref: >-
            #/components/schemas/DisputesDisputeIdEvidenceFilePostRequestBodyContentMultipartFormDataSchemaRequestEvidenceCategory
          description: >-
            Describes what type of information is contained in this piece of
            evidence.


            Current values:


            - `GENERIC_EVIDENCE`: Default evidence type used if no other
            category applies.

            - `ONLINE_OR_APP_ACCESS_LOG`: Server or activity logs that show
            proof of the cardholder’s identity and that the cardholder
            successfully ordered and received the goods (digitally or
            otherwise). Example evidence includes IP addresses, corresponding
            timestamps/dates, cardholder’s name and email address linked to a
            cardholder profile held by the seller, proof the same device and
            card (used in dispute) were previously used in prior undisputed
            transaction, and any related detailed activity.

            - `AUTHORIZATION_DOCUMENTATION`: **[File Only]** Evidence that the
            cardholder did provide authorization for the charge. Example
            evidence includes a signed credit card authorization.

            - `CANCELLATION_OR_REFUND_DOCUMENTATION`: Evidence that the
            cardholder acknowledged your refund or cancellation policy. Example
            evidence includes a signature or checkbox showing the cardholder’s
            acknowledgement of your refund or cancellation policy.

            - `CARDHOLDER_COMMUNICATION`: **[File Only]** Evidence that shows
            relevant communication with the cardholder. Example evidence
            includes emails or texts that show the cardholder received
            goods/services or demonstrate cardholder satisfaction.

            - `CARDHOLDER_INFORMATION`: Evidence that validates the customer's
            identity. Example evidence includes personally identifiable details
            such as name, email address, purchaser IP address, and a copy of the
            cardholder ID.

            - `PURCHASE_ACKNOWLEDGEMENT`: Evidence that shows proof of the
            sale/transaction. Example evidence includes an invoice, contract, or
            other item showing the customer’s acknowledgement of the purchase
            and your terms.

            - `DUPLICATE_CHARGE_DOCUMENTATION`: **[File Only]** Evidence that
            shows the charges in question are valid and distinct from one
            another. Example evidence includes receipts, shipping labels, and
            invoices along with their distinct payment IDs.

            - `PRODUCT_OR_SERVICE_DESCRIPTION`: A description of the product or
            service sold.

            - `RECEIPT`: A receipt or message sent to the cardholder detailing
            the charge. Note: You do not need to upload the Square receipt;
            Square submits the receipt on your behalf.

            - `SERVICE_RECEIVED_DOCUMENTATION`: Evidence that the service was
            provided to the cardholder or the expected date that services will
            be rendered. Example evidence includes a signed delivery form, work
            order, expected delivery date, or other written agreements.

            - `PROOF_OF_DELIVERY_DOCUMENTATION`: Evidence that shows the product
            was provided to the cardholder or the expected date of delivery.
            Example evidence includes a signed delivery form or written
            agreement acknowledging receipt of the goods or services.

            - `RELATED_TRANSACTION_DOCUMENTATION`: Evidence that shows the
            cardholder previously processed transactions on the same card and
            did not dispute them.

            - `REBUTTAL_EXPLANATION`: An explanation of why the cardholder’s
            claim is invalid. Example evidence includes an explanation of why
            each distinct charge is a legitimate purchase, why the cardholder’s
            claim for credit owed due to their attempt to cancel, return, or
            refund is invalid per your stated policy and cardholder agreement,
            or an explanation of how the cardholder did not attempt to remedy
            the issue with you first to receive credit.

            - `TRACKING_NUMBER`: The tracking number for the order provided by
            the shipping carrier. If you have multiple numbers, they need to be
            submitted individually as separate pieces of evidence.
        file:
          $ref: >-
            #/components/schemas/DisputesDisputeIdEvidenceFilePostRequestBodyContentMultipartFormDataSchemaRequestEvidenceFile
          description: Metadata about the uploaded file.
        metadata:
          $ref: '#/components/schemas/Metadata'
      required:
        - category
        - file
      description: Details about the evidence to create.
      title: >-
        DisputesDisputeIdEvidenceFilePostRequestBodyContentMultipartFormDataSchemaRequestEvidence
    DisputesDisputeIdEvidenceFilePostRequestBodyContentMultipartFormDataSchemaRequest:
      type: object
      properties:
        idempotency_key:
          $ref: '#/components/schemas/IdempotencyKey'
        evidence:
          $ref: >-
            #/components/schemas/DisputesDisputeIdEvidenceFilePostRequestBodyContentMultipartFormDataSchemaRequestEvidence
          description: Details about the evidence to create.
      description: JSON-encoded payload describing the contents of the file uploaded
      title: >-
        DisputesDisputeIdEvidenceFilePostRequestBodyContentMultipartFormDataSchemaRequest
    DisputeEvidenceCategory:
      type: string
      enum:
        - GENERIC_EVIDENCE
        - ONLINE_OR_APP_ACCESS_LOG
        - AUTHORIZATION_DOCUMENTATION
        - CANCELLATION_OR_REFUND_DOCUMENTATION
        - CARDHOLDER_COMMUNICATION
        - CARDHOLDER_INFORMATION
        - PURCHASE_ACKNOWLEDGEMENT
        - DUPLICATE_CHARGE_DOCUMENTATION
        - PRODUCT_OR_SERVICE_DESCRIPTION
        - RECEIPT
        - SERVICE_RECEIVED_DOCUMENTATION
        - PROOF_OF_DELIVERY_DOCUMENTATION
        - RELATED_TRANSACTION_DOCUMENTATION
        - REBUTTAL_EXPLANATION
        - TRACKING_NUMBER
      description: >-
        Describes what type of information is contained in this piece of
        evidence.


        Current values:


        - `GENERIC_EVIDENCE`: Default evidence type used if no other category
        applies.

        - `ONLINE_OR_APP_ACCESS_LOG`: Server or activity logs that show proof of
        the cardholder’s identity and that the cardholder successfully ordered
        and received the goods (digitally or otherwise). Example evidence
        includes IP addresses, corresponding timestamps/dates, cardholder’s name
        and email address linked to a cardholder profile held by the seller,
        proof the same device and card (used in dispute) were previously used in
        prior undisputed transaction, and any related detailed activity.

        - `AUTHORIZATION_DOCUMENTATION`: **[File Only]** Evidence that the
        cardholder did provide authorization for the charge. Example evidence
        includes a signed credit card authorization.

        - `CANCELLATION_OR_REFUND_DOCUMENTATION`: Evidence that the cardholder
        acknowledged your refund or cancellation policy. Example evidence
        includes a signature or checkbox showing the cardholder’s
        acknowledgement of your refund or cancellation policy.

        - `CARDHOLDER_COMMUNICATION`: **[File Only]** Evidence that shows
        relevant communication with the cardholder. Example evidence includes
        emails or texts that show the cardholder received goods/services or
        demonstrate cardholder satisfaction.

        - `CARDHOLDER_INFORMATION`: Evidence that validates the customer's
        identity. Example evidence includes personally identifiable details such
        as name, email address, purchaser IP address, and a copy of the
        cardholder ID.

        - `PURCHASE_ACKNOWLEDGEMENT`: Evidence that shows proof of the
        sale/transaction. Example evidence includes an invoice, contract, or
        other item showing the customer’s acknowledgement of the purchase and
        your terms.

        - `DUPLICATE_CHARGE_DOCUMENTATION`: **[File Only]** Evidence that shows
        the charges in question are valid and distinct from one another. Example
        evidence includes receipts, shipping labels, and invoices along with
        their distinct payment IDs.

        - `PRODUCT_OR_SERVICE_DESCRIPTION`: A description of the product or
        service sold.

        - `RECEIPT`: A receipt or message sent to the cardholder detailing the
        charge. Note: You do not need to upload the Square receipt; Square
        submits the receipt on your behalf.

        - `SERVICE_RECEIVED_DOCUMENTATION`: Evidence that the service was
        provided to the cardholder or the expected date that services will be
        rendered. Example evidence includes a signed delivery form, work order,
        expected delivery date, or other written agreements.

        - `PROOF_OF_DELIVERY_DOCUMENTATION`: Evidence that shows the product was
        provided to the cardholder or the expected date of delivery. Example
        evidence includes a signed delivery form or written agreement
        acknowledging receipt of the goods or services.

        - `RELATED_TRANSACTION_DOCUMENTATION`: Evidence that shows the
        cardholder previously processed transactions on the same card and did
        not dispute them.

        - `REBUTTAL_EXPLANATION`: An explanation of why the cardholder’s claim
        is invalid. Example evidence includes an explanation of why each
        distinct charge is a legitimate purchase, why the cardholder’s claim for
        credit owed due to their attempt to cancel, return, or refund is invalid
        per your stated policy and cardholder agreement, or an explanation of
        how the cardholder did not attempt to remedy the issue with you first to
        receive credit.

        - `TRACKING_NUMBER`: The tracking number for the order provided by the
        shipping carrier. If you have multiple numbers, they need to be
        submitted individually as separate pieces of evidence.
      title: DisputeEvidenceCategory
    DisputeEvidenceFileContentType:
      type: string
      enum:
        - application/pdf
        - image/heic
        - image/heif
        - image/jpeg
        - image/png
        - image/tiff
      description: |-
        The MIME type of the uploaded file.

        Current values:

        - `application/pdf`
        - `image/heic`
        - `image/heif`
        - `image/jpeg`
        - `image/png`
        - `image/tiff`
      title: DisputeEvidenceFileContentType
    DisputeEvidenceFile:
      type: object
      properties:
        filename:
          type: string
          description: >-
            Name of the uploaded file. It should be descriptive enough to
            indicate what type of information is contained in the uploaded file.
        content_type:
          $ref: '#/components/schemas/DisputeEvidenceFileContentType'
          description: |-
            The MIME type of the uploaded file.

            Current values:

            - `application/pdf`
            - `image/heic`
            - `image/heif`
            - `image/jpeg`
            - `image/png`
            - `image/tiff`
      required:
        - filename
        - content_type
      description: >-
        If the evidence is of type `FILE`, contains metadata about the binary
        file uploaded as evidence.
      title: DisputeEvidenceFile
    DisputeEvidenceType:
      type: string
      enum:
        - FILE
        - TEXT
      description: |-
        Indicates if the evidence is a file or plain text.

        Current values:
        - `TEXT`: The evidence is a blob of text under 500 characters.
        - `FILE`: The evidence is an uploaded binary file.
      title: DisputeEvidenceType
    DisputeEvidence:
      type: object
      properties:
        id:
          type: string
          description: |-
            A unique identifier for the dispute evidence issued by Cash App.

            Min length: `1`
            Max length: `128`
        dispute_id:
          type: string
          description: |-
            ID of the dispute this evidence is associated with.

            Min length: `1`
            Max length: `128`
        category:
          $ref: '#/components/schemas/DisputeEvidenceCategory'
          description: >-
            Describes what type of information is contained in this piece of
            evidence.


            Current values:


            - `GENERIC_EVIDENCE`: Default evidence type used if no other
            category applies.

            - `ONLINE_OR_APP_ACCESS_LOG`: Server or activity logs that show
            proof of the cardholder’s identity and that the cardholder
            successfully ordered and received the goods (digitally or
            otherwise). Example evidence includes IP addresses, corresponding
            timestamps/dates, cardholder’s name and email address linked to a
            cardholder profile held by the seller, proof the same device and
            card (used in dispute) were previously used in prior undisputed
            transaction, and any related detailed activity.

            - `AUTHORIZATION_DOCUMENTATION`: **[File Only]** Evidence that the
            cardholder did provide authorization for the charge. Example
            evidence includes a signed credit card authorization.

            - `CANCELLATION_OR_REFUND_DOCUMENTATION`: Evidence that the
            cardholder acknowledged your refund or cancellation policy. Example
            evidence includes a signature or checkbox showing the cardholder’s
            acknowledgement of your refund or cancellation policy.

            - `CARDHOLDER_COMMUNICATION`: **[File Only]** Evidence that shows
            relevant communication with the cardholder. Example evidence
            includes emails or texts that show the cardholder received
            goods/services or demonstrate cardholder satisfaction.

            - `CARDHOLDER_INFORMATION`: Evidence that validates the customer's
            identity. Example evidence includes personally identifiable details
            such as name, email address, purchaser IP address, and a copy of the
            cardholder ID.

            - `PURCHASE_ACKNOWLEDGEMENT`: Evidence that shows proof of the
            sale/transaction. Example evidence includes an invoice, contract, or
            other item showing the customer’s acknowledgement of the purchase
            and your terms.

            - `DUPLICATE_CHARGE_DOCUMENTATION`: **[File Only]** Evidence that
            shows the charges in question are valid and distinct from one
            another. Example evidence includes receipts, shipping labels, and
            invoices along with their distinct payment IDs.

            - `PRODUCT_OR_SERVICE_DESCRIPTION`: A description of the product or
            service sold.

            - `RECEIPT`: A receipt or message sent to the cardholder detailing
            the charge. Note: You do not need to upload the Square receipt;
            Square submits the receipt on your behalf.

            - `SERVICE_RECEIVED_DOCUMENTATION`: Evidence that the service was
            provided to the cardholder or the expected date that services will
            be rendered. Example evidence includes a signed delivery form, work
            order, expected delivery date, or other written agreements.

            - `PROOF_OF_DELIVERY_DOCUMENTATION`: Evidence that shows the product
            was provided to the cardholder or the expected date of delivery.
            Example evidence includes a signed delivery form or written
            agreement acknowledging receipt of the goods or services.

            - `RELATED_TRANSACTION_DOCUMENTATION`: Evidence that shows the
            cardholder previously processed transactions on the same card and
            did not dispute them.

            - `REBUTTAL_EXPLANATION`: An explanation of why the cardholder’s
            claim is invalid. Example evidence includes an explanation of why
            each distinct charge is a legitimate purchase, why the cardholder’s
            claim for credit owed due to their attempt to cancel, return, or
            refund is invalid per your stated policy and cardholder agreement,
            or an explanation of how the cardholder did not attempt to remedy
            the issue with you first to receive credit.

            - `TRACKING_NUMBER`: The tracking number for the order provided by
            the shipping carrier. If you have multiple numbers, they need to be
            submitted individually as separate pieces of evidence.
        file:
          $ref: '#/components/schemas/DisputeEvidenceFile'
          description: >-
            If the evidence is of type `FILE`, contains metadata about the
            binary file uploaded as evidence.
        text:
          type: string
          description: >-
            If the evidence is of type `TEXT`, contains the blob of text created
            as evidence.


            Min length: `1`

            Max length: `500`
        type:
          $ref: '#/components/schemas/DisputeEvidenceType'
          description: |-
            Indicates if the evidence is a file or plain text.

            Current values:
            - `TEXT`: The evidence is a blob of text under 500 characters.
            - `FILE`: The evidence is an uploaded binary file.
        created_at:
          type: string
          format: date-time
          description: >-
            When this evidence was created, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        metadata:
          $ref: '#/components/schemas/Metadata'
      required:
        - id
        - dispute_id
        - category
        - type
        - created_at
      title: DisputeEvidence
    Disputes_create-dispute-evidence-file_Response_201:
      type: object
      properties:
        evidence:
          $ref: '#/components/schemas/DisputeEvidence'
      required:
        - evidence
      title: Disputes_create-dispute-evidence-file_Response_201
    ErrorCategory:
      type: string
      enum:
        - API_ERROR
        - AUTHENTICATION_ERROR
        - BRAND_ERROR
        - DISPUTE_ERROR
        - MERCHANT_ERROR
        - INVALID_REQUEST_ERROR
        - PAYMENT_PROCESSING_ERROR
        - RATE_LIMIT_ERROR
        - WEBHOOK_ERROR
        - API_KEY_ERROR
        - GRANT_ERROR
      description: The high-level reason the error occurred
      title: ErrorCategory
    Error:
      type: object
      properties:
        category:
          $ref: '#/components/schemas/ErrorCategory'
          description: The high-level reason the error occurred
        code:
          type: string
          description: >-
            A unique identifier for the specific type of error that occurred.
            See the Error Code Reference for more information.


            Min length: `1`
        detail:
          type: string
          description: >-
            Human-readable description of why the error occurred and how to
            resolve it.


            Min length: `1`
        field:
          type: string
          description: >-
            The field in the request that caused the error, using array and
            object dot notation.


            Min length: `1`
      required:
        - category
        - code
      description: Represents an error encountered during a request to the API.
      title: Error
    ErrorResponse:
      type: object
      properties:
        errors:
          type: array
          items:
            $ref: '#/components/schemas/Error'
          description: |-
            A list of errors that occurred while processing the request.

            Min number of items: `1`
      required:
        - errors
      title: ErrorResponse

```

## SDK Code Examples

```python
import requests

url = "https://api.cash.app/network/v1/disputes/dispute_id/evidence-file"

files = { "file": "open('string', 'rb')" }
payload = { "request": "{
  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",
  \"evidence\": {
    \"category\": \"GENERIC_EVIDENCE\",
    \"file\": {
      \"filename\": \"filename\",
      \"content_type\": \"application/pdf\"
    }
  }
}" }
headers = {
    "Accept": "Accept",
    "X-Region": "X-Region",
    "X-Signature": "X-Signature",
    "User-Agent": "User-Agent"
}

response = requests.post(url, data=payload, files=files, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.cash.app/network/v1/disputes/dispute_id/evidence-file';
const form = new FormData();
form.append('request', '{
  "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
  "evidence": {
    "category": "GENERIC_EVIDENCE",
    "file": {
      "filename": "filename",
      "content_type": "application/pdf"
    }
  }
}');
form.append('file', 'string');

const options = {
  method: 'POST',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent'
  }
};

options.body = form;

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.cash.app/network/v1/disputes/dispute_id/evidence-file"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"request\"\r\n\r\n{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"evidence\": {\n    \"category\": \"GENERIC_EVIDENCE\",\n    \"file\": {\n      \"filename\": \"filename\",\n      \"content_type\": \"application/pdf\"\n    }\n  }\n}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Accept", "Accept")
	req.Header.Add("X-Region", "X-Region")
	req.Header.Add("X-Signature", "X-Signature")
	req.Header.Add("User-Agent", "User-Agent")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cash.app/network/v1/disputes/dispute_id/evidence-file")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"request\"\r\n\r\n{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"evidence\": {\n    \"category\": \"GENERIC_EVIDENCE\",\n    \"file\": {\n      \"filename\": \"filename\",\n      \"content_type\": \"application/pdf\"\n    }\n  }\n}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.cash.app/network/v1/disputes/dispute_id/evidence-file")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"request\"\r\n\r\n{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"evidence\": {\n    \"category\": \"GENERIC_EVIDENCE\",\n    \"file\": {\n      \"filename\": \"filename\",\n      \"content_type\": \"application/pdf\"\n    }\n  }\n}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cash.app/network/v1/disputes/dispute_id/evidence-file', [
  'multipart' => [
    [
        'name' => 'request',
        'contents' => '{
  "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
  "evidence": {
    "category": "GENERIC_EVIDENCE",
    "file": {
      "filename": "filename",
      "content_type": "application/pdf"
    }
  }
}'
    ],
    [
        'name' => 'file',
        'filename' => 'string',
        'contents' => null
    ]
  ]
  'headers' => [
    'Accept' => 'Accept',
    'User-Agent' => 'User-Agent',
    'X-Region' => 'X-Region',
    'X-Signature' => 'X-Signature',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.cash.app/network/v1/disputes/dispute_id/evidence-file");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
request.AddParameter("undefined", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"request\"\r\n\r\n{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"evidence\": {\n    \"category\": \"GENERIC_EVIDENCE\",\n    \"file\": {\n      \"filename\": \"filename\",\n      \"content_type\": \"application/pdf\"\n    }\n  }\n}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Accept": "Accept",
  "X-Region": "X-Region",
  "X-Signature": "X-Signature",
  "User-Agent": "User-Agent"
]
let parameters = [
  [
    "name": "request",
    "value": "{
  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",
  \"evidence\": {
    \"category\": \"GENERIC_EVIDENCE\",
    \"file\": {
      \"filename\": \"filename\",
      \"content_type\": \"application/pdf\"
    }
  }
}"
  ],
  [
    "name": "file",
    "fileName": "string"
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/network/v1/disputes/dispute_id/evidence-file")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

```python
import requests

url = "https://api.cash.app/network/v1/disputes/dispute_id/evidence-file"

files = { "file": "open('string', 'rb')" }
payload = { "request": "{
  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",
  \"evidence\": {
    \"category\": \"GENERIC_EVIDENCE\",
    \"file\": {
      \"filename\": \"filename\",
      \"content_type\": \"application/pdf\"
    },
    \"metadata\": {
      \"key\": \"value\"
    }
  }
}" }
headers = {
    "Accept": "Accept",
    "X-Region": "X-Region",
    "X-Signature": "X-Signature",
    "User-Agent": "User-Agent"
}

response = requests.post(url, data=payload, files=files, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.cash.app/network/v1/disputes/dispute_id/evidence-file';
const form = new FormData();
form.append('request', '{
  "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
  "evidence": {
    "category": "GENERIC_EVIDENCE",
    "file": {
      "filename": "filename",
      "content_type": "application/pdf"
    },
    "metadata": {
      "key": "value"
    }
  }
}');
form.append('file', 'string');

const options = {
  method: 'POST',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent'
  }
};

options.body = form;

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.cash.app/network/v1/disputes/dispute_id/evidence-file"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"request\"\r\n\r\n{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"evidence\": {\n    \"category\": \"GENERIC_EVIDENCE\",\n    \"file\": {\n      \"filename\": \"filename\",\n      \"content_type\": \"application/pdf\"\n    },\n    \"metadata\": {\n      \"key\": \"value\"\n    }\n  }\n}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Accept", "Accept")
	req.Header.Add("X-Region", "X-Region")
	req.Header.Add("X-Signature", "X-Signature")
	req.Header.Add("User-Agent", "User-Agent")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cash.app/network/v1/disputes/dispute_id/evidence-file")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"request\"\r\n\r\n{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"evidence\": {\n    \"category\": \"GENERIC_EVIDENCE\",\n    \"file\": {\n      \"filename\": \"filename\",\n      \"content_type\": \"application/pdf\"\n    },\n    \"metadata\": {\n      \"key\": \"value\"\n    }\n  }\n}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.cash.app/network/v1/disputes/dispute_id/evidence-file")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"request\"\r\n\r\n{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"evidence\": {\n    \"category\": \"GENERIC_EVIDENCE\",\n    \"file\": {\n      \"filename\": \"filename\",\n      \"content_type\": \"application/pdf\"\n    },\n    \"metadata\": {\n      \"key\": \"value\"\n    }\n  }\n}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cash.app/network/v1/disputes/dispute_id/evidence-file', [
  'multipart' => [
    [
        'name' => 'request',
        'contents' => '{
  "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
  "evidence": {
    "category": "GENERIC_EVIDENCE",
    "file": {
      "filename": "filename",
      "content_type": "application/pdf"
    },
    "metadata": {
      "key": "value"
    }
  }
}'
    ],
    [
        'name' => 'file',
        'filename' => 'string',
        'contents' => null
    ]
  ]
  'headers' => [
    'Accept' => 'Accept',
    'User-Agent' => 'User-Agent',
    'X-Region' => 'X-Region',
    'X-Signature' => 'X-Signature',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.cash.app/network/v1/disputes/dispute_id/evidence-file");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
request.AddParameter("undefined", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"request\"\r\n\r\n{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"evidence\": {\n    \"category\": \"GENERIC_EVIDENCE\",\n    \"file\": {\n      \"filename\": \"filename\",\n      \"content_type\": \"application/pdf\"\n    },\n    \"metadata\": {\n      \"key\": \"value\"\n    }\n  }\n}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Accept": "Accept",
  "X-Region": "X-Region",
  "X-Signature": "X-Signature",
  "User-Agent": "User-Agent"
]
let parameters = [
  [
    "name": "request",
    "value": "{
  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",
  \"evidence\": {
    \"category\": \"GENERIC_EVIDENCE\",
    \"file\": {
      \"filename\": \"filename\",
      \"content_type\": \"application/pdf\"
    },
    \"metadata\": {
      \"key\": \"value\"
    }
  }
}"
  ],
  [
    "name": "file",
    "fileName": "string"
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/network/v1/disputes/dispute_id/evidence-file")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```