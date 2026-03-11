# Source: https://redocly.com/blog/updates-2022-07.md

If we had to describe our summer activities in a word, "vacation" would nail it.
We've been missing from the blog.
And it's my fault... you see, I went on a one-month vacation.
When I returned, our team had shipped so much, it took me a long while to familiarize with the features to decide what to write about.

Redocly developers are continuing work on several new features behind the scenes.
Some of those features are mind-blowing... unless you're one of the lucky few you'll have to wait until early next year for those.

For now, here's a quick round-up of Redocly product enhancements from May, June, and July 2022.

â¨ Customer spotlight â¨
Checkr said: âThe insanely quick response time of the Redocly team to any and all requests for help clinched the deal.â

[Read their story](https://redocly.com/customers/checkr/).

## Workflows

On the Workflows side, a slew of bug fixes throughout the three months, and a few new features.

Some important things to point out:

- All project names were converted to lowercase.


New features we're really excited about:

- Added file editing to the API registry.
- The "Reference" tab was removed and "API docs" button was added to the registry screen.
All the former "Reference" settings were moved into the registry settings.
- Added an [API style guide](https://redocly.com/docs-legacy/settings/api-styleguide/) feature to enforce organization-wide API styles for better consistency across your organization.


![Workflows features](/assets/workflows.3eb9e6233ed54c01e56fbc7ef66291faa9ea4a94475d1521ff5f0bf3b04d92b3.978384e4.png)

## Reference docs is now called API docs

We've renamed **Reference docs** to **API docs** because it is more clear to new users.

**More try it controls**

Set the maximum number of response headers displayed with the `maxResponseHeadersToShowInTryIt` option.
Also, the feature toggle for try it was renamed from `showConsole` to `hideTryItPanel` (`false` by default).
We added support for a new extension `x-hideTryItPanel` so that you can control if the try it panel appears per API operation.
The code samples use values from the try it console.
This makes them the most practical code samples around.
We also added a toggle to clear values from the try it console.
We added support for array parameters (query, header, cookie) in the *Try it* console.

**Render schemas**

You can render schemas in a few easier ways.
We wrote a blog post about it: [Display Schemas](/blog/display-schemas).

Find more improvements and resolved issues in the [API docs changelog](/docs-legacy/api-reference-docs/changelog).

![API docs features](/assets/refdocs.bbb0c598669f5fcc4ed106cf15eb57362166b4f9632eccc273e27c6fbb97101f.978384e4.png)

## Developer portal

**Mostly bug fixes**

The developer portal you use and love is mostly in maintenance mode (bug fixes mostly) as we put all of our energy into a new developer portal (a ground up rewrite which has incredible performance, theming, and functional enhancements).
Don't worry, your content will be compatible with the new one.
We've been working on this project for about a year, and plan to start using it internally by September.
I mentioned I had to spent my time catching up with all of the releases when I returned from vacation.
Most of those features are related to this new developer portal.

**Developer portal changelog**
Read about all the latest fixes and enhancements in the [Developer portal changelog](/docs-legacy/developer-portal/changelog).

![Developer portal features](/assets/devportal.c653352a809d5345b0d11dc586e86f6da66f8e7357e54d2bc57a029b3709da8a.978384e4.png)

## OpenAPI CLI is Redocly CLI

**OpenAPI CLI** was renamed to **Redocly CLI**.
Why? Vanity? Maybe. We like the sound of it. And who knew Redocly is less syllables than OpenAPI?

**More rules**
We added a lot of built-in rules including a really powerful [assertions](/docs/cli/rules/configurable-rules) rule (renamed to custom rules in 1.0.0-beta.112).

Most importantly, we overhauled the [rules docs](/docs/cli/rules), going into depth with the API design principles and incorrect and correct examples related to each rule.

One of the reasons to give each rule a dedicated page is so that you could link to it from your own API styleguide docs.

**ð ð ð We're number 1 ð ð ð**

Help us celebrate!
As of July, we're the most downloaded OpenAPI-related styleguide tool (linter and bundler) in npm.

**Redocly CLI changelog**
The full list of fixes and enhancements is available in the [OpenAPI CLI changelog](/docs/cli/changelog).

## Redoc

We're working hard towards a general availability release of Redoc 2.0.

That was to give you context for the massive changes if you go check out that changelog on our GitHub repo.

Fingers crossed that release happens before our next update blog post.

**Redoc changelog**

You can find more fixes and enhancements in the [Redoc changelog](https://github.com/Redocly/redoc/blob/master/CHANGELOG.md).

## Write the docs at Redocly!

Want to do your part to accelerate API ubiquity?

We're looking for a [full-time Technical Writer](https://redocly.com/careers/#technical-writer) to work on product documentation and training materials (including, but not limited to videos) for our premium and open source products.

If you'd prefer to write different kinds of content (or even code), create product demos, and interact with developers, we have a role for that, too. Take a look at our [Developer Advocate](https://redocly.com/careers/#developer-advocate) position, and get in touch if you're interested.