# Source: https://virustotal.readme.io/reference/vote-object.md

# Votes

vote objects

* `attributes`: data about a specific vote.
  * `date`: when the vote was done.
  * `value`: weight given by this vote (positive or negative) for Community Score.
  * `verdict`: note if vote was for making it "malicious" or "harmless".
* `id`: resource identifier of the vote.
* `links`: contains "self", with a link to the vote itself.
* `type`: value is "vote", that is the object type.

```json
{
  "attributes": {"date": <int:timestamp>,
                 "value": <int>,
                 "verdict": "<string>"},
  "id": "<string>",
  "links": {"self": "<string>"},
  "type": "vote"
}
```