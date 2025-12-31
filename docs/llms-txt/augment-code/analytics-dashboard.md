# Source: https://docs.augmentcode.com/codereview/analytics-dashboard.md

# Analytics Dashboard

> Track code review metrics and measure the impact of Augment Code Review on your team.

## Code Review Analytics

Use the Code Review Analytics dashboard to track the review load automated by Augment, along with the comments made by Code Review that developers ultimately addressed.

1. **Navigate to Code Review** - In your browser, visit [Code Review Analytics](https://app.augmentcode.com/code-review/analytics).
2. **Filter by Date** - Refine your Analytics using the tabs for Last 7 Days, Last 30 Days, or Last 60 Days.

### Metric Definitions

* **Total PRs Reviewed**: The number of PRs that have been reviewed by Augment Code Review.
* **Total Reviews Performed**: The number of reviews that have been run by Augment Code Review. One PR can have multiple reviews if people manually trigger more reviews.
* **Total Comments**: The total number of inline comments left by Augment Code Review.
* **Percentage of Comments Addressed**: A comment is addressed if the developer resolved the concerns raised by the Augment Code Review comment. The percentage is calculated by dividing the number of addressed comments by the total number of comments left by Augment Code Review.
* **Percentage of Thumbs Up Reactions**: A thumbs up reaction is counted if a user reacts with the Thumbs Up emoji on GitHub on an inline comment left by Augment Code Review. The percentage is calculated by dividing the number of thumbs up reactions by the total number of thumbs up and thumbs down emoji reactions.
* **Estimated Dev Hours Saved**: Number of PRs multiplied by 10 minutes

### Reading the Charts

* **Addressed Comments**: A chart detailing total number of comments per day broken down by unaddressed (gray) vs addressed (green). You can interpret the green bar to mean Augment Code Review caught issues that developers fixed and may not have without the comment.
* **Reviewed PRs**: A chart detailing the total number of reviewed PRs per day (blue).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.augmentcode.com/llms.txt