# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/guides/export-developer-data

Atlas is useful for analyzing developer data sources like GitHub. By visualizing this data in interactive maps, teams can discover patterns in bug reports, feature requests, and system behavior to help guide development priorities.

## GitHub​

Before exporting data, set up authentication:

```
# Using GitHub CLIgh auth login# Using GitHub API directlyexport GITHUB_TOKEN="your_token_here"
```

### Issues​

Export issues with multiple methods:

```
# Using GitHub CLI (recommended)gh issue list \  --repo owner/repo \  --json number,title,body,created_at,closed_at,labels,assignees,author \  --limit 1000 \  > issues.json# Using GitHub APIcurl -H "Authorization: token $GITHUB_TOKEN" \     "https://api.github.com/repos/owner/repo/issues?state=all&per_page=100" \     > issues.json
```

### Pull Requests​

```
# Using GitHub CLIgh pr list \  --repo owner/repo \  --json number,title,body,created_at,merged_at,state,reviewers,author \  --limit 1000 \  > pull_requests.json# Using GitHub APIcurl -H "Authorization: token $GITHUB_TOKEN" \     "https://api.github.com/repos/owner/repo/pulls?state=all&per_page=100" \     > pull_requests.json
```

### Commits​

```
# Using GitHub CLIgh api \  repos/owner/repo/commits \  --paginate \  > commits.json# Using Git CLI (for local repository)git log --pretty=format:'{%n  "commit": "%H",%n  "author": "%an",%n  "date": "%ad",%n  "message": "%s"%n}' \  --date=iso \  > commits.json# Using GitHub APIcurl -H "Authorization: token $GITHUB_TOKEN" \     "https://api.github.com/repos/owner/repo/commits?per_page=100" \     > commits.json
```

### Repository Statistics​

```
# Code frequencycurl -H "Authorization: token $GITHUB_TOKEN" \     "https://api.github.com/repos/owner/repo/stats/code_frequency" \     > code_frequency.json# Commit activitycurl -H "Authorization: token $GITHUB_TOKEN" \     "https://api.github.com/repos/owner/repo/stats/commit_activity" \     > commit_activity.json# Contributors statisticscurl -H "Authorization: token $GITHUB_TOKEN" \     "https://api.github.com/repos/owner/repo/stats/contributors" \     > contributors.json
```

See the GitHub CLI documentation and GitHub REST API documentation for more information.

- GitHubIssuesPull RequestsCommitsRepository Statistics
- Issues
- Pull Requests
- Commits
- Repository Statistics
