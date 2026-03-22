# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/manage-datasets/manage-batches.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/manage-datasets/manage-batches.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/manage-datasets/manage-batches.md

# Source: https://docs.roboflow.com/datasets/manage-datasets/manage-batches.md

# Dataset Batches

Once you [upload your data](https://docs.roboflow.com/datasets/adding-data) into Roboflow, that data you uploaded turns into a batch. Batches are a group of images that you can track throughout the dataset process in Roboflow.

You can view all batches on the Annotate page of your project.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-604d87e6816990d465ab6573758a48cf50ba9282%2Fimage.png?alt=media" alt=""><figcaption><p>The view in the Annotate page. Note: The review column is not be available for Public users.</p></figcaption></figure>

Once images are uploaded, they are in the Unassigned column.

You can assign a batch for someone to annotate, sending it to the Annotating column. You can also assign a selection of images in a batch. In this case, any unassigned images are moved into a new batch in Unassigned.

Once images in a batch are annotated, they are sent to Review (for users with Review Mode available) or to the Dataset column.

If batches are in the Review column, some or all are either approved or rejected. Approved batches will go into the Dataset column. Rejected batches are sent back to the Annotating column

### Deleting a Batch

{% hint style="danger" %}
Deletions are permanent and irreversible. Roboflow cannot recover deleted batches.
{% endhint %}

You can only delete a batch in the Unassigned column. If the batch you want to delete is in the Annotating, Review or Dataset column, you will have to click `Move to unassigned` before clicking `Delete Job`.

You can delete batches by clicking on the three dots next to the batch name and clicking "Delete Batch".

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-01bd8772fefc8e63d3a62aa430aaa45b31471f53%2Fimage.png?alt=media" alt="" width="279"><figcaption></figcaption></figure>
