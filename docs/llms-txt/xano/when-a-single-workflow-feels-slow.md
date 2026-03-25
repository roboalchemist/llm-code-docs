# Source: https://docs.xano.com/troubleshooting-and-support/troubleshooting-performance/when-a-single-workflow-feels-slow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# When A Single Workflow Feels Slow

## When a single API Endpoint feels slow

### 1. Look at the response times in the Debugger

**Start by finding the API endpoint that is causing issues.**

When the Function stack is executed within Xano, you'll be able to see each statement's response time.

**Example**

This API endpoint takes a Star Wars planet name and returns information about the planet using the Star Wars API (swapi.dev). They don't have an API that searches a planet by name so this function stack has to recursively loop through the returned planets and match up the user's request.

#### **Debugging the screenshot below**

A. There are technically **three (3)** items in the function stack.

B. After you click **Run & Debug**, click the debugger tab to see the results and response times.

C. You'll see that while there were only three functions, **14 statements got executed.** This is because Function 3 is a For Each loop that goes through each result of what is returned by the API and creates a variable.

D. You'll see that the total response time is **5.39s** which is quite long for a response, however you can also see in Line 1 of the Debugger that the Star Wars API request is taking 5.37 seconds to return a response. Xano's execution of the request happens much faster.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/654a53ce-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=4f7e1630e1f47c671c232d562211a07b" width="1775" height="1020" data-path="images/654a53ce-image.jpeg" />
</Frame>

If you have already addressed efficiency concerns in your database and function stacks as detailed in [how to improve your API response time](/troubleshooting-and-support/troubleshooting-performance/function-stack-performance), the next step is to upgrade your Xano plan for improved performance.

## Contacting Support

If you are experiencing slowness with Xano and can't figure it out on your own, you can contact support.

Please carefully read the following to resolve your issue as streamlined as possible.

* Have you tried the debugging steps listed above to narrow down problematic requests or steps in your function stack?

* If you are having an issue on your front-end, have you taken the necessary steps to ensure that everything is set up correctly on your front-end to use external data sources (like Xano)?

* Have you consulted the Xano [community](https://community.xano.com/home) and the documentation on this issue?

If you have taken the steps to troubleshoot your endpoint, please make sure that you prove the following information when contacting support.

<Warning>
  Please be sure to read and understand [support expectations](/troubleshooting-and-support/getting-help#basic-support) around these types of issues.
</Warning>

**Please provide the following details**:

* Workspace name

* API endpoint/function/task that is slow (**please include the URL in your address bar**)

* JSON payload, if you are passing data

* Email or user ID, if authentication is required

* Screenshot of your usage graph and API request graph

  * <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/WBQXG-4Ngk82eYAW/images/ff562ed7-image.jpeg?fit=max&auto=format&n=WBQXG-4Ngk82eYAW&q=85&s=9f2fef51154fb626d5f1b63b19ae9c83" width="900" height="491" data-path="images/ff562ed7-image.jpeg" />
    </Frame>
    This is available by clicking your initials in the lower-left corner and clicking Instances.

  * <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/47d89b6d-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=b8164dceb3ee4f04f9628097510b448e" width="765" height="377" data-path="images/47d89b6d-image.jpeg" />
    </Frame>
    This is available by clicking Dashboard on the left-hand side menu.

* Other helpful information (describe the issue in detail), for example:

  * Is this always slow? intermittent?

  * Is this endpoint returning records? If it is, how many records is it returning, and does the amount of records seem high for what you are expecting or is it normal?

If you do not provide all of the information listed above, your support request will likely receive a delayed response

### Example Support request

<Info>
  Workspace name: Example API endpoint: [https://x07d-e032-f135.n7.xano.io/admin/workspace/1/api/2/query/13](https://x07d-e032-f135.n7.xano.io/admin/workspace/1/api/2/query/13) JSON data payload: \{"test": "hello there", "value": 123} Authentication: Yes - user: [test@email.com](mailto:test@email.com) Additional information and description of the issue: "This API endpoint seems to always be unusually slow. I'm experiencing a response time of x seconds. The endpoint is returning 25 records and the response looks to be correct. Let me know if you need any additional information"
</Info>

### How do I find all this information?

**Workspace name**:

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/28df6187-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=5e53619b686b443eca809b0b0a0725c4" width="782" height="175" data-path="images/28df6187-image.jpeg" />
</Frame>

**API Endpoint** **URL** that is slow:

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/05d797cc-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=27f7d2cc320b4c018c28dfff7ad54016" width="1450" height="196" data-path="images/05d797cc-image.jpeg" />
</Frame>

**JSON data payload** (if you are passing data to the API endpoint):

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/70d6cc07-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=615017c425474f12e2c1a05b77ca486f" width="529" height="279" data-path="images/70d6cc07-image.jpeg" />
</Frame>

**User ID or email address** (if the endpoint requires Authentication)

### What to Expect

Due to the complex nature of these requests, it can take an extended period for us to work together with you to diagnose and resolve these issues. Expect to budget **at least** **two to three weeks** to support these specific requests. We do have [priority support packages](/troubleshooting-and-support/getting-help#premium-support) available if this is not sufficient for you.

The team will review with you the actions you have already taken as detailed in our above, and make any recommendations for additional efficiency. Please understand that every Xano plan has its limits, and our ultimate recommendation may be to upgrade to a higher tier plan, but we will do everything we can to address outstanding issues before this.

#### Is there anywhere else I can get help?

We understand that sometimes waiting isn’t an option. There are multiple other avenues that you can take to get support with Xano.

* **The Xano Community** ([community.xano.com](https://community.xano.com))

* **Xano Development Partners** - We have Xano partners that we can connect you with if you would like direct help developing in Xano. If you would like to enlist a Xano Development Partner, please visit the [Marketplace](https://xano.com/marketplace) to find a development partner.

* **Connect With Xano Experts** - Create a post in the [Find an Expert](https://community.xano.com/find-a-xano-expert) category of the Community. Some members of the Community have a Trusted Xano Expert title. These members have been recognized by the Xano team to give great advice and support, however, they are not directly affiliated with Xano. These members may provide paid support services, which are also not affiliated with Xano in any way.


Built with [Mintlify](https://mintlify.com).