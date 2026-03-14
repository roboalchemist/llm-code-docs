# Source: https://docs.statsig.com/api-reference/experiments/list-experiments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Experiments



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/experiments
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
  /console/v1/experiments:
    get:
      tags:
        - Experiments
        - Experiments
      summary: List Experiments
      parameters:
        - name: layerID
          required: false
          in: query
          description: Which layer to place the experiment into.
          schema:
            type: string
        - name: idType
          required: false
          in: query
          description: The idType the experiment will be performed on
          schema:
            type: string
        - name: teamID
          required: false
          in: query
          description: The team ID associated with the experiment, Enterprise only.
          schema:
            type: string
            nullable: true
        - name: status
          required: false
          in: query
          description: The current status of the experiment
          schema:
            oneOf:
              - type: string
                enum:
                  - active
                  - setup
                  - decision_made
                  - abandoned
                  - archived
                  - experiment_stopped
                  - assignment_stopped
              - type: array
                items:
                  type: string
                  enum:
                    - active
                    - setup
                    - decision_made
                    - abandoned
                    - archived
                    - experiment_stopped
                    - assignment_stopped
        - name: targetAppID
          required: false
          in: query
          schema:
            type: string
        - name: stale
          required: false
          in: query
          description: >-
            When true, only returns stale experiments. If omitted or false,
            returns all experiments.
          schema:
            type: boolean
        - name: createdStartDate
          required: false
          in: query
          description: Expected valid date in the form of YYYY-MM-DD
          schema:
            example: '2024-01-01'
            type: string
        - name: createdEndDate
          required: false
          in: query
          description: Expected valid date in the form of YYYY-MM-DD
          schema:
            example: '2024-01-01'
            type: string
        - name: experimentType
          required: false
          in: query
          description: Filter by experiment type
          schema:
            oneOf:
              - type: string
                enum:
                  - BASE
                  - GEO
                  - SWITCHBACK
                  - PROMPT
                  - SIDECAR
                  - GRID_SEARCH
              - type: array
                items:
                  type: string
                  enum:
                    - BASE
                    - GEO
                    - SWITCHBACK
                    - PROMPT
                    - SIDECAR
                    - GRID_SEARCH
        - name: creatorName
          required: false
          in: query
          description: Name of the creator.
          schema:
            type: string
            nullable: true
        - name: creatorID
          required: false
          in: query
          description: ID of the user who created the entity.
          schema:
            type: string
            nullable: true
        - name: tags
          required: false
          in: query
          description: Filter by tags
          examples:
            single tag:
              value: tag1
            multiple tags:
              value:
                - tag1
                - tag2
          schema:
            oneOf:
              - type: string
              - type: array
                items:
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
          description: List Experiments Success
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginationResponseWithMessage'
                  - properties:
                      data:
                        type: array
                        items:
                          $ref: '#/components/schemas/ExternalExperimentDto'
                example:
                  message: Experiments listed successfully.
                  data:
                    - id: a_experiment
                      name: a_experiment
                      description: description
                      idType: userID
                      lastModifierID: 1vaQaBoLlkauH9iiuOSBP2
                      lastModifiedTime: 1707427635442
                      lastModifierName: CONSOLE API
                      lastModifierEmail: null
                      creatorID: 1vaQaBoLlkauH9iiuOSBP2
                      createdTime: 1707427634717
                      creatorName: CONSOLE API
                      creatorEmail: null
                      targetApps: []
                      holdoutIDs: []
                      tags: []
                      status: setup
                      experimentType: BASE
                      launchedGroupID: null
                      startTime: null
                      endTime: null
                      layerID: null
                      hypothesis: This will be a good feature :)
                      primaryMetrics:
                        - name: d1_retention_rate
                          type: user
                      primaryMetricTags: []
                      secondaryMetrics: []
                      secondaryMetricTags: []
                      groups:
                        - name: Control
                          id: 6sEQvUd4c6E55V6ljBYMeJ
                          size: 50
                          parameterValues:
                            assigned_group: control
                          description: ''
                        - name: Test
                          id: 6sEQvVS6EoNzpkEgUJUpxL
                          size: 50
                          parameterValues:
                            assigned_group: test
                          description: ''
                      allocation: 100
                      duration: 14
                      targetingGateID: ''
                      defaultConfidenceInterval: '95'
                      bonferroniCorrection: false
                      decisionReason: null
                      decisionTime: null
                      healthChecks: []
                      owner:
                        ownerType: USER
                        ownerName: Test User
                      inlineTargetingRulesJSON: '{}'
                      healthCheckStatus: PASSED
                      isStale: false
                    - id: b_experiment
                      name: b experiment
                      description: ''
                      idType: userID
                      inlineTargetingRulesJSON: '{}'
                      lastModifierID: 68ztZp2v2nFc81RAsvuvj4
                      lastModifiedTime: 1706744900374
                      lastModifierName: jacob O'Quinn
                      lastModifierEmail: jacob@statsig.com
                      creatorID: 68ztZp2v2nFc81RAsvuvj4
                      createdTime: 1678394676162
                      creatorName: jacob O'Quinn
                      creatorEmail: jacob@statsig.com
                      targetApps: []
                      holdoutIDs: []
                      tags:
                        - customTag
                        - asdf
                      status: archived
                      experimentType: BASE
                      launchedGroupID: null
                      startTime: null
                      endTime: null
                      layerID: null
                      hypothesis: ''
                      primaryMetrics: []
                      primaryMetricTags: []
                      secondaryMetrics: []
                      secondaryMetricTags:
                        - ★ Core
                      groups:
                        - name: Control
                          id: 7dCnwm0by2laSOcBNKIL8r
                          size: 50
                          parameterValues:
                            control: control value
                          description: ''
                        - name: Test
                          id: 7dCnwnFe0kuFcdKxoSEort
                          size: 50
                          parameterValues:
                            control: test value
                          description: ''
                      allocation: 100
                      duration: 14
                      targetingGateID: targeting_gate_to_select_users
                      defaultConfidenceInterval: '95'
                      bonferroniCorrection: false
                      decisionReason: null
                      decisionTime: null
                      healthCheckStatus: WAITING
                      healthChecks:
                        - name: Checks not yet detected
                          status: WAITING
                          description: >-
                            This experiment has not recorded any exposure checks
                            in production yet.
                        - name: Valid unit type not yet verified
                          status: WAITING
                          description: >-
                            Exposure checks for this experiment are pending
                            evaluation. This experiment requires exposure checks
                            with unit IDs of type userID
                        - name: Event metric data not yet verified
                          status: WAITING
                          description: >-
                            This experiment has recorded no event metric with a
                            valid unit ID yet, or these event metrics are
                            pending evaluation. If you are importing events,
                            this may take up to a day to reflect. This
                            experiment requires metrics with unit IDs of type
                            userID
                        - name: Pulse metrics not yet available
                          status: WAITING
                          description: >-
                            Expect to see your Pulse Results within 24 hours.
                            Statsig computes Pulse results on a daily basis.
                        - name: Exposure balance not yet verified
                          status: WAITING
                          description: >-
                            Exposure balance for this experiment is pending
                            evaluation. As the experiment records more
                            exposures, Statsig will continue to evaluate
                            experiment exposure balance.
                      isStale: false
              example:
                message: Experiments listed successfully.
                data:
                  - id: a_experiment
                    name: a_experiment
                    description: description
                    idType: userID
                    lastModifierID: 1vaQaBoLlkauH9iiuOSBP2
                    lastModifiedTime: 1707427635442
                    lastModifierName: CONSOLE API
                    lastModifierEmail: null
                    creatorID: 1vaQaBoLlkauH9iiuOSBP2
                    createdTime: 1707427634717
                    creatorName: CONSOLE API
                    creatorEmail: null
                    targetApps: []
                    holdoutIDs: []
                    tags: []
                    status: setup
                    experimentType: BASE
                    launchedGroupID: null
                    startTime: null
                    endTime: null
                    layerID: null
                    hypothesis: This will be a good feature :)
                    primaryMetrics:
                      - name: d1_retention_rate
                        type: user
                    primaryMetricTags: []
                    secondaryMetrics: []
                    secondaryMetricTags: []
                    groups:
                      - name: Control
                        id: 6sEQvUd4c6E55V6ljBYMeJ
                        size: 50
                        parameterValues:
                          assigned_group: control
                        description: ''
                      - name: Test
                        id: 6sEQvVS6EoNzpkEgUJUpxL
                        size: 50
                        parameterValues:
                          assigned_group: test
                        description: ''
                    allocation: 100
                    duration: 14
                    targetingGateID: ''
                    defaultConfidenceInterval: '95'
                    bonferroniCorrection: false
                    decisionReason: null
                    decisionTime: null
                    healthChecks: []
                    owner:
                      ownerType: USER
                      ownerName: Test User
                    inlineTargetingRulesJSON: '{}'
                    healthCheckStatus: PASSED
                    isStale: false
                  - id: b_experiment
                    name: b experiment
                    description: ''
                    idType: userID
                    inlineTargetingRulesJSON: '{}'
                    lastModifierID: 68ztZp2v2nFc81RAsvuvj4
                    lastModifiedTime: 1706744900374
                    lastModifierName: jacob O'Quinn
                    lastModifierEmail: jacob@statsig.com
                    creatorID: 68ztZp2v2nFc81RAsvuvj4
                    createdTime: 1678394676162
                    creatorName: jacob O'Quinn
                    creatorEmail: jacob@statsig.com
                    targetApps: []
                    holdoutIDs: []
                    tags:
                      - customTag
                      - asdf
                    status: archived
                    experimentType: BASE
                    launchedGroupID: null
                    startTime: null
                    endTime: null
                    layerID: null
                    hypothesis: ''
                    primaryMetrics: []
                    primaryMetricTags: []
                    secondaryMetrics: []
                    secondaryMetricTags:
                      - ★ Core
                    groups:
                      - name: Control
                        id: 7dCnwm0by2laSOcBNKIL8r
                        size: 50
                        parameterValues:
                          control: control value
                        description: ''
                      - name: Test
                        id: 7dCnwnFe0kuFcdKxoSEort
                        size: 50
                        parameterValues:
                          control: test value
                        description: ''
                    allocation: 100
                    duration: 14
                    targetingGateID: targeting_gate_to_select_users
                    defaultConfidenceInterval: '95'
                    bonferroniCorrection: false
                    decisionReason: null
                    decisionTime: null
                    healthCheckStatus: WAITING
                    healthChecks:
                      - name: Checks not yet detected
                        status: WAITING
                        description: >-
                          This experiment has not recorded any exposure checks
                          in production yet.
                      - name: Valid unit type not yet verified
                        status: WAITING
                        description: >-
                          Exposure checks for this experiment are pending
                          evaluation. This experiment requires exposure checks
                          with unit IDs of type userID
                      - name: Event metric data not yet verified
                        status: WAITING
                        description: >-
                          This experiment has recorded no event metric with a
                          valid unit ID yet, or these event metrics are pending
                          evaluation. If you are importing events, this may take
                          up to a day to reflect. This experiment requires
                          metrics with unit IDs of type userID
                      - name: Pulse metrics not yet available
                        status: WAITING
                        description: >-
                          Expect to see your Pulse Results within 24 hours.
                          Statsig computes Pulse results on a daily basis.
                      - name: Exposure balance not yet verified
                        status: WAITING
                        description: >-
                          Exposure balance for this experiment is pending
                          evaluation. As the experiment records more exposures,
                          Statsig will continue to evaluate experiment exposure
                          balance.
                    isStale: false
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
    ExternalExperimentDto:
      type: object
      properties:
        reviewSettings:
          type: object
          properties:
            requiredReview:
              type: boolean
            allowedReviewers:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: string
                  name:
                    type: string
                  email:
                    type: string
                required:
                  - id
                  - name
                  - email
              nullable: true
          required:
            - requiredReview
        activeReview:
          type: object
          properties:
            reviewID:
              type: string
            reviewStatus:
              type: string
            description:
              type: string
          required:
            - reviewID
            - reviewStatus
            - description
        id:
          type: string
          description: ID
        name:
          type: string
          maxLength: 100
          minLength: 3
          pattern: ^[a-zA-Z0-9_\- ]*$
          description: The display name of the experiment
        idType:
          type: string
        description:
          type: string
          maxLength: 1000
          description: A helpful summary of what this experiment does
        lastModifierID:
          type: string
          nullable: true
          description: ID of the last modifier.
        lastModifiedTime:
          type: number
          nullable: true
          description: Time of the last modification.
          format: double
        lastModifierEmail:
          type: string
          nullable: true
          description: Email of the last modifier.
        lastModifierName:
          type: string
          nullable: true
          description: Name of the last modifier.
        creatorID:
          type: string
          nullable: true
          description: The Statsig ID of the creator of this experiment
        createdTime:
          type: number
          description: Timestamp when the entity was created.
          format: double
        creatorName:
          type: string
          nullable: true
          description: Name of the creator.
        creatorEmail:
          type: string
          nullable: true
          description: The email of the creator of this experiment
        tags:
          type: array
          items:
            type: string
        targetApps:
          oneOf:
            - type: string
            - type: array
              items:
                type: string
          description: Target apps assigned to this experiment
        holdoutIDs:
          type: array
          items:
            type: string
          description: Holdouts applied to this configuration.
        team:
          type: string
          nullable: true
          description: The team name associated with the experiment, Enterprise only.
        teamID:
          type: string
          nullable: true
          description: The team ID associated with the experiment, Enterprise only.
        version:
          type: number
          description: Version number
          format: double
        secondaryIDType:
          type: string
          nullable: true
          description: >-
            The secondary ID type for the experiment used in WHN for ID
            resolution
        identifierMappingMode:
          type: string
          enum:
            - strictOneToOne
            - firstTouchOneToMany
            - lastTouchOneToMany
          description: >-
            The identifier mapping mode for the experiment used in WHN for ID
            resolution
        identityResolutionSource:
          type: string
          nullable: true
          description: >-
            The identity resolution entity property source for the experiment
            used in WHN for ID resolution
        hypothesis:
          type: string
          description: A statement that will be tested by this experiment
        links:
          type: array
          items:
            type: object
            properties:
              url:
                type: string
                format: uri
                description: The URL of the link
              title:
                type: string
                description: The title of the link
            required:
              - url
          description: Links to relevant documentation or resources
        externalEvents:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
              timestamp:
                type: number
            required:
              - name
              - timestamp
        groups:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
              id:
                type: string
                nullable: true
              size:
                type: number
                minimum: 0
                maximum: 100
              parameterValues:
                type: object
                additionalProperties: {}
              disabled:
                type: boolean
              description:
                type: string
              foreignGroupID:
                type: string
              highlighted:
                type: boolean
            required:
              - name
              - size
              - parameterValues
          description: The test groups for your experiment
        controlGroupID:
          type: string
          description: Optional control group ID
        allocation:
          type: number
          minimum: 0
          maximum: 100
          description: Percent of layer allocated to this experiment
          format: double
        userBuckets:
          type: array
          items:
            type: number
            minimum: 0
            maximum: 1000
            exclusiveMaximum: true
        primaryMetricTags:
          type: array
          items:
            type: string
          description: Primary metric tags for the experiment
        secondaryMetricTags:
          type: array
          items:
            type: string
          description: Secondary metric tags for the experiment
        primaryMetrics:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
                description: The metric name.
              type:
                type: string
                description: The metric type.
              direction:
                type: string
                enum:
                  - increase
                  - decrease
                description: >-
                  The expected direction for one-sided testing (a feature to
                  only measure metric movements in a single direction)
              hypothesizedValue:
                type: number
                description: >-
                  The comparison value for the one-sample testing (a feature to
                  use a fixed baseline as the control value)
            required:
              - name
              - type
        secondaryMetrics:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
                description: The metric name.
              type:
                type: string
                description: The metric type.
              direction:
                type: string
                enum:
                  - increase
                  - decrease
                description: >-
                  The expected direction for one-sided testing (a feature to
                  only measure metric movements in a single direction)
              hypothesizedValue:
                type: number
                description: >-
                  The comparison value for the one-sample testing (a feature to
                  use a fixed baseline as the control value)
            required:
              - name
              - type
        otherMetrics:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
                description: The metric name.
              type:
                type: string
                description: The metric type.
              direction:
                type: string
                enum:
                  - increase
                  - decrease
                description: >-
                  The expected direction for one-sided testing (a feature to
                  only measure metric movements in a single direction)
              hypothesizedValue:
                type: number
                description: >-
                  The comparison value for the one-sample testing (a feature to
                  use a fixed baseline as the control value)
            required:
              - name
              - type
          description: >-
            Additional metrics you want to investigate or learn from. The usual
            corrections applied to Primary and Secondary metrics are not applied
            to these.
        duration:
          type: integer
          minimum: 1
          exclusiveMinimum: true
          description: How long the experiment is expected to last in days
          format: int64
        targetExposures:
          type: integer
          minimum: 1
          exclusiveMinimum: true
          description: Target exposures for the experiment
          format: int64
        targetingGateID:
          type: string
          nullable: true
          description: Restrict your experiment to users passing the selected feature gate
        sequentialTesting:
          type: boolean
          description: Apply sequential testing?
        bonferroniCorrection:
          type: boolean
          description: Is Bonferroni correction applied per variant?
        bonferroniCorrectionPerMetric:
          type: boolean
          description: Is Bonferroni correction applied per metric?
        benjaminiHochbergPerVariant:
          type: boolean
          description: Is Benjamini-Hochberg procedure applied per variant?
        benjaminiHochbergPerMetric:
          type: boolean
          description: Is Benjamini-Hochberg procedure applied per metric?
        benjaminiPrimaryMetricsOnly:
          type: boolean
          description: Is Benjamini-Hochberg procedure applied for primary metrics only?
        defaultConfidenceInterval:
          type: string
          enum:
            - '80'
            - '90'
            - '95'
            - '98'
            - '99'
          description: Default error margin used for results
        defaultRollupWindow:
          type: integer
          description: >-
            Default rollup window in days for experiment results. Use -1 for
            cumulative. Only -1, 1, and 7 allowed for cloud experiments.
          format: int64
        defaultChanceToBeatThreshold:
          type: number
          description: Default chance-to-beat threshold used for Bayesian results.
          format: double
        bayesianPriors:
          type: array
          items:
            type: object
            properties:
              metric:
                type: object
                properties:
                  name:
                    type: string
                  type:
                    type: string
                required:
                  - name
                  - type
              priorMean:
                type: number
              priorStdDev:
                type: number
            required:
              - metric
              - priorMean
              - priorStdDev
          description: Bayesian prior settings by metric.
        manualQualityScores:
          type: array
          items:
            type: object
            properties:
              criteriaName:
                oneOf:
                  - type: string
                    enum:
                      - HYPOTHESIS_LENGTH
                      - BALANCED_EXPOSURE
                      - PRIMARY_METRICS_LENGTH
                      - COMPARISON_CORRECTION
                      - GUARDRAIL_METRIC_TAGS
                      - SUFFICIENT_SAMPLE
                      - POWER_ANALYSIS
                      - SEQUENTIAL_TESTING
                  - type: string
              status:
                type: string
                enum:
                  - PASSED
                  - FAILED
                  - WARNING
              criteriaDescription:
                type: string
              score:
                type: number
              weight:
                type: number
            required:
              - criteriaName
              - status
              - criteriaDescription
              - score
              - weight
          description: >-
            Up to 10 manually set quality scores for an experiment. The scores
            and weights will be added to the existing weights and scores, and
            then weights will be renormalized to 100. This can be set via the
            Statsig Console API. If targeting a default check, the weight of the
            check will be updated, but not the status or description. A default
            score can be removed by setting the weight to 0. The default score
            identifiers are one of: HYPOTHESIS_LENGTH, BALANCED_EXPOSURE,
            PRIMARY_METRICS_LENGTH, COMPARISON_CORRECTION,
            GUARDRAIL_METRIC_TAGS, SUFFICIENT_SAMPLE, POWER_ANALYSIS,
            SEQUENTIAL_TESTING
        status:
          type: string
          enum:
            - active
            - setup
            - decision_made
            - abandoned
            - archived
            - experiment_stopped
            - assignment_stopped
          description: The current status of the experiment
        launchedGroupID:
          type: string
          nullable: true
          description: ID of the launched group, null otherwise
        assignmentSourceName:
          type: string
        assignmentSourceExperimentName:
          type: string
          description: Name of the source experiment for assignment
        isAnalysisOnly:
          type: boolean
        allocationDuration:
          type: integer
          minimum: 1
          exclusiveMinimum: true
          nullable: true
          description: Warehouse Native Only - Allocation duration in days
          format: int64
        cohortedAnalysisDuration:
          type: integer
          minimum: 1
          exclusiveMinimum: true
          description: Warehouse Native Only - Cohorted analysis duration in days
          format: int64
        cohortedMetricsMatureAfterEnd:
          type: boolean
          description: >-
            Warehouse Native Only - Allow cohort metrics to mature after
            experiment end
        cohortWaitUntilEndToInclude:
          type: boolean
          description: >-
            Warehouse Native Only - Whether to filter to units whose experiment
            cohort analysis duration is complete, if cohortedAnalysisDuration
            exists
        fixedAnalysisDuration:
          type: integer
          minimum: 1
          exclusiveMinimum: true
          description: Fixed analysis duration in days
          format: int64
        scheduledReloadHour:
          type: integer
          minimum: 0
          maximum: 23
          nullable: true
          description: >-
            Warehouse Native only - UTC hour at which to run scheduled pulse
            loads
          format: int64
        scheduledReloadType:
          type: string
          enum:
            - full
            - incremental
          description: Warehouse Native only - reload type for scheduled reloads
        scheduledReloadDays:
          type: array
          items:
            type: integer
            minimum: 0
            maximum: 6
          nullable: true
          description: >-
            Warehouse Native only - days on which to run scheduled reloads from
            0 to 6, 0 meaning Sunday. Null to run reloads on all days.
        turboMode:
          type: boolean
          description: >-
            Warehouse Native only - whether to run scheduled reloads with Turbo
            mode.
        analysisEndTime:
          type: string
        assignmentSourceFilters:
          type: array
          items:
            type: object
            properties:
              column:
                type: string
                description: Column to filter on.
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
              values:
                type: array
                items:
                  type: string
                description: Optional array of values for the criterion to match against.
            required:
              - condition
          description: Array of criteria for filtering assignment sources.
        analyticsType:
          type: string
          nullable: true
        defaultSPRTPowerParam:
          type: number
          format: double
        defaultSPRTMDE:
          type: number
          format: double
        sprtBaselineMode:
          type: string
          enum:
            - manual
            - in_experiment_control
        sprtMDESettings:
          type: array
          items:
            type: object
            properties:
              metricKey:
                type: string
              groupSettings:
                type: array
                items:
                  type: object
                  properties:
                    groupKey:
                      type: string
                    mde:
                      type: number
                    stdDev:
                      type: number
                  required:
                    - groupKey
                    - mde
                    - stdDev
            required:
              - metricKey
              - groupSettings
        isSidecar:
          type: boolean
          description: Whether this is a Statsig Sidecar experiment.
        decisionReason:
          type: string
          nullable: true
        preComputedUserDimensions:
          type: array
          items:
            type: object
            properties:
              propertySource:
                type: string
              name:
                type: string
            required:
              - name
          description: User dimensions that will be computed for every metric in WHN
        cureCovariates:
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
          description: CURE Covariates to use in this experiment
        stratifiedSampling:
          type: object
          properties:
            status:
              type: string
              enum:
                - pending
                - success
                - error
            metric:
              type: object
              properties:
                name:
                  type: string
                startDate:
                  type: string
                endDate:
                  type: string
              required:
                - name
                - startDate
                - endDate
            entityPropertySource:
              type: object
              properties:
                propertySourceName:
                  type: string
                column:
                  type: string
              required:
                - propertySourceName
                - column
            csv:
              type: object
              properties:
                original:
                  type: string
                identifier:
                  type: string
              required:
                - original
                - identifier
          required:
            - status
          nullable: true
          description: The stratified sampling settings for the experiment
        enabledNonProdEnvironments:
          type: array
          items:
            type: string
        subtype:
          type: string
          enum:
            - conversion
            - reactivation
            - retention
        externalExperimentName:
          type: string
        layerID:
          type: string
          nullable: true
        startTime:
          type: number
          nullable: true
          format: double
        endTime:
          type: number
          nullable: true
          format: double
        decisionTime:
          type: number
          nullable: true
          format: double
        healthChecks:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
              description:
                type: string
              status:
                type: string
                enum:
                  - PASSED
                  - FAILED
                  - WAITING
                  - WARNING
                  - NOT_APPLIED
              metadata:
                type: object
                properties:
                  type:
                    type: string
                  lastPulseLoadTime:
                    type: number
                  crossoverPercent:
                    type: number
                  assignmentSourceID:
                    type: string
                  assignmentSourceName:
                    type: string
                  foreignExperimentID:
                    type: string
                  deduplication_rate:
                    type: number
                  deduplication_rates:
                    type: array
                    items:
                      type: object
                      properties:
                        group_id:
                          type: string
                        rate:
                          type: number
                        group_name:
                          type: string
                      required:
                        - group_id
                        - rate
                        - group_name
                  primary_id_type:
                    type: string
                  secondary_id_type:
                    type: string
                  missingMetrics:
                    type: array
                    items:
                      type: string
                  metrics:
                    type: array
                    items:
                      type: object
                      properties:
                        metric_name:
                          type: string
                        earliest_date:
                          type: string
                          format: date-time
                          nullable: true
                        latest_date:
                          type: string
                          format: date-time
                          nullable: true
                      required:
                        - metric_name
                        - earliest_date
                        - latest_date
                  lastUpdatedDs:
                    type: string
                  groups:
                    type: array
                    items:
                      type: object
                      properties:
                        groupID:
                          type: string
                        groupName:
                          type: string
                        status:
                          type: string
                          enum:
                            - PASSED
                            - FAILED
                            - WAITING
                            - WARNING
                            - NOT_APPLIED
                        metrics:
                          type: array
                          items:
                            type: object
                            properties:
                              metricKey:
                                type: string
                              metricTitle:
                                type: string
                              status:
                                type: string
                                enum:
                                  - PASSED
                                  - FAILED
                                  - WAITING
                                  - WARNING
                                  - NOT_APPLIED
                            required:
                              - metricKey
                              - metricTitle
                              - status
                      required:
                        - groupID
                        - groupName
                        - status
                        - metrics
                required:
                  - type
                  - primary_id_type
              type:
                type: string
                enum:
                  - has_checks
                  - has_valid_unit_type
                  - has_balanced_exposures
                  - has_event_metrics
                  - has_pulse_metrics
                  - assignment_health
                  - has_crossover
                  - has_exposures
                  - has_recent_exposures_for_analyze_whn
                  - user_metrics_exist
                  - deduplication_rate
                  - deduplication_rate_group_level
                  - windowed_metrics_have_outliers
                  - exposures_data_is_behind
                  - pre_experimental_bias_check
                  - segments_of_interest_analysis
                  - has_changed_parameter
                  - metric_history_for_topline_impact
                  - default_value_mismatch
                  - has_data_gaps
                  - has_correct_target_app
                  - has_dag_failures
                  - has_exploration_completed
                  - autotune_has_outcomes
                  - metric_stability
            required:
              - name
              - description
              - status
        healthCheckStatus:
          type: string
          enum:
            - PASSED
            - FAILED
            - WAITING
            - WARNING
            - NOT_APPLIED
          description: Overall health check status
        experimentType:
          type: string
          enum:
            - BASE
            - GEO
            - SWITCHBACK
            - PROMPT
            - SIDECAR
            - GRID_SEARCH
          description: The type of experiment
        isStale:
          type: boolean
          description: >-
            Whether the experiment is considered stale (e.g. in progress or
            decision-made and not modified in 30+ days).
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
          description: >-
            Schema for owner data including ID, type, name. Note that if Entity
            is created by CONSOLE API, owner will be undefined.
          example:
            ownerID: user123
            ownerType: USER
            ownerName: John Doe
            ownerEmail: owner123@test.com
          nullable: true
        inlineTargetingRulesJSON:
          type: string
          nullable: true
          description: A raw JSON string of the inline targeting rules
        inlineTargetingRules:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
                description: The name of this rule.
              passPercentage:
                type: number
                minimum: 0
                maximum: 100
                multipleOf: 0.01
                description: >-
                  Of the users that meet the conditions of this rule, what
                  percent should return true.
              conditions:
                type: array
                items:
                  type: object
                  properties:
                    targetValue:
                      oneOf:
                        - type: array
                          items:
                            type: string
                        - type: array
                          items:
                            type: number
                        - type: string
                        - type: number
                      nullable: true
                    operator:
                      type: string
                    field:
                      type: string
                      nullable: true
                    customID:
                      type: string
                      nullable: true
                    type:
                      type: string
                      enum:
                        - app_version
                        - browser_name
                        - browser_version
                        - country
                        - custom_field
                        - email
                        - environment_tier
                        - fails_gate
                        - fails_segment
                        - ip_address
                        - locale
                        - os_name
                        - os_version
                        - passes_gate
                        - passes_segment
                        - public
                        - time
                        - unit_id
                        - user_id
                        - user_agent
                        - url
                        - javascript
                        - device_model
                        - target_app
                        - experiment_group
                  required:
                    - type
                description: An array of Condition objects.
              environments:
                type: array
                items:
                  type: string
                nullable: true
                description: The environments this rule is enabled for.
              id:
                type: string
                description: The Statsig ID of this rule.
              baseID:
                type: string
                description: >-
                  The base ID of this rule, i.e. without any added metadata.
                  Will remain the exact same throughout
              returnValue:
                type: object
                additionalProperties: {}
                description: The return value of the rule.
              completedAutomatedRollouts:
                type: array
                items:
                  type: object
                  properties:
                    time:
                      type: number
                    passPercent:
                      type: number
                  required:
                    - passPercent
                readOnly: true
                description: >-
                  Read-only: Automated rollout phases that have already
                  completed.
              pendingAutomatedRollouts:
                type: array
                items:
                  type: object
                  properties:
                    time:
                      type: number
                    passPercent:
                      type: number
                  required:
                    - passPercent
                readOnly: true
                description: >-
                  Read-only: Automated rollout phases that are scheduled but not
                  yet complete.
            required:
              - name
              - passPercentage
              - conditions
          description: A formatted array of the inline targeting rules
        summarySections:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
              content:
                type: string
                nullable: true
            required:
              - name
              - content
          nullable: true
      required:
        - id
        - idType
        - description
        - lastModifierID
        - lastModifiedTime
        - lastModifierEmail
        - lastModifierName
        - createdTime
        - creatorName
        - tags
        - hypothesis
        - groups
        - allocation
        - primaryMetrics
        - secondaryMetrics
        - targetingGateID
        - bonferroniCorrection
        - defaultConfidenceInterval
        - status
        - decisionReason
        - layerID
        - startTime
        - endTime
        - decisionTime
        - healthCheckStatus
        - experimentType
        - isStale
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
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).