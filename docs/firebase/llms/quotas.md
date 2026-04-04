# Source: https://firebase.google.com/docs/firestore/enterprise/quotas.md.txt

# Source: https://firebase.google.com/docs/functions/quotas.md.txt

# Source: https://firebase.google.com/docs/firestore/quotas.md.txt

# Source: https://firebase.google.com/docs/ai-logic/quotas.md.txt

# Source: https://firebase.google.com/docs/firestore/quotas.md.txt

# Source: https://firebase.google.com/docs/ai-logic/quotas.md.txt

<br />

<br />

|----------------------------------------------------------------------------------------------------------------------------------|
| *Click yourGemini APIprovider to view provider-specific content and code on this page.* Gemini Developer APIVertex AI Gemini API |

<br />

<br />

Rate limits (commonly called quotas) regulate the number of requests you can make to theGemini APIwithin a given timeframe. These limits help ensure fair usage, protect against abuse, and help maintain system performance for all users.

When usingFirebase AI Logicto send requests toGeminiandImagenmodels, your project's rate limits depend on your chosen "Gemini API" provider.Firebase AI Logicalso provides a way to[set "per user" rate limits](https://firebase.google.com/docs/ai-logic/quotas#per-user-rate-limits).

[View rate limits for theGemini Developer API](https://ai.google.dev/gemini-api/docs/rate-limits)
| The rate limits (like requests per minute (RPM)) that are listed in the documentation are the*maximum* that theGemini Developer APIsupports.
|
| The*actual maximum quota**available to your Firebase project**and the model that you're using* are dependent on several factors (for example, the standing of your linkedCloud Billingaccount and capacity of the overall system).
|
| **Starting on December 7, 2025, theGemini Developer APIquota for both the Free Tier and Paid Tier 1 were adjusted. These changes may lead to unexpected 429 quota-exceeded errors.**

If you exceed the quota, then you'll get a 429 quota-exceeded error.

## How rate limits (quotas) work

Rate limits (quotas) are measured across four dimensions:

- Requests per minute (RPM)
- Requests per day (RPD)
- Tokens per minute (TPM)
- Tokens per day (TPD)

Your usage is evaluated against each limit, and exceeding any of them will trigger a 429 quota-exceeded error. For example, if your RPM limit is 20, then making 21 requests within a minute will result in an error, even if you haven't exceeded your TPM or other limits.

Rate limits are applied at the project-level and apply to all applications and IP addresses that use that Firebase project.

Limits vary depending on the specific model being used, and some limits only apply to specific models. For example, images per minute (IPM) is only calculated for models capable of generating images (Imagen), but is conceptually similar to TPM.

Rate limits are more restricted for experimental and preview models.

## Request a rate limit increase

If you're on a "paid tier" for theGemini Developer API, then you can[request a rate limit increase](https://ai.google.dev/gemini-api/docs/rate-limits#request-rate-limit-increase).

## Set "per user" rate limits

To useFirebase AI Logic, your project needs your chosenGemini APIprovider enabled, but you also need the[Firebase AI LogicAPI](https://console.cloud.google.com/apis/library/firebasevertexai.googleapis.com?project=_)enabled, which acts as a gateway between our client SDKs and yourGemini APIprovider. This API is enabled for you when you initially set upFirebase AI Logicin your Firebase project.

**You can use theFirebase AI LogicAPI rate limit (quota) as a "per user" rate limit for your app** , specifically for the AI features that rely onFirebase AI Logic. You should[set this limit](https://firebase.google.com/docs/ai-logic/quotas#edit-quota-or-request-quota-increase)to reasonably accommodate a single user accessing your AI features, while also ensuring that no single user overwhelms the limits of yourGemini APIprovider (which is meant to be shared by all your users).
| **Note:** TheFirebase AI LogicAPI rate limit is set quite high by default (100 RPM) to be usable for any app's use case. We recommend that you[adjust this rate limit](https://firebase.google.com/docs/ai-logic/quotas#edit-quota-or-request-quota-increase)to meet the actual needs of your app and use case.

### Details about the "per user" rate limit

Here are some important details about theFirebase AI LogicAPI rate limits (quotas) -- specifically, requests per minute (RPM):

- It's based on "Generate content requests" on a per-user per-region per-minute basis, and it's*not*based on model.

- It's the rate limit applied to*all* your users. Currently, there isn't a way to set the rate limit for a specific user or specific group of users^**\***^.

- It applies at the project-level and applies to all applications and IP addresses that use that Firebase project.

- It applies to any call that specifically comes from anyFirebase AI LogicSDK.

- The default rate limit is 100 RPM per user.  
  Note that you still need to consider the limits for yourGemini APIprovider (see above), which take precedence over theFirebase AI LogicAPI.

^**\*** *If you're using theVertex AIGemini APIand your app directs users to different regions (for example, using[Firebase Remote Config](https://firebase.google.com/docs/ai-logic/solutions/remote-config?api=vertex)), then you could set a specific rate limit for users in a specific region.*^

### Adjust the "per user" rate limit

To adjust a rate limit (quota), you must have the`serviceusage.quotas.update`permission, which is included by default in the Owner and Editor role.

Here's how to edit your rate limit (quota) or request an increase:

1. In theGoogle Cloudconsole, go to the page for the[Firebase AI LogicAPI](https://console.cloud.google.com/apis/library/firebasevertexai.googleapis.com?project=_).

2. Click**Manage**.

3. Lower on the page, click the**Quotas \& System Limits**tab.

4. Filter the table to show the quotas of interest, like the capability (requests for generating content) and region.

   For example, to view the per-user quotas for generating content requests in any of the supported Asian regions, your filter would look similar to this:`Generate content requests`+`Dimension:region:asia`
   | **Note:** To create a`Dimension`filter, you need to use the filter tooling, rather than just copy-pasting the values in this example above. Also, the`(default)`quota row doesn't apply toFirebase AI Logic.
5. Select the checkbox to the left of each quota of interest.

6. At the end of the quota's row, clickmore_vert, and then select**Edit quota**.

7. In the**Quota changes**form, do the following:

   1. Enter the increased quota in the*New value*field.

      This quota applies at the project-level and is shared across all applications and IP addresses that use that Firebase project.
   2. Complete any additional fields in the form, and then click**Done**.

   3. Click**Submit request**.