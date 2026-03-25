# Source: https://microsoft.github.io/lage/docs/introduction

Title: Introduction | Lage

URL Source: https://microsoft.github.io/lage/docs/introduction

Markdown Content:
Your JavaScript repository has grown large enough that you have turned to using a [monorepo](https://monorepo.tools/) to help you organize your code as multiple packages inside a repository. That's great! However, you realized quickly that the build scripts defined inside the workspace have to be run in package dependency order.

There exist many tools in the market that provide ways for you to run these npm scripts in the correct topological order. So why choose `lage` for your repository?

1.   `lage` is battle tested - it is in use by many JavaScript repositories number in the millions lines of code each
2.   `lage` can be easily adopted - all it takes is just one npm package install with a single configuration file for the entire repository
3.   `lage` supports remote cache as a fallback - never build the same code twice
4.   `lage` is optimized for modern multi-core development machines - don't waste your CPU resources waiting on a single core when you have so many to spare!

How does `lage` schedule tasks?[​](https://microsoft.github.io/lage/docs/introduction#how-does-lage-schedule-tasks "Direct link to how-does-lage-schedule-tasks")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

`lage` has a secret weapon: it has a "pipeline" configuration syntax to define the implicit relationship between tasks. Combined with a package graph, `lage` knows how to schedule which task to run first and which one can be run in parallel. Let's look at an example:

![Image 1: Package graph with task graph equals target graph](https://microsoft.github.io/lage/img/graph-diagram-light.png)

How does `lage` make builds faster?[​](https://microsoft.github.io/lage/docs/introduction#how-does-lage-make-builds-faster "Direct link to how-does-lage-make-builds-faster")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

So how does `lage` make builds faster? To fully appreciate how `lage` gives you the best build performance compared to other monorepo task runners, take a look at this example. Here we have a repo with this dependency graph:

### Level 1: Legacy Workspace Runners[​](https://microsoft.github.io/lage/docs/introduction#level-1-legacy-workspace-runners "Direct link to Level 1: Legacy Workspace Runners")

First, let's take a look at the typical workspace runners. `Lerna` (before), `pnpm recursive`, `rush` and `wsrun` all will run one task at a time. This creates a sort of "build phase" effect where `test` scripts are not allowed to run until `build`.

### Level 2: Scoping[​](https://microsoft.github.io/lage/docs/introduction#level-2-scoping "Direct link to Level 2: Scoping")

One of the first ways to speeding up build jobs is to use "scoping." Usually a change only affects a subset of the graph. We can get rid of the builds of `FooCore`, `FooApp1` and `FooApp2` if the only changes are inside `BarCore`. However, we'll note that `BarPage` is still affected, resulting in this.

### Level 3. Caching[​](https://microsoft.github.io/lage/docs/introduction#level-3-caching "Direct link to Level 3. Caching")

To further improve build times, we can take advantage of build caches. If we had previously built certain packages, we should be able to speed up the build with a cache. Here, the `BarCore` packages have already been built and tested, and so

### Level 4. Pipelining[​](https://microsoft.github.io/lage/docs/introduction#level-4-pipelining "Direct link to Level 4. Pipelining")

Finally, the last thing we can to speed things up is to break down the wall between build phases from the task runner. In `lage`, we define the relationship between scripts in the `pipeline` configuration.
