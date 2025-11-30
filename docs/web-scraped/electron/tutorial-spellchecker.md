# Source: https://www.electronjs.org/docs/latest/tutorial/spellchecker

On this page

# SpellChecker

Electron has built-in support for Chromium\'s spellchecker since Electron 8. On Windows and Linux this is powered by Hunspell dictionaries, and on macOS it makes use of the native spellchecker APIs.

## How to enable the spellchecker?[â€‹](#how-to-enable-the-spellchecker "Direct link to How to enable the spellchecker?") 

For Electron 9 and higher the spellchecker is enabled by default. For Electron 8 you need to enable it in `webPreferences`.

``` 
const myWindow = new BrowserWindow(
})
```

## How to set the languages the spellchecker uses?[â€‹](#how-to-set-the-languages-the-spellchecker-uses "Direct link to How to set the languages the spellchecker uses?") 

On macOS as we use the native APIs there is no way to set the language that the spellchecker uses. By default on macOS the native spellchecker will automatically detect the language being used for you.

For Windows and Linux there are a few Electron APIs you should use to set the languages for the spellchecker.

``` 
// Sets the spellchecker to check English US and French
myWindow.webContents.session.setSpellCheckerLanguages(['en-US', 'fr'])

// An array of all available language codes
const possibleLanguages = myWindow.webContents.session.availableSpellCheckerLanguages
```

By default the spellchecker will enable the language matching the current OS locale.

## How do I put the results of the spellchecker in my context menu?[â€‹](#how-do-i-put-the-results-of-the-spellchecker-in-my-context-menu "Direct link to How do I put the results of the spellchecker in my context menu?") 

All the required information to generate a context menu is provided in the [`context-menu`](/docs/latest/api/web-contents#event-context-menu) event on each `webContents` instance. A small example of how to make a context menu with this information is provided below.

``` 
const  = require('electron')

myWindow.webContents.on('context-menu', (event, params) => ))
  }

  // Allow users to add the misspelled word to the dictionary
  if (params.misspelledWord) )
    )
  }

  menu.popup()
})
```

## Does the spellchecker use any Google services?[â€‹](#does-the-spellchecker-use-any-google-services "Direct link to Does the spellchecker use any Google services?") 

Although the spellchecker itself does not send any typings, words or user input to Google services the hunspell dictionary files are downloaded from a Google CDN by default. If you want to avoid this you can provide an alternative URL to download the dictionaries from.

``` 
myWindow.webContents.session.setSpellCheckerDictionaryDownloadURL('https://example.com/dictionaries/')
```

Check out the docs for [`session.setSpellCheckerDictionaryDownloadURL`](/docs/latest/api/session#sessetspellcheckerdictionarydownloadurlurl) for more information on where to get the dictionary files from and how you need to host them.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/spellchecker.md)