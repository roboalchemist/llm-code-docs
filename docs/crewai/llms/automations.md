# Source: https://docs.crewai.com/en/enterprise/features/automations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.crewai.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Automations

> Manage, deploy, and monitor your live crews (automations) in one place.

## Overview

Automations is the live operations hub for your deployed crews. Use it to deploy from GitHub or a ZIP file, manage environment variables, re‑deploy when needed, and monitor the status of each automation.

<Frame>
    <img src="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-overview.png?fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=a7d0655da82c70b0ca152715cb8253f4" alt="Automations Overview" data-og-width="3648" width="3648" data-og-height="2266" height="2266" data-path="images/enterprise/automations-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-overview.png?w=280&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=18456289664a18d4b83b2acdae616a44 280w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-overview.png?w=560&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=4737cb32db15d7f121a1366ae5c80c0e 560w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-overview.png?w=840&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=69473aff76b3ea16974be8226590d114 840w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-overview.png?w=1100&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=a742c3a1f81537f0a2d9668e5671c1aa 1100w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-overview.png?w=1650&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=6a9aed77a2491e2dc3da8f511f391487 1650w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-overview.png?w=2500&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=c64e992c5464916085b9114abab0d7c0 2500w" />
</Frame>

## Deployment Methods

### Deploy from GitHub

Use this for version‑controlled projects and continuous deployment.

<Steps>
  <Step title="Connect GitHub">
    Click <b>Configure GitHub</b> and authorize access.
  </Step>

  <Step title="Select Repository & Branch">
    Choose the <b>Repository</b> and <b>Branch</b> you want to deploy from.
  </Step>

  <Step title="Enable Auto‑deploy (optional)">
    Turn on <b>Automatically deploy new commits</b> to ship updates on every push.
  </Step>

  <Step title="Add Environment Variables">
    Add secrets individually or use <b>Bulk View</b> for multiple variables.
  </Step>

  <Step title="Deploy">
    Click <b>Deploy</b> to create your live automation.
  </Step>
</Steps>

<Frame>
    <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-github.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=4fb72dc68799d5a0c35e2e74f1a7cc6c" alt="GitHub Deployment" data-og-width="3648" width="3648" data-og-height="2266" height="2266" data-path="images/enterprise/deploy-from-github.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-github.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=b15575b0b30c64e8b7a20de9e97468e5 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-github.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=c041da5b5b79d38cb2a3f8d6f00e14a7 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-github.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=0783c12a6f83d09ce83e66aa34edcacd 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-github.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=d703da835283f7e73079ef66f664587c 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-github.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=f73b6afc4c3c3075ded4da6559676fa3 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-github.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=c3d82425923c1f57264b7cb5af9004b3 2500w" />
</Frame>

### Deploy from ZIP

Ship quickly without Git—upload a compressed package of your project.

<Steps>
  <Step title="Choose File">
    Select the ZIP archive from your computer.
  </Step>

  <Step title="Add Environment Variables">
    Provide any required variables or keys.
  </Step>

  <Step title="Deploy">
    Click <b>Deploy</b> to create your live automation.
  </Step>
</Steps>

<Frame>
    <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-zip.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=8cea74868a553d34b0aa182ad5489099" alt="ZIP Deployment" data-og-width="3648" width="3648" data-og-height="2266" height="2266" data-path="images/enterprise/deploy-from-zip.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-zip.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=961637aa95a2795071b4a54e921f3f03 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-zip.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=62994bfdf5667fc17880ed33c32a7aa6 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-zip.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=b0c4ef28de74989c1fdbf1076d12ba3c 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-zip.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=19fe8b770051a0426f120d6b661a6f40 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-zip.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=a80e4bf6e8befdf57a5ea79840b45136 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-zip.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=61e870a88f47df3e282a134e754fc09d 2500w" />
</Frame>

## Automations Dashboard

The table lists all live automations with key details:

* **CREW**: Automation name
* **STATUS**: Online / Failed / In Progress
* **URL**: Endpoint for kickoff/status
* **TOKEN**: Automation token
* **ACTIONS**: Re‑deploy, delete, and more

Use the top‑right controls to filter and search:

* Search by name
* Filter by <b>Status</b>
* Filter by <b>Source</b> (GitHub / Studio / ZIP)

Once deployed, you can view the automation details and have the **Options** dropdown menu to `chat with this crew`, `Export React Component` and `Export as MCP`.

<Frame>
    <img src="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-table.png?fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=f7fb571e8473f5cb7940c3e3bb34f95c" alt="Automations Table" data-og-width="2874" width="2874" data-og-height="932" height="932" data-path="images/enterprise/automations-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-table.png?w=280&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=5833733acf6f2e07d0a39abffe87de40 280w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-table.png?w=560&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=858a8b93744d4f23e07e9ec58227aac0 560w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-table.png?w=840&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=e0fe6df6d821e1edc729681e8d314d22 840w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-table.png?w=1100&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=cb68b81e23a169714985d93bb0913170 1100w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-table.png?w=1650&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=401736c16a6074de6b60de8234cbe206 1650w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-table.png?w=2500&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=1b9a5f852f474d6a68a5cf4dda5a0021 2500w" />
</Frame>

## Best Practices

* Prefer GitHub deployments for version control and CI/CD
* Use re‑deploy to roll forward after code or config updates or set it to auto-deploy on every push

## Related

<CardGroup cols={3}>
  <Card title="Deploy a Crew" href="/en/enterprise/guides/deploy-crew" icon="rocket">
    Deploy a Crew from GitHub or ZIP file.
  </Card>

  <Card title="Automation Triggers" href="/en/enterprise/guides/automation-triggers" icon="trigger">
    Trigger automations via webhooks or API.
  </Card>

  <Card title="Webhook Automation" href="/en/enterprise/guides/webhook-automation" icon="webhook">
    Stream real-time events and updates to your systems.
  </Card>
</CardGroup>
