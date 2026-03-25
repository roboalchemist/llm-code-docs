# Source: https://virustotal.readme.io/docs/when-analysis-feeds.md

# When is an analysis included in the feeds?

The VirusTotal feeds include entries for it resources (files, URLs, domains or sandboxes, depending on the specific feed) based on the following events:

1. Initial Submission: A resource generates an entry in the feed when it is first submitted to VirusTotal for analysis. This initial entry contains the analysis results and the fundamental properties of the resource.

2. Re-analysis: A resource generates a new entry in the feed each time it is subsequently re-analyzed by VirusTotal.

When a resource entry appears due to re-analysis, it contains the updated information gathered from this latest analysis. Importantly, this entry also includes the original, unchanging basic properties of the resource, consistent with the first time it was seen.

Notice however that submitter is not present in all entries, it will be absent when resources are submitted via the web interface without triggering a new analysis due to recent submissions, or when resources are re-analyzed by VirusTotal without being submitted by some external user.