# Source: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/llms.txt

# Amazon Route 53 Developer Guide

> With RouteÂ 53, you can register domains, route traffic to the resources where your domains are hosted, and check the health of your resources. You can also route traffic based on the health of your resources. This guide explains how to register domains, configure DNS, and configure health checks using the RouteÂ 53 console.

- [Integration with other services](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/integration-with-other-services.html)
- [DNS domain name format](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html)
- [Creating AWS CloudFormation resources](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/creating-resources-with-cloudformation.html)
- [Sending findings to Security Hub CSPM](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/securityhub-integration.html)
- [IP address ranges](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-ip-addresses.html)
- [Tagging resources](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/tagging-resources.html)
- [Quotas](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html)
- [Related information](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Resources.html)
- [Document history](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/History.html)

## [What is Amazon RouteÂ 53?](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)

- [How domain registration works](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-domain-registration.html): If you want to create a website or a web application, you start by registering the name of your website, known as a .
- [How internet traffic is routed to your website or web application](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-dns-service.html): All computers on the internet, from your smart phone or laptop connect to the servers that serve content for massive retail websites, communicate with one another by using numbers.
- [How Amazon RouteÂ 53 checks the health of your resources](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-health-checks.html): Amazon RouteÂ 53 health checks monitor the health of your resources such as web servers and email servers.
- [Amazon RouteÂ 53 concepts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html): Describes Amazon RouteÂ 53 concepts related to registering domains, routing traffic to your resources (DNS), and checking the health of your resources.
- [How to get started with Amazon RouteÂ 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-how-to-get-started.html): For information about getting started with Amazon RouteÂ 53, see the following topics in this guide:
- [Accessing Amazon RouteÂ 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-accessing-route-53.html): You can access Amazon RouteÂ 53 in the following ways:
- [AWS Identity and Access Management](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/IAMRoute53.html): Gives an overview of how to use AWS Identity and Access Management with RouteÂ 53.
- [Amazon RouteÂ 53 pricing and billing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Route53Pricing.html): Describes the pricing for RouteÂ 53âyou only pay for your usage.
- [Working with AWS SDKs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.


## [Getting started](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html)

- [Set up](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/setting-up-route-53.html): Set up AWS for Amazon RouteÂ 53.
- [Route DNS traffic to an Amazon S3 static website](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started-s3.html): Use Amazon RouteÂ 53 to route DNS traffic for your domain to an Amazon Simple Storage Service bucket configured for static website hosting.
- [Route DNS traffic to a CloudFront distribution](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started-cloudfront-overview.html): Use Amazon RouteÂ 53 to route DNS traffic for your domain to Amazon CloudFront distributions that serve a static website stored in Amazon Simple Storage Service.


## [Registering and managing domains](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar.html)

### [Registering new domains](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register-update.html)

This section covers the following topics related to registering new domains with Amazon RouteÂ 53:

- [Registering a new domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register.html)
- [Values that you specify when you register or transfer a domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register-values-specify.html)
- [Values that Amazon RouteÂ 53 returns when you register a domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register-values-returned.html): When you register your domain with Amazon RouteÂ 53, RouteÂ 53 returns the following values in addition to the values that you specified.
- [Viewing the status of a domain registration](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-view-status.html): ICANN, the organization that maintains a central database of domain names, has developed a set of domain name status codes (also known as EPP status codes) that tell you the status of a variety of operations, for example, registering a domain name, transferring a domain name to another registrar, renewing the registration for a domain name, and so on.

### [Updating domain settings](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-update-settings.html)

Update settings for a domain that you registered with Amazon RouteÂ 53.

- [Updating contact information and ownership for a domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-update-contacts.html): Update contact information for a domain that you registered with Amazon RouteÂ 53.

### [Enabling or disabling privacy protection for contact information for a domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-privacy-protection.html)

Enable or disable privacy protection to hide or show your contact information in WHOIS queries.

- [TLDs that don't support privacy protection](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/privacy-protection-tld-support.html): List of top-level domains that do not support privacy protection for contact information.
- [Troubleshooting privacy protection issues](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/privacy-protection-troubleshooting.html): Resolve common issues with privacy protection for domain contact information.
- [Enabling or disabling automatic renewal for a domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-enable-disable-auto-renewal.html): Enable or disable automatic renewal for a domain that you registered with Amazon RouteÂ 53.
- [Locking a domain to prevent unauthorized transfer to another registrar](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-lock.html): Lock a domain that you registered with Amazon RouteÂ 53 to prevent unauthorized transfer to another registrar.
- [Extending the registration period for a domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-extend.html): Extend the registration period for a domain beyond the automatic renewal period.
- [Updating name servers to use another registrar](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register-other-dns-service.html): Update name servers for a domain to use a different DNS service provider.
- [Adding or changing name servers and glue records for a domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-name-servers-glue-records.html): Add or change name servers and glue records for a domain registered with Route 53.
- [Renewing registration for a domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-renew.html): When you register a domain with Amazon RouteÂ 53 or you transfer domain registration to RouteÂ 53, we configure the domain to renew automatically.
- [Restoring an expired or deleted domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-restore-expired.html): If you don't renew a domain before the end of the late-renewal period or if you accidentally delete the domain, for some registries for top-level domains (TLDs), you can restore the domain before it becomes available for others to register.
- [Replacing the hosted zone for a domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-replace-hosted-zone.html): If you delete the hosted zone for a domain, you need to create another hosted zone when you're ready to make the domain available on the internet.

### [Transferring domains](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer.html)

Transfer domain names to Amazon RouteÂ 53 and view the status of a transfer.

- [Choose your transfer type](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-decision-guide.html): Understand the difference between transferring domain registration to RouteÂ 53 versus using RouteÂ 53 for DNS hosting only to choose the right approach for your needs.
- [Pre-transfer checklist](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-checklist.html): Complete this checklist before transferring your domain to avoid common transfer failures.
- [Transfer to RouteÂ 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-to-route-53.html): Transfer domain registration from another registrar to Amazon RouteÂ 53 with step-by-step procedures, requirements, and authorization processes.
- [Common transfer issues](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-troubleshooting.html): Avoid common problems during active domain transfers to Amazon RouteÂ 53.
- [Transfer from RouteÂ 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-from-route-53.html): Transfer domain registration from Amazon RouteÂ 53 to another registrar with required information and DNS considerations.
- [Transfer to a different AWS account](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-between-aws-accounts.html): Transfer domain ownership between AWS accounts using the console, CLI, or programmatic methods at no cost.
- [Transfer status](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-to-route-53-status.html): Track and monitor the progress of domain transfers to Amazon RouteÂ 53 using the console and understand transfer status codes.
- [Transfer impact on domain expiration date](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-to-route-53-expiration.html): Understand how domain transfers affect expiration dates for different top-level domains and registry policies.
- [Resending authorization and confirmation emails](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-click-email-link.html): What to do if you didn't click the link in the confirmation or authorization email when you register or transfer a domain or change the registrant contact.
- [Configuring DNSSEC for a domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-configure-dnssec.html): Attackers sometimes hijack traffic to internet endpoints such as web servers by intercepting DNS queries and returning their own IP addresses to DNS resolvers in place of the actual IP addresses for those endpoints.

### [Finding your registrar](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/find-your-registrar.html)

To view domain information by using the GetDomainDetail API, you can use any of the SDKs or AWS CLI.

- [Viewing information about domains](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-whois-rdap.html)
- [Deleting a domain name registration](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-delete.html): For most top-level domains (TLDs), you can delete the registration if you no longer want it.
- [Contacting AWS Support about domain registration issues](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-contact-support.html): AWS provides a Basic support plan, free of charge, for all AWS customers.
- [Downloading a domain billing report](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-billing-report.html): If you manage multiple domains and you want to view charges by domain for a specified time period, you can download a domain billing report.

### [Domains that you can register with Amazon RouteÂ 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html)

List of top-level domains that you can register with Amazon RouteÂ 53.

### [Generic top-level domains](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list-generic.html)

Generic top-level domains (gTLDs) are global extensions that are used and recognized around the world, such as .com, .net, and .org.

- [.ac](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ac-xref.html): See .
- [.academy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/academy.html): Used by educational institutions such as schools and universities.
- [.accountants](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/accountants.html): Used by businesses, groups, and individuals affiliated with the accounting profession.
- [.actor](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/actor.html)
- [.adult](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/adult.html): Used for websites that host adults-only content.
- [.agency](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/agency.html): Used by any businesses or groups that identify as agencies.
- [.airforce](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/airforce.html)
- [.apartments](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/apartments.html): Used by real estate agents, landlords, and renters.
- [.associates](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/associates.html): Used by businesses and firms that include the term "associates" in their titles.
- [.auction](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/auction.html): Used for events related to auctions and auction-based buying and selling.
- [.audio](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/audio.html)
- [.band](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/band.html): Used for sharing information about musical bands and band events.
- [.bargains](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/bargains.html): Used for information about sales and promotions.
- [.beer](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/beer.html)
- [.bet](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/bet.html)
- [.bid](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/bid.html)
- [.bike](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/bike.html): Used by businesses or groups that cater to cyclists, such as bike stores, motorcycle dealerships, and repair shops.
- [.bingo](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/bingo.html): Used for online gaming websites or for sharing information about the game of bingo.
- [.bio](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/bio.html)
- [.biz](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/biz.html): Used for business or commercial use.
- [.black](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/black.html): Used by those who like the color black or those who want to associate the color black with their business or brand.
- [.blue](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/blue.html): Used by those who like the color blue or those who want to associate the color blue with their business or brand.
- [.bot](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/bot.html): Used for chatbot and AI-related products and services.
- [.boutique](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/boutique.html): Used for information about boutiques and small specialty shops.
- [.builders](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/builders.html): Used by companies and individuals affiliated with the construction industry.
- [.business](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/business.html): Used by any kind of business.
- [.buzz](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/buzz.html): Used for information about the latest news and events.
- [.cab](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/cab.html): Used by companies and individuals affiliated with the taxicab industry.
- [.cafe](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/cafe.html): Used by cafe businesses and those who have an interest in cafe culture.
- [.camera](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/camera.html): Used by photography enthusiasts and anyone who wants to share photos.
- [.camp](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/camp.html): Used by parks and recreation departments, summer camps, writers' workshops, fitness camps, and camping enthusiasts.
- [.capital](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/capital.html): Used as a general category that describes any kind of capital, such as financial capital or the capital of a city.
- [.cards](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/cards.html): Used by businesses that specialize in cards such as ecards, printed greeting cards, business cards, and playing cards.
- [.care](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/care.html): Used by businesses or agencies in the care-giving field.
- [.careers](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/careers.html): Used for information about job recruitment.
- [.cash](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/cash.html): Used by any organization, group, or individual engaged in money-related activities.
- [.casino](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/casino.html): Used by the gambling industry or by gamers who want to share information about gambling and casino games.
- [.catering](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/catering.html): Used by catering businesses or those who share information about food-related events.
- [.cc](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/cc-xref.html): See .
- [.center](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/center.html): Used as a generic extension for everything from research organizations to community centers.
- [.ceo](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ceo.html): Used for information about CEOs and their equals.
- [.chat](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/chat.html): Used by any kind of online chat website.
- [.cheap](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/cheap.html): Used by e-commerce websites to promote and sell inexpensive products.
- [.christmas](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/christmas.html)
- [.church](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/church.html): Used by churches of any size or denomination to connect with their congregations and to publish information about church-related events and activities.
- [.city](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/city.html): Used to provide information about specific cities, such as points of interest, top local spots to visit, or neighborhood activities.
- [.claims](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/claims.html): Used by companies that handle insurance claims or provide legal services.
- [.cleaning](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/cleaning.html): Used by businesses or individuals that provide cleaning services.
- [.click](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/click.html): Used by businesses that want to associate the action of clicking with their websites, for example, clicking products on a website to purchase them.
- [.clinic](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/clinic.html): Used by the health care industry and by medical professionals.
- [.clothing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/clothing.html): Used by those in the fashion industry, including retailers, department stores, designers, tailors, and outlets.
- [.cloud](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/cloud.html): Used as a general extension, but ideal for companies that provide cloud computing technologies and services.
- [.club](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/club.html): Used by any type of club or organization.
- [.coach](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/coach.html): Used by anyone with an interest in coaching, such as sports professionals, lifestyle coaches, or corporate trainers.
- [.codes](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/codes.html): Used as a generic extension for all kinds of code, such as codes of conduct, building codes, or programming code.
- [.coffee](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/coffee.html): Used by those in the coffee industry.
- [.college](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/college.html): Used by educational institutions such as schools and universities.
- [.com](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/com.html): Used for commercial websites.
- [.community](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/community.html): Used by any type of community, club, organization, or special interest group.
- [.company](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/company.html): Used as a generic extension for companies of all kinds.
- [.computer](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/computer.html): Used as a generic extension for information about computers.
- [.condos](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/condos.html): Used by individuals and businesses associated with condominiums.
- [.construction](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/construction.html): Used by those in the construction industry, such as builders and contractors.
- [.consulting](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/consulting.html): Used by consultants and others who are affiliated with the consulting industry.
- [.contact](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/contact.html): Used by churches of any size or denomination to connect with their congregations and to publish information about church-related events and activities.
- [.contractors](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/contractors.html): Used by contractors, such as contractors in the construction industry.
- [.cool](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/cool.html): Used by organizations and groups who want to associate their brand with the latest trends.
- [.coupons](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/coupons.html): Used by retailers and manufacturers that provide online coupons and coupon codes.
- [.credit](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/credit.html): Used by the credit industry.
- [.creditcard](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/creditcard.html): Used by companies or banks that issue credit cards.
- [.cruises](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/cruises.html): Used by the voyage industry.
- [.dance](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dance.html): Used by dancers, dance instructors, and dance schools.
- [.dating](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dating.html): Used for dating websites.
- [.deal](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/deal.html): Used for websites offering deals, discounts, and special offers.
- [.deals](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/deals.html): Used to provide information about online bargains and sales.
- [.degree](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/degree.html)
- [.delivery](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/delivery.html): Used by companies that deliver any kind of merchandise or service.
- [.democrat](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/democrat.html): Used for information about the Democratic Party.
- [.dental](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dental.html): Used by dental professionals and dental suppliers.
- [.design](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/design.html): Used by churches of any size or denomination to connect with their congregations and to publish information about church-related events and activities.
- [.diamonds](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/diamonds.html): Used by diamond enthusiasts and those in the diamond industry, including sellers, resellers, and merchandisers.
- [.diet](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/diet.html)
- [.digital](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/digital.html): Used for anything and everything digital, but ideal for technology businesses.
- [.direct](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/direct.html): Used as a general extension, but ideal for those who sell products directly to customers through an e-commerce website.
- [.directory](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/directory.html): Used by the media sector.
- [.discount](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/discount.html): Used for discount websites and businesses that slash prices.
- [.dog](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dog.html): Used by dog lovers and those who provide canine services and products.
- [.domains](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domains.html): Used for information about domain names.
- [.education](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/education.html): Used for information about education.
- [.email](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/email.html): Used for information about promoting email.
- [.energy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/energy.html): Used as a general extension, but ideal for those in the energy or energy conservation fields.
- [.engineering](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/engineering.html): Used by engineering firms and professionals.
- [.enterprises](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/enterprises.html): Used for information about enterprises and businesses.
- [.equipment](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/equipment.html): Used for information about equipment, equipment retailers or manufacturers, and rental shops.
- [.estate](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/estate.html): Used for information about housing and the housing sector.
- [.events](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/events.html): Used for information about events of all kinds.
- [.exchange](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/exchange.html): Used for any type of exchange: the stock exchange, the exchange of goods, or even the simple exchange of information.
- [.expert](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/expert.html): Used by those who have specialized knowledge in a variety of fields.
- [.exposed](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/exposed.html): Used as a generic extension for a variety of subjects, including photography, tabloids, and investigative journalism.
- [.express](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/express.html): Used as a general extension, but ideal for those who want to emphasize the speedy delivery of good or services.
- [.fail](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/fail.html): Used by anyone who has made mistakes, but ideal for publishing humorous "fail" blunders and bloopers.
- [.fan](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/fan.html)
- [.farm](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/farm.html): Used by those in the farming industry, such as farmers and agricultural engineers.
- [.finance](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/finance.html): Used by the financial sector.
- [.financial](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/financial.html): Used by the financial sector.
- [.fish](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/fish.html): Used as a general extension, but ideal for websites related to fish and fishing.
- [.fitness](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/fitness.html): Used to promote fitness and fitness services.
- [.flights](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/flights.html): Used by travel agents, airlines, and anyone affiliated with the travel industry.
- [.florist](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/florist.html): Used by florists.
- [.flowers](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/flowers.html)
- [.fm](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/fm-xref.html): See .
- [.football](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/football.html): Used by anyone involved in the sport of football.
- [.forsale](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/forsale.html): Used for selling goods and services.
- [.foundation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/foundation.html): Used by non-profit organizations, charities, and other kinds of foundations.
- [.free](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/free.html): Used for websites offering free products, services, or content.
- [.fun](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/fun.html)
- [.fund](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/fund.html): Used as a general extension for anything related to funding.
- [.furniture](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/furniture.html): Used by furniture makers and sellers and anyone affiliated with the furniture industry.
- [.futbol](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/futbol.html): Used for information about soccer (futbol).
- [.fyi](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/fyi.html): Used as a general extension, but ideal for sharing information of all kinds. "FYI" is an acronym for "for your information."
- [.gallery](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gallery.html): Used by owners of art galleries.
- [.games](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/games.html)
- [.gift](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gift.html): Used by businesses or organizations that sell gifts or provide gift-related services.
- [.gifts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gifts.html): Used by businesses or organizations that sell gifts or provide gift-related services.
- [.gives](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gives.html)
- [.glass](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/glass.html): Used by those in the glass industry, such as glass cutters and window installers.
- [.global](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/global.html): Used by businesses or groups with an international market or vision.
- [.gmbh](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gmbh.html)
- [.gold](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gold.html): Used as a general extension, but ideal for companies that purchase or sell gold or gold-related products.
- [.golf](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/golf.html): Used for websites devoted to the game of golf.
- [.graphics](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/graphics.html): Used by those in the graphics industry.
- [.gratis](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gratis.html): Used for websites that offer free products, such as promotional items, downloads, or coupons. "Gratis" is a Spanish word that means "free."
- [.green](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/green.html): Used for websites devoted to conservation, ecology, the environment, and the green lifestyle.
- [.gripe](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gripe.html): Used for sharing complaints and criticism.
- [.group](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/group.html)
- [.guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/guide.html): Used as a general extension, but ideal for websites that focus on travel destinations, services, and products.
- [.guitars](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/guitars.html)
- [.guru](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/guru.html): Used by those who want to share their knowledge about a variety of subjects.
- [.haus](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/haus.html): Used by real estate and construction industries. "Haus" is a German word that means "house."
- [.healthcare](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/healthcare.html): Used by the healthcare sector.
- [.help](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/help.html): Used as a general extension, but ideal for websites that provide online help and information.
- [.hiv](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hiv.html): Used for websites devoted to the fight against HIV.
- [.hockey](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hockey.html): Used for websites devoted to the game of hockey.
- [.holdings](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/holdings.html): Used by financial advisors, stockbrokers, and those who work with investments.
- [.holiday](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/holiday.html): Used by those in the travel industry and individuals and businesses involved in party planning and special occasions.
- [.host](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/host.html): Used by companies that provide web hosting platforms and services.
- [.hosting](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosting.html)
- [.hot](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hot.html): Used for websites featuring trending topics, popular content, or time-sensitive offers.
- [.house](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/house.html): Used by real estate agents and buyers and sellers of houses.
- [.im](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/im-xref.html): See .
- [.immo](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/immo.html): Used by the real estate sector.
- [.immobilien](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/immobilien.html): Used for information about real estate.
- [.industries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/industries.html): Used by any business or commercial enterprise that wants to identify as an industry.
- [.info](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/info.html): Used for the dissemination of information.
- [.ink](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ink.html): Used by tattoo enthusiasts or any industry related to ink, such as printing and publishing industries.
- [.institute](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/institute.html): Used by any organization or group, especially research and educational organizations.
- [.insure](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/insure.html): Used by insurance companies and insurance brokers.
- [.international](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/international.html): Used by businesses that have international chains, individuals who travel internationally, or charity organizations with an international influence.
- [.investments](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/investments.html): Used as a general extension, but ideal for promoting investment opportunities.
- [.io](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/io-xref.html): See .
- [.irish](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/irish.html): Used for promoting Irish culture and organizations.
- [.jewelry](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/jewelry.html): Used by jewelry sellers and buyers.
- [.juegos](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/juegos.html)
- [.kaufen](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/kaufen.html): Used for information about e-commerce.
- [.kim](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/kim.html): Used by people whose name or surname is Kim.
- [.kitchen](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/kitchen.html): Used by kitchen retailers, cooks, food bloggers, and anyone in the food industry.
- [.kiwi](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/kiwi.html): Used by companies and individuals who want to support New Zealand kiwi culture.
- [.land](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/land.html): Used by farmers, real estate agents, commercial developers, and anyone with an interest in property.
- [.law](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/law.html)
- [.lease](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/lease.html): Used by realtors, landlords, and renters.
- [.legal](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/legal.html): Used by members of the legal profession.
- [.lgbt](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/lgbt.html): Used by the community of lesbian, gay, bisexual, and transgender people.
- [.life](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/life.html): Used as a general extension, and suitable for a wide range of businesses, groups, and individuals.
- [.lighting](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/lighting.html): Used by photographers, designers, architects, engineers, and others with an interest in lighting.
- [.limited](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/limited.html): Used as a general extension, and suitable for a wide range of businesses, groups, and individuals.
- [.limo](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/limo.html): Used by chauffeurs, limousine companies, and car rental agencies.
- [.link](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/link.html): Used for information about the creation of online shortcut links.
- [.live](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/live.html): Used as a general extension, and suitable for a wide range of businesses, groups, and individuals.
- [.llc](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/llc.html)
- [.loan](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/loan.html): Used by lenders, borrowers, and credit professionals.
- [.loans](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/loans.html): Used by lenders, borrowers, and credit professionals.
- [.lol](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/lol.html): Used for humor and comedy websites. "LOL" is an acronym for "laugh out loud."
- [.ltd](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ltd.html)
- [.maison](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/maison.html): Used by the real estate sector.
- [.management](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/management.html): Used for information about the business world and company management.
- [.marketing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/marketing.html): Used by the marketing sector for a variety of purposes.
- [.mba](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/mba.html): Used for websites that provide information about the master's degree in business administration (MBA).
- [.media](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/media.html): Used by the media and entertainment sectors.
- [.memorial](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/memorial.html): Used by commemorative organizations dedicated to honoring events and people.
- [.mobi](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/mobi.html): Used by companies and individuals who want to have their websites accessible on mobile phones.
- [.moda](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/moda.html): Used for information about fashion.
- [.moi](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/moi.html): French for "me." Used to signal French-language content to Francophone end users.
- [.money](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/money.html): Used for websites that focus on money and money-related activities.
- [.mortgage](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/mortgage.html): Used by the mortgage industry.
- [.movie](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/movie.html): Used for websites that provide information about movies and movie-making.
- [.name](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/name.html): Used by anyone who wants to create a personalized web presence.
- [.net](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/net.html): Used for all types of websites.
- [.network](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/network.html): Used by those in the network industry or those who want to build connections through networking.
- [.news](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/news.html): Used for distributing any newsworthy information such as current events or information related to journalism and communication.
- [.ninja](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ninja.html): Used by individuals and businesses who want to associate themselves with the abilities of a ninja.
- [.now](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/now.html)
- [.onl](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/onl.html): The .onl extension is an abbreviation for "online," and it is also the short term in Spanish for non-profit organization.
- [.online](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/online.html): The .onl extension is an abbreviation for "online," and it is also the short term in Spanish for non-profit organization.
- [.org](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/org.html): Used by all kinds of organizations.
- [.partners](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/partners.html): Used by law firms, investors, and a variety of companies.
- [.parts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/parts.html): Used as a general extension, but ideal for parts manufacturers, sellers, and buyers.
- [.photo](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/photo.html): Used by photographers and anyone interested in photos.
- [.photography](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/photography.html): Used by photographers and anyone interested in photos.
- [.photos](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/photos.html): Used by photographers and anyone interested in photos.
- [.pics](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/pics.html): Used by photographers and anyone interested in photos.
- [.pictures](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/pictures.html): Used by anyone interested in photography, art, and media.
- [.pink](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/pink.html): Used by those who like the color pink or those who want to associate the color pink with their business or brand.
- [.pizza](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/pizza.html): Used by pizza restaurants and pizza lovers.
- [.place](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/place.html): Used as a general extension, but ideal for the home and travel sectors.
- [.plumbing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/plumbing.html): Used by those in the plumbing industry.
- [.plus](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/plus.html): Used as a general extension, but ideal for plus-size clothing, add-on software, or any product that offers "extra" features or dimensions.
- [.poker](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/poker.html): Used by poker players and gaming websites.
- [.porn](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/porn.html): Used for adults-only websites.
- [.press](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/press.html): Used for adults-only websites.
- [.pro](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/pro.html): Used by licensed and credentialed professionals and professional organizations.
- [.productions](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/productions.html): Used by studios and production houses that make commercials, radio ads, and music videos.
- [.properties](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/properties.html): Used for information about any type of property, including real estate or intellectual property.
- [.property](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/property.html): Used for information about any type of property, including real estate or intellectual property.
- [.pub](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/pub.html): Used by those in the publication, advertising, or brewing business.
- [.qpon](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/qpon.html): Used for coupons and promo codes.
- [.recipes](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/recipes.html): Used by those with recipes to share.
- [.red](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/red.html): Used by those who like the color red or those who want to associate the color red with their business or brand.
- [.reise](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/reise.html): Used for websites related to travels or journeys. "Reise" is a German word that means "rise," "arise," or "set out on a journey."
- [.reisen](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/reisen.html): Used for websites related to travels or journeys. "Reisen" is a German word that means "to travel."
- [.rentals](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rentals.html): Used for all types of rentals.
- [.repair](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/repair.html): Used by repair services or by those who want to teach others how to repair all kinds of items.
- [.report](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/report.html): Used as a general extension, but ideal for information about business reports, community publications, book reports, or news reporting.
- [.republican](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/republican.html): Used for information about the Republican Party.
- [.restaurant](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/restaurant.html): Used by the restaurant industry.
- [.reviews](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/reviews.html): Used by those who want give their opinions and read the comments of others.
- [.rip](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rip.html): Used for websites dedicated to death and memorials. "RIP" is an acronym for "rest in peace."
- [.rocks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rocks.html): Used as a general extension, but ideal for anyone who "rocks": musicians, geologists, jewelers, climbers, and more.
- [.run](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/run.html): Used as a general extension, but ideal for the fitness and sports industry.
- [.sale](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/sale.html): Used by e-commerce websites.
- [.sarl](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/sarl.html): Used by limited liability companies typically located in France. "SARL" is an acronym for SociÃ©tÃ© Ã  ResponsabilitÃ© LimitÃ©.
- [.school](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/school.html): Used for information about education, educational institutions, and school-related activities.
- [.schule](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/schule.html): Used for information about German-based education, educational institutions, and school-related activities. "Schule" is a German word that means "school."
- [.services](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/services.html): Used for websites that focus on services of any kind.
- [.sex](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/sex.html): Used for adults-only content.
- [.sexy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/sexy.html): Used for sexual content.
- [.shiksha](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/shiksha.html): Used by educational institutions. "Shiksha" is an Indian term for school.
- [.shoes](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/shoes.html): Used by shoe retailers, designers, manufacturers, or fashion bloggers.
- [.shop](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/shop.html): Used for online and brick-and-mortar retail businesses, as well as service providers.
- [.shopping](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/shopping.html)
- [.show](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/show.html): Used as a general extension, but ideal for the entertainment industry.
- [.singles](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/singles.html): Used by dating services, resorts, and other businesses that cater to those who want to make a connection.
- [.site](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/site.html)
- [.ski](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ski.html)
- [.soccer](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/soccer.html): Used for websites dedicated to the game of soccer.
- [.social](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/social.html): Used for information about social media, forums, and online conversations.
- [.solar](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/solar.html): Used for information about the solar system or solar energy.
- [.solutions](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/solutions.html): Used by consultants, do-it-yourself services, and advisors of all kinds.
- [.software](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/software.html)
- [.space](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/space.html)
- [.spot](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/spot.html)
- [.store](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/store.html)
- [.stream](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/stream.html)
- [.studio](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/studio.html): Used as a general extension, but ideal for those in the real estate, art, or entertainment industries.
- [.style](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/style.html): Used as a general extension, but ideal for websites dedicated to the latest trends, especially trends in fashion, design, architecture, and art.
- [.sucks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/sucks.html): Used as a general extension, but ideal for those who want to share negative experiences or warn others about scams, frauds, or faulty products.
- [.supplies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/supplies.html): Used by businesses that sell goods online.
- [.supply](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/supply.html): Used by businesses that sell goods online.
- [.support](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/support.html): Used by businesses, groups, or charities that offer any kind of support, including customer, product, or system support or emotional, financial, or spiritual support.
- [.surgery](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/surgery.html): Used for information about surgery, medicine, and healthcare.
- [.systems](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/systems.html): Used primarily by the technology industry and those who offer technology services.
- [.tattoo](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/tattoo.html): Used by tattoo enthusiasts and the tattoo industry.
- [.tax](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/tax.html): Used for information about taxes, tax preparation, and tax law.
- [.taxi](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/taxi.html): Used by cab, chauffeur, and shuttle companies.
- [.team](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/team.html): Used by any business or organization that wants to identify as a team.
- [.tech](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/tech.html): Used by technology enthusiasts and those dedicated to technology in companies, services, and manufacturers.
- [.technology](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/technology.html): Used by technology enthusiasts and those dedicated to technology in companies, services, and manufacturers.
- [.tennis](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/tennis.html): Used for information related to the game of tennis.
- [.theater](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/theater.html): Used for websites dedicated to theaters, plays, and musicals.
- [.tienda](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/tienda.html): Used by retail businesses that want to connect with Spanish-speaking consumers.
- [.tips](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/tips.html): Used by those who want to share their knowledge and advice on virtually any topic.
- [.tires](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/tires.html): Used by manufacturers, distributors, or buyers of tires.
- [.today](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/today.html): Used for information about current events, news, weather, entertainment, and more.
- [.tools](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/tools.html): Used for information about any kind of tool.
- [.tours](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/tours.html): Used as a general extension, but ideal for travel companies.
- [.town](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/town.html): Used to promote a city's locale, culture, and community.
- [.toys](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/toys.html): Used by the toy industry.
- [.trade](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/trade.html): Used as a general extension, but ideal for commerce websites or trading services.
- [.training](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/training.html): Used by trainers, coaches, and educators.
- [.tv](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/tv.html): Used for information about television and media.
- [.university](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/university.html): Used by universities and other educational organizations.
- [.uno](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/uno.html): Used for information about the Hispanic, Portuguese, and Italian communities.
- [.vacations](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/vacations.html): Used by the travel and tourism industry.
- [.vegas](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/vegas.html): Used to promote the city of Las Vegas and the Las Vegas lifestyle.
- [.ventures](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ventures.html): Used by entrepreneurs, startups, venture capitalists, investment banks, and financiers.
- [.vg](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/vg-xref.html): See .
- [.viajes](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/viajes.html): Used by travel agencies, tour operators, travel blogs, tour companies, rental services, travel bloggers, and travel retailers.
- [.video](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/video.html): Used by media and video industries.
- [.villas](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/villas.html): Used by real estate agents and property owners who have villas to sell, rent, or lease.
- [.vision](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/vision.html): Used as a general extension, but ideal for vision specialists such as optometrists and ophthalmologists.
- [.vote](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/vote.html)
- [.voyage](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/voyage.html): Used by travel agencies, tour operators, travel blogs, tour companies, rental services, travel bloggers, and travel retailers.
- [.watch](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/watch.html): Used for information about streaming websites, web TVs, video, or watches.
- [.website](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/website.html): Used for information about website development, promotion, improvements, and experiences.
- [.wedding](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/wedding.html)
- [.wiki](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/wiki.html): Used for information about online documentation.
- [.wine](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/wine.html)
- [.work](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/work.html)
- [.works](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/works.html): Used by businesses, organizations, and individuals for information about work, job, and employment services.
- [.world](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/world.html): Used by anyone who wants to provide information about global subjects.
- [.wtf](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/wtf.html): Used by anyone who wants to identify with the popular (but profane) acronym "WTF."
- [.xxx](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/xxx.html): Used for websites that host adults-only content.
- [.xyz](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/xyz.html): Used as a general extension for any purpose.
- [.zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/zone.html): Used for information about any kind of zone, including time zones, climate zones, and sports zones.

### [Geographic top-level domains](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list-geographic.html)

The following domain extensions are grouped by geography and include official country-specific extensions, known as country code top-level domains (ccTLDs).

### [Africa](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list-africa.html)

You can use the following top-level domains (TLDs) for Africa to register domains with Amazon RouteÂ 53.

- [.ac (Ascension Island)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ac.html)
- [.co.za (South Africa)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/co.za.html)
- [.sh (Saint Helena)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/sh.html)

### [Americas](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list-americas.html)

You can use the following top-level domains (TLDs) for the Americas to register domains with Amazon RouteÂ 53.

- [.ai (Anguilla)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ai.html)
- [.ca (Canada)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ca.html)
- [.cl (Chile)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/cl.html)
- [.co (Colombia)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/co.html)
- [.com.ar (Argentina)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/com.ar.html)
- [.com.br (Brazil)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/com.br.html)
- [.com.mx (Mexico)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/com.mx.html)
- [.mx (Mexico)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/mx.html)
- [.us (United States)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/us.html)
- [.vc (Saint Vincent and the Grenadines)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/vc.html): Also used as a generic TLD, often by those involved in venture capital financing, varsity colleges, and so on.
- [.vg (British Virgin Islands)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/vg.html): Also used as a generic TLD, often by organizations involved in video gaming.

### [Asia/Oceania](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list-asiaoceania.html)

You can use the following top-level domains (TLDs) for Asia and Oceania to register domains with Amazon RouteÂ 53.

- [.au (Australia)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/au.html)
- [.cc (Cocos (Keeling) Islands)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/cc.html)
- [.co.nz (New Zealand)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/co.nz.html)
- [.com.au (Australia)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/com.au.html)
- [.com.sg (Republic of Singapore)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/com.sg.html)
- [.fm (Federated States of Micronesia)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/fm.html): Also used as a generic TLD, often by organizations involved in online media and broadcasting.
- [.in (India)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/in.html)
- [.jp (Japan)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/jp.html)
- [.io (British Indian Ocean Territory)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/io.html): Also used as a generic TLD, often by computer-related organizations such as online services, browser-based games, and startup companies.
- [.net.au (Australia)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/net.au.html)
- [.net.nz (New Zealand)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/net.nz.html)
- [.nz (New Zealand)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/nz.html)
- [.org.nz (New Zealand)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/org.nz.html)
- [.pw (Palau)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/pw.html)
- [.qa (Qatar)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/qa.html)
- [.ru (Russian Federation)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ru.html)
- [.sg (Republic of Singapore)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/sg.html)

### [Europe](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list-europe.html)

You can use the following top-level domains (TLDs) for Europe to register domains with Amazon RouteÂ 53.

- [.be (Belgium)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/be.html)
- [.berlin (city of Berlin in Germany)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/berlin.html)
- [.ch (Switzerland)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ch.html)
- [.co.uk (United Kingdom)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/co.uk.html)
- [.cz (Czech Republic)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/cz.html)
- [.de (Germany)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/de.html)
- [.es (Spain)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/es.html)
- [.eu (European Union)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/eu.html)
- [.fi (Finland)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/fi.html)
- [.fr (France)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/fr.html)
- [.gg (Guernsey)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gg.html)
- [.im (Isle of Man)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/im.html): Also used as a generic TLD, often by instant messaging services or for individuals who want to develop an "I am" personal brand.
- [.it (Italy)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/it.html)
- [.me (Montenegro)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/me.html)
- [.me.uk (United Kingdom)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/me.uk.html)
- [.nl (the Netherlands)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/nl.html)
- [.org.uk (United Kingdom)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/org.uk.html)
- [.ruhr (Ruhr region, western part of Germany)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ruhr.html)
- [.se (Sweden)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/se.html)
- [.uk (United Kingdom)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/uk.html)
- [.wien (city of Vienna in Austria)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/wien.html)


## [Configuring Amazon RouteÂ 53 as your DNS service](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring.html)

### [Making RouteÂ 53 the DNS service for an existing domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/MigratingDNS.html)

Migrate an existing domain to use Amazon RouteÂ 53 as the DNS service provider.

- [Making RouteÂ 53 the DNS service for a domain that's in use](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/migrate-dns-domain-in-use.html): If you want to migrate DNS service to Amazon RouteÂ 53 for a domain that is currently getting trafficâfor example, if your users are using the domain name to browse to a website or access a web applicationâperform the procedures in this section.
- [Making RouteÂ 53 the DNS service for an inactive domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/migrate-dns-domain-inactive.html): If you want to migrate DNS service to Amazon RouteÂ 53 for a domain that isn't getting any traffic (or is getting very little traffic), perform the procedures in this section.
- [Configuring DNS routing for a new domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-new-domain.html): Set up DNS routing for domains registered with Route 53 or other registrars by creating hosted zones and configuring name servers.

### [Routing traffic to your resources](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-routing-traffic-to-resources.html)

Create a hosted zone and create records in the hosted zone to route traffic to your resources.

- [Routing traffic for subdomains](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-routing-traffic-for-subdomains.html): When you want to route traffic to your resources for a subdomain, such as acme.example.com or zenith.example.com, you have two options:

### [Working with hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-working-with.html)

Create and manage public and private hosted zones that contain DNS records for routing traffic to your resources.

### [Working with public hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/AboutHZWorkingWith.html)

Create, list, and delete public hosted zones using the RouteÂ 53 console.

- [Considerations when working with public hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-public-considerations.html): Note the following considerations when working with public hosted zones:
- [Creating a public hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/CreatingHostedZone.html): Create a hosted zone for a domain and create records to tell DNS how to route traffic on the internet for the domain.
- [Getting the name servers for a public hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/GetInfoAboutHostedZone.html): Get the name servers for a public hosted zone using the Amazon RouteÂ 53 console.
- [Listing public hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ListInfoOnHostedZone.html): List the public hosted zones associated with an AWS account using the RouteÂ 53 console.
- [Viewing DNS query metrics for a public hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-public-viewing-query-metrics.html): You can view the total number of DNS queries that RouteÂ 53 is responding to for a specified public hosted zone or combination of public hosted zones.
- [Deleting a public hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DeleteHostedZone.html): Delete a public hosted zone using the RouteÂ 53 console.
- [Checking DNS responses from RouteÂ 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-test.html): Use the checking tool in the Amazon RouteÂ 53 console to simulate queries from specific DNS resolver IP addresses or client IP addresses.
- [Configuring white-label name servers](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/white-label-name-servers.html): Configure Amazon RouteÂ 53 to use white-label name servers, such as ns1.example.com, in place of the default name servers that RouteÂ 53 assigns to your hosted zone.
- [NS and SOA records that Amazon RouteÂ 53 creates for a public hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/SOA-NSrecords.html): Describes the name server (NS) and start of authority (SOA) records that RouteÂ 53 automatically creates when you create a public hosted zone.
- [Enabling accelerated recovery for managing public DNS records](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/accelerated-recovery.html): Enable accelerated recovery to achieve a 60-minute Recovery Time Objective (RTO) for regaining the ability to make DNS changes during US East (N.

### [Working with private hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html)

Create, list, and delete private hosted zones using the RouteÂ 53 console.

- [Considerations when working with a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-considerations.html): Consider the following when using an Amazon RouteÂ 53 private hosted zone.
- [Creating a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-creating.html): Create a hosted zone for a domain and create records to tell RouteÂ 53 how to route traffic within an Amazon Virtual Private Cloud for that domain.
- [Listing private hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-listing.html): List the private hosted zones associated with an AWS account using the RouteÂ 53 console.
- [Associating more VPCs with a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-associate-vpcs.html): Associate additional Amazon Virtual Private Clouds with an Amazon RouteÂ 53 private hosted zone using the RouteÂ 53 console.
- [Associating an Amazon VPC and a private hosted zone that you created with different AWS accounts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-associate-vpcs-different-accounts.html): Authorize associating an Amazon Virtual Private Cloud that you created with one account with an Amazon RouteÂ 53 private hosted zone that you created with a different account.
- [Disassociating VPCs from a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-disassociate-vpcs.html): Disassociate Amazon Virtual Private Clouds from an Amazon RouteÂ 53 private hosted zone using the RouteÂ 53 console.
- [Deleting a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-deleting.html): Delete a private hosted zone using the RouteÂ 53 console.
- [VPC permissions](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-vpc-permissions.html): Overview of granular IAM policy condition for VPC permissions in RouteÂ 53.
- [Migrating a hosted zone to a different AWS account](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-migrating.html): Migrate a hosted zone from one AWS account to another using the recommended steps.

### [Working with records](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rrsets-working-with.html)

Create, change, delete, and list records using the RouteÂ 53 with the console.

### [Choosing a routing policy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html)

Choose a routing policy before you create records in Amazon RouteÂ 53.

- [Simple routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-simple.html): Simple routing lets you configure standard DNS records, with no special RouteÂ 53 routing such as weighted or latency.
- [Failover routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html): Failover routing lets you route traffic to a resource when the resource is healthy or to a different resource when the first resource is unhealthy.

### [Geolocation routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geo.html)

Geolocation routing lets you choose the resources that serve your traffic based on the geographic location of your users, meaning the location that DNS queries originate from.

- [Geolocation routing in private hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geo-phz.html): For private hosted zones, RouteÂ 53 responds to DNS queries based on the AWS Region of the VPC that the query originated from.
- [Geoproximity routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geoproximity.html): Geoproximity routing lets Amazon RouteÂ 53 route traffic to your resources based on the geographic location of your users and your resources.

### [Latency-based routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html)

If your application is hosted in multiple AWS Regions, you can improve performance for your users by serving their requests from the AWS Region that provides the lowest latency.

- [Latency-based routing in private hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency-phz.html): For private hosted zones, RouteÂ 53 answers DNS queries with an endpoint that is in the same AWS Region, or is closest in distance to the AWS Region of the VPC that the query originated from.

### [IP-based routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-ipbased.html)

With IP-based routing in Amazon RouteÂ 53, you can fine-tune your DNS routing by using your understanding of your network, applications, and clients to make the best DNS routing decisions for your end users.

- [Creating a CIDR collection with CIDR locations and blocks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating-cidr-collection.html): Create a CIDR collection and add CIDR blocks to it.
- [Working with CIDR locations and blocks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-working-with-cidr-locations.html): View and edit a CIDR location and blocks.
- [Deleting a CIDR collection](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-delete-cidr-collection.html): Delete a CIDR collection and the CIDR locations within.
- [Moving a geolocation to IP-based routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-move-geolocation-to-cidr.html): Move an existing geolocation routing configuration to IP-based routing.
- [Multivalue answer routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-multivalue.html): Multivalue answer routing lets you configure Amazon RouteÂ 53 to return multiple values, such as IP addresses for your web servers, in response to DNS queries.
- [Weighted routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html): Weighted routing lets you associate multiple resources with a single domain name (example.com) or subdomain name (acme.example.com) and choose how much traffic is routed to each resource.
- [How Amazon RouteÂ 53 uses EDNS0 to estimate the location of a user](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-edns0.html): To improve the accuracy of geolocation, geoproximity, IP-based, and latency routing, Amazon RouteÂ 53 supports the edns-client-subnet extension of EDNS0. (EDNS0 adds several optional extensions to the DNS protocol.) RouteÂ 53 can use edns-client-subnet only when DNS resolvers support it:
- [Choosing between alias and non-alias records](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html): Choose whether you want to create alias records in Amazon RouteÂ 53.
- [Supported DNS record types](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html): Describes the DNS record types that are supported by RouteÂ 53.
- [Creating records by using the Amazon RouteÂ 53 console](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html): Create records in Amazon RouteÂ 53.
- [Resource record set permissions](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-permissions.html): Overview of granular IAM policy conditions for resource record sets permissions in RouteÂ 53.

### [Values you specify](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html)

Learn the values that you specify when you create or edit Amazon RouteÂ 53 records.

- [Common values](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-shared.html): Learn the common values that you can specify when you create or edit Amazon RouteÂ 53 records.
- [Common values for alias records](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-alias-common.html): Learn the common alias values for all routing policies that you can specify when you create or edit Amazon RouteÂ 53 records.
- [Simple records values](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-basic.html): When you create simple records, you specify the following values.
- [Simple alias records values](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-alias.html): When you create alias records, you specify the following values.
- [Failover records values](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-failover.html): When you create failover records, you specify the following values.
- [Failover alias records values](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-failover-alias.html): When you create failover alias records, you specify the following values.
- [Geolocation records values](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-geo.html): When you create geolocation records, you specify the following values.
- [Geolocation alias records values](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-geo-alias.html): When you create geolocation alias records, you specify the following values.
- [Geoproximity records values](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-geoprox.html): When you create geoproximity records, you specify the following values.
- [Geoproximity alias records values](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-geoprox-alias.html): When you create geoproximity alias records, you specify the following values.
- [Latency records values](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-latency.html): When you create latency records, you specify the following values.
- [Latency alias records values](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-latency-alias.html): When you create latency alias records, you specify the following values.
- [IP-based records values](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-ipbased.html): When you create IP-based records, you specify the following values.
- [IP-based alias records values](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-ipbased-alias.html): When you create IP-based alias records, you specify the following values.
- [Multivalue answer records values](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-multivalue.html): When you create multivalue answer records, you specify the following values.
- [Weighted records values](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-weighted.html): When you create weighted records, you specify the following values.
- [Weighted alias records values](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-weighted-alias.html): When you create weighted alias records, you specify the following values.
- [Creating records by importing a zone file](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating-import.html): Create records by importing a zone file from your current DNS service provider.
- [Editing records](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-editing.html): Edit records in Amazon RouteÂ 53.
- [Deleting records](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-deleting.html): Delete records in Amazon RouteÂ 53.
- [Listing records](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-listing.html): Lists the records in a hosted zone using the RouteÂ 53 console.

### [Configuring DNSSEC signing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec.html)

Configure DNSSEC signing to let DNS resolvers validate that a DNS response came from RouteÂ 53 and has not been tampered with.

- [Enabling DNSSEC signing and establishing a chain of trust](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec-enable-signing.html)
- [Disabling DNSSEC signing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec-disable.html): The steps for disabling DNSSEC signing in RouteÂ 53 vary, depending on the chain of trust that your hosted zone is part of.
- [Working with customer managed keys](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec-cmk-requirements.html): When you enable DNSSEC signing in Amazon RouteÂ 53, RouteÂ 53 creates a key-signing key (KSK) for you.
- [Working with key-signing keys (KSKs)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec-ksk.html): When you enable DNSSEC signing, RouteÂ 53 creates a key-signing key (KSK) for you.
- [KMS key and ZSK management in RouteÂ 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec-zsk-management.html): This section describes the current practice RouteÂ 53 uses for your DNSSEC signing enabled zones.
- [DNSSEC proofs of nonexistence in Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec-proof-of-nonexistence.html)
- [Troubleshooting DNSSEC signing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec-troubleshoot.html): The information in this section can help you address issues with DNSSEC signing, including enabling, disabling, and with your key-signing keys (KSKs).
- [Using AWS Cloud Map to create records and health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/autonaming.html): Automatically create DNS records and health checks for microservices and application components using AWS Cloud Map.
- [DNS constraints and behaviors](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSBehavior.html): Describes the DNS constraints and behaviors for how you create and use hosted zones and records.
- [Related topics](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-related-topics.html): Links to domain transfer documentation for customers who want to transfer domain registration to Route 53.


## [Traffic Flow](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-flow.html)

- [Creating and managing traffic policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-policies.html)
- [Creating and managing policy records](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-policy-records.html): To route internet traffic to the resources that you specified when you created a traffic policy, you create one or more policy records.


## [What is VPC Resolver?](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html)

### [Resolving DNS queries between VPCs and your network](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-overview-DSN-queries-to-vpc.html)

Configure Route 53 Resolver endpoints to enable DNS query resolution between your VPCs and on-premises networks, including peered VPCs and networks connected via AWS Direct Connect or VPN.

- [How DNS queries from your network are forwarded to VPC Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-overview-forward-network-to-vpc.html): Learn how to configure inbound endpoints to enable DNS resolvers on your on-premises network to forward queries to Route 53 VPC Resolver, including default and delegation endpoint types.

### [How Resolver endpoints forward DNS queries from your VPCs to your network](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-overview-forward-vpc-to-network.html)

Configure outbound endpoints and forwarding rules to enable Route 53 VPC Resolver to forward DNS queries from EC2 instances in your VPCs to DNS resolvers on your on-premises network.

- [Using rules to control forwarded queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-overview-forward-vpc-to-network-using-rules.html): Learn how forwarding rules determine which DNS queries are sent from your VPCs to your on-premises network, including rule types and domain name matching.
- [How VPC Resolver matches domain name to rules](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-overview-forward-vpc-to-network-domain-name-matches.html): Understand how Route 53 VPC Resolver compares domain names in DNS queries against forwarding rules to determine whether queries should be forwarded to your network.
- [How VPC Resolver forwards DNS queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-overview-forward-vpc-to-network-where-to-forward-queries.html): Learn the step-by-step process Route 53 VPC Resolver uses to determine where to forward DNS queries when multiple rules and endpoints are configured.
- [Using rules in multiple Regions](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-overview-forward-vpc-to-network-using-rules-multiple-regions.html): Understand how Route 53 Resolver rules work across AWS Regions and how to share rules between AWS accounts for multi-region deployments.
- [Autodefined system rules](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-overview-forward-vpc-to-network-autodefined-rules.html): Learn about the automatic system rules that Route 53 VPC Resolver creates to handle AWS specific domain names and private hosted zones, and how they interact with custom forwarding rules.
- [Considerations when creating inbound and outbound endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-choose-vpc.html): Review important considerations for VPC selection, security groups, network interfaces, and regional planning when creating Route 53 Resolver endpoints.
- [Route 53 VPC Resolver availability and scaling](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-availability-scaling.html): Learn about Route 53 VPC Resolver's high availability architecture, automatic scaling capabilities, and performance characteristics across AWS Regions and Availability Zones.
- [Getting started with Route 53 VPC Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-getting-started.html): Use the Route 53 VPC Resolver console wizard to quickly set up inbound and outbound endpoints, create forwarding rules, and configure DNS resolution between your VPCs and on-premises network.

### [Forwarding inbound DNS queries to your VPCs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html)

Configure inbound endpoints to enable DNS resolvers on your on-premises network to forward queries to Route 53 VPC Resolver in your VPCs, including setup requirements and network connectivity options.

- [Configuring inbound forwarding](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries-configuring.html): Step-by-step instructions for creating inbound endpoints to enable DNS query forwarding from your on-premises network to Route 53 VPC Resolver.
- [Values that you specify when you create or edit inbound endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries-values.html): Reference guide for all configuration parameters and settings required when creating or modifying Resolver inbound endpoints.
- [Managing inbound endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries-managing.html): View, edit, and delete inbound endpoints, including procedures for updating endpoint configurations and monitoring endpoint status.

### [Forwarding outbound DNS queries to your network](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html)

Configure outbound endpoints and forwarding rules to enable DNS queries from EC2 instances in your VPCs to be forwarded to DNS resolvers on your on-premises network.

- [Configuring outbound forwarding](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries-configuring.html): Step-by-step instructions for creating outbound endpoints and forwarding rules to enable DNS query forwarding from your VPCs to your on-premises network.
- [Values that you specify when you create or edit outbound endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries-endpoint-values.html): Reference guide for all configuration parameters and settings required when creating or modifying Resolver outbound endpoints.
- [Values that you specify when you create or edit rules](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries-rule-values.html): Reference guide for all configuration parameters and settings required when creating or modifying Route 53 VPC Resolver forwarding rules.
- [Managing outbound endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries-managing.html): View, edit, and delete outbound endpoints, including procedures for updating endpoint configurations and monitoring endpoint status.
- [Managing forwarding rules](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-rules-managing.html): Create, configure, and manage forwarding rules that control which DNS queries are forwarded from your VPCs to your on-premises network, including rule sharing and association with VPCs.
- [Resolver delegation rules tutorial](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outbound-delegation-tutorial.html): The delegation rule allows the VPC Resolver to reach the name servers that host the delegated zone through the specified outbound endpoint.
- [Enabling DNSSEC validation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dnssec-validation.html): Configure DNSSEC validation in Route 53 to cryptographically verify DNS responses and protect against DNS spoofing and cache poisoning attacks in your VPCs.


## [Routing internet traffic to your AWS resources](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-aws-resources.html)

- [Amazon API Gateway API](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-api-gateway.html): Using RouteÂ 53 to route traffic to an API Gateway API.
- [Amazon CloudFront distribution](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.html): Using RouteÂ 53 to route traffic to an Amazon CloudFront distribution.
- [Amazon EC2 instance](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-ec2-instance.html): Route traffic using RouteÂ 53 to an Amazon EC2 instance.
- [App Runner service](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-app-runner.html): Route traffic using RouteÂ 53 to an App Runner service.
- [Global Accelerator](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-global-accelerator.html): Route traffic using RouteÂ 53 to a Global Accelerator.
- [AWS Elastic Beanstalk environment](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-beanstalk-environment.html): Route traffic using RouteÂ 53 to an Elastic Beanstalk environment.
- [ELB load balancer](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-elb-load-balancer.html): Route queries using RouteÂ 53 to an ELB Classic, Application, or Network Load Balancer.
- [Amazon S3 bucket](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/RoutingToS3Bucket.html): Route traffic using RouteÂ 53 to a website that is hosted in an Amazon S3 bucket.
- [Amazon Virtual Private Cloud interface endpoint](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.html): Using RouteÂ 53 to route traffic to an Amazon VPC interface endpoint.
- [Amazon WorkMail](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-workmail.html): Using RouteÂ 53 to route traffic to WorkMail.
- [Amazon OpenSearch Service](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-open-search-service.html): Using RouteÂ 53 to route traffic to Amazon OpenSearch Service domain endpoint.
- [VPC Lattice](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-vpc-lattice-service.html): Using RouteÂ 53 to route traffic to VPC Lattice service domain endpoint.
- [Other AWS resources](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-additional-aws-resources.html): Using RouteÂ 53 to route traffic to other AWS resources.


## [Creating health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html)

- [Types of health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-types.html): You can create the following types of Amazon RouteÂ 53 health checks:
- [How RouteÂ 53 determines whether a health check is healthy](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html): Describes how a RouteÂ 53 health check determines whether a health check is healthy.

### [Creating, updating, and deleting health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-deleting.html)

Create, update, and delete RouteÂ 53 health checks.

- [Creating and updating health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating.html): The following procedure describes how to create and update health checks using the RouteÂ 53 console.
- [Values that you specify when you create or update health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-values.html): When you create or update health checks, you specify the applicable values.
- [Values that RouteÂ 53 displays when you create a health check](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-values-displayed.html): The Create Health Check page displays the following values based on the values that you typed:
- [Updating health checks when you change CloudWatch alarm settings](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-updating-cloudwatch-alarm-settings.html): If you create a RouteÂ 53 health check that monitors the data stream for a CloudWatch alarm and then you update the settings in the CloudWatch alarm, RouteÂ 53 doesn't automatically update the alarm settings in the health check.
- [Disabling or enabling health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-disable.html): Disabling a health check stops RouteÂ 53 from performing health checks.
- [Inverting health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-invert.html): If you invert a health check, RouteÂ 53 considers the health check to be unhealthy when the status is healthy and vice versa.
- [Deleting health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-deleting.html): To disable health checks, perform the following procedure.
- [Updating or deleting health checks when DNS failover is configured](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-updating-deleting-tasks.html): When you want to update or delete health checks that are associated with records, or you want to change records that have associated health checks, you must consider how your changes affect routing of DNS queries and your DNS failover configuration.
- [Configuring router and firewall rules for health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-router-firewall-rules.html): Configure your router and firewall rules for RouteÂ 53 health checks.

### [Configuring DNS failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring.html)

When you have more than one resource performing the same functionâfor example, more than one HTTP server or mail serverâyou can configure Amazon RouteÂ 53 to check the health of your resources and respond to DNS queries using only the healthy resources.

- [Task list for configuring DNS failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-how-to.html): Configure RouteÂ 53 to check the health of your resources.
- [How health checks work in simple configurations](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-simple-configs.html): Describes how health checks work with simple RouteÂ 53 configurations to route internet traffic to available resources.
- [How health checks work in complex configurations](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html): Describes how health checks work with complex RouteÂ 53 configurations to check the health of your resources.
- [How RouteÂ 53 chooses records when health checking is configured](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-how-route-53-chooses-records.html): How RouteÂ 53 chooses the records to return in response to a DNS query when health checking is configured
- [Active-active and active-passive failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-types.html): How you use RouteÂ 53 to set up active-active and active-passive failover configurations
- [Configuring failover in a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html): If you're creating failover records in a private hosted zone, note the following:
- [How RouteÂ 53 averts failover problems](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-problems.html): Describes how RouteÂ 53 averts problems in the event of cascading failures or internet partitions.
- [Naming and tagging health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-tagging.html): Add tags to RouteÂ 53 health checks for cost allocation and for assigning names to health checks.
- [Using API versions before 2012-12-12](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-using-old-apis.html): Describes RouteÂ 53 behavior when you try to use health checks with older versions of the RouteÂ 53 API.


## [Monitoring health check status and getting notifications](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-monitor-view-status.html)

- [Viewing health check status and the reason for health check failures](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-view-status.html): On the RouteÂ 53 console, you can view the status (healthy or unhealthy) of your health checks as reported by RouteÂ 53 health checkers.
- [Monitoring the latency between health checkers and your endpoint](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-health-check-latency.html): When you create a health check, if you choose to monitor the status of an endpoint (not the status of other health checks) and you choose the Latency graphs option, you can view the following values on CloudWatch graphs on the RouteÂ 53 console:
- [Monitoring health checks using CloudWatch](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-health-checks.html): View and monitor the status of RouteÂ 53 health checks using CloudWatch metrics.


## [Resolver DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html)

- [How Resolver DNS Firewall works](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-overview.html): Resolver DNS Firewall lets you control access to sites and block DNS-level threats for DNS queries going out from your VPC through the Route 53 VPC Resolver.
- [Region availability for DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-availability.html): Lists Route 53 VPC Resolver availability in AWS Regions.
- [Getting started with Resolver DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-getting-started.html): The DNS Firewall console includes a wizard that guides you through the following steps for getting started with DNS Firewall:

### [DNS Firewall rule groups and rules](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-groups.html)

This section describes the settings that you can configure for your DNS Firewall rule groups and rules, to define the DNS Firewall behavior for your VPCs.

- [Rule group settings in DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-settings.html): When you create or edit a DNS Firewall rule group, you specify the following values:
- [Rule settings in DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-settings.html): When you create or edit a rule in a DNS Firewall rule group, you specify the following values:
- [Rule actions in DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-actions.html): When DNS Firewall finds a match between a DNS query and a domain specification in a rule, it applies the action that's specified in the rule to the query.

### [Managing rule groups and rules in DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-managing.html)

To manage rule groups and rules in the console, follow the guidance in this section.

- [Creating a rule group and rules](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-adding.html): To create a rule group and add rules to it, follow the steps in this procedure.
- [Viewing and updating a rule group and rules](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-editing.html): Use the following procedure to view the rule groups and the rules assigned to them.
- [Deleting a rule group](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-deleting.html): To delete a rule group, perform the following procedure.

### [Resolver DNS Firewall domain lists](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-domain-lists.html)

A domain list is a reusable set of domain specifications that you use in a DNS Firewall rule, inside a rule group.

- [Managed Domain Lists](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-managed-domain-lists.html): Protect your resources using domain lists that AWS manages for you.
- [Managing your own domain lists](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-user-managed-domain-lists.html): Protect your resources with your own domain lists, which are collections of domain specifications that you can reuse in multiple firewall rule group rules.
- [DNS Firewall Advanced](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/firewall-advanced.html): DNS Firewall Advanced detects suspicious DNS queries based on known threat signatures in DNS queries.
- [Configuring query logging for DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/firewall-resolver-query-logs-configuring.html): You can evaluate your DNS Firewall rules by using Amazon CloudWatch metrics and the Resolver query logs.
- [Sharing rule groups between accounts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-sharing.html): You can share DNS Firewall rule groups between AWS accounts.

### [Enabling DNS Firewall protections for your VPC](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-vpc-protections.html)

You enable DNS Firewall protections for your VPC by associating one or more rule groups with the VPC.

- [Managing associations between your VPC and firewall rule groups](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-vpc-associating-rule-group.html)
- [DNS Firewall VPC configuration](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-vpc-configuration.html): The DNS Firewall configuration for your VPC determines whether Route 53 VPC Resolver allows queries through or blocks them during failures, for example when DNS Firewall is impaired, unresponsive, or not available in the zone.


## [What are Amazon Route 53 Profiles?](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profiles.html)

- [Using Profiles](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profile-high-level-steps.html): Overview of the process to implement Route 53 Profiles in your VPCs.

### [Create a Profile](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profile-create.html)

Create a new Route 53 Profile using the console or CLI.

- [Associate DNS Firewall rule groups](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profile-associate-dns-firewall.html): Associate DNS Firewall rule groups to a Profile for domain filtering.
- [Associate private hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profile-associate-private-hz.html): Associate private hosted zones to a Profile for DNS resolution.
- [Associate Resolver rules](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profile-associate-resolver-rules.html): Associate Resolver rules to a Profile for DNS forwarding.
- [Associate VPC endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profile-associate-vpc-endpoints.html): Associate interface VPC endpoints to a Profile for private connectivity.
- [Associate query logging configurations](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profile-associate-query-logging.html): Associate Resolver query logging configurations to a Profile for DNS query monitoring.

### [Edit Profile configurations](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profile-edit-configurations.html)

Configure VPC settings for DNS validation, reverse lookup, and firewall failure mode.

- [Configuration settings for Profiles](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/values-for-profile-configuration.html): Reference for Profile configuration values and settings.
- [Associate VPCs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profile-associate-vpcs.html): Associate a Profile to VPCs to apply DNS configurations.
- [Viewing and updating Profiles](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profiles-editing.html): View and update Profile properties and settings.

### [Viewing and updating resources associated to Profiles](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profiles-resources-editing.html)

View and manage resources associated with Profiles.

- [Disassociating a resource](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profiles-disassociate-resources.html): Remove resource associations from a Profile.
- [Viewing VPCs associated to a Profile](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profiles-vpcs-editing.html): View VPC associations with Profiles.
- [Working with shared Route 53 Profiles](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/sharing-profiles.html): Working with shared Route 53 Profiles.


## [What is Amazon Route 53 on Outposts?](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver.html)

- [Getting started with VPC Resolver on AWS Outposts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver-getting-started.html): Set up Route 53 VPC Resolver on your AWS Outposts by opting in to the service and configuring DNS resolution for your Outpost environment.
- [Creating inbound endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver-add-inbound-endpoints.html): Create inbound endpoints on AWS Outposts to enable DNS resolvers on your on-premises network to forward DNS queries to Route 53 VPC Resolver for AWS resource resolution.
- [Creating outbound endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver-add-outbound-endpoints.html): Create outbound endpoints on AWS Outposts to enable Route 53 VPC Resolver to forward DNS queries from your Outpost environment to DNS resolvers on your on-premises network.
- [Managing Resolver on Outpost](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver-manage.html): View, edit, and manage your Route 53 VPC Resolver on Outposts configuration, including viewing resolver status and updating settings.
- [Managing inbound endpoints on Resolver on Outpost](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver-manage-inbound.html): View, edit, and manage inbound endpoints on Route 53 VPC Resolver for Outposts, including viewing endpoint status and updating endpoint configurations.
- [Managing outbound endpoints on Resolver on Outpost](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver-manage-outbound-outpost.html): View, edit, and manage outbound endpoints on Route 53 VPC Resolver for Outposts, including viewing endpoint status and updating endpoint configurations.


## [What is Amazon Route 53 Global Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-what-is-global-resolver.html)

- [Concepts and terminology](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-concepts-terminology.html): Understand how Route 53 Global Resolver components work together to enable split-traffic DNS resolution, provide high availability through global anycast architecture, and secure DNS traffic from exfiltration attacks.
- [How it works](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-how-it-works.html): Learn how Route 53 Global Resolver enables split-traffic DNS resolution, provides high availability through anycast routing, and secures DNS queries by intercepting requests and applying security policies.
- [Use cases](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-cloud-resolver-use-cases.html): Explore how Route 53 Global Resolver enables split-traffic DNS resolution, provides high availability through global anycast architecture, and secures DNS traffic from exfiltration attacks.
- [Related services](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-related-services.html): Discover AWS services that complement Route 53 Global Resolver including Route 53 for private hosted zones, CloudWatch for monitoring, VPC for network integration, and security services for comprehensive threat protection.
- [Accessing Global Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-accessing-cloud-resolver.html): Learn the different ways to access and manage Route 53 Global Resolver including the AWS Management Console, AWS CLI, AWS SDKs, and AWS CloudFormation for infrastructure as code deployments.
- [Opt-in Region considerations](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-opt-in-regions.html): Learn about behavioral considerations when using Route 53 Global Resolver with opt-in AWS Regions, including account requirements, data replication, and service impacts when opting out of Regions.
- [Setting up account access](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-setting-up.html): Configure AWS account prerequisites before using Route 53 Global Resolver for the first time.
- [Tutorial: Create your first Route 53 Global Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-getting-started.html): Step-by-step tutorial for creating your first DNS filtering setup using Route 53 Global Resolver.

### [Managing DNS views](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-manage-dns-views.html)

Manage ongoing Route 53 Global Resolver operations including updating DNS views to control which client device groups can resolve to internal resources and what domains to filter.

- [Configure settings for DNS views](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-configure-dns-view-settings.html): Set up DNS policies and access controls in Route 53 Global Resolver for different groups of client devices based on their security requirements and access needs.

### [Managing access controls](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-managing-access-controls.html)

Configure Access Sources and Access Tokens to control which client devices can use your Route 53 Global Resolver infrastructure.

- [Access control methods](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-understanding-access-control-methods.html): Compare IP-based access sources and token-based authentication methods in Route 53 Global Resolver.
- [Configuring access sources](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-configuring-access-sources.html): Create and manage IP-based access sources using access source rules in Route 53 Global Resolver.

### [Managing access tokens](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-managing-access-tokens.html)

Create, distribute, and manage encrypted access tokens for secure client authentication in Route 53 Global Resolver.

- [Platform examples](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-platform-configuration-examples.html): Use these platform-specific examples to configure client devices with your Route 53 Global Resolver access tokens and connection details.
- [Best practices](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-access-control-best-practices.html): Implement security best practices for access source and token management in Route 53 Global Resolver.

### [Securing DNS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-securing-dns.html)

Create rules to secure DNS queries made by your clients.

- [Configure and manage DNS Firewall rules](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-configure-manage-firewall-rules.html)
- [Managed Domain Lists](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-managed-domain-lists.html): Managed Domain Lists contain domain names that are associated with malicious activity or other potential threats.
- [Build domain lists](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-build-domain-lists.html): You can create your own domain lists to specify domain categories that you either don't find in the managed domain list offerings or that you prefer to handle on your own.
- [DNS Firewall Advanced protections](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-dns-firewall-advanced-protections.html): DNS Firewall Advanced detects suspicious DNS queries based on known threat signatures in DNS queries.
- [Manage security policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-manage-dns-security-policies.html): Route 53 Global Resolver requires ongoing management to maintain optimal security and performance.

### [Configuring private hosted associations](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-configuring-private-hosted-zone-associations.html)

Route 53 Global Resolver enables you to resolve records associated with your Route 53 private hosted zones from your authorized clients.

- [Manage private hosted zone associations](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-private-hosted-zone-associations.html): Route 53 Global Resolver enables resolution of RouteÂ 53 private hosted zones.

### [Monitoring DNS activity](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-monitoring.html)

Monitor DNS performance, security events, and client activity using Route 53 Global Resolver with AWS monitoring tools.

- [Gain DNS visibility](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-gain-visibility-into-dns-activity.html): Enable DNS query logging in Route 53 Global Resolver to monitor client device activity, identify potential security threats, and analyze DNS resolution patterns.
- [Configure DNS monitoring](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-configure-dns-monitoring.html): Set up DNS query logging and monitoring in Route 53 Global Resolver to track client device activity and enable security analysis.

### [Troubleshooting DNS issues](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-troubleshooting-dns-issues.html)

Diagnose and resolve DNS connectivity, performance, and configuration issues affecting client devices using Route 53 Global Resolver.

- [Diagnose connectivity issues](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-diagnose-connectivity-issues.html): Systematically diagnose and resolve DNS connectivity problems affecting client devices using Route 53 Global Resolver.
- [Resolve performance issues](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-resolve-performance-issues.html): Address slow DNS resolution and optimize query response times for better client device performance using Route 53 Global Resolver.
- [Troubleshoot configuration](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-troubleshoot-configuration-issues.html): Identify and resolve common Route 53 Global Resolver configuration problems that affect DNS resolution including authentication issues, DNS view misconfigurations, and firewall rule conflicts.
- [Quotas](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/gr-load-balancer-limits.html): Learn about the quotas for Route 53 Global Resolver.


## [Code examples](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/service_code_examples.html)

### [RouteÂ 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/service_code_examples_route-53.html)

Code examples that show how to use RouteÂ 53 with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/service_code_examples_route-53_basics.html)

The following code examples show how to use the basics of RouteÂ 53 with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/service_code_examples_route-53_actions.html)

The following code examples show how to use RouteÂ 53 with AWS SDKs.

- [ChangeResourceRecordSets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53_example_route-53_ChangeResourceRecordSets_section.html): Use ChangeResourceRecordSets with a CLI
- [CreateHostedZone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53_example_route-53_CreateHostedZone_section.html): Use CreateHostedZone with a CLI
- [DeleteHostedZone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53_example_route-53_DeleteHostedZone_section.html): Use DeleteHostedZone with a CLI
- [GetHostedZone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53_example_route-53_GetHostedZone_section.html): Use GetHostedZone with a CLI
- [ListHostedZones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53_example_route-53_ListHostedZones_section.html): Use ListHostedZones with an AWS SDK or CLI
- [ListHostedZonesByName](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53_example_route-53_ListHostedZonesByName_section.html): Use ListHostedZonesByName with a CLI
- [ListQueryLoggingConfigs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53_example_route-53_ListQueryLoggingConfigs_section.html): Use ListQueryLoggingConfigs with a CLI

### [RouteÂ 53 domain registration](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/service_code_examples_route-53-domains.html)

Code examples that show how to use RouteÂ 53 domain registration with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/service_code_examples_route-53-domains_basics.html)

The following code examples show how to use the basics of RouteÂ 53 domain registration with AWS SDKs.

- [Hello RouteÂ 53 domain registration](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-domains_example_route-53-domains_Hello_section.html): Hello RouteÂ 53 domain registration
- [Learn the basics](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-domains_example_route-53-domains_Scenario_GetStartedRoute53Domains_section.html): Learn the basics of RouteÂ 53 domain registration with an AWS SDK

### [Actions](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/service_code_examples_route-53-domains_actions.html)

The following code examples show how to use RouteÂ 53 domain registration with AWS SDKs.

- [CheckDomainAvailability](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-domains_example_route-53-domains_CheckDomainAvailability_section.html): Use CheckDomainAvailability with an AWS SDK or CLI
- [CheckDomainTransferability](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-domains_example_route-53-domains_CheckDomainTransferability_section.html): Use CheckDomainTransferability with an AWS SDK or CLI
- [GetDomainDetail](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-domains_example_route-53-domains_GetDomainDetail_section.html): Use GetDomainDetail with an AWS SDK or CLI
- [GetDomainSuggestions](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-domains_example_route-53-domains_GetDomainSuggestions_section.html): Use GetDomainSuggestions with an AWS SDK or CLI
- [GetOperationDetail](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-domains_example_route-53-domains_GetOperationDetail_section.html): Use GetOperationDetail with an AWS SDK or CLI
- [ListDomains](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-domains_example_route-53-domains_ListDomains_section.html): Use ListDomains with an AWS SDK or CLI
- [ListOperations](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-domains_example_route-53-domains_ListOperations_section.html): Use ListOperations with an AWS SDK or CLI
- [ListPrices](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-domains_example_route-53-domains_ListPrices_section.html): Use ListPrices with an AWS SDK
- [RegisterDomain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-domains_example_route-53-domains_RegisterDomain_section.html): Use RegisterDomain with an AWS SDK or CLI
- [ViewBilling](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-domains_example_route-53-domains_ViewBilling_section.html): Use ViewBilling with an AWS SDK or CLI


## [Security](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/security.html)

### [Data protection](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in RouteÂ 53.

- [Protection from dangling delegation records](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/protection-from-dangling-dns.html): Learn how the RouteÂ 53 provides protection from dangling delegation records.

### [Identity and access management](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/security-iam.html)

Identifies methods for controlling access to your Amazon RouteÂ 53 resources.

- [Overview of managing access](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-overview.html): Every AWS resource is owned by an AWS account, and permissions to create or access a resource are governed by permissions policies.
- [Using IAM policies for RouteÂ 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/access-control-managing-permissions.html): This topic provides examples of identity-based policies that demonstrate how an account administrator can attach permissions policies to IAM identities and thereby grant permissions to perform operations on Amazon RouteÂ 53 resources.
- [Using Service-Linked Roles](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/using-service-linked-roles.html): How to use service-linked roles to give VPC Resolver access to resources in your AWS account.
- [AWS managed policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/security-iam-awsmanpol-route53.html): Learn about AWS managed policies for RouteÂ 53 and recent changes to those policies.
- [Using conditions](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/specifying-conditions-route53.html): Create fine-grained access control to individual items and attributes to manage resource record sets or VPCs associated with hosted zones.
- [RouteÂ 53 API permissions reference](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/r53-api-permissions-ref.html): When you set up and write a permissions policy that you can attach to an IAM identity (identity-based policies), you can use the lists of Actions, resources, and condition keys for RouteÂ 53, Actions, resources, and condition keys for RouteÂ 53 Domains, Actions, resources, and condition keys for VPC Resolver, and Actions, resources, and condition keys for Amazon RouteÂ 53 Profiles enables sharing DNS settings with VPCs in the Service Authorization Reference.
- [Logging and monitoring](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/logging-monitoring.html): Overview of logging and monitoring features available from Amazon RouteÂ 53 and from other AWS services that RouteÂ 53 integrates with.
- [Compliance validation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon RouteÂ 53 features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/infrastructure-security.html): Learn how Amazon RouteÂ 53 isolates service traffic.


## [Monitoring](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-overview.html)

- [Public DNS query logging](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html): Log the DNS queries that RouteÂ 53 edge locations respond to for a specified hosted zone.

### [Resolver query logging](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs.html)

Log the DNS queries that originate in Amazon Virtual Private Cloud VPCs.

- [Resources that you can send Resolver query logs to](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs-choosing-target-resource.html)

### [Managing configurations](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logging-configurations-managing.html)

- [Values that appear in Resolver query logs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs-format.html): Each log file contains one log entry for each DNS query that Amazon RouteÂ 53 received from DNS resolvers in the corresponding edge location.

### [Resolver query log example](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs-example-json.html)

Here's a resolver query log example:

- [Sharing Resolver query logging configs with other accounts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logging-configurations-managing-sharing.html): You can share the query logging configurations that you created using one AWS account with other AWS accounts.
- [Monitoring domain registrations](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-domain-registrations.html): Use the Amazon RouteÂ 53 dashboard to monitor the status of domain registrations.
- [Monitoring your resources with Amazon RouteÂ 53 health checks and Amazon CloudWatch](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-cloudwatch.html): You can monitor your resources by creating Amazon RouteÂ 53 health checks, which use CloudWatch to collect and process raw data into readable, near real-time metrics.
- [Monitoring hosted zones using Amazon CloudWatch](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-hosted-zones-with-cloudwatch.html): You can monitor your public hosted zones by using Amazon CloudWatch to collect and process raw data into readable, near real-time metrics.
- [Monitoring Route 53 VPC Resolver endpoints with Amazon CloudWatch](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.html): You can use Amazon CloudWatch to monitor the number of DNS queries that are forwarded by Route 53 VPC Resolver endpoints.
- [Monitoring Resolver DNS Firewall rule groups with Amazon CloudWatch](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-dns-firewall-with-cloudwatch.html): You can use Amazon CloudWatch to monitor the number of DNS queries that are filtered by Resolver DNS Firewall rule groups.

### [Managing DNS Firewall events using EventBridge](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-firewall-eventbridge-integration.html)

Receive notifications when specific DNS Firewall events, such as an alert or block action, occur in an DNS Firewall with EventBridge.

- [Events DNS Firewall detail reference](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/events-detail-reference.html): All events from AWS services have a common set of fields containing metadata about the event, such as the AWS service that is the source of the event, the time the event was generated, the account and region in which the event took place, and others.
- [Logging Amazon RouteÂ 53 API calls with AWS CloudTrail](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/logging-using-cloudtrail.html): Learn about logging Amazon RouteÂ 53 with AWS CloudTrail.


## [Troubleshooting](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/troubleshooting-route-53.html)

- [My domain is unavailable on the internet](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/troubleshooting-domain-unavailable.html): Troubleshoot common causes of domain unavailability including email confirmation issues, DNS service problems, and incorrect name server configurations.
- [My domain is suspended (status is ClientHold)](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/troubleshooting-domain-suspended.html): Resolve domain suspension issues including expired domains, unverified email addresses, payment problems, and policy violations.
- [My domain operation failed](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/troubleshooting-domain-operation-failed.html): Resolve domain operation failures including registration, transfer, renewal, and contact update issues caused by invalid contact information.
- [Transferring my domain to Amazon RouteÂ 53 failed](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/troubleshooting-domain-transfer-failed.html): Diagnose and resolve failed domain transfers to Amazon RouteÂ 53 using error messages and common failure scenarios.
- [I changed DNS settings, but they haven't taken effect](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/troubleshooting-new-dns-settings-not-in-effect.html): Troubleshoot DNS propagation delays, caching issues, and incorrect name server configurations that prevent DNS changes from taking effect.
- [My browser displays a "Server not found" error](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/troubleshooting-server-not-found.html): Resolve "Server not found" browser errors caused by missing DNS records, incorrect record values, or unavailable resources.
- [I can't route traffic to an Amazon S3 bucket that's configured for website hosting](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/troubleshooting-s3-bucket-website-hosting.html): Fix routing issues to S3 website buckets including bucket naming requirements and website hosting configuration problems.
- [I was billed twice for the same hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/troubleshooting-billed-twice.html): Understand hosted zone billing including monthly charges, prorated billing, and why charges may appear on multiple invoices.
- [I was charged multiple invoices for my domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/troubleshooting-multiple-invoices.html): Understand domain billing including multiple invoices, waived charges, and how to view successful payments and refunds.
- [My AWS account is closed or permanently closed, and my domain is registered with RouteÂ 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/troubleshooting-account-closed.html): Understand what happens to Route 53 registered domains when AWS accounts are closed including suspension timelines and recovery options.


## [Tutorials](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Tutorials.html)

### [Using Amazon RouteÂ 53 as the DNS service for subdomains without migrating the parent domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/creating-migrating.html)

Migrate subdomains to use RouteÂ 53 as their DNS service without migrating the parent domain.

- [Creating a subdomain that uses Amazon RouteÂ 53 as the DNS service without migrating the parent domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/CreatingNewSubdomain.html): Create a subdomain that uses RouteÂ 53 as the DNS service without migrating the parent domain from another DNS service.
- [Migrating DNS service for a subdomain to Amazon RouteÂ 53 without migrating the parent domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/MigratingSubdomain.html): Migrating DNS service for an existing subdomain to RouteÂ 53 without migrating the parent domain.
- [Transitioning to latency-based routing in Amazon RouteÂ 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/TutorialTransitionToLBR.html): With latency-based routing, Amazon RouteÂ 53 can direct your users to the lowest-latency AWS endpoint available.
- [Adding another Region to your latency-based routing in Amazon RouteÂ 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/TutorialAddingLBRRegion.html): If you're using latency based routing and you want to add an instance in a new region, you can gradually shift traffic to the new region in the same way that you gradually shifted traffic to latency-based routing in .
- [Using latency and weighted records in Amazon RouteÂ 53 to route traffic to multiple Amazon EC2 instances in a Region](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/TutorialLBRMultipleEC2InRegion.html): If your application is running on Amazon EC2 instances in two or more Amazon EC2 regions, and if you have more than one Amazon EC2 instance in one or more regions, you can use latency-based routing to route traffic to the correct region and then use weighted records to route traffic to instances within the region based on weights that you specify.
- [Managing over 100 weighted records in Amazon RouteÂ 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/TutorialManagingOver100WRR.html): Amazon RouteÂ 53 lets you configure weighted records.
- [Weighting fault-tolerant multi-record answers in Amazon RouteÂ 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/TutorialWeightedFTMR.html)


## [Best practices](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices.html)

- [Best practices for Amazon RouteÂ 53 DNS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-dns.html): Follow these best practices to get the best results when using the Amazon RouteÂ 53 DNS service.

### [Best practices for VPC Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver.html)

This section provides best practices for optimizing Amazon Route 53 VPC Resolver, covering the following topics:

- [Avoid loop configurations with Resolver endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver-endpoints.html): Prevent DNS query loops by avoiding configurations where the same VPC is associated with both a Resolver rule and its inbound endpoint.
- [Resolver endpoint scaling](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver-endpoint-scaling.html): Resolver endpoint security groups use connection tracking to gather information about traffic to and from the endpoints.
- [High availability for Resolver endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver-endpoint-high-availability.html): Configure Route 53 Resolver endpoints across multiple Availability Zones with redundant network interfaces to ensure high availability and handle traffic surges.
- [DNS zone walking](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver-zone-walking.html): Understand DNS zone walking attacks and how Route 53 VPC Resolver automatically throttles suspicious traffic patterns to protect your endpoints.
- [Best practices for Amazon RouteÂ 53 health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-healthchecks.html): Effective health check configuration is essential for maintaining a highly available and resilient infrastructure.
