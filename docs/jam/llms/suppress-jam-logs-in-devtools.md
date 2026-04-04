# Source: https://jam.dev/docs/guides/tutorials/suppress-jam-logs-in-devtools.md

# Suppress Jam Logs in DevTools

If you’re a web developer using Jam, you may want to reset the file names you see in your console logs while developing. It’s unfortunately not possible from our end, but it is possible from yours. 😅

Here is how you can add Jam’s scripts to an ignore list, reseting the file names you see in the console:

What you will need to do is add Jam’s `jam-console-devtools.js` script to your ignore list. You can follow these instructions to do so on this page: [https://developer.chrome.com/docs/devtools/javascript/reference/#call-stack-ignore-list](https://developer.chrome.com/docs/devtools/javascript/reference/?ref=jam-documentation.ghost.io#call-stack-ignore-list)

Or, watch this video (instead of consolePlugin.ts it should be `jam-extension-console-proxy.js`):

{% embed url="<https://youtube.com/shorts/e-w8UtlG0iQ>" %}
