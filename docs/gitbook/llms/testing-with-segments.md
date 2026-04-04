# Source: https://gitbook.com/docs/documentation/ja-gitbook-documentation/publishing-documentation/adaptive-content/testing-with-segments.md

# Source: https://gitbook.com/docs/documentation/zh/publishing-documentation/adaptive-content/testing-with-segments.md

# Source: https://gitbook.com/docs/documentation/fr/publishing-documentation/adaptive-content/testing-with-segments.md

# Source: https://gitbook.com/docs/publishing-documentation/adaptive-content/testing-with-segments.md

# Testing with segments

Segments allow you to test the conditions you set by defining claims on a mock user.

For example, you might want to only show a page or section to beta users. By creating a segment and defining the properties associated with this group of mock users, you can mimic a segment that is specific to the users you’re targeting.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FYrErMp571tYPUN2RzJJ0%2F26_01_06_segment_editor%402x.png?alt=media&#x26;token=d73e0cd0-9158-41b1-bd4e-01d7def0a7aa" alt="A GitBook screenshot showing the segment editor"><figcaption><p>The segment editor in GitBook.</p></figcaption></figure>

### Create a segment

To create a new segment, head to the condition editor, and click the settings icon <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F6uYUpJto7WTkJf9BUPHv%2Fsettings%20-%20dark.svg?alt=media&#x26;token=bf52415f-e999-43a2-9a1a-c85176a014cd" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FwkBqgOPry9HAcW4cxJk0%2Fsettings.svg?alt=media&#x26;token=67bdbb00-ebf3-4a2d-9df8-0c822406f71c" alt="The Settings icon in GitBook"></picture> next to an existing segment in the segment dropdown.

Here you’ll be able to define the data that will appear on a mock user. Because this is the data that’s being represented, the `visitor.claims` key is omitted.

#### Example

To create a segment for beta users following the examples in our docs, you would create a new segment, and add the following data.

```json
{
  "isBetaUser": true
}
```

When heading back to the condition editor, selecting the beta segment we created should show that the page we’re viewing **would** be accessible to our test user.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FpTHHKitlueFU97EuEi14%2F26_01_06_testing_segments%402x.png?alt=media&#x26;token=10f3d1d1-f604-49cd-8be6-072202bd4f37" alt="A GitBook screenshot showing how to test a segment"><figcaption><p>Testing a segment in GitBook.</p></figcaption></figure>

### Detected segments

Detected segments allow you to get a sense of the type of claims you are receiving from visitors to your site.

These segments are not editable, but allow you to copy/paste claims from the segment editor to create your own user segments.

### Testing segments in the preview

In addition to testing segments in the segment editor, you’ll be able to use your segments in real time in the preview when viewing changes for your site.

Use the dropdown in the upper left corner when in preview mode for your site to choose a segment to see how your site will look for your chosen segment.
