# Source: https://virustotal.readme.io/reference/attack-technique-object-attack-tactics.md

# 🔀 attack_tactics

Attack technique's tactics.

The *attack\_tactics* relationship returns the list of ***all attack tactics where the technique appears***.

This relationship can be retrieved using the [relationships API](https://virustotal.readme.io/reference/get-attack-techniques-relationship) endpoint. The response contains a list of [Attack Tactic](https://virustotal.readme.io/reference/attack-tactics) objects.

```json /attack_techniques/{id}/attack_tactics
{
  "data": [
    <ATTACK_TACTIC_OBJECT>,
    <ATTACK_TACTIC_OBJECT>,
    ...
  ],
  "links": {
    "next": <string>,
    "self": <string>
  },
  "meta": {
    "count": <int>,
    "cursor": <string>
  }
}
```
```json Example
{
  "meta": {
    "count": 1
  },
  "data": [
    {
      "attributes": {
        "description": "The adversary is trying to move through your environment.\n\nLateral movement consists of techniques that enable an adversary to access and control remote systems on a network and could, but does not necessarily, include execution of tools on remote systems. The lateral movement techniques could allow an adversary to gather information from a system without needing additional tools, such as a remote access tool.",
        "creation_date": 1539735260,
        "link": "https://attack.mitre.org/tactics/TA0033/",
        "stix_id": "x-mitre-tactic--7be441c2-0095-4b1e-8125-fa8ffda29b0f",
        "last_modification_date": 1580133937,
        "name": "Lateral Movement"
      },
      "type": "attack_tactic",
      "id": "TA0033",
      "links": {
        "self": "https://www.virustotal.com/api/v3/attack_tactics/TA0033"
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/attack_techniques/T1428/attack_tactics?limit=10"
  }
}
```