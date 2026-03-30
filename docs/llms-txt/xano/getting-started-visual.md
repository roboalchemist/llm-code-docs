# Source: https://docs.xano.com/getting-started-visual.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Building Visually

> A guide to using Xano's visual builder to inspect, validate, and iterate on your backend workflows.

This guide walks you through running a pre-built signup endpoint, inspecting the steps, and making a small modification to send a welcome email to new users. Xano gives you a `user` table and default `authentication` APIs out of the box, and we'll use those here.

<Steps>
  <Step title="Open up your auth/signup endpoint">
    Navigate to the API section in the left-hand navigation, choose the Authentication group, and select your auth/signup endpoint.
  </Step>

  <Step title="Test the endpoint">
    Click <span class="ui-bubble">Run</span> in the top-right corner.

    Enter a name, email, and a password to create a new user. You'll use this later on, so make sure to remember the credentials you enter here. Click <span class="ui-bubble">Run</span> in the lower-right corner to execute the request.

        <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260108-172818.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=9a9f5569d16d02bbbd5d2bc6953932ce" alt="getting-started-visual-20260108-172818" width="1434" height="515" data-path="images/getting-started-visual-20260108-172818.png" />

    If all goes well, you should see a successful response with an <Tooltip tip="Xano generates JWE tokens for authentication. These tokens are secure and can be used to authenticate API requests.">
    authentication token
    </Tooltip> returned.

        <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260108-172851.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=97dcb74db07e41e372acbd5dbc332480" alt="getting-started-visual-20260108-172851" width="707" height="418" data-path="images/getting-started-visual-20260108-172851.png" />
  </Step>

  <Step title="Explore the visual builder">
    The visual builder has two different views: **Canvas** and **Stack**. Canvas presents a node-style view of the steps in your endpoint, while Stack presents a linear, step-by-step list of the same information, more similar to traditional code.

    <Frame caption="Canvas View">
            <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260108-175031.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=29fc03a0a0e77c4b9920189c1faee9b7" alt="getting-started-visual-20260108-175031" width="1170" height="841" data-path="images/getting-started-visual-20260108-175031.png" />
    </Frame>

    <Frame caption="Stack View">
            <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260108-175050.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=1ae673f6fbf5de9caa417527337c69bb" alt="getting-started-visual-20260108-175050" width="948" height="777" data-path="images/getting-started-visual-20260108-175050.png" />
    </Frame>

    Click on a step to see more details about what it does and how it's configured.
  </Step>

  <Step title="Modify the signup endpoint to add a welcome email">
    Let's add a step to send a welcome email after signup. We'll use the **Send Email** function for this.

    Click the <span class="ui-bubble">+ Add Step</span> button at the bottom of the stack view, or in between the Create Authentication Token step and the Response in the canvas view.

        <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260108-175517.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=e0400c3be1c8a6be893a127a9174496a" alt="getting-started-visual-20260108-175517" width="746" height="342" data-path="images/getting-started-visual-20260108-175517.png" />

    Select the **Send Email** function.

        <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260108-175545.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=f419a07ddc6f3abf5afd282c1e767e56" alt="getting-started-visual-20260108-175545" width="431" height="249" data-path="images/getting-started-visual-20260108-175545.png" />

    Add a subject and a body for the email. Xano includes free access to Resend for development and testing (up to 100 emails), limited to the email address you signed up for Xano with.

        <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260108-175705.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=983067965d96b790f17aa4a03b19a953" alt="getting-started-visual-20260108-175705" width="664" height="930" data-path="images/getting-started-visual-20260108-175705.png" />

    Click <span class="ui-bubble">Save</span> to save the step.
  </Step>

  <Step title="Test the modified signup endpoint">
    Run the signup endpoint again with a different email address. You should receive a welcome email shortly after the run completes.
  </Step>

  <Step title="Explore the Run panel">
    After a run, open the <span class="ui-bubble">Timing</span> dropdown to view step timing, output, inputs, and variables.

    Click the <span class="ui-bubble">></span> next to the first Get Record step. We can see the first Get Record function returned `null`, meaning that the user didn't already exist.

        <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260108-180843.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=3ed640484f3aaf40a67ed7ea4e230621" alt="getting-started-visual-20260108-180843" width="653" height="312" data-path="images/getting-started-visual-20260108-180843.png" />

    <Tip>
      Try to register the same user again to see how the output changes.

            <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260109-090050.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=44509ab70e5af9b5b2ca34fb5f222e0b" alt="getting-started-visual-20260109-090050" width="665" height="560" data-path="images/getting-started-visual-20260109-090050.png" />
    </Tip>

    Expand the `input` and `vars` sections for each step to see how the data changes throughout execution.

        <img src="https://mintcdn.com/xano-997cb9ee/TxMj3xizKt6xZHgd/images/getting-started-visual-20260108-181247.png?fit=max&auto=format&n=TxMj3xizKt6xZHgd&q=85&s=0e2fdee6acc2b08756973011409b5886" alt="getting-started-visual-20260108-181247" width="623" height="620" data-path="images/getting-started-visual-20260108-181247.png" />

    <Tip>
      Xano will automatically hide information labeled as sensitive, such as password fields, in the run panel.
    </Tip>
  </Step>

  <Step title="Publish your changes and test externally">
    Click the dropdown in the upper-right corner and choose <span class="ui-bubble">Publish Now</span>. This immediately deploys your changes to the live API.

    Click <span class="ui-bubble"><Icon icon="link" /></span> to copy the endpoint URL.

    Take it over to your favorite API testing tool, like [Postman](https://www.postman.com/), [Insomnia](https://www.insomnia.rest), or [Bruno](https://www.usebruno.com). Send a `POST` request to the signup endpoint with the required parameters (name, email, password) in the body.

    You should see a successful response, just like in Xano, and have received another welcome email.
  </Step>
</Steps>

## Troubleshooting

<Accordion title="🛟  I deleted my default authentication APIs; can I get them back?">
  <Steps>
    <Step title="">
      Click <span class="ui-bubble">API</span> in the left-hand navigation.
    </Step>

    <Step title="">
      Click the <span class="ui-bubble">+ Create API</span> button in the top-right corner.
    </Step>

    <Step title="">
      Select <span class="ui-bubble">Authentication</span>
    </Step>

    <Step title="">
      Add the three default API endpoints offered: `/signup`, `/login`, and `/me`
    </Step>
  </Steps>
</Accordion>

<Accordion title="🛟  Common Signup Errors">
  <Danger>
    **Error Traceback (Most recent call last):**

    at `API /auth/signup(Get Record)`
    Exception: Param: field\_value - Missing param: field\_value
  </Danger>

  > The required parameters were not provided when running the endpoint -- specifically the email. Make sure to enter a name, email, and a password.

  <Danger>
    **Error Traceback (Most recent call last):**

    at `API /auth/signup(Precondition)`
    Exception: Access Denied
  </Danger>

  > The account already exists. Try using a different email address to create a new user.

  <Danger>
    **Error Traceback (Most recent call last):**

    at `API /auth/signup(Add Record)`
    Exception: Param: password - Input does not meet minimum length requirement of 8 characters
  </Danger>

  > Password inputs have some default requirements: at least 8 characters, one uppercase letter, and one number. Make sure your password meets these requirements.
</Accordion>


Built with [Mintlify](https://mintlify.com).