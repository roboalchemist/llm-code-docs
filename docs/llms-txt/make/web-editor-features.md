# Source: https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/web-editor-features.md

# Make web interface

The Make web interface lets you create and manage the custom apps configuration directly within the Make platform.

## Access the Make web interface

To access the web interface:

{% stepper %}
{% step %}
Log in to Make.
{% endstep %}

{% step %}
In the left navigation, click **Custom Apps**.

You may need to first click **More** to see this option.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-e21787568a82c84ef53808e640808518fdeb168f%2Faccessing_web_interface.png?alt=media" alt="" width="111"><figcaption></figcaption></figure></div>
{% endstep %}
{% endstepper %}

The Custom Apps dashboard is where you can create a new app, see your existing apps, and see the status of your app (public or private).

See the [Create your first app section](https://developers.make.com/custom-apps-documentation/create-your-first-app/overview) to get started.

## Web code editor key features

After completing the initial set up of your app, you can use the web code editor to build your app.

The following are helpful features of the editor:

1. Hints with links to documentation for more information.
2. A format code button with a label showing the data format. The available data formats are:
   * `jsonc`
   * `json`
   * `javascript`
   * `markdown`
3. Context-aware code suggestions for the `jsonc` data format. The web code editor gives you hints about parameters or properties you can add to the custom app code. The code suggestions even work for RPCs.
4. Hints displayed when hovering over the custom app configuration.
5. Custom app code validation for the `jsonc` data format. If you misspell a code property name or if you place a property in an invalid code section, the web code editor highlights the error.
6. A **Save changes** button to save changes in all editor boxes on the page.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-ac01c039a15ea75308d84fa7fb642c4ab86eb199%2Feditor_fullimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

7. Hovering over [built-in IML functions](https://developers.make.com/custom-apps-documentation/app-components/iml-functions) shows detailed information.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-9b602ca3a6bf134bd63c8ff30fc7e323d7fb238f%2Fhover1.png?alt=media" alt="" width="434"><figcaption></figcaption></figure></div>

8. Hovering over [custom IML functions](https://developers.make.com/custom-apps-documentation/app-components/iml-functions) provides a link to the function definition.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-7d29c6b16dcf27981b08bc6e5e89984a2eeb766b%2Fhover2.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

9. Controls to expand and collapse the code. To view the controls, hover over the space between your code and editor line numbers.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-1496143f7167d8c8b7458a729349c5baf3ed8529%2Fcollapse_the_code.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

10. The editor highlights the IML syntax so it's distinct from the rest of the code.

## Web code editor keyboard shortcuts

The web code editor is built on the same backend as the Visual Studio Code. If you know VS Code, you will find that some shortcuts also work in the web code editor. Some of the most useful web code editor shortcuts are:

For **Windows** users:

<table><thead><tr><th width="187" valign="top">Shortcut</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><strong>Ctrl + Shift + H</strong></td><td valign="top">Show a cheat sheet with selected shortcuts</td></tr><tr><td valign="top"><strong>Ctrl + S</strong></td><td valign="top">Save changes to all of the editor boxes on the page</td></tr><tr><td valign="top"><strong>Ctrl + F</strong></td><td valign="top">Search in the editor box content</td></tr><tr><td valign="top"><strong>Ctrl + H</strong></td><td valign="top">Search and replace in the editor box content</td></tr><tr><td valign="top"><strong>Ctrl + Space</strong></td><td valign="top">Show a list of code suggestions valid in the current cursor context</td></tr><tr><td valign="top"><strong>Shift + Alt + F</strong></td><td valign="top">Format code</td></tr><tr><td valign="top"><strong>Ctrl + /</strong></td><td valign="top">Toggle line comments</td></tr><tr><td valign="top"><strong>F1</strong></td><td valign="top">Display web code editor command and shortcut reference</td></tr></tbody></table>

For **MacOS** users:

<table><thead><tr><th width="186">Shortcut</th><th>Description</th></tr></thead><tbody><tr><td><strong>Ctrl + Shift + H</strong></td><td>Show a cheat sheet with selected shortcuts</td></tr><tr><td><strong>Cmd + S</strong></td><td>Save changes to all of the editor boxes on the page</td></tr><tr><td><strong>Cmd + F</strong></td><td>Search in the editor box content</td></tr><tr><td><strong>Opt + Cmd + F</strong></td><td>Search and replace in the editor box content</td></tr><tr><td><strong>Ctrl + Space</strong></td><td>Show a list of code suggestions valid in the current cursor context</td></tr><tr><td><strong>Shift + Opt + F</strong></td><td>Format code</td></tr><tr><td><strong>F1</strong></td><td>Display web code editor command and shortcut reference</td></tr></tbody></table>

For a full reference of the web code editor shortcuts check the official [VSCode documentation](https://code.visualstudio.com/docs/getstarted/keybindings#_keyboard-shortcuts-reference) and the official VSCode shortcuts cards:

* [MacOS](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)
* [Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)

{% hint style="info" %}
Your browser might interpret some keyboard shortcuts differently. For example, the shortcut Ctrl + N creates a new file in VSCode, but in Google Chrome the shortcut creates a new browser window instead.
{% endhint %}
