# Source: https://docs.debricked.com/product/project-health/popularity.md

# Popularity

The popularity of a repository is another crucial indicator of the health of a project. It signifies interest from both developers and users alike, pointing towards viability and continued development. \
Between each layer, there are weights that determine the impact of any given feature on a practice, and of any given practice on the [metric](https://docs.debricked.com/product/project-health/..#what-is-a-health-metric). You can find the data model illustrated below:

### Usage

This practice describes the usage of a repository among open-source users. The following features of Usage are measured:

* Total Downloads - The total number of times a repository has been downloaded through its respective package manager.
* Total Forks - The total number of times a repository has been forked.

### Developer popularity

This practice describes how popular the repository is among the developers. More popular repositories attract more and more skilled developers to contribute.

The following features of Developer Popularity are measured:

* Total Stargazers - The total number the repository has been “starred” in GitHub.
* Total Watchers - The total number of users watching this repository in GitHub. Watchers are notified about activity on the chosen repository.
* Contributor Influence - How much attention the contributors attract to the repository.
* Contributor Trend - The change in contributors, averaged over 10 weeks.

### Community activity

This practice describes how active the community of a repository is. In this case, “community” entails both contributors and users. The activity is measured with features that analyze the current volume of commits, issues, and pull requests, as well as the trend of said volume.

The following features of Community Activity are measured:

* Recent Commits - How many new commits have been made to the master branch within the last 10 weeks.
* Commits Trend - The linear change in commits per week for the past 21 weeks (whether it is increasing or decreasing).
* Recent Issues - How many new issues have been posted within the last 10 weeks.
* Issues Trend - The linear change in posted issues per week for the past 21 weeks (whether it is increasing or decreasing).
* Recent Pull Requests - How many new pull requests have been made within the last 10 weeks.
* Pull Requests Trend - The linear change in pull requests per week for the past 21 weeks (whether it is increasing or decreasing).
* Recently Closed Issues - How many issues have been closed within the past 10 weeks.
* Closed Issues Trend - The linear change in closed issues per week for the past 21 weeks (whether it is increasing or decreasing).

### Ecosystem buzz

This practice describes the buzz of a particular open-source project in different parts of the ecosystem. A higher buzz implies better support from platforms such as StackOverflow.

The following feature of Ecosystem Buzz is measured:

* Total Discussions on Stackoverflow - The total number of search hits a repository/package has on Stackoverflow.
