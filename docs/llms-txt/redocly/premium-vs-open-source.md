# Source: https://redocly.com/blog/premium-vs-open-source.md

It's a good week when I don't have to answer the question about what makes our premium products different from our open source products.
If you can sense a bit of annoyance, then you are perceptive and correct.
So I thought, why not make a blog post so that I can answer with a link (and have only good weeks from here on out).

## The backgroundâ¦

While we have had some variation of a Redoc vs Redocly marketing page in the past.
It's never been specific enough to answer questions from detail-oriented folks (yes, Redockers are generally detail-oriented).

## Our love for open source

We love open source.
And the community supports us.

Our open source products are great.

They are most popular in their corresponding categories.

We have some like [OpenAPI Sampler](https://github.com/redocly/openapi-sampler) that is used by tool makers to generate OpenAPI request and response schema examples.
This blog post is not about those types of products.

This post is about our projects **Redoc** and **Redocly CLI**.

But the sad truth of business (at least for us) is that open source doesn't directly pay any bills.

We'll continue to invest in open source, as it does drive awareness of our premium products.

As such, we invest about 95% of our R&D into premium products.
These are products that we charge money for.

While there are some open source business models that charge for the hosted open source product... that's not our business model.
Our business model is our premium products expand upon our open source products; our premium products do a lot more for a reasonable price.

## Product level differences

Let's contrast our main open source and premium products.

| Product name | Purpose | Premium | Open Source |
|  --- | --- | --- | --- |
| Redocly CLI | Lint API descriptions. Additional utilities including bundle, preview and build static docs. | â | â |
| Redoc | Render OpenAPI descriptions. | â | â |
| Revel | External developer showcase including rich landing pages and contextual docs, guides, tutorials.
Render Markdown, Markdoc tags, React pages.
Additional features include localization, multi-product, versioning, and comprehensive customization. | â | â |
| Reef | Internal developer portal features a catalog, scorecard, and dynamic client registration. | â | â |
| Reunite | Hosting Redocly projects. Editor and visual reviews for collaboration. Feedback reports. Remote content automations. | â | â |


The reason for the table is because the rest of the blog post is mainly going to be about the differences between Redoc open source and Redoc premium.
If we also discuss Reef, Revel, and Reunite, this comparison becomes overwhelming because none of that functionality is available in Redoc or Redocly CLI.

## Feature level differences

Before moving on to Redoc, it's important to note that the premium Redoc includes the functions of Redocly CLI such as lint and bundle already.
The Reunite editor provides visual feedback and typeahead hints based on your lint rules.
Reef uses the same rules, but you can also set multiple sets of rules to run against your whole catalog of APIs and get a report in the form of a scorecard.

On to the Redoc-specific high-level features.

| Feature | Purpose | Premium | Open Source |
|  --- | --- | --- | --- |
| Render OpenAPI | Visually represent an OpenAPI description. | â | â |
| Render GraphQL | Visually represent a GraphQL SDL. | â | â |
| Render AsyncAPI | Visually represent an AsyncAPI description. | â | â |
| Render SOAP | Visually represent a WSDL defining a SOAP API. | â | â |


But let's dig deeper on the OpenAPI-specific features, because, even for OpenAPI, Redoc is quite different between premium and open source.

| Feature | Purpose | Premium | Open Source |
|  --- | --- | --- | --- |
| Mock server | Runs mock server based on OpenAPI example definitions and configuration. | â | â |
| Versioning | Support version switcher between versions of an OpenAPI description. | â | â |
| Try it console (Replay) | Try API requests from the browser. | â | â |
| Generated code samples | Automatically generated code samples in different languages. | â | â |
| Performance | Work with large OpenAPI definitions. | â | ð¡ |
| `x-rbac` support | Protect and hide operations and properties based on role-based access controls. | â | â |
| Multiple examples support | Support multiple examples including generated examples and examples used in the Replay try it panel. Synchronize request and response examples. | â | â |
| SEO optimized | More control over SEO-related tags such as meta description. | â | â |
| Advanced search | Filter by method, path, and more. | â | â |
| Deep linking | Link directly to any property useful for support and collaboration scenarios. | â | â |
| Enhanced nested schemas UX | Make it easier to traverse nested schemas and to identify your given location with additional visual cues. | â | â |
| Styles | More customizable with CSS variables. | â | â |
| `x-badges` support | Add custom badges next to any operation. | â | â |
| Broken link checker | Checks for broken links within docs. | â | â |
| PR previews | Build previews automatically based on pull requests from Reunite. | â | ð§ |
| Feedback | Gather feedback on API docs as well as code snippets. | â | â |
| Access controls | Protect content. Integrate with identity providers for SSO. | â | ð§ |


Legend

- ð§ - You need to make the automation yourself.
- ð¡ - Partial support.


## Premium advantage

After reviewing the above, you'd probably expect Redoc to cost a significant amount of money.
Given our scale, we're able to offer Redoc as low as $9/month (on an annual basis) per contributor seat.
For some perspective, we used to charge $360/month for that sold as a 10-seat pack.
This product is way better, and an incredible value.

For any business or even non-commercial purpose, it's cost effective and provides a great exchange of value for money.
We know you come mostly for Redoc, and we hope you stay for Revel and Reef, and more we have coming soon.