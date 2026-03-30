# Source: https://developers.webflow.com/data/reference/webhooks/events/form-submission.mdx

# Form Submission

POST 

Information about a form that was subitted

Reference: https://developers.webflow.com/data/reference/webhooks/events/form-submission

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  form-submission:
    post:
      operationId: form-submission
      summary: Form Submission
      description: Information about a form that was subitted
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                triggerType:
                  type: string
                  description: The type of event that triggered the request
                payload:
                  $ref: >-
                    #/components/schemas/WebhooksFormSubmissionPayloadContentApplicationJsonSchemaPayload
                  description: The payload of data sent from Webflow
components:
  schemas:
    WebhooksFormSubmissionPayloadContentApplicationJsonSchemaPayloadData:
      type: object
      properties: {}
      description: The data submitted in the form
      title: WebhooksFormSubmissionPayloadContentApplicationJsonSchemaPayloadData
    WebhooksFormSubmissionPayloadContentApplicationJsonSchemaPayloadSchemaItemsFieldType:
      type: string
      enum:
        - FormTextInput
        - FormTextarea
        - FormCheckboxInput
        - FormRadioInput
        - FormFileUploadInput
      description: Form field type
      title: >-
        WebhooksFormSubmissionPayloadContentApplicationJsonSchemaPayloadSchemaItemsFieldType
    WebhooksFormSubmissionPayloadContentApplicationJsonSchemaPayloadSchemaItems:
      type: object
      properties:
        fieldName:
          type: string
          description: Form field name
        fieldType:
          $ref: >-
            #/components/schemas/WebhooksFormSubmissionPayloadContentApplicationJsonSchemaPayloadSchemaItemsFieldType
          description: Form field type
        fieldElementId:
          type: string
          format: UUID
          description: Element ID of the Form Field
      title: >-
        WebhooksFormSubmissionPayloadContentApplicationJsonSchemaPayloadSchemaItems
    WebhooksFormSubmissionPayloadContentApplicationJsonSchemaPayload:
      type: object
      properties:
        name:
          type: string
          description: The name of the form
        siteId:
          type: string
          format: objectid
          description: The ID of the site that the form was submitted from
        data:
          $ref: >-
            #/components/schemas/WebhooksFormSubmissionPayloadContentApplicationJsonSchemaPayloadData
          description: The data submitted in the form
        schema:
          type: array
          items:
            $ref: >-
              #/components/schemas/WebhooksFormSubmissionPayloadContentApplicationJsonSchemaPayloadSchemaItems
          description: A list of fields from the submitted form
        submittedAt:
          type: string
          description: The timestamp the form was submitted
        id:
          type: string
          description: the ID of the event
        formId:
          type: string
          format: objectid
          description: The ID of the form submission
        formElementId:
          type:
            - string
            - 'null'
          description: The uniqueID of the Form element
      description: The payload of data sent from Webflow
      title: WebhooksFormSubmissionPayloadContentApplicationJsonSchemaPayload

```