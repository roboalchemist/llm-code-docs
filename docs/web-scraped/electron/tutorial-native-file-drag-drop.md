# Source: https://www.electronjs.org/docs/latest/tutorial/native-file-drag-drop

On this page

# Native File Drag & Drop

## Overview[â€‹](#overview "Direct link to Overview") 

Certain kinds of applications that manipulate files might want to support the operating system\'s native file drag & drop feature. Dragging files into web content is common and supported by many websites. Electron additionally supports dragging files and content out from web content into the operating system\'s world.

To implement this feature in your app, you need to call the [`webContents.startDrag(item)`](/docs/latest/api/web-contents#contentsstartdragitem) API in response to the `ondragstart` event.

## Example[â€‹](#example "Direct link to Example") 

An example demonstrating how you can create a file on the fly to be dragged out of the window.

### Preload.js[â€‹](#preloadjs "Direct link to Preload.js") 

In `preload.js` use the [`contextBridge`](/docs/latest/api/context-bridge) to inject a method `window.electron.startDrag(...)` that will send an IPC message to the main process.

``` 
const  = require('electron')

contextBridge.exposeInMainWorld('electron', )
```

### Index.html[â€‹](#indexhtml "Direct link to Index.html") 

Add a draggable element to `index.html`, and reference your renderer script:

``` 
<div style="border:2px solid black;border-radius:3px;padding:5px;display:inline-block" draggable="true" id="drag">Drag me</div>
<script src="renderer.js"></script>
```

### Renderer.js[â€‹](#rendererjs "Direct link to Renderer.js") 

In `renderer.js` set up the renderer process to handle drag events by calling the method you added via the [`contextBridge`](/docs/latest/api/context-bridge) above.

``` 
document.getElementById('drag').ondragstart = (event) => 
```

### Main.js[â€‹](#mainjs "Direct link to Main.js") 

In the Main process (`main.js` file), expand the received event with a path to the file that is being dragged and an icon:

[][][]

[docs/fiddles/features/drag-and-drop (39.2.4)](https://github.com/electron/electron/tree/v39.2.4/docs/fiddles/features/drag-and-drop)[Open in Fiddle](https://fiddle.electronjs.org/launch?target=electron/v39.2.4/docs/fiddles/features/drag-and-drop)

- main.js
- preload.js
- index.html
- renderer.js

``` 
const  = require('electron/main')
const path = require('node:path')
const fs = require('node:fs')
const https = require('node:https')

function createWindow () 
  })

  win.loadFile('index.html')
}

const iconName = path.join(__dirname, 'iconForDragAndDrop.png')
const icon = fs.createWriteStream(iconName)

// Create a new file to copy - you can also copy existing files.
fs.writeFileSync(path.join(__dirname, 'drag-and-drop-1.md'), '# First file to test drag and drop')
fs.writeFileSync(path.join(__dirname, 'drag-and-drop-2.md'), '# Second file to test drag and drop')

https.get('https://img.icons8.com/ios/452/drag-and-drop.png', (response) => )

app.whenReady().then(createWindow)

ipcMain.on('ondragstart', (event, filePath) => )
})

app.on('window-all-closed', () => 
})

app.on('activate', () => 
})
```

``` 
const  = require('electron/renderer')

contextBridge.exposeInMainWorld('electron', )
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
    <p>Drag the boxes below to somewhere in your OS (Finder/Explorer, Desktop, etc.) to copy an example markdown file.</p>
    <div style="border:2px solid black;border-radius:3px;padding:5px;display:inline-block" draggable="true" id="drag1">Drag me - File 1</div>
    <div style="border:2px solid black;border-radius:3px;padding:5px;display:inline-block" draggable="true" id="drag2">Drag me - File 2</div>
    <script src="renderer.js"></script>
</body>
</html>
```

``` 
document.getElementById('drag1').ondragstart = (event) => 

document.getElementById('drag2').ondragstart = (event) => 
```

After launching the Electron application, try dragging and dropping the item from the BrowserWindow onto your desktop. In this guide, the item is a Markdown file located in the root of the project:

![Drag and drop](/assets/images/drag-and-drop-67d61d654b54bcc6bd497a1d1608dc29.gif)

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/native-file-drag-drop.md)