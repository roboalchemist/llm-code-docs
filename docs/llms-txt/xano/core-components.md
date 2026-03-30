# Source: https://docs.xano.com/building/logic/core-components.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Core Components of Logic

> Learn about what makes up the logic and workflows you build in Xano

## Logic Basics

Logic that you build in Xano is made up of several core components that you'll see across the entire platform. Each primitive, or 'thing you can build' (like APIs, AI Agents, and more) has its own set of components it uses, but you'll also find some overlap between them. For example, APIs, custom functions, and AI tools all use inputs, but background tasks don't. However, those same primitives all have a stack which contains what will actually run when it's time to do so.

<Card title="Inputs" icon="input-text" href="/building/logic/core-components/inputs">
  Inputs are the data that the logic might need to perform its operation. They are declared in the input block of the primitives that support them. Inputs are optional, but the block must be declared even if empty.
</Card>

<br />

<Card title="Logic" icon="arrow-progress" href="/building/logic/core-components/logic">
  What happens during execution. Your logic can be comprised of any combination of:

  **Functions**

  * Functions are individual pieces of logic, like getting a record from the database, or generating a random number.

  <Card title="Learn more about functions" icon="function" horizontal href="/building/logic/core-components/functions" />

  **Filters**

  * Filters are applied 'inline' to other values, and are used to transform or manipulate data, such as trimming whitespace or converting to uppercase.

  <Card title="Learn more about filters" icon="filter" horizontal href="/building/logic/core-components/filters" />
</Card>

<br />

<Card title="Response" icon="box-open-full" href="/building/logic/core-components/response">
  The response is what the logic will return when it's executed. It can be a value, a message, a JSON object; almost anything you want. Responses can be returned from a variable, or manually defined in the response itself.
</Card>

<br />

<Columns col={2}>
  <Card title="Variables" icon="square-root-variable" href="/building/logic/working-with-data/variables">
    Variables are used to store data that can be reused throughout your logic. They are declared in the variable block of the primitives that support them. Variables are optional, but the block must be declared even if empty.
  </Card>

  <Card title="Environment Variables" icon="gear" href="/building/logic/working-with-data/environment-variables">
    Environment variables are persistent variables that are available across your entire workspace. Typically, these are used to store things like external API keys that you need to use across multiple function stacks.
  </Card>
</Columns>


Built with [Mintlify](https://mintlify.com).