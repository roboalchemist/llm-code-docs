# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/view/mixin/GridFeatures.md

# [GridFeatures](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridFeatures)

Mixin for Grid that handles features. Features are plugins that add functionality to the grid. Feature classes should register with Grid by calling [registerFeature](https://bryntum.com/docs/gantt/api/#Grid/feature/GridFeatureManager#function-registerFeature-static). This enables features to be specified and configured in grid config.

Define which features to use:

```
// specify which features to use (note that some features are used by default)
const grid = new Grid({
  features: {
     sort: 'name',
     search: true
  }
});
```

Access a feature in use:

```
grid.features.search.search('cat');
```

Basic example of implementing a feature:

```
class MyFeature extends InstancePlugin {

}

GridFeatures.registerFeature(MyFeature);

// using the feature
const grid = new Grid({
  features: {
    myFeature: true
  }
});
```

Enable and disable features at runtime
--------------------------------------

Each feature is either "enabled" (included by default), or "off" (excluded completely). You can always check the docs of a specific feature to find out how it is configured by default.

Features which are "off" completely are not available and cannot be enabled at runtime.

For a feature that is **off** by default that you want to enable later during runtime, configure it with `disabled : true`:

```
const grid = new Grid({
     featureName : {
         disabled : true // on and disabled, can be enabled later
     }
});

// enable the feature
grid.featureName.disabled = false;
```

If the feature is **disabled** by default, and you want to include and enable the feature, configure it as `true`:

```
const grid = new Grid({
     featureName : true // on and enabled, can be disabled later
});

// disable the feature
grid.featureName.disabled = true;
```

If the feature is **on** by default, but you want to turn it **off**, configure it as `false`:

```
const grid = new Grid({
     featureName : false // turned off, not included at all
});
```

If the feature is **enabled** by default and you have no need of reconfiguring it, you can omit the feature configuration.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[features](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridFeatures#config-features)
Specify which features to use on the grid. Most features accepts a boolean, some also accepts a config object. Please note that if you are not using the bundles you might need to import the features you want to use.

```
const grid = new Grid({
    features : {
        stripe : true,   // Enable stripe feature
        sort   : 'name', // Configure sort feature
        group  : false   // Disable group feature
    }
}
```

Setting this property has no effect when using framework wrappers.

When using framework wrappers, features must be configured via `featureNameFeature` properties. See [Framework Integration Guide](https://bryntum.com/docs/gantt/api/#Grid/guides/integration/react/guide.md#configuring-features) for details.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isGridFeatures](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridFeatures#property-isGridFeatures)
Identifies an object as an instance of [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures) class, or subclass thereof.

[isGridFeatures](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridFeatures#property-isGridFeatures-static)
Identifies an object as an instance of [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures) class, or subclass thereof.

[features](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridFeatures#property-features)
Map of the features available on the grid. Use it to access them on your grid object

```
grid.features.group.expandAll();
```

## Functions

Functions are methods available for calling on the class

[hasFeature](https://bryntum.com/docs/gantt/api/Grid/view/mixin/GridFeatures#function-hasFeature)
Check if a feature is included
