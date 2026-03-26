# Source: https://docs.debricked.com/product/vulnerability-management/data-sources.md

# Data sources

OpenText Core SCA's algorithms constantly scan various sources for information about vulnerabilities, licenses and health data. These include (but are not limited to: the NVD Database, NPM, C# Announcement, FriendsOfPHP's security advisories, Go Vulnerability Database, PyPA Python Advisory Database, GitHub Issues, GitHub Security Advisory, mailing lists, and more. OpenText Core SCA checks the sources every 15 minutes, giving fast and accurate data.

### **Data refinement**

When the data is collected, it is cleaned up since it is often quite messy. As the sources are a combination of structured and unstructured data, there are a lot of errors in it by default.

### **CVE-parsing**

The largest source of vulnerability data is the NVD database. The problem with this source is that the CPEs (or products connected to vulnerabilities) are often mislabelled, and it is common to see a time lag of up to four weeks in assigning CPEs to CVEs. OpenText Core SCA uses natural language processing to re-classify the vulnerabilities and increase the amount of correctly classified vulnerabilities and reduce that time lag to 0 days. This is one of many data-refinement activities that is carried out 24/7 for customers.

### LLM‑based vulnerability detection

When a newly published vulnerability lacks detailed analysis from the NVD or other advisory sources, the OpenText Core SCA LLM‑based parser immediately processes the raw description to extract the technical details required to identify affected packages and versions. This enables OpenText Core SCA to surface accurate insights early, even before official advisories are complete. Once those advisories are updated, OpenText Core SCA automatically cross‑verifies the new information with existing data and updates any fields that have changed or been added.

### **Fully automated**

What distinguishes OpenText Core SCA is its innovative approach to vulnerability analysis, which eliminates the need for manual assessments. The automated analysis guarantees that once a vulnerability is detected within a data source, it is indexed, refined, and a solution is generated efficiently, all within 15 to 30 minutes.

OpenText Core SCA provides continuous monitoring for changes related to specific vulnerabilities. Our systems operate around the clock to ensure that any detected vulnerabilities are promptly addressed by your development team, minimizing potential lag. OpenText Core SCA is committed to assisting you in establishing a strong and effective security framework.

### **Scanning the code for dependencies and matching**

In the next step, OpenText Core SCA scans your projects for dependency files. This can be done in a variety of ways, for example, by CI/CD integrations (recommended), manual uploads, and OpenText Core SCA APIs.

#### **What does** OpenText Core SCA **look for?**

OpenText Core SCA essentially scans for any declared dependencies in files, such as the well-known *package-lock.json*, *composer.json* and so on. Next, this dependency file is transformed into OpenText Core SCA own internal format and is sent to the matching and rule engines. Any indirect dependencies are also built or traversed in this process.

#### **Matching and rule engines**

Following are the two pieces of software that:

* Match your vendor and name of the dependency to OpenText Core SCA internal database
* Determine the likelihood of this match being correct

It is often the case that open-source projects have similar names, share parts of names, or even have the same names but different vendors. Hence, simple regular expressions, whitelists and blacklists are not enough. OpenText Core SCA makes use of modern tech, such as machine learning, to determine the likelihood of the match being a true positive or not based on OpenText Core SCA algorithms. The accuracy of these algorithms varies depending on the language and package manager being used.&#x20;

### **A solution to your problems**

In most cases, the solution to vulnerabilities in open-source dependencies is to simply update the dependency to a later version that is not vulnerable. Often the update is easy to make, but if the ga between the versions is large enough, an update could cause breaking changes to your code. We help you figure out which version to update to by finding the smallest possible update you can do, which still fixes the vulnerability, helping you fix the problem while keeping the risk of breaking changes as low as possible.
