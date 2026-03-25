# Source: https://docs.verda.com/storage/deleting-storage.md

# Deleting storage

When a storage item is deleted, it is sent to the trash for 96 hours, during which time it can be restored. The restore cost is the Pay As You Go price for the amount of time the volume was deleted, and will be deducted from your project balance.

To free up storage quota, you must permanently delete the storage. In the console, go to **Deleted volumes** and click **Permanently delete** from the actions menu. Please note that this action cannot be undone.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-1857f49c9d5506b5900b00dcfdb5ba24c8216b31%2Fdelete%20storage.png?alt=media" alt=""><figcaption></figcaption></figure>

Alternatively, you can also permanently delete a volume via the Public API by or Python SDK [by adding the flag `is_permanent:true`](https://api.datacrunch.io/v1/docs#tag/volumes/DELETE/v1/volumes/{volume_id}).
