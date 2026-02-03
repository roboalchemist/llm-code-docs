# Subscribe to Hosted Field events

## Important: This JavaScript SDK documentation uses the legacy HostedFields component. If you are integrated with the CardFields component, see [Card Field Events](/docs/checkout/advanced/customize/card-fields-events/) .

Subscribe to advanced credit and debit card payment events using an event listener. Event listeners can help you update the UI of your form based on the state of the fields.

You can subscribe to the following events:

| Event name | Description |
| --- | --- |
| [focus](#link-event-focus) | Triggers when a field gains focus. |
| [blur](#link-event-blur) | Triggers when a field loses focus. |
| [empty](#link-event-empty) | Triggers when a field transitions from having data to being empty. |
| [notEmpty](#link-event-notempty) | Triggers when a field transitions from being empty to having data. |
| [cardTypeChange](#link-event-cardtypechange) | Triggers when the possible card type changes. Only triggered by a change in the number field. |
| [validityChange](#link-event-validitychange) | Triggers when the validity of a field changes. |
| [inputSubmitRequest](#link-event-inputsubmitrequest) | Triggers when the payer requests submission of an input field. For example, when pressing Enter or Return on the keyboard. |

## 1. Set up

Set up an event listener using the advanced credit and debit card payments on() function. Use the event object to get information about your fields and update your UI.

```javascript
<ContentAccordion>
    <AccordionRow heading="cardTypeChange Example">
        <p style="margin-top: 3rem;" data-testid="dcac-cfe-acc1-p0">
            Here is an example of how to use <code>cardTypeChange</code> to update your CVV label and placeholder:
        </p>
        <NewCodeBlockWrapper>
            <NewCodeBlock
                className="language-javascript"
                children`
                paypal.HostedFields.render({ /* ... */ }).then(function (hostedFieldsInstance) {
                    var cvvLabel = document.querySelector('label[for="cvv"]'); // The label for your CVV field
                    hostedFieldsInstance.on('cardTypeChange', function (event) {
                        // This event triggers when a change in card type is detected.
                        // It triggers only from the number field.
                        var cvvText;
                        if (event.cards.length === 1) {
                            cvvText = event.cards[0].code.name;
                        } else {
                            cvvText = 'CVV';
                        }
                        cvvLabel.innerHTML = cvvText;
                        hostedFieldsInstance.setAttribute({ field: 'cvv', attribute: 'placeholder', value: cvvText });
                    });
                });
            `
            />
        </NewCodeBlockWrapper>
    </AccordionRow>
</ContentAccordion>
```

## 2. Get the state of your form

Use the getState function to get the state of your form without using events.

### State Example

The following example uses getState to confirm that all provided fields are valid before form submission:

```javascript
var form = document.querySelector('#my-sample-form');
paypal.HostedFields.render({/* ... */}).then(function(hostedFieldsInstance){
    form.addEventListener('submit',function(event){
        var state=hostedFieldsInstance.getState();
        var formValid=Object.keys(state.fields).every(function(key){
            return state.fields[key].isValid;
        });
        if(formValid){
            // Submit hosted fields card data
            hostedFieldsInstance.submit();
        }else{
            // Let the payer know their fields are invalid
            console.log(event.emittedBy,'gained focus');
        }
    });
});
```

## Sample event

### Listeners

The following examples show how to use event listeners.

- [focus](#link-event-focus)
- [blur](#link-event-blur)
- [empty](#link-event-empty)
- [notEmpty](#link-event-notempty)
- [cardTypeChange](#link-event-cardtypechange)
- [validityChange](#link-event-validitychange)
- [inputSubmitRequest](#link-event-inputsubmitrequest)

#### Focus

This event triggers when a field gains focus.

```javascript
paypal.HostedFields.render({/* ... */}).then(function(hostedFieldsInstance){
    hostedFieldsInstance.on('focus',function(event){
        // Your actions on focus
        console.log(event.emittedBy,'gained focus');
    });
});
```

#### Blur

This event triggers when a field loses focus.

```javascript
paypal.HostedFields.render({/* ... */}).then(function(hostedFieldsInstance){
    hostedFieldsInstance.on('blur',function(event){
        // Your actions on blur
        console.log(event.emittedBy,'lost focus');
    });
});
```

#### Empty

This event triggers when a field transitions from having data to being empty.

```javascript
paypal.HostedFields.render({/* ... */}).then(function(hostedFieldsInstance){
    hostedFieldsInstance.on('empty',function(event){
        // Your actions on empty
        console.log(event.emittedBy,'is now empty');
    });
});
```

#### NotEmpty

This event triggers when a field transitions from being empty to having data.

```javascript
paypal.HostedFields.render({/* ... */}).then(function(hostedFieldsInstance){
    hostedFieldsInstance.on('notEmpty',function(event){
        console.log(event.emittedBy,'has data');
    });
});
```

#### CardTypeChange

This event triggers when activity within the number field has changed, so the possible card type has also changed.

```javascript
paypal.HostedFields.render({/* ... */}).then(function(hostedFieldsInstance){
    hostedFieldsInstance.on('cardTypeChange',function(event){
        if(event.cards.length===1){
            console.log(event.cards[0].type);
        }else{
            console.log('Type of card not yet known');
        }
    });
});
```

#### ValidityChange

This event triggers when the validity of a field has changed. Validity is represented in the event object as two booleans: isValid and isPotentiallyValid .

```javascript
paypal.HostedFields.render({/* ... */}).then(function(hostedFieldsInstance){
    hostedFieldsInstance.on('validityChange',function(event){
        var field=event.fields[event.emittedBy];
        if(field.isValid){
            console.log(event.emittedBy,'is fully valid');
        } elseif(field.isPotentiallyValid){
            console.log(event.emittedBy,'is potentially valid');
        } else {
            console.log(event.emittedBy,'is not valid');
        }
    });
});
```

#### InputSubmitRequest

This event triggers when the payer requests submission of an input field. For example, when pressing Enter or Return on the keyboard.

```javascript
var hostedFields=require('braintree-web/hosted-fields');
var submitButton=document.querySelector('input[type="submit"]');
paypal.HostedFields.render({/* ... */}).then(function(hostedFieldsInstance){
    hostedFieldsInstance.on('inputSubmitRequest',function(){
        // User requested submission, e.g. by pressing Enter or equivalent
        submitButton.click();
    });
});
```

## Methods

The following methods are supported on parent and individual card fields:

- [render()](#link-method-render)
- [isEligible()](#link-method-iseligible)
- [addClass()](#link-method-addclass)
- [clear()](#link-method-clear)
- [focus()](#link-method-focus)
- [getstate()](#link-method-getstate)
- [on()](#link-method-on)
- [removeAttribute()](#link-method-removeattribute)
- [setAttribute()](#link-method-setattribute)
- [removeClass()](#link-method-removeclass)
- [setMessage()](#link-method-setmessage)

### render()

1. render(options)→{Promise|void}
   The render() method creates an instance of advanced credit and debit card payments and renders the card fields for checkout based on the mapping and styles provided by options .

   The options object maps the HTML element to each of the advanced credit and debit card
   payment inputs, style, and properties.

   The options object contains the following fields:

   - createOrder : A callback field that returns the order-id value. The order-id is a required reference ID for each order created. The order-id also associates the payer's card details with the order created.
   - styles : A [styleOptions](#link-type-styleoptions) parameter that defines the styling applied on each of the advanced credit and debit card payments
       inputs.
   - fields : A [fieldOptions](#link-type-fieldoptions) parameter that defines the mapping of the HTML element to the advanced credit and debit card
       payments inputs and their properties.

### isEligible()

1. isEligible()→{boolean}
   The isEligible() method checks if advanced credit and debit card payments are eligible to
   render based on configuration and business rules.

### addClass()

1. addClass(field,classname,callback<sub>opt</sub>)→{Promise|void}
   The addClass1() method adds a class to a field. Use this method to update field styles when
   events occur elsewhere in your checkout integration. Includes the following parameters:

   | Parameter | Type | Description |
   | --- | --- | --- |
   | field | string | The field you want to add a class to. Must be a validfieldOption. |
   | classname | string | The class to be added. |
   | callback | callback | This callback triggers on completion. It passes any errors that occur during the call. This
       returns no data if the call successfully adds the class. |

### clear()

1. clear(field,callback<sub>opt</sub>)→{Promise|void}
   The clear() method clears the value of a field. Includes the following parameters:

   | Parameter | Type | Description |
   | --- | --- | --- |
   | field | string | The field you want to clear. Must be a validfieldOption. |
   | callback | callback | This callback triggers on completion. It passes any errors that occur during the call. This
       returns no data if the call successfully adds the class. |

### focus()

1. focus(field,callback<sub>opt</sub>)→{void}
   The focus() method places focus on a field. Includes the following parameters:

   | Parameter | Type | Description |
   | --- | --- | --- |
   | field | string | The field you want to focus. Must be a validfieldOption. |
   | callback | callback | This callback triggers on completion. It passes any errors that occur during the call. This
       returns no data if the call successfully adds the class. |

### getState()

1. getState()→{object}
   The event payload is sent from on or getState .

   | Parameter | Type | Description |
   | --- | --- | --- |
   | cards | array | Returns an array of potential cards. If the card type has been determined, the array
       contains only one card. Advanced credit and debit card payments use
       credit-card-type, an open-source card detection library. |
   | emittedBy | string | The name of the field associated with an event. This is not included if returned by
       getState. Valid values are"number","cvv", and"expirationDate". |
   | fields | object[hostedFieldsFieldData](#link-type-hostedfieldsfielddata) | Contains data about the field in the context of the event. Valid values are"number","cvv", and"expirationDate". |

### on()

1. on(event,handler)→{void}
   The on() method subscribes a handler function to a named event. Events include:

   - blur
   - focus
   - empty
   - notEmpty
   - cardTypeChange
   - validityChange

   Events trigger a stateObject , which includes the following parameters:

   | Parameter | Type | Description |
   | --- | --- | --- |
   | event | string | The name of the event to which you are subscribing. |
   | handler | callback | A callback to handle the event. |

### removeAttribute()

1. removeAttribute(options,callback<sub>opt</sub>)→{Promise|void}
   The removeAttribute() method removes a supported attribute from a field. Includes the
   following parameters:

   | Parameter | Type | Description |
   | --- | --- | --- |
   | options | object | The options for the attribute you want to remove: -field: A string field
       from which you want to remove an attribute. Must be a validfieldOption. -attribute: The name of the attribute you want to remove from the field. |
   | callback | callback | This callback triggers on completion. It passes any errors that occur during the call. This
       returns no data if the call successfully adds the class. |

### setAttribute()

1. setAttribute(options,callback<sub>opt</sub>)→{Promise|void}
   The setAttribute() method sets an attribute of a field. Supported attributes are aria-invalid , aria-required , disabled , and placeholder . Includes the following parameters:

   | Parameter | Type | Description |
   | --- | --- | --- |
   | options | object | The options for the attribute you want to set. -field: A string field from
       which you want to add an attribute. Must be a validfieldOption. -attribute: The name of the attribute you want to add to the field. -value: The value for the attribute. |
   | callback | callback | This callback triggers on completion. It passes any errors that occur during the call. This
       returns no data if the call successfully adds the class. |

### removeClass()

1. removeClass(field,classname,callback<sub>opt</sub>)→{Promise|void}
   The removeClass() method removes a class from a field. Use this class to update field styles
   when events occur elsewhere in your checkout integration. Includes the following parameters:

   | Parameter | Type | Description |
   | --- | --- | --- |
   | field | string | The field you want to remove a class from. Must be a validfieldOption. |
   | classname | string | The class you want to remove. |
   | callback | callback | This callback triggers on completion. It passes any errors that occur during the call. This
       returns no data if the call successfully adds the class. |

### setMessage()

1. setMessage(options)→{void}
   The setMessage() method sets a visually hidden message for screen readers on a field.

   Includes the following options parameter, which contains the following:

   - field : A string field from which you want to add an attribute. Must be a valid fieldOption .
   - message : The message to set.

## Type definitions

Card field events use the following types of information:

- [field](#link-type-field)
- [fieldOptions](#link-type-fieldoptions)
- [styleOptions](#link-type-styleoptions)
- [cardSecurityCode](#link-type-cardsecuritycode)
- [hostedFieldsCard](#link-type-hostedfieldscard)
- [hostedFieldsFieldData](#link-type-hostedfieldsfielddata)
- [stateObject](#link-type-stateobject)

### field

Fields used in [fieldOptions](#link-type-fieldoptions) object.

| Property | Type | Description |
| --- | --- | --- |
| [](https://developer.paypal.com/docs/checkout/advanced/customize/card-fields/v1/events/#selectorstringa-css-selector-to-find-the-container-where-the-card-fields-are-inserted.)selector | string | A CSS selector to find the container where the card fields are inserted. |
| [](https://developer.paypal.com/docs/checkout/advanced/customize/card-fields/v1/events/#placeholderstringused-as-the-placeholder-attribute-of-the-input.-if-the-browser-doesn't-natively-supportplaceholder,-it-is-polyfilled.)placeholder | string | Used as theplaceholderattribute of the input. If the browser doesn't natively supportplaceholder, it is polyfilled. |
| [](https://developer.paypal.com/docs/checkout/advanced/customize/card-fields/v1/events/#typestringthe-type-attribute-of-the-input.-for-example,-to-mask-cvv-input-use-type:-%22password%22.)type | string | Thetypeattribute of the input. For example, to maskCVVinput usetype: "password". |
| [](https://developer.paypal.com/docs/checkout/advanced/customize/card-fields/v1/events/#formatinputbooleanallow-or-deny-automatic-formatting-on-this-field.-default-is-true.)formatInput | boolean | Allow or deny automatic formatting on this field. Default istrue. |
| [](https://developer.paypal.com/docs/checkout/advanced/customize/card-fields/v1/events/#maskinputobject-or-booleanallow-or-deny-input-masking-when-input-is-not-focused.-if-set-to-true,-instead-of-an-object,-the-defaults-for-the-maskinput-parameters-are-used.-default-is-false.-the-object-properties-are:-character:-a-string-field-which-specifies-the-character-to-use-when-masking-the-input.-the-default-character-('\xE2\x80\xA2')-uses-a-unicode-symbol,-so-the-web-page-must-support-utf-8-characters-when-using-the-default.-showlastfour:-a-boolean-field-applicable-only-for-the-credit-card-field.-defines-whether-to-show-the-last-4-digits-of-the-card-when-masking.-default-is-false.)maskInput | object or boolean | Allow or deny input masking when input is not focused. If set totrue, instead of an object, the defaults for themaskInputparameters are used. Default isfalse. The object properties are: character: A string field which specifies the character to use when masking the input. The default character ('•') uses a Unicode symbol, so the web page must support UTF-8 characters when using the default. showLastFour: A Boolean field applicable only for the credit card field. Defines whether to show the last 4 digits of the card when masking. Default isfalse. |
| maxCardLength | number | This option only applies to thenumberfield. Limits the card number length, even if the card brand supports longer card numbers. If the value that is passed is greater than the max length for a card brand, the smaller of the two values is used. For example, ifmaxCardLengthis set to 16, but an American Express card, which has a max card length of 15, is entered, the max card length is 15. |
| maxlength | number | This option applies only to thecvvfield. Used as themaxlengthattribute of the input if it is less than the default. Themaxlengthoption is most often used to limit the length of the CVV input for CVV-only verifications when the card type is known, and to limit the length of the postal code input when cards are coming from a known region. |
| minlength | number | This option applies only to thecvvfield. Used as theminlengthattribute of the input. The default value is3. Theminlengthattribute applies only to integrations capturing a CVV without anumberfield. |
| prefill | string | A value to be used to pre-fill the field. For example, when creating an update card form, you can pre-fill the expiration date fields with the old expiration date. |
| rejectUnsupportedCards | boolean | Allow only card types that your merchant account can process. Unsupported card types invalidate the card form. For example, if you only process Visa cards, a payer entering an American Express card would get an invalid card field. This can be used only for thenumberfield. The default isfalse. |

### fieldOptions

An object that has [field](#link-type-field) objects for each field.

| Property | Type | Description |
| --- | --- | --- |
| number | object[field](#link-type-field) | A field for card number. |
| expirationDate | object[field](#link-type-field) | A field for expiration date inMM/YYYYorMM/YYformat. |
| cvv | object[field](#link-type-field) | A field for a 3 or 4 digit card verification code, such asCVVorCID. |

### styleOptions

An object that represents CSS that is applied in each card field. This object looks similar to CSS, and changes font styles such as font-family or color .

You can also pass the name of a class on your site that contains the styles you want to apply. The style
properties are automatically pulled from the class and applied to the card field inputs

.

Note:  Using  styleOptions  is recommended only for input elements. If you use a  select  style for the expiration date, unexpected styling might occur.

### cardSecurityCode

Information about the security code for a card.

| Property | Type | Description |
| --- | --- | --- |
| name | string | The name of security code for card. Valid values areCVV,CID, andCVC. |
| size | number | The expected length of the security code, which is most often3or4. |

### hostedFieldsCard

Information about the card type, sent in stateObjects .

| Property | Type | Description |
| --- | --- | --- |
| type | string | The code-friendly card type. Valid values are: american-express diners-club discover jcb maestro master-card unionpay visa |
| niceType | string | The human-readable card type. Valid values: American Express Diners Club Discover JCB Discover JCB Maestro MasterCard UnionPay Visa |
| code | object[cardSecurityCode](#link-type-cardsecuritycode) | Contains data about the card brand's security code requirements. For example, on a Visa
card, theCVVis 3 digits, while on an American Express card, theCIDis 4 digits. |

### hostedFieldsFieldData

Fields data for advanced credit and debit card payments is sent in stateObjects .

| Property | Type | Description |
| --- | --- | --- |
| container | HTML element | The container DOM element on your page associated with the current event. |
| isFocused | boolean | Whether the input is currently focused. |
| isEmpty | boolean | Whether the user has entered a value in the input. |
| isPotentiallyValid | boolean | Whether the current input could potentially be valid. For example, if a payer is entering a
card number and types "41", the field recognizes that the input can become a valid entry.
However, if the payer enters "4x" it is clear that the card number can't become valid. The
value is true if the entry can become valid, and false if it can't. |
| isValid | boolean | Whether the input is valid and can be submitted. |

### stateObject

The event payload is sent from on or getState .

| Property | Type | Description |
| --- | --- | --- |
| cards | array | Returns an array of potential cards. If the card type has been determined, the array
contains only one card. Advanced credit and debit card payments usecredit-card-type, an open-source card detection library. |
| emittedBy | string | The name of the field associated with an event. This is not included if returned bygetState. Valid values are"number","cvv", and"expirationDate". |
| fields | object[hostedFieldsFieldData](#link-type-hostedfieldsfielddata) | Contains data about the field in the context of the event. Valid values are"number","cvv", and"expirationDate". |

## Methods

The following methods are supported on parent and individual card fields:

- [render()](#link-method-render)
- [isEligible()](#link-method-iseligible)
- [addClass()](#link-method-addclass)
- [clear()](#link-method-clear)
- [focus()](#link-method-focus)
- [getstate()](#link-method-getstate)
- [on()](#link-method-on)
- [removeAttribute()](#link-method-removeattribute)
- [setAttribute()](#link-method-setattribute)
- [removeClass()](#link-method-removeclass)
- [setMessage()](#link-method-setmessage)

### render()

1. render(options)→{Promise|void}
   The render() method creates an instance of advanced credit and debit card payments and renders the card fields for checkout based on the mapping and styles provided by options .

   The options object maps the HTML element to each of the advanced credit and debit card
   payment inputs, style, and properties.

   The options object contains the following fields:

   - createOrder : A callback field that returns the order-id value. The order-id is a required reference ID for each order created. The order-id also associates the payer's card details with the order created.
   - styles : A [styleOptions](#link-type-styleoptions) parameter that defines the styling applied on each of the advanced credit and debit card payments
       inputs.
   - fields : A [fieldOptions](#link-type-fieldoptions) parameter that defines the mapping of the HTML element to the advanced credit and debit card
       payments inputs and their properties.

### isEligible()

1. isEligible()→{boolean}
   The isEligible() method checks if advanced credit and debit card payments are eligible to
   render based on configuration and business rules.

### addClass()

1. addClass(field,classname,callback<sub>opt</sub>)→{Promise|void}
   The addClass1() method adds a class to a field. Use this method to update field styles when
   events occur elsewhere in your checkout integration. Includes the following parameters:

   | Parameter | Type | Description |
   | --- | --- | --- |
   | field | string | The field you want to add a class to. Must be a validfieldOption. |
   | classname | string | The class to be added. |
   | callback | callback | This callback triggers on completion. It passes any errors that occur during the call. This
       returns no data if the call successfully adds the class. |

### clear()

1. clear(field,callback<sub>opt</sub>)→{Promise|void}
   The clear() method clears the value of a field. Includes the following parameters:

   | Parameter | Type | Description |
   | --- | --- | --- |
   | field | string | The field you want to clear. Must be a validfieldOption. |
   | callback | callback | This callback triggers on completion. It passes any errors that occur during the call. This
       returns no data if the call successfully adds the class. |

### focus()

1. focus(field,callback<sub>opt</sub>)→{void}
   The focus() method places focus on a field. Includes the following parameters:

   | Parameter | Type | Description |
   | --- | --- | --- |
   | field | string | The field you want to focus. Must be a validfieldOption. |
   | callback | callback | This callback triggers on completion. It passes any errors that occur during the call. This
       returns no data if the call successfully adds the class. |

### getState()

1. getState()→{object}
   The event payload is sent from on or getState .

   | Parameter | Type | Description |
   | --- | --- | --- |
   | cards | array | Returns an array of potential cards. If the card type has been determined, the array
       contains only one card. Advanced credit and debit card payments usecredit-card-type, an open-source card detection library. |
   | emittedBy | string | The name of the field associated with an event. This is not included if returned by
       getState. Valid values are"number","cvv", and"expirationDate". |
   | fields | object[hostedFieldsFieldData](#link-type-hostedfieldsfielddata) | Contains data about the field in the context of the event. Valid values are"number","cvv", and"expirationDate". |

### on()

1. on(event,handler)→{void}
   The on() method subscribes a handler function to a named event. Events include:

   - blur
   - focus
   - empty
   - notEmpty
   - cardTypeChange
   - validityChange

   Events trigger a stateObject , which includes the following parameters:

   | Parameter | Type | Description |
   | --- | --- | --- |
   | event | string | The name of the event to which you are subscribing. |
   | handler | callback | A callback to handle the event. |

### removeAttribute()

1. removeAttribute(options,callback<sub>opt</sub>)→{Promise|void}
   The removeAttribute() method removes a supported attribute from a field. Includes the
   following parameters:

   | Parameter | Type | Description |
   | --- | --- | --- |
   | options | object | The options for the attribute you want to remove: -field: A string field
       from which you want to remove an attribute. Must be a validfieldOption. -attribute: The name of the attribute you want to remove from the field. |
   | callback | callback | This callback triggers on completion. It passes any errors that occur during the call. This
       returns no data if the call successfully adds the class. |

### setAttribute()

1. setAttribute(options,callback<sub>opt</sub>)→{Promise|void}
   The setAttribute() method sets an attribute of a field. Supported attributes are aria-invalid , aria-required , disabled , and placeholder . Includes the following parameters:

   | Parameter | Type | Description |
   | --- | --- | --- |
   | options | object | The options for the attribute you want to set. -field: A string field from
       which you want to add an attribute. Must be a validfieldOption. -attribute: The name of the attribute you want to add to the field. -value: The value for the attribute. |
   | callback | callback | This callback triggers on completion. It passes any errors that occur during the call. This
       returns no data if the call successfully adds the class. |

### removeClass()

1. removeClass(field,classname,callback<sub>opt</sub>)→{Promise|void}
   The removeClass() method removes a class from a field. Use this class to update field styles
   when events occur elsewhere in your checkout integration. Includes the following parameters:

   | Parameter | Type | Description |
   | --- | --- | --- |
   | field | string | The field you want to remove a class from. Must be a validfieldOption. |
   | classname | string | The class you want to remove. |
   | callback | callback | This callback triggers on completion. It passes any errors that occur during the call. This
       returns no data if the call successfully adds the class. |

### setMessage()

1. setMessage(options)→{void}
   The setMessage() method sets a visually hidden message for screen readers on a field.

   Includes the following options parameter, which contains the following:

   - field : A string field from which you want to add an attribute. Must be a valid fieldOption .
   - message : The message to set.

## Type definitions

Card field events use the following types of information:

- [field](#link-type-field)
- [fieldOptions](#link-type-fieldoptions)
- [styleOptions](#link-type-styleoptions)
- [cardSecurityCode](#link-type-cardsecuritycode)
- [hostedFieldsCard](#link-type-hostedfieldscard)
- [hostedFieldsFieldData](#link-type-hostedfieldsfielddata)
- [stateObject](#link-type-stateobject)

### field

Fields used in [fieldOptions](#link-type-fieldoptions) object.

| Property | Type | Description |
| --- | --- | --- |
| [](https://developer.paypal.com/docs/checkout/advanced/customize/card-fields/v1/events/#selectorstringa-css-selector-to-find-the-container-where-the-card-fields-are-inserted.)selector | string | A CSS selector to find the container where the card fields are inserted. |
| [](https://developer.paypal.com/docs/checkout/advanced/customize/card-fields/v1/events/#placeholderstringused-as-the-placeholder-attribute-of-the-input.-if-the-browser-doesn't-natively-supportplaceholder,-it-is-polyfilled.)placeholder | string | Used as theplaceholderattribute of the input. If the browser doesn't natively supportplaceholder, it is polyfilled. |
| [](https://developer.paypal.com/docs/checkout/advanced/customize/card-fields/v1/events/#typestringthe-type-attribute-of-the-input.-for-example,-to-mask-cvv-input-use-type:-%22password%22.)type | string | Thetypeattribute of the input. For example, to maskCVVinput usetype: "password". |
| [](https://developer.paypal.com/docs/checkout/advanced/customize/card-fields/v1/events/#formatinputbooleanallow-or-deny-automatic-formatting-on-this-field.-default-is-true.)formatInput | boolean | Allow or deny automatic formatting on this field. Default istrue. |
| [](https://developer.paypal.com/docs/checkout/advanced/customize/card-fields/v1/events/#maskinputobject-or-booleanallow-or-deny-input-masking-when-input-is-not-focused.-if-set-to-true,-instead-of-an-object,-the-defaults-for-the-maskinput-parameters-are-used.-default-is-false.-the-object-properties-are:-character:-a-string-field-which-specifies-the-character-to-use-when-masking-the-input.-the-default-character-('\xE2\x80\xA2')-uses-a-unicode-symbol,-so-the-web-page-must-support-utf-8-characters-when-using-the-default.-showlastfour:-a-boolean-field-applicable-only-for-the-credit-card-field.-defines-whether-to-show-the-last-4-digits-of-the-card-when-masking.-default-is-false.)maskInput | object or boolean | Allow or deny input masking when input is not focused. If set totrue, instead of an object, the defaults for themaskInputparameters are used. Default isfalse. The object properties are: character: A string field which specifies the character to use when masking the input. The default character ('•') uses a Unicode symbol, so the web page must support UTF-8 characters when using the default. showLastFour: A Boolean field applicable only for the credit card field. Defines whether to show the last 4 digits of the card when masking. Default isfalse. |
| maxCardLength | number | This option only applies to thenumberfield. Limits the card number length, even if the card brand supports longer card numbers. If the value that is passed is greater than the max length for a card brand, the smaller of the two values is used. For example, ifmaxCardLengthis set to 16, but an American Express card, which has a max card length of 15, is entered, the max card length is 15. |
| maxlength | number | This option applies only to thecvvfield. Used as themaxlengthattribute of the input if it is less than the default. Themaxlengthoption is most often used to limit the length of the CVV input for CVV-only verifications when the card type is known, and to limit the length of the postal code input when cards are coming from a known region. |
| minlength | number | This option applies only to thecvvfield. Used as theminlengthattribute of the input. The default value is3. Theminlengthattribute applies only to integrations capturing a CVV without anumberfield. |
| prefill | string | A value to be used to pre-fill the field. For example, when creating an update card form, you can pre-fill the expiration date fields with the old expiration date. |
| rejectUnsupportedCards | boolean | Allow only card types that your merchant account can process. Unsupported card types invalidate the card form. For example, if you only process Visa cards, a payer entering an American Express card would get an invalid card field. This can be used only for thenumberfield. The default isfalse. |

### fieldOptions

An object that has [field](#link-type-field) objects for each field.

| Property | Type | Description |
| --- | --- | --- |
| number | object[field](#link-type-field) | A field for card number. |
| expirationDate | object[field](#link-type-field) | A field for expiration date inMM/YYYYorMM/YYformat. |
| cvv | object[field](#link-type-field) | A field for a 3 or 4 digit card verification code, such asCVVorCID. |

### styleOptions

An object that represents CSS that is applied in each card field. This object looks similar to CSS, and changes font styles such as font-family or color .

You can also pass the name of a class on your site that contains the styles you want to apply. The style
properties are automatically pulled from the class and applied to the card field inputs

.

Note:  Using  styleOptions  is recommended only for input elements. If you use a  select  style for the expiration date, unexpected styling might occur.

### cardSecurityCode

Information about the security code for a card.

| Property | Type | Description |
| --- | --- | --- |
| name | string | The name of security code for card. Valid values areCVV,CID, andCVC. |
| size | number | The expected length of the security code, which is most often3or4. |

### hostedFieldsCard

Information about the card type, sent in stateObjects .

| Property | Type | Description |
| --- | --- | --- |
| type | string | The code-friendly card type. Valid values are: american-express diners-club discover jcb maestro master-card unionpay visa |
| niceType | string | The human-readable card type. Valid values: American Express Diners Club Discover JCB Discover JCB Maestro MasterCard UnionPay Visa |
| code | object[cardSecurityCode](#link-type-cardsecuritycode) | Contains data about the card brand's security code requirements. For example, on a Visa
card, theCVVis 3 digits, while on an American Express card, theCIDis 4 digits. |

### hostedFieldsFieldData

Fields data for advanced credit and debit card payments is sent in stateObjects .

| Property | Type | Description |
| --- | --- | --- |
| container | HTML element | The container DOM element on your page associated with the current event. |
| isFocused | boolean | Whether the input is currently focused. |
| isEmpty | boolean | Whether the user has entered a value in