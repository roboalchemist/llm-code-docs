# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/instances_manage/

[]

# How to manage instances[¶](#how-to-manage-instances "Link to this heading")

When listing the existing instances, you can see their type, status, and location (if applicable). You can filter the instances and display only the ones that you are interested in.

CLI

API

UI

Enter the following command to list all instances:

    lxc list

You can filter the instances that are displayed, for example, by type, status or the cluster member where the instance is located:

    lxc list type=container
    lxc list status=running
    lxc list location=server1

You can also filter by name. To list several instances, use a regular expression for the name. For example:

    lxc list ubuntu.*

Enter [[[`lxc`]` `[`list`]` `[`--help`]]](../../reference/manpages/lxc/list/#lxc-list-md) to see all filter options.

Query the [`/1.0/instances`] endpoint to list all instances. You can use [[Recursion]](../../rest-api/#rest-api-recursion) to display more information about the instances:

    lxc query --request GET /1.0/instances?recursion=2

You can [[filter]](../../rest-api/#rest-api-filtering) the instances that are displayed, by name, type, status or the cluster member where the instance is located:

    lxc query --request GET /1.0/instances?filter=name+eq+ubuntu
    lxc query --request GET /1.0/instances?filter=type+eq+container
    lxc query --request GET /1.0/instances?filter=status+eq+running
    lxc query --request GET /1.0/instances?filter=location+eq+server1

To list several instances, use a regular expression for the name. For example:

    lxc query --request GET /1.0/instances?filter=name+eq+ubuntu.*

See [[`GET`]` `[`/1.0/instances`]](/lxd/latest/api/#/instances/instances_get) for more information.

Go to [Instances] to see a list of all instances.

You can filter the instances that are displayed by status, instance type, or the profile they use by selecting the corresponding filter.

In addition, you can search for instances by entering a search text. The text you enter is matched against the name, the description, and the name of the base image.

## Show information about an instance[¶](#show-information-about-an-instance "Link to this heading")

CLI

API

UI

Enter the following command to show detailed information about an instance:

    lxc info <instance_name>

Add [`--show-log`] to the command to show the latest log lines for the instance:

    lxc info <instance_name> --show-log

Query the following endpoint to show detailed information about an instance:

    lxc query --request GET /1.0/instances/<instance_name>

See [[`GET`]` `[`/1.0/instances/`]](/lxd/latest/api/#/instances/instance_get) for more information.

Clicking an instance line in the overview will show a summary of the instance information right next to the instance list.

Click the instance name to go to the instance detail page, which contains detailed information about the instance.

[]

## Start an instance[¶](#start-an-instance "Link to this heading")

CLI

API

UI

Enter the following command to start an instance:

    lxc start <instance_name>

You will get an error if the instance does not exist or if it is running already.

To immediately attach to the console when starting, pass the [`--console`] flag. For example:

    lxc start <instance_name> --console

See [[How to access the console]](../instances_console/#instances-console) for more information.

To start an instance, send a PUT request to change the instance state:

    lxc query --request PUT /1.0/instances/<instance_name>/state --data ''

The return value of this query contains an operation ID, which you can use to query the status of the operation:

    lxc query --request GET /1.0/operations/<operation_ID>

Use the following query to monitor the state of the instance:

    lxc query --request GET /1.0/instances/<instance_name>/state

See [[`GET`]` `[`/1.0/instances//state`]](/lxd/latest/api/#/instances/instance_state_get) and [[`PUT`]` `[`/1.0/instances//state`]](/lxd/latest/api/#/instances/instance_state_put)for more information.

To start an instance, go to the instance list or the respective instance and click the [Start] button (▷).

You can also start several instances at the same time by selecting them in the instance list and clicking the [Start] button at the top.

On the instance detail page, select the [Console] tab to see the boot log with information about the instance starting up. Once it is running, you can select the [Terminal] tab to access the instance.

### Prevent accidental start of instances[¶](#prevent-accidental-start-of-instances "Link to this heading")

To protect a specific instance from being started, set [[`security.protection.start`]](../../reference/instance_options/#instance-security:security.protection.start) to [`true`] for the instance. See [[How to configure instances]](../instances_configure/#instances-configure) for instructions.

[]

## Stop an instance[¶](#stop-an-instance "Link to this heading")

CLI

API

UI

Enter the following command to stop an instance:

    lxc stop <instance_name>

You will get an error if the instance does not exist or if it is not running.

To stop an instance, send a PUT request to change the instance state:

    lxc query --request PUT /1.0/instances/<instance_name>/state --data ''

The return value of this query contains an operation ID, which you can use to query the status of the operation:

    lxc query --request GET /1.0/operations/<operation_ID>

Use the following query to monitor the state of the instance:

    lxc query --request GET /1.0/instances/<instance_name>/state

See [[`GET`]` `[`/1.0/instances//state`]](/lxd/latest/api/#/instances/instance_state_get) and [[`PUT`]` `[`/1.0/instances//state`]](/lxd/latest/api/#/instances/instance_state_put)for more information.

To stop an instance, go to the instance list or the respective instance and click the [Stop] button (□). You are then prompted to confirm.

Tip

To skip the confirmation prompt, hold the [Shift] key while clicking.

You can choose to force-stop the instance. If stopping the instance takes a long time or the instance is not responding to the stop request, click the spinning stop button to go back to the confirmation prompt, where you can select to force-stop the instance.

You can also stop several instances at the same time by selecting them in the instance list and clicking the [Stop] button at the top.

[]

## Delete an instance[¶](#delete-an-instance "Link to this heading")

If you don't need an instance anymore, you can remove it. The instance must be stopped before you can delete it.

CLI

API

UI

Enter the following command to delete an instance:

    lxc delete <instance_name>

To delete an instance, send a DELETE request to the instance:

    lxc query --request DELETE /1.0/instances/<instance_name>

See [[`DELETE`]` `[`/1.0/instances/`]](/lxd/latest/api/#/instances/instance_delete) for more information.

To delete an instance, go to its instance detail page and click [Delete instance]. You are then prompted to confirm.

Tip

To skip the confirmation prompt, hold the [Shift] key while clicking.

You can also delete several instances at the same time by selecting them in the instance list and clicking the [Delete] button at the top.

Caution

This command permanently deletes the instance and all its snapshots.

### Prevent accidental deletion of instances[¶](#prevent-accidental-deletion-of-instances "Link to this heading")

There are different ways to prevent accidental deletion of instances:

-   To protect a specific instance from being deleted, set [[`security.protection.delete`]](../../reference/instance_options/#instance-security:security.protection.delete) to [`true`] for the instance. See [[How to configure instances]](../instances_configure/#instances-configure) for instructions.

-   In the CLI client, you can create an alias to be prompted for approval every time you use the [[[`lxc`]` `[`delete`]]](../../reference/manpages/lxc/delete/#lxc-delete-md) command:

    ::: 
    ::: highlight
         lxc alias add delete "delete -i"
    :::
    :::

[]

## Rebuild an instance[¶](#rebuild-an-instance "Link to this heading")

If you want to wipe and re-initialize the root disk of your instance but keep the instance configuration, you can rebuild the instance.

Rebuilding is only possible for instances that do not have any snapshots.

Stop your instance before rebuilding it.

CLI

API

UI

Enter the following command to rebuild the instance with a different image:

    lxc rebuild <image_name> <instance_name>

Enter the following command to rebuild the instance with an empty root disk:

    lxc rebuild <instance_name> --empty

For more information about the [`rebuild`] command, see [[[`lxc`]` `[`rebuild`]` `[`--help`]]](../../reference/manpages/lxc/rebuild/#lxc-rebuild-md).

To rebuild the instance with a different image, send a POST request to the instance's [`rebuild`] endpoint. For example:

    lxc query --request POST /1.0/instances/<instance_name>/rebuild --data '
    }'

To rebuild the instance with an empty root disk, specify the source type as [`none`]:

    lxc query --request POST /1.0/instances/<instance_name>/rebuild --data '
    }'

See [[`POST`]` `[`/1.0/instances//rebuild`]](/lxd/latest/api/#/instances/instance_rebuild_post) for more information.

Rebuilding an instance is not yet supported in the UI.