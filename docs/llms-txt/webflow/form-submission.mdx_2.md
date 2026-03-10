# Source: https://developers.webflow.com/data/v1.0.0/reference/sites/sites/form-submission.mdx

# Form Submission

POST 

Reference: https://developers.webflow.com/data/v1.0.0/reference/sites/sites/form-submission

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
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        description: The form data submitted
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FormSubmission'
components:
  schemas:
    FormSubmissionData:
      type: object
      properties: {}
      description: The data submitted in the form
      title: FormSubmissionData
    FormSubmission:
      type: object
      properties:
        name:
          type: string
          description: The name of the form
        site:
          type: string
          format: uuid
          description: The ID of the site that the form was submitted from
        data:
          $ref: '#/components/schemas/FormSubmissionData'
          description: The data submitted in the form
        d:
          type: string
          description: The timestamp the form was submitted
        _id:
          type: string
          format: uuid
          description: The ID of the form submission
      title: FormSubmission

```