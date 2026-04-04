# Source: https://firebase.google.com/docs/firestore/enterprise/migrate-to-firestore-with-mongodb.md.txt

<br />

<br />

|--------------------------------------------------------|
| *Relevant to Cloud Firestore Enterprise edition only.* |

<br />

You can migrate your MongoDB-compatible source database to a Firestore with MongoDB compatibility database with minimal downtime.

## Migration steps

This section details out the various migration steps.

The Datastream service creates a stream between a source and a destination. In this case, the source is your current MongoDB-compatible deployment, while the destination is Cloud Storage. This process has the following steps:

1. [Create a source Datastream connection profile](https://cloud.google.com/firestore/mongodb-compatibility/docs/migrate-create-connection-profiles)for your MongoDB source. Specific instructions depend on the type and the way your MongoDB-compatible source is deployed.

2. [Create a Cloud Storage bucket](https://cloud.google.com/firestore/mongodb-compatibility/docs/migrate-configure-resources#create-bucket)that will receive the data and the change events from your MongoDB-compatible source database.

3. [Create a destination Datastream connection profile](https://cloud.google.com/firestore/mongodb-compatibility/docs/migrate-create-connection-profiles#connection-profile-storage)that uses this Cloud Storage bucket.

4. [Create and actuate a Datastream stream](https://cloud.google.com/firestore/mongodb-compatibility/docs/migrate-import-from-source)that connects the source connection profile to the destination connection profile.

5. [Initiate a Dataflow pipeline](https://cloud.google.com/firestore/mongodb-compatibility/docs/migrate-write-to-destination)to begin injecting the captured data into yourCloud Firestorewith MongoDB compatibility database.

6. [Monitor the stream](https://cloud.google.com/firestore/mongodb-compatibility/docs/migrate-traffic#migration-completion-milestones)to identify important milestones in the migration process to determine whether any errors were encountered during the data transfer.

7. When it's appropriate,[shut down write traffic](https://cloud.google.com/firestore/mongodb-compatibility/docs/migrate-traffic#shut-down-write-traffic)to the source database. After all data, including recent changes, was replicated to theCloud Firestorewith MongoDB compatibility database, redirect read traffic to the new destination.

8. [Enable write traffic](https://cloud.google.com/firestore/mongodb-compatibility/docs/migrate-traffic#migrate-write-traffic)to yourCloud Firestorewith MongoDB compatibility database.