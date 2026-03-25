# Source: https://docs.gitguardian.com/platform/getting-started/first-audit.md

# Assess your repositories' health

> Walkthrough of performing your first historical audit of an integrated VCS source to discover existing secrets in your codebase.

## How do I launch a historical scan of my repositories?

Now that you have integrated your first repositories, it's time to check if they
contain any secrets! GitGuardian gives you the ability to scan the entire commit
history, across all branches, of your repositories to check if they are safe.

> ## Understanding your perimeter
>
> Your perimeter is simply anywhere you are storing your shared code repositories. This includes shared repository hosting like GitHub, GitLab, Bitbucket or Azure Repos.
>
> <iframe width="560" height="315" src="https://www.youtube.com/embed/EmO_opxPOJo?controls=0&modestbranding=1&watchlater=0" title="Understanding Your Perimeter With GitGuardian Video" frameBorder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>

## Your perimeter view

Simply go to the
[**Perimeter view**](https://dashboard.gitguardian.com/perimeter) and launch
your first historical scan!

![perimeter historical scanning](/img/internal-monitoring/integrate-sources/perimeter/historical_scanning_highlighted.png)

## How do I read the results of my scan?

The [Perimeter view](https://dashboard.gitguardian.com/perimeter) contains a
table listing the sources of your monitored perimeter.

After running your first historical scan, GitGuardian will update the `Health`
status of each repository, it will be set to `AT RISK` if a repository contains
at least one hard-coded secret or `SAFE` if it doesn't contain any. The total
number of unique secrets found will also be displayed in the `Secret incidents`
column.

If your repositories contain any hardcoded secrets, click on the Open secrets
incidents link. It will take you to the `Incidents view` and display all the
secret incidents found in a particular source.
