# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/appendix/search-terms-ignored-further-details.md

# Search terms ignored - further details

As part of standard underlying features in Enate to optimise searches which users perform, certain commonly used terms are removed from searches if they've been manually entered. This is in order to ensure timely response for search results, plus avoid the returning of vast volumes of qualifying results which would obscure the desired results from the users. One of the approaches used for this is the use of 'Stop Lists'.

## Stop List

A stop list is a list of standard common words such as ‘and’ ‘the’, ‘me’ etc., which are ignored from searches that would otherwise return too many results.&#x20;

Below is a comprehensive list of all of the words in the stop list that ALL searches within Enate will ignore - this not only includes searches in Quickfind, but also searches which are performed for users, searches for emails, searches for Work Items e.g. for Tickets when merging Tickets etc. If you enter any of these terms, they will be auto-ignored as terms to return search results for.

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FaqRBSvFoWXuUWFtMezjn%2FEnate%20SQL%20Stop%20List.xlsx?alt=media&token=566d3255-db99-4036-ba08-62124a3452a2>" %}

Multiple Stop Lists are supported for various user languages.

{% hint style="info" %}
Note: When searching for Users and Emails, the English (British) stop list is always used. For work items (Title, Customer Name, Contract Name, Service Name, Case/Ticket Name, etc.) we use the language of the logged-on user to find the stop list. Additionally, please note that Hungarian is not directly supported by SQL, so the stop list applied for searches for Hungarian users is also the English stop list.
{% endhint %}

## Characters Ignored in Quickfind

Specific further characters are set to be ignored when performing searches in Quickfind, e.g. “\*”, “?”, “@” etc. This will mean for example that when searching for customer.com in Quickfind, the words 'customer' and 'com' would be searched for. As such, it’s recommended to place such word combinations in quotes to search for them as a specific phrase - i.e. searching for “customer.com” will likely bring back the results you are looking for.&#x20;

Below is a comprehensive list of all of the characters that searches in Quickfind will ignore:

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MdSaH4pw6gEgxw6-JX9%2F-MdSaPOm6gF11tKAu3JA%2FCharacters%20ignored%20in%20Quickfind.pdf?alt=media&token=0599d71d-22b9-4495-87ce-62addf780433>" %}
Characters ignored in Quickfind
{% endfile %}
