# Source: https://smartcar.com/docs/errors/connect-errors/oem-login-cancelled.md

# OEM Login Cancelled

> This error occurs when a user went to authorize directly with the OEM but exited the flow for some reason.

| Parameter           | Required | Description                                          |
| ------------------- | -------- | ---------------------------------------------------- |
| `error`             | `true`   | `oem_cancelled_login`                                |
| `error_description` | `true`   | The user did not complete authorization with the OEM |

```http Example redirect uri theme={null}
HTTP/1.1 302 Found
Location: https://example.com/callback
?error=oem_cancelled_login
&the%20user%20did%20not%20complete%20authorization%20with%20the%20OEM
```

<Frame caption="OEM Login Cancelled">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/oem-cancelled.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=809144a9de87c60d807cf552236babe0" data-og-width="1322" width="1322" data-og-height="1121" height="1121" data-path="images/errors/connect-errors/oem-cancelled.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/oem-cancelled.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=365a81c051c9bc890a80f803fae14d48 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/oem-cancelled.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=2ac28f3a48cdefcf6415c375ceaa2f9d 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/oem-cancelled.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c2cb8000dd88ea6342d1ad83d9084c63 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/oem-cancelled.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e1e21a85d978104ec6045741ea779acd 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/oem-cancelled.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=2f8500289efa26329c16d1c64aee9d4f 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/oem-cancelled.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=642123a43b235fe9a5862255bc5a2b2b 2500w" />
</Frame>
