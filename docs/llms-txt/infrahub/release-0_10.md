# Source: https://docs.infrahub.app/release-notes/infrahub/release-0_10.md

| Release Number   | 0.10.0                                                                                |
| ---------------- | ------------------------------------------------------------------------------------- |
| Release Date     | January 16, 2024                                                                      |
| Release Codename | Alpha #4                                                                              |
| Tag              | [infrahub-v0.10.0](https://github.com/opsmill/infrahub/releases/tag/infrahub-v0.10.0) |

# Release 0.10.0 - Alpha #4

## Main Changes[​](#main-changes "Direct link to Main Changes")

### Hierarchical mode[​](#hierarchical-mode "Direct link to Hierarchical mode")

It's now possible to organize some nodes of similar types in a hierarchy or a tree, to enable additional capabilities. As an example:

Groups can be organized in a hierarchy by default which makes it possible to query the members of all sub-groups at once. Assuming we have defined a Person object connected to a City object, which itself is part of a hierarchy of Location (Region > Country > City) , it will be possible to query all Person per Country or per Region natively without having a direct relationship between Person and Country

### New Infrahub test framework[​](#new-infrahub-test-framework "Direct link to New Infrahub test framework")

As a platform, Infrahub provides multiple ways for a user to extend the capabilities of the platform by providing different type of resources. Developing and maintaining these resources over time can be time consuming and challenging, this is why we did our best to provide the right tools and helpers to make it as easy as possible for someone to create and maintain these resources.

The framework is based on Pytest and introduces a new pytest plugin pytest-infrahub (part of the SDK), in this first version the Framework support unit tests for RFile and PythonTransform. IN the next release we'll add support for all type of resources and sanity and integration tests as well.

### Schema[​](#schema "Direct link to Schema")

#### Support both Node-level and Generic-level uniqueness for attributes[​](#support-both-node-level-and-generic-level-uniqueness-for-attributes "Direct link to Support both Node-level and Generic-level uniqueness for attributes")

Now, multiple classes can inherit from the same generic, with attributes that are unique across all sub-classes.

### API and GraphQL[​](#api-and-graphql "Direct link to API and GraphQL")

Access the version of infrahub Now, you can query the Infrahub version directly through our GraphQL API:

```
query {
    InfrahubInfo {
        version
    }
}
```

### Integration and deployment[​](#integration-and-deployment "Direct link to Integration and deployment")

#### Add support for webhooks[​](#add-support-for-webhooks "Direct link to Add support for webhooks")

You are now able to configure a new webhook and track the execution of all webhooks via the frontend and via GraphQL. Please note that the current version supports only POST requests and does not yet provide the ability to send a list of headers or specify events to subscribe to.

New codespace config file to launch a barbone version of Infrahub Previously, the codespace configuration we had in automatically launching Infrahub and loading the demo schema & data.

We added a new configuration file that will start a barebone version of infrahub by default. You will be able to configuration files under /.devcontainer folder.

### UX improvements[​](#ux-improvements "Direct link to UX improvements")

Infrahub is now faster than ever! We've optimized the frontend, bid farewell to unnecessary reloads and loaders, and introduced features for a smoother user experience:

* List rows can be opened in a new tab
* Browser tab titles indicate your current view for easy navigation.
* Display the version of infrahub into the UI
* On branch detail view, "contribute" button was renamed to "Proposed change"

#### New UI components[​](#new-ui-components "Direct link to New UI components")

form

* List Input: A new input specifically designed for attributes of type List.
* Color Picker: Introducing a color picker input for attributes of type Color.

list view

* Display attributes of kind Color
* Overall improvements to documentation
* Explore our upgraded docs now! 📚
