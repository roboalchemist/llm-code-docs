# Source: https://www.daytona.io/docs/en/git-operations.md

The Daytona SDK provides built-in Git support through the `git` module in Sandboxes. This guide covers all available Git operations and best practices.

## Basic Operations

Daytona SDK provides an option to clone, check status, and manage Git repositories in Sandboxes. You can interact with Git repositories using the `git` module.

Similarly to file operations the starting cloning dir is the current Sandbox working directory. Uses the WORKDIR specified in
the Dockerfile if present, or falling back to the user's home directory if not - e.g. `workspace/repo` implies `/my-work-dir/workspace/repo`, but you are free to provide an absolute workDir path as well (by starting the path with `/`).

### Cloning Repositories

Daytona SDK provides an option to clone Git repositories into Sandboxes using Python, TypeScript, and Ruby. You can clone public or private repositories, specific branches, and authenticate using personal access tokens.

```python
# Basic clone
sandbox.git.clone(
    url="https://github.com/user/repo.git",
    path="workspace/repo"
)

# Clone with authentication

sandbox.git.clone(
    url="https://github.com/user/repo.git",
    path="workspace/repo",
    username="git",
    password="personal_access_token"
)

# Clone specific branch

sandbox.git.clone(
    url="https://github.com/user/repo.git",
    path="workspace/repo",
    branch="develop"
)

```
```typescript
// Basic clone
await sandbox.git.clone(
    "https://github.com/user/repo.git",
    "workspace/repo"
);

// Clone with authentication
await sandbox.git.clone(
    "https://github.com/user/repo.git",
    "workspace/repo",
    undefined,
    undefined,
    "git",
    "personal_access_token"
);

// Clone specific branch
await sandbox.git.clone(
    "https://github.com/user/repo.git",
    "workspace/repo",
    "develop"
);
```


```ruby
# Basic clone
sandbox.git.clone(
  url: 'https://github.com/user/repo.git',
  path: 'workspace/repo'
)

# Clone with authentication
sandbox.git.clone(
  url: 'https://github.com/user/repo.git',
  path: 'workspace/repo',
  username: 'git',
  password: 'personal_access_token'
)

# Clone specific branch
sandbox.git.clone(
  url: 'https://github.com/user/repo.git',
  path: 'workspace/repo',
  branch: 'develop'
)
```


See: [clone (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/git.md#gitclone), [clone (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/git.md#clone), [clone (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/git.md#clone)

### Repository Status

Daytona SDK provides an option to check the status of Git repositories in Sandboxes. You can get the current branch, modified files, number of commits ahead and behind main branch using Python, TypeScript, and Ruby.

```python
# Get repository status
status = sandbox.git.status("workspace/repo")
print(f"Current branch: {status.current_branch}")
print(f"Commits ahead: {status.ahead}")
print(f"Commits behind: {status.behind}")
for file in status.file_status:
    print(f"File: {file.name}")

# List branches

response = sandbox.git.branches("workspace/repo")
for branch in response.branches:
    print(f"Branch: {branch}")

```
```typescript
// Get repository status
const status = await sandbox.git.status("workspace/repo");
console.log(`Current branch: ${status.currentBranch}`);
console.log(`Commits ahead: ${status.ahead}`);
console.log(`Commits behind: ${status.behind}`);
status.fileStatus.forEach(file => {
    console.log(`File: ${file.name}`);
});

// List branches
const response = await sandbox.git.branches("workspace/repo");
response.branches.forEach(branch => {
    console.log(`Branch: ${branch}`);
});
```


```ruby
# Get repository status
status = sandbox.git.status('workspace/repo')
puts "Current branch: #{status.current_branch}"
puts "Commits ahead: #{status.ahead}"
puts "Commits behind: #{status.behind}"
status.file_status.each do |file|
  puts "File: #{file.name}"
end

# List branches
response = sandbox.git.branches('workspace/repo')
response.branches.each do |branch|
  puts "Branch: #{branch}"
end
```


See: [status (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/git.md#gitstatus), [status (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/git.md#status), [status (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/git.md#status)

## Branch Operations

Daytona SDK provides an option to manage branches in Git repositories. You can create, switch, and delete branches.

### Managing Branches

Daytona SDK provides an option to create, switch, and delete branches in Git repositories using Python, TypeScript, and Ruby.

```python
# Create new branch
sandbox.git.create_branch("workspace/repo", "feature/new-feature")

# Switch branch

sandbox.git.checkout_branch("workspace/repo", "feature/new-feature")

# Delete branch

sandbox.git.delete_branch("workspace/repo", "feature/old-feature")

```
```typescript
// Create new branch
await sandbox.git.createBranch("workspace/repo", "feature/new-feature");

// Switch branch
await sandbox.git.checkoutBranch("workspace/repo", "feature/new-feature");

// Delete branch
await sandbox.git.deleteBranch("workspace/repo", "feature/old-feature");
```


```ruby
# Create new branch
sandbox.git.create_branch('workspace/repo', 'feature/new-feature')

# Switch branch
sandbox.git.checkout_branch('workspace/repo', 'feature/new-feature')

# Delete branch
sandbox.git.delete_branch('workspace/repo', 'feature/old-feature')
```


See: [create_branch (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/git.md#gitcreate_branch), [checkout_branch (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/git.md#gitcheckout_branch), [delete_branch (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/git.md#gitdelete_branch), [createBranch (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/git.md#createbranch), [checkoutBranch (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/git.md#checkoutbranch), [deleteBranch (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/git.md#deletebranch), [create_branch (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/git.md#create_branch), [checkout_branch (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/git.md#checkout_branch), [delete_branch (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/git.md#delete_branch)

## Staging and Committing

Daytona SDK provides an option to stage and commit changes in Git repositories. You can stage specific files, all changes, and commit with a message using Python, TypeScript, and Ruby.

### Working with Changes

```python
# Stage specific files
sandbox.git.add("workspace/repo", ["file1.txt", "file2.txt"])

# Stage all changes

sandbox.git.add("workspace/repo", ["."])

# Commit changes

sandbox.git.commit("workspace/repo", "feat: add new feature", "John Doe", "john@example.com")

```
```typescript
// Stage specific files
await sandbox.git.add("workspace/repo", ["file1.txt", "file2.txt"]);

// Stage all changes
await sandbox.git.add("workspace/repo", ["."]);

// Commit changes
await sandbox.git.commit("workspace/repo", "feat: add new feature", "John Doe", "john@example.com");
```


```ruby
# Stage specific files
sandbox.git.add('workspace/repo', ['file1.txt', 'file2.txt'])

# Stage all changes
sandbox.git.add('workspace/repo', ['.'])

# Commit changes
sandbox.git.commit('workspace/repo', 'feat: add new feature', 'John Doe', 'john@example.com')
```


See: [add (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/git.md#gitadd), [commit (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/git.md#gitcommit), [add (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/git.md#add), [commit (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/git.md#commit), [add (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/git.md#add), [commit (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/git.md#commit)

## Remote Operations

Daytona SDK provides an option to work with remote repositories in Git.

### Working with Remotes

Daytona SDK provides an option to push and pull changes using Python, TypeScript, and Ruby.

```python
# Push changes
sandbox.git.push("workspace/repo")

# Pull changes
sandbox.git.pull("workspace/repo")

```
```typescript
// Push changes
await sandbox.git.push("workspace/repo");

// Pull changes
await sandbox.git.pull("workspace/repo");
```


```ruby
# Push changes
sandbox.git.push('workspace/repo')

# Pull changes
sandbox.git.pull('workspace/repo')
```


See: [push (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/git.md#gitpush), [pull (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/git.md#gitpull), [push (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/git.md#push), [pull (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/git.md#pull), [push (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/git.md#push), [pull (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/git.md#pull)