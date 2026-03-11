# Source: https://docs.xano.com/realtime/channel-permissions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Channel Permissions

Channels are opened with your front-end's implementation of Realtime.

```javascript  theme={null}
const marvelChannel = this.xanoClient.channel("marvel-chat-room");
```

Each channel needs to have permissions defined to ensure that they behave in the way that you expect and remain secure. On this page, we'll go over the various permission settings available and show you how to apply them.

Securing your Realtime channels is a multi-step process, and is not always solely reliant on the channel permissions you set. This includes:

* Setting the proper channel permissions for your use case

* Using nested channels to separate data

* Using [Realtime Triggers](/the-function-stack/building-with-visual-development/triggers) to act as a primary or secondary measure to block messages from being sent to the channel

* Generating separate authentication tokens for connecting to the realtime server

* Obfuscating the implementation on your front-end, and ensuring that channel creation is handled properly

## Permissions

### Anonymous Clients

Anonymous Clients means that you allow unauthenticated users to connect to your channels, but they can not send messages.

### Presence

Every client connected to this channel will receive a the list of all the other clients (including yourself). Note that authenticated client details will be augmented with the extra information stored in their JWT token.

### Client Public Messaging

This option allows authenticated and unauthenticated clients to send messages to the channel. These messages will be sent to all the users connected to the channel.

###

Similar to Client Public Messaging, this permission allows only authenticated users to send messages to the channel. Unauthenticated clients can still see the messages being sent to the channel.

### Client Authenticated Messaging

Every message sent to the channel by authenticated clients will only broadcasted to all other authenticated clients. This means that anyone can connect to that channel, but only authenticated client will receive messages broadcasted by the channel. Anonymous client will not receive any messages.

### Client Private Messaging

This enables clients to send messages directly to other clients without requiring authentication as long as both clients are present in the channel.

###

This permission enables client private messaging only between authenticated clients. Unauthenticated clients can not send private messages.

<Warning>
  It's important to note that some of these permissions may appear to have logical dependencies, but they do not. For example, if you enable **Client Public Messaging**, this implies that \*\*Anonymous Clients \*\*is also enabled.
</Warning>

## Applying Permissions

From the Realtime Settings panel, click the icon shown below to define channel permissions.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/34f5bd72-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=9e231bf5ae998620ab7eaed0a5db0683" width="972" height="252" data-path="images/34f5bd72-image.jpeg" />
</Frame>

On the next panel that opens, fill in the options shown.

#### Channel Status

Defines whether or not these channel permissions are utilized

#### Channel Target

This is essentially the name of the channel you are creating permissions for. Channel names can be dynamic to support creation of new channels from your front-end by enabling the **nested channels** option. Using nested channels along with a name like "chatroom/\*" will allow you to create channels that begin with "chatroom/" and anything else afterwards, such as a unique channel identifier. If you do not enable nested channels, the permissions will just apply to the channel name you specify.

#### Description

Give your permission layout a description for organizational purposes, if you wish.

#### Permissions

Using the list of permissions on this page, determine the correct set of permissions to apply to any channels that match the name pattern.

**Channel Triggers**

Triggers are function stacks that can run when messages or events are sent to the channel(s) impacted by these permissions. You need to first save your changes to enable adding triggers when creating new permissions.

For more information about Realtime Triggers, see [this section](/the-function-stack/building-with-visual-development/triggers) of our documentation.

## Permission Examples

<Info>
  Please note that **Presence** is usually optional no matter the scenario and is just based on if you want to utilize presence updates in your realtime channels.
</Info>

| Context                                                                                                                                                                                                                                  | Permissions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A chat application where users can both connect and send messages anonymously                                                                                                                                                            | <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/4dd7c64b-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=09c9c6f8535c69a3e10a69b1586cfcac" width="900" height="936" data-path="images/4dd7c64b-image.jpeg" /> |
| A chat application where users can connect anonymously, but authentication is required to send messages                                                                                                                                  | <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f778da6f-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=0bf1c1d591e009131db82825c0782c78" width="900" height="955" data-path="images/f778da6f-image.jpeg" /> |
| A notification system that allows for unauthenticated users to connect so they can receive notifications, but sending messages is not allowed. You would send notifications to this type of channel through the Realtime Event function. | <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/dfb753e4-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=13bbc0d0487ecf47956afe40e10fc177" width="900" height="932" data-path="images/dfb753e4-image.jpeg" /> |
| A chat application that only allows authenticated users to connect and send messages                                                                                                                                                     | <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/79e1c0e3-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=7d9e898def38f68cfe2876f96b533f0b" width="900" height="957" data-path="images/79e1c0e3-image.jpeg" /> |
| A chat application that only allows authenticated users to connect, and allows direct client-client private messaging for authenticated users                                                                                            | <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b57877f3-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=08a3627bb9f9cd898f42bc3b9a2df0cc" width="900" height="959" data-path="images/b57877f3-image.jpeg" /> |


Built with [Mintlify](https://mintlify.com).