# Source: https://www.electronjs.org/docs/latest/api/structures/shortcut-details

# ShortcutDetails Object

- `target` string - The target to launch from this shortcut.
- `cwd` string (optional) - The working directory. Default is empty.
- `args` string (optional) - The arguments to be applied to `target` when launching from this shortcut. Default is empty.
- `description` string (optional) - The description of the shortcut. Default is empty.
- `icon` string (optional) - The path to the icon, can be a DLL or EXE. `icon` and `iconIndex` have to be set together. Default is empty, which uses the target\'s icon.
- `iconIndex` number (optional) - The resource ID of icon when `icon` is a DLL or EXE. Default is 0.
- `appUserModelId` string (optional) - The Application User Model ID. Default is empty.
- `toastActivatorClsid` string (optional) - The Application Toast Activator CLSID. Needed for participating in Action Center.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/shortcut-details.md)