# Source: https://docs.firehydrant.com/docs/runbook-step-post-a-gif-from-giphy.md

# Post a GIF From Giphy

The **Post a GIF from Giphy** step looks up a random GIF based on the keywords specified, along with a message with that GIF. Note that by default, we search GIFs with a `rating` of `g`. To see GIPHY's content rating levels, visit [their documentation](https://developers.giphy.com/docs/optional-settings/#rating).

> 📘 Note:
>
> Although we specify the `g` rating, we cannot guarantee the appropriateness of the images sent to us from Giphy as image moderation is done externally to FireHydrant.

## Configuration

<Image alt="Post a GIF from Giphy step" align="center" width="650px" src="https://files.readme.io/a935abf-image.png">
  Post a GIF from Giphy step
</Image>

This step has the following configurable fields:

* **Gif Keywords** - Keywords or search terms used to fetch a random GIF from Giphy. You can specify different keywords and search terms on new lines, and FireHydrant will randomly pick a search term for each execution
* **Random Phrase** - Phrases or quotes that may be posted with the GIF result. You can specify different phrases on new lines, and FireHydrant will randomly pick a phrase for each execution.

> 📘 Note:
>
> You should set the execution condition to **Incident Slack channel exists**, otherwise this runbook step might fail if it runs when the Slack channel hasn't been created yet.

Here is an example output in Slack from the example configuration in the image above:

<Image alt="Teamwork GIF" align="center" width="650px" src="https://files.readme.io/58db5b6-image.png">
  Teamwork GIF
</Image>