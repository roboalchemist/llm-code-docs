# Source: https://docs.logrocket.com/docs/galileo.md

# Galileo AI

LogRocket combines machine learning algorithms and large language models (LLMs) to surface impactful, actionable insights in natural language.

## Galileo AI for Session Highlights

### What is Galileo AI for Session Highlights?

Galileo Highlights is an AI-powered feature that summarizes sessions so you can find the moment you are looking for as quickly as possible.

Highlights will "watch" up to 10 sessions at a time from a single user. It will provide a general summary of all of these sessions, as well as more detailed summaries of each session. These overviews include links that take you right to that moment in the session, so you can zero-in on the moment you're looking for.

<Image align="center" src="https://files.readme.io/8f8048054730bb27cd4a57331619686f069acb403034b4e9fb5b9321e6f90923-What_is_Galileo_AI_for_Session_Highlights_.png" />

<br />

For more information about Galileo Highlights, and Galileo Highlights API, read more here:

* [Galileo Highlights Overview](https://docs.logrocket.com/docs/galileo-highlights-beta)
* [Galileo Highlights API](https://docs.logrocket.com/docs/session-highlights-api)

## Galileo AI for Issues

### What is Galileo AI for Issues?

Galileo is an AI layer that sits on top of the LogRocket platform. It combines information about how users react to problems with traditional error reporting and analytics to develop a human-like understanding of user behavior and uncover high-impact, actionable insights in user behavior, including:

* Severe technical issues such as errors, failed network requests, and [error states](https://docs.logrocket.com/docs/issues#error-state-issue-type).
* Usability issues leading to user struggle such as rage clicks, dead clicks, and frustrating network requests.
* Issues causing users to drop out of funnels and key workflows.

### How does Galileo AI for Issues work?

Galileo's models have been trained on billions of data points to predict whether identified issues and friction points are important, automating the analytics work that humans already do in LogRocket. Importance is based on vectors such as impact, frequency, and years of user feedback around what matters most.

Galileo learns via user feedback, so its recommendations are constantly improving. Activities such as [triaging issues](https://docs.logrocket.com/docs/issues#grouping-issues) as "high impact", "low impact", or "ignored" help Galileo better understand what matters most and make more accurate and relevant recommendations in the future.

### Galileo AI for Issues Features

Galileo scans your issues, assessing issue events for significant user impact that can be distinguished by user expressing frustration or confusion, or an explicit errors or error state disrupting and ending early a user journey.

#### Reduces noise, focuses on signal

Similar solutions create an incredible amount of noise and expect users to make sense of the noise, sifting through to look for signal. This is time- and resource-intensive for teams. Galileo directs users to the signal, filtering out the noise and leaving users with a short list of just the most impactful issues to save you time searching. It's not common for applications to have 5-15,000 issues, each with multiple issue events. Therefore, Galileo starts by reducing the a highlighted list of the 5-25 most impactful issues.

> 📘 Minimum issue event count to be severe
>
> Issues need to occur a minimum of 3 times before LogRocket will consider an issue severe.

#### [Issues Digest](https://docs.logrocket.com/docs/issues-digests)

Receive daily or weekly updates on the top recommended issues as identified by Galileo, delivered via **Slack**, **Microsoft Teams**, **email**, or **webhook**. Issues Digest will send the top 5 issues each week so that you can be efficient with your time and focus your efforts on the issues with the greatest impact.

<Image align="center" alt="example of an Issues Digest via email" border={true} caption="example of an Issues Digest via email" src="https://files.readme.io/2c53576-email-digest.jpg" width="350px" />

### Natural language issue titles (in Beta)

Galileo leverages an LLM to create natural language descriptions of all severe issues. It ingests session events to "watch" sessions and identify patterns in user behavior. It then asks itself questions about what is happening in those sessions and distills those answers into descriptions of the issue that is causing users to struggle.

This allows anyone -- regardless of technical experience -- to assess the impact on user experience and effectively prioritize a resolution.

Example of a standard JS error issue without natural language titles: `TypeError: Cannot read properties of undefined (reading 'pc') `

| Default Title                                                   | Natural Language Title                                                           |
| :-------------------------------------------------------------- | :------------------------------------------------------------------------------- |
| "TypeError: Cannot read properties of undefined (reading 'pc')" | "**Users encountering loading error message when navigating to Settings page."** |
| "Dead click on Submit button"                                   | **"Users unable to verify phone numbers during sign-up process"**                |
| "Network Error 404 GET query getInventory"                      | **"Users unable to load inventory list on Best Sellers page"**                   |

<br />

**Natural language issues are currently in Beta**. If you'd like access, you can activate them in the Issues tab, or by contacting us for a demo [here](https://lp.logrocket.com/galileo-ai-demo).

<Image align="center" className="border" border={true} src="https://files.readme.io/070879d2903b8dbdcfc76f49286535e9c2da8c41a884cfd370b2efdb1fbbecef-Natural_language_issue_titles_in_Beta.png" />

## Galileo AI For Funnel Insights

### What is Galileo AI for Funnel Insights?

Galileo Funnel Insights is an AI-powered feature that summarizes the behavior of non-converting users so that you can quickly understand drop-off and improve conversion.

Galileo will "watch" a sample of non-converting sessions. It will categorize the sessions it watches into "insights" which represent the common behavior exhibited in the sessions. Each "insight" will describe the users behavior and provide links to the relevant sessions. As such, you can quickly find and understand undesirable behaviors and make changes in your application to discourage unwanted patterns.

<Image align="center" src="https://files.readme.io/7bed4301acd5a45767dd66e73970e82713e9182c3e32e514cadb1203cebec420-What_is_Galileo_AI_for_Funnel_Insights_.png" />

For more information about Galileo Funnel Insights, read more here:

* [Galileo Funnel Insights Overview](https://docs.logrocket.com/docs/galileo-funnel-insights)

> 📘 How Galileo AI Uses Data
>
> LogRocket is committed to keeping all customer data safe and secure. The model used to calculate severity scores is proprietary and heavily redacted. It only uses generic counts of actions to keep data fully anonymous. Session data sent to LLMs is never used to train models, and the LLMs we use are fully compliant with SOC II, GDPR, and CCPA. All data sent is encrypted both in transit and at rest.
>
> If you have additional questions, please reach out to your Customer Success Manager, or contact us at [support@logrocket.com](mailto:support@logrocket.com)