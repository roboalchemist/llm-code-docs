# Source: https://docs.xano.com/testing-debugging/test-suites.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Test Suites

Workflow Testing allows you to create sets of different tests to validate user flows are working as expected.

## What is Workflow Testing?

Workflow Testing in Xano allows you to quickly build sets of tests that you can use to make sure a specific flow is working as expected. You can think of a 'flow' as a set of separate actions, such as multiple APIs that a user might hit when utilizing your application, or data processing across multiple function stacks.

Workflow Testing allows you to validate these sets or flows with a single click and get instant visibility into your backend functionality.

## How do I build workflow tests?

From the left-hand navigation menu, choose **Library** > **Workflow Tests**

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/-vy8_DWVOwkWo8Bt/images/86d49f76-image.jpeg?fit=max&auto=format&n=-vy8_DWVOwkWo8Bt&q=85&s=93bc5e6e5e9f6166be7b87a68a6ce4de" alt="" width="426" height="395" data-path="images/86d49f76-image.jpeg" />
</Frame>

Choose **Add Workflow Test** in the top-right corner. In the panel that opens, you can give your test a name, description, and add tags for easy access later.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/3d167f5b-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=de48fc873ee03d1721add77388c91149" alt="" width="1978" height="765" data-path="images/3d167f5b-image.jpeg" />
</Frame>

Click the

<img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/cbd9e333-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=7cbaa5f03ada1c9907f9cbafe1e605db" className="inline m-0" width="168" height="42" data-path="images/cbd9e333-image.jpeg" />

button to add a step to your Workflow Test. We've introduced some new functions to assist you in building your tests.

**Run Stacks**

Run stacks are functions you can add to your workflow tests to run other function stacks, such as APIs, custom functions, and middleware.

| Function Name    | Use Case                                                            |
| ---------------- | ------------------------------------------------------------------- |
| Run API Endpoint | Sends a request to one of your API endpoints and returns the result |
| Run Addon        | Runs an addon                                                       |
| Run Function     | Runs a custom function and returns the result                       |
| Run Middleware   | Runs a middleware and returns the result                            |
| Run Trigger      | Runs a trigger and returns the result                               |
| Run Task         | Runs a background task and returns the result                       |

#### Test Expressions

Test Expressions are functions used typically in conjunction with a Run Stack to determine if the output of a Run Stack is valid.

| Function Name                                                                                                                                           | Use Case                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Expect a variable to be defined Expect a variable to not be defined                                                                                     | Checks to see if a variable has been defined. **Example**: You have an API that returns a `user` object with a name key inside of it. You can use this to check if `user.name` is defined.                                                                                                     |
| Expect variable to be empty                                                                                                                             | Checks to see if a variable exists, but is empty. **Example:** You are calling an external API that is used to process data. If the API call is successful, you know that `response.result` is empty because the API just returns a status code informing you that the job is being processed. |
| Expect variable to be false Expect variable to be true                                                                                                  | Checks to see if a variable with a boolean data type is returning `false` or `true`                                                                                                                                                                                                            |
| Expect variable to be greater than Expect variable to be less than Expect variable to equal Expect a variable to not equal Expect variable to be within | Checks to see if a variable matches the specific condition, such as >, \<, =, or is within a certain range.                                                                                                                                                                                    |
| Expect variable to be null                                                                                                                              | Checks to see if a variable contains a `null` value                                                                                                                                                                                                                                            |
| Expect variable to start with Expect variable to end with                                                                                               | Checks to see if the value inside of a variable starts or ends with a specific value                                                                                                                                                                                                           |
| Expect function to throw                                                                                                                                | Checks a function to see if it throws an error                                                                                                                                                                                                                                                 |
| Expect function to match                                                                                                                                | Checks to see if the output of a variable matches a [regular expression](https://regexr.com/)                                                                                                                                                                                                  |

### Using Workflow Tests

In this example, we've built a workflow test to make sure our login flow works as expected.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/27f6db14-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=e2e919d740e545a6410bbe775729c497" alt="" width="994" height="693" data-path="images/27f6db14-image.jpeg" />
</Frame>

We've added a **Run Stack** function to run our auth/login endpoint, and provided it with a username and password.

After that, our **Test Expression** checks to make sure that the login function is returning an authToken, which is what our login endpoint returns if a valid username and password is provided. When we click **Run** we can see that our test passes!

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/-vy8_DWVOwkWo8Bt/images/83a0d311-image.jpeg?fit=max&auto=format&n=-vy8_DWVOwkWo8Bt&q=85&s=2f01cd27ce3fb2c3f06182be5576cb08" alt="" width="1221" height="471" data-path="images/83a0d311-image.jpeg" />
</Frame>

If we modify our **Run API Endpoint** run stack to provide an invalid password, we can see that by running our test again, we get an error. This test has failed because an authToken was not returned.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/9028563b-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=0f5d4246c1b17f9c7d69586269855e75" alt="" width="1210" height="610" data-path="images/9028563b-image.jpeg" />
</Frame>

From the main **Workflow Tests** page, we can run each of our tests by clicking the individual  buttons, or we can click **Run Test Suites** to run all of our workflow tests at once.

We can see by running all of our workflow tests the following information:

* We have **38% coverage**. This means that out of all of the function stacks that exist across our backend, 3/8 of them are used in our tests.
* We have **50% success**. This means that out of all of our workflow tests, half of them are successful.
* To run all of our tests takes less than a second.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/a477590e-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=a3790a5eb6e1e6a9a43f451eab7e161e" alt="" width="1079" height="555" data-path="images/a477590e-image.jpeg" />
</Frame>

#### Additional Information

* Click the **settings** icon next to a workflow test to clone or delete it.
* When adding a Run Stack, you can click the**Open**  icon to open that function stack being tested in a new window or tab and quickly make changes.
* When you test a function stack that currently is in draft mode, your workflow test will run the drafted version.
* You can change the data source that all of your workflow test's functions run against by clicking the **Live** button at the top of the workflow test function stack.

## Databases in Workflow Tests

<Frame caption="Selecting a Data Source for a Workflow Test">
    <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/60df04b6-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=d8addae44901885a845692527b439403" alt="" width="2025" height="568" data-path="images/60df04b6-image.jpeg" />
</Frame>

When you select a data source for your Workflow Test, it's important to note that a **copy** of the database is generated to ensure that no live data is impacted. This usually means that selecting your live database is not recommended — if your database is large in size, this can cause complications during testing.

It is recommended to use separate [Data Sources](/the-database/database-basics/data-sources) for running tests.


Built with [Mintlify](https://mintlify.com).