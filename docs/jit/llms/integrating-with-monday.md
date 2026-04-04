# Source: https://docs.jit.io/docs/integrating-with-monday.md

# Monday.com Integration

Integrating with monday.com

Integrating **monday.com** with Jit streamlines the process of assigning security-related items directly to Engineering and Security teams from the Jit platform. Learn more about this [here](https://docs.jit.io/docs/integrating-with-tms).

# Web app integration

## Quickstart

1. In Jit's webapp, go to the **Integrations page**:

[block:image]{"images":[{"image":["https://files.readme.io/6028ac3-monday.png",null,""],"align":"center"}]}[/block]

2. Find the "**Monday.com**" card and click "**Connect**".

3. You should now see a Monday integration window. Click on "Connect" at the top right corner.

   ![](https://files.readme.io/17cb277-image.png)

   * You will now need to supply your personal access token that will be used to create items.

   1. Log into your monday.com account.

   2. Click on your avatar/profile picture in the top right corner.

   3. Select **Developer**. This will open the Developer Center in another tab.

   4. Click **Developer > My Access Tokens > Show**.

   5. Copy your personal token. **Please note** that you can always regenerate a new token, but doing so will cause any previous tokens to expire.

   6. Paste it in the "**Monday API Token**" textbox.

   Learn more in [Monday documentation](https://developer.monday.com/api-reference/docs/authentication#developer-tab).

[block:image]{"images":[{"image":["https://files.readme.io/9660a44-image.png",null,""],"align":"center"}]}[/block]

4. If the token is valid, You can now choose the default board to create issues on.

![](https://files.readme.io/9b9a6da-image.png)

## Sample item

![](https://files.readme.io/85a0405-image.png)

<br />

## Notes

* An extra column named "**External ID-GUID** will be added to the item with the value "**Opened-by-jit**".
* Subitems, as detailed in this [support article](https://support.monday.com/hc/en-us/articles/360011905480-All-about-subitems), are not supported. If selected on the configuration screen, the create items action will fail with an `InvalidBoardIdException`. The error message will read: `Can't create an item on subitems board. Please use create_subitem mutation.` To avoid this issue, please select a primary board instead.