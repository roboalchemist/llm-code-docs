# Source: https://docs.beefree.io/beefree-sdk/other-customizations/advanced-options/display-conditions.md

# Display Conditions

{% hint style="info" %}
This feature is available on Beefree SDK [Core plan](https://developers.beefree.io/pricing-plans) and above. Upgrade a [development application](https://docs.beefree.io/beefree-sdk/getting-started/readme/development-applications) at no extra charge to explore features from higher plan tiers. **Note:** Usage on a development application still counts toward [usage-based fees](https://devportal.beefree.io/hc/en-us/articles/4403095825042-Usage-based-fees) and limits.
{% endhint %}

## How they work <a href="#how-they-work" id="how-they-work"></a>

Display conditions allow you to change the content that is shown to a recipient of an email depending on who the recipient is.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FbWiQ8F1WPxi7FNNr5pcj%2Fdisplay_conditions_row_example_children.png?alt=media&#x26;token=1f5b0019-8284-4ba0-8c73-b3c409477995" alt=""><figcaption></figcaption></figure>

Your users will have the ability to pick a condition (or write one from scratch if they are technically savvy), apply it to a row, and thus show different content based on who the recipient (or viewer) is.

The feature provides a number of benefits, including:

### **Ease of use for email designers**

Display conditions allow anyone that is using the builder to easily create personalized messages without writing a line of code.

### **Any syntax for the conditional statements**

Use whatever syntax your application understands. The feature is language agnostic: it can be used with whatever syntax matches your tech stack. Does your sending engine understand the Liquid markup? Then you can use Liquid. Does it use a proprietary templating language? No problem.

### **User permissions**

Restrict access to some of the functionality based on user roles. For example, some users may be able to edit the syntax of the conditional statements, while others may not. Use this flexibility to simplify the UI or promote upselling.

## Activating and using the feature <a href="#activating-and-using-the-feature" id="activating-and-using-the-feature"></a>

Please note that the Display conditions are **disabled by default.** You can turn this feature on by enabling it under the [Server-side configurations](https://docs.beefree.io/beefree-sdk/server-side-configurations/server-side-options). You must be on a paid plan (Core subscription and above) to enable this feature.

As the application hosting the builder, you can now pass an array of conditions.

```javascript

var rowDisplayConditions = [{
  type: 'Last ordered catalog',
  label: 'Women',
  description: 'Only people whose last ordered item is part of the Women catalog will see this',
  before: '{% if lastOrder.catalog == \'Women\' %}',
  after: '{% endif %}',
}, {
  type: 'Last ordered catalog',
  label: 'Men',
  description: 'Only people whose last ordered item is part of the Men catalog will see this',
  before: '{% if lastOrder.catalog == \'Men\' %}',
  after: '{% endif %}',
}, {
  type: 'Last ordered catalog',
  label: 'Children',
  description: 'Only people whose last ordered item is part of the Children catalog will see this',
  before: '{% if lastOrder.catalog == \'Children\' %}',
  after: '{% endif %}',
}, { ... }]

```

Those conditions become available for users of the editor to select, assuming the feature is turned **on** and the user has permissions to apply a condition to a row.

They will do so by browsing through categories or searching by keyword. For example…

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FizSWMNnAWh7ApRNYDrxn%2F2display_conditions_select_children.png?alt=media&#x26;token=5d39f4ff-d84c-45f2-9be5-6616283f11ed" alt=""><figcaption></figcaption></figure>

The condition that they pick is applied to the row and displayed when the row is selected.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FiPZpv5XBNOzTI3wLaMBh%2F3display_conditions_row_example_children-1.png?alt=media&#x26;token=2bc235be-4c95-406f-ae92-c3f0c95b0f3f" alt=""><figcaption></figcaption></figure>

It can be changed (i.e. the user decides to apply another condition) or edited (if the user has the technical skills to do so, and its user role has been granted those permissions).

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FCslKRMj0KI0go6os53qS%2F4display_conditions_edit.png?alt=media&#x26;token=11792a08-f92d-40f6-aa21-39312b2623da" alt=""><figcaption></figcaption></figure>

When the *Preview* feature is accessed, users can now simulate what recipients in a certain segment will see by toggling *Display conditions* on and off.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FWUo0mv2M3BwEvqy4iJHg%2F5display_conditions_preview_children.png?alt=media&#x26;token=6bd06f2b-1d86-428b-87e4-9d58ef81ca79" alt=""><figcaption></figcaption></figure>

## Display conditions and user roles & permissions <a href="#display-conditions-and-user-roles-permissions" id="display-conditions-and-user-roles-permissions"></a>

When active, the feature is available to all users by default. You can manage who can see and/or do what by leveraging user roles and permissions.

When the feature is ON, new permissions are available for you to configure when you create or edit a Role.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2Fla4VAOpM8yu9pSwAWWin%2FCleanShot%202025-03-13%20at%2014.44.11.png?alt=media&#x26;token=0329f027-33a6-492a-92a6-823b4c98648c" alt=""><figcaption></figcaption></figure>

A basic set up allows you to have 3 user levels:

1. **Can only view & preview**
   * None of the above options are selected
   * No widget will be shown unless the loaded message has display conditions assigned to one or more rows
   * If conditions are applied:
     * They are shown as ready-only
     * They can be applied in the Preview
2. **Can only select**
   * Only Can select conditions option is selected in the role settings (remove will be automatically selected too)
   * The widget shows and the user can select and apply any of the conditions specified in the editor configuration
   * The user cannot add a new condition
   * The user cannot edit a selected condition
3. **Full control**
   * All permissions are selected
   * The user can select and edit conditions (if provided) or add a new condition

**Note:** if there are no Display conditions passed in the configuration, and the user has the rights to access the feature, the editor will only show the Add condition action, which allows users to apply a new condition to a row by manually adding the condition’s syntax.

## Additional information <a href="#additional-information" id="additional-information"></a>

#### Identifying a row with an applied display condition

It’s easy to identify a row to which a display condition has been applied. A bifurcation icon is added to the row’s “Structure” tag, which is shown as you mouse over the row. Here’s an example:

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FfZnWXxXR5CPlvvAd42tP%2F7display_conditions_row_beacon.png?alt=media&#x26;token=b20d7137-ad1d-4022-a4b3-fc8a4904d548" alt=""><figcaption></figcaption></figure>

## Custom conditions

When a default Display condition is edited – by a user that has permissions to do so – it becomes a custom condition. Custom conditions are easy to recognize because:

* A blue dot is added next to the condition’s name
* The “Change condition” button is no longer available: a custom condition can only be removed
* The cancel icon is replaced by a trash button because an edited condition, once remove, is lost: it cannot be re-added.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FBaAnvUmigI8TwGRcocyh%2F8display_conditions_edit_custom.png?alt=media&#x26;token=947bb097-1169-49df-b4bf-0af66924c9ff" alt=""><figcaption></figcaption></figure>

Why these different behaviors for custom conditions? Because Beefree SDK does not save them to the configuration (you passed that configuration to the application: we don’t have access to the repository where you save that information). So, custom conditions do not exist in the array of conditions that the user can search and/or browse.

Reference our [Advanced Permissions documentation](https://docs.beefree.io/beefree-sdk/other-customizations/advanced-permissions#add-condition-and-edit-condition-buttons) to learn more about managing the visibility of the Add Condition and Edit Condition buttons.

## HTML output

Conditional syntax and row content are isolated from each other in the HTML generated by Beefree SDK, so your system can delete, repeat or change elements inside the row without impacting other parts of the message. For example, the HTML of a row might look like this:

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FdSTi03Sm2jbg9yFLBnyp%2F9display_conditions_example_code_html.png?alt=media&#x26;token=54d6d4d2-d513-4df1-a6c8-f850560198ad" alt=""><figcaption></figcaption></figure>

## Extending Display Conditions <a href="#extending-display-conditions" id="extending-display-conditions"></a>

You can extend this feature and allow users of the editor to build their own *Display Conditions*, on the fly, using a UI that you control. It’s part of the [Content Dialog](https://docs.beefree.io/beefree-sdk/other-customizations/advanced-options/content-dialog) functionality. This is an advanced feature that requires some development on the side of the hosting application, but that provides fantastic flexibility. [Check it out!](https://docs.beefree.io/beefree-sdk/other-customizations/advanced-options/content-dialog)

Here is an example of a custom builder of *Display Conditions*.

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FQkEhL5smqOtt0E2loBGR%2F10display.condition.dialog.jpg?alt=media&#x26;token=fe4d478c-1e85-447c-b476-42f20ad29409" alt=""><figcaption></figcaption></figure>

## Sample Code: Display Conditions

Here is a ready-to-run example demonstrating how to integrate the Beefree SDK Display Conditions feature into your application to enable personalized email content that adapts based on recipient attributes.

{% embed url="<https://github.com/BeefreeSDK/beefree-sdk-examples/tree/main/conditional-rows-example>" %}
