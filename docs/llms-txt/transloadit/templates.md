# Source: https://transloadit.com/docs/topics/templates.md

# Templates

You can send us your Assembly Instructionsdirectly with each request, or you can save them in a Template and refer to its `template_id` in your requests.

## Builtin Templates

Transloadit also provides Templates that are maintained and versioned by us. These Builtin Templates are useful as stable, ready-to-use starting points for common transformations.

See [Builtin Templates](/docs/topics/builtin-templates.md) for available builtins and how to list them via the API.

Sending Instructions directly allows for quick prototyping, but saving them in a Template comes with some advantages:

1. You can refrain from transmitting sensitive data and implementation details with each request to encode. This is especially interesting when you integrate with browsers.
2. Paired with `"allow_steps_override": false`,Instructions **cannot be tampered with**.
3. Paired with Assembly Notifications, you can enable Assembly Replays.
4. If you integrated Transloadit into an app, you can **change the encoding settings without deploying** or waiting for an App Store to release a new version.

## How to create a Template

1. [Create a Template in your account](/c/templates/new/).
2. Give your Template a name for future (human) reference.
3. Provide the Assembly Instructions JSON for your Template. You can select examples from a list, let our Wizard generateInstructions, duplicate an existing Template, or start from scratch.
4. Hit save.

Once the Template is saved, a page is displayed showing the Template you created. At the top of the page, the Template's ID is shown, e.g., `4b62ee4dbb38455d96fe13d972ec3211`. You can then copy/paste this ID into your integration code's `template_id`, or look further down theTemplate Editor where we already show examples including this ID.

###### Note

The Template Editor also has a testing area where you can test your Templates along with an upload form right in the browser without updating your integration (you don't even have to hit save).

## Overruling Templates at runtime

You would think they are mutually exclusive, but it is possible to supply both `template_id` and`steps` inside params, as this lets you change Template behavior at runtime. In fact, any other property inside `params`, with the exception of `allow_steps_override`, will be recursively merged over the Template that is loaded via `template_id`.

For example, let's take a look at the following Template that handles an upload, encodes a video to play well on iPads, and saves the result on S3:

![](/_next/static/media/copy.8f7d2926.svg?dpl=dpl_GAEaNRfbaNgVy6q3c3ke5o1s9Xtk)

```json
{
  "steps": {
    ":original": {
      "robot": "/upload/handle"
    },
    "encoded": {
      "use": ":original",
      "robot": "/video/encode",
      "preset": "ipad-high"
    },
    "exported": {
      "use": "encoded",
      "robot": "/s3/store",
      "credentials": "YOUR_S3_CREDENTIALS",
      "bucket": "main-bucket"
    }
  }
}

```

When you create an Assembly, we can tweak the Template's behavior at runtime, for instance, by adding a `steps` property:

![](/_next/static/media/copy.8f7d2926.svg?dpl=dpl_GAEaNRfbaNgVy6q3c3ke5o1s9Xtk)

```json
{
  "template_id": "4b62ee4dbb38455d96fe13d972ec3211",
  "steps": {
    "exported": {
      "bucket": "another-bucket"
    }
  }
}

```

This is then merged by Transloadit to create the followingAssembly Instructions:

![](/_next/static/media/copy.8f7d2926.svg?dpl=dpl_GAEaNRfbaNgVy6q3c3ke5o1s9Xtk)

```json
{
  "steps": {
    "encoded": {
      "use": ":original",
      "robot": "/video/encode",
      "preset": "ipad-high"
    },
    "exported": {
      "use": "encoded",
      "robot": "/s3/store",
      "credentials": "YOUR_S3_CREDENTIALS",
      "bucket": "another-bucket"
    }
  }
}

```

As you can see, the `bucket` value changed from `"main-bucket"` to `"another-bucket"`. This can be convenient and powerful in trusted environments.

In other environments, you may want to disallow overriding ofSteps so that a browser cannot modify the behavior. To do so, you would set `allow_steps_override` to `false` inside the saved Template, like so:

![](/_next/static/media/copy.8f7d2926.svg?dpl=dpl_GAEaNRfbaNgVy6q3c3ke5o1s9Xtk)

```jsonc
{
  "allow_steps_override": false,
  "steps": {
    // …
  },
}

```

Now, only `main-bucket` will ever be used, whether additional `steps` were supplied, or not.

## Template options

Besides `steps` and `allow_steps_override`, there are more options to control anAssembly's behavior.

Since most of them can also be set when not using Templates, they are documented in the[API docs for Creating a New Assembly](/docs/api/assemblies-post.md). However, if you integrate Transloadit into untrusted environments such as browsers, an abuser could easily change them. So, to allow dynamically changing a Template's parameters in untrusted environments, consider using[Signature Authentication](/docs/api/authentication.md).
