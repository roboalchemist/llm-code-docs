# Source: https://firebase.google.com/docs/reference/js/auth.recaptchaverifier.md.txt

# RecaptchaVerifier class

An [reCAPTCHA](https://www.google.com/recaptcha/)-based application verifier.

`RecaptchaVerifier` does not work in a Node.js environment.

**Signature:**  

    export declare class RecaptchaVerifier implements ApplicationVerifierInternal 

**Implements:** ApplicationVerifierInternal

## Constructors

|                                                                         Constructor                                                                          | Modifiers |                        Description                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------|
| [(constructor)(authExtern, containerOrId, parameters)](https://firebase.google.com/docs/reference/js/auth.recaptchaverifier.md#recaptchaverifierconstructor) |           | Constructs a new instance of the `RecaptchaVerifier` class |

## Properties

|                                               Property                                                | Modifiers |      Type      |          Description           |
|-------------------------------------------------------------------------------------------------------|-----------|----------------|--------------------------------|
| [type](https://firebase.google.com/docs/reference/js/auth.recaptchaverifier.md#recaptchaverifiertype) |           | (not declared) | The application verifier type. |

## Methods

|                                                   Method                                                    | Modifiers |                                   Description                                    |
|-------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------|
| [clear()](https://firebase.google.com/docs/reference/js/auth.recaptchaverifier.md#recaptchaverifierclear)   |           | Clears the reCAPTCHA widget from the page and destroys the instance.             |
| [render()](https://firebase.google.com/docs/reference/js/auth.recaptchaverifier.md#recaptchaverifierrender) |           | Renders the reCAPTCHA widget on the page.                                        |
| [verify()](https://firebase.google.com/docs/reference/js/auth.recaptchaverifier.md#recaptchaverifierverify) |           | Waits for the user to solve the reCAPTCHA and resolves with the reCAPTCHA token. |

## RecaptchaVerifier.(constructor)

Constructs a new instance of the `RecaptchaVerifier` class

Check the reCAPTCHA docs for a comprehensive list. All parameters are accepted except for the sitekey. Firebase Auth backend provisions a reCAPTCHA for each project and will configure this upon rendering. For an invisible reCAPTCHA, a size key must have the value 'invisible'.

**Signature:**  

    constructor(authExtern: Auth, containerOrId: HTMLElement | string, parameters?: RecaptchaParameters);

#### Parameters

|   Parameter   |                                                              Type                                                              |                                                      Description                                                       |
|---------------|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| authExtern    | [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface)                                              | The corresponding Firebase [Auth](https://firebase.google.com/docs/reference/js/auth.auth.md#auth_interface) instance. |
| containerOrId | HTMLElement \| string                                                                                                          | The reCAPTCHA container parameter.                                                                                     |
| parameters    | [RecaptchaParameters](https://firebase.google.com/docs/reference/js/auth.recaptchaparameters.md#recaptchaparameters_interface) | The optional reCAPTCHA parameters.                                                                                     |

## RecaptchaVerifier.type

The application verifier type.

For a reCAPTCHA verifier, this is 'recaptcha'.

**Signature:**  

    readonly type = "recaptcha";

## RecaptchaVerifier.clear()

Clears the reCAPTCHA widget from the page and destroys the instance.

**Signature:**  

    clear(): void;

**Returns:**

void

## RecaptchaVerifier.render()

Renders the reCAPTCHA widget on the page.

**Signature:**  

    render(): Promise<number>;

**Returns:**

Promise\<number\>

A Promise that resolves with the reCAPTCHA widget ID.

## RecaptchaVerifier.verify()

Waits for the user to solve the reCAPTCHA and resolves with the reCAPTCHA token.

**Signature:**  

    verify(): Promise<string>;

**Returns:**

Promise\<string\>

A Promise for the reCAPTCHA token.