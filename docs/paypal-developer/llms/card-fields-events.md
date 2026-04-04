# Subscribe to Card Field Events for Customization

## Information
This JavaScript SDK documentation uses the CardFields component. If you are integrated with the legacy HostedFields component, see [Hosted Field Events](/docs/checkout/advanced/customize/card-fields/v1/events/).

## Subscribe to events

Subscribe to advanced credit and debit card payment events using an event listener. Event listeners can help you update the UI of your form based on the state of the fields.

### inputEvents
You can pass an inputEvents object into a parent cardField component or each card field individually.

Pass an inputEvents object to the parent cardField component to apply the object to every field.

Pass an inputEvents object to an individual card field to apply the object to that field only. This overrides any object passed through a parent component.

### Example: inputEvents into parent component
```javascript
const cardField = paypal.CardFields({ 
  inputEvents: {
    onChange: function(data) {
      // Do something when an input changes
    },
    onFocus: function(data) {
      // Do something when a field gets focus
    },
    onBlur: function(data) {
      // Do something when a field loses focus
    },
    onInputSubmitRequest: function(data) {
      if (data.isFormValid) {
        // Submit the card form for the payer
      } else {
        // Inform payer that some fields are not valid
      }
    }
  }
});
```

### Example: inputEvents into individual component
```javascript
const cardField = paypal.CardFields(/* options */)
const nameField = cardField.NameField({ /* options */ })
nameField.render(cardNameContainer);
nameField.clear();
```

### Sample state object
Each of the event callbacks returns a state object similar to the following example:

```javascript
data: {
  cards: [{code: {name: 'CVV', size: 3}, niceType: "Visa", type: "visa"}],
  emittedBy: "number", // Not returned for getState()
  isFormValid: false,
  errors: ["INVALID_CVV"]
  fields: {
    cardCvvField: {
      isFocused: false,
      isEmpty: true,
      isValid: false,
      isPotentiallyValid: true,
    },
    cardNumberField: {
      isFocused: true,
      isEmpty: false,
      isValid: false,
      isPotentiallyValid: true,
    },
    cardNameField: {
      isFocused: false,
      isEmpty: true,
      isValid: false,
      isPotentiallyValid: true,
    },
    cardExpiryField: {
      isFocused: false,
      isEmpty: true,
      isValid: false,
      isPotentiallyValid: true,
    },
  },
}
```

### Validate individual fields
Validate individual fields when an input event occurs:

```javascript
const cardFields = paypal.CardFields({/* options */})
let cardContainer = document.getElementById("#card-number-field-container")
const cardNumberField = cardFields.NumberField({/* options */})
cardField.NumberField({/* options */}).render(cardNumberContainer);
```

### Validate entire card form
Validate an entire card form when an input event occurs:

```javascript
const formContainer = document.getElementById("form-container")
const cardFields = paypal.CardFields({/* options */})
const cardFields = paypal.CardFields({/* options */})
```

## Methods on parent card fields
The following methods are supported on parent card fields:

- getState()
- isEligible()
- submit()

### State object
```javascript
data: {
  cards: [{code: {name: 'CVV', size: 3}, niceType: "Visa", type: "visa"}],
  emittedBy: "number", // Not returned for getState()
  isFormValid: false,
  errors: ["INVALID_CVV"],
  fields: {
    cardCvvField: {
      isFocused: false,
      isEmpty: true,
      isValid: false,
      isPotentiallyValid: true,
    },
    cardNumberField: {
      isFocused: true,
      isEmpty: false,
      isValid: false,
      isPotentiallyValid: true,
    },
    cardNameField: {
      isFocused: false,
      isEmpty: true,
      isValid: false,
      isPotentiallyValid: true,
    },
    cardExpiryField: {
      isFocused: false,
      isEmpty: true,
      isValid: false,
      isPotentiallyValid: true,
    },
  },
}
```

### isEligible()
Checks if a cardField instance can render based on configuration and business rules.

Example
```javascript
const cardField = paypal.CardFields({/* options */})
if (cardFields.isEligible()) {
  cardFields.NumberField().render("#card-number-field-container");
  cardFields.CVVField().render("#card-cvv-field-container");
  // ...
}
```

### submit()
Submits payment information.

Example
```javascript
// Add click listener to your submit button
// and call the submit function on the CardField component
multiCardFieldButton.addEventListener("click", () => {
  cardField.submit().then(() => {
    console.log("Card Fields submit");
  }).catch((err) => {
    console.log("There was an error with card fields: ", err);
  });
});
```

### Methods on individual card fields
The following methods are supported on individual card fields:

- addClass()
- clear()
- focus()
- removeAttribute()
- removeClass()
- render()
- setAttribute()
- setMessage()
- close()

### Custom styles
```javascript
const cardField = paypal.CardFields({/* options */})
const nameField = cardField.NameField({/* options */})
nameField.setAttribute("placeholder", "Enter your full name");
nameField.render(cardNameContainer);
```

### Remove attributes
```javascript
const cardField = paypal.CardFields({/* options */})
const numberField = cardField.NumberField({/* options */})
numberField.render(cardNumberContainer);
numberField.removeAttribute("placeholder");
```

### Render
```javascript
const cardNumberContainer = document.getElementById("card-number-field-container");
const cardField = paypal.CardFields({/* options */})
cardField.NumberField({/* options */}).render(cardNumberContainer);
```

### Set attributes
```javascript
const cardField = paypal.CardFields({/* options */})
const nameField = cardField.NameField({/* options */})
nameField.setAttribute("placeholder", "Enter your full name");
nameField.render(cardNameContainer);
```

### Message
```javascript
const cardField = paypal.CardFields({/* options */})
const nameField = cardField.NameField({/* options */})
nameField.render(cardNameContainer);
nameField.setMessage("Enter your full name");
```

### Close
```javascript
const cardField = paypal.CardFields({/* options */})
const nameField = cardField.NameField({/* options */})
nameField.render(cardNameContainer);
// Call this to tear down nameField
nameField.close();