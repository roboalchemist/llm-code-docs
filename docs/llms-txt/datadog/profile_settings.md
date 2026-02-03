# Source: https://docs.datadoghq.com/incident_response/on-call/profile_settings.md

---
title: Profile Settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Incident Response > On-Call > Profile Settings
---

# Profile Settings

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% alert level="info" %}
To use Datadog On-Call on your mobile device, install the [Datadog mobile app](https://docs.datadoghq.com/mobile#installing).
{% /alert %}

You must [configure your profile settings](https://app.datadoghq.com/on-call/profile) before you can receive On-Call Pages. Your profile includes settings for contact methods, testing those methods, and notification preferences. These ensure that you receive timely and effective Pages.

## Configure your On-Call profile{% #configure-your-on-call-profile %}

Go to [My On-Call Profile](https://app.datadoghq.com/on-call/profile) to configure your settings.

### Contact methods{% #contact-methods %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/contact_methods.1e4714e4eadf122d332a96f00871234c.png?auto=format"
   alt="Adding contact methods in On-Call profile settings. A phone number, an email, and a mobile device are configured. The phone number is in a hover state, displaying 'Test Call' and 'Test SMS' options." /%}

- You must manually add your email or phone number. Afterwards, the screen asks you for consent to reach you through SMS. If you consent, a green badge appears next to your phone number, indicating that it can be used for SMS notification preferences below.
- If the Datadog [mobile app](https://docs.datadoghq.com/service_management/mobile/?tab=ios) is installed on your device, your device appears automatically in this list. Check your settings in the mobile app to ensure that your device can receive notifications.
- Datadog recommends that you test each of your contact methods. Hover over your contact method for test options.

{% alert level="info" %}
Phone number support varies by country. To see the supported list, open the phone number **Prefix** menu when adding a phone contact method in your On-Call profile. If your country does not appear, phone calls and SMS are not available for that location.
{% /alert %}

#### Supported contact methods{% #supported-contact-methods %}

- Push notifications through the [Datadog mobile app](https://docs.datadoghq.com/mobile)
- Emails (HTML or text format)
- SMS (Note, landlines, Voice Over Internet Protocol (VoIP) or virtual numbers are not supported.)
- Phone calls

To set up your mobile device, including how to **circumvent Do Not Disturb mode**, see [Set Up Your Mobile Device for Datadog On-Call](https://docs.datadoghq.com/incident_response/on-call/guides/configure-mobile-device-for-on-call).

### Notification preferences{% #notification-preferences %}

Notification preferences allow you to tailor how and when **you** are alerted for On-Call Pages based on the urgency of the situation. By configuring preferences for low urgency and high urgency, you can ensure that notifications are effective and unobtrusive, depending on the urgency of the Page. The urgency of a Page is determined within your [Routing Rules](https://docs.datadoghq.com/incident_response/on-call/routing_rules).

The system cycles through your configured notification preferences until you either acknowledge the Page, or the Page is escalated to the next on-call person as defined in the [Escalation Policy](https://docs.datadoghq.com/incident_response/on-call/escalation_policies).

#### High urgency notifications{% #high-urgency-notifications %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/high_urgency_notification_preferences.a668e089769b04f0a64eba05987262ea.png?auto=format"
   alt="Configuring high urgency notification preferences in On-Call profile settings: 'When a high urgency Page is triggered' set to notify a phone number immediately in order to quickly respond to critical Pages." /%}

Configure your high-urgency Pages (P1 monitor alerts, SEV-1 security threats, SEV-1 incidents, etc.), to demand immediate attention and escalation.

{% alert level="warning" %}
If you are paged for a high urgency incident and have not configured any notification preferences, Datadog automatically falls back to sending an email notification to ensure you are notified of critical issues.
{% /alert %}

For example, you can configure On-Call to start with a push notification, call after one minute, and send a follow-up push notification if unacknowledged after two minutes.

##### Best practices for high urgency{% #best-practices-for-high-urgency %}

- Use immediate push notifications and phone calls as the primary notification method for critical Pages.
- Keep follow-up intervals short to ensure rapid acknowledgment.
- Plan escalation policies carefully to avoid missed responses during emergencies.

#### Low urgency notifications{% #low-urgency-notifications %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/low_urgency_notification_preferences.5bcf0da072f5338c4f271b1534c4d0f8.png?auto=format"
   alt="Configuring low urgency notification preferences in On-Call profile settings: 'When a low urgency Page is triggered' set to notify an email immediately but don't escalate it further." /%}

Configure your low-urgency Pages (non-blocking issues, informational signals, etc.), to minimize disruptions while ensuring you stay informed. For example, you can opt to only yourself through email.

### Other notifications{% #other-notifications %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/settings_shift_reminder.65b458e30cddb9f5761cd4ac6a801eab.png?auto=format"
   alt="Configuring a shift reminder in On-Call profile settings. A shift reminder is configured to notify a phone number 10 minutes before the shift begins." /%}

Under **Other Notifications**, you can opt to receive a **Shift reminder** before your On-Call shift begins.

## Further Reading{% #further-reading %}

- [Datadog On-Call](https://docs.datadoghq.com/incident_response/on-call/)
