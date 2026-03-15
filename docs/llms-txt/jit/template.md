# Source: https://docs.jit.io/reference/template.md

# List available policies templates

Returns a list of all available policies with their metadata

**Requires the following permission:**
`jit.policies.read`

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "Jit Public APIs",
    "description": "Jit Public APIs.\n\nThe API requires that you log in first and obtain a JWT authentication bearer token:\n\nJIT Platform generates CLIENT_ID and SECRET under `Settings -> Users & Permissions -> API Tokens`\n\n For more information, refer to [Users and Permissions](https://docs.jit.io/docs/managing-users#generating-api-tokens)",
    "version": "1",
    "termsOfService": "https://www.jit.io/legal/terms"
  },
  "servers": [
    {
      "url": "https://api.jit.io",
      "description": "Jit API domain"
    }
  ],
  "externalDocs": {
    "url": "https://docs.jit.io/docs",
    "description": "Jit docs"
  },
  "security": [
    {
      "bearerAuth": []
    }
  ],
  "paths": {
    "/policies/": {
      "get": {
        "summary": "List available policies templates",
        "description": "Returns a list of all available policies with their metadata\n\n**Requires the following permission:**\n`jit.policies.read`",
        "operationId": "template",
        "parameters": [
          {
            "name": "enabled_rules_count",
            "in": "query",
            "description": "Include the count of enabled rules for each policy",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/enabled_rules_count"
            }
          }
        ],
        "tags": [
          "Policies"
        ],
        "responses": {
          "200": {
            "description": "List of policies returned successfully",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PoliciesTemplates"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin"
                }
              },
              "Access-Control-Allow-Credentials": {
                "description": "The Access-Control-Allow-Credentials response header tells browsers whether to expose the response to the frontend JavaScript code when the request's credentials mode ([Request.credentials](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)) is include. - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Credentials"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UnauthorizedAuthorizerError"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin"
                }
              },
              "Access-Control-Allow-Credentials": {
                "description": "The Access-Control-Allow-Credentials response header tells browsers whether to expose the response to the frontend JavaScript code when the request's credentials mode ([Request.credentials](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)) is include. - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Credentials"
                }
              }
            }
          },
          "403": {
            "description": "Forbidden",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ForbiddenError"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin"
                }
              },
              "Access-Control-Allow-Credentials": {
                "description": "The Access-Control-Allow-Credentials response header tells browsers whether to expose the response to the frontend JavaScript code when the request's credentials mode ([Request.credentials](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)) is include. - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Credentials"
                }
              }
            }
          },
          "500": {
            "description": "Internal server error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/InternalServerError"
                }
              }
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "description": "The Access-Control-Allow-Origin response header indicates whether the response can be shared with requesting code from the given [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin). - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Origin"
                }
              },
              "Access-Control-Allow-Credentials": {
                "description": "The Access-Control-Allow-Credentials response header tells browsers whether to expose the response to the frontend JavaScript code when the request's credentials mode ([Request.credentials](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)) is include. - [MDN Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)",
                "schema": {
                  "$ref": "#/components/schemas/Access-Control-Allow-Credentials"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "ForbiddenError": {
        "title": "ForbiddenErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "FORBIDDEN",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable error message.",
            "example": "Request is missing the required permissions.",
            "type": "string"
          },
          "missing_permissions": {
            "title": "Missing permissions",
            "description": "List of missing permissions.",
            "nullable": true,
            "example": [
              "jit.category.write",
              "jit.category.read"
            ],
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "InternalServerError": {
        "title": "InternalErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "INTERNAL_SERVER_ERROR",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable error message.",
            "example": "Some error message indicating the issue that occurred",
            "type": "string"
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "UnauthorizedAuthorizerError": {
        "title": "UnauthorizedAuthorizerErrorResponse",
        "type": "object",
        "properties": {
          "Message": {
            "title": "Error message",
            "description": "Human readable error message.\n\n**Important**: This schema does not contain `error` field.",
            "example": "Unauthorized",
            "type": "string"
          }
        },
        "required": [
          "Message"
        ]
      },
      "Access-Control-Allow-Origin": {
        "type": "string",
        "default": "*",
        "example": "https://developer.mozilla.org"
      },
      "Access-Control-Allow-Credentials": {
        "type": "boolean",
        "default": true
      },
      "PoliciesTemplates": {
        "title": "PoliciesTemplates",
        "type": "array",
        "items": {
          "title": "Policy",
          "type": "object",
          "properties": {
            "policy_slug": {
              "title": "Policy Slug",
              "type": "string"
            },
            "response_type": {
              "title": "PolicyResponseType",
              "description": "An enumeration.",
              "enum": [
                "boolean"
              ],
              "type": "string"
            },
            "display": {
              "title": "PolicyDisplay",
              "type": "object",
              "properties": {
                "display_name": {
                  "title": "Display Name",
                  "type": "string"
                },
                "description": {
                  "title": "Description",
                  "type": "string"
                },
                "icon": {
                  "title": "Icon",
                  "type": "string"
                },
                "docs_link": {
                  "title": "Docs Link",
                  "type": "string"
                }
              },
              "required": [
                "display_name",
                "description",
                "icon"
              ]
            },
            "rule_templates": {
              "title": "Rule Templates",
              "type": "array",
              "items": {
                "title": "RuleTemplate",
                "type": "object",
                "properties": {
                  "filter_conditions": {
                    "title": "Filter Conditions",
                    "type": "string"
                  },
                  "inputs": {
                    "title": "RuleTemplateInputs",
                    "type": "object",
                    "properties": {
                      "condition_entity": {
                        "title": "InputField",
                        "type": "object",
                        "properties": {
                          "label": {
                            "title": "Label",
                            "type": "string"
                          },
                          "input_type": {
                            "title": "Input Type",
                            "type": "string"
                          },
                          "options": {
                            "title": "Options",
                            "type": "array",
                            "items": {
                              "title": "Option",
                              "type": "object",
                              "properties": {
                                "value": {
                                  "title": "Value",
                                  "type": "string"
                                },
                                "label": {
                                  "title": "Label",
                                  "type": "string"
                                }
                              },
                              "required": [
                                "value",
                                "label"
                              ]
                            }
                          },
                          "default_value": {
                            "title": "Default Value",
                            "anyOf": [
                              {
                                "title": "Option",
                                "type": "object",
                                "properties": {
                                  "value": {
                                    "title": "Value",
                                    "type": "string"
                                  },
                                  "label": {
                                    "title": "Label",
                                    "type": "string"
                                  }
                                },
                                "required": [
                                  "value",
                                  "label"
                                ]
                              },
                              {
                                "type": "array",
                                "items": {
                                  "title": "Option",
                                  "type": "object",
                                  "properties": {
                                    "value": {
                                      "title": "Value",
                                      "type": "string"
                                    },
                                    "label": {
                                      "title": "Label",
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "value",
                                    "label"
                                  ]
                                }
                              }
                            ]
                          },
                          "required": {
                            "title": "Required",
                            "type": "boolean"
                          },
                          "multi": {
                            "title": "Multi",
                            "type": "boolean"
                          },
                          "depends_on": {
                            "title": "Depends On",
                            "type": "string"
                          },
                          "dynamic_config": {
                            "title": "Dynamic Config"
                          },
                          "placeholder": {
                            "title": "Placeholder",
                            "type": "string"
                          },
                          "options_callback": {
                            "title": "Options Callback",
                            "type": "string"
                          }
                        },
                        "required": [
                          "label"
                        ]
                      },
                      "condition_attribute": {
                        "title": "InputField",
                        "type": "object",
                        "properties": {
                          "label": {
                            "title": "Label",
                            "type": "string"
                          },
                          "input_type": {
                            "title": "Input Type",
                            "type": "string"
                          },
                          "options": {
                            "title": "Options",
                            "type": "array",
                            "items": {
                              "title": "Option",
                              "type": "object",
                              "properties": {
                                "value": {
                                  "title": "Value",
                                  "type": "string"
                                },
                                "label": {
                                  "title": "Label",
                                  "type": "string"
                                }
                              },
                              "required": [
                                "value",
                                "label"
                              ]
                            }
                          },
                          "default_value": {
                            "title": "Default Value",
                            "anyOf": [
                              {
                                "title": "Option",
                                "type": "object",
                                "properties": {
                                  "value": {
                                    "title": "Value",
                                    "type": "string"
                                  },
                                  "label": {
                                    "title": "Label",
                                    "type": "string"
                                  }
                                },
                                "required": [
                                  "value",
                                  "label"
                                ]
                              },
                              {
                                "type": "array",
                                "items": {
                                  "title": "Option",
                                  "type": "object",
                                  "properties": {
                                    "value": {
                                      "title": "Value",
                                      "type": "string"
                                    },
                                    "label": {
                                      "title": "Label",
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "value",
                                    "label"
                                  ]
                                }
                              }
                            ]
                          },
                          "required": {
                            "title": "Required",
                            "type": "boolean"
                          },
                          "multi": {
                            "title": "Multi",
                            "type": "boolean"
                          },
                          "depends_on": {
                            "title": "Depends On",
                            "type": "string"
                          },
                          "dynamic_config": {
                            "title": "Dynamic Config"
                          },
                          "placeholder": {
                            "title": "Placeholder",
                            "type": "string"
                          },
                          "options_callback": {
                            "title": "Options Callback",
                            "type": "string"
                          }
                        },
                        "required": [
                          "label"
                        ]
                      },
                      "condition_operator": {
                        "title": "InputField",
                        "type": "object",
                        "properties": {
                          "label": {
                            "title": "Label",
                            "type": "string"
                          },
                          "input_type": {
                            "title": "Input Type",
                            "type": "string"
                          },
                          "options": {
                            "title": "Options",
                            "type": "array",
                            "items": {
                              "title": "Option",
                              "type": "object",
                              "properties": {
                                "value": {
                                  "title": "Value",
                                  "type": "string"
                                },
                                "label": {
                                  "title": "Label",
                                  "type": "string"
                                }
                              },
                              "required": [
                                "value",
                                "label"
                              ]
                            }
                          },
                          "default_value": {
                            "title": "Default Value",
                            "anyOf": [
                              {
                                "title": "Option",
                                "type": "object",
                                "properties": {
                                  "value": {
                                    "title": "Value",
                                    "type": "string"
                                  },
                                  "label": {
                                    "title": "Label",
                                    "type": "string"
                                  }
                                },
                                "required": [
                                  "value",
                                  "label"
                                ]
                              },
                              {
                                "type": "array",
                                "items": {
                                  "title": "Option",
                                  "type": "object",
                                  "properties": {
                                    "value": {
                                      "title": "Value",
                                      "type": "string"
                                    },
                                    "label": {
                                      "title": "Label",
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "value",
                                    "label"
                                  ]
                                }
                              }
                            ]
                          },
                          "required": {
                            "title": "Required",
                            "type": "boolean"
                          },
                          "multi": {
                            "title": "Multi",
                            "type": "boolean"
                          },
                          "depends_on": {
                            "title": "Depends On",
                            "type": "string"
                          },
                          "dynamic_config": {
                            "title": "Dynamic Config"
                          },
                          "placeholder": {
                            "title": "Placeholder",
                            "type": "string"
                          },
                          "options_callback": {
                            "title": "Options Callback",
                            "type": "string"
                          }
                        },
                        "required": [
                          "label"
                        ]
                      },
                      "condition_value": {
                        "title": "InputField",
                        "type": "object",
                        "properties": {
                          "label": {
                            "title": "Label",
                            "type": "string"
                          },
                          "input_type": {
                            "title": "Input Type",
                            "type": "string"
                          },
                          "options": {
                            "title": "Options",
                            "type": "array",
                            "items": {
                              "title": "Option",
                              "type": "object",
                              "properties": {
                                "value": {
                                  "title": "Value",
                                  "type": "string"
                                },
                                "label": {
                                  "title": "Label",
                                  "type": "string"
                                }
                              },
                              "required": [
                                "value",
                                "label"
                              ]
                            }
                          },
                          "default_value": {
                            "title": "Default Value",
                            "anyOf": [
                              {
                                "title": "Option",
                                "type": "object",
                                "properties": {
                                  "value": {
                                    "title": "Value",
                                    "type": "string"
                                  },
                                  "label": {
                                    "title": "Label",
                                    "type": "string"
                                  }
                                },
                                "required": [
                                  "value",
                                  "label"
                                ]
                              },
                              {
                                "type": "array",
                                "items": {
                                  "title": "Option",
                                  "type": "object",
                                  "properties": {
                                    "value": {
                                      "title": "Value",
                                      "type": "string"
                                    },
                                    "label": {
                                      "title": "Label",
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "value",
                                    "label"
                                  ]
                                }
                              }
                            ]
                          },
                          "required": {
                            "title": "Required",
                            "type": "boolean"
                          },
                          "multi": {
                            "title": "Multi",
                            "type": "boolean"
                          },
                          "depends_on": {
                            "title": "Depends On",
                            "type": "string"
                          },
                          "dynamic_config": {
                            "title": "Dynamic Config"
                          },
                          "placeholder": {
                            "title": "Placeholder",
                            "type": "string"
                          },
                          "options_callback": {
                            "title": "Options Callback",
                            "type": "string"
                          }
                        },
                        "required": [
                          "label"
                        ]
                      },
                      "user_identity_type": {
                        "title": "InputField",
                        "type": "object",
                        "properties": {
                          "label": {
                            "title": "Label",
                            "type": "string"
                          },
                          "input_type": {
                            "title": "Input Type",
                            "type": "string"
                          },
                          "options": {
                            "title": "Options",
                            "type": "array",
                            "items": {
                              "title": "Option",
                              "type": "object",
                              "properties": {
                                "value": {
                                  "title": "Value",
                                  "type": "string"
                                },
                                "label": {
                                  "title": "Label",
                                  "type": "string"
                                }
                              },
                              "required": [
                                "value",
                                "label"
                              ]
                            }
                          },
                          "default_value": {
                            "title": "Default Value",
                            "anyOf": [
                              {
                                "title": "Option",
                                "type": "object",
                                "properties": {
                                  "value": {
                                    "title": "Value",
                                    "type": "string"
                                  },
                                  "label": {
                                    "title": "Label",
                                    "type": "string"
                                  }
                                },
                                "required": [
                                  "value",
                                  "label"
                                ]
                              },
                              {
                                "type": "array",
                                "items": {
                                  "title": "Option",
                                  "type": "object",
                                  "properties": {
                                    "value": {
                                      "title": "Value",
                                      "type": "string"
                                    },
                                    "label": {
                                      "title": "Label",
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "value",
                                    "label"
                                  ]
                                }
                              }
                            ]
                          },
                          "required": {
                            "title": "Required",
                            "type": "boolean"
                          },
                          "multi": {
                            "title": "Multi",
                            "type": "boolean"
                          },
                          "depends_on": {
                            "title": "Depends On",
                            "type": "string"
                          },
                          "dynamic_config": {
                            "title": "Dynamic Config"
                          },
                          "placeholder": {
                            "title": "Placeholder",
                            "type": "string"
                          },
                          "options_callback": {
                            "title": "Options Callback",
                            "type": "string"
                          }
                        },
                        "required": [
                          "label"
                        ]
                      },
                      "user_identity_value": {
                        "title": "InputField",
                        "type": "object",
                        "properties": {
                          "label": {
                            "title": "Label",
                            "type": "string"
                          },
                          "input_type": {
                            "title": "Input Type",
                            "type": "string"
                          },
                          "options": {
                            "title": "Options",
                            "type": "array",
                            "items": {
                              "title": "Option",
                              "type": "object",
                              "properties": {
                                "value": {
                                  "title": "Value",
                                  "type": "string"
                                },
                                "label": {
                                  "title": "Label",
                                  "type": "string"
                                }
                              },
                              "required": [
                                "value",
                                "label"
                              ]
                            }
                          },
                          "default_value": {
                            "title": "Default Value",
                            "anyOf": [
                              {
                                "title": "Option",
                                "type": "object",
                                "properties": {
                                  "value": {
                                    "title": "Value",
                                    "type": "string"
                                  },
                                  "label": {
                                    "title": "Label",
                                    "type": "string"
                                  }
                                },
                                "required": [
                                  "value",
                                  "label"
                                ]
                              },
                              {
                                "type": "array",
                                "items": {
                                  "title": "Option",
                                  "type": "object",
                                  "properties": {
                                    "value": {
                                      "title": "Value",
                                      "type": "string"
                                    },
                                    "label": {
                                      "title": "Label",
                                      "type": "string"
                                    }
                                  },
                                  "required": [
                                    "value",
                                    "label"
                                  ]
                                }
                              }
                            ]
                          },
                          "required": {
                            "title": "Required",
                            "type": "boolean"
                          },
                          "multi": {
                            "title": "Multi",
                            "type": "boolean"
                          },
                          "depends_on": {
                            "title": "Depends On",
                            "type": "string"
                          },
                          "dynamic_config": {
                            "title": "Dynamic Config"
                          },
                          "placeholder": {
                            "title": "Placeholder",
                            "type": "string"
                          },
                          "options_callback": {
                            "title": "Options Callback",
                            "type": "string"
                          }
                        },
                        "required": [
                          "label"
                        ]
                      }
                    },
                    "required": [
                      "condition_entity",
                      "condition_attribute",
                      "condition_operator",
                      "condition_value"
                    ]
                  },
                  "slug": {
                    "title": "Slug",
                    "type": "string"
                  },
                  "base_condition": {
                    "title": "Base Condition",
                    "type": "string"
                  }
                },
                "required": [
                  "filter_conditions",
                  "inputs",
                  "slug",
                  "base_condition"
                ]
              }
            },
            "dynamic_data": {
              "title": "DynamicData",
              "type": "object",
              "properties": {
                "enabled_rules_count": {
                  "title": "Enabled Rules Count",
                  "type": "integer"
                }
              }
            }
          },
          "required": [
            "policy_slug",
            "response_type",
            "display"
          ]
        }
      },
      "enabled_rules_count": {
        "title": "ParsingModel[bool]",
        "type": "boolean"
      }
    },
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "_id": {
    "buffer": {
      "0": 103,
      "1": 96,
      "2": 119,
      "3": 178,
      "4": 114,
      "5": 109,
      "6": 158,
      "7": 128,
      "8": 238,
      "9": 252,
      "10": 241,
      "11": 194
    }
  }
}
```