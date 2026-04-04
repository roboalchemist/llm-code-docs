# Source: https://io.net/docs/reference/vmaas/destroy-deployment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> Terminate and remove an existing deployment. All VMs and resources allocated to the deployment will be released.

# Destroy Deployment

<Note>
  When deleting a deployment, charges are handled as follows;

  * The first hour is **ALWAYS non-refundable**.
  * After the first hour, charges are calculated **to the exact duration** the cluster was active (not rounded to whole hours).
  * Any unused prepaid time is **refunded proportionally**.

  Example: If you pre-paid for 3 hours and delete the deployment after 1.2 hours, you are charged for 1.2 hours and refunded the remaining 1.8 hours.
</Note>


## OpenAPI

````yaml openapi/vmaas/destroy-deployment.json delete /enterprise/v1/io-cloud/vmaas/deployment/{deployment_id}
openapi: 3.1.0
info:
  title: IO API
  version: '1.0'
servers:
  - url: https://api.io.solutions/
security: []
paths:
  /enterprise/v1/io-cloud/vmaas/deployment/{deployment_id}:
    delete:
      tags:
        - io-cloud-vmaas
      summary: Destroy Deployment
      operationId: destroy_deployment_v1_io_cloud_vmaas_deployment__deployment_id__delete
      parameters:
        - name: deployment_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Deployment Id
        - name: token
          in: header
          required: false
          schema:
            type: string
            title: Token
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '404':
          description: Not found
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````