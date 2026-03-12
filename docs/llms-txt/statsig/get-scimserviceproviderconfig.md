# Source: https://docs.statsig.com/api-reference/scim-settings/get-scimserviceproviderconfig.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get scimserviceproviderconfig



## OpenAPI

````yaml access-management/scim/scimopenapi.json get /scim/ServiceProviderConfig
openapi: 3.0.0
info:
  title: SCIM API
  description: |2-

          APIs for SCIM compliance.
          
  version: '1.0'
  contact: {}
servers:
  - url: https://statsigapi.net
security: []
tags: []
paths:
  /scim/ServiceProviderConfig:
    get:
      tags:
        - SCIM Settings
      operationId: ScimSettingsController_getServiceProviderConfig
      parameters: []
      responses:
        '200':
          description: ''

````

Built with [Mintlify](https://mintlify.com).