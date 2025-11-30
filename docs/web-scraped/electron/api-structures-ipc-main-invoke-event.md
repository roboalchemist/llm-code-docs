# Source: https://www.electronjs.org/docs/latest/api/structures/ipc-main-invoke-event

# IpcMainInvokeEvent Object extends `Event`

- `type` String - Possible values include `frame`
- `processId` Integer - The internal ID of the renderer process that sent this message
- `frameId` Integer - The ID of the renderer frame that sent this message
- `sender` [WebContents](/docs/latest/api/web-contents) - Returns the `webContents` that sent the message
- `senderFrame` [WebFrameMain](/docs/latest/api/web-frame-main) \| null *Readonly* - The frame that sent this message. May be `null` if accessed after the frame has either navigated or been destroyed.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/ipc-main-invoke-event.md)