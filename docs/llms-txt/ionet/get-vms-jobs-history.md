# Source: https://io.net/docs/reference/vmaas/get-vms-jobs-history.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a VM's Jobs History

> Retrieve the job execution history for a specific VM or container within a deployment. Includes logs and status of completed or active jobs.



## OpenAPI

````yaml openapi/vmaas/get-vms-jobs-history.json get /enterprise/v1/io-cloud/vmaas/deployment/{deployment_id}/vms-jobs/{container_id}
openapi: 3.1.0
info:
  title: IO API
  version: '1.0'
servers:
  - url: https://api.io.solutions/
security: []
paths:
  /enterprise/v1/io-cloud/vmaas/deployment/{deployment_id}/vms-jobs/{container_id}:
    get:
      tags:
        - enterprise-io-cloud-vmaas
      summary: Get Vms Jobs History
      operationId: >-
        get_vms_jobs_history_enterprise_v1_io_cloud_vmaas_deployment__deployment_id__vms_jobs__container_id__get
      parameters:
        - name: deployment_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Deployment Id
        - name: container_id
          in: path
          required: true
          schema:
            type: string
            title: Container Id
        - name: page
          in: query
          required: false
          schema:
            type: integer
            minimum: 1
            default: 1
            title: Page
        - name: page_size
          in: query
          required: false
          schema:
            type: integer
            maximum: 100
            minimum: 1
            default: 20
            title: Page Size
        - name: x-api-key
          in: header
          required: false
          schema:
            type: string
            description: io.net provided API Key
            title: X-Api-Key
          description: io.net provided API Key
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetVmJobData'
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
    GetVmJobData:
      properties:
        data:
          $ref: '#/components/schemas/VmJobsData-Output'
      type: object
      required:
        - data
      title: GetVmJobData
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    VmJobsData-Output:
      properties:
        total:
          type: integer
          title: Total
        workers:
          items:
            $ref: >-
              #/components/schemas/io_cloud__schemas__response__enterprise__vmaas__WorkerData-Output
          type: array
          title: Workers
      type: object
      required:
        - total
        - workers
      title: VmJobsData
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
    io_cloud__schemas__response__enterprise__vmaas__WorkerData-Output:
      properties:
        device_id:
          type: string
          format: uuid
          title: Device Id
        vm_id:
          type: string
          title: Vm Id
        hardware:
          type: string
          title: Hardware
        brand_name:
          type: string
          title: Brand Name
        created_at:
          type: string
          format: date-time
          title: Created At
        uptime_percent:
          type: number
          title: Uptime Percent
        gpus_per_vm:
          type: integer
          title: Gpus Per Vm
        status:
          type: string
          title: Status
        vm_events:
          anyOf:
            - items:
                $ref: '#/components/schemas/VmEvent'
              type: array
            - type: 'null'
          title: Vm Events
        network_services:
          additionalProperties:
            $ref: '#/components/schemas/NetworkServiceResponse'
          type: object
          title: Network Services
        ssh_access:
          type: string
          title: Ssh Access
        is_external:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is External
          default: false
      type: object
      required:
        - device_id
        - vm_id
        - hardware
        - brand_name
        - created_at
        - uptime_percent
        - gpus_per_vm
        - status
        - vm_events
        - network_services
        - ssh_access
      title: WorkerData
    VmEvent:
      properties:
        time:
          type: string
          format: date-time
          title: Time
        message:
          type: string
          title: Message
      type: object
      required:
        - time
        - message
      title: VmEvent
    NetworkServiceResponse:
      properties:
        port:
          type: integer
          title: Port
        protocol:
          $ref: >-
            #/components/schemas/io_cloud__schemas__response__enterprise__vmaas__NetworkProtocol
        whitelist:
          items:
            type: string
            format: ipvanynetwork
          type: array
          title: Whitelist
        public_port:
          type: integer
          title: Public Port
        public_ip:
          type: string
          title: Public Ip
        srv_record:
          type: string
          title: Srv Record
      type: object
      required:
        - port
        - protocol
        - whitelist
        - public_port
        - public_ip
        - srv_record
      title: NetworkServiceResponse
    io_cloud__schemas__response__enterprise__vmaas__NetworkProtocol:
      type: string
      enum:
        - tcp
        - udp
      title: NetworkProtocol

````