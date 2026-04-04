# Source: https://render.com/docs/infrastructure-as-code.md

# Render Blueprints (IaC) — Manage your Render infrastructure with a single YAML file.

*Blueprints* are Render's infrastructure-as-code (IaC) model for defining, deploying, and managing multiple resources with a single YAML file:

[diagram]

*Show example Blueprint*

```yaml
# This is a basic example Blueprint for a Django web service and
# the Render Postgres database it connects to.
services:
  - type: web # A Python web service named django-app running on a free instance
    plan: free
    name: django-app
    runtime: python
    repo: https://github.com/render-examples/django.git
    buildCommand: './build.sh'
    startCommand: 'python -m gunicorn mysite.asgi:application -k uvicorn.workers.UvicornWorker'
    envVars:
      - key: DATABASE_URL # Sets DATABASE_URL to the connection string of the django-app-db database
        fromDatabase:
          name: django-app-db
          property: connectionString

databases:
  - name: django-app-db # A Render Postgres database named django-app-db running on a free instance
    plan: free
```

A Blueprint acts as the single source of truth for configuring an interconnected set of services, databases, and [environment groups](configure-environment-variables#environment-groups). Whenever you update a Blueprint, Render automatically redeploys any affected services to apply the new configuration (you can [disable this](#disabling-automatic-sync)).

As your infrastructure grows over time, Blueprints become more and more helpful for managing changes and additions to it.

> *Do not manage a particular service, database, or environment group with more than one Blueprint.*
>
> If you do this, Render always attempts to apply the configuration from whichever Blueprint was synced most recently. If the Blueprints differ in their configuration, this can result in unpredictable behavior for your services.
>
> To avoid this scenario, make sure that each of your resources is managed by at most one Blueprint.

## Setup

1. Create an empty YAML file in your repository where you'll define your Blueprint's resources.
   - By default, Render looks for the `render.yaml` file at the root of your repo, but you can define your Blueprint file anywhere.

2. Populate your Blueprint file with the details of the resources you want to create and manage.

   - If you're testing out Blueprints, try pasting the example Blueprint at the [top of this page](infrastructure-as-code).
   - See also the complete [Blueprint specification reference](blueprint-spec).

3. Commit and push your changes to your Git provider (GitHub, GitLab, or Bitbucket).

4. Open the [Render Dashboard](https://dashboard.render.com) and click *New > Blueprint*:

   [image: Creating a new Blueprint in the Render Dashboard]

5. In the list that appears, click the *Connect* button for whichever repo contains your Blueprint.

   - You'll first need to connect your GitHub/GitLab/Bitbucket account if you haven't yet.

6. In the form that appears, specify a name for your Blueprint and which branch of your repo to link.

   - Each push to the linked branch that modifies your Blueprint file triggers a deploy of any added or modified resources.

7. If needed, specify a custom file path to your Blueprint's YAML file in the *Blueprint Path* field.

   - By default, Render creates a Blueprint using the `render.yaml` file at your repository's root.

8. Review the list of the changes that Render will apply based on the linked Blueprint:

   [image: List of new resources from a Blueprint]

   If your Blueprint file contains errors, the page instead displays details about those errors.

9. If everything looks correct, click *Deploy Blueprint*.

You're all set! Render begins provisioning your Blueprint's  specified resources:

[image: Blueprint provisioning progress in the Render Dashboard]

## Generating a Blueprint from existing services

You can generate a `render.yaml` file using any combination of your existing Render services. This is useful if you want to start managing those exact resources with a Blueprint, or if you want to [replicate those resources](#replicating-a-blueprint).

In the [Render Dashboard](https://dashboard.render.com), select any number of your services, then click *Generate Blueprint* at the bottom of the page:

[image: UI for generating a Blueprint in the Render Dashboard]

This opens a page where you can download or copy the generated `render.yaml` file. The page provides additional instructions for creating a Blueprint from that file.

> *Important:* For security, the generated `render.yaml` file includes the _names_ of all defined environment variables for the selected services, _but not their values_. Instead, the file sets `sync: false` for each environment variable.
>
> If you use your `render.yaml` file to create a Blueprint with _new_ services instead of your existing ones, you'll need to provide values for these environment variables. For details, see [Setting environment variables](blueprint-spec#setting-environment-variables).

## Replicating a Blueprint

You can create multiple Blueprints from a single YAML file. Each Blueprint creates and manages a completely independent set of resources.

The Blueprint creation flow displays a notice if your new Blueprint matches existing Render resources:

[image: Notification that Blueprint matches existing resources]

As shown in the screenshot above, Render appends a suffix to the name of each new resource to prevent collisions with your existing resources.

Click *Deploy Blueprint* to create the new resources as usual.

## Managing Blueprint resources

### Adding an existing resource

> *Do not add an existing resource to a Blueprint if it's already managed by _another_ Blueprint.*
>
> Doing so can lead to unpredictable behavior for your services.

You can add an existing Render resource to your Blueprint. To do so, add the resource's details to your Blueprint file as you would for a new resource. See all supported fields and values for each service type in the [Blueprint specification reference](blueprint-spec).

*Make sure to include all configuration options that are currently set for the resource in the Render Dashboard.* For most services, this includes the service's `name`, `type`, `plan` (instance type), `buildCommand`, `startCommand`, and so on. If you omit some of these options, your Blueprint will use a default value that almost definitely differs from your service's existing configuration.

When you next sync your Blueprint, Render applies the new configuration to the existing resource. The resource retains any existing environment variable values that aren't overwritten by the Blueprint.

### Modifying a resource outside of its Blueprint

You _can_ still make changes to a Blueprint-managed resource in the [Render Dashboard](https://dashboard.render.com). However, if any of those changes conflict with configuration defined in the Blueprint, they're overwritten the next time you sync your Blueprint.

Even if you _delete_ a Blueprint-managed resource in the Render Dashboard, Render recreates it the next time you sync your Blueprint! See [Deleting a resource](#deleting-a-resource).

### Deleting a resource

*Syncing a Blueprint never deletes an existing resource.* This is true even if you remove a resource definition from your Blueprint file, or if you disconnect your Blueprint from Render entirely. This is a safeguard against accidental deletions (for example, if you revert your Blueprint to a commit that predates the addition of a critical resource).

To delete a Blueprint-managed resource, _first_ remove it from your Blueprint, _then_ delete it in the [Render Dashboard](https://dashboard.render.com) as usual.

> If you delete a resource in the Render Dashboard but _keep_ it in your Blueprint, Render _recreates_ that resource the next time you sync your Blueprint.

## Disabling automatic sync

By default, Render automatically updates affected resources every time you push Blueprint changes to your linked branch.

To instead control exactly when you sync a particular Blueprint, set *Auto Sync* to *No* on your Blueprint's Settings page:

[image: render.yaml settings screen]

You can then manually trigger a sync by clicking *Manual Sync* on your Blueprint's page.

## Supported fields and values

See the complete [Blueprint specification reference](blueprint-spec).