# Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/embed-your-app

# Embed your app

Embedding Streamlit Community Cloud apps enriches your content by integrating interactive, data-driven applications directly within your pages. Whether you're writing a blog post, a technical document, or sharing resources on platforms like Medium, Notion, or even StackOverflow, embedding Streamlit apps adds a dynamic component to your content. This allows your audience to interact with your ideas, rather than merely reading about them or looking at screenshots.

Streamlit Community Cloud supports both iframe and oEmbed methods for embedding **public** apps. This flexibility enables you to share your apps across a wide array of platforms, broadening your app's visibility and impact. In this guide, we'll cover how to use both methods effectively to share your Streamlit apps with the world.

## Embedding with iframes

Streamlit Community Cloud supports embedding **public** apps using the subdomain scheme. To embed a public app, add the query parameter `/?embed=true` to the end of the `*.streamlit.app` URL.

For example, say you want to embed the [30DaysOfStreamlit app](https://30days.streamlit.app/). The URL to include in your iframe is: `https://30days.streamlit.app/?embed=true`:

```html
<iframe src="https://30days.streamlit.app?embed=true" style="height: 450px; width: 100%;"></iframe>
```

Here's an example of [@chrieke](https://github.com/chrieke)'s [Prettymapp app](https://chrieke-prettymapp-streamlit-prettymappapp-1k0qxh.streamlit.app/) embedded in a Medium article:

![Example: Embed an app in a Medium article with oEmbed](https://docs.streamlit.io/images/streamlit-community-cloud/oembed.gif)

Ensure the platform hosting the embedded Streamlit app supports oEmbed.

## Embed options

When [Embedding with iframes](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/embed-your-app#embedding-with-iframes), Streamlit allows you to specify one or more instances of the `?embed_options` query parameter for granular control over the embedding behavior.

Both `?embed` and `?embed_options` are invisible to `st.query_params` and its precursors, `st.experimental_get_query_params`, and `st.experimental_set_query_params`. You can't get or set their values.

The supported values for `?embed_options` are listed below:

- Show the toolbar at the top right of the app which includes the app menu (more_vert).
- Show padding at the top and bottom of the app.
- Show the footer reading "Made with Streamlit." (This doesn't apply to Streamlit versions 1.29.0 and later since the footer was removed from the library.)
- Show the colored line at the top of the app.
- Hide the "skeleton" that appears while an app is loading.
- Disable scrolling for the main body of the app. (The sidebar will still be scrollable.)
- Open the app with light theme.
- Open the app with dark theme.

You can also combine the params:

```html
/?embed=true&embed_options=show_toolbar&embed_options=show_padding&embed_options=show_footer&embed_options=show_colored_line&embed_options=disable_scrolling
```

## Build an embed link

You can conveniently build an embed link for your app — right from your app!

1. From your app at `your-custom-subdomain.streamlit.app`, click "Share" in the upper-right corner.
2. Click "Embed" to access a list of selectable embed options.
3. Select your embed options and click "Get embed link" to copy the embed link to your clipboard.

![Access embed options from the share button](https://docs.streamlit.io/images/streamlit-community-cloud/share-menu-embed.png)

![Build a customized embed link for your app from the share button](https://docs.streamlit.io/images/streamlit-community-cloud/share-menu-embed-url.png)