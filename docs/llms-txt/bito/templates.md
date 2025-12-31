# Source: https://docs.bito.ai/ai-code-reviews-in-ide/templates.md

# Templates

Templates help you improve your code quality instantly with AI-powered analysis. Get automated suggestions for performance optimization, security fixes, style improvements, and code cleanup without leaving your editor. Each template provides actionable feedback and ready-to-use code improvements that you can review and apply with a single click.

## Available templates

1. **Performance Check:** Optimize code performance and efficiency
2. **Security Check:** Identify and fix security vulnerabilities
3. **Style Check:** Apply coding style and formatting standards
4. **Improve Readability:** Enhance code clarity and organization
5. **Clean Code:** Remove debugging and logging statements

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FSUfmpzVe0yq0ea7e9lj4%2Fscrnli_Q8Y7M7221K22CC.png?alt=media&#x26;token=a7bbc8bb-2a88-49f0-8a79-84b562537e09" alt=""><figcaption><p>Templates menu in Bito Panel</p></figcaption></figure>

## How to use templates

### Prerequisites

Select the code you want to analyze in your editor before using any template.

### Method 1: Click Templates button

1. Select code in your editor
2. Click the **Templates** button at the bottom of the Bito extension panel

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FIlm54ABFlep53SbO7Msl%2Fscrnli_LBZSDOD5kJEFCP.png?alt=media&#x26;token=152de194-82c8-438c-bad4-324a3dbfd330" alt=""><figcaption></figcaption></figure>

3. Choose the desired template from the dropdown menu

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FTmv57b2zTSu8ICeeNCm3%2FScreenshot%202025-09-24%20102702.png?alt=media&#x26;token=09ada6e2-347c-4acf-828d-29b42d66c6b0" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Quick navigation:** Use arrow keys, Tab, or Shift+Tab to navigate the template menu
{% endhint %}

### Method 2: Open context menu

1. Select code in your editor
2. Right-click in the editor window
3. Hover over "Bito AI" in the context menu
4. Select the desired template from the submenu

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Ffyd1ApBur9JzmIeIXXhN%2Fscrnli_yY9qlUNuqjsgEE.png?alt=media&#x26;token=a2a29dae-a4b3-4690-bbfc-87d912e74343" alt=""><figcaption></figcaption></figure>

### Method 3: Using slash `/` command in Bito chat box

1. Select code in your editor
2. Type `/` at the start of the Bito chat box
3. Choose the desired template from the dropdown menu

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fy6oQkPh1vEw2JhTJ6MnW%2Fscrnli_JtdylGOpPjV88Q.png?alt=media&#x26;token=5f92dbcd-0d01-48f3-bf3d-85beb34b2c50" alt=""><figcaption></figcaption></figure>

4. Type some text after the slash `/` to filter templates by name

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FkEoCYacM81CVY5qJdJdv%2Fscrnli_2L9qhV0bMjXexI.png?alt=media&#x26;token=447a8882-685e-4b98-a6e6-f574f57ec032" alt=""><figcaption></figcaption></figure>

### Method 4: Command Palette (VS Code)

1. Select code in your editor
2. Go to View → Command Palette (or press Ctrl+Shift+P / Cmd+Shift+P)
3. Type "bito" to see available templates
4. Select the desired template from the list

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FCVbZKpLylmEiUkPkVzFG%2Fscrnli_N85cjZ9T9Km35L.png?alt=media&#x26;token=5929d7f7-811f-4277-bc82-b5996fab2dbb" alt=""><figcaption></figcaption></figure>

## Applying code suggestions

When templates provide code improvements, you'll see an **Apply** button above the suggested code snippet.

1. Click the **Apply** button to open the diff view

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FrCdkW4vw2G9iBry12rvj%2Fscrnli_1kuwzDuJ2KtDkM.png?alt=media&#x26;token=ba3f30a3-86b8-4d57-8a58-6f9e20d10bcf" alt="" width="402"><figcaption></figcaption></figure>

2. Review the changes highlighted in the diff:
   * Red lines show code to be removed
   * Green lines show code to be added
3. Choose your action:
   * **Accept** - Apply the suggested changes to your code
   * **Undo** - Reject the changes and keep your original code

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F8HNiIQgoLELP1LQ1uSrT%2Fscrnli_JoOQ87pEpkZgyu.png?alt=media&#x26;token=f9ffdfad-6762-428b-95eb-5a73c6607d4f" alt=""><figcaption></figcaption></figure>

## Tips

* Select meaningful code blocks for better analysis results
* Templates work best with complete functions or logical code segments
* Review suggested changes before applying them to your codebase
* Verify that the changes don't break existing functionality
* Use multiple templates on the same code for comprehensive analysis
* Use the diff view to understand exactly what changes will be made
