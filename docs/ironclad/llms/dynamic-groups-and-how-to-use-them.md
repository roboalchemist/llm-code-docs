# Source: https://clickwrap-developer.ironcladapp.com/docs/dynamic-groups-and-how-to-use-them.md

# Filtering Templates - Virtual Groups

Ironclad Clickwrap offers the ability to create multiple templates, filter them, and display the relevant template(s) to the counterparty. This filter can be based on user input, pre-determined conditions, and/or other parameters. This capability is known as **Virtual Groups**.

For example, if you plan to embed a Clickwrap Group within your login page, Virtual Groups grant the flexibility to display an English Template to a user located in the United States, and a French Template to user located in France — with both of those Templates within one Clickwrap Group.

**Please note:** Loading a group of Contracts in this manner will affect load times on the page and is not subject to normal Ironclad Clickwrap SLAs. If you'd like to optimize how your Contracts are loaded on the page, check out [Loading a Clickwrap 101](https://clickwrap-developer.ironcladapp.com/docs/loading-a-clickwrap-101).

Here are additional use cases where Virtual Groups can be utilized:

* Displaying an additional agreement if an end-user opts in
* Depending on the end user’s location, display a different language contract

***

## Setting up your Ironclad Clickwrap Templates + Groups

Please refer to this [help center article](https://support.ironcladapp.com/hc/en-us/articles/14002064111767-Virtual-Groups-Overview) for guidance on setting up your templates and Clickwrap Groups to support Virtual Groups. This includes creating and publishing the relevant templates, applying properties to them, and adding them to a Clickwrap Group in your Ironclad Clickwrap site. When completed, ensure you have the following data points handy:

* Group Key
* Clickwrap Template filter options

> 📘 Filtering Contracts
>
> Filtering using properties will search through all templates available within your Site. Ensure you have unique properties to ensure you are pulling the correct templates. Additionally, ensure that these filters are specific - Ironclad Clickwrap's filtering will return a **maximum of 100 templates**.

***

## Loading the Group

### Using the Ironclad Clickwrap Snippet

When loading your Clickwrap, load the Clickwrap Group you can use the same `_ps('load')` method you would use with your traditional JavaScript library. However, within the groupOptions, add a filter parameter. This is where you can configure your filters to display templates based on the properties you have applied. Depending on the user flow or specific scenario, this filter option allows you to choose the specific template(s) to load onto the screen.

```javascript
var groupOptions = {
  filter: "locale==en-US", 
}
_ps('load', groupKey, groupOptions)
```

### Using the Activity API

When grabbing the load/html or load/json endpoints, include the filter parameter to search through your contracts and the Clickwrap Group key to track acceptance against .

```json
https://pactsafe.io/load/html
{
  "sid": "site_id",
  "filter": "locale==en-US",
  "group_key":"group_key"
}
```

> 📘 Contract Hyperlink
>
> When using the Activity API, the hyperlink that is included in the Clickwrap Group HTML or JSON body will download a version of the contract if clicked (rather than redirect the user to the Legal Center).

## Tips and Tricks when using Virtual Groups

### Filtering and Sorting Templates

Methods to sort through templates include filtering on id, tags, classification, locales, and countries.

* `tags==tag1,tag2` will display all contracts with either tag1 or tag2
* `tags==tag1 AND tags==tag2` will display contracts with both tag1 and tag2

Add a "sort" argument to alter the order that the contracts appear in.

```javascript
var groupOptions = {
  filter: "tags==US AND tags==midmarket", 
  sort: "created_time desc"
}
_ps('load', groupKey, groupOptions)
```

### Acceptance Language

In some scenarios, changing the template(s) that is shown to the end user also requires a change in the acceptance language. A common scenario is language-specific virtual groups. In these use cases, customers often also want the acceptance language to be translated to match the template language. This can be done by overriding the group options that are defined on the Ironclad Clickwrap platform, as shown below.

```javascript
var groupOptions = {
  filter:"tags==test",
  acceptance_language: "I do declare that {{contracts}} are enforceable"
}
_ps('load', groupKey, groupOptions)
```