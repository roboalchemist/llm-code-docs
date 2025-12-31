# Source: https://www.activepieces.com/docs/flows/passing-data.md

# Passing Data

> Using data from previous steps in the current one

## Data flow

Any Activepieces flow is a vertical diagram that **starts with a trigger step** followed by **any number of action steps**.

Steps are connected vertically. Data flows from parent steps to the children. Children steps have access to the output data of the parent steps.

## Example Steps

<video width="450" autoPlay muted loop playsinline src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-3steps.mp4?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=525e82220343a9d0e119dd469dc998c1" data-path="resources/passing-data-3steps.mp4" />

This flow has 3 steps, they can access data as follows:

* **Step 1** is the main data producer to be used in the next steps. Data produced by Step 1 will be accessible in Steps 2 and 3. Some triggers don't produce data though, like Schedules.

* **Step 2** can access data produced by Step 1. After execution, this step will also produce data to be used in the next step(s).

* **Step 3** can access data produced by Steps 1 and 2 as they're its parent steps. This step can produce data but since it's the last step in the flow, it can't be used by other ones.

## Data to Insert Panel

In order to use data from a previous step in your current step, place your cursor in any input, the **Data to Insert** panel will pop up.

<video autoPlay muted loop playsinline src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-data-to-insert-panel.mp4?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=3d46b25cb67d411f95ee083d71fc447c" data-path="resources/passing-data-data-to-insert-panel.mp4" />

This panel shows the accessible steps and their data. You can expand the data items to view their content, and you can click the items to insert them in your current settings input.

If an item in this panel has a caret (⌄) to the right, it means you can click on the item to expand its child properties. You can select the parent item or its properties as you need.

When you insert data from this panel, it gets inserted at the cursor's position in the input. This means you can combine static text and dynamic data in any field.

<video autoPlay muted loop playsinline src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-main-insert-data-example.mp4?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=2ae302d3f0edd883c207ffbf1dabee7a" data-path="resources/passing-data-main-insert-data-example.mp4" />

We generally recommend that you expand the items before inserting them to understand the type of data they contain and whether they're the right fit to the input you're filling.

## Testing Steps to Generate Data

We require you to test steps before accessing their data. This approach protects you from selecting the wrong data and breaking your flows after publishing them.

If a step is not tested and you try to access its data, you will see the following message:

<img width="350" src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-test-step-first.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=3bc8bb574124a5a119ba97ae4995acc8" alt="Test your automation step first" data-og-width="798" data-og-height="988" data-path="resources/passing-data-test-step-first.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-test-step-first.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=cabf8db7e71bab1723dc2799e1de0e29 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-test-step-first.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=395766bb57845ebb1d0e6c6aa176ed7f 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-test-step-first.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=34a3bce214b6665784158841a0c0598e 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-test-step-first.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=330141a5e22a170def0fedaf1c268def 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-test-step-first.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=4f2dee5f9d48e411fe12805e063a4ed3 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-test-step-first.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=04841ffe0b6ca0ba9835947574e951b7 2500w" />

To fix this, go to the step and use the Generate Sample Data panel to test it. Steps use different approaches for testing. These are the common ones:

* **Load Data:** Some triggers will let you load data from your connected account without having to perform any action in that account.
* **Test Trigger:** Some triggers will require you to head to your connected account and fire the trigger in order to generate sample data.
* **Send Data:** Webhooks require you to send a sample request to the webhook URL to generate sample data.
* **Test Action:** Action steps will let you run the action in order to generate sample data.

Follow the instructions in the Generate Sample Data panel to know how your step should be tested. Some triggers will also let you Use Mock Data, which will generate static sample data from the piece. We recommend that you test the step instead of using mock data.

This is an example for generating sample data for a trigger using the **Load Data** button:

<video autoPlay muted loop playsinline src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-load-data.mp4?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=318c97848c527caceb7186d926d50af7" data-path="resources/passing-data-load-data.mp4" />

## Advanced Tips

### Switching to Dynamic Values

Dropdowns and some other input types don't let you select data from previous steps. If you'd like to bypass this and use data from previous steps instead, switch the input into a dynamic one using this button:

<video autoPlay muted loop playsinline src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-dynamic-value.mp4?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=e25b49eb497509a2267dc9bd39cb3240" data-path="resources/passing-data-dynamic-value.mp4" />

### Accessing data by path

If you can't find the data you're looking for in the **Data to Insert** panel but you'd like to use it, you can write a JSON path instead.

Use the following syntax to write JSON paths:

`{{step_slug.path.to.property}}`

The `step_slug` can be found by moving your cursor over any of your flow steps, it will show to the right of the step.
