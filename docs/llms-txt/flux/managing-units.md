# Source: https://docs.flux.ai/reference/managing-units.md

# Managing units

This reference document covers how to work in Flux with multiple units, including default units for the whole project and also for specified individual objects or collections of objects as well.

> Currently, compatible length units in flux are: `um`, `mm`, `mil`, `inch`, `cm`, `ft`, `m`

When inputting any length in flux, you can specify the units after the inputted value. For example, if you want to set the position of an object (which is a 2D vector) you can input `2mm 3in`, which will set its position 2 mm horizontally from its origin, and 3 inches vertically.

## Default Units

Unless modified, flux defaults to using millimeters units. In other words, any rules or other elements that require a numerical value, unless intentionally changed, will expect millimeter values as input. For example, if you set _Dimension Unit_ to mm, and later enter `2 2` for Position, Flux will assume you mean 2 mm 2 mm.

### Change a Project’s Default Units

To change the default units of the whole project, add a _Dimension_ _Unit_ rule to the _Layout_ object located in the objects panel. It’s best to do this at the very beginning of your PCB layout process, as changing the default units in a project will cause any unlabeled units to switch over and may cause issues.

## Changing Units for a Specific Object

If you’d like to change the units of a specific object, then simply add a _Dimension Unit_ rule under the _Object-Specific Rules_ and select your desired units. 

To change the default units for a full subset of objects, assuming they share a common parent, do the same as above. All the sub-objects of the branch will then inherit these default units. 

## Working with Units Example

Suppose you'd like your whole project to be in mils, except for your net and trace-related measurement to be in mm. In this case, add the following rules:

1. Add the _Dimension Unit_ rule as an O_bject-Specific Rule_ to the _Layout_ object, set to `mil`. This will set all unlabeled units to be in mils. Ensure that you do this at the very beginning of the PCB layout project.
2. Add the _Dimension Unit_ rule as an O_bject-Specific Rule_ to the _Nets_ object, set to `mm`. This will make all traces and GND planes use millimeters as their default unit.