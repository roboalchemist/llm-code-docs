# Source: https://firebase.google.com/docs/reference/admin/python/firebase_admin.instance_id.md.txt

# firebase_admin.instance_id module

Firebase Instance ID module.

This module enables deleting instance IDs associated with Firebase projects.

## Functions

|                                                                                                                                                                                                                                                                                         ### delete_instance_id firebase_admin.instance_id.delete_instance_id(*instance_id* , *app=None* )                                                                                                                                                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Deletes the specified instance ID and the associated data from Firebase. Note that Google Analytics for Firebase uses its own form of Instance ID to keep track of analytics data. Therefore deleting a regular Instance ID does not delete Analytics data. See [Delete an Instance ID](https://firebase.google.com/support/privacy/manage-iids#delete_an_instance_id) for more information. Parameters: : - **instance_id** -- A non-empty instance ID string. - **app** -- An App instance (optional). Raises: : - **InstanceIdError** -- If an error occurs while invoking the backend instance ID service. - **ValueError** -- If the specified instance ID or app is invalid. |