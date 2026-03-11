# Source: https://docs.buildnatively.com/guides/integration/date-picker.md

# Date Picker

* [Bubble.io Plugin](#bubble.io-plugin)
* [JavaScript SDK](#javascript-sdk)

### 🧋 Bubble.io Plugin

#### \[Element] Natively - Date Picker

#### Events:

* Date selected
* Date Picker closed

#### States:

* Selected Date

#### Actions:

* Show Date Picker
  * Title
  * **Description \[iOS]**
  * Type - DATE, DATE\_AND\_TIME, or TIME
  * **Style \[iOS]** - DARK or LIGHT

### 🛠 JavaScript SDK

#### NativelyDatePicker

{% code overflow="wrap" lineNumbers="true" %}

```javascript
const picker = new NativelyDatePicker()
const datepicker_callback = function (resp) {
    const milliseconds = Number(resp.date);
    console.log(new Date(milliseconds));
};
const title = "Select Date";
const description = "";
const type = "DATE_AND_TIME" // "DATE"/"TIME"/"DATE_AND_TIME"
const style = "LIGHT" // "LIGHT"/"DARK"
picker.showDatePicker(title, description, type, style, datepicker_callback);
```

{% endcode %}
