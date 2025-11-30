# Source: https://www.electronjs.org/docs/latest/tutorial/represented-file

On this page

# Representing Files in a BrowserWindow

## Overview[â€‹](#overview "Direct link to Overview") 

On macOS, you can set a represented file for any window in your application. The represented file\'s icon will be shown in the title bar, and when users `Command-Click` or `Control-Click`, a popup with a path to the file will be shown.

![Represented File](https://cloud.githubusercontent.com/assets/639601/5082061/670a949a-6f14-11e4-987a-9aaa04b23c1d.png)

> NOTE: The screenshot above is an example where this feature is used to indicate the currently opened file in the Atom text editor.

You can also set the edited state for a window so that the file icon can indicate whether the document in this window has been modified.

To set the represented file of window, you can use the [BrowserWindow.setRepresentedFilename](/docs/latest/api/browser-window#winsetrepresentedfilenamefilename-macos) and [BrowserWindow.setDocumentEdited](/docs/latest/api/browser-window#winsetdocumenteditededited-macos) APIs.

## Example[â€‹](#example "Direct link to Example") 

[][][]

[docs/fiddles/features/represented-file (39.2.4)](https://github.com/electron/electron/tree/v39.2.4/docs/fiddles/features/represented-file)[Open in Fiddle](https://fiddle.electronjs.org/launch?target=electron/v39.2.4/docs/fiddles/features/represented-file)

- main.js
- index.html

``` 
const  = require('electron/main')
const os = require('node:os')

function createWindow () )

  win.setRepresentedFilename(os.homedir())
  win.setDocumentEdited(true)

  win.loadFile('index.html')
}

app.whenReady().then(() => 
  })
})

app.on('window-all-closed', () => 
})
```

``` 
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Hello World!</title>
    <meta http-equiv="Content-Security-Policy" content="script-src 'self' 'unsafe-inline';" />
    <link rel="stylesheet" type="text/css" href="./styles.css">
</head>
<body>
    <h1>Hello World!</h1>
    <p>
      Click on the title with the <pre>Command</pre> or <pre>Control</pre> key pressed.
      You should see a popup with the represented file at the top.
    </p>
  </body>
</body>
</html>
```

After launching the Electron application, click on the title with `Command` or `Control` key pressed. You should see a popup with the represented file at the top. In this guide, this is the current user\'s home directory:

![Represented file](/assets/images/represented-file-95ff830878c432520d91d1e95f4b55ac.png)

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/represented-file.md)