# Source: https://help.aikido.dev/getting-started/general-information/aikido-never-stores-your-code.md

# Aikido Never Stores Your Code

{% hint style="success" %}
In short: Aikido does not store your code after analysis has taken place. Some of the analysis jobs such as SAST or Secrets Detection require a git clone operation. Below we talk about the technical measures we take to ensure your code is protected:
{% endhint %}

* We perform different actions such as git clones in a fresh docker container for each repository. After analysis, the data is wiped and the docker container is terminated.
* For GitHub, no refresh or access tokens are ever stored in our database. We use the new GitHub Apps which do not require this. Even a database breach of Aikido itself would not result in your GitHub code being downloadable.
* By default, our integrations require a very minimal read-only scope. Only if you enable special features such as Autofix Pull Requests, Aikido will request write accesses.
* If you want to keep your code completely on-premise, without ever leaving your environment, you can use our [Local Scanner](https://help.aikido.dev/category/aikido-local-scan-setup/sg4xF4OsJciW). The results will seamlessly populate on the Aikido platform.
* Aikido has SOC2 Type 2 & ISO27001:2022 certification. A report is available [upon request](http://trustcenter.aikido.dev/). That means we adhere to several organizational and technical policies by default.
* Aikido runs AWS, with data residency in the EU and US region.That means all processing and storage will stay in that location.

The process we use to ensure code security:

![Secure repository scanning workflow: select, clone, scan, encrypt findings, destroy containers.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0acaf4018cdcba7833afcf08271e7f8c9ceeda00%2Faikido-never-stores-your-code_411acc55-32e2-4db5-88e5-c26b0896eb7a.png?alt=media)

**Disclaimer.**

Aikido has some features where certain parts of your code are stored. This is in the case for the following functionalities:

* AutoFix: Aikido stores the diffs (original and AutoFixed code) - only files that are part of the AutoFix
* Aikido stores the calltree for each AutoTriaged SAST finding for up to 2 weeks

All code that is stored is ran through Gitleaks. If there are any obvious secrets in the code, we make sure to definitely not store these.
