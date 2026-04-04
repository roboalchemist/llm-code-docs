# Source: https://firebase.google.com/docs/reference/js/ai.executablecode.md.txt

# ExecutableCode interface

An interface for executable code returned by the model.

**Signature:**

    export interface ExecutableCode 

## Properties

| Property | Type | Description |
|---|---|---|
| [code](https://firebase.google.com/docs/reference/js/ai.executablecode.md#executablecodecode) | string | The source code to be executed. |
| [language](https://firebase.google.com/docs/reference/js/ai.executablecode.md#executablecodelanguage) | [Language](https://firebase.google.com/docs/reference/js/ai.md#language) | The programming language of the code. |

## ExecutableCode.code

The source code to be executed.

**Signature:**

    code?: string;

## ExecutableCode.language

The programming language of the code.

**Signature:**

    language?: Language;