# Source: https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.defaultBucket.md.txt

# REST Resource: projects.defaultBucket

## Resource: DefaultBucket

The default Cloud Storage for Firebase bucket for the Firebase project. This resource exists if the underlying Cloud Storage bucket exists and it's linked to the Firebase project. One per project.

The bucket name format and [pricing plan](https://firebase.google.com/pricing) requirements depend on when the bucket was provisioned:

- **If provisioned *before* October 30, 2024** : The bucket name format is `{PROJECT_ID}.appspot.com`, and access to the bucket will require the pay-as-you-go Blaze pricing plan starting October 1, 2025.
- **If provisioned *on or after* October 30, 2024** : The bucket name format is `{PROJECT_ID}.firebasestorage.app`, and access to the bucket requires the pay-as-you-go Blaze pricing plan.

|                                                                         JSON representation                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "name": string, "location": string, "bucket": { object (https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets#Bucket) } } ``` |

|                                                                                                                                                                                                                              Fields                                                                                                                                                                                                                              ||
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`     | `string` Resource name of the default bucket.                                                                                                                                                                                                                                                                                                                                                                                                        |
| `location` | `string` Immutable. Location of the default bucket. This location depends on when the default bucket was provisioned: - If provisioned *before* October 30, 2024: one of the [available Google App Engine locations](https://cloud.google.com/about/locations#regions). - If provisioned *on or after* October 30, 2024: one of the [available Google Cloud Storage locations](https://cloud.google.com/storage/docs/locations#available-locations). |
| `bucket`   | `object (`[Bucket](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets#Bucket)`)` Output only. Underlying bucket resource.                                                                                                                                                                                                                                                                                         |

|                                                                                                 ## Methods                                                                                                 ||
|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| ### [create](https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.defaultBucket/create) | Creates the default Cloud Storage bucket and links it to the specified Firebase project. |