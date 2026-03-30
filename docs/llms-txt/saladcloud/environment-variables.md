# Source: https://docs.salad.com/container-engine/how-to-guides/environment-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Environment Variables

*Last Updated: September 03, 2025*

Environment variables are key-value pairs that can be used to configure and customize the behavior of server running
inside a container. These variables are accessible to processes running within the container and are commonly used to
store configuration settings, credentials, and other runtime information.

In SaladCloud Portal, you can set environment variables for your containers by providing a key-value pair. The "**key**"
represents the name of the environment variable, and the "**value**" represents its associated data.

## Default Environment Variables

Note that there are several environment variables that are set by Salad and always available to the container:

* `HOSTNAME`: Defaults to the Instance ID, but can be overridden by the user.
* `SALAD_ORGANIZATION_NAME`: The name of the organization the container is running under.
* `SALAD_ORGANIZATION_ID`: The ID of the organization the container is running under.
* `SALAD_PROJECT_NAME`: The name of the project the container is part of.
* `SALAD_PROJECT_ID`: The ID of the project the container is part of.
* `SALAD_CONTAINER_GROUP_NAME`: The name of the container group the container is part of.
* `SALAD_CONTAINER_GROUP_ID`: The ID of the entire container group.
* `SALAD_INSTANCE_ID`: The ID of the specific container instance. This is unique to each time a container is started.
* `SALAD_MACHINE_ID`: The ID of the machine the particular container instance is running on.

## **Using Environment Variables in SaladCloud Portal**

To use environment variables in SaladCloud Portal, follow these steps:

### Step 1: **Deploy a New Container**

If you haven't already, create a new container group. Please refer to our separate documentation on
"[How to Create a Container](/container-engine/explanation/container-groups/container-groups)" for detailed instructions
on this step.

### Step 2: Configure Environment Variables

In the container group creation or configuration process, locate the "Environment Variables" section in Optional
Settings and click on the "Edit" button.

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-environment-variables.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=27da9f13c0f3dae5f6071e9ae6e38895" data-og-width="649" width="649" data-og-height="111" height="111" data-path="container-engine/images/portal-edit-environment-variables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-environment-variables.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=f013fc75ab8788f1d0eb1774320415b6 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-environment-variables.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=f249ce0a7da004892940fd21d17de4b3 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-environment-variables.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=c5a4d329d941a715b98bb0846205fcf5 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-environment-variables.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=04d718955099a94ff6ce7954126dbfff 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-environment-variables.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=8b488f0ac62aa429466f1511f44f0c49 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-environment-variables.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=416fb8c5a45628de560c338235095b80 2500w" />

Enter the **key** and **value** for the environment variable you want to set and click the "Configure" button to confirm
the environment variable. Example: **Key:** HF\_TOKEN and **Value:** sometokenvalue.

<img src="https://mintcdn.com/salad/rJxc75QHrlPt5k2H/container-engine/images/portal-environment-variables-key-value-edit-2.png?fit=max&auto=format&n=rJxc75QHrlPt5k2H&q=85&s=ca6c04cf77ec4acf02d3c8c303ed66a7" data-og-width="850" width="850" data-og-height="471" height="471" data-path="container-engine/images/portal-environment-variables-key-value-edit-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/rJxc75QHrlPt5k2H/container-engine/images/portal-environment-variables-key-value-edit-2.png?w=280&fit=max&auto=format&n=rJxc75QHrlPt5k2H&q=85&s=8014b7dba6efb3d1f50203809dcf5b8a 280w, https://mintcdn.com/salad/rJxc75QHrlPt5k2H/container-engine/images/portal-environment-variables-key-value-edit-2.png?w=560&fit=max&auto=format&n=rJxc75QHrlPt5k2H&q=85&s=e3e8b6d00b2ec7b4cccfc495c683ef7b 560w, https://mintcdn.com/salad/rJxc75QHrlPt5k2H/container-engine/images/portal-environment-variables-key-value-edit-2.png?w=840&fit=max&auto=format&n=rJxc75QHrlPt5k2H&q=85&s=6b7ee605852feb9221ac05b23fcf8db3 840w, https://mintcdn.com/salad/rJxc75QHrlPt5k2H/container-engine/images/portal-environment-variables-key-value-edit-2.png?w=1100&fit=max&auto=format&n=rJxc75QHrlPt5k2H&q=85&s=394ba10672e15f33efc778b8a4aff31b 1100w, https://mintcdn.com/salad/rJxc75QHrlPt5k2H/container-engine/images/portal-environment-variables-key-value-edit-2.png?w=1650&fit=max&auto=format&n=rJxc75QHrlPt5k2H&q=85&s=fba967f5125d89a7b3426cf14a5fee3a 1650w, https://mintcdn.com/salad/rJxc75QHrlPt5k2H/container-engine/images/portal-environment-variables-key-value-edit-2.png?w=2500&fit=max&auto=format&n=rJxc75QHrlPt5k2H&q=85&s=5fa0a4da6d3b4ef9f839c65ae3b07796 2500w" />

### Step 3 : Run Your Container

Once the container is configured, you can deploy it by clicking on button “Deploy”. SaladCloud Portal will deploy the
container group and you can start the container by click on "Start" button.

<img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-start-container-group.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=02b01ffaccf38c3178e2620fa95f9890" data-og-width="1557" width="1557" data-og-height="574" height="574" data-path="container-engine/images/portal-start-container-group.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-start-container-group.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=eaec235570b59ac6365bd30e90e86661 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-start-container-group.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=c1639346e860d7ad9d4c9c25dabfff13 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-start-container-group.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=bb2cdad6fcfe1af98a4a5ca8c8de7a2d 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-start-container-group.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=ce7f762f5f9e03071917ca47d1969d7b 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-start-container-group.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=d2cecb467a9fb14f1caf1f1db6db5e8c 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-start-container-group.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=b0319a2287ff5e428d66bd1790fc8c8e 2500w" />

> 👍 Congratulations!
>
> Your container is now running and utilize environment variables to customize the behavior of your containers in Salad
> Portal. If you have any questions or need further assistance, please refer to our support resources or contact our
> [customer support team](mailto:cloud@salad.com).
