# Source: https://docs.api7.ai/enterprise/api-changelog.md

# API Changelog

Show allOnly Breakings

## From 3.8.x to 3.9.x[â](#from-38x-to-39x "Direct link to From 3.8.x to 3.9.x")

### New14

GET/api/gateway\_groups/{gateway\_group\_id}/debug\_sessions

POST/api/gateway\_groups/{gateway\_group\_id}/debug\_sessions

DELETE/api/gateway\_groups/{gateway\_group\_id}/debug\_sessions/{debug\_session\_id}

GET/api/gateway\_groups/{gateway\_group\_id}/debug\_sessions/{debug\_session\_id}

POST/api/gateway\_groups/{gateway\_group\_id}/debug\_sessions/{debug\_session\_id}/stop

GET/api/gateway\_groups/{gateway\_group\_id}/debug\_sessions/{debug\_session\_id}/traces

GET/api/gateway\_groups/{gateway\_group\_id}/debug\_sessions/{debug\_session\_id}/traces/{trace\_id}

POST/api/gateway\_groups/{gateway\_group\_id}/debug\_sessions/{debug\_session\_id}/traces/{trace\_id}/download

GET/api/portal/tokens

POST/api/portal/tokens

DELETE/api/portal/tokens/{portal\_token\_id}

GET/api/portal/tokens/{portal\_token\_id}

PUT/api/portal/tokens/{portal\_token\_id}

PUT /api/portal/tokens/{portal\_token\_id}/regeneratePOST/api/developers/invites

GET/api/portal/login\_options

POST/api/portal/login\_options

DELETE/api/portal/login\_options/{login\_option\_id}

GET/api/portal/login\_options/{login\_option\_id}

PATCH/api/portal/login\_options/{login\_option\_id}

PUT/api/portal/login\_options/{login\_option\_id}

GET/api/portal/system\_settings/scim

PUT/api/portal/system\_settings/scim

PUT/api/portal/system\_settings/scim/token

### Deleted10

GET/api/gateway\_groups/{gateway\_group\_id}/debug\_sessions

POST/api/gateway\_groups/{gateway\_group\_id}/debug\_sessions

DELETE/api/gateway\_groups/{gateway\_group\_id}/debug\_sessions/{debug\_session\_id}

GET/api/gateway\_groups/{gateway\_group\_id}/debug\_sessions/{debug\_session\_id}

POST/api/gateway\_groups/{gateway\_group\_id}/debug\_sessions/{debug\_session\_id}/stop

GET/api/gateway\_groups/{gateway\_group\_id}/debug\_sessions/{debug\_session\_id}/traces

GET/api/gateway\_groups/{gateway\_group\_id}/debug\_sessions/{debug\_session\_id}/traces/{trace\_id}

POST/api/gateway\_groups/{gateway\_group\_id}/debug\_sessions/{debug\_session\_id}/traces/{trace\_id}/download

GET/api/portal/tokens

POST/api/portal/tokens

DELETE/api/portal/tokens/{portal\_token\_id}

GET/api/portal/tokens/{portal\_token\_id}

PUT/api/portal/tokens/{portal\_token\_id}

PUT /api/portal/tokens/{portal\_token\_id}/regeneratePOST/api/developers/invites

GET/api/portal/login\_options

POST/api/portal/login\_options

DELETE/api/portal/login\_options/{login\_option\_id}

GET/api/portal/login\_options/{login\_option\_id}

PATCH/api/portal/login\_options/{login\_option\_id}

PUT/api/portal/login\_options/{login\_option\_id}

GET/api/portal/system\_settings/scim

PUT/api/portal/system\_settings/scim

PUT/api/portal/system\_settings/scim/token

### Modified950<!-- -->Breakings

Switch to `Show all` to see all changes

GET/api/alert/policies

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

POST/api/alert/policies

* Request Body

  * Modifiedproperty`trigger_conditions`

    * Items changed

      * Schemas added: subschema #7: Shared Dict Free Space Bytes, subschema #8: Shared Dict Free Space Percentage

      * Modifiedproperty`scope`

        * Newproperty`route_id`
        * Newproperty`service_id`

      * Modifiedproperty`value`BreakingBreakingBreakingBreakingBreaking

        * Format changed from 'int64' to 'int32'

      * Modifiedproperty`value`BreakingBreakingBreakingBreakingBreaking

        * Format changed from 'int64' to 'int32'

      * Modifiedproperty`value`BreakingBreakingBreakingBreakingBreaking

        * Format changed from 'int64' to 'int32'

      * Modifiedproperty`value`BreakingBreakingBreakingBreakingBreaking

        * Format changed from 'int64' to 'int32'

      * Modifiedproperty`value`BreakingBreakingBreakingBreakingBreaking

        * Format changed from 'int64' to 'int32'

* Responses

  * Modified response: 200

    * Modifiedproperty`value`BreakingBreakingBreakingBreakingBreaking

      * Modifiedproperty`trigger_conditions`

        * Items changed

          * Schemas added: subschema #7: Shared Dict Free Space Bytes, subschema #8: Shared Dict Free Space Percentage

          * Modifiedproperty`scope`

            * Newproperty`route_id`
            * Newproperty`service_id`

          * Modifiedproperty`value`BreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`value`BreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`value`BreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`value`BreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`value`BreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

GET/api/alert/policies/histories

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/alert/policies/{alert\_policy\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`trigger_conditions`

        * Items changed

          * Schemas added: subschema #7: Shared Dict Free Space Bytes, subschema #8: Shared Dict Free Space Percentage

          * Modifiedproperty`scope`

            * Newproperty`route_id`
            * Newproperty`service_id`

          * Modifiedproperty`value`

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`value`

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`value`

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`value`

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`value`

            * Format changed from 'int64' to 'int32'

PUT/api/alert/policies/{alert\_policy\_id}

* Request Body

  * Modifiedproperty`trigger_conditions`

    * Items changed

      * Schemas added: subschema #7: Shared Dict Free Space Bytes, subschema #8: Shared Dict Free Space Percentage

      * Modifiedproperty`scope`

        * Newproperty`route_id`
        * Newproperty`service_id`

      * Modifiedproperty`value`BreakingBreakingBreakingBreakingBreaking

        * Format changed from 'int64' to 'int32'

      * Modifiedproperty`value`BreakingBreakingBreakingBreakingBreaking

        * Format changed from 'int64' to 'int32'

      * Modifiedproperty`value`BreakingBreakingBreakingBreakingBreaking

        * Format changed from 'int64' to 'int32'

      * Modifiedproperty`value`BreakingBreakingBreakingBreakingBreaking

        * Format changed from 'int64' to 'int32'

      * Modifiedproperty`value`BreakingBreakingBreakingBreakingBreaking

        * Format changed from 'int64' to 'int32'

GET/api/api\_products

* Modified query param: page
  * Format changed from 'int64' to 'int32'

* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Schemas added: subschema #1: Gateway API Product, subschema #2: External API Product
        * Schemas deleted: subschema #1, subschema #2

POST/api/api\_products

* Request Body

  * Property 'AnyOf' changed
    * Schemas deleted: subschema #1, subschema #2

  * Schemas added: subschema #1, subschema #2

  * Type changed from 'object' to ''

  * Required changed

    * Deleted required property: name
    * Deleted required property: raw\_openapi
    * Deleted required property: type

  * Deletedproperty`name`

  * Deletedproperty`raw_openapi`

  * Deletedproperty`server_url`

  * Deletedproperty`server_urls`

  * Deletedproperty`status`

  * Deletedproperty`type`

  * Deletedproperty`visibility`

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Schemas added: subschema #1, subschema #2
      * Schemas deleted: subschema #1, subschema #2

GET/api/api\_products/{api\_product\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Schemas added: subschema #1, subschema #2
      * Schemas deleted: subschema #1, subschema #2

PATCH/api/api\_products/{api\_product\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Schemas added: subschema #1, subschema #2
      * Schemas deleted: subschema #1, subschema #2

PUT/api/api\_products/{api\_product\_id}

* Request Body

  * Property 'AnyOf' changed
    * Schemas deleted: subschema #1, subschema #2

  * Schemas added: subschema #1, subschema #2

  * Type changed from 'object' to ''

  * Required changed

    * Deleted required property: name
    * Deleted required property: raw\_openapi
    * Deleted required property: type

  * Deletedproperty`name`

  * Deletedproperty`raw_openapi`

  * Deletedproperty`server_url`

  * Deletedproperty`server_urls`

  * Deletedproperty`status`

  * Deletedproperty`type`

  * Deletedproperty`visibility`

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Schemas added: subschema #1, subschema #2
      * Schemas deleted: subschema #1, subschema #2

GET/api/api\_products/{api\_product\_id}/notification\_histories

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/api\_products/{api\_product\_id}/subscriptions

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/approvals

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/audit\_logs

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/contact\_points

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/contact\_points/{contact\_point\_id}/notification\_logs

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/contact\_points/{contact\_point\_id}/usages

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/custom\_plugins

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/dcr\_providers

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/developers

* Modified query param: page
  * Format changed from 'int64' to 'int32'

* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Deletedproperty`email`
        * Deletedproperty`email_verified`

DELETE/api/developers/{developer\_id}

* Modifiedpath param`developer_id`

  * Name changed from 'developer\_id' to 'developer\_external\_id'
  * Example changed from null to 'dev1'

GET/api/gateway\_groups

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/gateway\_groups/{gateway\_group\_id}/ca\_certificates/{ca\_certificate\_id}/usage

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/gateway\_groups/{gateway\_group\_id}/certificates/{certificate\_id}/usage

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/gateway\_groups/{gateway\_group\_id}/instances

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/gateway\_groups/{gateway\_group\_id}/secret\_providers/{secret\_provider}/{secret\_provider\_id}/usage

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/gateway\_groups/{gateway\_group\_id}/service\_registries

* Modified query param: page
  * Format changed from 'int64' to 'int32'

* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Schemas added: subschema #1, subschema #2
        * Schemas deleted: subschema #1, subschema #2

POST/api/gateway\_groups/{gateway\_group\_id}/service\_registries

* Request Body

  * Modifiedproperty`health_check`

    * Modifiedproperty`probe_interval`Breaking

      * Format changed from 'int64' to 'int32'

    * Modifiedproperty`probe_timeout`Breaking

      * Format changed from 'int64' to 'int32'

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`health_check`

        * Modifiedproperty`probe_interval`Breaking

          * Format changed from 'int64' to 'int32'

        * Modifiedproperty`probe_timeout`Breaking

          * Format changed from 'int64' to 'int32'

GET/api/gateway\_groups/{gateway\_group\_id}/service\_registries/{service\_registry\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`health_check`

        * Modifiedproperty`probe_interval`

          * Format changed from 'int64' to 'int32'

        * Modifiedproperty`probe_timeout`

          * Format changed from 'int64' to 'int32'

PUT/api/gateway\_groups/{gateway\_group\_id}/service\_registries/{service\_registry\_id}

* Request Body

  * Modifiedproperty`health_check`

    * Modifiedproperty`probe_interval`Breaking

      * Format changed from 'int64' to 'int32'

    * Modifiedproperty`probe_timeout`Breaking

      * Format changed from 'int64' to 'int32'

GET/api/gateway\_groups/{gateway\_group\_id}/service\_registries/{service\_registry\_id}/connected\_services

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/gateway\_groups/{gateway\_group\_id}/service\_registries/{service\_registry\_id}/health\_check\_history

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/gateway\_groups/{gateway\_group\_id}/services

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/healthcheck

* Newquery param`upstream_id`

GET/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/routes

* Modified query param: page
  * Format changed from 'int64' to 'int32'

* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Modifiedproperty`methods`

          * Items changed
            * New enum values: \[CONNECT]

GET/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/routes/{route\_template\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`methods`

        * Items changed
          * New enum values: \[CONNECT]

GET/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/runtime\_configuration

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Schemas added: subschema #1, subschema #2
      * Schemas deleted: subschema #1, subschema #2

PATCH/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/runtime\_configuration

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Schemas added: subschema #1, subschema #2
      * Schemas deleted: subschema #1, subschema #2

GET/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/stream\_routes

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/gateway\_groups/{gateway\_group\_id}/snis/{sni\_id}/usage

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/gateway\_groups/{gateway\_group\_id}/ssls/{ssl\_id}/usage

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

POST/api/import/services

* Request Body

  * Modifiedproperty`routes`

    * Items changed

      * Modifiedproperty`methods`

        * Items changed
          * New enum values: \[CONNECT]

POST/api/import/services/template

* Request Body

  * Modifiedproperty`routes`

    * Items changed

      * Modifiedproperty`methods`

        * Items changed
          * New enum values: \[CONNECT]

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`routes`

        * Items changed

          * Modifiedproperty`methods`

            * Items changed
              * New enum values: \[CONNECT]

GET/api/instances

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/instances/cores\_usages/export

* Modified query param: begin\_at
  * Format changed from 'int64' to 'int32'
* Modified query param: end\_at
  * Format changed from 'int64' to 'int32'

GET/api/license

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Schemas added: subschema #1, subschema #2
      * Schemas deleted: subschema #1, subschema #2

PUT/api/license

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`effective_at`

        * Format changed from 'int64' to 'int32'

      * Modifiedproperty`expired_at`

        * Format changed from 'int64' to 'int32'

      * Modifiedproperty`issuance_date`

        * Format changed from 'int64' to 'int32'

GET/api/login\_options

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/login\_options\_for\_login

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

PUT/api/openapi/convert

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`routes`

        * Items changed

          * Modifiedproperty`methods`

            * Items changed
              * New enum values: \[CONNECT]

GET/api/permission\_policies

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/portals

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

POST/api/resource\_names

* Request Body

  * Modifiedproperty`resource_type`

    * New enum values: \[published\_service published\_route]

GET/api/roles

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/roles/{role\_id}/permission\_policies

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/routes/template

* Modified query param: page
  * Format changed from 'int64' to 'int32'

* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Modifiedproperty`methods`

          * Items changed
            * New enum values: \[CONNECT]

POST/api/routes/template

* Request Body

  * Modifiedproperty`methods`

    * Items changed
      * New enum values: \[CONNECT]

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`methods`

        * Items changed
          * New enum values: \[CONNECT]

GET/api/routes/template/{route\_template\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`methods`

        * Items changed
          * New enum values: \[CONNECT]

PATCH/api/routes/template/{route\_template\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`methods`

        * Items changed
          * New enum values: \[CONNECT]

PUT/api/routes/template/{route\_template\_id}

* Request Body

  * Modifiedproperty`methods`

    * Items changed
      * New enum values: \[CONNECT]

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`methods`

        * Items changed
          * New enum values: \[CONNECT]

GET/api/service\_versions/{service\_version\_id}/routes

* Modified query param: page
  * Format changed from 'int64' to 'int32'

* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Modifiedproperty`methods`

          * Items changed
            * New enum values: \[CONNECT]

GET/api/service\_versions/{service\_version\_id}/routes/{route\_version\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`methods`

        * Items changed
          * New enum values: \[CONNECT]

GET/api/service\_versions/{service\_version\_id}/stream\_routes

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

POST/api/services/conflict\_check

* Request Body

  * Modifiedproperty`services`

    * Items changed

      * Modifiedproperty`routes`

        * Items changed

          * Modifiedproperty`methods`

            * Items changed
              * New enum values: \[CONNECT]

GET/api/services/template

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/stream\_routes/template

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/api/tokens

* Modified query param: page
  * Format changed from 'int64' to 'int32'

* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Modifiedproperty`expires_at`

          * Format changed from 'int64' to 'int32'

POST/api/tokens

* Request Body

  * Modifiedproperty`expires_at`Breaking

    * Format changed from 'int64' to 'int32'

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`expires_at`Breaking

        * Format changed from 'int64' to 'int32'

GET/api/tokens/{token\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`expires_at`

        * Format changed from 'int64' to 'int32'

PUT/api/tokens/{token\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`expires_at`

        * Format changed from 'int64' to 'int32'

PUT/api/tokens/{token\_id}/regenerate

* Request Body

  * Modifiedproperty`expires_at`Breaking

    * Format changed from 'int64' to 'int32'

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`expires_at`Breaking

        * Format changed from 'int64' to 'int32'

GET/api/users

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/apisix/admin/ca\_certificates

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/apisix/admin/certificates

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/apisix/admin/consumers

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/apisix/admin/consumers/{username}/credentials

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/apisix/admin/global\_rules

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/apisix/admin/protos

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/apisix/admin/routes

* Modified query param: page
  * Format changed from 'int64' to 'int32'

* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Modifiedproperty`methods`

          * Items changed
            * New enum values: \[CONNECT]

POST/apisix/admin/routes

* Request Body

  * Modifiedproperty`methods`

    * Items changed
      * New enum values: \[CONNECT]

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`methods`

        * Items changed
          * New enum values: \[CONNECT]

GET/apisix/admin/routes/{route\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`methods`

        * Items changed
          * New enum values: \[CONNECT]

PATCH/apisix/admin/routes/{route\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`methods`

        * Items changed
          * New enum values: \[CONNECT]

PUT/apisix/admin/routes/{route\_id}

* Request Body

  * Modifiedproperty`methods`

    * Items changed
      * New enum values: \[CONNECT]

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`methods`

        * Items changed
          * New enum values: \[CONNECT]

GET/apisix/admin/secret\_providers

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/apisix/admin/services

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

POST/apisix/admin/services

* Request Body

  * Modifiedproperty`upstream`

    * Modifiedproperty`checks`

      * Property 'AnyOf' changed

        * Modifiedproperty`active`

          * Modifiedproperty`concurrency`BreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`healthy`

            * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

          * Modifiedproperty`port`BreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`unhealthy`

            * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

        * Modifiedproperty`active`

          * Modifiedproperty`concurrency`BreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`healthy`

            * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

          * Modifiedproperty`port`BreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`unhealthy`

            * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

        * Modifiedproperty`passive`

          * Modifiedproperty`healthy`

            * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

          * Modifiedproperty`unhealthy`

            * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

  * Modifiedproperty`upstream`

    * Modifiedproperty`checks`

      * Property 'AnyOf' changed

        * Modifiedproperty`active`

          * Modifiedproperty`concurrency`BreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`healthy`

            * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

          * Modifiedproperty`port`BreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`unhealthy`

            * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

        * Modifiedproperty`active`

          * Modifiedproperty`concurrency`BreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`healthy`

            * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

          * Modifiedproperty`port`BreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`unhealthy`

            * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

        * Modifiedproperty`passive`

          * Modifiedproperty`healthy`

            * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

          * Modifiedproperty`unhealthy`

            * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

PUT/apisix/admin/services/{service\_id}

* Request Body

  * Modifiedproperty`upstream`

    * Modifiedproperty`checks`

      * Property 'AnyOf' changed

        * Modifiedproperty`active`

          * Modifiedproperty`concurrency`BreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`healthy`

            * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

          * Modifiedproperty`port`BreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`unhealthy`

            * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

        * Modifiedproperty`active`

          * Modifiedproperty`concurrency`BreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`healthy`

            * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

          * Modifiedproperty`port`BreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`unhealthy`

            * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

        * Modifiedproperty`passive`

          * Modifiedproperty`healthy`

            * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

          * Modifiedproperty`unhealthy`

            * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

  * Modifiedproperty`upstream`

    * Modifiedproperty`checks`

      * Property 'AnyOf' changed

        * Modifiedproperty`active`

          * Modifiedproperty`concurrency`BreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`healthy`

            * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

          * Modifiedproperty`port`BreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`unhealthy`

            * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

        * Modifiedproperty`active`

          * Modifiedproperty`concurrency`BreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`healthy`

            * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

          * Modifiedproperty`port`BreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`unhealthy`

            * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

        * Modifiedproperty`passive`

          * Modifiedproperty`healthy`

            * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

          * Modifiedproperty`unhealthy`

            * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

GET/apisix/admin/services/{service\_id}/upstreams

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Modifiedproperty`checks`

          * Property 'AnyOf' changed

            * Modifiedproperty`active`

              * Modifiedproperty`concurrency`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`healthy`

                * Modifiedproperty`interval`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`successes`

                  * Format changed from 'int64' to 'int32'

              * Modifiedproperty`port`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`unhealthy`

                * Modifiedproperty`http_failures`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`interval`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`tcp_failures`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`timeouts`

                  * Format changed from 'int64' to 'int32'

            * Modifiedproperty`active`

              * Modifiedproperty`concurrency`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`healthy`

                * Modifiedproperty`interval`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`successes`

                  * Format changed from 'int64' to 'int32'

              * Modifiedproperty`port`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`unhealthy`

                * Modifiedproperty`http_failures`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`interval`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`tcp_failures`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`timeouts`

                  * Format changed from 'int64' to 'int32'

            * Modifiedproperty`passive`

              * Modifiedproperty`healthy`

                * Modifiedproperty`successes`

                  * Format changed from 'int64' to 'int32'

              * Modifiedproperty`unhealthy`

                * Modifiedproperty`http_failures`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`tcp_failures`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`timeouts`

                  * Format changed from 'int64' to 'int32'

        * Modifiedproperty`checks`

          * Property 'AnyOf' changed

            * Modifiedproperty`active`

              * Modifiedproperty`concurrency`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`healthy`

                * Modifiedproperty`interval`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`successes`

                  * Format changed from 'int64' to 'int32'

              * Modifiedproperty`port`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`unhealthy`

                * Modifiedproperty`http_failures`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`interval`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`tcp_failures`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`timeouts`

                  * Format changed from 'int64' to 'int32'

            * Modifiedproperty`active`

              * Modifiedproperty`concurrency`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`healthy`

                * Modifiedproperty`interval`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`successes`

                  * Format changed from 'int64' to 'int32'

              * Modifiedproperty`port`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`unhealthy`

                * Modifiedproperty`http_failures`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`interval`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`tcp_failures`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`timeouts`

                  * Format changed from 'int64' to 'int32'

            * Modifiedproperty`passive`

              * Modifiedproperty`healthy`

                * Modifiedproperty`successes`

                  * Format changed from 'int64' to 'int32'

              * Modifiedproperty`unhealthy`

                * Modifiedproperty`http_failures`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`tcp_failures`

                  * Format changed from 'int64' to 'int32'

                * Modifiedproperty`timeouts`

                  * Format changed from 'int64' to 'int32'

POST/apisix/admin/services/{service\_id}/upstreams

* Request Body

  * Modifiedproperty`checks`

    * Property 'AnyOf' changed

      * Modifiedproperty`active`

        * Modifiedproperty`concurrency`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

          * Format changed from 'int64' to 'int32'

        * Modifiedproperty`healthy`

          * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

        * Modifiedproperty`port`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

          * Format changed from 'int64' to 'int32'

        * Modifiedproperty`unhealthy`

          * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

      * Modifiedproperty`active`

        * Modifiedproperty`concurrency`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

          * Format changed from 'int64' to 'int32'

        * Modifiedproperty`healthy`

          * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

        * Modifiedproperty`port`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

          * Format changed from 'int64' to 'int32'

        * Modifiedproperty`unhealthy`

          * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

      * Modifiedproperty`passive`

        * Modifiedproperty`healthy`

          * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

        * Modifiedproperty`unhealthy`

          * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

  * Modifiedproperty`checks`

    * Property 'AnyOf' changed

      * Modifiedproperty`active`

        * Modifiedproperty`concurrency`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

          * Format changed from 'int64' to 'int32'

        * Modifiedproperty`healthy`

          * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

        * Modifiedproperty`port`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

          * Format changed from 'int64' to 'int32'

        * Modifiedproperty`unhealthy`

          * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

      * Modifiedproperty`active`

        * Modifiedproperty`concurrency`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

          * Format changed from 'int64' to 'int32'

        * Modifiedproperty`healthy`

          * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

        * Modifiedproperty`port`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

          * Format changed from 'int64' to 'int32'

        * Modifiedproperty`unhealthy`

          * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

      * Modifiedproperty`passive`

        * Modifiedproperty`healthy`

          * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

        * Modifiedproperty`unhealthy`

          * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`checks`

        * Property 'AnyOf' changed

          * Modifiedproperty`active`

            * Modifiedproperty`concurrency`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`healthy`

              * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`port`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

          * Modifiedproperty`active`

            * Modifiedproperty`concurrency`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`healthy`

              * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`port`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

          * Modifiedproperty`passive`

            * Modifiedproperty`healthy`

              * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

      * Modifiedproperty`checks`

        * Property 'AnyOf' changed

          * Modifiedproperty`active`

            * Modifiedproperty`concurrency`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`healthy`

              * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`port`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

          * Modifiedproperty`active`

            * Modifiedproperty`concurrency`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`healthy`

              * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`port`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

          * Modifiedproperty`passive`

            * Modifiedproperty`healthy`

              * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

GET/apisix/admin/services/{service\_id}/upstreams/{upstream\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`checks`

        * Property 'AnyOf' changed

          * Modifiedproperty`active`

            * Modifiedproperty`concurrency`

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`healthy`

              * Modifiedproperty`interval`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`successes`

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`port`

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`interval`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`

                * Format changed from 'int64' to 'int32'

          * Modifiedproperty`active`

            * Modifiedproperty`concurrency`

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`healthy`

              * Modifiedproperty`interval`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`successes`

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`port`

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`interval`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`

                * Format changed from 'int64' to 'int32'

          * Modifiedproperty`passive`

            * Modifiedproperty`healthy`

              * Modifiedproperty`successes`

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`

                * Format changed from 'int64' to 'int32'

      * Modifiedproperty`checks`

        * Property 'AnyOf' changed

          * Modifiedproperty`active`

            * Modifiedproperty`concurrency`

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`healthy`

              * Modifiedproperty`interval`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`successes`

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`port`

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`interval`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`

                * Format changed from 'int64' to 'int32'

          * Modifiedproperty`active`

            * Modifiedproperty`concurrency`

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`healthy`

              * Modifiedproperty`interval`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`successes`

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`port`

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`interval`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`

                * Format changed from 'int64' to 'int32'

          * Modifiedproperty`passive`

            * Modifiedproperty`healthy`

              * Modifiedproperty`successes`

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`

                * Format changed from 'int64' to 'int32'

PATCH/apisix/admin/services/{service\_id}/upstreams/{upstream\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`checks`

        * Property 'AnyOf' changed

          * Modifiedproperty`active`

            * Modifiedproperty`concurrency`

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`healthy`

              * Modifiedproperty`interval`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`successes`

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`port`

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`interval`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`

                * Format changed from 'int64' to 'int32'

          * Modifiedproperty`active`

            * Modifiedproperty`concurrency`

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`healthy`

              * Modifiedproperty`interval`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`successes`

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`port`

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`interval`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`

                * Format changed from 'int64' to 'int32'

          * Modifiedproperty`passive`

            * Modifiedproperty`healthy`

              * Modifiedproperty`successes`

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`

                * Format changed from 'int64' to 'int32'

      * Modifiedproperty`checks`

        * Property 'AnyOf' changed

          * Modifiedproperty`active`

            * Modifiedproperty`concurrency`

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`healthy`

              * Modifiedproperty`interval`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`successes`

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`port`

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`interval`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`

                * Format changed from 'int64' to 'int32'

          * Modifiedproperty`active`

            * Modifiedproperty`concurrency`

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`healthy`

              * Modifiedproperty`interval`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`successes`

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`port`

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`interval`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`

                * Format changed from 'int64' to 'int32'

          * Modifiedproperty`passive`

            * Modifiedproperty`healthy`

              * Modifiedproperty`successes`

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`

                * Format changed from 'int64' to 'int32'

PUT/apisix/admin/services/{service\_id}/upstreams/{upstream\_id}

* Request Body

  * Modifiedproperty`checks`

    * Property 'AnyOf' changed

      * Modifiedproperty`active`

        * Modifiedproperty`concurrency`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

          * Format changed from 'int64' to 'int32'

        * Modifiedproperty`healthy`

          * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

        * Modifiedproperty`port`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

          * Format changed from 'int64' to 'int32'

        * Modifiedproperty`unhealthy`

          * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

      * Modifiedproperty`active`

        * Modifiedproperty`concurrency`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

          * Format changed from 'int64' to 'int32'

        * Modifiedproperty`healthy`

          * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

        * Modifiedproperty`port`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

          * Format changed from 'int64' to 'int32'

        * Modifiedproperty`unhealthy`

          * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

      * Modifiedproperty`passive`

        * Modifiedproperty`healthy`

          * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

        * Modifiedproperty`unhealthy`

          * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

  * Modifiedproperty`checks`

    * Property 'AnyOf' changed

      * Modifiedproperty`active`

        * Modifiedproperty`concurrency`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

          * Format changed from 'int64' to 'int32'

        * Modifiedproperty`healthy`

          * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

        * Modifiedproperty`port`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

          * Format changed from 'int64' to 'int32'

        * Modifiedproperty`unhealthy`

          * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

      * Modifiedproperty`active`

        * Modifiedproperty`concurrency`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

          * Format changed from 'int64' to 'int32'

        * Modifiedproperty`healthy`

          * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

        * Modifiedproperty`port`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

          * Format changed from 'int64' to 'int32'

        * Modifiedproperty`unhealthy`

          * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

      * Modifiedproperty`passive`

        * Modifiedproperty`healthy`

          * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

        * Modifiedproperty`unhealthy`

          * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

          * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

            * Format changed from 'int64' to 'int32'

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`checks`

        * Property 'AnyOf' changed

          * Modifiedproperty`active`

            * Modifiedproperty`concurrency`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`healthy`

              * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`port`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

          * Modifiedproperty`active`

            * Modifiedproperty`concurrency`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`healthy`

              * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`port`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

          * Modifiedproperty`passive`

            * Modifiedproperty`healthy`

              * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

      * Modifiedproperty`checks`

        * Property 'AnyOf' changed

          * Modifiedproperty`active`

            * Modifiedproperty`concurrency`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`healthy`

              * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`port`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

          * Modifiedproperty`active`

            * Modifiedproperty`concurrency`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`healthy`

              * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`port`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

              * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`interval`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

          * Modifiedproperty`passive`

            * Modifiedproperty`healthy`

              * Modifiedproperty`successes`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

            * Modifiedproperty`unhealthy`

              * Modifiedproperty`http_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`tcp_failures`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

              * Modifiedproperty`timeouts`BreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreakingBreaking

                * Format changed from 'int64' to 'int32'

GET/apisix/admin/snis

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/apisix/admin/ssls

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

GET/apisix/admin/stream\_routes

* Modified query param: page
  * Format changed from 'int64' to 'int32'
* Modified query param: page\_size
  * Format changed from 'int64' to 'int32'

## From 3.7.x to 3.8.x[â](#from-37x-to-38x "Direct link to From 3.7.x to 3.8.x")

### New26

GET/api/audit\_logs/config

GET/api/cas/{login\_option\_id}/login

GET/api/cas/{login\_option\_id}/logout

GET/api/dcr\_providers

POST/api/dcr\_providers

DELETE/api/dcr\_providers/{dcr\_provider\_id}

GET/api/dcr\_providers/{dcr\_provider\_id}

PUT/api/dcr\_providers/{dcr\_provider\_id}

DELETE/api/developers/{developer\_id}

GET/api/gateway\_groups/{gateway\_group\_id}/admin\_key

GET/api/gateway\_groups/{gateway\_group\_id}/deployment/docker-compose

GET/api/gateway\_groups/{gateway\_group\_id}/ingress/script

GET/api/gateway\_groups/{gateway\_group\_id}/ingress/step1

GET/api/portals

POST/api/portals

DELETE/api/portals/{portal\_id}

GET/api/portals/{portal\_id}

PUT/api/portals/{portal\_id}

GET/apisix/admin/protos

POST/apisix/admin/protos

DELETE/apisix/admin/protos/{proto\_id}

GET/apisix/admin/protos/{proto\_id}

PUT/apisix/admin/protos/{proto\_id}

DELETE/apisix/admin/secret\_providers/{secret\_provider}/{secret\_provider\_id}

GET/apisix/admin/secret\_providers/{secret\_provider}/{secret\_provider\_id}

PUT /apisix/admin/secret\_providers/{secret\_provider}/{secret\_provider\_id}GET/api/dataplane/consumer\_query

GET/api/dataplane/developer\_query

POST/api/dataplane/healthcheck

POST/api/dataplane/heartbeat

POST/api/dataplane/metrics

POST/api/dataplane/service\_registry\_healthcheck

DELETE/apisix/admin/secret\_providers/aws/{secret\_provider\_id}

GET/apisix/admin/secret\_providers/aws/{secret\_provider\_id}

PUT/apisix/admin/secret\_providers/aws/{secret\_provider\_id}

DELETE/apisix/admin/secret\_providers/kubernetes/{secret\_provider\_id}

GET/apisix/admin/secret\_providers/kubernetes/{secret\_provider\_id}

PUT/apisix/admin/secret\_providers/kubernetes/{secret\_provider\_id}

DELETE/apisix/admin/secret\_providers/vault/{secret\_provider\_id}

GET/apisix/admin/secret\_providers/vault/{secret\_provider\_id}

PUT/apisix/admin/secret\_providers/vault/{secret\_provider\_id}apisix:

replicaCount: 1

image:

repository: api7/api7-ee-3-gateway

tag: dev

extraEnvVars:

### Deleted15

GET/api/audit\_logs/config

GET/api/cas/{login\_option\_id}/login

GET/api/cas/{login\_option\_id}/logout

GET/api/dcr\_providers

POST/api/dcr\_providers

DELETE/api/dcr\_providers/{dcr\_provider\_id}

GET/api/dcr\_providers/{dcr\_provider\_id}

PUT/api/dcr\_providers/{dcr\_provider\_id}

DELETE/api/developers/{developer\_id}

GET/api/gateway\_groups/{gateway\_group\_id}/admin\_key

GET/api/gateway\_groups/{gateway\_group\_id}/deployment/docker-compose

GET/api/gateway\_groups/{gateway\_group\_id}/ingress/script

GET/api/gateway\_groups/{gateway\_group\_id}/ingress/step1

GET/api/portals

POST/api/portals

DELETE/api/portals/{portal\_id}

GET/api/portals/{portal\_id}

PUT/api/portals/{portal\_id}

GET/apisix/admin/protos

POST/apisix/admin/protos

DELETE/apisix/admin/protos/{proto\_id}

GET/apisix/admin/protos/{proto\_id}

PUT/apisix/admin/protos/{proto\_id}

DELETE/apisix/admin/secret\_providers/{secret\_provider}/{secret\_provider\_id}

GET/apisix/admin/secret\_providers/{secret\_provider}/{secret\_provider\_id}

PUT /apisix/admin/secret\_providers/{secret\_provider}/{secret\_provider\_id}GET/api/dataplane/consumer\_query

GET/api/dataplane/developer\_query

POST/api/dataplane/healthcheck

POST/api/dataplane/heartbeat

POST/api/dataplane/metrics

POST/api/dataplane/service\_registry\_healthcheck

DELETE/apisix/admin/secret\_providers/aws/{secret\_provider\_id}

GET/apisix/admin/secret\_providers/aws/{secret\_provider\_id}

PUT/apisix/admin/secret\_providers/aws/{secret\_provider\_id}

DELETE/apisix/admin/secret\_providers/kubernetes/{secret\_provider\_id}

GET/apisix/admin/secret\_providers/kubernetes/{secret\_provider\_id}

PUT/apisix/admin/secret\_providers/kubernetes/{secret\_provider\_id}

DELETE/apisix/admin/secret\_providers/vault/{secret\_provider\_id}

GET/apisix/admin/secret\_providers/vault/{secret\_provider\_id}

PUT/apisix/admin/secret\_providers/vault/{secret\_provider\_id}apisix:

replicaCount: 1

image:

repository: api7/api7-ee-3-gateway

tag: dev

extraEnvVars:

### Modified2900<!-- -->Breakings

Switch to `Show all` to see all changes

GET/api/alert/policies

* Modified query param: labels

  * Type changed from 'object' to 'string'
  * Example changed from null to 'labels%5Bversion%5D=v2'
  * AdditionalProperties changed
    * Schema deleted

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

POST/api/alert/policies

* Request Body

  * Modifiedproperty`desc`

    * Example changed from null to 'Object description.'

  * Modifiedproperty`labels`

    * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

  * Modifiedproperty`name`

    * Example changed from null to '500 status alert'

  * Modifiedproperty`notifications`

    * Items changed

      * Schemas added: subschema #1: Email, subschema #2: Webhook
      * Schemas deleted: subschema #1, subschema #2

  * Modifiedproperty`trigger_conditions`

    * Items changed

      * Schemas added: subschema #3: License Expiry, subschema #5: Data Plane Cores Exceeded

      * Schemas deleted: subschema #4: Dataplane Cores Exceeded

      * Modifiedproperty`event_config`

        * Modifiedproperty`duration`

          * Example changed from null to 60

        * Modifiedproperty`http_status_code`

          * Example changed from null to '500'

        * Modifiedproperty`unit`

          * Example changed from null to 'second'

      * Modifiedproperty`operator`

        * Example changed from null to 'larger\_than'

      * Modifiedproperty`scope`BreakingBreakingBreakingBreaking

        * Schemas added: subschema #1: Gateway Group IDs, subschema #2: Gateway Group Labels

        * Schemas deleted: subschema #1, subschema #2

        * Modifiedproperty`gateway_group_ids`

          * Items changed
            * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

        * Modifiedproperty`gateway_group_labels`

          * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

      * Modifiedproperty`value`

        * Example changed from null to 5

      * Modifiedproperty`scope`BreakingBreakingBreakingBreaking

        * Schemas added: subschema #1: Gateway Group IDs, subschema #2: Gateway Group Labels

        * Schemas deleted: subschema #1, subschema #2

        * Modifiedproperty`gateway_group_ids`

          * Items changed
            * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

        * Modifiedproperty`gateway_group_labels`

          * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

      * Modifiedproperty`scope`BreakingBreakingBreakingBreaking

        * Schemas added: subschema #1: Gateway Group IDs, subschema #2: Gateway Group Labels

        * Schemas deleted: subschema #1, subschema #2

        * Modifiedproperty`gateway_group_ids`

          * Items changed
            * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

        * Modifiedproperty`gateway_group_labels`

          * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

      * Modifiedproperty`value_unit`

        * Example changed from null to 'second'

      * Modifiedproperty`scope`BreakingBreakingBreakingBreaking

        * Schemas added: subschema #1: Gateway Group IDs, subschema #2: Gateway Group Labels

        * Schemas deleted: subschema #1, subschema #2

        * Modifiedproperty`gateway_group_ids`

          * Items changed
            * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

        * Modifiedproperty`gateway_group_labels`

          * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/alert/policies/histories

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

DELETE/api/alert/policies/{alert\_policy\_id}

* Responses

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/alert/policies/{alert\_policy\_id}

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PATCH/api/alert/policies/{alert\_policy\_id}

* Request Body

  * Items changed

    * Schemas added: subschema #1: add/replace, subschema #2: remove
    * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/alert/policies/{alert\_policy\_id}

* Request Body

  * Modifiedproperty`desc`

    * Example changed from null to 'Object description.'

  * Modifiedproperty`labels`

    * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

  * Modifiedproperty`name`

    * Example changed from null to '500 status alert'

  * Modifiedproperty`notifications`

    * Items changed

      * Schemas added: subschema #1: Email, subschema #2: Webhook
      * Schemas deleted: subschema #1, subschema #2

  * Modifiedproperty`trigger_conditions`

    * Items changed

      * Schemas added: subschema #3: License Expiry, subschema #5: Data Plane Cores Exceeded

      * Schemas deleted: subschema #4: Dataplane Cores Exceeded

      * Modifiedproperty`event_config`

        * Modifiedproperty`duration`

          * Example changed from null to 60

        * Modifiedproperty`http_status_code`

          * Example changed from null to '500'

        * Modifiedproperty`unit`

          * Example changed from null to 'second'

      * Modifiedproperty`operator`

        * Example changed from null to 'larger\_than'

      * Modifiedproperty`scope`BreakingBreakingBreakingBreaking

        * Schemas added: subschema #1: Gateway Group IDs, subschema #2: Gateway Group Labels

        * Schemas deleted: subschema #1, subschema #2

        * Modifiedproperty`gateway_group_ids`

          * Items changed
            * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

        * Modifiedproperty`gateway_group_labels`

          * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

      * Modifiedproperty`value`

        * Example changed from null to 5

      * Modifiedproperty`scope`BreakingBreakingBreakingBreaking

        * Schemas added: subschema #1: Gateway Group IDs, subschema #2: Gateway Group Labels

        * Schemas deleted: subschema #1, subschema #2

        * Modifiedproperty`gateway_group_ids`

          * Items changed
            * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

        * Modifiedproperty`gateway_group_labels`

          * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

      * Modifiedproperty`scope`BreakingBreakingBreakingBreaking

        * Schemas added: subschema #1: Gateway Group IDs, subschema #2: Gateway Group Labels

        * Schemas deleted: subschema #1, subschema #2

        * Modifiedproperty`gateway_group_ids`

          * Items changed
            * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

        * Modifiedproperty`gateway_group_labels`

          * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

      * Modifiedproperty`value_unit`

        * Example changed from null to 'second'

      * Modifiedproperty`scope`BreakingBreakingBreakingBreaking

        * Schemas added: subschema #1: Gateway Group IDs, subschema #2: Gateway Group Labels

        * Schemas deleted: subschema #1, subschema #2

        * Modifiedproperty`gateway_group_ids`

          * Items changed
            * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

        * Modifiedproperty`gateway_group_labels`

          * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

* Responses

  * Deleted response: default

  * Modified response: 200
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/allow\_access

* Request Body

  * Example changed from null to map\[hasAccess:map\[action:iam:UpdateCustomRole context:map\[role\_label:map\[platform:external]] resource:arn:api7:iam:role/767ff422-614b-4c0c-a4ea-287c26c773ba]]

  * AdditionalProperties changed

    * Title changed from '' to 'properties'

    * Modifiedproperty`context`Breaking

      * Property 'AnyOf' changed

        * Schemas added: subschema #1: Context for Gateway Group, subschema #2: Context for Service, subschema #3: Context for Published Service, subschema #4: Context for Role, subschema #5: Context for Permission Policy, subschema #6: Context for User, subschema #7: Context for Consumer, subschema #8: Context for Secret, subschema #9: Context for Contact Point, subschema #10: Context for Alert Policy, subschema #11: Context for Developer, subschema #12: Context for API Product, subschema #13: Context for CA Certificate, subschema #14: Context for Certificate, subschema #15: Context for SNI, subschema #16: Context for Portal
        * Schemas deleted: subschema #1: ContextForGatewayGroup, subschema #2: ContextForService, subschema #3: ContextForPublishedService, subschema #4: ContextForRole, subschema #5: ContextForPermissionPolicy, subschema #6: ContextForUser, subschema #7: ContextForConsumer, subschema #8: ContextForSecret, subschema #9: ContextForContactPoint, subschema #10: ContextForAlertPolicy, subschema #11: ContextForDeveloper, subschema #12: ContextForAPIProduct, subschema #13: ContextForCaCertificate, subschema #14: ContextForCertificate, subschema #15: ContextForSNI

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2
    * Example changed from null to map\[value:map\[hasAccess:true]]

GET/api/api\_products

* Tags changed from 'API Product' to 'Provider Portal - API Product'

* Newquery param`portal_id`

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Modified query param: service\_id
  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/api\_products

* Tags changed from 'API Product' to 'Provider Portal - API Product'

* Newquery param`portal_id`

* Request Body

  * Schemas added: subschema #1: Gateway API Product, subschema #2: External API Product
  * Schemas deleted: subschema #1: ExternalAPIProduct, subschema #2: GatewayAPIProduct

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

DELETE/api/api\_products/{api\_product\_id}

* Tags changed from 'API Product' to 'Provider Portal - API Product'

* Newquery param`portal_id`

* Modifiedpath param`api_product_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/api\_products/{api\_product\_id}

* Tags changed from 'API Product' to 'Provider Portal - API Product'

* Newquery param`portal_id`

* Modifiedpath param`api_product_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PATCH/api/api\_products/{api\_product\_id}

* Tags changed from 'API Product' to 'Provider Portal - API Product'

* Newquery param`portal_id`

* Modifiedpath param`api_product_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Request Body

  * Items changed

    * Schemas added: subschema #1: add/replace, subschema #2: remove
    * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/api\_products/{api\_product\_id}

* Tags changed from 'API Product' to 'Provider Portal - API Product'

* Newquery param`portal_id`

* Modifiedpath param`api_product_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Request Body

  * Schemas added: subschema #1: Gateway API Product, subschema #2: External API Product
  * Schemas deleted: subschema #1: ExternalAPIProduct, subschema #2: GatewayAPIProduct

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/api\_products/{api\_product\_id}/notification\_histories

* Tags changed from 'API Product' to 'Provider Portal - API Product'

* Newquery param`portal_id`

* Modifiedpath param`api_product_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: contact\_point\_id
  * Example changed from null to '6c97bc5f-3356-41f5-894c-c88df5389bd2'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/api\_products/{api\_product\_id}/subscriptions

* Tags changed from 'API Product' to 'Provider Portal - API Product'

* Newquery param`portal_id`

* Modifiedpath param`api_product_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: labels

  * Type changed from 'object' to 'string'
  * Example changed from null to 'labels%5Bversion%5D=v2'
  * AdditionalProperties changed
    * Schema deleted

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

DELETE/api/api\_products/{api\_product\_id}/subscriptions/{subscription\_id}

* Tags changed from 'API Product' to 'Provider Portal - API Product'

* Newquery param`portal_id`

* Modifiedpath param`api_product_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modifiedpath param`subscription_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/approvals

* Modified query param: result
  * New enum values: \[cancelled]

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/approvals/{approval\_id}/accept

* Modifiedpath param`approval_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/approvals/{approval\_id}/reject

* Modifiedpath param`approval_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/audit\_logs

* Modified query param: event\_type
  * Example changed from null to 'AddConsumerCredential'

* Responses

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/audit\_logs/event\_types

* Responses

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/audit\_logs/export

* Modified query param: event\_type
  * Example changed from null to 'AddConsumerCredential'

GET/api/contact\_points

* Modified query param: labels

  * Type changed from 'object' to 'string'
  * Example changed from null to 'labels%5Bversion%5D=v2'
  * AdditionalProperties changed
    * Schema deleted

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/contact\_points

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

DELETE/api/contact\_points/{contact\_point\_id}

* Modifiedpath param`contact_point_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'
  * MinLength changed from 0 to 1
  * MaxLength changed from null to 256
  * Pattern changed from '' to '^\[a-zA-Z0-9-\_.]+$'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/contact\_points/{contact\_point\_id}

* Modifiedpath param`contact_point_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'
  * MinLength changed from 0 to 1
  * MaxLength changed from null to 256
  * Pattern changed from '' to '^\[a-zA-Z0-9-\_.]+$'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/contact\_points/{contact\_point\_id}

* Modifiedpath param`contact_point_id`Breaking

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'
  * MinLength changed from 0 to 1
  * MaxLength changed from null to 256
  * Pattern changed from '' to '^\[a-zA-Z0-9-\_.]+$'

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/contact\_points/{contact\_point\_id}/notification\_logs

* Modifiedpath param`contact_point_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'
  * MinLength changed from 0 to 1
  * MaxLength changed from null to 256
  * Pattern changed from '' to '^\[a-zA-Z0-9-\_.]+$'

* Modified query param: status
  * New enum values: \[success failed]

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/contact\_points/{contact\_point\_id}/usages

* Modifiedpath param`contact_point_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'
  * MinLength changed from 0 to 1
  * MaxLength changed from null to 256
  * Pattern changed from '' to '^\[a-zA-Z0-9-\_.]+$'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/control\_plane/prometheus/{prometheus\_path}

* Modifiedpath param`prometheus_path`

  * Property 'AnyOf' changed
    * Schemas added: subschema #1: Fixed Endpoints, subschema #2: Dynamic Label Values Endpoint
  * Example changed from 'api/v1/query\_range?query=xxx\&start=1684722195\&end=1684723995\&step=15' to null

* Responses

  * New response: 400
  * Deleted response: default
  * Modified response: 200
    * Deletedproperty`warning_msg`

POST/api/control\_plane/prometheus/{prometheus\_path}

* Modifiedpath param`prometheus_path`

  * Property 'AnyOf' changed
    * Schemas added: subschema #1: Fixed Endpoints, subschema #2: Dynamic Label Values Endpoint
  * Example changed from 'api/v1/query\_range?query=xxx\&start=1684722195\&end=1684723995\&step=15' to null

* Responses

  * New response: 400
  * Deleted response: default
  * Modified response: 200
    * Deletedproperty`warning_msg`

GET/api/custom\_plugins

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

POST/api/custom\_plugins

* Request Body

  * Schemas added: subschema #1: Plugin Source Code, subschema #2: Plugin File

  * Schemas deleted: subschema #1, subschema #2

  * Deletedproperty`file`

  * Deletedproperty`source_code`

  * Modifiedproperty`author`

    * Example changed from null to 'plugindev'

  * Modifiedproperty`catalog`

    * Example changed from null to 'General'

  * Modifiedproperty`description`

    * Example changed from null to 'This plugin records the matched routeâs ID into an Nginx variable ($route\_id) for use in logging and monitoring.'

  * Modifiedproperty`documentation_link`

    * Example changed from 'https\://docs.api7.ai/hub/graphql-limit-count' to 'https\://docs.api7.ai/hub/route-id-register'

  * Modifiedproperty`gateway_groups`

    * Items changed

      * Example changed from null to 'bc1b95c9-b348-4832-acc3-e257d2342df1'
      * MinLength changed from 0 to 1
      * MaxLength changed from null to 256
      * Pattern changed from '' to '^\[a-zA-Z0-9-\_.]+$'

  * Modifiedproperty`logo`

    * Example changed from null to 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAH4SURBVHgBrVVLUhsxEH3SaBJSxJQWLLJKzAkClcqCVcINkhuYk6RygnCDkBOYI3iXTVKQE9ipggIGKKb42TAjNWrbY0+BkcY2b6ceqV/3688Ac6CrF+r/tfzmuyMxI25rL75klO+exDbFcxP0luItAjXbKteSsOe7qzAFWBJpbZOIVhNlkAkgyvHP96ZyBiyJMGaXnd8JQhJZgNBZSzGfRKS1LiRxR822dpwPPgq/PAyvRCzJnb1pukhXC9uZi5ylGfgPEzyZQbcWNwpJChtLcxyZ8WOaMYPua/XZRffzoT1xzq0Yn3vGX+B+EJOMr67yFkXZivO1XdjOnTRpROVr6XqKDmYh6JO4xy8vs00mMpJ2kpI0QwTl8RKUiZSlX+9yhcWSPqIiQaVBEyQ/Lbi2X7EK19LiULlOArWqvK00aC7wUSctWom3WcQZNH6/QT30VqACerX4HMMhY+yrfFxwgW3H9339aHLBgwQ8bG4e2sWZu+lAPSq4m0VsfDxF66E9KJE02Uge099Bj5ynzntjknNGuMgk3hd5JqU1McReluOrbx7CRRaynwGvCd5DIzOw5Vb1RmjYghkQdxCVNuhAks0PZ9hBBXgJSEPfGqoXPxdUkGQq8NK7WFL0Zxn0dxk/MAO8GQhX4E6cTSXJVAQnsdHXBmvzSHIP3R3bZScnj8UAAAAASUVORK5CYII='

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

PUT/api/custom\_plugins/code/parse

* Request Body

  * Modifiedproperty`file`

    * Example changed from null to 'bG9jYWwgY29yZSA9IHJlcXVpcmUoImFwaXNpeC5jb3JlIikKbG9jYWwgbmd4ID0gbmd4Cgpsb2NhbCBzY2hlbWEgPSB7CiAgICB0eXBlID0gIm9iamVjdCIKfQoKbG9jYWwgcGx1Z2luX25hbWUgPSAicm91dGUtaWQtcmVnaXN0ZXIiCgpsb2NhbCBfTSA9IHsKICB2ZXJzaW9uID0gMC4yLAogIHByaW9yaXR5ID0gMSwKICBuYW1lID0gcGx1Z2luX25hbWUsCiAgc2NoZW1hID0gc2NoZW1hLAogIHNjb3BlID0gImdsb2JhbCIsCn0KCmZ1bmN0aW9uIF9NLmNoZWNrX3NjaGVtYShjb25mKQogIHJldHVybiBjb3JlLnNjaGVtYS5jaGVjayhzY2hlbWEsIGNvbmYpOwplbmQKCmZ1bmN0aW9uIF9NLmxvZyhjb25mLCBjdHgpCiAgaWYgY3R4LnZhci5yb3V0ZV9pZCB0aGVuCiAgICBuZ3gudmFyLnJvdXRlX2lkID0gY3R4LnZhci5yb3V0ZV9pZAogIGVuZAplbmQKCnJldHVybiBfTQo='

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

DELETE/api/custom\_plugins/{custom\_plugin\_id}

* Responses

  * Deleted response: 500
  * Deleted response: default
  * Modified response: 200
    * Deletedproperty`warning_msg`

GET/api/custom\_plugins/{custom\_plugin\_id}

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

PUT/api/custom\_plugins/{custom\_plugin\_id}

* Request Body

  * Schemas added: subschema #1: Plugin Source Code, subschema #2: Plugin File

  * Schemas deleted: subschema #1, subschema #2

  * Deletedproperty`file`

  * Deletedproperty`source_code`

  * Modifiedproperty`author`

    * Example changed from null to 'plugindev'

  * Modifiedproperty`catalog`

    * Example changed from null to 'General'

  * Modifiedproperty`description`

    * Example changed from null to 'This plugin records the matched routeâs ID into an Nginx variable ($route\_id) for use in logging and monitoring.'

  * Modifiedproperty`documentation_link`

    * Example changed from 'https\://docs.api7.ai/hub/graphql-limit-count' to 'https\://docs.api7.ai/hub/route-id-register'

  * Modifiedproperty`gateway_groups`

    * Items changed

      * Example changed from null to 'bc1b95c9-b348-4832-acc3-e257d2342df1'
      * MinLength changed from 0 to 1
      * MaxLength changed from null to 256
      * Pattern changed from '' to '^\[a-zA-Z0-9-\_.]+$'

  * Modifiedproperty`logo`

    * Example changed from null to 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAH4SURBVHgBrVVLUhsxEH3SaBJSxJQWLLJKzAkClcqCVcINkhuYk6RygnCDkBOYI3iXTVKQE9ipggIGKKb42TAjNWrbY0+BkcY2b6ceqV/3688Ac6CrF+r/tfzmuyMxI25rL75klO+exDbFcxP0luItAjXbKteSsOe7qzAFWBJpbZOIVhNlkAkgyvHP96ZyBiyJMGaXnd8JQhJZgNBZSzGfRKS1LiRxR822dpwPPgq/PAyvRCzJnb1pukhXC9uZi5ylGfgPEzyZQbcWNwpJChtLcxyZ8WOaMYPua/XZRffzoT1xzq0Yn3vGX+B+EJOMr67yFkXZivO1XdjOnTRpROVr6XqKDmYh6JO4xy8vs00mMpJ2kpI0QwTl8RKUiZSlX+9yhcWSPqIiQaVBEyQ/Lbi2X7EK19LiULlOArWqvK00aC7wUSctWom3WcQZNH6/QT30VqACerX4HMMhY+yrfFxwgW3H9339aHLBgwQ8bG4e2sWZu+lAPSq4m0VsfDxF66E9KJE02Uge099Bj5ynzntjknNGuMgk3hd5JqU1McReluOrbx7CRRaynwGvCd5DIzOw5Vb1RmjYghkQdxCVNuhAks0PZ9hBBXgJSEPfGqoXPxdUkGQq8NK7WFL0Zxn0dxk/MAO8GQhX4E6cTSXJVAQnsdHXBmvzSHIP3R3bZScnj8UAAAAASUVORK5CYII='

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/developers

* Newquery param`portal_id`

* Deleted query param: labels

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/developers/invites

* Newquery param`portal_id`

* Request Body

  * Modifiedproperty`name`

    * Example changed from null to 'john'

  * Modifiedproperty`password`

    * Example changed from null to 'john-safe-password'

  * Modifiedproperty`username`

    * Example changed from null to 'john'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/email\_verified

* Responses

  * Deleted response: 500
  * Deleted response: default
  * Modified response: 200
    * Deletedproperty`warning_msg`

POST/api/export/services/template

* Request Body

  * Modifiedproperty`info`

    * Modifiedproperty`description`

      * Example changed from null to 'API description.'

    * Modifiedproperty`title`

      * Example changed from null to 'Swagger Petstore'

    * Modifiedproperty`version`

      * Example changed from null to '3.0.1'

  * Modifiedproperty`servers`

    * Items changed

      * Modifiedproperty`description`

        * Example changed from null to 'Localhost test server.'

      * Modifiedproperty`url`

        * Example changed from null to 'http\://localhost:8080'

  * Modifiedproperty`service_ids`

    * Items changed
      * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/gateway\_groups

* Newquery param`name`

* Modified query param: labels

  * Type changed from 'object' to 'string'
  * Example changed from null to 'labels%5Bversion%5D=v2'
  * AdditionalProperties changed
    * Schema deleted

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

POST/api/gateway\_groups

* Request Body

  * Modifiedproperty`description`

    * Example changed from null to 'Gateway group description.'

  * Modifiedproperty`labels`

    * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

  * Modifiedproperty`name`

    * Example changed from null to 'us-west-rsc'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/gateway\_groups/count/{resource\_type}

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

DELETE/api/gateway\_groups/{gateway\_group\_id}

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

GET/api/gateway\_groups/{gateway\_group\_id}

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

PUT/api/gateway\_groups/{gateway\_group\_id}

* Request Body

  * Modifiedproperty`description`

    * Example changed from null to 'Gateway group description.'

  * Modifiedproperty`labels`

    * Example changed from null to map\[env:prod version:v2]

    * AdditionalProperties changed

      * MinLength changed from 0 to 1
      * MaxLength changed from null to 65536
      * Pattern changed from '' to '^.+$'

  * Modifiedproperty`name`

    * Example changed from null to 'us-west-rsc'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

PUT/api/gateway\_groups/{gateway\_group\_id}/admin\_key

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/gateway\_groups/{gateway\_group\_id}/ca\_certificates/exists

* Request Body

  * Modifiedproperty`cert`

    * Example changed from null to '-----BEGIN CERTIFICATE-----
      <br />
      ...
      <br />
      \-----END CERTIFICATE-----'

* Responses

  * Deleted response: 404

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/gateway\_groups/{gateway\_group\_id}/ca\_certificates/{ca\_certificate\_id}/usage

* Modifiedpath param`ca_certificate_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/gateway\_groups/{gateway\_group\_id}/certificates/exists

* Request Body

  * Modifiedproperty`cert`BreakingBreaking

    * Schemas added: subschema #1: Certificate Reference, subschema #2: Certificate Content
    * Schemas deleted: subschema #1, subschema #2
    * Type changed from '' to 'string'

* Responses

  * Deleted response: 404

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/gateway\_groups/{gateway\_group\_id}/certificates/{certificate\_id}/usage

* Modifiedpath param`certificate_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/gateway\_groups/{gateway\_group\_id}/deployment/docker

* Newquery param`dp_manager_address`

* Newquery param`validity_period`

* Deleted query param: control\_plane\_address

* Modified query param: extra\_args\[]

  * Style changed from '' to 'form'
  * Items changed
    * MinLength changed from 1 to 0
  * Example changed from null to \[a=b c=d]

* Modified query param: image
  * Example changed from null to 'api7/api7-ee-3-gateway'

* Responses

  * Deleted response: default

  * Modified response: 200
    * Modified media type: text/plain
      * Example changed from null to 'docker run -d -e API7\_CONTROL\_PLANE\_ENDPOINTS='\["https\://12.12.123.123:31344"]'
        <br />
        -e API7\_GATEWAY\_GROUP\_SHORT\_ID=tabqbdwnahkqo
        <br />
        -e API7\_CONTROL\_PLANE\_CERT="-----BEGIN CERTIFICATE-----
        <br />
        MIIBhjCCATigAwIBAgICBAAwBQYDK2VwMEQxCzAJBgNVBAYTAlVTMRMwEQYDVQQI
        <br />
        ...
        <br />
        \-----END CERTIFICATE-----"
        <br />
        -e API7\_CONTROL\_PLANE\_KEY="-----BEGIN PRIVATE KEY-----
        <br />
        MC4CAQAwBQYDK2VwBCIEIG1Q/eJDdTZ4krnd7ezprKcZ2ASeTSrhpWglMzh9d0Hs
        <br />
        \-----END PRIVATE KEY-----"
        <br />
        -e API7\_CONTROL\_PLANE\_CA="-----BEGIN CERTIFICATE-----
        <br />
        MIIBdTCCASegAwIBAgIQVXqTFu/hH4caZptKdGp04zAFBgMrZXAwRDELMAkGA1UE
        <br />
        ...
        <br />
        \-----END CERTIFICATE-----"
        <br />
        -e API7\_CONTROL\_PLANE\_SNI="api7ee3-dp-manager"
        <br />
        -p 9080:9080
        <br />
        -p 9443:9443
        <br />
        api7/api7-ee-3-gateway:latest
        <br />
        '

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/gateway\_groups/{gateway\_group\_id}/deployment/helm/script

* Newquery param`dp_manager_address`

* Newquery param`validity_period`

* Deleted query param: control\_plane\_address

* Modified query param: cpu\_limit
  * Example changed from null to '6'

* Modified query param: extra\_values\[]

  * Style changed from '' to 'form'
  * Explode changed from null to true
  * Example changed from null to \[a=b c=d]

* Modified query param: memory\_limit
  * Example changed from null to '6Gi'

* Modified query param: workers
  * Example changed from null to 5

* Responses

  * Deleted response: default

  * Modified response: 200
    * Modified media type: text/plain
      * Example changed from null to 'helm repo add api7<https://charts.api7.ai>
        <br />
        helm repo update
        <br />
        cat > /tmp/tls.crt <\<EOF
        <br />
        \-----BEGIN CERTIFICATE-----
        <br />
        MIIBhjCCATigAwIBAgICBAAwBQYDK2VwMEQxCzAJBgNVBAYTAlVTMRMwEQYDVQQI
        <br />
        ...
        <br />
        \-----END CERTIFICATE-----
        <br />
        EOF
        <br />
        cat > /tmp/tls.key <\<EOF
        <br />
        \-----BEGIN PRIVATE KEY-----
        <br />
        MC4CAQAwBQ...AuNANhyrM9qUepu5ZGtVgXnX
        <br />
        \-----END PRIVATE KEY-----
        <br />
        EOF
        <br />
        cat > /tmp/ca.crt <\<EOF
        <br />
        \-----BEGIN CERTIFICATE-----
        <br />
        MIIBdTCCASegAwIBAgIQVXqTFu/hH4caZptKdGp04zAFBgMrZXAwRDELMAkGA1UE
        <br />
        ...
        <br />
        \-----END CERTIFICATE-----
        <br />
        \-----BEGIN CERTIFICATE-----
        <br />
        MIIBeDCCASqgAwIBAgIRAPNxgFOmSXOwtIdZOgynsLswBQYDK2VwMEQxCzAJBgNV
        <br />
        ...
        <br />
        \-----END CERTIFICATE-----
        <br />
        EOF
        <br />
        kubectl create namespace default --dry-run=client -o yaml | kubectl apply -f -
        <br />
        kubectl create secret generic -n default name-tls --from-file=tls.crt=/tmp/tls.crt --from-file=tls.key=/tmp/tls.key --from-file=ca.crt=/tmp/ca.crt
        <br />
        helm upgrade --install -n default --create-namespace name api7/gateway
        <br />
        \--set "etcd.auth.tls.enabled=true"
        <br />
        \--set "etcd.auth.tls.existingSecret=name-tls"
        <br />
        \--set "etcd.auth.tls.certFilename=tls.crt"
        <br />
        \--set "etcd.auth.tls.certKeyFilename=tls.key"
        <br />
        \--set "etcd.auth.tls.sni=api7ee3-dp-manager"
        <br />
        \--set "etcd.auth.tls.verify=true"
        <br />
        \--set "gateway.tls.existingCASecret=name-tls"
        <br />
        \--set "gateway.tls.certCAFilename=ca.crt"
        <br />
        \--set "apisix.extraEnvVars\[0].name=API7\_GATEWAY\_GROUP\_SHORT\_ID"
        <br />
        \--set "apisix.extraEnvVars\[0].value=tabqbdwnahkqo"
        <br />
        \--set "etcd.host\[0]=https\://12.12.123.123:31344"
        <br />
        \--set "apisix.resources.limits.cpu=4"
        <br />
        \--set "apisix.resources.limits.memory=7168Mi"
        <br />
        \--set "apisix.replicaCount=1"
        <br />
        \--set "apisix.image.repository=api7/api7-ee-3-gateway"
        <br />
        \--set "apisix.image.tag=latest"
        <br />
        '

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/gateway\_groups/{gateway\_group\_id}/deployment/helm/yaml

* Newquery param`dp_manager_address`

* Newquery param`validity_period`

* Deleted query param: control\_plane\_address

* Modified query param: cpu\_limit
  * Example changed from null to '6'

* Modified query param: memory\_limit
  * Example changed from null to '6Gi'

* Modified query param: workers
  * Example changed from null to 5

* Responses

  * Deleted response: default
  * Modified response: 200
    * Modified media type: text/plain
      * Example changed from null to 'apiVersion: v1
        <br />
        data:
        <br />
        tls.crt: LS0tLS1CRUdJTiB...
        <br />
        tls.key: LS0tLS1CRUdJTiB...
        <br />
        ca.crt: LS0tLS1CRUdJTiB...
        <br />
        kind: Secret
        <br />
        metadata:
        <br />
        name: name-tls
        <br />
        namespace: default
        <br />
        type: kubernetes.io/tls

GET/api/audit\_logs/config

GET/api/cas/{login\_option\_id}/login

GET/api/cas/{login\_option\_id}/logout

GET/api/dcr\_providers

POST/api/dcr\_providers

DELETE/api/dcr\_providers/{dcr\_provider\_id}

GET/api/dcr\_providers/{dcr\_provider\_id}

PUT/api/dcr\_providers/{dcr\_provider\_id}

DELETE/api/developers/{developer\_id}

GET/api/gateway\_groups/{gateway\_group\_id}/admin\_key

GET/api/gateway\_groups/{gateway\_group\_id}/deployment/docker-compose

GET/api/gateway\_groups/{gateway\_group\_id}/ingress/script

GET/api/gateway\_groups/{gateway\_group\_id}/ingress/step1

GET/api/portals

POST/api/portals

DELETE/api/portals/{portal\_id}

GET/api/portals/{portal\_id}

PUT/api/portals/{portal\_id}

GET/apisix/admin/protos

POST/apisix/admin/protos

DELETE/apisix/admin/protos/{proto\_id}

GET/apisix/admin/protos/{proto\_id}

PUT/apisix/admin/protos/{proto\_id}

DELETE/apisix/admin/secret\_providers/{secret\_provider}/{secret\_provider\_id}

GET/apisix/admin/secret\_providers/{secret\_provider}/{secret\_provider\_id}

PUT /apisix/admin/secret\_providers/{secret\_provider}/{secret\_provider\_id}GET/api/dataplane/consumer\_query

GET/api/dataplane/developer\_query

POST/api/dataplane/healthcheck

POST/api/dataplane/heartbeat

POST/api/dataplane/metrics

POST/api/dataplane/service\_registry\_healthcheck

DELETE/apisix/admin/secret\_providers/aws/{secret\_provider\_id}

GET/apisix/admin/secret\_providers/aws/{secret\_provider\_id}

PUT/apisix/admin/secret\_providers/aws/{secret\_provider\_id}

DELETE/apisix/admin/secret\_providers/kubernetes/{secret\_provider\_id}

GET/apisix/admin/secret\_providers/kubernetes/{secret\_provider\_id}

PUT/apisix/admin/secret\_providers/kubernetes/{secret\_provider\_id}

DELETE/apisix/admin/secret\_providers/vault/{secret\_provider\_id}

GET/apisix/admin/secret\_providers/vault/{secret\_provider\_id}

PUT/apisix/admin/secret\_providers/vault/{secret\_provider\_id}apisix:

replicaCount: 1

image:

repository: api7/api7-ee-3-gateway

tag: dev

extraEnvVars:

* name: API7\_GATEWAY\_GROUP\_SHORT\_ID
  <br />
  value: "tabqbdwnahkqo"
  <br />
  etcd:
  <br />
  host:

* "https\://12.12.123.123:31344"
  <br />
  auth:
  <br />
  tls:
  <br />
  enabled: true
  <br />
  existingSecret: name-tls
  <br />
  certFilename: tls.crt
  <br />
  certKeyFilename: tls.key
  <br />
  sni: api7ee3-dp-manager
  <br />
  verify: true
  <br />
  gateway:
  <br />
  tls:
  <br />
  existingCASecret: name-tls
  <br />
  certCAFilename: ca.crt
  <br />
  '

* Modified response: 400

  * Newproperty`value`

  * Modifiedproperty`error_msg`

    * Example changed from null to 'error message'

POST/api/gateway\_groups/{gateway\_group\_id}/dp\_client\_certificates

* Request Body

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

POST/api/gateway\_groups/{gateway\_group\_id}/instance\_token

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/gateway\_groups/{gateway\_group\_id}/instances

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * New response: 400

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

DELETE/api/gateway\_groups/{gateway\_group\_id}/instances/{gateway\_instance\_id}

* Responses

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/gateway\_groups/{gateway\_group\_id}/secret\_providers/{secret\_manager}/{secret\_provider\_id}/usage

* Modifiedpath param`secret_manager`

  * Name changed from 'secret\_manager' to 'secret\_provider'

* Modifiedpath param`secret_provider_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'
  * Pattern changed from '' to '^\[a-zA-Z0-9-\_.]+$'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/gateway\_groups/{gateway\_group\_id}/service\_registries

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

POST/api/gateway\_groups/{gateway\_group\_id}/service\_registries

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

DELETE/api/gateway\_groups/{gateway\_group\_id}/service\_registries/{service\_registry\_id}

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

GET/api/gateway\_groups/{gateway\_group\_id}/service\_registries/{service\_registry\_id}

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

PUT/api/gateway\_groups/{gateway\_group\_id}/service\_registries/{service\_registry\_id}

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: 500
  * Deleted response: default
  * Modified response: 200
    * Deletedproperty`warning_msg`

GET/api/gateway\_groups/{gateway\_group\_id}/service\_registries/{service\_registry\_id}/connected\_services

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/gateway\_groups/{gateway\_group\_id}/service\_registries/{service\_registry\_id}/health\_check\_history

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/gateway\_groups/{gateway\_group\_id}/service\_registries/{service\_registry\_id}/kubernetes/internal\_services

* Tags changed from 'Kubernetes' to ''

* Responses

  * Deleted response: 500
  * Deleted response: default
  * Modified response: 200
    * Deletedproperty`warning_msg`

GET/api/gateway\_groups/{gateway\_group\_id}/service\_registries/{service\_registry\_id}/nacos/namespaces

* Tags changed from 'Nacos' to ''

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/gateway\_groups/{gateway\_group\_id}/service\_registries/{service\_registry\_id}/nacos/namespaces/{nacos\_namespace}/groups

* Tags changed from 'Nacos' to ''

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/gateway\_groups/{gateway\_group\_id}/service\_registries/{service\_registry\_id}/nacos/namespaces/{nacos\_namespace}/groups/{nacos\_group}/services

* Tags changed from 'Nacos' to ''

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/gateway\_groups/{gateway\_group\_id}/service\_registries/{service\_registry\_id}/nacos/namespaces/{nacos\_namespace}/groups/{nacos\_group}/services/{nacos\_service}/instances\_metadata

* Tags changed from 'Nacos' to ''

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/gateway\_groups/{gateway\_group\_id}/services

* Deleted query param: runtime\_type

* Modified query param: labels

  * Type changed from 'object' to 'string'
  * Example changed from null to 'labels%5Bversion%5D=v2'
  * AdditionalProperties changed
    * Schema deleted

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

DELETE/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

GET/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/healthcheck

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Modifiedproperty`value`

      * Example changed from map\[httpbin.com:80:map\[gateway\_instances:\[map\[created\_at:0 hostname:api7ee3-apisix-699b68db7f-cxgcw id:xxx-yyy-zzz status:healthy updated\_at:0]] healthy:1 host:httpbin.com port:80 total:1 unhealthy:0 unknown:0 updated\_at:0]] to map\[httpbin.com:80:map\[gateway\_instances:\[map\[created\_at:1.7501503e+09 hostname:api7ee3-apisix-699b68db7f-cxgcw id:xxx-yyy-zzz status:healthy updated\_at:1.750150335e+09]] healthy:1 host:httpbin.com port:80 total:1 unhealthy:0 unknown:0 updated\_at:1.750150319e+09]]

      * AdditionalProperties changed

        * Title changed from '' to 'Upstream Service'

        * Modifiedproperty`gateway_instances`

          * Items changed

            * Modifiedproperty`created_at`

              * Example changed from null to 1.742288232e+09

            * Modifiedproperty`id`

              * Example changed from 'xxx-yyy-zzz' to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

            * Modifiedproperty`updated_at`

              * Example changed from null to 1.742288235e+09

        * Modifiedproperty`updated_at`

          * Example changed from null to 1.742288235e+09

GET/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/oas

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

PUT/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/oas

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Request Body

  * Modifiedproperty`raw_openapi`

    * Example changed from null to 'Raw OpenAPI spec'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/routes

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/routes/{route\_template\_id}

* Modifiedpath param`route_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/routes/{route\_template\_id}/runtime\_configuration

* Modifiedpath param`route_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

PATCH/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/routes/{route\_template\_id}/runtime\_configuration

* Modifiedpath param`route_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Request Body

  * Items changed

    * Schemas added: subschema #1: add/replace, subschema #2: remove
    * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/runtime\_configuration

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

PATCH/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/runtime\_configuration

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Request Body

  * Items changed

    * Schemas added: subschema #1: add/replace, subschema #2: remove
    * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/stream\_routes

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/stream\_routes/{stream\_route\_template\_id}

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modifiedpath param`stream_route_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/stream\_routes/{stream\_route\_template\_id}/runtime\_configuration

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modifiedpath param`stream_route_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

PATCH/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/stream\_routes/{stream\_route\_template\_id}/runtime\_configuration

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modifiedpath param`stream_route_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Request Body

  * Items changed

    * Schemas added: subschema #1: add/replace, subschema #2: remove
    * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/versions

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/gateway\_groups/{gateway\_group\_id}/snis/{sni\_id}/usage

* Modifiedpath param`sni_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/gateway\_groups/{gateway\_group\_id}/ssls/{ssl\_id}/usage

* Modifiedpath param`ssl_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/import/services

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/import/services/template

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/instances

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * New response: 400

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/instances/cores

* Responses

  * New response: 400
  * Deleted response: default
  * Modified response: 200
    * Deletedproperty`warning_msg`

GET/api/instances/cores\_usages/export

* Responses

  * Modified response: 200

    * Modified media type: text/csv

      * Type changed from 'object' to 'string'
      * Deletedproperty`max_dp_cores`
      * Deletedproperty`time`
      * Example changed from null to 'time,max\_dp\_cores
        <br />
        1749132000,9
        <br />
        1749128400,9
        <br />
        1749124800,9
        <br />
        1749121200,9
        <br />
        1749117600,9
        <br />
        1749114000,9
        <br />
        1749110400,9
        <br />
        1749106800,17
        <br />
        1749103200,1
        <br />
        1749099600,1
        <br />
        1749096000,1
        <br />
        1749092400,1
        <br />
        1749088800,1
        <br />
        '

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/instances/count/{field}

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * New response: 400

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

POST/api/invites

* Request Body

  * Modifiedproperty`password`

    * Example changed from null to 'safe-password'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/labels/{resource\_type}

* Modifiedpath param`resource_type`

  * New enum values: \[portal dcr\_provider]

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

POST/api/ldap/{login\_option\_id}/login

* Request Body

  * Modifiedproperty`password`

    * Example changed from null to 'safe-password'

  * Modifiedproperty`username`

    * Example changed from null to 'john'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Type changed from 'object' to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

POST/api/ldap/{login\_option\_id}/logout

* Responses

  * Deleted response: 500
  * Deleted response: default
  * Modified response: 200
    * Deletedproperty`warning_msg`

GET/api/license

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/license

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/login

* Request Body

  * Modifiedproperty`password`

    * Example changed from null to 'safe-password'

  * Modifiedproperty`username`

    * Example changed from null to 'john'

* Responses

  * Deleted response: 500
  * Deleted response: default
  * Modified response: 200
    * Deletedproperty`warning_msg`

GET/api/login\_options

* Tags changed from 'System Settings, Login Option' to 'Dashbord Login Option'

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

POST/api/login\_options

* Tags changed from 'System Settings, Login Option' to 'Dashbord Login Option'

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Deletedproperty`boundary_mapping`
  * Deletedproperty`builtin_config`
  * Deletedproperty`disable`
  * Deletedproperty`ldap_config`
  * Deletedproperty`logo`
  * Deletedproperty`name`
  * Deletedproperty`oidc_config`
  * Deletedproperty`provider_type`
  * Deletedproperty`role_mapping`
  * Deletedproperty`saml_config`

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

DELETE/api/login\_options/{login\_option\_id}

* Tags changed from 'System Settings, Login Option' to 'Dashbord Login Option'

* Responses

  * Deleted response: 500
  * Deleted response: default
  * Modified response: 200
    * Deletedproperty`warning_msg`

GET/api/login\_options/{login\_option\_id}

* Tags changed from 'System Settings, Login Option' to 'Dashbord Login Option'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

PATCH/api/login\_options/{login\_option\_id}

* Tags changed from 'System Settings, Login Option' to 'Dashbord Login Option'

* Request Body

  * Items changed

    * Schemas added: subschema #1: add/replace, subschema #2: remove
    * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

PUT/api/login\_options/{login\_option\_id}

* Tags changed from 'Login Option, System Settings' to 'Dashbord Login Option'

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Deletedproperty`boundary_mapping`
  * Deletedproperty`builtin_config`
  * Deletedproperty`disable`
  * Deletedproperty`ldap_config`
  * Deletedproperty`logo`
  * Deletedproperty`name`
  * Deletedproperty`oidc_config`
  * Deletedproperty`provider_type`
  * Deletedproperty`role_mapping`
  * Deletedproperty`saml_config`

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/login\_options\_for\_login

* Tags changed from 'Login Option, System Settings' to 'Dashbord Login Option'

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

POST/api/logout

* Responses

  * Deleted response: 500
  * Deleted response: default
  * Modified response: 200
    * Deletedproperty`warning_msg`

GET/api/me

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

PUT/api/me

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

DELETE/api/me/email

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

PUT/api/me/email

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

GET/api/oidc/{login\_option\_id}/callback

* Responses

  * Deleted response: 500
  * Deleted response: default

GET/api/oidc/{login\_option\_id}/login

* Responses

  * Deleted response: 500
  * Deleted response: default

GET/api/oidc/{login\_option\_id}/logout

* Responses

  * Deleted response: 500
  * Deleted response: default

PUT/api/openapi/convert

* Request Body

  * Modifiedproperty`raw_openapi`

    * Example changed from null to 'Raw OpenAPI spec'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/openapi/request\_body\_schema

* Modified query param: path
  * Example changed from 'GET' to '/apisix/admin/consumers'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/parse\_certificate

* Request Body

  * Modifiedproperty`cert`

    * Example changed from null to '-----BEGIN CERTIFICATE-----
      <br />
      ...
      <br />
      \-----END CERTIFICATE-----'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/password

* Request Body

  * Modifiedproperty`new_password`

    * Example changed from null to 'new-password'

  * Modifiedproperty`old_password`

    * Example changed from null to 'old-password'

* Responses

  * Deleted response: 500

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

GET/api/permission\_policies

* Modified query param: labels

  * Type changed from 'object' to 'string'
  * Example changed from null to 'labels%5Bversion%5D=v2'
  * AdditionalProperties changed
    * Schema deleted

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

POST/api/permission\_policies

* Request Body

  * Modifiedproperty`desc`

    * Example changed from null to 'Object description.'

  * Modifiedproperty`labels`

    * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

  * Modifiedproperty`name`

    * Example changed from null to 'sample-policy'

  * Modifiedproperty`policy_document`

    * Modifiedproperty`statement`

      * Items changed

        * Modifiedproperty`conditions`Breaking

          * Property 'AnyOf' changed

            * Schemas added: subschema #1: Condition for Gateway Group, subschema #2: Condition for Service, subschema #3: Condition for Permission Policy, subschema #4: Condition for Published Service, subschema #5: Condition for Role, subschema #6: Condition for User, subschema #7: Condition for Consumer, subschema #8: Condition for Secret, subschema #9: Condition for Contact Point, subschema #10: Condition for Alert Policy, subschema #11: Condition for Developer, subschema #12: Condition for API Product, subschema #13: Condition for CA Certificate, subschema #14: Condition for Certificate, subschema #15: Condition for SNI, subschema #16: Condition for Portal
            * Schemas deleted: subschema #1: ConditionForGatewayGroup, subschema #2: ConditionForService, subschema #3: ConditionForPermissionPolicy, subschema #4: ConditionForPublishedService, subschema #5: ConditionForRole, subschema #6: ConditionForUser, subschema #7: ConditionForConsumer, subschema #8: ConditionForSecret, subschema #9: ConditionForContactPoint, subschema #10: ConditionForAlertPolicy, subschema #11: ConditionForDeveloper, subschema #12: ConditionForAPIProduct, subschema #13: ConditionForCaCertificate, subschema #14: ConditionForCertificate, subschema #15: ConditionForSNI

  * Modifiedproperty`type`

    * New enum values: \[built\_in custom]

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

DELETE/api/permission\_policies/{permission\_policy\_id}

* Responses

  * Deleted response: default

  * Modified response: 200
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/permission\_policies/{permission\_policy\_id}

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

PUT/api/permission\_policies/{permission\_policy\_id}

* Request Body

  * Modifiedproperty`desc`

    * Example changed from null to 'Object description.'

  * Modifiedproperty`labels`

    * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

  * Modifiedproperty`name`

    * Example changed from null to 'sample-policy'

  * Modifiedproperty`policy_document`

    * Modifiedproperty`statement`

      * Items changed

        * Modifiedproperty`conditions`Breaking

          * Property 'AnyOf' changed

            * Schemas added: subschema #1: Condition for Gateway Group, subschema #2: Condition for Service, subschema #3: Condition for Permission Policy, subschema #4: Condition for Published Service, subschema #5: Condition for Role, subschema #6: Condition for User, subschema #7: Condition for Consumer, subschema #8: Condition for Secret, subschema #9: Condition for Contact Point, subschema #10: Condition for Alert Policy, subschema #11: Condition for Developer, subschema #12: Condition for API Product, subschema #13: Condition for CA Certificate, subschema #14: Condition for Certificate, subschema #15: Condition for SNI, subschema #16: Condition for Portal
            * Schemas deleted: subschema #1: ConditionForGatewayGroup, subschema #2: ConditionForService, subschema #3: ConditionForPermissionPolicy, subschema #4: ConditionForPublishedService, subschema #5: ConditionForRole, subschema #6: ConditionForUser, subschema #7: ConditionForConsumer, subschema #8: ConditionForSecret, subschema #9: ConditionForContactPoint, subschema #10: ConditionForAlertPolicy, subschema #11: ConditionForDeveloper, subschema #12: ConditionForAPIProduct, subschema #13: ConditionForCaCertificate, subschema #14: ConditionForCertificate, subschema #15: ConditionForSNI

  * Modifiedproperty`type`

    * New enum values: \[built\_in custom]

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/permission\_policies/{permission\_policy\_id}/references

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/plugins

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/plugins/catalogs

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/plugins/{plugin\_name}/usage

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/portal/login\_options

* Tags changed from 'Developer Login Settings' to 'Developer Portal Settings'

* Newquery param`portal_id`

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

POST/api/portal/login\_options

* Tags changed from 'Developer Login Settings' to 'Developer Portal Settings'

* Newquery param`portal_id`

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Deletedproperty`builtin_config`
  * Deletedproperty`disable`
  * Deletedproperty`ldap_config`
  * Deletedproperty`logo`
  * Deletedproperty`name`
  * Deletedproperty`oidc_config`
  * Deletedproperty`provider_type`
  * Deletedproperty`saml_config`

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

DELETE/api/portal/login\_options/{login\_option\_id}

* Tags changed from 'Developer Login Settings' to 'Developer Portal Settings'

* Newquery param`portal_id`

* Responses

  * Deleted response: 500
  * Deleted response: default
  * Modified response: 200
    * Deletedproperty`warning_msg`

GET/api/portal/login\_options/{login\_option\_id}

* Tags changed from 'Developer Login Settings' to 'Developer Portal Settings'

* Newquery param`portal_id`

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

PATCH/api/portal/login\_options/{login\_option\_id}

* Tags changed from 'Developer Login Settings' to 'Developer Portal Settings'

* Newquery param`portal_id`

* Request Body

  * Items changed

    * Schemas added: subschema #1: add/replace, subschema #2: remove
    * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

PUT/api/portal/login\_options/{login\_option\_id}

* Tags changed from 'Developer Login Settings' to 'Developer Portal Settings'

* Newquery param`portal_id`

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Deletedproperty`builtin_config`
  * Deletedproperty`disable`
  * Deletedproperty`ldap_config`
  * Deletedproperty`logo`
  * Deletedproperty`name`
  * Deletedproperty`oidc_config`
  * Deletedproperty`provider_type`
  * Deletedproperty`saml_config`

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/portal/monitor/query

* Newquery param`limit`

* Newquery param`portal_id`

* Newquery param`query`

* Newquery param`time`

* Newquery param`timeout`

* Responses

  * New response: 400
  * Deleted response: default
  * Modified response: 200
    * Deletedproperty`warning_msg`

GET/api/portal/monitor/query\_range

* Newquery param`end`

* Newquery param`limit`

* Newquery param`portal_id`

* Newquery param`query`

* Newquery param`start`

* Newquery param`step`

* Newquery param`timeout`

* Responses

  * New response: 400
  * Deleted response: default
  * Modified response: 200
    * Deletedproperty`warning_msg`

GET/api/portal/system\_settings/public\_access

* Tags changed from 'Developer Login Settings' to 'Developer Portal Settings'

* Newquery param`portal_id`

* Responses

  * Deleted response: default

  * Modified response: 200
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/portal/system\_settings/public\_access

* Tags changed from 'Developer Login Settings' to 'Developer Portal Settings'

* Newquery param`portal_id`

* Responses

  * Deleted response: default

  * Modified response: 200
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/portal/system\_settings/scim

* Tags changed from 'Developer Login Settings' to 'Developer Portal Settings'

* Newquery param`portal_id`

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/portal/system\_settings/scim

* Tags changed from 'Developer Login Settings' to 'Developer Portal Settings'

* Newquery param`portal_id`

* Request Body

  * Schemas added: subschema #1
  * Type changed from 'object' to ''
  * AdditionalProperties changed from false to null
  * Deletedproperty`enable_scim`

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/portal/system\_settings/scim/token

* Tags changed from 'Developer Login Settings' to 'Developer Portal Settings'

* Newquery param`portal_id`

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/resource\_names

* Request Body

  * Schemas added: subschema #1: Gateway Groups / Contact Points, subschema #2: Resources in a Gateway Group
  * Schemas deleted: subschema #1: NormalResource, subschema #2: GatewayGroupResource

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Deletedproperty`warning_msg`
    * Example changed from null to map\[value:map\[b5f57bda-b52b-41f6-9a30-a4c6442a3a74:gateway-group-1 f6ef6104-32a3-4382-a4b8-07cc17c466d8:gateway-group-2]]

GET/api/roles

* Modified query param: labels

  * Type changed from 'object' to 'string'
  * Example changed from null to 'labels%5Bversion%5D=v2'
  * AdditionalProperties changed
    * Schema deleted

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

POST/api/roles

* Request Body

  * Modifiedproperty`desc`

    * Example changed from null to 'This role allows users to view comsumers.'

  * Modifiedproperty`labels`

    * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

  * Modifiedproperty`name`

    * Example changed from null to 'View Consumer'

  * Modifiedproperty`policies`

    * Items changed
      * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

DELETE/api/roles/{role\_id}

* Modifiedpath param`role_id`

  * Example changed from null to '4b9b56d1-147e-49ef-bcaa-88cc5bcf403f'

* Responses

  * Deleted response: default

  * Modified response: 200
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/roles/{role\_id}

* Modifiedpath param`role_id`

  * Example changed from null to '4b9b56d1-147e-49ef-bcaa-88cc5bcf403f'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

PUT/api/roles/{role\_id}

* Modifiedpath param`role_id`

  * Example changed from null to '4b9b56d1-147e-49ef-bcaa-88cc5bcf403f'

* Request Body

  * Modifiedproperty`desc`

    * Example changed from null to 'This role allows users to view comsumers.'

  * Modifiedproperty`labels`

    * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

  * Modifiedproperty`name`

    * Example changed from null to 'View Consumer'

  * Modifiedproperty`policies`

    * Items changed
      * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/roles/{role\_id}/attach\_permission\_policies

* Modifiedpath param`role_id`

  * Example changed from null to '4b9b56d1-147e-49ef-bcaa-88cc5bcf403f'

* Request Body

  * Items changed
    * Example changed from null to 'efd3bcc7-b61a-47ec-942b-b36bf249f1da'

* Responses

  * Deleted response: default

  * Modified response: 200
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/roles/{role\_id}/detach\_permission\_policies

* Modifiedpath param`role_id`

  * Example changed from null to '4b9b56d1-147e-49ef-bcaa-88cc5bcf403f'

* Request Body

  * Items changed
    * Example changed from null to 'efd3bcc7-b61a-47ec-942b-b36bf249f1da'

* Responses

  * Deleted response: default

  * Modified response: 200
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/roles/{role\_id}/permission\_policies

* Modifiedpath param`role_id`

  * Example changed from null to '4b9b56d1-147e-49ef-bcaa-88cc5bcf403f'

* Modified query param: labels

  * Type changed from 'object' to 'string'
  * Example changed from null to 'labels%5Bversion%5D=v2'
  * AdditionalProperties changed
    * Schema deleted

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/routes/template

* Modified query param: labels

  * Type changed from 'object' to 'string'
  * Example changed from null to 'labels%5Bversion%5D=v2'
  * AdditionalProperties changed
    * Schema deleted

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Modified query param: service\_id
  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/routes/template

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

DELETE/api/routes/template/{route\_template\_id}

* Modifiedpath param`route_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * New response: 401

  * New response: 404

  * Deleted response: 400

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

GET/api/routes/template/{route\_template\_id}

* Modifiedpath param`route_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PATCH/api/routes/template/{route\_template\_id}

* Modifiedpath param`route_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Request Body

  * Items changed

    * Schemas added: subschema #1: add/replace, subschema #2: remove
    * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/routes/template/{route\_template\_id}

* Modifiedpath param`route_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/saml/{login\_option\_id}/acs

* Responses

  * Deleted response: 500
  * Deleted response: default

GET/api/saml/{login\_option\_id}/login

* Responses

  * Deleted response: 500
  * Deleted response: default

GET/api/saml/{login\_option\_id}/logout

* Responses

  * Deleted response: 500
  * Deleted response: default

GET/api/saml/{login\_option\_id}/metadata

* Responses

  * Deleted response: 500
  * Deleted response: default

GET/api/saml/{login\_option\_id}/slo

* Responses

  * Deleted response: 500
  * Deleted response: default

POST/api/saml/{login\_option\_id}/slo

* Responses

  * Deleted response: 500
  * Deleted response: default

GET/api/schema/core

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/service\_versions/{service\_version\_id}

* Modifiedpath param`service_version_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/service\_versions/{service\_version\_id}/oas

* Modifiedpath param`service_version_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/service\_versions/{service\_version\_id}/routes

* Modifiedpath param`service_version_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/service\_versions/{service\_version\_id}/routes/{route\_version\_id}

* Modifiedpath param`route_version_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modifiedpath param`service_version_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/service\_versions/{service\_version\_id}/stream\_routes

* Modifiedpath param`service_version_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/service\_versions/{service\_version\_id}/stream\_routes/{stream\_route\_version\_id}

* Modifiedpath param`service_version_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modifiedpath param`stream_route_version_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

POST/api/services/conflict\_check

* Request Body

  * Modifiedproperty`gateway_group_id`

    * Example changed from null to 'bc1b95c9-b348-4832-acc3-e257d2342df1'

  * Modifiedproperty`services`

    * Items changed

      * Schemas added: subschema #1, subschema #2
      * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/services/publish

* Request Body

  * Modifiedproperty`gateway_group_id`

    * Example changed from null to 'bc1b95c9-b348-4832-acc3-e257d2342df1'

  * Modifiedproperty`services`

    * Items changed

      * Modifiedproperty`service_id`

        * Example changed from null to 'b32e678e-7f6b-4a50-b113-550621ed4c01'

      * Modifiedproperty`service_version_id`

        * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/services/template

* Modified query param: labels

  * Type changed from 'object' to 'string'
  * Example changed from null to 'labels%5Bversion%5D=v2'
  * AdditionalProperties changed
    * Schema deleted

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/services/template

* Request Body

  * Modifiedproperty`desc`

    * Example changed from null to 'Object description.'

  * Modifiedproperty`labels`

    * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

  * Modifiedproperty`name`

    * Example changed from null to 'us-west-rsc'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

DELETE/api/services/template/{service\_template\_id}

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/services/template/{service\_template\_id}

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PATCH/api/services/template/{service\_template\_id}

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Request Body

  * Items changed

    * Schemas added: subschema #1: add/replace, subschema #2: remove
    * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/services/template/{service\_template\_id}

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Request Body

  * Modifiedproperty`desc`

    * Example changed from null to 'Object description.'

  * Modifiedproperty`labels`

    * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

  * Modifiedproperty`name`

    * Example changed from null to 'us-west-rsc'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/services/template/{service\_template\_id}/oas

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/services/template/{service\_template\_id}/oas

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Request Body

  * Modifiedproperty`raw_openapi`

    * Example changed from null to 'Raw OpenAPI spec'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/services/{service\_template\_id}/published\_services

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/services/{service\_template\_id}/versions/{version}

* Modifiedpath param`service_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/api/stream\_routes/template

* Modified query param: labels

  * Type changed from 'object' to 'string'
  * Example changed from null to 'labels%5Bversion%5D=v2'
  * AdditionalProperties changed
    * Schema deleted

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Modified query param: service\_id
  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/stream\_routes/template

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

DELETE/api/stream\_routes/template/{stream\_route\_template\_id}

* Modifiedpath param`stream_route_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/stream\_routes/template/{stream\_route\_template\_id}

* Modifiedpath param`stream_route_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/stream\_routes/template/{stream\_route\_template\_id}

* Modifiedpath param`stream_route_template_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/system\_infos

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/system\_settings

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/system\_settings

* Request Body

  * Newproperty`admin_api_address`
  * Newproperty`dp_manager_address`
  * Newproperty`source`
  * Deletedproperty`control_plane_address`

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/system\_settings/scim

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/system\_settings/scim

* Request Body

  * Schemas added: subschema #1
  * Type changed from 'object' to ''
  * AdditionalProperties changed from false to null
  * Deletedproperty`enable_scim`

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/system\_settings/scim/token

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/system\_settings/smtp\_server

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/system\_settings/smtp\_server

* Request Body

  * Modifiedproperty`address`

    * Example changed from null to 'smtp.example.com:587'

  * Modifiedproperty`from_address`

    * Example changed from null to 'sender\@example.com'

  * Modifiedproperty`from_name`

    * Example changed from null to 'John Doe'

  * Modifiedproperty`password`

    * Example changed from null to 'secretpassword123'

  * Modifiedproperty`username`

    * Example changed from null to 'smtp-user\@example.com'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/system\_settings/smtp\_server\_status

* Responses

  * Deleted response: default

  * Modified response: 200
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/tokens

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/api/tokens

* Request Body

  * Modifiedproperty`expires_at`

    * Example changed from null to 1.752288235e+09

  * Modifiedproperty`name`

    * Example changed from null to 'test-token'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

DELETE/api/tokens/{token\_id}

* Modifiedpath param`token_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/tokens/{token\_id}

* Modifiedpath param`token_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/tokens/{token\_id}

* Modifiedpath param`token_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Request Body

  * Modifiedproperty`name`

    * Example changed from null to 'test-token'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/tokens/{token\_id}/regenerate

* Modifiedpath param`token_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Request Body

  * Modifiedproperty`expires_at`

    * Example changed from null to 1.752288235e+09

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/users

* Deleted query param: login\_option\_name

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

DELETE/api/users/{user\_id}

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

GET/api/users/{user\_id}

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

PUT/api/users/{user\_id}

* Request Body

  * Modifiedproperty`labels`

    * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

PUT/api/users/{user\_id}/assigned\_roles

* Request Body

  * Modifiedproperty`roles`

    * Items changed
      * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: 500

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

PUT/api/users/{user\_id}/boundaries

* Request Body

  * Items changed
    * Example changed from null to 'efd3bcc7-b61a-47ec-942b-b36bf249f1da'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/api/users/{user\_id}/password\_reset

* Request Body

  * Modifiedproperty`password`

    * Example changed from null to 'safe-password'

* Responses

  * Deleted response: 500

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

PUT/api/validate\_cert\_key

* Request Body

  * Modifiedproperty`cert`

    * Example changed from null to '-----BEGIN CERTIFICATE-----
      <br />
      ...
      <br />
      \-----END CERTIFICATE-----'

  * Modifiedproperty`key`

    * Example changed from null to '-----BEGIN PRIVATE KEY-----
      <br />
      ...
      <br />
      \-----END PRIVATE KEY-----'

* Responses

  * Deleted response: default

  * Modified response: 200
    * Schemas deleted: subschema #1

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/api/verify\_email

* Responses

  * Deleted response: 500
  * Deleted response: default

GET/api/version

* Responses

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

GET/apisix/admin/ca\_certificates

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Modified query param: labels

  * Type changed from 'object' to 'string'
  * Example changed from null to 'labels%5Bversion%5D=v2'
  * AdditionalProperties changed
    * Schema deleted

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Modified query param: sni\_id
  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/apisix/admin/ca\_certificates

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Modifiedproperty`cert`

    * Example changed from null to '-----BEGIN CERTIFICATE-----
      <br />
      ...
      <br />
      \-----END CERTIFICATE-----'

  * Modifiedproperty`desc`

    * Example changed from null to 'Object description.'

  * Modifiedproperty`labels`

    * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

  * Modifiedproperty`name`

    * Example changed from null to 'us-west-rsc'

* Responses

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

DELETE/apisix/admin/ca\_certificates/{ca\_certificate\_id}

* Modifiedpath param`ca_certificate_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/ca\_certificates/{ca\_certificate\_id}

* Modifiedpath param`ca_certificate_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PATCH/apisix/admin/ca\_certificates/{ca\_certificate\_id}

* Modifiedpath param`ca_certificate_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Items changed

    * Schemas added: subschema #1: add/replace, subschema #2: remove
    * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/apisix/admin/ca\_certificates/{ca\_certificate\_id}

* Modifiedpath param`ca_certificate_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Modifiedproperty`cert`

    * Example changed from null to '-----BEGIN CERTIFICATE-----
      <br />
      ...
      <br />
      \-----END CERTIFICATE-----'

  * Modifiedproperty`desc`

    * Example changed from null to 'Object description.'

  * Modifiedproperty`labels`

    * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

  * Modifiedproperty`name`

    * Example changed from null to 'us-west-rsc'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/certificates

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Modified query param: labels

  * Type changed from 'object' to 'string'
  * Example changed from null to 'labels%5Bversion%5D=v2'
  * AdditionalProperties changed
    * Schema deleted

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Modified query param: sni\_id
  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/apisix/admin/certificates

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Schemas deleted: subschema #1, subschema #2

* Responses

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

DELETE/apisix/admin/certificates/{certificate\_id}

* Modifiedpath param`certificate_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/certificates/{certificate\_id}

* Modifiedpath param`certificate_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PATCH/apisix/admin/certificates/{certificate\_id}

* Modifiedpath param`certificate_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Items changed

    * Schemas added: subschema #1: add/replace, subschema #2: remove
    * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/apisix/admin/certificates/{certificate\_id}

* Modifiedpath param`certificate_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/consumers

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Modified query param: labels

  * Type changed from 'object' to 'string'
  * Example changed from null to 'labels%5Bversion%5D=v2'
  * AdditionalProperties changed
    * Schema deleted

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/apisix/admin/consumers

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Modifiedproperty`desc`

    * Example changed from null to 'Object description.'

  * Modifiedproperty`labels`

    * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

  * Modifiedproperty`plugins`

    * Example changed from null to map\[key-auth:map\[]]

  * Modifiedproperty`username`

    * Example changed from null to 'johndoe'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

DELETE/apisix/admin/consumers/{username}

* Modifiedpath param`username`

  * Example changed from null to 'johndoe'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/consumers/{username}

* Modifiedpath param`username`

  * Example changed from null to 'johndoe'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PATCH/apisix/admin/consumers/{username}

* Modifiedpath param`username`

  * Example changed from null to 'johndoe'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Items changed

    * Schemas added: subschema #1: add/replace, subschema #2: remove
    * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/apisix/admin/consumers/{username}

* Modifiedpath param`username`

  * Example changed from null to 'johndoe'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Modifiedproperty`desc`

    * Example changed from null to 'Object description.'

  * Modifiedproperty`labels`

    * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

  * Modifiedproperty`plugins`

    * Example changed from null to map\[key-auth:map\[]]

  * Modifiedproperty`username`

    * Example changed from null to 'johndoe'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/consumers/{username}/credentials

* Modifiedpath param`username`

  * Example changed from null to 'johndoe'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Modified query param: labels

  * Type changed from 'object' to 'string'
  * Example changed from null to 'labels%5Bversion%5D=v2'
  * AdditionalProperties changed
    * Schema deleted

* Modified query param: plugin\_name
  * Example changed from null to 'us-west-rsc'

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/apisix/admin/consumers/{username}/credentials

* Modifiedpath param`username`

  * Example changed from null to 'johndoe'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Modifiedproperty`desc`

    * Example changed from null to 'Object description.'

  * Modifiedproperty`labels`

    * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

  * Modifiedproperty`name`

    * Example changed from null to 'us-west-rsc'

  * Modifiedproperty`plugins`Breaking

    * Schemas added: subschema #1: key-auth, subschema #2: basic-auth, subschema #3: hmac-auth, subschema #4: jwt-auth
    * Schemas deleted: subschema #1, subschema #2, subschema #3, subschema #4
    * AdditionalProperties changed from false to null
    * MinProps changed from 0 to 1
    * MaxProps changed from null to 1
    * Deletedproperty`basic-auth`
    * Deletedproperty`hmac-auth`
    * Deletedproperty`jwt-auth`
    * Deletedproperty`key-auth`

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

DELETE/apisix/admin/consumers/{username}/credentials/{credential\_id}

* Modifiedpath param`credential_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modifiedpath param`username`

  * Example changed from null to 'johndoe'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * New response: 401

  * New response: 404

  * Deleted response: 400

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

GET/apisix/admin/consumers/{username}/credentials/{credential\_id}

* Modifiedpath param`credential_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modifiedpath param`username`

  * Example changed from null to 'johndoe'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/apisix/admin/consumers/{username}/credentials/{credential\_id}

* Modifiedpath param`credential_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modifiedpath param`username`

  * Example changed from null to 'johndoe'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Modifiedproperty`desc`

    * Example changed from null to 'Object description.'

  * Modifiedproperty`labels`

    * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

  * Modifiedproperty`name`

    * Example changed from null to 'us-west-rsc'

  * Modifiedproperty`plugins`Breaking

    * Schemas added: subschema #1: key-auth, subschema #2: basic-auth, subschema #3: hmac-auth, subschema #4: jwt-auth
    * Schemas deleted: subschema #1, subschema #2, subschema #3, subschema #4
    * AdditionalProperties changed from false to null
    * MinProps changed from 0 to 1
    * MaxProps changed from null to 1
    * Deletedproperty`basic-auth`
    * Deletedproperty`hmac-auth`
    * Deletedproperty`jwt-auth`
    * Deletedproperty`key-auth`

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/global\_rules

* Tags changed from 'Plugin, Gateway Group' to ''

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/apisix/admin/global\_rules

* Tags changed from 'Gateway Group, Plugin' to ''

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Modifiedproperty`plugins`

    * Example changed from null to map\[key-auth:map\[]]

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

DELETE/apisix/admin/global\_rules/{global\_rule\_id}

* Tags changed from 'Gateway Group, Plugin' to ''

* Modifiedpath param`global_rule_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/global\_rules/{global\_rule\_id}

* Tags changed from 'Gateway Group, Plugin' to ''

* Modifiedpath param`global_rule_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/apisix/admin/global\_rules/{global\_rule\_id}

* Tags changed from 'Gateway Group, Plugin' to ''

* Modifiedpath param`global_rule_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Modifiedproperty`plugins`

    * Example changed from null to map\[key-auth:map\[]]

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/plugin\_metadata

* Tags changed from 'Gateway Group, Plugin' to ''

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

DELETE/apisix/admin/plugin\_metadata/{plugin\_name}

* Tags changed from 'Gateway Group, Plugin' to ''

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/plugin\_metadata/{plugin\_name}

* Tags changed from 'Plugin, Gateway Group' to ''

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Deletedproperty`warning_msg`

    * Modifiedproperty`value`

      * Example changed from null to map\[disabled\_labels:map\[status:\[code]]]

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/apisix/admin/plugin\_metadata/{plugin\_name}

* Tags changed from 'Gateway Group, Plugin' to ''

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Example changed from null to map\[disabled\_labels:map\[status:\[code]]]

* Responses

  * Deleted response: default

  * Modified response: 200

    * Deletedproperty`warning_msg`

    * Modifiedproperty`value`

      * Example changed from null to map\[disabled\_labels:map\[status:\[code]]]

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/plugin\_metadata/{plugin\_name}/default

* Tags changed from 'Plugin' to ''

* Responses

  * Deleted response: default

  * Modified response: 200

    * Deletedproperty`warning_msg`

    * Modifiedproperty`value`

      * Example changed from null to map\[]

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/plugins

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/plugins/list

* Responses

  * Modified response: 200
    * Example changed from null to \[ip-restriction limit-conn mqtt-proxy prometheus syslog]

GET/apisix/admin/plugins/{plugin\_name}

* Responses

  * Deleted response: default

  * Modified response: 200

    * Deletedproperty`warning_msg`

    * Modifiedproperty`value`

      * Example changed from null to map\[$comment:this is a mark for our injected plugin schema properties:map\[\_meta:map\[properties:map\[disable:map\[type:boolean] error\_response:map\[oneOf:\[map\[type:string] map\[type:object]]] filter:map\[description:filter determines whether the plugin needs to be executed at runtime type:array] pre\_function:map\[description:function to be executed in each phase before execution of plugins. The pre\_function will have access to two arguments:`conf`and`ctx`. type:string] priority:map\[description:priority of plugins by customized order type:integer]] type:object] prefer\_name:map\[default:false type:boolean]] type:object]

GET/apisix/admin/routes

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Modified query param: service\_id

  * Required changed from false to true
  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/apisix/admin/routes

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

DELETE/apisix/admin/routes/{route\_id}

* Modifiedpath param`route_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * New response: 401

  * New response: 404

  * Deleted response: 400

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

GET/apisix/admin/routes/{route\_id}

* Modifiedpath param`route_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PATCH/apisix/admin/routes/{route\_id}

* Modifiedpath param`route_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Items changed

    * Schemas added: subschema #1: add/replace, subschema #2: remove
    * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/apisix/admin/routes/{route\_id}

* Modifiedpath param`route_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/schema/plugins/{plugin\_name}

* Responses

  * Deleted response: default

  * Modified response: 200

    * Deletedproperty`warning_msg`

    * Modifiedproperty`value`

      * Example changed from null to map\[$comment:this is a mark for our injected plugin schema properties:map\[\_meta:map\[properties:map\[disable:map\[type:boolean] error\_response:map\[oneOf:\[map\[type:string] map\[type:object]]] filter:map\[description:filter determines whether the plugin needs to be executed at runtime type:array] pre\_function:map\[description:function to be executed in each phase before execution of plugins. The pre\_function will have access to two arguments:`conf`and`ctx`. type:string] priority:map\[description:priority of plugins by customized order type:integer]] type:object] prefer\_name:map\[default:false type:boolean]] type:object]

GET/apisix/admin/schema/{resource\_name}

* Modifiedpath param`resource_name`

  * New enum values: \[service upstream stream\_service stream\_upstream route consumer consumer\_credential global\_rule ssl vault\_secret aws\_secret kubernetes\_secret plugin\_metadata stream\_route]
  * Example changed from 'route' to 'consumer'

* Responses

  * New response: 404

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/secret\_providers

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/services

* Deleted query param: runtime\_type

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Modified query param: labels

  * Type changed from 'object' to 'string'
  * Example changed from null to 'labels%5Bversion%5D=v2'
  * AdditionalProperties changed
    * Schema deleted

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/apisix/admin/services

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Schemas added: subschema #1, subschema #2, subschema #3
  * Schemas deleted: subschema #1, subschema #2, subschema #3
  * Schemas added: subschema #1, subschema #2, subschema #3
  * Schemas deleted: subschema #1, subschema #2, subschema #3

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

DELETE/apisix/admin/services/{service\_id}

* Modifiedpath param`service_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/services/{service\_id}

* Modifiedpath param`service_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PATCH/apisix/admin/services/{service\_id}

* Modifiedpath param`service_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Items changed

    * Schemas added: subschema #1: add/replace, subschema #2: remove
    * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/apisix/admin/services/{service\_id}

* Modifiedpath param`service_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Schemas added: subschema #1, subschema #2, subschema #3
  * Schemas deleted: subschema #1, subschema #2, subschema #3
  * Schemas added: subschema #1, subschema #2, subschema #3
  * Schemas deleted: subschema #1, subschema #2, subschema #3

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/services/{service\_id}/upstreams

* Modifiedpath param`service_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/apisix/admin/services/{service\_id}/upstreams

* Modifiedpath param`service_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Schemas added: subschema #1: HTTP Upstream, subschema #2: Stream Upstream
  * Schemas deleted: subschema #1: HTTPUpstream, subschema #2: StreamUpstream

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

DELETE/apisix/admin/services/{service\_id}/upstreams/{upstream\_id}

* Modifiedpath param`service_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modifiedpath param`upstream_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/services/{service\_id}/upstreams/{upstream\_id}

* Modifiedpath param`service_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modifiedpath param`upstream_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PATCH/apisix/admin/services/{service\_id}/upstreams/{upstream\_id}

* Modifiedpath param`service_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modifiedpath param`upstream_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Items changed

    * Schemas added: subschema #1: add/replace, subschema #2: remove
    * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/apisix/admin/services/{service\_id}/upstreams/{upstream\_id}

* Modifiedpath param`service_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modifiedpath param`upstream_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Schemas added: subschema #1: HTTP Upstream, subschema #2: Stream Upstream
  * Schemas deleted: subschema #1: HTTPUpstream, subschema #2: StreamUpstream

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/snis

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Modified query param: labels

  * Type changed from 'object' to 'string'
  * Example changed from null to 'labels%5Bversion%5D=v2'
  * AdditionalProperties changed
    * Schema deleted

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/apisix/admin/snis

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Modifiedproperty`certificates`

    * Items changed

      * Schemas added: subschema #1: Certificate Reference, subschema #2: Certificate Content
      * MinLength changed from 1 to 0
      * MaxLength changed from 256 to null
      * Pattern changed from '^\[a-zA-Z0-9-\_.]+$' to ''

  * Modifiedproperty`desc`

    * Example changed from null to 'Object description.'

  * Modifiedproperty`labels`

    * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

  * Modifiedproperty`mtls`

    * Modifiedproperty`ca_certificates`

      * Items changed

        * Schemas added: subschema #1: Certificate Reference, subschema #2: Certificate Content
        * MinLength changed from 1 to 0
        * MaxLength changed from 256 to null
        * Pattern changed from '^\[a-zA-Z0-9-\_.]+$' to ''

    * Modifiedproperty`enabled`

      * Example changed from null to true

  * Modifiedproperty`name`

    * Example changed from null to 'us-west-rsc'

* Responses

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

DELETE/apisix/admin/snis/{sni\_id}

* Modifiedpath param`sni_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/snis/{sni\_id}

* Modifiedpath param`sni_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PATCH/apisix/admin/snis/{sni\_id}

* Modifiedpath param`sni_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Items changed

    * Schemas added: subschema #1: add/replace, subschema #2: remove
    * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/apisix/admin/snis/{sni\_id}

* Modifiedpath param`sni_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Modifiedproperty`certificates`

    * Items changed

      * Schemas added: subschema #1: Certificate Reference, subschema #2: Certificate Content
      * MinLength changed from 1 to 0
      * MaxLength changed from 256 to null
      * Pattern changed from '^\[a-zA-Z0-9-\_.]+$' to ''

  * Modifiedproperty`desc`

    * Example changed from null to 'Object description.'

  * Modifiedproperty`labels`

    * Example changed from map\[keyA:valueA keyB:valueB] to map\[env:prod version:v2]

  * Modifiedproperty`mtls`

    * Modifiedproperty`ca_certificates`

      * Items changed

        * Schemas added: subschema #1: Certificate Reference, subschema #2: Certificate Content
        * MinLength changed from 1 to 0
        * MaxLength changed from 256 to null
        * Pattern changed from '^\[a-zA-Z0-9-\_.]+$' to ''

    * Modifiedproperty`enabled`

      * Example changed from null to true

  * Modifiedproperty`name`

    * Example changed from null to 'us-west-rsc'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/ssls

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Modified query param: labels

  * Type changed from 'object' to 'string'
  * Example changed from null to 'labels%5Bversion%5D=v2'
  * AdditionalProperties changed
    * Schema deleted

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Modified query param: type
  * Default changed from null to 'server'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/apisix/admin/ssls

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Schemas added: subschema #1: Use Key and Cert, subschema #2: Use Keys and Certs
  * Schemas deleted: subschema #1, subschema #2
  * Schemas deleted: subschema #1, subschema #2
  * Type changed from 'object' to ''

* Responses

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

DELETE/apisix/admin/ssls/{ssl\_id}

* Modifiedpath param`ssl_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/ssls/{ssl\_id}

* Modifiedpath param`ssl_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/apisix/admin/ssls/{ssl\_id}

* Modifiedpath param`ssl_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Schemas added: subschema #1: Use Key and Cert, subschema #2: Use Keys and Certs
  * Schemas deleted: subschema #1, subschema #2
  * Schemas deleted: subschema #1, subschema #2
  * Type changed from 'object' to ''

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/stream\_routes

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Modified query param: search
  * Example changed from null to 'version%3Dv2'

* Modified query param: service\_id

  * Required changed from false to true
  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

POST/apisix/admin/stream\_routes

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

DELETE/apisix/admin/stream\_routes/{stream\_route\_id}

* Modifiedpath param`stream_route_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Type changed from 'object' to 'string'
    * Example changed from null to ''
    * Deletedproperty`value`
    * Deletedproperty`warning_msg`

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/stream\_routes/{stream\_route\_id}

* Modifiedpath param`stream_route_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

PUT/apisix/admin/stream\_routes/{stream\_route\_id}

* Modifiedpath param`stream_route_id`

  * Example changed from null to 'bd58fce2-b6cc-4d2d-a53c-6ce11b19c101'

* Modified query param: gateway\_group\_id
  * Example changed from null to '86fb9981-d9d2-4555-9df8-91ae92129335'

* Request Body

  * Schemas added: subschema #1, subschema #2
  * Schemas deleted: subschema #1, subschema #2

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

GET/apisix/admin/variables

* Responses

  * Deleted response: default

  * Modified response: 200

    * Schemas added: subschema #1, subschema #2
    * Schemas deleted: subschema #1, subschema #2

  * Modified response: 400

    * Newproperty`value`

    * Modifiedproperty`error_msg`

      * Example changed from null to 'error message'

## From 3.6.x to 3.7.x[â](#from-36x-to-37x "Direct link to From 3.6.x to 3.7.x")

### New3

DELETE/apisix/admin/secret\_providers/kubernetes/{secret\_provider\_id}

GET/apisix/admin/secret\_providers/kubernetes/{secret\_provider\_id}

PUT/apisix/admin/secret\_providers/kubernetes/{secret\_provider\_id}

### Modified600<!-- -->Breakings

Switch to `Show all` to see all changes

GET/api/api\_products

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Modifiedproperty`server_url`

          * MaxLength changed from null to 4096

POST/api/api\_products

* Request Body

  * Modifiedproperty`server_url`

    * MaxLength changed from null to 4096

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`server_url`

        * MaxLength changed from null to 4096

GET/api/api\_products/{api\_product\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`server_url`

        * MaxLength changed from null to 4096

PATCH/api/api\_products/{api\_product\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`server_url`

        * MaxLength changed from null to 4096

PUT/api/api\_products/{api\_product\_id}

* Request Body

  * Modifiedproperty`server_url`

    * MaxLength changed from null to 4096

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`server_url`

        * MaxLength changed from null to 4096

GET/api/contact\_points

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Modifiedproperty`name`

          * MinLength changed from 0 to 1
          * MaxLength changed from null to 256

POST/api/contact\_points

* Request Body

  * Modifiedproperty`name`Breaking

    * MinLength changed from 0 to 1
    * MaxLength changed from null to 256

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`Breaking

        * MinLength changed from 0 to 1
        * MaxLength changed from null to 256

GET/api/contact\_points/{contact\_point\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MinLength changed from 0 to 1
        * MaxLength changed from null to 256

PUT/api/contact\_points/{contact\_point\_id}

* Request Body

  * Modifiedproperty`name`Breaking

    * MinLength changed from 0 to 1
    * MaxLength changed from null to 256

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`Breaking

        * MinLength changed from 0 to 1
        * MaxLength changed from null to 256

POST/api/gateway\_groups/{gateway\_group\_id}/ca\_certificates/exists

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

POST/api/gateway\_groups/{gateway\_group\_id}/certificates/exists

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

GET/api/gateway\_groups/{gateway\_group\_id}/secret\_providers/{secret\_manager}/{secret\_provider\_id}/usage

* Modifiedpath param`secret_manager`

  * New enum values: \[kubernetes]

* Modifiedpath param`secret_provider_id`

  * MinLength changed from 0 to 1
  * MaxLength changed from null to 256

GET/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/stream\_routes

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Modifiedproperty`name`

          * MaxLength changed from 100 to 65536

GET/api/gateway\_groups/{gateway\_group\_id}/services/{service\_template\_id}/stream\_routes/{stream\_route\_template\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

POST/api/login\_options

* Request Body

  * Modifiedproperty`name`Breaking

    * MinLength changed from 0 to 1
    * MaxLength changed from null to 256

PUT/api/login\_options/{login\_option\_id}

* Request Body

  * Modifiedproperty`name`Breaking

    * MinLength changed from 0 to 1
    * MaxLength changed from null to 256

POST/api/portal/login\_options

* Request Body

  * Modifiedproperty`name`Breaking

    * MinLength changed from 0 to 1
    * MaxLength changed from null to 256

PUT/api/portal/login\_options/{login\_option\_id}

* Request Body

  * Modifiedproperty`name`Breaking

    * MinLength changed from 0 to 1
    * MaxLength changed from null to 256

POST/api/roles

* Request Body

  * Modifiedproperty`name`Breaking

    * MinLength changed from 0 to 1
    * MaxLength changed from null to 256

PUT/api/roles/{role\_id}

* Request Body

  * Modifiedproperty`name`Breaking

    * MinLength changed from 0 to 1
    * MaxLength changed from null to 256

POST/api/routes/template

* Request Body

  * Required changed
    * Newrequired property`service_id`Breaking

GET/api/service\_versions/{service\_version\_id}/stream\_routes

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Modifiedproperty`name`

          * MaxLength changed from 100 to 65536

GET/api/service\_versions/{service\_version\_id}/stream\_routes/{stream\_route\_version\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

POST/api/services/conflict\_check

* Request Body

  * Modifiedproperty`services`

    * Items changed

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

GET/api/stream\_routes/template

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Modifiedproperty`name`

          * MaxLength changed from 100 to 65536

POST/api/stream\_routes/template

* Request Body

  * Modifiedproperty`name`

    * MaxLength changed from 100 to 65536

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

GET/api/stream\_routes/template/{stream\_route\_template\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

PUT/api/stream\_routes/template/{stream\_route\_template\_id}

* Request Body

  * Modifiedproperty`name`

    * MaxLength changed from 100 to 65536

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

GET/api/system\_settings/smtp\_server

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`from_address`

        * Format changed from '' to 'email'

      * Modifiedproperty`from_name`

        * Pattern changed from '' to '^s\*("(?:\[^"]|.)*"|(\[^<>@]+))?s*$'

PUT/api/system\_settings/smtp\_server

* Request Body

  * Modifiedproperty`from_address`Breaking

    * Format changed from '' to 'email'

  * Modifiedproperty`from_name`

    * Pattern changed from '' to '^s\*("(?:\[^"]|.)*"|(\[^<>@]+))?s*$'

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`from_address`Breaking

        * Format changed from '' to 'email'

      * Modifiedproperty`from_name`

        * Pattern changed from '' to '^s\*("(?:\[^"]|.)*"|(\[^<>@]+))?s*$'

GET/apisix/admin/ca\_certificates

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Modifiedproperty`name`

          * MaxLength changed from 100 to 65536

POST/apisix/admin/ca\_certificates

* Request Body

  * Modifiedproperty`name`

    * MaxLength changed from 100 to 65536

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

GET/apisix/admin/ca\_certificates/{ca\_certificate\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

PATCH/apisix/admin/ca\_certificates/{ca\_certificate\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

PUT/apisix/admin/ca\_certificates/{ca\_certificate\_id}

* Request Body

  * Modifiedproperty`name`

    * MaxLength changed from 100 to 65536

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

GET/apisix/admin/certificates

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Modifiedproperty`name`

          * MaxLength changed from 100 to 65536

POST/apisix/admin/certificates

* Request Body

  * Modifiedproperty`name`

    * MaxLength changed from 100 to 65536

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

GET/apisix/admin/certificates/{certificate\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

PATCH/apisix/admin/certificates/{certificate\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

PUT/apisix/admin/certificates/{certificate\_id}

* Request Body

  * Modifiedproperty`name`

    * MaxLength changed from 100 to 65536

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

GET/apisix/admin/secret\_providers

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed
        * Schemas added: subschema #3

DELETE/apisix/admin/secret\_providers/aws/{secret\_provider\_id}

* Modifiedpath param`secret_provider_id`

  * MinLength changed from 0 to 1
  * MaxLength changed from null to 256

GET/apisix/admin/secret\_providers/aws/{secret\_provider\_id}

* Modifiedpath param`secret_provider_id`

  * MinLength changed from 0 to 1
  * MaxLength changed from null to 256

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Schemas added: subschema #3

PUT/apisix/admin/secret\_providers/aws/{secret\_provider\_id}

* Modifiedpath param`secret_provider_id`

  * MinLength changed from 0 to 1
  * MaxLength changed from null to 256

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Schemas added: subschema #3

DELETE/apisix/admin/secret\_providers/vault/{secret\_provider\_id}

* Modifiedpath param`secret_provider_id`

  * MinLength changed from 0 to 1
  * MaxLength changed from null to 256

GET/apisix/admin/secret\_providers/vault/{secret\_provider\_id}

* Modifiedpath param`secret_provider_id`

  * MinLength changed from 0 to 1
  * MaxLength changed from null to 256

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Schemas added: subschema #3

PUT/apisix/admin/secret\_providers/vault/{secret\_provider\_id}

* Modifiedpath param`secret_provider_id`

  * MinLength changed from 0 to 1
  * MaxLength changed from null to 256

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Schemas added: subschema #3

GET/apisix/admin/snis

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Modifiedproperty`name`

          * MaxLength changed from 100 to 65536

POST/apisix/admin/snis

* Request Body

  * Modifiedproperty`name`

    * MaxLength changed from 100 to 65536

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

GET/apisix/admin/snis/{sni\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

PATCH/apisix/admin/snis/{sni\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

PUT/apisix/admin/snis/{sni\_id}

* Request Body

  * Modifiedproperty`name`

    * MaxLength changed from 100 to 65536

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

GET/apisix/admin/ssls

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Modifiedproperty`name`

          * MaxLength changed from 100 to 65536

POST/apisix/admin/ssls

* Request Body

  * Modifiedproperty`name`

    * MaxLength changed from 100 to 65536

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

GET/apisix/admin/ssls/{ssl\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

PUT/apisix/admin/ssls/{ssl\_id}

* Request Body

  * Modifiedproperty`name`

    * MaxLength changed from 100 to 65536

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

GET/apisix/admin/stream\_routes

* Responses

  * Modified response: 200

    * Modifiedproperty`list`

      * Items changed

        * Modifiedproperty`name`

          * MaxLength changed from 100 to 65536

POST/apisix/admin/stream\_routes

* Request Body

  * Modifiedproperty`name`

    * MaxLength changed from 100 to 65536

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

GET/apisix/admin/stream\_routes/{stream\_route\_id}

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536

PUT/apisix/admin/stream\_routes/{stream\_route\_id}

* Request Body

  * Modifiedproperty`name`

    * MaxLength changed from 100 to 65536

* Responses

  * Modified response: 200

    * Modifiedproperty`value`

      * Modifiedproperty`name`

        * MaxLength changed from 100 to 65536
