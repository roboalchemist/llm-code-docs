# Source: https://virustotal.readme.io/docs/comments.md

# Comments

Build your profile & retrieve your API key

After you have signed in, you can customize your picture, tell others who you really are, set your profile phrase and much more on the page. Becoming a VirusTotal Community member gives you the right to a public API key. This key can be used to automate file and URL scans, as well as to post comments. Your public API key can be retrieved through the *Settings* menu item under your user avatar once you have signed in. Learn more about the use of this key in the [public API documentation](https://virustotal.readme.io/reference/overview).

# How to comment on files and URLs

In the *Community* tab of each URL or file scan report you'll find a section devoted to comments. We strongly encourage users to review the samples or URLs they submit and comment on them; it can be very useful information for other users.

For example, let us assume we are software developers. We have uploaded one of our programs to VirusTotal to verify whether any antivirus solution incorrectly detects it. Indeed, one of the engines flags our program as a virus. Now it's time to comment the file and tell other users that this is a false positive. Naturally, we'll provide evidence by specifying our product's site and describing the program itself.

Note that comments are file/URL specific, not report specific. In other words, your comments will not be tied to a given moment in time; your comments will appear in the reports returned by future submissions of the same file or URL.

Some ideas for the topics of your comments:

* Describe the propagation or dissemination strategy of a given malware. You may want to include any links that download the sample. (Note that comments do not allow active links. Please replace the http prefix with hxxp when referring to malicious content.)
* Offer disinfection procedures to remove the malware sample (or even better, the family to which it belongs) from your system.
* Make reverse engineering reports of malware samples.
* Notify others of false positives.

There are obviously many other possible topics for your comments. As long as they are helpful for someone, your comments will always be interesting and welcomed.

# Address your comments

If you are answering another VirusTotal Community member's file or URL comment, don't forget to address your answer to them by using the @user\_nickname syntax:

@EmilianoMartinez

# Tag your comments

File and URL comments allow custom tags. To create a custom tag, precede the tag word with a "#" symbol inside the comment (as in Twitter-like syntax). For example:

*These are the instructions to remove this family of malware from your computer, I hope you find them useful...*

*\[... Instructions ...]*

*#disinfection #zbot*

# Users can then search through comments for specific tags using the VirusTotal Intelligence *comment* modifier.

These are some of the tags that you may want to use to create a standard community syntax:

* \#malware: malicious file.
* \#goodware: harmless file.
* \#grayware: files that behave in a manner that is annoying or undesirable, and yet less serious or troublesome than malware.
* \#spam-link: file located at a spammed link or URL travelling as a link in a spam message.
* \#spam-attachment: file travelling as an attachment in spam mail.
* \#p2p-download: malware sample downloaded from a P2P network.
* \#im-propagating: malware sample propagating via instant messaging
* \#network-worm: worm that propagates through a network by making use of some vulnerability exploit (e.g. MS04-011 used by the Sasser worm), network shares or similar methods.
* \#drive-by-download: Downloads which a person authorized but without understanding the consequences (e.g. downloads which install an unknown or counterfeit executable program, ActiveX component or Java applet). Any download that happens without a person's knowledge. Download of spyware, a computer virus or any kind of malware that happens without a person's knowledge.
* \#disinfection: Instructions to disinfect a computer from the malware whose report is being rendered.
* \#malicious: intended for URL comments, states that the URL is malicious.
* \#benign: intended for URL comments, states that the URL is harmless.
* \#phishing-site: intended for URL comments, states that the site whose report is being rendered is part of a phishing scam.
* \#browser-exploit: intended for URL comments, states that the site whose report is being rendered exploits browsers to install malware without the victims' knowledge.

# Flag files and URLs as malicious or harmless

A false positive occurs when antivirus software identifies a non-malicious file as malware. A false negative is when antivirus software fails to detect a malicious file. False positives and false negatives are the main problem in antivirus detection today, and we believe that the way to counteract them is through file reputation systems.

VirusTotal has developed its own file reputation system. Whenever you submit a file or URL, you'll see a chart which shows the reputation of the file or URL and ranges from -100 (fully malicious reputation) to 100 (fully harmless reputation). The reputation of each file or URL is built by (among other factors) VirusTotal Community user votes, which are recorded by clicking either the malicious or harmless icon below the reputation chart.

Even though the user votes are not the only way reputation is generated, we do strongly encourage users to vote files and URLs as malicious or harmless if they are absolutely certain about their nature. By doing this, VirusTotal Community members help the antivirus industry in their endless battle against false positives and false negatives.