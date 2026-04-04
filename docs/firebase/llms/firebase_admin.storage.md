# Source: https://firebase.google.com/docs/reference/admin/python/firebase_admin.storage.md.txt

# firebase_admin.storage module

Firebase Cloud Storage module.

This module contains utilities for accessing Google Cloud Storage buckets associated with
Firebase apps. This requires the google-cloud-storage Python module.

## Functions

|                                                                                                                                                                                                                                                                            ### bucket firebase_admin.storage.bucket(*name=None* , *app=None* ) â Bucket                                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Returns a handle to a Google Cloud Storage bucket. If the name argument is not provided, uses the 'storageBucket' option specified when initializing the App. If that is also not available raises an error. This function does not make any RPC calls. Parameters: : - **name** -- Name of a cloud storage bucket (optional). - **app** -- An App instance (optional). Returns: :   A handle to the specified bucket. Return type: :   google.cloud.storage.Bucket Raises: :   **ValueError** -- If a bucket name is not specified either via options or method arguments, or if the specified bucket name is not a valid string. |