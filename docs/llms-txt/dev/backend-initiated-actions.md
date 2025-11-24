# Source: https://dev.writer.com/framework/backend-initiated-actions.md

# Backend-initiated actions

Targeted, backend-initiated actions can be triggered from event handlers, using methods of `state`. Internally, this is achieved using Framework's `mail`, ephemeral state that is cleared when it reaches the intended user.

## Triggering a file download

The `file_download` method takes the `data` and `file_name` arguments. The first must contain raw bytes (a `bytes` object) or a packed file. As mentioned in the [Application State](/framework/application-state#managing-files-and-binary-data) section of the guide, a packed file is obtained using the `wf.pack_file` or `wf.pack_bytes` methods.

```py  theme={null}
def handle_file_download(state):
    # Pack the file as a FileWrapper object
    data = wf.pack_file("assets/story.txt", "text/plain")
    file_name = "thestory.txt"
    state.file_download(data, file_name)
```

## Adding a notification

<img src="https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/backend-initiated-actions.notifications.png?fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=ae08937660ab594dfbefadb6b5ef8bab" alt="Notifications" data-og-width="2291" width="2291" data-og-height="697" height="697" data-path="framework/images/backend-initiated-actions.notifications.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/backend-initiated-actions.notifications.png?w=280&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=85c22cfd26411eb89c0d7e28ca776db1 280w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/backend-initiated-actions.notifications.png?w=560&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=6e415f1179b026bc3de99b3723ddf6a9 560w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/backend-initiated-actions.notifications.png?w=840&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=9ee835d8e92ccba41e3c314149993bb6 840w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/backend-initiated-actions.notifications.png?w=1100&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=d55e383bba0746cf168bbe01f5a328f8 1100w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/backend-initiated-actions.notifications.png?w=1650&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=95999eea9d793b0801da0b1197a759ae 1650w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/backend-initiated-actions.notifications.png?w=2500&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=a32e0bcaa3e3dc7f91415d165d8941db 2500w" />

Framework adds notifications when a runtime error takes place. You can add your own notifications using the `add_notification` method, which takes the `type`, `title` and `message` arguments. `type` must be one of `error`, `warning`, `info`, `success`.

```py  theme={null}
def notify_of_things_that_happened(state):
    state.add_notification("error", "An Error", "Something bad happened.")
    state.add_notification("warning", "A Warning", "Be aware that something happened.")
    state.add_notification("info", "Some Info", "Something happened.")
    state.add_notification("success", "A Success", "Something good happened.")
```

## Opening a URL

Open a URL in a new tab using the `open_url` method, which takes the `url` argument.

```py  theme={null}
def handle_open_website(state):
    state.open_url("https://writer.com")
```

The URL will be safely opened with `noopener` and `noreferrer` options.

<Warning>
  Popup blockers: Given that the URL is opened asynchronously, popup blockers will likely block the new window —unless the user has opted in.
</Warning>

## Changing the active page

The active page and route parameters can be changed using the methods `set_page` and `set_route_vars`. This is explained in more detail in [Page Routes](/framework/page-routes).
