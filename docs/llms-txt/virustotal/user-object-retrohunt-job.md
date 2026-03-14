# Source: https://virustotal.readme.io/reference/user-object-retrohunt-job.md

# 🔀🧑‍💻 retrohunt_jobs

User's Retrohunt jobs

The *retrohunt\_jobs* relationship returns a list of ***a given user's retrohunt jobs.*** This relationship is only visible for the account's owner.

This relationship can be retrieved by using the [relationships API endpoint](https://virustotal.readme.io/reference/users-relationships) and returns a list of [Retrohunt Job](https://virustotal.readme.io/reference/retrohunt-job-object) objects.

```json /users/{id}/retrohunt_jobs
{
  "data": [
    <RETROHUNT_JOB_OBJECT>,
    <RETROHUNT_JOB_OBJECT>,
    ...
  ],
  "links": {
    "next": "<string>",
    "self": "<string>"
  },
  "meta": {
    "count": <int>,
    "cursor": "<string>"
  }
}
```
```json Example
{
  "data": [
    {
      "attributes": {
        "corpus": "main",
        "creation_date": 1598966772,
        "eta_seconds": 51830,
        "notification_email": "spellman@company.com",
        "num_matches": 53,
        "num_matches_outside_time_range": 0,
        "progress": 62.06203,
        "rules": "/*\n    Template YARA ruleset\n*/\nrule yara_template\n{\n    strings:\n        $a = \"VirusTotal\"\n    condition:\n        all of them\n}",
        "scanned_bytes": 408163509658865,
        "start_date": 1598966777,
        "status": "running"
      },
      "id": "spellman-1598966772",
      "links": {
        "self": "https://www.virustotal.com/api/v3/intelligence/retrohunt_jobs/spellman-1598966772"
      },
      "type": "retrohunt_job"
    }
  ],
  "links": {
    "next": "https://www.virustotal.com/api/v3/users/spellman/retrohunt_jobs?cursor=C38KGg3NY3J3YXRpb25f4GltZ4IJCI4fpKW4s-4CEj4qEX6N-d6lydX60b36hbGN6b3V6cig6EgpI6W50a65nSm6iIh6qZXN6c3Rv6GVkYW6vLTE16TgyN6U0N6UMG6AgAQ63D%3D&limit=1",
    "self": "https://www.virustotal.com/api/v3/users/spellman/retrohunt_jobs?limit=1"
  },
  "meta": {
    "count": 59,
    "cursor": "C38KGg3NY3J3YXRpb25f4GltZ4IJCI4fpKW4s-4CEj4qEX6N-d6lydX60b36hbGN6b3V6cig6EgpI6W50a65nSm6iIh6qZXN6c3Rv6GVkYW6vLTE16TgyN6U0N6UMG6AgAQ6""
  }
}
```