---
id: Schedules
title: Schedules Overview
---
There are 3 parts that are key in configuring a schedule:

1. Participants for the schedule
2. Rotation period for shifts (Layers)
3. Start and End date and time

## View all Schedules of a team

To view Schedules of a Team, simply click the "Manage" button corresponding to the Team. On the secondary header, select the tab "Schedules"

![](/img/sc_1.png)

## Creating a new Schedule for a team

To create a new escalation policy, simply click the "Create Schedule" button.

Give it a name and brief summary, and select the time zone in which your schedule applies.

![](/img/sc_2.png)

### Defining Layers

Layers are used to define and customize rotations. Rotation can be daily, weekly or custom. Daily rotation means participants will rotate every 24 hours from specified starting date and time.
Rotations can be restricted to certain days and times of the week. Limiting the time frame of the rotations allows defining different on-call rotations at different time periods, such as working hours, off hours, and weekends. Rotations are cumulative. If the time frames for rotations overlap, all the rotations apply, hence there may be multiple participants assigned to be on-call at the same time.

To define a rotation layer, click the "Add Layer" button. The fields in the "Add Layer" form are explained here:

* Name: Give this layer a name
* Shift Length: How long will each shift in the layer last- you can pick from hours, days or weeks.
* Start Time: Date and Time from which this layer will be in effect
* End Time: Date and Time at which this layer will stop being in effect
* Users in order: Pick the users that will rotate in the team. The order of the shifts will be the order in which you pick the users.
* Restrict this layer to specific times: If you want the rotation to only be applied for specific times of the day of the week, use this. You can add multiple restrictions to one layer

![](/img/sc_3.png)

### Schedule Overview

The Layers you define will be depicted visually in the "Schedule Overview" section. You can view the schedules by day, week or month, and adjust which period you want to view it for.

![](/img/sc_4.png)

Click "Create" to Save

### Overlapping Shifts

Rotation layers are cumulative. If the time frames for shifts overlap, all the layerss apply, hence there may be multiple participants assigned to be on-call at the same time.

### Schedule override

For times when the on-call user is unavailable for their on call duties for a specified duration of time, you can "override" the schedule and add a user that is avaiable to fill in for the unavailable user.

![](/img/sc_5.png)

### Nobody is On-Call

It is possible to have a schedule with gaps where no one is on-call during certain times. If no one is on-call at a certain escalation level, the incident will immediately escalate to the next level of the escalation policy. If no one is on-call on the entire escalation policy, an incident will not be assigned.

If you try to create a new incident in the web UI on a service where no one is on-call, you will need to specify who it should be assigned to.

When services automatically try to create incidents, they will be created, but remain unassigned.

## Editing a Schedule

Simply click on the "View" button next to the schedule you want to edit. Edit the form that shows up, and Save.

## Deleting a Schedule

Simply click on the "Remove" button next to the schedule you want to remove, and confirm.
