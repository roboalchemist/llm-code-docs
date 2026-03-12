# Source: https://docs.tokens.studio/figma/dev-mode.md

# Dev Mode in Figma

## Dev Mode in Figma

Tokens Studio for Figma is integrated with Figma's [Dev Mode](https://www.figma.com/dev-mode/), allowing developers to view and copy the names of Design Tokens applied with the Tokens Studio Plugin.&#x20;

[→ Read Figma's guide on Dev Mode for more details on this feature and their licence requirements.](https://help.figma.com/hc/en-us/articles/15023124644247-Guide-to-Dev-Mode)

Once the Plugin is connected to your Dev Mode account, you can select `Tokens Studio` as a programming language option to view the data from the Plugin attached to the layers you are currently inspecting in Dev Mode.&#x20;

{% hint style="info" %}
This setting is saved to your Figma user account.&#x20;

This means each person on your team using Dev Mode will need to enable the Plugin from their individual Figma account.&#x20;
{% endhint %}

### Add Tokens Studio to Dev Mode

From any Figma file, toggle to Dev Mode using the action at the bottom toolbar or use the keyboard shortcut shift + D.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Ft0LbY7dCELFFa0aLE7c2%2FtoggleDevMode-V2-4-1.png?alt=media&#x26;token=3c2095e5-656d-4392-be29-d63b0651ecbf" alt=""><figcaption><p>A Figma file shows the Dev Mode button annotated at the bottom center of the screenshot. </p></figcaption></figure>

From the Dev Mode panel, select the plugin tab on the top right of the Figma UI.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FfOXbgmDeYCIYsXt9X9Cp%2Fswitched-to-DevMode-V2-4-1.png?alt=media&#x26;token=d83c984f-2930-4cc6-977a-a530f2dddba6" alt=""><figcaption><p>A Figma file in Dev Mode is shown with the Plugin Tab annotated at the top right of the screenshot. </p></figcaption></figure>

Use the search feature (underneath the Plugin tab) to look for `Tokens Studio for Figma`.

Select the icon button with the ribbon symbol on the right side of the Plugin name to save it to your Figma account.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FcYD7gr1IaBqYaD3ZSmLq%2Fribbon-to-savePlugin-V2-4-1.png?alt=media&#x26;token=6add6629-3703-41b3-8fca-9376f6099513" alt=""><figcaption><p>A Figma file in Dev Mode is shown with the Plugin Tab annotated at the top right of the screenshot. The words "tokens studio for figma" are entered in the search input, and the ribbon symbol icon button with the label "save" is annotated.  </p></figcaption></figure>

### Viewing Tokens Studio Data in Dev Mode

Once the Plugin has been saved to your Dev Mode account, you can view Design Tokens applied to design elements by the Tokens Studio Plugin.&#x20;

\
From any Figma file, toggle to Dev Mode using the action at the bottom toolbar or use the keyboard shortcut shift + D.

* Navigate to the Inspect Tab in Dev Mode.&#x20;
* Find the Programming Language selector and choose `Tokens Studio`.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F0Zc93MvwNXi0RT9GIA29%2Fselect-TS-asLanguage-V2-4-1.png?alt=media&#x26;token=15ff5b64-088b-4b68-abcd-974413b1b815" alt=""><figcaption><p>A Figma file in Dev Mode is shown with on the Inspect Tab, located at the top right of the screenshot. The programming language select input is open, with Tokens Studio for Figma as the new option is highlighted. </p></figcaption></figure>

On the Figma canvas, select the specific layer you'd like to view.&#x20;

The names of any Tokens applied to that layer with the plugin will appear in the Dev Mode panel where code is displayed.&#x20;

{% hint style="info" %}
Figma can only show Tokens applied to one layer at a time. \
To view any Tokens applied to children layers, you need to select those layers individually.&#x20;
{% endhint %}

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F75WtktY9H6nRAz6ymbHh%2FselectFrame-to-displayTokens-in-devMode-V2-4-1.png?alt=media&#x26;token=5b6f6ac6-65c8-4fc5-a16a-c22eb768b356" alt=""><figcaption><p>A Figma file in Dev Mode is shown with on the Inspect Tab, located at the top right of the screenshot. The programming language is set to Tokens Studio for Figma. A card component has been selected on the Figma canvas, and several design token names appear next to the properties in the code display pannel on the right of the interface. </p></figcaption></figure>

If desired, you can use Figma's copy button to capture all Token Names appearing in Dev Mode to your clipboard to you can paste them elsewhere.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FUjxgxzu5dFyLMCkNMGa4%2FcopyTokens-in-devMode-V2-4-1.png?alt=media&#x26;token=196088a2-6f06-43d7-936d-78d68ee9fc3f" alt=""><figcaption><p>A Figma file in Dev Mode is shown with on the Inspect Tab, located at the top right of the screenshot. The programming language is set to Tokens Studio for Figma. A card component has been selected on the Figma canvas, and several design token names appear next to the properties in the code display pannel on the right of the interface. The copy code action is annotated. </p></figcaption></figure>

{% hint style="info" %}
A community plugin was created by Azmy Hanifa which allows you to see more Tokens in Dev Mode!\
→ [Tokens Studio Tree Inspector](https://www.figma.com/community/plugin/1507929423982882409/tokens-studio-tree-inspector)
{% endhint %}

***

### Resources

Mentioned in this guide:

* Figma Learn - [Guide to Dev Mode](https://help.figma.com/hc/en-us/articles/15023124644247-Guide-to-Dev-Mode)

#### Community resources:

* Figma Dev Mode Plugin by Azmy Hanifa - [Tokens Studio Tree Inspector](https://www.figma.com/community/plugin/1507929423982882409/tokens-studio-tree-inspector)

💡 Something to share? [Submit it here!](https://feedback.tokens.studio/)

#### Known issues and bugs

Tokens Studio Plugin GitHub - [Open issues for Figma Dev Mode](https://github.com/tokens-studio/figma-plugin/labels/Figma%20dev%20mode)

🐞  If you are experiencing an issue not listed here, please reach out to us on the Troubleshooting channel of our [community Slack](https://tokens.studio/slack), [submit it on our feedback tool](https://feedback.tokens.studio/), or send us an email <support@tokens.studio>

#### Requests, roadmap and changelog

* Enhance data in Dev Mode - [Feature Request](https://feedback.tokens.studio/p/enhance-data-in-dev-mode)

💌  Visit [https://feedback.tokens.studio/ ](https://feedback.tokens.studio/)to contribute or subscribe to updates.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>
