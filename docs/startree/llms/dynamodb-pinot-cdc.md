# Source: https://docs.startree.ai/recipes/dynamodb-pinot-cdc.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Replicating DynamoDB to Apache Pinot

In this developer guide, you'll learn how to ingest DynamoDB formatted change data capture data into Pinot.

## Introduction

Imagine having the robust storage capabilities of DynamoDB combined with the lightning-fast analytics of Apache Pinot.

## What You'll Need

* AWS account (with DynamoDB and Kinesis access)
* Apache Pinot cluster
* Your favorite code editor

## Setting Up the Replication Pipeline

### Step 1: Create a DynamoDB Table

Let's start by creating our source of truth - a DynamoDB table.

<img src="https://mintcdn.com/startree/ydxOgkfeGyqN5wki/recipes/images/create_dynamo_table.png?fit=max&auto=format&n=ydxOgkfeGyqN5wki&q=85&s=9e3fa806ae3c4fbeeacbc46ceffdeb7b" alt="DynamoDBUI" width="1712" height="1622" data-path="recipes/images/create_dynamo_table.png" />

### Step 2: Create a Kinesis Data Stream

Time to create a highway for our data - Kinesis stream where dynamo will push its CDC.

<img src="https://mintcdn.com/startree/ydxOgkfeGyqN5wki/recipes/images/create_kinesis_stream.png?fit=max&auto=format&n=ydxOgkfeGyqN5wki&q=85&s=f098e2f1936c1ed46fde4967a1bf3ef0" alt="KinesisUI" width="1720" height="1814" data-path="recipes/images/create_kinesis_stream.png" />

### Step 3: Enable DynamoDB-Kinesis stream

Now, let's turn on the data faucet by connecting dynamodb to kinesis

<img src="https://mintcdn.com/startree/ydxOgkfeGyqN5wki/recipes/images/connect_kinesis_stream.png?fit=max&auto=format&n=ydxOgkfeGyqN5wki&q=85&s=cef6dc84bf6463d87c0118d61c44598f" alt="DynamoDBUI" width="1824" height="1420" data-path="recipes/images/connect_kinesis_stream.png" />

### Step 4: Create Pinot Schema

Let's tell Pinot what our data looks like:

```json  theme={null}
{
  "schemaName": "pinot_dynamo_ingestion",
  "dimensionFieldSpecs": [
    {
        "name": "eventName",
        "dataType": "STRING",
        "notNull": false
    },
    {
      "name": "venue_name",
      "dataType": "STRING",
      "notNull": false
    },
    {
      "name": "meetup_name",
      "dataType": "STRING",
      "notNull": false
    },
    {
      "name": "meetup_id",
      "dataType": "STRING",
      "notNull": false
    },
    {
      "name": "group_city",
      "dataType": "STRING",
      "notNull": false
    },
    {
      "name": "group_country",
      "dataType": "STRING",
      "notNull": false
    },
    {
      "name": "group_id",
      "dataType": "LONG",
      "notNull": false
    },
    {
      "name": "group_name",
      "dataType": "STRING",
      "notNull": false
    },
    {
      "name": "group_lat",
      "dataType": "DOUBLE",
      "notNull": false
    },
    {
      "name": "group_lon",
      "dataType": "DOUBLE",
      "notNull": false
    },
    {
      "name": "location",
      "dataType": "BYTES",
      "transformFunction": "toSphericalGeography(stPoint(group_lon,group_lat))",
      "notNull": false
    },
    {
        "name": "is_delete",
        "dataType": "BOOLEAN",
        "transformFunction": "strcmp(eventName, 'REMOVE') = 0",
        "notNull": false
    }
  ],
  "metricFieldSpecs": [
    {
      "name": "rsvp_count",
      "dataType": "INT",
      "notNull": false
    }
  ],
  "dateTimeFieldSpecs": [
    {
      "name": "mtime",
      "dataType": "TIMESTAMP",
      "notNull": false,
      "format": "TIMESTAMP",
      "granularity": "1:MILLISECONDS"
    },
    {
        "name": "ApproximateCreationDateTime",
        "dataType": "TIMESTAMP",
        "notNull": false,
        "format": "TIMESTAMP",
        "granularity": "1:MILLISECONDS"
      }
  ],
  "primaryKeyColumns": ["meetup_id"]
}
```

### Step 5: Create Pinot Table Configuration

Now, let's set the table for our data feast!

```json  theme={null}
{
  "tableName": "pinot_dynamo_ingestion",
  "tableType": "REALTIME",
  "segmentsConfig": {
    "timeColumnName": "mtime",
    "timeType": "MILLISECONDS",
    "retentionTimeUnit": "DAYS",
    "retentionTimeValue": "7",
    "schemaName": "pinot_dynamo_ingestion",
    "replication": "1"
  },
  "tenants": {},
  "tableIndexConfig": {
    "loadMode": "MMAP",
    "streamConfigs": {
      "streamType": "kinesis",
      "stream.kinesis.topic.name": "pinot-ingestion-stream",
      "region": "us-east-1",
      "accessKey": "XXXX",
      "secretKey": "XXXX",
      "shardIteratorType": "AFTER_SEQUENCE_NUMBER",
      "stream.kinesis.consumer.type": "lowlevel",
      "stream.kinesis.fetch.timeout.millis": "120000",
      "stream.kinesis.decoder.class.name": "ai.startree.pinot.plugin.inputformat.dynamodb.DynamoDbMessageDecoder",
      "stream.kinesis.decoder.prop.dynamodb.timeColumnName": "created_at_timestamp",
      "stream.kinesis.decoder.prop.dynamodb.deleteColumnName": "is_deleted",
      "stream.kinesis.decoder.prop.dynamodb.envelope.decoder.class.name": "org.apache.pinot.plugin.inputformat.json.JSONMessageDecoder",
      "stream.kinesis.consumer.factory.class.name": "org.apache.pinot.plugin.stream.kinesis.KinesisConsumerFactory",
      "realtime.segment.flush.threshold.rows": "1000000",
      "realtime.segment.flush.threshold.time": "6h"
    },
    "nullHandlingEnabled": true
  },
  "routing": {
    "segmentPrunerTypes": ["time"],
    "instanceSelectorType": "strictReplicaGroup"
  },
  "ingestionConfig": {
    "transformConfigs": [
    ]
  },
  "upsertConfig": {
    "mode": "PARTIAL",
    "deleteRecordColumn": "is_delete",
    "partialUpsertStrategies":{},
    "comparisonColumns": ["ApproximateCreationDateTime"]
  },
  "metadata": {
    "customConfigs": {}
  }
}
```

### Why do we have so many configurations?

Let's try to understand which of these configs are necessary. When you enable CDC on dynamoDB table, it starts sending the data in the following format

```json  theme={null}
{
    "awsRegion": "us-east-2",
    "eventID": "e5c2d473-43e0-4dc3-bf28-cdcb575a83aa",
    "eventName": "INSERT",
    "userIdentity": null,
    "recordFormat": "application/json",
    "tableName": "pinot-ingestion-demo",
    "dynamodb": {
        "ApproximateCreationDateTime": 1719039879869591,
        "Keys": {
            "event_id": {
                "S": "badbe259-82d3-4869-b197-e935b0e942f2"
            },
            "mtime": {
                "N": "1719039879651"
            }
        },
        "NewImage": {
            "group_city": {
                "S": "New York"
            },
            "location": {
                "B": "Y0d4aFkyVm9iMnhrWlhKZllubDBaWE09"
            },
            "group_lon": {
                "N": "-97.169068"
            },
            "event_time": {
                "S": "2024-07-10T12:34:39.651036"
            },
            "group_id": {
                "N": "8032"
            },
            "mtime": {
                "N": "1719039879651"
            },
            "rsvp_count": {
                "N": "45"
            },
            "group_country": {
                "S": "UK"
            },
            "group_lat": {
                "N": "-41.13523"
            },
            "event_id": {
                "S": "badbe259-82d3-4869-b197-e935b0e942f2"
            },
            "venue_name": {
                "S": "Venue 1"
            },
            "group_name": {
                "S": "Group 10"
            },
            "event_name": {
                "S": "Event 3"
            }
        },
        "SizeBytes": 313,
        "ApproximateCreationDateTimePrecision": "MICROSECOND"
    },
    "eventSource": "aws:dynamodb"
}
```

```json  theme={null}
{
    "awsRegion": "us-east-1",
    "eventID": "1020b6ed-fc46-4767-8819-55c440041264",
    "eventName": "MODIFY",
    "userIdentity": null,
    "recordFormat": "application/json",
    "tableName": "pinot-ingestion-demo",
    "dynamodb": {
        "ApproximateCreationDateTime": 1719082124026,
        "Keys": {
            "mtime": {
                "N": "1719080907442"
            },
            "meetup_id": {
                "S": "4a60c849-d475-4ad5-adbc-776cbf7ca5df"
            }
        },
        "NewImage": {
            "group_city": {
                "S": "New York"
            },
            "mtime": {
                "N": "1719080907442"
            },
            "group_lon": {
                "N": "74.891677"
            },
            "rsvp_count": {
                "N": "23"
            },
            "group_lat": {
                "N": "-59.493753"
            },
            "group_country": {
                "S": "UK"
            },
            "meetup_id": {
                "S": "4a60c849-d475-4ad5-adbc-776cbf7ca5df"
            },
            "venue_name": {
                "S": "Updated Venue 3"
            },
            "group_id": {
                "N": "4673"
            },
            "meetup_name": {
                "S": "Meetup 6"
            },
            "group_name": {
                "S": "Group 8"
            }
        },
        "OldImage": {
            "group_city": {
                "S": "New York"
            },
            "mtime": {
                "N": "1719080907442"
            },
            "group_lon": {
                "N": "-130.035739"
            },
            "rsvp_count": {
                "N": "22"
            },
            "group_lat": {
                "N": "66.888498"
            },
            "group_country": {
                "S": "UK"
            },
            "meetup_id": {
                "S": "4a60c849-d475-4ad5-adbc-776cbf7ca5df"
            },
            "venue_name": {
                "S": "Updated Venue 2"
            },
            "group_id": {
                "N": "4673"
            },
            "meetup_name": {
                "S": "Meetup 6"
            },
            "group_name": {
                "S": "Group 8"
            }
        },
        "SizeBytes": 467
    },
    "eventSource": "aws:dynamodb"
}
```

```json  theme={null}
{
    "awsRegion": "us-east-1",
    "eventID": "78b55ff0-82ab-4fec-9f03-6312c5d2f6eb",
    "eventName": "REMOVE",
    "userIdentity": null,
    "recordFormat": "application/json",
    "tableName": "pinot-ingestion-demo",
    "dynamodb": {
        "ApproximateCreationDateTime": 1719081613486,
        "Keys": {
            "mtime": {
                "N": "1719080908912"
            },
            "meetup_id": {
                "S": "735fd994-2071-4145-8f35-7e69e537aaba"
            }
        },
        "OldImage": {
            "group_city": {
                "S": "London"
            },
            "mtime": {
                "N": "1719080908912"
            },
            "rsvp_count": {
                "N": "26"
            },
            "group_lon": {
                "N": "-19.773637"
            },
            "group_country": {
                "S": "Germany"
            },
            "group_lat": {
                "N": "23.60754"
            },
            "meetup_id": {
                "S": "735fd994-2071-4145-8f35-7e69e537aaba"
            },
            "venue_name": {
                "S": "Venue 2"
            },
            "group_id": {
                "N": "8524"
            },
            "meetup_name": {
                "S": "Meetup 2"
            },
            "group_name": {
                "S": "Group 6"
            }
        },
        "SizeBytes": 257
    },
    "eventSource": "aws:dynamodb"
}
```

#### Decoder Configuration

To help pinot understand the dynamodb data format, we need to add decoder configs to our table

```json  theme={null}
"stream.kinesis.decoder.class.name": "ai.startree.pinot.plugin.inputformat.dynamodb.DynamoDbMessageDecoder",
"stream.kinesis.decoder.prop.dynamodb.timeColumnName": "created_at_timestamp",
"stream.kinesis.decoder.prop.dynamodb.deleteColumnName": "is_deleted",
"stream.kinesis.decoder.prop.dynamodb.envelope.decoder.class.name": "org.apache.pinot.plugin.inputformat.json.JSONMessageDecoder"
```

The `decoder.class.name` specifies our primary decoder.
The `timeColumnName` specifies the column that should be filled with the `ApproximateCreationDateTime` from dynamodb json record.
the `deleteColumnName` specifies the column that should be set to `true` in  case we receive a `REMOVE` record from dynamodb
Finally, the `envelope.decoder.class.name` simply specifies the vanilla decoder that should be used to parse the message. Since them dynamodb messages come in json format, we specify the `JSONMessageDecoder` here

#### Upserts Configuration

To handle updates properly, you need to enable upserts in Pinot. This is done in the `upsertConfig` section of the table configuration:

```json  theme={null}
"upsertConfig": {
  "mode": "PARTIAL",
  "deleteRecordColumn": "is_delete",
  "partialUpsertStrategies": {},
  "comparisonColumns": ["ApproximateCreationDateTime"]
}
```

Key points:

* `mode`: Set to "PARTIAL" for partial updates.
* `deleteRecordColumn`: Specifies the column that indicates if a record should be deleted.
* `comparisonColumns`: Uses `ApproximateCreationDateTime` to determine the order of changes.

#### Derived Column for Deletions

A new derived column `is_delete` is created in the schema to signify whether a key needs to be removed from the upsert metadata:

```json  theme={null}
{
  "name": "is_delete",
  "dataType": "BOOLEAN",
  "transformFunction": "strcmp(eventName, 'REMOVE') = 0",
  "notNull": false
}
```

This column is set to true when the `eventName` in the DynamoDB stream event is "REMOVE".

#### Handling Different Event Types

The configuration handles different event types as follows:

1. INSERT: New records are added to Pinot.
2. MODIFY: Existing records are updated using the upsert configuration.
3. REMOVE: Records are marked for deletion using the `is_delete` column.

#### ApproximateCreationDateTime Usage

The `ApproximateCreationDateTime` from the DynamoDB payload is used in the `comparisonColumns` of the upsert configuration. This ensures that changes are applied in the correct order, as it represents the sequence of events in DynamoDB.

```json  theme={null}
"comparisonColumns": ["ApproximateCreationDateTime"]
```

A corresponding column is added to the schema:

```json  theme={null}
{
  "name": "ApproximateCreationDateTime",
  "dataType": "TIMESTAMP",
  "notNull": false,
  "format": "TIMESTAMP",
  "granularity": "1:MILLISECONDS"
}
```

### Step 6: Create Pinot Table

Let's bring our table to life!

```bash  theme={null}
bin/pinot-admin.sh AddTable \
    -schemaFile /tmp/pinot/schema.json 
    -tableConfigFile /tmp/pinot/table_config.json 
    -exec
```

## Insert, Update, Delete

### Insert

Let's add some data to our DynamoDB table:

```bash  theme={null}
python publish_data.py

Publish item with meetup_id: cc3fbaca-445c-4ebb-8f60-7b2a5eab3530 and mtime = 1719124016204
Publish item with meetup_id: c1731e4b-6726-40f5-8c8f-b34bc34a0744 and mtime = 1719124017046
Publish item with meetup_id: 9c4b139b-26aa-4d45-8efe-5d1ad2d4e1e3 and mtime = 1719124017265
Publish item with meetup_id: cfcb025b-7547-4002-9b52-95ad0b0a4ac8 and mtime = 1719124017488
Publish item with meetup_id: be08dc25-42a4-4fd3-8b6f-0bdaaeb4caf7 and mtime = 1719124017787
Publish item with meetup_id: bdc86183-a63a-4bc2-9901-22be89eb9774 and mtime = 1719124018010
Publish item with meetup_id: 0b27b577-dce5-43d1-b23f-8372b1882571 and mtime = 1719124018232
Publish item with meetup_id: 4d959048-796a-464f-ab6c-5afe174ec015 and mtime = 1719124018506
Publish item with meetup_id: 8a2e679c-3044-4526-bd9d-a2de908dbc62 and mtime = 1719124018723
Publish item with meetup_id: 98b3c314-75c2-420b-a154-d891a43e6efa and mtime = 1719124018945
DynamoDB insertion completed.
```

Check your Pinot table, and you'll see these rows magically appear!

<img src="https://mintcdn.com/startree/ydxOgkfeGyqN5wki/recipes/images/all_pinot_data.png?fit=max&auto=format&n=ydxOgkfeGyqN5wki&q=85&s=7e12c28ef74cf20d796ec413d6e16ef1" alt="Pinot UI" width="2440" height="1848" data-path="recipes/images/all_pinot_data.png" />

### Update

Let's update a row:

```bash  theme={null}
python update_data.py --meetup_id cc3fbaca-445c-4ebb-8f60-7b2a5eab3530 --mtime 1719124016204

Updated item in DynamoDB with meetup_id: cc3fbaca-445c-4ebb-8f60-7b2a5eab3530 and mtime: 1719124016204
UpdatedAttributes: {'group_lon': Decimal('28.454082'), 'rsvp_count': Decimal('84'), 'venue_name': 'Updated Venue 1', 'group_lat': Decimal('11.194998')}
```

Query Pinot, and witness the transformation!

#### Row before update

<img src="https://mintcdn.com/startree/SwAzqeuInnw8J52u/recipes/images/data_before_update.png?fit=max&auto=format&n=SwAzqeuInnw8J52u&q=85&s=d79985e48e7303f625e8243ca8cafd4b" alt="Pinot UI" width="2416" height="980" data-path="recipes/images/data_before_update.png" />

#### Row after update

<img src="https://mintcdn.com/startree/ydxOgkfeGyqN5wki/recipes/images/data_after_update.png?fit=max&auto=format&n=ydxOgkfeGyqN5wki&q=85&s=80510d9bd750a86eba9cb9fc23063ba5" alt="Pinot UI" width="2446" height="1404" data-path="recipes/images/data_after_update.png" />

### Delete

To remove a row:

```bash  theme={null}
python delete_data.py --meetup_id cc3fbaca-445c-4ebb-8f60-7b2a5eab3530 --mtime 1719124016204

Deleted item with meetup_id: cc3fbaca-445c-4ebb-8f60-7b2a5eab3530 and mtime: 1719124016204
```

Check Pinot:
<img src="https://mintcdn.com/startree/SwAzqeuInnw8J52u/recipes/images/data_deleted.png?fit=max&auto=format&n=SwAzqeuInnw8J52u&q=85&s=a37a95b49eb35395396ff1a192f44697" alt="Pinot UI" width="2426" height="1292" data-path="recipes/images/data_deleted.png" />

## Behind the Scenes: Viewing Operation Order

Use the following in your Pinot queries:

```sql  theme={null}
SELECT * FROM pinot_dynamo_ingestion 
WHERE meetup_id = 'cc3fbaca-445c-4ebb-8f60-7b2a5eab3530' 
ORDER BY ApproximateCreationDateTime DESC 
OPTION(skipUpsert=True)
```

This will reveal the entire history of your data's journey.
<img src="https://mintcdn.com/startree/SwAzqeuInnw8J52u/recipes/images/skip_upsert.png?fit=max&auto=format&n=SwAzqeuInnw8J52u&q=85&s=b738b1051287666b5421bbd44dc3adb7" alt="Pinot UI" width="2444" height="1534" data-path="recipes/images/skip_upsert.png" />

## Conclusion

You've successfully created a real-time replication pipeline from DynamoDB to Apache Pinot. Your data is now ready for lightning-fast analytics while maintaining the reliability of DynamoDB.

Built with [Mintlify](https://mintlify.com).
