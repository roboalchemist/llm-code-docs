# Source: https://developer.mixpanel.com/reference/funnels-query.md

# Query Saved Report

Get data for a funnel. The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "Query API",
    "description": "query api",
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "contact": {
      "url": "https://mixpanel.com/get-support"
    },
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "https://{regionAndDomain}.com/api/query",
      "description": "Mixpanel's calculated data API",
      "variables": {
        "regionAndDomain": {
          "default": "mixpanel",
          "enum": [
            "mixpanel",
            "eu.mixpanel",
            "in.mixpanel"
          ],
          "description": "The server location to be used:\n  * `mixpanel` - The default (US) servers used for most projects\n  * `eu.mixpanel` - EU servers if you are enrolled in EU Data Residency\n  * `in.mixpanel` - India servers if you are enrolled in India Data Residency\n"
        }
      }
    }
  ],
  "security": [
    {
      "ServiceAccount": []
    },
    {
      "ProjectSecret": []
    }
  ],
  "tags": [
    {
      "name": "Funnels",
      "description": "Query data shown in your Funnels reports"
    }
  ],
  "paths": {
    "/funnels": {
      "get": {
        "operationId": "funnels-query",
        "summary": "Query Saved Report",
        "tags": [
          "Funnels"
        ],
        "description": "Get data for a funnel. The Query API has a rate limit of 60 queries per hour and a maximum of 5 concurrent queries.",
        "parameters": [
          {
            "$ref": "#/components/parameters/projectId"
          },
          {
            "$ref": "#/components/parameters/workspaceId"
          },
          {
            "in": "query",
            "name": "funnel_id",
            "schema": {
              "type": "integer"
            },
            "description": "The funnel that you wish to get data for.",
            "required": true
          },
          {
            "$ref": "#/components/parameters/fromDate"
          },
          {
            "$ref": "#/components/parameters/toDate"
          },
          {
            "in": "query",
            "name": "length",
            "schema": {
              "type": "integer"
            },
            "description": "The number of units (defined by length_unit) each user has to complete the funnel, starting from the time they triggered the first step in the funnel. May not be greater than 90 days. Note that we will query for events past the end of to_date to look for funnel completions. This defaults to the value that was previously saved in the UI for this funnel."
          },
          {
            "in": "query",
            "name": "length_unit",
            "schema": {
              "type": "string",
              "enum": [
                "day",
                "hour",
                "minute",
                "second"
              ],
              "description": "The unit applied to the length parameter can be \"second\", \"minute\", \"hour\", or \"day\". Defaults to the value that was previously saved in the UI for this funnel.",
              "example": "day"
            }
          },
          {
            "in": "query",
            "name": "interval",
            "schema": {
              "type": "integer"
            },
            "description": "The number of days you want each bucket to contain. The default value is 1."
          },
          {
            "in": "query",
            "name": "unit",
            "schema": {
              "type": "string",
              "enum": [
                "day",
                "week",
                "month"
              ]
            },
            "description": "This is an alternate way of specifying interval and can be \"day\", \"week\", or \"month\"."
          },
          {
            "$ref": "#/components/parameters/on"
          },
          {
            "$ref": "#/components/parameters/where"
          },
          {
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "integer"
            },
            "description": "Return the top property values. Defaults to 255 if not explicitly included. Maximum value 10,000. This parameter does nothing if \\\"on\\\" is not specified."
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "examples": {
                  "example": {
                    "value": {
                      "meta": {
                        "dates": [
                          "2016-09-12",
                          "2016-09-19",
                          "2016-09-26"
                        ]
                      },
                      "data": {
                        "2016-09-12": {
                          "steps": [
                            {
                              "count": 32688,
                              "avg_time": 2,
                              "avg_time_from_start": 5,
                              "step_conv_ratio": 1,
                              "goal": "App Open",
                              "overall_conv_ratio": 1,
                              "event": "App Open"
                            },
                            {
                              "count": 20524,
                              "avg_time": 133,
                              "avg_time_from_start": 133,
                              "step_conv_ratio": 0.627875673029858,
                              "goal": "$custom_event:12345",
                              "step_label": "Game Played",
                              "custom_event": true,
                              "custom_event_id": 12345,
                              "overall_conv_ratio": 0.627875673029858,
                              "event": "$custom_event:12345"
                            }
                          ],
                          "analysis": {
                            "completion": 20524,
                            "starting_amount": 32688,
                            "steps": 2,
                            "worst": 1
                          }
                        },
                        "2016-09-19": {
                          "steps": [
                            {
                              "count": 32486,
                              "avg_time": 10,
                              "avg_time_from_start": 10,
                              "step_conv_ratio": 1,
                              "goal": "App Open",
                              "overall_conv_ratio": 1,
                              "event": "App Open"
                            },
                            {
                              "count": 20809,
                              "avg_time": 75,
                              "avg_time_from_start": 75,
                              "step_conv_ratio": 0.6405528535369082,
                              "goal": "$custom_event:12345",
                              "step_label": "Game Played",
                              "custom_event": true,
                              "custom_event_id": 12345,
                              "overall_conv_ratio": 0.6405528535369082,
                              "event": "$custom_event:12345"
                            }
                          ],
                          "analysis": {
                            "completion": 20809,
                            "starting_amount": 32486,
                            "steps": 2,
                            "worst": 1
                          }
                        },
                        "2016-09-26": {
                          "steps": [
                            {
                              "count": 16103,
                              "avg_time": 10,
                              "avg_time_from_start": 5,
                              "step_conv_ratio": 1,
                              "goal": "App Open",
                              "overall_conv_ratio": 1,
                              "event": "App Open"
                            },
                            {
                              "count": 12679,
                              "avg_time": 571,
                              "avg_time_from_start": 571,
                              "step_conv_ratio": 0.7873688132646091,
                              "goal": "$custom_event:12345",
                              "step_label": "Game Played",
                              "custom_event": true,
                              "custom_event_id": 12345,
                              "overall_conv_ratio": 0.7873688132646091,
                              "event": "$custom_event:12345"
                            }
                          ],
                          "analysis": {
                            "completion": 12679,
                            "starting_amount": 16103,
                            "steps": 2,
                            "worst": 1
                          }
                        }
                      }
                    }
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "meta": {
                      "type": "object",
                      "properties": {
                        "dates": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "description": "Date in YYYY-mm-dd format"
                          }
                        }
                      }
                    },
                    "data": {
                      "type": "object",
                      "additionalProperties": {
                        "type": "object",
                        "properties": {
                          "steps": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {
                                "count": {
                                  "type": "integer",
                                  "description": "Number of conversions."
                                },
                                "goal": {
                                  "type": "string",
                                  "description": "The name of the event"
                                },
                                "step_conv_ratio": {
                                  "type": "number",
                                  "format": "float",
                                  "description": "Conversion from previous step"
                                },
                                "overall_conv_ratio": {
                                  "type": "number",
                                  "format": "float",
                                  "description": "Conversion from start of funnel"
                                },
                                "avg_time": {
                                  "type": "integer",
                                  "description": "mean time to convert; null for step 0."
                                },
                                "avg_time_from_start": {
                                  "type": "integer",
                                  "description": "time to convert from first step."
                                },
                                "event": {
                                  "type": "string",
                                  "description": "The name of the event"
                                },
                                "step_label": {
                                  "type": "string",
                                  "description": "same as event OR custom event name"
                                },
                                "custom_event": {
                                  "type": "boolean",
                                  "description": "`true` if the event is a custom event, otherwise key is not present"
                                },
                                "custom_event_id": {
                                  "type": "integer",
                                  "description": "Only present if the event is a custom event."
                                }
                              }
                            }
                          },
                          "analysis": {
                            "type": "object",
                            "properties": {
                              "completion": {
                                "type": "integer",
                                "description": "Count in final step"
                              },
                              "starting_amount": {
                                "type": "integer",
                                "description": "Count in first step"
                              },
                              "steps": {
                                "type": "integer",
                                "description": "Number of steps"
                              },
                              "worst": {
                                "type": "integer",
                                "description": "Step with highest drop off"
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "ServiceAccount": {
        "type": "http",
        "scheme": "basic",
        "description": "Service Account"
      },
      "ProjectSecret": {
        "type": "http",
        "scheme": "basic",
        "description": "Project Secret"
      }
    },
    "parameters": {
      "workspaceId": {
        "in": "query",
        "name": "workspace_id",
        "schema": {
          "type": "integer"
        },
        "description": "The id of the workspace if applicable."
      },
      "on": {
        "in": "query",
        "name": "on",
        "schema": {
          "type": "string"
        },
        "description": "The property expression to segment the event on. See the [expression to segment](https://developer.mixpanel.com/reference/segmentation-expressions) below."
      },
      "where": {
        "in": "query",
        "name": "where",
        "schema": {
          "type": "string"
        },
        "description": "An expression to filter events by. See the [expression to segment](https://developer.mixpanel.com/reference/segmentation-expressions) below."
      },
      "projectId": {
        "in": "query",
        "name": "project_id",
        "schema": {
          "type": "integer"
        },
        "description": "Required if using service account to authenticate request.",
        "required": true
      },
      "fromDate": {
        "in": "query",
        "name": "from_date",
        "schema": {
          "type": "string"
        },
        "description": "The date in yyyy-mm-dd format to begin querying from. This date is inclusive.",
        "required": true
      },
      "toDate": {
        "in": "query",
        "name": "to_date",
        "schema": {
          "type": "string"
        },
        "description": "The date in yyyy-mm-dd format to query to. This date is inclusive.",
        "required": true
      }
    }
  },
  "x-readme-deploy-id": "query"
}
```