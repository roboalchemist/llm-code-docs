# Source: https://docs.unifygtm.com/reference/plays/triggers.md

# Play Triggers

> Triggers represent the events and data sources that a Play runs on.

## Overview

Plays run on invidiual records, such as companies or people. Triggers define
when a Play should run and what data should be provided to it. Below are the
triggers you can choose from when creating a Play.

## Available triggers

### Champions

This trigger is a shortcut for running a Play on champions that Unify has
tracked for your business. Once selected, you can customize the matching
criteria similar to the record match trigger. This trigger always returns
People.

<Frame caption="The configuration panel for a champions trigger.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/champions-trigger.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a26582da988298dbdedc223863e17682" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/champions-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/champions-trigger.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=74b7e908d46c5baea5e5dffb763b6cf1 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/champions-trigger.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=9c6d99afe8db8e34f4b7a81675e64217 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/champions-trigger.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f2c7222c77b79c3f039256474a9b7f2f 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/champions-trigger.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=00737c09734267cecf660579ade055a8 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/champions-trigger.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=0677416141bc204f1fc82384078465d3 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/champions-trigger.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c6dec9c784c790daaf0bec4584f1ff47 2500w" />
</Frame>

In order to use this trigger, you must have enabled and configured champion
tracking in your settings. For more information, see [Champion Tracking](/reference/signals/champions).

### Find lookalike companies

This trigger runs a Play on companies that are similar to a set of companies
you specify. This is useful for finding new companies that are similar to your
existing customers or ideal customer profile.

<Frame caption="The criteria panel for a lookalike companies trigger.">
  <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=c1b6b19abcb96637ada83885fc3594c7" data-og-width="2304" width="2304" data-og-height="1638" height="1638" data-path="images/reference/signals/lookalikes-criteria-panel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=24108a56f46defdb2a7cd8532d7f35c3 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=e082600be56e2e8e51f92f5b6c2b53d1 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=ad6e60a9ab61f9bb56dc6b85c4f0fa9d 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=533504120e70cc6efedf3c40f4d4b114 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=e05e930b767632122fda43bbd544dade 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-criteria-panel.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=21eddece4a8dbbd255acce80fe6116e9 2500w" />
</Frame>

Once you've defined the criteria that specifies which companies to find
lookalikes for, you can define some additional options for the trigger, such as
additional filters to apply or exclusions to enable and disable.

<Frame caption="The configuration panel for a lookalike companies trigger.">
  <img src="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=11e4dd11db05b12b7586fa07031668d5" data-og-width="2304" width="2304" data-og-height="1638" height="1638" data-path="images/reference/signals/lookalikes-configuration-panel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=280&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=d476fac45cafa4a90b0276e2e3feb54b 280w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=560&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=3a5c06738c881929fe9461124612b10b 560w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=840&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=56b0970bee1a35256829f2464863ef41 840w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=1100&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=be8f6bd13d7d47c35c2844624973b733 1100w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=1650&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=ceb8d2545cdc7e918eee00f519f9bf26 1650w, https://mintcdn.com/unify-19/2bGCds6YQ9Qo4--E/images/reference/signals/lookalikes-configuration-panel.png?w=2500&fit=max&auto=format&n=2bGCds6YQ9Qo4--E&q=85&s=f03b70c53fc8620d588f8a20adcc783e 2500w" />
</Frame>

This trigger is powered by [Ocean.io](https://www.ocean.io/). The integration is
fully managed by Unify and included in your plan, so no additional subscription
or setup is required.

### Record enters an Audience

This trigger runs a Play once on every company or person that "enters" an
audience. A record enters an audience when it meets the criteria of the audience
for the first time.

<Frame caption="The configuration panel for an audience trigger.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/audience-trigger.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=751a2369977272fb19ea23245f51627d" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/audience-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/audience-trigger.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=696ff812de2dd2e958f18a432d4d9733 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/audience-trigger.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f3667b137cee2ee8e20b8bbc0cc3bcba 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/audience-trigger.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=ea8bdf9df29a73328232ab8c96633e37 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/audience-trigger.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=e8a891b067cd78ced213640b6137ecd1 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/audience-trigger.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=630398b748be76d9b13369040b87c8b7 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/audience-trigger.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a99a0f1035dbc85e96dc181fbddcdb6e 2500w" />
</Frame>

When you select an audience trigger, you will be prompted to select an audience
from the list of audiences you have created. Audiences are reusable in Unify,
which means you can use the same audience in multiple Plays.

You also have the choice to run the Play on either companies that enter the
audience or people that enter the audience. If you select companies, the output
of this trigger will be a company record. Otherwise, the output will be a person
record.

### Record matches criteria

This trigger runs a Play once on every company or person that matches a set of
filters. This trigger behaves the same as the audience trigger, but it doesn't
require that you already have an audience created. Instead, you can define the
filters directly in the Play.

<Frame caption="The configuration panel for a record match trigger.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/record-match-trigger.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=312374b3bbe33c6dc447a5c092c2848c" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/record-match-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/record-match-trigger.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=830f88561e84a75d244c865a6feb4695 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/record-match-trigger.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=f4a6c485e1a6cbc9fc67c310660c3905 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/record-match-trigger.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=6c29cd5cb1a665b5f907af66e4c7165c 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/record-match-trigger.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=af479b57aa8bb8b801887a7d1745a498 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/record-match-trigger.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=28ad0475f6a61dd6964ac38fee319983 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/record-match-trigger.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=e3e27d7441ed8496629ec00e16a66f3d 2500w" />
</Frame>

When you select a criteria trigger, you will be prompted to add filters to
select the companies or people that the Play should run on. Just like building
audiences, you can add as many filters as you like and preview the records that
match the filters before saving the trigger.

As with audience triggers, you can choose to run the Play on either companies or
people. This will determine what type of record the trigger outputs.

### Website visitors

This trigger is a shortcut for running a Play on companies that visit your
website. Once selected, you can customize the matching criteria similar to the
record match trigger. This trigger always returns Companies.

<Frame caption="The configuration panel for a website visitors trigger.">
  <img src="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/website-visitors-trigger.png?fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=ed575ee55f0e23aa0b40f0323a29284e" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/reference/plays/website-visitors-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/website-visitors-trigger.png?w=280&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=74244388cb6e6e8349178f6781a52943 280w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/website-visitors-trigger.png?w=560&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=62819080d980f172d63aff91609849f5 560w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/website-visitors-trigger.png?w=840&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=c5fe15a653f9235c6ec507b2a1dc8c94 840w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/website-visitors-trigger.png?w=1100&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=1bbd3ecd4840405ba738dea02c7801f8 1100w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/website-visitors-trigger.png?w=1650&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=e07e0c78d6b1a11b4134396eedcf525a 1650w, https://mintcdn.com/unify-19/FV7_ax32WGUYsOt7/images/reference/plays/website-visitors-trigger.png?w=2500&fit=max&auto=format&n=FV7_ax32WGUYsOt7&q=85&s=a9205bc4897ed64a8b0ddf44932129bb 2500w" />
</Frame>

## Coming soon

There are lots of additional triggers in the works including webhooks, third-party
events, schedules, and more. If you're interested in one that isn't available
yet, [let us know](mailto:support@unifygtm.com)! We'll get you in the beta as
soon as it's ready.

## FAQ

<AccordionGroup>
  <Accordion title="Should I use an Audience trigger or a record match trigger?">
    Audience triggers and record match triggers can both be used to accomplish
    the same goal. The main difference is that audience triggers require you to
    create an audience ahead of time, while record match triggers allow you to
    define the filters directly in the Play.

    Audiences can be reused in multiple Plays, which is useful if you have a set
    of filters that you use frequently. Audiences can also be viewed, edited,
    and exported from the **Audiences** tab.

    Record match triggers are a great option for quickly iterating on a Play or
    if you don't want to create an audience for a one-off Play. You can always
    come back later, convert the filters into an audience, and then swap the
    trigger out for an audience trigger.
  </Accordion>

  <Accordion title="Is an Audience trigger the same as sending an Audience to a manual trigger?">
    Audiences are dynamic lists of companies and people that can change over
    time according to the filters you specify. For example, an audience might
    capture all companies that have visited your website in the last 30 days.

    When you send an audience to a manual trigger, you are sending the current
    list of companies or people that are in the audience at that moment. This
    is useful if you want to run a Play on a snapshot of the audience but not on
    a recurring basis.

    By contrast, an audience trigger will run a Play on every company or person
    that enters the audience in the future. This is useful if you want to run a
    Play on every company or person that meets the audience criteria now and in
    the future.
  </Accordion>
</AccordionGroup>
