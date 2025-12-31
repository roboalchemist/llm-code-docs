# Source: https://firebase.google.com/docs/firestore/enterprise/securing-with-vpc-sc.md.txt

<br />

[VPC Service Controls](https://cloud.google.com/vpc-service-controls/)lets organizations define a perimeter aroundGoogle Cloudresources to mitigate data exfiltration risks. With VPC Service Controls, you create perimeters that protect the resources and data of services that you explicitly specify.

## BundledCloud Firestoreservices

The following APIs are bundled together in VPC Service Controls:

- `firestore.googleapis.com`
- `datastore.googleapis.com`
- `firestorekeyvisualizer.googleapis.com`

When you restrict the`firestore.googleapis.com`service in a perimeter, the perimeter also restricts the`datastore.googleapis.com`and`firestorekeyvisualizer.googleapis.com`services.

### Restrict the datastore.googleapis.com service

The`datastore.googleapis.com`service is bundled under the`firestore.googleapis.com`service. To restrict the`datastore.googleapis.com`service, you must restrict the`firestore.googleapis.com`service as follows:

- When creating a service perimeter using the Google Cloud console, addCloud Firestoreas the restricted service.
- When creating a service perimeter using theGoogle Cloud CLI, use`firestore.googleapis.com`instead of`datastore.googleapis.com`.

      --perimeter-restricted-services=firestore.googleapis.com

### App Enginelegacy bundled services forDatastore

[App Enginelegacy bundled services forDatastore](https://cloud.google.com/appengine/docs/standard/python/bundled-services-overview)don't support service perimeters. Protecting theDatastoreservice with a service perimeter blocks traffic fromApp Enginelegacy bundled services. Legacy bundled services include:

- [Java 8DatastorewithApp EngineAPIs](https://cloud.google.com/appengine/docs/standard/java/datastore)
- [Python 2 NDB client library forDatastore](https://cloud.google.com/appengine/docs/standard/python/ndb/creating-entities)
- [Go 1.11DatastorewithApp EngineAPIs](https://cloud.google.com/appengine/docs/standard/go111/datastore)

## Egress protection on import and export operations

Cloud Firestore with MongoDB compatibility supports VPC Service Controls but requires additional configuration to get full egress protection on import and export operations. You must use theCloud Firestoreservice agent to authorize import and export operations instead of the defaultApp Engineservice account. Use the following instructions to view and configure the authorization account for import and export operations.