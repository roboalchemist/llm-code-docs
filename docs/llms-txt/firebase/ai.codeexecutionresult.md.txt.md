# Source: https://firebase.google.com/docs/reference/js/ai.codeexecutionresult.md.txt

# CodeExecutionResult interface

The results of code execution run by the model.

**Signature:**

    export interface CodeExecutionResult 

## Properties

| Property | Type | Description |
|---|---|---|
| [outcome](https://firebase.google.com/docs/reference/js/ai.codeexecutionresult.md#codeexecutionresultoutcome) | [Outcome](https://firebase.google.com/docs/reference/js/ai.md#outcome) | The result of the code execution. |
| [output](https://firebase.google.com/docs/reference/js/ai.codeexecutionresult.md#codeexecutionresultoutput) | string | The output from the code execution, or an error message if it failed. |

## CodeExecutionResult.outcome

The result of the code execution.

**Signature:**

    outcome?: Outcome;

## CodeExecutionResult.output

The output from the code execution, or an error message if it failed.

**Signature:**

    output?: string;