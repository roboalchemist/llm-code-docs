# Source: https://docs.datafold.com/integrations/databases/mongodb.md

# MongoDB

> Our MongoDB integration allows you to diff data within MongoDB, or between MongoDB and a relational database (or even a file!).

<Note>
  Our MongoDB integration is still in beta. Some features, such as column-level lineage, are not yet supported. Please contact us if you need assistance.
</Note>

**Steps to complete:**

1. [Configure user in MongoDB](#configure-user-in-mongodb)
2. [Configure your data connection in Datafold](#configure-in-datafold)
3. [Diff your data](#diff-your-data)

## Configure user in MongoDB

To connect to MongoDB, create a user with read-only access to all databases you plan to diff.

## Configure in Datafold

| Field Name              | Description                                                      |
| ----------------------- | ---------------------------------------------------------------- |
| Connection Name         | The name you'd like to assign to this connection in Datafold     |
| Host                    | The hostname for your MongoDB instance                           |
| Port                    | MongoDB endpoint port (default value is 27017)                   |
| User ID                 | User ID (e.g. `DATAFOLD`)                                        |
| Password                | Password for the user provided above                             |
| Database                | Database to connect to                                           |
| Authentication Database | Database name associated with the user credentials (e.g. `main`) |

Click **Create**. Your data connection is now ready!

## Diff your data

<img src="https://mintcdn.com/datafold/6lw1Jw9hmpKMxP4_/images/mongodb.png?fit=max&auto=format&n=6lw1Jw9hmpKMxP4_&q=85&s=b34d51e42a44012a9a8bb7f1c838d123" alt="Write your MongoDB query" data-og-width="1156" width="1156" data-og-height="786" height="786" data-path="images/mongodb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6lw1Jw9hmpKMxP4_/images/mongodb.png?w=280&fit=max&auto=format&n=6lw1Jw9hmpKMxP4_&q=85&s=1e5d1e043b3e2d6ac81b3a7bb74c48d9 280w, https://mintcdn.com/datafold/6lw1Jw9hmpKMxP4_/images/mongodb.png?w=560&fit=max&auto=format&n=6lw1Jw9hmpKMxP4_&q=85&s=70602df16b4660d64755427f261133ba 560w, https://mintcdn.com/datafold/6lw1Jw9hmpKMxP4_/images/mongodb.png?w=840&fit=max&auto=format&n=6lw1Jw9hmpKMxP4_&q=85&s=11e11ba68b97e45b21dadd64cb45441f 840w, https://mintcdn.com/datafold/6lw1Jw9hmpKMxP4_/images/mongodb.png?w=1100&fit=max&auto=format&n=6lw1Jw9hmpKMxP4_&q=85&s=4213b5d6dca1b6b0cee35fb668d0fee1 1100w, https://mintcdn.com/datafold/6lw1Jw9hmpKMxP4_/images/mongodb.png?w=1650&fit=max&auto=format&n=6lw1Jw9hmpKMxP4_&q=85&s=55ccabd3ac64ec4244e9750df68b57f7 1650w, https://mintcdn.com/datafold/6lw1Jw9hmpKMxP4_/images/mongodb.png?w=2500&fit=max&auto=format&n=6lw1Jw9hmpKMxP4_&q=85&s=8af2b8e31c760ae48d6cf12cc0da9857 2500w" />

MongoDB works a bit differently from our other integrations. Under the hood, we flatten your collections into datasets you can query with SQL. Here's how to diff your MongoDB data:

1. Create a new data diff
2. Select your MongoDB data connection
3. Select `Query` diff (`Table` diffs aren't supported at this time)
4. Write a SQL query against the flattened dataset, including a `PRAGMA` statement with the collection name on the first line. Here's an example:
   ```sql  theme={null}
   PRAGMA mongodb_collections('tracks_v1_1m');

   SELECT point_id,
       device_id,
       timestamp,
       location.longitude as longitude,
       location.latitude as latitude
   FROM mongo_tracks_v1_1m
   WHERE point_id < 100000;
   ```
5. Configure the rest of your diff and run it!
