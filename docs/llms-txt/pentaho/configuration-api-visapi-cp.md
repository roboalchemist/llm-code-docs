# Source: https://docs.pentaho.com/pdia-admin/administer/platform-javascript-apis/configuration-api-visapi-cp.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/pentaho-developer-center-overview-cp/platform-javascript-apis/configuration-api-visapi-cp.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/configuration-api-visapi-cp.md

# Configuration API

You can configure the JavaScript modules with the Pentaho `Configuration API`. Pentaho uses JavaScript objects, known as Configurations, to conform to the `pentaho.config.spec.IRuleSet` interface. These Configurations are a set of configuration rules defined in `pentaho.config.spec.IRule`. Configurations are provided through the value returned by the AMD/RequireJS module. You must register the configuration module with `pentaho/modules` as an instance of `pentaho/config/spec/IRuleSet` to use these Configurations.

The Configurations (the configuration rules) are composed of the following parts:

* **The `select` object**

  Specifies the targeted module, and the values of any `Pentaho environment variables` to which it applies. Alternative values for a variable can be specified using a JavaScript array. The most useful environment variable is `application`, as it allows creating rules that only apply when a module is being used by a certain application. For example, when a variable is used by the [CDF](https://community.hitachivantara.com/s/article/community-dashboard-framework) or [Analyzer](https://www.hitachivantara.com/en-us/products/data-management-analytics/lumada-analytics.html) application. See [Known Values of Pentaho Environment Variables](#known-values-of-pentaho-platform-environment-variables) for known values for common applications and themes.
* **The `apply` object**

  Specifies the configuration properties and their values. Consult the reference documentation of your target module for a list of available properties. For example, the `Visualization API`’s `Model` type, being a `Complex` type, can be configured with the properties of the `IComplexType` interface. The `apply` property can also be a function. You can call it to determine the configuration object, only when and if the selected module or modules are loaded.
* **The `deps` array**

  Contains a list of additional module identifiers that are loaded only when and if the selected module or modules are loaded. When `apply` is a function, the values of the specified modules are given as arguments.
* **The `priority` value**

  Allows fine-tuning of the order by which rules that target the same module are merged for fine-tuning. Higher values have higher priority. The `priority` value is optional and defaults to 0. See `Rule Specificity` for more information on the order by which configuration rules having the same target are merged.

## Configuration module example

The following example AMD/RequireJS configuration module contains four configuration rules:

```javascript
define(function() {
  "use strict";
  // The value of the module is an IRuleSet.
  return {
    rules: [
      // IRule 1
      {
        select: {
          module: "my/Car",
          application: "my/vehicleEditor"
        },
        apply: {
          tireSize: 18,
          exteriorColor: "caribbean-blue"
        }
      },
    
      // IRule 2
      {
        priority: 1,
        select: {
          module: "my/Candy"
        },
        apply: {
          cocoaPercentage: 0.9,
          fillingFlavour: "orange"
        }
      },
      
      // IRule 3
      {
        select: {
          module: [
            "my/friends/john", 
            "my/friends/marie"
          ]
        },
        apply: {
          empathyLevel: 0.6
        }
      },
      
      // IRule 4
      {
        select: {
          module: "my/houses/main"
        },
        deps: [
          "lodash", 
          "./baseHouseSchematics"
        ],
        apply: function(_, baseHouseSchematics) {
          return _.merge(baseHouseSchematics, {
            averageSummerTemperature: 23
          });
        }
      }
    ]
  }
});

```

This above example contains the following four configuration rules:

* **The first rule**

  Targets the `my/Car` type module when it is used by the `my/vehicleEditor` application. This module specifies the value of its `tireSize` and `exteriorColor` properties.
* **The second rule**

  Targets the `my/Candy` type module for whichever application is using it. This rule has a higher-than-default priority and specifies the value of its `cocoaPercentage` and `fillingFlavour` properties.
* **The third rule**

  Targets the `my/friends/john1` and `my/friends/marie` instance modules for whichever application using them. These modules specify the value of their `empathyLevel` property.
* **The fourth rule**

  Targets the instance module `my/houses/main`, whatever the application using it, and configures it; the configuration is based on a configuration obtained as a dependency from the sibling module `baseHouseSchematics`.

## Global configuration file

Your systems integrators or system administrators can add ad hoc configuration rules by placing them in the global configuration file, which is pre-registered.

The `config/web-client/config.js` file is located within the Apache Karaf folder. Depending on the product, the Karaf folder is located in following location:

* **PDI**

  `data-integration/system/karaf/`
* **Pentaho Server**

  `pentaho-server/pentaho-solutions/system/karaf/`

Your system refreshes its configurations after you edit and save the file. You do not need to restart to apply these ad hoc configurations.

The configuration file is shipped with a small set of illustrative (but commented-out) rules.

You can bundle and deploy your own Pentaho web package containing a registered configuration module as an alternative to using a global configuration file. You can also use the same Pentaho web package to include and register a default configuration along with the component. See **Pentaho Web Package** for further instructions.

## Known values of Pentaho platform environment variables

The following values are already defined as Pentaho platform environment variables:

* `application`
  * **CDF**

    `pentaho/cdf`
  * **Analyzer**

    `pentaho/analyzer`
  * **Analyzer in Dashboard Designer**

    `pentaho/dashboardDesigner`
  * **PDI**

    `pentaho/det`
* `theme`
  * `sapphire`
  * `crystal`
  * `ruby`
* `locale`

The possible values are those defined by [RFC 5646](https://tools.ietf.org/html/rfc5646).
