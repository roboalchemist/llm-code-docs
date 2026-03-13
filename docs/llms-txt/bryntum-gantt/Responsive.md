# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/mixin/Responsive.md

# [Responsive](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Responsive)

This mixin provides management of a named set of [ResponsiveState](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#typedef-ResponsiveState) objects that are conditionally applied in response to the widget's size or other platform details. The names of the [ResponsiveState](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#typedef-ResponsiveState) objects are the keys of the [responsive](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#config-responsive) config object.

This allows all Bryntum components to operate in a mobile-friendly way by adapting to the size of the device they are being used on. For example:

```
 class ResponsiveButton extends Button.mixin(Responsive) {
     static configurable = {
         responsive : {
             small : {
                 // this is a ResponsiveState object named "small"
                 text : 'S'
             },
             medium : {
                 text : 'M'
             }
             large : {
                 text : 'L'
             }
         }
     };
 }
```

When the conditions are right for the button to be in the `'small'` responsive state, the `text` config will be set to `'S'`.

Any desired configs can be present in a [ResponsiveState](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#typedef-ResponsiveState) object, however, the `when` and `callback` properties have special meaning to this mixin and are reserved.

Selecting the Responsive State
------------------------------

To determine the current responsive state, the `when` property is consulted for each candidate state.

If `when` is a number, it is understood to be a width threshold and, if the widget's `width` is equal or less than that value, the score is that value. For example, a value of 400 would produce a score of 400 if the widget's width were less than or equal to 400. If the widget's width is greater than 400, the state would be skipped.

If `when` is a function, it is called with two parameters: a readonly reference to the widget and the [BrowserHelper](https://bryntum.com/docs/gantt/api/#Core/helper/BrowserHelper) singleton object. The function should return the numeric score if the state is applicable, or `null` or `false` if the state should be skipped.

The state that has the minimum score is selected as the responsive state for the widget.

Consider the default responsive states and their `when` values:

```
 responsive : {
     small : {
         when : 400
     },

     medium : {
         when : 800
     },

     large : {
         when : () => Infinity
     },

     '*' : {}
 },
```

For example, if the width of the widget is 300: the score for the `small` responsive state is 400, the score for the `medium` responsive state is 800, and the score for `large` is infinity. In effect, the `large` state is always a candidate, but will also always lose to other candidate states. In this case, the `small` state has the minimum score and is selected as the responsive state.

If the width of the widget is 600: the `small` state would be skipped, while the `medium` and `large` states would produce the same scores resulting in `medium` being the responsive state.

The `when` functions have access to any properties of the widget instance in the first argument, but are also passed the [BrowserHelper](https://bryntum.com/docs/gantt/api/#Core/helper/BrowserHelper) singleton as a second argument. This can be used as shown in the following, over-simplified example:

```
 class ResponsiveWidget extends Widget.mixin(Responsive) {
     static configurable = {
         responsive : {
             small : {
                 when : ({ width }, { isMobileSafari }) => isMobileSafari && width <= 600 && 10
                 text : 'iPhone'
             },
             medium : {
                 when : ({ width }, { isMobileSafari }) => isMobileSafari && width <= 1024 && 20
                 text : 'iPad'
             }
             large : {
                 text : 'Desktop'
             }
         }
     };
 }
```

It is best to avoid mixing `when` threshold values and `when` functions as the resulting scores can be confusing.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[responsive](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Responsive#config-responsive)
Specifies the various responsive state objects keyed by their name. Each key (except `'*'`, see below) in this object is a state name (see [responsiveState](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#config-responsiveState)) and its corresponding value is the associated [ResponsiveState](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#typedef-ResponsiveState) object.

This property makes it easy to create mobile-friendly widgets that adapt to the size of the device they are being used on.

Some properties of a `ResponsiveState` object are special, for example `when` and `callback`. All other properties of the state object are config properties to apply when that state is active.

The `when` property can be a function that computes the score for the state. The state whose `when` function returns the lowest score is selected and its non-special properties will be assigned to the instance. If `when` is a number, it will be converted into a scoring function (see below).

A `when` function accepts two readonly parameters and returns either a numeric score if the state should be considered, or `false` or `null` if the state should be ignored (i.e., it does match with the current state).

The first parameter is a readonly proxy for the [widget](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#config-responsiveTarget) whose size and other properties determine the state's score. The proxy tracks property access to that widget in order to update the responsive state should any of those properties change.

The second argument to a `when` function is the [BrowserHelper](https://bryntum.com/docs/gantt/api/#Core/helper/BrowserHelper) singleton. This allows a `when` function to conveniently test platform and browser information.

The state whose `when` function returns the lowest score is selected as the new [responsiveState](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#config-responsiveState) and its config object (minus the `when` function and other special properties) is applied to the instance.

If `when` is a number, it is converted to function. The following two snippets produce the same `when` scoring:

```
     small : {
         when : 400,
         ...
     }
```

The above converted to:

```
     small : {
         when : ({ width }) => width <= 400 && 400,
         ...
     }
```

Selecting the lowest score as the winner allows for the simple conversion of width threshold to score value, such that the state with the smallest matching width is selected.

If the `responsive` config object has an asterisk key (`'*'`), its value is used as the default set of config properties to apply all other states. This will be the only config properties to apply if no `when` function returns a score. In this way, this special state object acts as a default state as well as a set of default values for other states to share. This state object has no `when` function.

The default for this config is:

```
 {
     small : {
         when : 400
     },

     medium : {
         when : 800
     },

     large : {
         when : () => Infinity
     },

     '*' : {}
 }
```

A derived class (or instance) can use these states by populating other config properties, define additional states, and/or adjust the `when` properties to use different size thresholds.

[responsiveDefaults](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Responsive#config-responsiveDefaults)
The defaults for the [responsive](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#config-responsive) config. These are separated so that the act of setting the [responsive](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#config-responsive) config is what triggers additional processing.

[responsiveRoot](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Responsive#config-responsiveRoot)
Set to `true` to mark this instance as the default [responsiveTarget](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#config-responsiveTarget) for descendants that do not specify an explicit [responsiveTarget](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#config-responsiveTarget) of their own.

[responsiveState](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Responsive#config-responsiveState)
The name of the active state of the [responsive](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#config-responsive) config. This is assigned internally and should not be assigned directly.

[responsiveTarget](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Responsive#config-responsiveTarget)
The widget whose size and other properties drive this object's responsive behavior. If this config is not specified, the closest ancestor that specified [responsiveRoot=true](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#config-responsiveRoot) will be used. If there is no such ancestor, then the instance using this mixin is used.

If this value is set to `'@'`, then this instance is used even if there is a [responsiveRoot](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#config-responsiveRoot) ancestor.

If this config is a string that starts with `'@'`, the text following the first character is the name of the property on this instance that holds the target to use. For example, `'@owner'` to use the value of the `owner` property as the responsive target.

If this config is a string that does not start with `'@'`, that string is passed to [up](https://bryntum.com/docs/gantt/api/#Core/widget/Widget#function-up) to find the closest matching ancestor.

If another widget is used as the `responsiveTarget` and if this instance does not specify any explicit `when` properties in its [responsive](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#config-responsive) config, then the `when` definitions of the `responsiveTarget` will be used for this instance.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isResponsive](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Responsive#property-isResponsive)
Identifies an object as an instance of [Responsive](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive) class, or subclass thereof.

[isResponsive](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Responsive#property-isResponsive-static)
Identifies an object as an instance of [Responsive](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive) class, or subclass thereof.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[beforeResponsiveStateChange](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Responsive#event-beforeResponsiveStateChange)
Triggered before a new [responsiveState](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#config-responsiveState) is applied.

[responsiveStateChange](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Responsive#event-responsiveStateChange)
Triggered when a new [responsiveState](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#config-responsiveState) is applied.

## Typedefs

Typedefs are type definitions for the class

[ResponsiveState](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Responsive#typedef-ResponsiveState)
A state definition object used by the [responsive](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive#config-responsive) config property.

```
 {
     responsive : {
         small : {
             // a ResponsiveState object
             when : 400,

             callback() {
                 console.log('Applied small not first time');
             },

             once : {
                 mode : 'full',

                 callback() {
                     console.log('Applied small first time');
                 }
             }

             // All other properties are configs to apply when
             // the state is active
             text  : null,
             color : 'b-blue'
         }
     }
 }
```

See [Responsive](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Responsive) for more details.
