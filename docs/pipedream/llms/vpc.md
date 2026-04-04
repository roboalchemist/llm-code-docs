# Source: https://pipedream.com/docs/workflows/vpc.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Virtual Private Clouds

<Frame>
  <iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/E_dfTCCccPE" title="Virtual Private Clouds" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</Frame>

Pipedream VPCs enable you to run workflows in dedicated and isolated networks with static outbound egress IP addresses that are unique to your workspace (unlike other platforms that provide static IPs common to all customers on the platform).

Outbound network requests from workflows that run in a VPC will originate from these static IP addresses, so you can whitelist access to sensitive resources (like databases and APIs) with confidence that the requests will only originate from the Pipedream workflows in your workspace.

## Getting started

### Create a new VPC

1. Open the [Virtual Private Clouds tab](https://pipedream.com/settings/networks):

<Frame>
  <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/95e7c149-CleanShot_2023-08-01_at_14.29.24_slx1a7.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=6fb62c49564665d393e229663ac4bd67" width="704" height="128" data-path="images/95e7c149-CleanShot_2023-08-01_at_14.29.24_slx1a7.png" />
</Frame>

1. Click on **New VPC** in the upper right of the page:

<Frame>
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/2ebfb428-CleanShot_2023-08-01_at_14.30.47_okdiyx.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=45bc8f7932f6ef733268fa2b6b09fa37" width="173" height="77" data-path="images/2ebfb428-CleanShot_2023-08-01_at_14.30.47_okdiyx.png" />
</Frame>

1. Enter a network name and click **Create**:

<Frame>
  <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/725402b6-CleanShot_2023-08-01_at_14.03.24_smxujq.png?fit=max&auto=format&n=anb6FA0wpd8jtdUB&q=85&s=89e84af091674a7aa3447288e797e27f" width="684" height="303" data-path="images/725402b6-CleanShot_2023-08-01_at_14.03.24_smxujq.png" />
</Frame>

1. It may take 5-10 minutes to complete setting up your network. The status will change to **Available** when complete:

<Frame>
  <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/a940c197-CleanShot_2023-08-01_at_14.04.22_ro2bgx.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=57da6e37e1218aae5e2072664f4806af" width="102" height="109" data-path="images/a940c197-CleanShot_2023-08-01_at_14.04.22_ro2bgx.png" />
</Frame>

### Run workflows within a VPC

To run workflows in a VPC, check the **Run in Private Network** option in workflow settings and select the network you created. All outbound network requests for the workflow will originate from the static egress IP for the VPC (both when testing a workflow or when running the workflow in production).

<Frame>
  <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/6b756091-CleanShot_2023-08-01_at_14.18.42_rihwff.png?fit=max&auto=format&n=anb6FA0wpd8jtdUB&q=85&s=f0ccd5974344cd3203f35713d1f89828" width="682" height="108" data-path="images/6b756091-CleanShot_2023-08-01_at_14.18.42_rihwff.png" />
</Frame>

If you don’t see the network listed, the network setup may still be in progress. If the issue persists longer than 10 minutes, please [contact support](https://pipedream.com/support).

### Find the static outbound IP address for a VPC

You can view and copy the static outbound IP address for each VPC in your workspace from the [Virtual Private Cloud settings](https://pipedream.com/settings/networks). If you need to restrict access to sensitive resources (e.g., a database) by IP address, copy this address and configure it in your application with the `/32` CIDR block. Network requests from workflows running in the VPC will originate from this address.

<Frame>
  <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/c142448c-CleanShot_2023-08-01_at_14.34.56_lp5jt3.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=d7cf3c94bbc3ec1851bdbe5736f4117b" width="1094" height="88" data-path="images/c142448c-CleanShot_2023-08-01_at_14.34.56_lp5jt3.png" />
</Frame>

## Managing a VPC

To rename or delete a VPC, navigate to the [Virtual Private Cloud settings](https://pipedream.com/settings/networks) for your workspace and select the option from the menu to the right of the VPC you want to manage.

## Self-hosting and VPC peering

If you’re interested in running Pipedream workflows in your own infrastructure, or configure VPC peering to allow Pipedream to communicate to resources in a private network, please reach out to our [Sales team](mailto:sales@pipedream.com).

## Limitations

* Only workflows can run in VPCs (other resources like sources or data stores are not currently supported). For example, [sources](/workflows/building-workflows/triggers/) cannot yet run in VPCs.

* Creating a new network can take up to 5 minutes. Deploying your first workflow into a new network and testing that workflow for the first time can take up to 1 min. Subsequent operations should be as fast as normal.

* VPCs only provide static IPs for outbound network requests. This feature does not provide a static IP for or otherwise restrict inbound requests.

* You can’t set a default network for all new workflows in a workspace or project (you must select the network every time you create a new workflow). Please [reach out](https://pipedream.com/support) if you’re interesting in imposing controls like this in your workspace.

* Workflows running in a VPC will still route specific requests routed through [the shared Pipedream network](/workflows/data-management/destinations/http/#ip-addresses-for-pipedream-http-requests):

  * [`$.send.http()`](/workflows/data-management/destinations/http/) requests
  * Async options requests (these are requests that are made to populate options in drop down menus for actions while a building a workflow — e.g., the option to “select a Google Sheet” when using the “add row to Google Sheets” action)

## FAQ

### Will HTTP requests sent from Node.js, Python and the HTTP request steps use the assigned static IP address?

Yes, all steps that send HTTP requests from a workflow assigned to a VPC will use that VPC’s IP address to send HTTP requests.

This will also include `axios`, `requests`, `fetch` or any HTTP client you prefer in your language of choice.

The only exception are requests sent by `$.send.http()` or the HTTP requests used to populate async options that power props like “Select a Google Sheet” or “Select a Slack channel”. These requests will route through the [standard set of Pipedream IP addresses.](/privacy-and-security/#hosting-details)

### Can a single workflow live within multiple VPCs?

No, a VPC can contain many workflows, but a single workflow can only belong to one VPC.

### Can I modify my VPC’s IP address to another address?

No, IP addresses are assigned to VPCs for you, and they are not changeable.

### How much will VPCs cost?

VPCs are available on the **Business** plan. [Upgrade your plan here](https://pipedream.com/pricing).

Built with [Mintlify](https://mintlify.com).
