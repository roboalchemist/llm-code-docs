# Source: https://docs.flux.ai/reference/rule-modifiers.md

# Layout Rules Modifiers

In addition to standard rules, Flux has a variety of supplemental _rule modifiers_. These are useful for tweaking the behavior of specific parts or assemblies. See the list below for specific examples.

## !important flag

The _!important_ flag, when added to a rule, forces Flux to override any other rules with the flagged rule. 

![](https://uploads.developerhub.io/prod/86Yw/1d5jxmrwi8d7417yt9n91639ls1dvwqbtd7247b3bhmekhr5pypn4fx8ihorw0nt.png)

Take, for example, a part, module or sublayout  that in general you cannot modify. However, Flux allows you to override this default behavior and modify objects or parts you consume using the _!important_ flag when added onto specific rules. Simply adding the _!important_ flag to a rule will ensure the flagged rule is granted.

One way to see this in action is selecting just the silk text of an object and moving it slightly. This will generate a new _Position_ rule found in the rules sidebar on the left with the _!important_ flag automatically added. The newly generated rule will target the UID of the object (found in the _Selector_ section of the right sidebar).

Another method is locating the object’s UID, and manually creating a new rule. Create a new ruleset from the rules sidebar on the left. Then open the _New ruleset_ sidebar on the right, and enter _[uid=objectUID]_ in the selector section, with _objectUID_ replaced by the object’s unique ID. Then modify the object however you like. 

A common applications for this flag include hiding silk text from the PCB editor. This is especially useful for parts with a lot of silk that may add unneeded distraction in the PCB editor. The other main application is when you are consuming sublayouts as opposed to creating one. 

The `!important`flag works with objects, modules, and sublayouts.

> When the !important flag has been added to a rule, a new DRC warning called "Component Overrides" will be created.

### Example: Hiding Silkscreen Text on Imported Parts or Sublayouts

The `!important` flag can be used to override silkscreen visibility. Specifically, some objects that you may import come with a lot of silkscreen text information. Having a lot of modules or sublayouts in your project may lead to potentially too much text that you may want to reduce.

Simply double-click the component or sublayout to edit it, and move the desired silkscreen to create an override rule. Add an additional `enable`rule set to `false`with the `!important` flag. This essentially adds a rule that disables the text, but uses the _!important_ flag’s feature to ensure that this rule is granted.  See here for a full [tutorial](https://docs.flux.ai/flux/reference/silkscreen-reference#modifying-existing-silkscreen).