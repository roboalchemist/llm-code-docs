# Source: https://docs.flux.ai/reference/expressions-overview.md

# Expressions

Flux features a powerful math expression engine within the Code editor,  properties, and PCB layout rules that give it spreadsheet-like superpowers.

![](https://uploads.developerhub.io/prod/86Yw/oko9hmlq8o4i2e3zoosndxm26uz7f7nl8pwyoi41d2gqaoo7hjt3blti3bxigkkn.png)

## Overview

Expressions allow you to input math functions as values in many different contexts, including the Code editor, object properties and object rules. Learn how to leverage expressions to create faster and more efficient designs.

## Getting Started

In this document, we'll cover the different use-cases where you can incorporate expressions:

- **What is an Expression?** learn how to integrate expressions in your project
- **Expression Results:** learn how Flux shows the result of an expression
- **Basic expressions**: learn how to create basic math operations and unit management.
- **Advanced expressions**: learn how to work with more advanced math functions and expressions.
- **Functions**: learn how to use Flux-specific additional functions.
- **Accessing object data**: learn how to access properties and rules inside objects.
- **Accessing project data**: learn how to access project data like a URL or description

### What is an Expression?

An expression is a way to input dynamic data into a property or rule. The expression will be evaluated in real time to calculate the value of the property or rule. Let's consider the following example:

#### Example: Position Rule

An element's position can be defined by modifying the "Position Y" rule. The normal way would be to simply type the final position in the rule, for example `20mm`

![](https://uploads.developerhub.io/prod/86Yw/12pg0boa3jod62tbyy820n3npq26u30ozh1wqkkh582256t5azl2d1l3im7o61k6.png)

Using an expression, we could calculate the "Position Y" rule based on another rule, like "Position X". It would look like this:

![](https://uploads.developerhub.io/prod/86Yw/bkiyb1hfm6ntoagdy1z4b6zzvq5ilm27dj7l6xgbmrg9hq1uzxy8wt249lwyj34k.png)

### Expression Results

The result of the expression will be shown right below whenever possible. This is usually the case when using expressions in properties or [object-specific](https://docs.flux.ai/flux/reference/object-specific-pcb-rules) rules, as there is always a single result for the expression.

![](https://uploads.developerhub.io/prod/86Yw/7075w7zv67x82srsq4ndqfe1mh4mfbkps5tua7hpzyghaddv8m1imtnnrilxlb08.png)

But when using an expression on a [selector-based](https://docs.flux.ai/flux/reference/pcb-layout-rule-selectors) rule, there could be multiple results. In that case, Flux won't show the result of the expression. You will see the` Outputs multiple values` legend instead.

### Basic Expressions

```javascript
//////// Expressions with units ////////
//Example 1 - Basic unit workflow
= 12mV
//This example returns: 0.012 


// Example 2 - Convert units
= 22ohm to mOhm
//This example returns: 0.000022


//Example 3 - Flux uses default units if none are specified
= 22mm + 1
//This example returns: 1.866142inches

//////// Expressions with basic math ////////
//Example 4 - Basic Math
= 22deg * 2
//This example returns: 44deg
```



### Advanced Expressions

Flux supports most of the [Math.js expressions syntax](https://mathjs.org/docs/expressions/syntax.html).

```javascript
//////// Working with advanced math formulas ////////
// Example 1 - Sine function
= sin(45 deg)
// This example returns: 0.7071067811865475

// Example 2 - Mixed math and units
= 9.81 m/s^2 * 5 s to mi/h
// This example returns: 109.72172512527


//////// Working with strings ////////
// Example 1 - Strings can be used in the evaluate function, to parse expressions inside the expression parser
= evaluate("2 + 3")
//This example returns: 5
```



### Flux-specific Function Helpers

We've added a few additional electronics-oriented functions that you might find useful.

```javascript
//////// Working with the Function ledBallast ////////
// Example 1 - Calculate the current-limiting resistor necessary for a 0.02A current flow and 2.9V voltage drop (Vsupply - Vforward)
= ledBallast(0.02, 2.9) 
//This example returns: 145ohm


//////// Calculating E series values for resistors ////////
//////// Available functions: toE6, toE12, toE24, toE48, toE96 and toE192 ////////
// Example 2 - Round 17 to nearst E6 type Resistor 
= toE6(17)
//This example returns: 15
```



### Accessing Object Data

Accessing object data differs depending on if you're trying to access the data from within a layout rule or an object property.

#### Accessing Object Data from a Rule

If you're trying to access object data within a [layout rule](https://docs.flux.ai/flux/reference/layout-rules-types), the `.this`directive will have the following structure:

```javascript
this: {
    uid: string;
    parentUid: string;
    type: string;
    designator: string;
    rules: {[key: string]: PcbLayoutRuleValue};
    activeRules: {[key: string]: PcbLayoutRuleValue};
    bakedRules?: IPcbLayoutBakedData;
    
    // element represents the associated element the node belongs to
    element?: {
        designator?: string;
        defaultPropertyValue?: string;
        properties: {[pascalCasePropertyName: string]: PropertyValues};
        part: {
            name?: string;
            url?: string;
        };
    };
```



**Examples**

```javascript
// Example 1 - Get the objects uid
= this.uid
// This example returns: "<your objects uid>"

// Example 2 - Get the objects type
= this.type
// This example returns: "element"

// Example 3 - Get the objects position rule
= this.rules.position
// This example returns: "12mm 3mm"

// Example 4 - Get an object's element property called ManufacturerPartNumber
// property names will be convert to Pascal case. eg. "My property name" becomes "MyPropertyName"
= this.element.properties.ManufacturerPartNumber
// This example returns: "<Manufacturar Part Number>"

// Example 5 - get the objects element part name
= this.element.part.name
// This example returns: "Samsung Resistor"
```



#### Accessing Object Data from a Property

If you're trying to access object data within a [property](https://docs.flux.ai/flux/reference/reference-inspector-properties), the `.this`directive will have the following structure:

```javascript
this: {
    designator?: string;
    defaultPropertyValue?: string;
    properties: {[pascalCasePropertyName: string]: PropertyValues};
    part: {
        name?: string;
        url?: string;
    };
   
    // Careful, not all elements have an associated node
    node?: {
       uid: string;
       parentUid: string;
       type: string;
       designator: string;
       rules: {[key: string]: PcbLayoutRuleValue};
       activeRules: {[key: string]: PcbLayoutRuleValue};
       bakedRules?: IPcbLayoutBakedData;
    };
}
```



**Examples**

```javascript
// Example 1 - Get the object's designator
= this.designator
// This example returns: "<your objects designator>"

// Example 2 - Get an object's property called ManufacturerPartNumber
// Property names will be convert to Pascal case. eg. "My property name" becomes "MyPropertyName"
= this.properties.ManufacturerPartNumber
// This example returns: "<Manufacturar Part Number>"

// Example 3 - Get the object's node UID
= this.node.uid
// This example returns: "<UID>"

// Example 4 - Get the object's node rule called Position
= this.node.rules.position
// This example returns: "<Element position>"
```



### Accessing Project Data

#### Project Data Schema

```javascript
project: {
  	name: string;
    description: string;
    properties: {[pascalCasePropertyName: string]: PropertyValues};
    url: string;
    slug: string;
    owner: {
        handle: string;
        url: string;
    };
    changeHistory: {
        currentChangeUid: string;
        currentChangeShortUid: string;
    };
}
```



#### Examples

```javascript
// Example 1 - get the project's name
= project.name
// This example returns: <your projects name>

// Example 2 - get the project's description
= project.description

//returns <your projects description>
  
// Example 3 - get the project's properties
// property names will be convert to Pascal case. eg. "My property name" becomes "MyPropertyName"
= project.properties.MyPropertyName
// This example returns: <my properties value>

// Example 4 - get the project's url
= project.url
// This example returns: <url of the project>

// Example 4 - get the project's slug
= project.slug
// This example returns: <slug of the project>
```

