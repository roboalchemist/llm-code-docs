# Source: https://www.cosmicjs.com/docs/dashboard/buckets.md

# Buckets

Learn about Buckets; where you manage your Cosmic content, media, extensions, and add-ons.

## Creating a Bucket

You can create a new Bucket in a few different ways:

1. When creating a new Project.
2. When adding a new Bucket on an existing Project.
3. When cloning a Bucket in an existing Project.

### Buckets home

After you have created your Bucket, you will have a Bucket home view which gives you access to your recently modified content as well as other helpful links and resources.

## Object types

Object types are how you organize your content into specific content models. For example, if you are building content for your website, some Object types that you might create include: pages, blog posts, authors, etc.

Object types can be multiple or singleton. The `slug` field you include will be used to request the Objects in this type from the API.

Optional features on the Object type include:

1. Emoji: This is displayed on the dashboard for easy orginization and visual cues.
2. Localization: Set different locales on your Objects to provide content in different languages.
3. Preview link: Enable content editors to access a preview link from the Object edit view.

Organize your Object types into content folders to make them easily available
in the sidebar of the Bucket > Content view.

## Localization

You can add localization to your Object types to create versions of content in different languages. This is found in Bucket > Object type settings.

Set a priority locale to make this locale required and organize your Objects table with this one being displayed first.

## Metafields

Use Metafields to create your Object type content model. Available Metafields include:

1. Input fields: text, number, text area, rich text, markdown, JSON
2. Select fields: dropdown, date, radio, checkbox, switch, color picker, and emoji
3. Media fields: image, video, audio, document, as well as other types
4. Group fields: parent (contains other Metafields), repeater (contains and can repeat groups of Metafields)
5. Object relationships: single Object, multiple Objects

Use validation and help text on Metafields to provide content editors with
proper guard rails and content creation assistance.

## Objects

Objects are the building blocks of your content in Cosmic.

In the add / edit Object view, content editors can perform a number of tasks including:

1. Create long form content.
2. Update Metafield values.
3. Set content to draft / published status.
4. Schedule content for publish / unpublish.
5. View revisions / restore to a prior version.

## Media

Go to Bucket > Media to manage the media in your Bucket. You can upload many different media types including images, video, audio, as well as documents such as PDFs, JSON files, etc.

Organize your media into folders to keep them organized and easy to filter
when adding media to Objects.

Media added here will be available for use in your Bucket Objects that have media Metafields.

## Extensions

Extensions enable you to extend the functionality of your Cosmic dashboard to build custom views, connect with third party services, and create time saving workflows. Specifically, they provide an iframe view into an external website or web application while supplying your Project API credentials to enable a streamlined connection. They can be added as a full page view, or included in select locations in your dashboard.

Pictured below is the [Cosmic Media](https://github.com/cosmicjs/cosmic-media-extension) extension which enables you to search millions of high-quality, royalty-free stock photos, videos, images, and vectors and add them directly to your Cosmic project.

### Adding an Extension

To add Extensions to your Project, go to Project > Extensions. Prebuilt Extensions are available to install and get up and running quickly. See the available Extensions on the [Cosmic integrations page](https://www.cosmicjs.com/integrations). Install them for free and browse the open source code to learn how to build your own Extensions.

### Build your own Extensions

An Extension provides an iframe view into a URL with dynamic query parameters. This enables you to connect to third-party APIs to interact with your Bucket directly from your Cosmic dashboard. The only requirements is that the URL is served securly with `https://` and has `X-Frame Options` enabled.

Go to Project > Extensions > Add Extension to add an Extension using any valid URL.

A good starting point is the [Cosmic Next Template](https://github.com/cosmicjs/cosmic-next-template), which comes prebuilt with the [Cosmic JavaScript SDK](https://www.npmjs.com/package/@cosmicjs/sdk), query parameter fetching, theming, and more. You can then deploy this codebase to your preferred hosting provider and use the URL to add as an Extension.

### Query parameters

After adding your Extension, query parameters are automatically attached to the URL for easy connection to your Bucket. The format looks like this:
```
https://my-extension.vercel.app?bucket_slug=your-bucket-slug&read_key=your-bucket-read-key&write_key=your-bucket-write-key&theme=dark

```
Available query parameters include:

| Name                     | Description                                                                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bucket_slug`            | Your Bucket slug. Use this to connect to your Cosmic Bucket for read / write / edits.                                                                               |
| `read_key`               | Your Bucket read key. Needed to read from your Bucket if this value is set in Bucket Settings > Basic.                                                              |
| `write_key`              | Your Bucket write key. Needed for writes to your Bucket if this value is set in Bucket Settings > Basic.                                                            |
| [`custom_key` / `value`] | You can add unlimited custom query parameters such as third party API keys to connect to different services. Find this in your Cosmic Extension settings page.      |
| `theme`                  | `light` or `dark`. Use this query parameter to get the current dashboard theme.                                                                                     |
| `page`                   | If location set to the edit Object page value is `edit-object`.                                                                                                     |
| `location`               | If location set to media modal value is `media-modal`.                                                                                                              |
| `object_id`              | If location set to edit Object, value is the Object id. Can be used to query more information about the Object. See [API reference for Objects](/docs/api/objects). |

### Extension locations

You can enable Extensions to appear in a few different locations:

1. **Full page** - appears in Project / Bucket / Extensions. Frame height is not editable.
2. **Add Object page** - appears in add Object page. Available locations include below the Object title, below the Object slug, below Metafields, and in the Object actions sidebar. Frame height is editable.
3. **Edit Object page** - appears in edit Object page. Available locations include below the Object title, below the Object slug, below Metafields, and in the Object actions sidebar. Frame height is editable.
4. **Media modal** - appears in an additional tab in the media modal. Frame height is not editable.

## Webhooks

Webhooks enable you to communicate with third-party services. The webhooks feature can be added to any project or workspace to connect to any third-party service via HTTP `POST` requests when certain events occur in your Buckets.

### Creating webhooks

Create a new webhook by going to Bucket > Settings > Webhooks and click "Add Webhook".

### Testing webhooks

You can use a service like [Beeceptor](https://beeceptor.com/) to test your webhooks and view response data.

See the [API reference for webhooks](/docs/api/webhooks) for more API information.

## Backups

The backups feature can be added to any project or workspace to enable automatic backups for any Bucket. Automatic backups occur daily at 12AM UTC.

Go to Bucket > Settings > Backups to view Bucket backups. You can also create a snapshot at any time. Download and restore to a previous backup snapshot.

## Import / Export

All Buckets include the ability to import or export all of the content in the Bucket at any time. This export is a JSON file which includes data for Object types, Objects, Media, folders, but does not include team members, Object revisions, or backups. Go to Bucket > Settings > Import / Export to perform this action.