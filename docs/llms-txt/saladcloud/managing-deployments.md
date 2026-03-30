# Source: https://docs.salad.com/container-engine/how-to-guides/managing-deployments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Deployments

*Last Updated: October 9, 2025*

### Listing your Container Deployments

In the SaladCloud Portal, you're able to see your deployments for each project on the Container Deployments List page.
This page shows a high-level view for each of the container groups within the project, including:

* Name of the deployment
* Date created
* [Deployment status (Preparing, Stopped, Deploying, Running, Failed)](/container-engine/explanation/container-groups/deployment-lifecycle)
* Replicas running
* Version
* Container Gateway details (if enabled)
* Image source
* Allocated resources (total desired replica count and vCPUs, RAM and GPU(s) allocated to each replica)

<img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-list-container-groups.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=7cdd620286539ed0c0e49118c380ed37" data-og-width="1421" width="1421" data-og-height="820" height="820" data-path="container-engine/images/portal-list-container-groups.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-list-container-groups.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=a6953ade92bab1a20096d36b0ded6eef 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-list-container-groups.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=e1299f039655068a8efc9951b7e33600 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-list-container-groups.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=6760ea0735489563b4b7248db8c5c825 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-list-container-groups.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=c807dd093015af1e428f11d2e960194a 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-list-container-groups.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=958bf04f380ac5fd262532e628708054 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-list-container-groups.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=ac5d1fd8c41bec65ca08480a56a64a39 2500w" />

### Managing a Container Deployment

Click on any of your deployments to drill down to the Container Deployment Detail page. From here, you can start, stop,
and delete your deployment, as well as edit the display name, replica count, image source, resource requirements, and
other configuration settings

<img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-view-container-group.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=caa05c96772e2ee8b4a40a11640df87b" data-og-width="1423" width="1423" data-og-height="905" height="905" data-path="container-engine/images/portal-view-container-group.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-view-container-group.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=4bb0bdfdadade429344c9bb72b0bf16f 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-view-container-group.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=16df7ced8d937050d01b9e98338257a0 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-view-container-group.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=8b34873bede32b1dbc676d1285909b7c 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-view-container-group.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=ba6736b4221d8f3f32cc1f14e70ab0b3 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-view-container-group.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=fd40a2b76ef8a92b505272fa8d0bd93d 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-view-container-group.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=8aa122987952642f718df5e8cbd617e2 2500w" />

### Managing Container Instances

On this page, you can also see a table of all instances of your container that have been allocated, are running,
stopping, or failed. You can also manage these instances by clicking the action button next to an entry in the list of
running instances.

You can perform the following actions:

**Restart a container instance** Occasionally, a workload may run for awhile on your node and then some part of the
application might hang. In these cases, it's typically faster to get back up and running by restarting the container on
the same node, rather than searching for a new one. The **Restart** option allows you to restart your container on the
node, with all settings and downloaded data intact.

**Recreate a container instance** For a harder reset, the **Recreate** option allows you to rebuild the container from
scratch on the node. These features are accessible from the actions dropdown next to each node on the container group
detail page.

**Reallocate a container instance** If a workload fails to run, SaladCloud will automatically reallocate your container
to a new node that matches the requirements you specified. However, in some rare cases, a node has trouble running a
container replica but doesn't outright *fail*. If this happens, it's helpful to be able to manually trigger a
reallocation of the workload to a new node.

**View Container Logs** Use this link to open the Container Logs tab with the Machine ID filter pre-filled.

### Failures

If container images exit with a 0 exit code, they may be restarted on the same node. If container images exit with a
non-0 exit code, they will be blocked from the current node and reallocated to another node. Customization of this
behavior is coming soon.

### Editing Your Container Group Deployment

Inside the "Edit" option on the Managing Deployments page in Salad, you have the flexibility to modify key parameters of
your Container Group deployment.

* You can change the Display Name to make deployments more descriptive and easily identifiable. Note: the Container
  Group Name, set upon creation, cannot be edited.
* You can update the Image Source URL. For private registries, re-enter authentication details. You'll see the first 12
  characters of the image digest hash after saving.
* You can adjust the replica count to scale your application up or down as needed.
* You can modify hardware resource requirements, such as the number of vCPUs, Memory (RAM), GPUs, and
  [Disk Space](/container-engine/explanation/container-groups/disk-space).
* You can edit the [Health Check Probes](/container-engine/explanation/infrastructure-platform/health-probes) (Startup,
  and Liveness).
* You can edit the [Command](/container-engine/how-to-guides/specifying-a-command).
* If enabled, you can edit the [Container Gateway](/container-engine/explanation/infrastructure-platform/networking)
  Port. Note: the edit Container Group functionality doesn't allow for the Container Gateway to be disabled, enabled, or
  authentication to be changed.
* You can modify or enable/disable the
  [External Logging](/container-engine/explanation/infrastructure-platform/external-logging) Services.
* You can edit the [Environment Variables](/container-engine/how-to-guides/environment-variables).

This editing functionality lets you update your container images, change hardware requirements, adjust configuration
aspects, and utilize new features that SaladCloud may release. As you make changes, you will see the predicted cost
associated with those choices updated in real-time.

**Runtime changes restart replicas when required**

* When you save any change that produces a new container version—such as adjustments to the image, command, health
  probes, environment variables, or gateway settings—SaladCloud restarts every replica so the new configuration is
  applied consistently. If the update references a new image, the platform pulls the image first and then restarts the
  replicas when the download completes.
* Updating CPU, RAM, GPU class, or disk space settings keeps existing replicas running if their current nodes still
  satisfy the new requirements. Replicas that fall outside the updated limits are reallocated to compliant nodes, so
  only those instances restart.
* Display name edits, replica count adjustments, and autoscaler configuration updates apply without forcing a restart.
* Because restarts happen right away, plan rollouts carefully and consult
  [Deployment Strategies on SaladCloud](/container-engine/how-to-guides/deployment-strategies) for approaches that
  maintain availability during updates.

If you are updating the Image Source, you will not be able to make additional edits until the new image is done
preparing/pulling. To avoid confusion the “Edit” button will be disabled until this process is complete.

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-instance-actions.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=8a65c71f600da256535dc3bcf7c780a0" data-og-width="1223" width="1223" data-og-height="620" height="620" data-path="container-engine/images/portal-container-instance-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-instance-actions.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=c52691eb077bfef2094c4c9f99867f63 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-instance-actions.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=7d12c709cdfb4a35e98f741d2614e801 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-instance-actions.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=37d400ec34d83043b5e2e247705eb3d5 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-instance-actions.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=7cc9b08cd7f1fb03022f8d674f158a47 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-instance-actions.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=5c610fa29d65c6c876b5bb2d1881dab9 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-instance-actions.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=b5ce1f73c0685fe524a85822cb26c6a8 2500w" />

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-instance-version.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=017d35be28819c3cf0320dce7c357ede" data-og-width="1162" width="1162" data-og-height="190" height="190" data-path="container-engine/images/portal-container-instance-version.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-instance-version.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=54ab9b9ad9a9d945187878b584f958a2 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-instance-version.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=346a696cf0c5fcf88ad7483ee78ac12a 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-instance-version.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=27dc9550c7685d8dca14e77e4ec59e04 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-instance-version.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=9e5108eaa965cec416adc6d3120a0d4a 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-instance-version.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=24c39e6445d9bc60075945cb961f0a09 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-container-instance-version.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=4e4e3aad634003f375aeb623c3726c01 2500w" />

To access the editing options for your Container Group deployment, simply navigate to the SaladCloud dashboard, locate
your deployment, and select the "Edit" option. To access the Reallocate option after edits resulting in a new container
version, locate the container instance (on the Container Group detail page) expand the menu in the Actions column, and
select "Reallocate".
