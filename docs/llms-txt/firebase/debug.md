# Source: https://firebase.google.com/docs/dynamic-links/debug.md.txt

# Source: https://firebase.google.com/docs/studio/debug.md.txt

# Source: https://firebase.google.com/docs/dynamic-links/debug.md.txt

# Source: https://firebase.google.com/docs/studio/debug.md.txt

Firebase Studiooffers a few different ways to debug your app, directly from your workspace. For web and Flutter apps, a web console and[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview)are directly integrated into the workspace. Flutter apps offer Android and web previews to spot-check and test your app while you code.

Richer, breakpoint-based debugging is also available for most common languages, through the built-in Debug Console, and extensible with[Debugger extensions from OpenVSX](https://open-vsx.org/?category=Debuggers). For breakpoint-based debugging of your frontend web code (like JavaScript), you can continue using your browser's built-in developer tools, like[Chrome's DevTools](https://developer.chrome.com/docs/devtools).

## Preview your app

Firebase Studioincludes[in-workspace app previews](https://firebase.google.com/docs/studio/preview-apps)for web apps (Chrome) and Flutter apps (Android, Chrome). The Android and Chrome previews support hot reload and hot refresh, and offer full emulator capabilities.

To learn more aboutFirebase Studiopreviews, see[Preview your app](https://firebase.google.com/docs/studio/preview-apps).

## Use the integrated web console for web previews

![Minimized console bar in the Firebase Studio web preview](https://firebase.google.com/static/docs/studio/images/web-console.png)

The integrated web console helps you diagnose issues in your app directly from the web preview. You can access the web console in theFirebase Studioweb preview panel by expanding the bar at the bottom.

Note that this feature is experimental and isn't enabled by default. To turn it on, follow these steps, and[share your feedback](https://firebase.google.com/support/troubleshooter/studio)after you've tried it out:

1. Add the web console to yourFirebase Studioworkspace:

   1. Open**Settings** by clickingsettingsor pressing`Ctrl + ,`(on Windows/Linux/ChromeOS) or`Cmd + ,`(on MacOS).
   2. Find the**Firebase Studio: Web Dev Tools** setting and enable it. If you're editing your`settings.json`file directly, you can add`"IDX.webDevTools": true`.
   3. Refresh your browser window to reload yourFirebase Studioworkspace.
2. Open the web preview inFirebase Studio: Open the command palette (`Cmd+Shift+P`on Mac or`Ctrl+Shift+P`on ChromeOS, Windows, or Linux) and select**Firebase Studio: Show Web Preview**.

3. The web console panel is minimized within the web preview panel by default. Click the bar or drag it up to expand it.

The web console panel in theFirebase Studioweb preview works similarly to other consoles, such as the one available in[Chrome DevTools](https://developer.chrome.com/docs/devtools):

- JavaScript errors and`console.log`statements will appear there as you use your app.
  - For errors and warnings, you also have the option to get assistance fromGeminiby selecting the**Understand this error**button at the right of the error message.
- You can evaluate arbitrary JavaScript in the context of your web preview by using the prompt bar at the bottom.

## Run Lighthouse for web previews

[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview)audits your app based on the specific audit categories you select, and returns a report with findings and suggestions. You can run Lighthouse reports directly from the web preview inFirebase Studio.

1. Open the web preview inFirebase Studio: Open the command palette (`Cmd+Shift+P`on Mac or`Ctrl+Shift+P`on ChromeOS, Windows, or Linux) select**Firebase Studio: Show Web Preview**.

2. Click the![image of a speed check icon](https://firebase.google.com/static/docs/studio/images/icons/mono-perf.svg)**Run Lighthouse**icon from the web preview toolbar.

3. ![image of the lighthouse panel in Firebase Studio](https://firebase.google.com/static/docs/studio/images/lighthouse-panel.png)In the Lighthouse panel, select the audit categories you want. You can choose from reports auditing[performance](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring),[accessibility](https://developer.chrome.com/docs/lighthouse/accessibility/scoring),[conformance with best practices](https://developer.chrome.com/docs/lighthouse/best-practices/doctype),[SEO](https://developer.chrome.com/docs/lighthouse/seo/meta-description), and[Progressive Web App performance](https://developer.chrome.com/docs/lighthouse/pwa/load-fast-enough-for-pwa). Click**Analyze page**to generate the reports.

   The reports might take a few minutes to generate.
4. After the reports appear in the Lighthouse panel, you can review the findings for each audit category, or switch between audit categories by clicking the score and category name.

## Use the Debug Console

Firebase Studioincludes the built-in Debug Console from Code OSS. Use this console to debug your app with out-of-the-box debuggers for most common programming languages, or add a debugging extension from[OpenVSX](https://open-vsx.org/?category=Debuggers).

To customize your debugging experience, you can also add a`.vscode/launch.json`file to your workspace and specify custom launch configurations. Learn more about using launch configuration files to customize debugging at[Visual Studio Code debug configuration](https://github.com/microsoft/vscode-docs/blob/main/docs/debugtest/debugging-configuration.md).

## Debug withGemini

You can use Gemini inFirebaseto help you debug your code with chat in your**Code** workspace or theApp Prototyping agent.

WhileGeminican write code for you, it might sometimes also produce errors. When it detects an error, it will attempt to fix it. If you find that it isn't able to resolve the issue given the error message, you can try some of the following techniques:

- **Describe the issue:** In the chat interface, describe the problem you're encountering as clearly and concisely as possible. WhileGeminimight have access to context like error messages and logs, it might not understand the full context. Describing the behavior along with the error message can helpGeminifix errors faster.

- **Ask specific questions:** Don't be afraid to askGeminidirect questions about your code. For example, "What could be causing a null pointer exception in this function?" or "How can I prevent this race condition?"

- **Break down complex problems:** If you're dealing with a complex issue, break it down into smaller, more manageable parts. AskGeminito help you debug each part separately and think through problems step-by-step.

- **Use code fences:** When sharing code snippets, use code fences to ensure that the code is properly formatted. This makes it easier forGeminito read and understand your code.

- **Iterate and refine:** Geminimay not always provide the perfect solution on the first try. Review the responses, ask clarifying questions, and provide additional information as needed.

- **Avoid prompting loops:** IfGeminigets stuck in a loop or is unable to answer your question, try rephrasing your prompt or providing additional context. Sometimes, just rewording your question can helpGeminiunderstand what you're asking.

  If rephrasing your prompt doesn't resolve the loop, try the following techniques:
  - **Start a new chat:** If you're using Gemini inFirebasechat in yourCodeworkspace, start a new chat session to resetGemini's context. This can help break free from any misconceptions or assumptions thatGeminimay have made in the previous conversation.

  - **Provide counter-examples:** IfGeminiis making incorrect assumptions, provide counter-examples to help it understand the correct behavior.