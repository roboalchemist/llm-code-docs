# Source: https://docs.buildnatively.com/guides/integration/contacts.md

# Source: https://docs.buildnatively.com/natively-platform/features/contacts.md

# Bottom Bar

### How the Bottom Bar feature works

The Bottom Bar automatically appears in your app upon launch when this option is enabled. If you link tabs to pages requiring login, logged-out users will encounter a standard workflow (e.g., redirection to a login page within the tab) instead of seeing the page content.

Tabs function like browser tabs, remembering their navigation state. If a user navigates from a tab's linked page to another page within the app, the tab will display the last visited page, not the original linked page. This behavior persists even when switching between tabs.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FEAKSBo0I4Z9EY8sf4Oga%2Fbottom_bar_example.png?alt=media&#x26;token=8518bd5f-66f5-4ed2-8a19-e244a5d2c558" alt=""><figcaption></figcaption></figure>

### Setting up the Bottom Bar

Turn on the **Bottom Bar** feature and set colors:

* Bottom Bar Background Color - sets the background color of the bar.
* Icon / Label Default Color - sets the color of inactive tab icons and labels.
* Icon / Label Active Color - sets the color of the active tab icon and label.
* Icon / Label Active Background Color - sets the background color of the active tab.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FPYtG0dFgtVrvsBFggZ1r%2Fbottom_bar_colors.png?alt=media&#x26;token=f88cbbfc-2873-4e28-b9d6-5f7b7eb5e18c" alt=""><figcaption></figcaption></figure>

Configure **options**:

* Haptic Feedback - enables haptic feedback when tapping tabs.
* Show Icons - show or hide tab icons.
* Show Labels - show or hide tab labels.
* Show on launch - when this option is disabled, the bottom bar will not automatically appear when the app is launched. You can then display it later by using the 'Show bottom bar' action.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FdrlIF9vDvmHRIaa7klpQ%2Fbottom_bar_options.png?alt=media&#x26;token=8a8dc0dd-8a09-49f8-9baa-c7844fc0a8ee" alt=""><figcaption></figcaption></figure>

### Configuring tabs

You can add up to 5 tabs to the bottom bar.

1. Enter a label in the input field and click 'Add'. This creates a new tab with customizable settings. The label will be enclosed in quotation marks automatically, but these won't be visible in your app.
2. Assign a number from 0 to 5 to determine the tab's position in the bar. Tabs are arranged based on these numbers.
3. Enter the URL the tab should link to. This URL will also be enclosed in quotation marks automatically, but they won't be visible in your app.
4. Provide an SVG icon for the tab.
5. Click 'Save Tab' to apply your changes.

{% hint style="info" %}
All fields (Label, Order, URL, and Icon) are required. If any field is missing or invalid, the tab will not appear in the Bottom Bar.
{% endhint %}

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FajfCCWcZq8mv3vdm7uoy%2Fbottom_bar_tabs_settings.png?alt=media&#x26;token=3318cc6c-a6fc-4b45-9cc2-3cbcd9f782b9" alt=""><figcaption></figcaption></figure>

### Edit tabs

You can change the Label, Order, URL, and Icon of each tab. Remember to save any changes by clicking the 'Save Tab' button.&#x20;

To change the icon, first delete the existing one by clicking the 'Trash' icon. This will reveal the 'Upload icon' button.

To delete a tab entirely, click the 'Delete Tab' button. You can then add a new tab if needed.

### Apply chages to the app

To apply the changes to your app, save the settings and rebuild your app.

### How to use the Bottom Bar?

{% content-ref url="../../guides/integration/bottom-bar" %}
[bottom-bar](https://docs.buildnatively.com/guides/integration/bottom-bar)
{% endcontent-ref %}
