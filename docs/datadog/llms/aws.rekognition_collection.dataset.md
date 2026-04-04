# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rekognition_collection.dataset.md

---
title: Rekognition Collection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Rekognition Collection
---

# Rekognition Collection

An Amazon Rekognition Collection is a container used to store and manage facial feature vectors for face recognition. It allows you to index faces, search for matches, and organize face data for applications like identity verification, user authentication, or security monitoring.

```
aws.rekognition_collection
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                              | Description |
| ------------------ | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| collection_arn     | core | string     | The Amazon Resource Name (ARN) of the collection.                                                                                                                                      |
| creation_timestamp | core | timestamp  | The number of milliseconds since the Unix epoch time until the creation of the collection. The Unix epoch time is 00:00:00 Coordinated Universal Time (UTC), Thursday, 1 January 1970. |
| face_count         | core | int64      | The number of faces that are indexed into the collection. To index faces into a collection, use IndexFaces.                                                                            |
| face_model_version | core | string     | The version of the face model that's used by the collection for face detection. For more information, see Model versioning in the Amazon Rekognition Developer Guide.                  |
| tags               | core | hstore_csv |
| user_count         | core | int64      | The number of UserIDs assigned to the specified colleciton.                                                                                                                            |
