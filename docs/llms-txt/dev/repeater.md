# Source: https://dev.writer.com/agent-builder/repeater.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Build dynamic UI components with Repeaters

> Display dynamic lists of data in Agent Builder UI with Repeaters. Create repeating components for lists, dictionaries, and nested data structures.

The [**Repeater** component](/components/repeater) in Agent Builder allows you to display dynamic lists of data in your UI. It's similar to the [For-each loop block](/blueprints/for-eachloop) in blueprints, but for UI elements.

This document provides an overview of Repeaters and how to use them in your Agent Builder agents with two examples.

## Overview

A Repeater takes a list or dictionary and creates a copy of its child components for each item in that data. Inside the Repeater, you can access:

* `@{item}`: the current item's value
* `@{itemId}`: the current item's index, for arrays, or key, for dictionaries

Below is an example interface with a Repeater that displays a list of recipes based on user input. The Repeater is used to display each recipe in a tabbed layout and also to display the ingredients and steps for each recipe as nested text Repeaters.

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-demo-app.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=0e9c3ddeced43dfe128aa2391e690685" alt="Repeater demo that displays a list of recipes based on user input" data-og-width="3456" width="3456" data-og-height="1812" height="1812" data-path="images/agent-builder/repeater-demo-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-demo-app.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=a0513a9b783ae60540a852e7393ecbd5 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-demo-app.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=c6da51b40321fb9f78eb4c1c1b566216 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-demo-app.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=831aee9c58d3403eeb5b548625529791 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-demo-app.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=61ae5467e2066a6680fae1a9e73b7781 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-demo-app.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=88161edba46ade30bfc77c8ac5668034 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-demo-app.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=2d1299474de1eb8030f1a194d34ca48a 2500w" />

See the [tutorial](#tutorial%3A-build-a-recipe-generator-with-repeaters) below for more details about building this recipe generator.

### When to use Repeaters

Repeaters are useful for displaying:

* Lists of files, tasks, or messages
* Search results or product catalogs
* User-generated content like comments or reviews
* Data from APIs or structured output
* Any collection where you don't know the exact number of items

## Example: Display a list of items

This example starts with a small use case to dynamically display whatever a user selects from a select input.

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-example.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=3782e6778c72fc04c9fc101d6305164f" alt="Repeater example" data-og-width="3456" width="3456" data-og-height="656" height="656" data-path="images/agent-builder/repeater-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-example.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=f9374ee09f4fe19049bd6c29ba85fbea 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-example.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=715db04326ea77851160a3fcde97930e 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-example.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=9ff80a974b2fdbf35feb2ff9f2e1eb97 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-example.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=696befd90acbe5fd34c687a95bdb9461 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-example.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=485adcb19611e3fe09a6ea90dd7ff418 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-example.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=c3e00dde7ac2c5b550644c8a8cadcc92 2500w" />

To start, you should have a new Agent Builder agent and clear the demo agent so you can start from scratch. See the instructions for [clearing the demo agent](/agent-builder/quickstart#clear-the-demo-agent) in the Agent Builder quickstart.

### Set up the select input

The select input allows the user to select multiple items from a list. You'll use it to select the items to display in the Repeater.

<Steps>
  <Step title="Add the select input to the agent">
    First, add a **Select input** block to the agent's interface. This is the input that will be used to select the items to display in the Repeater.

    Update the following settings:

    * **Label**: `Items`
    * Under **Options**, add a few key-value pairs as options for the dropdown. For example:
      * Key: Apple, Value: Apple
      * Key: Berry, Value: Berry
      * Key: Cherry, Value: Cherry
    * **Link variable** under **Binding**: `list`

    <Note>
      When you define the options for the select input, the values are what the user sees in the select dropdown, and the keys are what will be stored in the state variable.
    </Note>
  </Step>

  <Step title="Add a Heading component">
    Add a **Heading** component to the agent's interface. This separates the select input from the Repeater.

    Under **Text**, update the text to `You selected:`. Next, you'll add the Repeater below this heading.

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-heading.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=39268147ab4ac031809436244b470d39" alt="Heading component" data-og-width="3456" width="3456" data-og-height="1810" height="1810" data-path="images/agent-builder/repeater-heading.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-heading.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=e1942fb2ae6ee784a98c588bbe8d1553 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-heading.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=ef73ff680f544418472a2dd6f67a3dac 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-heading.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=0db7c4fef14876ca864973eda248a6df 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-heading.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=adc41b30e4b93911838cfe7ca2395c1d 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-heading.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=25367d955ccc01e0fa792f04de93f90e 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-heading.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=a51b55be3a471a78a1024410ebd4d680 2500w" />
  </Step>
</Steps>

### Add the Repeater

The Repeater displays a list of items dynamically. You'll use it to display the items selected from the select input.

<Steps>
  <Step title="Add a Repeater component">
    Add a **Repeater** component to your page. Update the following settings:

    * **Repeater object**: `@{list}`. This is the list of items to display in the Repeater.

    The **Key variable name** and the **Value variable name** default to `itemId` and `item`. These are the variable names you use to access the current item's index and value within the Repeater. You can change them to anything you want. In this example, you'll use the default names.

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-repeater.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=714d7c4e40d1a880259de798182bcb2a" alt="Repeater component" data-og-width="3456" width="3456" data-og-height="1804" height="1804" data-path="images/agent-builder/repeater-repeater.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-repeater.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=1ec542b57013dbc160d15f77b7a7d3c9 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-repeater.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=bcd12c2d515b4f4060d4b7af536665bc 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-repeater.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=5f66b88f10e015066d10e4d08cbf9f31 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-repeater.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=d72865fc1d53656c8167f6e31db305fb 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-repeater.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=393c8a55242ded6ef4892ab1861944e0 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-repeater.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=6989720c5e5447e61fb728a5431a479c 2500w" />
  </Step>

  <Step title="Add a Text component inside the Repeater">
    Drag a **Text** component inside the Repeater.

    Inside the text component, set the text to ` @{item}` to display the value of the current item in the Repeater.

    When the `list` state variable is empty, the text displays placeholder text. When the user selects items from the multiselect input, the text displays the selected items.

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-text.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=ec7895afc8e3a8322401d3bd5fb30af5" alt="Text component" data-og-width="3456" width="3456" data-og-height="1814" height="1814" data-path="images/agent-builder/repeater-text.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-text.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=cf158754a5ace1392742c4b309e36fc1 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-text.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=cc41fe3029ceb61f9636970102c6307a 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-text.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=8f891e0b23cdc625bf04c2aa9fd72762 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-text.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=319fffca26f9faa06e1b1ffc8b9c8aa9 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-text.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=2523c44ab4e76a39fbd43cb5627124d9 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-text.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=a675f482f40f8f2d6f4991e72656e972 2500w" />
  </Step>

  <Step title="Update the Repeater's visibility">
    Once you add components to a Repeater, you can no longer see the parent Repeater component in the agent's interface view. You can find and edit the invisible component from the **Interface Layers** tab.

        <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/interface-layers.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=6ee428aa5b41dcb67eac1b8879c0bda3" alt="Repeater component" data-og-width="498" width="498" data-og-height="194" height="194" data-path="images/agent-builder/interface-layers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/interface-layers.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=5b80b6977b19c568b389204c6312fce4 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/interface-layers.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=8f46494a79cb8cbb6dd63eb040e7a44e 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/interface-layers.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=219d157e352a68da25148f52e89500a7 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/interface-layers.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=1487be01695f993e114941c32b1f0c8b 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/interface-layers.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=3cc3b111ea4bf7f94e7ee3d58eb0a7cb 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/interface-layers.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=5a0aa1a9f740c7c8fc8b257c92c72034 2500w" />

    Navigate to the **Interface Layers** sidebar within the agent's **Interface** tab. Then, click the Repeater component to open its configuration menu.

    Under **Visibility** in the Repeater's configuration menu, select **Custom**. Set the condition to `list`. This ensures the Repeater is only visible when the user has selected at least one item from the select input and the `list` state variable isn't empty.

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-visibility.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=57a514bbbcb09e88ca4dfa1989790570" alt="Repeater visibility" data-og-width="3456" width="3456" data-og-height="1804" height="1804" data-path="images/agent-builder/repeater-visibility.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-visibility.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=05485cd38551684d783551727905927a 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-visibility.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=621b2626120f1dea1182feecf751be34 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-visibility.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=9a9384caeaf75aa053b4fab93c29807e 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-visibility.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=ca6e5a6603cd5e0690fe4d2bb88e0349 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-visibility.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=bc38b84e99377161d87f8f5bc533117e 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-visibility.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=2b0162a480dd888e7fb7bc81ba17ee83 2500w" />

    <Tip>
      Once you set a component's visibility to become hidden, you can no longer see it or its children within the agent's interface view. You can find and edit the invisible component from the **Interface Layers** tab.
    </Tip>
  </Step>

  <Step title="Preview the Repeater">
    Navigate to the **Preview** tab to see the Repeater in action.

    Select a few items from the select input to see the Repeater display the corresponding items.

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-example.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=3782e6778c72fc04c9fc101d6305164f" alt="Repeater preview" data-og-width="3456" width="3456" data-og-height="656" height="656" data-path="images/agent-builder/repeater-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-example.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=f9374ee09f4fe19049bd6c29ba85fbea 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-example.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=715db04326ea77851160a3fcde97930e 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-example.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=9ff80a974b2fdbf35feb2ff9f2e1eb97 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-example.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=696befd90acbe5fd34c687a95bdb9461 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-example.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=485adcb19611e3fe09a6ea90dd7ff418 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-example.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=c3e00dde7ac2c5b550644c8a8cadcc92 2500w" />
  </Step>
</Steps>

## Tutorial: Build a recipe generator with Repeaters

This tutorial uses multiple Repeaters to display a list of recipes based on user input.

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-demo-app.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=0e9c3ddeced43dfe128aa2391e690685" alt="Repeater demo that displays a list of recipes based on user input" data-og-width="3456" width="3456" data-og-height="1812" height="1812" data-path="images/agent-builder/repeater-demo-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-demo-app.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=a0513a9b783ae60540a852e7393ecbd5 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-demo-app.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=c6da51b40321fb9f78eb4c1c1b566216 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-demo-app.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=831aee9c58d3403eeb5b548625529791 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-demo-app.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=61ae5467e2066a6680fae1a9e73b7781 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-demo-app.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=88161edba46ade30bfc77c8ac5668034 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-demo-app.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=2d1299474de1eb8030f1a194d34ca48a 2500w" />

The recipe generator:

* Accepts a list of dish names from the user
* Generates complete recipes in the blueprint using AI structured output
* Displays each recipe in an organized, tabbed layout using nested Repeaters

### Part 1: Set up a minimal UI and the blueprint

First, you'll set up a minimal UI and the blueprint. This UI won't use any Repeaters yet, but it will be the foundation for the recipe generator.

#### Create the input interface

<Steps>
  <Step title="Add a Text Input">
    Add a **Text Input** to your page. Update the following settings:

    * **Label**: `Recipes`
    * **Placeholder text**: `Enter dish names (e.g., "Pizza, Chocolate Chip Cookies, Tacos")`
    * **Link variable** under **Binding**: `request`
  </Step>

  <Step title="Add a Button to trigger the blueprint">
    Add a **Button** to your page. Update the following settings:

    * **Label**: `Get recipes`
  </Step>
</Steps>

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-minimal-ui.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=db45ef81a8e936fe69cd506599c670c7" alt="Minimal UI" data-og-width="3456" width="3456" data-og-height="648" height="648" data-path="images/agent-builder/repeater-minimal-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-minimal-ui.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=4516342a459b85f429c1c1cd1693e712 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-minimal-ui.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=a4dce7994f13f15a0c331735da2954e2 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-minimal-ui.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=36c416b42cddf3f3c214b7256be83277 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-minimal-ui.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=39247fa8f43fc00ccf401949960c55ed 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-minimal-ui.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=77c5a9307fbbe0fbb98e8491ff80ca07 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-minimal-ui.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=dcf8740010bf32bb811015355e286c13 2500w" />

#### Build the blueprint

The blueprint contains three blocks:

* **UI Trigger** to trigger the blueprint when a user clicks the **Get recipes** button
* **Structured Output** block to generate the recipes and provide structured output that the Repeaters can use
* **Set State** block to store the recipes in the state variable `recipes`

<Steps>
  <Step title="Add a UI Trigger block">
    Add a **UI Trigger** block to your blueprint. Update the following settings:

    * **Component Id**: Select the **Get recipes** button
    * **Action**: `wf-click`
  </Step>

  <Step title="Add a Structured Output block">
    Add a **Structured Output** block to your blueprint. Update the following settings:

    * **Prompt**:
      ```
      You are a helpful cooking assistant. The user will provide you with a list of dish names. For each dish mentioned, create a complete recipe with the name, ingredients list, and step-by-step cooking instructions.

      Guidelines:
      - Provide practical, easy-to-follow recipes suitable for home cooking
      - Include specific measurements for ingredients (cups, tablespoons, etc.)
      - Write clear, numbered steps that a beginner could follow
      - Keep recipes simple but complete
      - If a dish name is vague, choose a popular/classic version of that dish

      For each dish in the user's input, generate a separate recipe object with:
      - name: The specific recipe name
      - ingredients: A detailed list of all ingredients with measurements
      - steps: Clear, sequential cooking instructions

      Example input: "Pizza, Chocolate Chip Cookies"
      This should generate recipes for both pizza and chocolate chip cookies.

      Process all dishes mentioned in the user's input and provide complete recipes for each one.

      User input: @{request}
      ```

    * **JSON Schema**: The JSON schema below defines the structure of the recipes as a list of recipe objects. Each recipe object has a name, ingredients, and steps. The Repeaters will use this schema to display the recipes.
      ```json  theme={null}
      {
        "type": "array",
        "description": "Array of recipe objects",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the recipe"
            },
            "ingredients": {
              "type": "array",
              "description": "List of ingredients needed for the recipe",
              "items": {
                "type": "string"
              }
            },
            "steps": {
              "type": "array",
              "description": "Step-by-step cooking instructions",
              "items": {
                "type": "string"
              }
            }
          },
          "required": ["name", "ingredients", "steps"]
        }
      }
      ```
  </Step>

  <Step title="Add a Set State block">
    Add a **Set State** block to your blueprint. Update the following settings:

    * **State variable**: `recipes`
    * **Value**: `@{result}`
  </Step>
</Steps>

The complete blueprint should look like this:
<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-blueprint.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=e27ee3256e43e71a6339ba930dfd1c66" alt="Complete blueprint" data-og-width="3456" width="3456" data-og-height="1806" height="1806" data-path="images/agent-builder/repeater-blueprint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-blueprint.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=d4d354d7a3df191de8655dbc8f011a24 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-blueprint.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=45d44cd02ac5bc4616a226bdf244af1a 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-blueprint.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=8f9069dd89488e0307c9b51d4e54359a 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-blueprint.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=c7b38380997a3436ebbcdcf86a326da2 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-blueprint.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=599e3fb5d833da5717a0f2207ada50e1 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-blueprint.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=4d4d1215aa62b762c6472ef84e871760 2500w" />

#### Test the blueprint

Now you can test that the blueprint works before you add the Repeaters.

Navigate to the **Preview** tab to test the blueprint.

Enter something like "Pizza, Chocolate Chip Cookies" in the text input and click the **Get recipes** button.

You should see the `request` and the structured output in the `result` state variables in your state before moving to the next step.

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-state-variables.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=90e453db9c71a8909e8066f5569e3303" alt="State variables" data-og-width="3456" width="3456" data-og-height="1810" height="1810" data-path="images/agent-builder/repeater-state-variables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-state-variables.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=056db6fa875db803ddee392be3286455 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-state-variables.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=1c9eeda20d5ba1ad95cea7ead8e64f80 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-state-variables.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=01be1f72d5435958e7983c796ea9ebac 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-state-variables.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=faaaa671c48d55c89e77e048653860c4 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-state-variables.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=34af632ab162b5d4dd141e6b6d4c3d80 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-state-variables.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=85e31482de4b5679c2344ac574d594ec 2500w" />

### Part 2: Add the main recipe Repeater

Navigate back to the **Interface** tab to continue building the recipe generator's UI.

<Steps>
  <Step title="Add a Repeater component">
    Add a **Repeater** component to your page. Update the following settings:

    * **Repeater object**: `@{recipes}`. This is the list of recipes you stored in the `recipes` state variable.
  </Step>

  <Step title="Add a Heading component inside the Repeater">
    Add a **Heading** component inside the Repeater. Update the following settings:

    * **Text**: `@{item.name}`

    This displays the name of each recipe as a heading.
  </Step>
</Steps>

If you preview the agent now, you should see a heading for each recipe name.

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-preview-headings.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=78aa4feda3f5858fc92b2a629f166ced" alt="Repeater preview" data-og-width="3456" width="3456" data-og-height="1804" height="1804" data-path="images/agent-builder/repeater-preview-headings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-preview-headings.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=ee4b9adb77625b6625b14a84fa7911a3 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-preview-headings.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=7f22882df51dc0c4b94daf266ef1dd85 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-preview-headings.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=0b28cee8389fabea74d8fd6f20a04d68 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-preview-headings.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=f1ceb22cebb7145bb10eb2ed602f3523 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-preview-headings.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=35fb76ef2585e9d2260565504ecb50b9 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-preview-headings.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=a06c6018570056836de471d1ead8e8ea 2500w" />

At this point, when there are no recipes, the Repeater still displays placeholder text. At the end of the tutorial you'll update the Repeater to be invisible when there are no recipes.

### Part 3: Add nested Repeaters for ingredients and steps

Now you'll add nested Repeaters for ingredients and steps. You'll use a **Tab Container** to display the ingredients and steps in separate tabs.

<Steps>
  <Step title="Add a Tab Container inside the main Repeater">
    Add a **Tab Container** inside the Repeater by dragging it into the space that contains the heading. You can verify that the tab container is inside the Repeater by checking the **Interface Layers** sidebar.

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-tab-container.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=02aeb336cca872112c4f6801b67abea1" alt="Tab Container inside the Repeater" data-og-width="3456" width="3456" data-og-height="1812" height="1812" data-path="images/agent-builder/repeater-tab-container.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-tab-container.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=bff0adaa1447d99ded6bfcf028bb5769 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-tab-container.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=70ac8abc376569b4b9aa6628f2bab375 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-tab-container.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=b30640a2e46caaf7202e9ef3c76be6d3 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-tab-container.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=d8aac79ba8f2f29baeb24acc9bb95f55 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-tab-container.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=f5deeedecf612d2a659b1fb0d9d900aa 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-tab-container.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=0c8db85450da1380fc74a8f37a46764c 2500w" />
  </Step>

  <Step title="Create the first tab">
    Add a **Tab** component to the tab container. Update the following settings:

    * **Tab name**: "Ingredients"

    Then drag a **Repeater** inside the tab. Update the following settings:

    * **Repeater object**: `@{item.ingredients}`

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-ingredients-repeater.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=2a4698fe80cd7771ea0d004605f2bf66" alt="Ingredients tab" data-og-width="3456" width="3456" data-og-height="1808" height="1808" data-path="images/agent-builder/repeater-ingredients-repeater.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-ingredients-repeater.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=ac8841688d03f089bf33768f606ec52b 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-ingredients-repeater.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=7da5c9790bbc7d8a8b2a5b1a80996480 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-ingredients-repeater.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=ebe65baa5d28ff79ef3a8d2221fc4211 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-ingredients-repeater.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=e3245369c597152e25944befa23b087c 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-ingredients-repeater.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=7802c845b4fb8b57880c59f19fdd301c 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-ingredients-repeater.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=14d83a196180816821e8c8bc280545a6 2500w" />
  </Step>

  <Step title="Add a Text component inside the first tab's Repeater">
    Add a **Text** component inside the first tab's Repeater. Update the following settings:

    * **Text**: `- @{item}`

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-ingredients-text.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=bb1459d71ec49ac6a5985e97eff42729" alt="Ingredients tab" data-og-width="3456" width="3456" data-og-height="1808" height="1808" data-path="images/agent-builder/repeater-ingredients-text.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-ingredients-text.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=a2b33e0db731656338ddbbdd50130953 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-ingredients-text.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=a0bcd40f1d56083d656daef10715a403 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-ingredients-text.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=e3b9ff37ccd5150240c4264e43b11f0e 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-ingredients-text.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=ee4c5a1d5be868d319d4aa9f8d70e63f 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-ingredients-text.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=d115227a7cd72d1286e0d11a1e20646b 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-ingredients-text.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=435773d1a9a42c039be8127463dd6f45 2500w" />
  </Step>

  <Step title="Create the second tab with a Repeater">
    Add a second **Tab** component to the tab container. Update the following settings:

    * **Tab name**: "Instructions"

    Then drag a **Repeater** inside the tab. Update the following settings:

    * **Repeater object**: `@{item.steps}`

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-instructions-repeater.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=1a9c19796f7bedddafe7ae0122653228" alt="Ingredients tab" data-og-width="3456" width="3456" data-og-height="1804" height="1804" data-path="images/agent-builder/repeater-instructions-repeater.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-instructions-repeater.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=c02593b359a2c535988b4833427148f1 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-instructions-repeater.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=de7b344073ef1b35e843f0fbf000043e 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-instructions-repeater.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=01efa29fd2b7aad74a6dc888c8616fd8 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-instructions-repeater.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=930165406d7852df5927d28a33198066 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-instructions-repeater.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=8b8c9ded3d90668f397c3a0110962194 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-instructions-repeater.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=fddba8517f696cecb96a4aa5e7c9d87c 2500w" />
  </Step>

  <Step title="Add a Text component inside the second tab's Repeater">
    Add a **Text** component inside the second tab's Repeater. Update the following settings:

    * **Text**: `- @{item}`

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-instructions-text.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=57aaa9d6361e81bf57de2e548c6a8670" alt="Instructions tab" data-og-width="3456" width="3456" data-og-height="1808" height="1808" data-path="images/agent-builder/repeater-instructions-text.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-instructions-text.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=e533d1829aa991334a5f76e0f7864bcb 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-instructions-text.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=d39e98cc79d0cfa0606de955fc792512 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-instructions-text.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=fe1b08e6c0d8a0cb3c741116c783813d 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-instructions-text.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=8a5601654f1f68711bafc6ac8a5a41e8 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-instructions-text.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=bc5a9ae9cd23a34490a520275fad97e3 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-instructions-text.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=f9556965a23480f33e587ada5513df30 2500w" />
  </Step>

  <Step title="Update the Repeater's visibility">
    From the **Interface Layers** sidebar, click the first Repeater component, which contains the headings and tab components. Under **Visibility** in the main Repeater's configuration menu, select **Custom**. Set the condition to `recipes`. This ensures the Repeater is only visible when the user has selected at least one recipe.

        <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-visibility-2.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=2cf328492e10ccd990a1798184e56fb2" alt="Repeater visibility" data-og-width="3456" width="3456" data-og-height="1810" height="1810" data-path="images/agent-builder/repeater-visibility-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-visibility-2.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=184c03664e84005c0a118d5d612faa5b 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-visibility-2.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=39326b3e8dccf95581bed19e2298db47 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-visibility-2.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=edee9732188146262cdaf8d6b76008d2 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-visibility-2.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=dcd04de07915fa0a7ea77064295adba0 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-visibility-2.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=ea769c0027fe6496f725e8544637d3c7 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/repeater-visibility-2.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=29d54a5ddb2e2c539866d0e41b1230e8 2500w" />
  </Step>
</Steps>

If you preview the agent now, you should see the ingredients and steps for each recipe in separate tabs. You also shouldn't see the Repeater if there are no recipes.

### Understanding nested Repeaters

In this tutorial, you used three different Repeaters:

1. **Main Repeater**: iterates over the recipes array (`@{recipes}`)
2. **Ingredients Repeater**: iterates over each recipe's ingredients array (`@{item.ingredients}`). This Repeater is nested inside the main Repeater.
3. **Steps Repeater**: iterates over each recipe's steps array (`@{item.steps}`)

Each Repeater creates its own `@{item}` context, so the inner Repeaters access individual ingredients and steps as `@{item}`, while the outer Repeater's `@{item}` refers to the entire recipe object.

### Next steps

Try extending this tutorial by:

* Adding cooking time and difficulty level to the recipe schema
* Styling the recipe cards with colors and spacing
* Adding images or icons to make the recipes more visual
* Creating filters to show only certain types of recipes
