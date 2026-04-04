# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v9.0.0/introducing-llamb-content-regression-testing.md

# Introducing "LLaMB Content Regression Testing"

In this release, a new feature `LLaMB Content Regression Testing` has been introduced for LLaMB. Previously available only for other skills, this functionality has now been extended to include LLaMB-specific skills.

Regression testing is a tool for verifying that an agent's responses are accurate and consistent with previous versions. It helps ensure that queries and their corresponding responses remain correct, even as the underlying models and AI tools evolve.&#x20;

The goal of regression testing is to ensure that query responses remain consistent over time, providing users with confidence in the agent’s performance and reliability.

To access LLaMB regression testing, go to the `Agent` page and click `Test > LLaMB Regression` in the left navigation menu.

{% hint style="info" %}
**Note:** The LLaMB Regression Test option is visible only if the agent is configured with an `LLaMB` content skill.
{% endhint %}

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fl1gCwkf8H3HhTAPNOqpE%2Fimage%20(5).png?alt=media&#x26;token=df38f644-427d-4b08-b33a-fe5b9fa77bf3" alt=""><figcaption></figcaption></figure>

## How to use it?

The steps to set up regression, execute it, and download the results remain similar to those of classic agents; however, the regression test file format for preparing the input file and analyzing the results differs in LLaMB. See [LLaMB regression testing](https://docs.avaamo.com/user-guide/llamb/regression-testing), for more information.

### Step 1: Prepare regression test input file

A regression test file contains a set of questions, the actual answer to each question, which is the ground truth, and any user properties specific to that answer.&#x20;

{% hint style="success" %}
**Key point:** Collaborate with Subject Matter Experts to build a regression test file in the Discovery phase itself.
{% endhint %}

The following is a sample regression test input file. See [Regression test file format](https://docs.avaamo.com/user-guide/llamb/regression-testing/regression-test-file-format), for more information.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FNRvsxQqNntTrmIFCVTxn%2FScreenshot%202025-04-15%20at%2011.13.40%E2%80%AFAM.png?alt=media&#x26;token=72085f99-9bde-4439-ab64-6ab93d05aefc" alt=""><figcaption></figcaption></figure>

### Step 2: Run the regression test

Running LLaMB remains the same as running regression for classic agents. See [Run regression test](https://docs.avaamo.com/user-guide/llamb/regression-testing/run-regression-test), for more information.

### Step 3: Analyze the results and improvise

You can analyse the results after the run by downloading the file, which includes details of the pass/fail statistics for each query.

The following is a sample regression test input file. See [Understanding results](https://docs.avaamo.com/user-guide/llamb/regression-testing/understanding-results), for more information.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FVJeoBmq8mmzu0cRTChdq%2FScreenshot%202025-04-24%20at%2010.30.02%E2%80%AFAM.png?alt=media&#x26;token=a217017f-d15d-4896-9541-00cde69ff513" alt=""><figcaption></figcaption></figure>

&#x20;Next step is to improve your accuracy. See [How to improve accuracy?](https://docs.avaamo.com/user-guide/llamb/regression-testing/how-to-improve-accuracy) for more information.
