# Source: https://docs.avaamo.com/user-guide/llamb/llamb-filters/hallucination-filters.md

# Hallucination filters

A hallucination filter in LLaMB involves a mechanism designed to detect and mitigate instances where the model generates false, misleading, or fabricated information.

## How does it work? <a href="#id-5rcbmb1ikk1p" id="id-5rcbmb1ikk1p"></a>

The hallucination filter in LLaMB works by detecting and generating faithful responses to the claims made in the answer from the given context.

The generated answer is considered faithful if all the claims made can be inferred from the given context. To determine this, a set of claims from the generated answer is first identified. Each of these claims is then cross-checked with the provided context to verify whether it can be inferred from that context.

## **Post-Go-Live** phase

### Step 1 - Review and Monitor

The first 2 weeks after going live, review every thumbs-down feedback in a given 24-hour period. See [Analytics](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics) and [Query insights](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/query-insights), for more information on how to extract the analytics data.

### Step 2 - Report the observations for swift action

* Report your observation and attach an Urgency.xls file with the Jailbreak query, current response, and suggested response.
* All hallucination production scenarios are considered at the highest severity and Avaamo Support will take immediate action based on the information provided.

{% hint style="info" %}
**Note**: This is the emergency response that suppresses LLaMB-generated response instantly. This works on question similarity. There is no need to add a lot of variations, however, Avaamo Support can add variations you tested.
{% endhint %}

## Examples <a href="#g3n48ngsae" id="g3n48ngsae"></a>

The following example illustrates how the hallucination filters work in LLaMB by generating faithful and factual responses:

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FS9h2Wv1WxjCWLxRmo6SX%2F5.png?alt=media" alt="" width="375"></div>
