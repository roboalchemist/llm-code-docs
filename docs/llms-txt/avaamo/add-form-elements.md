# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-form-elements.md

# Add form elements

You can add form elements to [Card](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-skill-messages-responses#card) responses. You can add the following form elements:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MF4X7Jx975luv0RolFY%2F-MF4XiimquH7YHE7RhaK%2Fdialog-add-form-elements.png?alt=media\&token=00d633f1-3c01-4f6b-b338-15cfdcfc0603)

| Form Element     | Description                                                                       |
| ---------------- | --------------------------------------------------------------------------------- |
| Single line text | Adds a single-line text field in the form.                                        |
| Multi line text  | Adds a multi-line text field in the form. Typically, used for descriptive fields. |
| Number           | Adds a scroll bar at the end of the field to pick a number.                       |
| Date             | Adds a date picker to the form. The default format is MM-DD-YYYY.                 |
| Poll             | Adds radio-button elements in the form.                                           |
| Checklist        | Adds checkbox elements in the form.                                               |
| Picklist         | Adds options in a dropdown list.                                                  |
| Rating           | Adds a 5-star rating field to the form.                                           |

### Key points

Make a note of the following key points related to form elements:

* You can add upto 25 form elements to the card.
* Make a note of the field identifier. You can use this to get the text entered by the user in JS using context.last\_message.<\<ID>>. See [Context](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context), for more information.
* See [Card](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card), for more information on programmatically creating all these form elements in card response with enhanced functionality.

### Example

Consider that you wish to create a registration form in your Pizza agent. This form captures all the details such as first name, date of birth, preferred choices of pizza.

**To create a form**:

* Create a card response in the Flow designer. See Card, for more information.
* Add the required form elements. the following is an example of all the form elements in Card response. Make a note of field identifiers.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MQQduiYNFGyFKzpvyb9%2F-MQQzPNJdA5dhm8iEJqg%2Fdialog-add-form-elements-all.png?alt=media\&token=bd25224a-da32-4791-adf7-23817bd586b5)

* Post a query as specified in the intent to trigger the response. The following form elements as defined in the card response is displayed in the agent:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FHHVB9zHshbVMhiHBfwkU%2Fimage.png?alt=media\&token=91e34efa-d891-40f1-9415-d1548ee72109)

* You can access the form elements to get the text entered by the user in JS using context.last\_message.<\<ID>>. See [Context](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context), for more information.
