# Source: https://docs.asapp.com/generativeagent/configuring/deploying-to-generativeagent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploying to GenerativeAgent

> Learn how to deploy GenerativeAgent.

After importing your Knowledge Base and connecting your APIs to GenerativeAgent, you need to manage deployments for GenerativeAgent's use.

You can deploy and undeploy articles and API Connections in the GenerativeAgent UI. There are also options to view version history and roll back changes in the UI.

<Note>
  You must deploy Articles or Functions separately from each other.
</Note>

## Environments

The GenerativeAgent UI offers the following environments to deploy, undeploy, or roll back:

* **Draft**: In this environment, you can try out any article or API connection.
* **Sandbox**: This environment works as a staging version to test GenerativeAgent's responses. You can test the behavior of GenerativeAgent and how it performs tasks or calls functions before deploying to a live environment.
* **Production**: When you deploy to this version, GenerativeAgent will be live in collaborating in the flows and taking over tasks within your Production environments.

For any version or environment, you can deploy Articles. API Connections are tested via Trial Mode.

This way, you are able to test how GenerativeAgent behaves with a specific article, resource, or API Connection.

## GenerativeAgent Versions

As we continue to update GenerativeAgent, we will release new versions of the core system. You can manage which version of GenerativeAgent is deployed for your organization with Pinned Versions.

On the Settings page, you can choose which version of GenerativeAgent that you want to test in the [Previewer](/generativeagent/configuring/previewer) by selecting a specific version from the Version selector.

This allows you to test how GenerativeAgent would behave under a new version.

* The `Default` version will always point to the latest version of GenerativeAgent.
* Versions with a `stable` badge have been thoroughly tested and will not change.
* Versions with a `beta` badge are in development and may change. Eventually they will become `stable`.

<Note>
  Your GenerativeAgent will use the `Default` version if no other version is pinned.

  Using the `Default` version ensures that GenerativeAgent is always using the safest version with the latest features.
</Note>

If you do want to manually pin your GenerativeAgent to specific version, select the version from Settings and deploy the Settings to your production environment.

<Frame>
  <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/PinnedVersionSelector.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=ad670c19b880f7bfdd598ef154a1a235" data-og-width="426" width="426" data-og-height="393" height="393" data-path="images/generativeagent/PinnedVersionSelector.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/PinnedVersionSelector.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=5be5b0cb79c65efb339acf53a15007b0 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/PinnedVersionSelector.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=292617ecf55604d42896e306fe35e7ee 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/PinnedVersionSelector.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=a34c7afef5547a17d84600ed6fc04964 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/PinnedVersionSelector.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=1836def9129e2681606fd5c26dbdf2c0 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/PinnedVersionSelector.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=cb18c77085843a69b0f6cc2c23636e7c 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/PinnedVersionSelector.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=cd669a02ebcc03bffd4422ac2de8aba8 2500w" />
</Frame>

<Note>
  Older versions will eventually become deprecated. ASAPP will reach out to you if you are using a deprecated version to communicate timelines and best practices for migration.
</Note>

## Articles

### Deploy Articles

To Deploy Content to Sandbox or Production environments:

1. Click on Deploy, then choose the root and the target environments.
2. Write any Release Notes that you deem necessary.
3. For Resource, select Knowledge Base.
4. You will be prompted with a list of all resources pulled from your file. Choose the content you want to upload to the Knowledge Base Tooling.
5. Click on Deploy and the system will save the content in the new version.

You can now see a list of all recently deployed content.

### Undeploy Articles

You can undeploy Content from Sandbox or Production environments:

1. Head to the Content Row and click on the ellipsis, then on Undeploy.
2. Select the environments that should undeploy the Resource.

A confirmation message appears every time you successfully undeploy a resource. Keep in mind undeployed resources can be redeployed via individual deployment.

### View Current Articles and Versions

After clicking on a Resource, you can see all of its details. You can also review each Resource's detail per version.

### View Deployment History

Deployment History shows a detailed account of all deployments across environments for each article.

<Frame>
  <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DeploymentHistory2.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=ecb6019b89d7e00986e7ac5f295f1d99" data-og-width="1600" width="1600" data-og-height="860" height="860" data-path="images/generativeagent/DeploymentHistory2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DeploymentHistory2.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=3e643b74be66a39a8d7de670e037fe78 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DeploymentHistory2.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=bb2b7cef7df4d3db3c4c6714d5c46a4e 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DeploymentHistory2.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=b0af931f8ea3e4014d65bff1103b9142 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DeploymentHistory2.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=8783029b44eee1920fd840fa76ce8780 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DeploymentHistory2.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=41580a5be7a0e1070440eddbf094fdc1 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DeploymentHistory2.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=e3d63c88ac745848eb014f08c0b3d46d 2500w" />
</Frame>

On the Deployment History tab, you can:

1. Toggle between Production and Sandbox to access environment specific deployments.
2. Filter deployment records by time frames.
3. Manage Deployment and rollback to previous versions.

<Note>
  Each deployment entry shows date, time, type, and a brief description of deployment.
</Note>

## API Connections

When you create an API Connection, it will automatically be available for GenerativeAgent. You can test resources that use APIs like Functions into the same environments before going live.

### Trial Mode

ASAPP safely deploys new API use cases to production via Trial Mode.

You configure Trial Mode in a way that if there are multiple APIs configured for a task or a function, GenerativeAgent is only allowed to call the first API.

After GenerativeAgent calls an API, it will immediately escalate to an agent. This way to observe GenerativeAgent's behavior after the API call.

Once you and your ASAPP Team are confident that GenerativeAgent is correctly using API Connections, you give GenerativeAgent full access to use the Connection. After that, you start Functional Testing on the next API Connection.

## Rollbacks

Rollback involves reverting a deployed resource to a previous version or state. Rollbacks restore the previous version of the resource, undoing any changes introduced by the most recent update. Version pointers for each resource indicate the new\_version\_number from the chosen deployment for rollback.

### Undeployment

Undeployment is restricted to individual resources (a task, a function, or an article). It is possible to remove resources from specific environments without deploying any version of them. Undeploying a resource does not change the state of the draft, and the system still considers the latest modification of the draft as the latest version.

Undeploying also generates a new line item within the deployment history. If a resource is critical for the functioning of other resources or services, undeployment is blocked to prevent system failures or disruptions.

### Edit History

Each resource has a history of all modifications. You can use Edit History to restore a resource to a past version.

### Resource Deletion

Deleting a resource results in the resource becoming inaccessible and invisible on the list. The system prohibits deletion if there are any dependencies, such as a task utilizing a function. The system does not permit deletion of deployed resources until the resource is undeployed from all the dependent environments to ensure uninterrupted service.

If a resource is critical for the functioning of other resources or services, the system blocks deletion to prevent system failures or disruptions.

## Next Steps

With a functioning Knowledge Base Deployment, you are ready to use GenerativeAgent. You may find one of the following sections helpful in advancing your integration:

<CardGroup>
  <Card title="Configuring GenerativeAgent" href="/generativeagent/configuring" />

  <Card title="Safety and Troubleshooting" href="/generativeagent/configuring/safety-and-troubleshooting" />

  <Card title="Go Live" href="/generativeagent/go-live" />
</CardGroup>
