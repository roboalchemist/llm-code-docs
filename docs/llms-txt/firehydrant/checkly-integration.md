# Source: https://docs.firehydrant.com/docs/checkly-integration.md

# Checkly

Checkly is an API and E2E monitoring platform. You can use it to configure synthetic and API monitoring as part of your existing infrastructure codebase, cover E2E scenarios using JavaScript, and adapt checks with Node.js-based setup and teardown scripts.

Integrating FireHydrant with Checkly lets you automatically send alert data from Checkly to FireHydrant to declare an incident and kick off a Runbook. This way, you'll see an alert in your configured Slack channel when a check fails.

## Prerequisites

* You will need <Glossary>Owner</Glossary> permissions to configure integrations on FireHydrant
* Ensure you have [Slack](https://docs.firehydrant.com/docs/slack-integration) configured and a default notification channel set in the configuration settings

## Installing the Checkly integration

<Image alt="Checkly tile on the integrations page" align="center" width="650px" src="https://files.readme.io/eafa27d-image.png">
  Checkly tile on the integrations page
</Image>

1. Go to FireHydrant's [Integrations](https://app.firehydrant.io/organizations/integrations) page and search for the **Checkly**  integration card. Click '+'.
2. On the next page, click **Authorize Application**. This will generate a webhook, which you should copy to your clipboard for the next steps.
3. Log in to [Checkly](https://www.checklyhq.com/). On the left side navigation, go to **Alerts**.
4. Click on **Add more channels**, find FireHydrant on the list, and then click **Add channel**. This opens the FireHydrant configuration page in Checkly.

<Image alt="FireHydrant on the list of channels in Checkly" align="center" width="400px" src="https://files.readme.io/e5d2d94-Screenshot_2024-01-18_at_2.39.48_PM.png">
  FireHydrant on the list of channels in Checkly
</Image>

5. On this configuration page, fill in the **Name** field and then paste the webhook from Step #2 into **URL**. You can leave the other settings as-is. Click "Save FireHydrant webhook" when finished.

<Image alt="FH_checkly_config.png" align="center" width="650px" src="https://files.readme.io/cfe43ff-Screenshot_2024-01-18_at_2.42.00_PM.png">
  FireHydrant config page on Checkly
</Image>

### Validating the integration

It should work immediately once you've configured the alert and subscribed channels to it. If you want to validate, however, you can do the following as a quick test:

1. On the Checkly home page, you should see a dashboard for your alerts. You can either create a new simple one or click the contextual kebab menu for any existing alert and select **Edit check**.
2. From the next page that opens, you can edit your check configuration. Modify the HTTP request URL so that you can "fail" your check (this will help to confirm that you'll receive alerts from Checkly as configured). In the upper-right corner of the page, click **Save check**.

<Image alt="Deliberately failing the check" align="center" width="650px" src="https://files.readme.io/e3cdbc7-image.png">
  Deliberately failing the check
</Image>

3. Go back to your dashboard and click **Run now**. The dashboard should turn red to indicate the failed check. An alert should pop up in the default alerts channel you configured in Slack.

<Image alt="Click **Yes, open & edit** to open an incident from the alert" align="center" width="400px" src="https://files.readme.io/b7b864c-image.png">
  Click **Yes, open & edit** to open an incident from the alert
</Image>

4. Once the incident has been opened, you can return to Checkly and modify the script so that the check is passing again:

<Image alt="Deliberately passing the check" align="center" width="650px" src="https://files.readme.io/31deef8-image.png">
  Deliberately passing the check
</Image>

5. As soon as the check runs again and passes, the incident started in FireHydrant will automatically resolve.

<Image alt="Incident automatically resolving once the next check passes" align="center" width="400px" src="https://files.readme.io/f98cab8-image.png">
  Incident automatically resolving once the next check passes
</Image>

## Uninstalling the integration

To uninstall, navigate to the integration tile for Checkly on the [Integrations](https://app.firehydrant.io/organizations/integrations) page, and at the very bottom, locate **Uninstall Checkly** button.

Once it's removed from FireHydrant, remember to remove the Alert in Checkly.

## Next Steps

For more information on unlocking useful features via automation, check out the following articles:

* See how [Alert Routing](https://docs.firehydrant.com/docs/alert-routing) can streamline your incident management process
* Reduce the manual work required by leveraging [Runbook automation](https://docs.firehydrant.com/docs/runbook-basics)
* Turn outages into learning opportunities with [Retrospectives](https://docs.firehydrant.com/docs/incident-followup) and [Analytics](https://docs.firehydrant.com/docs/analytics-basics)
* Learn how to get started with FireHydrant either [as an admin](https://docs.firehydrant.com/docs/admin-quickstart) or as a responder [via Slack](https://docs.firehydrant.com/docs/slack-responder-guide) or [FireHydrant's web interface](https://docs.firehydrant.com/docs/web-ui-responder-guide)