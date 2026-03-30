# Source: https://console.groq.com/docs/flutterflow

---
description: Learn how to use FlutterFlow with Groq to build and deploy fast, cross-platform AI-powered applications with beautiful UIs and rapid iteration.
title: FlutterFlow + Groq: Fast, Cross-Platform AI Apps - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [FlutterFlow + Groq: Fast & Powerful Cross-Platform Apps](#flutterflow--groq-fast--powerful-crossplatform-apps)

[**FlutterFlow**](https://flutterflow.io/) is a visual development platform to build high-quality, custom, cross-platform apps. By leveraging Groq's fast AI inference in FlutterFlow, you can build beautiful AI-powered apps to:

* **Build for Scale**: Collaborate efficiently to create robust apps that grow with your needs.
* **Iterate Fast**: Rapidly test, refine, and deploy your app, accelerating your development.
* **Fully Integrate Your Project**: Access databases, APIs, and custom widgets in one place.
* **Deploy Cross-Platform**: Launch on iOS, Android, web, and desktop from a single codebase.

### [FlutterFlow + Groq Quick Start (10 minutes to hello world)](#flutterflow--groq-quick-start-10-minutes-to-hello-world)

#### [1\. Securely store your Groq API Key in FlutterFlow as an App State Variable](#1-securely-store-your-groq-api-key-in-flutterflow-as-an-app-state-variable)

Go to the App Values tab in the FlutterFlow Builder, add `groqApiKey` as an app state variable, and enter your API key. It should have type `String` and be `persisted` (that way, the API Key is remembered even if you close out of your application).

![Store your api key securely as an App State variable by selecting "secure persisted fields"](https://console.groq.com/showcase-applications/flutterflow/flutterflow_1.png)

_Store your api key securely as an App State variable by selecting "secure persisted fields"_

#### [2\. Create a call to the Groq API](#2-create-a-call-to-the-groq-api)

Next, navigate to the API calls tab Create a new API call, call it `Groq Completion`, set the method type as `POST`, and for the API URL, use: <https://api.groq.com/openai/v1/chat/completions>

Now, add the following variables:

* `token` \- This is your Groq API key, which you can get from the App Values tab.
* `model` \- This is the model you want to use. For this example, we'll use `llama-3.3-70b-versatile`.
* `text` \- This is the text you want to send to the Groq API.

![Screenshot 2025-02-11 at 12.05.22 PM.png](https://console.groq.com/showcase-applications/flutterflow/flutterflow_2.png)

#### [3\. Define your API call header](#3-define-your-api-call-header)

Once you have added the relevant variables, define your API call header. You can reference the token variable you defined by putting it in square brackets (\[\]).

Define your API call header as follows: `Authorization: Bearer [token]`

![Screenshot 2025-02-11 at 12.05.38 PM.png](https://console.groq.com/showcase-applications/flutterflow/flutterflow_3.png)

#### [4\. Define the body of your API call](#4-define-the-body-of-your-api-call)

You can drag and drop your variables into the JSON body, or include them in angle brackets.

Select JSON, and add the following:

* `model` \- This is the model we defined in the variables section.
* `messages` \- This is the message you want to send to the Groq API. We need to add the 'text' variable we defined in the variables section within the message within the system-message.

You can modify the system message to fit your specific use-case. We are going to use a generic system message: "Provide a helpful answer for the following question - text"

![Screenshot 2025-02-11 at 12.05.49 PM.png](https://console.groq.com/showcase-applications/flutterflow/flutterflow_4.png)

#### [5\. Test your API call](#5-test-your-api-call)

By clicking on the “Response & Test” button, you can test your API call. Provide values for your variables, and hit “Test API call” to see the response.

![Screenshot 2025-02-11 at 12.32.34 PM.png](https://console.groq.com/showcase-applications/flutterflow/flutterflow_5.png)

#### [6\. Save relevant JSON Paths of the response](#6-save-relevant-json-paths-of-the-response)

Once you have your API response, you can save relevant JSON Paths of the response. To save the content of the response from Groq, you can scroll down and click “Add JSON Path” for `$.choices[:].message.content` and provide a name for it, such as “groqResponse”

![Screenshot 2025-02-11 at 12.34.22 PM.png](https://console.groq.com/showcase-applications/flutterflow/flutterflow_6.png)

#### [7\. Connect the API call to your UI with an action](#7-connect-the-api-call-to-your-ui-with-an-action)

Now that you have added & tested your API call, let’s connect the API call to your UI with an action.

_If you are interested in following along, you can_ [**clone the project**](https://app.flutterflow.io/project/groq-documentation-vc2rt1) _and include your own API Key. You can also follow along with this [3-minute video.](https://www.loom.com/share/053ee6ab744e4cf4a5179fac1405a800?sid=4960f7cd-2b29-4538-89bb-51aa5b76946c)_

![Screenshot 2025-02-25 at 3.48.16 PM.png](https://console.groq.com/showcase-applications/flutterflow/flutterflow_7.png)

In this page, we create a simple UI that includes a TextField for a user to input their question, a button to trigger our Groq Completion API call, and a Text widget to display the result from the API. We define a page state variable, groqResult, which will be updated to the result from the API. We then bind the Text widget to our page state variable groqResult, as shown below.

![Screenshot 2025-02-25 at 3.58.57 PM.png](https://console.groq.com/showcase-applications/flutterflow/flutterflow_8.png)

#### [8\. Define an action that calls our API](#8-define-an-action-that-calls-our-api)

Now that we have created our UI, we can add an action to our button that will call the API, and update our Text with the API’s response. To do this, click on the button, open the action editor, and add an action to call the Groq Completion API.

![Screenshot 2025-02-25 at 4.05.30 PM.png](https://console.groq.com/showcase-applications/flutterflow/flutterflow_9.png)

To create our first action to the Groq endpoint, create an action of type Backend API call, and set the "group or call name" to `Groq Completion`. Then add two additional variables:

* `token` \- This is your Groq API key, which you can get from the App State tab.
* `text` \- This is the text you want to send to the Groq API, which you can get from the TextField widget.

Finally, rename the action output to `groqResponse`.![Screenshot 2025-02-25 at 4.57.28 PM.png](https://console.groq.com/showcase-applications/flutterflow/flutterflow_10.png)

#### [9\. Update the page state variable](#9-update-the-page-state-variable)

Once the API call succeeds, we can update our page state variable `groqResult` to the contents of the API response from Groq, using the JSON path we created when defining the API call.

Click on the "+" button for True, and add an action of type "Update Page State". Add a field for `groqResult`, and set the value to `groqResponse`, found under Action Output. Select `JSON Body` for the API Response Options, `Predifined Path` Path for the Available Options, and `groqResponse` for the Path.

![Screenshot 2025-02-25 at 5.03.33 PM.png](https://console.groq.com/showcase-applications/flutterflow/flutterflow_11.png)

![Screenshot 2025-02-25 at 5.03.47 PM.png](https://console.groq.com/showcase-applications/flutterflow/flutterflow_12.png)

#### [10\. Run your app in test mode](#10-run-your-app-in-test-mode)

Now that we have connected our API call to the UI as an action, we can run our app in test mode.

_Watch a [video](https://www.loom.com/share/8f965557a51d43c7ba518280b9c4fd12?sid=006c88e6-a0f2-4c31-bf03-6ba7fc8178a3) of the app live in test mode._

![Screenshot 2025-02-25 at 5.37.17 PM.png](https://console.groq.com/showcase-applications/flutterflow/flutterflow_13.png)

![Result from Test mode session](https://console.groq.com/showcase-applications/flutterflow/flutterflow_14.png)

_Result from Test mode session_

**Challenge:** Add to the above example and create a chat-interface, showing the history of the conversation, the current question, and a loading indicator.

### [Additional Resources](#additional-resources)

For additional documentation and support, see the following:

* [Flutterflow Documentation](https://docs.flutterflow.io/)