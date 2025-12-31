# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.userpropertyvalue.md.txt

# analytics.UserPropertyValue class

Predefined or custom properties stored on the client side.

**Signature:**  

    export declare class UserPropertyValue 

## Constructors

|                                                                                Constructor                                                                                | Modifiers |                        Description                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------|
| [(constructor)(wireFormat)](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.userpropertyvalue.md#analyticsuserpropertyvalueconstructor) |           | Constructs a new instance of the `UserPropertyValue` class |

## Properties

|                                                                      Property                                                                       | Modifiers |  Type  |                     Description                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------|------------------------------------------------------|
| [setTime](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.userpropertyvalue.md#analyticsuserpropertyvaluesettime) |           | string | UTC client time when the user property was last set. |
| [value](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.userpropertyvalue.md#analyticsuserpropertyvaluevalue)     |           | string | The last set value of a user property.               |

## analytics.UserPropertyValue.(constructor)

Constructs a new instance of the `UserPropertyValue` class

**Signature:**  

    constructor(wireFormat: any);

### Parameters

| Parameter  | Type | Description |
|------------|------|-------------|
| wireFormat | any  |             |

## analytics.UserPropertyValue.setTime

UTC client time when the user property was last set.

**Signature:**  

    setTime: string;

## analytics.UserPropertyValue.value

The last set value of a user property.

**Signature:**  

    value: string;