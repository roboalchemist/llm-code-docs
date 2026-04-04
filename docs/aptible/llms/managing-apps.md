# Source: https://www.aptible.com/docs/core-concepts/apps/managing-apps.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Apps

> Learn how to manage Aptible Apps

# Overview

Aptible makes managing your application simple. Whether you're using the Aptible Dashboard, CLI, or Terraform, you have full control over your App’s lifecycle without needing to worry about the underlying infrastructure.

# Learn More

<AccordionGroup>
  <Accordion title="Manually Scaling Apps">
    <Frame>
            <img src="https://mintcdn.com/aptible/gJr2xlqbHzeeHUse/images/app-scaling2.gif?s=a61137120d0be85d65c2cde65b50549b" alt="scaling" data-og-width="1186" width="1186" data-og-height="720" height="720" data-path="images/app-scaling2.gif" data-optimize="true" data-opv="3" />
    </Frame>

    Apps can be manually scaled both horizontially (number of containers) and vertically (RAM/CPU) can be scaled on-demand with zero downtime deployments. Refer to [App Scaling](/core-concepts/scaling/app-scaling) for more information.
  </Accordion>

  <Accordion title="Autoscaling Apps">
    Read more in the [App Scaling page](/core-concepts/scaling/app-scaling)
  </Accordion>

  <Accordion title="Restarting Apps">
    Apps can be restarted the following ways:

    * Using the [aptible restart](/reference/aptible-cli/cli-commands/cli-restart) command
    * Within the Aptible Dashboard, by:

      * Navigating to the app
      * Selecting the Settings tab
      * Selecting Restart

      Like all [Releases](/core-concepts/apps/deploying-apps/releases/overview), when Apps are restarted, a new set of [Containers](/core-concepts/architecture/containers/overview) will be launched to replace the existing ones for each of your App's [Services](/core-concepts/apps/deploying-apps/services).
  </Accordion>

  <Accordion title="Achieving High Availability">
    <Note> High Availability Apps are only available on [Production and Enterprise](https://www.aptible.com/pricing)[ plans.](https://www.aptible.com/pricing)</Note>

    Apps scaled to 2 or more Containers are automatically deployed in a high-availability configuration, with Containers deployed in separate [AWS Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html).
  </Accordion>

  <Accordion title="Renaming Apps">
    An App can be renamed in the following ways:

    * Using the [`aptible apps:rename`](/reference/aptible-cli/cli-commands/cli-apps-rename) command
    * Using the Aptible [Terraform Provider](https://registry.terraform.io/providers/aptible/aptible/latest/docs)

    For the change to take effect, the App must be restarted.

    <Warning>App handles cannot start with "internal-" or "sg-" because applications with these prefixes cannot have [Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/overview) allocated due to AWS limitations.</Warning>
  </Accordion>

  <Accordion title="Deprovisioning an App">
    Apps can be deleted/deprovisioned using one of these three methods:

    * Within the Aptible Dashboard:
      * Selecting the Environment in which the App lives
      * Selecting the **Apps** tab
      * Selecting the given App
      * Selecting the **Deprovision** tab
    * Using the [`aptible apps:deprovision`](/reference/aptible-cli/cli-commands/cli-apps-deprovision) command
    * Using the Aptible [Terraform Provider](https://registry.terraform.io/providers/aptible/aptible/latest/docs)
  </Accordion>
</AccordionGroup>
