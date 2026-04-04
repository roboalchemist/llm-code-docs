# Source: https://docs.mailtrap.io/email-sandbox/testing/spam-blacklist-reports.md

# Spam & Blacklist reports

### Spam Report

Go to the **Spam Analysis** tab to view the Spam Report. It contains the general score and a detailed table with spam test points and their descriptions.

[Apache SpamAssassin](https://mailtrap.io/blog/spamassassin-score/), the most popular email filter, runs numerous tests on email headers and body text and assigns a score to each of them.

A score below 5 points is considered good. If your email gets more than 5 points, it will most likely be treated as spam by various email clients. In this case, check the rules that gained the highest score and fix your email template accordingly.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-8f5379403481f939e52b03b660bac93739db5d00%2Fsandbox-spam-analysis-report.png?alt=media" alt="Spam Analysis report showing SpamAssassin score breakdown with detailed test results" width="563"></div>

### Blacklists Report

You will find the Blacklists Report in the **Spam** **Analysis** tab as well.

It checks whether your IP or domain has been listed on any of the commonly used blacklists. It shows resources that have been queried and your current status. If your domain or IP is blacklisted, click the resource name; it's hyperlinked to the blacklist website -- check their rules for delisting and follow their instructions.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-9b686c549e6408c33c9464b827cddca2755b5c5c%2Fsandbox-blacklists-report.png?alt=media" alt="Blacklists Report displaying domain and IP blacklist checking results" width="563"></div>
