# Source: https://docs.hypermode.com/agents/30-days-of-agents/day-3.md

# Day 3: Morning Stand-up Automation with Sidekick

> Connect your Google Calendar and have Sidekick draft your morning stand-up updates automatically. Learn how agents understand your schedule and priorities.

<Card title="Day 3 challenge" icon="calendar-check">
  **Goal**: automate your daily stand-up preparation

  **Theme**: foundation week - calendar intelligence

  **Time investment**: \~10 minutes
</Card>

Welcome to Day 3! Yesterday you experienced how Sidekick researches and creates
calendar events. Today we're going deeper into calendar intelligence—having
Sidekick understand your schedule and automatically draft your daily stand-up
updates.

This is where you see the power of agents that understand context, not just
commands.

## What you'll accomplish today

* Ensure your Google Calendar connection is active
* Have Sidekick analyze your day's schedule
* Generate a draft stand-up update based on your meetings
* Experience how agents interpret calendar context

<Warning>
  This isn't about reading your calendar aloud. Sidekick analyzes meeting
  patterns, identifies priorities, and suggests talking points for your
  stand-up.
</Warning>

## Step 1: verify your calendar connection

If you completed Day 2, your Google Calendar should already be connected. Let's
verify and explore what Sidekick can see:

**Ask Sidekick:**

```text
What meetings do I have today? Can you see my calendar?
```

<img src="https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-calendar-check.png?fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=ec8d898730d0fc432df69c7d33b97fa0" alt="Calendar Connection Status - Placeholder" width="2784" height="1736" data-path="images/agents/30-days-of-agents/day3-calendar-check.png" srcset="https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-calendar-check.png?w=280&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=8b4bc4f1b54f56d5aeeda0624c2b991f 280w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-calendar-check.png?w=560&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=4acc49b7ba7d0753deb0281eb83496cb 560w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-calendar-check.png?w=840&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=7d3918d62ce65cde8fb6f8f995c6ce5d 840w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-calendar-check.png?w=1100&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=1d3607e0cba462c4da64670b8a202de1 1100w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-calendar-check.png?w=1650&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=f7aaeb537187f5c400719f2f31eaf86e 1650w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-calendar-check.png?w=2500&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=27eb51c12567b5729d5d223f12443e3d 2500w" data-optimize="true" data-opv="2" />

Sidekick should be able to:

* List your meetings for today
* Show meeting times and attendees
* Identify meeting types (1:1 s, team meetings, external calls)

<Info>
  If your calendar isn't connected, follow the connection steps from Day 2.
  Sidekick guides you through the OAuth flow.
</Info>

## Step 2: request your stand-up draft

Now for the magic. Instead of manually reviewing your calendar and thinking
about what to share in stand-up, let Sidekick do the analysis:

```text
Based on my calendar today, can you draft my morning stand-up update?
Include what I'm working on, any blockers you can identify from my schedule, and what I focus on today.
```

<img src="https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-standup-draft.png?fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=f46ac382418164403c3590057e932780" alt="Stand-up Draft Generation - Placeholder" width="2784" height="1736" data-path="images/agents/30-days-of-agents/day3-standup-draft.png" srcset="https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-standup-draft.png?w=280&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=9e7ba2b9562fa7069277ff6f5ef2b9b2 280w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-standup-draft.png?w=560&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=e017090c4eadb95c11c13a43afa85f67 560w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-standup-draft.png?w=840&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=bb837777e2790df977e389c987143ae0 840w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-standup-draft.png?w=1100&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=7c9b60a31e0d682909fae5268f45620a 1100w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-standup-draft.png?w=1650&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=fb8f648f810b1b8d028d34049a41da40 1650w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-standup-draft.png?w=2500&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=004d0ff001830cf79c928d0528bb2ec3 2500w" data-optimize="true" data-opv="2" />

Watch how Sidekick:

* Analyzes your meeting types and identifies work streams
* Spots potential scheduling conflicts or back-to-back meetings
* Suggests priorities based on meeting importance and attendees
* Drafts talking points in a natural, conversational tone

<Tip>
  **Agent learning moment**: notice how Sidekick infers context from calendar
  data, and how it's interpreting patterns and making intelligent suggestions.
</Tip>

## Step 3: refine your stand-up style

Your stand-up format might be different from Sidekick's initial draft. Let's
teach it your team's style:

```text
Our stand-ups follow this format:
- Yesterday's accomplishments
- Today's priorities (max 3 items)
- Any blockers or help needed

Can you redraft my update in this format? Also, our team prefers bullet points over paragraphs.
```

<img src="https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-format-update.png?fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=b92d304c20f8aea9e4bdb8f6a3c21b77" alt="Stand-up Format Refinement - Placeholder" width="2784" height="1736" data-path="images/agents/30-days-of-agents/day3-format-update.png" srcset="https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-format-update.png?w=280&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=e20a9adfe914035dd5e4c28fe89561b4 280w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-format-update.png?w=560&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=886e74ef5b49ef516bc1a9bb2a47d750 560w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-format-update.png?w=840&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=edc05f625c38fb8f1a802ab2cf8b35dc 840w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-format-update.png?w=1100&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=43f3e68b3cac459c89c5f044e2a47822 1100w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-format-update.png?w=1650&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=cc75500e6e11ae146722579a5d0704f9 1650w, https://mintcdn.com/hypermode/hnPwKRjst4guczp3/images/agents/30-days-of-agents/day3-format-update.png?w=2500&fit=max&auto=format&n=hnPwKRjst4guczp3&q=85&s=fba720f8de7733fe8a33aae15ab4c29c 2500w" data-optimize="true" data-opv="2" />

Sidekick adapts the content to match your team's preferred structure and
communication style.

## Step 4: identify intelligent insights

Ask Sidekick to go beyond basic calendar reading:

```text
Looking at my schedule, what patterns do you notice?
Are there any potential issues or opportunities for improving my day?
```

Sidekick might identify:

* **Time blocks**: "You have three 1:1 s back-to-back 2–3:30 PM"
* **Preparation needs**: "Your client presentation at 4 PM follows immediately
  after your team planning session"
* **Travel time**: "Note the location change between your 10 AM and 11 AM
  meetings"
* **Energy management**: "Consider scheduling buffer time before your most
  important calls"

## What just happened?

In just 10 minutes, you've experienced sophisticated calendar intelligence:

**Context understanding** Sidekick doesn't just read calendar entries—it
interprets meeting types, identifies work streams, and understands priorities

**Pattern recognition** It spots scheduling conflicts, preparation
opportunities, and ways to optimize your approach

**Communication intelligence** It adapts content format and tone to match your
team's communication style

**Proactive insights** Beyond the immediate request, it offers strategic
suggestions for time management

## The power of calendar intelligence

Unlike static calendar apps, Sidekick understands the story your schedule tells.
It can identify when you're overbooked, suggest optimal meeting prep time, and
even recognize when you need buffer time between high-stakes meetings.

<Card title="Tomorrow - Day 4" icon="arrow-right" href="/agents/30-days-of-agents/day-4">
  Daily agenda preparation with contextual notes. Learn to have Sidekick prep
  your entire day with meeting insights and action item tracking.
</Card>

## Pro tip for today

Before tomorrow's session, try this experiment:

```text
If you were managing my calendar, what changes would you suggest for tomorrow to make it more productive?
```

This teaches Sidekick to think strategically about your time management, not
just report what's scheduled.

***

**Time to complete**: \~10 minutes

**Skills learned**: calendar intelligence, automated content generation, context
interpretation, communication style adaptation

**Next** day 4 - Daily agenda preparation with contextual insights

<Tip>
  **Remember** every interaction teaches Sidekick more about your work patterns,
  communication style, and priorities. The agent is learning your preferences to
  become more helpful over time.
</Tip>
