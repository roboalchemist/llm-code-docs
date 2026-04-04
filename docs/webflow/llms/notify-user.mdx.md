# Source: https://developers.webflow.com/designer/reference/notify-user.mdx

***

title: Send notification to user
slug: designer/reference/notify-user
description: ''
hidden: false
'og:title': 'Webflow Designer API: Send notification to user'
'og:description': >-
Send an in-Designer notification to the user. The notification can be styled
as either a success, error, or general information message. Error messages
provide users with the opportunity to close the Designer Extension
------------------------------------------------------------------

## `notify(opts)`

Send an in-Designer notification to the user. The notification can be styled as either a success, error, or general information message. Error messages provide users with the opportunity to close the Designer Extension.

<video autoplay loop muted>
    

  <source src="https://dhygzobemt712.cloudfront.net/Web/developers/videos/24005_API%20Documentation_User%20Events.webm" type="video/webm" />

    Your browser doesn't support HTML video.
</video>

### Syntax

```typescript
webflow.notify(
  opts: {
    type: 'Error' | 'Info' | 'Success',
    message: string,
  }
): Promise<void>
```

### Parameters

**`opts`** :   `{message: string, type: 'Error' | 'Info' | 'Success'`

The options for the notification.

* **message**: string
* **type**: "Error" | "Info" | "Success"

### Returns

**Promise\<*Void*>**

A Promise that returns a value of `undefined`.

### Example

```typescript
webflow.notify({ type: 'Info', message: 'Great work!' }); // General notification
webflow.notify({ type: 'Error', message: 'Something went wrong, try again!' }); // Error notification
webflow.notify({ type: 'Success', message: 'Successfully did something!' }); // Success notification
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

***
