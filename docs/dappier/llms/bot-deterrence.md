# Bot Deterrence
Source: https://docs.dappier.com/bot-deterrence



Bots are automated programs that perform tasks on the internet. While some bots, like search engine crawlers, are beneficial, others, like scrapers and spammers, can harm your site.

Bad bots can cause massive problems for web properties. Too much bot traffic can put a heavy load on web servers, slowing or denying service to legitimate users (DDoS attacks are an extreme version of this scenario). Bad bots can also scrape or download content from a website, steal user credentials, take over user accounts, rapidly post spam content, and perform various other kinds of attacks. Bot management is necessary to prevent these performance and security impacts on websites, applications, and APIs, by leveraging a range of security, machine learning, and web development technologies to accurately detect bots and block malicious activity while allowing legitimate bots to operate uninterrupted.

**What are the bot detection techniques?**

Some of the popular bot detection techniques include

* Browser fingerprinting – this refers to information that is gathered about a computing device for identification purposes (any browser will pass on specific data points to the connected website’s servers, such as your operating system, language, plugins, fonts, hardware, etc.)
* Browser consistency – checking the presence of specific features that should or should not be in a browser. This can be done by executing certain JavaScript requests.
* Behavioral inconsistencies – this involves behavioral analysis of nonlinear mouse movements, rapid button and mouse clicks, repetitive patterns, average page time, average requests per page, and similar bot behavior.
* CAPTCHA – a popular anti-bot measure, is a challenge-response type of test that often asks you to fill in correct codes or identify objects in pictures.

**Best Practices for Bot Deterrence**

* Create a robots.txt file for your website. A good starting point might be to provide crawling instructions for bots accessing your website's resources. See these examples of Google's robots.txt file.
* Implement CAPTCHAs: Use CAPTCHAs to distinguish between human users and bots.
* Rate Limiting: Set limits on the number of requests a user can make in a given timeframe.
* Regular Monitoring: Continuously monitor traffic and update your security settings to stay ahead of bot activity.
* Set up a web application firewall (WAF). WAFs can be used to filter out suspicious requests and block IP addresses based on various factors
* Use honeypot traps. Honeypots are specifically designed to attract unwanted or malicious bots, allowing websites to detect bots and ban their IP addresses.

**Cloudflare Bot Solutions**

Cloudflare Bot Solutions offer comprehensive protection against malicious bots that can disrupt your website's performance and security. By leveraging Cloudflare's global network and advanced machine learning algorithms, you can effectively detect and deter unwanted bot traffic, ensuring a seamless experience for your legitimate users.

Key Features:

1. Bot Fight Mode:

* Active Defense: Automatically detects and mitigates bot traffic by deploying challenge-response tests.
* Ease of Use: Simple to enable from the Cloudflare dashboard, providing immediate protection without complex configurations.

2. Bot Management:

* Machine Learning Algorithms: Uses sophisticated machine learning to differentiate between good and bad bots.
* Behavioral Analysis: Monitors traffic patterns to identify and block suspicious activities in real-time.
* Custom Rules: Allows you to create custom rules to address specific bot threats tailored to your business needs.

3. Threat Intelligence:

* Global Insights: Utilizes data from Cloudflare's extensive network to stay ahead of evolving bot threats.
* Updated Databases: Regularly updates bot databases to include new and emerging bot patterns, ensuring up-to-date protection.

4. Analytics and Reporting:

* Detailed Insights: Provides comprehensive analytics and reports on bot traffic, helping you understand the impact and adjust defenses accordingly.
* User-friendly Dashboard: Easy-to-navigate dashboard where you can monitor bot activity and manage your settings.

**How to Implement Cloudflare Bot Solutions**

* Sign Up and Add Your Site:
  Create an account on Cloudflare and add your domain. Follow the prompts to configure your DNS settings.
* Enable Bot Fight Mode: Navigate to the Firewall section in the Cloudflare dashboard and toggle on Bot Fight Mode. This feature will start protecting your site immediately.
  <img src="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-bot-navigate.png?fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=320cf57f102475c9c701fe30da547821" alt="" data-og-width="265" width="265" data-og-height="433" height="433" data-path="images/cf-bot-navigate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-bot-navigate.png?w=280&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=553fbb8f2ee5d2a1cbebf063154400d3 280w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-bot-navigate.png?w=560&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=69349661c280e6697c78caff03b9f75d 560w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-bot-navigate.png?w=840&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=e3fb3a36458faf76eea5fd4709a4e425 840w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-bot-navigate.png?w=1100&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=0de0c9f773a9b9f643e17a8b653398b4 1100w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-bot-navigate.png?w=1650&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=7ae58e1ea2a576693f7464620c21e7d4 1650w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-bot-navigate.png?w=2500&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=fc34b305c7192b047dee8e15135e0737 2500w" />

Activate Bot Fight Mode and Block AI Scrapers and Crawlers if not enabled already
<img src="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-bot-enable.png?fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=1c9b91f65dc7230a8a71f1e67da64066" alt="" data-og-width="699" width="699" data-og-height="325" height="325" data-path="images/cf-bot-enable.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-bot-enable.png?w=280&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=46a2ea12d8e1de1a0aa8986ef7a8380b 280w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-bot-enable.png?w=560&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=af0489692f27720a1c4979719c6c9e99 560w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-bot-enable.png?w=840&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=f5771a64825e06c41755ab3fcbe6ef19 840w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-bot-enable.png?w=1100&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=4da638941d169d1772e557d1baffc330 1100w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-bot-enable.png?w=1650&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=c00a9ae60e8289aad0eff0849293279a 1650w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-bot-enable.png?w=2500&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=be990fe38a97dba14441cb3825a82ca1 2500w" />

* Configure Bot Management:
  Access the Bot Management section to set up advanced rules and customize your bot protection strategy. Use the provided analytics to monitor bot activity and adjust settings as needed.
* Monitor and Adjust:
  Regularly check the Cloudflare dashboard for updates on bot traffic and make necessary adjustments to your bot management rules to keep your site protected against new threats.
  <img src="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-monitor-1.png?fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=befbd4ae5e543c975df8e417ea2f3421" alt="" data-og-width="252" width="252" data-og-height="194" height="194" data-path="images/cf-monitor-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-monitor-1.png?w=280&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=51da698de14e896a6e8aa8df3bb9291d 280w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-monitor-1.png?w=560&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=0ef90ba1f88f8efc1dded233e64821f3 560w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-monitor-1.png?w=840&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=83923a87de6ff59f48749e66bb81a7f6 840w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-monitor-1.png?w=1100&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=184e005804e79622125ffc5436be111f 1100w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-monitor-1.png?w=1650&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=3b4c12cee2f3a6f3f0e33241adb543c7 1650w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-monitor-1.png?w=2500&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=a4a638a4ef515ef410217797440f3040 2500w" />
  The dashboard gives information about threats and bots identified by Cloudflare
  <img src="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-monitor-2.png?fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=5436ca736013fc20f69de1f2cf7b0cd1" alt="" data-og-width="742" width="742" data-og-height="440" height="440" data-path="images/cf-monitor-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-monitor-2.png?w=280&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=6ed8bed263a087f251ac71d636fccfea 280w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-monitor-2.png?w=560&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=7a24d7b0e4e5c94fe72f137fca4361de 560w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-monitor-2.png?w=840&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=eeedc8f662079d17bc89880529cd63fa 840w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-monitor-2.png?w=1100&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=665821f5f945d1d70c8e37b78d1d1b61 1100w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-monitor-2.png?w=1650&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=b5b800a8702933b7de15ea164abb99ca 1650w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-monitor-2.png?w=2500&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=7e6eaf1528d38b79f63f4ac5a2fefae6 2500w" />

**Bot detection using AWS WAF**

AWS WAF is a web application firewall that helps protect your web applications from common web exploits that could affect application availability, compromise security, or consume excessive resources. With AWS WAF, you can create rules to filter web traffic based on various conditions, including IP addresses, HTTP headers, URI strings, and the origin of the requests.

To begin using AWS WAF, follow these steps:

1. Create a Web ACL (Access Control List):
   Navigate to the AWS WAF & Shield console.
   <img src="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-3.png?fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=0ebc29513a527572f8f8a04024a9fe9f" alt="" data-og-width="631" width="631" data-og-height="85" height="85" data-path="images/cf-waf-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-3.png?w=280&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=550be9bdf4065cc5266ac88bdf121715 280w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-3.png?w=560&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=d2557b114d36fcc4175b3df35f368219 560w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-3.png?w=840&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=7622ef60b7b4c13732836f612e0c506c 840w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-3.png?w=1100&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=80a6fac0ddc46676a83a588df8f15dd0 1100w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-3.png?w=1650&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=e8aec4a847defc735d7b21855136e6d6 1650w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-3.png?w=2500&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=eafa78894bdbcf4ac5d225f43891db77 2500w" />
   Create a new Web ACL and associate it with your CloudFront distribution, API Gateway, or ALB (Application Load Balancer).
   <img src="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-2.png?fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=f40d786c76aa726826c894ad2035410e" alt="" data-og-width="1619" width="1619" data-og-height="561" height="561" data-path="images/cf-waf-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-2.png?w=280&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=1cfe79c5efae1402ad8b55e511c1072a 280w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-2.png?w=560&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=b21963b87dbeba98c8f97ad9ffa6257a 560w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-2.png?w=840&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=7078b41835f99aa54cc01114e6c288f9 840w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-2.png?w=1100&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=2c914a2a0ef2156c438e234fb55b78ac 1100w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-2.png?w=1650&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=27066ebaee6ae8f7d1d0686091bc110e 1650w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-2.png?w=2500&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=564e9b7b5e9e7f22e9f5d7b410d6bd7a 2500w" />
   <img src="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-4.png?fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=c47d9078d7dc54f3f898861eb1239f86" alt="" data-og-width="1136" width="1136" data-og-height="684" height="684" data-path="images/cf-waf-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-4.png?w=280&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=69e67fa829177a721fe0a4b8d202b0ec 280w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-4.png?w=560&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=d7b021692329e5b0e3008a41156ce650 560w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-4.png?w=840&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=10114da8ed245c2cbaf8e9600e9f3428 840w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-4.png?w=1100&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=faed0c22021faca611f9d2631ebfa1e7 1100w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-4.png?w=1650&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=976c455a50033b36148fde08540d6f20 1650w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-4.png?w=2500&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=367e7f095e01a29b3a936bdaeea15bd2 2500w" />
   Add AWS resources that need to be monitored
   <img src="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-5.png?fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=f065e099bf836306c797b542b9b34b3b" alt="" data-og-width="708" width="708" data-og-height="221" height="221" data-path="images/cf-waf-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-5.png?w=280&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=efbc052ae81484bec3a1bc2e116178ba 280w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-5.png?w=560&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=f654e8d7f4ac919b6f12686c6af15cdf 560w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-5.png?w=840&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=6157073e77b2058fa072b13bbfe760ab 840w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-5.png?w=1100&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=32ed888cacfe5fe68cd1cf332e8d26b1 1100w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-5.png?w=1650&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=5361d6b20bdf9f6042a0e03e9b2d6383 1650w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-5.png?w=2500&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=47e1fbdf75cac51e97dff8e133dfcc3b 2500w" />
2. Add Rules to Detect Bots:

* User-Agent Filtering: Add a custom rule to inspect the User-Agent header. You can block requests with known bot User-Agent strings or allow only specific User-Agent strings.

* Rate-Based Rules: Use rate-based rules to limit the number of requests from a single IP address. This can help mitigate bots that generate high volumes of traffic.

* AWS Managed Rules: Utilize AWS Managed Rules for bots and scraping detection. AWS offers a Bot Control rule group that specifically targets known bot traffic.
  <img src="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-6.png?fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=41c51fa5d9ac17a0f615fed576724393" alt="" data-og-width="748" width="748" data-og-height="423" height="423" data-path="images/cf-waf-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-6.png?w=280&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=fa6c82a752a4200c4ec7291856874fbb 280w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-6.png?w=560&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=3b6bfe5dd138ba4ddd6f59e13e1f6d98 560w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-6.png?w=840&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=27fbcdaf0740238dbfd30221e9ad9757 840w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-6.png?w=1100&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=0b31af0bff6fa88a238aaa733aa31a68 1100w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-6.png?w=1650&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=1ee931e77692fc745a39e4eeb640063e 1650w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-6.png?w=2500&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=51dd3f942db7ff1497eef41ca9f9d1e2 2500w" />
  You can choose AWS Managed Rules to begin with and configure to block bots depending on configurations.
  <img src="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-7.png?fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=92c611932f917b7bfc2a4a9b3aef3bfe" alt="" data-og-width="678" width="678" data-og-height="507" height="507" data-path="images/cf-waf-7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-7.png?w=280&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=7a20fc93c4c605ff3e8a0daabefcd5ee 280w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-7.png?w=560&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=5a0609a1619728c2b68db57629f9e095 560w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-7.png?w=840&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=9bf97f6f99e61d2eca6a3d34224e4f9b 840w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-7.png?w=1100&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=3ee44b280518fe54add772ba9d577fef 1100w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-7.png?w=1650&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=f0493435bfee0fe24c85be0f1e619bfc 1650w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-7.png?w=2500&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=1d7451be0a2910c84b889367821b6d83 2500w" />

* Click on “Add to web ACL” and edit to add required configurations
  <img src="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-8.png?fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=42d5b06732a5afe6b7e7f7229c7c1d24" alt="" data-og-width="711" width="711" data-og-height="471" height="471" data-path="images/cf-waf-8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-8.png?w=280&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=f2df1281bd28e7805d287d77beb15353 280w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-8.png?w=560&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=46bffcde4d8d4ebe505f485e0e3b421b 560w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-8.png?w=840&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=fd7371c00713e30a225a346e578f15c1 840w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-8.png?w=1100&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=5ea38b32b69fe8f3b64d90f65ff51ff8 1100w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-8.png?w=1650&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=7f25e173d14fd03a33fcd031374b3fa3 1650w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-8.png?w=2500&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=6a00d9b7e7b4d6f878abc32d0b450dda 2500w" />

* You can choose multiple categories based on your requirements to block the bots
  <img src="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-9.png?fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=5c61e743b1abe75436c8839665d20a87" alt="" data-og-width="672" width="672" data-og-height="687" height="687" data-path="images/cf-waf-9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-9.png?w=280&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=88fd6cdca438b29a4f1a032f67c8ad8e 280w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-9.png?w=560&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=fd31313e43f3b7d1d98482dedc5de56e 560w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-9.png?w=840&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=d312536ad918afe52dec424d1b8cb25d 840w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-9.png?w=1100&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=76abb6812a9b430c3edf20eec1b44562 1100w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-9.png?w=1650&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=e451147bf3163b841e909df7c3367f19 1650w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-9.png?w=2500&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=9108e43514dc05d3303a592a692646b6 2500w" />

* Once the rules are added, monitoring can be done using the bot control dashboard
  <img src="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-10.png?fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=9fdc5d3eab10a21efefb1a6d95067e68" alt="" data-og-width="141" width="141" data-og-height="150" height="150" data-path="images/cf-waf-10.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-10.png?w=280&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=2712a92e72a431550e6e71d126c2f59e 280w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-10.png?w=560&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=63d79deb519073ad9d92be48b5c8c674 560w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-10.png?w=840&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=bae994197cfaac4ba789df23d604f6de 840w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-10.png?w=1100&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=82a53e60bb85cae94a128bebbf5d96db 1100w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-10.png?w=1650&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=d6892c190b25cf3632834afc45219ac9 1650w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/cf-waf-10.png?w=2500&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=80e1b3579d23d170cde74fb37acad914 2500w" />

**Boilerplate for robots.txt**

In the below example, currently known AI data scrapers and undocumented AI agents are blocked. You can use it as a starting point and manually customize it as needed.

```
User-agent: Applebot-Extended
Disallow: /


User-agent: Bytespider
Disallow: /


User-agent: CCBot
Disallow: /


User-agent: ClaudeBot
Disallow: /


User-agent: Diffbot
Disallow: /


User-agent: FacebookBot
Disallow: /


User-agent: Google-Extended
Disallow: /


User-agent: GPTBot
Disallow: /


User-agent: Meta-ExternalAgent
Disallow: /


User-agent: omgili
Disallow: /


User-agent: Timpibot
Disallow: /


User-agent: anthropic-ai
Disallow: /


User-agent: Claude-Web
Disallow: /


User-agent: cohere-ai
Disallow: /
```

You can validate robots.txt using [this](https://technicalseo.com/tools/robots-txt/) online service.