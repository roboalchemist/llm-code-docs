# Source: https://docs.datadoghq.com/incident_response/on-call/triggering_pages/live_call_routing.md

---
title: Live Call Routing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Incident Response > On-Call > Trigger a Page > Live Call Routing
---

# Live Call Routing

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% alert level="info" %}
Live call routing is provisioned by Datadog. To enable it for your organization, contact your account manager or [Datadog Support](mailto:support@datadoghq.com). Include your use case and the country and country code where you need the number provisioned (for example, `+1`, United States).
{% /alert %}

## Overview{% #overview %}

Live call routing connects phone calls to your On-Call team. When someone calls your dedicated number, the system handles the call according to your configuration.

Datadog On-Call supports two routing types:

- **Direct call routing**: Connects the caller to an active responder, following the escalation policy for the On-Call team. Enables real-time coordination during critical incidents.
- **Voicemail routing**: Prompts the caller to leave a voicemail, then converts the voice message to a page for the On-Call team. Useful for non-technical callers or third-party vendors who need to report issues without a live conversation.

## Configuration{% #configuration %}

### Basic route settings{% #basic-route-settings %}

Each live call route includes:

- **Name**: A descriptive label, such as "Production Incidents" or "Security Escalations."
- **Phone Number**: The dedicated number provisioned by Datadog for this route.
- **Region Code**: The geographic region for the phone number (for example, `US` for the United States).
- **Active Status**: Whether the route is currently accepting calls.
- **Routing Type**: How calls are handled (see Routing types).

### Keypad options{% #keypad-options %}

Keypad options offer callers a menu when they dial your routing number.

You can configure up to nine options per route. Each option maps a key (1-9) to an On-Call team and triggers that team's paging process. To improve usability:

- Use option 1 for the most critical team or escalation path.
- Group related teams under adjacent keys.
- Keep menu prompts concise and clear.

## Routing types{% #routing-types %}

Datadog On-Call supports two routing types: direct call routing and voicemail routing.

### Direct call routing{% #direct-call-routing %}

In direct call routing, the system follows the On-Call team's escalation policy to connect the caller to the first available responder.

Responders must have valid phone numbers in their profiles; On-Call skips any responders that don't.

Responders then have the following options:

- Press `1` to acknowledge the call.
- Press `2` to escalate it.
- Press `3` to resolve it.

#### Escalation logic{% #escalation-logic %}

For direct call routing, escalation proceeds as follows:

- **Multiple responders at the same level**: All responders are called simultaneously. The first to answer is connected.
- **Responder rejects a call**: The system immediately escalates to the next responder.
- **Responder has no phone number**: The system skips the responder.
- **Only one escalation level is defined**: If the responder is unreachable, the caller is informed that no one is available, and the call ends.
- **No responders have valid phone numbers**: The caller is informed that no one is available, and the call ends.

#### Best practices{% #best-practices %}

- Use multi-level escalation policies to avoid dropped calls.
- Add multiple responders at critical levels for redundancy.
- Test your routing setup regularly:
  - Test each keypad option to verify it routes to the correct team.
  - Simulate escalation behavior by rejecting or not answering a call.
  - Check that responders' phone numbers are valid, reachable, and configured with appropriate voicemail settings.
  - Verify that calls successfully connect to available responders.

### Voicemail routing{% #voicemail-routing %}

In voicemail routing, callers are prompted to leave a message. The message is transcribed and sent as a page to the On-Call team.

#### Best practices{% #best-practices-1 %}

- Confirm team members have notification preferences configured to receive pages.
- Test your routing setup regularly:
  - Test each keypad option to verify it routes to the correct team.
  - Confirm that voicemail recordings are properly captured and transcribed.
  - Verify that pages are created and sent to the correct team members.

## Troubleshooting{% #troubleshooting %}

### Route issues{% #route-issues %}

If your route isn't accepting calls:

- Ensure the route is active.
- Confirm provisioning is complete.
- Verify the phone number is correctly configured.

### Keypad problems{% #keypad-problems %}

- Ensure keypad options are linked to a valid On-Call team, and test each option individually.
- Verify that your phone system supports DTMF (touch-tone) input.

### Voicemail and page issues{% #voicemail-and-page-issues %}

If voicemail isn't converting to pages:

- For **direct call routing**: If calls fall back to voicemail or fail to page, confirm that the On-Call team is properly configured and that team members have valid notification preferences in place.
- For **voicemail routing**: Confirm that your routing type is set to voicemail, the On-Call team is properly configured, and team members have valid notification preferences configured to receive pages.
