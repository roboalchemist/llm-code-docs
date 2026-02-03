# Source: https://docs.replit.com/getting-started/quickstarts/import-from-figma.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Import from Figma

> Learn how to import Figma designs into Replit and convert them into functional React applications.

export const YouTubeEmbed = ({videoId, title = "YouTube video", startAt}) => {
  if (!videoId) {
    return null;
  }
  let url = "https://www.youtube.com/embed/" + videoId;
  if (startAt) {
    url = url + "?start=" + startAt;
  }
  return <Frame>
      <iframe src={url} title={title} allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>
    </Frame>;
};

export const platform_0 = "Figma"

export const projectType_0 = "design"

export const setupDescription_0 = "Replit automatically sets up your app's environment and dependencies"

## Import your Figma design

⏰ *Estimated time: three minutes*

You can import your Figma designs and turn them into functional React apps on Replit.

<YouTubeEmbed videoId="NBiFBZaBnaE" />

This quickstart covers how to convert your designs into working applications using AI-powered code generation.

For comprehensive import options including other platforms like GitHub, Bolt, and Lovable, see the [Import feature documentation](/replit-app/import-to-replit).

<Frame>
  <img src="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=38babb9582d24c957cf796a2835998ff" alt="Preview of Figma design import in Replit" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/workspace/import/figma.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma.jpg?w=280&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=6787bd6628aa63b60cd3eb89b2b4b18a 280w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma.jpg?w=560&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=bbe9df9f11127e9129da4de554a989e1 560w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma.jpg?w=840&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=cd38d54b9474007534010144cffae99f 840w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma.jpg?w=1100&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=ae2da1dd78f4e144c86f0eac8958301c 1100w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma.jpg?w=1650&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=d1e026158873d451e0feb021297c62bc 1650w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma.jpg?w=2500&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=ac83eb96357667bbc2eb0e4745f086d3 2500w" />
</Frame>

## Import your design

1. Navigate to <a href="https://replit.com/import" target="_blank">[https://replit.com/import](https://replit.com/import)</a>.

<Frame>
  <img src="https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=da889239a53ed37e7d3434a2a8a34557" alt="Replit import interface showing available sources" data-og-width="2314" width="2314" data-og-height="1026" height="1026" data-path="images/workspace/import/importer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?w=280&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=78fd4da44bc74153eac8aa8b8580576b 280w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?w=560&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=3650524ad81098c312509c0be726d613 560w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?w=840&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=80c475f748da291593f20aa586855cbb 840w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?w=1100&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=3564782931bb3ddf96cc85f55be6b471 1100w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?w=1650&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=d4a3d1aa5c113359124c9e7c0467b48d 1650w, https://mintcdn.com/replit/MK9i8SYxV1DZCZTD/images/workspace/import/importer.png?w=2500&fit=max&auto=format&n=MK9i8SYxV1DZCZTD&q=85&s=215bae2f594267c3365bd1c4e8d3659c 2500w" />
</Frame>

2. Select **Figma** from the available import sources.

3. **Connect your Figma account** to authorize access to your designs.

<Frame>
  <img src="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-auth.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=b26e735e1ebc34e302383526641df7b4" alt="Figma authentication process in Replit" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/workspace/import/figma-auth.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-auth.jpg?w=280&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=45001ea054929ac43be8f4b2885a8074 280w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-auth.jpg?w=560&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=52fda67a22868cd84a235ad4327344d6 560w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-auth.jpg?w=840&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=bfdbd6a71982c9823bcbef08b171e538 840w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-auth.jpg?w=1100&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=3556ac5efe35bdebfcc581ea1510288e 1100w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-auth.jpg?w=1650&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=79280b1dbc01cc277eef4dce6a9c367e 1650w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-auth.jpg?w=2500&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=db960ea332e6098306c54caf6124b002 2500w" />
</Frame>

4. **In Figma, select the frame** you want to build in Replit.

<Frame>
  <img src="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-frame.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=1c46a57f9ac479f4e0dec81a1d6d27d7" alt="Selecting a frame in Figma for import" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/workspace/import/figma-frame.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-frame.jpg?w=280&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=d69039b20ca926d847d524403d469f6d 280w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-frame.jpg?w=560&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=2e6c848a22b17fc683d45f21e472f132 560w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-frame.jpg?w=840&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=752b18d008c275434c473145148ef927 840w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-frame.jpg?w=1100&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=ca89ac4e66898794c39268ac2e850477 1100w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-frame.jpg?w=1650&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=79fb7058ccaa73eb28bc57f06dcb4042 1650w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-frame.jpg?w=2500&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=27ead57ec016534e1013c810f16b0dc1 2500w" />
</Frame>

5. **Copy the frame URL** from Figma and paste it into the Replit import interface.

6. Select **Import** to start the conversion process.

<Frame>
  <img src="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-progress.jpg?fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=d27e3e9f76e7381f431826ee8d90bdb4" alt="Figma import progress in Replit" data-og-width="712" width="712" data-og-height="708" height="708" data-path="images/workspace/import/figma-progress.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-progress.jpg?w=280&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=0b085b04ed7fd033f443ed9a394b32d6 280w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-progress.jpg?w=560&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=379f2c481bccebb3fdb982d2c1790c54 560w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-progress.jpg?w=840&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=acddb443b71f5459b5844e89c35679ff 840w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-progress.jpg?w=1100&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=37b802bbd51bdab8d4b5cf947a09a994 1100w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-progress.jpg?w=1650&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=11ccebc33e5e592f5bd08ca9a59ec94b 1650w, https://mintcdn.com/replit/9NKf1XREDj9JhKJb/images/workspace/import/figma-progress.jpg?w=2500&fit=max&auto=format&n=9NKf1XREDj9JhKJb&q=85&s=d04aa6d5d23bb713f3882bb57ace148c 2500w" />
</Frame>

## What gets imported

During the import process, Replit converts your Figma design into a functional React application:

* **Theme & components**: Design system elements, colors, typography, and reusable components
* **Assets & icons**: Images, icons, and other visual assets from your design
* **App scaffolding**: Basic application structure and layout framework

## Figma design guidelines

To copy the Figma Design frame URL:

1. Right-click the frame
2. Select **Copy/Paste as**
3. Select **Copy link to selection**

For optimal conversion results, ensure your Figma design is well-structured with clear component hierarchies complete with auto layout constraints.

Follow [these guidelines](https://support.animaapp.com/en/articles/6431384-create-responsive-designs-in-figma) for responsive designs in Figma. You can also ask Agent to help you make your design responsive.

### Tips

* Use auto layout constraints to ensure your design is responsive.
* Name your layers something short and meaningful.
* Convert any groups to frames
* Mark image assets for export

## Configure and run your app

During the import process, {setupDescription_0}.
If your app doesn't run as expected, Replit offers the following workspace tools to help you resolve the issues:

* **[Agent](/replitai/agent)**: Use AI to add new features, refine your imported project, and get help with code questions
* **[Secrets](/replit-workspace/workspace-features/secrets)**: Add your API keys and environment variables
* **[Workflows](/replit-workspace/workflows)**: Configure the Run button to your preferred command

## Interact in Agent chat (beta)

After importing, you can paste Figma links into Agent chat to explore layers, extract tokens, and request code changes. These Agent chat features require a Figma <strong>Dev</strong> or <strong>Full</strong> seat; the initial import does not.

See the guide: [Figma MCP Integration](/replitai/mcp/figma).

## Continue your journey

Now that you've imported your {platform_0} {projectType_0}, learn more about what you can do with your Replit App:

* [Replit Agent](/replitai/agent): Get AI assistance with code review, testing, and feature implementation
* [Make your Replit App Public](/replit-app/collaborate#make-your-replit-app-public): Share your app as a Template for others to remix
* [Replit Deployments](/category/replit-deployments): Publish your app to the cloud with a few clicks
* [Collaborate](/replit-app/collaborate): Work with others on your imported projects
