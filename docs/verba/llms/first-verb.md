# Source: https://docs.verba.ink/guides/first-verb.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.verba.ink/llms.txt
> Use this file to discover all available pages before exploring further.

# Create your first verb

> Design personality, visuals, and behavior in one flow.

## 1. Define the essentials

Start with the basics: name, description, age, and language. These fields shape
how your verb is introduced and how it speaks.

<Info>
  Keep the description short and concrete. Focus on tone, role, and what the
  verb helps with.
</Info>

## 2. Build a visual identity

Upload an avatar and banner that match the personality you want users to feel.

<Columns cols={2}>
  <div>
    **Avatar**

    * Clear, centered subject
    * Works at small sizes
    * Consistent style with your banner
  </div>

  <div>
    **Banner**

    * Wider framing, more context
    * Reinforce the theme or mood
    * Optional but impactful
  </div>
</Columns>

## 3. Write the personality

Fill in core personality, backstory, beliefs, likes, and dislikes. This is the
primary source of behavior.

<CardGroup cols={2}>
  <Card title="Core personality" icon="star">
    The non-negotiable traits and quirks.
  </Card>

  <Card title="Backstory" icon="book">
    Motivations that explain the personality.
  </Card>

  <Card title="Beliefs" icon="compass">
    Opinions and values that guide responses.
  </Card>

  <Card title="Likes and dislikes" icon="heart">
    Quick hooks for natural conversation.
  </Card>
</CardGroup>

## 4. Tune behavior

Set your AI engine controls to balance creativity and consistency. Start with
defaults, then iterate while chatting.

<Tip>
  If responses feel too generic, raise temperature slightly. If they drift off
  topic, lower it and reduce top-p.
</Tip>

## 5. Test and iterate

Run live chats, adjust prompts, and refine until the personality holds under
real usage.

<Card title="AI engine guide" icon="sliders" href="/guides/ai-engine">
  Learn how each control changes behavior.
</Card>

Built with [Mintlify](https://mintlify.com).
