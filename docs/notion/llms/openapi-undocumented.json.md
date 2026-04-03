# Source: https://developers.notion.com/openapi-undocumented.json

{
  "openapi": "3.1.0",
  "info": {
    "title": "Notion API (Undocumented)",
    "version": "1.0.0",
    "description": "Internal/undocumented Notion API endpoints. These endpoints are not part of the public API and may change without notice. Do not rely on these for production integrations.",
    "termsOfService": "https://notion.notion.site/Terms-and-Privacy-28ffdd083dc3473e9c2da6ec011b58ac",
    "x-noIndex": true
  },
  "servers": [
    {
      "url": "https://api.notion.com"
    }
  ],
  "security": [
    {
      "bearerAuth": []
    }
  ],
  "tags": [
    {
      "name": "Internal",
      "description": "Internal/undocumented endpoints",
      "x-hidden": true
    }
  ],
  "components": {
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer"
      },
      "basicAuth": {
        "type": "http",
        "scheme": "basic"
      }
    },
    "schemas": {
      "annotationRequest": {
        "type": "object",
        "properties": {
          "bold": {
            "type": "boolean",
            "description": "Whether the text is formatted as bold."
          },
          "italic": {
            "type": "boolean",
            "description": "Whether the text is formatted as italic."
          },
          "strikethrough": {
            "type": "boolean",
            "description": "Whether the text is formatted with a strikethrough."
          },
          "underline": {
            "type": "boolean",
            "description": "Whether the text is formatted with an underline."
          },
          "code": {
            "type": "boolean",
            "description": "Whether the text is formatted as code."
          },
          "color": {
            "$ref": "#/components/schemas/apiColor",
            "description": "The color of the text."
          }
        }
      },
      "annotationResponse": {
        "type": "object",
        "properties": {
          "bold": {
            "type": "boolean"
          },
          "italic": {
            "type": "boolean"
          },
          "strikethrough": {
            "type": "boolean"
          },
          "underline": {
            "type": "boolean"
          },
          "code": {
            "type": "boolean"
          },
          "color": {
            "$ref": "#/components/schemas/apiColor"
          }
        },
        "additionalProperties": false,
        "required": [
          "bold",
          "italic",
          "strikethrough",
          "underline",
          "code",
          "color"
        ]
      },
      "apiColor": {
        "type": "string",
        "enum": [
          "default",
          "gray",
          "brown",
          "orange",
          "yellow",
          "green",
          "blue",
          "purple",
          "pink",
          "red",
          "default_background",
          "gray_background",
          "brown_background",
          "orange_background",
          "yellow_background",
          "green_background",
          "blue_background",
          "purple_background",
          "pink_background",
          "red_background"
        ],
        "description": "One of: `default`, `gray`, `brown`, `orange`, `yellow`, `green`, `blue`, `purple`, `pink`, `red`, `default_background`, `gray_background`, `brown_background`, `orange_background`, `yellow_background`, `green_background`, `blue_background`, `purple_background`, `pink_background`, `red_background`"
      },
      "apiTranscriptionStatus": {
        "type": "string",
        "enum": [
          "transcription_not_started",
          "transcription_paused",
          "transcription_in_progress",
          "summary_in_progress",
          "notes_ready"
        ]
      },
      "audioBlockObjectResponse": {
        "title": "Audio",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "audio"
          },
          "audio": {
            "$ref": "#/components/schemas/mediaContentWithFileAndCaptionResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "audio",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "blockIdCommentParentResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "block_id",
            "description": "Always `block_id`"
          },
          "block_id": {
            "$ref": "#/components/schemas/idResponse"
          }
        },
        "additionalProperties": false,
        "required": [
          "type",
          "block_id"
        ],
        "title": "Block Id"
      },
      "blockIdParentForBlockBasedObjectResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "block_id",
            "description": "The parent type."
          },
          "block_id": {
            "$ref": "#/components/schemas/idResponse",
            "description": "The ID of the parent block."
          }
        },
        "additionalProperties": false,
        "required": [
          "type",
          "block_id"
        ]
      },
      "blockObjectResponse": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/paragraphBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/heading1BlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/heading2BlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/heading3BlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/heading4BlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/bulletedListItemBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/numberedListItemBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/quoteBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/toDoBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/toggleBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/templateBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/syncedBlockBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/childPageBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/childDatabaseBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/equationBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/codeBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/calloutBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/dividerBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/breadcrumbBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/tableOfContentsBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/tabBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/columnListBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/columnBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/linkToPageBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/tableBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/tableRowBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/meetingNotesBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/embedBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/bookmarkBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/imageBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/videoBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/pdfBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/fileBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/audioBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/linkPreviewBlockObjectResponse"
          },
          {
            "$ref": "#/components/schemas/unsupportedBlockObjectResponse"
          }
        ]
      },
      "bookmarkBlockObjectResponse": {
        "title": "Bookmark",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "bookmark"
          },
          "bookmark": {
            "$ref": "#/components/schemas/mediaContentWithUrlAndCaptionResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "bookmark",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "booleanFormulaPropertyResponse": {
        "title": "Boolean",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "boolean"
          },
          "boolean": {
            "type": [
              "boolean",
              "null"
            ]
          }
        },
        "required": [
          "type",
          "boolean"
        ]
      },
      "botInfoResponse": {
        "type": "object",
        "properties": {
          "owner": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "user",
                    "description": "Always `user`"
                  },
                  "user": {
                    "oneOf": [
                      {
                        "type": "object",
                        "properties": {
                          "id": {
                            "$ref": "#/components/schemas/idResponse",
                            "description": "The ID of the user."
                          },
                          "object": {
                            "type": "string",
                            "const": "user",
                            "description": "The user object type name."
                          },
                          "name": {
                            "oneOf": [
                              {
                                "type": "string"
                              },
                              {
                                "type": "null"
                              }
                            ],
                            "description": "The name of the user."
                          },
                          "avatar_url": {
                            "oneOf": [
                              {
                                "type": "string"
                              },
                              {
                                "type": "null"
                              }
                            ],
                            "description": "The avatar URL of the user."
                          },
                          "type": {
                            "type": "string",
                            "const": "person",
                            "description": "The type of the user."
                          },
                          "person": {
                            "type": "object",
                            "properties": {
                              "email": {
                                "type": "string",
                                "description": "The email of the person."
                              }
                            },
                            "additionalProperties": false,
                            "description": "The person info of the user."
                          }
                        },
                        "additionalProperties": false,
                        "required": [
                          "id",
                          "object",
                          "name",
                          "avatar_url",
                          "type",
                          "person"
                        ]
                      },
                      {
                        "$ref": "#/components/schemas/partialUserObjectResponse"
                      }
                    ],
                    "description": "Details about the owner of the bot, when the `type` of the owner is `user`. This means the bot is for a integration."
                  }
                },
                "additionalProperties": false,
                "required": [
                  "type",
                  "user"
                ],
                "title": "User"
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "workspace",
                    "description": "Always `workspace`"
                  },
                  "workspace": {
                    "type": "boolean",
                    "const": true,
                    "description": "Details about the owner of the bot, when the `type` of the owner is `workspace`. This means the bot is for an internal integration."
                  }
                },
                "additionalProperties": false,
                "required": [
                  "type",
                  "workspace"
                ],
                "title": "Workspace"
              }
            ],
            "description": "Details about the owner of the bot."
          },
          "workspace_id": {
            "type": "string",
            "description": "The ID of the bot's workspace."
          },
          "workspace_limits": {
            "type": "object",
            "properties": {
              "max_file_upload_size_in_bytes": {
                "type": "integer",
                "minimum": 0,
                "description": "The maximum allowable size of a file upload, in bytes"
              }
            },
            "additionalProperties": false,
            "required": [
              "max_file_upload_size_in_bytes"
            ],
            "description": "Limits and restrictions that apply to the bot's workspace"
          },
          "workspace_name": {
            "oneOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "description": "The name of the bot's workspace."
          }
        },
        "additionalProperties": false,
        "required": [
          "owner",
          "workspace_id",
          "workspace_limits",
          "workspace_name"
        ]
      },
      "botUserObjectResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "bot",
            "description": "Indicates this user is a bot."
          },
          "bot": {
            "oneOf": [
              {
                "$ref": "#/components/schemas/emptyObject"
              },
              {
                "$ref": "#/components/schemas/botInfoResponse"
              }
            ],
            "description": "Details about the bot, when the `type` of the user is `bot`."
          }
        },
        "required": [
          "type",
          "bot"
        ],
        "title": "Bot"
      },
      "breadcrumbBlockObjectResponse": {
        "title": "Breadcrumb",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "breadcrumb"
          },
          "breadcrumb": {
            "$ref": "#/components/schemas/emptyObject"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "breadcrumb",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "bulletedListItemBlockObjectResponse": {
        "title": "Bulleted List Item",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "bulleted_list_item"
          },
          "bulleted_list_item": {
            "$ref": "#/components/schemas/contentWithRichTextAndColorResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "bulleted_list_item",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "buttonPropertyItemObjectResponse": {
        "title": "Button",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "button"
          },
          "button": {
            "$ref": "#/components/schemas/emptyObject"
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "button",
          "object",
          "id"
        ]
      },
      "calloutBlockObjectResponse": {
        "title": "Callout",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "callout"
          },
          "callout": {
            "type": "object",
            "properties": {
              "rich_text": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/richTextItemResponse"
                },
                "maxItems": 100
              },
              "color": {
                "$ref": "#/components/schemas/apiColor"
              },
              "icon": {
                "anyOf": [
                  {
                    "$ref": "#/components/schemas/pageIconResponse"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "required": [
              "rich_text",
              "color",
              "icon"
            ]
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "callout",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "checkboxDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "checkbox",
            "description": "Always `checkbox`"
          },
          "checkbox": {
            "$ref": "#/components/schemas/emptyObject"
          }
        },
        "required": [
          "type",
          "checkbox"
        ],
        "title": "Checkbox"
      },
      "checkboxPropertyItemObjectResponse": {
        "title": "Checkbox",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "checkbox"
          },
          "checkbox": {
            "type": "boolean"
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "checkbox",
          "object",
          "id"
        ]
      },
      "childDatabaseBlockObjectResponse": {
        "title": "Child Database",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "child_database"
          },
          "child_database": {
            "$ref": "#/components/schemas/titleObjectResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "child_database",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "childPageBlockObjectResponse": {
        "title": "Child Page",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "child_page"
          },
          "child_page": {
            "$ref": "#/components/schemas/titleObjectResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "child_page",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "codeBlockObjectResponse": {
        "title": "Code",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "code"
          },
          "code": {
            "type": "object",
            "properties": {
              "rich_text": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/richTextItemResponse"
                },
                "maxItems": 100
              },
              "caption": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/richTextItemResponse"
                },
                "maxItems": 100
              },
              "language": {
                "$ref": "#/components/schemas/languageRequest"
              }
            },
            "required": [
              "rich_text",
              "caption",
              "language"
            ]
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "code",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "columnBlockObjectResponse": {
        "title": "Column",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "column"
          },
          "column": {
            "$ref": "#/components/schemas/columnResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "column",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "columnListBlockObjectResponse": {
        "title": "Column List",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "column_list"
          },
          "column_list": {
            "$ref": "#/components/schemas/emptyObject"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "column_list",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "columnResponse": {
        "type": "object",
        "properties": {
          "width_ratio": {
            "description": "Ratio between 0 and 1 of the width of this column relative to all columns in the list. If not provided, uses an equal width.",
            "examples": [
              0.5
            ],
            "type": "number"
          }
        }
      },
      "commentObjectResponse": {
        "type": "object",
        "properties": {
          "object": {
            "type": "string",
            "const": "comment",
            "description": "The comment object type name."
          },
          "id": {
            "$ref": "#/components/schemas/idResponse",
            "description": "The ID of the comment."
          },
          "parent": {
            "$ref": "#/components/schemas/commentParentResponse",
            "description": "The parent of the comment."
          },
          "discussion_id": {
            "$ref": "#/components/schemas/idResponse",
            "description": "The ID of the discussion thread this comment belongs to."
          },
          "created_time": {
            "type": "string",
            "format": "date-time",
            "description": "The time when the comment was created."
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time",
            "description": "The time when the comment was last edited."
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse",
            "description": "The user who created the comment."
          },
          "rich_text": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/richTextItemResponse"
            },
            "maxItems": 100,
            "description": "The rich text content of the comment."
          },
          "display_name": {
            "type": "object",
            "properties": {
              "type": {
                "type": "string",
                "enum": [
                  "custom",
                  "user",
                  "integration"
                ],
                "description": "One of: `custom`, `user`, `integration`"
              },
              "resolved_name": {
                "oneOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false,
            "required": [
              "type",
              "resolved_name"
            ],
            "description": "The display name of the comment."
          },
          "attachments": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "category": {
                  "type": "string",
                  "enum": [
                    "audio",
                    "image",
                    "pdf",
                    "productivity",
                    "video"
                  ],
                  "description": "One of: `audio`, `image`, `pdf`, `productivity`, `video`"
                },
                "file": {
                  "$ref": "#/components/schemas/internalFileResponse"
                }
              },
              "additionalProperties": false,
              "required": [
                "category",
                "file"
              ]
            },
            "maxItems": 100,
            "description": "Any file attachments associated with the comment."
          }
        },
        "additionalProperties": false,
        "required": [
          "object",
          "id",
          "parent",
          "discussion_id",
          "created_time",
          "last_edited_time",
          "created_by",
          "rich_text",
          "display_name"
        ]
      },
      "commentParentResponse": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/pageIdCommentParentResponse"
          },
          {
            "$ref": "#/components/schemas/blockIdCommentParentResponse"
          }
        ]
      },
      "contentWithRichTextAndColorAndListResponse": {
        "type": "object",
        "properties": {
          "rich_text": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/richTextItemResponse"
            },
            "maxItems": 100
          },
          "color": {
            "$ref": "#/components/schemas/apiColor"
          },
          "list_start_index": {
            "type": "integer",
            "minimum": 1
          },
          "list_format": {
            "$ref": "#/components/schemas/numberedListFormat"
          }
        },
        "required": [
          "rich_text",
          "color"
        ]
      },
      "contentWithRichTextAndColorResponse": {
        "type": "object",
        "properties": {
          "rich_text": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/richTextItemResponse"
            },
            "maxItems": 100
          },
          "color": {
            "$ref": "#/components/schemas/apiColor"
          }
        },
        "required": [
          "rich_text",
          "color"
        ]
      },
      "contentWithRichTextColorAndIconResponse": {
        "type": "object",
        "properties": {
          "rich_text": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/richTextItemResponse"
            },
            "maxItems": 100
          },
          "color": {
            "$ref": "#/components/schemas/apiColor"
          },
          "icon": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/pageIconResponse"
              },
              {
                "type": "null"
              }
            ]
          }
        },
        "required": [
          "rich_text",
          "color",
          "icon"
        ]
      },
      "contentWithTableResponse": {
        "type": "object",
        "properties": {
          "has_column_header": {
            "type": "boolean"
          },
          "has_row_header": {
            "type": "boolean"
          },
          "table_width": {
            "type": "integer",
            "minimum": 1
          }
        },
        "required": [
          "has_column_header",
          "has_row_header",
          "table_width"
        ]
      },
      "contentWithTableRowResponse": {
        "type": "object",
        "properties": {
          "cells": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/richTextItemResponse"
              },
              "maxItems": 100
            },
            "maxItems": 100
          }
        },
        "required": [
          "cells"
        ]
      },
      "createdByDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "created_by",
            "description": "Always `created_by`"
          },
          "created_by": {
            "$ref": "#/components/schemas/emptyObject"
          }
        },
        "required": [
          "type",
          "created_by"
        ],
        "title": "Created By"
      },
      "createdByPropertyItemObjectResponse": {
        "title": "Created By",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "created_by"
          },
          "created_by": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/partialUserObjectResponse"
              },
              {
                "$ref": "#/components/schemas/userObjectResponse"
              }
            ]
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "created_by",
          "object",
          "id"
        ]
      },
      "createdTimeDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "created_time",
            "description": "Always `created_time`"
          },
          "created_time": {
            "$ref": "#/components/schemas/emptyObject"
          }
        },
        "required": [
          "type",
          "created_time"
        ],
        "title": "Created Time"
      },
      "createdTimePropertyItemObjectResponse": {
        "title": "Created Time",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "created_time"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "created_time",
          "object",
          "id"
        ]
      },
      "customEmojiPageIconRequest": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "custom_emoji",
            "description": "Always `custom_emoji`"
          },
          "custom_emoji": {
            "type": "object",
            "properties": {
              "id": {
                "$ref": "#/components/schemas/idRequest",
                "description": "The ID of the custom emoji."
              },
              "name": {
                "type": "string",
                "description": "The name of the custom emoji."
              },
              "url": {
                "type": "string",
                "description": "The URL of the custom emoji."
              }
            },
            "required": [
              "id"
            ]
          }
        },
        "required": [
          "custom_emoji"
        ],
        "title": "Custom Emoji"
      },
      "customEmojiPageIconResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "custom_emoji",
            "description": "Type of icon. In this case, a custom emoji."
          },
          "custom_emoji": {
            "$ref": "#/components/schemas/customEmojiResponse",
            "description": "The custom emoji details for the icon."
          }
        },
        "additionalProperties": false,
        "required": [
          "type",
          "custom_emoji"
        ],
        "title": "Custom Emoji"
      },
      "customEmojiResponse": {
        "type": "object",
        "properties": {
          "id": {
            "$ref": "#/components/schemas/idResponse",
            "description": "The ID of the custom emoji."
          },
          "name": {
            "type": "string",
            "description": "The name of the custom emoji."
          },
          "url": {
            "type": "string",
            "description": "The URL of the custom emoji."
          }
        },
        "additionalProperties": false,
        "required": [
          "id",
          "name",
          "url"
        ]
      },
      "dataSourceObjectResponse": {
        "type": "object",
        "properties": {
          "object": {
            "type": "string",
            "const": "data_source",
            "description": "The data source object type name."
          },
          "id": {
            "$ref": "#/components/schemas/idResponse",
            "description": "The ID of the data source."
          },
          "title": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/richTextItemResponse"
            },
            "maxItems": 100,
            "description": "The title of the data source."
          },
          "description": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/richTextItemResponse"
            },
            "maxItems": 100,
            "description": "The description of the data source."
          },
          "parent": {
            "$ref": "#/components/schemas/parentOfDataSourceResponse",
            "description": "The parent of the data source."
          },
          "database_parent": {
            "$ref": "#/components/schemas/parentOfDatabaseResponse",
            "description": "The parent of the data source's containing database. This is typically a page, block, or workspace, but can be another database in the case of wikis."
          },
          "is_inline": {
            "type": "boolean",
            "description": "Whether the data source is inline."
          },
          "in_trash": {
            "type": "boolean",
            "description": "Whether the data source is in the trash."
          },
          "created_time": {
            "type": "string",
            "format": "date-time",
            "description": "The time when the data source was created."
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time",
            "description": "The time when the data source was last edited."
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse",
            "description": "The user who created the data source."
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse",
            "description": "The user who last edited the data source."
          },
          "properties": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/databasePropertyConfigResponse"
            },
            "description": "The properties schema of the data source."
          },
          "icon": {
            "oneOf": [
              {
                "$ref": "#/components/schemas/pageIconResponse"
              },
              {
                "type": "null"
              }
            ],
            "description": "The icon of the data source."
          },
          "cover": {
            "oneOf": [
              {
                "$ref": "#/components/schemas/pageCoverResponse"
              },
              {
                "type": "null"
              }
            ],
            "description": "The cover of the data source."
          },
          "url": {
            "type": "string",
            "description": "The URL of the data source."
          },
          "public_url": {
            "oneOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "description": "The public URL of the data source if it is publicly accessible."
          }
        },
        "additionalProperties": false,
        "required": [
          "object",
          "id",
          "title",
          "description",
          "parent",
          "database_parent",
          "is_inline",
          "in_trash",
          "created_time",
          "last_edited_time",
          "created_by",
          "last_edited_by",
          "properties",
          "icon",
          "cover",
          "url",
          "public_url"
        ]
      },
      "dataSourceParentResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "data_source_id",
            "description": "The parent type."
          },
          "data_source_id": {
            "$ref": "#/components/schemas/idResponse",
            "description": "The ID of the parent data source."
          },
          "database_id": {
            "$ref": "#/components/schemas/idResponse",
            "description": "The ID of the data source's parent database."
          }
        },
        "additionalProperties": false,
        "required": [
          "type",
          "data_source_id",
          "database_id"
        ]
      },
      "databaseParentResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "database_id",
            "description": "The parent type."
          },
          "database_id": {
            "$ref": "#/components/schemas/idResponse",
            "description": "The ID of the parent database."
          }
        },
        "additionalProperties": false,
        "required": [
          "type",
          "database_id"
        ]
      },
      "databasePropertyConfigResponse": {
        "allOf": [
          {
            "$ref": "#/components/schemas/databasePropertyConfigResponseCommon"
          },
          {
            "oneOf": [
              {
                "$ref": "#/components/schemas/numberDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/formulaDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/selectDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/multiSelectDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/statusDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/relationDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/rollupDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/uniqueIdDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/titleDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/richTextDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/urlDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/peopleDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/filesDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/emailDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/phoneNumberDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/dateDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/checkboxDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/createdByDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/createdTimeDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/lastEditedByDatabasePropertyConfigResponse"
              },
              {
                "$ref": "#/components/schemas/lastEditedTimeDatabasePropertyConfigResponse"
              }
            ]
          }
        ]
      },
      "databasePropertyConfigResponseCommon": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "The ID of the property."
          },
          "name": {
            "type": "string",
            "description": "The name of the property."
          },
          "description": {
            "oneOf": [
              {
                "$ref": "#/components/schemas/propertyDescriptionRequest"
              },
              {
                "type": "null"
              }
            ],
            "description": "The description of the property."
          }
        },
        "additionalProperties": false,
        "required": [
          "id",
          "name",
          "description"
        ]
      },
      "databasePropertyRelationConfigResponse": {
        "allOf": [
          {
            "$ref": "#/components/schemas/databasePropertyRelationConfigResponseCommon"
          },
          {
            "oneOf": [
              {
                "$ref": "#/components/schemas/singlePropertyDatabasePropertyRelationConfigResponse"
              },
              {
                "$ref": "#/components/schemas/dualPropertyDatabasePropertyRelationConfigResponse"
              }
            ]
          }
        ]
      },
      "databasePropertyRelationConfigResponseCommon": {
        "type": "object",
        "properties": {
          "database_id": {
            "$ref": "#/components/schemas/idResponse"
          },
          "data_source_id": {
            "$ref": "#/components/schemas/idResponse"
          }
        },
        "additionalProperties": false,
        "required": [
          "database_id",
          "data_source_id"
        ]
      },
      "dateDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "date",
            "description": "Always `date`"
          },
          "date": {
            "$ref": "#/components/schemas/emptyObject"
          }
        },
        "required": [
          "type",
          "date"
        ],
        "title": "Date"
      },
      "dateFormulaPropertyResponse": {
        "title": "Date",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "date"
          },
          "date": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/dateResponse"
              },
              {
                "type": "null"
              }
            ]
          }
        },
        "required": [
          "type",
          "date"
        ]
      },
      "datePropertyItemObjectResponse": {
        "title": "Date",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "date"
          },
          "date": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/dateResponse"
              },
              {
                "type": "null"
              }
            ]
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "date",
          "object",
          "id"
        ]
      },
      "dateRequest": {
        "type": "object",
        "properties": {
          "start": {
            "type": "string",
            "format": "date",
            "description": "The start date of the date object."
          },
          "end": {
            "oneOf": [
              {
                "type": "string",
                "format": "date"
              },
              {
                "type": "null"
              }
            ],
            "description": "The end date of the date object, if any."
          },
          "time_zone": {
            "oneOf": [
              {
                "$ref": "#/components/schemas/timeZoneRequest"
              },
              {
                "type": "null"
              }
            ],
            "description": "The time zone of the date object, if any. E.g. America/Los_Angeles, Europe/London, etc."
          }
        },
        "additionalProperties": false,
        "required": [
          "start"
        ]
      },
      "dateResponse": {
        "type": "object",
        "properties": {
          "start": {
            "type": "string",
            "format": "date",
            "description": "The start date of the date object."
          },
          "end": {
            "oneOf": [
              {
                "type": "string",
                "format": "date"
              },
              {
                "type": "null"
              }
            ],
            "description": "The end date of the date object, if any."
          },
          "time_zone": {
            "oneOf": [
              {
                "$ref": "#/components/schemas/timeZoneRequest"
              },
              {
                "type": "null"
              }
            ],
            "description": "The time zone of the date object."
          }
        },
        "additionalProperties": false,
        "required": [
          "start",
          "end",
          "time_zone"
        ]
      },
      "dividerBlockObjectResponse": {
        "title": "Divider",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "divider"
          },
          "divider": {
            "$ref": "#/components/schemas/emptyObject"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "divider",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "dualPropertyDatabasePropertyRelationConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "dual_property",
            "description": "Always `dual_property`"
          },
          "dual_property": {
            "type": "object",
            "properties": {
              "synced_property_id": {
                "type": "string"
              },
              "synced_property_name": {
                "type": "string"
              }
            },
            "additionalProperties": false,
            "required": [
              "synced_property_id",
              "synced_property_name"
            ]
          }
        },
        "required": [
          "dual_property"
        ],
        "title": "Dual Property"
      },
      "emailDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "email",
            "description": "Always `email`"
          },
          "email": {
            "$ref": "#/components/schemas/emptyObject"
          }
        },
        "required": [
          "type",
          "email"
        ],
        "title": "Email"
      },
      "emailPropertyItemObjectResponse": {
        "title": "Email",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "email"
          },
          "email": {
            "type": [
              "string",
              "null"
            ]
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "email",
          "object",
          "id"
        ]
      },
      "embedBlockObjectResponse": {
        "title": "Embed",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "embed"
          },
          "embed": {
            "$ref": "#/components/schemas/mediaContentWithUrlAndCaptionResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "embed",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "emojiPageIconRequest": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "emoji",
            "description": "Always `emoji`"
          },
          "emoji": {
            "$ref": "#/components/schemas/emojiRequest",
            "description": "An emoji character."
          }
        },
        "required": [
          "emoji"
        ],
        "title": "Emoji"
      },
      "emojiPageIconResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "emoji",
            "description": "Type of icon. In this case, an emoji."
          },
          "emoji": {
            "$ref": "#/components/schemas/emojiRequest",
            "description": "The emoji character used as the icon."
          }
        },
        "additionalProperties": false,
        "required": [
          "type",
          "emoji"
        ],
        "title": "Emoji"
      },
      "emojiRequest": {
        "type": "string"
      },
      "emptyObject": {
        "type": "object",
        "properties": {},
        "additionalProperties": false
      },
      "equationBlockObjectResponse": {
        "title": "Equation",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "equation"
          },
          "equation": {
            "$ref": "#/components/schemas/expressionObjectResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "equation",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "equationRichTextItemRequest": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "equation",
            "description": "Always `equation`"
          },
          "equation": {
            "type": "object",
            "properties": {
              "expression": {
                "type": "string",
                "examples": [
                  "e=mc^2"
                ],
                "description": "A KaTeX compatible string."
              }
            },
            "required": [
              "expression"
            ],
            "description": "Notion supports inline LaTeX equations as rich text objects with a type value of `equation`."
          }
        },
        "required": [
          "equation"
        ],
        "title": "Equation"
      },
      "equationRichTextItemResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "equation",
            "description": "Always `equation`"
          },
          "equation": {
            "type": "object",
            "properties": {
              "expression": {
                "type": "string",
                "examples": [
                  "e=mc^2"
                ],
                "description": "A KaTeX compatible string."
              }
            },
            "additionalProperties": false,
            "required": [
              "expression"
            ],
            "description": "Notion supports inline LaTeX equations as rich text objects with a type value of `equation`."
          }
        },
        "required": [
          "type",
          "equation"
        ],
        "title": "Equation"
      },
      "error_api_400": {
        "allOf": [
          {
            "$ref": "#/components/schemas/publicApiCommonErrorResponse"
          },
          {
            "type": "object",
            "properties": {
              "code": {
                "enum": [
                  "invalid_json",
                  "invalid_request_url",
                  "invalid_request",
                  "missing_version",
                  "validation_error"
                ]
              },
              "status": {
                "const": 400
              }
            },
            "required": [
              "code",
              "status"
            ],
            "additionalProperties": false
          }
        ]
      },
      "error_api_401": {
        "allOf": [
          {
            "$ref": "#/components/schemas/publicApiCommonErrorResponse"
          },
          {
            "type": "object",
            "properties": {
              "code": {
                "enum": [
                  "unauthorized"
                ]
              },
              "status": {
                "const": 401
              }
            },
            "required": [
              "code",
              "status"
            ],
            "additionalProperties": false
          }
        ]
      },
      "error_api_403": {
        "allOf": [
          {
            "$ref": "#/components/schemas/publicApiCommonErrorResponse"
          },
          {
            "type": "object",
            "properties": {
              "code": {
                "enum": [
                  "restricted_resource"
                ]
              },
              "status": {
                "const": 403
              }
            },
            "required": [
              "code",
              "status"
            ],
            "additionalProperties": false
          }
        ]
      },
      "error_api_404": {
        "allOf": [
          {
            "$ref": "#/components/schemas/publicApiCommonErrorResponse"
          },
          {
            "type": "object",
            "properties": {
              "code": {
                "enum": [
                  "object_not_found"
                ]
              },
              "status": {
                "const": 404
              }
            },
            "required": [
              "code",
              "status"
            ],
            "additionalProperties": false
          }
        ]
      },
      "error_api_409": {
        "allOf": [
          {
            "$ref": "#/components/schemas/publicApiCommonErrorResponse"
          },
          {
            "type": "object",
            "properties": {
              "code": {
                "enum": [
                  "conflict_error"
                ]
              },
              "status": {
                "const": 409
              }
            },
            "required": [
              "code",
              "status"
            ],
            "additionalProperties": false
          }
        ]
      },
      "error_api_429": {
        "allOf": [
          {
            "$ref": "#/components/schemas/publicApiCommonErrorResponse"
          },
          {
            "type": "object",
            "properties": {
              "code": {
                "enum": [
                  "rate_limited"
                ]
              },
              "status": {
                "const": 429
              }
            },
            "required": [
              "code",
              "status"
            ],
            "additionalProperties": false
          }
        ]
      },
      "error_api_500": {
        "allOf": [
          {
            "$ref": "#/components/schemas/publicApiCommonErrorResponse"
          },
          {
            "type": "object",
            "properties": {
              "code": {
                "enum": [
                  "internal_server_error"
                ]
              },
              "status": {
                "const": 500
              }
            },
            "required": [
              "code",
              "status"
            ],
            "additionalProperties": false
          }
        ]
      },
      "error_api_503": {
        "allOf": [
          {
            "$ref": "#/components/schemas/publicApiCommonErrorResponse"
          },
          {
            "type": "object",
            "properties": {
              "code": {
                "enum": [
                  "service_unavailable"
                ]
              },
              "status": {
                "const": 503
              }
            },
            "required": [
              "code",
              "status"
            ],
            "additionalProperties": false
          }
        ]
      },
      "error_api_504": {
        "allOf": [
          {
            "$ref": "#/components/schemas/publicApiCommonErrorResponse"
          },
          {
            "type": "object",
            "properties": {
              "code": {
                "enum": [
                  "gateway_timeout"
                ]
              },
              "status": {
                "const": 504
              }
            },
            "required": [
              "code",
              "status"
            ],
            "additionalProperties": false
          }
        ]
      },
      "error_oauth_400": {
        "allOf": [
          {
            "$ref": "#/components/schemas/publicApiCommonErrorResponse"
          },
          {
            "type": "object",
            "properties": {
              "code": {
                "enum": [
                  "invalid_request",
                  "invalid_grant",
                  "unauthorized_client",
                  "unsupported_grant_type",
                  "invalid_scope"
                ]
              },
              "status": {
                "const": 400
              }
            },
            "required": [
              "code",
              "status"
            ],
            "additionalProperties": false
          }
        ]
      },
      "error_oauth_401": {
        "allOf": [
          {
            "$ref": "#/components/schemas/publicApiCommonErrorResponse"
          },
          {
            "type": "object",
            "properties": {
              "code": {
                "enum": [
                  "invalid_client"
                ]
              },
              "status": {
                "const": 401
              }
            },
            "required": [
              "code",
              "status"
            ],
            "additionalProperties": false
          }
        ]
      },
      "error_oauth_403": {
        "allOf": [
          {
            "$ref": "#/components/schemas/publicApiCommonErrorResponse"
          },
          {
            "type": "object",
            "properties": {
              "code": {
                "enum": [
                  "test_env_error"
                ]
              },
              "status": {
                "const": 403
              }
            },
            "required": [
              "code",
              "status"
            ],
            "additionalProperties": false
          }
        ]
      },
      "error_oauth_500": {
        "allOf": [
          {
            "$ref": "#/components/schemas/publicApiCommonErrorResponse"
          },
          {
            "type": "object",
            "properties": {
              "code": {
                "enum": [
                  "internal_server_error"
                ]
              },
              "status": {
                "const": 500
              }
            },
            "required": [
              "code",
              "status"
            ],
            "additionalProperties": false
          }
        ]
      },
      "expressionObjectResponse": {
        "type": "object",
        "properties": {
          "expression": {
            "type": "string"
          }
        },
        "required": [
          "expression"
        ]
      },
      "externalInternalOrExternalFileWithNameResponse": {
        "title": "External",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "external"
          },
          "external": {
            "type": "object",
            "properties": {
              "url": {
                "$ref": "#/components/schemas/textRequest"
              }
            },
            "required": [
              "url"
            ]
          },
          "name": {
            "$ref": "#/components/schemas/stringRequest"
          }
        },
        "required": [
          "type",
          "external",
          "name"
        ]
      },
      "externalMediaContentWithFileAndCaptionResponse": {
        "title": "External",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "external"
          },
          "external": {
            "type": "object",
            "properties": {
              "url": {
                "$ref": "#/components/schemas/textRequest"
              }
            },
            "required": [
              "url"
            ]
          },
          "caption": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/richTextItemResponse"
            },
            "maxItems": 100
          }
        },
        "required": [
          "type",
          "external",
          "caption"
        ]
      },
      "externalMediaContentWithFileNameAndCaptionResponse": {
        "title": "External",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "external"
          },
          "external": {
            "type": "object",
            "properties": {
              "url": {
                "$ref": "#/components/schemas/textRequest"
              }
            },
            "required": [
              "url"
            ]
          },
          "caption": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/richTextItemResponse"
            },
            "maxItems": 100
          },
          "name": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "external",
          "caption",
          "name"
        ]
      },
      "externalPageCoverResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "external",
            "description": "Type of cover. In this case, an external URL."
          },
          "external": {
            "type": "object",
            "properties": {
              "url": {
                "type": "string",
                "description": "The URL of the external file or resource."
              }
            },
            "additionalProperties": false,
            "required": [
              "url"
            ],
            "description": "The external URL for the cover."
          }
        },
        "additionalProperties": false,
        "required": [
          "type",
          "external"
        ],
        "title": "External"
      },
      "externalPageIconRequest": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "external",
            "description": "Always `external`"
          },
          "external": {
            "type": "object",
            "properties": {
              "url": {
                "type": "string",
                "description": "The URL of the external file."
              }
            },
            "required": [
              "url"
            ]
          }
        },
        "required": [
          "external"
        ],
        "title": "External"
      },
      "externalPageIconResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "external",
            "description": "Type of icon. In this case, an external URL."
          },
          "external": {
            "type": "object",
            "properties": {
              "url": {
                "type": "string",
                "description": "The URL of the external file or resource."
              }
            },
            "additionalProperties": false,
            "required": [
              "url"
            ],
            "description": "The external URL for the icon."
          }
        },
        "additionalProperties": false,
        "required": [
          "type",
          "external"
        ],
        "title": "External"
      },
      "fileBlockObjectResponse": {
        "title": "File",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "file"
          },
          "file": {
            "$ref": "#/components/schemas/mediaContentWithFileNameAndCaptionResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "file",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "fileInternalOrExternalFileWithNameResponse": {
        "title": "File",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "file"
          },
          "file": {
            "$ref": "#/components/schemas/internalFileResponse"
          },
          "name": {
            "$ref": "#/components/schemas/stringRequest"
          }
        },
        "required": [
          "type",
          "file",
          "name"
        ]
      },
      "fileMediaContentWithFileAndCaptionResponse": {
        "title": "File",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "file"
          },
          "file": {
            "$ref": "#/components/schemas/internalFileResponse"
          },
          "caption": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/richTextItemResponse"
            },
            "maxItems": 100
          }
        },
        "required": [
          "type",
          "file",
          "caption"
        ]
      },
      "fileMediaContentWithFileNameAndCaptionResponse": {
        "title": "File",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "file"
          },
          "file": {
            "$ref": "#/components/schemas/internalFileResponse"
          },
          "caption": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/richTextItemResponse"
            },
            "maxItems": 100
          },
          "name": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "file",
          "caption",
          "name"
        ]
      },
      "filePageCoverResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "file",
            "description": "Type of cover. In this case, a file."
          },
          "file": {
            "$ref": "#/components/schemas/internalFileResponse",
            "description": "The file URL for the cover."
          }
        },
        "additionalProperties": false,
        "required": [
          "type",
          "file"
        ],
        "title": "File"
      },
      "filePageIconResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "file",
            "description": "Type of icon. In this case, a file."
          },
          "file": {
            "$ref": "#/components/schemas/internalFileResponse",
            "description": "The file URL for the icon."
          }
        },
        "additionalProperties": false,
        "required": [
          "type",
          "file"
        ],
        "title": "File"
      },
      "fileUploadPageIconRequest": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "file_upload",
            "description": "Always `file_upload`"
          },
          "file_upload": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "description": "ID of a FileUpload object that has the status `uploaded`."
              }
            },
            "required": [
              "id"
            ]
          }
        },
        "required": [
          "file_upload"
        ],
        "title": "File Upload"
      },
      "filesDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "files",
            "description": "Always `files`"
          },
          "files": {
            "$ref": "#/components/schemas/emptyObject"
          }
        },
        "required": [
          "type",
          "files"
        ],
        "title": "Files"
      },
      "filesPropertyItemObjectResponse": {
        "title": "Files",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "files"
          },
          "files": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/internalOrExternalFileWithNameResponse"
            },
            "maxItems": 100
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "files",
          "object",
          "id"
        ]
      },
      "formulaDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "formula",
            "description": "Always `formula`"
          },
          "formula": {
            "type": "object",
            "properties": {
              "expression": {
                "type": "string"
              }
            },
            "additionalProperties": false,
            "required": [
              "expression"
            ]
          }
        },
        "required": [
          "type",
          "formula"
        ],
        "title": "Formula"
      },
      "formulaPropertyItemObjectResponse": {
        "title": "Formula",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "formula"
          },
          "formula": {
            "$ref": "#/components/schemas/formulaPropertyResponse"
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "formula",
          "object",
          "id"
        ]
      },
      "formulaPropertyResponse": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/stringFormulaPropertyResponse"
          },
          {
            "$ref": "#/components/schemas/dateFormulaPropertyResponse"
          },
          {
            "$ref": "#/components/schemas/numberFormulaPropertyResponse"
          },
          {
            "$ref": "#/components/schemas/booleanFormulaPropertyResponse"
          }
        ]
      },
      "groupObjectResponse": {
        "type": "object",
        "properties": {
          "name": {
            "type": [
              "string",
              "null"
            ]
          },
          "id": {
            "$ref": "#/components/schemas/idResponse"
          },
          "object": {
            "type": "string",
            "const": "group"
          }
        },
        "required": [
          "name",
          "id",
          "object"
        ]
      },
      "headerContentWithRichTextAndColorResponse": {
        "type": "object",
        "properties": {
          "rich_text": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/richTextItemResponse"
            },
            "maxItems": 100
          },
          "color": {
            "$ref": "#/components/schemas/apiColor"
          },
          "is_toggleable": {
            "type": "boolean"
          }
        },
        "required": [
          "rich_text",
          "color",
          "is_toggleable"
        ]
      },
      "heading1BlockObjectResponse": {
        "title": "Heading 1",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "heading_1"
          },
          "heading_1": {
            "$ref": "#/components/schemas/headerContentWithRichTextAndColorResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "heading_1",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "heading2BlockObjectResponse": {
        "title": "Heading 2",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "heading_2"
          },
          "heading_2": {
            "$ref": "#/components/schemas/headerContentWithRichTextAndColorResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "heading_2",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "heading3BlockObjectResponse": {
        "title": "Heading 3",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "heading_3"
          },
          "heading_3": {
            "$ref": "#/components/schemas/headerContentWithRichTextAndColorResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "heading_3",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "heading4BlockObjectResponse": {
        "title": "Heading 4",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "heading_4"
          },
          "heading_4": {
            "$ref": "#/components/schemas/headerContentWithRichTextAndColorResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "heading_4",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "iconPageIconRequest": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "icon",
            "description": "Always `icon`"
          },
          "icon": {
            "type": "object",
            "properties": {
              "name": {
                "$ref": "#/components/schemas/noticonName",
                "description": "The name of the Notion icon (e.g. pizza, meeting, home). See the Notion icon picker for valid names."
              },
              "color": {
                "$ref": "#/components/schemas/noticonColor",
                "description": "The color variant of the icon. Defaults to gray if not specified. Valid values: gray, lightgray, brown, yellow, orange, green, blue, purple, pink, red."
              }
            },
            "required": [
              "name"
            ],
            "description": "A Notion native icon, specified by name and optional color."
          }
        },
        "required": [
          "icon"
        ],
        "title": "Icon"
      },
      "iconPageIconResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "icon",
            "description": "Type of icon. In this case, a Notion native icon."
          },
          "icon": {
            "$ref": "#/components/schemas/noticonIconResponse",
            "description": "The Notion native icon, specified by name and color."
          }
        },
        "additionalProperties": false,
        "required": [
          "type",
          "icon"
        ],
        "title": "Icon"
      },
      "idRequest": {
        "type": "string"
      },
      "idResponse": {
        "type": "string",
        "format": "uuid"
      },
      "imageBlockObjectResponse": {
        "title": "Image",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "image"
          },
          "image": {
            "$ref": "#/components/schemas/mediaContentWithFileAndCaptionResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "image",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "internalFileResponse": {
        "type": "object",
        "properties": {
          "url": {
            "type": "string",
            "description": "The URL of the file."
          },
          "expiry_time": {
            "type": "string",
            "format": "date-time",
            "description": "The time when the URL will expire."
          }
        },
        "additionalProperties": false,
        "required": [
          "url",
          "expiry_time"
        ]
      },
      "internalOrExternalFileWithNameResponse": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/fileInternalOrExternalFileWithNameResponse"
          },
          {
            "$ref": "#/components/schemas/externalInternalOrExternalFileWithNameResponse"
          }
        ]
      },
      "languageRequest": {
        "type": "string",
        "enum": [
          "abap",
          "abc",
          "agda",
          "arduino",
          "ascii art",
          "assembly",
          "bash",
          "basic",
          "bnf",
          "c",
          "c#",
          "c++",
          "clojure",
          "coffeescript",
          "coq",
          "css",
          "dart",
          "dhall",
          "diff",
          "docker",
          "ebnf",
          "elixir",
          "elm",
          "erlang",
          "f#",
          "flow",
          "fortran",
          "gherkin",
          "glsl",
          "go",
          "graphql",
          "groovy",
          "haskell",
          "hcl",
          "html",
          "idris",
          "java",
          "javascript",
          "json",
          "julia",
          "kotlin",
          "latex",
          "less",
          "lisp",
          "livescript",
          "llvm ir",
          "lua",
          "makefile",
          "markdown",
          "markup",
          "matlab",
          "mathematica",
          "mermaid",
          "nix",
          "notion formula",
          "objective-c",
          "ocaml",
          "pascal",
          "perl",
          "php",
          "plain text",
          "powershell",
          "prolog",
          "protobuf",
          "purescript",
          "python",
          "r",
          "racket",
          "reason",
          "ruby",
          "rust",
          "sass",
          "scala",
          "scheme",
          "scss",
          "shell",
          "smalltalk",
          "solidity",
          "sql",
          "swift",
          "toml",
          "typescript",
          "vb.net",
          "verilog",
          "vhdl",
          "visual basic",
          "webassembly",
          "xml",
          "yaml",
          "java/c/c++/c#"
        ]
      },
      "lastEditedByDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "last_edited_by",
            "description": "Always `last_edited_by`"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/emptyObject"
          }
        },
        "required": [
          "type",
          "last_edited_by"
        ],
        "title": "Last Edited By"
      },
      "lastEditedByPropertyItemObjectResponse": {
        "title": "Last Edited By",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "last_edited_by"
          },
          "last_edited_by": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/partialUserObjectResponse"
              },
              {
                "$ref": "#/components/schemas/userObjectResponse"
              }
            ]
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "last_edited_by",
          "object",
          "id"
        ]
      },
      "lastEditedTimeDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "last_edited_time",
            "description": "Always `last_edited_time`"
          },
          "last_edited_time": {
            "$ref": "#/components/schemas/emptyObject"
          }
        },
        "required": [
          "type",
          "last_edited_time"
        ],
        "title": "Last Edited Time"
      },
      "lastEditedTimePropertyItemObjectResponse": {
        "title": "Last Edited Time",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "last_edited_time"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "last_edited_time",
          "object",
          "id"
        ]
      },
      "linkMentionResponse": {
        "type": "object",
        "properties": {
          "href": {
            "type": "string",
            "description": "The href of the link mention."
          },
          "title": {
            "type": "string",
            "description": "The title of the link."
          },
          "description": {
            "type": "string",
            "description": "The description of the link."
          },
          "link_author": {
            "type": "string",
            "description": "The author of the link."
          },
          "link_provider": {
            "type": "string",
            "description": "The provider of the link."
          },
          "thumbnail_url": {
            "type": "string",
            "description": "The thumbnail URL of the link."
          },
          "icon_url": {
            "type": "string",
            "description": "The icon URL of the link."
          },
          "iframe_url": {
            "type": "string",
            "description": "The iframe URL of the link."
          },
          "height": {
            "type": "integer",
            "description": "The height of the link preview iframe."
          },
          "padding": {
            "type": "integer",
            "description": "The padding of the link preview iframe."
          },
          "padding_top": {
            "type": "integer",
            "description": "The top padding of the link preview iframe."
          }
        },
        "additionalProperties": false,
        "required": [
          "href"
        ]
      },
      "linkPreviewBlockObjectResponse": {
        "title": "Link Preview",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "link_preview"
          },
          "link_preview": {
            "$ref": "#/components/schemas/mediaContentWithUrlResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "link_preview",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "linkPreviewMentionResponse": {
        "type": "object",
        "properties": {
          "url": {
            "type": "string",
            "description": "The URL of the link preview mention."
          }
        },
        "additionalProperties": false,
        "required": [
          "url"
        ]
      },
      "linkToPageBlockObjectResponse": {
        "title": "Link To Page",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "link_to_page"
          },
          "link_to_page": {
            "anyOf": [
              {
                "title": "Page Id",
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "page_id"
                  },
                  "page_id": {
                    "$ref": "#/components/schemas/idRequest"
                  }
                },
                "required": [
                  "type",
                  "page_id"
                ]
              },
              {
                "title": "Database Id",
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "database_id"
                  },
                  "database_id": {
                    "$ref": "#/components/schemas/idRequest"
                  }
                },
                "required": [
                  "type",
                  "database_id"
                ]
              },
              {
                "title": "Comment Id",
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "comment_id"
                  },
                  "comment_id": {
                    "$ref": "#/components/schemas/idRequest"
                  }
                },
                "required": [
                  "type",
                  "comment_id"
                ]
              }
            ]
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "link_to_page",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "mediaContentWithFileAndCaptionResponse": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/externalMediaContentWithFileAndCaptionResponse"
          },
          {
            "$ref": "#/components/schemas/fileMediaContentWithFileAndCaptionResponse"
          }
        ]
      },
      "mediaContentWithFileNameAndCaptionResponse": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/externalMediaContentWithFileNameAndCaptionResponse"
          },
          {
            "$ref": "#/components/schemas/fileMediaContentWithFileNameAndCaptionResponse"
          }
        ]
      },
      "mediaContentWithUrlAndCaptionResponse": {
        "type": "object",
        "properties": {
          "url": {
            "type": "string"
          },
          "caption": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/richTextItemResponse"
            },
            "maxItems": 100
          }
        },
        "required": [
          "url",
          "caption"
        ]
      },
      "mediaContentWithUrlResponse": {
        "type": "object",
        "properties": {
          "url": {
            "$ref": "#/components/schemas/textRequest"
          }
        },
        "required": [
          "url"
        ]
      },
      "meetingNotesBlockObjectResponse": {
        "title": "Meeting Notes",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "meeting_notes"
          },
          "meeting_notes": {
            "$ref": "#/components/schemas/transcriptionBlockResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "meeting_notes",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "mentionRichTextItemRequest": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "mention",
            "description": "Always `mention`"
          },
          "mention": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "user",
                    "description": "Always `user`"
                  },
                  "user": {
                    "$ref": "#/components/schemas/partialUserObjectRequest",
                    "description": "Details of the user mention."
                  }
                },
                "required": [
                  "user"
                ],
                "title": "User"
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "date",
                    "description": "Always `date`"
                  },
                  "date": {
                    "$ref": "#/components/schemas/dateRequest",
                    "description": "Details of the date mention."
                  }
                },
                "required": [
                  "date"
                ],
                "title": "Date"
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "page",
                    "description": "Always `page`"
                  },
                  "page": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "$ref": "#/components/schemas/idRequest",
                        "description": "The ID of the page in the mention."
                      }
                    },
                    "required": [
                      "id"
                    ],
                    "description": "Details of the page mention."
                  }
                },
                "required": [
                  "page"
                ],
                "title": "Page"
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "database",
                    "description": "Always `database`"
                  },
                  "database": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "$ref": "#/components/schemas/idRequest",
                        "description": "The ID of the database in the mention."
                      }
                    },
                    "required": [
                      "id"
                    ],
                    "description": "Details of the database mention."
                  }
                },
                "required": [
                  "database"
                ],
                "title": "Database"
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "template_mention",
                    "description": "Always `template_mention`"
                  },
                  "template_mention": {
                    "$ref": "#/components/schemas/templateMentionRequest",
                    "description": "Details of the template mention."
                  }
                },
                "required": [
                  "template_mention"
                ],
                "title": "Template Mention"
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "custom_emoji",
                    "description": "Always `custom_emoji`"
                  },
                  "custom_emoji": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "$ref": "#/components/schemas/idRequest",
                        "description": "The ID of the custom emoji."
                      },
                      "name": {
                        "type": "string",
                        "description": "The name of the custom emoji."
                      },
                      "url": {
                        "type": "string",
                        "description": "The URL of the custom emoji."
                      }
                    },
                    "required": [
                      "id"
                    ],
                    "description": "Details of the custom emoji mention."
                  }
                },
                "required": [
                  "custom_emoji"
                ],
                "title": "Custom Emoji"
              }
            ],
            "description": "Mention objects represent an inline mention of a database, date, link preview mention, page, template mention, or user. A mention is created in the Notion UI when a user types `@` followed by the name of the reference."
          }
        },
        "required": [
          "mention"
        ],
        "title": "Mention"
      },
      "mentionRichTextItemResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "mention",
            "description": "Always `mention`"
          },
          "mention": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "user",
                    "description": "Always `user`"
                  },
                  "user": {
                    "$ref": "#/components/schemas/userValueResponse",
                    "description": "Details of the user mention."
                  }
                },
                "additionalProperties": false,
                "required": [
                  "type",
                  "user"
                ],
                "title": "User"
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "date",
                    "description": "Always `date`"
                  },
                  "date": {
                    "$ref": "#/components/schemas/dateResponse",
                    "description": "Details of the date mention."
                  }
                },
                "additionalProperties": false,
                "required": [
                  "type",
                  "date"
                ],
                "title": "Date"
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "link_preview",
                    "description": "Always `link_preview`"
                  },
                  "link_preview": {
                    "$ref": "#/components/schemas/linkPreviewMentionResponse",
                    "description": "Details of the link preview mention."
                  }
                },
                "additionalProperties": false,
                "required": [
                  "type",
                  "link_preview"
                ],
                "title": "Link Preview"
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "link_mention",
                    "description": "Always `link_mention`"
                  },
                  "link_mention": {
                    "$ref": "#/components/schemas/linkMentionResponse",
                    "description": "Details of the link mention."
                  }
                },
                "additionalProperties": false,
                "required": [
                  "type",
                  "link_mention"
                ],
                "title": "Link Mention"
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "page",
                    "description": "Always `page`"
                  },
                  "page": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "$ref": "#/components/schemas/idResponse",
                        "description": "The ID of the page in the mention."
                      }
                    },
                    "additionalProperties": false,
                    "required": [
                      "id"
                    ],
                    "description": "Details of the page mention."
                  }
                },
                "additionalProperties": false,
                "required": [
                  "type",
                  "page"
                ],
                "title": "Page"
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "database",
                    "description": "Always `database`"
                  },
                  "database": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "$ref": "#/components/schemas/idResponse",
                        "description": "The ID of the database in the mention."
                      }
                    },
                    "additionalProperties": false,
                    "required": [
                      "id"
                    ],
                    "description": "Details of the database mention."
                  }
                },
                "additionalProperties": false,
                "required": [
                  "type",
                  "database"
                ],
                "title": "Database"
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "template_mention",
                    "description": "Always `template_mention`"
                  },
                  "template_mention": {
                    "$ref": "#/components/schemas/templateMentionResponse",
                    "description": "Details of the template mention."
                  }
                },
                "additionalProperties": false,
                "required": [
                  "type",
                  "template_mention"
                ],
                "title": "Template Mention"
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "custom_emoji",
                    "description": "Always `custom_emoji`"
                  },
                  "custom_emoji": {
                    "$ref": "#/components/schemas/customEmojiResponse",
                    "description": "Details of the custom emoji mention."
                  }
                },
                "additionalProperties": false,
                "required": [
                  "type",
                  "custom_emoji"
                ],
                "title": "Custom Emoji"
              }
            ],
            "description": "Mention objects represent an inline mention of a database, date, link preview mention, page, template mention, or user. A mention is created in the Notion UI when a user types `@` followed by the name of the reference."
          }
        },
        "required": [
          "type",
          "mention"
        ],
        "title": "Mention"
      },
      "multiSelectDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "multi_select",
            "description": "Always `multi_select`"
          },
          "multi_select": {
            "type": "object",
            "properties": {
              "options": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/selectPropertyResponse"
                },
                "maxItems": 100
              }
            },
            "additionalProperties": false,
            "required": [
              "options"
            ]
          }
        },
        "required": [
          "type",
          "multi_select"
        ],
        "title": "Multi Select"
      },
      "multiSelectPropertyItemObjectResponse": {
        "title": "Multi Select",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "multi_select"
          },
          "multi_select": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/partialSelectResponse"
            },
            "maxItems": 100
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "multi_select",
          "object",
          "id"
        ]
      },
      "noticonColor": {
        "type": "string",
        "enum": [
          "gray",
          "lightgray",
          "brown",
          "yellow",
          "orange",
          "green",
          "blue",
          "purple",
          "pink",
          "red"
        ],
        "description": "One of: `gray`, `lightgray`, `brown`, `yellow`, `orange`, `green`, `blue`, `purple`, `pink`, `red`"
      },
      "noticonIconResponse": {
        "type": "object",
        "properties": {
          "name": {
            "$ref": "#/components/schemas/noticonName",
            "description": "The name of the Notion icon (e.g. pizza, meeting, home). See the Notion icon picker for valid names."
          },
          "color": {
            "$ref": "#/components/schemas/noticonColor",
            "description": "The color variant of the icon. Valid values: gray, lightgray, brown, yellow, orange, green, blue, purple, pink, red."
          }
        },
        "additionalProperties": false,
        "required": [
          "name",
          "color"
        ]
      },
      "noticonName": {
        "type": "string",
        "examples": [
          "pizza",
          "meeting",
          "home",
          "star",
          "robot"
        ]
      },
      "numberDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "number",
            "description": "Always `number`"
          },
          "number": {
            "type": "object",
            "properties": {
              "format": {
                "$ref": "#/components/schemas/numberFormat",
                "description": "The number format for the property."
              }
            },
            "additionalProperties": false,
            "required": [
              "format"
            ]
          }
        },
        "required": [
          "type",
          "number"
        ],
        "title": "Number"
      },
      "numberFormat": {
        "type": "string"
      },
      "numberFormulaPropertyResponse": {
        "title": "Number",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "number"
          },
          "number": {
            "type": [
              "number",
              "null"
            ]
          }
        },
        "required": [
          "type",
          "number"
        ]
      },
      "numberPropertyItemObjectResponse": {
        "title": "Number",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "number"
          },
          "number": {
            "type": [
              "number",
              "null"
            ]
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "number",
          "object",
          "id"
        ]
      },
      "numberedListFormat": {
        "type": "string",
        "enum": [
          "numbers",
          "letters",
          "roman"
        ]
      },
      "numberedListItemBlockObjectResponse": {
        "title": "Numbered List Item",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "numbered_list_item"
          },
          "numbered_list_item": {
            "$ref": "#/components/schemas/contentWithRichTextAndColorAndListResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "numbered_list_item",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "pageCoverResponse": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/filePageCoverResponse"
          },
          {
            "$ref": "#/components/schemas/externalPageCoverResponse"
          }
        ]
      },
      "pageIconRequest": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/fileUploadPageIconRequest"
          },
          {
            "$ref": "#/components/schemas/emojiPageIconRequest"
          },
          {
            "$ref": "#/components/schemas/externalPageIconRequest"
          },
          {
            "$ref": "#/components/schemas/customEmojiPageIconRequest"
          },
          {
            "$ref": "#/components/schemas/iconPageIconRequest"
          }
        ]
      },
      "pageIconResponse": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/emojiPageIconResponse"
          },
          {
            "$ref": "#/components/schemas/filePageIconResponse"
          },
          {
            "$ref": "#/components/schemas/externalPageIconResponse"
          },
          {
            "$ref": "#/components/schemas/customEmojiPageIconResponse"
          },
          {
            "$ref": "#/components/schemas/iconPageIconResponse"
          }
        ]
      },
      "pageIdCommentParentResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "page_id",
            "description": "Always `page_id`"
          },
          "page_id": {
            "$ref": "#/components/schemas/idResponse"
          }
        },
        "additionalProperties": false,
        "required": [
          "type",
          "page_id"
        ],
        "title": "Page Id"
      },
      "pageIdParentForBlockBasedObjectResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "page_id",
            "description": "The parent type."
          },
          "page_id": {
            "$ref": "#/components/schemas/idResponse",
            "description": "The ID of the parent page."
          }
        },
        "additionalProperties": false,
        "required": [
          "type",
          "page_id"
        ]
      },
      "pageObjectResponse": {
        "type": "object",
        "properties": {
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "properties": {
            "type": "object",
            "additionalProperties": {
              "anyOf": [
                {
                  "title": "Number",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "number"
                    },
                    "number": {
                      "type": [
                        "number",
                        "null"
                      ]
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "number",
                    "id"
                  ]
                },
                {
                  "title": "Url",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "url"
                    },
                    "url": {
                      "type": [
                        "string",
                        "null"
                      ]
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "url",
                    "id"
                  ]
                },
                {
                  "title": "Select",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "select"
                    },
                    "select": {
                      "anyOf": [
                        {
                          "$ref": "#/components/schemas/partialSelectResponse"
                        },
                        {
                          "type": "null"
                        }
                      ]
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "select",
                    "id"
                  ]
                },
                {
                  "title": "Multi Select",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "multi_select"
                    },
                    "multi_select": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/partialSelectResponse"
                      },
                      "maxItems": 100
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "multi_select",
                    "id"
                  ]
                },
                {
                  "title": "Status",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "status"
                    },
                    "status": {
                      "anyOf": [
                        {
                          "$ref": "#/components/schemas/partialSelectResponse"
                        },
                        {
                          "type": "null"
                        }
                      ]
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "status",
                    "id"
                  ]
                },
                {
                  "title": "Date",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "date"
                    },
                    "date": {
                      "anyOf": [
                        {
                          "$ref": "#/components/schemas/dateResponse"
                        },
                        {
                          "type": "null"
                        }
                      ]
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "date",
                    "id"
                  ]
                },
                {
                  "title": "Email",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "email"
                    },
                    "email": {
                      "type": [
                        "string",
                        "null"
                      ]
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "email",
                    "id"
                  ]
                },
                {
                  "title": "Phone Number",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "phone_number"
                    },
                    "phone_number": {
                      "type": [
                        "string",
                        "null"
                      ]
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "phone_number",
                    "id"
                  ]
                },
                {
                  "title": "Checkbox",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "checkbox"
                    },
                    "checkbox": {
                      "type": "boolean"
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "checkbox",
                    "id"
                  ]
                },
                {
                  "title": "Files",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "files"
                    },
                    "files": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/internalOrExternalFileWithNameResponse"
                      },
                      "maxItems": 100
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "files",
                    "id"
                  ]
                },
                {
                  "title": "Created By",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "created_by"
                    },
                    "created_by": {
                      "anyOf": [
                        {
                          "$ref": "#/components/schemas/partialUserObjectResponse"
                        },
                        {
                          "$ref": "#/components/schemas/userObjectResponse"
                        }
                      ]
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "created_by",
                    "id"
                  ]
                },
                {
                  "title": "Created Time",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "created_time"
                    },
                    "created_time": {
                      "type": "string",
                      "format": "date-time"
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "created_time",
                    "id"
                  ]
                },
                {
                  "title": "Last Edited By",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "last_edited_by"
                    },
                    "last_edited_by": {
                      "anyOf": [
                        {
                          "$ref": "#/components/schemas/partialUserObjectResponse"
                        },
                        {
                          "$ref": "#/components/schemas/userObjectResponse"
                        }
                      ]
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "last_edited_by",
                    "id"
                  ]
                },
                {
                  "title": "Last Edited Time",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "last_edited_time"
                    },
                    "last_edited_time": {
                      "type": "string",
                      "format": "date-time"
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "last_edited_time",
                    "id"
                  ]
                },
                {
                  "title": "Formula",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "formula"
                    },
                    "formula": {
                      "$ref": "#/components/schemas/formulaPropertyResponse"
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "formula",
                    "id"
                  ]
                },
                {
                  "title": "Button",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "button"
                    },
                    "button": {
                      "$ref": "#/components/schemas/emptyObject"
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "button",
                    "id"
                  ]
                },
                {
                  "title": "Unique Id",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "unique_id"
                    },
                    "unique_id": {
                      "type": "object",
                      "properties": {
                        "prefix": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "number": {
                          "type": [
                            "number",
                            "null"
                          ]
                        }
                      },
                      "required": [
                        "prefix",
                        "number"
                      ]
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "unique_id",
                    "id"
                  ]
                },
                {
                  "title": "Verification",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "verification"
                    },
                    "verification": {
                      "anyOf": [
                        {
                          "$ref": "#/components/schemas/verificationPropertyValueResponse"
                        },
                        {
                          "type": "null"
                        }
                      ]
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "verification",
                    "id"
                  ]
                },
                {
                  "title": "Place",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "place"
                    },
                    "place": {
                      "type": [
                        "object",
                        "null"
                      ],
                      "properties": {
                        "lat": {
                          "type": "number"
                        },
                        "lon": {
                          "type": "number"
                        },
                        "name": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "address": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "aws_place_id": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "google_place_id": {
                          "type": [
                            "string",
                            "null"
                          ]
                        }
                      },
                      "required": [
                        "lat",
                        "lon"
                      ]
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "place",
                    "id"
                  ]
                },
                {
                  "title": "Title",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "title"
                    },
                    "title": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/richTextItemResponse"
                      },
                      "maxItems": 100
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "title",
                    "id"
                  ]
                },
                {
                  "title": "Rich Text",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "rich_text"
                    },
                    "rich_text": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/richTextItemResponse"
                      },
                      "maxItems": 100
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "rich_text",
                    "id"
                  ]
                },
                {
                  "title": "People",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "people"
                    },
                    "people": {
                      "type": "array",
                      "items": {
                        "anyOf": [
                          {
                            "anyOf": [
                              {
                                "$ref": "#/components/schemas/partialUserObjectResponse"
                              },
                              {
                                "$ref": "#/components/schemas/userObjectResponse"
                              }
                            ]
                          },
                          {
                            "$ref": "#/components/schemas/groupObjectResponse"
                          }
                        ]
                      },
                      "maxItems": 100
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "people",
                    "id"
                  ]
                },
                {
                  "title": "Relation",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "relation"
                    },
                    "relation": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string",
                            "format": "uuid"
                          }
                        },
                        "required": [
                          "id"
                        ]
                      },
                      "maxItems": 100
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "relation",
                    "id"
                  ]
                },
                {
                  "title": "Rollup",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "rollup"
                    },
                    "rollup": {
                      "anyOf": [
                        {
                          "title": "Number",
                          "type": "object",
                          "properties": {
                            "type": {
                              "type": "string",
                              "const": "number"
                            },
                            "number": {
                              "type": [
                                "number",
                                "null"
                              ]
                            },
                            "function": {
                              "$ref": "#/components/schemas/rollupFunction"
                            }
                          },
                          "required": [
                            "type",
                            "number",
                            "function"
                          ]
                        },
                        {
                          "title": "Date",
                          "type": "object",
                          "properties": {
                            "type": {
                              "type": "string",
                              "const": "date"
                            },
                            "date": {
                              "anyOf": [
                                {
                                  "$ref": "#/components/schemas/dateResponse"
                                },
                                {
                                  "type": "null"
                                }
                              ]
                            },
                            "function": {
                              "$ref": "#/components/schemas/rollupFunction"
                            }
                          },
                          "required": [
                            "type",
                            "date",
                            "function"
                          ]
                        },
                        {
                          "title": "Array",
                          "type": "object",
                          "properties": {
                            "type": {
                              "type": "string",
                              "const": "array"
                            },
                            "array": {
                              "type": "array",
                              "items": {
                                "anyOf": [
                                  {
                                    "title": "Number",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "number"
                                      },
                                      "number": {
                                        "type": [
                                          "number",
                                          "null"
                                        ]
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "number"
                                    ]
                                  },
                                  {
                                    "title": "Url",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "url"
                                      },
                                      "url": {
                                        "type": [
                                          "string",
                                          "null"
                                        ]
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "url"
                                    ]
                                  },
                                  {
                                    "title": "Select",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "select"
                                      },
                                      "select": {
                                        "anyOf": [
                                          {
                                            "$ref": "#/components/schemas/partialSelectResponse"
                                          },
                                          {
                                            "type": "null"
                                          }
                                        ]
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "select"
                                    ]
                                  },
                                  {
                                    "title": "Multi Select",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "multi_select"
                                      },
                                      "multi_select": {
                                        "type": "array",
                                        "items": {
                                          "$ref": "#/components/schemas/partialSelectResponse"
                                        },
                                        "maxItems": 100
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "multi_select"
                                    ]
                                  },
                                  {
                                    "title": "Status",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "status"
                                      },
                                      "status": {
                                        "anyOf": [
                                          {
                                            "$ref": "#/components/schemas/partialSelectResponse"
                                          },
                                          {
                                            "type": "null"
                                          }
                                        ]
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "status"
                                    ]
                                  },
                                  {
                                    "title": "Date",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "date"
                                      },
                                      "date": {
                                        "anyOf": [
                                          {
                                            "$ref": "#/components/schemas/dateResponse"
                                          },
                                          {
                                            "type": "null"
                                          }
                                        ]
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "date"
                                    ]
                                  },
                                  {
                                    "title": "Email",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "email"
                                      },
                                      "email": {
                                        "type": [
                                          "string",
                                          "null"
                                        ]
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "email"
                                    ]
                                  },
                                  {
                                    "title": "Phone Number",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "phone_number"
                                      },
                                      "phone_number": {
                                        "type": [
                                          "string",
                                          "null"
                                        ]
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "phone_number"
                                    ]
                                  },
                                  {
                                    "title": "Checkbox",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "checkbox"
                                      },
                                      "checkbox": {
                                        "type": "boolean"
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "checkbox"
                                    ]
                                  },
                                  {
                                    "title": "Files",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "files"
                                      },
                                      "files": {
                                        "type": "array",
                                        "items": {
                                          "$ref": "#/components/schemas/internalOrExternalFileWithNameResponse"
                                        },
                                        "maxItems": 100
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "files"
                                    ]
                                  },
                                  {
                                    "title": "Created By",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "created_by"
                                      },
                                      "created_by": {
                                        "anyOf": [
                                          {
                                            "$ref": "#/components/schemas/partialUserObjectResponse"
                                          },
                                          {
                                            "$ref": "#/components/schemas/userObjectResponse"
                                          }
                                        ]
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "created_by"
                                    ]
                                  },
                                  {
                                    "title": "Created Time",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "created_time"
                                      },
                                      "created_time": {
                                        "type": "string",
                                        "format": "date-time"
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "created_time"
                                    ]
                                  },
                                  {
                                    "title": "Last Edited By",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "last_edited_by"
                                      },
                                      "last_edited_by": {
                                        "anyOf": [
                                          {
                                            "$ref": "#/components/schemas/partialUserObjectResponse"
                                          },
                                          {
                                            "$ref": "#/components/schemas/userObjectResponse"
                                          }
                                        ]
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "last_edited_by"
                                    ]
                                  },
                                  {
                                    "title": "Last Edited Time",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "last_edited_time"
                                      },
                                      "last_edited_time": {
                                        "type": "string",
                                        "format": "date-time"
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "last_edited_time"
                                    ]
                                  },
                                  {
                                    "title": "Formula",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "formula"
                                      },
                                      "formula": {
                                        "$ref": "#/components/schemas/formulaPropertyResponse"
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "formula"
                                    ]
                                  },
                                  {
                                    "title": "Button",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "button"
                                      },
                                      "button": {
                                        "$ref": "#/components/schemas/emptyObject"
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "button"
                                    ]
                                  },
                                  {
                                    "title": "Unique Id",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "unique_id"
                                      },
                                      "unique_id": {
                                        "type": "object",
                                        "properties": {
                                          "prefix": {
                                            "type": [
                                              "string",
                                              "null"
                                            ]
                                          },
                                          "number": {
                                            "type": [
                                              "number",
                                              "null"
                                            ]
                                          }
                                        },
                                        "required": [
                                          "prefix",
                                          "number"
                                        ]
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "unique_id"
                                    ]
                                  },
                                  {
                                    "title": "Verification",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "verification"
                                      },
                                      "verification": {
                                        "anyOf": [
                                          {
                                            "$ref": "#/components/schemas/verificationPropertyValueResponse"
                                          },
                                          {
                                            "type": "null"
                                          }
                                        ]
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "verification"
                                    ]
                                  },
                                  {
                                    "title": "Place",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "place"
                                      },
                                      "place": {
                                        "type": [
                                          "object",
                                          "null"
                                        ],
                                        "properties": {
                                          "lat": {
                                            "type": "number"
                                          },
                                          "lon": {
                                            "type": "number"
                                          },
                                          "name": {
                                            "type": [
                                              "string",
                                              "null"
                                            ]
                                          },
                                          "address": {
                                            "type": [
                                              "string",
                                              "null"
                                            ]
                                          },
                                          "aws_place_id": {
                                            "type": [
                                              "string",
                                              "null"
                                            ]
                                          },
                                          "google_place_id": {
                                            "type": [
                                              "string",
                                              "null"
                                            ]
                                          }
                                        },
                                        "required": [
                                          "lat",
                                          "lon"
                                        ]
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "place"
                                    ]
                                  },
                                  {
                                    "title": "Title",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "title"
                                      },
                                      "title": {
                                        "type": "array",
                                        "items": {
                                          "$ref": "#/components/schemas/richTextItemResponse"
                                        },
                                        "maxItems": 100
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "title"
                                    ]
                                  },
                                  {
                                    "title": "Rich Text",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "rich_text"
                                      },
                                      "rich_text": {
                                        "type": "array",
                                        "items": {
                                          "$ref": "#/components/schemas/richTextItemResponse"
                                        },
                                        "maxItems": 100
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "rich_text"
                                    ]
                                  },
                                  {
                                    "title": "People",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "people"
                                      },
                                      "people": {
                                        "type": "array",
                                        "items": {
                                          "anyOf": [
                                            {
                                              "anyOf": [
                                                {
                                                  "$ref": "#/components/schemas/partialUserObjectResponse"
                                                },
                                                {
                                                  "$ref": "#/components/schemas/userObjectResponse"
                                                }
                                              ]
                                            },
                                            {
                                              "$ref": "#/components/schemas/groupObjectResponse"
                                            }
                                          ]
                                        },
                                        "maxItems": 100
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "people"
                                    ]
                                  },
                                  {
                                    "title": "Relation",
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "relation"
                                      },
                                      "relation": {
                                        "type": "array",
                                        "items": {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              "type": "string",
                                              "format": "uuid"
                                            }
                                          },
                                          "required": [
                                            "id"
                                          ]
                                        },
                                        "maxItems": 100
                                      }
                                    },
                                    "required": [
                                      "type",
                                      "relation"
                                    ]
                                  }
                                ]
                              },
                              "maxItems": 100
                            },
                            "function": {
                              "$ref": "#/components/schemas/rollupFunction"
                            }
                          },
                          "required": [
                            "type",
                            "array",
                            "function"
                          ]
                        }
                      ]
                    },
                    "id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "type",
                    "rollup",
                    "id"
                  ]
                }
              ]
            }
          },
          "icon": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/pageIconResponse"
              },
              {
                "type": "null"
              }
            ]
          },
          "cover": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/pageCoverResponse"
              },
              {
                "type": "null"
              }
            ]
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "is_locked": {
            "description": "Whether the page is locked from editing in the Notion app UI.",
            "type": "boolean"
          },
          "object": {
            "type": "string",
            "const": "page"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "in_trash": {
            "type": "boolean"
          },
          "is_archived": {
            "type": "boolean"
          },
          "url": {
            "type": "string"
          },
          "public_url": {
            "type": [
              "string",
              "null"
            ]
          }
        },
        "required": [
          "parent",
          "properties",
          "icon",
          "cover",
          "created_by",
          "last_edited_by",
          "is_locked",
          "object",
          "id",
          "created_time",
          "last_edited_time",
          "in_trash",
          "is_archived",
          "url",
          "public_url"
        ]
      },
      "paragraphBlockObjectResponse": {
        "title": "Paragraph",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "paragraph"
          },
          "paragraph": {
            "$ref": "#/components/schemas/contentWithRichTextColorAndIconResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "paragraph",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "parentForBlockBasedObjectResponse": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/databaseParentResponse"
          },
          {
            "$ref": "#/components/schemas/dataSourceParentResponse"
          },
          {
            "$ref": "#/components/schemas/pageIdParentForBlockBasedObjectResponse"
          },
          {
            "$ref": "#/components/schemas/blockIdParentForBlockBasedObjectResponse"
          },
          {
            "$ref": "#/components/schemas/workspaceParentForBlockBasedObjectResponse"
          }
        ]
      },
      "parentOfDataSourceResponse": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/databaseParentResponse"
          },
          {
            "$ref": "#/components/schemas/dataSourceParentResponse"
          }
        ],
        "description": "The parent of the data source. This is typically a database (`database_id`), but for externally synced data sources, can be another data source (`data_source_id`)."
      },
      "parentOfDatabaseResponse": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/pageIdParentForBlockBasedObjectResponse"
          },
          {
            "$ref": "#/components/schemas/workspaceParentForBlockBasedObjectResponse"
          },
          {
            "$ref": "#/components/schemas/databaseParentResponse"
          },
          {
            "$ref": "#/components/schemas/blockIdParentForBlockBasedObjectResponse"
          }
        ]
      },
      "partialBlockObjectResponse": {
        "type": "object",
        "properties": {
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          }
        },
        "required": [
          "object",
          "id"
        ]
      },
      "partialCommentObjectResponse": {
        "type": "object",
        "properties": {
          "object": {
            "type": "string",
            "const": "comment",
            "description": "The comment object type name."
          },
          "id": {
            "$ref": "#/components/schemas/idResponse",
            "description": "The ID of the comment."
          }
        },
        "additionalProperties": false,
        "required": [
          "object",
          "id"
        ]
      },
      "partialDataSourceObjectResponse": {
        "type": "object",
        "properties": {
          "object": {
            "type": "string",
            "const": "data_source",
            "description": "The data source object type name."
          },
          "id": {
            "$ref": "#/components/schemas/idResponse",
            "description": "The ID of the data source."
          },
          "properties": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/databasePropertyConfigResponse"
            },
            "description": "The properties schema of the data source."
          }
        },
        "additionalProperties": false,
        "required": [
          "object",
          "id",
          "properties"
        ]
      },
      "partialPageObjectResponse": {
        "type": "object",
        "properties": {
          "object": {
            "type": "string",
            "const": "page"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          }
        },
        "required": [
          "object",
          "id"
        ]
      },
      "partialSelectResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "color": {
            "$ref": "#/components/schemas/selectColor"
          }
        },
        "required": [
          "id",
          "name",
          "color"
        ]
      },
      "partialUserObjectRequest": {
        "type": "object",
        "properties": {
          "id": {
            "$ref": "#/components/schemas/idRequest",
            "description": "The ID of the user."
          },
          "object": {
            "type": "string",
            "const": "user",
            "description": "The user object type name."
          }
        },
        "required": [
          "id"
        ]
      },
      "partialUserObjectResponse": {
        "type": "object",
        "properties": {
          "id": {
            "$ref": "#/components/schemas/idResponse"
          },
          "object": {
            "type": "string",
            "const": "user",
            "description": "Always `user`"
          }
        },
        "additionalProperties": false,
        "required": [
          "id",
          "object"
        ]
      },
      "pdfBlockObjectResponse": {
        "title": "Pdf",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "pdf"
          },
          "pdf": {
            "$ref": "#/components/schemas/mediaContentWithFileAndCaptionResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "pdf",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "peopleDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "people",
            "description": "Always `people`"
          },
          "people": {
            "$ref": "#/components/schemas/emptyObject"
          }
        },
        "required": [
          "type",
          "people"
        ],
        "title": "People"
      },
      "peoplePropertyItemObjectResponse": {
        "title": "People",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "people"
          },
          "people": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/partialUserObjectResponse"
              },
              {
                "$ref": "#/components/schemas/userObjectResponse"
              }
            ]
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "people",
          "object",
          "id"
        ]
      },
      "personUserObjectResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "person",
            "description": "Indicates this user is a person."
          },
          "person": {
            "type": "object",
            "properties": {
              "email": {
                "type": "string",
                "description": "The email of the person."
              }
            },
            "additionalProperties": false,
            "description": "Details about the person, when the `type` of the user is `person`."
          }
        },
        "required": [
          "type",
          "person"
        ],
        "title": "Person"
      },
      "phoneNumberDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "phone_number",
            "description": "Always `phone_number`"
          },
          "phone_number": {
            "$ref": "#/components/schemas/emptyObject"
          }
        },
        "required": [
          "type",
          "phone_number"
        ],
        "title": "Phone Number"
      },
      "phoneNumberPropertyItemObjectResponse": {
        "title": "Phone Number",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "phone_number"
          },
          "phone_number": {
            "type": [
              "string",
              "null"
            ]
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "phone_number",
          "object",
          "id"
        ]
      },
      "placePropertyItemObjectResponse": {
        "title": "Place",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "place"
          },
          "place": {
            "type": [
              "object",
              "null"
            ],
            "properties": {
              "lat": {
                "type": "number"
              },
              "lon": {
                "type": "number"
              },
              "name": {
                "type": [
                  "string",
                  "null"
                ]
              },
              "address": {
                "type": [
                  "string",
                  "null"
                ]
              },
              "aws_place_id": {
                "type": [
                  "string",
                  "null"
                ]
              },
              "google_place_id": {
                "type": [
                  "string",
                  "null"
                ]
              }
            },
            "required": [
              "lat",
              "lon"
            ]
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "place",
          "object",
          "id"
        ]
      },
      "propertyDescriptionRequest": {
        "type": "string",
        "minLength": 1,
        "maxLength": 280
      },
      "propertyItemListResponse": {
        "$ref": "#/components/schemas/propertyItemPropertyItemListResponse"
      },
      "propertyItemObjectResponse": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/numberPropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/urlPropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/selectPropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/multiSelectPropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/statusPropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/datePropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/emailPropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/phoneNumberPropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/checkboxPropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/filesPropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/createdByPropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/createdTimePropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/lastEditedByPropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/lastEditedTimePropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/formulaPropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/buttonPropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/uniqueIdPropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/verificationPropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/placePropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/titlePropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/richTextPropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/peoplePropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/relationPropertyItemObjectResponse"
          },
          {
            "$ref": "#/components/schemas/rollupPropertyItemObjectResponse"
          }
        ]
      },
      "propertyItemPropertyItemListResponse": {
        "title": "Property Item",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "property_item"
          },
          "property_item": {
            "anyOf": [
              {
                "title": "Title",
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "title"
                  },
                  "title": {
                    "$ref": "#/components/schemas/emptyObject"
                  },
                  "next_url": {
                    "type": [
                      "string",
                      "null"
                    ]
                  },
                  "id": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "title",
                  "next_url",
                  "id"
                ]
              },
              {
                "title": "Rich Text",
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "rich_text"
                  },
                  "rich_text": {
                    "$ref": "#/components/schemas/emptyObject"
                  },
                  "next_url": {
                    "type": [
                      "string",
                      "null"
                    ]
                  },
                  "id": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "rich_text",
                  "next_url",
                  "id"
                ]
              },
              {
                "title": "People",
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "people"
                  },
                  "people": {
                    "$ref": "#/components/schemas/emptyObject"
                  },
                  "next_url": {
                    "type": [
                      "string",
                      "null"
                    ]
                  },
                  "id": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "people",
                  "next_url",
                  "id"
                ]
              },
              {
                "title": "Relation",
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "relation"
                  },
                  "relation": {
                    "$ref": "#/components/schemas/emptyObject"
                  },
                  "next_url": {
                    "type": [
                      "string",
                      "null"
                    ]
                  },
                  "id": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "relation",
                  "next_url",
                  "id"
                ]
              },
              {
                "title": "Rollup",
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "rollup"
                  },
                  "rollup": {
                    "anyOf": [
                      {
                        "title": "Number",
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "number"
                          },
                          "number": {
                            "type": [
                              "number",
                              "null"
                            ]
                          },
                          "function": {
                            "$ref": "#/components/schemas/rollupFunction"
                          }
                        },
                        "required": [
                          "type",
                          "number",
                          "function"
                        ]
                      },
                      {
                        "title": "Date",
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "date"
                          },
                          "date": {
                            "anyOf": [
                              {
                                "$ref": "#/components/schemas/dateResponse"
                              },
                              {
                                "type": "null"
                              }
                            ]
                          },
                          "function": {
                            "$ref": "#/components/schemas/rollupFunction"
                          }
                        },
                        "required": [
                          "type",
                          "date",
                          "function"
                        ]
                      },
                      {
                        "title": "Array",
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "array"
                          },
                          "array": {
                            "type": "array",
                            "items": {
                              "$ref": "#/components/schemas/emptyObject"
                            },
                            "maxItems": 100
                          },
                          "function": {
                            "$ref": "#/components/schemas/rollupFunction"
                          }
                        },
                        "required": [
                          "type",
                          "array",
                          "function"
                        ]
                      },
                      {
                        "title": "Unsupported",
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "unsupported"
                          },
                          "unsupported": {
                            "$ref": "#/components/schemas/emptyObject"
                          },
                          "function": {
                            "$ref": "#/components/schemas/rollupFunction"
                          }
                        },
                        "required": [
                          "type",
                          "unsupported",
                          "function"
                        ]
                      },
                      {
                        "title": "Incomplete",
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "incomplete"
                          },
                          "incomplete": {
                            "$ref": "#/components/schemas/emptyObject"
                          },
                          "function": {
                            "$ref": "#/components/schemas/rollupFunction"
                          }
                        },
                        "required": [
                          "type",
                          "incomplete",
                          "function"
                        ]
                      }
                    ]
                  },
                  "next_url": {
                    "type": [
                      "string",
                      "null"
                    ]
                  },
                  "id": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "rollup",
                  "next_url",
                  "id"
                ]
              }
            ]
          },
          "object": {
            "type": "string",
            "const": "list"
          },
          "next_cursor": {
            "type": [
              "string",
              "null"
            ]
          },
          "has_more": {
            "type": "boolean"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/propertyItemObjectResponse"
            }
          }
        },
        "required": [
          "type",
          "property_item",
          "object",
          "next_cursor",
          "has_more",
          "results"
        ]
      },
      "publicApiCommonErrorResponse": {
        "type": "object",
        "properties": {
          "object": {
            "const": "error"
          },
          "message": {
            "type": "string"
          },
          "additional_data": {
            "type": "object",
            "additionalProperties": {
              "oneOf": [
                {
                  "type": "string"
                },
                {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                }
              ]
            }
          }
        },
        "required": [
          "object",
          "message"
        ]
      },
      "quoteBlockObjectResponse": {
        "title": "Quote",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "quote"
          },
          "quote": {
            "$ref": "#/components/schemas/contentWithRichTextAndColorResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "quote",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "relationDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "relation",
            "description": "Always `relation`"
          },
          "relation": {
            "$ref": "#/components/schemas/databasePropertyRelationConfigResponse"
          }
        },
        "required": [
          "type",
          "relation"
        ],
        "title": "Relation"
      },
      "relationPropertyItemObjectResponse": {
        "title": "Relation",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "relation"
          },
          "relation": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            },
            "required": [
              "id"
            ]
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "relation",
          "object",
          "id"
        ]
      },
      "richTextDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "rich_text",
            "description": "Always `rich_text`"
          },
          "rich_text": {
            "$ref": "#/components/schemas/emptyObject"
          }
        },
        "required": [
          "type",
          "rich_text"
        ],
        "title": "Rich Text"
      },
      "richTextItemRequest": {
        "allOf": [
          {
            "$ref": "#/components/schemas/richTextItemRequestCommon"
          },
          {
            "oneOf": [
              {
                "$ref": "#/components/schemas/textRichTextItemRequest"
              },
              {
                "$ref": "#/components/schemas/mentionRichTextItemRequest"
              },
              {
                "$ref": "#/components/schemas/equationRichTextItemRequest"
              }
            ]
          }
        ]
      },
      "richTextItemRequestCommon": {
        "type": "object",
        "properties": {
          "annotations": {
            "$ref": "#/components/schemas/annotationRequest",
            "description": "All rich text objects contain an annotations object that sets the styling for the rich text."
          }
        }
      },
      "richTextItemResponse": {
        "allOf": [
          {
            "$ref": "#/components/schemas/richTextItemResponseCommon"
          },
          {
            "oneOf": [
              {
                "$ref": "#/components/schemas/textRichTextItemResponse"
              },
              {
                "$ref": "#/components/schemas/mentionRichTextItemResponse"
              },
              {
                "$ref": "#/components/schemas/equationRichTextItemResponse"
              }
            ]
          }
        ]
      },
      "richTextItemResponseCommon": {
        "type": "object",
        "properties": {
          "plain_text": {
            "type": "string",
            "description": "The plain text content of the rich text object, without any styling."
          },
          "href": {
            "oneOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "description": "A URL that the rich text object links to or mentions."
          },
          "annotations": {
            "$ref": "#/components/schemas/annotationResponse",
            "description": "All rich text objects contain an annotations object that sets the styling for the rich text."
          }
        },
        "additionalProperties": false,
        "required": [
          "plain_text",
          "href",
          "annotations"
        ]
      },
      "richTextPropertyItemObjectResponse": {
        "title": "Rich Text",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "rich_text"
          },
          "rich_text": {
            "$ref": "#/components/schemas/richTextItemResponse"
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "rich_text",
          "object",
          "id"
        ]
      },
      "rollupDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "rollup",
            "description": "Always `rollup`"
          },
          "rollup": {
            "type": "object",
            "properties": {
              "function": {
                "$ref": "#/components/schemas/rollupFunction",
                "description": "The function to use for the rollup, e.g. count, count_values, percent_not_empty, max."
              },
              "rollup_property_name": {
                "type": "string"
              },
              "relation_property_name": {
                "type": "string"
              },
              "rollup_property_id": {
                "type": "string"
              },
              "relation_property_id": {
                "type": "string"
              }
            },
            "additionalProperties": false,
            "required": [
              "function",
              "rollup_property_name",
              "relation_property_name",
              "rollup_property_id",
              "relation_property_id"
            ]
          }
        },
        "required": [
          "type",
          "rollup"
        ],
        "title": "Rollup"
      },
      "rollupFunction": {
        "type": "string",
        "enum": [
          "average",
          "checked",
          "count_per_group",
          "count",
          "count_values",
          "date_range",
          "earliest_date",
          "empty",
          "latest_date",
          "max",
          "median",
          "min",
          "not_empty",
          "percent_checked",
          "percent_empty",
          "percent_not_empty",
          "percent_per_group",
          "percent_unchecked",
          "range",
          "unchecked",
          "unique",
          "show_original",
          "show_unique",
          "sum"
        ]
      },
      "rollupPropertyItemObjectResponse": {
        "title": "Rollup",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "rollup"
          },
          "rollup": {
            "anyOf": [
              {
                "title": "Number",
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "number"
                  },
                  "number": {
                    "type": [
                      "number",
                      "null"
                    ]
                  },
                  "function": {
                    "$ref": "#/components/schemas/rollupFunction"
                  }
                },
                "required": [
                  "type",
                  "number",
                  "function"
                ]
              },
              {
                "title": "Date",
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "date"
                  },
                  "date": {
                    "anyOf": [
                      {
                        "$ref": "#/components/schemas/dateResponse"
                      },
                      {
                        "type": "null"
                      }
                    ]
                  },
                  "function": {
                    "$ref": "#/components/schemas/rollupFunction"
                  }
                },
                "required": [
                  "type",
                  "date",
                  "function"
                ]
              },
              {
                "title": "Array",
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "array"
                  },
                  "array": {
                    "type": "array",
                    "items": {
                      "$ref": "#/components/schemas/emptyObject"
                    },
                    "maxItems": 100
                  },
                  "function": {
                    "$ref": "#/components/schemas/rollupFunction"
                  }
                },
                "required": [
                  "type",
                  "array",
                  "function"
                ]
              },
              {
                "title": "Unsupported",
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "unsupported"
                  },
                  "unsupported": {
                    "$ref": "#/components/schemas/emptyObject"
                  },
                  "function": {
                    "$ref": "#/components/schemas/rollupFunction"
                  }
                },
                "required": [
                  "type",
                  "unsupported",
                  "function"
                ]
              },
              {
                "title": "Incomplete",
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "incomplete"
                  },
                  "incomplete": {
                    "$ref": "#/components/schemas/emptyObject"
                  },
                  "function": {
                    "$ref": "#/components/schemas/rollupFunction"
                  }
                },
                "required": [
                  "type",
                  "incomplete",
                  "function"
                ]
              }
            ]
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "rollup",
          "object",
          "id"
        ]
      },
      "selectColor": {
        "type": "string",
        "enum": [
          "default",
          "gray",
          "brown",
          "orange",
          "yellow",
          "green",
          "blue",
          "purple",
          "pink",
          "red"
        ],
        "description": "One of: `default`, `gray`, `brown`, `orange`, `yellow`, `green`, `blue`, `purple`, `pink`, `red`"
      },
      "selectDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "select",
            "description": "Always `select`"
          },
          "select": {
            "type": "object",
            "properties": {
              "options": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/selectPropertyResponse"
                },
                "maxItems": 100
              }
            },
            "additionalProperties": false,
            "required": [
              "options"
            ]
          }
        },
        "required": [
          "type",
          "select"
        ],
        "title": "Select"
      },
      "selectPropertyItemObjectResponse": {
        "title": "Select",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "select"
          },
          "select": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/partialSelectResponse"
              },
              {
                "type": "null"
              }
            ]
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "select",
          "object",
          "id"
        ]
      },
      "selectPropertyResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "color": {
            "$ref": "#/components/schemas/selectColor"
          },
          "description": {
            "oneOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ]
          }
        },
        "additionalProperties": false,
        "required": [
          "id",
          "name",
          "color",
          "description"
        ]
      },
      "singlePropertyDatabasePropertyRelationConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "single_property",
            "description": "Always `single_property`"
          },
          "single_property": {
            "$ref": "#/components/schemas/emptyObject"
          }
        },
        "required": [
          "type",
          "single_property"
        ],
        "title": "Single Property"
      },
      "statusDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "status",
            "description": "Always `status`"
          },
          "status": {
            "type": "object",
            "properties": {
              "options": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/statusPropertyResponse"
                },
                "maxItems": 100,
                "description": "The options for the status property."
              },
              "groups": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "description": "The ID of the status group."
                    },
                    "name": {
                      "type": "string",
                      "description": "The name of the status group."
                    },
                    "color": {
                      "$ref": "#/components/schemas/selectColor",
                      "description": "The color of the status group."
                    },
                    "option_ids": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      },
                      "maxItems": 100,
                      "description": "The IDs of the status options in this group."
                    }
                  },
                  "additionalProperties": false,
                  "required": [
                    "id",
                    "name",
                    "color",
                    "option_ids"
                  ]
                },
                "maxItems": 100,
                "description": "The groups for the status property."
              }
            },
            "additionalProperties": false,
            "required": [
              "options",
              "groups"
            ]
          }
        },
        "required": [
          "type",
          "status"
        ],
        "title": "Status"
      },
      "statusPropertyItemObjectResponse": {
        "title": "Status",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "status"
          },
          "status": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/partialSelectResponse"
              },
              {
                "type": "null"
              }
            ]
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "status",
          "object",
          "id"
        ]
      },
      "statusPropertyResponse": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "The ID of the status option."
          },
          "name": {
            "type": "string",
            "description": "The name of the status option."
          },
          "color": {
            "$ref": "#/components/schemas/selectColor",
            "description": "The color of the status option."
          },
          "description": {
            "oneOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "description": "The description of the status option."
          }
        },
        "additionalProperties": false,
        "required": [
          "id",
          "name",
          "color",
          "description"
        ]
      },
      "stringFormulaPropertyResponse": {
        "title": "String",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "string"
          },
          "string": {
            "type": [
              "string",
              "null"
            ]
          }
        },
        "required": [
          "type",
          "string"
        ]
      },
      "stringRequest": {
        "type": "string",
        "maxLength": 100,
        "minLength": 1
      },
      "syncedBlockBlockObjectResponse": {
        "title": "Synced Block",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "synced_block"
          },
          "synced_block": {
            "type": "object",
            "properties": {
              "synced_from": {
                "title": "Block Id",
                "type": [
                  "object",
                  "null"
                ],
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "block_id"
                  },
                  "block_id": {
                    "$ref": "#/components/schemas/idRequest"
                  }
                },
                "required": [
                  "type",
                  "block_id"
                ]
              }
            },
            "required": [
              "synced_from"
            ]
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "synced_block",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "tabBlockObjectResponse": {
        "title": "Tab",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "tab"
          },
          "tab": {
            "$ref": "#/components/schemas/emptyObject"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "tab",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "tableBlockObjectResponse": {
        "title": "Table",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "table"
          },
          "table": {
            "$ref": "#/components/schemas/contentWithTableResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "table",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "tableOfContentsBlockObjectResponse": {
        "title": "Table Of Contents",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "table_of_contents"
          },
          "table_of_contents": {
            "type": "object",
            "properties": {
              "color": {
                "$ref": "#/components/schemas/apiColor"
              }
            },
            "required": [
              "color"
            ]
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "table_of_contents",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "tableRowBlockObjectResponse": {
        "title": "Table Row",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "table_row"
          },
          "table_row": {
            "$ref": "#/components/schemas/contentWithTableRowResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "table_row",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "templateBlockObjectResponse": {
        "title": "Template",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "template"
          },
          "template": {
            "type": "object",
            "properties": {
              "rich_text": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/richTextItemResponse"
                },
                "maxItems": 100
              }
            },
            "required": [
              "rich_text"
            ]
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "template",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "templateMentionDateTemplateMentionRequest": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "template_mention_date",
            "description": "Always `template_mention_date`"
          },
          "template_mention_date": {
            "type": "string",
            "enum": [
              "today",
              "now"
            ],
            "description": "The date of the template mention."
          }
        },
        "additionalProperties": false,
        "required": [
          "template_mention_date"
        ],
        "title": "Template Mention Date"
      },
      "templateMentionDateTemplateMentionResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "template_mention_date",
            "description": "Always `template_mention_date`"
          },
          "template_mention_date": {
            "type": "string",
            "enum": [
              "today",
              "now"
            ],
            "description": "The date of the template mention."
          }
        },
        "additionalProperties": false,
        "required": [
          "type",
          "template_mention_date"
        ],
        "title": "Template Mention Date"
      },
      "templateMentionRequest": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/templateMentionDateTemplateMentionRequest"
          },
          {
            "$ref": "#/components/schemas/templateMentionUserTemplateMentionRequest"
          }
        ]
      },
      "templateMentionResponse": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/templateMentionDateTemplateMentionResponse"
          },
          {
            "$ref": "#/components/schemas/templateMentionUserTemplateMentionResponse"
          }
        ]
      },
      "templateMentionUserTemplateMentionRequest": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "template_mention_user",
            "description": "Always `template_mention_user`"
          },
          "template_mention_user": {
            "type": "string",
            "const": "me",
            "description": "The user of the template mention."
          }
        },
        "additionalProperties": false,
        "required": [
          "template_mention_user"
        ],
        "title": "Template Mention User"
      },
      "templateMentionUserTemplateMentionResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "template_mention_user",
            "description": "Always `template_mention_user`"
          },
          "template_mention_user": {
            "type": "string",
            "const": "me",
            "description": "The user of the template mention."
          }
        },
        "additionalProperties": false,
        "required": [
          "type",
          "template_mention_user"
        ],
        "title": "Template Mention User"
      },
      "textRequest": {
        "type": "string",
        "maxLength": 2000,
        "minLength": 1
      },
      "textRichTextItemRequest": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "text",
            "description": "Always `text`"
          },
          "text": {
            "type": "object",
            "properties": {
              "content": {
                "type": "string",
                "maxLength": 2000,
                "description": "The actual text content of the text."
              },
              "link": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "url": {
                        "type": "string",
                        "examples": [
                          "https://www.notion.com"
                        ],
                        "description": "The URL of the link."
                      }
                    },
                    "required": [
                      "url"
                    ]
                  },
                  {
                    "type": "null"
                  }
                ],
                "description": "An object with information about any inline link in this text, if included."
              }
            },
            "additionalProperties": false,
            "required": [
              "content"
            ],
            "description": "If a rich text object's type value is `text`, then the corresponding text field contains an object including the text content and any inline link."
          }
        },
        "required": [
          "text"
        ],
        "title": "Text"
      },
      "textRichTextItemResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "text",
            "description": "Always `text`"
          },
          "text": {
            "type": "object",
            "properties": {
              "content": {
                "type": "string",
                "maxLength": 2000,
                "description": "The actual text content of the text."
              },
              "link": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "url": {
                        "type": "string",
                        "examples": [
                          "https://www.notion.com"
                        ],
                        "description": "The URL of the link."
                      }
                    },
                    "additionalProperties": false,
                    "required": [
                      "url"
                    ]
                  },
                  {
                    "type": "null"
                  }
                ],
                "description": "An object with information about any inline link in this text, if included."
              }
            },
            "additionalProperties": false,
            "required": [
              "content",
              "link"
            ],
            "description": "If a rich text object's type value is `text`, then the corresponding text field contains an object including the text content and any inline link."
          }
        },
        "required": [
          "type",
          "text"
        ],
        "title": "Text"
      },
      "timeZoneRequest": {
        "type": "string"
      },
      "titleDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "title",
            "description": "Always `title`"
          },
          "title": {
            "$ref": "#/components/schemas/emptyObject"
          }
        },
        "required": [
          "type",
          "title"
        ],
        "title": "Title"
      },
      "titleObjectResponse": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          }
        },
        "required": [
          "title"
        ]
      },
      "titlePropertyItemObjectResponse": {
        "title": "Title",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "title"
          },
          "title": {
            "$ref": "#/components/schemas/richTextItemResponse"
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "title",
          "object",
          "id"
        ]
      },
      "toDoBlockObjectResponse": {
        "title": "To Do",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "to_do"
          },
          "to_do": {
            "type": "object",
            "properties": {
              "rich_text": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/richTextItemResponse"
                },
                "maxItems": 100
              },
              "color": {
                "$ref": "#/components/schemas/apiColor"
              },
              "checked": {
                "type": "boolean"
              }
            },
            "required": [
              "rich_text",
              "color",
              "checked"
            ]
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "to_do",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "toggleBlockObjectResponse": {
        "title": "Toggle",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "toggle"
          },
          "toggle": {
            "$ref": "#/components/schemas/contentWithRichTextAndColorResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "toggle",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "transcriptionBlockResponse": {
        "type": "object",
        "properties": {
          "title": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/richTextItemResponse"
            },
            "maxItems": 100
          },
          "status": {
            "$ref": "#/components/schemas/apiTranscriptionStatus"
          },
          "children": {
            "$ref": "#/components/schemas/transcriptionChildrenResponse"
          },
          "calendar_event": {
            "$ref": "#/components/schemas/transcriptionCalendarEventResponse"
          },
          "recording": {
            "$ref": "#/components/schemas/transcriptionRecordingResponse"
          }
        }
      },
      "transcriptionCalendarEventResponse": {
        "type": "object",
        "properties": {
          "start_time": {
            "type": "string",
            "format": "date-time"
          },
          "end_time": {
            "type": "string",
            "format": "date-time"
          },
          "attendees": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/idRequest"
            },
            "maxItems": 100
          }
        },
        "required": [
          "start_time",
          "end_time"
        ]
      },
      "transcriptionChildrenResponse": {
        "type": "object",
        "properties": {
          "summary_block_id": {
            "$ref": "#/components/schemas/idRequest"
          },
          "notes_block_id": {
            "$ref": "#/components/schemas/idRequest"
          },
          "transcript_block_id": {
            "$ref": "#/components/schemas/idRequest"
          }
        }
      },
      "transcriptionRecordingResponse": {
        "type": "object",
        "properties": {
          "start_time": {
            "type": "string",
            "format": "date-time"
          },
          "end_time": {
            "type": "string",
            "format": "date-time"
          }
        }
      },
      "uniqueIdDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "unique_id",
            "description": "Always `unique_id`"
          },
          "unique_id": {
            "type": "object",
            "properties": {
              "prefix": {
                "oneOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ],
                "description": "The prefix for the unique ID."
              }
            },
            "additionalProperties": false,
            "required": [
              "prefix"
            ]
          }
        },
        "required": [
          "type",
          "unique_id"
        ],
        "title": "Unique Id"
      },
      "uniqueIdPropertyItemObjectResponse": {
        "title": "Unique Id",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "unique_id"
          },
          "unique_id": {
            "type": "object",
            "properties": {
              "prefix": {
                "type": [
                  "string",
                  "null"
                ]
              },
              "number": {
                "type": [
                  "number",
                  "null"
                ]
              }
            },
            "required": [
              "prefix",
              "number"
            ]
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "unique_id",
          "object",
          "id"
        ]
      },
      "unsupportedBlockObjectResponse": {
        "title": "Unsupported",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "unsupported"
          },
          "unsupported": {
            "type": "object",
            "properties": {
              "block_type": {
                "description": "The underlying block type that is not currently supported by the Public API. Example values include: form, button, drive.",
                "type": "string"
              }
            },
            "required": [
              "block_type"
            ]
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "unsupported",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "urlDatabasePropertyConfigResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "url",
            "description": "Always `url`"
          },
          "url": {
            "$ref": "#/components/schemas/emptyObject"
          }
        },
        "required": [
          "type",
          "url"
        ],
        "title": "Url"
      },
      "urlPropertyItemObjectResponse": {
        "title": "Url",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "url"
          },
          "url": {
            "type": [
              "string",
              "null"
            ]
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "url",
          "object",
          "id"
        ]
      },
      "userObjectResponse": {
        "allOf": [
          {
            "$ref": "#/components/schemas/userObjectResponseCommon"
          },
          {
            "oneOf": [
              {
                "$ref": "#/components/schemas/personUserObjectResponse"
              },
              {
                "$ref": "#/components/schemas/botUserObjectResponse"
              }
            ]
          }
        ]
      },
      "userObjectResponseCommon": {
        "type": "object",
        "properties": {
          "id": {
            "$ref": "#/components/schemas/idResponse",
            "description": "The ID of the user."
          },
          "object": {
            "type": "string",
            "const": "user",
            "description": "The user object type name."
          },
          "name": {
            "oneOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "description": "The name of the user."
          },
          "avatar_url": {
            "oneOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "description": "The avatar URL of the user."
          }
        },
        "additionalProperties": false,
        "required": [
          "id",
          "object",
          "name",
          "avatar_url"
        ]
      },
      "userValueResponse": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          {
            "$ref": "#/components/schemas/userObjectResponse"
          }
        ]
      },
      "verificationPropertyItemObjectResponse": {
        "title": "Verification",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "verification"
          },
          "verification": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/verificationPropertyValueResponse"
              },
              {
                "type": "null"
              }
            ]
          },
          "object": {
            "type": "string",
            "const": "property_item"
          },
          "id": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "verification",
          "object",
          "id"
        ]
      },
      "verificationPropertyResponse": {
        "type": "object",
        "properties": {
          "state": {
            "type": "string",
            "enum": [
              "verified",
              "expired"
            ]
          },
          "date": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/dateResponse"
              },
              {
                "type": "null"
              }
            ]
          },
          "verified_by": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/partialUserObjectResponse"
              },
              {
                "type": "null"
              }
            ]
          }
        },
        "required": [
          "state",
          "date",
          "verified_by"
        ]
      },
      "verificationPropertyUnverifiedResponse": {
        "type": "object",
        "properties": {
          "state": {
            "type": "string",
            "const": "unverified"
          },
          "date": {
            "type": "null"
          },
          "verified_by": {
            "type": "null"
          }
        },
        "required": [
          "state",
          "date",
          "verified_by"
        ]
      },
      "verificationPropertyValueResponse": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/verificationPropertyUnverifiedResponse"
          },
          {
            "$ref": "#/components/schemas/verificationPropertyResponse"
          }
        ]
      },
      "videoBlockObjectResponse": {
        "title": "Video",
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "video"
          },
          "video": {
            "$ref": "#/components/schemas/mediaContentWithFileAndCaptionResponse"
          },
          "parent": {
            "$ref": "#/components/schemas/parentForBlockBasedObjectResponse"
          },
          "object": {
            "type": "string",
            "const": "block"
          },
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "created_time": {
            "type": "string",
            "format": "date-time"
          },
          "created_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "last_edited_time": {
            "type": "string",
            "format": "date-time"
          },
          "last_edited_by": {
            "$ref": "#/components/schemas/partialUserObjectResponse"
          },
          "has_children": {
            "type": "boolean"
          },
          "in_trash": {
            "type": "boolean"
          }
        },
        "required": [
          "type",
          "video",
          "parent",
          "object",
          "id",
          "created_time",
          "created_by",
          "last_edited_time",
          "last_edited_by",
          "has_children",
          "in_trash"
        ]
      },
      "workspaceParentForBlockBasedObjectResponse": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "const": "workspace",
            "description": "The parent type."
          },
          "workspace": {
            "type": "boolean",
            "const": true,
            "description": "Always true for workspace parent."
          }
        },
        "additionalProperties": false,
        "required": [
          "type",
          "workspace"
        ]
      }
    },
    "parameters": {
      "notionVersion": {
        "name": "Notion-Version",
        "in": "header",
        "required": true,
        "schema": {
          "enum": [
            "2026-03-11"
          ]
        },
        "description": "The [API version](/reference/versioning) to use for this request. The latest version is `2026-03-11`."
      }
    }
  },
  "paths": {
    "/v1/external/decagon": {
      "post": {
        "summary": "Tools for Decagon's CX chatbot",
        "operationId": "external-decagon",
        "security": [
          {
            "basicAuth": []
          }
        ],
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "tool": {
                        "type": "string",
                        "const": "educationEmailVerification"
                      },
                      "user_id": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "tool",
                      "user_id"
                    ]
                  },
                  {
                    "type": "object",
                    "properties": {
                      "tool": {
                        "type": "string",
                        "const": "refundEligibility"
                      },
                      "space_id": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "tool",
                      "space_id"
                    ]
                  },
                  {
                    "type": "object",
                    "properties": {
                      "tool": {
                        "type": "string",
                        "const": "getFreeChartsForSpace"
                      },
                      "space_id": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "tool",
                      "space_id"
                    ]
                  },
                  {
                    "type": "object",
                    "properties": {
                      "tool": {
                        "type": "string",
                        "const": "optOutNotionAIDataSharing"
                      },
                      "user_id": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "tool",
                      "user_id"
                    ]
                  },
                  {
                    "type": "object",
                    "properties": {
                      "tool": {
                        "type": "string",
                        "const": "isWorkspaceDeleted"
                      },
                      "space_id": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "tool",
                      "space_id"
                    ]
                  }
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "anyOf": [
                    {
                      "type": "object",
                      "properties": {
                        "tool": {
                          "type": "string",
                          "const": "educationEmailVerification"
                        },
                        "is_education_email": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "tool",
                        "is_education_email"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "tool": {
                          "type": "string",
                          "const": "refundEligibility"
                        },
                        "subscription_exists": {
                          "type": "boolean",
                          "const": false
                        }
                      },
                      "required": [
                        "tool",
                        "subscription_exists"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "tool": {
                          "type": "string",
                          "const": "refundEligibility"
                        },
                        "subscription_exists": {
                          "type": "boolean",
                          "const": true
                        },
                        "is_eligible": {
                          "type": "boolean",
                          "const": true
                        },
                        "product_name": {
                          "type": "string",
                          "enum": []
                        },
                        "invoice_id": {
                          "type": "string"
                        },
                        "eligible_amount": {
                          "type": "number"
                        },
                        "eligible_currency": {
                          "type": "string"
                        },
                        "reason": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "tool",
                        "subscription_exists",
                        "is_eligible",
                        "product_name",
                        "invoice_id",
                        "eligible_amount",
                        "eligible_currency",
                        "reason"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "tool": {
                          "type": "string",
                          "const": "refundEligibility"
                        },
                        "subscription_exists": {
                          "type": "boolean",
                          "const": true
                        },
                        "is_eligible": {
                          "type": "boolean",
                          "const": false
                        },
                        "reason": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "tool",
                        "subscription_exists",
                        "is_eligible",
                        "reason"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "tool": {
                          "type": "string",
                          "const": "getFreeChartsForSpace"
                        },
                        "hasFreeChart": {
                          "type": "boolean"
                        },
                        "spaceCanViewUnlimitedCharts": {
                          "type": "boolean"
                        },
                        "freeChartIds": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          }
                        },
                        "freeChartUrls": {
                          "type": "array",
                          "items": {
                            "type": [
                              "string",
                              "null"
                            ]
                          }
                        }
                      },
                      "required": [
                        "tool",
                        "hasFreeChart",
                        "spaceCanViewUnlimitedCharts",
                        "freeChartIds",
                        "freeChartUrls"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "tool": {
                          "type": "string",
                          "const": "optOutNotionAIDataSharing"
                        },
                        "success": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "tool",
                        "success"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "tool": {
                          "type": "string",
                          "const": "isWorkspaceDeleted"
                        },
                        "isDeleted": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "tool",
                        "isDeleted"
                      ]
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_oauth_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_oauth_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_oauth_403"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_oauth_500"
                }
              }
            }
          }
        }
      }
    },
    "/v1/external/refundEligibility": {
      "get": {
        "summary": "Check if a user is eligible for a refund",
        "operationId": "external-refund-eligibility",
        "security": [
          {
            "basicAuth": []
          }
        ],
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "space_id",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "space_id": {
                    "type": "string"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "anyOf": [
                    {
                      "type": "object",
                      "properties": {
                        "subscription_exists": {
                          "type": "boolean",
                          "const": false
                        }
                      },
                      "required": [
                        "subscription_exists"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "subscription_exists": {
                          "type": "boolean",
                          "const": true
                        },
                        "is_eligible": {
                          "type": "boolean",
                          "const": true
                        },
                        "product_name": {
                          "type": "string",
                          "enum": []
                        },
                        "invoice_id": {
                          "type": "string"
                        },
                        "eligible_amount": {
                          "type": "number"
                        },
                        "eligible_currency": {
                          "type": "string"
                        },
                        "reason": {
                          "type": "string"
                        },
                        "invoice_generated_date": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "subscription_exists",
                        "is_eligible",
                        "product_name",
                        "invoice_id",
                        "eligible_amount",
                        "eligible_currency",
                        "reason",
                        "invoice_generated_date"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "subscription_exists": {
                          "type": "boolean",
                          "const": true
                        },
                        "is_eligible": {
                          "type": "boolean",
                          "const": false
                        },
                        "reason": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "subscription_exists",
                        "is_eligible",
                        "reason"
                      ]
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_oauth_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_oauth_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_oauth_403"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_oauth_500"
                }
              }
            }
          }
        }
      }
    },
    "/v1/agents/{agent_id}/chat": {
      "post": {
        "summary": "Chat with agent",
        "operationId": "chat-with-agent",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "agent_id",
            "in": "path",
            "required": true,
            "schema": {
              "oneOf": [
                {
                  "$ref": "#/components/schemas/idRequest"
                },
                {
                  "type": "string",
                  "const": "33333333-3333-3333-3333-333333333333",
                  "description": "Always `33333333-3333-3333-3333-333333333333`"
                }
              ],
              "description": "The ID of the agent to chat with. Use a UUID for custom agents, or `33333333-3333-3333-3333-333333333333` for the personal agent (Notion AI)."
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "message": {
                    "type": "string",
                    "maxLength": 10000,
                    "description": "The message to send to the agent."
                  },
                  "thread_id": {
                    "$ref": "#/components/schemas/idRequest",
                    "description": "The ID of an existing thread to continue the conversation. If not provided, a new thread will be created."
                  },
                  "attachments": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "file_upload": {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "string",
                              "description": "ID of a FileUpload object that has the status `uploaded`."
                            }
                          },
                          "required": [
                            "id"
                          ],
                          "description": "ID of a FileUpload object that has the status `uploaded`."
                        },
                        "type": {
                          "type": "string",
                          "const": "file_upload",
                          "description": "The type of the attachment. Only supports \"file_upload\"."
                        },
                        "name": {
                          "type": "string",
                          "description": "An optional display name override for the attachment."
                        }
                      },
                      "required": [
                        "file_upload"
                      ]
                    },
                    "maxItems": 100,
                    "description": "An array of file uploads to attach to this chat turn. Use the File Upload APIs to create uploads and pass their IDs here."
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "object": {
                      "type": "string",
                      "const": "chat.invocation",
                      "description": "Always `chat.invocation`"
                    },
                    "agent_id": {
                      "type": "string"
                    },
                    "thread_id": {
                      "type": "string"
                    },
                    "status": {
                      "type": "string",
                      "const": "pending",
                      "description": "Always `pending`"
                    }
                  },
                  "additionalProperties": false,
                  "required": [
                    "object",
                    "agent_id",
                    "thread_id",
                    "status"
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        },
        "x-notion-docs-ref": "https://developers.notion.com/reference/internal/chat-with-agent"
      }
    },
    "/v1/agents/{agent_id}/chatStream": {
      "post": {
        "summary": "Chat with agent (streaming)",
        "operationId": "chat-with-agent-stream",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "agent_id",
            "in": "path",
            "required": true,
            "schema": {
              "oneOf": [
                {
                  "$ref": "#/components/schemas/idRequest"
                },
                {
                  "type": "string",
                  "const": "33333333-3333-3333-3333-333333333333",
                  "description": "Always `33333333-3333-3333-3333-333333333333`"
                }
              ],
              "description": "The ID of the agent to chat with. Use a UUID for custom agents, or `33333333-3333-3333-3333-333333333333` for the personal agent (Notion AI)."
            }
          },
          {
            "name": "verbose",
            "in": "query",
            "schema": {
              "type": "boolean",
              "description": "Whether to include verbose agent output (thinking, tool calls, tool results). Defaults to true."
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "message": {
                    "type": "string",
                    "maxLength": 10000,
                    "description": "The message to send to the agent."
                  },
                  "thread_id": {
                    "$ref": "#/components/schemas/idRequest",
                    "description": "The ID of an existing thread to continue the conversation. If not provided, a new thread will be created."
                  },
                  "attachments": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "file_upload": {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "string",
                              "description": "ID of a FileUpload object that has the status `uploaded`."
                            }
                          },
                          "required": [
                            "id"
                          ],
                          "description": "ID of a FileUpload object that has the status `uploaded`."
                        },
                        "type": {
                          "type": "string",
                          "const": "file_upload",
                          "description": "The type of the attachment. Only supports \"file_upload\"."
                        },
                        "name": {
                          "type": "string",
                          "description": "An optional display name override for the attachment."
                        }
                      },
                      "required": [
                        "file_upload"
                      ]
                    },
                    "maxItems": 100,
                    "description": "An array of file uploads to attach to this chat turn. Use the File Upload APIs to create uploads and pass their IDs here."
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "oneOf": [
                    {
                      "type": "object",
                      "properties": {
                        "type": {
                          "type": "string",
                          "const": "message",
                          "description": "Always `message`"
                        },
                        "id": {
                          "$ref": "#/components/schemas/idResponse"
                        },
                        "role": {
                          "type": "string",
                          "enum": [
                            "user",
                            "agent"
                          ],
                          "description": "One of: `user`, `agent`"
                        },
                        "content": {
                          "type": "string"
                        },
                        "attachments": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "name": {
                                "type": "string"
                              },
                              "content_type": {
                                "type": "string"
                              },
                              "url": {
                                "type": "string"
                              },
                              "expiry_time": {
                                "type": "string",
                                "format": "date-time",
                                "description": "The time when the attachment URL will expire."
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "name",
                              "content_type",
                              "url"
                            ]
                          },
                          "maxItems": 100
                        },
                        "content_parts": {
                          "type": "array",
                          "items": {
                            "oneOf": [
                              {
                                "type": "object",
                                "properties": {
                                  "type": {
                                    "type": "string",
                                    "const": "text",
                                    "description": "Always `text`"
                                  },
                                  "text": {
                                    "type": "string"
                                  }
                                },
                                "additionalProperties": false,
                                "required": [
                                  "type",
                                  "text"
                                ]
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "type": {
                                    "type": "string",
                                    "const": "thinking",
                                    "description": "Always `thinking`"
                                  },
                                  "text": {
                                    "type": "string"
                                  }
                                },
                                "additionalProperties": false,
                                "required": [
                                  "type",
                                  "text"
                                ]
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "type": {
                                    "type": "string",
                                    "const": "tool_call",
                                    "description": "Always `tool_call`"
                                  },
                                  "tool_call_id": {
                                    "oneOf": [
                                      {
                                        "type": "string"
                                      },
                                      {
                                        "type": "null"
                                      }
                                    ]
                                  },
                                  "tool_name": {
                                    "type": "string"
                                  },
                                  "input": {
                                    "type": "string"
                                  },
                                  "results": {
                                    "type": "array",
                                    "items": {
                                      "type": "object",
                                      "properties": {
                                        "id": {
                                          "$ref": "#/components/schemas/idResponse"
                                        },
                                        "agent_step_id": {
                                          "oneOf": [
                                            {
                                              "$ref": "#/components/schemas/idResponse"
                                            },
                                            {
                                              "type": "null"
                                            }
                                          ]
                                        },
                                        "tool_call_id": {
                                          "oneOf": [
                                            {
                                              "type": "string"
                                            },
                                            {
                                              "type": "null"
                                            }
                                          ]
                                        },
                                        "tool_name": {
                                          "type": "string"
                                        },
                                        "tool_type": {
                                          "type": "string"
                                        },
                                        "state": {
                                          "type": "string"
                                        },
                                        "input": {
                                          "oneOf": [
                                            {},
                                            {
                                              "type": "null"
                                            }
                                          ]
                                        },
                                        "output": {
                                          "oneOf": [
                                            {},
                                            {
                                              "type": "null"
                                            }
                                          ]
                                        },
                                        "error": {
                                          "oneOf": [
                                            {
                                              "type": "string"
                                            },
                                            {
                                              "type": "null"
                                            }
                                          ]
                                        },
                                        "started_at": {
                                          "type": "integer",
                                          "minimum": 0
                                        },
                                        "finished_at": {
                                          "oneOf": [
                                            {
                                              "type": "integer",
                                              "minimum": 0
                                            },
                                            {
                                              "type": "null"
                                            }
                                          ]
                                        },
                                        "duration_ms": {
                                          "oneOf": [
                                            {
                                              "type": "integer",
                                              "minimum": 0
                                            },
                                            {
                                              "type": "null"
                                            }
                                          ]
                                        }
                                      },
                                      "additionalProperties": false,
                                      "required": [
                                        "id",
                                        "agent_step_id",
                                        "tool_call_id",
                                        "tool_name",
                                        "tool_type",
                                        "state",
                                        "input",
                                        "output",
                                        "error",
                                        "started_at",
                                        "finished_at",
                                        "duration_ms"
                                      ]
                                    },
                                    "maxItems": 100
                                  }
                                },
                                "additionalProperties": false,
                                "required": [
                                  "type",
                                  "tool_call_id",
                                  "tool_name",
                                  "input"
                                ]
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "type": {
                                    "type": "string",
                                    "const": "follow_ups",
                                    "description": "Always `follow_ups`"
                                  },
                                  "follow_ups": {
                                    "type": "array",
                                    "items": {
                                      "type": "object",
                                      "properties": {
                                        "label": {
                                          "type": "string"
                                        },
                                        "message": {
                                          "type": "string"
                                        }
                                      },
                                      "additionalProperties": false,
                                      "required": [
                                        "label",
                                        "message"
                                      ]
                                    },
                                    "maxItems": 100
                                  }
                                },
                                "additionalProperties": false,
                                "required": [
                                  "type",
                                  "follow_ups"
                                ]
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "type": {
                                    "type": "string",
                                    "const": "custom_agent_template_picker",
                                    "description": "Always `custom_agent_template_picker`"
                                  }
                                },
                                "additionalProperties": false,
                                "required": [
                                  "type"
                                ]
                              }
                            ]
                          },
                          "maxItems": 100
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "type",
                        "id",
                        "role",
                        "content"
                      ],
                      "title": "Message"
                    },
                    {
                      "type": "object",
                      "properties": {
                        "type": {
                          "type": "string",
                          "const": "started",
                          "description": "Always `started`"
                        },
                        "thread_id": {
                          "$ref": "#/components/schemas/idResponse"
                        },
                        "agent_id": {
                          "type": "string",
                          "description": "Agent identifier echoed from the request path. May be a UUID with or without dashes."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "type",
                        "thread_id",
                        "agent_id"
                      ],
                      "title": "Started"
                    },
                    {
                      "type": "object",
                      "properties": {
                        "type": {
                          "type": "string",
                          "const": "done",
                          "description": "Always `done`"
                        },
                        "thread_id": {
                          "$ref": "#/components/schemas/idResponse"
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "type",
                        "thread_id"
                      ],
                      "title": "Done"
                    },
                    {
                      "type": "object",
                      "properties": {
                        "type": {
                          "type": "string",
                          "const": "error",
                          "description": "Always `error`"
                        },
                        "code": {
                          "type": "string",
                          "enum": [
                            "invalid_json",
                            "invalid_request_url",
                            "invalid_request",
                            "missing_version",
                            "validation_error",
                            "unauthorized",
                            "restricted_resource",
                            "object_not_found",
                            "rate_limited",
                            "internal_server_error",
                            "service_unavailable",
                            "gateway_timeout",
                            "conflict_error"
                          ],
                          "description": "Programmatic error code. Matches the error codes used by non-streaming Public API endpoints."
                        },
                        "message": {
                          "type": "string"
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "type",
                        "code",
                        "message"
                      ],
                      "title": "Error"
                    }
                  ],
                  "title": "Chat stream chunk",
                  "description": "A single NDJSON chunk from the chat streaming response. Each line in the stream is one of these chunk types."
                }
              },
              "application/x-ndjson": {
                "schema": {
                  "type": "string",
                  "description": "Newline-delimited JSON (NDJSON) stream. Each line is a JSON-encoded chunk object."
                }
              }
            }
          }
        },
        "x-notion-docs-ref": "https://developers.notion.com/reference/internal/chat-with-agent-stream"
      }
    },
    "/v1/boxy/boxes": {
      "post": {
        "summary": "Create box",
        "operationId": "create-box",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string",
                    "examples": [
                      "box_123"
                    ],
                    "description": "The ID of the box."
                  },
                  "ownerEmail": {
                    "type": "string",
                    "examples": [
                      "alice@makenotion.com"
                    ],
                    "description": "The owner email of the box."
                  }
                },
                "required": [
                  "id",
                  "ownerEmail"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "examples": [
                        "box_123"
                      ],
                      "description": "The ID of the created box."
                    }
                  },
                  "additionalProperties": false,
                  "required": [
                    "id"
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/boxy/boxes/{id}/threads": {
      "post": {
        "summary": "Create box thread",
        "operationId": "create-box-thread",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "examples": [
                "box_123"
              ],
              "description": "The ID of the box."
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "agent": {
                    "type": "string",
                    "examples": [
                      "codex"
                    ],
                    "description": "The agent identifier."
                  },
                  "cwd": {
                    "type": "string",
                    "examples": [
                      "/data/notion-next"
                    ],
                    "description": "The working directory for the thread session."
                  },
                  "model": {
                    "type": "string",
                    "examples": [
                      "auto"
                    ],
                    "description": "The model selector for the thread."
                  },
                  "instruction": {
                    "type": "string",
                    "examples": [
                      "Do the thing"
                    ],
                    "description": "The initial instruction for the thread."
                  }
                },
                "required": [
                  "agent",
                  "cwd",
                  "model",
                  "instruction"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "threadId": {
                      "type": "string",
                      "examples": [
                        "th_123"
                      ],
                      "description": "The ID of the created thread."
                    },
                    "boxId": {
                      "type": "string",
                      "examples": [
                        "box_123"
                      ],
                      "description": "The ID of the box that contains the thread."
                    }
                  },
                  "additionalProperties": false,
                  "required": [
                    "threadId",
                    "boxId"
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/teamspaces": {
      "post": {
        "summary": "Create teamspace",
        "operationId": "create-teamspace",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string",
                    "examples": [
                      "Engineering Team"
                    ],
                    "description": "The name of the teamspace to create."
                  },
                  "visibility": {
                    "type": "string",
                    "enum": [
                      "default",
                      "open",
                      "closed",
                      "private"
                    ],
                    "description": "The teamspace's visibility in the workspace. Options include: default, open, closed, private."
                  },
                  "description": {
                    "type": "string",
                    "examples": [
                      "Team for engineering projects"
                    ],
                    "description": "The description for the teamspace."
                  },
                  "icon": {
                    "$ref": "#/components/schemas/pageIconRequest",
                    "description": "The icon for the teamspace."
                  },
                  "settings": {
                    "type": "object",
                    "properties": {
                      "allow_members_to_invite_members": {
                        "type": "boolean",
                        "description": "When true, members can invite other members. When false, only teamspace owners can. Corresponds to the 'Who can invite or remove teamspace members` setting."
                      },
                      "allow_members_to_change_sidebar": {
                        "type": "boolean",
                        "description": "When true, members can edit the sidebar. When false, only teamspace owners can. Corresponds to the `Who can edit teamspace sidebar` setting."
                      },
                      "disable_invite_link": {
                        "type": "boolean",
                        "description": "When true, invite links are disabled. Corresponds to the `Invite Link` toggle."
                      },
                      "disable_public_pages": {
                        "type": "boolean",
                        "description": "When true, public pages are disabled. Corresponds to the `Disable publishing sites, forms, and public links` toggle."
                      },
                      "disable_guests": {
                        "type": "boolean",
                        "description": "When true, guests are disabled and removed from the teamspace. Corresponds to the `Disable guests` toggle."
                      },
                      "disable_restricted_members": {
                        "type": "boolean",
                        "description": "When true, restricted members are disabled and removed from the teamspace. Corresponds to the `Disable restricted members` toggle."
                      },
                      "disable_export": {
                        "type": "boolean",
                        "description": "When true, exporting pages is disabled. Corresponds to the `Disable export` toggle."
                      }
                    },
                    "description": "The settings of the teamspace."
                  }
                },
                "required": [
                  "name",
                  "visibility"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "object": {
                      "type": "string",
                      "const": "teamspace",
                      "description": "The team object type name."
                    },
                    "id": {
                      "$ref": "#/components/schemas/idResponse",
                      "description": "The ID of the teamspace."
                    },
                    "name": {
                      "type": "string",
                      "description": "The name of the teamspace."
                    },
                    "description": {
                      "oneOf": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "null"
                        }
                      ],
                      "description": "The description of the teamspace."
                    },
                    "icon": {
                      "oneOf": [
                        {
                          "$ref": "#/components/schemas/pageIconResponse"
                        },
                        {
                          "type": "null"
                        }
                      ],
                      "description": "The icon of the teamspace."
                    },
                    "in_trash": {
                      "type": "boolean",
                      "description": "Whether the teamspace is in the trash."
                    },
                    "visibility": {
                      "type": "string",
                      "enum": [
                        "default",
                        "open",
                        "closed",
                        "private"
                      ],
                      "description": "The teamspace's visibility in the workspace."
                    },
                    "settings": {
                      "oneOf": [
                        {
                          "type": "object",
                          "properties": {
                            "allow_members_to_invite_members": {
                              "type": "boolean",
                              "description": "Whether members can invite other members."
                            },
                            "allow_members_to_change_sidebar": {
                              "type": "boolean",
                              "description": "Whether members can change the sidebar."
                            },
                            "disable_invite_link": {
                              "type": "boolean",
                              "description": "Whether invite links are allowed."
                            },
                            "disable_public_pages": {
                              "type": "boolean",
                              "description": "Whether public pages are allowed."
                            },
                            "disable_guests": {
                              "type": "boolean",
                              "description": "Whether guests are allowed."
                            },
                            "disable_restricted_members": {
                              "type": "boolean",
                              "description": "Whether restricted members are allowed."
                            },
                            "disable_export": {
                              "type": "boolean",
                              "description": "Whether export is allowed."
                            }
                          },
                          "additionalProperties": false,
                          "required": [
                            "allow_members_to_invite_members",
                            "allow_members_to_change_sidebar",
                            "disable_invite_link",
                            "disable_public_pages",
                            "disable_guests",
                            "disable_restricted_members",
                            "disable_export"
                          ]
                        },
                        {
                          "type": "null"
                        }
                      ],
                      "description": "The teamspace's settings."
                    }
                  },
                  "additionalProperties": false,
                  "required": [
                    "object",
                    "id",
                    "name",
                    "description",
                    "icon",
                    "in_trash",
                    "visibility",
                    "settings"
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      },
      "get": {
        "summary": "List teamspaces",
        "operationId": "list-teamspaces",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "start_cursor",
            "in": "query",
            "schema": {
              "type": "string",
              "description": "If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results."
            }
          },
          {
            "name": "page_size",
            "in": "query",
            "schema": {
              "type": "integer",
              "description": "Number of teamspaces desired in the response."
            }
          },
          {
            "name": "user_id",
            "in": "query",
            "schema": {
              "$ref": "#/components/schemas/idRequest",
              "description": "If provided, returns the teamspaces that the given user can access."
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "object": {
                      "type": "string",
                      "const": "list",
                      "description": "Always `list`"
                    },
                    "next_cursor": {
                      "oneOf": [
                        {
                          "$ref": "#/components/schemas/idResponse"
                        },
                        {
                          "type": "null"
                        }
                      ]
                    },
                    "has_more": {
                      "type": "boolean"
                    },
                    "results": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "object": {
                            "type": "string",
                            "const": "teamspace",
                            "description": "The teamspace object type name."
                          },
                          "id": {
                            "$ref": "#/components/schemas/idResponse",
                            "description": "The ID of the teamspace."
                          },
                          "teamspace_name": {
                            "type": "string",
                            "description": "The name of the teamspace."
                          }
                        },
                        "additionalProperties": false,
                        "required": [
                          "object",
                          "id",
                          "teamspace_name"
                        ]
                      }
                    },
                    "type": {
                      "type": "string",
                      "const": "teamspace",
                      "description": "Always `teamspace`"
                    },
                    "teamspace": {
                      "$ref": "#/components/schemas/emptyObject"
                    }
                  },
                  "required": [
                    "object",
                    "next_cursor",
                    "has_more",
                    "results",
                    "type",
                    "teamspace"
                  ],
                  "additionalProperties": false
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/comments/{comment_id}": {
      "delete": {
        "summary": "Delete a comment",
        "operationId": "delete-a-comment",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "comment_id",
            "in": "path",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/idRequest",
              "description": "The ID of the comment to delete."
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "oneOf": [
                    {
                      "$ref": "#/components/schemas/partialCommentObjectResponse"
                    },
                    {
                      "$ref": "#/components/schemas/commentObjectResponse"
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      },
      "patch": {
        "summary": "Update a comment",
        "operationId": "update-a-comment",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "comment_id",
            "in": "path",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/idRequest",
              "description": "The ID of the comment to update."
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "rich_text": {
                    "type": "array",
                    "items": {
                      "$ref": "#/components/schemas/richTextItemRequest"
                    },
                    "maxItems": 100,
                    "description": "An array of rich text objects that represent the updated content of the comment."
                  }
                },
                "required": [
                  "rich_text"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "oneOf": [
                    {
                      "$ref": "#/components/schemas/partialCommentObjectResponse"
                    },
                    {
                      "$ref": "#/components/schemas/commentObjectResponse"
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/export/{id}": {
      "get": {
        "summary": "Export a page",
        "operationId": "export-page",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/idRequest",
              "description": "The ID of the page or block to export."
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "object": {
                      "type": "string",
                      "const": "export",
                      "description": "The type of object, always 'export'."
                    },
                    "id": {
                      "$ref": "#/components/schemas/idResponse",
                      "description": "The ID of the exported page or block."
                    },
                    "pdf_export_url": {
                      "type": "string",
                      "description": "URL to download the page export (PDF)."
                    },
                    "metadata_export_url": {
                      "type": "string",
                      "description": "URL to download the metadata export (JSON)."
                    },
                    "comments_export_url": {
                      "type": "string",
                      "description": "URL to download the comments export (JSON)."
                    },
                    "attachments_export_url": {
                      "type": "string",
                      "description": "URL to download the attachments export (JSON)."
                    },
                    "permissions_export_url": {
                      "type": "string",
                      "description": "URL to download the permissions export (JSON)."
                    }
                  },
                  "additionalProperties": false,
                  "required": [
                    "object",
                    "id",
                    "pdf_export_url",
                    "metadata_export_url",
                    "comments_export_url",
                    "attachments_export_url",
                    "permissions_export_url"
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/boxy/boxes/{id}": {
      "get": {
        "summary": "Get box",
        "operationId": "get-box",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "examples": [
                "box_123"
              ],
              "description": "The ID of the box."
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "boxName": {
                      "type": "string",
                      "examples": [
                        "box-mock"
                      ],
                      "description": "The human-readable name of the box."
                    },
                    "status": {
                      "type": "string",
                      "enum": [
                        "provisioning",
                        "ready",
                        "failed",
                        "deleting",
                        "deleted"
                      ],
                      "description": "The current lifecycle status of the box."
                    },
                    "operationId": {
                      "type": "string",
                      "examples": [
                        "op_123"
                      ],
                      "description": "The latest operation ID for this box."
                    }
                  },
                  "additionalProperties": false,
                  "required": [
                    "boxName",
                    "status",
                    "operationId"
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/teamspaces/{team_id}": {
      "get": {
        "summary": "Get teamspace",
        "operationId": "get-teamspace",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "team_id",
            "in": "path",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/idRequest",
              "description": "The ID of the teamspace to retrieve."
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "object": {
                      "type": "string",
                      "const": "teamspace",
                      "description": "The team object type name."
                    },
                    "id": {
                      "$ref": "#/components/schemas/idResponse",
                      "description": "The ID of the teamspace."
                    },
                    "name": {
                      "type": "string",
                      "description": "The name of the teamspace."
                    },
                    "description": {
                      "oneOf": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "null"
                        }
                      ],
                      "description": "The description of the teamspace."
                    },
                    "icon": {
                      "oneOf": [
                        {
                          "$ref": "#/components/schemas/pageIconResponse"
                        },
                        {
                          "type": "null"
                        }
                      ],
                      "description": "The icon of the teamspace."
                    },
                    "in_trash": {
                      "type": "boolean",
                      "description": "Whether the teamspace is in the trash."
                    },
                    "visibility": {
                      "type": "string",
                      "enum": [
                        "default",
                        "open",
                        "closed",
                        "private"
                      ],
                      "description": "The teamspace's visibility in the workspace."
                    },
                    "settings": {
                      "oneOf": [
                        {
                          "type": "object",
                          "properties": {
                            "allow_members_to_invite_members": {
                              "type": "boolean",
                              "description": "Whether members can invite other members."
                            },
                            "allow_members_to_change_sidebar": {
                              "type": "boolean",
                              "description": "Whether members can change the sidebar."
                            },
                            "disable_invite_link": {
                              "type": "boolean",
                              "description": "Whether invite links are allowed."
                            },
                            "disable_public_pages": {
                              "type": "boolean",
                              "description": "Whether public pages are allowed."
                            },
                            "disable_guests": {
                              "type": "boolean",
                              "description": "Whether guests are allowed."
                            },
                            "disable_restricted_members": {
                              "type": "boolean",
                              "description": "Whether restricted members are allowed."
                            },
                            "disable_export": {
                              "type": "boolean",
                              "description": "Whether export is allowed."
                            }
                          },
                          "additionalProperties": false,
                          "required": [
                            "allow_members_to_invite_members",
                            "allow_members_to_change_sidebar",
                            "disable_invite_link",
                            "disable_public_pages",
                            "disable_guests",
                            "disable_restricted_members",
                            "disable_export"
                          ]
                        },
                        {
                          "type": "null"
                        }
                      ],
                      "description": "The teamspace's settings."
                    }
                  },
                  "additionalProperties": false,
                  "required": [
                    "object",
                    "id",
                    "name",
                    "description",
                    "icon",
                    "in_trash",
                    "visibility",
                    "settings"
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      },
      "patch": {
        "summary": "Update teamspace",
        "operationId": "update-teamspace",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "team_id",
            "in": "path",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/idRequest",
              "description": "The ID of the teamspace to update."
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string",
                    "examples": [
                      "Engineering Team"
                    ],
                    "description": "The name of the teamspace."
                  },
                  "visibility": {
                    "type": "string",
                    "enum": [
                      "default",
                      "open",
                      "closed",
                      "private"
                    ],
                    "description": "The teamspace's visibility in the workspace. Options include: default, open, closed, private."
                  },
                  "description": {
                    "type": "string",
                    "examples": [
                      "Team for engineering projects"
                    ],
                    "description": "The description for the teamspace."
                  },
                  "icon": {
                    "$ref": "#/components/schemas/pageIconRequest",
                    "description": "The icon for the teamspace."
                  },
                  "settings": {
                    "type": "object",
                    "properties": {
                      "allow_members_to_invite_members": {
                        "type": "boolean",
                        "description": "When true, members can invite other members. When false, only teamspace owners can. Corresponds to the 'Who can invite or remove teamspace members` setting."
                      },
                      "allow_members_to_change_sidebar": {
                        "type": "boolean",
                        "description": "When true, members can edit the sidebar. When false, only teamspace owners can. Corresponds to the `Who can edit teamspace sidebar` setting."
                      },
                      "disable_invite_link": {
                        "type": "boolean",
                        "description": "When true, invite links are disabled. Corresponds to the `Invite Link` toggle."
                      },
                      "disable_public_pages": {
                        "type": "boolean",
                        "description": "When true, public pages are disabled. Corresponds to the `Disable publishing sites, forms, and public links` toggle."
                      },
                      "disable_guests": {
                        "type": "boolean",
                        "description": "When true, guests are disabled and removed from the teamspace. Corresponds to the `Disable guests` toggle."
                      },
                      "disable_restricted_members": {
                        "type": "boolean",
                        "description": "When true, restricted members are disabled and removed from the teamspace. Corresponds to the `Disable restricted members` toggle."
                      },
                      "disable_export": {
                        "type": "boolean",
                        "description": "When true, exporting pages is disabled. Corresponds to the `Disable export` toggle."
                      }
                    },
                    "description": "The settings of the teamspace."
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "object": {
                      "type": "string",
                      "const": "teamspace",
                      "description": "The team object type name."
                    },
                    "id": {
                      "$ref": "#/components/schemas/idResponse",
                      "description": "The ID of the teamspace."
                    },
                    "name": {
                      "type": "string",
                      "description": "The name of the teamspace."
                    },
                    "description": {
                      "oneOf": [
                        {
                          "type": "string"
                        },
                        {
                          "type": "null"
                        }
                      ],
                      "description": "The description of the teamspace."
                    },
                    "icon": {
                      "oneOf": [
                        {
                          "$ref": "#/components/schemas/pageIconResponse"
                        },
                        {
                          "type": "null"
                        }
                      ],
                      "description": "The icon of the teamspace."
                    },
                    "in_trash": {
                      "type": "boolean",
                      "description": "Whether the teamspace is in the trash."
                    },
                    "visibility": {
                      "type": "string",
                      "enum": [
                        "default",
                        "open",
                        "closed",
                        "private"
                      ],
                      "description": "The teamspace's visibility in the workspace."
                    },
                    "settings": {
                      "oneOf": [
                        {
                          "type": "object",
                          "properties": {
                            "allow_members_to_invite_members": {
                              "type": "boolean",
                              "description": "Whether members can invite other members."
                            },
                            "allow_members_to_change_sidebar": {
                              "type": "boolean",
                              "description": "Whether members can change the sidebar."
                            },
                            "disable_invite_link": {
                              "type": "boolean",
                              "description": "Whether invite links are allowed."
                            },
                            "disable_public_pages": {
                              "type": "boolean",
                              "description": "Whether public pages are allowed."
                            },
                            "disable_guests": {
                              "type": "boolean",
                              "description": "Whether guests are allowed."
                            },
                            "disable_restricted_members": {
                              "type": "boolean",
                              "description": "Whether restricted members are allowed."
                            },
                            "disable_export": {
                              "type": "boolean",
                              "description": "Whether export is allowed."
                            }
                          },
                          "additionalProperties": false,
                          "required": [
                            "allow_members_to_invite_members",
                            "allow_members_to_change_sidebar",
                            "disable_invite_link",
                            "disable_public_pages",
                            "disable_guests",
                            "disable_restricted_members",
                            "disable_export"
                          ]
                        },
                        {
                          "type": "null"
                        }
                      ],
                      "description": "The teamspace's settings."
                    }
                  },
                  "additionalProperties": false,
                  "required": [
                    "object",
                    "id",
                    "name",
                    "description",
                    "icon",
                    "in_trash",
                    "visibility",
                    "settings"
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/export": {
      "post": {
        "summary": "Export a page",
        "operationId": "initiate-page-export",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "blockId": {
                    "$ref": "#/components/schemas/idRequest",
                    "description": "The ID of the page or block to export."
                  }
                },
                "required": [
                  "blockId"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "object": {
                      "type": "string",
                      "const": "export",
                      "description": "The type of object, always 'export'."
                    },
                    "id": {
                      "$ref": "#/components/schemas/idResponse",
                      "description": "The ID of the exported page or block."
                    },
                    "pdf_export_url": {
                      "type": "string",
                      "description": "URL to download the page export (PDF)."
                    },
                    "metadata_export_url": {
                      "type": "string",
                      "description": "URL to download the metadata export (JSON)."
                    },
                    "comments_export_url": {
                      "type": "string",
                      "description": "URL to download the comments export (JSON)."
                    },
                    "attachments_export_url": {
                      "type": "string",
                      "description": "URL to download the attachments export (JSON)."
                    },
                    "permissions_export_url": {
                      "type": "string",
                      "description": "URL to download the permissions export (JSON)."
                    }
                  },
                  "additionalProperties": false,
                  "required": [
                    "object",
                    "id",
                    "pdf_export_url",
                    "metadata_export_url",
                    "comments_export_url",
                    "attachments_export_url",
                    "permissions_export_url"
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/agents": {
      "get": {
        "summary": "List agents",
        "operationId": "list-agents",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "name",
            "in": "query",
            "schema": {
              "type": "string",
              "description": "Filter agents by name (case-insensitive substring match)."
            }
          },
          {
            "name": "start_cursor",
            "in": "query",
            "schema": {
              "type": "string",
              "description": "If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results."
            }
          },
          {
            "name": "page_size",
            "in": "query",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100,
              "description": "The number of items from the full list desired in the response. Maximum: 100"
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "object": {
                      "type": "string",
                      "const": "list",
                      "description": "Always `list`"
                    },
                    "type": {
                      "type": "string",
                      "const": "agent",
                      "description": "Always `agent`"
                    },
                    "results": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "object": {
                            "type": "string",
                            "const": "agent",
                            "description": "Always `agent`"
                          },
                          "id": {
                            "$ref": "#/components/schemas/idResponse"
                          },
                          "name": {
                            "type": "string"
                          },
                          "description": {
                            "oneOf": [
                              {
                                "type": "string"
                              },
                              {
                                "type": "null"
                              }
                            ]
                          },
                          "instruction": {
                            "oneOf": [
                              {
                                "type": "string"
                              },
                              {
                                "type": "null"
                              }
                            ]
                          },
                          "instructions_page_id": {
                            "oneOf": [
                              {
                                "$ref": "#/components/schemas/idResponse"
                              },
                              {
                                "type": "null"
                              }
                            ]
                          },
                          "icon": {
                            "oneOf": [
                              {
                                "$ref": "#/components/schemas/pageIconResponse"
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "type": {
                                    "type": "string",
                                    "const": "custom_agent_avatar",
                                    "description": "Type of icon. In this case, a custom agent avatar."
                                  },
                                  "custom_agent_avatar": {
                                    "type": "object",
                                    "properties": {
                                      "static_url": {
                                        "type": "string",
                                        "description": "The URL of the static custom agent avatar."
                                      },
                                      "animated_url": {
                                        "type": "string",
                                        "description": "The URL of the animated custom agent avatar."
                                      }
                                    },
                                    "additionalProperties": false,
                                    "required": [
                                      "static_url",
                                      "animated_url"
                                    ],
                                    "description": "The static and animated URLs for the agent avatar."
                                  }
                                },
                                "additionalProperties": false,
                                "required": [
                                  "type",
                                  "custom_agent_avatar"
                                ]
                              },
                              {
                                "type": "null"
                              }
                            ]
                          },
                          "version": {
                            "oneOf": [
                              {
                                "type": "object",
                                "properties": {
                                  "id": {
                                    "$ref": "#/components/schemas/idResponse",
                                    "description": "The ID of the published artifact."
                                  },
                                  "number": {
                                    "type": "number",
                                    "description": "The version number."
                                  },
                                  "published_at": {
                                    "type": "string",
                                    "description": "The ISO 8601 timestamp when this version was published."
                                  }
                                },
                                "additionalProperties": false,
                                "required": [
                                  "id",
                                  "number",
                                  "published_at"
                                ]
                              },
                              {
                                "type": "null"
                              }
                            ]
                          },
                          "created_time": {
                            "type": "string",
                            "format": "date-time",
                            "description": "Date and time when this agent was created."
                          },
                          "last_edited_time": {
                            "type": "string",
                            "format": "date-time",
                            "description": "Date and time when this agent was last edited."
                          }
                        },
                        "additionalProperties": false,
                        "required": [
                          "object",
                          "id",
                          "name",
                          "description",
                          "instruction",
                          "instructions_page_id",
                          "icon",
                          "version"
                        ]
                      },
                      "maxItems": 100
                    },
                    "has_more": {
                      "type": "boolean"
                    },
                    "next_cursor": {
                      "oneOf": [
                        {
                          "title": "Cursor",
                          "type": "string"
                        },
                        {
                          "type": "null"
                        }
                      ]
                    }
                  },
                  "additionalProperties": false,
                  "required": [
                    "object",
                    "type",
                    "results",
                    "has_more",
                    "next_cursor"
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        },
        "x-notion-docs-ref": "https://developers.notion.com/reference/internal/list-agents"
      }
    },
    "/v1/boxy/boxes/{id}/threads/{threadId}/messages": {
      "get": {
        "summary": "List box thread messages",
        "operationId": "list-box-thread-messages",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "examples": [
                "box_123"
              ],
              "description": "The ID of the box."
            }
          },
          {
            "name": "threadId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "examples": [
                "th_123"
              ],
              "description": "The ID of the thread within the box."
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "title": "Boxy thread messages",
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "examples": [
                          "assistant",
                          "user"
                        ],
                        "description": "The type of message."
                      },
                      "message": {
                        "type": "string",
                        "examples": [
                          "Mocked response"
                        ],
                        "description": "The message content."
                      },
                      "time": {
                        "type": "string",
                        "format": "date-time",
                        "description": "The timestamp of the message."
                      }
                    },
                    "additionalProperties": false,
                    "required": [
                      "type",
                      "message",
                      "time"
                    ]
                  },
                  "maxItems": 100
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      },
      "post": {
        "summary": "Send message to thread",
        "operationId": "send-message-to-thread",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "examples": [
                "box_123"
              ],
              "description": "The ID of the box."
            }
          },
          {
            "name": "threadId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "examples": [
                "th_123"
              ],
              "description": "The ID of the thread."
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "message": {
                    "type": "string",
                    "examples": [
                      "Please continue"
                    ],
                    "description": "Message to send to the thread."
                  }
                },
                "required": [
                  "message"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "threadId": {
                      "type": "string",
                      "examples": [
                        "th_123"
                      ],
                      "description": "The ID of the created thread."
                    }
                  },
                  "additionalProperties": false,
                  "required": [
                    "threadId"
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/data_sources": {
      "get": {
        "summary": "List data sources",
        "operationId": "get-databases",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "start_cursor",
            "in": "query",
            "schema": {
              "type": "string",
              "description": "If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results."
            }
          },
          {
            "name": "page_size",
            "in": "query",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100,
              "description": "The number of items from the full list desired in the response. Maximum: 100"
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "object": {
                      "type": "string",
                      "const": "list",
                      "description": "Always `list`"
                    },
                    "next_cursor": {
                      "oneOf": [
                        {
                          "$ref": "#/components/schemas/idResponse"
                        },
                        {
                          "type": "null"
                        }
                      ]
                    },
                    "has_more": {
                      "type": "boolean"
                    },
                    "results": {
                      "type": "array",
                      "items": {
                        "oneOf": [
                          {
                            "$ref": "#/components/schemas/partialDataSourceObjectResponse"
                          },
                          {
                            "$ref": "#/components/schemas/dataSourceObjectResponse"
                          }
                        ]
                      }
                    },
                    "type": {
                      "type": "string",
                      "const": "data_source",
                      "description": "Always `data_source`"
                    },
                    "data_source": {
                      "$ref": "#/components/schemas/emptyObject"
                    }
                  },
                  "required": [
                    "object",
                    "next_cursor",
                    "has_more",
                    "results",
                    "type",
                    "data_source"
                  ],
                  "additionalProperties": false
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/teamspaces/{team_id}/membership": {
      "get": {
        "summary": "Lists team membership (users/groups that are owners/members) of a team.",
        "operationId": "listTeamMembership",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "team_id",
            "in": "path",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/idRequest",
              "description": "The ID of the teamspace to retrieve membership for."
            }
          },
          {
            "name": "page_size",
            "in": "query",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100,
              "description": "Number of Team Membership desired in the response. Maximum: 100"
            }
          },
          {
            "name": "start_cursor",
            "in": "query",
            "schema": {
              "type": "string",
              "description": "If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results."
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "object": {
                      "type": "string",
                      "const": "list",
                      "description": "Indicates this is a list response."
                    },
                    "type": {
                      "type": "string",
                      "const": "teamspace_member",
                      "description": "The object type contained in the results array."
                    },
                    "results": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "object": {
                            "type": "string",
                            "const": "teamspace_member",
                            "description": "The teamspace member object type name."
                          },
                          "id": {
                            "$ref": "#/components/schemas/idResponse",
                            "description": "The ID of the user or group on the teamspace."
                          },
                          "type": {
                            "type": "string",
                            "enum": [
                              "person",
                              "group"
                            ],
                            "description": "Type of the member: person or group."
                          },
                          "membership": {
                            "type": "string",
                            "enum": [
                              "owner",
                              "member"
                            ],
                            "description": "Role of the member within the teamspace."
                          }
                        },
                        "additionalProperties": false,
                        "required": [
                          "object",
                          "id",
                          "type",
                          "membership"
                        ]
                      },
                      "maxItems": 100,
                      "description": "Array of teamspace membership entries."
                    },
                    "id": {
                      "$ref": "#/components/schemas/idResponse",
                      "description": "The ID of the teamspace whose membership is listed."
                    },
                    "next_cursor": {
                      "oneOf": [
                        {
                          "$ref": "#/components/schemas/idResponse"
                        },
                        {
                          "type": "null"
                        }
                      ],
                      "description": "Cursor for the next page of results, or null if there are no more results."
                    },
                    "has_more": {
                      "type": "boolean",
                      "description": "Whether there are more results after this page."
                    }
                  },
                  "additionalProperties": false,
                  "required": [
                    "object",
                    "type",
                    "results",
                    "id",
                    "next_cursor",
                    "has_more"
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      },
      "patch": {
        "summary": "Updates team membership for a given team.",
        "operationId": "update-team-membership",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "team_id",
            "in": "path",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/idRequest",
              "description": "The ID of the teamspace to update membership for."
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "operations": {
                    "type": "array",
                    "items": {
                      "allOf": [
                        {
                          "type": "object",
                          "properties": {
                            "entity_id": {
                              "$ref": "#/components/schemas/idRequest",
                              "description": "The ID of the entity (person or group)."
                            },
                            "entity_type": {
                              "type": "string",
                              "enum": [
                                "person",
                                "group"
                              ],
                              "description": "The type of entity being added/updated/removed."
                            }
                          },
                          "required": [
                            "entity_id",
                            "entity_type"
                          ]
                        },
                        {
                          "oneOf": [
                            {
                              "type": "object",
                              "properties": {
                                "op": {
                                  "type": "string",
                                  "const": "add",
                                  "description": "Always `add`"
                                },
                                "membership": {
                                  "type": "string",
                                  "enum": [
                                    "owner",
                                    "member"
                                  ],
                                  "description": "Whether to add the entity as a teamspace owner or member."
                                }
                              },
                              "required": [
                                "op",
                                "membership"
                              ],
                              "title": "Add"
                            },
                            {
                              "type": "object",
                              "properties": {
                                "op": {
                                  "type": "string",
                                  "const": "replace",
                                  "description": "Always `replace`"
                                },
                                "membership": {
                                  "type": "string",
                                  "enum": [
                                    "owner",
                                    "member"
                                  ],
                                  "description": "Whether the entity should be an owner or member."
                                }
                              },
                              "required": [
                                "op",
                                "membership"
                              ],
                              "title": "Replace"
                            },
                            {
                              "type": "object",
                              "properties": {
                                "op": {
                                  "type": "string",
                                  "const": "remove",
                                  "description": "Always `remove`"
                                }
                              },
                              "required": [
                                "op"
                              ],
                              "title": "Remove"
                            }
                          ]
                        }
                      ]
                    },
                    "maxItems": 100,
                    "description": "Array of operations to perform on team's membership."
                  }
                },
                "required": [
                  "operations"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/emptyObject"
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/teamspaces/{team_id}/permissions": {
      "get": {
        "summary": "List permission roles for various entities in a teamspace.",
        "operationId": "listTeamPermissions",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "team_id",
            "in": "path",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/idRequest",
              "description": "The ID of the teamspace to retrieve permissions for"
            }
          },
          {
            "name": "page_size",
            "in": "query",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100,
              "description": "Number of Team Permissions desired in the response. Maximum: 100"
            }
          },
          {
            "name": "start_cursor",
            "in": "query",
            "schema": {
              "type": "string",
              "description": "If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results."
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "object": {
                      "type": "string",
                      "const": "list",
                      "description": "Indicates this is a list response."
                    },
                    "type": {
                      "type": "string",
                      "const": "teamspace_permission",
                      "description": "The object type contained in the results array."
                    },
                    "results": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "object": {
                            "type": "string",
                            "const": "teamspace_permission",
                            "description": "Indicates this is a teamspace permission response."
                          },
                          "id": {
                            "$ref": "#/components/schemas/idResponse",
                            "description": "The ID of corresponding permission type. E.g. space, team (for members and owners), group, or person id."
                          },
                          "type": {
                            "type": "string",
                            "enum": [
                              "space",
                              "owners",
                              "members",
                              "group",
                              "person"
                            ],
                            "description": "Type of permission: space, team owners, team members, custom group role, or custom person role."
                          },
                          "role": {
                            "type": "string",
                            "enum": [
                              "can_read",
                              "can_comment",
                              "can_edit",
                              "full_access"
                            ],
                            "description": "Permission role within the teamspace."
                          }
                        },
                        "additionalProperties": false,
                        "required": [
                          "object",
                          "id",
                          "type",
                          "role"
                        ]
                      },
                      "maxItems": 100,
                      "description": "Array of teamspace permission entries."
                    },
                    "id": {
                      "$ref": "#/components/schemas/idResponse",
                      "description": "The ID of the teamspace whose permissions are listed."
                    },
                    "next_cursor": {
                      "oneOf": [
                        {
                          "$ref": "#/components/schemas/idResponse"
                        },
                        {
                          "type": "null"
                        }
                      ],
                      "description": "Cursor for the next page of results, or null if there are no more results."
                    },
                    "has_more": {
                      "type": "boolean",
                      "description": "Whether there are more results after this page."
                    }
                  },
                  "additionalProperties": false,
                  "required": [
                    "object",
                    "type",
                    "results",
                    "id",
                    "next_cursor",
                    "has_more"
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      },
      "patch": {
        "summary": "Updates permission levels for a given teamspace.",
        "operationId": "update-teamspace-permissions",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "team_id",
            "in": "path",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/idRequest",
              "description": "The ID of the teamspace to update permissions for."
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "operations": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "id": {
                          "$ref": "#/components/schemas/idRequest",
                          "description": "The ID of the entity (space, team, group, or person)."
                        },
                        "type": {
                          "type": "string",
                          "enum": [
                            "space",
                            "owners",
                            "members",
                            "group",
                            "person"
                          ],
                          "description": "The type of entity being assigned permissions."
                        },
                        "role": {
                          "type": "string",
                          "enum": [
                            "none",
                            "can_read",
                            "can_comment",
                            "can_edit",
                            "full_access"
                          ],
                          "description": "The permission role for the entity in the teamspace."
                        }
                      },
                      "required": [
                        "id",
                        "type",
                        "role"
                      ]
                    },
                    "maxItems": 100,
                    "description": "Array of operations to perform on team's permissions."
                  }
                },
                "required": [
                  "operations"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/emptyObject"
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/threads/{thread_id}/messages": {
      "get": {
        "summary": "List thread messages",
        "operationId": "list-thread-messages",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "thread_id",
            "in": "path",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/idRequest",
              "description": "The ID of the thread."
            }
          },
          {
            "name": "verbose",
            "in": "query",
            "schema": {
              "type": "boolean",
              "description": "Whether to include verbose agent output (thinking, tool calls, tool results). Defaults to true."
            }
          },
          {
            "name": "role",
            "in": "query",
            "schema": {
              "type": "string",
              "enum": [
                "user",
                "agent"
              ],
              "description": "Filter messages by role (user or agent)."
            }
          },
          {
            "name": "start_cursor",
            "in": "query",
            "schema": {
              "type": "string",
              "description": "If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results."
            }
          },
          {
            "name": "page_size",
            "in": "query",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100,
              "description": "The number of items from the full list desired in the response. Maximum: 100"
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "object": {
                      "type": "string",
                      "const": "list",
                      "description": "Always `list`"
                    },
                    "type": {
                      "type": "string",
                      "const": "thread_message",
                      "description": "Always `thread_message`"
                    },
                    "results": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "object": {
                            "type": "string",
                            "const": "thread_message",
                            "description": "Always `thread_message`"
                          },
                          "id": {
                            "$ref": "#/components/schemas/idResponse"
                          },
                          "role": {
                            "type": "string",
                            "enum": [
                              "user",
                              "agent"
                            ],
                            "description": "One of: `user`, `agent`"
                          },
                          "content": {
                            "type": "string"
                          },
                          "created_time": {
                            "type": "string",
                            "format": "date-time",
                            "description": "Date and time when this message was created."
                          },
                          "parent": {
                            "type": "object",
                            "properties": {
                              "type": {
                                "type": "string",
                                "const": "thread",
                                "description": "The parent type."
                              },
                              "id": {
                                "$ref": "#/components/schemas/idResponse",
                                "description": "The ID of the parent thread."
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "type",
                              "id"
                            ]
                          },
                          "attachments": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {
                                "name": {
                                  "type": "string"
                                },
                                "content_type": {
                                  "type": "string"
                                },
                                "url": {
                                  "type": "string"
                                },
                                "expiry_time": {
                                  "type": "string",
                                  "format": "date-time",
                                  "description": "The time when the attachment URL will expire."
                                }
                              },
                              "additionalProperties": false,
                              "required": [
                                "name",
                                "content_type",
                                "url"
                              ]
                            },
                            "maxItems": 100
                          },
                          "content_parts": {
                            "type": "array",
                            "items": {
                              "oneOf": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "type": {
                                      "type": "string",
                                      "const": "text",
                                      "description": "Always `text`"
                                    },
                                    "text": {
                                      "type": "string"
                                    }
                                  },
                                  "additionalProperties": false,
                                  "required": [
                                    "type",
                                    "text"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "type": {
                                      "type": "string",
                                      "const": "thinking",
                                      "description": "Always `thinking`"
                                    },
                                    "text": {
                                      "type": "string"
                                    }
                                  },
                                  "additionalProperties": false,
                                  "required": [
                                    "type",
                                    "text"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "type": {
                                      "type": "string",
                                      "const": "tool_call",
                                      "description": "Always `tool_call`"
                                    },
                                    "tool_call_id": {
                                      "oneOf": [
                                        {
                                          "type": "string"
                                        },
                                        {
                                          "type": "null"
                                        }
                                      ]
                                    },
                                    "tool_name": {
                                      "type": "string"
                                    },
                                    "input": {
                                      "type": "string"
                                    },
                                    "results": {
                                      "type": "array",
                                      "items": {
                                        "type": "object",
                                        "properties": {
                                          "id": {
                                            "$ref": "#/components/schemas/idResponse"
                                          },
                                          "agent_step_id": {
                                            "oneOf": [
                                              {
                                                "$ref": "#/components/schemas/idResponse"
                                              },
                                              {
                                                "type": "null"
                                              }
                                            ]
                                          },
                                          "tool_call_id": {
                                            "oneOf": [
                                              {
                                                "type": "string"
                                              },
                                              {
                                                "type": "null"
                                              }
                                            ]
                                          },
                                          "tool_name": {
                                            "type": "string"
                                          },
                                          "tool_type": {
                                            "type": "string"
                                          },
                                          "state": {
                                            "type": "string"
                                          },
                                          "input": {
                                            "oneOf": [
                                              {},
                                              {
                                                "type": "null"
                                              }
                                            ]
                                          },
                                          "output": {
                                            "oneOf": [
                                              {},
                                              {
                                                "type": "null"
                                              }
                                            ]
                                          },
                                          "error": {
                                            "oneOf": [
                                              {
                                                "type": "string"
                                              },
                                              {
                                                "type": "null"
                                              }
                                            ]
                                          },
                                          "started_at": {
                                            "type": "integer",
                                            "minimum": 0
                                          },
                                          "finished_at": {
                                            "oneOf": [
                                              {
                                                "type": "integer",
                                                "minimum": 0
                                              },
                                              {
                                                "type": "null"
                                              }
                                            ]
                                          },
                                          "duration_ms": {
                                            "oneOf": [
                                              {
                                                "type": "integer",
                                                "minimum": 0
                                              },
                                              {
                                                "type": "null"
                                              }
                                            ]
                                          }
                                        },
                                        "additionalProperties": false,
                                        "required": [
                                          "id",
                                          "agent_step_id",
                                          "tool_call_id",
                                          "tool_name",
                                          "tool_type",
                                          "state",
                                          "input",
                                          "output",
                                          "error",
                                          "started_at",
                                          "finished_at",
                                          "duration_ms"
                                        ]
                                      },
                                      "maxItems": 100
                                    }
                                  },
                                  "additionalProperties": false,
                                  "required": [
                                    "type",
                                    "tool_call_id",
                                    "tool_name",
                                    "input"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "type": {
                                      "type": "string",
                                      "const": "follow_ups",
                                      "description": "Always `follow_ups`"
                                    },
                                    "follow_ups": {
                                      "type": "array",
                                      "items": {
                                        "type": "object",
                                        "properties": {
                                          "label": {
                                            "type": "string"
                                          },
                                          "message": {
                                            "type": "string"
                                          }
                                        },
                                        "additionalProperties": false,
                                        "required": [
                                          "label",
                                          "message"
                                        ]
                                      },
                                      "maxItems": 100
                                    }
                                  },
                                  "additionalProperties": false,
                                  "required": [
                                    "type",
                                    "follow_ups"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "type": {
                                      "type": "string",
                                      "const": "custom_agent_template_picker",
                                      "description": "Always `custom_agent_template_picker`"
                                    }
                                  },
                                  "additionalProperties": false,
                                  "required": [
                                    "type"
                                  ]
                                }
                              ]
                            },
                            "maxItems": 100
                          }
                        },
                        "additionalProperties": false,
                        "required": [
                          "object",
                          "id",
                          "role",
                          "content",
                          "created_time",
                          "parent"
                        ]
                      },
                      "maxItems": 100
                    },
                    "has_more": {
                      "type": "boolean"
                    },
                    "next_cursor": {
                      "oneOf": [
                        {
                          "title": "Cursor",
                          "type": "string"
                        },
                        {
                          "type": "null"
                        }
                      ]
                    }
                  },
                  "additionalProperties": false,
                  "required": [
                    "object",
                    "type",
                    "results",
                    "has_more",
                    "next_cursor"
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        },
        "x-notion-docs-ref": "https://developers.notion.com/reference/internal/list-thread-messages"
      }
    },
    "/v1/agents/{agent_id}/threads": {
      "get": {
        "summary": "List threads",
        "operationId": "list-threads",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "agent_id",
            "in": "path",
            "required": true,
            "schema": {
              "oneOf": [
                {
                  "$ref": "#/components/schemas/idRequest"
                },
                {
                  "type": "string",
                  "const": "33333333-3333-3333-3333-333333333333",
                  "description": "Always `33333333-3333-3333-3333-333333333333`"
                }
              ],
              "description": "The ID of the agent. Use a UUID for custom agents, or `33333333-3333-3333-3333-333333333333` for the personal agent (Notion AI)."
            }
          },
          {
            "name": "id",
            "in": "query",
            "schema": {
              "$ref": "#/components/schemas/idRequest",
              "description": "Filter threads by ID (exact match)."
            }
          },
          {
            "name": "title",
            "in": "query",
            "schema": {
              "type": "string",
              "description": "Filter threads by title (case-insensitive substring match)."
            }
          },
          {
            "name": "status",
            "in": "query",
            "schema": {
              "type": "string",
              "enum": [
                "pending",
                "completed",
                "failed"
              ],
              "description": "Filter threads by status."
            }
          },
          {
            "name": "start_cursor",
            "in": "query",
            "schema": {
              "type": "string",
              "description": "If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results."
            }
          },
          {
            "name": "page_size",
            "in": "query",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100,
              "description": "The number of items from the full list desired in the response. Maximum: 100"
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "object": {
                      "type": "string",
                      "const": "list",
                      "description": "Always `list`"
                    },
                    "type": {
                      "type": "string",
                      "const": "thread",
                      "description": "Always `thread`"
                    },
                    "results": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "object": {
                            "type": "string",
                            "const": "thread",
                            "description": "Always `thread`"
                          },
                          "id": {
                            "$ref": "#/components/schemas/idResponse"
                          },
                          "title": {
                            "type": "string"
                          },
                          "status": {
                            "type": "string",
                            "enum": [
                              "pending",
                              "completed",
                              "failed"
                            ],
                            "description": "One of: `pending`, `completed`, `failed`"
                          },
                          "created_time": {
                            "type": "string",
                            "format": "date-time",
                            "description": "Date and time when this thread was created."
                          },
                          "last_edited_time": {
                            "type": "string",
                            "format": "date-time",
                            "description": "Date and time when this thread was last updated."
                          },
                          "created_by": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "$ref": "#/components/schemas/idResponse",
                                "description": "The ID of the bot for the calling integration that created this thread."
                              },
                              "type": {
                                "type": "string",
                                "const": "bot",
                                "description": "The creator type. List threads only returns bot-created threads."
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "id",
                              "type"
                            ]
                          },
                          "agent_version": {
                            "oneOf": [
                              {
                                "type": "object",
                                "properties": {
                                  "id": {
                                    "$ref": "#/components/schemas/idResponse",
                                    "description": "The ID of the published artifact."
                                  },
                                  "number": {
                                    "type": "number",
                                    "description": "The version number."
                                  },
                                  "published_at": {
                                    "type": "string",
                                    "description": "The ISO 8601 timestamp when this version was published."
                                  }
                                },
                                "additionalProperties": false,
                                "required": [
                                  "id",
                                  "number",
                                  "published_at"
                                ]
                              },
                              {
                                "type": "null"
                              }
                            ]
                          },
                          "error": {
                            "type": "string"
                          }
                        },
                        "additionalProperties": false,
                        "required": [
                          "object",
                          "id",
                          "title",
                          "status",
                          "created_time",
                          "last_edited_time",
                          "created_by",
                          "agent_version"
                        ]
                      },
                      "maxItems": 100
                    },
                    "has_more": {
                      "type": "boolean"
                    },
                    "next_cursor": {
                      "oneOf": [
                        {
                          "title": "Cursor",
                          "type": "string"
                        },
                        {
                          "type": "null"
                        }
                      ]
                    }
                  },
                  "additionalProperties": false,
                  "required": [
                    "object",
                    "type",
                    "results",
                    "has_more",
                    "next_cursor"
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        },
        "x-notion-docs-ref": "https://developers.notion.com/reference/internal/list-threads"
      }
    },
    "/v1/pages/{page_id}/remove_guests": {
      "post": {
        "summary": "Remove guests from a page",
        "operationId": "remove-page-guest",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "page_id",
            "in": "path",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/idRequest"
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {},
                "additionalProperties": false
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "anyOf": [
                    {
                      "$ref": "#/components/schemas/pageObjectResponse"
                    },
                    {
                      "$ref": "#/components/schemas/partialPageObjectResponse"
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/eval/run": {
      "post": {
        "summary": "Run an eval instance",
        "operationId": "run-eval-instance",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "vars": {
                    "type": "object",
                    "properties": {
                      "context_braintrust_id": {
                        "type": "string",
                        "examples": [
                          "project:dataset:rowId"
                        ],
                        "description": "Braintrust dataset row ID in 'project:dataset:rowId' format. Provide either this or context_json."
                      }
                    },
                    "description": "Scenario data source."
                  },
                  "options": {
                    "type": "object",
                    "properties": {
                      "run_mode": {
                        "type": "string",
                        "enum": [
                          "agent",
                          "inference"
                        ],
                        "description": "Execution mode. 'agent' (default) runs the closed-loop agent runner. 'inference' runs a single open-loop completion."
                      },
                      "notion_model_name": {
                        "type": "string",
                        "examples": [
                          "orange-tart"
                        ],
                        "description": "Model name. Defaults to 'orange-tart'."
                      },
                      "workflow_agent_mode": {
                        "type": "string",
                        "enum": [
                          "basic",
                          "all"
                        ],
                        "description": "Workflow agent mode."
                      },
                      "context_page_id": {
                        "type": "string",
                        "examples": [
                          "page-uuid"
                        ],
                        "description": "Context page ID for the eval run."
                      }
                    },
                    "description": "Execution options."
                  }
                },
                "required": [
                  "vars"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "raw": {
                      "description": "Raw inference result."
                    },
                    "formatted": {
                      "type": "string",
                      "examples": [
                        "<text>Hello</text>"
                      ],
                      "description": "XML-formatted model output."
                    }
                  },
                  "additionalProperties": false,
                  "required": [
                    "raw",
                    "formatted"
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/tools/run": {
      "post": {
        "summary": "Run an AI tool",
        "operationId": "run-tool",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "search",
                        "description": "The name of the tool to run."
                      },
                      "search": {
                        "type": "object",
                        "properties": {
                          "query": {
                            "type": "string",
                            "minLength": 1,
                            "description": "Semantic search query over your entire Notion workspace and connected sources\n(Slack, Google Drive, Github, Jira, Microsoft Teams, Sharepoint, OneDrive,\nor Linear). For best results, don't provide more than one question per tool call.\nUse a separate \"search\" tool call for each search you want to perform.\n\nAlternatively, the query can be a substring or keyword to find users by matching\nagainst their name or email address. For example: \"john\" or \"john@example.com\""
                          },
                          "query_type": {
                            "type": "string",
                            "enum": [
                              "internal",
                              "user"
                            ],
                            "description": "Specify type of the query as either \"internal\" or \"user\". Always include this input if performing\n\"user\" search."
                          },
                          "content_search_mode": {
                            "type": "string",
                            "enum": [
                              "workspace_search",
                              "ai_search"
                            ],
                            "description": "Select search backend: \"workspace_search\" (faster, workspace-only) or \"ai_search\" (semantic, includes Slack/Linear/etc.). If omitted, uses AI search if available. Content searches only."
                          },
                          "data_source_url": {
                            "type": "string",
                            "description": "Optionally, provide the URL of a Data source to search. This will perform a semantic search over\nthe pages in the Data Source. Note: must be a Data Source, not a Database. <data-source> tags are\npart of the Notion flavored Markdown format returned by tools like fetch. The full spec is\navailable in the create-pages tool description."
                          },
                          "page_url": {
                            "type": "string",
                            "description": "Optionally, provide the URL or ID of a page to search within. This will perform a semantic search\nover the content within and under the specified page. Accepts either a full page URL\n(e.g. https://notion.so/workspace/Page-Title-1234567890) or just the page ID (UUIDv4) with or\nwithout dashes."
                          },
                          "teamspace_id": {
                            "type": "string",
                            "description": "Optionally, provide the ID of a teamspace to restrict search results to. This will perform a search\nover content within the specified teamspace only. Accepts the teamspace ID (UUIDv4) with or\nwithout dashes."
                          },
                          "filters": {
                            "type": "object",
                            "properties": {
                              "created_date_range": {
                                "type": "object",
                                "properties": {
                                  "start_date": {
                                    "type": "string",
                                    "format": "date",
                                    "description": "The start date of the date range as an ISO 8601 date string, if any."
                                  },
                                  "end_date": {
                                    "type": "string",
                                    "format": "date",
                                    "description": "The end date of the date range as an ISO 8601 date string, if any."
                                  }
                                },
                                "description": "Optional filter to only produce search results created within the specified date range."
                              },
                              "created_by_user_ids": {
                                "type": "array",
                                "items": {
                                  "$ref": "#/components/schemas/idRequest"
                                },
                                "maxItems": 100,
                                "description": "Optional filter to only produce search results created by the Notion users that have the specified user IDs."
                              }
                            },
                            "description": "Optionally provide filters to apply to the search results. Only valid when query_type is 'internal'."
                          },
                          "page_size": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 25,
                            "description": "Maximum number of results to return (default 10). Lower values reduce response size."
                          },
                          "max_highlight_length": {
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 500,
                            "description": "Maximum character length for result highlights (default 200). Set to 0 to omit highlights entirely."
                          }
                        },
                        "required": [
                          "query"
                        ],
                        "description": "The parameters for the search tool. Perform a search over:\n\t\t- \"internal\": Semantic search over Notion workspace and connected sources (Slack, Google Drive,\n\t\t  Github, Jira, Microsoft Teams, Sharepoint, OneDrive, Linear). Supports filtering by creation\n\t\t  date and creator.\n\t\t- \"user\": Search for users by name or email.\n\n\t\tAuto-selects AI search (with connected sources) or workspace search (workspace-only, faster)\n\t\tbased on user's access to Notion AI. Use content_search_mode to override.\n\n\t\tUse \"fetch\" tool for full page/database contents after getting search results.\n\t\tEach result's \"url\" field contains a page ID for Notion results (pass directly to\n\t\tfetch tool's \"id\" param) or a full URL for external connector results (Slack, Google\n\t\tDrive, etc.). Set page_size (default 10, max 25) and max_highlight_length (default\n\t\t200, 0 to omit) as low as possible to minimize response size.\n\n\t\tTo search within a database: First fetch the database to get the data source URL\n\t\t(collection://...) from <data-source url=\"...\"> tags, then use that as data_source_url.\n\t\tFor multi-source databases, match by view ID (?v=...) in URL or search all sources separately.\n\n\t\tDon't combine database URL/ID with collection:// prefix for data_source_url. Don't use\n\t\tdatabase URL as page_url.\n\n\t\t<example description=\"Search with date range filter (only documents created in 2024)\">\n\t\t{\n\t\t\t\"query\": \"quarterly revenue report\",\n\t\t\t\"query_type\": \"internal\",\n\t\t\t\"filters\": {\n\t\t\t\t\"created_date_range\": {\n\t\t\t\t\t\"start_date\": \"2024-01-01\",\n\t\t\t\t\t\"end_date\": \"2025-01-01\"\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Teamspace + creator filter\">\n\t\t{\"query\": \"project updates\", \"query_type\": \"internal\", \"teamspace_id\": \"f336d0bc-b841-465b-8045-024475c079dd\", \"filters\": {\"created_by_user_ids\": [\"a1b2c3d4-e5f6-7890-abcd-ef1234567890\"]}}\n\t\t</example>\n\n\t\t<example description=\"Database with date + creator filters\">\n\t\t{\"query\": \"design review\", \"data_source_url\": \"collection://f336d0bc-b841-465b-8045-024475c079dd\", \"filters\": {\"created_date_range\": {\"start_date\": \"2024-10-01\"}, \"created_by_user_ids\": [\"a1b2c3d4-e5f6-7890-abcd-ef1234567890\", \"b2c3d4e5-f6a7-8901-bcde-f12345678901\"]}}\n\t\t</example>\n\n\t\t<example description=\"User search\">\n\t\t{\"query\": \"john@example.com\", \"query_type\": \"user\"}\n\t\t</example>"
                      }
                    },
                    "required": [
                      "type",
                      "search"
                    ],
                    "title": "Search"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "fetch",
                        "description": "The name of the tool to run."
                      },
                      "fetch": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string",
                            "description": "The ID or URL of the Notion page, database, or data source to fetch. Supports notion.so URLs, Notion Sites URLs (*.notion.site), raw UUIDs, and data source URLs (collection://...)."
                          },
                          "include_transcript": {
                            "type": "boolean",
                            "description": "Whether to include meeting note transcripts. Defaults to false. When true, full transcripts are included; when false, a placeholder with the meeting note URL is shown instead."
                          },
                          "include_discussions": {
                            "type": "boolean",
                            "description": "Whether to include discussion/comment indicators in the page output. When true, adds a <page-discussions> summary with discussion count, preview snippets, and discussion:// URLs. Use with the get_comments tool to retrieve full discussion content. Defaults to false."
                          }
                        },
                        "required": [
                          "id"
                        ],
                        "description": "The parameters for the fetch tool. Retrieves details about a Notion entity (page, database, or data source) by URL or ID.\n\nProvide URL or ID in `id` parameter. Make multiple calls to fetch multiple entities.\n\nPages use enhanced Markdown format. For the complete specification, fetch the MCP resource\nat `notion://docs/enhanced-markdown-spec`.\n\nDatabases return all data sources (collections). Each data source has a unique ID shown in\n`<data-source url=\"collection://...\">` tags. You can pass a data source ID directly to this\ntool to fetch details about that specific data source, including its schema and properties.\nUse data source IDs with update_data_source and query_data_sources tools. Multi-source\ndatabases (e.g., with linked sources) will show multiple data sources.\n\nSet `include_discussions` to true to see discussion counts and inline discussion markers\nthat correlate with the `get_comments` tool. The page output will include a\n`<page-discussions>` summary tag with discussion count, preview snippets, and\n`discussion://` URLs that match the discussion IDs returned by `get_comments`.\n\n<example>{\"id\": \"https://notion.so/workspace/Page-a1b2c3d4e5f67890\"}</example>\n<example>{\"id\": \"12345678-90ab-cdef-1234-567890abcdef\"}</example>\n<example>{\"id\": \"https://myspace.notion.site/Page-Title-abc123def456\"}</example>\n<example>{\"id\": \"page-uuid\", \"include_discussions\": true}</example>\n<example>{\"id\": \"collection://12345678-90ab-cdef-1234-567890abcdef\"}</example>"
                      }
                    },
                    "required": [
                      "type",
                      "fetch"
                    ],
                    "title": "Fetch"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "create_pages",
                        "description": "The name of the tool to run."
                      },
                      "create_pages": {
                        "type": "object",
                        "properties": {
                          "pages": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {
                                "properties": {
                                  "type": "object",
                                  "additionalProperties": {
                                    "oneOf": [
                                      {
                                        "type": "string"
                                      },
                                      {
                                        "type": "number"
                                      },
                                      {
                                        "type": "null"
                                      }
                                    ]
                                  },
                                  "description": "The properties of the new page, which is a JSON map of property names to SQLite values.\nFor pages in a database, use the SQLite schema definition shown in <database>.\nFor pages outside of a database, the only allowed property is \"title\", which is the title of the page and is automatically shown at the top of the page as a large heading."
                                },
                                "content": {
                                  "type": "string",
                                  "description": "The content of the new page, using Notion Markdown."
                                },
                                "template_id": {
                                  "type": "string",
                                  "description": "The ID of a template to apply to this page. When specified, do not provide 'content' as the template will provide it. Properties can still be set alongside the template. Get template IDs from the <templates> section in the fetch tool results."
                                },
                                "icon": {
                                  "type": "string",
                                  "description": "An emoji character (e.g. \"🚀\"), a custom emoji by name (e.g. \":rocket_ship:\"), or an external image URL. Use \"none\" to explicitly set no icon. Omit to leave unchanged."
                                },
                                "cover": {
                                  "type": "string",
                                  "description": "An external image URL for the page cover. Use \"none\" to explicitly set no cover. Omit to leave unchanged."
                                }
                              },
                              "additionalProperties": false
                            },
                            "maxItems": 100,
                            "description": "The pages to create."
                          },
                          "parent": {
                            "oneOf": [
                              {
                                "type": "object",
                                "properties": {
                                  "page_id": {
                                    "$ref": "#/components/schemas/idRequest",
                                    "description": "The ID of the parent page (with or without dashes), for example, 195de9221179449fab8075a27c979105"
                                  },
                                  "type": {
                                    "type": "string",
                                    "const": "page_id",
                                    "description": "Always `page_id`"
                                  }
                                },
                                "required": [
                                  "page_id"
                                ]
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "database_id": {
                                    "$ref": "#/components/schemas/idRequest",
                                    "description": "The ID of the parent database (with or without dashes), for example, 195de9221179449fab8075a27c979105"
                                  },
                                  "type": {
                                    "type": "string",
                                    "const": "database_id",
                                    "description": "Always `database_id`"
                                  }
                                },
                                "required": [
                                  "database_id"
                                ]
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "data_source_id": {
                                    "$ref": "#/components/schemas/idRequest",
                                    "description": "The ID of the parent data source (collection), with or without dashes. For example, f336d0bc-b841-465b-8045-024475c079dd"
                                  },
                                  "type": {
                                    "type": "string",
                                    "const": "data_source_id",
                                    "description": "Always `data_source_id`"
                                  }
                                },
                                "required": [
                                  "data_source_id"
                                ]
                              }
                            ],
                            "description": "The parent under which the new pages will be created. This can be a page (page_id), a database page (database_id), or a data source/collection under a database (data_source_id). If omitted, the new pages will be created as private pages at the workspace level. Use data_source_id when you have a collection:// URL from the fetch tool."
                          }
                        },
                        "required": [
                          "pages"
                        ],
                        "description": "The parameters for the create_pages tool. ## Overview\n\n\t\tCreates one or more Notion pages, with the specified properties and content.\n\n\t\t## Parent\n\n\t\tAll pages created with a single call to this tool will have the same parent.\n\t\tThe parent can be a Notion page (\"page_id\") or data source (\"data_source_id\").\n\t\tIf the parent is omitted, the pages are created as standalone, workspace-level\n\t\tprivate pages, and the person that created them can organize them later as they\n\t\tsee fit.\n\n\t\tIf you have a database URL, ALWAYS pass it to the \"fetch\" tool first to get the schema\n\t\tand URLs of each data source under the database. You can't use the \"database_id\"\n\t\tparent type if the database has more than one data source, so you'll need to identify\n\t\twhich \"data_source_id\" to use based on the situation and the results from the fetch tool\n\t\t(data source URLs look like collection://<data_source_id>).\n\n\t\tIf you know the pages should be created under a data source, do NOT use the database ID\n\t\tor URL under the \"page_id\" parameter; \"page_id\" is only for regular, non-database pages.\n\n\t\t## Content\n\n\t\tNotion page content is a string in Notion-flavored Markdown format.\n\n\t\tDon't include the page title at the top of the page's content. Only include it under\n\t\t\"properties\".\n\n\t\t**IMPORTANT**: For the complete Markdown specification, always first fetch the MCP resource\n\t\tat `notion://docs/enhanced-markdown-spec`. Do NOT guess or hallucinate Markdown syntax.\n\t\tThis spec is also applicable to other tools like update-page and fetch.\n\n\t\t## Properties\n\n\t\tNotion page properties are a JSON map of property names to SQLite values.\n\n\t\tWhen creating pages in a database:\n\t\t- Use the correct property names from the data source schema shown in the fetch tool results.\n\t\t- Always include a title property. Data sources always have exactly one title property, but\n\t\t  it may not be named \"title\", so, again, rely on the fetched data source schema.\n\n\t\tFor pages outside of a database:\n\t\t- The only allowed property is \"title\",\twhich is the title of the page in inline markdown format.\n\t\t  Always include a \"title\" property.\n\n\t\t**IMPORTANT**: Some property types require expanded formats:\n\t\t- Date properties: Split into \"date:{property}:start\", \"date:{property}:end\" (optional), and\n\t\t  \"date:{property}:is_datetime\" (0 or 1)\n\t\t- Place properties: Split into \"place:{property}:name\", \"place:{property}:address\",\n\t\t  \"place:{property}:latitude\", \"place:{property}:longitude\", and\n\t\t  \"place:{property}:google_place_id\" (optional)\n\t\t- Number properties: Use JavaScript numbers (not strings)\n\t\t- Checkbox properties: Use \"__YES__\" for checked, \"__NO__\" for unchecked\n\n\t\t**Special property naming**: Properties named \"id\" or \"url\" (case insensitive) must be\n\t\tprefixed with \"userDefined:\" (e.g., \"userDefined:URL\", \"userDefined:id\")\n\n\t\t## Templates\n\n\t\tWhen creating a page in a database, you can apply a template to pre-populate it with\n\t\tcontent and property values. Use the \"fetch\" tool on a database to see available\n\t\ttemplates in the <templates> section of each data source.\n\n\t\tWhen using a template:\n\t\t- Pass the template's ID as \"template_id\" in the page object.\n\t\t- Do NOT include \"content\" when using a template, as the template provides it.\n\t\t- You can still set \"properties\" alongside the template to override template defaults.\n\t\t- Template application is asynchronous. The page is created immediately but starts\n\t\t  blank; the template content will appear shortly after.\n\n\t\t## Icon and Cover\n\n\t\tEach page can optionally have an icon and a cover image.\n\t\t- \"icon\": An emoji character (e.g. \"🚀\"), a custom emoji by name (e.g. \":rocket_ship:\"),\n\t\t  or an external image URL. Use \"none\" to remove. Omit to leave unchanged.\n\t\t- \"cover\": An external image URL. Use \"none\" to remove. Omit to leave unchanged.\n\n\t\t## Examples\n\n\t\t<example description=\"Create a page with an icon and cover\">\n\t\t{\n\t\t\t\"pages\": [\n\t\t\t\t{\n\t\t\t\t\t\"properties\": {\"title\": \"My Page\"},\n\t\t\t\t\t\"icon\": \"🚀\",\n\t\t\t\t\t\"cover\": \"https://example.com/cover.jpg\"\n\t\t\t\t}\n\t\t\t]\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Create a page from a database template\">\n\t\t{\n\t\t\t\"parent\": {\"data_source_id\": \"f336d0bc-b841-465b-8045-024475c079dd\"},\n\t\t\t\"pages\": [\n\t\t\t\t{\n\t\t\t\t\t\"template_id\": \"a5da15f6-b853-455d-8827-f906fb52db2b\",\n\t\t\t\t\t\"properties\": {\n\t\t\t\t\t\t\"Task Name\": \"New urgent bug\"\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t]\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Create a standalone page with a title and content\">\n\t\t{\n\t\t\t\"pages\": [\n\t\t\t\t{\n\t\t\t\t\t\"properties\": {\"title\": \"Page title\"},\n\t\t\t\t\t\"content\": \"# Section 1 {color=\"blue\"}\nSection 1 content\n<details>\n<summary>Toggle block</summary>\n\tHidden content inside toggle\n</details>\"\n\t\t\t\t}\n\t\t\t]\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Create a page under a database's data source\">\n\t\t{\n\t\t\t\"parent\": {\"data_source_id\": \"f336d0bc-b841-465b-8045-024475c079dd\"},\n\t\t\t\"pages\": [\n\t\t\t\t{\n\t\t\t\t\t\"properties\": {\n\t\t\t\t\t\t\"Task Name\": \"Task 123\",\n\t\t\t\t\t\t\"Status\": \"In Progress\",\n\t\t\t\t\t\t\"Priority\": 5,\n\t\t\t\t\t\t\"Is Complete\": \"__YES__\",\n\t\t\t\t\t\t\"date:Due Date:start\": \"2024-12-25\",\n\t\t\t\t\t\t\"date:Due Date:is_datetime\": 0\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t]\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Create a page with an existing page as a parent\">\n\t\t{\n\t\t\t\"parent\": {\"page_id\": \"a1b2c3d4-e5f6-7890-abcd-ef1234567890\"},\n\t\t\t\"pages\": [\n\t\t\t\t{\n\t\t\t\t\t\"properties\": {\"title\": \"Page title\"},\n\t\t\t\t\t\"content\": \"# Section 1\n\nSection 1 content\n\n# Section 2\n\nSection 2 content\"\n\t\t\t\t}\n\t\t\t]\n\t\t}\n\t\t</example>"
                      }
                    },
                    "required": [
                      "type",
                      "create_pages"
                    ],
                    "title": "Create Pages"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "update_page",
                        "description": "The name of the tool to run."
                      },
                      "update_page": {
                        "type": "object",
                        "properties": {
                          "page_id": {
                            "type": "string",
                            "description": "The ID of the page to update, with or without dashes."
                          },
                          "command": {
                            "type": "string",
                            "enum": [
                              "update_properties",
                              "update_content",
                              "replace_content",
                              "apply_template",
                              "update_verification"
                            ],
                            "description": "The update command to execute."
                          },
                          "properties": {
                            "type": "object",
                            "additionalProperties": {
                              "oneOf": [
                                {
                                  "type": "string"
                                },
                                {
                                  "type": "number"
                                },
                                {
                                  "type": "null"
                                }
                              ]
                            },
                            "description": "Required for \"update_properties\" command. A JSON object that updates the page's properties.\nFor pages in a database, use the SQLite schema definition shown in <database>.\nFor pages outside of a database, the only allowed property is \"title\", which is the title of the page in inline markdown format.\nUse null to remove a property's value."
                          },
                          "new_str": {
                            "type": "string",
                            "description": "Required for \"replace_content\" command. The new content string to replace the entire page content with."
                          },
                          "content_updates": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {
                                "old_str": {
                                  "type": "string",
                                  "description": "The existing content string to find and replace. Must exactly match the page content."
                                },
                                "new_str": {
                                  "type": "string",
                                  "description": "The new content string to replace old_str with."
                                },
                                "replace_all_matches": {
                                  "type": "boolean",
                                  "description": "If true, replaces all occurrences of old_str. If false (default), the operation fails if there are multiple matches."
                                }
                              },
                              "required": [
                                "old_str",
                                "new_str"
                              ]
                            },
                            "maxItems": 100,
                            "description": "Required for \"update_content\" command. An array of search-and-replace operations, each with old_str (content to find) and new_str (replacement content)."
                          },
                          "allow_deleting_content": {
                            "type": "boolean",
                            "description": "Optional for \"replace_content\" and \"update_content\" commands. Set to true to allow deletion of child pages and databases that are not referenced in the new content. If false or omitted, the operation will fail with an error listing the pages/databases that would be deleted."
                          },
                          "template_id": {
                            "type": "string",
                            "description": "Required for \"apply_template\" command. The ID of a template to apply to this page. Template content is appended to any existing page content."
                          },
                          "verification_status": {
                            "type": "string",
                            "enum": [
                              "verified",
                              "unverified"
                            ],
                            "description": "Required for \"update_verification\" command. Set to \"verified\" to mark the page as verified, or \"unverified\" to remove verification."
                          },
                          "verification_expiry_days": {
                            "type": "integer",
                            "minimum": 1,
                            "description": "Optional for \"update_verification\" command when verification_status is \"verified\". Number of days until verification expires (e.g. 7, 30, 90). Omit for indefinite verification."
                          },
                          "icon": {
                            "type": "string",
                            "description": "An emoji character (e.g. \"🚀\"), a custom emoji by name (e.g. \":rocket_ship:\"), or an external image URL. Use \"none\" to remove the icon. Omit to leave unchanged. Can be set alongside any command."
                          },
                          "cover": {
                            "type": "string",
                            "description": "An external image URL for the page cover. Use \"none\" to remove the cover. Omit to leave unchanged. Can be set alongside any command."
                          }
                        },
                        "required": [
                          "page_id",
                          "command"
                        ],
                        "description": "The parameters for the update_page tool. ## Overview\n\n\t\tUpdate a Notion page's properties or content.\n\n\t\t## Properties\n\n\t\tNotion page properties are a JSON map of property names to SQLite values.\n\n\t\tFor pages in a database:\n\t\t- ALWAYS use the \"fetch\" tool first to get the data source schema and the\texact property names.\n\t\t- Provide a non-null value to update a property's value.\n\t\t- Omitted properties are left unchanged.\n\n\t\t**IMPORTANT**: Some property types require expanded formats:\n\t\t- Date properties: Split into \"date:{property}:start\", \"date:{property}:end\" (optional), and\n\t\t  \"date:{property}:is_datetime\" (0 or 1)\n\t\t- Place properties: Split into \"place:{property}:name\", \"place:{property}:address\",\n\t\t  \"place:{property}:latitude\", \"place:{property}:longitude\", and\n\t\t  \"place:{property}:google_place_id\" (optional)\n\t\t- Number properties: Use JavaScript numbers (not strings)\n\t\t- Checkbox properties: Use \"__YES__\" for checked, \"__NO__\" for unchecked\n\n\t\t**Special property naming**: Properties named \"id\" or \"url\" (case insensitive) must be\n\t\tprefixed with \"userDefined:\" (e.g., \"userDefined:URL\", \"userDefined:id\")\n\n\t\tFor pages outside of a database:\n\t\t- The only allowed property is \"title\",\twhich is the title of the page in inline markdown format.\n\n\t\t## Content\n\n\t\tNotion page content is a string in Notion-flavored Markdown format.\n\n\t\t**IMPORTANT**: For the complete Markdown specification, first fetch the MCP resource at\n\t\t`notion://docs/enhanced-markdown-spec`. Do NOT guess or hallucinate Markdown syntax.\n\n\t\tBefore updating a page's content with this tool, use the \"fetch\" tool first to get the existing\n\t\tcontent to find out the Markdown snippets to use in the \"update_content\" command's old_str fields.\n\n\t\t### Preserving Child Pages and Databases\n\n\t\tWhen using \"replace_content\", the operation will check if any\n\t\tchild pages or databases would be deleted. If so, it will fail with an error listing the\n\t\taffected items.\n\n\t\tTo preserve child pages/databases, include them in new_str using `<page url=\"...\">` or\n\t\t`<database url=\"...\">` tags. Get the exact URLs from the \"fetch\" tool output.\n\n\t\t**CRITICAL**: To intentionally delete child content:\n\t\tif the call failed with validation and requires `allow_deleting_content` to be true,\n\t\tDO NOT automatically assume the content should be deleted.\n\t\tALWAYS show the list of pages to be deleted and ask for user confirmation before proceeding.\n\n\t\t## Icon and Cover\n\n\t\tYou can set or remove a page's icon and cover alongside any command.\n\t\t- \"icon\": An emoji character (e.g. \"🚀\"), a custom emoji by name (e.g. \":rocket_ship:\"),\n\t\t  or an external image URL. Use \"none\" to remove. Omit to leave unchanged.\n\t\t- \"cover\": An external image URL. Use \"none\" to remove. Omit to leave unchanged.\n\n\t\t## Examples\n\n\t\t<example description=\"Update page icon and cover\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"update_properties\",\n\t\t\t\"properties\": {\"title\": \"My Page\"},\n\t\t\t\"icon\": \"🚀\",\n\t\t\t\"cover\": \"https://example.com/cover.jpg\"\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Update page properties\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"update_properties\",\n\t\t\t\"properties\": {\n\t\t\t\t\"title\": \"New Page Title\",\n\t\t\t\t\"status\": \"In Progress\",\n\t\t\t\t\"priority\": 5,\n\t\t\t\t\"checkbox\": \"__YES__\",\n\t\t\t\t\"date:deadline:start\": \"2024-12-25\",\n\t\t\t\t\"date:deadline:is_datetime\": 0,\n\t\t\t\t\"place:office:name\": \"HQ\",\n\t\t\t\t\"place:office:latitude\": 37.7749,\n\t\t\t\t\"place:office:longitude\": -122.4194\n\t\t\t}\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Replace the entire content of a page\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"replace_content\",\n\t\t\t\"new_str\": \"# New Section\\nUpdated content goes here\"\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Update specific content in a page (search-and-replace)\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"update_content\",\n\t\t\t\"content_updates\": [\n\t\t\t\t{\n\t\t\t\t\t\"old_str\": \"# Old Section\\nOld content here\",\n\t\t\t\t\t\"new_str\": \"# New Section\\nUpdated content goes here\"\n\t\t\t\t}\n\t\t\t]\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Insert content after a specific location\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"update_content\",\n\t\t\t\"content_updates\": [\n\t\t\t\t{\n\t\t\t\t\t\"old_str\": \"## Previous section\\nExisting content\",\n\t\t\t\t\t\"new_str\": \"## Previous section\\nExisting content\\n\\n## New Section\\nContent to insert goes here\"\n\t\t\t\t}\n\t\t\t]\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Multiple content updates in a single call\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"update_content\",\n\t\t\t\"content_updates\": [\n\t\t\t\t{\n\t\t\t\t\t\"old_str\": \"Old text 1\",\n\t\t\t\t\t\"new_str\": \"New text 1\"\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\t\"old_str\": \"Old text 2\",\n\t\t\t\t\t\"new_str\": \"New text 2\"\n\t\t\t\t}\n\t\t\t]\n\t\t}\n\t\t</example>\n\n\t\t## Templates\n\n\t\tYou can apply a template to an existing page using the \"apply_template\" command.\n\t\tThe template content is appended to the page asynchronously. Get template IDs from\n\t\tthe <templates> section in the fetch tool results for a database, or use any page ID\n\t\tas a template.\n\n\t\t<example description=\"Apply a template to an existing page\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"apply_template\",\n\t\t\t\"template_id\": \"a5da15f6-b853-455d-8827-f906fb52db2b\"\n\t\t}\n\t\t</example>\n\n\t\t## Verification\n\n\t\tYou can verify or unverify a page using the \"update_verification\" command.\n\t\tVerification marks a page as reviewed and up-to-date. Requires a Business or Enterprise\n\t\tplan (or the page must be in a wiki).\n\n\t\t<example description=\"Verify a page for 90 days\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"update_verification\",\n\t\t\t\"verification_status\": \"verified\",\n\t\t\t\"verification_expiry_days\": 90\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Verify a page indefinitely\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"update_verification\",\n\t\t\t\"verification_status\": \"verified\"\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Remove verification from a page\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"update_verification\",\n\t\t\t\"verification_status\": \"unverified\"\n\t\t}\n\t\t</example>"
                      }
                    },
                    "required": [
                      "type",
                      "update_page"
                    ],
                    "title": "Update Page"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "move_pages",
                        "description": "The name of the tool to run."
                      },
                      "move_pages": {
                        "type": "object",
                        "properties": {
                          "page_or_database_ids": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            },
                            "maxItems": 100,
                            "minItems": 1,
                            "description": "An array of up to 100 page or database IDs to move. IDs are v4 UUIDs and can be supplied with or without dashes (e.g. extracted from a <page> or <database> URL given by the \"search\" or \"fetch\" tool). Data Sources under Databases can't be moved individually."
                          },
                          "new_parent": {
                            "oneOf": [
                              {
                                "type": "object",
                                "properties": {
                                  "page_id": {
                                    "$ref": "#/components/schemas/idRequest",
                                    "description": "The ID of the parent page (with or without dashes), for example, 195de9221179449fab8075a27c979105"
                                  },
                                  "type": {
                                    "type": "string",
                                    "const": "page_id",
                                    "description": "Always `page_id`"
                                  }
                                },
                                "required": [
                                  "page_id"
                                ]
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "database_id": {
                                    "$ref": "#/components/schemas/idRequest",
                                    "description": "The ID of the parent database (with or without dashes), for example, 195de9221179449fab8075a27c979105"
                                  },
                                  "type": {
                                    "type": "string",
                                    "const": "database_id",
                                    "description": "Always `database_id`"
                                  }
                                },
                                "required": [
                                  "database_id"
                                ]
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "data_source_id": {
                                    "$ref": "#/components/schemas/idRequest",
                                    "description": "The ID of the parent data source (collection), with or without dashes. For example, f336d0bc-b841-465b-8045-024475c079dd"
                                  },
                                  "type": {
                                    "type": "string",
                                    "const": "data_source_id",
                                    "description": "Always `data_source_id`"
                                  }
                                },
                                "required": [
                                  "data_source_id"
                                ]
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "type": {
                                    "type": "string",
                                    "const": "workspace",
                                    "description": "The parent type."
                                  }
                                },
                                "required": [
                                  "type"
                                ]
                              }
                            ],
                            "description": "The new parent under which the pages will be moved. This can be a page, the workspace, a database, or a specific data source under a database when there are multiple. Moving pages to the workspace level adds them as private pages and should rarely be used."
                          }
                        },
                        "required": [
                          "page_or_database_ids",
                          "new_parent"
                        ],
                        "description": "The parameters for the move_pages tool. Move one or more Notion pages or databases to a new parent."
                      }
                    },
                    "required": [
                      "type",
                      "move_pages"
                    ],
                    "title": "Move Pages"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "duplicate_page",
                        "description": "The name of the tool to run."
                      },
                      "duplicate_page": {
                        "type": "object",
                        "properties": {
                          "page_id": {
                            "type": "string",
                            "description": "The ID of the page to duplicate. This is a v4 UUID, with or without dashes, and can be parsed from a Notion page URL."
                          }
                        },
                        "required": [
                          "page_id"
                        ],
                        "description": "The parameters for the duplicate_page tool. Duplicate a Notion page. The page must be within the current workspace, and you must have permission to access it. The duplication completes asynchronously, so do not rely on the new page identified by the returned ID or URL to be populated immediately. Let the user know that the duplication is in progress and that they can check back later using the 'fetch' tool or by clicking the returned URL and viewing it in the Notion app."
                      }
                    },
                    "required": [
                      "type",
                      "duplicate_page"
                    ],
                    "title": "Duplicate Page"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "create_database",
                        "description": "The name of the tool to run."
                      },
                      "create_database": {
                        "type": "object",
                        "properties": {
                          "schema": {
                            "type": "string",
                            "description": "SQL DDL CREATE TABLE statement defining the database schema. Column names must be double-quoted, type options use single quotes."
                          },
                          "parent": {
                            "type": "object",
                            "properties": {
                              "page_id": {
                                "$ref": "#/components/schemas/idRequest",
                                "description": "The ID of the parent page (with or without dashes), for example, 195de9221179449fab8075a27c979105"
                              },
                              "type": {
                                "type": "string",
                                "const": "page_id",
                                "description": "Always `page_id`"
                              }
                            },
                            "required": [
                              "page_id"
                            ],
                            "description": "The parent under which to create the new database. If omitted, the database will be created as a private page at the workspace level."
                          },
                          "title": {
                            "type": "string",
                            "description": "The title of the new database."
                          },
                          "description": {
                            "type": "string",
                            "description": "The description of the new database."
                          }
                        },
                        "required": [
                          "schema"
                        ],
                        "description": "The parameters for the create_database tool. Creates a new Notion database using SQL DDL syntax.\n\nIf no title property provided, \"Name\" is auto-added. Returns Markdown with schema,\nSQLite definition, and data source ID in <data-source> tag for use with\nupdate_data_source and query_data_sources tools.\n\nThe schema param accepts a CREATE TABLE statement defining columns.\n\nType syntax:\n- Simple: TITLE, RICH_TEXT, DATE, PEOPLE, CHECKBOX, URL, EMAIL, PHONE_NUMBER, STATUS, FILES\n- SELECT('opt':color, ...) / MULTI_SELECT('opt':color, ...)\n- NUMBER [FORMAT 'dollar'] / FORMULA('expression')\n- RELATION('data_source_id') — one-way relation\n- RELATION('data_source_id', DUAL) — two-way relation\n- RELATION('data_source_id', DUAL 'synced_name') — two-way with synced property name\n- RELATION('data_source_id', DUAL 'synced_name' 'synced_id') — two-way with synced name and ID (for self-relations)\n- ROLLUP('rel_prop', 'target_prop', 'function')\n- UNIQUE_ID [PREFIX 'X'] / CREATED_TIME / LAST_EDITED_TIME\n- Any column: COMMENT 'description text'\nColors: default, gray, brown, orange, yellow, green, blue, purple, pink, red\n\n<example description=\"Minimal\">{\"schema\": \"CREATE TABLE (\\\"Name\\\" TITLE)\"}</example>\n<example description=\"Task DB\">{\"title\": \"Tasks\", \"schema\": \"CREATE TABLE (\\\"Task Name\\\" TITLE, \\\"Status\\\" SELECT('To Do':red, 'Done':green), \\\"Due Date\\\" DATE)\"}</example>\n<example description=\"With parent and options\">{\"parent\": {\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\"}, \"title\": \"Projects\", \"schema\": \"CREATE TABLE (\\\"Name\\\" TITLE, \\\"Budget\\\" NUMBER FORMAT 'dollar', \\\"Tags\\\" MULTI_SELECT('eng':blue, 'design':pink), \\\"Task ID\\\" UNIQUE_ID PREFIX 'PRJ')\"}</example>\n<example description=\"Self-relation (two-step: create database first, then use its data source ID with update_data_source to add self-relations)\">{\"title\": \"Tasks\", \"schema\": \"CREATE TABLE (\\\"Name\\\" TITLE, \\\"Parent\\\" RELATION('ds_id', DUAL 'Children' 'children'), \\\"Children\\\" RELATION('ds_id', DUAL 'Parent' 'parent'))\"}</example>"
                      }
                    },
                    "required": [
                      "type",
                      "create_database"
                    ],
                    "title": "Create Database"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "update_data_source",
                        "description": "The name of the tool to run."
                      },
                      "update_data_source": {
                        "type": "object",
                        "properties": {
                          "data_source_id": {
                            "type": "string",
                            "description": "The data source to update. Accepts a collection:// URI from <data-source> tags, a bare UUID, or a database ID (only if the database has a single data source)."
                          },
                          "statements": {
                            "type": "string",
                            "description": "Semicolon-separated SQL DDL statements to update the schema. Supports ADD COLUMN, DROP COLUMN, RENAME COLUMN, ALTER COLUMN SET."
                          },
                          "title": {
                            "type": "string",
                            "description": "The new title of the data source."
                          },
                          "description": {
                            "type": "string",
                            "description": "The new description of the data source."
                          },
                          "is_inline": {
                            "type": "boolean",
                            "description": "Whether the database should display inline (true) or as full page (false). Only applicable for single-source databases."
                          },
                          "in_trash": {
                            "type": "boolean",
                            "description": "Move data source to trash. Cannot be undone without Notion UI."
                          }
                        },
                        "required": [
                          "data_source_id"
                        ],
                        "description": "The parameters for the update_data_source tool. Update a Notion data source's schema, title, or attributes using SQL DDL statements.\nReturns Markdown showing updated structure and schema.\n\nAccepts a data source ID (collection ID from fetch response's <data-source> tag)\nor a single-source database ID. Multi-source databases require the specific\ndata source ID.\n\nThe statements param accepts semicolon-separated DDL statements:\n- ADD COLUMN \"Name\" <type> - add a new property\n- DROP COLUMN \"Name\" - remove a property\n- RENAME COLUMN \"Old\" TO \"New\" - rename a property\n- ALTER COLUMN \"Name\" SET <type> - change type/options\n\nSame type syntax as create_database. Key types:\n- SELECT('opt':color, ...) / MULTI_SELECT('opt':color, ...)\n- NUMBER [FORMAT 'dollar'] / FORMULA('expression')\n- RELATION('ds_id') / RELATION('ds_id', DUAL) / RELATION('ds_id', DUAL 'synced_name' 'synced_id')\n- ROLLUP('rel_prop', 'target_prop', 'function') / UNIQUE_ID [PREFIX 'X']\n- Simple: TITLE, RICH_TEXT, DATE, PEOPLE, CHECKBOX, URL, EMAIL, PHONE_NUMBER, STATUS, FILES\n\n<example description=\"Add properties\">{\"data_source_id\": \"f336d0bc-b841-465b-8045-024475c079dd\", \"statements\": \"ADD COLUMN \\\"Priority\\\" SELECT('High':red, 'Medium':yellow, 'Low':green); ADD COLUMN \\\"Due Date\\\" DATE\"}</example>\n<example description=\"Rename property\">{\"data_source_id\": \"f336d0bc-b841-465b-8045-024475c079dd\", \"statements\": \"RENAME COLUMN \\\"Status\\\" TO \\\"Project Status\\\"\"}</example>\n<example description=\"Remove property\">{\"data_source_id\": \"f336d0bc-b841-465b-8045-024475c079dd\", \"statements\": \"DROP COLUMN \\\"Old Property\\\"\"}</example>\n<example description=\"Add self-relation\">{\"data_source_id\": \"f336d0bc-b841-465b-8045-024475c079dd\", \"statements\": \"ADD COLUMN \\\"Parent\\\" RELATION('f336d0bc-b841-465b-8045-024475c079dd', DUAL 'Children' 'children'); ADD COLUMN \\\"Children\\\" RELATION('f336d0bc-b841-465b-8045-024475c079dd', DUAL 'Parent' 'parent')\"}</example>\n<example description=\"Update title\">{\"data_source_id\": \"f336d0bc-b841-465b-8045-024475c079dd\", \"title\": \"Project Tracker 2024\"}</example>\n<example description=\"Trash data source\">{\"data_source_id\": \"f336d0bc-b841-465b-8045-024475c079dd\", \"in_trash\": true}</example>\n\nNotes: Cannot delete/create title properties. Max one unique_id property.\nCannot update synced databases. Use \"fetch\" first to see current schema\nand get the data source ID from <data-source url=\"collection://...\"> tags."
                      }
                    },
                    "required": [
                      "type",
                      "update_data_source"
                    ],
                    "title": "Update Data Source"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "create_comment",
                        "description": "The name of the tool to run."
                      },
                      "create_comment": {
                        "type": "object",
                        "properties": {
                          "rich_text": {
                            "type": "array",
                            "items": {
                              "$ref": "#/components/schemas/richTextItemRequest"
                            },
                            "maxItems": 100,
                            "description": "An array of rich text objects that represent the content of the comment."
                          },
                          "page_id": {
                            "type": "string",
                            "description": "The ID of the page to comment on (with or without dashes)."
                          },
                          "discussion_id": {
                            "type": "string",
                            "description": "The ID or URL of an existing discussion to reply to (e.g., discussion://pageId/blockId/discussionId)."
                          },
                          "selection_with_ellipsis": {
                            "type": "string",
                            "description": "Unique start and end snippet of the content to comment on.\nDO NOT provide the entire string. Instead, provide up to the first ~10 characters, an ellipsis, and then up to the last ~10 characters.\nMake sure you provide enough of the start and end snippet to uniquely identify the content.\nFor example: \"# Section heading...last paragraph.\""
                          }
                        },
                        "required": [
                          "rich_text",
                          "page_id"
                        ],
                        "description": "The parameters for the create_comment tool. Add a comment to a page or specific content.\n\nCreates a new comment. Provide `page_id` to identify the page, then choose ONE targeting mode:\n- `page_id` alone: Page-level comment on the entire page\n- `page_id` + `selection_with_ellipsis`: Comment on specific block content\n- `discussion_id`: Reply to an existing discussion thread (page_id is still required)\n\nFor content targeting, use `selection_with_ellipsis` with ~10 chars from start and end: \"# Section Ti...tle content\"\n\n<example description=\"Page-level comment\">\n{\"page_id\": \"uuid\", \"rich_text\": [{\"text\": {\"content\": \"Comment\"}}]}\n</example>\n<example description=\"Comment on specific content\">\n{\"page_id\": \"uuid\", \"selection_with_ellipsis\": \"# Meeting No...es heading\",\n \"rich_text\": [{\"text\": {\"content\": \"Comment on this section\"}}]}\n</example>\n<example description=\"Reply to discussion\">\n{\"page_id\": \"uuid\", \"discussion_id\": \"discussion://pageId/blockId/discussionId\",\n \"rich_text\": [{\"text\": {\"content\": \"Reply\"}}]}\n</example>"
                      }
                    },
                    "required": [
                      "type",
                      "create_comment"
                    ],
                    "title": "Create Comment"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "get_comments",
                        "description": "The name of the tool to run."
                      },
                      "get_comments": {
                        "type": "object",
                        "properties": {
                          "page_id": {
                            "type": "string",
                            "description": "Identifier for a Notion page."
                          },
                          "include_resolved": {
                            "type": "boolean",
                            "description": "Include resolved discussions in the response. Defaults to false."
                          },
                          "include_all_blocks": {
                            "type": "boolean",
                            "description": "Include discussions on child blocks, not just page-level discussions. Defaults to false."
                          },
                          "discussion_id": {
                            "type": "string",
                            "description": "Fetch a specific discussion by ID or discussion URL (e.g., discussion://pageId/blockId/discussionId)."
                          }
                        },
                        "required": [
                          "page_id"
                        ],
                        "description": "The parameters for the get_comments tool. Get comments and discussions from a Notion page.\n\nReturns discussions with full comment content in XML format.\nBy default, returns page-level discussions only.\n\nTip: Use the `fetch` tool with `include_discussions: true` first to see where discussions\nare anchored in the page content, then use this tool to retrieve full discussion threads.\nThe `discussion://` URLs in the fetch output match the discussion IDs returned here.\n\nParameters:\n- `include_all_blocks`: Include discussions on child blocks (default: false)\n- `include_resolved`: Include resolved discussions (default: false)\n- `discussion_id`: Fetch a specific discussion by ID or URL\n\n<example>{\"page_id\": \"page-uuid\"}</example>\n<example>{\"page_id\": \"page-uuid\", \"include_all_blocks\": true}</example>\n<example>{\"page_id\": \"page-uuid\", \"discussion_id\": \"discussion://pageId/blockId/discussionId\"}</example>"
                      }
                    },
                    "required": [
                      "type",
                      "get_comments"
                    ],
                    "title": "Get Comments"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "get_teams",
                        "description": "The name of the tool to run."
                      },
                      "get_teams": {
                        "type": "object",
                        "properties": {
                          "query": {
                            "type": "string",
                            "minLength": 1,
                            "maxLength": 100,
                            "description": "Optional search query to filter teams by name (case-insensitive)."
                          }
                        },
                        "description": "The parameters for the get_teams tool. Retrieves a list of teams (teamspaces) in the current workspace. Shows which teams\nexist, user membership status, IDs, names, and roles.\n\nTeams are returned split by membership status and limited to a maximum of\n10 results.\n\n<examples>\n1. List all teams (up to the limit of each type): {}\n\n2. Search for teams by name: {\"query\": \"engineering\"}\n\n3. Find a specific team: {\"query\": \"Product Design\"}\n</examples>"
                      }
                    },
                    "required": [
                      "type",
                      "get_teams"
                    ],
                    "title": "Get Teams"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "get_users",
                        "description": "The name of the tool to run."
                      },
                      "get_users": {
                        "type": "object",
                        "properties": {
                          "query": {
                            "type": "string",
                            "minLength": 1,
                            "maxLength": 100,
                            "description": "Optional search query to filter users by name or email (case-insensitive)."
                          },
                          "start_cursor": {
                            "type": "string",
                            "minLength": 1,
                            "maxLength": 100,
                            "description": "Cursor for pagination. Use the next_cursor value from the previous response to get the next page."
                          },
                          "page_size": {
                            "type": "integer",
                            "minimum": 1,
                            "maximum": 100,
                            "description": "Number of users to return per page (default: 100, max: 100)."
                          },
                          "user_id": {
                            "type": "string",
                            "minLength": 1,
                            "maxLength": 100,
                            "description": "Return only the user matching this ID. Pass \"self\" to fetch the current user."
                          }
                        },
                        "description": "The parameters for the get_users tool. Retrieves a list of users in the current workspace. Shows workspace members\nand guests with their IDs, names, emails (if available), and types (person or bot).\n\nSupports cursor-based pagination to iterate through all users in the workspace.\n\n<examples>\n1. List all users (first page): {}\n\n2. Search for users by name or email: {\"query\": \"john\"}\n\n3. Get next page of results: {\"start_cursor\": \"abc123\"}\n\n4. Set custom page size: {\"page_size\": 20}\n\n5. Fetch a specific user by ID: {\"user_id\": \"00000000-0000-4000-8000-000000000000\"}\n\n6. Fetch the current user: {\"user_id\": \"self\"}\n</examples>"
                      }
                    },
                    "required": [
                      "type",
                      "get_users"
                    ],
                    "title": "Get Users"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "answer_question",
                        "description": "The name of the tool to run."
                      },
                      "answer_question": {
                        "type": "object",
                        "properties": {
                          "question": {
                            "type": "string",
                            "minLength": 1,
                            "maxLength": 2000,
                            "description": "Text containing a question about your Notion workspace content"
                          }
                        },
                        "required": [
                          "question"
                        ],
                        "description": "The parameters for the answer_question tool. Provides an AI-powered answer to questions about content in your Notion workspace.\nUses natural language understanding to find relevant information and synthesize a\ncomprehensive answer.\n\nUse when you need:\n- Direct answers to questions about workspace content\n- Synthesis of information from multiple sources\n- Natural language explanations of concepts or data\n\nMore focused than the search tool; provides one condensed answer, not a list of\nsearch results."
                      }
                    },
                    "required": [
                      "type",
                      "answer_question"
                    ],
                    "title": "Answer Question"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "query_data_sources",
                        "description": "The name of the tool to run."
                      },
                      "query_data_sources": {
                        "type": "object",
                        "properties": {
                          "data": {
                            "oneOf": [
                              {
                                "type": "object",
                                "properties": {
                                  "data_source_urls": {
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    },
                                    "maxItems": 100,
                                    "description": "Array of data source URLs to query. These are obtained from the fetch tool\nin the format: collection://f336d0bc-b841-465b-8045-024475c079dd"
                                  },
                                  "query": {
                                    "type": "string",
                                    "description": "SQLite query to execute against the data sources.\nUse the data source URL as the table name in your query.\nExample: SELECT * FROM \"collection://...\" WHERE ..."
                                  },
                                  "mode": {
                                    "type": "string",
                                    "const": "sql",
                                    "description": "Optional mode parameter. Defaults to 'sql' if not specified."
                                  },
                                  "params": {
                                    "type": "array",
                                    "items": {
                                      "type": "string"
                                    },
                                    "maxItems": 100,
                                    "description": "Optional array of parameter values for parameterized queries.\nFor example, if query contains WHERE status = ?, provide the value here.\nUse \"__YES__\" for checked checkboxes and \"__NO__\" for unchecked checkboxes."
                                  }
                                },
                                "required": [
                                  "data_source_urls",
                                  "query"
                                ],
                                "title": "Sql"
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "mode": {
                                    "type": "string",
                                    "const": "view",
                                    "description": "Mode for executing a database view's existing query"
                                  },
                                  "view_url": {
                                    "type": "string",
                                    "description": "URL of a specific database view to query.\nExample: https://www.notion.so/workspace/db-id?v=view-id"
                                  }
                                },
                                "required": [
                                  "mode",
                                  "view_url"
                                ],
                                "title": "View"
                              }
                            ],
                            "description": "The data required for querying data sources"
                          }
                        },
                        "required": [
                          "data"
                        ],
                        "description": "The parameters for the query_data_sources tool. Query data from Notion databases using SQL or by specifying a view.\n\nBy default, uses SQL mode to execute SQLite queries across one or more data sources.\nAlternatively, use view mode to execute a database view's existing filters and sorts.\n\nPrerequisites:\n1. Use the \"fetch\" tool first to get database schema and data source URLs\n2. Data source URLs are found in <data-source url=\"...\"> tags in fetch results\n\nSQL mode (default):\nExecute custom SQLite queries across one or more data sources.\n- Use data source URLs as table names in your query\n- Supports parameterized queries for security\n- Checkbox values: use \"__YES__\" for checked, \"__NO__\" for unchecked\n\nExamples:\n1. Simple query without explicit mode (defaults to SQL):\n{\n  \"data\": {\n    \"data_source_urls\": [\"collection://f336d0bc-b841-465b-8045-024475c079dd\"],\n    \"query\": \"SELECT * FROM \\\"collection://f336d0bc-b841-465b-8045-024475c079dd\\\" LIMIT 10\"\n  }\n}\n\n2. Query with parameters:\n{\n  \"data\": {\n    \"mode\": \"sql\",\n    \"data_source_urls\": [\"collection://abc123\"],\n    \"query\": \"SELECT * FROM \\\"collection://abc123\\\" WHERE Status = ? AND Priority = ?\",\n    \"params\": [\"In Progress\", \"High\"]\n  }\n}\n\n3. Query checkboxes:\n{\n  \"data\": {\n    \"data_source_urls\": [\"collection://def456\"],\n    \"query\": \"SELECT * FROM \\\"collection://def456\\\" WHERE Completed = ?\",\n    \"params\": [\"__YES__\"]\n  }\n}\n\nView mode:\nExecute a specific database view's query with its filters and sorts.\n\nExample:\n{\n  \"data\": {\n    \"mode\": \"view\",\n    \"view_url\": \"https://www.notion.so/workspace/Tasks-DB-abc123?v=def456\"\n  }\n}\n\nCommon use cases:\n- Aggregate data across databases\n- Filter records by complex conditions\n- Export data for analysis\n- Validate data quality\n- Generate reports from database content"
                      }
                    },
                    "required": [
                      "type",
                      "query_data_sources"
                    ],
                    "title": "Query Data Sources"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "query_database_view",
                        "description": "The name of the tool to run."
                      },
                      "query_database_view": {
                        "type": "object",
                        "properties": {
                          "view_url": {
                            "type": "string",
                            "description": "URL of a specific database view to query.\nExample: https://www.notion.so/workspace/db-id?v=view-id"
                          }
                        },
                        "required": [
                          "view_url"
                        ],
                        "description": "The parameters for the query_database_view tool. Query data from a Notion database view.\n\nExecutes a database view's existing filters, sorts, and column selections to return matching pages.\n\nPrerequisites:\n1. Use the \"fetch\" tool first to get the database and its view URLs\n2. View URLs are found in database responses, typically in the format:\n   https://www.notion.so/workspace/db-id?v=view-id\n\nExample:\n{\n  \"view_url\": \"https://www.notion.so/workspace/Tasks-DB-abc123?v=def456\"\n}\n\nCommon use cases:\n- Query databases using pre-defined views (filters/sorts already configured), e.g. look for all tickets marked \"In Progress\" in a Tasks DB\n- Export filtered data for analysis\n- Generate reports from database content"
                      }
                    },
                    "required": [
                      "type",
                      "query_database_view"
                    ],
                    "title": "Query Database View"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "query_meeting_notes",
                        "description": "The name of the tool to run."
                      },
                      "query_meeting_notes": {
                        "type": "object",
                        "properties": {
                          "filter": {
                            "type": "object",
                            "properties": {
                              "operator": {
                                "type": "string",
                                "enum": [
                                  "and",
                                  "or"
                                ],
                                "description": "Operator for combinator filters."
                              },
                              "filters": {
                                "type": "array",
                                "items": {
                                  "description": "Meeting notes filter node (combinator or property filter).",
                                  "anyOf": [
                                    {
                                      "type": "object",
                                      "properties": {
                                        "operator": {
                                          "type": "string",
                                          "enum": [
                                            "and",
                                            "or"
                                          ],
                                          "description": "Operator for nested combinator filters."
                                        },
                                        "filters": {
                                          "type": "array",
                                          "items": {
                                            "anyOf": [
                                              {
                                                "type": "object",
                                                "properties": {
                                                  "property": {
                                                    "type": "string",
                                                    "description": "Property name."
                                                  },
                                                  "filter": {
                                                    "type": "object",
                                                    "properties": {
                                                      "operator": {
                                                        "type": "string",
                                                        "description": "Operator."
                                                      },
                                                      "value": {
                                                        "description": "Value for the operator.",
                                                        "anyOf": [
                                                          {
                                                            "type": "object",
                                                            "description": "Single date/datetime filter value.",
                                                            "properties": {
                                                              "type": {
                                                                "type": "string",
                                                                "enum": [
                                                                  "relative",
                                                                  "exact"
                                                                ]
                                                              },
                                                              "value": {
                                                                "anyOf": [
                                                                  {
                                                                    "type": "string"
                                                                  },
                                                                  {
                                                                    "type": "object",
                                                                    "properties": {
                                                                      "type": {
                                                                        "type": "string",
                                                                        "enum": [
                                                                          "date",
                                                                          "datetime"
                                                                        ]
                                                                      },
                                                                      "start_date": {
                                                                        "type": "string"
                                                                      },
                                                                      "start_time": {
                                                                        "type": "string"
                                                                      },
                                                                      "time_zone": {
                                                                        "type": "string"
                                                                      }
                                                                    },
                                                                    "required": [
                                                                      "type",
                                                                      "start_date"
                                                                    ]
                                                                  }
                                                                ]
                                                              }
                                                            },
                                                            "required": [
                                                              "type",
                                                              "value"
                                                            ]
                                                          },
                                                          {
                                                            "type": "object",
                                                            "description": "Date range filter value.",
                                                            "properties": {
                                                              "type": {
                                                                "type": "string",
                                                                "enum": [
                                                                  "relative",
                                                                  "exact"
                                                                ]
                                                              },
                                                              "value": {
                                                                "anyOf": [
                                                                  {
                                                                    "type": "string"
                                                                  },
                                                                  {
                                                                    "type": "object",
                                                                    "properties": {
                                                                      "type": {
                                                                        "type": "string",
                                                                        "enum": [
                                                                          "daterange"
                                                                        ]
                                                                      },
                                                                      "start_date": {
                                                                        "type": "string"
                                                                      },
                                                                      "end_date": {
                                                                        "type": "string"
                                                                      }
                                                                    },
                                                                    "required": [
                                                                      "type",
                                                                      "start_date"
                                                                    ]
                                                                  }
                                                                ]
                                                              },
                                                              "direction": {
                                                                "type": "string",
                                                                "enum": [
                                                                  "past",
                                                                  "future"
                                                                ]
                                                              },
                                                              "unit": {
                                                                "type": "string",
                                                                "enum": [
                                                                  "day",
                                                                  "week",
                                                                  "month",
                                                                  "year"
                                                                ]
                                                              },
                                                              "count": {
                                                                "type": "number"
                                                              }
                                                            },
                                                            "required": [
                                                              "type",
                                                              "value"
                                                            ]
                                                          },
                                                          {
                                                            "type": "object",
                                                            "description": "Text filter value for string_contains and similar operators.",
                                                            "properties": {
                                                              "type": {
                                                                "type": "string",
                                                                "enum": [
                                                                  "exact"
                                                                ]
                                                              },
                                                              "value": {
                                                                "type": "string",
                                                                "description": "The text value to filter on."
                                                              }
                                                            },
                                                            "required": [
                                                              "type",
                                                              "value"
                                                            ]
                                                          },
                                                          {
                                                            "type": "array",
                                                            "description": "Array of person references for person_contains/person_does_not_contain filters.",
                                                            "items": {
                                                              "type": "object",
                                                              "properties": {
                                                                "type": {
                                                                  "type": "string",
                                                                  "enum": [
                                                                    "exact"
                                                                  ]
                                                                },
                                                                "value": {
                                                                  "type": "object",
                                                                  "properties": {
                                                                    "table": {
                                                                      "type": "string",
                                                                      "enum": [
                                                                        "notion_user"
                                                                      ]
                                                                    },
                                                                    "id": {
                                                                      "type": "string"
                                                                    }
                                                                  },
                                                                  "required": [
                                                                    "table",
                                                                    "id"
                                                                  ]
                                                                }
                                                              },
                                                              "required": [
                                                                "type",
                                                                "value"
                                                              ]
                                                            }
                                                          }
                                                        ]
                                                      }
                                                    },
                                                    "required": [
                                                      "operator"
                                                    ]
                                                  }
                                                },
                                                "required": [
                                                  "property",
                                                  "filter"
                                                ]
                                              },
                                              {
                                                "type": "object",
                                                "properties": {
                                                  "operator": {
                                                    "type": "string",
                                                    "enum": [
                                                      "and",
                                                      "or"
                                                    ],
                                                    "description": "Operator for nested combinator filters."
                                                  },
                                                  "filters": {
                                                    "type": "array",
                                                    "items": {
                                                      "anyOf": [
                                                        {
                                                          "type": "object",
                                                          "properties": {
                                                            "property": {
                                                              "type": "string",
                                                              "description": "Property name."
                                                            },
                                                            "filter": {
                                                              "type": "object",
                                                              "properties": {
                                                                "operator": {
                                                                  "type": "string",
                                                                  "description": "Operator."
                                                                },
                                                                "value": {
                                                                  "description": "Value for the operator.",
                                                                  "anyOf": [
                                                                    {
                                                                      "type": "object",
                                                                      "description": "Single date/datetime filter value.",
                                                                      "properties": {
                                                                        "type": {
                                                                          "type": "string",
                                                                          "enum": [
                                                                            "relative",
                                                                            "exact"
                                                                          ]
                                                                        },
                                                                        "value": {
                                                                          "anyOf": [
                                                                            {
                                                                              "type": "string"
                                                                            },
                                                                            {
                                                                              "type": "object",
                                                                              "properties": {
                                                                                "type": {
                                                                                  "type": "string",
                                                                                  "enum": [
                                                                                    "date",
                                                                                    "datetime"
                                                                                  ]
                                                                                },
                                                                                "start_date": {
                                                                                  "type": "string"
                                                                                },
                                                                                "start_time": {
                                                                                  "type": "string"
                                                                                },
                                                                                "time_zone": {
                                                                                  "type": "string"
                                                                                }
                                                                              },
                                                                              "required": [
                                                                                "type",
                                                                                "start_date"
                                                                              ]
                                                                            }
                                                                          ]
                                                                        }
                                                                      },
                                                                      "required": [
                                                                        "type",
                                                                        "value"
                                                                      ]
                                                                    },
                                                                    {
                                                                      "type": "object",
                                                                      "description": "Date range filter value.",
                                                                      "properties": {
                                                                        "type": {
                                                                          "type": "string",
                                                                          "enum": [
                                                                            "relative",
                                                                            "exact"
                                                                          ]
                                                                        },
                                                                        "value": {
                                                                          "anyOf": [
                                                                            {
                                                                              "type": "string"
                                                                            },
                                                                            {
                                                                              "type": "object",
                                                                              "properties": {
                                                                                "type": {
                                                                                  "type": "string",
                                                                                  "enum": [
                                                                                    "daterange"
                                                                                  ]
                                                                                },
                                                                                "start_date": {
                                                                                  "type": "string"
                                                                                },
                                                                                "end_date": {
                                                                                  "type": "string"
                                                                                }
                                                                              },
                                                                              "required": [
                                                                                "type",
                                                                                "start_date"
                                                                              ]
                                                                            }
                                                                          ]
                                                                        },
                                                                        "direction": {
                                                                          "type": "string",
                                                                          "enum": [
                                                                            "past",
                                                                            "future"
                                                                          ]
                                                                        },
                                                                        "unit": {
                                                                          "type": "string",
                                                                          "enum": [
                                                                            "day",
                                                                            "week",
                                                                            "month",
                                                                            "year"
                                                                          ]
                                                                        },
                                                                        "count": {
                                                                          "type": "number"
                                                                        }
                                                                      },
                                                                      "required": [
                                                                        "type",
                                                                        "value"
                                                                      ]
                                                                    },
                                                                    {
                                                                      "type": "object",
                                                                      "description": "Text filter value for string_contains and similar operators.",
                                                                      "properties": {
                                                                        "type": {
                                                                          "type": "string",
                                                                          "enum": [
                                                                            "exact"
                                                                          ]
                                                                        },
                                                                        "value": {
                                                                          "type": "string",
                                                                          "description": "The text value to filter on."
                                                                        }
                                                                      },
                                                                      "required": [
                                                                        "type",
                                                                        "value"
                                                                      ]
                                                                    },
                                                                    {
                                                                      "type": "array",
                                                                      "description": "Array of person references for person_contains/person_does_not_contain filters.",
                                                                      "items": {
                                                                        "type": "object",
                                                                        "properties": {
                                                                          "type": {
                                                                            "type": "string",
                                                                            "enum": [
                                                                              "exact"
                                                                            ]
                                                                          },
                                                                          "value": {
                                                                            "type": "object",
                                                                            "properties": {
                                                                              "table": {
                                                                                "type": "string",
                                                                                "enum": [
                                                                                  "notion_user"
                                                                                ]
                                                                              },
                                                                              "id": {
                                                                                "type": "string"
                                                                              }
                                                                            },
                                                                            "required": [
                                                                              "table",
                                                                              "id"
                                                                            ]
                                                                          }
                                                                        },
                                                                        "required": [
                                                                          "type",
                                                                          "value"
                                                                        ]
                                                                      }
                                                                    }
                                                                  ]
                                                                }
                                                              },
                                                              "required": [
                                                                "operator"
                                                              ]
                                                            }
                                                          },
                                                          "required": [
                                                            "property",
                                                            "filter"
                                                          ]
                                                        }
                                                      ]
                                                    }
                                                  }
                                                },
                                                "required": [
                                                  "operator",
                                                  "filters"
                                                ]
                                              }
                                            ]
                                          },
                                          "description": "Nested filters for combinator filters."
                                        }
                                      },
                                      "required": [
                                        "operator",
                                        "filters"
                                      ]
                                    },
                                    {
                                      "type": "object",
                                      "properties": {
                                        "property": {
                                          "type": "string",
                                          "description": "Property name."
                                        },
                                        "filter": {
                                          "type": "object",
                                          "properties": {
                                            "operator": {
                                              "type": "string",
                                              "description": "Operator."
                                            },
                                            "value": {
                                              "description": "Value for the operator.",
                                              "anyOf": [
                                                {
                                                  "type": "object",
                                                  "description": "Single date/datetime filter value.",
                                                  "properties": {
                                                    "type": {
                                                      "type": "string",
                                                      "enum": [
                                                        "relative",
                                                        "exact"
                                                      ]
                                                    },
                                                    "value": {
                                                      "anyOf": [
                                                        {
                                                          "type": "string"
                                                        },
                                                        {
                                                          "type": "object",
                                                          "properties": {
                                                            "type": {
                                                              "type": "string",
                                                              "enum": [
                                                                "date",
                                                                "datetime"
                                                              ]
                                                            },
                                                            "start_date": {
                                                              "type": "string"
                                                            },
                                                            "start_time": {
                                                              "type": "string"
                                                            },
                                                            "time_zone": {
                                                              "type": "string"
                                                            }
                                                          },
                                                          "required": [
                                                            "type",
                                                            "start_date"
                                                          ]
                                                        }
                                                      ]
                                                    }
                                                  },
                                                  "required": [
                                                    "type",
                                                    "value"
                                                  ]
                                                },
                                                {
                                                  "type": "object",
                                                  "description": "Date range filter value.",
                                                  "properties": {
                                                    "type": {
                                                      "type": "string",
                                                      "enum": [
                                                        "relative",
                                                        "exact"
                                                      ]
                                                    },
                                                    "value": {
                                                      "anyOf": [
                                                        {
                                                          "type": "string"
                                                        },
                                                        {
                                                          "type": "object",
                                                          "properties": {
                                                            "type": {
                                                              "type": "string",
                                                              "enum": [
                                                                "daterange"
                                                              ]
                                                            },
                                                            "start_date": {
                                                              "type": "string"
                                                            },
                                                            "end_date": {
                                                              "type": "string"
                                                            }
                                                          },
                                                          "required": [
                                                            "type",
                                                            "start_date"
                                                          ]
                                                        }
                                                      ]
                                                    },
                                                    "direction": {
                                                      "type": "string",
                                                      "enum": [
                                                        "past",
                                                        "future"
                                                      ]
                                                    },
                                                    "unit": {
                                                      "type": "string",
                                                      "enum": [
                                                        "day",
                                                        "week",
                                                        "month",
                                                        "year"
                                                      ]
                                                    },
                                                    "count": {
                                                      "type": "number"
                                                    }
                                                  },
                                                  "required": [
                                                    "type",
                                                    "value"
                                                  ]
                                                },
                                                {
                                                  "type": "object",
                                                  "description": "Text filter value for string_contains and similar operators.",
                                                  "properties": {
                                                    "type": {
                                                      "type": "string",
                                                      "enum": [
                                                        "exact"
                                                      ]
                                                    },
                                                    "value": {
                                                      "type": "string",
                                                      "description": "The text value to filter on."
                                                    }
                                                  },
                                                  "required": [
                                                    "type",
                                                    "value"
                                                  ]
                                                },
                                                {
                                                  "type": "array",
                                                  "description": "Array of person references for person_contains/person_does_not_contain filters.",
                                                  "items": {
                                                    "type": "object",
                                                    "properties": {
                                                      "type": {
                                                        "type": "string",
                                                        "enum": [
                                                          "exact"
                                                        ]
                                                      },
                                                      "value": {
                                                        "type": "object",
                                                        "properties": {
                                                          "table": {
                                                            "type": "string",
                                                            "enum": [
                                                              "notion_user"
                                                            ]
                                                          },
                                                          "id": {
                                                            "type": "string"
                                                          }
                                                        },
                                                        "required": [
                                                          "table",
                                                          "id"
                                                        ]
                                                      }
                                                    },
                                                    "required": [
                                                      "type",
                                                      "value"
                                                    ]
                                                  }
                                                }
                                              ]
                                            }
                                          },
                                          "required": [
                                            "operator"
                                          ]
                                        }
                                      },
                                      "required": [
                                        "property",
                                        "filter"
                                      ]
                                    }
                                  ]
                                },
                                "maxItems": 100,
                                "description": "Nested filters; each may be a combinator (and/or) or property filter."
                              }
                            },
                            "required": [
                              "operator"
                            ],
                            "description": "Acceptable filter for querying current user's meeting notes data source."
                          }
                        },
                        "description": "The parameters for the query_meeting_notes tool. Query the current user's meeting notes data source.\n\nApplies a filter over meeting note properties. Title keyword searching is done via filter on property \"title\" (e.g. string_contains).\nTitle keyword matching is case-insensitive; capitalization does not matter.\nReturns up to 50 rows of matching meeting notes.\n\nPrerequisites:\n1. Use the \"search\" tool to find people IDs if you need to filter by attendees\n\nQuery building:\n- Ignore terms semantically related to meeting outputs (e.g. \"summaries\", \"notes\", \"todos\", \"action items\", \"deliverables\"). These signal the user wants outcomes from their meetings, not a title filter.\n- For example, \"what are my meeting todos?\" means filter meetings and find action items — do NOT add a title filter for \"todos\".\n- Only add a title filter when confident the user is targeting a specific meeting title (e.g. \"standup\", \"sprint planning\", \"1:1 with Alice\").\n- Generic date phrases like \"recent meetings\", \"latest meetings\", \"meetings this week\", or \"yesterday's meetings\" should be interpreted as date range filters — never as title filters.\n- If a filter returns no results, simplify to a single term. The system is lexical, so multi-word title filters may not match.\n- Unless a user explicitly asks about a meeting titled with another user's name, assume they're referring to attendees or creators. Only add a title filter with a person's name as a fallback if attendee filtering returns no results.\n\nDefault behavior:\n- This tool by default returns meeting notes where the current user is an attendee or creator. There is no need to add a filter for the current user.\n\nFilterable properties:\n- \"title\" (text) — meeting title\n- \"notion://meeting_notes/attendees\" (person) — meeting attendees\n- \"created_time\" (date) — when the meeting note was created\n- \"created_by\" (person) — who created the meeting note\n- \"last_edited_time\" (date) — when the meeting note was last edited\n- \"last_edited_by\" (person) — who last edited the meeting note\n\nCombinator filters use \"filters\" (not \"operands\"):\n{\n  \"operator\": \"and\" | \"or\",\n  \"filters\": [ ... ]\n}\n\nDate filtering (recommended default: date_is_within):\n- Prefer \"date_is_within\" for relative windows like \"past N days/weeks/months\".\n- Relative (common): { type: \"relative\", value: \"the_past_week\" | \"the_past_month\" | \"this_week\" }\n- Relative (custom): { type: \"relative\", value: \"custom\", direction: \"past\" | \"future\", unit: \"day\" | \"week\" | \"month\" | \"year\", count: <number> }\n- Exact range: { type: \"exact\", value: { type: \"daterange\", start_date: \"YYYY-MM-DD\", end_date: \"YYYY-MM-DD\" } }\n- Single-date operators (\"date_is\", \"date_is_before\", \"date_is_after\", \"date_is_on_or_before\", \"date_is_on_or_after\"):\n  - Exact: { type: \"exact\", value: { type: \"date\", start_date: \"YYYY-MM-DD\" } }\n  - Relative shortcuts: today | tomorrow | yesterday | one_week_ago | one_week_from_now | one_month_ago | one_month_from_now\n\nTitle keyword filtering (OR vs AND):\n- Use OR (\"operator\": \"or\") when unsure or for broad discovery.\n- Use AND (\"operator\": \"and\") when the user is specific and you want to narrow results.\n- Break multi-word phrases into individual terms and filter on each term separately.\n\nExample 1: Filter meetings from the past week (relative):\n{\n  \"filter\": {\n    \"operator\": \"and\",\n    \"filters\": [\n      {\n        \"property\": \"created_time\",\n        \"filter\": {\n          \"operator\": \"date_is_within\",\n          \"value\": { \"type\": \"relative\", \"value\": \"the_past_week\" }\n        }\n      }\n    ]\n  }\n}\n\nExample 2: Filter meetings from the past 3 days (custom relative):\n{\n  \"filter\": {\n    \"operator\": \"and\",\n    \"filters\": [\n      {\n        \"property\": \"created_time\",\n        \"filter\": {\n          \"operator\": \"date_is_within\",\n          \"value\": { \"type\": \"relative\", \"value\": \"custom\", \"direction\": \"past\", \"unit\": \"day\", \"count\": 3 }\n        }\n      }\n    ]\n  }\n}\n\nExample 3: Filter meetings by exact date range:\n{\n  \"filter\": {\n    \"operator\": \"and\",\n    \"filters\": [\n      {\n        \"property\": \"created_time\",\n        \"filter\": {\n          \"operator\": \"date_is_within\",\n          \"value\": { \"type\": \"exact\", \"value\": { \"type\": \"daterange\", \"start_date\": \"2025-01-01\", \"end_date\": \"2025-12-31\" } }\n        }\n      }\n    ]\n  }\n}\n\nExample 4: Filter meetings created after a specific date:\n{\n  \"filter\": {\n    \"operator\": \"and\",\n    \"filters\": [\n      {\n        \"property\": \"created_time\",\n        \"filter\": {\n          \"operator\": \"date_is_after\",\n          \"value\": { \"type\": \"exact\", \"value\": { \"type\": \"date\", \"start_date\": \"2025-06-01\" } }\n        }\n      }\n    ]\n  }\n}\n\nExample 5: Filter meetings by a specific attendee (use \"search\" tool first to get user ID):\n{\n  \"filter\": {\n    \"operator\": \"and\",\n    \"filters\": [\n      {\n        \"property\": \"notion://meeting_notes/attendees\",\n        \"filter\": {\n          \"operator\": \"person_contains\",\n          \"value\": [\n            { \"type\": \"exact\", \"value\": { \"table\": \"notion_user\", \"id\": \"a1b2c3d4-e5f6-7890-abcd-ef1234567890\" } }\n          ]\n        }\n      }\n    ]\n  }\n}\n\nExample 6: Combine attendees with date range:\n{\n  \"filter\": {\n    \"operator\": \"and\",\n    \"filters\": [\n      {\n        \"property\": \"created_time\",\n        \"filter\": {\n          \"operator\": \"date_is_on_or_after\",\n          \"value\": { \"type\": \"exact\", \"value\": { \"type\": \"date\", \"start_date\": \"2025-01-01\" } }\n        }\n      },\n      {\n        \"property\": \"created_time\",\n        \"filter\": {\n          \"operator\": \"date_is_on_or_before\",\n          \"value\": { \"type\": \"exact\", \"value\": { \"type\": \"date\", \"start_date\": \"2025-01-31\" } }\n        }\n      },\n      {\n        \"property\": \"notion://meeting_notes/attendees\",\n        \"filter\": {\n          \"operator\": \"person_contains\",\n          \"value\": [\n            { \"type\": \"exact\", \"value\": { \"table\": \"notion_user\", \"id\": \"a1b2c3d4-e5f6-7890-abcd-ef1234567890\" } }\n          ]\n        }\n      }\n    ]\n  }\n}\n\nExample 7: Filter meetings by title content:\n{\n  \"filter\": {\n    \"operator\": \"and\",\n    \"filters\": [\n      {\n        \"property\": \"title\",\n        \"filter\": {\n          \"operator\": \"string_contains\",\n          \"value\": { \"type\": \"exact\", \"value\": \"design review\" }\n        }\n      }\n    ]\n  }\n}\n\nExample 8: Filter meetings matching any of several title terms (using \"or\"):\n{\n  \"filter\": {\n    \"operator\": \"or\",\n    \"filters\": [\n      {\n        \"property\": \"title\",\n        \"filter\": {\n          \"operator\": \"string_contains\",\n          \"value\": { \"type\": \"exact\", \"value\": \"standup\" }\n        }\n      },\n      {\n        \"property\": \"title\",\n        \"filter\": {\n          \"operator\": \"string_contains\",\n          \"value\": { \"type\": \"exact\", \"value\": \"sync\" }\n        }\n      }\n    ]\n  }\n}"
                      }
                    },
                    "required": [
                      "type",
                      "query_meeting_notes"
                    ],
                    "title": "Query Meeting Notes"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "list_agents",
                        "description": "The name of the tool to run."
                      },
                      "list_agents": {
                        "type": "object",
                        "properties": {
                          "query": {
                            "type": "string",
                            "minLength": 1,
                            "maxLength": 100,
                            "description": "Optional search query to filter agents by name or description (case-insensitive)."
                          }
                        },
                        "description": "The parameters for the list_agents tool. Retrieves a list of all custom agents (workflows) that the authenticated user has access to in the current workspace.\nThis tool provides visibility into available agents including their names, IDs, descriptions, and system instructions.\n\nThe returned data includes:\n- Agent ID (for use with the chat tool)\n- Agent name\n- Agent description\n- Agent system instructions\n\n<examples>\n1. List all available agents: {}\n\n2. Search for agents by name or description: {\"query\": \"customer support\"}\n\n3. Find agents related to a specific topic: {\"query\": \"data analysis\"}\n</examples>"
                      }
                    },
                    "required": [
                      "type",
                      "list_agents"
                    ],
                    "title": "List Agents"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "chat",
                        "description": "The name of the tool to run."
                      },
                      "chat": {
                        "type": "object",
                        "properties": {
                          "agent_id": {
                            "type": "string",
                            "minLength": 1,
                            "description": "The unique identifier of the custom agent to chat with. This should be the\nagent ID of the custom agent you want to interact with. The agent must\nbe accessible to your workspace and have appropriate permissions.\n\nSupports both UUID formats:\n- With dashes: \"12345678-1234-1234-1234-123456789012\"\n- Without dashes: \"12345678123412341234123456789012\""
                          },
                          "message": {
                            "type": "string",
                            "minLength": 1,
                            "description": "The message to send to the custom agent. This will be processed by the agent\nbased on its configuration, available tools, and conversation context. The\nagent can understand natural language and perform various tasks based on your request."
                          },
                          "session_id": {
                            "type": "string",
                            "description": "Optional session ID to continue an existing conversation. If provided, the\nagent will have access to the previous conversation context and can maintain\ncontinuity across multiple interactions."
                          },
                          "include_transcript": {
                            "type": "boolean",
                            "description": "Whether to include the conversation transcript in the response. Defaults to false.\nWhen true, the response will include the full conversation history for context."
                          },
                          "thread_id": {
                            "type": "string",
                            "description": "Optional thread ID to use for the conversation. If not provided, a new thread\nwill be created. This allows you to reference specific conversation threads\nor continue existing ones."
                          },
                          "sync": {
                            "type": "boolean",
                            "description": "Whether to run the chat in sync mode. Defaults to false (async mode).\nWhen true, the response waits for the agent to complete processing and returns\nthe full response. When false (default), the response is returned immediately\nwith a chat_url and a generic acknowledgement message. The agent processes the\nrequest in the background, and users can continue the conversation from the chat_url."
                          }
                        },
                        "required": [
                          "agent_id",
                          "message"
                        ],
                        "description": "The parameters for the chat tool. Chat with a custom agent using Notion's AI chat system.\n\t\t\n\t\tThis tool provides a conversational interface to interact with custom agents\n\t\tthat can understand context, access Notion data, and perform various tasks.\n\t\tThe agent will process your message and respond based on its configuration,\n\t\tcapabilities, and the conversation context.\n\t\t\n\t\tKey features:\n\t\t- Start new conversations or continue existing ones\n\t\t- Access to Notion workspace data and connected sources\n\t\t- Support for tool use and complex reasoning\n\t\t- Optional conversation history inclusion\n\t\t\n\t\tCRITICAL: The response includes a 'chat_url' field. You MUST ALWAYS render this URL \n\t\tto the user immediately after receiving the response, formatted as a clickable link. \n\t\tThis allows them to continue the conversation directly in Notion's interface.\n\t\t\n\t\tExample format:\n\t\t**Continue the conversation in Notion:** [Chat with Agent](chat_url)\n\t\t\n\t\tExamples:\n\t\t1. Start new conversation:\n\t\t{\n\t\t\t\"agent_id\": \"agent_12345678-1234-1234-1234-123456789012\",\n\t\t\t\"message\": \"Help me create a project plan for our Q4 goals\"\n\t\t}\n\t\t\n\t\t2. Continue existing conversation:\n\t\t{\n\t\t\t\"agent_id\": \"agent_12345678-1234-1234-1234-123456789012\",\n\t\t\t\"message\": \"Can you add a timeline section to that plan?\",\n\t\t\t\"session_id\": \"session_87654321-4321-4321-4321-210987654321\"\n\t\t}\n\t\t\n\t\t3. Include full conversation history:\n\t\t{\n\t\t\t\"agent_id\": \"agent_12345678-1234-1234-1234-123456789012\",\n\t\t\t\"message\": \"Summarize our discussion\",\n\t\t\t\"include_transcript\": true\n\t\t}\n\t\t\n\t\t4. Use sync mode (waits for completion):\n\t\t{\n\t\t\t\"agent_id\": \"agent_12345678-1234-1234-1234-123456789012\",\n\t\t\t\"message\": \"Analyze all our project documents\",\n\t\t\t\"sync\": true\n\t\t}"
                      }
                    },
                    "required": [
                      "type",
                      "chat"
                    ],
                    "title": "Chat"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "create_view",
                        "description": "The name of the tool to run."
                      },
                      "create_view": {
                        "type": "object",
                        "properties": {
                          "database_id": {
                            "type": "string",
                            "description": "The database to create a view in. Accepts a Notion URL or a bare UUID."
                          },
                          "data_source_id": {
                            "type": "string",
                            "description": "The data source (collection) ID. Accepts a collection:// URI from <data-source> tags or a bare UUID."
                          },
                          "name": {
                            "type": "string",
                            "description": "The name of the view."
                          },
                          "type": {
                            "type": "string",
                            "enum": [
                              "table",
                              "board",
                              "list",
                              "calendar",
                              "timeline",
                              "gallery",
                              "form",
                              "chart",
                              "map",
                              "dashboard"
                            ],
                            "description": "The type of view to create."
                          },
                          "configure": {
                            "type": "string",
                            "description": "View configuration DSL string. Supports FILTER, SORT BY, GROUP BY, CALENDAR BY, TIMELINE BY, MAP BY, CHART, FORM, SHOW, HIDE, COVER, WRAP CELLS, and FREEZE COLUMNS directives. See notion://docs/view-dsl-spec."
                          }
                        },
                        "required": [
                          "database_id",
                          "data_source_id",
                          "name",
                          "type"
                        ],
                        "description": "The parameters for the create_view tool. Create a new view on a Notion database.\n\nUse \"fetch\" first to get the database_id and data_source_id\n(from <data-source> tags in the response).\n\nSupported types: table, board, list, calendar, timeline, gallery, form, chart, map, dashboard.\n\nThe optional \"configure\" param accepts a DSL for filters, sorts, grouping,\nand display options. See the notion://docs/view-dsl-spec resource for full\nsyntax. Key directives:\n- FILTER \"Property\" = \"value\" — filter rows\n- SORT BY \"Property\" ASC — sort rows\n- GROUP BY \"Property\" — group by property (required for board views)\n- CALENDAR BY \"Property\" — date property (required for calendar views)\n- TIMELINE BY \"Start\" TO \"End\" — date range (required for timeline views)\n- MAP BY \"Property\" — location property (required for map views)\n- CHART column|bar|line|donut|number — chart type with optional AGGREGATE, COLOR, HEIGHT, SORT, STACK BY, CAPTION\n- FORM CLOSE|OPEN — close/open form submissions\n- FORM ANONYMOUS true|false — toggle anonymous submissions\n- FORM PERMISSIONS none|reader|editor — set submission permissions\n- SHOW \"Prop1\", \"Prop2\" — set visible properties\n- COVER \"Property\" — cover image property\n\n<example description=\"Table view\">{\"database_id\": \"abc123\", \"data_source_id\": \"def456\", \"name\": \"All Tasks\", \"type\": \"table\"}</example>\n<example description=\"Board grouped by Status\">{\"database_id\": \"abc123\", \"data_source_id\": \"def456\", \"name\": \"Task Board\", \"type\": \"board\", \"configure\": \"GROUP BY \\\"Status\\\"\"}</example>\n<example description=\"Filtered + sorted table\">{\"database_id\": \"abc123\", \"data_source_id\": \"def456\", \"name\": \"Active\", \"type\": \"table\", \"configure\": \"FILTER \\\"Status\\\" = \\\"In Progress\\\"; SORT BY \\\"Due Date\\\" ASC\"}</example>\n<example description=\"Calendar view\">{\"database_id\": \"abc123\", \"data_source_id\": \"def456\", \"name\": \"Calendar\", \"type\": \"calendar\", \"configure\": \"CALENDAR BY \\\"Due Date\\\"\"}</example>\n<example description=\"Dashboard\">{\"database_id\": \"abc123\", \"data_source_id\": \"def456\", \"name\": \"Overview\", \"type\": \"dashboard\"}</example>"
                      }
                    },
                    "required": [
                      "type",
                      "create_view"
                    ],
                    "title": "Create View"
                  },
                  {
                    "type": "object",
                    "properties": {
                      "type": {
                        "type": "string",
                        "const": "update_view",
                        "description": "The name of the tool to run."
                      },
                      "update_view": {
                        "type": "object",
                        "properties": {
                          "view_id": {
                            "type": "string",
                            "description": "The view to update. Accepts a view:// URI, a Notion URL with ?v= parameter, or a bare UUID."
                          },
                          "name": {
                            "type": "string",
                            "description": "New name for the view."
                          },
                          "configure": {
                            "type": "string",
                            "description": "View configuration DSL string. Supports FILTER, SORT BY, GROUP BY, CALENDAR BY, TIMELINE BY, MAP BY, CHART, FORM, SHOW, HIDE, COVER, WRAP CELLS, FREEZE COLUMNS, and CLEAR directives."
                          }
                        },
                        "required": [
                          "view_id"
                        ],
                        "description": "The parameters for the update_view tool. Update a view's name, filters, sorts, or display configuration.\n\nUse \"fetch\" to get view IDs from database responses. Only include fields\nyou want to change. The \"configure\" param uses the same DSL as create_view.\nUse CLEAR to remove settings:\n- CLEAR FILTER — remove all filters\n- CLEAR SORT — remove all sorts\n- CLEAR GROUP BY — remove grouping\n\nSee notion://docs/view-dsl-spec resource for full syntax.\n\n<example description=\"Rename\">{\"view_id\": \"abc123\", \"name\": \"Sprint Board\"}</example>\n<example description=\"Update filter\">{\"view_id\": \"abc123\", \"configure\": \"FILTER \\\"Status\\\" = \\\"Done\\\"\"}</example>\n<example description=\"Clear filter, add sort\">{\"view_id\": \"abc123\", \"configure\": \"CLEAR FILTER; SORT BY \\\"Created\\\" DESC\"}</example>\n<example description=\"Update grouping\">{\"view_id\": \"abc123\", \"configure\": \"GROUP BY \\\"Priority\\\"; SHOW \\\"Name\\\", \\\"Status\\\"\"}</example>"
                      }
                    },
                    "required": [
                      "type",
                      "update_view"
                    ],
                    "title": "Update View"
                  }
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "oneOf": [
                    {
                      "type": "object",
                      "properties": {
                        "pages": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string"
                              },
                              "url": {
                                "type": "string"
                              },
                              "properties": {
                                "type": "object",
                                "additionalProperties": {
                                  "oneOf": [
                                    {
                                      "type": "string"
                                    },
                                    {
                                      "type": "number"
                                    },
                                    {
                                      "type": "null"
                                    }
                                  ]
                                }
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "id",
                              "url",
                              "properties"
                            ]
                          },
                          "maxItems": 100
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "pages"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "page_id": {
                          "$ref": "#/components/schemas/idResponse"
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "page_id"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "result": {
                          "type": "string"
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "result"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "page_id": {
                          "type": "string",
                          "description": "The ID of the created page."
                        },
                        "page_url": {
                          "type": "string",
                          "description": "The Notion URL of the created page."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "page_id",
                        "page_url"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "type": {
                          "type": "string",
                          "enum": [
                            "ai_search",
                            "workspace_search",
                            "none"
                          ],
                          "description": "The type of internal search that was performed, based on the user's access to Notion AI. Users without Notion AI will get a workspace search only, not including connected tools. If the search was not performed, this will be 'none'."
                        },
                        "results": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string"
                              },
                              "title": {
                                "type": "string"
                              },
                              "url": {
                                "type": "string",
                                "description": "Page ID for Notion results (pass to fetch tool) or full URL for external connector results."
                              },
                              "type": {
                                "type": "string"
                              },
                              "highlight": {
                                "type": "string"
                              },
                              "timestamp": {
                                "type": "string"
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "id",
                              "title",
                              "url",
                              "type",
                              "highlight",
                              "timestamp"
                            ]
                          },
                          "maxItems": 100,
                          "description": "An array of combined and deduplicated search results from the internal search queries."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "type",
                        "results"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "type": {
                          "type": "string",
                          "const": "user_search",
                          "description": "The type of users search that was performed."
                        },
                        "results": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "string",
                                "description": "All results of user search"
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "text"
                            ]
                          },
                          "maxItems": 100,
                          "description": "An array of search results from the users search queries."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "type",
                        "results"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "title": {
                          "type": "string"
                        },
                        "url": {
                          "type": "string"
                        },
                        "text": {
                          "type": "string"
                        },
                        "metadata": {
                          "type": "object",
                          "properties": {
                            "type": {
                              "type": "string",
                              "enum": [
                                "page",
                                "database",
                                "data_source"
                              ],
                              "description": "One of: `page`, `database`, `data_source`"
                            }
                          },
                          "additionalProperties": false,
                          "required": [
                            "type"
                          ]
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "title",
                        "url",
                        "text",
                        "metadata"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "result": {
                          "type": "string",
                          "description": "A rendered Markdown string describing the structure and details of the newly created database."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "result"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "result": {
                          "type": "string",
                          "description": "A rendered Markdown string describing the structure and details of the updated data source."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "result"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "results": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "additionalProperties": {
                              "oneOf": [
                                {
                                  "type": "string"
                                },
                                {
                                  "type": "number"
                                },
                                {
                                  "type": "boolean"
                                },
                                {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  },
                                  "maxItems": 100
                                },
                                {
                                  "type": "null"
                                }
                              ]
                            }
                          },
                          "maxItems": 100,
                          "description": "Array of query result rows, where each row is a record with column names as keys"
                        },
                        "has_more": {
                          "type": "boolean",
                          "description": "Whether there are more results available beyond the returned limit"
                        },
                        "data_source_ids": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "maxItems": 100,
                          "description": "IDs of data sources that were queried (only present for SQL queries)"
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "results",
                        "has_more"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "results": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "additionalProperties": {
                              "oneOf": [
                                {
                                  "type": "string"
                                },
                                {
                                  "type": "number"
                                },
                                {
                                  "type": "boolean"
                                },
                                {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  },
                                  "maxItems": 100
                                },
                                {
                                  "type": "null"
                                }
                              ]
                            }
                          },
                          "maxItems": 100,
                          "description": "Array of query result rows, where each row is a record with column names as keys"
                        },
                        "has_more": {
                          "type": "boolean",
                          "description": "Whether there are more results available beyond the returned limit"
                        },
                        "data_source_ids": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "maxItems": 100,
                          "description": "IDs of data sources that were queried"
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "results",
                        "has_more"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "results": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "additionalProperties": {
                              "oneOf": [
                                {
                                  "type": "string"
                                },
                                {
                                  "type": "number"
                                },
                                {
                                  "type": "boolean"
                                },
                                {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  },
                                  "maxItems": 100
                                },
                                {
                                  "type": "null"
                                }
                              ]
                            }
                          },
                          "maxItems": 100,
                          "description": "Array of meeting note rows, where each row is a record with column names as keys"
                        },
                        "has_more": {
                          "type": "boolean",
                          "description": "Whether there are more results available beyond the returned limit"
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "results",
                        "has_more"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "result": {
                          "type": "object",
                          "properties": {
                            "status": {
                              "type": "string",
                              "const": "success",
                              "description": "The status of the operation."
                            },
                            "id": {
                              "type": "string",
                              "description": "The ID of the created comment."
                            }
                          },
                          "additionalProperties": false,
                          "required": [
                            "status",
                            "id"
                          ],
                          "description": "The result of the create comment operation."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "result"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "string",
                          "description": "XML-formatted discussions and comments from the page."
                        }
                      },
                      "additionalProperties": false
                    },
                    {
                      "type": "object",
                      "properties": {
                        "joinedTeams": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "type": {
                                "type": "string",
                                "const": "team",
                                "description": "The type of the result."
                              },
                              "id": {
                                "$ref": "#/components/schemas/idResponse",
                                "description": "The unique identifier of the team."
                              },
                              "name": {
                                "type": "string",
                                "description": "The display name of the team."
                              },
                              "in_trash": {
                                "type": "boolean",
                                "description": "Whether the team is in the trash."
                              },
                              "role": {
                                "type": "string",
                                "enum": [
                                  "owner",
                                  "member",
                                  "guest",
                                  "none"
                                ],
                                "description": "The authenticated user's role in this team: 'owner' (full admin access), 'member' (content access), 'guest' (limited access), or 'none' (no access)."
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "type",
                              "id",
                              "name",
                              "in_trash",
                              "role"
                            ]
                          },
                          "maxItems": 100,
                          "description": "Teams that the authenticated user is a member of."
                        },
                        "otherTeams": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "type": {
                                "type": "string",
                                "const": "team",
                                "description": "The type of the result."
                              },
                              "id": {
                                "$ref": "#/components/schemas/idResponse",
                                "description": "The unique identifier of the team."
                              },
                              "name": {
                                "type": "string",
                                "description": "The display name of the team."
                              },
                              "in_trash": {
                                "type": "boolean",
                                "description": "Whether the team is in the trash."
                              },
                              "role": {
                                "type": "string",
                                "enum": [
                                  "owner",
                                  "member",
                                  "guest",
                                  "none"
                                ],
                                "description": "The authenticated user's role in this team: 'owner' (full admin access), 'member' (content access), 'guest' (limited access), or 'none' (no access)."
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "type",
                              "id",
                              "name",
                              "in_trash",
                              "role"
                            ]
                          },
                          "maxItems": 100,
                          "description": "Teams that the authenticated user is not a member of but can see."
                        },
                        "hasMore": {
                          "type": "boolean",
                          "description": "Whether there are more teams that were not included due to the result limit."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "joinedTeams",
                        "otherTeams",
                        "hasMore"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "results": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "type": {
                                "type": "string",
                                "enum": [
                                  "person",
                                  "bot"
                                ],
                                "description": "The type of user: 'person' or 'bot'."
                              },
                              "id": {
                                "type": "string",
                                "description": "The unique identifier of the user."
                              },
                              "name": {
                                "type": "string",
                                "description": "The display name of the user."
                              },
                              "email": {
                                "type": "string",
                                "description": "The email address of the user (only for person types)."
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "type",
                              "id",
                              "name",
                              "email"
                            ]
                          },
                          "maxItems": 100,
                          "description": "List of users (both workspace members and guests) and bots in the current page."
                        },
                        "has_more": {
                          "type": "boolean",
                          "description": "Whether there are more users available in the next page."
                        },
                        "next_cursor": {
                          "type": "string",
                          "description": "Cursor for the next page of results. Use this value as start_cursor in the next request to get the next page."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "results",
                        "has_more",
                        "next_cursor"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "agents": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "type": {
                                "type": "string",
                                "const": "agent",
                                "description": "The type of the result."
                              },
                              "id": {
                                "$ref": "#/components/schemas/idResponse",
                                "description": "The unique identifier of the agent."
                              },
                              "name": {
                                "type": "string",
                                "description": "The display name of the agent."
                              },
                              "description": {
                                "type": "string",
                                "description": "A short description of what the agent does."
                              },
                              "instructions": {
                                "type": "string",
                                "description": "The system instructions that define how the agent behaves."
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "type",
                              "id",
                              "name"
                            ]
                          },
                          "maxItems": 100,
                          "description": "List of available custom agents."
                        },
                        "hasMore": {
                          "type": "boolean",
                          "description": "Whether there are more agents that were not included due to the result limit."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "agents",
                        "hasMore"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "answer": {
                          "type": "string",
                          "description": "The AI-generated answer to the question"
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "answer"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "agent_id": {
                          "type": "string",
                          "description": "The unique identifier of the agent that processed the request"
                        },
                        "session_id": {
                          "type": "string",
                          "description": "The session ID for this conversation"
                        },
                        "thread_id": {
                          "type": "string",
                          "description": "The thread ID for this conversation thread"
                        },
                        "response": {
                          "type": "string",
                          "description": "The agent's response to the user's message"
                        },
                        "chat_url": {
                          "type": "string",
                          "description": "URL to view this chat conversation in the Notion app"
                        },
                        "is_new_conversation": {
                          "type": "boolean",
                          "description": "Whether this was a new conversation or a continuation"
                        },
                        "timestamp": {
                          "type": "string",
                          "description": "Timestamp when the response was generated"
                        },
                        "transcript": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string"
                              },
                              "type": {
                                "type": "string"
                              }
                            },
                            "required": [
                              "id",
                              "type"
                            ],
                            "additionalProperties": true
                          },
                          "maxItems": 100,
                          "description": "Optional conversation transcript if requested"
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "agent_id",
                        "session_id",
                        "thread_id",
                        "response",
                        "chat_url",
                        "is_new_conversation",
                        "timestamp"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "result": {
                          "type": "string",
                          "description": "A rendered Markdown string describing the newly created view."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "result"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "result": {
                          "type": "string",
                          "description": "A rendered Markdown string describing the updated view."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "result"
                      ]
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/tools/run/eval": {
      "post": {
        "summary": "Run an AI tool in eval mode",
        "operationId": "run-tool-eval",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "allOf": [
                  {
                    "type": "object",
                    "properties": {
                      "eval_session_id": {
                        "type": "string",
                        "description": "The eval session ID for tracking operations across multiple tool calls."
                      },
                      "eval_run_id": {
                        "type": "string",
                        "description": "The eval run ID for organizing a group of eval sessions."
                      }
                    },
                    "required": [
                      "eval_session_id",
                      "eval_run_id"
                    ]
                  },
                  {
                    "oneOf": [
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "search",
                            "description": "The name of the tool to run."
                          },
                          "search": {
                            "type": "object",
                            "properties": {
                              "query": {
                                "type": "string",
                                "minLength": 1,
                                "description": "Semantic search query over your entire Notion workspace and connected sources\n(Slack, Google Drive, Github, Jira, Microsoft Teams, Sharepoint, OneDrive,\nor Linear). For best results, don't provide more than one question per tool call.\nUse a separate \"search\" tool call for each search you want to perform.\n\nAlternatively, the query can be a substring or keyword to find users by matching\nagainst their name or email address. For example: \"john\" or \"john@example.com\""
                              },
                              "query_type": {
                                "type": "string",
                                "enum": [
                                  "internal",
                                  "user"
                                ],
                                "description": "Specify type of the query as either \"internal\" or \"user\". Always include this input if performing\n\"user\" search."
                              },
                              "content_search_mode": {
                                "type": "string",
                                "enum": [
                                  "workspace_search",
                                  "ai_search"
                                ],
                                "description": "Select search backend: \"workspace_search\" (faster, workspace-only) or \"ai_search\" (semantic, includes Slack/Linear/etc.). If omitted, uses AI search if available. Content searches only."
                              },
                              "data_source_url": {
                                "type": "string",
                                "description": "Optionally, provide the URL of a Data source to search. This will perform a semantic search over\nthe pages in the Data Source. Note: must be a Data Source, not a Database. <data-source> tags are\npart of the Notion flavored Markdown format returned by tools like fetch. The full spec is\navailable in the create-pages tool description."
                              },
                              "page_url": {
                                "type": "string",
                                "description": "Optionally, provide the URL or ID of a page to search within. This will perform a semantic search\nover the content within and under the specified page. Accepts either a full page URL\n(e.g. https://notion.so/workspace/Page-Title-1234567890) or just the page ID (UUIDv4) with or\nwithout dashes."
                              },
                              "teamspace_id": {
                                "type": "string",
                                "description": "Optionally, provide the ID of a teamspace to restrict search results to. This will perform a search\nover content within the specified teamspace only. Accepts the teamspace ID (UUIDv4) with or\nwithout dashes."
                              },
                              "filters": {
                                "type": "object",
                                "properties": {
                                  "created_date_range": {
                                    "type": "object",
                                    "properties": {
                                      "start_date": {
                                        "type": "string",
                                        "format": "date",
                                        "description": "The start date of the date range as an ISO 8601 date string, if any."
                                      },
                                      "end_date": {
                                        "type": "string",
                                        "format": "date",
                                        "description": "The end date of the date range as an ISO 8601 date string, if any."
                                      }
                                    },
                                    "description": "Optional filter to only produce search results created within the specified date range."
                                  },
                                  "created_by_user_ids": {
                                    "type": "array",
                                    "items": {
                                      "$ref": "#/components/schemas/idRequest"
                                    },
                                    "maxItems": 100,
                                    "description": "Optional filter to only produce search results created by the Notion users that have the specified user IDs."
                                  }
                                },
                                "description": "Optionally provide filters to apply to the search results. Only valid when query_type is 'internal'."
                              },
                              "page_size": {
                                "type": "integer",
                                "minimum": 1,
                                "maximum": 25,
                                "description": "Maximum number of results to return (default 10). Lower values reduce response size."
                              },
                              "max_highlight_length": {
                                "type": "integer",
                                "minimum": 0,
                                "maximum": 500,
                                "description": "Maximum character length for result highlights (default 200). Set to 0 to omit highlights entirely."
                              }
                            },
                            "required": [
                              "query"
                            ],
                            "description": "The parameters for the search tool. Perform a search over:\n\t\t- \"internal\": Semantic search over Notion workspace and connected sources (Slack, Google Drive,\n\t\t  Github, Jira, Microsoft Teams, Sharepoint, OneDrive, Linear). Supports filtering by creation\n\t\t  date and creator.\n\t\t- \"user\": Search for users by name or email.\n\n\t\tAuto-selects AI search (with connected sources) or workspace search (workspace-only, faster)\n\t\tbased on user's access to Notion AI. Use content_search_mode to override.\n\n\t\tUse \"fetch\" tool for full page/database contents after getting search results.\n\t\tEach result's \"url\" field contains a page ID for Notion results (pass directly to\n\t\tfetch tool's \"id\" param) or a full URL for external connector results (Slack, Google\n\t\tDrive, etc.). Set page_size (default 10, max 25) and max_highlight_length (default\n\t\t200, 0 to omit) as low as possible to minimize response size.\n\n\t\tTo search within a database: First fetch the database to get the data source URL\n\t\t(collection://...) from <data-source url=\"...\"> tags, then use that as data_source_url.\n\t\tFor multi-source databases, match by view ID (?v=...) in URL or search all sources separately.\n\n\t\tDon't combine database URL/ID with collection:// prefix for data_source_url. Don't use\n\t\tdatabase URL as page_url.\n\n\t\t<example description=\"Search with date range filter (only documents created in 2024)\">\n\t\t{\n\t\t\t\"query\": \"quarterly revenue report\",\n\t\t\t\"query_type\": \"internal\",\n\t\t\t\"filters\": {\n\t\t\t\t\"created_date_range\": {\n\t\t\t\t\t\"start_date\": \"2024-01-01\",\n\t\t\t\t\t\"end_date\": \"2025-01-01\"\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Teamspace + creator filter\">\n\t\t{\"query\": \"project updates\", \"query_type\": \"internal\", \"teamspace_id\": \"f336d0bc-b841-465b-8045-024475c079dd\", \"filters\": {\"created_by_user_ids\": [\"a1b2c3d4-e5f6-7890-abcd-ef1234567890\"]}}\n\t\t</example>\n\n\t\t<example description=\"Database with date + creator filters\">\n\t\t{\"query\": \"design review\", \"data_source_url\": \"collection://f336d0bc-b841-465b-8045-024475c079dd\", \"filters\": {\"created_date_range\": {\"start_date\": \"2024-10-01\"}, \"created_by_user_ids\": [\"a1b2c3d4-e5f6-7890-abcd-ef1234567890\", \"b2c3d4e5-f6a7-8901-bcde-f12345678901\"]}}\n\t\t</example>\n\n\t\t<example description=\"User search\">\n\t\t{\"query\": \"john@example.com\", \"query_type\": \"user\"}\n\t\t</example>"
                          }
                        },
                        "required": [
                          "type",
                          "search"
                        ],
                        "title": "Search"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "fetch",
                            "description": "The name of the tool to run."
                          },
                          "fetch": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string",
                                "description": "The ID or URL of the Notion page, database, or data source to fetch. Supports notion.so URLs, Notion Sites URLs (*.notion.site), raw UUIDs, and data source URLs (collection://...)."
                              },
                              "include_transcript": {
                                "type": "boolean",
                                "description": "Whether to include meeting note transcripts. Defaults to false. When true, full transcripts are included; when false, a placeholder with the meeting note URL is shown instead."
                              },
                              "include_discussions": {
                                "type": "boolean",
                                "description": "Whether to include discussion/comment indicators in the page output. When true, adds a <page-discussions> summary with discussion count, preview snippets, and discussion:// URLs. Use with the get_comments tool to retrieve full discussion content. Defaults to false."
                              }
                            },
                            "required": [
                              "id"
                            ],
                            "description": "The parameters for the fetch tool. Retrieves details about a Notion entity (page, database, or data source) by URL or ID.\n\nProvide URL or ID in `id` parameter. Make multiple calls to fetch multiple entities.\n\nPages use enhanced Markdown format. For the complete specification, fetch the MCP resource\nat `notion://docs/enhanced-markdown-spec`.\n\nDatabases return all data sources (collections). Each data source has a unique ID shown in\n`<data-source url=\"collection://...\">` tags. You can pass a data source ID directly to this\ntool to fetch details about that specific data source, including its schema and properties.\nUse data source IDs with update_data_source and query_data_sources tools. Multi-source\ndatabases (e.g., with linked sources) will show multiple data sources.\n\nSet `include_discussions` to true to see discussion counts and inline discussion markers\nthat correlate with the `get_comments` tool. The page output will include a\n`<page-discussions>` summary tag with discussion count, preview snippets, and\n`discussion://` URLs that match the discussion IDs returned by `get_comments`.\n\n<example>{\"id\": \"https://notion.so/workspace/Page-a1b2c3d4e5f67890\"}</example>\n<example>{\"id\": \"12345678-90ab-cdef-1234-567890abcdef\"}</example>\n<example>{\"id\": \"https://myspace.notion.site/Page-Title-abc123def456\"}</example>\n<example>{\"id\": \"page-uuid\", \"include_discussions\": true}</example>\n<example>{\"id\": \"collection://12345678-90ab-cdef-1234-567890abcdef\"}</example>"
                          }
                        },
                        "required": [
                          "type",
                          "fetch"
                        ],
                        "title": "Fetch"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "create_pages",
                            "description": "The name of the tool to run."
                          },
                          "create_pages": {
                            "type": "object",
                            "properties": {
                              "pages": {
                                "type": "array",
                                "items": {
                                  "type": "object",
                                  "properties": {
                                    "properties": {
                                      "type": "object",
                                      "additionalProperties": {
                                        "oneOf": [
                                          {
                                            "type": "string"
                                          },
                                          {
                                            "type": "number"
                                          },
                                          {
                                            "type": "null"
                                          }
                                        ]
                                      },
                                      "description": "The properties of the new page, which is a JSON map of property names to SQLite values.\nFor pages in a database, use the SQLite schema definition shown in <database>.\nFor pages outside of a database, the only allowed property is \"title\", which is the title of the page and is automatically shown at the top of the page as a large heading."
                                    },
                                    "content": {
                                      "type": "string",
                                      "description": "The content of the new page, using Notion Markdown."
                                    },
                                    "template_id": {
                                      "type": "string",
                                      "description": "The ID of a template to apply to this page. When specified, do not provide 'content' as the template will provide it. Properties can still be set alongside the template. Get template IDs from the <templates> section in the fetch tool results."
                                    },
                                    "icon": {
                                      "type": "string",
                                      "description": "An emoji character (e.g. \"🚀\"), a custom emoji by name (e.g. \":rocket_ship:\"), or an external image URL. Use \"none\" to explicitly set no icon. Omit to leave unchanged."
                                    },
                                    "cover": {
                                      "type": "string",
                                      "description": "An external image URL for the page cover. Use \"none\" to explicitly set no cover. Omit to leave unchanged."
                                    }
                                  },
                                  "additionalProperties": false
                                },
                                "maxItems": 100,
                                "description": "The pages to create."
                              },
                              "parent": {
                                "oneOf": [
                                  {
                                    "type": "object",
                                    "properties": {
                                      "page_id": {
                                        "$ref": "#/components/schemas/idRequest",
                                        "description": "The ID of the parent page (with or without dashes), for example, 195de9221179449fab8075a27c979105"
                                      },
                                      "type": {
                                        "type": "string",
                                        "const": "page_id",
                                        "description": "Always `page_id`"
                                      }
                                    },
                                    "required": [
                                      "page_id"
                                    ]
                                  },
                                  {
                                    "type": "object",
                                    "properties": {
                                      "database_id": {
                                        "$ref": "#/components/schemas/idRequest",
                                        "description": "The ID of the parent database (with or without dashes), for example, 195de9221179449fab8075a27c979105"
                                      },
                                      "type": {
                                        "type": "string",
                                        "const": "database_id",
                                        "description": "Always `database_id`"
                                      }
                                    },
                                    "required": [
                                      "database_id"
                                    ]
                                  },
                                  {
                                    "type": "object",
                                    "properties": {
                                      "data_source_id": {
                                        "$ref": "#/components/schemas/idRequest",
                                        "description": "The ID of the parent data source (collection), with or without dashes. For example, f336d0bc-b841-465b-8045-024475c079dd"
                                      },
                                      "type": {
                                        "type": "string",
                                        "const": "data_source_id",
                                        "description": "Always `data_source_id`"
                                      }
                                    },
                                    "required": [
                                      "data_source_id"
                                    ]
                                  }
                                ],
                                "description": "The parent under which the new pages will be created. This can be a page (page_id), a database page (database_id), or a data source/collection under a database (data_source_id). If omitted, the new pages will be created as private pages at the workspace level. Use data_source_id when you have a collection:// URL from the fetch tool."
                              }
                            },
                            "required": [
                              "pages"
                            ],
                            "description": "The parameters for the create_pages tool. ## Overview\n\n\t\tCreates one or more Notion pages, with the specified properties and content.\n\n\t\t## Parent\n\n\t\tAll pages created with a single call to this tool will have the same parent.\n\t\tThe parent can be a Notion page (\"page_id\") or data source (\"data_source_id\").\n\t\tIf the parent is omitted, the pages are created as standalone, workspace-level\n\t\tprivate pages, and the person that created them can organize them later as they\n\t\tsee fit.\n\n\t\tIf you have a database URL, ALWAYS pass it to the \"fetch\" tool first to get the schema\n\t\tand URLs of each data source under the database. You can't use the \"database_id\"\n\t\tparent type if the database has more than one data source, so you'll need to identify\n\t\twhich \"data_source_id\" to use based on the situation and the results from the fetch tool\n\t\t(data source URLs look like collection://<data_source_id>).\n\n\t\tIf you know the pages should be created under a data source, do NOT use the database ID\n\t\tor URL under the \"page_id\" parameter; \"page_id\" is only for regular, non-database pages.\n\n\t\t## Content\n\n\t\tNotion page content is a string in Notion-flavored Markdown format.\n\n\t\tDon't include the page title at the top of the page's content. Only include it under\n\t\t\"properties\".\n\n\t\t**IMPORTANT**: For the complete Markdown specification, always first fetch the MCP resource\n\t\tat `notion://docs/enhanced-markdown-spec`. Do NOT guess or hallucinate Markdown syntax.\n\t\tThis spec is also applicable to other tools like update-page and fetch.\n\n\t\t## Properties\n\n\t\tNotion page properties are a JSON map of property names to SQLite values.\n\n\t\tWhen creating pages in a database:\n\t\t- Use the correct property names from the data source schema shown in the fetch tool results.\n\t\t- Always include a title property. Data sources always have exactly one title property, but\n\t\t  it may not be named \"title\", so, again, rely on the fetched data source schema.\n\n\t\tFor pages outside of a database:\n\t\t- The only allowed property is \"title\",\twhich is the title of the page in inline markdown format.\n\t\t  Always include a \"title\" property.\n\n\t\t**IMPORTANT**: Some property types require expanded formats:\n\t\t- Date properties: Split into \"date:{property}:start\", \"date:{property}:end\" (optional), and\n\t\t  \"date:{property}:is_datetime\" (0 or 1)\n\t\t- Place properties: Split into \"place:{property}:name\", \"place:{property}:address\",\n\t\t  \"place:{property}:latitude\", \"place:{property}:longitude\", and\n\t\t  \"place:{property}:google_place_id\" (optional)\n\t\t- Number properties: Use JavaScript numbers (not strings)\n\t\t- Checkbox properties: Use \"__YES__\" for checked, \"__NO__\" for unchecked\n\n\t\t**Special property naming**: Properties named \"id\" or \"url\" (case insensitive) must be\n\t\tprefixed with \"userDefined:\" (e.g., \"userDefined:URL\", \"userDefined:id\")\n\n\t\t## Templates\n\n\t\tWhen creating a page in a database, you can apply a template to pre-populate it with\n\t\tcontent and property values. Use the \"fetch\" tool on a database to see available\n\t\ttemplates in the <templates> section of each data source.\n\n\t\tWhen using a template:\n\t\t- Pass the template's ID as \"template_id\" in the page object.\n\t\t- Do NOT include \"content\" when using a template, as the template provides it.\n\t\t- You can still set \"properties\" alongside the template to override template defaults.\n\t\t- Template application is asynchronous. The page is created immediately but starts\n\t\t  blank; the template content will appear shortly after.\n\n\t\t## Icon and Cover\n\n\t\tEach page can optionally have an icon and a cover image.\n\t\t- \"icon\": An emoji character (e.g. \"🚀\"), a custom emoji by name (e.g. \":rocket_ship:\"),\n\t\t  or an external image URL. Use \"none\" to remove. Omit to leave unchanged.\n\t\t- \"cover\": An external image URL. Use \"none\" to remove. Omit to leave unchanged.\n\n\t\t## Examples\n\n\t\t<example description=\"Create a page with an icon and cover\">\n\t\t{\n\t\t\t\"pages\": [\n\t\t\t\t{\n\t\t\t\t\t\"properties\": {\"title\": \"My Page\"},\n\t\t\t\t\t\"icon\": \"🚀\",\n\t\t\t\t\t\"cover\": \"https://example.com/cover.jpg\"\n\t\t\t\t}\n\t\t\t]\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Create a page from a database template\">\n\t\t{\n\t\t\t\"parent\": {\"data_source_id\": \"f336d0bc-b841-465b-8045-024475c079dd\"},\n\t\t\t\"pages\": [\n\t\t\t\t{\n\t\t\t\t\t\"template_id\": \"a5da15f6-b853-455d-8827-f906fb52db2b\",\n\t\t\t\t\t\"properties\": {\n\t\t\t\t\t\t\"Task Name\": \"New urgent bug\"\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t]\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Create a standalone page with a title and content\">\n\t\t{\n\t\t\t\"pages\": [\n\t\t\t\t{\n\t\t\t\t\t\"properties\": {\"title\": \"Page title\"},\n\t\t\t\t\t\"content\": \"# Section 1 {color=\"blue\"}\nSection 1 content\n<details>\n<summary>Toggle block</summary>\n\tHidden content inside toggle\n</details>\"\n\t\t\t\t}\n\t\t\t]\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Create a page under a database's data source\">\n\t\t{\n\t\t\t\"parent\": {\"data_source_id\": \"f336d0bc-b841-465b-8045-024475c079dd\"},\n\t\t\t\"pages\": [\n\t\t\t\t{\n\t\t\t\t\t\"properties\": {\n\t\t\t\t\t\t\"Task Name\": \"Task 123\",\n\t\t\t\t\t\t\"Status\": \"In Progress\",\n\t\t\t\t\t\t\"Priority\": 5,\n\t\t\t\t\t\t\"Is Complete\": \"__YES__\",\n\t\t\t\t\t\t\"date:Due Date:start\": \"2024-12-25\",\n\t\t\t\t\t\t\"date:Due Date:is_datetime\": 0\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t]\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Create a page with an existing page as a parent\">\n\t\t{\n\t\t\t\"parent\": {\"page_id\": \"a1b2c3d4-e5f6-7890-abcd-ef1234567890\"},\n\t\t\t\"pages\": [\n\t\t\t\t{\n\t\t\t\t\t\"properties\": {\"title\": \"Page title\"},\n\t\t\t\t\t\"content\": \"# Section 1\n\nSection 1 content\n\n# Section 2\n\nSection 2 content\"\n\t\t\t\t}\n\t\t\t]\n\t\t}\n\t\t</example>"
                          }
                        },
                        "required": [
                          "type",
                          "create_pages"
                        ],
                        "title": "Create Pages"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "update_page",
                            "description": "The name of the tool to run."
                          },
                          "update_page": {
                            "type": "object",
                            "properties": {
                              "page_id": {
                                "type": "string",
                                "description": "The ID of the page to update, with or without dashes."
                              },
                              "command": {
                                "type": "string",
                                "enum": [
                                  "update_properties",
                                  "update_content",
                                  "replace_content",
                                  "apply_template",
                                  "update_verification"
                                ],
                                "description": "The update command to execute."
                              },
                              "properties": {
                                "type": "object",
                                "additionalProperties": {
                                  "oneOf": [
                                    {
                                      "type": "string"
                                    },
                                    {
                                      "type": "number"
                                    },
                                    {
                                      "type": "null"
                                    }
                                  ]
                                },
                                "description": "Required for \"update_properties\" command. A JSON object that updates the page's properties.\nFor pages in a database, use the SQLite schema definition shown in <database>.\nFor pages outside of a database, the only allowed property is \"title\", which is the title of the page in inline markdown format.\nUse null to remove a property's value."
                              },
                              "new_str": {
                                "type": "string",
                                "description": "Required for \"replace_content\" command. The new content string to replace the entire page content with."
                              },
                              "content_updates": {
                                "type": "array",
                                "items": {
                                  "type": "object",
                                  "properties": {
                                    "old_str": {
                                      "type": "string",
                                      "description": "The existing content string to find and replace. Must exactly match the page content."
                                    },
                                    "new_str": {
                                      "type": "string",
                                      "description": "The new content string to replace old_str with."
                                    },
                                    "replace_all_matches": {
                                      "type": "boolean",
                                      "description": "If true, replaces all occurrences of old_str. If false (default), the operation fails if there are multiple matches."
                                    }
                                  },
                                  "required": [
                                    "old_str",
                                    "new_str"
                                  ]
                                },
                                "maxItems": 100,
                                "description": "Required for \"update_content\" command. An array of search-and-replace operations, each with old_str (content to find) and new_str (replacement content)."
                              },
                              "allow_deleting_content": {
                                "type": "boolean",
                                "description": "Optional for \"replace_content\" and \"update_content\" commands. Set to true to allow deletion of child pages and databases that are not referenced in the new content. If false or omitted, the operation will fail with an error listing the pages/databases that would be deleted."
                              },
                              "template_id": {
                                "type": "string",
                                "description": "Required for \"apply_template\" command. The ID of a template to apply to this page. Template content is appended to any existing page content."
                              },
                              "verification_status": {
                                "type": "string",
                                "enum": [
                                  "verified",
                                  "unverified"
                                ],
                                "description": "Required for \"update_verification\" command. Set to \"verified\" to mark the page as verified, or \"unverified\" to remove verification."
                              },
                              "verification_expiry_days": {
                                "type": "integer",
                                "minimum": 1,
                                "description": "Optional for \"update_verification\" command when verification_status is \"verified\". Number of days until verification expires (e.g. 7, 30, 90). Omit for indefinite verification."
                              },
                              "icon": {
                                "type": "string",
                                "description": "An emoji character (e.g. \"🚀\"), a custom emoji by name (e.g. \":rocket_ship:\"), or an external image URL. Use \"none\" to remove the icon. Omit to leave unchanged. Can be set alongside any command."
                              },
                              "cover": {
                                "type": "string",
                                "description": "An external image URL for the page cover. Use \"none\" to remove the cover. Omit to leave unchanged. Can be set alongside any command."
                              }
                            },
                            "required": [
                              "page_id",
                              "command"
                            ],
                            "description": "The parameters for the update_page tool. ## Overview\n\n\t\tUpdate a Notion page's properties or content.\n\n\t\t## Properties\n\n\t\tNotion page properties are a JSON map of property names to SQLite values.\n\n\t\tFor pages in a database:\n\t\t- ALWAYS use the \"fetch\" tool first to get the data source schema and the\texact property names.\n\t\t- Provide a non-null value to update a property's value.\n\t\t- Omitted properties are left unchanged.\n\n\t\t**IMPORTANT**: Some property types require expanded formats:\n\t\t- Date properties: Split into \"date:{property}:start\", \"date:{property}:end\" (optional), and\n\t\t  \"date:{property}:is_datetime\" (0 or 1)\n\t\t- Place properties: Split into \"place:{property}:name\", \"place:{property}:address\",\n\t\t  \"place:{property}:latitude\", \"place:{property}:longitude\", and\n\t\t  \"place:{property}:google_place_id\" (optional)\n\t\t- Number properties: Use JavaScript numbers (not strings)\n\t\t- Checkbox properties: Use \"__YES__\" for checked, \"__NO__\" for unchecked\n\n\t\t**Special property naming**: Properties named \"id\" or \"url\" (case insensitive) must be\n\t\tprefixed with \"userDefined:\" (e.g., \"userDefined:URL\", \"userDefined:id\")\n\n\t\tFor pages outside of a database:\n\t\t- The only allowed property is \"title\",\twhich is the title of the page in inline markdown format.\n\n\t\t## Content\n\n\t\tNotion page content is a string in Notion-flavored Markdown format.\n\n\t\t**IMPORTANT**: For the complete Markdown specification, first fetch the MCP resource at\n\t\t`notion://docs/enhanced-markdown-spec`. Do NOT guess or hallucinate Markdown syntax.\n\n\t\tBefore updating a page's content with this tool, use the \"fetch\" tool first to get the existing\n\t\tcontent to find out the Markdown snippets to use in the \"update_content\" command's old_str fields.\n\n\t\t### Preserving Child Pages and Databases\n\n\t\tWhen using \"replace_content\", the operation will check if any\n\t\tchild pages or databases would be deleted. If so, it will fail with an error listing the\n\t\taffected items.\n\n\t\tTo preserve child pages/databases, include them in new_str using `<page url=\"...\">` or\n\t\t`<database url=\"...\">` tags. Get the exact URLs from the \"fetch\" tool output.\n\n\t\t**CRITICAL**: To intentionally delete child content:\n\t\tif the call failed with validation and requires `allow_deleting_content` to be true,\n\t\tDO NOT automatically assume the content should be deleted.\n\t\tALWAYS show the list of pages to be deleted and ask for user confirmation before proceeding.\n\n\t\t## Icon and Cover\n\n\t\tYou can set or remove a page's icon and cover alongside any command.\n\t\t- \"icon\": An emoji character (e.g. \"🚀\"), a custom emoji by name (e.g. \":rocket_ship:\"),\n\t\t  or an external image URL. Use \"none\" to remove. Omit to leave unchanged.\n\t\t- \"cover\": An external image URL. Use \"none\" to remove. Omit to leave unchanged.\n\n\t\t## Examples\n\n\t\t<example description=\"Update page icon and cover\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"update_properties\",\n\t\t\t\"properties\": {\"title\": \"My Page\"},\n\t\t\t\"icon\": \"🚀\",\n\t\t\t\"cover\": \"https://example.com/cover.jpg\"\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Update page properties\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"update_properties\",\n\t\t\t\"properties\": {\n\t\t\t\t\"title\": \"New Page Title\",\n\t\t\t\t\"status\": \"In Progress\",\n\t\t\t\t\"priority\": 5,\n\t\t\t\t\"checkbox\": \"__YES__\",\n\t\t\t\t\"date:deadline:start\": \"2024-12-25\",\n\t\t\t\t\"date:deadline:is_datetime\": 0,\n\t\t\t\t\"place:office:name\": \"HQ\",\n\t\t\t\t\"place:office:latitude\": 37.7749,\n\t\t\t\t\"place:office:longitude\": -122.4194\n\t\t\t}\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Replace the entire content of a page\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"replace_content\",\n\t\t\t\"new_str\": \"# New Section\\nUpdated content goes here\"\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Update specific content in a page (search-and-replace)\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"update_content\",\n\t\t\t\"content_updates\": [\n\t\t\t\t{\n\t\t\t\t\t\"old_str\": \"# Old Section\\nOld content here\",\n\t\t\t\t\t\"new_str\": \"# New Section\\nUpdated content goes here\"\n\t\t\t\t}\n\t\t\t]\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Insert content after a specific location\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"update_content\",\n\t\t\t\"content_updates\": [\n\t\t\t\t{\n\t\t\t\t\t\"old_str\": \"## Previous section\\nExisting content\",\n\t\t\t\t\t\"new_str\": \"## Previous section\\nExisting content\\n\\n## New Section\\nContent to insert goes here\"\n\t\t\t\t}\n\t\t\t]\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Multiple content updates in a single call\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"update_content\",\n\t\t\t\"content_updates\": [\n\t\t\t\t{\n\t\t\t\t\t\"old_str\": \"Old text 1\",\n\t\t\t\t\t\"new_str\": \"New text 1\"\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\t\"old_str\": \"Old text 2\",\n\t\t\t\t\t\"new_str\": \"New text 2\"\n\t\t\t\t}\n\t\t\t]\n\t\t}\n\t\t</example>\n\n\t\t## Templates\n\n\t\tYou can apply a template to an existing page using the \"apply_template\" command.\n\t\tThe template content is appended to the page asynchronously. Get template IDs from\n\t\tthe <templates> section in the fetch tool results for a database, or use any page ID\n\t\tas a template.\n\n\t\t<example description=\"Apply a template to an existing page\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"apply_template\",\n\t\t\t\"template_id\": \"a5da15f6-b853-455d-8827-f906fb52db2b\"\n\t\t}\n\t\t</example>\n\n\t\t## Verification\n\n\t\tYou can verify or unverify a page using the \"update_verification\" command.\n\t\tVerification marks a page as reviewed and up-to-date. Requires a Business or Enterprise\n\t\tplan (or the page must be in a wiki).\n\n\t\t<example description=\"Verify a page for 90 days\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"update_verification\",\n\t\t\t\"verification_status\": \"verified\",\n\t\t\t\"verification_expiry_days\": 90\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Verify a page indefinitely\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"update_verification\",\n\t\t\t\"verification_status\": \"verified\"\n\t\t}\n\t\t</example>\n\n\t\t<example description=\"Remove verification from a page\">\n\t\t{\n\t\t\t\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\",\n\t\t\t\"command\": \"update_verification\",\n\t\t\t\"verification_status\": \"unverified\"\n\t\t}\n\t\t</example>"
                          }
                        },
                        "required": [
                          "type",
                          "update_page"
                        ],
                        "title": "Update Page"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "move_pages",
                            "description": "The name of the tool to run."
                          },
                          "move_pages": {
                            "type": "object",
                            "properties": {
                              "page_or_database_ids": {
                                "type": "array",
                                "items": {
                                  "type": "string"
                                },
                                "maxItems": 100,
                                "minItems": 1,
                                "description": "An array of up to 100 page or database IDs to move. IDs are v4 UUIDs and can be supplied with or without dashes (e.g. extracted from a <page> or <database> URL given by the \"search\" or \"fetch\" tool). Data Sources under Databases can't be moved individually."
                              },
                              "new_parent": {
                                "oneOf": [
                                  {
                                    "type": "object",
                                    "properties": {
                                      "page_id": {
                                        "$ref": "#/components/schemas/idRequest",
                                        "description": "The ID of the parent page (with or without dashes), for example, 195de9221179449fab8075a27c979105"
                                      },
                                      "type": {
                                        "type": "string",
                                        "const": "page_id",
                                        "description": "Always `page_id`"
                                      }
                                    },
                                    "required": [
                                      "page_id"
                                    ]
                                  },
                                  {
                                    "type": "object",
                                    "properties": {
                                      "database_id": {
                                        "$ref": "#/components/schemas/idRequest",
                                        "description": "The ID of the parent database (with or without dashes), for example, 195de9221179449fab8075a27c979105"
                                      },
                                      "type": {
                                        "type": "string",
                                        "const": "database_id",
                                        "description": "Always `database_id`"
                                      }
                                    },
                                    "required": [
                                      "database_id"
                                    ]
                                  },
                                  {
                                    "type": "object",
                                    "properties": {
                                      "data_source_id": {
                                        "$ref": "#/components/schemas/idRequest",
                                        "description": "The ID of the parent data source (collection), with or without dashes. For example, f336d0bc-b841-465b-8045-024475c079dd"
                                      },
                                      "type": {
                                        "type": "string",
                                        "const": "data_source_id",
                                        "description": "Always `data_source_id`"
                                      }
                                    },
                                    "required": [
                                      "data_source_id"
                                    ]
                                  },
                                  {
                                    "type": "object",
                                    "properties": {
                                      "type": {
                                        "type": "string",
                                        "const": "workspace",
                                        "description": "The parent type."
                                      }
                                    },
                                    "required": [
                                      "type"
                                    ]
                                  }
                                ],
                                "description": "The new parent under which the pages will be moved. This can be a page, the workspace, a database, or a specific data source under a database when there are multiple. Moving pages to the workspace level adds them as private pages and should rarely be used."
                              }
                            },
                            "required": [
                              "page_or_database_ids",
                              "new_parent"
                            ],
                            "description": "The parameters for the move_pages tool. Move one or more Notion pages or databases to a new parent."
                          }
                        },
                        "required": [
                          "type",
                          "move_pages"
                        ],
                        "title": "Move Pages"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "duplicate_page",
                            "description": "The name of the tool to run."
                          },
                          "duplicate_page": {
                            "type": "object",
                            "properties": {
                              "page_id": {
                                "type": "string",
                                "description": "The ID of the page to duplicate. This is a v4 UUID, with or without dashes, and can be parsed from a Notion page URL."
                              }
                            },
                            "required": [
                              "page_id"
                            ],
                            "description": "The parameters for the duplicate_page tool. Duplicate a Notion page. The page must be within the current workspace, and you must have permission to access it. The duplication completes asynchronously, so do not rely on the new page identified by the returned ID or URL to be populated immediately. Let the user know that the duplication is in progress and that they can check back later using the 'fetch' tool or by clicking the returned URL and viewing it in the Notion app."
                          }
                        },
                        "required": [
                          "type",
                          "duplicate_page"
                        ],
                        "title": "Duplicate Page"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "create_database",
                            "description": "The name of the tool to run."
                          },
                          "create_database": {
                            "type": "object",
                            "properties": {
                              "schema": {
                                "type": "string",
                                "description": "SQL DDL CREATE TABLE statement defining the database schema. Column names must be double-quoted, type options use single quotes."
                              },
                              "parent": {
                                "type": "object",
                                "properties": {
                                  "page_id": {
                                    "$ref": "#/components/schemas/idRequest",
                                    "description": "The ID of the parent page (with or without dashes), for example, 195de9221179449fab8075a27c979105"
                                  },
                                  "type": {
                                    "type": "string",
                                    "const": "page_id",
                                    "description": "Always `page_id`"
                                  }
                                },
                                "required": [
                                  "page_id"
                                ],
                                "description": "The parent under which to create the new database. If omitted, the database will be created as a private page at the workspace level."
                              },
                              "title": {
                                "type": "string",
                                "description": "The title of the new database."
                              },
                              "description": {
                                "type": "string",
                                "description": "The description of the new database."
                              }
                            },
                            "required": [
                              "schema"
                            ],
                            "description": "The parameters for the create_database tool. Creates a new Notion database using SQL DDL syntax.\n\nIf no title property provided, \"Name\" is auto-added. Returns Markdown with schema,\nSQLite definition, and data source ID in <data-source> tag for use with\nupdate_data_source and query_data_sources tools.\n\nThe schema param accepts a CREATE TABLE statement defining columns.\n\nType syntax:\n- Simple: TITLE, RICH_TEXT, DATE, PEOPLE, CHECKBOX, URL, EMAIL, PHONE_NUMBER, STATUS, FILES\n- SELECT('opt':color, ...) / MULTI_SELECT('opt':color, ...)\n- NUMBER [FORMAT 'dollar'] / FORMULA('expression')\n- RELATION('data_source_id') — one-way relation\n- RELATION('data_source_id', DUAL) — two-way relation\n- RELATION('data_source_id', DUAL 'synced_name') — two-way with synced property name\n- RELATION('data_source_id', DUAL 'synced_name' 'synced_id') — two-way with synced name and ID (for self-relations)\n- ROLLUP('rel_prop', 'target_prop', 'function')\n- UNIQUE_ID [PREFIX 'X'] / CREATED_TIME / LAST_EDITED_TIME\n- Any column: COMMENT 'description text'\nColors: default, gray, brown, orange, yellow, green, blue, purple, pink, red\n\n<example description=\"Minimal\">{\"schema\": \"CREATE TABLE (\\\"Name\\\" TITLE)\"}</example>\n<example description=\"Task DB\">{\"title\": \"Tasks\", \"schema\": \"CREATE TABLE (\\\"Task Name\\\" TITLE, \\\"Status\\\" SELECT('To Do':red, 'Done':green), \\\"Due Date\\\" DATE)\"}</example>\n<example description=\"With parent and options\">{\"parent\": {\"page_id\": \"f336d0bc-b841-465b-8045-024475c079dd\"}, \"title\": \"Projects\", \"schema\": \"CREATE TABLE (\\\"Name\\\" TITLE, \\\"Budget\\\" NUMBER FORMAT 'dollar', \\\"Tags\\\" MULTI_SELECT('eng':blue, 'design':pink), \\\"Task ID\\\" UNIQUE_ID PREFIX 'PRJ')\"}</example>\n<example description=\"Self-relation (two-step: create database first, then use its data source ID with update_data_source to add self-relations)\">{\"title\": \"Tasks\", \"schema\": \"CREATE TABLE (\\\"Name\\\" TITLE, \\\"Parent\\\" RELATION('ds_id', DUAL 'Children' 'children'), \\\"Children\\\" RELATION('ds_id', DUAL 'Parent' 'parent'))\"}</example>"
                          }
                        },
                        "required": [
                          "type",
                          "create_database"
                        ],
                        "title": "Create Database"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "update_data_source",
                            "description": "The name of the tool to run."
                          },
                          "update_data_source": {
                            "type": "object",
                            "properties": {
                              "data_source_id": {
                                "type": "string",
                                "description": "The data source to update. Accepts a collection:// URI from <data-source> tags, a bare UUID, or a database ID (only if the database has a single data source)."
                              },
                              "statements": {
                                "type": "string",
                                "description": "Semicolon-separated SQL DDL statements to update the schema. Supports ADD COLUMN, DROP COLUMN, RENAME COLUMN, ALTER COLUMN SET."
                              },
                              "title": {
                                "type": "string",
                                "description": "The new title of the data source."
                              },
                              "description": {
                                "type": "string",
                                "description": "The new description of the data source."
                              },
                              "is_inline": {
                                "type": "boolean",
                                "description": "Whether the database should display inline (true) or as full page (false). Only applicable for single-source databases."
                              },
                              "in_trash": {
                                "type": "boolean",
                                "description": "Move data source to trash. Cannot be undone without Notion UI."
                              }
                            },
                            "required": [
                              "data_source_id"
                            ],
                            "description": "The parameters for the update_data_source tool. Update a Notion data source's schema, title, or attributes using SQL DDL statements.\nReturns Markdown showing updated structure and schema.\n\nAccepts a data source ID (collection ID from fetch response's <data-source> tag)\nor a single-source database ID. Multi-source databases require the specific\ndata source ID.\n\nThe statements param accepts semicolon-separated DDL statements:\n- ADD COLUMN \"Name\" <type> - add a new property\n- DROP COLUMN \"Name\" - remove a property\n- RENAME COLUMN \"Old\" TO \"New\" - rename a property\n- ALTER COLUMN \"Name\" SET <type> - change type/options\n\nSame type syntax as create_database. Key types:\n- SELECT('opt':color, ...) / MULTI_SELECT('opt':color, ...)\n- NUMBER [FORMAT 'dollar'] / FORMULA('expression')\n- RELATION('ds_id') / RELATION('ds_id', DUAL) / RELATION('ds_id', DUAL 'synced_name' 'synced_id')\n- ROLLUP('rel_prop', 'target_prop', 'function') / UNIQUE_ID [PREFIX 'X']\n- Simple: TITLE, RICH_TEXT, DATE, PEOPLE, CHECKBOX, URL, EMAIL, PHONE_NUMBER, STATUS, FILES\n\n<example description=\"Add properties\">{\"data_source_id\": \"f336d0bc-b841-465b-8045-024475c079dd\", \"statements\": \"ADD COLUMN \\\"Priority\\\" SELECT('High':red, 'Medium':yellow, 'Low':green); ADD COLUMN \\\"Due Date\\\" DATE\"}</example>\n<example description=\"Rename property\">{\"data_source_id\": \"f336d0bc-b841-465b-8045-024475c079dd\", \"statements\": \"RENAME COLUMN \\\"Status\\\" TO \\\"Project Status\\\"\"}</example>\n<example description=\"Remove property\">{\"data_source_id\": \"f336d0bc-b841-465b-8045-024475c079dd\", \"statements\": \"DROP COLUMN \\\"Old Property\\\"\"}</example>\n<example description=\"Add self-relation\">{\"data_source_id\": \"f336d0bc-b841-465b-8045-024475c079dd\", \"statements\": \"ADD COLUMN \\\"Parent\\\" RELATION('f336d0bc-b841-465b-8045-024475c079dd', DUAL 'Children' 'children'); ADD COLUMN \\\"Children\\\" RELATION('f336d0bc-b841-465b-8045-024475c079dd', DUAL 'Parent' 'parent')\"}</example>\n<example description=\"Update title\">{\"data_source_id\": \"f336d0bc-b841-465b-8045-024475c079dd\", \"title\": \"Project Tracker 2024\"}</example>\n<example description=\"Trash data source\">{\"data_source_id\": \"f336d0bc-b841-465b-8045-024475c079dd\", \"in_trash\": true}</example>\n\nNotes: Cannot delete/create title properties. Max one unique_id property.\nCannot update synced databases. Use \"fetch\" first to see current schema\nand get the data source ID from <data-source url=\"collection://...\"> tags."
                          }
                        },
                        "required": [
                          "type",
                          "update_data_source"
                        ],
                        "title": "Update Data Source"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "create_comment",
                            "description": "The name of the tool to run."
                          },
                          "create_comment": {
                            "type": "object",
                            "properties": {
                              "rich_text": {
                                "type": "array",
                                "items": {
                                  "$ref": "#/components/schemas/richTextItemRequest"
                                },
                                "maxItems": 100,
                                "description": "An array of rich text objects that represent the content of the comment."
                              },
                              "page_id": {
                                "type": "string",
                                "description": "The ID of the page to comment on (with or without dashes)."
                              },
                              "discussion_id": {
                                "type": "string",
                                "description": "The ID or URL of an existing discussion to reply to (e.g., discussion://pageId/blockId/discussionId)."
                              },
                              "selection_with_ellipsis": {
                                "type": "string",
                                "description": "Unique start and end snippet of the content to comment on.\nDO NOT provide the entire string. Instead, provide up to the first ~10 characters, an ellipsis, and then up to the last ~10 characters.\nMake sure you provide enough of the start and end snippet to uniquely identify the content.\nFor example: \"# Section heading...last paragraph.\""
                              }
                            },
                            "required": [
                              "rich_text",
                              "page_id"
                            ],
                            "description": "The parameters for the create_comment tool. Add a comment to a page or specific content.\n\nCreates a new comment. Provide `page_id` to identify the page, then choose ONE targeting mode:\n- `page_id` alone: Page-level comment on the entire page\n- `page_id` + `selection_with_ellipsis`: Comment on specific block content\n- `discussion_id`: Reply to an existing discussion thread (page_id is still required)\n\nFor content targeting, use `selection_with_ellipsis` with ~10 chars from start and end: \"# Section Ti...tle content\"\n\n<example description=\"Page-level comment\">\n{\"page_id\": \"uuid\", \"rich_text\": [{\"text\": {\"content\": \"Comment\"}}]}\n</example>\n<example description=\"Comment on specific content\">\n{\"page_id\": \"uuid\", \"selection_with_ellipsis\": \"# Meeting No...es heading\",\n \"rich_text\": [{\"text\": {\"content\": \"Comment on this section\"}}]}\n</example>\n<example description=\"Reply to discussion\">\n{\"page_id\": \"uuid\", \"discussion_id\": \"discussion://pageId/blockId/discussionId\",\n \"rich_text\": [{\"text\": {\"content\": \"Reply\"}}]}\n</example>"
                          }
                        },
                        "required": [
                          "type",
                          "create_comment"
                        ],
                        "title": "Create Comment"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "get_comments",
                            "description": "The name of the tool to run."
                          },
                          "get_comments": {
                            "type": "object",
                            "properties": {
                              "page_id": {
                                "type": "string",
                                "description": "Identifier for a Notion page."
                              },
                              "include_resolved": {
                                "type": "boolean",
                                "description": "Include resolved discussions in the response. Defaults to false."
                              },
                              "include_all_blocks": {
                                "type": "boolean",
                                "description": "Include discussions on child blocks, not just page-level discussions. Defaults to false."
                              },
                              "discussion_id": {
                                "type": "string",
                                "description": "Fetch a specific discussion by ID or discussion URL (e.g., discussion://pageId/blockId/discussionId)."
                              }
                            },
                            "required": [
                              "page_id"
                            ],
                            "description": "The parameters for the get_comments tool. Get comments and discussions from a Notion page.\n\nReturns discussions with full comment content in XML format.\nBy default, returns page-level discussions only.\n\nTip: Use the `fetch` tool with `include_discussions: true` first to see where discussions\nare anchored in the page content, then use this tool to retrieve full discussion threads.\nThe `discussion://` URLs in the fetch output match the discussion IDs returned here.\n\nParameters:\n- `include_all_blocks`: Include discussions on child blocks (default: false)\n- `include_resolved`: Include resolved discussions (default: false)\n- `discussion_id`: Fetch a specific discussion by ID or URL\n\n<example>{\"page_id\": \"page-uuid\"}</example>\n<example>{\"page_id\": \"page-uuid\", \"include_all_blocks\": true}</example>\n<example>{\"page_id\": \"page-uuid\", \"discussion_id\": \"discussion://pageId/blockId/discussionId\"}</example>"
                          }
                        },
                        "required": [
                          "type",
                          "get_comments"
                        ],
                        "title": "Get Comments"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "get_teams",
                            "description": "The name of the tool to run."
                          },
                          "get_teams": {
                            "type": "object",
                            "properties": {
                              "query": {
                                "type": "string",
                                "minLength": 1,
                                "maxLength": 100,
                                "description": "Optional search query to filter teams by name (case-insensitive)."
                              }
                            },
                            "description": "The parameters for the get_teams tool. Retrieves a list of teams (teamspaces) in the current workspace. Shows which teams\nexist, user membership status, IDs, names, and roles.\n\nTeams are returned split by membership status and limited to a maximum of\n10 results.\n\n<examples>\n1. List all teams (up to the limit of each type): {}\n\n2. Search for teams by name: {\"query\": \"engineering\"}\n\n3. Find a specific team: {\"query\": \"Product Design\"}\n</examples>"
                          }
                        },
                        "required": [
                          "type",
                          "get_teams"
                        ],
                        "title": "Get Teams"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "get_users",
                            "description": "The name of the tool to run."
                          },
                          "get_users": {
                            "type": "object",
                            "properties": {
                              "query": {
                                "type": "string",
                                "minLength": 1,
                                "maxLength": 100,
                                "description": "Optional search query to filter users by name or email (case-insensitive)."
                              },
                              "start_cursor": {
                                "type": "string",
                                "minLength": 1,
                                "maxLength": 100,
                                "description": "Cursor for pagination. Use the next_cursor value from the previous response to get the next page."
                              },
                              "page_size": {
                                "type": "integer",
                                "minimum": 1,
                                "maximum": 100,
                                "description": "Number of users to return per page (default: 100, max: 100)."
                              },
                              "user_id": {
                                "type": "string",
                                "minLength": 1,
                                "maxLength": 100,
                                "description": "Return only the user matching this ID. Pass \"self\" to fetch the current user."
                              }
                            },
                            "description": "The parameters for the get_users tool. Retrieves a list of users in the current workspace. Shows workspace members\nand guests with their IDs, names, emails (if available), and types (person or bot).\n\nSupports cursor-based pagination to iterate through all users in the workspace.\n\n<examples>\n1. List all users (first page): {}\n\n2. Search for users by name or email: {\"query\": \"john\"}\n\n3. Get next page of results: {\"start_cursor\": \"abc123\"}\n\n4. Set custom page size: {\"page_size\": 20}\n\n5. Fetch a specific user by ID: {\"user_id\": \"00000000-0000-4000-8000-000000000000\"}\n\n6. Fetch the current user: {\"user_id\": \"self\"}\n</examples>"
                          }
                        },
                        "required": [
                          "type",
                          "get_users"
                        ],
                        "title": "Get Users"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "answer_question",
                            "description": "The name of the tool to run."
                          },
                          "answer_question": {
                            "type": "object",
                            "properties": {
                              "question": {
                                "type": "string",
                                "minLength": 1,
                                "maxLength": 2000,
                                "description": "Text containing a question about your Notion workspace content"
                              }
                            },
                            "required": [
                              "question"
                            ],
                            "description": "The parameters for the answer_question tool. Provides an AI-powered answer to questions about content in your Notion workspace.\nUses natural language understanding to find relevant information and synthesize a\ncomprehensive answer.\n\nUse when you need:\n- Direct answers to questions about workspace content\n- Synthesis of information from multiple sources\n- Natural language explanations of concepts or data\n\nMore focused than the search tool; provides one condensed answer, not a list of\nsearch results."
                          }
                        },
                        "required": [
                          "type",
                          "answer_question"
                        ],
                        "title": "Answer Question"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "query_data_sources",
                            "description": "The name of the tool to run."
                          },
                          "query_data_sources": {
                            "type": "object",
                            "properties": {
                              "data": {
                                "oneOf": [
                                  {
                                    "type": "object",
                                    "properties": {
                                      "data_source_urls": {
                                        "type": "array",
                                        "items": {
                                          "type": "string"
                                        },
                                        "maxItems": 100,
                                        "description": "Array of data source URLs to query. These are obtained from the fetch tool\nin the format: collection://f336d0bc-b841-465b-8045-024475c079dd"
                                      },
                                      "query": {
                                        "type": "string",
                                        "description": "SQLite query to execute against the data sources.\nUse the data source URL as the table name in your query.\nExample: SELECT * FROM \"collection://...\" WHERE ..."
                                      },
                                      "mode": {
                                        "type": "string",
                                        "const": "sql",
                                        "description": "Optional mode parameter. Defaults to 'sql' if not specified."
                                      },
                                      "params": {
                                        "type": "array",
                                        "items": {
                                          "type": "string"
                                        },
                                        "maxItems": 100,
                                        "description": "Optional array of parameter values for parameterized queries.\nFor example, if query contains WHERE status = ?, provide the value here.\nUse \"__YES__\" for checked checkboxes and \"__NO__\" for unchecked checkboxes."
                                      }
                                    },
                                    "required": [
                                      "data_source_urls",
                                      "query"
                                    ],
                                    "title": "Sql"
                                  },
                                  {
                                    "type": "object",
                                    "properties": {
                                      "mode": {
                                        "type": "string",
                                        "const": "view",
                                        "description": "Mode for executing a database view's existing query"
                                      },
                                      "view_url": {
                                        "type": "string",
                                        "description": "URL of a specific database view to query.\nExample: https://www.notion.so/workspace/db-id?v=view-id"
                                      }
                                    },
                                    "required": [
                                      "mode",
                                      "view_url"
                                    ],
                                    "title": "View"
                                  }
                                ],
                                "description": "The data required for querying data sources"
                              }
                            },
                            "required": [
                              "data"
                            ],
                            "description": "The parameters for the query_data_sources tool. Query data from Notion databases using SQL or by specifying a view.\n\nBy default, uses SQL mode to execute SQLite queries across one or more data sources.\nAlternatively, use view mode to execute a database view's existing filters and sorts.\n\nPrerequisites:\n1. Use the \"fetch\" tool first to get database schema and data source URLs\n2. Data source URLs are found in <data-source url=\"...\"> tags in fetch results\n\nSQL mode (default):\nExecute custom SQLite queries across one or more data sources.\n- Use data source URLs as table names in your query\n- Supports parameterized queries for security\n- Checkbox values: use \"__YES__\" for checked, \"__NO__\" for unchecked\n\nExamples:\n1. Simple query without explicit mode (defaults to SQL):\n{\n  \"data\": {\n    \"data_source_urls\": [\"collection://f336d0bc-b841-465b-8045-024475c079dd\"],\n    \"query\": \"SELECT * FROM \\\"collection://f336d0bc-b841-465b-8045-024475c079dd\\\" LIMIT 10\"\n  }\n}\n\n2. Query with parameters:\n{\n  \"data\": {\n    \"mode\": \"sql\",\n    \"data_source_urls\": [\"collection://abc123\"],\n    \"query\": \"SELECT * FROM \\\"collection://abc123\\\" WHERE Status = ? AND Priority = ?\",\n    \"params\": [\"In Progress\", \"High\"]\n  }\n}\n\n3. Query checkboxes:\n{\n  \"data\": {\n    \"data_source_urls\": [\"collection://def456\"],\n    \"query\": \"SELECT * FROM \\\"collection://def456\\\" WHERE Completed = ?\",\n    \"params\": [\"__YES__\"]\n  }\n}\n\nView mode:\nExecute a specific database view's query with its filters and sorts.\n\nExample:\n{\n  \"data\": {\n    \"mode\": \"view\",\n    \"view_url\": \"https://www.notion.so/workspace/Tasks-DB-abc123?v=def456\"\n  }\n}\n\nCommon use cases:\n- Aggregate data across databases\n- Filter records by complex conditions\n- Export data for analysis\n- Validate data quality\n- Generate reports from database content"
                          }
                        },
                        "required": [
                          "type",
                          "query_data_sources"
                        ],
                        "title": "Query Data Sources"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "query_database_view",
                            "description": "The name of the tool to run."
                          },
                          "query_database_view": {
                            "type": "object",
                            "properties": {
                              "view_url": {
                                "type": "string",
                                "description": "URL of a specific database view to query.\nExample: https://www.notion.so/workspace/db-id?v=view-id"
                              }
                            },
                            "required": [
                              "view_url"
                            ],
                            "description": "The parameters for the query_database_view tool. Query data from a Notion database view.\n\nExecutes a database view's existing filters, sorts, and column selections to return matching pages.\n\nPrerequisites:\n1. Use the \"fetch\" tool first to get the database and its view URLs\n2. View URLs are found in database responses, typically in the format:\n   https://www.notion.so/workspace/db-id?v=view-id\n\nExample:\n{\n  \"view_url\": \"https://www.notion.so/workspace/Tasks-DB-abc123?v=def456\"\n}\n\nCommon use cases:\n- Query databases using pre-defined views (filters/sorts already configured), e.g. look for all tickets marked \"In Progress\" in a Tasks DB\n- Export filtered data for analysis\n- Generate reports from database content"
                          }
                        },
                        "required": [
                          "type",
                          "query_database_view"
                        ],
                        "title": "Query Database View"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "query_meeting_notes",
                            "description": "The name of the tool to run."
                          },
                          "query_meeting_notes": {
                            "type": "object",
                            "properties": {
                              "filter": {
                                "type": "object",
                                "properties": {
                                  "operator": {
                                    "type": "string",
                                    "enum": [
                                      "and",
                                      "or"
                                    ],
                                    "description": "Operator for combinator filters."
                                  },
                                  "filters": {
                                    "type": "array",
                                    "items": {
                                      "description": "Meeting notes filter node (combinator or property filter).",
                                      "anyOf": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "operator": {
                                              "type": "string",
                                              "enum": [
                                                "and",
                                                "or"
                                              ],
                                              "description": "Operator for nested combinator filters."
                                            },
                                            "filters": {
                                              "type": "array",
                                              "items": {
                                                "anyOf": [
                                                  {
                                                    "type": "object",
                                                    "properties": {
                                                      "property": {
                                                        "type": "string",
                                                        "description": "Property name."
                                                      },
                                                      "filter": {
                                                        "type": "object",
                                                        "properties": {
                                                          "operator": {
                                                            "type": "string",
                                                            "description": "Operator."
                                                          },
                                                          "value": {
                                                            "description": "Value for the operator.",
                                                            "anyOf": [
                                                              {
                                                                "type": "object",
                                                                "description": "Single date/datetime filter value.",
                                                                "properties": {
                                                                  "type": {
                                                                    "type": "string",
                                                                    "enum": [
                                                                      "relative",
                                                                      "exact"
                                                                    ]
                                                                  },
                                                                  "value": {
                                                                    "anyOf": [
                                                                      {
                                                                        "type": "string"
                                                                      },
                                                                      {
                                                                        "type": "object",
                                                                        "properties": {
                                                                          "type": {
                                                                            "type": "string",
                                                                            "enum": [
                                                                              "date",
                                                                              "datetime"
                                                                            ]
                                                                          },
                                                                          "start_date": {
                                                                            "type": "string"
                                                                          },
                                                                          "start_time": {
                                                                            "type": "string"
                                                                          },
                                                                          "time_zone": {
                                                                            "type": "string"
                                                                          }
                                                                        },
                                                                        "required": [
                                                                          "type",
                                                                          "start_date"
                                                                        ]
                                                                      }
                                                                    ]
                                                                  }
                                                                },
                                                                "required": [
                                                                  "type",
                                                                  "value"
                                                                ]
                                                              },
                                                              {
                                                                "type": "object",
                                                                "description": "Date range filter value.",
                                                                "properties": {
                                                                  "type": {
                                                                    "type": "string",
                                                                    "enum": [
                                                                      "relative",
                                                                      "exact"
                                                                    ]
                                                                  },
                                                                  "value": {
                                                                    "anyOf": [
                                                                      {
                                                                        "type": "string"
                                                                      },
                                                                      {
                                                                        "type": "object",
                                                                        "properties": {
                                                                          "type": {
                                                                            "type": "string",
                                                                            "enum": [
                                                                              "daterange"
                                                                            ]
                                                                          },
                                                                          "start_date": {
                                                                            "type": "string"
                                                                          },
                                                                          "end_date": {
                                                                            "type": "string"
                                                                          }
                                                                        },
                                                                        "required": [
                                                                          "type",
                                                                          "start_date"
                                                                        ]
                                                                      }
                                                                    ]
                                                                  },
                                                                  "direction": {
                                                                    "type": "string",
                                                                    "enum": [
                                                                      "past",
                                                                      "future"
                                                                    ]
                                                                  },
                                                                  "unit": {
                                                                    "type": "string",
                                                                    "enum": [
                                                                      "day",
                                                                      "week",
                                                                      "month",
                                                                      "year"
                                                                    ]
                                                                  },
                                                                  "count": {
                                                                    "type": "number"
                                                                  }
                                                                },
                                                                "required": [
                                                                  "type",
                                                                  "value"
                                                                ]
                                                              },
                                                              {
                                                                "type": "object",
                                                                "description": "Text filter value for string_contains and similar operators.",
                                                                "properties": {
                                                                  "type": {
                                                                    "type": "string",
                                                                    "enum": [
                                                                      "exact"
                                                                    ]
                                                                  },
                                                                  "value": {
                                                                    "type": "string",
                                                                    "description": "The text value to filter on."
                                                                  }
                                                                },
                                                                "required": [
                                                                  "type",
                                                                  "value"
                                                                ]
                                                              },
                                                              {
                                                                "type": "array",
                                                                "description": "Array of person references for person_contains/person_does_not_contain filters.",
                                                                "items": {
                                                                  "type": "object",
                                                                  "properties": {
                                                                    "type": {
                                                                      "type": "string",
                                                                      "enum": [
                                                                        "exact"
                                                                      ]
                                                                    },
                                                                    "value": {
                                                                      "type": "object",
                                                                      "properties": {
                                                                        "table": {
                                                                          "type": "string",
                                                                          "enum": [
                                                                            "notion_user"
                                                                          ]
                                                                        },
                                                                        "id": {
                                                                          "type": "string"
                                                                        }
                                                                      },
                                                                      "required": [
                                                                        "table",
                                                                        "id"
                                                                      ]
                                                                    }
                                                                  },
                                                                  "required": [
                                                                    "type",
                                                                    "value"
                                                                  ]
                                                                }
                                                              }
                                                            ]
                                                          }
                                                        },
                                                        "required": [
                                                          "operator"
                                                        ]
                                                      }
                                                    },
                                                    "required": [
                                                      "property",
                                                      "filter"
                                                    ]
                                                  },
                                                  {
                                                    "type": "object",
                                                    "properties": {
                                                      "operator": {
                                                        "type": "string",
                                                        "enum": [
                                                          "and",
                                                          "or"
                                                        ],
                                                        "description": "Operator for nested combinator filters."
                                                      },
                                                      "filters": {
                                                        "type": "array",
                                                        "items": {
                                                          "anyOf": [
                                                            {
                                                              "type": "object",
                                                              "properties": {
                                                                "property": {
                                                                  "type": "string",
                                                                  "description": "Property name."
                                                                },
                                                                "filter": {
                                                                  "type": "object",
                                                                  "properties": {
                                                                    "operator": {
                                                                      "type": "string",
                                                                      "description": "Operator."
                                                                    },
                                                                    "value": {
                                                                      "description": "Value for the operator.",
                                                                      "anyOf": [
                                                                        {
                                                                          "type": "object",
                                                                          "description": "Single date/datetime filter value.",
                                                                          "properties": {
                                                                            "type": {
                                                                              "type": "string",
                                                                              "enum": [
                                                                                "relative",
                                                                                "exact"
                                                                              ]
                                                                            },
                                                                            "value": {
                                                                              "anyOf": [
                                                                                {
                                                                                  "type": "string"
                                                                                },
                                                                                {
                                                                                  "type": "object",
                                                                                  "properties": {
                                                                                    "type": {
                                                                                      "type": "string",
                                                                                      "enum": [
                                                                                        "date",
                                                                                        "datetime"
                                                                                      ]
                                                                                    },
                                                                                    "start_date": {
                                                                                      "type": "string"
                                                                                    },
                                                                                    "start_time": {
                                                                                      "type": "string"
                                                                                    },
                                                                                    "time_zone": {
                                                                                      "type": "string"
                                                                                    }
                                                                                  },
                                                                                  "required": [
                                                                                    "type",
                                                                                    "start_date"
                                                                                  ]
                                                                                }
                                                                              ]
                                                                            }
                                                                          },
                                                                          "required": [
                                                                            "type",
                                                                            "value"
                                                                          ]
                                                                        },
                                                                        {
                                                                          "type": "object",
                                                                          "description": "Date range filter value.",
                                                                          "properties": {
                                                                            "type": {
                                                                              "type": "string",
                                                                              "enum": [
                                                                                "relative",
                                                                                "exact"
                                                                              ]
                                                                            },
                                                                            "value": {
                                                                              "anyOf": [
                                                                                {
                                                                                  "type": "string"
                                                                                },
                                                                                {
                                                                                  "type": "object",
                                                                                  "properties": {
                                                                                    "type": {
                                                                                      "type": "string",
                                                                                      "enum": [
                                                                                        "daterange"
                                                                                      ]
                                                                                    },
                                                                                    "start_date": {
                                                                                      "type": "string"
                                                                                    },
                                                                                    "end_date": {
                                                                                      "type": "string"
                                                                                    }
                                                                                  },
                                                                                  "required": [
                                                                                    "type",
                                                                                    "start_date"
                                                                                  ]
                                                                                }
                                                                              ]
                                                                            },
                                                                            "direction": {
                                                                              "type": "string",
                                                                              "enum": [
                                                                                "past",
                                                                                "future"
                                                                              ]
                                                                            },
                                                                            "unit": {
                                                                              "type": "string",
                                                                              "enum": [
                                                                                "day",
                                                                                "week",
                                                                                "month",
                                                                                "year"
                                                                              ]
                                                                            },
                                                                            "count": {
                                                                              "type": "number"
                                                                            }
                                                                          },
                                                                          "required": [
                                                                            "type",
                                                                            "value"
                                                                          ]
                                                                        },
                                                                        {
                                                                          "type": "object",
                                                                          "description": "Text filter value for string_contains and similar operators.",
                                                                          "properties": {
                                                                            "type": {
                                                                              "type": "string",
                                                                              "enum": [
                                                                                "exact"
                                                                              ]
                                                                            },
                                                                            "value": {
                                                                              "type": "string",
                                                                              "description": "The text value to filter on."
                                                                            }
                                                                          },
                                                                          "required": [
                                                                            "type",
                                                                            "value"
                                                                          ]
                                                                        },
                                                                        {
                                                                          "type": "array",
                                                                          "description": "Array of person references for person_contains/person_does_not_contain filters.",
                                                                          "items": {
                                                                            "type": "object",
                                                                            "properties": {
                                                                              "type": {
                                                                                "type": "string",
                                                                                "enum": [
                                                                                  "exact"
                                                                                ]
                                                                              },
                                                                              "value": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                  "table": {
                                                                                    "type": "string",
                                                                                    "enum": [
                                                                                      "notion_user"
                                                                                    ]
                                                                                  },
                                                                                  "id": {
                                                                                    "type": "string"
                                                                                  }
                                                                                },
                                                                                "required": [
                                                                                  "table",
                                                                                  "id"
                                                                                ]
                                                                              }
                                                                            },
                                                                            "required": [
                                                                              "type",
                                                                              "value"
                                                                            ]
                                                                          }
                                                                        }
                                                                      ]
                                                                    }
                                                                  },
                                                                  "required": [
                                                                    "operator"
                                                                  ]
                                                                }
                                                              },
                                                              "required": [
                                                                "property",
                                                                "filter"
                                                              ]
                                                            }
                                                          ]
                                                        }
                                                      }
                                                    },
                                                    "required": [
                                                      "operator",
                                                      "filters"
                                                    ]
                                                  }
                                                ]
                                              },
                                              "description": "Nested filters for combinator filters."
                                            }
                                          },
                                          "required": [
                                            "operator",
                                            "filters"
                                          ]
                                        },
                                        {
                                          "type": "object",
                                          "properties": {
                                            "property": {
                                              "type": "string",
                                              "description": "Property name."
                                            },
                                            "filter": {
                                              "type": "object",
                                              "properties": {
                                                "operator": {
                                                  "type": "string",
                                                  "description": "Operator."
                                                },
                                                "value": {
                                                  "description": "Value for the operator.",
                                                  "anyOf": [
                                                    {
                                                      "type": "object",
                                                      "description": "Single date/datetime filter value.",
                                                      "properties": {
                                                        "type": {
                                                          "type": "string",
                                                          "enum": [
                                                            "relative",
                                                            "exact"
                                                          ]
                                                        },
                                                        "value": {
                                                          "anyOf": [
                                                            {
                                                              "type": "string"
                                                            },
                                                            {
                                                              "type": "object",
                                                              "properties": {
                                                                "type": {
                                                                  "type": "string",
                                                                  "enum": [
                                                                    "date",
                                                                    "datetime"
                                                                  ]
                                                                },
                                                                "start_date": {
                                                                  "type": "string"
                                                                },
                                                                "start_time": {
                                                                  "type": "string"
                                                                },
                                                                "time_zone": {
                                                                  "type": "string"
                                                                }
                                                              },
                                                              "required": [
                                                                "type",
                                                                "start_date"
                                                              ]
                                                            }
                                                          ]
                                                        }
                                                      },
                                                      "required": [
                                                        "type",
                                                        "value"
                                                      ]
                                                    },
                                                    {
                                                      "type": "object",
                                                      "description": "Date range filter value.",
                                                      "properties": {
                                                        "type": {
                                                          "type": "string",
                                                          "enum": [
                                                            "relative",
                                                            "exact"
                                                          ]
                                                        },
                                                        "value": {
                                                          "anyOf": [
                                                            {
                                                              "type": "string"
                                                            },
                                                            {
                                                              "type": "object",
                                                              "properties": {
                                                                "type": {
                                                                  "type": "string",
                                                                  "enum": [
                                                                    "daterange"
                                                                  ]
                                                                },
                                                                "start_date": {
                                                                  "type": "string"
                                                                },
                                                                "end_date": {
                                                                  "type": "string"
                                                                }
                                                              },
                                                              "required": [
                                                                "type",
                                                                "start_date"
                                                              ]
                                                            }
                                                          ]
                                                        },
                                                        "direction": {
                                                          "type": "string",
                                                          "enum": [
                                                            "past",
                                                            "future"
                                                          ]
                                                        },
                                                        "unit": {
                                                          "type": "string",
                                                          "enum": [
                                                            "day",
                                                            "week",
                                                            "month",
                                                            "year"
                                                          ]
                                                        },
                                                        "count": {
                                                          "type": "number"
                                                        }
                                                      },
                                                      "required": [
                                                        "type",
                                                        "value"
                                                      ]
                                                    },
                                                    {
                                                      "type": "object",
                                                      "description": "Text filter value for string_contains and similar operators.",
                                                      "properties": {
                                                        "type": {
                                                          "type": "string",
                                                          "enum": [
                                                            "exact"
                                                          ]
                                                        },
                                                        "value": {
                                                          "type": "string",
                                                          "description": "The text value to filter on."
                                                        }
                                                      },
                                                      "required": [
                                                        "type",
                                                        "value"
                                                      ]
                                                    },
                                                    {
                                                      "type": "array",
                                                      "description": "Array of person references for person_contains/person_does_not_contain filters.",
                                                      "items": {
                                                        "type": "object",
                                                        "properties": {
                                                          "type": {
                                                            "type": "string",
                                                            "enum": [
                                                              "exact"
                                                            ]
                                                          },
                                                          "value": {
                                                            "type": "object",
                                                            "properties": {
                                                              "table": {
                                                                "type": "string",
                                                                "enum": [
                                                                  "notion_user"
                                                                ]
                                                              },
                                                              "id": {
                                                                "type": "string"
                                                              }
                                                            },
                                                            "required": [
                                                              "table",
                                                              "id"
                                                            ]
                                                          }
                                                        },
                                                        "required": [
                                                          "type",
                                                          "value"
                                                        ]
                                                      }
                                                    }
                                                  ]
                                                }
                                              },
                                              "required": [
                                                "operator"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "property",
                                            "filter"
                                          ]
                                        }
                                      ]
                                    },
                                    "maxItems": 100,
                                    "description": "Nested filters; each may be a combinator (and/or) or property filter."
                                  }
                                },
                                "required": [
                                  "operator"
                                ],
                                "description": "Acceptable filter for querying current user's meeting notes data source."
                              }
                            },
                            "description": "The parameters for the query_meeting_notes tool. Query the current user's meeting notes data source.\n\nApplies a filter over meeting note properties. Title keyword searching is done via filter on property \"title\" (e.g. string_contains).\nTitle keyword matching is case-insensitive; capitalization does not matter.\nReturns up to 50 rows of matching meeting notes.\n\nPrerequisites:\n1. Use the \"search\" tool to find people IDs if you need to filter by attendees\n\nQuery building:\n- Ignore terms semantically related to meeting outputs (e.g. \"summaries\", \"notes\", \"todos\", \"action items\", \"deliverables\"). These signal the user wants outcomes from their meetings, not a title filter.\n- For example, \"what are my meeting todos?\" means filter meetings and find action items — do NOT add a title filter for \"todos\".\n- Only add a title filter when confident the user is targeting a specific meeting title (e.g. \"standup\", \"sprint planning\", \"1:1 with Alice\").\n- Generic date phrases like \"recent meetings\", \"latest meetings\", \"meetings this week\", or \"yesterday's meetings\" should be interpreted as date range filters — never as title filters.\n- If a filter returns no results, simplify to a single term. The system is lexical, so multi-word title filters may not match.\n- Unless a user explicitly asks about a meeting titled with another user's name, assume they're referring to attendees or creators. Only add a title filter with a person's name as a fallback if attendee filtering returns no results.\n\nDefault behavior:\n- This tool by default returns meeting notes where the current user is an attendee or creator. There is no need to add a filter for the current user.\n\nFilterable properties:\n- \"title\" (text) — meeting title\n- \"notion://meeting_notes/attendees\" (person) — meeting attendees\n- \"created_time\" (date) — when the meeting note was created\n- \"created_by\" (person) — who created the meeting note\n- \"last_edited_time\" (date) — when the meeting note was last edited\n- \"last_edited_by\" (person) — who last edited the meeting note\n\nCombinator filters use \"filters\" (not \"operands\"):\n{\n  \"operator\": \"and\" | \"or\",\n  \"filters\": [ ... ]\n}\n\nDate filtering (recommended default: date_is_within):\n- Prefer \"date_is_within\" for relative windows like \"past N days/weeks/months\".\n- Relative (common): { type: \"relative\", value: \"the_past_week\" | \"the_past_month\" | \"this_week\" }\n- Relative (custom): { type: \"relative\", value: \"custom\", direction: \"past\" | \"future\", unit: \"day\" | \"week\" | \"month\" | \"year\", count: <number> }\n- Exact range: { type: \"exact\", value: { type: \"daterange\", start_date: \"YYYY-MM-DD\", end_date: \"YYYY-MM-DD\" } }\n- Single-date operators (\"date_is\", \"date_is_before\", \"date_is_after\", \"date_is_on_or_before\", \"date_is_on_or_after\"):\n  - Exact: { type: \"exact\", value: { type: \"date\", start_date: \"YYYY-MM-DD\" } }\n  - Relative shortcuts: today | tomorrow | yesterday | one_week_ago | one_week_from_now | one_month_ago | one_month_from_now\n\nTitle keyword filtering (OR vs AND):\n- Use OR (\"operator\": \"or\") when unsure or for broad discovery.\n- Use AND (\"operator\": \"and\") when the user is specific and you want to narrow results.\n- Break multi-word phrases into individual terms and filter on each term separately.\n\nExample 1: Filter meetings from the past week (relative):\n{\n  \"filter\": {\n    \"operator\": \"and\",\n    \"filters\": [\n      {\n        \"property\": \"created_time\",\n        \"filter\": {\n          \"operator\": \"date_is_within\",\n          \"value\": { \"type\": \"relative\", \"value\": \"the_past_week\" }\n        }\n      }\n    ]\n  }\n}\n\nExample 2: Filter meetings from the past 3 days (custom relative):\n{\n  \"filter\": {\n    \"operator\": \"and\",\n    \"filters\": [\n      {\n        \"property\": \"created_time\",\n        \"filter\": {\n          \"operator\": \"date_is_within\",\n          \"value\": { \"type\": \"relative\", \"value\": \"custom\", \"direction\": \"past\", \"unit\": \"day\", \"count\": 3 }\n        }\n      }\n    ]\n  }\n}\n\nExample 3: Filter meetings by exact date range:\n{\n  \"filter\": {\n    \"operator\": \"and\",\n    \"filters\": [\n      {\n        \"property\": \"created_time\",\n        \"filter\": {\n          \"operator\": \"date_is_within\",\n          \"value\": { \"type\": \"exact\", \"value\": { \"type\": \"daterange\", \"start_date\": \"2025-01-01\", \"end_date\": \"2025-12-31\" } }\n        }\n      }\n    ]\n  }\n}\n\nExample 4: Filter meetings created after a specific date:\n{\n  \"filter\": {\n    \"operator\": \"and\",\n    \"filters\": [\n      {\n        \"property\": \"created_time\",\n        \"filter\": {\n          \"operator\": \"date_is_after\",\n          \"value\": { \"type\": \"exact\", \"value\": { \"type\": \"date\", \"start_date\": \"2025-06-01\" } }\n        }\n      }\n    ]\n  }\n}\n\nExample 5: Filter meetings by a specific attendee (use \"search\" tool first to get user ID):\n{\n  \"filter\": {\n    \"operator\": \"and\",\n    \"filters\": [\n      {\n        \"property\": \"notion://meeting_notes/attendees\",\n        \"filter\": {\n          \"operator\": \"person_contains\",\n          \"value\": [\n            { \"type\": \"exact\", \"value\": { \"table\": \"notion_user\", \"id\": \"a1b2c3d4-e5f6-7890-abcd-ef1234567890\" } }\n          ]\n        }\n      }\n    ]\n  }\n}\n\nExample 6: Combine attendees with date range:\n{\n  \"filter\": {\n    \"operator\": \"and\",\n    \"filters\": [\n      {\n        \"property\": \"created_time\",\n        \"filter\": {\n          \"operator\": \"date_is_on_or_after\",\n          \"value\": { \"type\": \"exact\", \"value\": { \"type\": \"date\", \"start_date\": \"2025-01-01\" } }\n        }\n      },\n      {\n        \"property\": \"created_time\",\n        \"filter\": {\n          \"operator\": \"date_is_on_or_before\",\n          \"value\": { \"type\": \"exact\", \"value\": { \"type\": \"date\", \"start_date\": \"2025-01-31\" } }\n        }\n      },\n      {\n        \"property\": \"notion://meeting_notes/attendees\",\n        \"filter\": {\n          \"operator\": \"person_contains\",\n          \"value\": [\n            { \"type\": \"exact\", \"value\": { \"table\": \"notion_user\", \"id\": \"a1b2c3d4-e5f6-7890-abcd-ef1234567890\" } }\n          ]\n        }\n      }\n    ]\n  }\n}\n\nExample 7: Filter meetings by title content:\n{\n  \"filter\": {\n    \"operator\": \"and\",\n    \"filters\": [\n      {\n        \"property\": \"title\",\n        \"filter\": {\n          \"operator\": \"string_contains\",\n          \"value\": { \"type\": \"exact\", \"value\": \"design review\" }\n        }\n      }\n    ]\n  }\n}\n\nExample 8: Filter meetings matching any of several title terms (using \"or\"):\n{\n  \"filter\": {\n    \"operator\": \"or\",\n    \"filters\": [\n      {\n        \"property\": \"title\",\n        \"filter\": {\n          \"operator\": \"string_contains\",\n          \"value\": { \"type\": \"exact\", \"value\": \"standup\" }\n        }\n      },\n      {\n        \"property\": \"title\",\n        \"filter\": {\n          \"operator\": \"string_contains\",\n          \"value\": { \"type\": \"exact\", \"value\": \"sync\" }\n        }\n      }\n    ]\n  }\n}"
                          }
                        },
                        "required": [
                          "type",
                          "query_meeting_notes"
                        ],
                        "title": "Query Meeting Notes"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "list_agents",
                            "description": "The name of the tool to run."
                          },
                          "list_agents": {
                            "type": "object",
                            "properties": {
                              "query": {
                                "type": "string",
                                "minLength": 1,
                                "maxLength": 100,
                                "description": "Optional search query to filter agents by name or description (case-insensitive)."
                              }
                            },
                            "description": "The parameters for the list_agents tool. Retrieves a list of all custom agents (workflows) that the authenticated user has access to in the current workspace.\nThis tool provides visibility into available agents including their names, IDs, descriptions, and system instructions.\n\nThe returned data includes:\n- Agent ID (for use with the chat tool)\n- Agent name\n- Agent description\n- Agent system instructions\n\n<examples>\n1. List all available agents: {}\n\n2. Search for agents by name or description: {\"query\": \"customer support\"}\n\n3. Find agents related to a specific topic: {\"query\": \"data analysis\"}\n</examples>"
                          }
                        },
                        "required": [
                          "type",
                          "list_agents"
                        ],
                        "title": "List Agents"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "chat",
                            "description": "The name of the tool to run."
                          },
                          "chat": {
                            "type": "object",
                            "properties": {
                              "agent_id": {
                                "type": "string",
                                "minLength": 1,
                                "description": "The unique identifier of the custom agent to chat with. This should be the\nagent ID of the custom agent you want to interact with. The agent must\nbe accessible to your workspace and have appropriate permissions.\n\nSupports both UUID formats:\n- With dashes: \"12345678-1234-1234-1234-123456789012\"\n- Without dashes: \"12345678123412341234123456789012\""
                              },
                              "message": {
                                "type": "string",
                                "minLength": 1,
                                "description": "The message to send to the custom agent. This will be processed by the agent\nbased on its configuration, available tools, and conversation context. The\nagent can understand natural language and perform various tasks based on your request."
                              },
                              "session_id": {
                                "type": "string",
                                "description": "Optional session ID to continue an existing conversation. If provided, the\nagent will have access to the previous conversation context and can maintain\ncontinuity across multiple interactions."
                              },
                              "include_transcript": {
                                "type": "boolean",
                                "description": "Whether to include the conversation transcript in the response. Defaults to false.\nWhen true, the response will include the full conversation history for context."
                              },
                              "thread_id": {
                                "type": "string",
                                "description": "Optional thread ID to use for the conversation. If not provided, a new thread\nwill be created. This allows you to reference specific conversation threads\nor continue existing ones."
                              },
                              "sync": {
                                "type": "boolean",
                                "description": "Whether to run the chat in sync mode. Defaults to false (async mode).\nWhen true, the response waits for the agent to complete processing and returns\nthe full response. When false (default), the response is returned immediately\nwith a chat_url and a generic acknowledgement message. The agent processes the\nrequest in the background, and users can continue the conversation from the chat_url."
                              }
                            },
                            "required": [
                              "agent_id",
                              "message"
                            ],
                            "description": "The parameters for the chat tool. Chat with a custom agent using Notion's AI chat system.\n\t\t\n\t\tThis tool provides a conversational interface to interact with custom agents\n\t\tthat can understand context, access Notion data, and perform various tasks.\n\t\tThe agent will process your message and respond based on its configuration,\n\t\tcapabilities, and the conversation context.\n\t\t\n\t\tKey features:\n\t\t- Start new conversations or continue existing ones\n\t\t- Access to Notion workspace data and connected sources\n\t\t- Support for tool use and complex reasoning\n\t\t- Optional conversation history inclusion\n\t\t\n\t\tCRITICAL: The response includes a 'chat_url' field. You MUST ALWAYS render this URL \n\t\tto the user immediately after receiving the response, formatted as a clickable link. \n\t\tThis allows them to continue the conversation directly in Notion's interface.\n\t\t\n\t\tExample format:\n\t\t**Continue the conversation in Notion:** [Chat with Agent](chat_url)\n\t\t\n\t\tExamples:\n\t\t1. Start new conversation:\n\t\t{\n\t\t\t\"agent_id\": \"agent_12345678-1234-1234-1234-123456789012\",\n\t\t\t\"message\": \"Help me create a project plan for our Q4 goals\"\n\t\t}\n\t\t\n\t\t2. Continue existing conversation:\n\t\t{\n\t\t\t\"agent_id\": \"agent_12345678-1234-1234-1234-123456789012\",\n\t\t\t\"message\": \"Can you add a timeline section to that plan?\",\n\t\t\t\"session_id\": \"session_87654321-4321-4321-4321-210987654321\"\n\t\t}\n\t\t\n\t\t3. Include full conversation history:\n\t\t{\n\t\t\t\"agent_id\": \"agent_12345678-1234-1234-1234-123456789012\",\n\t\t\t\"message\": \"Summarize our discussion\",\n\t\t\t\"include_transcript\": true\n\t\t}\n\t\t\n\t\t4. Use sync mode (waits for completion):\n\t\t{\n\t\t\t\"agent_id\": \"agent_12345678-1234-1234-1234-123456789012\",\n\t\t\t\"message\": \"Analyze all our project documents\",\n\t\t\t\"sync\": true\n\t\t}"
                          }
                        },
                        "required": [
                          "type",
                          "chat"
                        ],
                        "title": "Chat"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "create_view",
                            "description": "The name of the tool to run."
                          },
                          "create_view": {
                            "type": "object",
                            "properties": {
                              "database_id": {
                                "type": "string",
                                "description": "The database to create a view in. Accepts a Notion URL or a bare UUID."
                              },
                              "data_source_id": {
                                "type": "string",
                                "description": "The data source (collection) ID. Accepts a collection:// URI from <data-source> tags or a bare UUID."
                              },
                              "name": {
                                "type": "string",
                                "description": "The name of the view."
                              },
                              "type": {
                                "type": "string",
                                "enum": [
                                  "table",
                                  "board",
                                  "list",
                                  "calendar",
                                  "timeline",
                                  "gallery",
                                  "form",
                                  "chart",
                                  "map",
                                  "dashboard"
                                ],
                                "description": "The type of view to create."
                              },
                              "configure": {
                                "type": "string",
                                "description": "View configuration DSL string. Supports FILTER, SORT BY, GROUP BY, CALENDAR BY, TIMELINE BY, MAP BY, CHART, FORM, SHOW, HIDE, COVER, WRAP CELLS, and FREEZE COLUMNS directives. See notion://docs/view-dsl-spec."
                              }
                            },
                            "required": [
                              "database_id",
                              "data_source_id",
                              "name",
                              "type"
                            ],
                            "description": "The parameters for the create_view tool. Create a new view on a Notion database.\n\nUse \"fetch\" first to get the database_id and data_source_id\n(from <data-source> tags in the response).\n\nSupported types: table, board, list, calendar, timeline, gallery, form, chart, map, dashboard.\n\nThe optional \"configure\" param accepts a DSL for filters, sorts, grouping,\nand display options. See the notion://docs/view-dsl-spec resource for full\nsyntax. Key directives:\n- FILTER \"Property\" = \"value\" — filter rows\n- SORT BY \"Property\" ASC — sort rows\n- GROUP BY \"Property\" — group by property (required for board views)\n- CALENDAR BY \"Property\" — date property (required for calendar views)\n- TIMELINE BY \"Start\" TO \"End\" — date range (required for timeline views)\n- MAP BY \"Property\" — location property (required for map views)\n- CHART column|bar|line|donut|number — chart type with optional AGGREGATE, COLOR, HEIGHT, SORT, STACK BY, CAPTION\n- FORM CLOSE|OPEN — close/open form submissions\n- FORM ANONYMOUS true|false — toggle anonymous submissions\n- FORM PERMISSIONS none|reader|editor — set submission permissions\n- SHOW \"Prop1\", \"Prop2\" — set visible properties\n- COVER \"Property\" — cover image property\n\n<example description=\"Table view\">{\"database_id\": \"abc123\", \"data_source_id\": \"def456\", \"name\": \"All Tasks\", \"type\": \"table\"}</example>\n<example description=\"Board grouped by Status\">{\"database_id\": \"abc123\", \"data_source_id\": \"def456\", \"name\": \"Task Board\", \"type\": \"board\", \"configure\": \"GROUP BY \\\"Status\\\"\"}</example>\n<example description=\"Filtered + sorted table\">{\"database_id\": \"abc123\", \"data_source_id\": \"def456\", \"name\": \"Active\", \"type\": \"table\", \"configure\": \"FILTER \\\"Status\\\" = \\\"In Progress\\\"; SORT BY \\\"Due Date\\\" ASC\"}</example>\n<example description=\"Calendar view\">{\"database_id\": \"abc123\", \"data_source_id\": \"def456\", \"name\": \"Calendar\", \"type\": \"calendar\", \"configure\": \"CALENDAR BY \\\"Due Date\\\"\"}</example>\n<example description=\"Dashboard\">{\"database_id\": \"abc123\", \"data_source_id\": \"def456\", \"name\": \"Overview\", \"type\": \"dashboard\"}</example>"
                          }
                        },
                        "required": [
                          "type",
                          "create_view"
                        ],
                        "title": "Create View"
                      },
                      {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "const": "update_view",
                            "description": "The name of the tool to run."
                          },
                          "update_view": {
                            "type": "object",
                            "properties": {
                              "view_id": {
                                "type": "string",
                                "description": "The view to update. Accepts a view:// URI, a Notion URL with ?v= parameter, or a bare UUID."
                              },
                              "name": {
                                "type": "string",
                                "description": "New name for the view."
                              },
                              "configure": {
                                "type": "string",
                                "description": "View configuration DSL string. Supports FILTER, SORT BY, GROUP BY, CALENDAR BY, TIMELINE BY, MAP BY, CHART, FORM, SHOW, HIDE, COVER, WRAP CELLS, FREEZE COLUMNS, and CLEAR directives."
                              }
                            },
                            "required": [
                              "view_id"
                            ],
                            "description": "The parameters for the update_view tool. Update a view's name, filters, sorts, or display configuration.\n\nUse \"fetch\" to get view IDs from database responses. Only include fields\nyou want to change. The \"configure\" param uses the same DSL as create_view.\nUse CLEAR to remove settings:\n- CLEAR FILTER — remove all filters\n- CLEAR SORT — remove all sorts\n- CLEAR GROUP BY — remove grouping\n\nSee notion://docs/view-dsl-spec resource for full syntax.\n\n<example description=\"Rename\">{\"view_id\": \"abc123\", \"name\": \"Sprint Board\"}</example>\n<example description=\"Update filter\">{\"view_id\": \"abc123\", \"configure\": \"FILTER \\\"Status\\\" = \\\"Done\\\"\"}</example>\n<example description=\"Clear filter, add sort\">{\"view_id\": \"abc123\", \"configure\": \"CLEAR FILTER; SORT BY \\\"Created\\\" DESC\"}</example>\n<example description=\"Update grouping\">{\"view_id\": \"abc123\", \"configure\": \"GROUP BY \\\"Priority\\\"; SHOW \\\"Name\\\", \\\"Status\\\"\"}</example>"
                          }
                        },
                        "required": [
                          "type",
                          "update_view"
                        ],
                        "title": "Update View"
                      }
                    ]
                  }
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "oneOf": [
                    {
                      "type": "object",
                      "properties": {
                        "pages": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string"
                              },
                              "url": {
                                "type": "string"
                              },
                              "properties": {
                                "type": "object",
                                "additionalProperties": {
                                  "oneOf": [
                                    {
                                      "type": "string"
                                    },
                                    {
                                      "type": "number"
                                    },
                                    {
                                      "type": "null"
                                    }
                                  ]
                                }
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "id",
                              "url",
                              "properties"
                            ]
                          },
                          "maxItems": 100
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "pages"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "page_id": {
                          "$ref": "#/components/schemas/idResponse"
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "page_id"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "result": {
                          "type": "string"
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "result"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "page_id": {
                          "type": "string",
                          "description": "The ID of the created page."
                        },
                        "page_url": {
                          "type": "string",
                          "description": "The Notion URL of the created page."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "page_id",
                        "page_url"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "type": {
                          "type": "string",
                          "enum": [
                            "ai_search",
                            "workspace_search",
                            "none"
                          ],
                          "description": "The type of internal search that was performed, based on the user's access to Notion AI. Users without Notion AI will get a workspace search only, not including connected tools. If the search was not performed, this will be 'none'."
                        },
                        "results": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string"
                              },
                              "title": {
                                "type": "string"
                              },
                              "url": {
                                "type": "string",
                                "description": "Page ID for Notion results (pass to fetch tool) or full URL for external connector results."
                              },
                              "type": {
                                "type": "string"
                              },
                              "highlight": {
                                "type": "string"
                              },
                              "timestamp": {
                                "type": "string"
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "id",
                              "title",
                              "url",
                              "type",
                              "highlight",
                              "timestamp"
                            ]
                          },
                          "maxItems": 100,
                          "description": "An array of combined and deduplicated search results from the internal search queries."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "type",
                        "results"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "type": {
                          "type": "string",
                          "const": "user_search",
                          "description": "The type of users search that was performed."
                        },
                        "results": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "string",
                                "description": "All results of user search"
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "text"
                            ]
                          },
                          "maxItems": 100,
                          "description": "An array of search results from the users search queries."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "type",
                        "results"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "title": {
                          "type": "string"
                        },
                        "url": {
                          "type": "string"
                        },
                        "text": {
                          "type": "string"
                        },
                        "metadata": {
                          "type": "object",
                          "properties": {
                            "type": {
                              "type": "string",
                              "enum": [
                                "page",
                                "database",
                                "data_source"
                              ],
                              "description": "One of: `page`, `database`, `data_source`"
                            }
                          },
                          "additionalProperties": false,
                          "required": [
                            "type"
                          ]
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "title",
                        "url",
                        "text",
                        "metadata"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "result": {
                          "type": "string",
                          "description": "A rendered Markdown string describing the structure and details of the newly created database."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "result"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "result": {
                          "type": "string",
                          "description": "A rendered Markdown string describing the structure and details of the updated data source."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "result"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "results": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "additionalProperties": {
                              "oneOf": [
                                {
                                  "type": "string"
                                },
                                {
                                  "type": "number"
                                },
                                {
                                  "type": "boolean"
                                },
                                {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  },
                                  "maxItems": 100
                                },
                                {
                                  "type": "null"
                                }
                              ]
                            }
                          },
                          "maxItems": 100,
                          "description": "Array of query result rows, where each row is a record with column names as keys"
                        },
                        "has_more": {
                          "type": "boolean",
                          "description": "Whether there are more results available beyond the returned limit"
                        },
                        "data_source_ids": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "maxItems": 100,
                          "description": "IDs of data sources that were queried (only present for SQL queries)"
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "results",
                        "has_more"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "results": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "additionalProperties": {
                              "oneOf": [
                                {
                                  "type": "string"
                                },
                                {
                                  "type": "number"
                                },
                                {
                                  "type": "boolean"
                                },
                                {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  },
                                  "maxItems": 100
                                },
                                {
                                  "type": "null"
                                }
                              ]
                            }
                          },
                          "maxItems": 100,
                          "description": "Array of query result rows, where each row is a record with column names as keys"
                        },
                        "has_more": {
                          "type": "boolean",
                          "description": "Whether there are more results available beyond the returned limit"
                        },
                        "data_source_ids": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "maxItems": 100,
                          "description": "IDs of data sources that were queried"
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "results",
                        "has_more"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "results": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "additionalProperties": {
                              "oneOf": [
                                {
                                  "type": "string"
                                },
                                {
                                  "type": "number"
                                },
                                {
                                  "type": "boolean"
                                },
                                {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  },
                                  "maxItems": 100
                                },
                                {
                                  "type": "null"
                                }
                              ]
                            }
                          },
                          "maxItems": 100,
                          "description": "Array of meeting note rows, where each row is a record with column names as keys"
                        },
                        "has_more": {
                          "type": "boolean",
                          "description": "Whether there are more results available beyond the returned limit"
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "results",
                        "has_more"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "result": {
                          "type": "object",
                          "properties": {
                            "status": {
                              "type": "string",
                              "const": "success",
                              "description": "The status of the operation."
                            },
                            "id": {
                              "type": "string",
                              "description": "The ID of the created comment."
                            }
                          },
                          "additionalProperties": false,
                          "required": [
                            "status",
                            "id"
                          ],
                          "description": "The result of the create comment operation."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "result"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "string",
                          "description": "XML-formatted discussions and comments from the page."
                        }
                      },
                      "additionalProperties": false
                    },
                    {
                      "type": "object",
                      "properties": {
                        "joinedTeams": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "type": {
                                "type": "string",
                                "const": "team",
                                "description": "The type of the result."
                              },
                              "id": {
                                "$ref": "#/components/schemas/idResponse",
                                "description": "The unique identifier of the team."
                              },
                              "name": {
                                "type": "string",
                                "description": "The display name of the team."
                              },
                              "in_trash": {
                                "type": "boolean",
                                "description": "Whether the team is in the trash."
                              },
                              "role": {
                                "type": "string",
                                "enum": [
                                  "owner",
                                  "member",
                                  "guest",
                                  "none"
                                ],
                                "description": "The authenticated user's role in this team: 'owner' (full admin access), 'member' (content access), 'guest' (limited access), or 'none' (no access)."
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "type",
                              "id",
                              "name",
                              "in_trash",
                              "role"
                            ]
                          },
                          "maxItems": 100,
                          "description": "Teams that the authenticated user is a member of."
                        },
                        "otherTeams": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "type": {
                                "type": "string",
                                "const": "team",
                                "description": "The type of the result."
                              },
                              "id": {
                                "$ref": "#/components/schemas/idResponse",
                                "description": "The unique identifier of the team."
                              },
                              "name": {
                                "type": "string",
                                "description": "The display name of the team."
                              },
                              "in_trash": {
                                "type": "boolean",
                                "description": "Whether the team is in the trash."
                              },
                              "role": {
                                "type": "string",
                                "enum": [
                                  "owner",
                                  "member",
                                  "guest",
                                  "none"
                                ],
                                "description": "The authenticated user's role in this team: 'owner' (full admin access), 'member' (content access), 'guest' (limited access), or 'none' (no access)."
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "type",
                              "id",
                              "name",
                              "in_trash",
                              "role"
                            ]
                          },
                          "maxItems": 100,
                          "description": "Teams that the authenticated user is not a member of but can see."
                        },
                        "hasMore": {
                          "type": "boolean",
                          "description": "Whether there are more teams that were not included due to the result limit."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "joinedTeams",
                        "otherTeams",
                        "hasMore"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "results": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "type": {
                                "type": "string",
                                "enum": [
                                  "person",
                                  "bot"
                                ],
                                "description": "The type of user: 'person' or 'bot'."
                              },
                              "id": {
                                "type": "string",
                                "description": "The unique identifier of the user."
                              },
                              "name": {
                                "type": "string",
                                "description": "The display name of the user."
                              },
                              "email": {
                                "type": "string",
                                "description": "The email address of the user (only for person types)."
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "type",
                              "id",
                              "name",
                              "email"
                            ]
                          },
                          "maxItems": 100,
                          "description": "List of users (both workspace members and guests) and bots in the current page."
                        },
                        "has_more": {
                          "type": "boolean",
                          "description": "Whether there are more users available in the next page."
                        },
                        "next_cursor": {
                          "type": "string",
                          "description": "Cursor for the next page of results. Use this value as start_cursor in the next request to get the next page."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "results",
                        "has_more",
                        "next_cursor"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "agents": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "type": {
                                "type": "string",
                                "const": "agent",
                                "description": "The type of the result."
                              },
                              "id": {
                                "$ref": "#/components/schemas/idResponse",
                                "description": "The unique identifier of the agent."
                              },
                              "name": {
                                "type": "string",
                                "description": "The display name of the agent."
                              },
                              "description": {
                                "type": "string",
                                "description": "A short description of what the agent does."
                              },
                              "instructions": {
                                "type": "string",
                                "description": "The system instructions that define how the agent behaves."
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "type",
                              "id",
                              "name"
                            ]
                          },
                          "maxItems": 100,
                          "description": "List of available custom agents."
                        },
                        "hasMore": {
                          "type": "boolean",
                          "description": "Whether there are more agents that were not included due to the result limit."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "agents",
                        "hasMore"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "answer": {
                          "type": "string",
                          "description": "The AI-generated answer to the question"
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "answer"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "agent_id": {
                          "type": "string",
                          "description": "The unique identifier of the agent that processed the request"
                        },
                        "session_id": {
                          "type": "string",
                          "description": "The session ID for this conversation"
                        },
                        "thread_id": {
                          "type": "string",
                          "description": "The thread ID for this conversation thread"
                        },
                        "response": {
                          "type": "string",
                          "description": "The agent's response to the user's message"
                        },
                        "chat_url": {
                          "type": "string",
                          "description": "URL to view this chat conversation in the Notion app"
                        },
                        "is_new_conversation": {
                          "type": "boolean",
                          "description": "Whether this was a new conversation or a continuation"
                        },
                        "timestamp": {
                          "type": "string",
                          "description": "Timestamp when the response was generated"
                        },
                        "transcript": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string"
                              },
                              "type": {
                                "type": "string"
                              }
                            },
                            "required": [
                              "id",
                              "type"
                            ],
                            "additionalProperties": true
                          },
                          "maxItems": 100,
                          "description": "Optional conversation transcript if requested"
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "agent_id",
                        "session_id",
                        "thread_id",
                        "response",
                        "chat_url",
                        "is_new_conversation",
                        "timestamp"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "result": {
                          "type": "string",
                          "description": "A rendered Markdown string describing the newly created view."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "result"
                      ]
                    },
                    {
                      "type": "object",
                      "properties": {
                        "result": {
                          "type": "string",
                          "description": "A rendered Markdown string describing the updated view."
                        }
                      },
                      "additionalProperties": false,
                      "required": [
                        "result"
                      ]
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/users/transfer": {
      "post": {
        "summary": "Transfer workspace user content",
        "operationId": "transfer-user-content",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "from_user_id": {
                    "$ref": "#/components/schemas/idRequest",
                    "description": "The ID of the source user to transfer content from."
                  },
                  "to_user_id": {
                    "$ref": "#/components/schemas/idRequest",
                    "description": "The ID of the destination user to transfer content to."
                  },
                  "content_types": {
                    "type": "array",
                    "items": {
                      "type": "string",
                      "enum": [
                        "pages",
                        "agents"
                      ],
                      "description": "One of: `pages`, `agents`"
                    },
                    "maxItems": 100,
                    "description": "What content types to transfer. Defaults to pages for backwards compatibility."
                  }
                },
                "required": [
                  "from_user_id",
                  "to_user_id"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "object": {
                      "type": "string",
                      "const": "content_transfer",
                      "description": "The content transfer object type name."
                    }
                  },
                  "additionalProperties": false,
                  "required": [
                    "object"
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/pages/{page_id}/unshare_from_web": {
      "post": {
        "summary": "Unshare a page from web",
        "operationId": "unshare-page-from-web",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "page_id",
            "in": "path",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/idRequest"
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {},
                "additionalProperties": false
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "anyOf": [
                    {
                      "anyOf": [
                        {
                          "$ref": "#/components/schemas/pageObjectResponse"
                        },
                        {
                          "$ref": "#/components/schemas/partialPageObjectResponse"
                        }
                      ]
                    },
                    {
                      "anyOf": [
                        {
                          "$ref": "#/components/schemas/partialBlockObjectResponse"
                        },
                        {
                          "$ref": "#/components/schemas/blockObjectResponse"
                        }
                      ]
                    },
                    {
                      "anyOf": [
                        {
                          "$ref": "#/components/schemas/partialDataSourceObjectResponse"
                        },
                        {
                          "$ref": "#/components/schemas/dataSourceObjectResponse"
                        }
                      ]
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/_/pages/{page_id}/permissions": {
      "patch": {
        "summary": "Update page permissions",
        "operationId": "private-update-page-permissions",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "name": "page_id",
            "in": "path",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/idRequest"
            }
          },
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "permissions": {
                    "type": "array",
                    "items": {
                      "anyOf": [
                        {
                          "type": "object",
                          "properties": {
                            "role": {
                              "type": "string",
                              "enum": [
                                "full_owner",
                                "can_edit",
                                "can_comment",
                                "can_view"
                              ]
                            },
                            "type": {
                              "type": "string",
                              "const": "user_permission"
                            },
                            "user_id": {
                              "type": "string",
                              "format": "uuid"
                            }
                          },
                          "required": [
                            "role",
                            "type",
                            "user_id"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "role": {
                              "type": "string",
                              "enum": [
                                "full_owner",
                                "can_edit",
                                "can_comment",
                                "can_view"
                              ]
                            },
                            "type": {
                              "type": "string",
                              "const": "group_permission"
                            },
                            "group_id": {
                              "type": "string",
                              "format": "uuid"
                            }
                          },
                          "required": [
                            "role",
                            "type",
                            "group_id"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "role": {
                              "type": "string",
                              "enum": [
                                "full_owner",
                                "can_edit",
                                "can_comment",
                                "can_view"
                              ]
                            },
                            "type": {
                              "type": "string",
                              "const": "teamspace_owner"
                            }
                          },
                          "required": [
                            "role",
                            "type"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "role": {
                              "type": "string",
                              "enum": [
                                "full_owner",
                                "can_edit",
                                "can_comment",
                                "can_view"
                              ]
                            },
                            "type": {
                              "type": "string",
                              "const": "teamspace_members"
                            }
                          },
                          "required": [
                            "role",
                            "type"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "role": {
                              "type": "string",
                              "enum": [
                                "full_owner",
                                "can_edit",
                                "can_comment",
                                "can_view"
                              ]
                            },
                            "type": {
                              "type": "string",
                              "const": "workspace_permission"
                            },
                            "discoverability": {
                              "type": "string",
                              "enum": [
                                "discoverable",
                                "unlisted"
                              ]
                            }
                          },
                          "required": [
                            "role",
                            "type",
                            "discoverability"
                          ]
                        }
                      ]
                    }
                  },
                  "is_restricted": {
                    "type": "boolean"
                  }
                },
                "additionalProperties": false,
                "required": [
                  "permissions"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "anyOf": [
                    {
                      "$ref": "#/components/schemas/pageObjectResponse"
                    },
                    {
                      "$ref": "#/components/schemas/partialPageObjectResponse"
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    },
    "/v1/workspace/search": {
      "post": {
        "summary": "Search a workspace",
        "operationId": "search-workspace",
        "tags": [
          "Internal"
        ],
        "x-hidden": true,
        "x-noIndex": true,
        "parameters": [
          {
            "$ref": "#/components/parameters/notionVersion"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "keyword": {
                    "anyOf": [
                      {
                        "type": "string"
                      },
                      {
                        "anyOf": [
                          {
                            "type": "object",
                            "properties": {
                              "and": {
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "and"
                            ]
                          },
                          {
                            "type": "object",
                            "properties": {
                              "or": {
                                "type": "array",
                                "items": {
                                  "type": "string"
                                }
                              }
                            },
                            "additionalProperties": false,
                            "required": [
                              "or"
                            ]
                          }
                        ]
                      },
                      {
                        "type": "null"
                      }
                    ]
                  },
                  "shared_with_ids": {
                    "type": "array",
                    "items": {
                      "type": "string",
                      "format": "uuid"
                    }
                  },
                  "location": {
                    "type": "object",
                    "properties": {},
                    "additionalProperties": false
                  },
                  "date_range_filter": {
                    "type": "object",
                    "properties": {},
                    "additionalProperties": false
                  },
                  "options": {
                    "type": "object",
                    "properties": {},
                    "additionalProperties": false
                  },
                  "start_cursor": {
                    "type": "string",
                    "format": "uuid"
                  },
                  "page_size": {
                    "type": "number"
                  },
                  "result_type": {
                    "type": "string",
                    "enum": [
                      "page",
                      "database"
                    ]
                  }
                },
                "additionalProperties": false
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "title": "Search Result",
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "const": "search_result"
                    },
                    "search_result": {
                      "$ref": "#/components/schemas/emptyObject"
                    },
                    "object": {
                      "type": "string",
                      "const": "list"
                    },
                    "next_cursor": {
                      "type": [
                        "string",
                        "null"
                      ]
                    },
                    "has_more": {
                      "type": "boolean"
                    },
                    "results": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "object": {
                            "type": "string",
                            "const": "search_result"
                          },
                          "id": {
                            "type": "string",
                            "format": "uuid"
                          },
                          "path": {
                            "type": "string"
                          },
                          "created_time": {
                            "type": "number"
                          },
                          "created_by": {
                            "anyOf": [
                              {
                                "$ref": "#/components/schemas/partialUserObjectResponse"
                              },
                              {
                                "$ref": "#/components/schemas/userObjectResponse"
                              }
                            ]
                          },
                          "last_edited_by": {
                            "anyOf": [
                              {
                                "$ref": "#/components/schemas/partialUserObjectResponse"
                              },
                              {
                                "$ref": "#/components/schemas/userObjectResponse"
                              }
                            ]
                          },
                          "last_edited_time": {
                            "type": "string",
                            "format": "date-time"
                          },
                          "deleted": {
                            "type": "boolean"
                          },
                          "teamspace_id": {
                            "type": [
                              "string",
                              "null"
                            ],
                            "format": "uuid"
                          },
                          "teamspace_name": {
                            "type": [
                              "string",
                              "null"
                            ]
                          },
                          "space_id": {
                            "type": "string",
                            "format": "uuid"
                          },
                          "space_name": {
                            "type": "string"
                          },
                          "title": {
                            "type": "string"
                          },
                          "result_type": {
                            "type": "string",
                            "enum": [
                              "database",
                              "page"
                            ]
                          }
                        },
                        "required": [
                          "object",
                          "id",
                          "path",
                          "created_time",
                          "created_by",
                          "last_edited_by",
                          "last_edited_time",
                          "deleted",
                          "teamspace_id",
                          "teamspace_name",
                          "space_id",
                          "space_name",
                          "title",
                          "result_type"
                        ]
                      }
                    },
                    "total": {
                      "type": "number"
                    }
                  },
                  "required": [
                    "type",
                    "search_result",
                    "object",
                    "next_cursor",
                    "has_more",
                    "results",
                    "total"
                  ]
                }
              }
            }
          },
          "400": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_400"
                }
              }
            }
          },
          "401": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_401"
                }
              }
            }
          },
          "403": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_403"
                }
              }
            }
          },
          "404": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_404"
                }
              }
            }
          },
          "409": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_409"
                }
              }
            }
          },
          "429": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_429"
                }
              }
            }
          },
          "500": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_500"
                }
              }
            }
          },
          "503": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_503"
                }
              }
            }
          },
          "504": {
            "description": "",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/error_api_504"
                }
              }
            }
          }
        }
      }
    }
  }
}