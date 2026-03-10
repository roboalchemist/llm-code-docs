# Source: https://firebase.google.com/docs/storage/locations.md.txt

# Locations for Cloud Storage for Firebase

<br />

When you provision a Cloud Storage bucket, you must choose a *location* for the
bucket. To reduce latency and increase availability, store your data close to
the users and services that need it.

You can optionally create multiple buckets in your project, each with its own
location setting. For details, see the Cloud Storage getting started guide for
your platform (
[iOS+](https://firebase.google.com/docs/storage/ios/start#use_multiple_storage_buckets) \|
[Android+](https://firebase.google.com/docs/storage/android/start#use_multiple_storage_buckets) \|
[Web](https://firebase.google.com/docs/storage/web/start#use_multiple_storage_buckets) \|
[Flutter](https://firebase.google.com/docs/storage/flutter/start#use_multiple_storage_buckets) \|
[Unity](https://firebase.google.com/docs/storage/unity/start#use_multiple_storage_buckets) \|
[C++](https://firebase.google.com/docs/storage/cpp/start#use_multiple_storage_buckets)
).

Be aware that once you provision a bucket, you cannot change its location
setting.

In the Google Cloud Storage documentation, you can find more information
about location settings and
[available Cloud Storage locations](https://cloud.google.com/storage/docs/locations#available-locations).
These locations are applicable to your default Cloud Storage bucket with the name
format `PROJECT_ID.firebasestorage.app` as well any additional
Cloud Storage buckets in your project.

> [!NOTE]
> **Note:** At this time, Cloud Storage for Firebase does not support [configurable dual-regions](https://cloud.google.com/storage/docs/locations#configurable).

Buckets in `US-CENTRAL1`, `US-EAST1`, and `US-WEST1` can take advantage of the
["Always Free" tier](https://cloud.google.com/storage/pricing#cloud-storage-always-free) for Google Cloud Storage. Buckets
in all other locations follow
[Google Cloud Storage pricing and usage](https://cloud.google.com/storage/pricing).

> [!NOTE]
> **Important** : If your project has a default Cloud Storage bucket with the name format `PROJECT_ID.appspot.com`, note the following about its location:
>
> - Its location is one of the [available Google App Engine locations](https://cloud.google.com/about/locations#region).
> - Its location has a dependency on the ["location for default Google Cloud resources"](https://firebase.google.com/docs/projects/locations#default-cloud-location). When you provisioned that default bucket, the location might have already been set, either during project creation or when setting up another service that shares this location dependency.
>
>   The location setting for a default Cloud Storage bucket with the name
>   format `PROJECT_ID.firebasestorage.app` does not share this
>   dependency.