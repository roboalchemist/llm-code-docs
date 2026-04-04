# Source: https://configcat.com/docs/main-concepts.md

# Main Concepts

Copy page

## Feature Flag or Setting[​](#feature-flag-or-setting "Direct link to Feature Flag or Setting")

A *Setting* is an essential bit of *ConfigCat*. It can be of multiple types, such as an on/off switch (bool), number (int, double) or any text (string). You can use it to change your application's behavior remotely, without a new deployment.

A *Feature Flag* is a *Setting* of type Bool.

### Anatomy of a *Feature Flag* or *Setting*[​](#anatomy-of-a-feature-flag-or-setting "Direct link to anatomy-of-a-feature-flag-or-setting")

| Properties | Description                                                                                                            |
| ---------- | ---------------------------------------------------------------------------------------------------------------------- |
| Name       | A human readable name that differentiates the *Setting* on the *ConfigCat Dashboard*. e.g., `My Cool Feature enabled`. |
| Key        | A variable name within your code. e.g., `isCoolFeatureEnabled`.                                                        |
| Type       | Type of information you'd like to keep in the *Setting*. e.g., On/Off Toggle, Text, Number                             |
| Value      | The actual value of your *Setting*. e.g., `true`, `false`. Can be different in each environment.                       |

### About *Setting* types[​](#about-setting-types "Direct link to about-setting-types")

| Setting Kind   | Setting Type | Description                                                                       |
| -------------- | ------------ | --------------------------------------------------------------------------------- |
| On/Off Toggle  | Boolean      | true/false, usually referenced as Feature Flag, Feature Toggle or Feature switch. |
| Text           | String       | Any string, max. 100000 characters, can't be empty.                               |
| Whole Number   | Integer      | Any whole number within the range of `Int32`.                                     |
| Decimal Number | Double       | Any decimal number within the range of `double`.                                  |

## Config[​](#config "Direct link to Config")

A *Config* is a collection of *Settings*. *Configs* help you organize settings around topics, or around your software components. A *Config* is like an online version of a traditional config file.

## Environment[​](#environment "Direct link to Environment")

An environment in ConfigCat represents an environment in your development lifecycle (like production, staging, development etc.). Different environments have the same settings but can have different values.

info

Each environment-config pair has its own SDK Key which must be used to initialize the ConfigCat SDK within your application.

## Product[​](#product "Direct link to Product")

A collection of *Configs*, *Environments* and *Team members*. A *Product* typically represents your application (or your service) and the people working on it. It might be a good idea to invite others to your *Product* to collaborate.

## Organization[​](#organization "Direct link to Organization")

An *Organization* represents a collection of preferences that are valid for all the *Products* and *Members* who belong to an *Organization*. Like billing information, authentication rules or data privacy preferences.
