# Source: https://developers.kit.com/plugins/content-blocks/plugin-security.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Plugin security

> Security for your content block plugins

When we receive an HTML string from your server, we will [sanitize it](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) to conform with recommended security practices. That means we’ll reject your HTML response if it includes any of the following:

* Scripts, iframes
* Audio, video elements
* Form, input, command, action, prompt elements
* External CSS styles, and CSS URLs


Built with [Mintlify](https://mintlify.com).