# Source: https://pipedream.com/docs/workflows/building-workflows/using-props.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Props

<Frame>
  <iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/RW9FBVuHDHQ" title="Using Props" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</Frame>

Props are fields that can be added to code steps in a workflow to abstract data from the code and improve reusability. Most actions use props to capture user input (e.g., to allow users to customize the URL, method and payload for the Send HTTP Request action). Props support the entry of simple values (e.g., `hello world` or `123`) or expressions in `{{ }}` that can reference objects in scope or run basic Node.js code.

## Entering Expressions

Expressions make it easy to pass data exported from previous steps into a code step or action via props. For example, if your workflow is triggered on new Tweets and you want to send the Tweet content to an HTTP or webhook destination, you would reference `{{steps.trigger.event.body}}` to do that.

While the data expected by each input depends on the data type (e.g., string, integer, array, etc) and the data entry mode (structured or non-structured — if applicable), the format for entering expressions is always the same; expressions are always enclosed in `{{ }}`.

There are three ways to enter expressions in a prop field — you can use the object explorer, enter it manually, or paste a reference from a step export.

### Use the object explorer

When you click into a prop field, an object explorer expands below the input. You can explore all the objects in scope, filter for keywords (e.g., a key name), and then select the element to insert into the form as an expression.

<Frame>
  <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/7b2d1c9b-CleanShot_2022-04-05_at_10.35.37_nxykkx.gif?s=b26f8acbc5685756e651058e86d4379b" width="800" height="406" data-path="images/7b2d1c9b-CleanShot_2022-04-05_at_10.35.37_nxykkx.gif" />
</Frame>

### Manually enter or edit an expression

To manually enter or edit an expression, just enter or edit a value between double curly braces `{{ }}`. Pipedream provides auto-complete support as soon as you type.

<Frame>
  <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/07454d28-CleanShot_2024-03-15_at_09.38.09_topm8f.gif?s=78072894b8f191d2879999d0a55e1a0a" width="744" height="330" data-path="images/07454d28-CleanShot_2024-03-15_at_09.38.09_topm8f.gif" />
</Frame>

You can also run Node.js code in `{{ }}`. For example, if `event.foo` is a JSON object and you want to pass it to a param as a string, you can run `{{JSON.stringify(event.foo)}}`.

### Paste a reference from a step export

To paste a reference from a step export, find the reference you want to use, click **Copy Path** and then paste it into the input.

<Frame>
  <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/88e49519-CleanShot_2024-03-15_at_09.39.18_mfd5wa.gif?s=5957162aef25878a1866ffa084ca7928" width="740" height="652" data-path="images/88e49519-CleanShot_2024-03-15_at_09.39.18_mfd5wa.gif" />
</Frame>

Built with [Mintlify](https://mintlify.com).
