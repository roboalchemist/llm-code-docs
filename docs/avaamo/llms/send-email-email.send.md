# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/send-email-email.send.md

# Send Email - Email.send

You can send email notifications from the skill using the **Email.send** function. See [Notifications](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/reference-library/notifications#email-send), for more information on the complete syntax.

Consider that after placing the order in **Mac Pizza Agent**, you wish to send an email notification to the user. The following is a sample JS to send email notifications:

```javascript
Email.send({ 
from: ["admin@macpizza.com"],
 to: ["john@avaamo.com"],
 subject: "Mac Pizza Order Placed Successfully.",
 body: "Thank you for placing order. Your order has been placed successfully and will be delivered soon. Visit Mac Pizza website for more details."
})
```

An email is sent according to the details mentioned in the **Email.send** function:

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LrPSJXyQxNhf8wj6na1%2F-LrPSM6EeD4WWk-XFfOK%2Fjs-send-email.png?alt=media&#x26;token=36cb3375-30c5-4651-ab5c-d8b2d37d80fc" alt=""></div>

### SMS notification &#x20;
