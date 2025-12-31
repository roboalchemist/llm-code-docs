# Source: https://firebase.google.com/docs/reference/admin/python/firebase_admin.firestore.md.txt

# firebase_admin.firestore module

Cloud Firestore module.

This module contains utilities for accessing the Google Cloud Firestore databases associated with
Firebase apps. This requires the google-cloud-firestore Python module.

## Functions

|                                                                                                                                                                                                                                                            ### client firebase_admin.firestore.client(*app: [App](https://firebase.google.com/docs/reference/admin/python/firebase_admin#firebase_admin.App "firebase_admin.App") \| None = None* , *database_id: str \| None = None* ) â Client                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Returns a client that can be used to interact with Google Cloud Firestore. Parameters: : - **app** -- An App instance (optional). - **database_id** -- The database ID of the Google Cloud Firestore database to be used. Defaults to the default Firestore database ID if not specified or an empty string (optional). Returns: :   A [Firestore Client](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client). Return type: :   google.cloud.firestore.Firestore Raises: :   **ValueError** -- If the specified database ID is not a valid string, or if a project ID is not specified either via options, credentials or environment variables, or if the specified project ID is not a valid string. |