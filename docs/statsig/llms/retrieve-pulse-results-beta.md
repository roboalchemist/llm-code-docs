# Source: https://docs.statsig.com/api-reference/experiments/retrieve-pulse-results-beta.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve Pulse Results (Beta)



## OpenAPI

````yaml https://api.statsig.com/openapi/20240601.json get /console/v1/experiments/{id}/pulse_results
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
  /console/v1/experiments/{id}/pulse_results:
    get:
      tags:
        - Experiments
        - Experiments
      summary: Retrieve Pulse Results (Beta)
      parameters:
        - name: id
          required: true
          in: path
          description: id
          schema:
            type: string
        - name: control
          required: true
          in: query
          description: Control Group ID
          schema:
            type: string
        - name: test
          required: true
          in: query
          description: Test Group ID
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
        - name: applyBonferroniPerVariant
          required: false
          in: query
          description: >-
            Whether to apply Bonferroni Per Variant. Allowed values are "true"
            or "false".
          schema:
            type: string
        - name: applyBonferroniPerMetric
          required: false
          in: query
          description: >-
            Whether to apply Bonferroni Per Metric. Allowed values are "true" or
            "false".
          schema:
            type: string
        - name: bonferroniPrimaryMetricWeight
          required: false
          in: query
          description: α allocated to primary metrics
          schema:
            type: string
        - name: applyBenjaminiHochbergPerMetric
          required: false
          in: query
          description: >-
            Whether to apply Benjamini-Hochberg Correction Per Metric. Allowed
            values are "true" or "false".
          schema:
            type: string
        - name: applyBenjaminiHochbergPerVariant
          required: false
          in: query
          description: >-
            Whether to apply Benjamini-Hochberg Correction Per Variant. Allowed
            values are "true" or "false".
          schema:
            type: string
        - name: date
          required: false
          in: query
          description: Date for pulse results. format must be YYYY-MM-DD
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
                        $ref: '#/components/schemas/ExperimentPulseResultsDto'
                example:
                  message: Successfully loaded Pulse Results
                  data:
                    primaryMetrics:
                      - metricID: Purchase::user_warehouse
                        value: -0.5656598720428505
                        confidence_interval_delta: 1.3331521511820725
                        confidence_interval:
                          lower: -1.8988120232249
                          upper: 0.7674922791392
                        percent_change: -0.9104559464139017
                        percent_confidence_interval_delta: 2.145770565507353
                        percent_confidence_interval:
                          lower: -3.0562265119213
                          upper: 1.2353146190935
                        percent_sequential_testing_confidence_interval_delta: -1.6095466399726037
                        percent_sequential_testing_confidence_interval:
                          lower: 0.6990906935587
                          upper: -2.5200025863865
                        test_mean: 61.56363636363636
                        control_mean: 62.12929623567921
                        test_std: 0.7461734327711735
                        control_std: 0.7248273669644147
                        test_units: 1669
                        control_units: 1589
                        p_value: 0.7066986120589813
                    secondaryMetrics:
                      - metricID: Support Success Rate::user_warehouse
                        value: 0.0032568848232868985
                        confidence_interval_delta: 0.009120368109978388
                        confidence_interval:
                          lower: -0.00586348328669149
                          upper: 0.012377252933265286
                        percent_change: 0.4569873400680713
                        percent_confidence_interval_delta: 1.2797175795779019
                        percent_confidence_interval:
                          lower: -0.8227302395098306
                          upper: 1.736704919646
                        percent_sequential_testing_confidence_interval_delta: -140.31424654645156
                        percent_sequential_testing_confidence_interval:
                          lower: 140.77123388651964
                          upper: -139.8572592063835
                        test_mean: 0.7159428911362284
                        control_mean: 0.7126860063129415
                        test_std: 0.0038882253564431193
                        control_std: 0.003953024266669566
                        test_units: 4696
                        control_units: 4690
                        p_value: 0.5569502167465609
              example:
                message: Successfully loaded Pulse Results
                data:
                  primaryMetrics:
                    - metricID: Purchase::user_warehouse
                      value: -0.5656598720428505
                      confidence_interval_delta: 1.3331521511820725
                      confidence_interval:
                        lower: -1.8988120232249
                        upper: 0.7674922791392
                      percent_change: -0.9104559464139017
                      percent_confidence_interval_delta: 2.145770565507353
                      percent_confidence_interval:
                        lower: -3.0562265119213
                        upper: 1.2353146190935
                      percent_sequential_testing_confidence_interval_delta: -1.6095466399726037
                      percent_sequential_testing_confidence_interval:
                        lower: 0.6990906935587
                        upper: -2.5200025863865
                      test_mean: 61.56363636363636
                      control_mean: 62.12929623567921
                      test_std: 0.7461734327711735
                      control_std: 0.7248273669644147
                      test_units: 1669
                      control_units: 1589
                      p_value: 0.7066986120589813
                  secondaryMetrics:
                    - metricID: Support Success Rate::user_warehouse
                      value: 0.0032568848232868985
                      confidence_interval_delta: 0.009120368109978388
                      confidence_interval:
                        lower: -0.00586348328669149
                        upper: 0.012377252933265286
                      percent_change: 0.4569873400680713
                      percent_confidence_interval_delta: 1.2797175795779019
                      percent_confidence_interval:
                        lower: -0.8227302395098306
                        upper: 1.736704919646
                      percent_sequential_testing_confidence_interval_delta: -140.31424654645156
                      percent_sequential_testing_confidence_interval:
                        lower: 140.77123388651964
                        upper: -139.8572592063835
                      test_mean: 0.7159428911362284
                      control_mean: 0.7126860063129415
                      test_std: 0.0038882253564431193
                      control_std: 0.003953024266669566
                      test_units: 4696
                      control_units: 4690
                      p_value: 0.5569502167465609
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
    ExperimentPulseResultsDto:
      type: object
      properties:
        ds:
          type: string
        primaryMetrics:
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
        secondaryMetrics:
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
        otherMetrics:
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
        - primaryMetrics
        - secondaryMetrics
  securitySchemes:
    STATSIG-API-KEY:
      type: apiKey
      name: STATSIG-API-KEY
      in: header

````

Built with [Mintlify](https://mintlify.com).