# Storybook Documentation
# Source: https://storybook.js.org/docs/sharing/embed
# Page: /docs/sharing/embed

# Embed stories

ReactVueAngularWeb ComponentsMore

Embed stories to showcase your work to teammates and the developer community at large. In order to use embeds, your Storybook must be published and publicly accessible.

Storybook supports `<iframe>` embeds out of the box. If you use Chromatic to [publish Storybook](./publish-storybook#publish-storybook-with-chromatic), you can also embed stories in Notion, Medium, and countless other platforms that support the oEmbed standard.

## 

Embed a story with the toolbar

Embed a story with the toolbar, and paste the published story URL. For example:
    
    
    // oEmbed
    https://5ccbc373887ca40020446347-wtuhidckxo.chromatic.com/?path=/story/shadowboxcta--default
     
    // iframe embed
    <iframe
      src="https://5ccbc373887ca40020446347-wtuhidckxo.chromatic.com/?path=/story/shadowboxcta--default&full=1&shortcuts=false&singleStory=true"
      width="800"
      height="260"
    ></iframe>

  


## 

Embed a story without the toolbar

To embed a plain story without Storybook's toolbar, click the "open canvas in new tab" icon in the top-right corner of Storybook to get the canvas URL. For example:
    
    
    // oEmbed
    https://5ccbc373887ca40020446347-wtuhidckxo.chromatic.com/iframe.html?id=/story/shadowboxcta--default&viewMode=story
     
    // iframe embed
     <iframe
      src="https://5ccbc373887ca40020446347-wtuhidckxo.chromatic.com/iframe.html?id=shadowboxcta--default&viewMode=story&shortcuts=false&singleStory=true"
      width="800"
      height="200"
    ></iframe>

  


## 

Embed documentation

Embed a documentation page by replacing `viewMode=story` with the uniquely auto-generated documentation entry for the story.
    
    
    // oEmbed
    https://5ccbc373887ca40020446347-wtuhidckxo.chromatic.com/iframe.html?id=shadowboxcta--docs&viewMode=docs&shortcuts=false&singleStory=true
     
    // iframe embed
     <iframe
      src="https://5ccbc373887ca40020446347-wtuhidckxo.chromatic.com/iframe.html?id=shadowboxcta--docs&viewMode=docs&shortcuts=false&singleStory=true"
      width="800"
      height="400"
    ></iframe>

  


## 

Embed stories on other platforms

Every platform has different levels of embed support. Check the documentation of your service to see how they recommend embedding external content.

How to embed in Medium

Paste the Storybook URL into your Medium article, then press Enter. The embed will automatically resize to fit the story's height.

While editing an article, Medium renders all embeds non-interactive. Once your article is published, it will become interactive. [Preview a demo on Medium](https://medium.com/@ghengeveld/embedding-storybook-on-medium-ce8a280c03ad).

How to embed in Notion

In your Notion document, type /embed, press Enter, and paste the story URL as the embed link. You can resize the embed as necessary.

![Embed Notion](/docs-assets/10.1/sharing/embed-notion.png)

How to embed in Ghost

Type `/html` in your Ghost post, press Enter and paste the iframe URL. You can resize the embed via the width and height properties as required.

![Embed Ghost](/docs-assets/10.1/sharing/embed-ghost.png)

Was this page useful?

👍👎

[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/sharing/embed.mdx)