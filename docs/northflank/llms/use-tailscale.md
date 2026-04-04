# Source: https://northflank.com/docs/v1/application/network/use-tailscale.md

# Use Tailscale

You can enable Tailscale in a project to give your resources secure access to your Tailscale network. Your resources will be able to access Tailscale devices, and normal Northflank networking to public and private resources will continue to work as usual.

You will be able to access Tailscale devices from your Northflank resources by their IP addresses, or the fully-qualified domain name for the device (for example `device1.<id>.ts.net`). The shortened form of the Tailscale domain for a device will not work.

## Enable Tailscale

You will integrate Tailscale with Northflank using an OAuth client so that Northflank can automatically regenerate auth keys for your project.

### Create a Tailscale tag

You'll need one or more [Tailscale tags](https://tailscale.com/kb/1068/tags) to create an OAuth Client for use with Northflank. You can use one tag for all your Northflank projects, or create and assign as many tags as you require.

To create a Tailscale tag, open your [access control](https://login.tailscale.com/admin/acls/file) page in Tailscale and add a new entry in the `tagOwners` object. You may need to add this object if you don't already have any tags.

Example Tailscale tag definition

```json
{
  "tagOwners": {
    "tag:northflank": [],
  }
}
```

You must leave tag owners empty, so it can be applied by your generated auth key.

### Create an OAuth Client

To create your OAuth client open [OAuth clients](https://login.tailscale.com/admin/settings/oauth) on your Tailscale settings page, under Tailnet Settings. Select generate OAuth client, give it a recognisable description, and grant it write scope for `auth_keys`.

Add at least one tag for the `auth keys` scope, and click generate client. Copy the ID and secret somewhere secure or keep the page open while you configure Northflank, as you will not be able to access the values in full again.

### Add your OAuth client to Northflank

Open your [project settings](https://app.northflank.com/s/project/settings) and enable Tailscale.

Copy the client ID and secret to the corresponding fields. Next, enter the Tailscale tags that are assigned to the `auth keys` scope of your OAuth client. They should be added in full, in the format `tag:name`.

You can now configure Tailscale for your project, detailed below, or click update to add Tailscale to your project.

> [!note] Identify your Northflank resources on Tailscale
> When you deploy new resources, or redeploy existing resources in your project after enabling Tailscale, they will appear in your Tailscale machines list. To identify a Northflank resource in Tailscale, open the resource in Northflank and navigate to the containers page for a service, or the job runs page for a job. The first two parts of the container name or the job run name, separated by a dash, will be the name of the machine listed in Tailscale. For example `proxy-54fcd583a7-adf5c` would appear as `proxy-54fcd583a7`.

## Restrict Tailscale access

Select restrict Tailscale to only allow specific resources access to your Tailscale network.

Resources are [restricted by Northflank tag](https://northflank.com/docs/v1/application/release/tag-workloads-and-resources). Select the tags that will allow Tailscale, and ensure the resources you want to have access are tagged appropriately.

## Accept advertised routes from your tailnet

You can choose to accept advertised routes from the Tailscale network. If you have [configured subnet routers](https://tailscale.com/kb/1019/subnets) in your Tailscale network this will allow you to access the other devices connected via the subnet.

Without enabling this feature your resources will only be able to access devices that have the Tailscale client installed on them directly.

## Auto-redeploy on key regeneration

All auth keys expire within 90 days. Running containers will not be disconnected from Tailscale, but if a container restarts (for example due to a crash), it will not be able to authenticate with the expired key.

You can enable auto-redeploy on key regeneration to automatically redeploy resources with then updated auth key to ensure they have access to your tailnet.

If Tailscale is restricted to specific [tagged resources](https://northflank.com/docs/v1/application/release/tag-workloads-and-resources), only resources using Tailscale will be redeployed when a new auth key is generated.

## Disable Tailscale

If you have restricted Tailscale you can disable specific resources from accessing Tailscale by either removing the tag from the resource, or by removing the tag from the Tailscale tag restrictions list, and redeploying the relevant resources.

If you want to disable Tailscale for all resources, uncheck enable tailscale sidecar, update, and redeploy the relevant resources.

## Next steps

- [Network security: Set IP policies and add basic authentication to your deployments.](/v1/application/network/networking-on-northflank)
- [Add private ports: Configure ports to allow your services to communicate securely within your project.](/v1/application/network/configure-ports#private-ports)
- [Forward deployments and databases: Forward deployments and databases to your local machine for development.](/v1/api/forwarding)
- [Configure basic authentication: Require users to enter a username and password to access your site.](/v1/application/network/add-security-policies-for-ports#require-credentials)
