# Source: https://docs.avaamo.com/user-guide/release-notes/v5.0-to-v5.8.x-releases/v5.8.x/release-notes-v5.8.0.md

# Release notes v5.8.0

Accessibility is to provide equal access and equal opportunity to people with diverse abilities. This often becomes not only a regulatory requirement in many organizations but also required to facilitate an increase in the adoption of the product to its full potential.&#x20;

The primary focus of the v5.8.0 release is to make accessibility an inclusive capability in the Avaamo Conversational AI Platform agents.

Accessibility capabilities are now built-in in the Avaamo Conversational AI Platform agents, hence:

* Organizations can accelerate the adoption of the agents.
* It is easier to access and use the Avaamo agents, irrespective of the diverse abilities, or even in the absence of a mouse.

{% embed url="<https://youtu.be/DxXuwgKsU0Q>" %}

## Accessibility readiness

This release ensures that all the UI elements in the Header, Conversation body, and the Message area of the Avaamo Conversational AI Platform agents are **Accessibility ready**. Your agents now have inclusive accessibility capability right from launching the agents to the process of carrying out a complete conversation flow with your agents until you exit from the agents.

For example, in the following illustration, you can view a comparison of the agent UI in the previous and the current release. In the agent with accessibility, you can view, few key enhancements incorporated for accessibility in this release:

* **Keyboard navigation**: Highlighted with outlines and color contrast to indicate keyboard focus in the Message area of the agent.
* **Color contrast**: High color contrast in the header, conversation body, and the message area

  to ensure that the viewers who cannot see the full-color spectrum are able to read the text.&#x20;
* **Highlighted links**: Close button and Quick reply button links are highlighted for better accessibility.
* **Text and Spacing**: Larger text and better text spacing in the header, conversation body, and the message area of the agent for better accessibility.

|                                                                                                                                  Previous                                                                                                                                 |                                                                                                                            With Accessibility                                                                                                                            |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MjcON8HIUhjKQGh5pMS%2F-Mjc_x-I2Tq1lf_czmVe%2F5.8-rn-before.png?alt=media&#x26;token=6d5687a2-a691-47c6-af07-b55e9bcea355" alt="" data-size="original"> | <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MjceBtuGZVU9Er7ufD5%2F-MjcfH5kR1LG76pqeMHx%2F5.8-rn-after.png?alt=media&#x26;token=06a4742b-daed-4ed7-bdca-da685ce08032" alt="" data-size="original"> |

## Accessibility enhancements

As a part of accessibility readiness based on WCAG 2.0 (Web Content Accessibility Guidelines), this release includes enhancements in the following areas:

* [Keyboard navigation](#keyboard-navigation)
* [Focus management](#focus-management)
* [Screen reader](#screen-reader)
* [Contextually accessible names](#contextually-accessible-names)
* [Status message](#status-message)
* [Color contrast](#color-contrast)

### Keyboard navigation

Keyboard accessibility is one of the most important aspects of web accessibility. In the release, the following are the keyboard accessibility enhancements in the Avaamo Conversational AI Platform agents:

* All the UI elements in the Header, Conversation body, and the Message area of the agents are accessible with the keyboard.
* Users can navigate the Conversation history by using up/down arrow keys
* Users can access and move between links, buttons, forms, and other controls using the Tab key and other keystrokes.
* The keyboard navigation order is logical and intuitive. The tab order follows the visual flow of the agent: left to right, top to bottom.
* Outlines and color contrast indicate keyboard focus.

Few main functions (but not limited to) in the Avaamo Conversational AI Platform agents that are made available with keyboard include -`Agent widget icon, Agent response, Persistent menu, Send button, Auto-complete, Close chat element, Live agent hyperlinks, and Feedback icons.`&#x20;

The following illustration depicts how keyboard navigation with tab, outlines and highlights the Persistent menu in the agent:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fgkcy31wYlyAYP6FjmcET%2Fimage.png?alt=media\&token=7de05ab5-119e-4b17-be86-3cfd77f9e433)

Another example is where the user can navigate the Conversation history by using up/down arrow keys.

### Focus management

The concept of focus management is important in understanding how assistive technologies handle announcing elements in the DOM. In the release, the following are the accessibility enhancements in the Avaamo Conversational AI Platform agents with respect to "Focus management":

* Users can navigate all the UI elements in the agents with the keyboard using `tab` and `shift + tab` and a few arrow key combinations with a proper outline and visible focus state.
* For the HTML elements such as links, buttons where the focus is implicitly available, the focus is logical and preserved
* For the non-focusable elements such as div, h1-h6 tags, the focus is preserved using ARIA labels in all such UI elements of the agent.

Few main functions (but not limited to) in the Avaamo Conversational AI Platform agents that are enhanced with focus include - `Open agent, Send message textbox, Disambiguation options, Hyperlinks, Persistent menu options, Agent logo, Agent minimize button, Auto-complete, and Feedback.`

The following illustration depicts how the focus is preserved in the Persistent menu of the agent:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mjd-An0OYU6Hi5ylzB5%2F-Mjd68R_sXkdc0F4jKbV%2FAccessibility.gif?alt=media\&token=fb76d41d-71bc-416f-866f-54e36aaeea2c)

### Screen reader

A Screen reader is a gesture-based reader that enables people to experience the interface on their devices without having to see the screen.&#x20;

As a part of **Accessibility readiness**, all the UI elements in the agents have been enhanced to include appropriate accessible names, labels, and roles. You can now enable screen readers in your devices and the agents use this capability to read it out using screen readers. See [Contexually accessible names](#contextually-accessible-names), for more information.

### Contextually accessible names

An [accessible name](https://www.w3.org/TR/accname-1.1/) is a name that assistive technologies use to identify an element on the agent to users. Example: **alt** attribute in the **img** HTML tag is used by the screen readers to announce the image.

In the release, all the UI elements in the Header, Conversation body, and the Message area of the agents are enhanced to use WAI-ARIA (Web Accessibility Initiative – Accessible Rich Internet Applications) has been used wherever applicable to provide better accessibility. The primary focus of this release with respect to "Accessible Name and Description" is to:

* Provide contextually accessible names to all the UI elements in the agent
* Provide contextually accessible labels to all the UI elements in the agent
* Provide an accessible role for each UI element&#x20;
* Provide and maintain accurate states and values for each UI element:&#x20;

The following lists a few examples:

* `aria-label` or `aria-labelledby` attributes are added to the `link` tag, `minimize` buttons
* Added appropriate role on UI elements such as ComboBox, TextArea
* `alt` attribute is added to the `img` tag

### Status message

According to the WCAG glossary, the formal [definition of a status message](https://www.w3.org/TR/WCAG21/#dfn-status-messages) is "a change in content that is not a change of context, and that provides information to the user on the success or results of an action, on the waiting state of an application, on the progress of a process, or on the existence of errors."

Assistive technology users must be able to detect when important changes occur on the agents. This can be when the user is waiting for the agent to load, or when the user is waiting for the agent to respond.

In the release, the following are the accessibility enhancements in the Avaamo Conversational AI Platform agents with respect to "Status messages":

* The loading animation such as the agent loading animation does not last more than five seconds.
* If any loading animation lasts more than five seconds then information is provided to the user on the success or results of an action.
* All the content in the agent is announced to screen readers when it appears on the screen so that the users are notified about such updates for example,&#x20;
  * Screen reader users are informed that their feedback has been submitted.
  * Information on the status of the form’s submission is announced to screen readers.
  * Agent unavailability, if any, say due to a lost internet connection is announced to screen readers.
  * Inform status to the user when the user query is sent to the agent.
  * Inform status to the user when a new reply is received from the agent.

### Color contrast

As per the accessibility guidelines, text and interactive elements must have a color contrast ratio of at least 4.5:1. This means that there is enough contrast between text and its background so that it can be clearly read by people even with moderately low vision.

In the release, color contrast is available for all the UI elements in the Header, Conversation body, and the Message area of the agents. This ensures that viewers who cannot see the full-color spectrum are able to read the text. The following illustration depicts few examples of the color contrast in agents with accessibility:

|                                                                                                                       <p>Previous release  </p><p>No Contrast</p>                                                                                                                       |                                                                                                                                   High Contrast                                                                                                                                  |                                                                                                                                   Desaturate                                                                                                                                  |                                                                                                                                   Invert                                                                                                                                  |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MjcfqvE7J0g4pBeHRfk%2F-Mjchl3A6Lx0WWQmv5Z1%2F5.8-rn-no-contrast-previous.png?alt=media&#x26;token=2e1817fd-f9fd-41fd-b616-14b1d668bb75" alt="" data-size="original"> | <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MjcfqvE7J0g4pBeHRfk%2F-Mjci2EzkLsPU1dOlH1f%2F5.8-rn-high-contrast.png?alt=media&#x26;token=ed36528f-16a2-463a-94a5-72dc257e8a15" alt="" data-size="original"> | <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MjcfqvE7J0g4pBeHRfk%2F-MjciD6lruz8fkpzt8ho%2F5.8-rn-desaturate.png?alt=media&#x26;token=d0e43c11-2415-4355-b941-2152575cfe4c" alt="" data-size="original"> | <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MjcfqvE7J0g4pBeHRfk%2F-MjciUJMyJrcR3hessEA%2F5.8-rn-invert.png?alt=media&#x26;token=caad9e5a-3aaa-49e9-a8cd-0aacddf0f05e" alt="" data-size="original"> |
