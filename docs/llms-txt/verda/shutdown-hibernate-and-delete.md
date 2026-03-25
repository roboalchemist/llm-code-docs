# Source: https://docs.verda.com/cpu-and-gpu-instances/shutdown-hibernate-and-delete.md

# Shutdown and Delete

{% hint style="info" %}
UPDATE: We have removed **Hibernate** because it was the same as **Delete** while keeping all storage. You can select storage items when deleting an instance, providing more flexibility and accuracy.
{% endhint %}

## What is the difference between shutting down and deleting GPU instances?

### Shutdown

Shutting down an instance temporarily pauses it so technical processes can occur, such as attaching or detaching volumes.

{% hint style="warning" %}
Shutdown instances continue to charge your account.
{% endhint %}

You can shutdown instances from two locations: the actions menu on the Instance card and on the overview page (image below). This is useful when you are editing, attaching, or detaching storage.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-aac44aeeb0cea80e14826dd69df9057f6887b7d1%2Fshutdown.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Force shutdown

Use **Force shutdown** if regular shutdown is not responsive. All running processes will be stopped with possible data loss or corruption.

#### Delete

Deleting an instance removes the instance and attached volumes of your choosing. You can find the **Delete instance** option in the same action menus listed above.

By default, no storage is selected for deletion. All storage not marked for deletion will continue to charge you account. Detached storage can be attached to new instances.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-e2c757c310ed819b9c75cbbd79a96940a78e2f36%2Fdelete%20compute.png?alt=media" alt=""><figcaption></figcaption></figure>
