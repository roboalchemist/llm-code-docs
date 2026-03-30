# Source: https://novita.ai/docs/guides/gpu-instance-quickstart-manage-instances.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Instances

In this guide, we will show you how to stop or terminate your instances.

## Stop an Instance

* Go to <a href="https://novita.ai/gpu-instance/console/instances">Console - Instances</a>;
* In the instance list, select the instance you need to stop;
* Click the **More Operations - Stop** button;
* Confirm the **Stop** action in the pop-up window.

<Warning>
  After stopping your instance, you can start it later, but it is not guaranteed to be available because the resources may have been preempted, and all data will be saved for 7 days at most.

  Please note that you will be **charged for volume storage** while your instance is stopped. If you won't start this instance later, please terminate it to avoid disk charges.
</Warning>

## Terminate an Instance

* In the instance list, find the instance and click the **More Operations** button;
* In the action menu, select the **Terminate** option;
* Confirm the **Terminate** action in the pop-up window.

<Warning>
  Please note that terminating an instance will permanently delete the data on the instance.
</Warning>


Built with [Mintlify](https://mintlify.com).