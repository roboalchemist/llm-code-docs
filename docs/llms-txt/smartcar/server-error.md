# Source: https://smartcar.com/docs/errors/connect-errors/server-error.md

# Server

> If there is a server error, the user will return to your application.

| Parameter          | Required | Description                                |
| ------------------ | -------- | ------------------------------------------ |
| error              | true     | server\_error                              |
| error\_description | true     | Unexpected server error. Please try again. |

```http Example redirect uri theme={null}
HTTP/1.1 302 Found
Location: https://example.com/callback
?error=configuration_error
&error_description=There%20has%20been%20an%20error%20in%20the%20configuration%20of%20your%20application.&status_code=400
&error_message=You%20have%20entered%20a%20test%20mode%20VIN.%20Please%20enter%20a%20VIN%20that%20belongs%20to%20a%20real%20vehicle.
```

<Note>
  We only show the “Exit” button if a redirect URI is available. If there is a failure before the validation of the redirect URI,  we are unable to include the “Exit” button on the Error page. In those cases, we would not be able to report the `status_code` and `error_message` back to the developer, but they will still be available on screen in the Error page.
</Note>

<Frame caption="Server Error">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/server-error.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=94b0f9f1020d0dcd1156754de31c4231" data-og-width="2000" width="2000" data-og-height="1602" height="1602" data-path="images/errors/connect-errors/server-error.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/server-error.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=9d225822dd6024c1cac4ada2250c45d9 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/server-error.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=d929cb64c48fecfae38c9f35ef9132d9 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/server-error.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=874e0804fd145ee9fb5cffc370cd0afd 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/server-error.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=6ca984de7807d5d6f2a225f1640375d6 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/server-error.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=5d3c20c1d070c54d543058fd4797951b 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/server-error.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=04f572a9df9d09c7c47979dc06bee0f0 2500w" />
</Frame>
