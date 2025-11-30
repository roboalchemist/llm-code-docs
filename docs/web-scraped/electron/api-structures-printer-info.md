# Source: https://www.electronjs.org/docs/latest/api/structures/printer-info

On this page

# PrinterInfo Object

- `name` string - the name of the printer as understood by the OS.
- `displayName` string - the name of the printer as shown in Print Preview.
- `description` string - a longer description of the printer\'s type.
- `options` Object - an object containing a variable number of platform-specific printer information.

The number represented by `status` means different things on different platforms: on Windows its potential values can be found [here](https://learn.microsoft.com/en-us/windows/win32/printdocs/printer-info-2), and on Linux and macOS they can be found [here](https://www.cups.org/doc/cupspm.html).

## Example[â€‹](#example "Direct link to Example") 

Below is an example of some of the additional options that may be set which may be different on each platform.

``` 

}
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/printer-info.md)