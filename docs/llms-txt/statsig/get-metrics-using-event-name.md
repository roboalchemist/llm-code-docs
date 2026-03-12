# Source: https://docs.statsig.com/api-reference/events/get-metrics-using-event-name.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get metrics using event name



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/events/{eventName}/metrics
openapi: 3.0.0
info:
  title: Console API
  description: >-
    The "Console API" is the CRUD API for performing the actions offered on
    console.statsig.com without needing to go through the web UI.

    If you have any feature requests, drop on in to our [slack
    channel](https://www.statsig.com/slack) and let us know.

    <br /><br />

    <b>Authorization</b>

    <br />

    All requests must include the **STATSIG-API-KEY** field in the header. The
    value should be a **Console API Key** which can be created in the Project
    Settings on
    [console.statsig.com/api_keys](https://console.statsig.com/api_keys)

    <br /><br />

    <b>Rate Limiting</b>

    <br />

    Requests to the Console API are limited to <code>~ 100reqs / 10secs and ~
    900reqs / 15 mins</code>.

    <br /><br />

    <b>Keyboard Search</b>

    <br />

    Use <code>Ctrl/Cmd + K</code> to search for specific endpoints.
  version: 20240601.0.0
  contact: {}
servers:
  - url: https://statsigapi.net
security: []
tags: []
paths:
  /console/v1/events/{eventName}/metrics:
    get:
      tags:
        - Events
      summary: Get metrics using event name
      parameters:
        - name: eventName
          required: true
          in: path
          schema:
            type: string
        - name: limit
          required: false
          in: query
          description: Results per page
          schema:
            example: 10
            oneOf:
              - type: string
              - type: number
            type: integer
        - name: page
          required: false
          in: query
          description: Page number
          schema:
            example: 1
            oneOf:
              - type: string
              - type: number
            type: integer
      responses:
        '200':
          description: Get metrics from events response
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: >-
                            #/components/schemas/ExternalMetricDefinitionContractDto
                example:
                  message: Metrics listed successfully.
                  data:
                    - id: add_to_cart::event_count
                      name: add_to_cart
                      directionality: increase
                      type: event_count
                      description: ''
                      isPermanent: false
                      isReadOnly: false
                      isHidden: false
                      isVerified: false
                      tags:
                        - dashboard_test
                      createdTime: 1678165878415
                      lineage:
                        events:
                          - add_to_cart
                        metrics: []
                      team: null
                    - id: add_to_cart::event_dau
                      name: add_to_cart
                      directionality: increase
                      type: event_dau
                      description: ''
                      isPermanent: false
                      isReadOnly: false
                      isHidden: false
                      isVerified: false
                      tags:
                        - asdf
                        - dashboard_test
                      createdTime: 1680128775716
                      lineage:
                        events:
                          - add_to_cart
                        metrics: []
                      team: null
                    - id: test funnel 1::funnel
                      name: test funnel 1
                      directionality: increase
                      type: funnel
                      description: ''
                      isPermanent: false
                      isReadOnly: false
                      isHidden: false
                      isVerified: false
                      tags: []
                      creatorName: Test User
                      creatorEmail: test@statsig.com
                      createdTime: 1695253296002
                      owner:
                        name: Test User
                      lineage:
                        events: []
                        metrics:
                          - add_to_cart::event_count
                          - add_to_cart_games::event_count_custom
                      team: null
                      funnelCountDistinct: events
                      funnelEventList:
                        - name: add_to_cart
                          type: event_count
                        - name: add_to_cart_games
                          type: event_count_custom
                    - id: >-
                        super_long_metric_nameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee_thing::funnel
                      name: >-
                        super_long_metric_nameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee_thing
                      directionality: increase
                      type: funnel
                      description: test
                      isPermanent: false
                      isReadOnly: false
                      isHidden: false
                      isVerified: false
                      tags:
                        - Funnels
                      creatorName: 'Test User '
                      creatorEmail: test@statsig.com
                      createdTime: 1698427486777
                      owner:
                        name: Test User
                      lineage:
                        events: []
                        metrics:
                          - add_to_cart::event_dau
                          - new_custom_metric::event_user
                      team: null
                      funnelCountDistinct: users
                      funnelEventList:
                        - name: add_to_cart
                          type: event_dau
                        - name: new_custom_metric
                          type: event_user
                    - id: test_funnel_metric::funnel
                      name: test_funnel_metric
                      directionality: decrease
                      type: funnel
                      description: ''
                      isPermanent: false
                      isReadOnly: false
                      isHidden: false
                      isVerified: false
                      tags:
                        - Funnels
                      creatorName: Test User
                      creatorEmail: test@statsig.com
                      createdTime: 1701984009755
                      owner:
                        name: Test User
                      lineage:
                        events: []
                        metrics:
                          - add_to_cart::event_dau
                      team: null
                      funnelCountDistinct: users
                      funnelEventList:
                        - name: add_to_cart
                          type: event_dau
                  pagination:
                    itemsPerPage: 5
                    pageNumber: 1
                    totalItems: 1254
                    nextPage: '?page=2&limit=5'
                    previousPage: null
                    all: ''
              example:
                message: Metrics listed successfully.
                data:
                  - id: add_to_cart::event_count
                    name: add_to_cart
                    directionality: increase
                    type: event_count
                    description: ''
                    isPermanent: false
                    isReadOnly: false
                    isHidden: false
                    isVerified: false
                    tags:
                      - dashboard_test
                    createdTime: 1678165878415
                    lineage:
                      events:
                        - add_to_cart
                      metrics: []
                    team: null
                  - id: add_to_cart::event_dau
                    name: add_to_cart
                    directionality: increase
                    type: event_dau
                    description: ''
                    isPermanent: false
                    isReadOnly: false
                    isHidden: false
                    isVerified: false
                    tags:
                      - asdf
                      - dashboard_test
                    createdTime: 1680128775716
                    lineage:
                      events:
                        - add_to_cart
                      metrics: []
                    team: null
                  - id: test funnel 1::funnel
                    name: test funnel 1
                    directionality: increase
                    type: funnel
                    description: ''
                    isPermanent: false
                    isReadOnly: false
                    isHidden: false
                    isVerified: false
                    tags: []
                    creatorName: Test User
                    creatorEmail: test@statsig.com
                    createdTime: 1695253296002
                    owner:
                      name: Test User
                    lineage:
                      events: []
                      metrics:
                        - add_to_cart::event_count
                        - add_to_cart_games::event_count_custom
                    team: null
                    funnelCountDistinct: events
                    funnelEventList:
                      - name: add_to_cart
                        type: event_count
                      - name: add_to_cart_games
                        type: event_count_custom
                  - id: >-
                      super_long_metric_nameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee_thing::funnel
                    name: >-
                      super_long_metric_nameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee_thing
                    directionality: increase
                    type: funnel
                    description: test
                    isPermanent: false
                    isReadOnly: false
                    isHidden: false
                    isVerified: false
                    tags:
                      - Funnels
                    creatorName: 'Test User '
                    creatorEmail: test@statsig.com
                    createdTime: 1698427486777
                    owner:
                      name: Test User
                    lineage:
                      events: []
                      metrics:
                        - add_to_cart::event_dau
                        - new_custom_metric::event_user
                    team: null
                    funnelCountDistinct: users
                    funnelEventList:
                      - name: add_to_cart
                        type: event_dau
                      - name: new_custom_metric
                        type: event_user
                  - id: test_funnel_metric::funnel
                    name: test_funnel_metric
                    directionality: decrease
                    type: funnel
                    description: ''
                    isPermanent: false
                    isReadOnly: false
                    isHidden: false
                    isVerified: false
                    tags:
                      - Funnels
                    creatorName: Test User
                    creatorEmail: test@statsig.com
                    createdTime: 1701984009755
                    owner:
                      name: Test User
                    lineage:
                      events: []
                      metrics:
                        - add_to_cart::event_dau
                    team: null
                    funnelCountDistinct: users
                    funnelEventList:
                      - name: add_to_cart
                        type: event_dau
                pagination:
                  itemsPerPage: 5
                  pageNumber: 1
                  totalItems: 1254
                  nextPage: '?page=2&limit=5'
                  previousPage: null
                  all: ''
        '400':
          description: Invalid request. Please check the request input and try again.
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: integer
                    enum:
                      - 400
                  message:
                    type: string
                required:
                  - status
                  - message
              examples:
                Invalid Request:
                  value:
                    status: 400
                    message: >-
                      Invalid request. Please check the request input and try
                      again.
        '401':
          description: >-
            This endpoint only accepts an active CONSOLE key, but an invalid key
            was sent. Key: console-xxxXXXxxxXXXxxx
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: integer
                    enum:
                      - 401
                  message:
                    type: string
                required:
                  - status
                  - message
              examples:
                Invalid Endpoint:
                  value:
                    status: 401
                    message: >-
                      This endpoint only accepts an active CONSOLE key, but an
                      invalid key was sent. Key: console-xxxXXXxxxXXXxxx
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    PaginationResponseWithMessage:
      type: object
      properties:
        message:
          type: string
          description: A simple string explaining the result of the operation.
        data:
          description: Array of results returned by pagination limit.
          type: array
          items:
            type: object
        pagination:
          description: Pagination metadata for checking if there is next page for example.
          allOf:
            - $ref: '#/components/schemas/PaginationResponseMetadataDto'
      required:
        - message
        - data
        - pagination
    ExternalMetricDefinitionContractDto:
      type: object
      properties:
        name:
          type: string
          description: The name of the metric, serving as its primary identifier.
          example: metricName
        type:
          type: string
          enum:
            - ratio
            - sum
            - composite
            - mean
            - event_count_custom
            - event_user
            - funnel
            - undefined
            - setup_incomplete
            - composite_sum
            - import_window
            - user_warehouse
            - hybrid_warehouse
            - count_distinct
            - ads_segment_exposed_user_days
            - percentile
          description: >-
            The type of the metric, defining its aggregation method and
            characteristics.
          example: sum
        isVerified:
          type: boolean
          description: >-
            Marks the metric as verified, indicating trustworthiness within the
            organization.
          example: false
        isReadOnly:
          type: boolean
          description: >-
            Set to true to make the metric definition editable only through the
            Console API.
          example: false
        unitTypes:
          type: array
          items:
            type: string
          description: >-
            Array of unit types associated with the metric, such as stableID or
            userID.
          example:
            - stableID
            - userID
        metricEvents:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
                description: The name of the metric event.
              type:
                type: string
                enum:
                  - count
                  - count_distinct
                  - value
                  - metadata
                nullable: true
                description: >-
                  The type of metric event. Allowed values include: count,
                  count_distinct, value, and metadata.
              metadataKey:
                type: string
                description: The key for associated metadata, if applicable.
              criteria:
                type: array
                items:
                  $ref: '#/components/schemas/MetricEventsCriteriaDto'
                  description: >-
                    Array of event criteria for defining filtering conditions in
                    metrics analysis.
                description: >-
                  Filtering criteria for the metric event, including conditions
                  and values to refine the event data.
            required:
              - name
          description: An array of event definitions used to compute the metric.
          example:
            - name: event1
              type: value
        metricComponentMetrics:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
              type:
                type: string
            required:
              - name
              - type
          description: >-
            List of input metrics used to calculate the new metric for composite
            types.
          example: []
        description:
          type: string
          description: >-
            An optional description providing additional context about the
            metric.
          example: the description of this metric
        directionality:
          type: string
          enum:
            - increase
            - decrease
          description: >-
            Specifies the desired directionality for the metric, indicating
            whether an increase or decrease is favorable.
          example: increase
        tags:
          type: array
          items:
            type: string
          description: >-
            Optional tags for categorizing the metric and improving
            searchability.
          example:
            - tag1
            - tag2
        isPermanent:
          type: boolean
          description: Indicates whether the metric is permanent and should not be deleted.
          example: false
        rollupTimeWindow:
          type: string
          description: >-
            Time window for the metric rollup. Specify "custom" for a customized
            time window.
          example: custom
        customRollUpStart:
          type: number
          description: Custom time window start date in days since exposure.
          example: 1
          format: double
        customRollUpEnd:
          type: number
          description: Custom time window end date in days since exposure.
          example: 1
          format: double
        funnelEventList:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
                description: The name of the funnel event used in the metric.
                example: event1
              type:
                type: string
                enum:
                  - event_dau
                  - event_user
                  - event_count
                  - event_count_custom
                description: The type of funnel event, specifying how the event is tracked.
                example: event_dau
            required:
              - name
              - type
          description: List of events used to create funnel metrics.
        funnelCountDistinct:
          type: string
          enum:
            - events
            - users
          description: >-
            Specifies whether to count events or distinct users for the funnel
            metric.
        warehouseNative:
          type: object
          properties:
            aggregation:
              type: string
              enum:
                - count
                - sum
                - mean
                - daily_participation
                - ratio
                - funnel
                - count_distinct
                - percentile
                - first_value
                - latest_value
                - retention
                - max
                - min
                - composite
                - ''
              description: >-
                Allowed:
                count┃sum┃mean┃daily_participation┃ratio┃funnel┃count_distinct┃percentile
            metricSourceName:
              type: string
              description: >-
                Deprecated: use `metricSources` instead. If provided, this will
                overwrite all metric sources. For Count, Sum, Mean, User Count
                aggregation types: the name of metric source
            criteria:
              type: array
              items:
                $ref: '#/components/schemas/MetricEventsCriteriaDto'
                description: >-
                  Array of event criteria for defining filtering conditions in
                  metrics analysis.
              description: >-
                Deprecated: use `metricSources` instead. If provided with
                `metricSourceName`, this will overwrite all metric sources.
                Filtering criteria for the metric source
            metricSources:
              type: array
              items:
                type: object
                properties:
                  metricSourceName:
                    type: string
                  criteria:
                    type: array
                    items:
                      $ref: '#/components/schemas/MetricEventsCriteriaDto'
                      description: >-
                        Array of event criteria for defining filtering
                        conditions in metrics analysis.
                    description: Filtering criteria for the metric source
                  valueColumn:
                    type: string
                required:
                  - metricSourceName
                  - criteria
              description: List of metric sources for this metric.
            waitForCohortWindow:
              type: boolean
            denominatorCriteria:
              type: array
              items:
                $ref: '#/components/schemas/MetricEventsCriteriaDto'
                description: >-
                  Array of event criteria for defining filtering conditions in
                  metrics analysis.
              description: >-
                Filtering criteria for the denominator metric source for a
                ratio, or the start event for a retention metric if
                useSecondaryRetentionEvent is set
            denominatorAggregation:
              type: string
              enum:
                - count
                - sum
                - mean
                - daily_participation
                - ratio
                - funnel
                - count_distinct
                - percentile
                - first_value
                - latest_value
                - retention
                - max
                - min
                - composite
                - ''
              description: >-
                Allowed:
                count┃sum┃mean┃daily_participation┃ratio┃funnel┃count_distinct┃percentile
            denominatorCustomRollupEnd:
              type: number
              description: >-
                Custom end window for ratio denominator unit count metrics with
                "custom" rollup time window. Measured in days or minutes
                depending on the "denominatorCustomRollupMeasureInMinutes" flag.
              format: double
            denominatorCustomRollupStart:
              type: number
              description: >-
                Custom start window for ratio denominator unit count metrics
                with "custom" rollup time window. Measured in days or minutes
                depending on the "denominatorCustomRollupMeasureInMinutes" flag.
              format: double
            denominatorMetricSourceName:
              type: string
              description: >-
                Name of the metric source for the denominator of a ratio, or the
                start event for a retention metric if useSecondaryRetentionEvent
                is set
            denominatorRollupTimeWindow:
              type: string
              description: >-
                Rollup-mode for ratio denominator unit count metrics. Allowed
                values: "daily" for daily participation rate, "max" for one-time
                event, "custom" for a custom attribution window
            denominatorValueColumn:
              type: string
              description: Column name for the denominator’s value.
            funnelCalculationWindow:
              type: number
              description: Duration for counting funnel events in days.
              format: double
            funnelCountDistinct:
              type: string
              enum:
                - sessions
                - users
              description: >-
                Allowed: users┃sessions for distinct count method in funnel
                events.
            funnelEvents:
              type: array
              items:
                type: object
                properties:
                  criteria:
                    type: array
                    items:
                      $ref: '#/components/schemas/MetricEventsCriteriaDto'
                      description: >-
                        Array of event criteria for defining filtering
                        conditions in metrics analysis.
                    description: >-
                      Optional array of criteria to filter the funnel events,
                      defined by various types and conditions.
                  metricSourceName:
                    type: string
                    description: >-
                      Optional name of the metric source associated with the
                      funnel event.
                  name:
                    type: string
                    nullable: true
                    description: >-
                      Optional step name for the funnel event, can be null if
                      not specified.
                  sessionIdentifierField:
                    type: string
                    nullable: true
                    description: >-
                      Name of column which being used as session identifier.
                      Funnel event with the same metric source
              description: List of funnel events with associated criteria and identifiers.
            funnelStartCriteria:
              type: string
              enum:
                - start_event
                - exposure
              description: >-
                Allowed: start_event┃exposure to determine funnel start
                criteria.
            metricDimensionColumns:
              type: array
              items:
                type: string
              description: Specify metadata columns for breaking down metric analysis.
            metricDimensionLimits:
              type: array
              items:
                type: object
                properties:
                  name:
                    type: string
                    description: Name of the metadata dimension to apply a breakdown limit.
                  limit:
                    type: integer
                    minimum: 0
                    maximum: 100
                    description: >-
                      Maximum number of values to retain for this dimension
                      (0-100).
                    example: 10
                required:
                  - name
                  - limit
              description: >-
                Per-dimension breakdown limits; values beyond the limit are
                grouped into OTHER.
            metricBakeDays:
              type: number
              description: Number of days for metric baking; specify duration for analysis.
              format: double
            loadingWindow:
              type: number
              description: >-
                Lookback window in days for loading metric data. Defaults to 90
                days.
              example: 90
              format: double
            numeratorAggregation:
              type: string
              enum:
                - count
                - sum
                - mean
                - daily_participation
                - ratio
                - funnel
                - count_distinct
                - percentile
                - first_value
                - latest_value
                - retention
                - max
                - min
                - composite
                - ''
              description: >-
                Aggregation type for numerator; Allowed:
                count┃sum┃mean┃daily_participation┃ratio┃funnel┃count_distinct┃percentile.
            valueColumn:
              type: string
              description: >-
                Deprecated: use `metricSources` instead. If provided with
                `metricSourceName`, this will overwrite all metric sources.
                Column name representing the metric’s value.
            valueThreshold:
              type: number
              description: Threshold value for filtering metrics.
              format: double
            allowNullRatioDenominator:
              type: boolean
              description: >-
                Include units which do not have a denominator. Only applicable
                to ratios.
            funnelStrictOrdering:
              type: boolean
            funnelUseExposureAsFirstEvent:
              type: boolean
            funnelTimestampAllowanceMs:
              type: number
              format: double
            funnelTimeToConvert:
              type: boolean
            winsorizationHigh:
              type: number
              maximum: 1
              minimum: 0
              description: High threshold for winsorization; must be between 0 and 1.
              format: double
            winsorizationLow:
              type: number
              maximum: 1
              minimum: 0
              description: Low threshold for winsorization; must be between 0 and 1.
              format: double
            winsorizationHighDenominator:
              type: number
              maximum: 1
              minimum: 0
              format: double
            winsorizationLowDenominator:
              type: number
              maximum: 1
              minimum: 0
              format: double
            cupedAttributionWindow:
              type: number
              nullable: true
              description: Attribution window for CUPED adjustments in days.
              format: double
            rollupTimeWindow:
              type: string
              description: >-
                Rollup-mode for unit count metrics. Allowed values: "daily" for
                daily participation rate, "max" for one-time event, "custom" for
                a custom attribution window
            customRollUpStart:
              type: number
              description: >-
                Custom start window for unit count metrics with "custom" rollup
                time window, or for other metrics with the "Use Cohort Window in
                Experiments" option on enabled. Measured in days or minutes
                depending on the "customRollupMeasureInMinutes" flag.
              format: double
            customRollUpEnd:
              type: number
              description: >-
                Custom end window for unit count metrics with "custom" rollup
                time window, or for other metrics with the "Use Cohort Window in
                Experiments" option on enabled. Measured in days or minutes
                depending on the "customRollupMeasureInMinutes" flag.
              format: double
            onlyIncludeUsersWithConversionEvent:
              type: boolean
              description: >-
                Flag to include only users with a conversion event in the
                metric.
            denominatorCustomRollupMeasureInMinutes:
              type: boolean
              description: >-
                Flag to measure the denominator custom rollup window in minutes
                instead of days.
            customRollupMeasureInMinutes:
              type: boolean
              description: >-
                Flag to measure the custom rollup window in minutes instead of
                days.
            percentile:
              type: number
              description: Percentile value for statistical calculations.
              format: double
            useLogTransform:
              type: boolean
              description: Use log transform for the metric.
            useSecondaryRetentionEvent:
              type: boolean
              description: >-
                Use a different start and completion event for retention
                calculations.
            retentionEnd:
              type: number
              description: Retention end in days.
              format: double
            retentionLength:
              type: number
              description: Retention lookback window in days.
              format: double
            logTransformBase:
              type: number
              nullable: true
              description: Log transform base to be used for the metric.
              format: double
            cap:
              type: number
              description: Maximum cap for metric values.
              format: double
            surrogateMetricMSE:
              type: number
              nullable: true
              description: Mean Squared Error for surrogate metric.
              format: double
            components:
              type: array
              items:
                type: object
                properties:
                  operator:
                    type: string
                    enum:
                      - +
                      - '-'
                    description: Operator for this component
                  aggregation:
                    type: string
                    enum:
                      - count
                      - sum
                      - mean
                      - daily_participation
                      - ratio
                      - funnel
                      - count_distinct
                      - percentile
                      - first_value
                      - latest_value
                      - retention
                      - max
                      - min
                      - composite
                      - ''
                    description: Aggregation type for this component
                  metricSourceName:
                    type: string
                    description: Metric source name for this component
                  name:
                    type: string
                    nullable: true
                    description: Optional name for this component
                  criteria:
                    type: array
                    items:
                      $ref: '#/components/schemas/MetricEventsCriteriaDto'
                      description: >-
                        Array of event criteria for defining filtering
                        conditions in metrics analysis.
                    description: Optional filtering criteria for this component
                  valueColumn:
                    type: string
                    description: Value column for this component
                required:
                  - operator
              description: >-
                Components for composite metrics, defining each component of the
                formula
          description: Defines warehouse native metrics for advanced configurations.
        team:
          type: string
          nullable: true
          description: >-
            The team associated with the metric, applicable for enterprise
            environments.
        teamID:
          type: string
          nullable: true
          description: >-
            The team ID associated with the metric, applicable for enterprise
            environments.
        dryRun:
          type: boolean
          description: >-
            Skips persisting the metric (used to validate that inputs are
            correct)
        id:
          type: string
          description: >-
            Unique identifier for the metric, used for referencing within the
            system.
          example: metricId
        isHidden:
          type: boolean
          description: Indicates if the metric is hidden from the user interface.
          example: false
        lineage:
          type: object
          properties:
            events:
              type: array
              items:
                type: string
              description: List of event names that contribute to the metric’s calculation.
              example:
                - event1
                - event2
            metrics:
              type: array
              items:
                type: string
              description: List of metric names that are part of this metric’s lineage.
              example:
                - metric1
                - metric2
          required:
            - events
            - metrics
        creatorName:
          type: string
          nullable: true
          description: Name of the person who created the metric, if available.
          example: creatorName
        creatorEmail:
          type: string
          nullable: true
          description: Email address of the metric creator for contact purposes.
          example: creatorEmail
        createdTime:
          type: number
          description: Timestamp indicating when the metric was created.
          example: 1716230400
          format: double
        lastModifierID:
          type: string
          nullable: true
          description: ID of the last modifier.
        lastModifiedTime:
          type: number
          nullable: true
          description: Time of the last modification to this metric.
          format: double
        lastModifierEmail:
          type: string
          nullable: true
          description: Email of the last modifier.
        lastModifierName:
          type: string
          nullable: true
          description: Name of the last modifier.
        owner:
          type: object
          properties:
            ownerID:
              type: string
              description: ID of the owner
              example: abc123
            ownerType:
              type: string
              description: Type of the owner (e.g., SDK_KEY or USER)
              example: USER
            ownerName:
              type: string
              description: The name of the owner. This field is optional.
              example: John Doe
            ownerEmail:
              type: string
              description: The email of the owner. This field is optional.
            name:
              type: string
              description: The name of the owner.
              example: John Doe
          required:
            - name
      required:
        - name
        - type
        - directionality
        - id
        - lineage
    PaginationResponseMetadataDto:
      type: object
      properties:
        itemsPerPage:
          type: number
          format: double
        pageNumber:
          type: number
          format: double
        nextPage:
          type: string
          nullable: true
        previousPage:
          type: string
          nullable: true
        totalItems:
          type: number
          format: double
        all:
          type: string
      required:
        - itemsPerPage
        - pageNumber
        - nextPage
        - previousPage
    MetricEventsCriteriaDto:
      type: object
      properties:
        type:
          type: string
          enum:
            - value
            - metadata
            - user
            - user_custom
          description: >-
            Type of event criterion for filtering metrics. Options include
            `value`, `metadata`, `user`, and `user_custom`; in Warehouse Native,
            this should always be `metadata`.
        column:
          type: string
          description: Optional column specifying which data attribute to filter on.
        condition:
          type: string
          enum:
            - in
            - not_in
            - '='
            - '>'
            - <
            - '>='
            - <=
            - is_null
            - non_null
            - contains
            - not_contains
            - sql_filter
            - starts_with
            - ends_with
            - after_exposure
            - before_exposure
            - is_true
            - is_false
          description: >-
            sql_filter, start_withs, ends_with, after_exposure, and
            before_exposure are only applicable in Warehouse Native
        values:
          type: array
          items:
            type: string
          description: Optional array of values for the criterion to match against.
        nullVacuousOverride:
          type: boolean
          description: If true, overrides null values in criterion evaluation.
      required:
        - type
        - condition
      description: >-
        Array of event criteria for defining filtering conditions in metrics
        analysis.
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).