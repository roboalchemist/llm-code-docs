# Source: https://docs.xano.com/using-ai-builders-with-xano.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using AI Builders With Xano

> Get the latest on using platforms like Bolt.new, v0, and Cursor with Xano

<CardGroup col={2}>
  <Card href="https://youtu.be/m4YoJXaqdEc?si=-T0O0RXVTL93HHls">
    <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/d334434e-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=0358bc76374ac71372a41977459cf4d3" width="1128" height="634" data-path="images/d334434e-image.jpeg" />

    Using Xano with Cursor
  </Card>

  <Card>
    <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/4822c986-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=cee25d0b9cd482cf698efd05403786d0" width="1128" height="634" data-path="images/4822c986-image.jpeg" />

    Using Swagger Docs with ChatGPT
  </Card>
</CardGroup>

## The Key: Auto-documented APIs

When you're building API endpoints in Xano, they're auto-documented in the OpenAPI specification using Swagger. This means that without any effort from you, you already have AI-ready documentation that can be used in combination with your favorite AI builder to spin up fully baked applications very quickly.

We have a full section on this functionality here: [Swagger (OpenAPI Documentation)](/the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation). For now though, you can get started quickly with the instructions below.

<Steps>
  <Step title="Get your API documentation">
    Inside your API group(s), you'll find a link to the documentation in the top-right, as shown below.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/5e7cadf8-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=0ad1802dad0d2b6d0ed18f6ff20fc0c3" width="2035" height="492" data-path="images/5e7cadf8-image.jpeg" />
    </Frame>
  </Step>

  <Step title="On the documentation page that opens, save the JSON version by right-clicking the link at the top and saving it.">
    You'll want to save separate files for each of the API groups that you want to use in the AI builder.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/0e2c5dee-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=01aef88bded4afdbb07f9614dd871b21" width="630" height="650" data-path="images/0e2c5dee-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Import the documentation into your AI of choice, and start building!">
    Here's a quick demo of us importing some API documentation into ChatGPT, and getting a fully functional app returned.

    <Frame caption="Please note that this video does not contain any audio, and is not intended to be a full tutorial; only a quick demonstration.">
      <iframe width="707" height="398" src="https://www.youtube.com/embed/4ULVUlsjN9U" title="Xano Swagger Docs to ChatGPT Example" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
    </Frame>
  </Step>
</Steps>

## Best Practices and Tips

* **Start with a clear objective**

  * Understand the scope of what you want the end result to look like. Try to keep in mind what a successful MVP (minimum viable product) or version 1 would require, and use that to guide the AI builder.

* **Use versioning**

  * Store your app's code on Github and use versioning to ensure that you can always roll back, and that it's easier to start new conversations if necessary with other AI platforms. [Here's a great tutorial from FreeCodeCamp.](https://www.freecodecamp.org/news/git-and-github-for-beginners/)


Built with [Mintlify](https://mintlify.com).