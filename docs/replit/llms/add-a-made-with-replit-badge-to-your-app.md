# Source: https://docs.replit.com/additional-resources/add-a-made-with-replit-badge-to-your-app.md

# Add a Replit Badge to your app

> Add, customize, and embed a Replit Badge in your Replit App to showcase your project and link back to your cover page.

The Replit Badge allows you to showcase that you built your app on Replit. When added to your Replit App, it links back to your App's cover page so visitors can learn more about your creations.

## Features

The Replit Badge enhances your app with official Replit branding while providing easy navigation back to your project.

* **Simple integration**: Add the badge to any app with a single line of code
* **Customizable appearance**: Choose from multiple themes and positions
* **Flexible implementation**: Use the script tag or custom HTML/CSS options
* **Markdown support**: Embed badges in your GitHub repository and other Markdown files

## Usage

### Adding the badge

You can add a Badge to any Replit App with an index page. Websites created with the official HTML template have this Badge added by default.

1. **Locate your index.html file**\
   Go to your Replit App's file browser and find `index.html`
   <Frame>
     <img src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/img-indexfile.png?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=ffcfe3ffc4bb3a53e625428c119c6a97" alt="File browser showing index.html file" width="400" height="400" data-og-width="696" data-og-height="464" data-path="images/misc/img-indexfile.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/img-indexfile.png?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=1a96ed97fd9bbbb2da334927b7b7611e 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/img-indexfile.png?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=6d325a314163b89d14d6212be7209f17 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/img-indexfile.png?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=71104ff9a95850f9eac05cc0c6ab9ab8 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/img-indexfile.png?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=0d528fb3e866f94e5eb6277acaee9124 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/img-indexfile.png?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=073d4fd1fbcfe6d2a13a8c26d8809532 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/img-indexfile.png?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=ecb27567a61e25ba43611bb44ee25165 2500w" />
   </Frame>

2. **Add the badge script**\
   Add the following code before the closing `</body>` tag:
   ```html  theme={null}
   <script
     src="https://replit.com/public/js/replit-badge-v2.js"
     theme="dark"
     position="bottom-right"
   ></script>
   ```
   <Frame>
     <img src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/img-htmlcode.png?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3aad5c3f9030a458750ddd5d3998ebc5" alt="HTML code example showing badge script" data-og-width="1240" width="1240" data-og-height="1112" height="1112" data-path="images/misc/img-htmlcode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/img-htmlcode.png?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=9177718a7712794ad61afc490d777fcc 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/img-htmlcode.png?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=6a139df59e51dde65cf8b45c9f5daf7e 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/img-htmlcode.png?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=c3e50813596af8bfffc8edcbbbd6a1eb 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/img-htmlcode.png?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=2b0b632e339e3464f8328ece4ea03b95 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/img-htmlcode.png?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=b3ebae4645e34ce15f4d846c890a6396 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/img-htmlcode.png?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=b27c8619f875edc80b4e39afcfe43368 2500w" />
   </Frame>

### Testing your badge

1. **Run your app**\
   Run your Replit App, then select **Open in a new tab**
   <Frame>
     <img src="https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/misc/img-openintab.png?fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=732574a185edd33c9086f77c602565d5" alt="Open in a new tab button" data-og-width="1378" width="1378" data-og-height="648" height="648" data-path="images/misc/img-openintab.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/misc/img-openintab.png?w=280&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=b122e48a007a0eed65d70923ea273579 280w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/misc/img-openintab.png?w=560&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=6a8218bf46b8d2c8bc0c7536eb67d0fe 560w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/misc/img-openintab.png?w=840&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=d5b48a1282f1ce0aa2e8eeae3e2ba292 840w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/misc/img-openintab.png?w=1100&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=434a7813355cadd8b7dd4bfa96df4ab8 1100w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/misc/img-openintab.png?w=1650&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=bc4445e090f55fe350b75f1040ef3b99 1650w, https://mintcdn.com/replit/AZ1L8RlIroSxuJDa/images/misc/img-openintab.png?w=2500&fit=max&auto=format&n=AZ1L8RlIroSxuJDa&q=85&s=6caa5f9a2d8f4b06879cec03d31d48ad 2500w" />
   </Frame>

2. **View the badge**\
   Your Badge should appear in the lower right corner. This is what visitors to your page will see.
   <Frame>
     <img src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/badge-preview.png?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4a59ad02f12488fa7f9c16a96caf0a28" alt="Badge Preview" data-og-width="3122" width="3122" data-og-height="1742" height="1742" data-path="images/misc/badge-preview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/badge-preview.png?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d45017c013c5be3d10194f1aff374d0b 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/badge-preview.png?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3e3fedb9f44ae0d96d7e451dc54293b6 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/badge-preview.png?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=69fea8135f0e2ca53bd0eee5f3020a93 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/badge-preview.png?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=82d30c2cff9e682b4ee7cb3ed5b1eef0 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/badge-preview.png?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=cf1c81a675c8fdc86e5db06831a142ac 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/misc/badge-preview.png?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=068e7d76820bb85890e09f8858ac7911 2500w" />
   </Frame>

3. **Test the link**\
   Select your Badge to verify it links back to the Replit App's cover page

### Customizing your badge

<Accordion title="Changing the color theme">
  You can change the color of your Badge by modifying the `theme` attribute with any of these colors: dark, light, red, orange, yellow, lime, green, teal, blue, blurple, purple, magenta, or pink.

  ```html  theme={null}
  <script
    src="https://replit.com/public/js/replit-badge-v2.js"
    theme="pink"
    position="bottom-right"
  ></script>
  ```
</Accordion>

<Accordion title="Changing the position">
  You can change the position of your Badge by modifying the `position` attribute with one of these values: `top-left`, `top-right`, `bottom-left`, or `bottom-right`.

  ```html  theme={null}
  <script
    src="https://replit.com/public/js/replit-badge-v2.js"
    theme="dark"
    position="top-left"
  ></script>
  ```

  <Note>
    If the position isn't changing, check the browser console for more information—you may have specified an invalid position.
  </Note>
</Accordion>

<Accordion title="Removing the badge">
  If the Badge was added by default and you want to remove it, delete the script from `index.html`:

  ```html  theme={null}
  <!-- Delete this -->
  <script src="https://replit.com/public/js/replit-badge-v2.js"></script>
  ```
</Accordion>

### Advanced options

<Accordion title="Creating custom badges">
  If the default configurations don't meet your needs, you can create custom badges with standard HTML and CSS.

  Badges are hosted on `https://replit.com/badge`, allowing you to embed them as images and further style them with CSS.

  ```html  theme={null}
  <style>
    #replitBadge {
      position: fixed;
      bottom: 0;
      left: 0;
    }
  </style>

  <img
    src="https://replit.com/badge?theme=light"
    id="replitBadge"
    alt="Replit Badge"
  />
  ```

  You can also use additional options not available in the script:

  **Custom caption** (maximum 30 characters):

  ```
  https://replit.com/badge?caption=Amazing%20Badges
  ```

  <Frame>
    ![Amazing Replit Badge](https://replit.com/badge?caption=Amazing%20Badges)
  </Frame>

  **Smaller variant**:

  ```
  https://replit.com/badge?caption=Amazing%20Badges&variant=small
  ```

  <Frame>
    ![Amazing small Replit Badge](https://replit.com/badge?caption=Amazing%20Badges\&variant=small)
  </Frame>
</Accordion>

<Accordion title="Embedding in Markdown">
  You can showcase your Replit Badge by embedding it in your repository README. This Markdown snippet combines a link and image to redirect users to your Replit App:

  ```
  [![Try with Replit Badge](https://replit.com/badge?caption=Try%20with%20Replit)](https://replit.com/)
  ```

  Try selecting this:

  <Frame>
    [![Try with Replit Badge](https://replit.com/badge?caption=Try%20with%20Replit)](https://replit.com/)
  </Frame>
</Accordion>

Share your feedback about this feature in the Community!
