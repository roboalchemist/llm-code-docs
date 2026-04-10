# Source: https://dev.writer.com/no-code/newsletter-agent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a newsletter generation agent

Newsletters need to easy-to-understand and jargon-free, and can take hours to write—especially if you're sending them weekly. Creating an agent can help you get these newsletters out faster and written in a way that your customers can understand.

<img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/newsletter.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=95ecb65c1fdb3a9b92255090cbcd1de8" alt="newsletter agent showing inputs, prompts, and the generated newsletter content preview." data-og-width="3428" width="3428" data-og-height="1692" height="1692" data-path="images/no-code/newsletter.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/newsletter.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=9df6d604f85f75f80acadb4d6b218144 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/newsletter.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=6bd707c3b2d4e5b40993a3201408602d 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/newsletter.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=ce0ae1cc7c13ac738c6624b091e1be11 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/newsletter.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=a56c0acba8be5beb2523183613419596 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/newsletter.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=5d9421fd78493db137e8d38d083ba2a0 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/newsletter.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=b96ae67cf10b0c0166968768fe86f325 2500w" />

Below are the steps to create this newsletter agent. To follow along, first log in to [AI Studio](https://app.writer.com/aistudio).

<Steps>
  <Step title="Create a new agent with text generation capabilities">
    From the [AI Studio home page](https://app.writer.com/aistudio), click **Build an agent** in the top right corner. Then, select **Text generation** as the type of agent you want to create.
  </Step>

  <Step title="Define your inputs">
    This example is a newsletter that always includes three key components:

    * Communication about new features, products, or white papers
    * A customer spotlight
    * Information about the latest blog post

    Each of these components is an input. Define three inputs, each of the type **File upload**, with the names:

    * Feature info/whitepapers
    * Customer Spotlight
    * Blog to promote
  </Step>

  <Step title="Write your prompts">
    There are several ways to break up the prompts for generating a newsletter. In this example, create two prompts: one to generate the subject line and one to generate the body of the newsletter.

    The prompt for the subject line is:

    > Create a subject line for a weekly newsletter about the new features, customer spotlights, and featured blog posts.

    The prompt for the body of the newsletter is:

    > Create a newsletter for Writer customers. The newsletter should include:
    >
    > * communication about new features, products, or white papers. These items to highlight are in `@Feature info/whitepapers`
    > * a customer spotlight. The customer spotlight information is in `@Customer Spotlight`
    > * a blog article to promote, which is in `@Blog to promote`
    >
    > Avoid jargon and complex language. Although the newsletter may cover fairly complex topics, it should be accessible to everyone.
    > The newsletter should follow this format:
    >
    > * a greeting and introduction
    > * new features/products/whitepaper communications
    > * the customer spotlight
    > * blog article to promote
    >
    > Include suggestions for images that can break up each section.
  </Step>

  <Step title="Format your output">
    Decide how you want your output to look in the Output formatting section. You can use [Markdown](https://www.markdownguide.org/) to format your output.

    In this example, the output is a newsletter with a subject line and body:

    > @subject\_line
    >
    > @body
  </Step>

  <Step title="Test and refine your output">
    The first version of your newsletter may not be what you're looking for. That's okay! The more you tweak your prompts and provide examples, the better your output will be.

    It can also be helpful to provide examples in your prompts of newsletters and subject lines you think are the best. That way, Writer can learn from what you consider to be the best newsletters.
  </Step>

  <Step title="Deploy your agent">
    Once you're happy with how everything looks, [deploy your agent](/no-code/deploying-an-agent) so that everyone can use it. Developers can also [invoke this agent with the API](/home/applications) and [use it with tool calling](/home/applications-tool-calling) to integrate into other agentic workflows.
  </Step>
</Steps>
