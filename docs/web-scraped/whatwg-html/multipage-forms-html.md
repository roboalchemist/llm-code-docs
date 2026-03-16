# Source: https://html.spec.whatwg.org/multipage/forms.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/forms.html

Published Time: Mon, 16 Mar 2026 07:32:47 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 4.9 Tabular data](https://html.spec.whatwg.org/multipage/tables.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [4.10.5 The input element →](https://html.spec.whatwg.org/multipage/input.html)
1.       1.   [4.10 Forms](https://html.spec.whatwg.org/multipage/forms.html#forms)
        1.   [4.10.1 Introduction](https://html.spec.whatwg.org/multipage/forms.html#introduction-4)
            1.   [4.10.1.1 Writing a form's user interface](https://html.spec.whatwg.org/multipage/forms.html#writing-a-form's-user-interface)
            2.   [4.10.1.2 Implementing the server-side processing for a form](https://html.spec.whatwg.org/multipage/forms.html#implementing-the-server-side-processing-for-a-form)
            3.   [4.10.1.3 Configuring a form to communicate with a server](https://html.spec.whatwg.org/multipage/forms.html#configuring-a-form-to-communicate-with-a-server)
            4.   [4.10.1.4 Client-side form validation](https://html.spec.whatwg.org/multipage/forms.html#client-side-form-validation)
            5.   [4.10.1.5 Enabling client-side automatic filling of form controls](https://html.spec.whatwg.org/multipage/forms.html#enabling-client-side-automatic-filling-of-form-controls)
            6.   [4.10.1.6 Improving the user experience on mobile devices](https://html.spec.whatwg.org/multipage/forms.html#improving-the-user-experience-on-mobile-devices)
            7.   [4.10.1.7 The difference between the field type, the autofill field name, and the input modality](https://html.spec.whatwg.org/multipage/forms.html#the-difference-between-the-field-type,-the-autofill-field-name,-and-the-input-modality)
            8.   [4.10.1.8 Date, time, and number formats](https://html.spec.whatwg.org/multipage/forms.html#input-author-notes)

        2.   [4.10.2 Categories](https://html.spec.whatwg.org/multipage/forms.html#categories)
        3.   [4.10.3 The `form` element](https://html.spec.whatwg.org/multipage/forms.html#the-form-element)
        4.   [4.10.4 The `label` element](https://html.spec.whatwg.org/multipage/forms.html#the-label-element)

### 4.10 Forms[](https://html.spec.whatwg.org/multipage/forms.html#forms)

[Element#Forms](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Forms "This page lists all the HTML elements, which are created using tags.")

Support in all current engines.

Firefox 4+Safari 4+Chrome 61+

* * *

Opera 52+Edge 79+

* * *

Edge (Legacy)16+Internet Explorer 10+

* * *

Firefox Android 5+Safari iOS 3.2+Chrome Android 61+WebView Android 61+Samsung Internet 8.0+Opera Android 47+

#### 4.10.1 Introduction[](https://html.spec.whatwg.org/multipage/forms.html#introduction-4)

_This section is non-normative._

A form is a component of a web page that has form controls, such as text, buttons, checkboxes, range, or color picker controls. A user can interact with such a form, providing data that can then be sent to the server for further processing (e.g. returning the results of a search or calculation). No client-side scripting is needed in many cases, though an API is available so that scripts can augment the user experience or use forms for purposes other than submitting data to a server.

Writing a form consists of several steps, which can be performed in any order: writing the user interface, implementing the server-side processing, and configuring the user interface to communicate with the server.

##### 4.10.1.1 Writing a form's user interface[](https://html.spec.whatwg.org/multipage/forms.html#writing-a-form's-user-interface)

_This section is non-normative._

For the purposes of this brief introduction, we will create a pizza ordering form.

Any form starts with a `form` element, inside which are placed the controls. Most controls are represented by the `input` element, which by default provides a text control. To label a control, the `label` element is used; the label text and the control itself go inside the `label` element. Each part of a form is considered a [paragraph](https://html.spec.whatwg.org/multipage/dom.html#paragraph), and is typically separated from other parts using `p` elements. Putting this together, here is how one might ask for the customer's name:

```
<form>
 <p><label>Customer name: <input></label></p>
</form>
```

To let the user select the size of the pizza, we can use a set of radio buttons. Radio buttons also use the `input` element, this time with a `type` attribute with the value `radio`. To make the radio buttons work as a group, they are given a common name using the `name` attribute. To group a batch of controls together, such as, in this case, the radio buttons, one can use the `fieldset` element. The title of such a group of controls is given by the first element in the `fieldset`, which has to be a `legend` element.

```
<form>
 <p><label>Customer name: <input></label></p>
 <fieldset>
  <legend> Pizza Size </legend>
  <p><label> <input type=radio name=size> Small </label></p>
  <p><label> <input type=radio name=size> Medium </label></p>
  <p><label> <input type=radio name=size> Large </label></p>
 </fieldset>
</form>
```

Changes from the previous step are highlighted.

To pick toppings, we can use checkboxes. These use the `input` element with a `type` attribute with the value `checkbox`:

```
<form>
 <p><label>Customer name: <input></label></p>
 <fieldset>
  <legend> Pizza Size </legend>
  <p><label> <input type=radio name=size> Small </label></p>
  <p><label> <input type=radio name=size> Medium </label></p>
  <p><label> <input type=radio name=size> Large </label></p>
 </fieldset>
 <fieldset>
  <legend> Pizza Toppings </legend>
  <p><label> <input type=checkbox> Bacon </label></p>
  <p><label> <input type=checkbox> Extra Cheese </label></p>
  <p><label> <input type=checkbox> Onion </label></p>
  <p><label> <input type=checkbox> Mushroom </label></p>
 </fieldset>
</form>
```

The pizzeria for which this form is being written is always making mistakes, so it needs a way to contact the customer. For this purpose, we can use form controls specifically for telephone numbers (`input` elements with their `type` attribute set to `tel`) and email addresses (`input` elements with their `type` attribute set to `email`):

```
<form>
 <p><label>Customer name: <input></label></p>
 <p><label>Telephone: <input type=tel></label></p>
 <p><label>Email address: <input type=email></label></p>
 <fieldset>
  <legend> Pizza Size </legend>
  <p><label> <input type=radio name=size> Small </label></p>
  <p><label> <input type=radio name=size> Medium </label></p>
  <p><label> <input type=radio name=size> Large </label></p>
 </fieldset>
 <fieldset>
  <legend> Pizza Toppings </legend>
  <p><label> <input type=checkbox> Bacon </label></p>
  <p><label> <input type=checkbox> Extra Cheese </label></p>
  <p><label> <input type=checkbox> Onion </label></p>
  <p><label> <input type=checkbox> Mushroom </label></p>
 </fieldset>
</form>
```

We can use an `input` element with its `type` attribute set to `time` to ask for a delivery time. Many of these form controls have attributes to control exactly what values can be specified; in this case, three attributes of particular interest are `min`, `max`, and `step`. These set the minimum time, the maximum time, and the interval between allowed values (in seconds). This pizzeria only delivers between 11am and 9pm, and doesn't promise anything better than 15 minute increments, which we can mark up as follows:

```
<form>
 <p><label>Customer name: <input></label></p>
 <p><label>Telephone: <input type=tel></label></p>
 <p><label>Email address: <input type=email></label></p>
 <fieldset>
  <legend> Pizza Size </legend>
  <p><label> <input type=radio name=size> Small </label></p>
  <p><label> <input type=radio name=size> Medium </label></p>
  <p><label> <input type=radio name=size> Large </label></p>
 </fieldset>
 <fieldset>
  <legend> Pizza Toppings </legend>
  <p><label> <input type=checkbox> Bacon </label></p>
  <p><label> <input type=checkbox> Extra Cheese </label></p>
  <p><label> <input type=checkbox> Onion </label></p>
  <p><label> <input type=checkbox> Mushroom </label></p>
 </fieldset>
 <p><label>Preferred delivery time: <input type=time min="11:00" max="21:00" step="900"></label></p>
</form>
```

The `textarea` element can be used to provide a multiline text control. In this instance, we are going to use it to provide a space for the customer to give delivery instructions:

```
<form>
 <p><label>Customer name: <input></label></p>
 <p><label>Telephone: <input type=tel></label></p>
 <p><label>Email address: <input type=email></label></p>
 <fieldset>
  <legend> Pizza Size </legend>
  <p><label> <input type=radio name=size> Small </label></p>
  <p><label> <input type=radio name=size> Medium </label></p>
  <p><label> <input type=radio name=size> Large </label></p>
 </fieldset>
 <fieldset>
  <legend> Pizza Toppings </legend>
  <p><label> <input type=checkbox> Bacon </label></p>
  <p><label> <input type=checkbox> Extra Cheese </label></p>
  <p><label> <input type=checkbox> Onion </label></p>
  <p><label> <input type=checkbox> Mushroom </label></p>
 </fieldset>
 <p><label>Preferred delivery time: <input type=time min="11:00" max="21:00" step="900"></label></p>
 <p><label>Delivery instructions: <textarea></textarea></label></p>
</form>
```

Finally, to make the form submittable we use the `button` element:

```
<form>
 <p><label>Customer name: <input></label></p>
 <p><label>Telephone: <input type=tel></label></p>
 <p><label>Email address: <input type=email></label></p>
 <fieldset>
  <legend> Pizza Size </legend>
  <p><label> <input type=radio name=size> Small </label></p>
  <p><label> <input type=radio name=size> Medium </label></p>
  <p><label> <input type=radio name=size> Large </label></p>
 </fieldset>
 <fieldset>
  <legend> Pizza Toppings </legend>
  <p><label> <input type=checkbox> Bacon </label></p>
  <p><label> <input type=checkbox> Extra Cheese </label></p>
  <p><label> <input type=checkbox> Onion </label></p>
  <p><label> <input type=checkbox> Mushroom </label></p>
 </fieldset>
 <p><label>Preferred delivery time: <input type=time min="11:00" max="21:00" step="900"></label></p>
 <p><label>Delivery instructions: <textarea></textarea></label></p>
 <p><button>Submit order</button></p>
</form>
```

##### 4.10.1.2 Implementing the server-side processing for a form[](https://html.spec.whatwg.org/multipage/forms.html#implementing-the-server-side-processing-for-a-form)

_This section is non-normative._

The exact details for writing a server-side processor are out of scope for this specification. For the purposes of this introduction, we will assume that the script at `https://pizza.example.com/order.cgi` is configured to accept submissions using the `application/x-www-form-urlencoded` format, expecting the following parameters sent in an HTTP POST body:

`custname`Customer's name`custtel`Customer's telephone number`custemail`Customer's email address`size`The pizza size, either `small`, `medium`, or `large``topping`A topping, specified once for each selected topping, with the allowed values being `bacon`, `cheese`, `onion`, and `mushroom``delivery`The requested delivery time`comments`The delivery instructions
##### 4.10.1.3 Configuring a form to communicate with a server[](https://html.spec.whatwg.org/multipage/forms.html#configuring-a-form-to-communicate-with-a-server)

_This section is non-normative._

Form submissions are exposed to servers in a variety of ways, most commonly as HTTP GET or POST requests. To specify the exact method used, the `method` attribute is specified on the `form` element. This doesn't specify how the form data is encoded, though; to specify that, you use the `enctype` attribute. You also have to specify the [URL](https://url.spec.whatwg.org/#concept-url) of the service that will handle the submitted data, using the `action` attribute.

For each form control you want submitted, you then have to give a name that will be used to refer to the data in the submission. We already specified the name for the group of radio buttons; the same attribute (`name`) also specifies the submission name. Radio buttons can be distinguished from each other in the submission by giving them different values, using the `value` attribute.

Multiple controls can have the same name; for example, here we give all the checkboxes the same name, and the server distinguishes which checkbox was checked by seeing which values are submitted with that name — like the radio buttons, they are also given unique values with the `value` attribute.

Given the settings in the previous section, this all becomes:

```
<form method="post"
      enctype="application/x-www-form-urlencoded"
      action="https://pizza.example.com/order.cgi">
 <p><label>Customer name: <input name="custname"></label></p>
 <p><label>Telephone: <input type=tel name="custtel"></label></p>
 <p><label>Email address: <input type=email name="custemail"></label></p>
 <fieldset>
  <legend> Pizza Size </legend>
  <p><label> <input type=radio name=size value="small"> Small </label></p>
  <p><label> <input type=radio name=size value="medium"> Medium </label></p>
  <p><label> <input type=radio name=size value="large"> Large </label></p>
 </fieldset>
 <fieldset>
  <legend> Pizza Toppings </legend>
  <p><label> <input type=checkbox name="topping" value="bacon"> Bacon </label></p>
  <p><label> <input type=checkbox name="topping" value="cheese"> Extra Cheese </label></p>
  <p><label> <input type=checkbox name="topping" value="onion"> Onion </label></p>
  <p><label> <input type=checkbox name="topping" value="mushroom"> Mushroom </label></p>
 </fieldset>
 <p><label>Preferred delivery time: <input type=time min="11:00" max="21:00" step="900" name="delivery"></label></p>
 <p><label>Delivery instructions: <textarea name="comments"></textarea></label></p>
 <p><button>Submit order</button></p>
</form>
```

There is no particular significance to the way some of the attributes have their values quoted and others don't. The HTML syntax allows a variety of equally valid ways to specify attributes, as discussed [in the syntax section](https://html.spec.whatwg.org/multipage/syntax.html#syntax-attributes).

For example, if the customer entered "Denise Lawrence" as their name, "555-321-8642" as their telephone number, did not specify an email address, asked for a medium-sized pizza, selected the Extra Cheese and Mushroom toppings, entered a delivery time of 7pm, and left the delivery instructions text control blank, the user agent would submit the following to the online web service:

`custname=Denise+Lawrence&custtel=555-321-8642&custemail=&size=medium&topping=cheese&topping=mushroom&delivery=19%3A00&comments=`
##### 4.10.1.4 Client-side form validation[](https://html.spec.whatwg.org/multipage/forms.html#client-side-form-validation)

[Form_validation](https://developer.mozilla.org/en-US/docs/Web/Forms/Form_validation "Client-side form validation sometimes requires JavaScript if you want to customize styling and error messages, but it always requires you to think carefully about the user. Always remember to help your users correct the data they provide. To that end, be sure to:")

Support in all current engines.

Firefox 4+Safari 5+Chrome 4+

* * *

Opera≤12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS 4+Chrome Android?WebView Android≤37+Samsung Internet?Opera Android≤12.1+

_This section is non-normative._

Forms can be annotated in such a way that the user agent will check the user's input before the form is submitted. The server still has to verify the input is valid (since hostile users can easily bypass the form validation), but it allows the user to avoid the wait incurred by having the server be the sole checker of the user's input.

The simplest annotation is the `required` attribute, which can be specified on `input` elements to indicate that the form is not to be submitted until a value is given. By adding this attribute to the customer name, pizza size, and delivery time fields, we allow the user agent to notify the user when the user submits the form without filling in those fields:

```
<form method="post"
      enctype="application/x-www-form-urlencoded"
      action="https://pizza.example.com/order.cgi">
 <p><label>Customer name: <input name="custname" required></label></p>
 <p><label>Telephone: <input type=tel name="custtel"></label></p>
 <p><label>Email address: <input type=email name="custemail"></label></p>
 <fieldset>
  <legend> Pizza Size </legend>
  <p><label> <input type=radio name=size required value="small"> Small </label></p>
  <p><label> <input type=radio name=size required value="medium"> Medium </label></p>
  <p><label> <input type=radio name=size required value="large"> Large </label></p>
 </fieldset>
 <fieldset>
  <legend> Pizza Toppings </legend>
  <p><label> <input type=checkbox name="topping" value="bacon"> Bacon </label></p>
  <p><label> <input type=checkbox name="topping" value="cheese"> Extra Cheese </label></p>
  <p><label> <input type=checkbox name="topping" value="onion"> Onion </label></p>
  <p><label> <input type=checkbox name="topping" value="mushroom"> Mushroom </label></p>
 </fieldset>
 <p><label>Preferred delivery time: <input type=time min="11:00" max="21:00" step="900" name="delivery" required></label></p>
 <p><label>Delivery instructions: <textarea name="comments"></textarea></label></p>
 <p><button>Submit order</button></p>
</form>
```

It is also possible to limit the length of the input, using the `maxlength` attribute. By adding this to the `textarea` element, we can limit users to 1000 characters, preventing them from writing huge essays to the busy delivery drivers instead of staying focused and to the point:

```
<form method="post"
      enctype="application/x-www-form-urlencoded"
      action="https://pizza.example.com/order.cgi">
 <p><label>Customer name: <input name="custname" required></label></p>
 <p><label>Telephone: <input type=tel name="custtel"></label></p>
 <p><label>Email address: <input type=email name="custemail"></label></p>
 <fieldset>
  <legend> Pizza Size </legend>
  <p><label> <input type=radio name=size required value="small"> Small </label></p>
  <p><label> <input type=radio name=size required value="medium"> Medium </label></p>
  <p><label> <input type=radio name=size required value="large"> Large </label></p>
 </fieldset>
 <fieldset>
  <legend> Pizza Toppings </legend>
  <p><label> <input type=checkbox name="topping" value="bacon"> Bacon </label></p>
  <p><label> <input type=checkbox name="topping" value="cheese"> Extra Cheese </label></p>
  <p><label> <input type=checkbox name="topping" value="onion"> Onion </label></p>
  <p><label> <input type=checkbox name="topping" value="mushroom"> Mushroom </label></p>
 </fieldset>
 <p><label>Preferred delivery time: <input type=time min="11:00" max="21:00" step="900" name="delivery" required></label></p>
 <p><label>Delivery instructions: <textarea name="comments" maxlength=1000></textarea></label></p>
 <p><button>Submit order</button></p>
</form>
```

When a form is submitted, `invalid` events are fired at each form control that is invalid. This can be useful for displaying a summary of the problems with the form, since typically the browser itself will only report one problem at a time.

##### 4.10.1.5 Enabling client-side automatic filling of form controls[](https://html.spec.whatwg.org/multipage/forms.html#enabling-client-side-automatic-filling-of-form-controls)

_This section is non-normative._

Some browsers attempt to aid the user by automatically filling form controls rather than having the user reenter their information each time. For example, a field asking for the user's telephone number can be automatically filled with the user's phone number.

To help the user agent with this, the `autocomplete` attribute can be used to describe the field's purpose. In the case of this form, we have three fields that can be usefully annotated in this way: the information about who the pizza is to be delivered to. Adding this information looks like this:

```
<form method="post"
      enctype="application/x-www-form-urlencoded"
      action="https://pizza.example.com/order.cgi">
 <p><label>Customer name: <input name="custname" required autocomplete="shipping name"></label></p>
 <p><label>Telephone: <input type=tel name="custtel" autocomplete="shipping tel"></label></p>
 <p><label>Email address: <input type=email name="custemail" autocomplete="shipping email"></label></p>
 <fieldset>
  <legend> Pizza Size </legend>
  <p><label> <input type=radio name=size required value="small"> Small </label></p>
  <p><label> <input type=radio name=size required value="medium"> Medium </label></p>
  <p><label> <input type=radio name=size required value="large"> Large </label></p>
 </fieldset>
 <fieldset>
  <legend> Pizza Toppings </legend>
  <p><label> <input type=checkbox name="topping" value="bacon"> Bacon </label></p>
  <p><label> <input type=checkbox name="topping" value="cheese"> Extra Cheese </label></p>
  <p><label> <input type=checkbox name="topping" value="onion"> Onion </label></p>
  <p><label> <input type=checkbox name="topping" value="mushroom"> Mushroom </label></p>
 </fieldset>
 <p><label>Preferred delivery time: <input type=time min="11:00" max="21:00" step="900" name="delivery" required></label></p>
 <p><label>Delivery instructions: <textarea name="comments" maxlength=1000></textarea></label></p>
 <p><button>Submit order</button></p>
</form>
```

##### 4.10.1.6 Improving the user experience on mobile devices[](https://html.spec.whatwg.org/multipage/forms.html#improving-the-user-experience-on-mobile-devices)

_This section is non-normative._

Some devices, in particular those with virtual keyboards can provide the user with multiple input modalities. For example, when typing in a credit card number the user may wish to only see keys for digits 0-9, while when typing in their name they may wish to see a form field that by default capitalizes each word.

Using the `inputmode` attribute we can select appropriate input modalities:

```
<form method="post"
      enctype="application/x-www-form-urlencoded"
      action="https://pizza.example.com/order.cgi">
 <p><label>Customer name: <input name="custname" required autocomplete="shipping name"></label></p>
 <p><label>Telephone: <input type=tel name="custtel" autocomplete="shipping tel"></label></p>
 <p><label>Buzzer code: <input name="custbuzz" inputmode="numeric"></label></p>
 <p><label>Email address: <input type=email name="custemail" autocomplete="shipping email"></label></p>
 <fieldset>
  <legend> Pizza Size </legend>
  <p><label> <input type=radio name=size required value="small"> Small </label></p>
  <p><label> <input type=radio name=size required value="medium"> Medium </label></p>
  <p><label> <input type=radio name=size required value="large"> Large </label></p>
 </fieldset>
 <fieldset>
  <legend> Pizza Toppings </legend>
  <p><label> <input type=checkbox name="topping" value="bacon"> Bacon </label></p>
  <p><label> <input type=checkbox name="topping" value="cheese"> Extra Cheese </label></p>
  <p><label> <input type=checkbox name="topping" value="onion"> Onion </label></p>
  <p><label> <input type=checkbox name="topping" value="mushroom"> Mushroom </label></p>
 </fieldset>
 <p><label>Preferred delivery time: <input type=time min="11:00" max="21:00" step="900" name="delivery" required></label></p>
 <p><label>Delivery instructions: <textarea name="comments" maxlength=1000></textarea></label></p>
 <p><button>Submit order</button></p>
</form>
```

##### 4.10.1.7 The difference between the field type, the autofill field name, and the input modality[](https://html.spec.whatwg.org/multipage/forms.html#the-difference-between-the-field-type,-the-autofill-field-name,-and-the-input-modality)

_This section is non-normative._

The `type`, `autocomplete`, and `inputmode` attributes can seem confusingly similar. For instance, in all three cases, the string "`email`" is a valid value. This section attempts to illustrate the difference between the three attributes and provides advice suggesting how to use them.

The `type` attribute on `input` elements decides what kind of control the user agent will use to expose the field. Choosing between different values of this attribute is the same choice as choosing whether to use an `input` element, a `textarea` element, a `select` element, etc.

The `autocomplete` attribute, in contrast, describes what the value that the user will enter actually represents. Choosing between different values of this attribute is the same choice as choosing what the label for the element will be.

First, consider telephone numbers. If a page is asking for a telephone number from the user, the right form control to use is `<input type=tel>`. However, which `autocomplete` value to use depends on which phone number the page is asking for, whether they expect a telephone number in the international format or just the local format, and so forth.

For example, a page that forms part of a checkout process on an e-commerce site for a customer buying a gift to be shipped to a friend might need both the buyer's telephone number (in case of payment issues) and the friend's telephone number (in case of delivery issues). If the site expects international phone numbers (with the country code prefix), this could thus look like this:

```
<p><label>Your phone number: <input type=tel name=custtel autocomplete="billing tel"></label>
<p><label>Recipient's phone number: <input type=tel name=shiptel autocomplete="shipping tel"></label>
<p>Please enter complete phone numbers including the country code prefix, as in "+1 555 123 4567".
```

But if the site only supports British customers and recipients, it might instead look like this (notice the use of `tel-national` rather than `tel`):

```
<p><label>Your phone number: <input type=tel name=custtel autocomplete="billing tel-national"></label>
<p><label>Recipient's phone number: <input type=tel name=shiptel autocomplete="shipping tel-national"></label>
<p>Please enter complete UK phone numbers, as in "(01632) 960 123".
```

Now, consider a person's preferred languages. The right `autocomplete` value is `language`. However, there could be a number of different form controls used for the purpose: a text control (`<input type=text>`), a drop-down list (`<select>`), radio buttons (
```
<input
  type=radio>
```
), etc. It only depends on what kind of interface is desired.

Finally, consider names. If a page just wants one name from the user, then the relevant control is `<input type=text>`. If the page is asking for the user's full name, then the relevant `autocomplete` value is `name`.

```
<p><label>Japanese name: <input name="j" type="text" autocomplete="section-jp name"></label>
<label>Romanized name: <input name="e" type="text" autocomplete="section-en name"></label>
```

In this example, the "`section-*`" keywords in the `autocomplete` attributes' values tell the user agent that the two fields expect _different_ names. Without them, the user agent could automatically fill the second field with the value given in the first field when the user gave a value to the first field.

The "`-jp`" and "`-en`" parts of the keywords are opaque to the user agent; the user agent cannot guess, from those, that the two names are expected to be in Japanese and English respectively.

Separate from the choices regarding `type` and `autocomplete`, the `inputmode` attribute decides what kind of input modality (e.g., virtual keyboard) to use, when the control is a text control.

Consider credit card numbers. The appropriate input type is _not_`<input type=number>`, [as explained below](https://html.spec.whatwg.org/multipage/input.html#when-number-is-not-appropriate); it is instead `<input type=text>`. To encourage the user agent to use a numeric input modality anyway (e.g., a virtual keyboard displaying only digits), the page would use

```
<p><label>Credit card number:
                <input name="cc" type="text" inputmode="numeric" pattern="[0-9]{8,19}" autocomplete="cc-number">
</label></p>
```

_This section is non-normative._

In this pizza delivery example, the times are specified in the format "HH:MM": two digits for the hour, in 24-hour format, and two digits for the time. (Seconds could also be specified, though they are not necessary in this example.)

In some locales, however, times are often expressed differently when presented to users. For example, in the United States, it is still common to use the 12-hour clock with an am/pm indicator, as in "2pm". In France, it is common to separate the hours from the minutes using an "h" character, as in "14h00".

Similar issues exist with dates, with the added complication that even the order of the components is not always consistent — for example, in Cyprus the first of February 2003 would typically be written "1/2/03", while that same date in Japan would typically be written as "2003年02月01日" — and even with numbers, where locales differ, for example, in what punctuation is used as the decimal separator and the thousands separator.

It is therefore important to distinguish the time, date, and number formats used in HTML and in form submissions, which are always the formats defined in this specification (and based on the well-established ISO 8601 standard for computer-readable date and time formats), from the time, date, and number formats presented to the user by the browser and accepted as input from the user by the browser.

The format used "on the wire", i.e., in HTML markup and in form submissions, is intended to be computer-readable and consistent irrespective of the user's locale. Dates, for instance, are always written in the format "YYYY-MM-DD", as in "2003-02-01". While some users might see this format, others might see it as "01.02.2003" or "February 1, 2003".

The time, date, or number given by the page in the wire format is then translated to the user's preferred presentation (based on user preferences or on the locale of the page itself), before being displayed to the user. Similarly, after the user inputs a time, date, or number using their preferred format, the user agent converts it back to the wire format before putting it in the DOM or submitting it.

This allows scripts in pages and on servers to process times, dates, and numbers in a consistent manner without needing to support dozens of different formats, while still supporting the users' needs.

See also the [implementation notes](https://html.spec.whatwg.org/multipage/input.html#input-impl-notes) regarding localization of form controls.

#### 4.10.2 Categories[](https://html.spec.whatwg.org/multipage/forms.html#categories)

Mostly for historical reasons, elements in this section fall into several overlapping (but subtly different) categories in addition to the usual ones like [flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2), [phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), and [interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2).

A number of the elements are form-associated elements, which means they can have a [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner).

*   `button`
*   `fieldset`
*   `input`
*   `object`
*   `output`
*   `select`
*   `textarea`
*   `img`
*   [form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element)

The [form-associated elements](https://html.spec.whatwg.org/multipage/forms.html#form-associated-element) fall into several subcategories:

Listed elements
Denotes elements that are listed in the `form.elements` and `fieldset.elements` APIs. These elements also have a `form` content attribute, and a matching `form` IDL attribute, that allow authors to specify an explicit [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner).

*   `button`
*   `fieldset`
*   `input`
*   `object`
*   `output`
*   `select`
*   `textarea`
*   [form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element)

Submittable elements
Denotes elements that can be used for [constructing the entry list](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#constructing-the-form-data-set) when a `form` element is [submitted](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-form-submit).

*   `button`
*   `input`
*   `select`
*   `textarea`
*   [form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element)

Some [submittable elements](https://html.spec.whatwg.org/multipage/forms.html#category-submit) can be, depending on their attributes, buttons. The prose below defines when an element is a button. Some buttons are specifically submit buttons.

Resettable elements
Denotes elements that can be affected when a `form` element is [reset](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-form-reset).

*   `input`
*   `output`
*   `select`
*   `textarea`
*   [form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element)

Autocapitalize-and-autocorrect-inheriting elements
Denotes elements that inherit the `autocapitalize` and `autocorrect` attributes from their [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner).

*   `button`
*   `fieldset`
*   `input`
*   `output`
*   `select`
*   `textarea`

Some elements, not all of them [form-associated](https://html.spec.whatwg.org/multipage/forms.html#form-associated-element), are categorized as labelable elements. These are elements that can be associated with a `label` element.

*   `button`
*   `input` (if the `type` attribute is _not_ in the [Hidden](https://html.spec.whatwg.org/multipage/input.html#hidden-state-(type=hidden)) state)
*   `meter`
*   `output`
*   `progress`
*   `select`
*   `textarea`
*   [form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element)

#### 4.10.3 The `form` element[](https://html.spec.whatwg.org/multipage/forms.html#the-form-element)

[Element/form](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form "The <form> HTML element represents a document section containing interactive controls for submitting information.")

Support in all current engines.

Firefox 1+Safari 4+Chrome 1+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLFormElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement "The HTMLFormElement interface represents a <form> element in the DOM. It allows access to—and, in some cases, modification of—aspects of the form, as well as access to its component elements.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 8+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

[HTMLFormElement/acceptCharset](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/acceptCharset "The HTMLFormElement.acceptCharset property represents a list of the supported character encodings for the given <form> element. This list can be comma-separated or space-separated.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[HTMLFormElement/name](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/name "The HTMLFormElement.name property represents the name of the current <form> element as a string.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[HTMLFormElement/target](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/target "The target property of the HTMLFormElement interface represents the target of the form's action (i.e., the frame in which to render its output).")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) is expected.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2), but with no `form` element descendants.[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`accept-charset` — Character encodings to use for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2)`action` — [URL](https://url.spec.whatwg.org/#concept-url) to use for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2)`autocomplete` — Default setting for autofill feature for controls in the form `enctype` — [Entry list](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#entry-list) encoding type to use for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2)`method` — Variant to use for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2)`name` — Name of form to use in the `document.forms` API `novalidate` — Bypass form control validation for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2)`target` — [Navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) for [form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-submission-2)`rel`[Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-form).[For implementers](https://w3c.github.io/html-aam/#el-form).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window,
 LegacyOverrideBuiltIns,
 LegacyUnenumerableNamedProperties]
interface HTMLFormElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, Reflect="accept-charset"] attribute DOMString acceptCharset;
  [CEReactions, ReflectSetter] attribute USVString action;
  [CEReactions] attribute DOMString autocomplete;
  [CEReactions] attribute DOMString enctype;
  [CEReactions] attribute DOMString encoding;
  [CEReactions] attribute DOMString method;
  [CEReactions, Reflect] attribute DOMString name;
  [CEReactions, Reflect] attribute boolean noValidate;
  [CEReactions, Reflect] attribute DOMString target;
  [CEReactions, Reflect] attribute DOMString rel;
  [SameObject, PutForwards=value, Reflect="rel"] readonly attribute DOMTokenList relList;

  [SameObject] readonly attribute HTMLFormControlsCollection elements;
  readonly attribute unsigned long length;
  getter Element (unsigned long index);
  getter (RadioNodeList or Element) (DOMString name);

  undefined submit();
  undefined requestSubmit(optional HTMLElement? submitter = null);
  [CEReactions] undefined reset();
  boolean checkValidity();
  boolean reportValidity();
};
```

The `form` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) a [hyperlink](https://html.spec.whatwg.org/multipage/links.html#hyperlink) that can be manipulated through a collection of [form-associated elements](https://html.spec.whatwg.org/multipage/forms.html#form-associated-element), some of which can represent editable values that can be submitted to a server for processing.

The `accept-charset` attribute gives the character encodings that are to be used for the submission. If specified, the value must be an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for "`UTF-8`". [[ENCODING]](https://html.spec.whatwg.org/multipage/references.html#refsENCODING)

The `name` attribute represents the `form`'s name within the `forms` collection. The value must not be the empty string, and the value must be unique amongst the `form` elements in the `forms` collection that it is in, if any.

The `autocomplete` attribute is an [enumerated attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#enumerated-attribute) with the following keywords and states:

| Keyword | State | Brief description |
| --- | --- | --- |
| `on` | On | Form controls will have their [autofill field name](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill-field-name) set to "`on`" by default. |
| `off` | Off | Form controls will have their [autofill field name](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#autofill-field-name) set to "`off`" by default. |

The `action`, `enctype`, `method`, `novalidate`, and `target` attributes are [attributes for form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attributes-for-form-submission).

The `rel` attribute on `form` elements controls what kinds of links the elements create. The attribute's value must be a [unordered set of unique space-separated tokens](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#unordered-set-of-unique-space-separated-tokens). The [allowed keywords and their meanings](https://html.spec.whatwg.org/multipage/links.html#linkTypes) are defined in an earlier section.

`rel`'s [supported tokens](https://dom.spec.whatwg.org/#concept-supported-tokens) are the keywords defined in [HTML link types](https://html.spec.whatwg.org/multipage/links.html#linkTypes) which are allowed on `form` elements, impact the processing model, and are supported by the user agent. The possible [supported tokens](https://dom.spec.whatwg.org/#concept-supported-tokens) are `noreferrer`, `noopener`, and `opener`. `rel`'s [supported tokens](https://dom.spec.whatwg.org/#concept-supported-tokens) must only include the tokens from this list that the user agent implements the processing model for.

`form.elements`

[HTMLFormElement/elements](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/elements "The HTMLFormElement property elements returns an HTMLFormControlsCollection listing all the form controls contained in the <form> element.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 8+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

Returns an `HTMLFormControlsCollection` of the form controls in the form (excluding image buttons for historical reasons).

`form.length`

[HTMLFormElement/length](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/length "The HTMLFormElement.length read-only property returns the number of controls in the <form> element.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

Returns the number of form controls in the form (excluding image buttons for historical reasons).

`form[index]`
Returns the index th element in the form (excluding image buttons for historical reasons).

`form[name]`
Returns the form control (or, if there are several, a `RadioNodeList` of the form controls) in the form with the given [ID](https://dom.spec.whatwg.org/#concept-id) or `name` (excluding image buttons for historical reasons); or, if there are none, returns the `img` element with the given ID.

Once an element has been referenced using a particular name, that name will continue being available as a way to reference that element in this method, even if the element's actual [ID](https://dom.spec.whatwg.org/#concept-id) or `name` changes, for as long as the element remains in the [tree](https://dom.spec.whatwg.org/#concept-tree).

If there are multiple matching items, then a `RadioNodeList` object containing all those elements is returned.

`form.submit()`

[HTMLFormElement/submit](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/submit "The HTMLFormElement.submit() method submits a given <form>.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

Submits the form, bypassing [interactive constraint validation](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#interactively-validate-the-constraints) and without firing a `submit` event.

`form.requestSubmit([ submitter ])`

[HTMLFormElement/requestSubmit](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/requestSubmit "The HTMLFormElement method requestSubmit() requests that the form be submitted using a specific submit button.")

Support in all current engines.

Firefox 75+Safari 16+Chrome 76+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Requests to submit the form. Unlike `submit()`, this method includes [interactive constraint validation](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#interactively-validate-the-constraints) and firing a `submit` event, either of which can cancel submission.

The submitter argument can be used to point to a specific [submit button](https://html.spec.whatwg.org/multipage/forms.html#concept-submit-button), whose `formaction`, `formenctype`, `formmethod`, `formnovalidate`, and `formtarget` attributes can impact submission. Additionally, the submitter will be included when [constructing the entry list](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#constructing-the-form-data-set) for submission; normally, buttons are excluded.

`form.reset()`

[HTMLFormElement/reset](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/reset "The HTMLFormElement.reset() method restores a form element's default values. This method does the same thing as clicking the form's <input type=\"reset\"> control.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 8+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

Resets the form.

`form.checkValidity()`
Returns true if the form's controls are all valid; otherwise, returns false.

`form.reportValidity()`
Returns true if the form's controls are all valid; otherwise, returns false and informs the user.

* * *

The `elements` IDL attribute must return an `HTMLFormControlsCollection` rooted at the `form` element's [root](https://dom.spec.whatwg.org/#concept-tree-root), whose filter matches [listed elements](https://html.spec.whatwg.org/multipage/forms.html#category-listed) whose [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner) is the `form` element, with the exception of `input` elements whose `type` attribute is in the [Image Button](https://html.spec.whatwg.org/multipage/input.html#image-button-state-(type=image)) state, which must, for historical reasons, be excluded from this particular collection.

The `length` IDL attribute must return the number of nodes [represented](https://dom.spec.whatwg.org/#represented-by-the-collection) by the `elements` collection.

The [supported property indices](https://webidl.spec.whatwg.org/#dfn-supported-property-indices) at any instant are the indices supported by the object returned by the `elements` attribute at that instant.

To [determine the value of an indexed property](https://webidl.spec.whatwg.org/#dfn-determine-the-value-of-an-indexed-property) for a `form` element, the user agent must return the value returned by the `item` method on the `elements` collection, when invoked with the given index as its argument.

* * *

Each `form` element has a mapping of names to elements called the past names map. It is used to persist names of controls even when they change names.

The [supported property names](https://webidl.spec.whatwg.org/#dfn-supported-property-names) consist of the names obtained from the following algorithm, in the order obtained from this algorithm:

1.   Let sourced names be an initially empty ordered list of tuples consisting of a string, an element, a source, where the source is either _id_, _name_, or _past_, and, if the source is _past_, an age.

2.   For each [listed element](https://html.spec.whatwg.org/multipage/forms.html#category-listed)candidate whose [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner) is the `form` element, with the exception of any `input` elements whose `type` attribute is in the [Image Button](https://html.spec.whatwg.org/multipage/input.html#image-button-state-(type=image)) state:

    1.   If candidate has an `id` attribute, add an entry to sourced names with that `id` attribute's value as the string, candidate as the element, and _id_ as the source.

    2.   If candidate has a `name` attribute, add an entry to sourced names with that `name` attribute's value as the string, candidate as the element, and _name_ as the source.

3.   For each `img` element candidate whose [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner) is the `form` element:

    1.   If candidate has an `id` attribute, add an entry to sourced names with that `id` attribute's value as the string, candidate as the element, and _id_ as the source.

    2.   If candidate has a `name` attribute, add an entry to sourced names with that `name` attribute's value as the string, candidate as the element, and _name_ as the source.

4.   For each entry past entry in the [past names map](https://html.spec.whatwg.org/multipage/forms.html#past-names-map), add an entry to sourced names with the past entry's name as the string, past entry's element as the element, _past_ as the source, and the length of time past entry has been in the [past names map](https://html.spec.whatwg.org/multipage/forms.html#past-names-map) as the age.

5.   Sort sourced names by [tree order](https://dom.spec.whatwg.org/#concept-tree-order) of the element entry of each tuple, sorting entries with the same element by putting entries whose source is _id_ first, then entries whose source is _name_, and finally entries whose source is _past_, and sorting entries with the same element and source by their age, oldest first.

6.   Remove any entries in sourced names that have the empty string as their name.

7.   Remove any entries in sourced names that have the same name as an earlier entry in the map.

8.   Return the list of names from sourced names, maintaining their relative order.

To [determine the value of a named property](https://webidl.spec.whatwg.org/#dfn-determine-the-value-of-a-named-property)name for a `form` element, the user agent must run the following steps:

1.   Let candidates be a [live](https://html.spec.whatwg.org/multipage/infrastructure.html#live)`RadioNodeList` object containing all the [listed elements](https://html.spec.whatwg.org/multipage/forms.html#category-listed), whose [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner) is the `form` element, that have either an `id` attribute or a `name` attribute equal to name, with the exception of `input` elements whose `type` attribute is in the [Image Button](https://html.spec.whatwg.org/multipage/input.html#image-button-state-(type=image)) state, in [tree order](https://dom.spec.whatwg.org/#concept-tree-order).

2.   If candidates is empty, let candidates be a [live](https://html.spec.whatwg.org/multipage/infrastructure.html#live)`RadioNodeList` object containing all the `img` elements, whose [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner) is the `form` element, that have either an `id` attribute or a `name` attribute equal to name, in [tree order](https://dom.spec.whatwg.org/#concept-tree-order).

3.   If candidates is empty, name is the name of one of the entries in the `form` element's [past names map](https://html.spec.whatwg.org/multipage/forms.html#past-names-map): return the object associated with name in that map.

4.   If candidates contains more than one node, return candidates.

5.   Otherwise, candidates contains exactly one node. Add a mapping from name to the node in candidates in the `form` element's [past names map](https://html.spec.whatwg.org/multipage/forms.html#past-names-map), replacing the previous entry with the same name, if any.

6.   Return the node in candidates.

If an element listed in a `form` element's [past names map](https://html.spec.whatwg.org/multipage/forms.html#past-names-map) changes [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner), then its entries must be removed from that map.

* * *

The `requestSubmit(submitter)` method, when invoked, must run the following steps:

1.   If submitter is not null, then:

    1.   If submitter is not a [submit button](https://html.spec.whatwg.org/multipage/forms.html#concept-submit-button), then throw a `TypeError`.

    2.   If submitter's [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner) is not this `form` element, then throw a ["`NotFoundError`"](https://webidl.spec.whatwg.org/#notfounderror)`DOMException`.

2.   Otherwise, set submitter to this `form` element.

3.   [Submit](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-form-submit) this `form` element, from submitter.

The `reset()` method, when invoked, must run the following steps:

1.   If the `form` element is marked as _[locked for reset](https://html.spec.whatwg.org/multipage/forms.html#locked-for-reset)_, then return.

2.   Mark the `form` element as locked for reset.

3.   [Reset](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#concept-form-reset) the `form` element.

4.   Unmark the `form` element as _[locked for reset](https://html.spec.whatwg.org/multipage/forms.html#locked-for-reset)_.

If the `checkValidity()` method is invoked, the user agent must [statically validate the constraints](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#statically-validate-the-constraints) of the `form` element, and return true if the constraint validation returned a _positive_ result, and false if it returned a _negative_ result.

If the `reportValidity()` method is invoked, the user agent must [interactively validate the constraints](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#interactively-validate-the-constraints) of the `form` element, and return true if the constraint validation returned a _positive_ result, and false if it returned a _negative_ result.

This example shows two search forms:

```
<form action="https://www.google.com/search" method="get">
 <label>Google: <input type="search" name="q"></label> <input type="submit" value="Search...">
</form>
<form action="https://www.bing.com/search" method="get">
 <label>Bing: <input type="search" name="q"></label> <input type="submit" value="Search...">
</form>
```

#### 4.10.4 The `label` element[](https://html.spec.whatwg.org/multipage/forms.html#the-label-element)

[Element/label](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label "The <label> HTML element represents a caption for an item in a user interface.")

Support in all current engines.

Firefox 1+Safari 4+Chrome 1+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLLabelElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement "The HTMLLabelElement interface gives access to properties specific to <label> elements. It inherits methods and properties from the base HTMLElement interface.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android 37+Samsung Internet?Opera Android 12.1+

[HTMLLabelElement/htmlFor](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/htmlFor "The HTMLLabelElement.htmlFor property reflects the value of the for content property. That means that this script-accessible property is used to set and read the value of the content property for, which is the ID of the label's associated control element.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).[Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2).[Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) is expected.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), but with no descendant [labelable elements](https://html.spec.whatwg.org/multipage/forms.html#category-label) unless it is the element's [labeled control](https://html.spec.whatwg.org/multipage/forms.html#labeled-control), and no descendant `label` elements.[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`for` — Associate the label with form control [Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-label).[For implementers](https://w3c.github.io/html-aam/#el-label).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLLabelElement : HTMLElement {
  [HTMLConstructor] constructor();

  readonly attribute HTMLFormElement? form;
  [CEReactions, Reflect="for"] attribute DOMString htmlFor;
  readonly attribute HTMLElement? control;
};
```

The `label` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) a caption in a user interface. The caption can be associated with a specific form control, known as the `label` element's labeled control, either using the `for` attribute, or by putting the form control inside the `label` element itself.

Except where otherwise specified by the following rules, a `label` element has no [labeled control](https://html.spec.whatwg.org/multipage/forms.html#labeled-control).

[Attributes/for](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/for "The for attribute is an allowed attribute for <label> and <output>. When used on a <label> element it indicates the form element that this label describes. When used on an <output> element it allows for an explicit relationship between the elements that represent values which are used in the output.")

Support in all current engines.

Firefox 1+Safari 4+Chrome 1+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `for` attribute may be specified to indicate a form control with which the caption is to be associated. If the attribute is specified, the attribute's value must be the [ID](https://dom.spec.whatwg.org/#concept-id) of a [labelable element](https://html.spec.whatwg.org/multipage/forms.html#category-label) in the same [tree](https://dom.spec.whatwg.org/#concept-tree) as the `label` element. If the attribute is specified and there is an element in the [tree](https://dom.spec.whatwg.org/#concept-tree) whose [ID](https://dom.spec.whatwg.org/#concept-id) is equal to the value of the `for` attribute, and the first such element in [tree order](https://dom.spec.whatwg.org/#concept-tree-order) is a [labelable element](https://html.spec.whatwg.org/multipage/forms.html#category-label), then that element is the `label` element's [labeled control](https://html.spec.whatwg.org/multipage/forms.html#labeled-control).

If the `for` attribute is not specified, but the `label` element has a [labelable element](https://html.spec.whatwg.org/multipage/forms.html#category-label) descendant, then the first such descendant in [tree order](https://dom.spec.whatwg.org/#concept-tree-order) is the `label` element's [labeled control](https://html.spec.whatwg.org/multipage/forms.html#labeled-control).

The `label` element's exact default presentation and behavior, in particular what its [activation behavior](https://dom.spec.whatwg.org/#eventtarget-activation-behavior) might be, if anything, should match the platform's label behavior. The [activation behavior](https://dom.spec.whatwg.org/#eventtarget-activation-behavior) of a `label` element for events targeted at [interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) descendants of a `label` element, and any descendants of those [interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2) descendants, must be to do nothing.

[Form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) are [labelable elements](https://html.spec.whatwg.org/multipage/forms.html#category-label), so for user agents where the `label` element's [activation behavior](https://dom.spec.whatwg.org/#eventtarget-activation-behavior) impacts the [labeled control](https://html.spec.whatwg.org/multipage/forms.html#labeled-control), both built-in and custom elements will be impacted.

For example, on platforms where clicking a label activates the form control, clicking the `label` in the following snippet could trigger the user agent to [fire a `click` event](https://html.spec.whatwg.org/multipage/webappapis.html#fire-a-click-event) at the `input` element, as if the element itself had been triggered by the user:

`<label><input type=checkbox name=lost> Lost</label>`
Similarly, assuming `my-checkbox` was declared as a [form-associated custom element](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element) (like in [this example](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-elements-face-example)), then the code

`<label><my-checkbox name=lost></my-checkbox> Lost</label>`
would have the same behavior, [firing a `click` event](https://html.spec.whatwg.org/multipage/webappapis.html#fire-a-click-event) at the `my-checkbox` element.

On other platforms, the behavior in both cases might be just to focus the control, or to do nothing.

The following example shows three form controls each with a label, two of which have small text showing the right format for users to use.

```
<p><label>Full name: <input name=fn> <small>Format: First Last</small></label></p>
<p><label>Age: <input name=age type=number min=0></label></p>
<p><label>Post code: <input name=pc> <small>Format: AB12 3CD</small></label></p>
```

`label.control`

[HTMLLabelElement/control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control "The read-only HTMLLabelElement.control property returns a reference to the control (in the form of an object of type HTMLElement or one of its derivatives) with which the <label> element is associated, or null if the label isn't associated with a control.")

Support in all current engines.

Firefox 4+Safari 5.1+Chrome 6+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)18 Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 3+Samsung Internet?Opera Android 12.1+

Returns the form control that is associated with this element.

`label.form`

[HTMLLabelElement/form](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/form "The read-only HTMLLabelElement.form property returns an HTMLFormElement object which represents the form of which the label's associated control is a part, or null if there is either no associated control, or if that control isn't in a form.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 6+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

Returns the [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner) of the form control that is associated with this element.

Returns null if there isn't one.

The `control` IDL attribute must return the `label` element's [labeled control](https://html.spec.whatwg.org/multipage/forms.html#labeled-control), if any, or null if there isn't one.

The `form` IDL attribute must run the following steps:

1.   If the `label` element has no [labeled control](https://html.spec.whatwg.org/multipage/forms.html#labeled-control), then return null.

2.   If the `label` element's [labeled control](https://html.spec.whatwg.org/multipage/forms.html#labeled-control) is not a [form-associated element](https://html.spec.whatwg.org/multipage/forms.html#form-associated-element), then return null.

3.   Return the `label` element's [labeled control](https://html.spec.whatwg.org/multipage/forms.html#labeled-control)'s [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner) (which can still be null).

The `form` IDL attribute on the `label` element is different from the `form` IDL attribute on [listed](https://html.spec.whatwg.org/multipage/forms.html#category-listed)[form-associated elements](https://html.spec.whatwg.org/multipage/forms.html#form-associated-element), and the `label` element does not have a `form` content attribute.

* * *

`control.labels`

[HTMLButtonElement/labels](https://developer.mozilla.org/en-US/docs/Web/API/HTMLButtonElement/labels "The HTMLButtonElement.labels read-only property returns a NodeList of the <label> elements associated with the <button> element.")

Support in all current engines.

Firefox 56+Safari 5.1+Chrome 6+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)18 Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 3+Samsung Internet?Opera Android 12.1+

[HTMLInputElement/labels](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/labels "The HTMLInputElement.labels read-only property returns a NodeList of the <label> elements associated with the <input> element, if the element is not hidden. If the element has the type hidden, the property returns null.")

Support in all current engines.

Firefox 56+Safari 5+Chrome 6+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)18 Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 3+Samsung Internet?Opera Android 12.1+

[HTMLMeterElement/labels](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMeterElement/labels "The HTMLMeterElement.labels read-only property returns a NodeList of the <label> elements associated with the <meter> element.")

Support in all current engines.

Firefox 56+Safari 6+Chrome 6+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)18 Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[HTMLOutputElement/labels](https://developer.mozilla.org/en-US/docs/Web/API/HTMLOutputElement/labels "The HTMLOutputElement.labels read-only property returns a NodeList of the <label> elements associated with the <output> element.")

Support in all current engines.

Firefox 56+Safari 5.1+Chrome 9+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)18 Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 3+Samsung Internet?Opera Android 12.1+

[HTMLProgressElement/labels](https://developer.mozilla.org/en-US/docs/Web/API/HTMLProgressElement/labels "The HTMLProgressElement.labels read-only property returns a NodeList of the <label> elements associated with the <progress> element.")

Support in all current engines.

Firefox 56+Safari 6+Chrome 6+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)18 Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[HTMLSelectElement/labels](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/labels "The HTMLSelectElement.labels read-only property returns a NodeList of the <label> elements associated with the <select> element.")

Support in all current engines.

Firefox 56+Safari 5.1+Chrome 6+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)18 Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 3+Samsung Internet?Opera Android 12.1+

[HTMLTextAreaElement/labels](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTextAreaElement/labels "The HTMLTextAreaElement.labels read-only property returns a NodeList of the <label> elements associated with the <textarea> element.")

Support in all current engines.

Firefox 56+Safari 5.1+Chrome 6+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)18 Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 3+Samsung Internet?Opera Android 12.1+

Returns a `NodeList` of all the `label` elements that the form control is associated with.

[Labelable elements](https://html.spec.whatwg.org/multipage/forms.html#category-label) and all `input` elements have a [live](https://html.spec.whatwg.org/multipage/infrastructure.html#live)`NodeList` object associated with them that represents the list of `label` elements, in [tree order](https://dom.spec.whatwg.org/#concept-tree-order), whose [labeled control](https://html.spec.whatwg.org/multipage/forms.html#labeled-control) is the element in question. The `labels` IDL attribute of [labelable elements](https://html.spec.whatwg.org/multipage/forms.html#category-label) that are not [form-associated custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#form-associated-custom-element), and the `labels` IDL attribute of `input` elements, on getting, must return that `NodeList` object, and that same value must always be returned, unless this element is an `input` element whose `type` attribute is in the [Hidden](https://html.spec.whatwg.org/multipage/input.html#hidden-state-(type=hidden)) state, in which case it must instead return null.

[ElementInternals/labels](https://developer.mozilla.org/en-US/docs/Web/API/ElementInternals/labels "The labels read-only property of the ElementInternals interface returns the labels associated with the element.")

Support in all current engines.

Firefox 98+Safari 16.4+Chrome 77+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

This (non-conforming) example shows what happens to the `NodeList` and what `labels` returns when an `input` element has its `type` attribute changed.

```
<!doctype html>
<p><label><input></label></p>
<script>
 const input = document.querySelector('input');
 const labels = input.labels;
 console.assert(labels.length === 1);

 input.type = 'hidden';
 console.assert(labels.length === 0); // the input is no longer the label's labeled control
 console.assert(input.labels === null);

 input.type = 'checkbox';
 console.assert(labels.length === 1); // the input is once again the label's labeled control
 console.assert(input.labels === labels); // same value as returned originally
</script>
```

[← 4.9 Tabular data](https://html.spec.whatwg.org/multipage/tables.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [4.10.5 The input element →](https://html.spec.whatwg.org/multipage/input.html)
