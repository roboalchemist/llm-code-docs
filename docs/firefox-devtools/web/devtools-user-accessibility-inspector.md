# Source: https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector

Title: Accessibility Inspector — Firefox Source Docs documentation

URL Source: https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector

Published Time: Thu, 12 Mar 2026 22:04:46 GMT

Markdown Content:
The Accessibility Inspector provides a means to access important information exposed to assistive technologies on the current page via the accessibility tree, allowing you to check what’s missing or otherwise needs attention. This article takes you through the main features of the Accessibility Inspector and how to use it.

A (very) brief guide to accessibility[](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector#a-very-brief-guide-to-accessibility "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Accessibility is the practice of making your websites usable by as many people as possible. This means trying your best to not lock anyone out of accessing information because of any disability they may have, or any other personal circumstances such as the device they are using, the speed of their network connection, or their geographic location or locale. You can find more extensive information in the [Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility) section of MDN Web Docs.

Here we are mainly talking about exposing information to people with visual disabilities — this is done via the [accessibility APIs](https://www.smashingmagazine.com/2015/03/web-accessibility-with-accessibility-api/) available inside web browsers, which expose information on what roles the different elements on your page play (e.g., are they just text, or are they buttons, links, form elements, etc.?).

Semantic DOM elements have roles assigned to them by default that hint at what their purpose is. Sometimes, however, you need to use some non-semantic markup (e.g., [div](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div) s) to build a complex custom control, and the control won’t have a default role that reflects its purpose. In such a situation, you can use [WAI-ARIA](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/WAI-ARIA_basics) role attributes to provide your own roles.

Roles and other information exposed by browser accessibility APIs are presented in a hierarchical structure called the accessibility tree. This is a bit like the DOM tree, except that it contains a more limited set of elements and slightly different information about them.

Assistive technologies like screenreaders use this information to find out what’s on a web page, tell their users what’s there, and enable them to interact with the page. The Accessibility Inspector also uses this information to provide valuable accessibility debugging capabilities in the DevTools.

Accessing the Accessibility Inspector[](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector#accessing-the-accessibility-inspector "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When you first open any of the other Developer Tools, the accessibility features are turned off (unless you’ve already got them turned on in another browser tab, or got the Firefox accessibility engine started already, e.g., you might be a screenreader user or tester).

The accessibility inspector is automatically enabled when you do one of the following:

*   Choose **Accessibility** in the **Tools > Browser Tools** menu.

*   Select the **Accessibility** tab in the Developer Tools toolbox.

*   Right-click in the main browser window, and choose **Inspect Accessibility Properties** in the context menu.

*   Right-click an item in the HTML pane of the [Page Inspector](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/index.html), and choose **Show Accessibility Properties** in the context menu.

Once activated, the accessibility engine remains running until you close the Developer Tools toolbox.

Note

The accessibility engine runs in the background when the accessibility features are turned on. When enabled it may affect the metrics from other panels such as [Memory](https://firefox-source-docs.mozilla.org/devtools-user/memory/index.html) and [Performance](https://firefox-source-docs.mozilla.org/devtools-user/performance/index.html), and have some impact onoverall browser performance.

If you don’t wish to allow the accessibility features to be automatically enabled, you can use the [Configuration Editor](https://support.mozilla.org/en-US/kb/about-config-editor-firefox) (also known as `about:config`) to define the preference `devtools.accessibility.auto-init.enabled`, and set it to `False`.

If you don’t wish to use the accessibility features at all, you can use the [Configuration Editor](https://support.mozilla.org/en-US/kb/about-config-editor-firefox) to set the preference `devtools.accessibility.enabled` to `False`. If you do this, the methods listed above for activating the Accessibility Inspector do nothing.

Features of the Accessibility panel[](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector#features-of-the-accessibility-panel "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The enabled accessibility panel looks like so:

![Image 1: Shows issue checker toolbar with "contrast" and "text label" options](https://firefox-source-docs.mozilla.org/_images/accessibility-inspector-tabbing_order.png)
On the left-hand side, there is a tree diagram representing all the items in the accessibility tree for the current page. Items with nested children have arrows that can be clicked to reveal the children, so you can move deeper into the hierarchy. Each item has two properties listed:

*   _Role_ — the role this item has on the page (e.g., `pushbutton`, or `footer`). This can be either a default role provided by the browser, or a role given to it via a WAI-ARIA `role` attribute.

*   _Name_ — the name this item has on the page. The name depends on the element; for example, the name of most text elements is their `textContent`, whereas form elements’ names are the contents of their associated [label](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label).

On the right-hand side, you can see further information about the currently selected item. The listed properties are as follows:

*   _name_ — the item’s name, as described above.

*   _role_ — the item’s role, as described above.

*   _actions_ — a list of actions that can be performed on the item, for example, a pushbutton would have “Press” listed, while a link would have “Jump” listed.

*   _value_ — the value of the item. This can mean different things depending on the type of the item; for example, a form input (role: entry) would have a value of whatever is entered in the input, whereas a link’s value would be the URL in the corresponding `<a>` element’s `href`.

*   _DOMNode_ — the type of DOM node that the item in the accessibility tree represents. You can click on the “target” icon that comes after it to select the node in the [Page Inspector](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/index.html). Hovering over the “target” icon highlights the DOM node in the page content.

![Image 2: DOMNode property in accessibility inspector with target icon highlighted](https://firefox-source-docs.mozilla.org/_images/dom-node-target-icon.png)
*   _description_ — any further description provided on the element, usually by the content of a title attribute.

*   _keyboardShortcut_ — any keyboard shortcut that is available to activate the element, as specified in an `accessKey` attribute.

*   _childCount_ — the number of child items the current item has in the accessibility tree hierarchy.

*   _indexInParent_ — an index value indicating what number child the item is, inside its parent. If the item is the first item inside its parent, it has a value of 0. If it is the second, it has a value of 1. And so on.

*   _states_ — a list of the different accessibility-relevant states that can apply to the current item. For example, one of the links in one demo has states of focusable, linked, selectable text, opaque, enabled, and sensitive. For a full list of internal states, see Gecko states.

*   _relations_ — a list of the accessibility-relevant relationships between this item and other items. For example, in a form, an entry item could have a “labelled by” relation with a label item, which in turn has a “label for” relation to the entry item.

*   _attributes_ — a list of all the accessibility-relevant attributes that are applied to the item. This can include style-related attributes such as margin-left and text-indent, and other useful states for accessibility information, such as draggable and level (e.g., what heading level is it, in the case of headings). For a full list of possible attributes, see Gecko object attributes.

Note

The exposed information is the same across all platforms — the inspector exposes Gecko’s accessibility tree, rather than information from the platform accessibility layer.

### Keyboard controls[](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector#keyboard-controls "Link to this heading")

The _Accessibility_ tab is fully keyboard-accessible:

*   You can tab between _Check for Issues_, _Simulate_, _Show tabbing order_, and left and right panels.

*   When one of the panels is focused, you can move the focus up and down items using the up and down arrow keys, and use the left and right arrow keys to expand and collapse expandable rows (e.g., different hierarchy levels of the accessibility tree).

### Print accessibility tree to JSON[](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector#print-accessibility-tree-to-json "Link to this heading")

You can print the contents of the accessibility tree to JSON by right-clicking on an entry in the Accessibility tab and selecting **Print to JSON:**

![Image 3: Print to JSON right-click menu in left panel](https://firefox-source-docs.mozilla.org/_images/accessibility-inspector-print_tree_to_json.png)
When you do, you will get a new tab with the selected accessibility tree loaded into the JSON viewer:

![Image 4: Accessibility tree loaded in new tab JSON viewer](https://firefox-source-docs.mozilla.org/_images/accessibility_json.png)
Once opened, you can save or copy the data as necessary. The JSON viewer can also show you the raw JSON data on a separate tab in the viewer.

### Show web page tabbing order[](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector#show-web-page-tabbing-order "Link to this heading")

People who are unable to navigate a page with the mouse or a trackpad can use the tab key to toggle through focusable items on the page (i.e. buttons, links, form controls).The order that items are focused is one of the most important aspects of web accessibility, as it allows keyboard users to properly navigate a web page — if the tab order is incorrect, the page may be confusing!

Firefox can enable a visual overlay showing the tabbing order. This provides a high-level overview of how the page will be navigated using the tab key, which may highlight problems more effectively than tabbing through the elements. The overlay is toggled on/off using the**Show Tabbing Order** checkbox.

![Image 5: Accessibility inspector and page with checkbox Show tab order selected.](https://firefox-source-docs.mozilla.org/_images/accessibility-inspector-show_tab_order.png)
All focusable items have a numbered marker and the currently focused item is highlighted in a different color. In some cases the marker may be hidden by other elements, as is true for items 1 and 2 in the page below.

![Image 6: A page where some of the markers for selection items are hidden](https://firefox-source-docs.mozilla.org/_images/accessibility-inspector-hidden_items.png)
These become visible in the overlay when the item is the current item.

![Image 7: Shows a hidden selection item in the tabbing order overlay when it is selected.](https://firefox-source-docs.mozilla.org/_images/accessibility-inspector-hidden_item_revealed.png)

Note

The overlay reflects the tab order at the time that the checkbox is selected (i.e. it is not dynamic). If a user does anything that adds items to the tab order (e.g. opens a visual element that contains more links), these new items will not be reflected in the overlay until the Accessibility Inspector is re-launched.

### Check for accessibility issues[](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector#check-for-accessibility-issues "Link to this heading")

You can check for accessibility issues by clicking the drop-down menu next to: **Check for issues**. The available menu items include:

*   **None** — Don’t show the possible list of issues.

*   **All Issues** — Check for all types of issues.

*   **Contrast** — Check for [issues with visual contrast.](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Understanding_WCAG/Perceivable/Color_contrast)

*   **Keyboard** — Check for [issues with navigating via a keyboard.](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Understanding_WCAG/Keyboard)

*   **Text Labels** — Check for [issues with missing text labels.](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Understanding_WCAG/Text_labels_and_names)

When you select one of the menu items, Firefox scans your document for the type of issues you selected. Depending on the size and complexity of your document, this may take a few seconds. When the scan is complete, the left side of the Accessibility Inspector panel displays only the items that have that type of issue. In the right side of the panel, the _Checks_ subpanel lists the specific issue with the selected node. For each type of issue, there is a **Learn more** link to further information on _MDN Web Docs_ about the issue.

![Image 8: Accessibility Inspector - Showing the options when you select the Check for Issues button](https://firefox-source-docs.mozilla.org/_images/accessibility-inspector-check_for_issues.png)
The menu items act as toggles. Select the item to view that type of issue; select the item again to clear the display of issues of that type.

Issues with a particular item are always displayed in the _Checks_ subpanel as you browse the tree. The **Check for issues** menuitems are a quick way to view all and only those items that have issues.

### Simulate[](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector#simulate "Link to this heading")

The Accessibility Inspector offers, a [simulator](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector/simulation/index.html) that lets you see what a web page would look like to users with various forms of _color vision deficiency_ (better known as “color blindness”), as well as _contrast sensitivity loss_.

Typical use cases[](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector#typical-use-cases "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

The Accessibility Inspector is very useful for spotting accessibility problems at a glance. For a start, you can investigate items that don’t have a proper text equivalent — images without `alt` text and form elements without proper labels have a `name` property of `null`, for example.

![Image 9: A form input highlighted in the UI, with information about it shown in the accessibility inspector to reveal that it has no label — it has a name property of null](https://firefox-source-docs.mozilla.org/_images/use-case-no-label.png)
It is also very handy for verifying semantics — you can use the _Inspect Accessibility Properties_ context menu option to quickly see whether an item has the correct role set on it (e.g., whether a button is really a button, or a link is really a link).

![Image 10: A UI element that looks like a button, with information about it shown in the accessibility inspector to reveal that it isn't a button, it is a section element. It has a name property of null](https://firefox-source-docs.mozilla.org/_images/use-case-fake-button.png)
See also[](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector#see-also "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------

*   [Accessibility tutorials](https://developer.mozilla.org/en-US/docs/Learn/Accessibility)

*   [Web accessibility overview](https://developer.mozilla.org/en-US/docs/Web/Accessibility)

*   [Practical debugging information](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Cross_browser_testing/Accessibility)

*   [Understanding WCAG](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Understanding_WCAG)

*   [WAI-ARIA basics](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/WAI-ARIA_basics)

*   [Accessibility APIs: A Key To Web Accessibility](https://www.smashingmagazine.com/2015/03/web-accessibility-with-accessibility-api/) by Léonie Watson
