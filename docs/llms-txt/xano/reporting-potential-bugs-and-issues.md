# Source: https://docs.xano.com/troubleshooting-and-support/reporting-potential-bugs-and-issues.md

# Source: https://docs.xano.com/troubleshooting-and-support/getting-help/reporting-potential-bugs-and-issues.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reporting Potential Bugs & Issues

> Follow these guidelines to get the best possible support from our team.

### 🛠️ Best Practices for Reporting Issues in Xano

Having trouble with something in Xano and not sure how to get help? This guide will walk you through the best way to report a bug or performance issue so that our support team can assist you as efficiently as possible.

#### ✅ Before You Submit a Request

To save time and get a quicker resolution, make sure you've done the following first:

* **Tried debugging your function stack** to identify the problem area.
* **Checked your front-end setup**, especially if you're using external data sources (like Xano).
* **Searched the Xano Documentation and Community** for similar issues.
* **Verified your usage graphs** to detect performance bottlenecks.

If you've taken those steps and still need help, please submit your issue using the template below.

***

### 📝 Copy & Paste Support Request Template

> 💡 Just copy this into your support request and fill it in with your details.

```
Workspace Name: 

URL to where you are experiencing the issue (API endpoint, function, table, etc...): 

JSON Payload for testing (if applicable): 

Is Authentication Required? Yes/No
  - If yes, provide user email or ID: 
  
Screenshots (Usage Graph/API Request Graph): 
  - [Attach screenshots showing recent usage]
  
Video Demonstration of Issue:
  - Use Loom, Tella, Jam.dev or your preferred service
  
Describe the issue in detail:
  - Is the issue consistent or intermittent?
  - Are records being returned? If so, how many?
  - Any recent changes that might have affected this?

Additional Notes:
```

***

### 🧾 Example (Filled Out Template)

```
Workspace Name: Example Workspace

URL to where you are experiencing the issue (API endpoint, function, table, etc...): https://x07d-e032-f135.n7.xano.io/admin/workspace/1/api/2/query/13

JSON Payload for testing (if applicable): {"test": "hello there", "value": 123}

Is Authentication Required? Yes
  - If yes, provide user email or ID: Yes - test@email.com
  
Screenshots:
  - [Attached: CPU usage graph, API request graph for last 24 hours]
  
Video Demonstration of Issue:
  - http://loom.com/my-video
  
Describe the issue in detail:
  - The endpoint is always slow — taking ~7 seconds to respond.
  - It returns 25 records consistently, and the response appears correct.
  - When we run it in Xano, it's fine, but outside of Xano, it's not working as expected -- see video
  - No changes have been made to the function stack recently.
  
Additional Notes:
  - Please let me know if you need any more details.
```

***

#### ⏳ What to Expect After Submitting

* **Response Time**: It can take 2–3 weeks to fully resolve complex issues, especially performance-related ones. Your Xano plan may dictate more specific SLAs or response times.
* **Support Review**: Our team will walk through the steps you've already tried and may suggest additional improvements.
* **Plan Consideration**: Some issues might be tied to usage limits on your current plan. We’ll explore every avenue before recommending a plan upgrade.

Need faster help? Consider our [priority support packages](..#premium-support).

***

### 🔍 Other Ways to Get Help

If you're in a hurry or want to explore more help options:

* [**Xano Community**](https://community.xano.com/) – Ask questions, share issues, and learn from others.
* **Xano Development Partners** – Find expert developers through the [Xano Marketplace](https://www.xano.com/marketplace).


Built with [Mintlify](https://mintlify.com).