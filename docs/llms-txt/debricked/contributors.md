# Source: https://docs.debricked.com/product/project-health/contributors.md

# Contributors

Open-Source projects are affected by contributors. Theyhave the power to make a project thrive or die. When deciding what open source project to bring into your software, it is important to inspect and analyze its contributors.

Between each layer, there are weights that determine the impact of any given feature on a practice, and of any given practice on the [metric](https://docs.debricked.com/product/project-health/..#what-is-a-health-metric). You can find the data model illustrated below:

### Contributor experience

This practice describes the contributor's experience in a specific repository. Experienced contributors tend to write more efficient, more secure, and usable code, and are therefore preferred.

The following features of Contributor Experience are measured:

* Contributor Influence - How much attention the contributors attract to the repository.
* External Pull Requests Merged per Developer - The average number of pull requests merged in other projects.

### Contributor efficiency

This practice describes the contributor efficiency in a specific repository. It is measured by looking at the rate at which the contributors code, merge pull requests, and close issues.

The following features of Contributor Efficiency are measured:

* Closed Issues per Developer - The average number of issues closed per developer in the past 52 weeks.
* Pull Requests Merged per Developer -The average number of pull requests merged per developer in the past 52 weeks.
* Developer Velocity - The average coding speed of the developers. It is calculated as lines of code merged/closed per week, averaged over the past 10 weeks.

### Contributor diversity

This practice describes the diversity in the contributing community for a specific repository. It is measured by looking at the rate of new contributors, the rate of contribution per contributor, the total number of contributors, and the contributor trend.

The following features of Contributor Diversity are measured:

* Total Contributors - The total number of contributors.
* Contributor Trend - The change in contributors, averaged over 10 weeks.
* New Contributors - How many new contributors (with their first merged pull request within the past year) a repository has.
* Developers per Commit - How many developers there are per commit.
* Contribution Skew - The contribution skewness in terms of how many pull requests were contributed by one-time contributors, or a few very active contributors. The raw score is non-linear and varies between 0.5 and 1.0, where values > 0.8 mean contributions are distributed on many contributors, and scores < 0.6 mean that very few contributors developed most of the project.

### Contributor activity

This practice describes how active the contributors of a repository are. It is measured with features that analyze the current volume of commits, closed issues, pull requests, and the trend of said volume.

The following features of Contributor Activity are measured:

* Recent Commits - How many new commits have been made to the master branch within the last 10 weeks.
* Commits Trend - The linear change in commits per week for the past 21 weeks (whether it is increasing or decreasing).
* Recent Pull Requests - How many new pull requests have been made within the last 10 weeks.
* Pull Requests Trend - The linear change in pull requests per week for the past 21 weeks (whether it is increasing or decreasing).
* Recently Closed Issues -How many issues have been closed within the past 10 weeks.
* Closed Issues Trend - The linear change in closed issues per week for the past 21 weeks (whether it is increasing or decreasing).

### Core team commitment

This practice describes how committed the core team is to the project. The following features of Core Team Commitment are measured:

* Recent Core Team Commits - How many new commits the core team has contributed to the master branch within the past 10 weeks.
* Core Team Commits Trend - The linear trend of the number of commits the core team has made to the master branch in the last 21 weeks.
* Core Team Issue Closing - How many issues the core team has closed in the past 10 weeks.
* Recent Merges - How many pull requests have been merged in the past 10 weeks.
* Merges Trend - The linear change in merged pull requests per week for the past 21 weeks, that is, whether it is increasing or decreasing.
* Company Involvement - The highest ratio of commits from the same company in the past period of 21 weeks.

### Contributor longevity

This practice describes the longevity of the contributors. If the developers are contributing long-term, then it might be a sign that the project has been proven valuable.

The following features of Contributor Longevity are measured:

* Developer Lifetime - The average time a developer contributes regularly to the repository.
* Loyal Developer Commits - The number of commits made by long-term (loyal) developers.
