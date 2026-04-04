# Source: https://docs.tavus.io/sections/replica/replica-training.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Replica Training

> Guide to recording a high-quality training video for generating a high-quality Replica using the Phoenix model.

You can record the Replica training video directly in the <a href="https://platform.tavus.io/" target="_blank">Developer Portal</a> or upload a pre-recorded one via the <a href="/api-reference/phoenix-replica-model/create-replica" target="_blank">API</a>.

## Talking Head Replica

### Environment

* Record in a quiet, well-lit space with no background noise or movement.
* Use diffuse lighting to avoid shadows on your face.
* Choose a simple background and avoid any moving people or objects.

### Camera

* Place the camera at eye level and ensure your face fills at least 25% of the frame.
* Use a desktop recording app (e.g., **QuickTime** on Mac or **Camera** on Windows) — avoid browser-based tools.

### Microphone

* Use your device’s built-in microphone.
* **Avoid** high-end mics or wireless earbuds like AirPods.
* Turn off audio effects like noise suppression or EQ adjustments.

### Yourself

<Frame>
    <img src="https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/replica-training/charlie.png?fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=5280478561a274ea807c3cc05d3b0afa" alt="" data-og-width="2087" width="2087" data-og-height="1177" height="1177" data-path="images/replica-training/charlie.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/replica-training/charlie.png?w=280&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=b709ad30493b9b67974e1903c3a3dbb2 280w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/replica-training/charlie.png?w=560&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=501268d91b44dc95679371d6aca98fcc 560w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/replica-training/charlie.png?w=840&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=d3c2ed6bcb3343bb225f261580503763 840w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/replica-training/charlie.png?w=1100&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=47568cc946602aa0a9d3145e3e43234d 1100w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/replica-training/charlie.png?w=1650&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=5ed27beb35b1f06f673ba0ee4818b0d5 1650w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/replica-training/charlie.png?w=2500&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=9904491a85f775ce5f2cfa25f9e4520b 2500w" />
</Frame>

| ✅ Do                                                                                | ❌ Don’t                                                |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------ |
| Keep your full head visible, with a clear view of your face                         | Wear clothes that blend into the background            |
| Ensure your face and upper body are in sharp focus                                  | Wear accessories like hats, thick glasses, or earrings |
| If using smartphone, make sure you follow the same framing/distance from the camera | Turn your head away from the camera                    |
| Tuck back any hair covering your face                                               | Block your chin or mouth with your microphone          |
| Sit upright in a stable, seated position                                            | Stand or shift positions during the video              |

### Video Format

If you're uploading a pre-recorded training video via our <a href="/api-reference/phoenix-replica-model/create-replica" target="_blank">API</a>, ensure it meets the following requirements:

* **Minimum FPS**: 25 fps
* **Accepted formats**:
  * `webm`
  * `mp4` with **H.264** video codec and **AAC** audio codec
* **Maximum file size**: 750MB
* **Minimum resolution**: 1080p

### Consent Statement

If you're creating a **personal replica**, you must include a verbal consent statement in the video. This ensures ethical use and compliance with data protection laws.

**Steps**:

* Begin with a big smile and look directly into the camera for one second.
* Clearly read the following script:

> I, (your name), am currently speaking and give consent to Tavus to create an AI clone of me by using the audio and video samples I provide. I understand that this AI clone can be used to create videos that look and sound like me.

<Note>
  This step is **only required for personal replicas**. If you’re creating an **AI replica**, you can skip this video.
</Note>

## Recording Your Training Video

Your video must be **one continuous shot**, containing:

<Tip>
  **Pro tips**:

  * Keep body and head movements subtle
  * Avoid heavy hand gestures
  * Only one person should appear in the video
</Tip>

<Steps>
  <Step title="1 Minute of Talking">
    * Smile widely for at least 2 seconds.
    * Look directly at the camera, positioned just below eye level.
    * Speak casually, as if talking to a friend.
    * Pause briefly (close lips) every 1–2 sentences.
    * Minimize body movement.
    * Avoid hand gestures at all times.
    * Sample script:

    ```txt [expandable] theme={null}
    For the next 2 minutes, I’ll read you a story that will for sure make you smile and feel good. I will be relaxed and keep a happy face while reading. I will also read this story at a faster pace than I normally speak. I will close my lips fully after every sentence. I will read this script in a casual and conversational tone as if I am telling a story to my friend.

    The sun was shining brightly, casting a warm glow over the park as Emma, Jake, and Sophie spread out their picnic blanket. Now I will close my lips fully.

    Emma looked around, her face beaming with excitement. "Can you believe how perfect today is?" she exclaimed. "The sun is shining, and the weather is just right!" Her enthusiasm was contagious, and Jake couldn't help but smile as he laid back on the blanket, soaking in the sunlight. Now I will close my lips fully after this sentence.

    Jake nodded in agreement, a relaxed grin spreading across his face. "It really is," he said. "Days like this remind me why I love summer. I will close my lips fully after this sentence.

    Sophie, always the energetic one, jumped up from the blanket with a burst of excitement. "And we have the whole day to ourselves!" she declared. "So many possibilities. What should we do first? Fly a kite? Play frisbee? Go for a hike?" Her eyes sparkled. I will close my lips fully after this sentence. This is the last sentence I will read and then I will stand still to record my listening segment with minimal head and body movement as if I am listening to someone share a story.

    ```

    <Frame>
            <img src="https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/replica-training/image1.png?fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=2d681b2bb21ab3ec4cc1c40df63431fa" alt="" data-og-width="1826" width="1826" data-og-height="1067" height="1067" data-path="images/replica-training/image1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/replica-training/image1.png?w=280&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=c80676458909495355f740782fd746dc 280w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/replica-training/image1.png?w=560&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=c774ce7efc26156740c28c8a3602bbe7 560w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/replica-training/image1.png?w=840&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=27b4dab3bfecc96f2e9e4dd2c5b4a857 840w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/replica-training/image1.png?w=1100&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=bbac974783ce0fceeed9ba375f5c8bad 1100w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/replica-training/image1.png?w=1650&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=5abf6be4670c84c35c5e3c6f1b482db4 1650w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/replica-training/image1.png?w=2500&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=ef0736be92582f2a4e798d5a2d313705 2500w" />
    </Frame>
  </Step>

  <Step title="1 Minute of Silence">
    * Sit still with a relaxed, attentive posture.
    * Keep lips gently closed the entire time.
    * Slight, natural head movements (like you’re listening on a Zoom call).

    <Frame>
            <img src="https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/replica-training/image3.gif?s=30c7dff99d5de4d75b86f5837c870b5b" alt="" data-og-width="412" width="412" data-og-height="232" height="232" data-path="images/replica-training/image3.gif" data-optimize="true" data-opv="3" />
    </Frame>
  </Step>
</Steps>

<Note>
  Replica training typically takes **4–5 hours**. You can track the training progress by:

  * Providing a `callback_url` when creating the replica via API
  * Using the <a href="/api-reference/phoenix-replica-model/get-replica" target="_blank">**Get Replica Status**</a> API
  * Checking the <a href="https://platform.tavus.io/" target="_blank">Developer Portal</a>
</Note>

## High-Quality Training Example

<Frame>
  <iframe src="https://drive.google.com/file/d/1kXliTbzz9t-8FIyMDeOq8h6C1ZqDKiIu/preview" width="600" height="350" allow="autoplay" />
</Frame>

## Full Body Replica

To create a full body replica for conversational video, follow these guidelines:

<Frame>
    <img src="https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/image1.png?fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=cdfeb363f16d0aad8213a4315fed87e0" alt="" data-og-width="264" width="264" data-og-height="459" height="459" data-path="images/image1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/image1.png?w=280&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=b21a26324765af5909bbc00d554dcd2b 280w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/image1.png?w=560&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=ee84bc403e9b4354e608e1f5e6b6ab2b 560w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/image1.png?w=840&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=b8bc60cd518b0a535324e9e392641a53 840w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/image1.png?w=1100&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=cbbb342e4d5fd76e617f1370e6ef2700 1100w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/image1.png?w=1650&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=78456807c2ac4b1cdb8b52c1e4947c53 1650w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/image1.png?w=2500&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=d2a374f3461c6db3e2af2868e0a2cf80 2500w" />
</Frame>

### Framing & Orientation

* The subject must be captured **from head to toe**, with no extra space above or below.
* Record in **vertical format** (portrait mode) or crop appropriately to maintain vertical framing.

### Posture & Movement

* Remain **standing still** throughout the recording.
* **Avoid hand gestures** or exaggerated body movements to maintain consistency and model quality.

### Resolution & Quality

* A **4K resolution** is recommended for best results.
* Ensure consistent lighting, with no shadows or sudden changes in exposure.
