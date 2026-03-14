# Source: https://docs.statsig.com/api-reference/holdouts/retrieve-pulse-results.md

# Source: https://docs.statsig.com/api-reference/gates/retrieve-pulse-results.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve Pulse Results



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/gates/{id}/rules/{ruleID}/pulse_results
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
  /console/v1/gates/{id}/rules/{ruleID}/pulse_results:
    get:
      tags:
        - Gates
      summary: Retrieve Pulse Results
      parameters:
        - name: id
          required: true
          in: path
          description: Gate ID
          schema:
            type: string
        - name: ruleID
          required: true
          in: path
          description: Rule ID
          schema:
            type: string
        - name: cuped
          required: false
          in: query
          description: Whether to apply CUPED. Allowed values are "true" or "false".
          schema:
            type: string
        - name: confidence
          required: false
          in: query
          description: Confidence interval (0-100)
          schema:
            type: string
      responses:
        '200':
          description: Get Pulse Results Success
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/SingleDataResponse'
                  - properties:
                      data:
                        $ref: '#/components/schemas/GatePulseResultsDto'
                example:
                  message: Successfully loaded Pulse Results
                  data:
                    ds: '2024-09-12'
                    monitoringMetrics:
                      - metricID: conversion_rate
                        metricName: Conversion Rate
                        directionality: increase
                        absoluteChange: 0.0025
                        confidenceIntervalDelta: 0.0015
                        percentChange: 2.5
                        percentConfidenceIntervalDelta: 1.5
                        percentSequentialTestingConfidenceIntervalDelta: -0.8
                        testMean: 0.1025
                        controlMean: 0.1
                        testStd: 0.0012
                        controlStd: 0.0011
                        testUnits: 1500
                        controlUnits: 1480
                        pValue: 0.045
                      - metricID: user_engagement
                        metricName: User Engagement Score
                        directionality: increase
                        absoluteChange: 0.15
                        confidenceIntervalDelta: 0.08
                        percentChange: 3.2
                        percentConfidenceIntervalDelta: 1.7
                        percentSequentialTestingConfidenceIntervalDelta: -2.1
                        testMean: 4.85
                        controlMean: 4.7
                        testStd: 0.35
                        controlStd: 0.32
                        testUnits: 2200
                        controlUnits: 2150
                        pValue: 0.025
              example:
                message: Successfully loaded Pulse Results
                data:
                  ds: '2024-09-12'
                  monitoringMetrics:
                    - metricID: conversion_rate
                      metricName: Conversion Rate
                      directionality: increase
                      absoluteChange: 0.0025
                      confidenceIntervalDelta: 0.0015
                      percentChange: 2.5
                      percentConfidenceIntervalDelta: 1.5
                      percentSequentialTestingConfidenceIntervalDelta: -0.8
                      testMean: 0.1025
                      controlMean: 0.1
                      testStd: 0.0012
                      controlStd: 0.0011
                      testUnits: 1500
                      controlUnits: 1480
                      pValue: 0.045
                    - metricID: user_engagement
                      metricName: User Engagement Score
                      directionality: increase
                      absoluteChange: 0.15
                      confidenceIntervalDelta: 0.08
                      percentChange: 3.2
                      percentConfidenceIntervalDelta: 1.7
                      percentSequentialTestingConfidenceIntervalDelta: -2.1
                      testMean: 4.85
                      controlMean: 4.7
                      testStd: 0.35
                      controlStd: 0.32
                      testUnits: 2200
                      controlUnits: 2150
                      pValue: 0.025
      security:
        - STATSIG-API-KEY: []
components:
  schemas:
    SingleDataResponse:
      type: object
      properties:
        message:
          type: string
          description: A simple string explaining the result of the operation.
        data:
          type: object
          description: A single result.
      required:
        - message
        - data
    GatePulseResultsDto:
      type: object
      properties:
        ds:
          type: string
        monitoringMetrics:
          type: array
          items:
            type: object
            properties:
              metricID:
                type: string
              metricName:
                type: string
              directionality:
                type: string
                enum:
                  - increase
                  - decrease
                description: >-
                  Indicates the desired change direction for the metric. Use
                  "increase" for positive changes and "decrease" for negative
                  changes.
                example: increase
              absoluteChange:
                type: number
              confidenceIntervalDelta:
                type: number
                description: Absolute confidence interval delta
              confidenceInterval:
                type: object
                properties:
                  lower:
                    type: number
                  upper:
                    type: number
                required:
                  - lower
                  - upper
                additionalProperties: false
                description: Confidence interval bounds
                example:
                  lower: -1.33
                  upper: 1.33
              percentChange:
                type: number
              sequentialTestingConfidenceIntervalDelta:
                type: number
              sequentialTestingConfidenceInterval:
                type: object
                properties:
                  lower:
                    type: number
                  upper:
                    type: number
                required:
                  - lower
                  - upper
                additionalProperties: false
                description: Confidence interval bounds
                example:
                  lower: -1.33
                  upper: 1.33
              percentConfidenceIntervalDelta:
                type: number
              percentConfidenceInterval:
                type: object
                properties:
                  lower:
                    type: number
                  upper:
                    type: number
                required:
                  - lower
                  - upper
                additionalProperties: false
                description: Confidence interval bounds
                example:
                  lower: -1.33
                  upper: 1.33
              percentSequentialTestingConfidenceIntervalDelta:
                type: number
              percentSequentialTestingConfidenceInterval:
                type: object
                properties:
                  lower:
                    type: number
                  upper:
                    type: number
                required:
                  - lower
                  - upper
                additionalProperties: false
                description: Confidence interval bounds
                example:
                  lower: -1.33
                  upper: 1.33
              testMean:
                type: number
              controlMean:
                type: number
              testStd:
                type: number
              controlStd:
                type: number
              testUnits:
                type: number
              controlUnits:
                type: number
              pValue:
                type: number
              reversePower:
                type: number
              absoluteToplineImpact:
                type: number
              absoluteToplineImpactDelta:
                type: number
              relativeToplineImpact:
                type: number
              relativeToplineImpactDelta:
                type: number
              projectedAbsoluteToplineImpact:
                type: number
              projectedAbsoluteToplineImpactDelta:
                type: number
              projectedRelativeToplineImpact:
                type: number
              projectedRelativeToplineImpactDelta:
                type: number
            required:
              - metricID
              - metricName
              - directionality
            additionalProperties: false
      required:
        - ds
        - monitoringMetrics
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).