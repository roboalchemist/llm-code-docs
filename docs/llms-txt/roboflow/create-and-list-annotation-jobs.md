# Source: https://docs.roboflow.com/developer/rest-api/create-and-list-annotation-jobs.md

# Create and List Annotation Jobs

You can use the jobs endpoint to get info about your annotation jobs, their current status or assign images for labeling by creating a new Annotation Job with images from one of your batches.

### Create a New Annotation Job

{% hint style="warning" %}
**You need to set both reviewer and labeler to an email that belong to a user in your workspace.**

If your workspace does not have Role Based Access Control enabled, you won't see the reviewer in the app interface, and should set the reviewer to the same user as the labeler.
{% endhint %}

{% tabs %}
{% tab title="Python SDK" %}
To create an annotation job, you will need an upload batch that you would like to assign to a labeler and a reviewer:

```python
import roboflow

rf = roboflow.Roboflow(api_key=ROBOFLOW_API_KEY)

project = rf.workspace().project(PROJECT_ID)

job = project.create_annotation_job(
    name="Test Annotation Job",
    batch_id=UPLOAD_BATCH_ID,
    num_images=UPLOAD_BATCH_SIZE,
    labeler_email="test@example.com",
    reviewer_email="test@example.com",
)
```

{% endtab %}

{% tab title="REST API" %}
You can make a POST request to the /jobs endpoint of your project to create a new Annotation Job in your project. To create a new job the you need to provide some JSON encoded data in the body of your POST request.

To create a new Annotation Job in a project, that assigns 10 images from one of the batches in the project to be annotated by <lenny@roboflow.com> you can make a POST request like this:

```bash
curl --location --request POST 'https://api.roboflow.com/${WORKSPACE}/${PROJECT}/jobs?api_key=${ROBOFLOW_API_KEY}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Job created by API",
    "batch": "<BATCH_ID>",
    "num_images": 10,
    "labelerEmail": "lenny@roboflow.com",
    "reviewerEmail": "lenny@roboflow.com"
}'
```

This request returns the following data:

```json
{
    "created": {
        "_seconds": 1669234345,
        "_nanoseconds": 61000000
    },
    "rejected": 0,
    "annotated": 0,
    "numImages": 2,
    "createdBy": "API",
    "owner": "holeSv3hwbzrOv37vH5b",
    "instructionsText": "No instructions provided",
    "unannotated": 2,
    "reviewer": "thomas@roboflow.com",
    "labeler": "korryn@roboflow.com",
    "name": "API Job 1",
    "project": "PBDhem3YRI1rKtQZSqRK",
    "approved": 0,
    "status": "assigned",
    "sourceBatch": "PBDhem3YRI1rKtQZSqRK/6VN0fFQIWU1E24bDjGsN",
    "id": "0IzntY4ms4ogwHwJNkIB"
}
```

{% endtab %}
{% endtabs %}

### Retrieve Annotation Job Data from the API

{% tabs %}
{% tab title="REST API" %}
To retrieve annotation job data from the REST API, make a request to the following endpoint:

```bash
curl https://api.roboflow.com/${WORKSPACE}/${PROJECT}/jobs?api_key=${ROBOFLOW_API_KEY}
```

This will return data in the following format:

```json
{
    "jobs": [
        {
            "owner": "holeSv3hwbzrOv37vH5b",
            "approved": 0,
            "createdBy": "g12lCVib0pgurZ6EqWLnApJJ4gr1",
            "sourceBatch": "PBDhem3YRI1rKtQZSqRK/6VN0fFQIWU1E24bDjGsN",
            "annotated": 3,
            "rejected": 0,
            "labeler": "thomas@roboflow.com",
            "numImages": 26,
            "status": "assigned",
            "instructionsText": "",
            "name": "Uploaded on 11/22/22 at 1:39 pm: Job 9",
            "reviewer": "thomas@roboflow.com",
            "created": {
                "_seconds": 1669148088,
                "_nanoseconds": 297000000
            },
            "project": "PBDhem3YRI1rKtQZSqRK",
            "unannotated": 23,
            "id": "5LfYNJg10Z9Kvx5Tt5Uq"
        },

        {
            "approved": 0,
            "unannotated": 2,
            "instructionsText": "Please label all the racoons in the images using polygons",
            "annotated": 12,
            "sourceBatch": "PBDhem3YRI1rKtQZSqRK/6VN0fFQIWU1E24bDjGsN",
            "project": "PBDhem3YRI1rKtQZSqRK",
            "rejected": 0,
            "owner": "holeSv3hwbzrOv37vH5b",
            "createdBy": "API",
            "status": "assigned",
            "created": {
                "_seconds": 1669148192,
                "_nanoseconds": 651000000
            },
            "labeler": "korryn@roboflow.com",
            "name": "Test Job",
            "numImages": 25,
            "reviewer": "thomas@roboflow.com",
            "id": "h2E42jt686yLyMIxxqOQ"
        }
    ]
}
```

To retrieve information about a specific job, specify the job ID:

```bash
curl https://api.roboflow.com/${WORKSPACE}/${PROJECT}/jobs/${JOB_ID}?api_key=${ROBOFLOW_API_KEY}
```

Here is the response format from this request:

```json
{
    "approved": 0,
    "unannotated": 2,
    "instructionsText": "Please label all the racoons in the images using polygons",
    "annotated": 12,
    "sourceBatch": "PBDhem3YRI1rKtQZSqRK/6VN0fFQIWU1E24bDjGsN",
    "project": "PBDhem3YRI1rKtQZSqRK",
    "rejected": 0,
    "owner": "holeSv3hwbzrOv37vH5b",
    "createdBy": "API",
    "status": "assigned",
    "created": {
        "_seconds": 1669148192,
        "_nanoseconds": 651000000
    },
    "labeler": "korryn@roboflow.com",
    "name": "Test Job",
    "numImages": 25,
    "reviewer": "thomas@roboflow.com",
    "id": "<JOB_ID>"
}
```

{% endtab %}
{% endtabs %}
