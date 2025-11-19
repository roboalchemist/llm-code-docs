# Source: https://docs.tavus.io/sections/conversational-video-interface/component-library/blocks.md

# Blocks

> High-level component compositions that combine multiple UI elements into complete interface layouts

### Conversation block

The Conversation component provides a complete video chat interface for one-to-one conversations with AI replicas

```bash  theme={null}
npx @tavus/cvi-ui@latest add conversation-01
```

<Tabs>
  <Tab title="Description">
    The `Conversation` component provides a complete video chat interface for one-to-one conversations with AI replicas, featuring main video display, self-view preview, and integrated controls.

    **Features:**

    * **Main Video Display**: Large video area showing the AI replica or screen share
    * **Self-View Preview**: Small preview window showing local camera feed
    * **Screen Sharing Support**: Automatic switching between replica video and screen share
    * **Device Controls**: Integrated microphone, camera, and screen share controls
    * **Error Handling**: Graceful handling of camera/microphone permission errors
    * **Responsive Layout**: Adaptive design for different screen sizes

    **Props:**

    * `conversationUrl` (string): Daily.co room URL for joining
    * `onLeave` (function): Callback when user leaves the conversation
  </Tab>

  <Tab title="Code">
    ```tsx  theme={null}
    import { Conversation } from './components/cvi/components/conversation';
    ```

    ```tsx  theme={null}
    <Conversation
      conversationUrl={conversationUrl}
      onLeave={() => handleLeaveCall()}
    />
    ```
  </Tab>
</Tabs>

Preview

<Frame>
    <img src="https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/conversation_01_preview.png?fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=6044bc06c6284980b25ba241e8170e8a" alt="Conversation Block Preview" data-og-width="2260" width="2260" data-og-height="1402" height="1402" data-path="images/conversation_01_preview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/conversation_01_preview.png?w=280&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=5c1ad75844fa252801adbba8a3dc1f64 280w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/conversation_01_preview.png?w=560&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=367e8980b33b20b65a387212b693ed6e 560w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/conversation_01_preview.png?w=840&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=e6b770f67e02c63e905d81839f5e016c 840w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/conversation_01_preview.png?w=1100&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=e26dd9c688621a84d03bfda1234b15e2 1100w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/conversation_01_preview.png?w=1650&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=fd2fb8f7ec87702f44fba90cc95550ef 1650w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/conversation_01_preview.png?w=2500&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=5c86084deb64ad185d7892bf0f24558c 2500w" />
</Frame>

### Hair Check

The HairCheck component provides a pre-call interface for users to test and configure their audio/video devices before joining a video chat.

```bash  theme={null}
npx @tavus/cvi-ui@latest add hair-check-01
```

<Tabs>
  <Tab title="Description">
    The `HairCheck` component provides a pre-call interface for users to test and configure their audio/video devices before joining a video chat.

    **Features:**

    * **Device Testing**: Live preview of camera feed with mirror effect
    * **Permission Management**: Handles camera and microphone permission requests
    * **Device Controls**: Integrated microphone and camera controls
    * **Join Interface**: Call-to-action button to join the video chat
    * **Responsive Design**: Works on both desktop and mobile devices

    **Props:**

    * `isJoinBtnLoading` (boolean): Shows loading state on join button
    * `onJoin` (function): Callback when user clicks join
    * `onCancel` (function, optional): Callback when user cancels
  </Tab>

  <Tab title="Code">
    ```tsx  theme={null}
    import { HairCheck } from './components/cvi/components/hair-check';
    ```

    ```tsx  theme={null}
    <HairCheck
      isJoinBtnLoading={isLoading}
      onJoin={handleJoinCall}
      onCancel={handleCancel}
    />
    ```
  </Tab>
</Tabs>

Preview

<Frame><img src="https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/haircheck_01_preview.png?fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=7ef2056a38131d3f8caa5416c9dd0d31" alt="Haircheck Block Preview" data-og-width="2412" width="2412" data-og-height="1388" height="1388" data-path="images/haircheck_01_preview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/haircheck_01_preview.png?w=280&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=d1476461af1be9d952c30bf352118d6b 280w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/haircheck_01_preview.png?w=560&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=baa6efe01df631f044a77b00cec6673e 560w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/haircheck_01_preview.png?w=840&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=1a542cd4a5c995230a13316763a94441 840w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/haircheck_01_preview.png?w=1100&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=9ccb982940c78bd8f9d4317d7d0cb2db 1100w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/haircheck_01_preview.png?w=1650&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=c8e3ba04bcd0b8c7d17a6480d2a519e5 1650w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/haircheck_01_preview.png?w=2500&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=394a6b3ba4defc9ccab312f11cb21384 2500w" /></Frame>
