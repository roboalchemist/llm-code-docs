# Source: https://docs.flux.ai/reference/reference-forking-cloning.md

# Forking and cloning

Learn how to effectively get a copy of other project of components in Flux using forking and cloning.



## Overview

In Flux, managing your project versions effectively is crucial for a smooth and efficient workflow. This guide provides an in-depth look at two key features that Flux offers for project version management: _forking and cloning._

> It is important to note that forking and cloning do not preserve interactions between users, especially comments

## Forking

**When you fork a project, all its history of changes is preserved.** Meaning the forked part can eventually be merged back with the original.

To fork a project, navigate to the project you want to fork and then select "Fork project" from the Flux menu on the top left.

- Alternatively, you can use the "Fork" shortcut next to the "Star" icon in the top left.

![](https://uploads.developerhub.io/prod/86Yw/3i2xsrjvwgwa9rbm2wozoioflbjtzfdsvpqy2a2e5yj5ne7wc9v4ujr3c4l99av2.png)

> A project can only be forked once, so if you try to create "a fork of a fork," the option will be unavailable.

## Cloning

**Cloning a project makes a clean copy without any history preservation**. Since the clone doesn't contain any link to the original part, it won't be able to be merged back.

To clone a project, navigate to the project you want to fork and then select "Clone project" from the Flux menu on the top left.

![](https://uploads.developerhub.io/prod/86Yw/ylf3t97c8z03ye29mwd3er0medx6bphu2mexsyo5opo4fbe3u52wxy6p8krwri2c.png)

## When to Clone Versus Fork

Whenever you find a publicly accessible project or part in the library, and you decide to duplicate the project, then you will need to decide whether to clone or fork the project.

If you want to maintain access to all earlier versions of the project in your duplicate version, then you should fork the project. This is a common option you would use when experimenting with an earlier version of a design. However, if you do not need to have access to the earlier versions of the duplicate project, then you should clone the project.

Read this resource to learn more about using cloning and forking in Flux.

## Merging

Version control systems like Git provide a function called merging, where a forked project is consolidated back into its original branch. At the moment, this capability is not included in Flux. In the future, we will release merging back to the original project.