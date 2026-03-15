# Source: https://docs.firehydrant.com/docs/runbook-testing.md

# Runbook Testing

Every Runbook in FireHydrant can be tested independently without going through the pain of declaring an incident. More specifically, when you execute a Runbook test, FireHydrant creates an incident with a `GAMEDAY` severity (therefore excluding it from metrics and analytics) and can isolate the Runbook so no other Runbooks execute.

## Executing the Test

<Image alt="Testing a Runbook" align="center" width="650px" src="https://files.readme.io/00bce4a-image.png">
  Testing a Runbook
</Image>

In this example, we have a simple Runbook containing an [Asana](https://docs.firehydrant.com/docs/asana-integration) step. Each time this Runbook executes, an incident task will be created in Asana in the project we've configured and selected.

<Image alt="Confirming whether this runbook should be tested in isolation" align="center" width="400px" src="https://files.readme.io/af0b35c-image.png">
  Confirming whether this runbook should be tested in isolation
</Image>

1. To test any Runbook, click the "Test" button on the Runbook page. This will open a modal where you can confirm testing method.
   1. Testing Runbooks in isolation can be useful if you're trying to debug very specific things.
   2. On the other hand, it can be useful to uncheck this setting if you need to test a Runbook in conjunction with other Runbooks to see how your overall automation is configured.
2. Once you click "Confirm," you'll then be redirected to a test incident with only the selected Runbook attached (or others, depending on what you selected in the last step).
3. And voilà! In this example, you can see an Asana ticket has been created for this incident.

<Image alt="Asana ticket created" align="center" width="650px" src="https://files.readme.io/cff3986-image.png">
  Asana ticket created
</Image>

And we can see the ticket in Asana as well.

<Image alt="The same ticket in Asana" align="center" width="650px" src="https://files.readme.io/91368c1-image.png">
  The same ticket in Asana
</Image>

## Troubleshooting Runbooks

<Image alt="Viewing a Runbook's steps in an incident" align="center" width="650px" src="https://files.readme.io/2982f14f3d233ed00877050fb4b27f96ff13c49a83a1539e6394d15907cc84c2-CleanShot_2025-01-03_at_13.40.192x.png">
  Viewing a Runbook's steps in an incident
</Image>

In [The Command Center](https://docs.firehydrant.com/docs/the-command-center), there is a dedicated tab for Runbooks and execution. On top of listing the Runbooks and all of the steps, you will also see the execution status of all steps.

Clicking on a dropdown will also show additional details like conditions and/or error messages if a step fails to execute. Use this to understand the state of your workflows and automation at any given time.

<Image alt="Expanding a step's details" align="center" width="650px" src="https://files.readme.io/0f10e48e7051c63426590aa5317a4e92f43b0f25bf2db8e2789af9228ee10c97-CleanShot_2025-01-03_at_13.43.032x.png">
  Expanding a step's details
</Image>

Step execution status can also be browsed from Slack within the incident channel with `/fh runbooks`.

## Next Steps

* Read more about [Runbook Best Practices](https://docs.firehydrant.com/docs/runbook-best-practices)
* Browse the [available Runbook steps](https://docs.firehydrant.com/docs/runbook-steps) FireHydrant offers