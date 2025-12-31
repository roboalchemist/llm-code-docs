# Source: https://upstash.com/docs/devops/developer-api/redis/list_databases.md

# List Databases

> This endpoint list all databases of user.

## OpenAPI

````yaml devops/developer-api/openapi.yml get /redis/databases
paths:
  path: /redis/databases
  method: get
  servers:
    - url: https://api.upstash.com/v2
  request:
    security:
      - title: basicAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: basic
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/Database'
        examples:
          example:
            value:
              - database_id: 96ad0856-03b1-4ee7-9666-e81abd0349e1
                database_name: MyRedis
                region: global
                port: 6379
                creation_time: 1752649602
                state: active
                endpoint: beloved-stallion-58500
                tls: true
                db_max_clients: 10000
                db_max_request_size: 10485760
                db_disk_threshold: 107374182400
                db_max_entry_size: 104857600
                db_memory_threshold: 3221225472
                db_max_commands_per_second: 10000
                db_request_limit: 8024278031528737000
                type: paid
                budget: 360
                primary_region: us-east-1
                primary_members:
                  - us-east-1
                all_members:
                  - us-east-1
                eviction: false
                auto_upgrade: false
                consistent: false
                modifying_state: ''
                db_resource_size: L
                db_type: pebble
                db_conn_idle_timeout: 21600000000000
                db_lua_timeout: 250000000
                db_lua_credits_per_min: 10000000000
                db_store_max_idle: 900000000000
                db_max_loads_per_sec: 1000000
                db_acl_enabled: 'false'
                db_acl_default_user_status: 'true'
                db_eviction: false
                last_plan_upgrade_time: 0
                replicas: 5
                customer_id: example@upstash.com
                daily_backup_enabled: false
                read_regions:
                  - us-east-2
                securityAddons:
                  ipWhitelisting: false
                  vpcPeering: false
                  privateLink: false
                  tlsMutualAuth: false
                  encryptionAtRest: false
                prometheus_enabled: 'false'
                prod_pack_enabled: false
        description: OK
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/redis/list_databases
components:
  schemas:
    Database:
      type: object
      properties:
        database_id:
          type: string
          description: ID of the database
          example: 96ad0856-03b1-4ee7-9666-e81abd0349e1
        database_name:
          type: string
          description: Name of the database
          example: MyRedis
        region:
          type: string
          description: The region where database is hosted
          enum:
            - global
          example: global
        port:
          type: integer
          description: Database port for clients to connect
          format: int64
          example: 6379
        creation_time:
          type: integer
          description: Creation time of the database as Unix time
          format: int64
          example: 1752649602
        state:
          type: string
          description: State of database
          enum:
            - active
            - suspended
            - passive
          example: active
        endpoint:
          type: string
          description: >-
            Endpoint identifier or hostname of the database (may be a slug like
            "beloved-stallion-58500" or a full host)
          example: beloved-stallion-58500
        tls:
          type: boolean
          description: TLS/SSL is enabled or not
          example: true
        db_max_clients:
          type: integer
          description: >-
            Max number of concurrent clients can be opened on this database
            currently
          format: int64
          example: 10000
        db_max_request_size:
          type: integer
          description: >-
            Max size of a request that will be accepted by the database
            currently(in bytes)
          format: int64
          example: 10485760
        db_disk_threshold:
          type: integer
          description: >-
            Total disk size limit that can be used for the database currently(in
            bytes)
          format: int64
          example: 107374182400
        db_max_entry_size:
          type: integer
          description: >-
            Max size of an entry that will be accepted by the database
            currently(in bytes)
          format: int64
          example: 104857600
        db_memory_threshold:
          type: integer
          description: Max size of a memory the database can use(in bytes)
          format: int64
          example: 3221225472
        db_max_commands_per_second:
          type: integer
          description: Max number of commands can be sent to the database per second
          format: int64
          example: 10000
        db_request_limit:
          type: integer
          description: Total number of commands can be sent to the database
          format: int64
          example: 8024278031528737000
        type:
          type: string
          description: Payment plan of the database
          enum:
            - free
            - payg
            - pro
            - paid
          example: paid
        budget:
          type: integer
          description: Allocated monthly budget for the database
          format: int64
          example: 360
        primary_region:
          type: string
          description: Primary region of the database cluster
          enum:
            - ap-south-1
            - ap-southeast-1
            - ap-southeast-2
            - ap-northeast-1
            - eu-west-1
            - eu-west-2
            - eu-central-1
            - us-east-1
            - us-west-1
            - us-west-2
            - us-east-2
            - sa-east-1
            - ca-central-1
          example: us-east-1
        primary_members:
          type: array
          items:
            type: string
          description: List of primary regions in the database cluster
          example:
            - us-east-1
        all_members:
          type: array
          items:
            type: string
          description: List of all regions in the database cluster
          example:
            - us-east-1
        eviction:
          type: boolean
          description: Entry eviction is enabled
          example: false
        auto_upgrade:
          type: boolean
          description: Automatic upgrade capability is enabled
          example: false
        consistent:
          type: boolean
          description: Strong consistency mode is enabled
          example: false
        modifying_state:
          type: string
          description: Current modifying state of the database
          example: ''
        db_resource_size:
          type: string
          description: Resource allocation tier
          enum:
            - S
            - M
            - L
            - XL
            - XXL
            - 3XL
          example: L
        db_type:
          type: string
          description: Database storage engine type
          enum:
            - bolt
            - badger
            - pebble
          example: pebble
        db_conn_idle_timeout:
          type: integer
          description: Connection idle timeout in nanoseconds
          format: int64
          example: 21600000000000
        db_lua_timeout:
          type: integer
          description: Lua script execution timeout in nanoseconds
          format: int64
          example: 250000000
        db_lua_credits_per_min:
          type: integer
          description: Lua script execution credits per minute
          format: int64
          example: 10000000000
        db_store_max_idle:
          type: integer
          description: Store connection idle timeout in nanoseconds
          format: int64
          example: 900000000000
        db_max_loads_per_sec:
          type: integer
          description: Maximum load operations per second
          format: int64
          example: 1000000
        db_acl_enabled:
          type: string
          description: Access Control List enabled status
          enum:
            - 'true'
            - 'false'
          example: 'false'
        db_acl_default_user_status:
          type: string
          description: Default user access status in ACL
          enum:
            - 'true'
            - 'false'
          example: 'true'
        db_eviction:
          type: boolean
          description: Database-level eviction policy status
          example: false
        last_plan_upgrade_time:
          type: integer
          format: int64
          description: Unix timestamp of the last plan upgrade
          example: 0
        replicas:
          type: integer
          description: Replica factor of the database
          example: 5
        customer_id:
          type: string
          description: >-
            Owner identifier of the database (may be email or marketplace-scoped
            email)
          example: example@upstash.com
        daily_backup_enabled:
          type: boolean
          description: Whether daily backup is enabled
          example: false
        read_regions:
          type: array
          items:
            type: string
          description: Array of read regions of the database
          example:
            - us-east-2
        securityAddons:
          type: object
          description: Security add-ons and their enablement status
          properties:
            ipWhitelisting:
              type: boolean
            vpcPeering:
              type: boolean
            privateLink:
              type: boolean
            tlsMutualAuth:
              type: boolean
            encryptionAtRest:
              type: boolean
          example:
            ipWhitelisting: false
            vpcPeering: false
            privateLink: false
            tlsMutualAuth: false
            encryptionAtRest: false
        prometheus_enabled:
          type: string
          description: Prometheus integration enabled status
          enum:
            - 'true'
            - 'false'
          example: 'false'
        prod_pack_enabled:
          type: boolean
          description: Production pack enabled status
          example: false
      xml:
        name: database

````