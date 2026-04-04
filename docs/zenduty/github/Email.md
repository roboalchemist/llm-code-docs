---
id: Email
title: Email
---
To create incidents via Email with Zenduty, complete the following steps:

1. Go to your service page and click on Add integration.

2. Select Email.

3. Zenduty will generate an email endpoint in the format - integration-key@integrations.zenduty.com.

4. Copy the email address and paste it the email notification section of your tool.

5. Zenduty will create an alert and incident for every email received.
.
6. The hash of subject of the email(with keywords and special characters removed) will be the entity_id for the incident.

FAQ

Q: I am trying to send an email to the given email address, but it's not creating an incident:
A: Possible reasons for this to happen:
a) The email being sent does not contain the integration email address in the "To" section.
b) The email is sent to a group email address and not to the Zenduty email address individually
c) The email source is unverified. Make sure that the email is being sent by a genuine mail server and a verified mail account.
