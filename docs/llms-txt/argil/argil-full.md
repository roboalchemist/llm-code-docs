# Argil Documentation

Source: https://docs.argil.ai/llms-full.txt

---

# Get an Asset by id
Source: https://docs.argil.ai/api-reference/endpoint/assets.get

get /assets/{id}
Returns a single Asset identified by its id

Returns an asset identified by its id from your library that can be used in your videos.

## Audio Assets

Audio assets from this endpoint can be used as background music in your videos. When creating a video, you can reference an audio asset's ID in the `backgroundMusic` parameter to add it as background music. See the [Create Video endpoint](/api-reference/endpoint/videos.create) for more details.

***


# List Assets
Source: https://docs.argil.ai/api-reference/endpoint/assets.list

get /assets
Get a list of available assets from your library

Returns an array of assets from your library that can be used in your videos.

## Audio Assets

Audio assets from this endpoint can be used as background music in your videos. When creating a video, you can reference an audio asset's ID in the `backgroundMusic` parameter to add it as background music. See the [Create Video endpoint](/api-reference/endpoint/videos.create) for more details.

***


# Create a new Avatar
Source: https://docs.argil.ai/api-reference/endpoint/avatars.create

post /avatars
Creates a new Avatar by uploading source videos and launches training. The process is asynchronous - the avatar will initially be created with 'NOT_TRAINED' status and will transition to 'TRAINING' then 'IDLE' once ready.



# Get an Avatar by id
Source: https://docs.argil.ai/api-reference/endpoint/avatars.get

get /avatars/{id}
Returns a single Avatar identified by its id



# List all avatars
Source: https://docs.argil.ai/api-reference/endpoint/avatars.list

get /avatars
Returns an array of Avatar objects available for the user



# List subtitle styles
Source: https://docs.argil.ai/api-reference/endpoint/subtitles.list

get /subtitles
Returns a paginated array of subtitle styles available for the user



# Create a new Video
Source: https://docs.argil.ai/api-reference/endpoint/videos.create

post /videos
Creates a new Video with the specified details



# Delete a Video by id
Source: https://docs.argil.ai/api-reference/endpoint/videos.delete

delete /videos/{id}
Delete a single Video identified by its id



# Get a Video by id
Source: https://docs.argil.ai/api-reference/endpoint/videos.get

get /videos/{id}
Returns a single Video identified by its id



# Paginated list of Videos
Source: https://docs.argil.ai/api-reference/endpoint/videos.list

get /videos
Returns a paginated array of Videos



# Render a Video by id
Source: https://docs.argil.ai/api-reference/endpoint/videos.render

post /videos/{id}/render
Returns a single Video object, with its updated status and information



# Get a Voice by id
Source: https://docs.argil.ai/api-reference/endpoint/voices.get

get /voices/{id}
Returns a single Voice identified by its id



# List all voices
Source: https://docs.argil.ai/api-reference/endpoint/voices.list

get /voices
Returns an array of Voice objects available for the user



# Create a new webhook
Source: https://docs.argil.ai/api-reference/endpoint/webhooks.create

post /webhooks
Creates a new webhook with the specified details.



# Delete a webhook
Source: https://docs.argil.ai/api-reference/endpoint/webhooks.delete

delete /webhooks/{id}
Deletes a single webhook identified by its ID.



# Retrieve all webhooks
Source: https://docs.argil.ai/api-reference/endpoint/webhooks.list

get /webhooks
Retrieves all webhooks for the authenticated user.



# Update a webhook
Source: https://docs.argil.ai/api-reference/endpoint/webhooks.update

PUT /webhooks/{id}
Updates the specified details of an existing webhook.



# API Credentials
Source: https://docs.argil.ai/pages/get-started/credentials

Create, manage and safely store your Argil's credentials

<Info>
  `Prerequisite` You should have access to Argil's app with a paid plan to
  complete this step.
</Info>

<Steps>
  <Step title="Go to the API integration page from the app">
    Manage your API keys by clicking [here](https://app.argil.ai/developers) or
    directly from the app's sidebar.
  </Step>

  <Step title="Create your API Key">
    From the UI, click on `New API key` and follow the process.

    <Frame>
      <img src="https://mintcdn.com/argil/BBUki6oAamfarwsT/images/api-key.png?fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=9b2425b5bb6269a0f906860fa26fe4aa" style={{ borderRadius: "0.5rem" }} data-og-width="1576" width="1576" data-og-height="419" height="419" data-path="images/api-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/BBUki6oAamfarwsT/images/api-key.png?w=280&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=bad0eb248a6d3d131202b3d0a7ec33f4 280w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/api-key.png?w=560&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=949fc3af500b7ef591cba3f8ce9a348a 560w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/api-key.png?w=840&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=6d273bbb7c65a663400c7fef9be04f87 840w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/api-key.png?w=1100&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=95c5bc649f11eb9c7307a2546f82c6a8 1100w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/api-key.png?w=1650&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=bbe26c5fd2f43377887d5d4d74ba2c30 1650w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/api-key.png?w=2500&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=64f400cf311a3453b409c54729b1fc51 2500w" />
    </Frame>
  </Step>

  <Step title="Use it in your request headers">
    Authenticate your requests by including your API key in the `x-api-key`
    header. \`\`\`http x-api-key: YOUR\_API\_KEY. \`\`\`\`
  </Step>

  <Step title="Implementing Best Practices for Storage and API Key Usage">
    It is essential to adhere to best practices regarding the storage and usage
    of your API key. This information is sensitive and crucial for maintaining
    the security of your services.

    <Tip>
      If any doubt about the corruption of your key, delete it and create a new
      one.
    </Tip>

    <Warning>
      Don't share your credentials with anyone. This API key enables video
      generation featuring your avatar, which may occur without your explicit
      authorization.
    </Warning>

    <Warning>Please note that Argil cannot be held responsible for any misuse of this functionality. Always ensure that your API key is handled securely to prevent unauthorized access.</Warning>
  </Step>
</Steps>

## Troubleshooting

Here's how to solve some common problems when working around your credentials setup.

<AccordionGroup>
  <Accordion title="Having troubles with your credentials setup?">
    Let us assist by [Mail](mailto:brivael@argil.ai) or
    [Discord](https://discord.gg/Xy5NEqUv).
  </Accordion>
</AccordionGroup>


# Introduction
Source: https://docs.argil.ai/pages/get-started/introduction

Welcome to Argil's API documentation

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/argil/BBUki6oAamfarwsT/images/doc-hero.png?fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=cb59bfa370195ca2f8c50d3f4c42033f" style={{ borderRadius: "8px" }} alt="Hero Light" data-og-width="2880" width="2880" data-og-height="1000" height="1000" data-path="images/doc-hero.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/BBUki6oAamfarwsT/images/doc-hero.png?w=280&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=c9f5bfea812f10ad20785287348fbd67 280w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/doc-hero.png?w=560&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=959daf0204155c29b29d7a92dc7ba64e 560w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/doc-hero.png?w=840&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=fb7236b2ee85d307a0a042ce94c89588 840w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/doc-hero.png?w=1100&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=2e6d3dae1db2840caa5dc2ffa2d3af95 1100w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/doc-hero.png?w=1650&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=f8addb860df00cf38d494769d80a9e5d 1650w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/doc-hero.png?w=2500&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=a2164cbc061288750af2d081fb94e91a 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/argil/BBUki6oAamfarwsT/images/doc-hero.png?fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=cb59bfa370195ca2f8c50d3f4c42033f" style={{ borderRadius: "8px" }} alt="Hero Dark" data-og-width="2880" width="2880" data-og-height="1000" height="1000" data-path="images/doc-hero.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/BBUki6oAamfarwsT/images/doc-hero.png?w=280&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=c9f5bfea812f10ad20785287348fbd67 280w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/doc-hero.png?w=560&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=959daf0204155c29b29d7a92dc7ba64e 560w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/doc-hero.png?w=840&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=fb7236b2ee85d307a0a042ce94c89588 840w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/doc-hero.png?w=1100&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=2e6d3dae1db2840caa5dc2ffa2d3af95 1100w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/doc-hero.png?w=1650&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=f8addb860df00cf38d494769d80a9e5d 1650w, https://mintcdn.com/argil/BBUki6oAamfarwsT/images/doc-hero.png?w=2500&fit=max&auto=format&n=BBUki6oAamfarwsT&q=85&s=a2164cbc061288750af2d081fb94e91a 2500w" />
</Frame>

This service allows content creators to seamlessly integrate video generation capabilities into their workflow, leveraging their AI Clone for personalized videos creation. Whether you're looking to enhance your social media presence, boost user engagement, or offer personalized content, Argil makes it simple and efficient.

## Setting Up

Get started with Argil's API by setting up your credentials and generate your first avatar video using our API service.

<CardGroup cols={2}>
  <Card title="Manage API Keys" icon="key" href="/pages/get-started/credentials">
    Create, manage and safely store your Argil's credentials
  </Card>

  <Card title="Quickstart" icon="flag-checkered" href="/pages/get-started/quickstart">
    Jump straight into video creation with our quick start guide
  </Card>
</CardGroup>

## Build something on top of Argil

Elaborate complex infrastructures with on-demand avatar video generation capabilities using our `Public API` and `Webhooks`.

<CardGroup>
  <Card title="Reference APIs" icon="square-code" href="/api-reference">
    Integrate your on-demand avatar anywhere.
  </Card>

  <Card title="Webhooks" icon="webhook" href="/pages/webhook-events">
    Subscribe to events and get notified on generation success and other events
  </Card>
</CardGroup>


# Quickstart
Source: https://docs.argil.ai/pages/get-started/quickstart

Start automating your content creation workflow

<Info>
  `Prerequisite` You should be all setup with your [API Credentials](/pages/get-started/credentials) before starting this tutorial.
</Info>

<Info>
  `Prerequisite` You should have successfully trained at least one [Avatar](https://app.argil.ai/avatars) from the app.
</Info>

<Steps>
  <Step icon="magnifying-glass" title="Get a look at your avatar and voice resources">
    In order to generate your first video through our API, you'll need to know which avatar and voice you want to use.

    <Note>
      Not finding your Avatar? It might not be ready yet. Check at your [Avatars](https://app.argil.ai/avatars) page for updates.
    </Note>

    <AccordionGroup>
      <Accordion icon="user" title="Check your available avatars">
        Get your avatars list by running a GET request on the `/avatars` route.

        <Tip>
          Check the [Avatars API Reference](/api-reference/endpoint/avatars.list) to run the request using an interactive UI.
        </Tip>
      </Accordion>

      <Accordion icon="microphone" title="Check your available voices">
        Get your voices list by running a GET request on the `/voices` route.

        <Tip>
          Check the [Voices API Reference](/api-reference/endpoint/voices.list) to run the request using an interactive UI.
        </Tip>
      </Accordion>
    </AccordionGroup>

    <Check>
      You are done with this step if you have the id of the avatar and and the id of the voice you want to use for the next steps.
    </Check>
  </Step>

  <Step icon="square-plus" title="Create a video">
    Create a video by running a POST request on the `/videos` route.

    <Tip>
      Check the [Video creation API Reference](/api-reference/endpoint/videos.create) to run the request using an interactive UI.
    </Tip>

    To create a `Video` resource, you'll need:

    * A `name` for the video
    * A list of `Moment` objects, representing segments of your final video. For each moment, you will be able to choose the `avatar`, the `voice` and the `transcript` to be used.

    <Tip>
      For each moment, you can also optionally specify:

      * An audioUrl to be used as voice for the moment. This audio will override our voice generation.
      * A gestureSlug to select which gesture from the avatar should be used for the moment.
    </Tip>

    ```mermaid  theme={null}
    flowchart TB
        subgraph video["Video {name}"]
            direction LR
              subgraph subgraph1["Moment 1"]
                  direction LR
                  item1{{avatar}}
                  item2{{voice}}
                  item3{{transcript}}
                  item4{{optional - gestureSlug}}
                  item5{{optional - audioUrl}}
              end
              subgraph subgraph2["Moment n"]
                  direction LR
                  item6{{avatar}}
                  item7{{voice}}
                  item8{{transcript}}
                  item9{{optional - gestureSlug}}
                  item10{{optional - audioUrl}}
              end
              subgraph subgraph3["Moment n+1"]
                  direction LR
                  item11{{avatar}}
                  item12{{voice}}
                  item13{{transcript}}
                  item14{{optional - gestureSlug}}
                  item15{{optional - audioUrl}}
              end
              subgraph1 --> subgraph2
              subgraph2 --> subgraph3
        end
    ```

    <Check>
      You are done with this step if the request returned a status 201 and a Video object as body.
      <br />Note the `Video id` for the next step.
    </Check>
  </Step>

  <Step icon="video" title="Render the video you have created">
    Render a video by running a POST request on the `/videos/{video_id}/render` route.

    <Tip>
      Check the [Render API Reference](/api-reference/endpoint/videos.render) to run the request using an interactive UI.
    </Tip>

    <Check>
      You are done with this step if the route returned a Video object, with its status set to `GENERATING_AUDIO` or `GENERATING_VIDEO`.
    </Check>
  </Step>

  <Step icon="badge-check" title="Check for updates until your avatar's video generation is finished">
    Get your video's updates by running a GET request on the `/videos/[id]` route.

    <Tip>
      Check the [Videos API Reference](/api-reference/endpoint/videos.get) to run the request using an interactive UI.
    </Tip>

    <Check>
      You are done with this step once the route returns a `Video` object with status set to `DONE`.
    </Check>
  </Step>

  <Step icon="share-nodes" title="Retrieve your avatar's video">
    From the Video object you obtains in the previous step, retrieve the `videoUrl` field.

    <Tip>
      Use this url anywhere to download / share / publish your video and automate your workflow.
    </Tip>
  </Step>
</Steps>


# Avatar Training Failed Webhook
Source: https://docs.argil.ai/pages/webhook-events/avatar-training-failed

Get notified when an avatar training failed

## About the Avatar Training Failed Event

The `AVATAR_GENERATION_FAILED` event is triggered when an avatar training process fails in Argil. This webhook event provides your service with a payload containing detailed information about the failed generation.

## Payload Details

When this event triggers, the following data is sent to your callback URL:

```json  theme={null}
{
  "event": "AVATAR_TRAINING_FAILED",
  "data": {
    "avatarId": "<avatar_id>",
    "avatarName": "<avatar_name>",
    "extras": "<additional_key-value_data_related_to_the_avatar>"
  }
}
```

<Note>
  For detailed instructions on setting up this webhook event, visit our [Webhooks API Reference](/pages/api-reference/endpoint/webhooks.create).
</Note>


# Avatar Training Success Webhook
Source: https://docs.argil.ai/pages/webhook-events/avatar-training-success

Get notified when an avatar training completed successfully

## About the Avatar Training Success Event

The `AVATAR_TRAINING_SUCCESS` event is triggered when an avatar training process completes successfully in Argil. This webhook event provides your service with a payload containing detailed information about the successful avatar training.

## Payload Details

When this event triggers, the following data is sent to your callback URL:

```json  theme={null}
{
  "event": "AVATAR_TRAINING_SUCCESS",
  "data": {
    "avatarId": "<avatar_id>",
    "voiceId": "<voice_id>",
    "avatarName": "<avatar_name>",
    "extras": "<additional_key-value_data_related_to_the_avatar>"
  }
}
```

<Note>
  For detailed instructions on setting up this webhook event, visit our [Webhooks API Reference](/pages/api-reference/endpoint/webhooks.create).
</Note>


# Introduction to Argil's Webhook Events
Source: https://docs.argil.ai/pages/webhook-events/introduction

Learn what webhooks are, how they work, and how to set them up with Argil through our API.

## What are Webhooks?

Webhooks are automated messages sent from apps when something happens. In the context of Argil, webhooks allow you to receive real-time notifications about various events occurring within your environment, such as video generation successes and failures or avatar training successes and failures.

## How Webhooks Work

Webhooks in Argil send a POST request to your specified callback URL whenever subscribed events occur. This enables your applications to respond immediately to events within Argil as they happen.

### Available Events for subscription

<AccordionGroup>
  <Accordion title="Video Generation Success">
    This event is triggered when an avatar video generation is successful.<br />
    Check our [VIDEO\_GENERATION\_SUCCESS Event Documentation](/pages/webhook-events/video-generation-success) for more information about this event.
  </Accordion>

  <Accordion title="Video Generation Failed">
    This event is triggered when an avatar video generation is failed.<br />
    Check our [VIDEO\_GENERATION\_FAILED Event Documentation](/pages/webhook-events/video-generation-failed) for more information about this event.
  </Accordion>

  <Accordion title="Avatar Training Success">
    This event is triggered when an avatar training is successful.<br />
    Check our [AVATAR\_TRAINING\_SUCCESS Event Documentation](/pages/webhook-events/avatar-training-success) for more information about this event.
  </Accordion>

  <Accordion title="Avatar Training Failed">
    This event is triggered when an avatar training is failed.<br />
    Check our [AVATAR\_TRAINING\_FAILED Event Documentation](/pages/webhook-events/avatar-training-failed) for more information about this event.
  </Accordion>
</AccordionGroup>

<Tip>
  A single webhook can subscribe to multiple events.
</Tip>

## Managing Webhooks via API

You can manage your webhooks entirely through API calls, which allows you to programmatically list, register, edit, and unregister webhooks. Below are the primary actions you can perform with our API:

<AccordionGroup>
  <Accordion title="List All Webhooks">
    Retrieve a list of all your registered webhook.<br />
    [API Reference for Listing Webhooks](/api-reference/endpoint/webhooks.list)
  </Accordion>

  <Accordion title="Register to a Webhook">
    Learn how to register a webhook by specifying a callback URL and the events you are interested in.<br />
    [API Reference for Creating Webhooks](/api-reference/endpoint/webhooks.create)
  </Accordion>

  <Accordion title="Unregister a Webhook">
    Unregister a webhook when it's no longer needed.<br />
    [API Reference for Deleting Webhooks](/api-reference/endpoint/webhooks.delete)
  </Accordion>

  <Accordion title="Edit a Webhook">
    Update your webhook settings, such as changing the callback URL or events.<br />
    [API Reference for Editing Webhooks](/api-reference/endpoint/webhooks.update)
  </Accordion>
</AccordionGroup>


# Video Generation Failed Webhook
Source: https://docs.argil.ai/pages/webhook-events/video-generation-failed

Get notified when an avatar video generation failed

## About the Video Generation Failed Event

The `VIDEO_GENERATION_FAILED` event is triggered when a video generation process fails in Argil. This webhook event provides your service with a payload containing detailed information about the failed generation.

## Payload Details

When this event triggers, the following data is sent to your callback URL:

```json  theme={null}
{
  "event": "VIDEO_GENERATION_FAILED",
  "data": {
    "videoId": "<video_id>",
    "videoName": "<video_name>",
    "videoUrl": "<public_url_to_access_video>",
    "extras": "<additional_key-value_data_related_to_the_video>"
  }
}
```

<Note>
  For detailed instructions on setting up this webhook event, visit our [Webhooks API Reference](/pages/api-reference/endpoint/webhooks.create).
</Note>


# Video Generation Success Webhook
Source: https://docs.argil.ai/pages/webhook-events/video-generation-success

Get notified when an avatar video generation completed successfully

## About the Video Generation Success Event

The `VIDEO_GENERATION_SUCCESS` event is triggered when a video generation process completes successfully in Argil. This webhook event provides your service with a payload containing detailed information about the successful video generation.

## Payload Details

When this event triggers, the following data is sent to your callback URL:

```json  theme={null}
{
  "event": "VIDEO_GENERATION_SUCCESS",
  "data": {
    "videoId": "<video_id>",
    "videoName": "<video_name>",
    "videoUrl": "<public_url_to_access_video>",
    "extras": "<additional_key-value_data_related_to_the_video>"
  }
}
```

<Note>
  For detailed instructions on setting up this webhook event, visit our [Webhooks API Reference](/pages/api-reference/endpoint/webhooks.create).
</Note>


# Account settings
Source: https://docs.argil.ai/resources/account-settings

Issues with logging in (Google Sign up and normal email sign up)

### Account Merger

When you created an account using Google Sign up, you will have a possibility to create another account via email + password with the same email adress. You will then be asked to merge accounts and need to click on yes.

<Warning>
  If you see a merger prompt during login, **click on "continue"** to proceed.
</Warning>

<img src="https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-01-03a%CC%8000.17.22.png?fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=fd457934fa07b883aa55a008dc1df662" alt="" data-og-width="634" width="634" data-og-height="806" height="806" data-path="images/Captured’écran2025-01-03à00.17.22.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-01-03a%CC%8000.17.22.png?w=280&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=87c83b2bbec8a2344a27569e48759c1f 280w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-01-03a%CC%8000.17.22.png?w=560&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=28e496c4b61bde631f75ea567ebc9194 560w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-01-03a%CC%8000.17.22.png?w=840&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=f5f0936391018944bd3b52ac6a103c96 840w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-01-03a%CC%8000.17.22.png?w=1100&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=dd51a76a4d5b088373ff306dff8aa4c4 1100w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-01-03a%CC%8000.17.22.png?w=1650&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=f753075c1ab8ee17780497594c9c6c8a 1650w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-01-03a%CC%8000.17.22.png?w=2500&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=ea5c2afc527ffdeb6e62a4a8951fad6d 2500w" />

It means that you created your account with Google then via normal email for a second account but with the same address. This creates two different accounts that you need to merge.

### Password Reset

<Steps>
  <Step title="Log out">
    Sign out of your current account
  </Step>

  <Step title="Reset password">
    Click on "Forgot password?" and follow the instructions
  </Step>
</Steps>

### Workspaces

<Card title="Coming Soon" icon="users">
  Workspaces will allow multiple team members with different emails to collaborate in the same studio.

  Need early access? Contact us at [support@argil.ai](mailto:support@argil.ai)
</Card>


# Affiliate Program
Source: https://docs.argil.ai/resources/affiliates

Earn money by referring users to Argil

### Join Our Affiliate Program

<CardGroup cols="1">
  <Card title="Start Earning Now" icon="rocket" href="https://argil.getrewardful.com/signup">
    Click here to join the Argil Affiliate Program and start earning up to €5k/month
  </Card>
</CardGroup>

<Warning>
  SEA campaigns and Facebook ads campaigns are forbidden.
</Warning>

### How it works

Get 30% of your affiliates' generated revenue for 12 months by sharing your unique referral link. You get paid every first week of the month, no minimum threshold required.

### Getting started

1. Click the signup button above to create your account
2. Fill out the required information
3. Receive your unique referral link
4. Share your link with your network
5. [Track earnings in your dashboard](https://argil.getrewardful.com/)

### Earnings

<CardGroup cols="2">
  <Card title="Revenue Share" icon="money-bill">
    30% commission per referral with potential earnings up to €5k/month
  </Card>

  <Card title="Duration" icon="clock">
    Valid for 12 months from signup
  </Card>

  <Card title="Tracking" icon="chart-line">
    Real-time dashboard analytics
  </Card>
</CardGroup>

### Managing your account

1. Access dashboard at argil.getrewardful.com
2. View revenue overview with filters
3. Track referred users and earnings
4. Monitor payment status

### Success story

<Note>
  "I've earned \$4,500 in three months by simply referring others to their AI video platform" - Othmane Khadri, CEO of Earleads
</Note>

<Warning>
  Always disclose your affiliate relationship when promoting Argil
</Warning>


# API - Pricing
Source: https://docs.argil.ai/resources/api-pricings

Here are the pricings for the API

All prices below apply to all clients that are on a **Classic plan or above.**

<Warning>
  If you **are an entreprise client** (over **60,000 credits/month** or requiring **specific support**), please [contact us here](mailto:enterprise@argil.ai).
</Warning>

| Feature                           | Pricing per unit   |
| --------------------------------- | ------------------ |
| Video                             | 140 credits/minute |
| Voice                             | 20 credits/minute  |
| Royalty (Argil's v1 avatars only) | 20 credits/video   |
| B-roll (AI image)                 | 10 credit/b-roll   |
| B-roll (stock video)              | 20 credit/b-roll   |

<Note>
  For a 30 second video with 3 Image B-rolls and Argil v1 avatar, the credit cost will be \
  70 (*video*)\\+ 10 (voice) + 20 (royalty) + 30 (b-rolls) =  130 credits$0.35 (video) \+ $
</Note>

### Frequently asked questions

<Note>
  Avatar Royalties only apply to Argil's avatars - if you train your own avatar, you will not pay for it.
</Note>

<AccordionGroup>
  <Accordion title="Can I avoid paying for voice?" defaultOpen="false">
    Yes, we have a partnership with [Elevenlabs](https://elevenlabs.io/) for voice. If you have an account there with your voices, you can link your Elevenlabs account to Argil (see how here) and you will not pay for voice using the API.
  </Accordion>

  <Accordion title="What is the &#x22;avatar royalty&#x22;?" defaultOpen="false">
    At Argil, we are commited to give our actors (generic avatars) their fair share - we thus have a royalty system in place with them. By measure of transparency and since it may evolve, we're adding it as a separate pricing for awareness.
  </Accordion>

  <Accordion title="Why do I need to subscribe to a plan for the API?" defaultOpen="false">
    We make it simpler for clients to use any of our products by sharing their credits regardless of what platform they use - we thus require to create an account to use our API.
  </Accordion>

  <Accordion title="How to buy credits?" defaultOpen="false">
    To buy credits, just go to app.argil.ai. On the bottom left, click on "get more" or "upgrade" and you will be able to buy more credits from there.
  </Accordion>
</AccordionGroup>


# Article to video
Source: https://docs.argil.ai/resources/article-to-video

How does the article to video feature work?

<Note>
  Some links may not work - in this case, please reach out to [support@argil.ai](mailto:support@argil.ai)
</Note>

Transforming article into videos yields <u>major benefits</u> and is extremely simple. It allows:

* Better SEO rankings
* Social-media ready video content on a video that ha
* Monetizing the video if you have the ability to

### How to transform an article into a video

<Steps>
  <Step title="Pick the article-to-video template">
        <img src="https://mintcdn.com/argil/bb8X9WKnnGHAPpTE/images/Captured%E2%80%99e%CC%81cran2025-10-23a%CC%8015.30.39.png?fit=max&auto=format&n=bb8X9WKnnGHAPpTE&q=85&s=fd289d3246714c63e3f34e8a1ca626ea" alt="Captured’écran2025 10 23à15 30 39 Pn" data-og-width="524" width="524" data-og-height="142" height="142" data-path="images/Captured’écran2025-10-23à15.30.39.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/bb8X9WKnnGHAPpTE/images/Captured%E2%80%99e%CC%81cran2025-10-23a%CC%8015.30.39.png?w=280&fit=max&auto=format&n=bb8X9WKnnGHAPpTE&q=85&s=9a24cfa6c00a708a2d35b3e714d0c4cd 280w, https://mintcdn.com/argil/bb8X9WKnnGHAPpTE/images/Captured%E2%80%99e%CC%81cran2025-10-23a%CC%8015.30.39.png?w=560&fit=max&auto=format&n=bb8X9WKnnGHAPpTE&q=85&s=9b04b24adff8afa845df4f4d8a3a7930 560w, https://mintcdn.com/argil/bb8X9WKnnGHAPpTE/images/Captured%E2%80%99e%CC%81cran2025-10-23a%CC%8015.30.39.png?w=840&fit=max&auto=format&n=bb8X9WKnnGHAPpTE&q=85&s=ad03038fc2d6c4d16de0bf2beea66d59 840w, https://mintcdn.com/argil/bb8X9WKnnGHAPpTE/images/Captured%E2%80%99e%CC%81cran2025-10-23a%CC%8015.30.39.png?w=1100&fit=max&auto=format&n=bb8X9WKnnGHAPpTE&q=85&s=59992612c6cc534b715803d77d42eb6c 1100w, https://mintcdn.com/argil/bb8X9WKnnGHAPpTE/images/Captured%E2%80%99e%CC%81cran2025-10-23a%CC%8015.30.39.png?w=1650&fit=max&auto=format&n=bb8X9WKnnGHAPpTE&q=85&s=1a66097503da52647e796be3c6a55261 1650w, https://mintcdn.com/argil/bb8X9WKnnGHAPpTE/images/Captured%E2%80%99e%CC%81cran2025-10-23a%CC%8015.30.39.png?w=2500&fit=max&auto=format&n=bb8X9WKnnGHAPpTE&q=85&s=c58cdeec08df55a1da180ae4f8860c20 2500w" />
  </Step>

  <Step title="Paste the link of your article and choose the format">
    You can choose a social media format (with a social media tone) or a more classic format to embed in your articles, that will produce a longer video.
  </Step>

  <Step title="Pick the avatar of your choice">
        <img src="https://mintcdn.com/argil/bb8X9WKnnGHAPpTE/images/Captured%E2%80%99e%CC%81cran2025-10-23a%CC%8015.30.15.png?fit=max&auto=format&n=bb8X9WKnnGHAPpTE&q=85&s=80ce8a5a9e8ce9fbc22afd6178e5c043" alt="Captured’écran2025 10 23à15 30 15 Pn" data-og-width="497" width="497" data-og-height="303" height="303" data-path="images/Captured’écran2025-10-23à15.30.15.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/bb8X9WKnnGHAPpTE/images/Captured%E2%80%99e%CC%81cran2025-10-23a%CC%8015.30.15.png?w=280&fit=max&auto=format&n=bb8X9WKnnGHAPpTE&q=85&s=a6b191eb49155291e94f2b3c0724af34 280w, https://mintcdn.com/argil/bb8X9WKnnGHAPpTE/images/Captured%E2%80%99e%CC%81cran2025-10-23a%CC%8015.30.15.png?w=560&fit=max&auto=format&n=bb8X9WKnnGHAPpTE&q=85&s=340615f8280e6358cf3515f2f251874f 560w, https://mintcdn.com/argil/bb8X9WKnnGHAPpTE/images/Captured%E2%80%99e%CC%81cran2025-10-23a%CC%8015.30.15.png?w=840&fit=max&auto=format&n=bb8X9WKnnGHAPpTE&q=85&s=3884e191f2b49801040b1230e0897937 840w, https://mintcdn.com/argil/bb8X9WKnnGHAPpTE/images/Captured%E2%80%99e%CC%81cran2025-10-23a%CC%8015.30.15.png?w=1100&fit=max&auto=format&n=bb8X9WKnnGHAPpTE&q=85&s=fb13ec8125bdc184569d49ee5ff40713 1100w, https://mintcdn.com/argil/bb8X9WKnnGHAPpTE/images/Captured%E2%80%99e%CC%81cran2025-10-23a%CC%8015.30.15.png?w=1650&fit=max&auto=format&n=bb8X9WKnnGHAPpTE&q=85&s=44fc1c3323ca6d6981c9befc69f138c8 1650w, https://mintcdn.com/argil/bb8X9WKnnGHAPpTE/images/Captured%E2%80%99e%CC%81cran2025-10-23a%CC%8015.30.15.png?w=2500&fit=max&auto=format&n=bb8X9WKnnGHAPpTE&q=85&s=46a0f0e3fe2fb0fb484624b0c53a7b5d 2500w" />
  </Step>

  <Step title="Review the generated script and media">
    A script is automatically created for your video, but we also pull the images & videos we found in the original article. Remove those that you do not want, and pick the other options (see our editing tips (**add link)** for that).
  </Step>

  <Step title="Click &#x22;generate video&#x22; to arrive in the studio">
    From there, just follow the editing tips (add link) to get the best possible video.
  </Step>
</Steps>

### Frequently asked questions

<Accordion title="Can I use Article to video via API?" defaultOpen="false">
  Yes you can! See our API documentation
</Accordion>


# Assets
Source: https://docs.argil.ai/resources/assets

How do assets work, what type of files can be uploaded

If you are using the same images or videos quite often, uploading them to the asset section is the best way to have them all stored at the same place.

### How do I add an image or a video to the assets?

You can either:

a) Go in the asset section on the left panel then "Upload" directly\
b) Go into create a video then "Upload media" in the next tab\
c) If you are editing a video in the studio, all the images and videos that you upload there will be stored in the assets section.

<Info>
  Video B-rolls from Getty image won't be stored
</Info>

### Are Veo3 and Hailuo videos automatically saved in the asset section?

Yes, Veo3 and Hailuo videos generated via Argil will always be saved in the asset section.


# Upload audio and voice-transformation
Source: https://docs.argil.ai/resources/audio-and-voicetovoice

Get more control on the dynamism of your voice. 

Two ways to use audio instead of text to generate a video:

<Warning>
  Supported audio formats are **mp3, wav, m4a** with a maximum size of **50mb**.
</Warning>

<CardGroup cols="2">
  <Card title="Upload audio file" icon="upload">
    Upload your pre-recorded audio file and let our AI transcribe it automatically
  </Card>

  <Card title="Record on Argil" icon="microphone">
    Use our built-in recorder to capture your voice with perfect audio quality
  </Card>
</CardGroup>

### Voice transformation guarantees amazing results

<Tip>
  After uploading, our AI will transcribe your audio and let you transform your voice while preserving emotions and tone.
</Tip>

<img src="https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-01-02a%CC%8023.42.08.png?fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=5f73d92b9de2eab01aaf921b13a326ce" alt="" data-og-width="872" width="872" data-og-height="238" height="238" data-path="images/Captured’écran2025-01-02à23.42.08.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-01-02a%CC%8023.42.08.png?w=280&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=9ceeafc6c587eb859ecfba9ad0727e51 280w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-01-02a%CC%8023.42.08.png?w=560&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=1f4d41aaf009043f1ff91d88a4fbb8ea 560w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-01-02a%CC%8023.42.08.png?w=840&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=ff32737330cbff371f86e91c396ff1b3 840w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-01-02a%CC%8023.42.08.png?w=1100&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=9f069fdbace34c13864a8277b379e20a 1100w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-01-02a%CC%8023.42.08.png?w=1650&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=7cd60ba3340bf7f77e1699141a91bbd8 1650w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-01-02a%CC%8023.42.08.png?w=2500&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=4d1efbb1fb64da894813257344fa65e2 2500w" />


# B-roll & medias
Source: https://docs.argil.ai/resources/brolls



### Adding B-rolls or medias to a clip

To enrich your videos, you can add image or video B-rolls to your video - they can be placed automatically by our algorithm or you can place them yourself on a specific clip. You can also upload your own media.&#x20;

<Tip>
  Toggling "Auto b-rolls" in the script screen will automatically populate your video with B-rolls in places that our AI magic editing finds the most relevant&#x20;
</Tip>

### There are 4 types of B-rolls&#x20;

<Warning>
  Supported formats for uploads are **jpg, png, mov, mp4** with a maximum size of **50mb.**
  You can use websites such as [freeconvert](https://www.freeconvert.com/) if your image/video is in the wrong format or too heavy.
</Warning>

<CardGroup cols="2">
  <Card title="AI image" icon="image">
    This will generate an AI image in a style fitting the script, for that specific moment. It will take into account the whole video and the other B-rolls in order to place the most accurate one.&#x20;
  </Card>

  <Card title="Stock video" icon="video">
    This will find a small stock video of the right format and place it on your video
  </Card>

  <Card title="Google images" icon="google">
    This will search google for the most relevant image to add to this moment
  </Card>

  <Card title="Upload image/video" icon="upload">
    In case you wish to add your own image or video. Supported formats are jpg, png mp4 mov
  </Card>
</CardGroup>

### Adding a B-roll or media to a clip

<Tip>
  A B-roll or media
</Tip>

<Steps>
  <Step title="Click on the right clip">
    Choose the clip you want to add the B-roll to and click on it. A small box will appear with a media icon. Click on it.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/argil/Screenshot2024-12-31at11.18.05.png" alt="" />
  </Step>

  <Step title="Choose the type of B-roll you want to add">
    At the top, pick the type of B-roll you wish to add.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/argil/Screenshot2024-12-31at11.23.13.png" alt="" />
  </Step>

  <Step title="Shuffle until satisfied">
    If the first image isn't satisfactory, press the shuffle (left icon) until you like the results. Each B-roll can be shuffled 3 times.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/argil/Screenshot2024-12-31at11.38.46.png" alt="" />
  </Step>

  <Step title="Adjust settings">
    You can pick 2 settings: display and length

    1. Display: this will either display the image **in front of your avatar** or **behind your avatar**. Very convenient when you wish to have yourself speaking

    2. Length: if the moment is too long

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/argil/Screenshot2024-12-31at11.41.10.png" alt="" />
  </Step>

  <Step title="Add media">
    When you're happy with the preview, don't forget to click "Add media" to add the b-roll to this clip! You can then preview the video.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/argil/Screenshot2024-12-31at11.38.46.png" alt="" />
  </Step>
</Steps>

### B-roll options

<AccordionGroup>
  <Accordion title="Display (placing b-roll behind avatar)" defaultOpen={false}>
    Sometimes, you may want your avatar to be visible and speaking while showing the media - in order to do this, the **display** option is available.&#x20;

    1. Display "front" will place the image **in front** of your avatar, thus hiding it

    2. Display "back" will place the image **behind** your avatar, showing it speaking while the image is playing
  </Accordion>

  <Accordion title="Length" defaultOpen={false}>
    If the clip is too long, you may wish that the b-roll doesn't display for its full length. For this, an option exists to **cut the b-roll in half** of its duration. Just click on "Length: 1/2". We will add more options in the future.

    Note that for dynamic and engaging videos, we advise to avoid making specific clips too long - see our editing tips below&#x20;
  </Accordion>
</AccordionGroup>

<Card title="Editing tips" icon="bolt" horizontal={1}>
  Check out our editing tips to make your video the most engaging possible
</Card>

### **Deleting a B-roll**

To remove the B-roll from this clip, simply click on the b-roll to open the popup then press the 🗑️ trash icon in the popup.&#x20;


# Captions
Source: https://docs.argil.ai/resources/captions



Captions are a crucial part of a video - among other topics, it allows viewers to watch them on mobile without sound or understand the video better.

/

### Adding captions from a script

<Tip>
  Make sure to enable "Auto-captions" on the script page before generating the preview to avoid generating them later
</Tip>

<Steps>
  <Step title="Toggle the captions in the right sidebar">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/argil/Screenshot2025-01-02at15.47.30.png" alt="" />
  </Step>

  <Step title="Pick style, size and position">
    Click on the "CC" icon to open the styling page and pick your preferences.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/argil/Screenshot2025-01-02at15.48.34.png" alt="" />
  </Step>

  <Step title="Preview the results">
    Preview the results by clicking play and make sure the results work well
  </Step>

  <Step title="Re-generate captions if you edit text">
    If you changed the text after generating captions, note that a new icon appears with 2 blue arrows. Click on it to <u>re-generate captions</u> after editing text.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/argil/Screenshot2025-01-02at15.55.59.png" alt="" />
  </Step>
</Steps>

### Editing captions for Audio-to-video

If you uploaded an audio instead of typing a script, we use a different way to generate captions <u>since we don't have an original text to pull from</u>. As such, this method contains more error.

<Steps>
  <Step title="Preview the captions to see if there are typos">
    Depending on the
  </Step>

  <Step title="Click on the audio segment that has inaccurate captions">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/argil/Screenshot2025-01-02at15.53.10.png" alt="" />
  </Step>

  <Step title="Click on the word you wish to fix, correct it, then save">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/argil/Screenshot2025-01-02at15.54.34.png" alt="" />
  </Step>

  <Step title="Don't forget to re-generate captions!">
    Click on the 2 blue arrows that appeared to regenerate captions with the new text

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/argil/Screenshot2025-01-02at15.55.59.png" alt="" />
  </Step>
</Steps>

### Frequently asked questions

<AccordionGroup>
  <Accordion title="How do I fix a typo in captions?" defaultOpen="false">
    If the captions are not working, you're probably using a video input and our algorithm got the transcript wrong - just click "edit text" on the right segment, change the incorrect words, save, then re-generate captions.
  </Accordion>

  <Accordion title="Do captions work in any language?" defaultOpen="false">
    Yes, captions work in any language
  </Accordion>
</AccordionGroup>


# Contact Support & Community
Source: https://docs.argil.ai/resources/contactsupport

Get help from the support and the community here

<div data-tf-live="01JGXDX8VPGNCBWGMMQ75DDKPV" />

<div data-tf-live="01JGXDX8VPGNCBWGMMQ75DDKPV" />

<script src="//embed.typeform.com/next/embed.js" />

<script src="//embed.typeform.com/next/embed.js" />

<Card title="Send us an email" icon="inbox" color="purple" horizontal={200} href="mailto:support@argil.ai">
  Click on here to send us an email ([support@argil.ai](mailto:support@argil.ai))
</Card>

<Card title="Join our community on Discord!" icon="robot" color="purple" horizontal={200} href="https://discord.gg/E4E3WFVzTw">
  Learn from our hundreds of other users and use cases
</Card>


# Create an avatar from scratch
Source: https://docs.argil.ai/resources/create-an-avatar

There are two ways to create an avatar: a picture or a generation in the builder. Let's see the differences and how to create the two of them. We will also see how to pick your voice. 

<img src="https://mintcdn.com/argil/aljDgH83krSQCQxS/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8015.20.19.png?fit=max&auto=format&n=aljDgH83krSQCQxS&q=85&s=444cd30e8800bd69839830e30f3c916f" alt="Personal avatar VS AI influencer" data-og-width="824" width="824" data-og-height="654" height="654" data-path="images/Captured’écran2025-10-14à15.20.19.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/aljDgH83krSQCQxS/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8015.20.19.png?w=280&fit=max&auto=format&n=aljDgH83krSQCQxS&q=85&s=571a8f9ef412d5a5681d9b2b43434f2b 280w, https://mintcdn.com/argil/aljDgH83krSQCQxS/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8015.20.19.png?w=560&fit=max&auto=format&n=aljDgH83krSQCQxS&q=85&s=dc3d3f278f234573857f77b3c76935a1 560w, https://mintcdn.com/argil/aljDgH83krSQCQxS/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8015.20.19.png?w=840&fit=max&auto=format&n=aljDgH83krSQCQxS&q=85&s=2eb54831c4a3d107c4e77852191af39a 840w, https://mintcdn.com/argil/aljDgH83krSQCQxS/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8015.20.19.png?w=1100&fit=max&auto=format&n=aljDgH83krSQCQxS&q=85&s=f96900c9710ec9a7044a80fb74f78608 1100w, https://mintcdn.com/argil/aljDgH83krSQCQxS/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8015.20.19.png?w=1650&fit=max&auto=format&n=aljDgH83krSQCQxS&q=85&s=5e7035f48842318e9d9ae85e5d503400 1650w, https://mintcdn.com/argil/aljDgH83krSQCQxS/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8015.20.19.png?w=2500&fit=max&auto=format&n=aljDgH83krSQCQxS&q=85&s=b6117fbe3c65da59a3871e4df926c748 2500w" />

### Personal avatar VS AI influencer

A personal avatar is based on your own image or picture. An AI influencer is created using your own prompts. You can directly add images or products to your AI influencer whereas it comes in a second step for the personal avatar.

### How to create a great personal avatar?

The picture you should take of yourself needs to check the following boxes:

1. **Have great lighting (put yourself in front of a window)**

2. **Don't smile and if possible, have your mouth slitghtly opened like in the middle of a sentence**

3. **All of your face should be within the frame**

4. **The closer you are to the camera, the better the output will be**

<Tip>
  The pictures that work best are with a single human-like face. Avoid animals or multiple people on screen (even on posters).
</Tip>

### How to generate a great AI influencer?

To create an AI influencer, you have to take care of the avatar itself and then of the setup. Lastly, you'll be able to add products or clothes to your avatar.

**Appearance**\
You have three toggles to pick from (age, gender, ethnicity) and then it is all prompting. The more details you give, the better the output will be. Don't be afraid to give it 10 to 30 lines of prompt.

<img src="https://mintcdn.com/argil/dnk2g0B7n5WICRFW/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.45.48.png?fit=max&auto=format&n=dnk2g0B7n5WICRFW&q=85&s=70943ae785b88230d2de473574a35d76" alt="Captured’écran2025 10 14à17 45 48 Pn" data-og-width="678" width="678" data-og-height="466" height="466" data-path="images/Captured’écran2025-10-14à17.45.48.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/dnk2g0B7n5WICRFW/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.45.48.png?w=280&fit=max&auto=format&n=dnk2g0B7n5WICRFW&q=85&s=c4e87c3c96c3b2ee53d6a417e301b7c4 280w, https://mintcdn.com/argil/dnk2g0B7n5WICRFW/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.45.48.png?w=560&fit=max&auto=format&n=dnk2g0B7n5WICRFW&q=85&s=d921085d20f6d88e0edf424d168bb955 560w, https://mintcdn.com/argil/dnk2g0B7n5WICRFW/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.45.48.png?w=840&fit=max&auto=format&n=dnk2g0B7n5WICRFW&q=85&s=bcdd490918f6126f8156caa212835043 840w, https://mintcdn.com/argil/dnk2g0B7n5WICRFW/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.45.48.png?w=1100&fit=max&auto=format&n=dnk2g0B7n5WICRFW&q=85&s=347219f3451db7900e8bc9f504e504dd 1100w, https://mintcdn.com/argil/dnk2g0B7n5WICRFW/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.45.48.png?w=1650&fit=max&auto=format&n=dnk2g0B7n5WICRFW&q=85&s=ee58fe9ad473973891be34bb9b5bd2ef 1650w, https://mintcdn.com/argil/dnk2g0B7n5WICRFW/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.45.48.png?w=2500&fit=max&auto=format&n=dnk2g0B7n5WICRFW&q=85&s=3e61f73aaf9e8f9bbb06234e0736eb91 2500w" />

**Background**\
You have two toggles to pick from (camera angle and time of day) and then it is all prompting. The more details you give, the better the output will be. Don't be afraid to give it 10 to 30 lines of prompt.

<img src="https://mintcdn.com/argil/7gDn7rrSfU6wHIeu/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.45.56.png?fit=max&auto=format&n=7gDn7rrSfU6wHIeu&q=85&s=8d6de04fe2d15f20e84b7f8b0d5f3e64" alt="Captured’écran2025 10 14à17 45 56 Pn" data-og-width="654" width="654" data-og-height="504" height="504" data-path="images/Captured’écran2025-10-14à17.45.56.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/7gDn7rrSfU6wHIeu/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.45.56.png?w=280&fit=max&auto=format&n=7gDn7rrSfU6wHIeu&q=85&s=a45eab722717785e0a4aedbf530b16a2 280w, https://mintcdn.com/argil/7gDn7rrSfU6wHIeu/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.45.56.png?w=560&fit=max&auto=format&n=7gDn7rrSfU6wHIeu&q=85&s=e472549bcdb3296a2d47ee5b49b41f7b 560w, https://mintcdn.com/argil/7gDn7rrSfU6wHIeu/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.45.56.png?w=840&fit=max&auto=format&n=7gDn7rrSfU6wHIeu&q=85&s=71a6333b5bf866aa538927fc0204fdd2 840w, https://mintcdn.com/argil/7gDn7rrSfU6wHIeu/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.45.56.png?w=1100&fit=max&auto=format&n=7gDn7rrSfU6wHIeu&q=85&s=00029cbfb7550998169e1be2840db80a 1100w, https://mintcdn.com/argil/7gDn7rrSfU6wHIeu/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.45.56.png?w=1650&fit=max&auto=format&n=7gDn7rrSfU6wHIeu&q=85&s=678bd5c3a0c9dc6a8c6edf1d42895c02 1650w, https://mintcdn.com/argil/7gDn7rrSfU6wHIeu/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.45.56.png?w=2500&fit=max&auto=format&n=7gDn7rrSfU6wHIeu&q=85&s=ea78d9d0edb476c22390c5431b9106ba 2500w" />

**Assets: products, logos and clothes**\
Here you can drop images of clothes, logos or products you want in the frame with your avatar. Be aware that you can always create an avatar without anything and add more styles later with the objects of your choice. \
Without prompting, we'll go with what seems to make the most sense. A bottle will be held by the avatar. But you can prompt it to define where the assets are located.

\
<u>Example:</u>\
You drop an image of a sweater as well as logo. The prompt can be "make that person wear the sweater and put the logo on the sweater".

<img src="https://mintcdn.com/argil/dnk2g0B7n5WICRFW/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.48.36.png?fit=max&auto=format&n=dnk2g0B7n5WICRFW&q=85&s=027ae974a8c7ec3cce2897513b981a66" alt="Captured’écran2025 10 14à17 48 36 Pn" data-og-width="684" width="684" data-og-height="392" height="392" data-path="images/Captured’écran2025-10-14à17.48.36.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/dnk2g0B7n5WICRFW/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.48.36.png?w=280&fit=max&auto=format&n=dnk2g0B7n5WICRFW&q=85&s=63d13c47363782987f6055f7f2426984 280w, https://mintcdn.com/argil/dnk2g0B7n5WICRFW/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.48.36.png?w=560&fit=max&auto=format&n=dnk2g0B7n5WICRFW&q=85&s=3d3c5db079f577e313dab06beacd82da 560w, https://mintcdn.com/argil/dnk2g0B7n5WICRFW/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.48.36.png?w=840&fit=max&auto=format&n=dnk2g0B7n5WICRFW&q=85&s=7ad7982c250ca5da3bd16aa35402a30d 840w, https://mintcdn.com/argil/dnk2g0B7n5WICRFW/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.48.36.png?w=1100&fit=max&auto=format&n=dnk2g0B7n5WICRFW&q=85&s=5b8d128c17a2e6fd7936eb92ff77275c 1100w, https://mintcdn.com/argil/dnk2g0B7n5WICRFW/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.48.36.png?w=1650&fit=max&auto=format&n=dnk2g0B7n5WICRFW&q=85&s=88029daac113a3ff6dfac8aff71bfbd1 1650w, https://mintcdn.com/argil/dnk2g0B7n5WICRFW/images/Captured%E2%80%99e%CC%81cran2025-10-14a%CC%8017.48.36.png?w=2500&fit=max&auto=format&n=dnk2g0B7n5WICRFW&q=85&s=a41c3ac971f2d6685a9d19bd766761a3 2500w" />


# Creating avatar styles
Source: https://docs.argil.ai/resources/create-avatar-styles

What does it mean to add styles and how to add styles to your avatar

### What is a style?

Styles are keeping your face appearance while putting you in different environments, actions, or clothes. You can full prompt the style you want for your avatar. Each time you upload an image, we offer you a range of avatar styles you can pick from.

<Tip>
  You can edit any style, like the color of a shirt or a hair cut. [Learn how here.](https://docs.argil.ai/resources/edit-avatar-styles)
</Tip>

### How to create a style?

When you are in the avatar tab, you can either hover over avatar cards and click on "New style" or click on the avatar image and then click on "New syle".

Then you will be able to describe in full where you want to be standing, what you are wearing, the light, etc.

Last step is to pick whether you want a vertical avatar or a horizontal one.

<Expandable title="Example of prompt">
  "is in a crowded restaurant, with a formal suit. The light is a bit dark. We can see from the chest to the head, hands are visible."
</Expandable>

### How to use "Vary "and "Use settings"?

<img src="https://mintcdn.com/argil/YEO4oKxniKA5ClEl/images/Captured%E2%80%99e%CC%81cran2025-10-15a%CC%8014.50.15.png?fit=max&auto=format&n=YEO4oKxniKA5ClEl&q=85&s=d43ff6d1fbb5a1ac06202a4781083fb9" alt="Captured’écran2025 10 15à14 50 15 Pn" data-og-width="968" width="968" data-og-height="98" height="98" data-path="images/Captured’écran2025-10-15à14.50.15.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/YEO4oKxniKA5ClEl/images/Captured%E2%80%99e%CC%81cran2025-10-15a%CC%8014.50.15.png?w=280&fit=max&auto=format&n=YEO4oKxniKA5ClEl&q=85&s=00d3885d90174741196d6f64cf1d6638 280w, https://mintcdn.com/argil/YEO4oKxniKA5ClEl/images/Captured%E2%80%99e%CC%81cran2025-10-15a%CC%8014.50.15.png?w=560&fit=max&auto=format&n=YEO4oKxniKA5ClEl&q=85&s=908d1d2b6ded8341180380505d6e9c14 560w, https://mintcdn.com/argil/YEO4oKxniKA5ClEl/images/Captured%E2%80%99e%CC%81cran2025-10-15a%CC%8014.50.15.png?w=840&fit=max&auto=format&n=YEO4oKxniKA5ClEl&q=85&s=9b28c5389620f49120378e74a7ff4a66 840w, https://mintcdn.com/argil/YEO4oKxniKA5ClEl/images/Captured%E2%80%99e%CC%81cran2025-10-15a%CC%8014.50.15.png?w=1100&fit=max&auto=format&n=YEO4oKxniKA5ClEl&q=85&s=7e74481795d817c0f6dbde43bd6627e8 1100w, https://mintcdn.com/argil/YEO4oKxniKA5ClEl/images/Captured%E2%80%99e%CC%81cran2025-10-15a%CC%8014.50.15.png?w=1650&fit=max&auto=format&n=YEO4oKxniKA5ClEl&q=85&s=c9ebcc22b4c8aeee19625e440ef82e97 1650w, https://mintcdn.com/argil/YEO4oKxniKA5ClEl/images/Captured%E2%80%99e%CC%81cran2025-10-15a%CC%8014.50.15.png?w=2500&fit=max&auto=format&n=YEO4oKxniKA5ClEl&q=85&s=ce0c542117ee594bf9e74d42e80fbe0a 2500w" />

Once you get a result, you can click on "Vary" to obtain a slightly different version of the image you obtained.

Once you have created a range of styles that appear on the history on the right, you can pick any of them and get the description your wrote by clicking on "Use settings".


# Deleting your account
Source: https://docs.argil.ai/resources/delete-account

How to delete your account

<Warning>
  Deleting your account will delete **all projects, videos, drafts, and avatars you have trained**. If you create a new account, you will have to **use up a new avatar training** to train every avatar.
</Warning>

If you are 100% sure that you want to delete your account and never come back to your avatars & videos in the future, please contact us at [support@argil.ai](mailto:support@argil.ai) and mention your account email address. We will delete it in the next 720 days.


# Edit the style of your avatar
Source: https://docs.argil.ai/resources/edit-avatar-styles

How to create different styles and variations for your avatar

### What does "Edit style" do?

Variations allow you to add any product to your avatar or simply edit any aspect of the picture, whether it is the color of a shirt, the position of the hands or the background.

<u>Major benefits:</u>

* if you have created a style your are 95% satisfied with, you can still edit it later within Argil
* you can develop a whole branding easily around your avatar

**In the "Avatars" tab section, you can click on any avatar > click on "Edit style".**

Then you can add your instructions to operate slight variations of your avatar like these:

<Check>
  Examples:

  "change the color of this car to red", "zoom out on this picture", "change the haircut to a ponytail".
</Check>


# Editing tips
Source: https://docs.argil.ai/resources/editingtips

Some tips regarding a good editing and improving the quality of the video results

Editing will transform a boring video into a really engaging one. Thankfully, you can use our many features to **very quickly** make a video more engaging.

<Tip>
  Cutting your sentences in 2 paragraphs and playing with zooms & B-rolls is the easiest way to add dynamism to your video - and increase engagement metrics
</Tip>

### Use zooms wisely

Zooms add heavy emphasis to anything you say. We <u>advise to cut your sentences in 2 to add zooms</u>. Think of it as the video version of adding underlining or bold to a part of your sentence to make it more impactful.

Instead of this:

```
And at the end of his conquest, he was named king
```

Prefer a much more dynamic and heavy

```
And at the end of his conquest
[zoom in] He was named king
```

### Make shorter clips

In the TikTok era, we are used to dynamic editing - an avatar speaking for 20 seconds with nothing else on screen will have the viewer bored.

Prefer <u>cutting your scripts in short sentences</u>, or even cutting the sentences in 2 to add a zoom, a camera angles or a B-roll.

### Add more B-rolls

B-rolls and media will enrich the purpose of your video - thankfully, <u>you don't need to prompt to add a B-roll</u> on Argil. Simply click the "shuffle" button to rotate until you find a good one.

<Note>
  B-rolls will take the length of the clip you append it to. If it is too long, toggle the "1/2" button on it to make it shorter
</Note>

<Card title="Use a &#x22;Pro voice&#x22;" icon="robot" color="purple" href="https://docs.argil.ai/resources/voices-and-provoices">
  To have a voice <u>that respects your tone and emotion</u>, we advise recording a "pro voice" and linking it to your avatar.
</Card>

<Card title="Record your voice instead of typing text" icon="volume" color="purple" horizontal={false} href="https://docs.argil.ai/resources/audio-and-voicetovoice">
  It is much easier to record your voice than to film yourself, and <u>voice to video gives the best results</u>. You can <u>transform your voice into any avatar's voice</u>, and our "AI cleanup" will remove background noises and echo.
</Card>

<Card title="Add music" icon="music" color="purple" horizontal={false} href="https://docs.argil.ai/resources/music">
  Music is the final touch of your masterpiece. It will add intensity and emotions to the message you convey.
</Card>


# Fictions - Veo 3 & Hailuo
Source: https://docs.argil.ai/resources/fictions

You can now create your own medias and videos with VEO3 or Hailuo directly integrated into Argil using your own avatars or Argil's licensed avatars. It also integrates Nano Banana.

\*\*Fictions allow you to fully prompt 8 second-clips using the latest AI video models with a frame of reference. It will also apply the voice you picked. \*\*

## **Video tutorial (text tutorial below)**

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/pfKuPcGov_w" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## How to create a Fiction video?

<Steps>
  <Step title="Select the Fictions menu">
        <img src="https://mintcdn.com/argil/9nM_cOQ-qGGd-4XH/images/Captured%E2%80%99e%CC%81cran2025-09-03a%CC%8017.01.32.png?fit=max&auto=format&n=9nM_cOQ-qGGd-4XH&q=85&s=4e9c1216acaf3e1202139fadfe43eb2d" alt="Captured’écran2025 09 03à17 01 32 Pn" data-og-width="662" width="662" data-og-height="311" height="311" data-path="images/Captured’écran2025-09-03à17.01.32.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/9nM_cOQ-qGGd-4XH/images/Captured%E2%80%99e%CC%81cran2025-09-03a%CC%8017.01.32.png?w=280&fit=max&auto=format&n=9nM_cOQ-qGGd-4XH&q=85&s=d3de342dd2d4689c015fe42f3197b4da 280w, https://mintcdn.com/argil/9nM_cOQ-qGGd-4XH/images/Captured%E2%80%99e%CC%81cran2025-09-03a%CC%8017.01.32.png?w=560&fit=max&auto=format&n=9nM_cOQ-qGGd-4XH&q=85&s=212648a201e4a4d21dda215052b5f613 560w, https://mintcdn.com/argil/9nM_cOQ-qGGd-4XH/images/Captured%E2%80%99e%CC%81cran2025-09-03a%CC%8017.01.32.png?w=840&fit=max&auto=format&n=9nM_cOQ-qGGd-4XH&q=85&s=a4f1c07a3659e6ad247e8d4b6fbafbc6 840w, https://mintcdn.com/argil/9nM_cOQ-qGGd-4XH/images/Captured%E2%80%99e%CC%81cran2025-09-03a%CC%8017.01.32.png?w=1100&fit=max&auto=format&n=9nM_cOQ-qGGd-4XH&q=85&s=d91f215d3df10a356ec1a0f0f41590a8 1100w, https://mintcdn.com/argil/9nM_cOQ-qGGd-4XH/images/Captured%E2%80%99e%CC%81cran2025-09-03a%CC%8017.01.32.png?w=1650&fit=max&auto=format&n=9nM_cOQ-qGGd-4XH&q=85&s=b4bbb6ffa92fbfb83025ab4df8201c8b 1650w, https://mintcdn.com/argil/9nM_cOQ-qGGd-4XH/images/Captured%E2%80%99e%CC%81cran2025-09-03a%CC%8017.01.32.png?w=2500&fit=max&auto=format&n=9nM_cOQ-qGGd-4XH&q=85&s=4df8e7b5e01db2626566ded8ea8e4d72 2500w" />
  </Step>

  <Step title="Upload your image or pick an avatar from the list">
    You can put in any picture of your choice or pick from the list of avatars from the platform (your own or Argil's). We will keep the different characteristics of the face being sent so you can be sure the ressemblance stays here!

        <img src="https://mintcdn.com/argil/_UxAuUsDhcKhuPsl/images/Captured%E2%80%99e%CC%81cran2025-09-03a%CC%8017.08.59.png?fit=max&auto=format&n=_UxAuUsDhcKhuPsl&q=85&s=ef014b6906126cef91495b38bed8124a" alt="Captured’écran2025 09 03à17 08 59 Pn" data-og-width="516" width="516" data-og-height="76" height="76" data-path="images/Captured’écran2025-09-03à17.08.59.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/_UxAuUsDhcKhuPsl/images/Captured%E2%80%99e%CC%81cran2025-09-03a%CC%8017.08.59.png?w=280&fit=max&auto=format&n=_UxAuUsDhcKhuPsl&q=85&s=fcf1c65c9cad3efcd9a2f34aa9d17a0e 280w, https://mintcdn.com/argil/_UxAuUsDhcKhuPsl/images/Captured%E2%80%99e%CC%81cran2025-09-03a%CC%8017.08.59.png?w=560&fit=max&auto=format&n=_UxAuUsDhcKhuPsl&q=85&s=67fec0d09bcfdfa4feae579e11797f9d 560w, https://mintcdn.com/argil/_UxAuUsDhcKhuPsl/images/Captured%E2%80%99e%CC%81cran2025-09-03a%CC%8017.08.59.png?w=840&fit=max&auto=format&n=_UxAuUsDhcKhuPsl&q=85&s=895019e3274807023066368ab13ec29a 840w, https://mintcdn.com/argil/_UxAuUsDhcKhuPsl/images/Captured%E2%80%99e%CC%81cran2025-09-03a%CC%8017.08.59.png?w=1100&fit=max&auto=format&n=_UxAuUsDhcKhuPsl&q=85&s=b07679a5d3f6df80fc6ccc959f400aa3 1100w, https://mintcdn.com/argil/_UxAuUsDhcKhuPsl/images/Captured%E2%80%99e%CC%81cran2025-09-03a%CC%8017.08.59.png?w=1650&fit=max&auto=format&n=_UxAuUsDhcKhuPsl&q=85&s=a6168637a60053edb57fd561ffa1c8a8 1650w, https://mintcdn.com/argil/_UxAuUsDhcKhuPsl/images/Captured%E2%80%99e%CC%81cran2025-09-03a%CC%8017.08.59.png?w=2500&fit=max&auto=format&n=_UxAuUsDhcKhuPsl&q=85&s=1191c2aef526e6164200de0b296564a0 2500w" />
  </Step>

  <Step title="Add your outfit and product">
    Using Nano Banana, you can now also add a picture of an outfit or an item. If you are starting from an existing frame, only the outfit will be changed.\
    You can add indications in the prompt on how to hold the item.
  </Step>

  <Step title="Change the settings">
    **Model**: You can pick between Veo3 Fast and Normal. Fast works perfectly fine for simple scenes. For scenes with a lot of people, a lot of cuts going on, Normal will work best.\
    **Sound on:** decide if you want to receive a video with sound\
    **Selected voice for this video:** if you want your avatar to keep the same voice as usual, pick the voice from the platform. Otherwise, you can delete the voice and let Veo3 pick the voice. \
    \
    <u>No matter your choice, we will always keep the sound effects.</u>
  </Step>

  <Step title="Prompt your scene (example at the bottom)">
    Regarding the prompting, you can always do a one-liner. \
    What we advise you to do is give indications for the following: \
    **Advised indications:** Subject, Setting, Actions, Camera and Audio.  \
    **Bonus indications:** lighting and constraints

    The more precise your prompt is, the more likely it is to look as you want.

    <Tip>
      No need to refer to the image you are using. You can just write the man or the woman (avoid using real names except for scripts and writings on items)
    </Tip>
  </Step>

  <Step title="Re-use a prompt and the first frame">
    Once a video is generated, hover your mouse over it to see the "Remix" button. It will allow you to reuse the same prompting, same voices and same first frame (that you can decide to delete to start from scratch).
  </Step>
</Steps>

## How to store and reuse those videos?

Each video is automatically stored in the "Assets" section of Argil. They can be used in any video project created on the platform later on using the "play video" icon like shown below.

<img src="https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-08-20a%CC%8000.29.33.png?fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=982efbafc416c35e9f8c3be934b9d721" alt="Captured’écran2025 08 20à00 29 33 Pn" data-og-width="738" width="738" data-og-height="172" height="172" data-path="images/Captured’écran2025-08-20à00.29.33.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-08-20a%CC%8000.29.33.png?w=280&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=5e74a1b61a508171df261369dc38751c 280w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-08-20a%CC%8000.29.33.png?w=560&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=399b056c52c26173d846fdcc4eea84e6 560w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-08-20a%CC%8000.29.33.png?w=840&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=2df07627f12183e266a7e8ddbb021535 840w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-08-20a%CC%8000.29.33.png?w=1100&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=10bb2123c85369f67c4d211d87c3682c 1100w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-08-20a%CC%8000.29.33.png?w=1650&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=3d796886716d34d24fc1555ce7a2715d 1650w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-08-20a%CC%8000.29.33.png?w=2500&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=3a1db06f9fb50e4bd6b323e18ae5331e 2500w" />

<Tip>
  If you want to reuse those shots in your avatar videos, they will appear in the "assets" tab and saty available in the studio when uploading files.
</Tip>

## Prompt examples

<Accordion title="Prompt example 1" icon="sparkles">
  Subject: Person in obvious cardboard robot costume with "HUMAN" written on chest

  Setting: Futuristic-looking room with LED lights and screens

  Action: Robot-walking stiffly, says in monotone: "As a totally real human, I can confirm Argil is... suspiciously good"

  Style/Genre: Absurdist comedy, intentionally bad acting

  Camera/Composition: Static shot, slightly low angle for dramatic effect

  Lighting/Mood: Dramatic blue and purple sci-fi lighting

  Audio: Mechanical voice filter, robotic sound effects, computer beeps

  Constraints: Obviously fake robot movements, cardboard clearly visible (no subtitles)
</Accordion>

<Accordion title="Prompt example 2" icon="sparkles">
  Subject: Skilled anime warrior with spiky hair and determined expression, holding katana

  Setting: Japanese dojo courtyard with cherry blossoms falling, golden hour

  Action: Sprint-attacking multiple masked opponents, fluid sword movements, acrobatic jumps while shouting: "Through Anime, we explore worlds that reality simply cannot contain!"

  Style/Genre: High-energy shounen anime, Dragon Ball Z inspired

  Camera/Composition: Fast-paced camera work, dramatic angles, slow-motion sword strikes

  Lighting/Mood: Dynamic lighting with anime-style energy auras and impact flashes

  Audio:  sword clashing

  Constraints: Exaggerated anime physics, speed lines, energy effects (no subtitles)
</Accordion>

<Accordion title="Prompt example 3" icon="sparkles">
  An intense tracking close-up follows a rugged military captain as he strides down a narrow, dimly lit corridor inside a present-day battleship. The camera stays tight on his face and upper torso, capturing every subtle twitch of tension. He's on his phone, jaw tight, eyes scanning the space ahead as flickering emergency lights strobe across his features.

  "We need to figure out what the hell is going on, I think it's time to initiate project X" he says, his voice low and urgent, cutting through the ambient hum. Echoing footsteps and distant alarms punctuate the silence, while a faint, tense score builds beneath. The corridor is slick with shadows and gleaming metal, casting realistic reflections and hard edges. The visual style is cinematic realism—gritty and grounded—enhanced by subtle motion blur, soft lens flares from overhead fluorescents, and rich depth of field that isolates the captain from the blurred chaos behind him. The mood is taut and foreboding, every frame steeped in urgency.
</Accordion>


# Getting started with Argil
Source: https://docs.argil.ai/resources/introduction

Here's how to start leveraging video avatars to reach your goals

Welcome to Argil! Argil is your content creator sidekick that uses AI avatars to generate engaging videos in a few clicks.

<Note>
  For high-volume API licenses, please pick a [call slot here](https://calendly.com/laodis-argil/15min) - otherwise check the [API pricings here](https://docs.argil.ai/resources/api-pricings)
</Note>

## Getting Started

<Card title="Create your account" icon="user" color="purple" href="https://app.argil.ai/">
  Create a free account to start generating AI videos
</Card>

<Card title="Watch this full video tutorial to get the best out of Argil" icon="clapperboard-play" color="#9e0983" href="https://youtu.be/raWKq7SwD6k?si=bBUYMDpKst9lVtSg" />

## Setup Your Account

<CardGroup cols={2}>
  <Card title="Sign up and sign in" icon="user-plus" color="purple" href="/resources/sign-up-sign-in">
    Create your account and sign in to access all features
  </Card>

  <Card title="Choose your plan" icon="credit-card" color="purple" href="/resources/subscription-and-plans">
    Select a subscription plan that fits your needs
  </Card>
</CardGroup>

## Create Your First Video

<CardGroup cols={2}>
  <Card title="Create a video" icon="video" color="purple" href="/resources/create-a-video">
    Start creating your first AI-powered video
  </Card>

  <Card title="Write your script" icon="pen" color="purple" href="/resources/create-a-video#writing-script">
    Create your first text script for the video
  </Card>

  <Card title="Record your voice" icon="microphone" color="purple" href="/resources/audio-and-voicetovoice">
    Record and transform your voice into any avatar's voice
  </Card>

  <Card title="Production settings" icon="sliders" color="purple" href="/resources/create-a-video#production-settings">
    Configure your video production settings
  </Card>

  <Card title="Use templates" icon="copy" color="purple" href="/resources/article-to-video">
    Generate a video quickly by pasting an article link
  </Card>
</CardGroup>

## Control Your Avatar

<CardGroup cols={2}>
  <Card title="Body language" icon="person-walking" color="purple" href="/resources/body-language">
    Add natural movements and gestures to your avatar
  </Card>

  <Card title="Camera control" icon="camera" color="purple" href="/resources/cameras-angles">
    Master camera angles and zoom effects
  </Card>
</CardGroup>

## Make Your Video Dynamic

<CardGroup cols={2}>
  <Card title="Add media" icon="photo-film" color="purple" href="/resources/brolls">
    Enhance your video with B-rolls and media
  </Card>

  <Card title="Add captions" icon="closed-captioning" color="purple" href="/resources/captions">
    Make your content accessible with captions
  </Card>

  <Card title="Add music" icon="music" color="purple" href="/resources/music">
    Set the mood with background music
  </Card>

  <Card title="Editing tips" icon="wand-magic-sparkles" color="purple" href="/resources/editingtips">
    Learn pro editing techniques
  </Card>
</CardGroup>

## Train Your Avatar

<CardGroup cols={2}>
  <Card title="Create avatar" icon="user-plus" color="purple" href="/resources/create-avatar-from-image">
    Create a custom avatar from scratch
  </Card>

  <Card title="Training tips" icon="graduation-cap" color="purple" href="/resources/training-tips">
    Learn best practices for avatar training
  </Card>

  <Card title="Style & camera" icon="camera-retro" color="purple" href="/resources/styles-and-cameras">
    Add custom styles and camera angles
  </Card>

  <Card title="Body language" icon="person-rays" color="purple" href="/resources/create-body-language">
    Add expressive movements to your avatar
  </Card>

  <Card title="Voice setup" icon="microphone-lines" color="purple" href="/resources/link-a-voice">
    Link and customize your avatar's voice
  </Card>
</CardGroup>

## Manage Your Account

<CardGroup cols={2}>
  <Card title="Account settings" icon="gear" color="purple" href="/resources/account-settings">
    Configure your account preferences
  </Card>

  <Card title="Affiliate program" icon="handshake" color="purple" href="/resources/affiliates">
    Join our affiliate program
  </Card>
</CardGroup>

## Developers

<Card title="API Documentation" icon="code" color="purple" href="/resources/api-pricings">
  Access our API documentation and pricing
</Card>


# Media and avatar layouts (positioning)
Source: https://docs.argil.ai/resources/layouts

How to use split screen and different avatar positionnings

Create more engaging social media video with our magic editor that let's you switch between:

* Full screen avatar: takes up the whole screen, no media in front
* Small avatar: puts your avatar in small in one of the 4 corners of the frame with media behind
* Splitscreen: puts your avatar on the top/bottom half (9:16 ratio) or right/left half (16:9 ratio)
* Back avatar: the avatar isn't visible anymore, the media is in front in full screen

### How to use layouts?

<Steps>
  <Step title="Pick the layout in the options">
    After picking your avatar, enable the B-rolls and pick the layout option you like.

    <Info>
      Picking "Auto" will put a mix of different settings.
    </Info>

        <img src="https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-06-18a%CC%8014.23.28.png?fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=f326b0207ed2339885298782d160302b" alt="Captured’écran2025 06 18à14 23 28 Pn" data-og-width="400" width="400" data-og-height="420" height="420" data-path="images/Captured’écran2025-06-18à14.23.28.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-06-18a%CC%8014.23.28.png?w=280&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=b18eb4aa31fed8fa1fa925fbada706c2 280w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-06-18a%CC%8014.23.28.png?w=560&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=336c40730c83725fb98cff08862ccac4 560w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-06-18a%CC%8014.23.28.png?w=840&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=a8db727ccf4d4439aa923b62c5b4b5b5 840w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-06-18a%CC%8014.23.28.png?w=1100&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=dfbe821cf5981c7a1a5a27ff674c2c3c 1100w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-06-18a%CC%8014.23.28.png?w=1650&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=0a9cf8935a01eb54641a705b50c20379 1650w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-06-18a%CC%8014.23.28.png?w=2500&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=c25e97804639d5e6bdee972712f6e2c1 2500w" />
  </Step>

  <Step title="In the studio editor, edit each individual media layout">
    You can click on any media and change the independant settings for each of them. Then if you want to apply that change to all your medias, click on "apply to all medias".

        <img src="https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-06-18a%CC%8014.24.30.png?fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=f5bb7172dec53795feb9476e8b097f68" alt="Captured’écran2025 06 18à14 24 30 Pn" data-og-width="372" width="372" data-og-height="760" height="760" data-path="images/Captured’écran2025-06-18à14.24.30.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-06-18a%CC%8014.24.30.png?w=280&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=44858089a7f68c67794c3288e2c2309e 280w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-06-18a%CC%8014.24.30.png?w=560&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=624e86a41b9a8a7287e4376e5b3cd000 560w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-06-18a%CC%8014.24.30.png?w=840&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=c3619a7901be7b9047e7a69f1065cb67 840w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-06-18a%CC%8014.24.30.png?w=1100&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=cb2c8172296ae7c2521f85f4978f62d9 1100w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-06-18a%CC%8014.24.30.png?w=1650&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=30452fda31b83cdff47917dee1e77809 1650w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-06-18a%CC%8014.24.30.png?w=2500&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=53459dd441638f9ee20d6aa8a45fad56 2500w" />
  </Step>
</Steps>


# Link a new voice to your avatar
Source: https://docs.argil.ai/resources/link-a-voice

Change the default voice of your avatar

<Steps>
  <Step title="Access avatar settings">
    Click on your avatar to open styles panel
  </Step>

  <Step title="Open individual settings">
    Click again to access individual avatar settings
  </Step>

  <Step title="Change voice">
    Under the name section, locate and modify "linked voice"
  </Step>
</Steps>

<Card title="Learn More About Voices" icon="microphone" href="/resources/voices-and-provoices" style={{width: "200px", color: "#741FFF", display: "flex", alignItems: "center"}}>
  Discover voice settings and pro voices
</Card>


# Create a Make automation with Argil
Source: https://docs.argil.ai/resources/make-automation

Step by step tutorial on Make

<Card title="Access our documentation" href="https://argilai.notion.site/Argil-x-Make-1a312e820a1f80d6a023c6105a40439c?pvs=4">
  All you need to know about creating a Make to Argil connexion
</Card>


# Managing Your Subscription
Source: https://docs.argil.ai/resources/manage-plan

How to upgrade, downgrade and cancel your subscription

### How to upgrade?

<Steps>
  <Step title="Open subscription settings">
    Navigate to the bottom left corner of your screen
  </Step>

  <Step title="Upgrade your plan">
    Click the "upgrade" button
  </Step>
</Steps>

### How to downgrade?

<Steps>
  <Step title="Access plan management">
    Click "manage plan" at the bottom left corner
  </Step>

  <Step title="Request management link">
    Click "Send email"
  </Step>

  <Step title="Open management page">
    Check your email and click the link you received
  </Step>

  <Step title="Update subscription">
    Click "Manage subscription" and select your new plan
  </Step>
</Steps>

### How to cancel?

1. Go to "My workspace" on the top left corner of your screen.
2. Go to "Settings"
3. Go to "Cancel"


# Moderated content
Source: https://docs.argil.ai/resources/moderated-content

Here are the current rules we apply to the content we moderate. 

<Info>
  Note that content restrictions only apply to Argil’s avatars. If you wish to generate content outside of our restrictions, please train your own avatar ([see how](https://docs.argil.ai/resources/training-tips))
</Info>

<Warning>
  Moderation from fiction is done by 3rd parties over which Argil has no control of. Videos generations which fails are automatically refunded.
</Warning>

On Argil, to protect our customers and to comply with our “safe synthetic content guidelines”, we prevent some content to be generated. There are 3 scenarios:

* Video generated with **your** avatar: no content is restricted
* Video generated with **Argil’s human avatars**: submitted to content restrictions (see below)

***

### Here’s an exhaustive list of content that is restricted:

You will not use the Platform to generate, upload, or share any content that is obscene, pornographic, offensive, hateful, violent, or otherwise objectionable, including but not limited to content that falls in the following categories:

### **Finance\***

* Anything that invites people to earn more money with a product or service described in the content (includes crypto and gambling).

**Banned:** Content is flagged when it makes unverified promises of financial gain, promotes get-rich-quick schemes, or markets financial products deceptively. Claims like "double your income overnight" or "risk-free investments" are explicitly prohibited.

**Allowed**: General discussions of financial products or markets that do not promote specific services or methods for profit. Describing the perks of a product (nice banking cards, easy user interface, etc.) not related to the ability to make more money.

### Illicit promotion\*

* Promotion of cryptocurrencies
* Promotion of gambling sites

**Banned:** Content is flagged when it encourages risky financial behavior, such as investing in cryptocurrencies without disclaimers or promoting gambling platforms. Misleading claims of easy profits or exaggerated benefits are also prohibited.

**Allowed**: General discussions of financial products or markets that do not promote specific services or methods for profit. Promoting the characteristics of your product (card

### Criminal / Illegal activies

* Pedo-criminality
* Promotion of illegal activities
* Human trafficking
* Drug use or abuse
* Malware or phishing

**Banned**: Content is banned when it provides explicit instructions, encourages, or normalizes illegal acts. For example, sharing methods for hacking, promoting drug sales, or justifying exploitation falls into this category. Any attempt to glorify such activities is strictly prohibited.

### Violence and harm

* Blood, gore, self harm
* Extreme violence, graphic violence, incitement to violence
* Terrorism

**Banned**: Content that portrays graphic depictions of physical harm, promotes violent behavior, or incites others to harm themselves or others is not allowed. This includes highly descriptive language or imagery that glorifies violence or presents it as a solution.

### Hate speech and discrimination

* Racism, sexism, misogyny, misandry, homophobia, transphobia
* Hate speech, defamation or slander
* Discrimination
* Explicit or offensive language

**Banned**: Hate speech is banned when it directly attacks or dehumanizes individuals or groups based on their identity. Content encouraging segregation, using slurs, or promoting ideologies of hate (e.g., white supremacy) is prohibited. Defamation targeting specific individuals also falls under this category.

### **Privacy and Intellectual Property**

* Intellectual property infringement
* Invasion of privacy

**Banned:** Content that encourages removing watermarks, using pirated software, or disclosing private information without consent is disallowed. This includes sharing unauthorized personal details or methods to bypass intellectual property protections.

### **Nudity and sexual content**

**Banned:** Sexual content is banned when it contains graphic descriptions of acts, uses explicit language, or is intended to arouse rather than inform or educate. Depictions of non-consensual or illegal sexual acts are strictly forbidden.

### **Harassment**

**Banned:** Harassment includes targeted attacks, threats, or content meant to humiliate an individual. Persistent, unwanted commentary or personal attacks against a specific person also fall under this banned category.

### **Misinformation** and fake news

**Banned:** Misinformation is flagged when it spreads false narratives as facts, especially on topics like health, science, or current events. Conspiracy theories or fabricated claims that could mislead or harm the audience are strictly not allowed.

### **Sensitive Political Topics**

**Banned:** Content is banned when it incites unrest, promotes illegal political actions, or glorifies controversial figures without nuance. Content that polarizes communities or compromises public safety through biased narratives is flagged.

**Allowed:** Balanced discussions on political issues, provided they are neutral, educational, and avoid inflammatory language.

**Why do we restrict content?**

We have very strong contracts in place with our actors that are used as Argil’s avatars.

If you think that a video has been wrongly flagged, please send an email to [support@argil.ai](mailto:support@argil.ai) (**and ideally include the transcript of said video**).

*Please note that Argil created a feature on the platform to automatically filter the generation of prohibited content, but this feature can be too strict and in some cases doesn’t work.*

### Users that violate these guidelines may see the immediate termination of their access to the Platform and a permanent ban from future use.

\*not moderated if you are using a fictional avatar


# Music
Source: https://docs.argil.ai/resources/music



Music is a great way to add more emotion to your video and is extremely simple to add.&#x20;

### How to add music&#x20;

<Steps>
  <Step title="Step 1">
    On the side bar, click on "None" under "Music"&#x20;

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/argil/Screenshot2025-01-02at11.40.38.png" alt="" />
  </Step>

  <Step title="Step 2">
    Preview musics by pressing the play button and setting the volume

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/argil/Screenshot2025-01-02at11.43.44.png" alt="" />
  </Step>

  <Step title="Step 3">
    When you found the perfect symphony for your video, click on it and click the "back" button to the main menu ; you can then preview the video with your Music&#x20;

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/argil/Screenshot2025-01-02at11.41.26.png" alt="" />
  </Step>
</Steps>

### Can I add my own music?

Not yet - we will be adding this feature shortly.&#x20;


# Pay-as-you-go credits explained
Source: https://docs.argil.ai/resources/pay-as-you-go-pricings

Prices for additional avatars (clones and influencers) and credits purchases 

<Tip>
  You can purchase as much Pay-as-you-go credits as you wish. **They never expire.**
</Tip>

<Card title="Purchase your additionnal credits here" href="https://app.argil.ai/?workspaceSettingsModalOpen=true" cta="Click here to access the shop">
  You can purchase as many pay-as-you-go credits as you wish. They never expire.
</Card>

### For videos:

| Feature                           | Unit      | Cost in credit |
| --------------------------------- | --------- | -------------- |
| Video (Atom model)\*              | 1 min     | 140            |
| Voice                             | 1 min     | 20             |
| B-roll images                     | 1 B-rolls | 10             |
| B-roll videos                     | 1 B-roll  | 20             |
| Royalties (Argil v1 avatars only) | 1 vidéos  | 20             |

If you do a 30 sec video with 2 video B-rolls with one of our licenced avatars that are NOT v1, you will pay:

40 (2 video B-rolls) + 10 (30sec of talking avatar) + 70 (30sec of Atom model) = 120 credits

\*For legacy users (before 20th of october 2025): Argil v1 costs 60 credits for 3 minutes


# Sign up & sign in
Source: https://docs.argil.ai/resources/sign-up-sign-in

Create and access your Argil account

### Getting Started

Choose your preferred sign-up method to create your Argil account.

<CardGroup cols="2">
  <Card title="Email Sign Up" icon="envelope">
    Create an account using your email address and password.
  </Card>

  <Card title="Google Sign Up" icon="google">
    Quick sign up using your Google account credentials.
  </Card>
</CardGroup>

### Create Your Account

<Steps>
  <Step title="Go to Argil">
    Visit [app.argil.ai](https://app.argil.ai) and click "Sign Up"
  </Step>

  <Step title="Choose Sign Up Method">
    Select "Email" or "Continue with Google"
  </Step>

  <Step title="Complete Registration">
    Enter your details or select your Google account
  </Step>

  <Step title="Verify Email">
    Click the verification link sent to your inbox
  </Step>
</Steps>

<Tip>
  Enterprise users can use SSO (Single Sign-On). Contact your organization admin for access.
</Tip>

### Sign In to Your Account

<Steps>
  <Step title="Access Sign In">
    Go to [app.argil.ai](https://app.argil.ai) and click "Sign In"
  </Step>

  <Step title="Enter Credentials">
    Use email/password or click "Continue with Google"
  </Step>
</Steps>

### Troubleshooting

<AccordionGroup>
  <Accordion title="Gmail Issues" defaultOpen={false}>
    * Check email validity

    * Verify permissions

    * Clear browser cache
  </Accordion>

  <Accordion title="Password Reset" defaultOpen={false}>
    Click "Forgot Password?" and follow email instructions
  </Accordion>

  <Accordion title="Account Verification" defaultOpen={false}>
    Check spam folder or click "Resend Verification Email"
  </Accordion>
</AccordionGroup>

<Warning>
  Never share your login credentials. Always sign out on shared devices.
</Warning>

### Need Support?

Contact us through [support@argil.ai](mailto:support@argil.ai) or join our [Discord](https://discord.gg/CnqyRA3bHg)


# Plans
Source: https://docs.argil.ai/resources/subscription-and-plans

What are the different plans available, how to upgrade, downgrade and cancel a subscription.

<Note>
  Choose the plan that best fits your needs. You can upgrade or downgrade at any time.
</Note>

## Available Plans

<CardGroup cols={2}>
  <Card title="Classic Plan - $39/month" href="https://app.argil.ai">
    1,500 credits per month

    * 10 avatar styles
    * \
      100+ Argil avatars
    * Magic editing\
      Fictions playground (Veo3, Hailuo,...)
    * API access
  </Card>

  <Card title="Pro Plan - $149/month" href="https://app.argil.ai">
    6,000 minutes per month

    * Unlimited Avatar styles
    * Style editing
    *
    * All classic features
    * Fast generation
  </Card>

  <Card title="Scale Plan - $499/month" horizontal={false} href="app.argil.ai">
    ### 6,000 minutes per month

    * Unlimited Avatar styles
    * 3 workspace seats included
    *
    * All classic and pro features
    * Fastest support
    * Priority support
  </Card>

  <Card title="Entreprise plan - 1000$+/month" href="mailto:entreprise@argil.ai">
    ### Early access to features and models

    * Unlimited video minutes
    * Unlimited avatar trainings
    * Custom avatar development
    * Dedicated support team
    * Custom integrations
    * **Talk to us for pricing**
  </Card>
</CardGroup>

### How to buy more training credits as well as video credits?

You can purchase more credits by clicking on the bottom left of your screen "Upgrade" or "Get more". That window will pop up where you can purchase your extra credits.

### <img src="https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-04-24a%CC%8014.10.51.png?fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=05d05dd8fdb5b871aaf60585710cd70f" alt="Captured’écran2025 04 24à14 10 51 Pn" data-og-width="1529" width="1529" data-og-height="754" height="754" data-path="images/Captured’écran2025-04-24à14.10.51.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-04-24a%CC%8014.10.51.png?w=280&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=10d2134be6e216c85045f06819a7af61 280w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-04-24a%CC%8014.10.51.png?w=560&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=bde01e6da28621af85b1e30f5a56043f 560w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-04-24a%CC%8014.10.51.png?w=840&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=4f726e285c70aaea069d0145a5cd9675 840w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-04-24a%CC%8014.10.51.png?w=1100&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=afd40c218d304752dcc37090e0c1ed16 1100w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-04-24a%CC%8014.10.51.png?w=1650&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=e9ebf6caaf461472d9f7f2483674e89f 1650w, https://mintcdn.com/argil/-UAhf1yAWS2oQpVh/images/Captured%E2%80%99e%CC%81cran2025-04-24a%CC%8014.10.51.png?w=2500&fit=max&auto=format&n=-UAhf1yAWS2oQpVh&q=85&s=c222509662b5138713b03855c39eefe4 2500w" />

### Frequently Asked Questions

<AccordionGroup>
  <Accordion title="What happens when I upgrade my plan?" defaultOpen="false">
    When you upgrade to the Pro plan, you'll immediately get access to all the features included in the plan as well as a full top up of your credits. If you used all your classic credits and upgrade to pro, you will get back 6000 credits. Your billing will be adjusted according to the prorata. 
  </Accordion>

  <Accordion title="Can I switch plans at any time?" defaultOpen="false">
    Yes, you can upgrade or downgrade your plan at any time by going to your "Workspace" then "settings" and then "manage plan".
  </Accordion>

  <Accordion title="Will I lose my existing content when changing plans?" defaultOpen="false">
    No, your existing content will remain intact when changing plans. However, if you downgrade, you won't be able to create new content using Pro or Scale only features.
  </Accordion>
</AccordionGroup>


# Voice creation & Settings
Source: https://docs.argil.ai/resources/voices-and-provoices

Configure voice settings and set up pro voices for your avatars and learn about supported languages. 

## Voice creation from scratch

You can create any voice in the "voices" panel section > "+create voice" on the top right > upload 20 seconds to 5 minutes of audio.

<Tip>
  ### What is a good voice dataset?

  * no moments of silence
  * keep the tone and energy you would want your avatar to have, you can exagerate a little if needed
  * no hesitations, they will be replicated
  * be careful not to have outside noise or microphone crackles while you record
</Tip>

<iframe src="https://youtube.com/embed/Nd0xlSrzWOo" title="YouTube video player" frameborder="0" className="w-full aspect-video rounded-xl" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />

## Voice creation when creating an avatar

If you are creating an avatar, you will be presented with three options: - **select a voice :** which is from your own library, from the voices you already have

* **create my voice:** upload any audio file of yourself talking
* \*\*generate my voice: \*\*pick among three voices created for you according to the person we see on your image

<Tip>
  Don't hesitate to edit your voices in the "voices" section in order to increase the speed to 1.05 or 1.1. This can make all of your videos more entertaining.
</Tip>

## Elevenlabs instant and pro voices settings

<Note>
  If you use ElevenLabs for voice generation, don't hesitate to visit the [ElevenLabs documentation](https://elevenlabs.io/docs/speech-synthesis/voice-settings).
</Note>

<CardGroup cols="2">
  <Card title="Standard Voices" icon="microphone" color="purple">
    * Stability: 50-80
    * Similarity: 60-100
    * Style: Varies by voice tone
  </Card>

  <Card title="Pro Voices" icon="microphone-lines" color="purple">
    * Stability: 70-100
    * Similarity: 80-100
    * Style: Varies by voice tone
  </Card>
</CardGroup>

<Info>
  How to add pauses ? \
  To create pauses or hesitations in your script and voice, you can use the following:

  * Signs: "..." or "--"
</Info>

## Connect ElevenLabs

1. Add desired voices to your ElevenLabs account
2. Create an API key
3. Paste API key in "voices" > "ElevenLabs" on Argil
4. Click "synchronize" after adding new voices

<Card title="Link Your Voice" icon="link" color="purple" href="/resources/link-a-voice">
  Learn how to link voices to your avatar
</Card>

## Languages

We currently support about 30 different languages via Elevenlabs: English (USA), English (UK), English (Australia), English (Canada), Japanese, Chinese, German, Hindi, French (France), French (Canada), Korean, Portuguese (Brazil), Portuguese (Portugal), Italian, Spanish (Spain), Spanish (Mexico), Indonesian, Dutch, Turkish, Filipino, Polish, Swedish, Bulgarian, Romanian, Arabic (Saudi Arabia), Arabic (UAE), Czech, Greek, Finnish, Croatian, Malay, Slovak, Danish, Tamil, Ukrainian, Russian

[Click here to see the full list.  ](https://help.elevenlabs.io/hc/en-us/articles/13313366263441-What-languages-do-you-support)

## Create Pro Voice

Pro voices offer hyper-realistic voice cloning for maximum authenticity. While you are limited to only 1 pro voice per elevenlabs account, you can connect multiple accounts to Argil.

1. Subscribe to ElevenLabs creator plan
2. Record 30 minutes of clean audio (no pauses/noise)
3. Create and paste API key in "voices" > "ElevenLabs"
4. Edit avatar to link your Pro voice

<Frame>
  <iframe src="https://www.loom.com/embed/f083b2f5b86f4971851d158009d60772?sid=bc9df527-2dba-45c1-bee7-dc81870770c7" frameBorder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowFullScreen style={{ width:"100%",height:"400px" }} />
</Frame>

<Card title="Voice Transformation" icon="wand-magic-sparkles" color="purple" href="/resources/audio-and-voicetovoice">
  Learn about voice transformation features
</Card>


