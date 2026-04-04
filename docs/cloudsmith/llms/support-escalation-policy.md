# Source: https://help.cloudsmith.io/docs/support-escalation-policy.md

# Support Escalation Policy

As part of the support offered to customers with the **Enterprise Support** package, you can escalate urgent matters of importance to the on-call team at Cloudsmith.

## Policy

As this is effectively a *bat signal* directly to the on-call team, we must establish a clear policy around the use (and misuse) of the escalation channel. Our team are only Human, and it's important to protect them from accidental and/or frequent alerting.

### Good Reasons to Escalate

Some good reasons to use the escalation channel:

* Your service has been severely impacted, and the Cloudsmith status page hasn't yet been updated.
* A security attack has hit you, and you need an immediate lockdown of your account.
* You suspect that the security of your critical Cloudsmith account(s) has been compromised.
* You are completely locked out of your account (as an owner) and urgently need access to log in.

For any of these or those like it, we'd recommend using the escalation channel if needed.

### Bad Reasons to Escalate

Some bad reasons to use the escalation channel:

* You need non-urgent support (e.g. queries, password resets, 2FA resets, etc.)
* You are locked out of your account and can't log in.
* You are having issues uploading and/or downloading, but it isn't related to a service outage.
* You are waiting for support via normal channels but haven't had a response yet.
* You're having a service outage, but the [Cloudsmith Status Site](https://status.cloudsmith.io) already acknowledges the outage.

For any of these or those like it, we'd recommend the normal support channels. You might need to be a little more patient than usual if outside of our normal support hours (mostly UK-centric).

### Terms and Conditions

This service is offered with the disclaimer that this is a benefit of the Enterprise Support package.

The escalation channel should really only be used as a last resort, and certainly no more than once per event, and not if an issue has already been acknowledged (either directly or via the [Cloudsmith Status Site](https://status.cloudsmith.io)). The on-call team will acknowledge your issue and keep you updated at a regular interval.

Please treat the escalation channel the same way that you might an emergency service, such as the police, ambulance, fire or coast guard.

Of course, if it really *is* an emergency, then that's what the team is there for. We're here to ensure that Cloudsmith is as-available as possible and that any disruptions to your service are minimised.

Thanks for being an awesome and considerate user. :-)

### Timeliness

Although the on-call team is alerted immediately, they might not be able to respond immediately. Our target is to acknowledge within 15 minutes, but this is not guaranteed. We do guarantee that you will get an acknowledgement/reply within 60 mins.

## How To Escalate

> ❗️ STOP, and listen
>
> **Remember:** The escalation is for *truly urgent issues* only. Please double-check the "Good Reasons to Escalate" and "Bad Reasons to Escalate" above before using the escalation channels. A happy, healthy and rested on-call support team serves you best. :-)

### Via Support Portal (Zendesk)

In order to escalate via our [Support Portal](https://support.cloudsmith.com), please ensure you're logged in, and submit a request - as you usually would when submitting questions or issues.

<Image align="center" width="-3px" src="https://files.readme.io/6b22974be6bedcef3c5f6354141881c76e05adc7312e9818e46c544083fa5fa1-zendesk-submit-request.png" />

Once you have provided all relevant information related to your issue, ensure you have set the Issue Severity to **SEV 1 - Critical (Business-Critical Impact)**. This will immediately alert us.

<Image align="center" className="border" width="-3px" border={true} src="https://files.readme.io/01b680a679feb072585fc44c3fa1a200ceedb23a0f04a13ea97eefdbae4a271f-zendesk-sev-1.png" />

### Via Slack (only available if we have a shared channel!)

In order to escalate via Slack, simply create a ticket \[using the :ticket: emoji] as you would normally, and ensure you have set the Issue Severity to **SEV 1 - Critical (Business-Critical Impact)**. This will immediately alert us. Please ensure that you provide us with as much information about the issue as possible to help our team triage effectively.

<Image title="escalation_1.jpg" alt={741} align="center" src="https://files.readme.io/18c1a962c5495ac5770a5034d132c7e12ff2581827e5678ad912cfcafe0f6cfa-slack-ticket-sev-1.png">
  SEV-1 Critical / Business Impact
</Image>