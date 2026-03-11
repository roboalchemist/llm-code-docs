# Source: https://docs-containers.back4app.com/docs/cloud-code-functions/code-complexity.md

---
title: Complexity Report
slug: docs/cloud-code-functions/code-complexity
description: Learn how to create report showing the code complexity in cloud code functions in Back4App.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-02-28T13:58:14.341Z
updatedAt: 2025-01-17T14:25:11.662Z
---

# How to Create a Report showing the Complexity of your Cloud Code

## Introduction

This section will teach you to generate a Code Complexity report of your Cloud Code using [**Plato**](https://www.npmjs.com/package/plato).

Cloud Code must be efficient from design. As it is called many many times, a slightly worse performance can become a huge problem and affect your production environment badly.

If you take your time to design your cloud code efficiently, you will be able to serve more requests using smaller servers, which can lead to huge savings over time.
On the other hand, badly designed cloud code can only scale up in bigger, more expensive machines, which also has limitations. This situation can and probably will lead to the necessity of rewriting code and more spendings over time.

Please take your time to test, load test and constantly check reports on code complexity.

## Prerequisites

:::hint{type="info"}
- To complete this tutorial, you will need:

- A local environment with Node.js installed to apply unit tests. You can follow the [**Official NodeJS tutorial**](https://nodejs.org/en/download/package-manager/) to successfully install Node.js at your terminal.
- An app created at Back4App.
- Follow the [**Create New App tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create an app at Back4App.
- Back4App Command Line Configured with the project.
- Follow the [**Setting up Cloud Code tutorial**](https://www.back4app.com/docs/local-development/parse-cli) to learn how to set up cloud code for a project.
:::

## First off, we need to talk about Plato

We usually start developing by creating a smaller set of functions that break a big problem into smaller, easier to address ones.
This approach is usually fine and these initial smaller functions grow over time, making more complex operations and dealing with more data.
As data grows in your application, computing intensive tasks such as loops and recursive calls get called more and more, which tends to slow the application. In severe cases it might even freeze the application completely.
This is where [**Plato**](https://www.npmjs.com/package/plato) comes in.

[**Plato**](https://www.npmjs.com/package/plato) is a JavaScript source code visualization, static analysis, and complexity tool that generates reports showing how complex your application is getting and where to address fixes to potentially speed up processes.

### 1 - Installing Plato

If you have [**NodeJS**](https://nodejs.org/en/download/package-manager/) and [**NPM**](https://www.npmjs.com/) installed in your system, installing [**Plato**](https://www.npmjs.com/package/plato) is as easy as typing

:::BlockQuote
1   npm install -g plato
:::

If you don’t, please install those before proceeding.

### 2 - Running Plato

Running [**Plato**](https://www.npmjs.com/package/plato) after installation consists of typing the following command from the directory where your Cloud Code is:

:::BlockQuote
1   plato -r -d MyReportFolder -t "My Report for this App" -x .json \*.js
:::

the options mean:

- -r: Recursive, meaning it will go into directories and subdirectories looking for files
- -d MyReportFolder: (output) Directory. Plato will create a directory named MyReportFolder where it will store its results
- -t “My Report for this App”: Title. Plato will name this report My Report for this App. This is useful to create multiple reports over time and keep track
- -x .json: Exclude .json files. You can tell Plato to ignore file types so it runs faster
- \*.js: Look for anything with the extension .js to be evaluated

### 3 - Getting results

In the MyReportFolder created by the command above, you will find an index.html containing the report. Open that file in a browser and you will find something like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/m7y26fYbFw_pxzXbDa9E-_image.png)

In my case, I only had a file named main.js, but depending on your code, you can have more files.
Scroll down to the Files section and click the file name you want to open (main.js in my case). This will open the report for that file:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/TqMI00Zb4hLBqZul0SQmX_image.png)

- Maintainability is a value between 0 and 100 that represents the relative ease of maintaining the code. A high value means better maintainability.
- Difficulty measure is related to the difficulty of the program to write or understand.
- Estimated Errors is Halstead’s delivered bugs is an estimate for the number of errors in the implementation.

The Function Weight has two metrics:

- By Complexity: This metric counts the number of distinct paths through a block of code. Lower values are better.
- By SLOC: Source Lines of Code / Logical Lines of Code

Now you can scroll down and watch the alerts and possible fixes that are suggested:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/nf44nHZSFHVQYA2bY-0DO_image.png)

In my case, it is telling that arrow function syntax (=>)' is only available in ES6 (use 'esversion: 6'), which is not a problem.
But let’s add some very inefficient code to that function and re-evaluate:

```javascript
1function getSquareRootOf(numberOne, numberTwo, numberThree){
2	var finalResult;
3
4	var i = 0;
5	var j = 0;
6	var k = 0;
7
8	for (i = 0; i < 100; i ++){
9		for (j = 0; j < 100; i ++){
10			for (k = 0; k < 100; k++){
11				var resultOne = getSquareRootOf(numberOne);
12				var resultTwo = getSquareRootOf(numberTwo);
13				var resultThree = getSquareRootOf(numberThree);
14				finalResult = resultOne + resultTwo + resultThree;
15			}
16		}
17	}
18}
```

And evaluate the result:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/izF-yrFGm7JcbDQ6XZV1X_image.png)

As we can see, the complexity of this function is 4, which is OK. The higher the number you get, the more complex the function is and the more you should ensure it is efficient.

[**Plato**](https://www.npmjs.com/package/plato) will also warn you of missing semicolons and other potential Javascript errors.

## Conclusion

Having a tool such as [**Plato**](https://www.npmjs.com/package/plato) checking the complexity of your code and continuously reworking cloud code to be as fast, and efficient as possible can lead to huge savings over time.
You and all developers should include this step or something similar in your development process to ensure you get the most bang for your buck serving requests.
