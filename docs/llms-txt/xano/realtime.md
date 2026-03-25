# Source: https://docs.xano.com/building/logic/triggers/realtime.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Realtime Triggers

<Steps>
  <Step title="Realtime Triggers">
    Realtime triggers are created for each channel. Once you've created a realtime channel, click the + Add Channel Trigger button to create a new channel trigger.

    Select the **actions** that will activate the trigger.

    **Message**\
    Any time a new message is sent to the channel

    **Join**\
    Any time someone attempts to join the channel

    The Join trigger fires **before** the user joins the channel, which means it will fire whether or not the user can / is authorized to join that channel. The purpose of this is to allow you to block the user from joining the channel if necessary.

    To prevent the user from joining, you can return a `false` response from the trigger. Anything else will allow the user to join the channel.

    ***

    Realtime triggers have predefined inputs that contain all of the information you'll need to build a workflow based on the realtime event.

    `Action` and **~~Command~~**\
    This will be either 'join' or 'message' depending on what was responsible for executing the trigger.

    *****Action and Command currently have the same values, but behind the scenes, the values do not come from the same source. We maintain two separate inputs for the purpose of expanding this functionality in the future.*****

    `Channel`\
    The channel that this command or message is being sent to

    `commandOptions`\
    Any options that are provided with the command being sent to the channel

    `payload`\
    The contents of the command, such as the message body

    `client`\
    An internal client ID

    ***
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).