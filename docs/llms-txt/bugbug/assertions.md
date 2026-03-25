# Source: https://docs.bugbug.io/editing-tests/assertions.md

# Assertions

## Why add assertions?

Use assertions to **observe** if everything works as it should.&#x20;

An assertion is a check that does not interact with your page, for example, you can check if your page shows a specific text without clicking anything.

{% hint style="info" %}
[Here](https://docs.bugbug.io/recording-tests-steps/recording-assertions) you can read about how to record assertions for a test.
{% endhint %}

## Types of assertions

By default, BugBug records two types of assertions:

1. `Element is visible`
2. `Element has text`

which you can edit later in your recorded test details view, and switch between a wider list of available ones, such as:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FhlpH8pssBgh2cZtE2Hu0%2FAdd_a_new_assertions_step.png?alt=media&#x26;token=f1b3014c-7bfa-41f9-bf49-bebc78b77171" alt=""><figcaption><p>List of available assertions</p></figcaption></figure>

Select one of the following assertion types.

{% hint style="info" %}
We are regularly adding more assertion types to this list - please contact us if you need a new assertion type.
{% endhint %}

| Type of assertion                | What happens                                                                                                                                                                    |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Element is visible               | BugBug checks if the element is actually visible on the screen, if the element is not covered or scrolled outside of the viewport                                               |
| Element is not visible           | BugBug checks if the element isn't visible on the screen                                                                                                                        |
| Element has text                 | BugBug checks if the element is visible, but also checks if it has a specific text                                                                                              |
| Form field has value             | BugBug checks if any form input has a specific value, for example, you can check if your radio buttons group is selected to "No" after the user clicks "No" button              |
| Form input is checked            | BugBug checks if the checkbox is checked. You can claim that your radio button was checked after the user clicked it                                                            |
| Form input is not checked        | BugBug checks if the checkbox is unchecked. You can claim that your radio button was disabled after the user clicked it twice                                                   |
| Page shows specific text         | BugBug checks if there is text anywhere on the page                                                                                                                             |
| Page does not show specific text | BugBug checks if there is no text anywhere on the page. Helpful with negative assertions                                                                                        |
| Page has title                   | BugBug checks the document.title                                                                                                                                                |
| URL address                      | BugBug checks the URL of the page. You can verify that the redirect works fine                                                                                                  |
| Download started                 | BugBug checks if the download process for a selected file has started within the browser *(however, there is no verification that the download has been successful)*            |
| Custom JavaScript                | Run any JS function and if it returns true, the assertion is passed - learn more in [custom javascript actions](https://docs.bugbug.io/editing-tests/custom-javascript-actions) |
| \</> DOM element does exist      | BugBug checks if there is an element on the page you're looking for                                                                                                             |
| \</> DOM element does not exist  | BugBug checks if there is no element on the page you're looking for. Helpful with negative assertions                                                                           |
| Number of elements in DOM        | BugBug checks if there are a certain number of elements on the page you're looking for                                                                                          |
| Variable value                   | BugBug checks if the variable's output value matches the set condition                                                                                                          |

## Editing assertions

By default, BugBug records assertions that are best suited to what you are looking for. But you can also create advanced assertions, such as checking if a number is greater than a certain value. Select options from the drop-down menu to perform a more thorough check of your test case.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FJkhSMNTXhUmenBz2GSA2%2F2_editingAssertions.png?alt=media&#x26;token=600da1c1-6694-40b3-8e28-27b290da78d2" alt=""><figcaption><p>Example of assertion modification after recording</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FajNZqb0nGix1XgOASOPT%2FProjekt%20bez%20tytu%C5%82u%202.png?alt=media&#x26;token=708b7a31-32b3-43ba-aad4-4e4505c29a3d" alt=""><figcaption><p>Values can be confirmed under certain conditions</p></figcaption></figure>

| Assertion                        | Use it when                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Element is visible               | You want to check if an element is visible, meaning that it's in the viewport, opacity is not 0, and its visibility is not set to hidden. For example, you can assert that some error message is shown and visible to the user                                                                                                                                      |
| Element is not visible           | You want to check if an element is in DOM but not visible, meaning that it's not in the viewport or opacity is 0 or its visibility is set to hidden                                                                                                                                                                                                                 |
| Element has text                 | You want to assert the text in an element, for example, if a registration button contains a "`Sign up"` text. This is the most common type of assertion                                                                                                                                                                                                             |
| Form input has value             | You want to check if the value of the form element matches specific conditions. Only works with `form` elements like `input`, `select`, `checkbox`, `radio`, etc.                                                                                                                                                                                                   |
| Form input is checked            | You want to check if a checkbox or radio button is checked, meaning that it is selected, enabled                                                                                                                                                                                                                                                                    |
| Form input is not checked        | You want to check if a checkbox or radio button is unselected, unchecked                                                                                                                                                                                                                                                                                            |
| Download started                 | You want to check whether the download process for a selected file has started from the server. Additional settings for this assertion focus on the file name                                                                                                                                                                                                       |
| Custom JavaScript                | You need to do an advanced assertion, ex. comparing the element text with [variables](https://docs.bugbug.io/editing-tests/variables), making an API request, or using `localStorage`. When your JS function returns `true`, the assertion will be marked as `passed.` Also see [custom JS actions](https://docs.bugbug.io/editing-tests/custom-javascript-actions) |
| \</> DOM element exists          | You want to check if an element exists in the DOM (HTML structure), but not necessarily is visible                                                                                                                                                                                                                                                                  |
| \</> DOM element does not exists | You want to check if an element is not present in the DOM (HTML structure), ex. you want to make sure that some element disappeared completely from the page, and that it's not just set to `"display: none"`                                                                                                                                                       |
| Number of elements in DOM        | You want to check the number of elements that match a given selector, for example, you want to assert that a list shows 10 elements                                                                                                                                                                                                                                 |
| Variable value                   | You want to check if its computed value matches the set condition between: is/is not/contains/does not contain/matches regex                                                                                                                                                                                                                                        |

&#x20;
