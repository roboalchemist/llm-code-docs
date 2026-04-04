# Source: https://docs.debricked.com/tips-and-tricks/workarounds/scanning-a-repository-with-different-services.md

# Scanning a repository with different services

Debricked can handle “multiple services” in the same repository. It is common to have monorepositories with different deployments/microservices/etc. in them, but they should be logically separated in the Debricked UI. \
\
This is easy to do through the CLI. Have a look at this repository to learn how:

<https://github.com/Debricked-Community/debricked-split-repo>

This is how the base action looks. Debricked suggests splitting this into two separate actions to get a better overview of what service triggers what rules, and potentially only run the scans on changes in each service:

{% @github-files/github-code-block url="<https://github.com/Debricked-Community/debricked-split-repo/blob/main/.github/workflows/debricked.yml>" %}
