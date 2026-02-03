# Source: https://docs.argil.ai/pages/get-started/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

> Start automating your content creation workflow

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
