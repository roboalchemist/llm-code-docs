# Source: https://docs.avaamo.com/user-guide/tutorials-and-exercises/part-1-creating-my-agent/chapter-5-building-a-dialog-skill/exercise-5.3-capturing-data-from-a-conversation.md

# Exercise 5.3: Capturing data from a conversation

There are two ways to capture and store data from a conversation:&#x20;

* Using a JavaScript property `context.variables`.&#x20;
* Using Javascript methods: `Storage.user.set()` to store and `Storage.user.get()` to retrieve. For this example, you will be using context.variables. Context values are stored only along one single branch, if your conversation switches branches then the value is lost.

In the post-processing section of the document add this code for each node as shown below:

### Node 2&#x20;

* Name: `capture short description`
* Intent Type: Training Phrases
* Post Processing: Yes
* Post Processing Script:`context.variables.short_description = context.last_message;`

![](https://lh4.googleusercontent.com/yJX7uQB_qQAXKspW9VpJO-1onKeZz6bM7Ga7QZ4X2r__EbzUwWpvhcCG_lwuWNpc6e1fWFSabSDyhWO_Gf6rSKJ6mSbhWYK4mawaYVTUILPbjhpiKssrh8i0DBqce_0p675TRo6D)

### Node 3&#x20;

* Name: `capture description`&#x20;
* Intent Type: Custom Intent Code:&#x20;
* `return true`&#x20;
* Post Processing Script: `context.variables.short_description = context.last_message`;

![](https://lh5.googleusercontent.com/A1JtpP__McGORctdFMuP0GtSfCOb_6nocborCKJXzx8xONdigMxSXOUDL5YH5uk8ZQfyoWBFXHjQnLXmAGf6rwqU0XtI2hZAej0pa84Uei7hgbI5NEEjBHQTNvPqQJAw4uLjPVhj)

### Node 4&#x20;

* Name: `Capture Urgency`&#x20;
* Intent Type = Custom Intent Code
* `return true`&#x20;
* Post Processing: Yes &#x20;
* Post Processing Script: `context.variables.short_description = context.last_message;`

![](https://lh3.googleusercontent.com/iTjiDknDCPxm-gDwgoFJxreNGOf3QgzxaZbbWU14NoyIBsuy_w3SpYcRcehN89kUarcKKuq2dEnzRwdkYJ4jGvnt4eA87WZOJHTX3fApNdeM8A8t3dJAj-y4eiGTR48-MFjSaPXm)
