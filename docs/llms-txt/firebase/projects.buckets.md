# Source: https://firebase.google.com/docs/reference/rest/storage/rest/v1alpha/projects.buckets.md.txt

# Source: https://firebase.google.com/docs/reference/rest/storage/rest/v1beta/projects.buckets.md.txt

# REST Resource: projects.buckets

## Resource: Bucket

A storage bucket and its relation to a parent Firebase project.

|    JSON representation     |
|----------------------------|
| ``` { "name": string } ``` |

|                    Fields                     ||
|--------|---------------------------------------|
| `name` | `string` Resource name of the bucket. |

|                                                                                            ## Methods                                                                                            ||
|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| ### [addFirebase](https://firebase.google.com/docs/reference/rest/storage/rest/v1beta/projects.buckets/addFirebase)       | Links a Google Cloud Storage bucket to a Firebase project.            |
| ### [get](https://firebase.google.com/docs/reference/rest/storage/rest/v1beta/projects.buckets/get)                       | Gets a single linked storage bucket.                                  |
| ### [list](https://firebase.google.com/docs/reference/rest/storage/rest/v1beta/projects.buckets/list)                     | Lists the linked storage buckets for a project.                       |
| ### [removeFirebase](https://firebase.google.com/docs/reference/rest/storage/rest/v1beta/projects.buckets/removeFirebase) | Unlinks a linked Google Cloud Storage bucket from a Firebase project. |