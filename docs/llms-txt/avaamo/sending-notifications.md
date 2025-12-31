# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/sending-notifications.md

# Send SMS - SMS.send

You can send SMS notifications from the skill using the **SMS.send** function. See [Notifications](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/reference-library/notifications#email-send), for more information on the complete syntax.

Consider that after placing the order in **Mac Pizza Agent**, you wish to send an SMS notification to the user. The following is a sample JS to send SMS notifications with order details:

{% code overflow="wrap" %}

```javascript
SMS.send("Thank you for placing order. Your order has been placed successfully and will be delivered soon. Visit Mac Pizza website for more details",["+918889997654"]);
```

{% endcode %}

An SMS is sent according to the details mentioned in the **SMS.send** function:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fz2xfz30T6B5wB4lE5y1k%2Fimage.png?alt=media\&token=ee34fca5-2d40-4ad7-9322-4b33a5bed0af)
