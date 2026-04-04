# Source: https://virustotal.readme.io/reference/file-object-crowdsourced-ids-results.md

# crowdsourced_ids_results

IDS matches for the file.

IDS (Snort and Suricata) matches for the file. If the file it's not a PCAP, the matches are taken from a PCAP generated after running the file in a sandbox. Results are sorted by severity level, there is only one item per matched alert and every item on the list contains:

* `alert_context`: <*list of dictionaries*> context for every match of that alert:
  * `dest_ip`: <*string*> destiny IP.
  * `dest_port`: <*integer*> destination port.
  * `hostname`: <*string*> in case the alert is related to an HTTP event, destination hostname.
  * `protocol`: <*string*> communication protocol.
  * `src_ip`: <*string*> source IP.
  * `src_port`: <*integer*> source port.
  * `url`: <*string*> in case the alert is related to an HTTP event, destination URL.
* `alert_severity`: <*string*> one of `high`, `medium`, `low` or `info`.
* `rule_category`: <*string*> alert category description.
* `rule_id`: <*string*> Suricata/Snort rule SID.
* `rule_msg`: <*string*> alert description.
* `rule_source`: <*string*> rule source, determined by SID range.