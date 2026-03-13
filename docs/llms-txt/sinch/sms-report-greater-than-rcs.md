# Source: https://docs.sinch.com/send-a-message/sms-report-greater-than-rcs.md

# SMS Report > RCS

SMS Report > RCS On the Messaging platform, it is now possible to send SMS converted into RCS.&#x20;

To gain access, talk to your **Account Executive** and ask our [**team for help**](https://docs-latam.messaging.sinch.com/support) in configuring your account!

Once you have this configuration and have taken shots, the best way to monitor the success of your campaign will be to view the report, right?&#x20;

Well, here is a brief guide to what you need to know!&#x20;

**New Columns:** find out what this report has to offer

Here we list the new columns:&#x20;

**Read:** containing only YES/NO \
**Read at:** containing date and time it was opened \
**Billing type:** indicating whether the message is Basic / Single and in cases where it only has a dash (-), it means that we are talking about an SMS message. \
**Sent as SMS (if there was a fallback to SMS):** Yes/No \
**Message parts:** number of parts that were sent&#x20;

### Understanding your MTs&#x20;

You will see your MTs that were converted as RCS only.&#x20;

### Viewing MOs&#x20;

Here you will see the MOs that interacted in the messages sent and converted to RCS only.

This is because the MOs of users who received the fallback SMS will be treated as “common MO”, without having any type of identification that indicates that the message was from the **SMS flow -> RCS.**&#x20;

To identify these MOs, it will be necessary to go to the SMS report and look at the MT that was associated with the MO, or the customer/subaccount of the MO, to find out if it is from a subaccount configured to send as SMS -> RCS.
