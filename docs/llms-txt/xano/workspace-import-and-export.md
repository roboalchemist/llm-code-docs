# Source: https://docs.xano.com/xano-features/metadata-api/workspace-import-and-export.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Workspace Import And Export

<Info>
  **Before you proceed...**

  Workspace exports will only contain one branch which defaults to live unless you specify a branch in the request.

  Drafts are not exported.

  Imports overwrite the entire contents of the destination workspace.

  These endpoints will only function properly on **paid Xano plans**.
</Info>

<Warning>
  For large workspaces, import may not function properly using the Metadata API. In these cases, reach out to support and we can assist with the import process.
</Warning>

<Frame>
  <iframe width="1000" height="500" src="https://www.youtube.com/embed/Tv0puLXd6B0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />
</Frame>

### export the database table + branch schema

post

[https://xxfo-0dml-kzcl.dev.xano.io/api:meta/workspace/\{workspace\_id}/export-schema](https://xxfo-0dml-kzcl.dev.xano.io/api:meta/workspace/\{workspace_id}/export-schema)

Leave the `branch` parameter empty to indicate the current live branch. `password` is optional. If provided, will encrypt the export and will be required when importing the file. Required API Scope: Instance Workspace: Read

Authorizations

Path parameters

workspace\_idinteger · int64Required

Body

application/json

passwordstringOptional

branchstringOptional

Responses

200

Success!

application/json

Responseobject

400

Input Error. Check the request payload for issues.

401

Unauthorized

403

Access denied. Additional privileges are needed access the requested resource.

404

Not Found. The requested resource does not exist.

429

Rate Limited. Too many requests.

500

Unexpected error

post

/workspace/\{workspace\_id}/export-schema

HTTP

```bash  theme={null}
POST /api:meta/workspace/{workspace_id}/export-schema HTTP/1.1
Host: xxfo-0dml-kzcl.dev.xano.io
Authorization: Bearer JWT
Content-Type: application/json
Accept: */*
Content-Length: 27

{
  "branch": "",
  "password": ""
}
```

application/json

Test it

200

Success!

```
{}
```

### export the workspace and content

post

[https://xxfo-0dml-kzcl.dev.xano.io/api:meta/workspace/\{workspace\_id}/export](https://xxfo-0dml-kzcl.dev.xano.io/api:meta/workspace/\{workspace_id}/export)

Leave the `branch` parameter empty to indicate the current live branch. `password` is optional. If provided, will encrypt the export and will be required when importing the file. Required API Scope: Instance Workspace: Read

Authorizations

Path parameters

workspace\_idinteger · int64Required

Body

application/json

passwordstringOptional

branchstringOptional

Responses

200

Success!

application/json

Responseobject

400

Input Error. Check the request payload for issues.

401

Unauthorized

403

Access denied. Additional privileges are needed access the requested resource.

404

Not Found. The requested resource does not exist.

429

Rate Limited. Too many requests.

500

Unexpected error

post

/workspace/\{workspace\_id}/export

HTTP

```bash  theme={null}
POST /api:meta/workspace/{workspace_id}/export HTTP/1.1
Host: xxfo-0dml-kzcl.dev.xano.io
Authorization: Bearer JWT
Content-Type: application/json
Accept: */*
Content-Length: 27

{
  "branch": "",
  "password": ""
}
```

application/json

Test it

200

Success!

```
{}
```

### import schema into a new branch and optionally set it live

post

[https://xxfo-0dml-kzcl.dev.xano.io/api:meta/workspace/\{workspace\_id}/import-schema](https://xxfo-0dml-kzcl.dev.xano.io/api:meta/workspace/\{workspace_id}/import-schema)

\import schema into a new branch and optionally set it live Authentication: required Required API Scope: Instance Workspace: Read

Authorizations

Path parameters

workspace\_idinteger · int64Required

Body

filestring · binaryRequired

newbranchstringRequired

setlivebooleanOptional

passwordstringOptional

Responses

200

Success!

application/json

Responseobject

400

Input Error. Check the request payload for issues.

401

Unauthorized

403

Access denied. Additional privileges are needed access the requested resource.

404

Not Found. The requested resource does not exist.

429

Rate Limited. Too many requests.

500

Unexpected error

post

/workspace/\{workspace\_id}/import-schema

HTTP

```bash  theme={null}
POST /api:meta/workspace/{workspace_id}/import-schema HTTP/1.1
Host: xxfo-0dml-kzcl.dev.xano.io
Authorization: Bearer JWT
Content-Type: multipart/form-data
Accept: */*
Content-Length: 69

{
  "file": "binary",
  "newbranch": "text",
  "setlive": true,
  "password": "text"
}
```

Test it

200

Success!

```
{}
```

### import the archive into the specified workspace and replace it with supplied content and configuration

post

[https://xxfo-0dml-kzcl.dev.xano.io/api:meta/workspace/\{workspace\_id}/import](https://xxfo-0dml-kzcl.dev.xano.io/api:meta/workspace/\{workspace_id}/import)

If the file is encrypted, the correct `password` is required to decrypt. Required API Scope: Instance Workspace: Update

Authorizations

Path parameters

workspace\_idinteger · int64Required

Body

passwordstringOptional

filestring · binaryRequired

Responses

200

Success!

application/json

Responseobject

Show properties

400

Input Error. Check the request payload for issues.

401

Unauthorized

403

Access denied. Additional privileges are needed access the requested resource.

404

Not Found. The requested resource does not exist.

429

Rate Limited. Too many requests.

500

Unexpected error

post

/workspace/\{workspace\_id}/import

HTTP

```bash  theme={null}
POST /api:meta/workspace/{workspace_id}/import HTTP/1.1
Host: xxfo-0dml-kzcl.dev.xano.io
Authorization: Bearer JWT
Content-Type: multipart/form-data
Accept: */*
Content-Length: 35

{
  "password": "text",
  "file": "binary"
}
```

Test it

200

Success!

```json  theme={null}
{
  "id": 1,
  "name": "text",
  "description": "text",
  "branch": {
    "id": 1,
    "created_at": "text",
    "updated_at": "text",
    "description": "text",
    "label": "text",
    "backup": true,
    "color": "#ebc346",
    "parent_id": 1,
    "guid": "text",
    "workspace": {
      "id": 1
    },
    "user": {
      "id": 1,
      "name": "text",
      "email": "name@gmail.com"
    },
    "history": {
      "function_enabled": true,
      "function_limit": 100,
      "middleware_enabled": true,
      "middleware_limit": 100,
      "query_enabled": true,
      "query_limit": 100,
      "trigger_enabled": true,
      "trigger_limit": 100,
      "task_enabled": true,
      "task_limit": 100
    },
    "middleware": {
      "function_pre": [
        {
          "name": "text",
          "as": "text",
          "context": {},
          "description": "text",
          "disabled": true,
          "_xsid": "text",
          "input": [
            {
              "name": "text",
              "value": "text",
              "tag": "input",
              "ignore": true,
              "expand": true,
              "children": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {}
                          ]
                        }
                      ]
                    }
                  ],
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {}
                  ]
                }
              ],
              "filters": [
                {
                  "name": "text",
                  "disabled": true,
                  "arg": [
                    {
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                                {}
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "output": {
            "customize": true,
            "filters": [
              {
                "name": "text",
                "disabled": true,
                "arg": [
                  {
                    "value": "text",
                    "tag": "input",
                    "filters": [
                      {
                        "name": "text",
                        "disabled": true,
                        "arg": [
                          {
                            "value": "text",
                            "tag": "input",
                            "filters": [
                              {}
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "items": [
              {
                "name": "text",
                "children": [
                  {
                    "name": "text",
                    "children": [
                      {}
                    ]
                  }
                ]
              }
            ]
          },
          "addon": [
            {
              "id": {},
              "offset": "text",
              "as": "text",
              "children": [
                {
                  "id": {},
                  "offset": "text",
                  "as": "text",
                  "input": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                                {}
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                        {}
                      ]
                    }
                  ],
                  "output": {
                    "customize": true,
                    "items": [
                      {
                        "name": "text",
                        "children": [
                          {}
                        ]
                      }
                    ]
                  },
                  "children": [
                    {}
                  ]
                }
              ],
              "input": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                                {}
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                        {}
                      ]
                    }
                  ],
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {
                              "name": "text",
                              "disabled": true,
                              "arg": [
                                {
                                  "value": "text",
                                  "tag": "input",
                                  "filters": [
                                    {}
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "output": {
                "customize": true,
                "items": [
                  {
                    "name": "text",
                    "children": [
                      {
                        "name": "text",
                        "children": [
                          {}
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ],
      "function_post": [
        {
          "name": "text",
          "as": "text",
          "context": {},
          "description": "text",
          "disabled": true,
          "_xsid": "text",
          "input": [
            {
              "name": "text",
              "value": "text",
              "tag": "input",
              "ignore": true,
              "expand": true,
              "children": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {}
                          ]
                        }
                      ]
                    }
                  ],
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {}
                  ]
                }
              ],
              "filters": [
                {
                  "name": "text",
                  "disabled": true,
                  "arg": [
                    {
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                                {}
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "output": {
            "customize": true,
            "filters": [
              {
                "name": "text",
                "disabled": true,
                "arg": [
                  {
                    "value": "text",
                    "tag": "input",
                    "filters": [
                      {
                        "name": "text",
                        "disabled": true,
                        "arg": [
                          {
                            "value": "text",
                            "tag": "input",
                            "filters": [
                              {}
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "items": [
              {
                "name": "text",
                "children": [
                  {
                    "name": "text",
                    "children": [
                      {}
                    ]
                  }
                ]
              }
            ]
          },
          "addon": [
            {
              "id": {},
              "offset": "text",
              "as": "text",
              "children": [
                {
                  "id": {},
                  "offset": "text",
                  "as": "text",
                  "input": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                                {}
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                        {}
                      ]
                    }
                  ],
                  "output": {
                    "customize": true,
                    "items": [
                      {
                        "name": "text",
                        "children": [
                          {}
                        ]
                      }
                    ]
                  },
                  "children": [
                    {}
                  ]
                }
              ],
              "input": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                                {}
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                        {}
                      ]
                    }
                  ],
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {
                              "name": "text",
                              "disabled": true,
                              "arg": [
                                {
                                  "value": "text",
                                  "tag": "input",
                                  "filters": [
                                    {}
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "output": {
                "customize": true,
                "items": [
                  {
                    "name": "text",
                    "children": [
                      {
                        "name": "text",
                        "children": [
                          {}
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ],
      "query_pre": [
        {
          "name": "text",
          "as": "text",
          "context": {},
          "description": "text",
          "disabled": true,
          "_xsid": "text",
          "input": [
            {
              "name": "text",
              "value": "text",
              "tag": "input",
              "ignore": true,
              "expand": true,
              "children": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {}
                          ]
                        }
                      ]
                    }
                  ],
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {}
                  ]
                }
              ],
              "filters": [
                {
                  "name": "text",
                  "disabled": true,
                  "arg": [
                    {
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                                {}
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "output": {
            "customize": true,
            "filters": [
              {
                "name": "text",
                "disabled": true,
                "arg": [
                  {
                    "value": "text",
                    "tag": "input",
                    "filters": [
                      {
                        "name": "text",
                        "disabled": true,
                        "arg": [
                          {
                            "value": "text",
                            "tag": "input",
                            "filters": [
                              {}
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "items": [
              {
                "name": "text",
                "children": [
                  {
                    "name": "text",
                    "children": [
                      {}
                    ]
                  }
                ]
              }
            ]
          },
          "addon": [
            {
              "id": {},
              "offset": "text",
              "as": "text",
              "children": [
                {
                  "id": {},
                  "offset": "text",
                  "as": "text",
                  "input": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                                {}
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                        {}
                      ]
                    }
                  ],
                  "output": {
                    "customize": true,
                    "items": [
                      {
                        "name": "text",
                        "children": [
                          {}
                        ]
                      }
                    ]
                  },
                  "children": [
                    {}
                  ]
                }
              ],
              "input": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                                {}
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                        {}
                      ]
                    }
                  ],
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {
                              "name": "text",
                              "disabled": true,
                              "arg": [
                                {
                                  "value": "text",
                                  "tag": "input",
                                  "filters": [
                                    {}
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "output": {
                "customize": true,
                "items": [
                  {
                    "name": "text",
                    "children": [
                      {
                        "name": "text",
                        "children": [
                          {}
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ],
      "query_post": [
        {
          "name": "text",
          "as": "text",
          "context": {},
          "description": "text",
          "disabled": true,
          "_xsid": "text",
          "input": [
            {
              "name": "text",
              "value": "text",
              "tag": "input",
              "ignore": true,
              "expand": true,
              "children": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {}
                          ]
                        }
                      ]
                    }
                  ],
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {}
                  ]
                }
              ],
              "filters": [
                {
                  "name": "text",
                  "disabled": true,
                  "arg": [
                    {
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                                {}
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "output": {
            "customize": true,
            "filters": [
              {
                "name": "text",
                "disabled": true,
                "arg": [
                  {
                    "value": "text",
                    "tag": "input",
                    "filters": [
                      {
                        "name": "text",
                        "disabled": true,
                        "arg": [
                          {
                            "value": "text",
                            "tag": "input",
                            "filters": [
                              {}
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "items": [
              {
                "name": "text",
                "children": [
                  {
                    "name": "text",
                    "children": [
                      {}
                    ]
                  }
                ]
              }
            ]
          },
          "addon": [
            {
              "id": {},
              "offset": "text",
              "as": "text",
              "children": [
                {
                  "id": {},
                  "offset": "text",
                  "as": "text",
                  "input": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                                {}
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                        {}
                      ]
                    }
                  ],
                  "output": {
                    "customize": true,
                    "items": [
                      {
                        "name": "text",
                        "children": [
                          {}
                        ]
                      }
                    ]
                  },
                  "children": [
                    {}
                  ]
                }
              ],
              "input": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                                {}
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                        {}
                      ]
                    }
                  ],
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {
                              "name": "text",
                              "disabled": true,
                              "arg": [
                                {
                                  "value": "text",
                                  "tag": "input",
                                  "filters": [
                                    {}
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "output": {
                "customize": true,
                "items": [
                  {
                    "name": "text",
                    "children": [
                      {
                        "name": "text",
                        "children": [
                          {}
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ],
      "task_pre": [
        {
          "name": "text",
          "as": "text",
          "context": {},
          "description": "text",
          "disabled": true,
          "_xsid": "text",
          "input": [
            {
              "name": "text",
              "value": "text",
              "tag": "input",
              "ignore": true,
              "expand": true,
              "children": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {}
                          ]
                        }
                      ]
                    }
                  ],
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {}
                  ]
                }
              ],
              "filters": [
                {
                  "name": "text",
                  "disabled": true,
                  "arg": [
                    {
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                                {}
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "output": {
            "customize": true,
            "filters": [
              {
                "name": "text",
                "disabled": true,
                "arg": [
                  {
                    "value": "text",
                    "tag": "input",
                    "filters": [
                      {
                        "name": "text",
                        "disabled": true,
                        "arg": [
                          {
                            "value": "text",
                            "tag": "input",
                            "filters": [
                              {}
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "items": [
              {
                "name": "text",
                "children": [
                  {
                    "name": "text",
                    "children": [
                      {}
                    ]
                  }
                ]
              }
            ]
          },
          "addon": [
            {
              "id": {},
              "offset": "text",
              "as": "text",
              "children": [
                {
                  "id": {},
                  "offset": "text",
                  "as": "text",
                  "input": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                                {}
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                        {}
                      ]
                    }
                  ],
                  "output": {
                    "customize": true,
                    "items": [
                      {
                        "name": "text",
                        "children": [
                          {}
                        ]
                      }
                    ]
                  },
                  "children": [
                    {}
                  ]
                }
              ],
              "input": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                                {}
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                        {}
                      ]
                    }
                  ],
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {
                              "name": "text",
                              "disabled": true,
                              "arg": [
                                {
                                  "value": "text",
                                  "tag": "input",
                                  "filters": [
                                    {}
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "output": {
                "customize": true,
                "items": [
                  {
                    "name": "text",
                    "children": [
                      {
                        "name": "text",
                        "children": [
                          {}
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ],
      "task_post": [
        {
          "name": "text",
          "as": "text",
          "context": {},
          "description": "text",
          "disabled": true,
          "_xsid": "text",
          "input": [
            {
              "name": "text",
              "value": "text",
              "tag": "input",
              "ignore": true,
              "expand": true,
              "children": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {}
                          ]
                        }
                      ]
                    }
                  ],
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {}
                  ]
                }
              ],
              "filters": [
                {
                  "name": "text",
                  "disabled": true,
                  "arg": [
                    {
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                                {}
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "output": {
            "customize": true,
            "filters": [
              {
                "name": "text",
                "disabled": true,
                "arg": [
                  {
                    "value": "text",
                    "tag": "input",
                    "filters": [
                      {
                        "name": "text",
                        "disabled": true,
                        "arg": [
                          {
                            "value": "text",
                            "tag": "input",
                            "filters": [
                              {}
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "items": [
              {
                "name": "text",
                "children": [
                  {
                    "name": "text",
                    "children": [
                      {}
                    ]
                  }
                ]
              }
            ]
          },
          "addon": [
            {
              "id": {},
              "offset": "text",
              "as": "text",
              "children": [
                {
                  "id": {},
                  "offset": "text",
                  "as": "text",
                  "input": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                                {}
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                        {}
                      ]
                    }
                  ],
                  "output": {
                    "customize": true,
                    "items": [
                      {
                        "name": "text",
                        "children": [
                          {}
                        ]
                      }
                    ]
                  },
                  "children": [
                    {}
                  ]
                }
              ],
              "input": [
                {
                  "name": "text",
                  "value": "text",
                  "tag": "input",
                  "ignore": true,
                  "expand": true,
                  "children": [
                    {
                      "name": "text",
                      "value": "text",
                      "tag": "input",
                      "filters": [
                        {
                          "name": "text",
                          "disabled": true,
                          "arg": [
                            {
                              "value": "text",
                              "tag": "input",
                              "filters": [
                                {}
                              ]
                            }
                          ]
                        }
                      ],
                      "ignore": true,
                      "expand": true,
                      "children": [
                        {}
                      ]
                    }
                  ],
                  "filters": [
                    {
                      "name": "text",
                      "disabled": true,
                      "arg": [
                        {
                          "value": "text",
                          "tag": "input",
                          "filters": [
                            {
                              "name": "text",
                              "disabled": true,
                              "arg": [
                                {
                                  "value": "text",
                                  "tag": "input",
                                  "filters": [
                                    {}
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ],
              "output": {
                "customize": true,
                "items": [
                  {
                    "name": "text",
                    "children": [
                      {
                        "name": "text",
                        "children": [
                          {}
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ]
    },
    "defaults": {
      "db_primary_key": "int"
    }
  }
}
```


Built with [Mintlify](https://mintlify.com).