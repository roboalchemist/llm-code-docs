# Source: https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/glossary.md

# Source: https://docs.gitguardian.com/platform/glossary.md

# Glossary

> Definitions of key terms used throughout GitGuardian documentation, including workspace, incidents, detectors, and more.

Here you can find a list of some Git, GitHub and GitGuardian specific terms and concepts that we use across our documentation.

### Author vs Committer

[From Git definitions](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History):

- The author is the person who originally wrote the work
- The committer is the person who most recently applied a set of changes, for example by using commands such as `rebase` or `cherry-pick`

### Commit

A commit is a Git object. It "is an individual change to a file (or set of files)". See the [GitHub glossary](https://help.github.com/en/github/getting-started-with-github/github-glossary#commit) for a more precise definition.
Commits typically include a commit message, which provides a brief description of the changes made, the date of the commit, and the **author** and **committer** of the commit, who can be two distinct users.

### Commit author

The Git user who makes the commit.

### Commit SHA

Unique identifier of a commit created by Git. It is a 40-character checksum hash. For the sake of convenience, only the first 7 characters are usually displayed.

### Custom webhooks

Custom webhooks allow you to build dedicated integration to receive different type of events (like incidents) from GitGuardian.
It provides a way to integrate your different services with the GitGuardian alerting pipeline.

### GitHub contributor

A contributor is a GitHub user who does not have collaborator access to a repository but has contributed to a project and
had a pull request they opened merged into the repository.

### GitHub events

Every interaction between a user and GitHub is logged in a GitHub Event. The complete list of event types is available [here](https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/github-event-types)
It contains useful information, such as:

- the **actor**, the GitHub user who triggered the event (in the case of a `PushEvent`, i.e when pushing several commits on GitHub, the actor is also referred to as the **pusher**)
- the **organization** id, if the event occurred on a GitHub organization
- the **payload** which depend on the event's type
- the **repo** on which the event happened
- the **type**

### GitHub organization

GitHub organizations are a group of multiple users that typically mirror the structure of your real-world organization. GitGuardian
can monitor as many GitHub organizations and scan their associated activity.

### Git users vs GitHub Users

A commit as defined in the Git protocol, contains both an `author` and `committer`, defined by their email address and name.
For example `"Author Name <user@example.com>"` is a valid git user (either a committer or an author).
This email is configured at the git protocol level, on your developersâ computers, using the commands:

```bash
git config --global user.name "FIRST_NAME LAST_NAME"
```

```bash
git config --global user.email "MY_NAME@MY_DOMAIN.com"
```

On top of that, GitHub **sometimes** adds a GitHub author and / or committer, if it managed to link the git user to an existing GitHub user, based on the **email addresses**.
In that case, the commit also contains a GitHub login as the author and / or the committer.

### Patch and diff

A patch/diff is a git concept that represents the difference in changes between two commits, or saved changes.
The diff will visually describe what was added or removed from a file since its last commit.

### Push event

A Push Event is triggered whenever several commits are pushed on GitHub, from a local repository, and therefore its
payload contains a list of commits. That is the main type of event we monitor, since it is the one containing commits,
reflecting changes in code.

### Repository

Following [GitHub's definition](https://help.github.com/en/github/getting-started-with-github/github-glossary#repository), a repository is the most basic element of GitHub.
They are the easiest to imagine as a project's folder. A repository contains all of the project files (including documentation),
and stores each file's revision history. Repositories can have multiple collaborators and can be either public or private.

### Secret

A secret is any of the following: API keys, database connection strings, certificates.
