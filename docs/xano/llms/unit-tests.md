# Source: https://docs.xano.com/testing-debugging/unit-tests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Unit Tests

## Building a Unit Test

The fastest way to create a unit test is by using Run & Debug. Once you are achieving the desired result by running your function stack, you can click **Create Unit Test** under the result.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f55250f4-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=8607c041b673a99bef9e465fdb3b71e2" width="687" height="466" data-path="images/f55250f4-image.jpeg" />
</Frame>

You can also create a test manually at any time from the API settings menu.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/4145e564-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=6d48fb7f8dcd4f986e7f231ceb66a383" width="639" height="633" data-path="images/4145e564-image.jpeg" />
</Frame>

Give your unit test a name, a description, and the data source that it should use to run the test if different from your live data source.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/8eef8083-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=88c52ff5b0d78a317f7e7adbf277e6b6" width="736" height="446" data-path="images/8eef8083-image.jpeg" />
</Frame>

Unit tests are defined by your **input** and **expects**.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/-vy8_DWVOwkWo8Bt/images/86e21a5e-image.jpeg?fit=max&auto=format&n=-vy8_DWVOwkWo8Bt&q=85&s=8db1422c75c6395ea864bf5b1bc4f49e" width="741" height="452" data-path="images/86e21a5e-image.jpeg" />
</Frame>

In this example, we are providing an input of 2 and expect a response of 2.

* **Inputs** align with the inputs that your function stack expects. You can fill out any desired values here that you would like to use to run the test. If you used the **Create Unit Test** option in Run & Debug, this should already be populated for you.

* **Expects** are the statements that are used to validate your test. These could be anything from a simple equals statement, or use more complex operators based on your needs.

Your unit test can have multiple expect statements, which can be added by clicking the **+ Add an expect statement** option.

* Use the ✏️ button to delete expect statements.

* Use the ⏩ button to check all expect statements, or you can run them selectively with the ▶️ button.

**Unit Tests and Authentication**

When creating a unit test on a function stack that requires authentication, you can provide an auth token and extras just like you would during Run & Debug.

To avoid having to recycle the auth token upon expiration, we have added the ability to ignore auth token expiration when running your unit tests.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f56a16b8-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=d4723fb0e588f1066b024da281e1e5d6" width="736" height="201" data-path="images/f56a16b8-image.jpeg" />
</Frame>

#### Using the Testing Suite

Once you have your unit tests built, you can always run them individually from that API's testing panel. If you want to run all of your tests at once, you can use the testing suite.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/33d947ec-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=2b435836cc3facae27889f4b56c976b7" width="271" height="528" data-path="images/33d947ec-image.jpeg" />
</Frame>

In the left-hand navigation menu, find your Library and click Unit Tests.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/WBQXG-4Ngk82eYAW/images/fe8ca60b-image.jpeg?fit=max&auto=format&n=WBQXG-4Ngk82eYAW&q=85&s=1de8188882ed9867b14d75869bee1ad1" width="2304" height="782" data-path="images/fe8ca60b-image.jpeg" />
</Frame>

Once inside the testing suite, you can perform the following actions:

* Review where your application has and is missing coverage.

* Run all tests at once.

For complex applications with a significant number of objects, you have the ability to dial down further into checking coverage and tests for functions, APIs, and middleware separately. You can also filter your tests by tested / untested only, or failed only, to quickly understand where your attention should be to ensure 100% coverage and success.

## Mocking Responses

For each of the functions in your function stack, you can add *mock responses* to assist in the consistency of your unit tests.

<Steps>
  <Step title="Right-click on a function and choose Mock Test Response">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e8265537-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=d2ad542e41e72a537112a469d1db6897" width="1116" height="513" data-path="images/e8265537-image.jpeg" />
    </Frame>
  </Step>

  <Step title="In the panel that opens on the right, you can add mock data for this function that will be used during your unit test.">
    You can specify different pieces of data for each individual unit test you've built for this function stack.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/a4b0cee9-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=0b3e850bdd53e1529cd3f3bb2d2dd891" width="599" height="545" data-path="images/a4b0cee9-image.jpeg" />
    </Frame>
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).