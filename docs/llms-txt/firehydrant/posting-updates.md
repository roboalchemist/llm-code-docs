# Source: https://docs.firehydrant.com/docs/posting-updates.md

# Posting Updates

Responders typically post updates on the remediation status throughout an incident. Incident updates are more formal updates about the remediation status and are often posted to status pages. FireHydrant supports this via **Incident Updates/Notes**.

Status update notes and messages continue to be posted to Slack, Microsoft Teams, and Status Pages throughout the entire incident lifecycle, including after an incident has been resolved. This allows teams to provide ongoing updates and post-mortem communications to stakeholders.

Note that you can only post to status pages if they have been added or attached to the incident. This can be done manually or automatically via Runbooks. For more information, see [External Status Pages](https://docs.firehydrant.com/docs/external-status-pages).

All updates will always be posted to the incident's [Internal Status Page](https://docs.firehydrant.com/docs/internal-status-pages).

## Via Slack

<Image alt="Slack Update modal" align="center" width="400px" src="https://files.readme.io/3363e54-Screenshot_2023-12-06_at_12.23.52_PM.png">
  Slack Update modal
</Image>

With linked external status pages, you can post any incident notes directly from Slack. Multiple commands are available for posting updates in Slack (all open the same modal).

```
/fh update
/fh add note # alias
/fh post     # alias
```

<Image alt="Options for posting to external status pages when running `/fh update` via Slack" align="center" width="400px" src="https://files.readme.io/585abfb-image.png">
  Options for posting to external status pages when running `/fh update` via Slack
</Image>

## Via Command Center

<Image alt="Additional primary action (update)" align="center" width="400px" src="https://files.readme.io/3e6658e-image.png">
  Additional primary action (update)
</Image>

In the Command Center for the incident, you can click the additional primary action dropdown on the right side to reveal the "Update incident" action. This opens a modal that functions the same way as the Slack modal above.

<Image alt="Update incident modal in Command Center" align="center" width="650px" src="https://files.readme.io/b017a7a-CleanShot_2024-03-28_at_11.45.092x.png">
  Update incident modal in Command Center
</Image>

Alternatively, you can navigate to the **Status Pages** tab to post to individual status pages. The **[internal status page](/docs/internal-status-pages/)** will always be available to post updates. **[External status pages](/docs/publishing-to-external-status-pages/)** can optionally be posted to, but if you post to an external page, FireHydrant will also automatically post to the Internal status page.

<Image alt="Status Pages tab in Command Center" align="center" width="650px" src="https://files.readme.io/ea5b9c0-image.png">
  Status Pages tab in Command Center
</Image>

## Status Templates

If you have [Status Templates](https://docs.firehydrant.com/docs/status-templates) configured, your responders can select from a list of pre-defined update templates to further reduce cognitive load and toil during incidents. This dropdown will not be visible if no status templates exist. You can visit the docs linked above for more information.

<Image alt="Example of status template selection (if at least one has been configured)" align="center" width="400px" src="https://files.readme.io/5439397-image.png">
  Example of status template selection (if at least one has been configured)
</Image>

## Additional Notes

* **Runbook Conditions** - Posting incident updates will trigger the condition `Time since last incident note` if it is used in any of your Runbooks or steps. This allows you to do things like reminding the channel to post an update if it's been 30 minutes since the previous update, etc.

## Next Steps

* Look into configuring [Status Templates](https://docs.firehydrant.com/docs/status-templates)
* Read about [Triggering Runbooks](https://docs.firehydrant.com/docs/triggering-runbooks), the automation engine on FireHydrant
* Learn how to mark [Impacted Components](https://docs.firehydrant.com/docs/marking-impacted-components) on incidents