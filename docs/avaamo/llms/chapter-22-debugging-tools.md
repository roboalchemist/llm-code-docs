# Source: https://docs.avaamo.com/user-guide/tutorials-and-exercises/part-3-advanced-topics/chapter-22-debugging-tools.md

# Chapter 12: Debugging Tools

After completing the exercises in the lesson you will be able to:

* Use logging to troubleshoot code
* View Javascript errors

### **12.1** **Exercise: Logging Within JavaScript Blocks**

You can use console.log() to log errors and monitor these errors while testing the agent. Let us see how to add a console.log() a message and see it in the debug logs.

Navigate to your order pizza skill in my assistant agent:

* In the first node of the Dialog skill add a message to the console.
* Add a JavaScript response node in the first node and add the following code:&#x20;

`console.log("Hello World! This is my first console.log")`

* Navigate to your **Agent-> Debug-> Debug log**. This will open the debugging log on the left side of the screen. Test your agent and your console.log() statement will appear in the debugging logs.

![](https://lh5.googleusercontent.com/4nGz0OlmErUrEonUj7WQMjMIaN1Oi3emN37eyay-uKMAcI324ezNiOj1e8QFaN3nSargWfMzWKsJMCSXy1MhPnryKRB_w_Cwgs0soAmkOT8gIxR5-UlVKbpjy0ZyaR9RSO4NDGVP)

It is a good practice to add console.log() in API calls so that it is easier to figure out errors if an&#x79;**.**

### **12.2** **Exercise: Viewing JavaScript Errors**

You can view JavaScript errors from the agent dashboard.

* To view JavaScript errors navigate to **Agent -> Debug -> JS Errors**
* In the agent, My Assistant, navigate to JS errors to see if you can find any errors in your agent.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fv5%2F-MCQ5cA57CNCjlqZsBu8%2F-MCQ9svsUx0-4EioOrA7%2F68.jpeg?generation=1594962461615220\&alt=media)

See [Debug agents](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents), for more information.
