# Source: https://docs.xano.com/xano-features/metadata-api/tables-and-schema.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tables And Schema

The following are various examples of how to leverage the Metadata API to create and modify database tables including the schema and indexes included within them.

<Frame>
  <iframe width="1000" height="500" src="https://www.youtube.com/embed/jsFTr4ihUYY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />
</Frame>

### Get Workspaces

Browse the workspaces of the instance. This API endpoint does not require any parameters. Retrieving the workspaces gives you information on the workspace name and ID. The workspace ID is particularly important for use in other Metadata API endpoints.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/251f7111-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=0ef2541383c4e10d6bc4f5f3c5f6eecf" width="2292" height="100" data-path="images/251f7111-image.jpeg" />
</Frame>

Example response body:

```json  theme={null}
[
  {
    "id": 1,
    "name": "my workspace 1",
    "description": ""
  },
  {
    "id": 3,
    "name": "test",
    "description": ""
  },
  {
    "id": 2,
    "name": "to do app",
    "description": "my to do app example"
  }
]
```

### Get Tables of a Workspace

Browse workspace tables. This API endpoint requires a workspace ID and will provide various information about each database table in a workspace, including database table ID, which is needed in various Metadata API endpoints.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c77d328d-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=24453de46795165bdf1f7459512f123c" width="2300" height="902" data-path="images/c77d328d-image.jpeg" />
</Frame>

Example response body:

```json  theme={null}
[
  {
    "id": 7,
    "created_at": "2023-04-12 22:00:38+0000",
    "updated_at": "2023-04-12 22:00:42+0000",
    "name": "category",
    "description": "",
    "guid": "yu2eB8E0dSEtL6MbBPzzJUM06gA",
    "auth": false
  },
  {
    "id": 8,
    "created_at": "2023-04-12 22:00:51+0000",
    "updated_at": "2023-04-12 22:01:07+0000",
    "name": "items",
    "description": "",
    "guid": "eP9O-rD-7sGKpbLOEhdED6YGrmA",
    "auth": false
  },
  {
    "id": 1,
    "created_at": "2022-03-24 20:20:26+0000",
    "updated_at": "2022-03-24 20:20:26+0000",
    "name": "user",
    "description": "",
    "guid": "nTOiqqb31ecz1Te6v_3YMkfp5xc",
    "auth": true
  }
]
```

### Create Table and Add Schema One by One

First, create a new table in the desired workspace. The default request values suffice. In this example, first, we will create a table and then add schema individually. The Metadata API is capable of adding schema in bulk but that will be covered in another example.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/dca41f87-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=8f27cf5ba0c4d3aef00a95e1b2b2ebe6" width="2302" height="1232" data-path="images/dca41f87-image.jpeg" />
</Frame>

Example response body:

```json  theme={null}
{
  "id": 9
}
```

Taking the newly created database table ID, we can add schema 1 by 1 to the table.

1. A text field called name.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/4865eace-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=40239427086a77b7b7ed6292d9b464fe" width="2304" height="1279" data-path="images/4865eace-image.jpeg" />
</Frame>

Example response body:

```json  theme={null}
{
  "name": "name"
}
```

Next, let's add an integer field called score with a default value of 30

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/d7da764b-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=f6740adb817553e29d3c3f48ef952214" width="2304" height="1183" data-path="images/d7da764b-image.jpeg" />
</Frame>

As we execute these Metadata API calls, our new table in Xano is being created along with the new schema, one by one.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/14f479c9-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=0fa2bf50411f8e91ecb6d24f7d929c7c" width="808" height="511" data-path="images/14f479c9-image.jpeg" />
</Frame>

### Create an Index

The Metadata API gives control over indexes on database tables. In this example, let's create a Unique Index on the name field of new table 123.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/526ba428-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=31153cef8c85f15971d760ba93f05e98" width="2304" height="1271" data-path="images/526ba428-image.jpeg" />
</Frame>

Example response body:

```json  theme={null}
{
  "id": "baa524c4"
}
```

The API responds with the ID of the index. In Xano, we can see the index has been created:

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/WBQXG-4Ngk82eYAW/images/ff47a8b4-image.jpeg?fit=max&auto=format&n=WBQXG-4Ngk82eYAW&q=85&s=3c4ca6e9392380783bd088a51242726c" width="593" height="545" data-path="images/ff47a8b4-image.jpeg" />
</Frame>

### Create Table with Schema and an Index in One Call

In this example, we will create a new database table along with schema and an index in the same API call. The Metadata API is flexible enough to accommodate this method.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/1a0c1e21-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=13fc86de55974e83072e48d76846ae00" width="2304" height="1205" data-path="images/1a0c1e21-image.jpeg" />
</Frame>

Here's the example request body:

```json  theme={null}
{
  "name": "new stuff",
  "description": "",
  "auth": null,
  "guid": null,
  "schema": [
    {
      "name": "id",
      "type": "int",
      "description": "",
      "nullable": false,
      "default": "",
      "required": true,
      "access": "public",
      "style": "single"
    },
    {
      "name": "created_at",
      "type": "timestamp",
      "description": "",
      "nullable": false,
      "default": "",
      "required": true,
      "access": "public",
      "style": "single"
    },
    {
      "name": "name",
      "type": "text",
      "description": "",
      "nullable": false,
      "default": "",
      "required": true,
      "access": "public",
      "style": "single"
    }
  ],
  "index":[
    {
      "type": "btree",
      "fields": [
        {
          "name": "name",
          "op": "desc"
        }
      ]
    }
  ]
}
```

This creates a new table called "new stuff" with three fields: id, created\_at, and name with an index on the name field.

<Info>
  For defining schema, the Metadata API needs a minimum of "name" and "type" but the other fields aren't required. If you are defining schema during table creation, the first field must be the ID field.

  For Request body examples of schema and index, check out the PUT examples in Swagger for table/schema and table/index.
</Info>

### Browse Content

Browse table content is a simple method of getting content (database records) in a database table. It requires a workspace ID and table ID, while paging is optional.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b2bed4f6-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=4e100c9d7bc0824b4df6fc2b4a4afd59" width="2304" height="1108" data-path="images/b2bed4f6-image.jpeg" />
</Frame>

Example response body:

```json  theme={null}
{
  "items": [
    {
      "id": 1,
      "created_at": 1681336868222,
      "name": "Basketball",
      "description": "round ball to shoot hoops",
      "category_id": 1
    },
    {
      "id": 2,
      "created_at": 1681336868456,
      "name": "French Press",
      "description": "Make delicious coffee with this",
      "category_id": 2
    },
    {
      "id": 3,
      "created_at": 1681336868658,
      "name": "Bluetooth Speaker",
      "description": "Portable music player",
      "category_id": 3
    },
    {
      "id": 4,
      "created_at": 1681336868931,
      "name": "Camera",
      "description": "Take photos with this",
      "category_id": 3
    }
  ],
  "itemsReceived": 4,
  "curPage": 1,
  "nextPage": null,
  "prevPage": null,
  "offset": 0,
  "itemsTotal": 4,
  "pageTotal": 1
}
```

###


Built with [Mintlify](https://mintlify.com).