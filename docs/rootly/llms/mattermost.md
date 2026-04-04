# Source: https://docs.rootly.com/integrations/mattermost.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Mattermost

> Integrate Rootly with Mattermost to create and track incidents directly from your chat platform.

## Introduction

**Mattermost** Integration allows you to:

* Create and manage an incident directly from Mattermost using slash commands
* Automatically create Mattermost channel when new incident is declared in Rootly

## Installation

Let's create an Oauth2 client

<Frame caption="Menu > Integrations">
    <img src="https://mintcdn.com/rootly/EZBU89ISF00990Wy/images/integrations/mattermost-step-1.webp?fit=max&auto=format&n=EZBU89ISF00990Wy&q=85&s=cabe54b42224b79590ae4f1ef6957c61" alt="" width="868" height="1124" data-path="images/integrations/mattermost-step-1.webp" />
</Frame>

<Frame caption="OAuth 2.0">
    <img src="https://mintcdn.com/rootly/EZBU89ISF00990Wy/images/integrations/mattermost-step-2.webp?fit=max&auto=format&n=EZBU89ISF00990Wy&q=85&s=e4f362c549d78635335b52576dc427b5" alt="" width="862" height="869" data-path="images/integrations/mattermost-step-2.webp" />
</Frame>

<Frame caption="Configuration">
    <img src="https://mintcdn.com/rootly/EZBU89ISF00990Wy/images/integrations/mattermost-step-3.webp?fit=max&auto=format&n=EZBU89ISF00990Wy&q=85&s=ecf2acf4259dbff2676214f97b9de37a" alt="" width="885" height="795" data-path="images/integrations/mattermost-step-3.webp" />
</Frame>

`https://rootly.com/auth/mattermost/callback`

`https://rootly.com/auth/sign_in_mattermost/callback`

And finally copy `client_id` and `client_secret` into Rootly configuration

<Frame>
    <img src="https://mintcdn.com/rootly/EZBU89ISF00990Wy/images/integrations/mattermost-step-4.webp?fit=max&auto=format&n=EZBU89ISF00990Wy&q=85&s=8d8cb08fdcb3c9817266393837519df2" alt="" width="862" height="274" data-path="images/integrations/mattermost-step-4.webp" />
</Frame>

## Configuration

Rootly allows you to customize your Mattermost integration. To do so, navigate to the configuration modal (**Configuration** > **Integrations** > **Mattermost** > **Configure**)

<img src="https://mintcdn.com/rootly/jL2nQYfo_IMOD5x3/images/CleanShot2025-09-26at11.17.09.png?fit=max&auto=format&n=jL2nQYfo_IMOD5x3&q=85&s=8b628281d4b34f5bbaa09a0605f82f1d" alt="CleanShot 2025-09-26 at 11.17.09.png" width="757" height="466" data-path="images/CleanShot2025-09-26at11.17.09.png" />

You can customize how you want the incident channels to be named, what data to collect on incident creation, etc.

<img src="https://mintcdn.com/rootly/jL2nQYfo_IMOD5x3/images/CleanShot2025-09-26at11.18.57.png?fit=max&auto=format&n=jL2nQYfo_IMOD5x3&q=85&s=0a58859ee41453448cb8d3a31d896833" alt="CleanShot 2025-09-26 at 11.18.57.png" width="872" height="1278" data-path="images/CleanShot2025-09-26at11.18.57.png" />

## Connect to Rootly

<Note>
  Every user who wishes to use Rootly through Mattermost will have to perform this step.
</Note>

After successfully installing Mattermost, run `/incident connect` command to establish a connection between your Rootly org and your Mattermost account.

Click on the `Connect now` bot message following the command.

<img src="https://mintcdn.com/rootly/jL2nQYfo_IMOD5x3/images/CleanShot2025-09-26at10.52.57.png?fit=max&auto=format&n=jL2nQYfo_IMOD5x3&q=85&s=57b621efd9c5163b740c9cae8ec92233" alt="CleanShot 2025-09-26 at 10.52.57.png" width="493" height="190" data-path="images/CleanShot2025-09-26at10.52.57.png" />

Click on `Allow` to authorize access.

<img src="https://mintcdn.com/rootly/jL2nQYfo_IMOD5x3/images/CleanShot2025-09-26at10.53.30.png?fit=max&auto=format&n=jL2nQYfo_IMOD5x3&q=85&s=a11dcd0b60608c13c8ada53d688513c6" alt="CleanShot 2025-09-26 at 10.53.30.png" width="699" height="330" data-path="images/CleanShot2025-09-26at10.53.30.png" />

Now you're ready to manage incidents on Rootly through Mattermost!

## Manage Incidents

### Declaring an Incident

To declare a new incident, use the `/incident new` command. You can make execute this command in any channel.

You'll be prompted on create a new incident.

<img src="https://mintcdn.com/rootly/jL2nQYfo_IMOD5x3/images/CleanShot2025-09-26at11.08.52.png?fit=max&auto=format&n=jL2nQYfo_IMOD5x3&q=85&s=464860b88aa9a93a2b940968421dd711" alt="CleanShot 2025-09-26 at 11.08.52.png" width="632" height="669" data-path="images/CleanShot2025-09-26at11.08.52.png" />

This will result in an incident being created in Rootly and a designated channel created in Mattermost.

### Mitigating an Incident

To mark an incident as `mitigated`, use the `/incident mitigate` command.

<Note>
  You'll have to execute this command in the incident-specific channel created from the previous step.
</Note>

<img src="https://mintcdn.com/rootly/jL2nQYfo_IMOD5x3/images/CleanShot2025-09-26at11.12.10.png?fit=max&auto=format&n=jL2nQYfo_IMOD5x3&q=85&s=8f2c70c05eae46815d7214920d77ec59" alt="CleanShot 2025-09-26 at 11.12.10.png" width="589" height="455" data-path="images/CleanShot2025-09-26at11.12.10.png" />

### Resolving an Incident

To mark an incident as resolved, use the `/incident resolve` command.

<Note>
  You'll have to execute this command in the incident-specific channel created from the previous step.
</Note>

<img src="https://mintcdn.com/rootly/jL2nQYfo_IMOD5x3/images/CleanShot2025-09-26at11.13.08.png?fit=max&auto=format&n=jL2nQYfo_IMOD5x3&q=85&s=fce963dfc25abe23b24e33ab9b15623f" alt="CleanShot 2025-09-26 at 11.13.08.png" width="585" height="447" data-path="images/CleanShot2025-09-26at11.13.08.png" />

### List of Commands

If you ever forget what commands are available, you can run `/incident help` to get a reminder of the available commands. As Rootly adds more commands, this list will grow.

<img src="https://mintcdn.com/rootly/jL2nQYfo_IMOD5x3/images/CleanShot2025-09-26at11.15.07.png?fit=max&auto=format&n=jL2nQYfo_IMOD5x3&q=85&s=12d72ae62e090432fe3b77924ffa4da6" alt="CleanShot 2025-09-26 at 11.15.07.png" width="495" height="124" data-path="images/CleanShot2025-09-26at11.15.07.png" />

## Uninstall

You can **uninstall** this integration in the integrations panel by clicking **Configure > Delete**


Built with [Mintlify](https://mintlify.com).