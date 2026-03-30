# Source: https://docs.wandb.ai/weave/reference/service-api/service/get-caller-location.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Caller Location

> Lookup the geographic location of a user based on their IP address.

This API exists for debugging purposes and may not be available in the future.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json get /geolocate
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /geolocate:
    get:
      tags:
        - Service
      summary: Get Caller Location
      description: >-
        Lookup the geographic location of a user based on their IP address.


        This API exists for debugging purposes and may not be available in the
        future.
      operationId: get_caller_location_geolocate_get
      parameters:
        - name: ip
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: IP address to geolocate, defaults to client IP address
            examples:
              - 1.2.3.4
            title: Ip
          description: IP address to geolocate, defaults to client IP address
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GeolocationRes'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    GeolocationRes:
      properties:
        ip:
          type: string
          title: Ip
          description: Resolved IP address, useful for debugging
        location:
          anyOf:
            - $ref: '#/components/schemas/Geolocation'
            - type: 'null'
          description: >-
            Information about the location of the IP address, None if could not
            be determined
        allowed:
          type: boolean
          title: Allowed
          description: Whether the IP address is allowed to be used for inference.
          default: false
      type: object
      required:
        - ip
      title: GeolocationRes
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    Geolocation:
      properties:
        file_index:
          type: integer
          title: File Index
          description: row in CSV file
        range_start_int:
          type: integer
          title: Range Start Int
          description: Start of IP range as integer
        range_end_int:
          type: integer
          title: Range End Int
          description: End of IP range as integer
        range_start_ip:
          type: string
          title: Range Start Ip
          description: Start of IP range in dotted decimal notation
        range_end_ip:
          type: string
          title: Range End Ip
          description: End of IP range in dotted decimal notation
        country_code:
          type: string
          title: Country Code
          description: 2-letter country code in ISO 3166-1 Alpha 2 format
        country_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Country Name
          description: Country name, None if could not be determined
      type: object
      required:
        - file_index
        - range_start_int
        - range_end_int
        - range_start_ip
        - range_end_ip
        - country_code
      title: Geolocation
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