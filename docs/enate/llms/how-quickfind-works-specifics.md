# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/quickfind/how-quickfind-works-specifics.md

# How Quickfind works - specifics

Some further explanation of how Quickfind works: There are three different kinds of searches going on in parallel when you are entering Quickfind search data:

**1) Specific search against reference number**. This is based upon recognizing a known format of the system’s refence number for work items and then returning results related to Tickets, Cases, Actions which have that reference. You can just type the reference, e.g. ‘40308-T’ and the system will recognize it as a reference. You don’t need to enter a leading short code.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MjA3OoT2nCAxbsV8dQa%2F-MjA65fGB-pu1C0DIa9Z%2Fimage.png?alt=media\&token=8b85eab4-af1b-4fa3-bd0c-3e480f5e91c9)

Note: There's also support for certain formats of your own internal reference numbers. Specifically, Quickfind will recognize text  strings made up of a series of digits and a '.' decimal point marker, up to 10 digit characters, i.e. with the format 'NNNNN.NNNNN', no matter where the '.' character appears within this string.

**2) Custom Data Field** searches. As described above. The system will know to do this kind of search when you enter a known short code, e.g. ‘FN: ’. The search will be for a field which contains the specific value you enter. See further note below on Wildcards.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MjA0xUKb944CbFdMH4z%2F-MjA36E-nGuNRGMyCEXG%2Fimage.png?alt=media\&token=d586e10b-2088-4540-9020-4efb777cc07c)

**3) Free text searching for work items, communications and people** against anything else you enter which doesn’t conform to the first two types of recognized data. The system free text searches the individual words against various system attributes of work items, communication and people, e.g. work item title, email subject and body.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MjA0xUKb944CbFdMH4z%2F-MjA3Jbz3yVxTkjjN9uA%2Fimage.png?alt=media\&token=8ce6f61c-4dbb-4741-97c1-63b14de261e6)

**4) 'Start with' searching for files** - the system uses 'start with' logic for searching for files where it adds a wildcard to the END of search texts. This means that if you are searching for a file called 'Invoice Processing.docx', searches for 'processing' would not find the file, but searches for 'invoice' would.

## Wildcards for open searching <a href="#a-wildcards-for-open-searching" id="a-wildcards-for-open-searching"></a>

When searching, the system will add a wildcard to the END of search texts, but not the start.

For Custom Data Searches specifically, an example of behaviour would be:\
searching for e.g. “p:John Smi” would find items with the value “John Smith” in a field ‘person’ but searching just for “p:Smith” would NOT find it.

In short: With Custom Data Field searches, we’re searching for the precise value of the field, or the start of the value. Free text searches aren’t *quite* the same as this, since a free text search will try to match against each individual word within a text value to get a match, rather than the value as a whole.

Wildcards are added to the end of reference number searches also.

### **Running Wildcards while typing** <a href="#running-wildcards-while-typing" id="running-wildcards-while-typing"></a>

While you are typing in Quickfind, the system will wildcard search against the very last word, e.g. if you’re free text search typing: "John return prio", the system will wildcard the last word and would also bring back results with e.g. ‘priority’.

Once you’ve pressed the space bar the system will conclude you’ve finished typing that word and will search against it without a trailing wildcard.

## Other search terms ignored <a href="#b-other-search-terms-ignored" id="b-other-search-terms-ignored"></a>

In order to retain system performance, the following are ignored from searches:

* Words of 1 to 2 characters.
* Words in the system 'Stop List'. These are standard common words such as ‘and’ ‘the’, ‘me’ etc., which would otherwise return too many results. Please see here for the [full stop list of words which are ignored in searches](https://docs.enate.net/enate-help/work-manager/appendix/search-terms-ignored-further-details#stop-list) (in Quickfind and indeed in any other system searches).
* Specific characters which are set to be ignored, e.g. “\*”, “?”, “@” etc. in Quckfind specifically. Please see here for a [full list of the characters which are ignored](https://docs.enate.net/enate-help/work-manager/appendix/search-terms-ignored-further-details#characters-ignored-in-quickfind). This will mean for example that when searching for customer.com in Quickfind, the words 'customer' and 'com' would be searched for. As such, it’s recommended to place such word combinations in quotes to search for them as a specific phrase - i.e. searching for “customer.com” will likely bring back the results you are looking for.&#x20;

## Further things to note for Quickfind&#x20;

Quickfind is a text-driven search. Entering dates in the text strings may bring back inconsistent results. Use “quotes” where possible if such searching is necessary to help the search look for entire strings of characters such as "search for where this entire string occurs".&#x20;

Use the date sliders to search for results in specific date ranges.&#x20;

When searching for multiple words, the search will be using an ‘AND’ logic rather than ‘OR’, i.e. bring back items with 'Apple' AND 'Banana' AND 'Pear'.&#x20;

## Specifics of Searches against Work Items vs Emails&#x20;

It’s important to note that Quickfind performs three independent searches,&#x20;

* one for for work items (Cases, Actions, Tickets),&#x20;
* one for the Emails that may relate to them, and&#x20;
* one for people. &#x20;

An effect of this can be that if you are e.g. searching against a combination of three words, e.g. 'apple' and 'banana' and 'pear', Quickfind will return results of any work items where all three words occur, and separately any emails where all three words occur. Situations where two of the words appear in the work item, and the third only in an associated email, would NOT be brought back by either search.&#x20;

The specific attributes which the work item searches are performed against are as follows:&#x20;

* Work Item Reference&#x20;
* Title&#x20;
* Customer Name&#x20;
* Supplier Name&#x20;
* Contract Name&#x20;
* Service Name&#x20;
* Service Line Name&#x20;
* Process Type Name&#x20;

The specific attributes which the Communications searches are performed against are as follows:&#x20;

* Email Title&#x20;
* Email Body&#x20;
* Email Addresses (From, To, CC, BCC)&#x20;
* Internal Note Body (for notes added in Enate / Self Service).&#x20;
