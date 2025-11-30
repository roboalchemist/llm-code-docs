# Source: https://www.electronjs.org/docs/latest/tutorial/examples

On this page

# Examples Overview

In this section, we have collected a set of guides for common features that you may want to implement in your Electron application. Each guide contains a practical example in a minimal, self-contained example app. The easiest way to run these examples is by downloading [Electron Fiddle](https://www.electronjs.org/fiddle).

Once Fiddle is installed, you can press on the \"Open in Fiddle\" button that you will find below code samples like the following one:

[][][]

[docs/fiddles/quick-start (39.2.4)](https://github.com/electron/electron/tree/v39.2.4/docs/fiddles/quick-start)[Open in Fiddle](https://fiddle.electronjs.org/launch?target=electron/v39.2.4/docs/fiddles/quick-start)

- main.js
- preload.js
- index.html

``` 
const  = require('electron/main')
const path = require('node:path')

function createWindow () 
  })

  win.loadFile('index.html')
}

app.whenReady().then(() => 
  })
})

app.on('window-all-closed', () => 
})
```

``` 
window.addEventListener('DOMContentLoaded', () => 

  for (const type of ['chrome', 'node', 'electron']) -version`, process.versions[type])
  }
})
```

``` 
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Hello World!</title>
    <meta http-equiv="Content-Security-Policy" content="script-src 'self' 'unsafe-inline';" />
</head>
<body>
    <h1>Hello World!</h1>
    <p>
        We are using Node.js <span id="node-version"></span>,
        Chromium <span id="chrome-version"></span>,
        and Electron <span id="electron-version"></span>.
    </p>
</body>
</html>
```

## How to\...?[â€‹](#how-to "Direct link to How to...?") 

You can find the full list of \"How to?\" in the sidebar. If there is something that you would like to do that is not documented, please join our [Discord server](https://discord.com/invite/electronjs) and let us know!

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/examples.md)