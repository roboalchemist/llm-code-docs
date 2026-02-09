# Source: https://docs.warp.dev/university/how-warp-uses-warp/using-images-as-context-with-warp.md

# Using Images As Context With Warp

{% embed url="<https://youtu.be/_Pc7bL0zAoM?si=v7-0svwdNgv9t-Se>" %}

### 1. Why Images Matter

Humans process visuals much faster than text — and the same applies to AI.\
\
When you’re trying to explain a UI issue (“this button is off by a few pixels”), describing it with words can be clunky.\
\
That’s why Warp supports images as context — letting you attach screenshots directly to your prompts.

> 🧠 “An image is worth a thousand words” — especially when debugging UI or building frontend components.

***

### 2. What Image Context Does

Image Context allows you to:

* Attach one or more screenshots to an agent query
* Give visual references for bugs, designs, or features
* Let the agent visually interpret what you mean

This is especially useful for frontend tasks like:

* Rebuilding a design from Figma
* Identifying layout misalignments
* Debugging visual bugs

***

### 3. Building an MCP Marketplace from Figma

Taking a Figma mock of an MCP Server Marketplace and using it as input for Warp.

#### Step 1. Capture the Mock

Take a screenshot of your design (e.g., the MCP Marketplace layout).

#### Step 2. Attach the Image

In Warp:

1. Click the 📎 image icon in the input bar
2. Select your screenshot
3. Confirm it’s attached to the query

***

### 4. Running the Task

Once attached, Warp’s agent:

1. Detects the attached image
2. Searches your repo (e.g., `collection.rs`)
3. Generates diffs that recreate the UI from the mock
4. Creates corresponding components and layout logic

You can view and edit these diffs in the Code Diff Viewer, similar to GitHub’s diff interface.

> 💡 Warp recommends smaller, focused diffs — agents perform better when working iteratively.

***

### 5. Reviewing the Results

The agent built:

* A UI component for the MCP Marketplace
* Static data for three MCP servers (`Linear`, `GitHub`, `Stripe`)
* Proper rendering logic and styling

Verify the UI in Warp:

> “It matched the mock almost perfectly — something that would’ve taken me two days was done in 20 minutes.”

***

### 6. Optimizing for Performance

Because images can consume tokens quickly, Warp automatically:

* Resizes images client-side
* Compresses them intelligently before sending
* Minimizes token usage without losing clarity
