# Source: https://render.com/docs/hipaa-compliance.md

# HIPAA on Render — Run HIPAA-compliant apps and store protected health information.


> *HIPAA-enabled workspaces require an Organization or Enterprise plan.*

*HIPAA* is a United States federal law that sets standards for protecting individuals' healthcare data. It defines administrative, physical, and technical safeguards for organizations that process or store protected health information (PHI).

Render provides *HIPAA-enabled workspaces* for organizations subject to HIPAA requirements. These workspaces run services and datastores on access-restricted hosts, helping to secure any PHI processed or stored by your applications. Access to these hosts by Render staff is subject to strict controls.

## Setup

> *Before proceeding, review all [important considerations](#important-considerations) below.*

The following steps must be completed by a workspace admin:

1. In the [Render Dashboard](https://dashboard.render.com), open your *Workspace Settings* page and scroll down to the *Compliance* section:

   [image: Enabling HIPAA compliance in the Render Dashboard]

2. Click *Get Started*. This opens a confirmation flow to receive Render's Business Associate Agreement (BAA).

3. Review all enablement steps, best practices, and workspace details outlined in the confirmation flow.

4. After you complete the confirmation flow, Render emails you a link to sign the BAA.

5. After you sign the BAA, return to the *Compliance* section of your workspace settings. After about a minute, your HIPAA Compliance status updates to *Pending*:

   [image: HIPAA compliance pending in the Render Dashboard]

6. When you're ready, click *Enable HIPAA* to initiate the enablement process.

   - Before proceeding, review all details in the confirmation dialog that appears.
   - If you don't initiate the enablement process manually, Render initiates it automatically 72 hours after you sign the BAA.

   As part of enablement, Render redeploys all of your workspace's existing services and datastores to access-restricted hosts. Your services might become unavailable for a few minutes.

   Render emails you when the enablement process begins, then a second time after it completes.

7. After the process completes, your HIPAA Compliance status updates to *Enabled*:

   [image: HIPAA compliance enabled in the Render Dashboard]

   Your workspace is now ready to host HIPAA-compliant applications.

## Important considerations

*Before upgrading to a HIPAA-enabled workspace, note all of the following:*

- Upgrading to a HIPAA-enabled workspace is an irreversible action.
- An additional 20% fee applies to all usage (compute, storage, etc.) in a HIPAA-enabled workspace. The minimum monthly fee is $250.
- HIPAA-enabled workspaces cannot deploy or run services in Render's Singapore [region](regions) at this time. All other regions are supported.
- HIPAA-enabled workspaces cannot deploy or run [free instances](free).
  - This is because free instances run on hosts that do not support restricted access for HIPAA compliance.
  - If your workspace has existing free instances, Render migrates them to the smallest paid instance type as part of the upgrade process.
  - Render also _suspends_ free web services migrated this way (Postgres and Key Value instances are not suspended). These services are not billed while suspended. You can resume them any time after upgrading.
- For [*Enterprise* plans](enterprise-orgs), Render upgrades _one_ of your workspaces to a HIPAA-enabled workspace.
  - You specify which workspace to upgrade in your BAA.
  - Your other workspaces are _not_ HIPAA-enabled. All HIPAA-compliant workflows must run in the HIPAA-enabled workspace.
- Even in a HIPAA-enabled workspace, you _must not_ include PHI in certain resources.
  - For details, see [Where can I process and store PHI?](#where-can-i-process-and-store-phi)
- *A HIPAA-enabled workspace does not automatically make your applications HIPAA-compliant.*
  - You are responsible for adhering to HIPAA regulations for all applications in your workspace.
  - For more information, see Render's [shared responsibility model](shared-responsibility-model).

## Where can I process and store PHI?

> *Never process or store PHI on Render outside of a HIPAA-enabled workspace.*

Not all resources in a HIPAA-enabled workspace support HIPAA-compliant processing and storing of PHI. See the following table for details:

------

###### *Live services*

---

###### Resource

[Web services](web-services)

###### PHI OK?

🟢

###### Details

---

###### Resource

[Static sites](static-sites)

###### PHI OK?

❌

###### Details

Static sites consist of static assets hosted at a publicly accessible URL. Those assets _must not_ include any PHI.

---

###### Resource

[Private services](private-services)

###### PHI OK?

🟢

###### Details

---

###### Resource

[Background workers](background-workers)

###### PHI OK?

🟢

###### Details

---

###### Resource

[Cron jobs](cronjobs)

###### PHI OK?

🟢

###### Details

---

###### Resource

Service-generated [logs](logging)

###### PHI OK?

❌

###### Details

Never include PHI in any message logged by any Render service, whether at build time or runtime.

---

###### Resource

[Service previews](service-previews) and [preview environments](preview-environments)

###### PHI OK?

🟢

###### Details

Preview instances run on access-restricted hosts, just like their production counterparts.

---

###### *Datastores*

---

###### Resource

[Persistent disks](disks)

###### PHI OK?

🟢

###### Details

All disks and their daily snapshots are encrypted at rest.

---

###### Resource

[Render Postgres](postgresql) databases

###### PHI OK?

🟢

###### Details

Your primary databases, [read replicas](postgresql-read-replicas), and [high availability](postgresql-high-availability) standby databases all support HIPAA-compliant workflows.

---

###### Resource

[Render Key Value](key-value) instances

###### PHI OK?

🟢

###### Details

---

###### *Builds*

---

###### Resource

Build artifacts

###### PHI OK?

❌

###### Details

This is the bundle generated by your service's [build command.](/deploys#build-command) It includes application code, dependencies, static assets, and any other files needed to run your service. These generated files must not include PHI.

---

###### Resource

Infrastructure-as-code config

###### PHI OK?

❌

###### Details

This includes `render.yaml` files for [Blueprints](infrastructure-as-code), along with [Terraform](terraform-provider) configuration files.

---

###### Resource

Resource names

###### PHI OK?

❌

###### Details

Do not include PHI in the name you assign to _any_ resource, including:

- Service names
- Environment variable names
- Secret file filenames
- Table or column names in your database

------
