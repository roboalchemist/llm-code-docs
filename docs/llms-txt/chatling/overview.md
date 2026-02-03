# Source: https://docs.chatling.ai/whatsapp/overview.md

# Source: https://docs.chatling.ai/web-widget/installation/overview.md

# Source: https://docs.chatling.ai/team-members/overview.md

# Source: https://docs.chatling.ai/knowledge-base/overview.md

# Source: https://docs.chatling.ai/chatbot/contacts/overview.md

# Source: https://docs.chatling.ai/chatbot/builder/blocks/trigger/overview.md

# Source: https://docs.chatling.ai/chatbot/builder/blocks/overview.md

# Source: https://docs.chatling.ai/chatbot/builder/blocks/hubspot/overview.md

# Source: https://docs.chatling.ai/chatbot/builder/blocks/condition/overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Learn about the condition blocks and how to use them

Condition blocks are used to create conditional logic in your bot. You can use it to check if a certain condition is met and then perform different actions based on the result.

Similar to an "if-else" statement in programming, condition blocks evaluate a condition and executes different paths based on whether the condition is true or false.

<img src="https://chatling-assets.b-cdn.net/condition-block.jpeg" alt="Condition block" width="500" />

## Types of condition blocks

There are two types of condition blocks available in Chatling:

* [**Variable**](./variable): Compares a variable with a value or another variable.
* **Language**: Checks if the user's language matches a specific language. Useful for creating multilingual bots.

## How do condition blocks work?

Condition blocks consist of two main parts:

* **Conditions**: The conditions that the block will evaluate. You can use variables, languages, comparison operators, and logical operators to create complex conditions.
* **Paths**: The paths that the block will follow based on the result of the conditions. Every condition you add will have a corresponding path that the block will follow if the condition is true.

<img src="https://chatling-assets.b-cdn.net/condition-block-components.jpeg" alt="Condition block components" width="600" />

Here's an example of how a condition block works:

1. The block evaluates conditions in the order they are added.
2. If a condition is true, the block follows the path associated with that condition.
3. If none of the conditions are true, the block follows the "Else" path.

## The Else condition

The `Else` condition is executed if none of the other conditions are met. You can use it to define a fallback path that the block will follow if none of the other conditions are true.

## Comparison operators

Conditions support a variety of comparison operators that you can use to compare values. Here are some of the operators you can use:

* **Equals**: Checks if the variable is equal to the value.
* **Not equals**: Checks if the variable is not equal to the value.
* **Contains**: Checks if the variable contains the value.
* **Not contains**: Checks if the variable does not contain the value.
* **Greater than or equals**: Checks if the variable is greater than or equal to the value.
* **Less than**: Checks if the variable is less than the value.
* **Less than or equals**: Checks if the variable is less than or equal to the value.
* **Starts with**: Checks if the variable starts with the value.
* **Ends with**: Checks if the variable ends with the value.
* **Is empty**: Checks if the variable is empty.
* **Is not empty**: Checks if the variable is not empty.

## Group and child conditions

Conditions are grouped together to create complex logic using logical operators like "AND" and "OR". Every group contains one or more conditions that are evaluated together.

<img src="https://chatling-assets.b-cdn.net/group-and-child-conditions.jpg" alt="Group and child conditions" />

Conditions within a group are evaluated together to determine if the group is true or false. You can use logical operators such as "AND" and "OR" to combine conditions within a group.

For example, you can create a group with two conditions and set it to "AND" to require both conditions to be true for the group to be true. On the other hand, you can set it to "OR" to require only one of the conditions to be true for the group to be true.

By default, condition blocks have one group with one condition. To add additional groups, click the `Add group condition` button.

## Logical operators

Logical operators are used to combine conditions within a group. You can choose from the following logical operators:

* **AND**: Requires all conditions in the group to be true for the group to be true.
* **OR**: Requires at least one condition in the group to be true for the group to be true.

<Accordion title="Example">
  - Group 1:
    * Condition 1: Variable A equals 5
    * Condition 2: Variable B equals 10
    * Logical operator: AND

  - Group 2:
    * Condition 1: Variable C contains "hello"
    * Condition 2: Variable D contains "world"
    * Logical operator: OR

  In this example, Group 1 will be true only if Variable A equals 5 and Variable B equals 10. Group 2 will be true if either Variable C contains "hello" or Variable D contains "world".
</Accordion>
