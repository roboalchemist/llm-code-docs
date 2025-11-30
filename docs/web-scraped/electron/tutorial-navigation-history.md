# Source: https://www.electronjs.org/docs/latest/tutorial/navigation-history

On this page

# Navigation History

## Overview[â€‹](#overview "Direct link to Overview") 

The [NavigationHistory](/docs/latest/api/navigation-history) class allows you to manage and interact with the browsing history of your Electron application. This powerful feature enables you to create intuitive navigation experiences for your users.

## Accessing NavigationHistory[â€‹](#accessing-navigationhistory "Direct link to Accessing NavigationHistory") 

Navigation history is stored per [`WebContents`](/docs/latest/api/web-contents) instance. To access a specific instance of the NavigationHistory class, use the WebContents class\'s [`contents.navigationHistory` instance property](https://www.electronjs.org/docs/latest/api/web-contents#contentsnavigationhistory-readonly).

``` 
const  = require('electron')

const mainWindow = new BrowserWindow()
const  = mainWindow.webContents
```

## Navigating through history[â€‹](#navigating-through-history "Direct link to Navigating through history") 

Easily implement back and forward navigation:

``` 
// Go back
if (navigationHistory.canGoBack()) 

// Go forward
if (navigationHistory.canGoForward()) 
```

## Accessing history entries[â€‹](#accessing-history-entries "Direct link to Accessing history entries") 

Retrieve and display the user\'s browsing history:

``` 
const entries = navigationHistory.getAllEntries()

entries.forEach((entry) => : $`)
})
```

Each navigation entry corresponds to a specific page. The indexing system follows a sequential order:

- Index 0: Represents the earliest visited page.
- Index N: Represents the most recent page visited.

## Navigating to specific entries[â€‹](#navigating-to-specific-entries "Direct link to Navigating to specific entries") 

Allow users to jump to any point in their browsing history:

``` 
// Navigate to the 5th entry in the history, if the index is valid
navigationHistory.goToIndex(4)

// Navigate to the 2nd entry forward from the current position
if (navigationHistory.canGoToOffset(2)) 
```

## Restoring history[â€‹](#restoring-history "Direct link to Restoring history") 

A common flow is that you want to restore the history of a webContents - for instance to implement an \"undo close tab\" feature. To do so, you can call `navigationHistory.restore()`. This will restore the webContent\'s navigation history and the webContents location in said history, meaning that `goBack()` and `goForward()` navigate you through the stack as expected.

``` 
const firstWindow = new BrowserWindow()

// Later, you want a second window to have the same history and navigation position
async function restore () )
}
```

Here\'s a full example that you can open with Electron Fiddle:

[][][]

[docs/fiddles/features/navigation-history (39.2.4)](https://github.com/electron/electron/tree/v39.2.4/docs/fiddles/features/navigation-history)[Open in Fiddle](https://fiddle.electronjs.org/launch?target=electron/v39.2.4/docs/fiddles/features/navigation-history)

- main.js
- preload.js
- index.html
- renderer.js
- style.css

``` 
const  = require('electron')
const path = require('path')

function createWindow () 
  })

  mainWindow.loadFile('index.html')

  const view = new BrowserView()
  mainWindow.setBrowserView(view)
  view.setBounds()
  view.setAutoResize()

  const navigationHistory = view.webContents.navigationHistory
  ipcMain.handle('nav:back', () =>
    navigationHistory.goBack()
  )

  ipcMain.handle('nav:forward', () => )

  ipcMain.handle('nav:canGoBack', () => navigationHistory.canGoBack())
  ipcMain.handle('nav:canGoForward', () => navigationHistory.canGoForward())
  ipcMain.handle('nav:loadURL', (_, url) =>
    view.webContents.loadURL(url)
  )
  ipcMain.handle('nav:getCurrentURL', () => view.webContents.getURL())
  ipcMain.handle('nav:getHistory', () => )

  view.webContents.on('did-navigate', () => )

  view.webContents.on('did-navigate-in-page', () => )
}

app.whenReady().then(createWindow)

app.on('window-all-closed', () => )

app.on('activate', () => )
```

``` 
const  = require('electron')

contextBridge.exposeInMainWorld('electronAPI', )
```

``` 
<!DOCTYPE html>
<html>

<head>
    <title>Enhanced Browser with Navigation History</title>
    <link href="styles.css" rel="stylesheet" />
</head>

<body>

    <div id="controls">
        <button id="backBtn" title="Go back">Back</button>
        <button id="forwardBtn" title="Go forward">Forward</button>
        <button id="backHistoryBtn" title="Show back history">Back History</button>
        <button id="forwardHistoryBtn" title="Show forward history">Forward History</button>
        <input id="urlInput" type="text" placeholder="Enter URL">
        <button id="goBtn" title="Navigate to URL">Go</button>
    </div>

    <div id="historyPanel" class="history-panel"></div>

    <div id="description">
        <h2>Navigation History Demo</h2>
        <p>This demo showcases Electron's NavigationHistory API functionality.</p>
        <p><strong>Back/Forward:</strong> Navigate through your browsing history.</p>
        <p><strong>Back History/Forward History:</strong> View and select from your browsing history.</p>
        <p><strong>URL Bar:</strong> Enter a URL and click 'Go' or press Enter to navigate.</p>
    </div>
    <script src="renderer.js"></script>
</body>

</html>
```

``` 
const backBtn = document.getElementById('backBtn')
const forwardBtn = document.getElementById('forwardBtn')
const backHistoryBtn = document.getElementById('backHistoryBtn')
const forwardHistoryBtn = document.getElementById('forwardHistoryBtn')
const urlInput = document.getElementById('urlInput')
const goBtn = document.getElementById('goBtn')
const historyPanel = document.getElementById('historyPanel')

async function updateButtons () 

async function updateURL () 

function transformURL (url) 
  return url
}

async function navigate (url) 

async function showHistory (forward = false) 

  const relevantHistory = forward
    ? history.slice(currentIndex + 1)
    : history.slice(0, currentIndex).reverse()

  historyPanel.innerHTML = ''
  relevantHistory.forEach(entry => , URL: $`
    div.onclick = () => navigate(entry.url)
    historyPanel.appendChild(div)
  })

  historyPanel.style.display = 'block'
}

backBtn.addEventListener('click', () => window.electronAPI.goBack())
forwardBtn.addEventListener('click', () => window.electronAPI.goForward())
backHistoryBtn.addEventListener('click', () => showHistory(false))
forwardHistoryBtn.addEventListener('click', () => showHistory(true))
goBtn.addEventListener('click', () => navigate(urlInput.value))

urlInput.addEventListener('keypress', (e) => 
})

document.addEventListener('click', (e) => 
})

window.electronAPI.onNavigationUpdate(() => )

updateButtons()
```

``` 
body 
#controls 
button 
button:hover 
button:disabled 
#urlInput 

#historyPanel 
  #historyPanel div 

#description 
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/navigation-history.md)