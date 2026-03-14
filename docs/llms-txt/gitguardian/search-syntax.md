# Source: https://docs.gitguardian.com/public-monitoring/explore/search-syntax.md

# Search syntax

> Query language and search syntax for Explore to search public GitHub commits, including boolean operators and field-specific searches.

Explore uses a powerful query language to search through public GitHub commits and patches. This guide covers the essential syntax for building effective searches to find secrets related to your organization.

## Basic search concepts

### Simple term search
Enter a term in the search bar to search across all indexed fields:

```query
yourcompany
```

### Boolean operators
Combine terms using boolean operators:

- **AND** - Both terms must be present
- **OR** - At least one term must be present  
- **NOT** - Exclude a term

**â ï¸ Boolean operators MUST be in CAPITAL LETTERS.**

```query
yourcompany AND database
yourcompany OR yourdomain
yourcompany AND NOT test
```

For complex queries mixing operators, use parentheses:
```query
(yourcompany OR yourdomain.com) AND database AND NOT test
```

## Field-specific searches

Target specific types of information by specifying which field to search:

### Common search fields

| Field | Query term | Description |
|-------|-----------|-------------|
| Patch content | `file.patch` | Search within the actual code changes |
| Author email | `commit.author.email` | Email of the code author |
| Author name | `commit.author.name` | Name of the code author |
| Author GitHub username | `author.login` | GitHub username of author |
| Committer email | `commit.committer.email` | Email of the person who committed |
| Committer name | `commit.committer.name` | Name of the person who committed |
| Committer GitHub username | `committer.login` | GitHub username of committer |
| Filename | `file.filename` | Name of the changed file |
| File extension | `file.file_extension` | Extension of the changed file |

### Basic field search examples

```query
# Search for patches from a specific email
commit.author.email: john@yourcompany.com

# Search patch content
file.patch: database

# Search across multiple fields
commit.author.email: @yourcompany.com OR file.patch: yourcompany
```

### Searching for phrases
Use quotes to search for terms that appear together:
```query
file.patch: "production database
```

### Exact keyword matching
For exact matches (case-sensitive), add `.keyword` suffix:
```query
source_metadata.repo_name.keyword: "YourCompany/api-service"
```

## Practical search examples

| What you're looking for | Query to use |
|------------------------|-------------|
| Patches containing a term | `file.patch: yourcompany` |
| Patches with multiple terms (OR) | `file.patch: yourcompany OR file.patch: yourdomain` |
| Patches with multiple terms (AND) | `file.patch: yourcompany AND file.patch: database` |
| Patches from a GitHub username | `author.login: username OR committer.login: username` |
| Patches from an email domain | `commit.author.email: @yourcompany.com OR commit.committer.email: @yourcompany.com` |
| Patches from a specific person | `(commit.author.name: "John Doe") OR (commit.committer.name: "John Doe")` |
| Patches from a user after a date | `(author.login: username OR committer.login: username) AND commit.committer.date:{2024-01-01 TO *}` |
| Patches from a user in date range | `(author.login: username OR committer.login: username) AND (commit.committer.date:{2024-01-01 TO 2024-03-31})` |
| Patches from multiple users | `(author.login: (user1 OR user2) OR committer.login: (user1 OR user2))` |
| Patches in specific repository | `source_metadata.repo_name: yourrepo` |

<details>
<summary>Advanced search capabilities</summary>

## Field types and advanced searching

Different field types support different search methods:

### Date fields
Use range operators with ISO 8601 format dates. All dates are stored in UTC.

```query
# After a date (inclusive)
source_metadata.created_at:[2024-01-01 TO *]

# Between dates (exclusive start, inclusive end)
commit.author.date:{2024-01-01 TO 2024-03-31]

# Before a date (exclusive)
commit.committer.date:[* TO 2024-01-01}
```

- Square brackets `[]` = inclusive
- Curly brackets `{}` = exclusive
- Asterisk `*` = wildcard for open-ended ranges

### Integer fields
Search numeric fields with exact values or ranges:

```query
# Exactly 10 additions
file.additions: 10

# At least 100 additions
file.additions: [100 TO *]

# Between 50 and 200 additions
file.additions: [50 TO 200]
```

### Text fields vs Keyword fields
- **Text fields** (e.g., `file.patch`): Tokenized and analyzed for flexible searching
- **Keyword fields** (e.g., `source_metadata.repo_name.keyword`): Exact match, case-sensitive

### Text field processing
Text fields like `file.patch` undergo complex processing:
- Split on special characters (/, :, =, etc.)
- Extract camelCase terms: `GitGuardian` â `git`, `guardian`, `gitguardian`
- Extract email parts: `user@company.com` â `user`, `company.com`, `user@company.com`
- Extract domain components and IP address parts
- Convert to lowercase
- Remove terms shorter than 3 characters

## Complete field reference

| Field | Type | Description |
|-------|------|-------------|
| `sha` | keyword | Commit SHA |
| `html_url` | path | GitHub commit URL |
| `author.id` | keyword | GitHub author ID |
| `author.login` | keyword | GitHub author username |
| `committer.id` | keyword | GitHub committer ID |
| `committer.login` | keyword | GitHub committer username |
| `commit.message` | text | Git commit message |
| `commit.author.email` | text | Git author email |
| `commit.author.name` | text | Git author name |
| `commit.author.date` | date | Git author date |
| `commit.committer.email` | text | Git committer email |
| `commit.committer.name` | text | Git committer name |
| `commit.committer.date` | date | Git committer date |
| `file.filename` | path | Patch filename |
| `file.patch` | text | Patch content |
| `file.file_extension` | keyword | File extension |
| `file.sha` | keyword | File SHA |
| `file.additions` | int | Lines added |
| `file.deletions` | int | Lines deleted |
| `file.changes` | int | Lines changed |
| `source_metadata.created_at` | date | GitHub processing date |
| `source_metadata.repo_id` | keyword | Repository ID |
| `source_metadata.repo_name` | text | Repository name |

**Note**: Many fields have both text and keyword versions (e.g., `commit.author.name` vs `commit.author.name.keyword`).

## Search limitations

### Text field limitations
- Cannot search terms shorter than 3 characters
- Cannot search numbers smaller than 10,000
- Cannot search special characters directly: `; , " ' ` = : / \ $ # & ~ | ^ < > { } [ ] ( ) ? ! Â§ * Â°`
- Cannot perform exact substring matching

### Subdomain searching
Domain searching has specific behavior:
- Domains with 3 or fewer levels: `file.patch: company.com` matches `api.company.com`
- Domains with more than 3 levels: requires exact match or middle subdomain search

</details>

## Building effective searches

Focus your searches on terms most likely to appear near secrets:
- **Company domains**: `yourcompany.com`, `api.yourcompany.com`
- **Email patterns**: `@yourcompany.com`, specific employee emails
- **Internal services**: database names, API endpoints, service identifiers
- **Repository names**: company-owned repositories
- **User activity**: current or former employee usernames

**Remember**: More specific searches yield more actionable results and help stay within the 10,000 result limit required for scanning.

## Search scope options

- **Entire Public GitHub**: Search across all public GitHub repositories (default)
- **Company perimeter**: Restrict searches to within your [company's public perimeter](../perimeter/overview.md)
