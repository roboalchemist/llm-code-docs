---
---
title: Event Processors
description: "Learn more about how you can add your own event processors globally or to the current scope."
---

You can enrich events with additional data by adding your own event processors, either on the scope level or globally. Though event processors are similar to  and , there are two key differences:

- Event processors added with either  or  run in an undetermined order, which means changes to the event may still be made after the event processor runs.  and  are guaranteed to be run last, after all other event processors, (which means they get the final version of the event right before it's sent, hence the name).
- While , , and processors added with  run globally, regardless of scope, processors added with  only run on events captured while that scope is active.

Like  and , event processors are passed two arguments, the event itself and a `hint` object containing extra metadata.

