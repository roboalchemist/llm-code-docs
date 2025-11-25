# Source: https://smartcar.com/docs/errors/connect-errors/configuration-error.md

# Configuration

> This error occurs when the user has encountered an Error page in Connect and has chosen to return to your application.

| Parameter           | Required | Description                                                       |
| ------------------- | -------- | ----------------------------------------------------------------- |
| `error`             | `true`   | `configuration_error`                                             |
| `error_description` | `true`   | There has been an error in the configuration of your application. |
| `status_code`       | `true`   | The status code of the error encountered in Connect               |
| `error_message`     | `true`   | The error message seen by the user                                |

```http Example redirect uri theme={null}
HTTP/1.1 302 Found
Location: https://example.com/callback
?error=configuration_error
&error_description=There%20has%20been%20an%20error%20in%20the%20configuration%20of%20your%20application.&status_code=400
&error_message=You%20have%20entered%20a%20test%20mode%20VIN.%20Please%20enter%20a%20VIN%20that%20belongs%20to%20a%20real%20vehicle.
```

On redirect, Connect will return the status code and message of the error that they encountered. This will be triggered if:

* A user tried to directly navigate to a page that is past their current step in Connect (ie. going directly from the Preamble screen to the Permission Grants screen by directly going to connect.smartcar.com/grant).
* A user is trying to use Single Select in live mode with a test mode VIN or with a simulated VIN in a non-simulated mode.
* A user is trying to use Single Select with an invalid mock VIN.
* A validation error occurs when trying to check compatibility by VIN.

These cases will trigger the following error and give the user the ability to “Exit” Connect.

<Frame caption="Error Page">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/error_page.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=69b4a1e91f6223798b03ed57e696f9e8" data-og-width="457" width="457" data-og-height="590" height="590" data-path="images/api-reference/error_page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/error_page.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=2f208da34113d1c7b21406c00c7555c3 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/error_page.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=f93e888a88c515ed8f83b69754db53e2 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/error_page.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1afc3e47c727f6526a9bf22bdaf56e10 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/error_page.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=fac59069a414dfd5d4f87795f08c138e 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/error_page.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=12945d56509b0cb91d6d51609f60be57 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/error_page.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=f6fcac1b5d72e1e32ed4281b7c645187 2500w" />
</Frame>
