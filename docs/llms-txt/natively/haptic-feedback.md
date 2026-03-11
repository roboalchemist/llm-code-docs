# Source: https://docs.buildnatively.com/guides/integration/haptic-feedback.md

# Haptic Feedback

* [Bubble.io Plugin](#bubble.io-plugin)
* [JavaScript SDK](#javascript-sdk)

### 🧋 Bubble.io Plugin

#### \[Action] Natively - Haptic Impact

* Type - LIGHT,MEDIUM,HEAVY,RIGID or SOFT

#### \[Action] Natively - Haptic Notification

* Type - SUCCESS, ERROR, or WARNING

#### \[Action] Natively - Haptic Pattern

* Pattern - as a text (example: ..oO-Oo..)\
  Use pattern symbols to represent custom vibrations.
  * `O` - heavy impact
  * `o` - medium impact
  * `.` - light impact
  * `X` - rigid impact
  * `x` - soft impact
  * `-` - wait 0.1 second
* Delay - number (example: 0.1)

### 🛠 JavaScript SDK

#### Haptic Impact

{% code overflow="wrap" lineNumbers="true" %}

```javascript
const type = "LIGHT"; // LIGHT,MEDIUM,HEAVY,RIGID or SOFT
window.natively.hapticImpact(type);
```

{% endcode %}

#### Haptic Notification

{% code overflow="wrap" lineNumbers="true" %}

```javascript
const type = "SUCCESS"; // SUCCESS, ERROR, or WARNING
window.natively.hapticNotification(type);
```

{% endcode %}

#### Haptic Pattern

```javascript
// 'O' heavy impact 
// 'o' medium impact 
// '.' light impact 
// 'X' rigid impact 
// 'x' soft impact 
// '-' wait 0.1 second
const pattern = "..oO-Oo.."; 
const delay = 0.1; //
window.natively.hapticPattern(pattern, delay);
```
