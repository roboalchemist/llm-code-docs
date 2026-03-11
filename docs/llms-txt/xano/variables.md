# Source: https://docs.xano.com/xanoscript/function-reference/data-manipulation/variables.md

# Source: https://docs.xano.com/building/logic/working-with-data/variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Variables

> Variables are used to store temporary information that you need to access later in a workflow

## What are variables?

Variables are like containers or labels that store information you want to use later in a workflow. Think of them as named boxes where you can keep different types of items, such as numbers, words, or lists. You give each box a name so you can easily find and use the information it holds whenever you need it in your project. This makes it simple to update or change the data without needing to rewrite everything.

Variables are temporary and exist only while a workflow is running, used for storing information you need to access quickly, whereas values in a database are like records in a filing cabinet, stored permanently until you decide to update or delete them, accessible across various workflows and sessions. This makes databases ideal for managing large sets of data over time, and variables more appropriate for temporary data handling.

## Creating a variable

<Steps>
  <Step title="Add a Create Variable function.">
    You'll find this function as a default favorite at the top of the function menu, or inside of the Data Manipulation section.
    <Frame>    <img src="https://mintcdn.com/xano-997cb9ee/4xy0p5vdU3hAE_8U/images/variables-20251013-092915.png?fit=max&auto=format&n=4xy0p5vdU3hAE_8U&q=85&s=6752a7a6340efe127a7c361b70f462d4" alt="variables-20251013-092915" width="1412" height="1151" data-path="images/variables-20251013-092915.png" /></Frame>
  </Step>

  <Step title="Give your variable a name and a value.">
    The variable name should be a descriptive name that you can easily recognize. Names can only contain letters, numbers, and underscores, and must start with a letter. The value can be anything you'd like, from simple text and integers all the way to large, complex data types.

    You can also just establish an empty variable by leaving the value blank if you're going to add a value later.
    <img src="https://mintcdn.com/xano-997cb9ee/4xy0p5vdU3hAE_8U/images/variables-20251013-093127.png?fit=max&auto=format&n=4xy0p5vdU3hAE_8U&q=85&s=9821e9e65f012c34d780dac98e4bcd8f" alt="variables-20251013-093127" width="546" height="264" data-path="images/variables-20251013-093127.png" />
  </Step>
</Steps>

## Using a variable

Inside of your logic, you can reference the variable by using the variable name. You'll find it under the **VAR** dropdown, or you can just type the variable name directly into the value field.

<Frame><img src="https://mintcdn.com/xano-997cb9ee/4xy0p5vdU3hAE_8U/images/variables-20251013-093209.png?fit=max&auto=format&n=4xy0p5vdU3hAE_8U&q=85&s=256d283872d4a82fe2b62d72ce80bfa0" alt="variables-20251013-093209" width="545" height="284" data-path="images/variables-20251013-093209.png" /></Frame><br />

Need to specify a value that's the same as the variable name? Click the **CONST** section and choose the `text` data type.<br /><br />
<Frame><img src="https://mintcdn.com/xano-997cb9ee/4xy0p5vdU3hAE_8U/images/variables-20251013-093340.png?fit=max&auto=format&n=4xy0p5vdU3hAE_8U&q=85&s=c315496e42c346c83cd303d66fe9c5c2" alt="variables-20251013-093340" width="542" height="290" data-path="images/variables-20251013-093340.png" /></Frame>

## Updating a variable

If you need to update a variable, you can use the **Update Variable** function. This will overwrite the existing value with the new one.

<Frame><img src="https://mintcdn.com/xano-997cb9ee/4xy0p5vdU3hAE_8U/images/variables-20251013-093500.png?fit=max&auto=format&n=4xy0p5vdU3hAE_8U&q=85&s=a6281d4bc9a5eb6f7c06a8a98c55dd2b" alt="variables-20251013-093500" width="542" height="412" data-path="images/variables-20251013-093500.png" /></Frame>

Remember, you can use [dot notation](/building/logic/working-with-data/dot-notation) to target a specific piece of data inside of the variable if it's an array or object.

## Deleting a variable

There is no 'delete variable' function, but you can overwrite the variable with an empty value to effectively delete it. However, usually this is not necessary, as variables are automatically deleted when the logic is complete.


Built with [Mintlify](https://mintlify.com).