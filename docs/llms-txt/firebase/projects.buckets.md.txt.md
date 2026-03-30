# Source: https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets.md.txt

# REST Resource: projects.buckets

## Resource: Bucket

A Google Cloud Storage bucket and its relationship to a parent Firebase project.

| JSON representation |
|---|
| ``` { "name": string } ``` |

| Fields ||
|---|---|
| `name` | `string` Output only. Resource name of the bucket. |

| ## Methods ||
|---|---|
| ### `https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets/addFirebase` | Links a Google Cloud Storage bucket to the specified Firebase project. |
| ### `https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets/get` | Gets the specified linked Cloud Storage for Firebase bucket. |
| ### `https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets/list` | Lists the linked Cloud Storage for Firebase buckets for the specified Firebase project. |
| ### `https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets/removeFirebase` | Unlinks a linked Cloud Storage for Firebase bucket from the specified Firebase project. |