# Source: https://docs.rootly.com/incidents/incident-timeline/adding-events-to-timeline-via-email.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding Events to Timeline via Email

> Learn how to add events to incident timelines by responding to incident emails through the Email integration.

### Overview

Using our [Email integration](/integrations/email), you can add timeline events simply by **replying to an incident email**.\
This makes it easy for stakeholders—especially those who don’t live in Slack or the web interface—to contribute updates directly to the incident record.

When you reply to an incident email, Rootly automatically logs that message as a timeline entry, preserving its content, sender information, and relevant metadata.

<Frame>
    <img src="https://mintcdn.com/rootly/RUi0EYcf6x_7UXYC/images/adding-events/email.webp?fit=max&auto=format&n=RUi0EYcf6x_7UXYC&q=85&s=77b2aedad616950d432f08da0150348a" alt="Adding an event using email" width="894" height="401" data-path="images/adding-events/email.webp" />
</Frame>

***

### How It Works

#### **Replying to an Existing Incident**

When you reply to an incident’s email thread:

* A new **Email** timeline event is automatically created
* The event includes:
  * The parsed message body
  * Sender information (matched to a Rootly user if possible)
  * The To/From header values
  * A permalink-style reference to the inbound message
* The event is timestamped using the time the email was received
* The event is **non-editable**, ensuring integrity

Rootly determines which incident the message belongs to by scanning the email’s **References** header, which preserves threading.

#### **Starting a New Incident by Email**

If an email is not part of an existing thread, Rootly can create a **new incident** using:

* The subject → incident title
* The body → summary
* Best-effort parsing to extract:
  * Severity
  * Services
  * Functionalities
  * Environments
  * Incident types

<Info>
  Metadata parsing works best when your teams follow consistent subject/body formatting conventions.
</Info>

***

### Setup Requirements

To ensure reliable processing of inbound email:

* Confirm the Email integration is **enabled**
* Ensure all expected sender domains are listed under **Allowed Domains**
* If provenance enforcement is enabled, only whitelisted domains may send emails
* Provide the incident thread’s email address to anyone who needs to contribute via email

<Warning>
  Emails from unapproved domains may be rejected when provenance checks are enabled.
</Warning>

***

### Behavior & Limitations

* Email-created timeline events are **not editable**
* Forwarded emails or replies that strip the **References** header cannot be attached to the existing incident
* If a sender’s email does not match any Rootly user, Rootly assigns attribution to the **Rootly bot**
* Email events default to **internal visibility**
* Attachments are not ingested as timeline files (only the text body is added)

***

### Troubleshooting

<AccordionGroup>
  <Accordion title="My email reply didn’t create a timeline event">
    The reply may have lost the critical **References** header, which Rootly uses to link messages to incidents.\
    Other causes include:

    * Sender domain not whitelisted
    * Email integration disabled
    * Message rejected due to provenance enforcement
  </Accordion>

  <Accordion title="Why is the event authored by the Rootly bot?">
    This occurs when Rootly cannot match the sender’s email address to a user in your workspace.\
    In those cases, the system defaults to the Rootly bot.
  </Accordion>

  <Accordion title="Can I edit or change the visibility of email events?">
    No. Email-created timeline events are immutable and always internal.
  </Accordion>

  <Accordion title="Can I start incidents via email?">
    Yes. When an inbound message does not belong to an existing thread, Rootly creates a new incident using its subject, body, and any auto-parsed metadata.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).