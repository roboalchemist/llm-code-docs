# Source: https://developers.activecampaign.com/reference/list-all-tasks.md

# List all tasks

Retrieve a list of existing tasks

```json GET /dealTasks (Example RESPONSE)
{
  "dealTasks": [{
    "id":"1",
    "duedate":"2017-02-25T12:00:00-06:00",
    "edate":"2017-02-25T12:15:00-06:00",
    "status":0,
    "title":null,
    "note":"Testing Task",
    "relid":"7",
    "reltype":"Subscriber",
    "dealTasktype":"1",
    "cdate":"2017-02-24T13:21:56-06:00",
    "udate":"2017-02-24T13:21:56-06:00",
    "automation":null,
    "doneAutomation":null,
    "user":"1",
    "assignee":"2",
    "owner":{
      "type":"contact",
      "id":"7"
    },
    "outcomeId": null,
		"outcomeInfo": null,
    "links": {
      "activities":"/1/activities",
      "automation":"/1/automation",
      "dealTasktype":"/1/dealTasktype",
      "doneAutomation":"/1/doneAutomation",
      "notes":"/1/notes",
      "owner":"/1/owner",
      "taskNotifications":"/1/taskNotifications",
      "user":"/3/dealTasks/1/user",
      "assignee":"/1/assignee"
    }
  },
  {
    "id":"2",
    "duedate":"2017-02-25T12:00:00-06:00",
    "edate":"2017-02-25T12:15:00-06:00",
    "status":0,
    "title":null,
    "note":"Testing Task 2",
    "relid":"8",
    "reltype":"Deal",
    "dealTasktype":"1",
    "cdate":"2017-02-24T13:21:56-06:00",
    "udate":"2017-02-24T13:21:56-06:00",
    "automation":null,
    "doneAutomation":null,
    "user":"1",
    "assignee":"2",
    "owner":{
      "type":"deal",
      "id":"5"
    },
    "outcomeId": 91,
		"outcomeInfo": "More details about the outcome",
    "links": {
      "activities":"/2/activities",
      "automation":"/2/automation",
      "dealTasktype":"/2/dealTasktype",
      "doneAutomation":"/2/doneAutomation",
      "notes":"/2/notes",
      "owner":"/2/owner",
      "taskNotifications":"/2/taskNotifications",
      "user":"/2/user",
      "assignee":"/1/assignee"
    }
  }],
  "meta":{
    "total":"2"
  }
}
```

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "v3",
    "version": "3"
  },
  "servers": [
    {
      "url": "https://{youraccountname}.api-us1.com/api/3",
      "variables": {
        "youraccountname": {
          "default": "youraccountname"
        }
      }
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "name": "Api-Token",
        "in": "header",
        "x-default": ""
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/dealTasks": {
      "get": {
        "summary": "List all tasks",
        "description": "Retrieve a list of existing tasks",
        "operationId": "list-all-tasks",
        "parameters": [
          {
            "name": "filters[title]",
            "in": "query",
            "description": "The title to be assigned to the task",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters[reltype]",
            "in": "query",
            "description": "The name of the relating object (see relationships table)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters[relid]",
            "in": "query",
            "description": "The id of the relational object for this task",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "filters[status]",
            "in": "query",
            "description": "Task status means complete or incomplete. 1 is complete and 0 is incomplete.",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "filters[note]",
            "in": "query",
            "description": "The content describing the task",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters[duedate]",
            "in": "query",
            "description": "Due date of the task",
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "name": "filters[d_tasktypeid]",
            "in": "query",
            "description": "The type of the task based on the available Task Types in the account",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "filters[userid]",
            "in": "query",
            "description": "User ID this task belongs to",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "filters[due_after]",
            "in": "query",
            "description": "Filter deal tasks that are due after a specific date",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Fitlers[due_before]",
            "in": "query",
            "description": "Filter deal tasks that are due before a specific date",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters[duedate_range]",
            "in": "query",
            "description": "Filter deal tasks that are due between specific date range (YYYY-MM-DD+YYYY-MM-DD format) or get categorized tasks (upcoming, scheduled, overdue values)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filters[assignee_userid]",
            "in": "query",
            "description": "The id of the user a task is assigned to",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "filters[outcome_id]",
            "in": "query",
            "description": "The id of a task outcome that the task belongs to.",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          }
        ],
        "responses": {
          "201": {
            "description": "201",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"dealTasks\": [{\n    \"id\":\"1\",\n    \"duedate\":\"2017-02-25T12:00:00-06:00\",\n    \"edate\":\"2017-02-25T12:15:00-06:00\",\n    \"status\":0,\n    \"title\":null,\n    \"note\":\"Testing Task\",\n    \"relid\":\"7\",\n    \"reltype\":\"Subscriber\",\n    \"dealTasktype\":\"1\",\n    \"cdate\":\"2017-02-24T13:21:56-06:00\",\n    \"udate\":\"2017-02-24T13:21:56-06:00\",\n    \"automation\":null,\n    \"doneAutomation\":null,\n    \"user\":\"1\",\n    \"assignee\":\"2\",\n    \"owner\":{\n      \"type\":\"contact\",\n      \"id\":\"7\"\n    },\n    \"outcomeId\": null,\n\t\t\"outcomeInfo\": null,\n    \"links\": {\n      \"activities\":\"/1/activities\",\n      \"automation\":\"/1/automation\",\n      \"dealTasktype\":\"/1/dealTasktype\",\n      \"doneAutomation\":\"/1/doneAutomation\",\n      \"notes\":\"/1/notes\",\n      \"owner\":\"/1/owner\",\n      \"taskNotifications\":\"/1/taskNotifications\",\n      \"user\":\"/3/dealTasks/1/user\",\n      \"assignee\":\"/1/assignee\"\n    }\n  },\n  {\n    \"id\":\"2\",\n    \"duedate\":\"2017-02-25T12:00:00-06:00\",\n    \"edate\":\"2017-02-25T12:15:00-06:00\",\n    \"status\":0,\n    \"title\":null,\n    \"note\":\"Testing Task 2\",\n    \"relid\":\"8\",\n    \"reltype\":\"Deal\",\n    \"dealTasktype\":\"1\",\n    \"cdate\":\"2017-02-24T13:21:56-06:00\",\n    \"udate\":\"2017-02-24T13:21:56-06:00\",\n    \"automation\":null,\n    \"doneAutomation\":null,\n    \"user\":\"1\",\n    \"assignee\":\"2\",\n    \"owner\":{\n      \"type\":\"deal\",\n      \"id\":\"5\"\n    },\n    \"outcomeId\": 91,\n\t\t\"outcomeInfo\": \"More details about the outcome\",\n    \"links\": {\n      \"activities\":\"/2/activities\",\n      \"automation\":\"/2/automation\",\n      \"dealTasktype\":\"/2/dealTasktype\",\n      \"doneAutomation\":\"/2/doneAutomation\",\n      \"notes\":\"/2/notes\",\n      \"owner\":\"/2/owner\",\n      \"taskNotifications\":\"/2/taskNotifications\",\n      \"user\":\"/2/user\",\n      \"assignee\":\"/1/assignee\"\n    }\n  }],\n  \"meta\":{\n    \"total\":\"2\"\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "dealTasks": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string",
                            "example": "1"
                          },
                          "duedate": {
                            "type": "string",
                            "example": "2017-02-25T12:00:00-06:00"
                          },
                          "edate": {
                            "type": "string",
                            "example": "2017-02-25T12:15:00-06:00"
                          },
                          "status": {
                            "type": "integer",
                            "example": 0,
                            "default": 0
                          },
                          "title": {},
                          "note": {
                            "type": "string",
                            "example": "Testing Task"
                          },
                          "relid": {
                            "type": "string",
                            "example": "7"
                          },
                          "reltype": {
                            "type": "string",
                            "example": "Subscriber"
                          },
                          "dealTasktype": {
                            "type": "string",
                            "example": "1"
                          },
                          "cdate": {
                            "type": "string",
                            "example": "2017-02-24T13:21:56-06:00"
                          },
                          "udate": {
                            "type": "string",
                            "example": "2017-02-24T13:21:56-06:00"
                          },
                          "automation": {},
                          "doneAutomation": {},
                          "user": {
                            "type": "string",
                            "example": "1"
                          },
                          "assignee": {
                            "type": "string",
                            "example": "2"
                          },
                          "owner": {
                            "type": "object",
                            "properties": {
                              "type": {
                                "type": "string",
                                "example": "contact"
                              },
                              "id": {
                                "type": "string",
                                "example": "7"
                              }
                            }
                          },
                          "outcomeId": {},
                          "outcomeInfo": {},
                          "links": {
                            "type": "object",
                            "properties": {
                              "activities": {
                                "type": "string",
                                "example": "/1/activities"
                              },
                              "automation": {
                                "type": "string",
                                "example": "/1/automation"
                              },
                              "dealTasktype": {
                                "type": "string",
                                "example": "/1/dealTasktype"
                              },
                              "doneAutomation": {
                                "type": "string",
                                "example": "/1/doneAutomation"
                              },
                              "notes": {
                                "type": "string",
                                "example": "/1/notes"
                              },
                              "owner": {
                                "type": "string",
                                "example": "/1/owner"
                              },
                              "taskNotifications": {
                                "type": "string",
                                "example": "/1/taskNotifications"
                              },
                              "user": {
                                "type": "string",
                                "example": "/3/dealTasks/1/user"
                              },
                              "assignee": {
                                "type": "string",
                                "example": "/1/assignee"
                              }
                            }
                          }
                        }
                      }
                    },
                    "meta": {
                      "type": "object",
                      "properties": {
                        "total": {
                          "type": "string",
                          "example": "2"
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "deprecated": false
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": false,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```