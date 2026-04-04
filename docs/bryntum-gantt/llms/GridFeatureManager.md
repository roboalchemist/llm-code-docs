# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/GridFeatureManager.md

# [GridFeatureManager](https://bryntum.com/docs/gantt/api/Grid/feature/GridFeatureManager)

Static class intended to register and query grid features (also applies to Scheduler, Scheduler Pro and Gantt).

A feature for Grid, Scheduler, Scheduler Pro or Gantt must extend [InstancePlugin](https://bryntum.com/docs/gantt/api/#Core/mixin/InstancePlugin).

Note that features for Calendar and TaskBoard differ, they should not be registered with GridFeatureManager, and they use different base classes.

Registering a custom feature
----------------------------

First define a new feature, extending InstancePlugin:

```
export default class MyFeature extends InstancePlugin {
   // Class name, needed since the actual class name might be mangled by the minifier
   static $name = 'MyFeature';

   construct(client, config) {
       // Set things up here
   }
}
```

You can supply a `construct` function to set things up after the feature is plugged into the target component (Grid, Scheduler etc). Use it to for example register a click listener:

```
   construct(client, config) {
+      EventHelper.on({
+          element   : client.element,
+          thisObj   : this,
+          click     : this.clickCounter,
+          mouseover : this.trackMouse,
+      });
   }

+   clickCounter() {}

+   trackMouse() {}
```

Then register it with GridFeatureManager:

```
GridFeatureManager.registerFeature(MyFeature);
```

After that it is ready to use:

```
const grid = new Grid({
   features : {
     myFeature : true
   }
});
```

The feature name always starts with a lowercase letter

## Functions

Functions are methods available for calling on the class

[registerFeature](https://bryntum.com/docs/gantt/api/Grid/feature/GridFeatureManager#function-registerFeature-static)
Register a feature class with the Grid. Enables it to be created and configured using config Grid#features.

[getTypeNameFeatures](https://bryntum.com/docs/gantt/api/Grid/feature/GridFeatureManager#function-getTypeNameFeatures-static)
Get all the features registered for the given type name in an object where keys are feature names and values are feature constructors.

[getTypeNameDefaultFeatures](https://bryntum.com/docs/gantt/api/Grid/feature/GridFeatureManager#function-getTypeNameDefaultFeatures-static)
Get all the default features registered for the given type name in an object where keys are feature names and values are feature constructors.

[getInstanceFeatures](https://bryntum.com/docs/gantt/api/Grid/feature/GridFeatureManager#function-getInstanceFeatures-static)
Gets all the features registered for the given instance type name chain. First builds the type name chain then queries for features for each type name and combines them into one object, see [getTypeNameFeatures](https://bryntum.com/docs/gantt/api/#Grid/feature/GridFeatureManager#function-getTypeNameFeatures-static)() for returned object description.

If feature is registered for both parent and child type name then feature for child overrides feature for parent.

[getInstanceDefaultFeatures](https://bryntum.com/docs/gantt/api/Grid/feature/GridFeatureManager#function-getInstanceDefaultFeatures-static)
Gets all the _default_ features registered for the given instance type name chain. First builds the type name chain then queries for features for each type name and combines them into one object, see [getTypeNameFeatures](https://bryntum.com/docs/gantt/api/#Grid/feature/GridFeatureManager#function-getTypeNameFeatures-static)() for returned object description.

If feature is registered for both parent and child type name then feature for child overrides feature for parent.

[isDefaultFeatureForTypeName](https://bryntum.com/docs/gantt/api/Grid/feature/GridFeatureManager#function-isDefaultFeatureForTypeName-static)
Checks if the given feature class is default for the type name

[isDefaultFeatureForInstance](https://bryntum.com/docs/gantt/api/Grid/feature/GridFeatureManager#function-isDefaultFeatureForInstance-static)
Checks if the given feature class is default for the given instance type name chain. If the feature is not default for the parent type name but it is for the child type name, then the child setting overrides the parent one.

[reset](https://bryntum.com/docs/gantt/api/Grid/feature/GridFeatureManager#function-reset-static)
Resets feature registration date, used in tests to reset state after test
