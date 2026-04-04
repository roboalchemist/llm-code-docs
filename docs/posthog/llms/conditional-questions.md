# Source: https://posthog.com/docs/surveys/conditional-questions.md

# Conditional questions - Docs

It is useful to be able to display survey questions conditionally. For example, you may want to ask follow-up questions based on a user's responses. PostHog offers several ways to do this:

## Simple branching

For every question type, you can define the next step to navigate to after a question is completed. Click on **After this question, go to:**, then choose the next step you want to transition to. The options are:

-   Next question
-   Any specific question
-   Confirmation message (if present) or End

## Response-based conditions

For the **single choice** and **rating** question types, you can define the next step based on the response received.

Click on **After this question, go to:**, and then choose **Specific question based on answer**. Depending on your question type, this will present the following options:

1.  For the **Single choice** question type, you can specify the next step based on the selected answer.

![Survey single choice branching](https://res.cloudinary.com/dmukukwp6/image/upload/surveys_branching_singlechoice_8053dd1700.png)![Survey single choice branching](https://res.cloudinary.com/dmukukwp6/image/upload/surveys_branching_singlechoice_dark_0ec63f974a.png)

2.  For the **Rating** question type, you can specify the next step based on the response bucket received. For example, for a rating question with a scale from 1 to 5, the responses will be bucketed into categories: *negative*, *neutral*, and *positive*. The conditions are executed based on which bucket the individual response falls into.

![Survey rating branching](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2024_07_03_at_14_09_29_210ff7ced4.png)![Survey rating branching](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2024_07_03_at_14_10_37_7804a733b4.png)

By default, a question proceeds to the next question in the survey unless specified otherwise. If you want a question to be the last one, but it is not the final question in the list, you need to explicitly set the value for **After this question go to** to **Confirmation message** (if present) or **End**..

![Survey end branching](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2024_07_03_at_14_15_15_8d0d9053d9.png)![Survey end branching](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2024_07_03_at_14_16_21_683fb41cda.png)

## Testing

We currently don't have the ability to test the survey flow interactively via preview, but we will add this feature soon. In the meantime, we recommend testing the branching flows by first releasing the survey to yourself.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better