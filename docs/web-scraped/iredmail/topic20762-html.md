# Source: https://forum.iredmail.org/topic20762.html

Title: A Heartfelt Thank You to Our iRedAdmin-Pro and iRedMail Easy Customers (Page 1) — News, Announcements, Bug fixes... — iRedMail

URL Source: https://forum.iredmail.org/topic20762.html

Markdown Content:
Pages**1**

You must [login](https://forum.iredmail.org/login.html) or [register](https://forum.iredmail.org/register.html) to post a reply

### 1[2025-01-24 17:10:38](https://forum.iredmail.org/post90232.html#p90232 "Permanent link to this post")

*   ![Image 1: ZhangHuangbin](https://forum.iredmail.org/img/avatars/2.png)
*   **ZhangHuangbin**
*   iRedMail Developers
*   Offline

*   Registered: **2009-05-06**
*   Posts: **31,619**

#### Topic: A Heartfelt Thank You to Our iRedAdmin-Pro and iRedMail Easy Customers

We are incredibly grateful for your continued support. As you already know, first stable release of our flagship product ["iRedMail Enterprise Edition" version v1.0.0 is out](https://forum.iredmail.org/topic20761-exciting-news-iredmail-enterprise-edition-ee-v100-is-here.html). As part of our commitment to you, we’re pleased to offer the following benefits for our iRedAdmin-Pro and iRedMail Easy customers.

##### For iRedAdmin-Pro Customers:

*   If you purchased an iRedAdmin-Pro license before January 25, 2025 (excluding the 25th) AND it’s still valid, we’re offering you an **EE license** with **unlimited mailboxes** support at **no additional cost**. This EE license will have the same expiration date and renewal fee ($250 per year) as your current iRedAdmin-Pro license.

    *   **Exception:** If you hold a lifetime iRedAdmin-Pro license (last sold in January 2015, which was 10 years ago), your complimentary EE license will be valid for **one year**.

    *   Your existing iRedAdmin-Pro license remains valid. After migrating to iRedMail EE, you can choose to use either license and renew only one—or continue using both if you prefer.

##### For iRedMail Easy Customers:

*   If you’re on an **annual subscription**, we’re offering you an EE license with **unlimited mailboxes** support, and same expiration date as your iRedMail Easy subscription -- **completely free**. The renewal fee will match that of the iRedAdmin-Pro license ($250 per year).

*   If you’re on a **monthly plan**, simply switch to the annual plan, then we’ll provide you with an EE license aligned with your new annual subscription term, also at no extra cost.

*   Please note that the iRedMail Easy platform will be discontinued on January 25, 2026.

##### How to get the free EE license

You're free to request the free EE license anytime BEFORE your iRedAdmin-Pro license or iRedMail Easy subscription expired. We will generate the EE license key for you as soon as possible. ![Image 2: smile](https://forum.iredmail.org/img/smilies/smile.png)

*   Please sign up to our iRedMail Store: [https://store.iredmail.org/](https://store.iredmail.org/)

*   Login to iRedMail Store and create a ticket with your valid iRedAdmin-Pro license key. We will create EE license for you as soon as possible.

##### Migration Tutorials

*   [Migrate from a server deployed with the downloadable iRedMail installer](https://docs.iredmail.org/iredmail.to.ee.html)

*   [Migrate from a server deployed with iRedMail Easy](https://docs.iredmail.org/easy.to.ee.html)

----

[Spider Email Archiver](https://spiderd.io/): On-Premises, lightweight email archiving software developed by iRedMail team. Supports Amazon S3 compatible storage and custom branding.

### 2 Reply by **jstewart**[2025-01-24 23:53:39](https://forum.iredmail.org/post90236.html#p90236 "Permanent link to this post")

*   **jstewart**
*   Member
*   Offline

*   Registered: **2017-02-10**
*   Posts: **104**

#### Re: A Heartfelt Thank You to Our iRedAdmin-Pro and iRedMail Easy Customers

Looks good. I have question about the license - we have a Pro licence, since 2018, up for renewal in July. Do I understand that I can get the new free EE licence now and deploy it to a new server that I can then work on migrating mail to the new server? And on the pricing page, I see $3000 per server with a $1200 renewal. Do I understand correctly that if I get the EE licence now because I have an existing Pro license the annual renewal will still be $250 per year?

### 3 Reply by **ZhangHuangbin**[2025-01-25 00:01:02](https://forum.iredmail.org/post90237.html#p90237 "Permanent link to this post")

*   ![Image 3: ZhangHuangbin](https://forum.iredmail.org/img/avatars/2.png)
*   **ZhangHuangbin**
*   iRedMail Developers
*   Offline

*   Registered: **2009-05-06**
*   Posts: **31,619**

#### Re: A Heartfelt Thank You to Our iRedAdmin-Pro and iRedMail Easy Customers

jstewart wrote:

> Looks good. I have question about the license - we have a Pro licence, since 2018, up for renewal in July. Do I understand that I can get the new free EE licence now and deploy it to a new server that I can then work on migrating mail to the new server?

Hi @jstewart,

- Yes you can get the free EE license NOW, or anytime before your iRedAdmin-Pro license expired.

- You can migrate to EE in-place instead of setup a new server and move. Migration tutorials attached in the announcement post above. (sorry i forgot to add them at the beginning.) And of course moving to a new server is always an option too.

jstewart wrote:

> And on the pricing page, I see $3000 per server with a $1200 renewal. Do I understand correctly that if I get the EE licence now because I have an existing Pro license the annual renewal will still be $250 per year?

YES, as mentioned in the announcement.

Since you own a valid iRedAdmin-Pro license (and purchased before Jan 25 2025), you get one EE license without additional cost (which means you save $3000 - the initial purchase). And as promised, you can renew it at $250 per year before EE license expired.

### 4 Reply by **jstewart**[2025-01-25 00:11:34](https://forum.iredmail.org/post90238.html#p90238 "Permanent link to this post")

*   **jstewart**
*   Member
*   Offline

*   Registered: **2017-02-10**
*   Posts: **104**

#### Re: A Heartfelt Thank You to Our iRedAdmin-Pro and iRedMail Easy Customers

Excellent. Our existing server was initially deployed in 2018, so it is running Centos 7. I'm thinking the ideal path would be to create a new almalinux 9 server and migrate accounts to the new server, then retire the old server.

Is there anything important to consider prior to the migration, and do you have steps for that rather than an in-place upgrade? This is an LDAP installation.

### 5 Reply by **ZhangHuangbin**[2025-01-25 00:14:15](https://forum.iredmail.org/post90239.html#p90239 "Permanent link to this post")

*   ![Image 4: ZhangHuangbin](https://forum.iredmail.org/img/avatars/2.png)
*   **ZhangHuangbin**
*   iRedMail Developers
*   Offline

*   Registered: **2009-05-06**
*   Posts: **31,619**

### 6 Reply by **FMB**[2025-01-25 00:18:13](https://forum.iredmail.org/post90240.html#p90240 "Permanent link to this post")

*   **FMB**
*   Member
*   Offline

*   Registered: **2018-05-04**
*   Posts: **13**

#### Re: A Heartfelt Thank You to Our iRedAdmin-Pro and iRedMail Easy Customers

Will you keep providing updates for iRedAdmin-Pro?

### 7 Reply by **ZhangHuangbin**[2025-01-25 10:37:29](https://forum.iredmail.org/post90246.html#p90246 "Permanent link to this post")

*   ![Image 5: ZhangHuangbin](https://forum.iredmail.org/img/avatars/2.png)
*   **ZhangHuangbin**
*   iRedMail Developers
*   Offline

*   Registered: **2009-05-06**
*   Posts: **31,619**

#### Re: A Heartfelt Thank You to Our iRedAdmin-Pro and iRedMail Easy Customers

FMB wrote:

> Will you keep providing updates for iRedAdmin-Pro?

Yes, we will keep maintaining iRedAdmin-Pro, but mostly small features, bug / security fixes, no more big changes.

### 8 Reply by **Jochen**[2025-01-26 23:23:47](https://forum.iredmail.org/post90262.html#p90262 "Permanent link to this post")

*   **Jochen**
*   Member
*   Offline

*   Registered: **2014-03-31**
*   Posts: **80**

#### Re: A Heartfelt Thank You to Our iRedAdmin-Pro and iRedMail Easy Customers

Hi,

congratulation on the release. I hope it goes well for you in the future, as you seem to focus a totally new customer niche.

We are long time users of iRedMail, we have an iRedAdminPro LTD and an ongoing Easy managed server.

The Easy manged server is our main Mail-Server holding the accounts. A second, smaller server is run as backupMX using the iRedAdminPro for administering this.

Do I get this right, that we should change the Easy subscription to an EE subscription and that will cost $250 per year. The license is similar in that it is per server and does not restrict the numbers of domains or mailboxes. Can we keep running the backup mx setup using iRedAdminPro?

Thanks, best

Jochen

### 9 Reply by **ZhangHuangbin**[2025-01-27 10:56:55](https://forum.iredmail.org/post90266.html#p90266 "Permanent link to this post")

*   ![Image 6: ZhangHuangbin](https://forum.iredmail.org/img/avatars/2.png)
*   **ZhangHuangbin**
*   iRedMail Developers
*   Offline

*   Registered: **2009-05-06**
*   Posts: **31,619**

#### Re: A Heartfelt Thank You to Our iRedAdmin-Pro and iRedMail Easy Customers

Jochen wrote:

> Do I get this right, that we should change the Easy subscription to an EE subscription and that will cost $250 per year.

Easy subscription costs either $499 (annual plan) or $588 ($49 per month, 12 months). After switched to EE (without additional cost in this case) costs $250 annual renewal fee for loyal Easy subscribers like you, it's at least 2 times cheaper ($499 / $588 vs $250)

Jochen wrote:

> The license is similar in that it is per server and does not restrict the numbers of domains or mailboxes.

Yes, the offered EE license supports unlimited mailboxes, just like iRedAdmin-Pro.

Jochen wrote:

> Can we keep running the backup mx setup using iRedAdminPro?

Yes.

### 10 Reply by **Jochen**[2025-01-27 20:35:19](https://forum.iredmail.org/post90268.html#p90268 "Permanent link to this post")

*   **Jochen**
*   Member
*   Offline

*   Registered: **2014-03-31**
*   Posts: **80**

#### Re: A Heartfelt Thank You to Our iRedAdmin-Pro and iRedMail Easy Customers

ZhangHuangbin wrote:

> Easy subscription costs either $499 (annual plan) or $588 ($49 per month, 12 months). After switched to EE (without additional cost in this case) costs $250 annual renewal fee for loyal Easy subscribers like you, it's at least 2 times cheaper ($499 / $588 vs $250)
> 
> 
> 
> Jochen wrote:
> 
> 
> > Can we keep running the backup mx setup using iRedAdminPro?
> 
> 
> Yes.

Cool, thank you. I hope this change in strategy goes well for you.

Best,

Jochen

### 11 Reply by **acomav**[2025-03-12 19:42:18](https://forum.iredmail.org/post90520.html#p90520 "Permanent link to this post")

*   **acomav**
*   Member
*   Offline

*   Registered: **2015-06-22**
*   Posts: **10**

#### Re: A Heartfelt Thank You to Our iRedAdmin-Pro and iRedMail Easy Customers

"Exception: If you hold a lifetime iRedAdmin-Pro license (last sold in January 2015, which was 10 years ago), your complimentary EE license will be valid for one year.

Your existing iRedAdmin-Pro license remains valid. After migrating to iRedMail EE, you can choose to use either license and renew only one—or continue using both if you prefer."

Hi,

 Can you please elaborate on customers with the lifetime Pro license? I understand we get an EE license for 1 year, but what it the renewal price after that?Is it $250 or $1200 or something else? 

Thanks,

 David

### 12 Reply by **ZhangHuangbin**[2025-03-13 08:54:23](https://forum.iredmail.org/post90521.html#p90521 "Permanent link to this post")

*   ![Image 7: ZhangHuangbin](https://forum.iredmail.org/img/avatars/2.png)
*   **ZhangHuangbin**
*   iRedMail Developers
*   Offline

*   Registered: **2009-05-06**
*   Posts: **31,619**

#### Re: A Heartfelt Thank You to Our iRedAdmin-Pro and iRedMail Easy Customers

acomav wrote:

> I understand we get an EE license for 1 year, but what it the renewal price after that?Is it $250 or $1200 or something else?

$250 per year.

### 13 Reply by **rbd2**[2025-04-08 01:43:16](https://forum.iredmail.org/post90673.html#p90673 "Permanent link to this post")

*   **rbd2**
*   Member
*   Offline

*   Registered: **2014-10-31**
*   Posts: **6**

#### Re: A Heartfelt Thank You to Our iRedAdmin-Pro and iRedMail Easy Customers

Hi Zhang!

Is there any reason we would not want to convert our Pro into an EE? i.e. Any local customization or flexibility issues - or anything else I'm not thinking about?

It looks like a lot of manual pre-configuration to make the switch.

Thanks,

Ray

### 14 Reply by **ZhangHuangbin**[2025-04-08 10:06:21](https://forum.iredmail.org/post90674.html#p90674 "Permanent link to this post")

*   ![Image 8: ZhangHuangbin](https://forum.iredmail.org/img/avatars/2.png)
*   **ZhangHuangbin**
*   iRedMail Developers
*   Offline

*   Registered: **2009-05-06**
*   Posts: **31,619**

#### Re: A Heartfelt Thank You to Our iRedAdmin-Pro and iRedMail Easy Customers

rbd2 wrote:

> Is there any reason we would not want to convert our Pro into an EE? i.e. Any local customization or flexibility issues - or anything else I'm not thinking about?
> 
> It looks like a lot of manual pre-configuration to make the switch.

Hi Ray,

You may not migrate to EE if:

- you made complex customizations to Postfix/Dovecot/...

- you run iRedAdmin-Pro in a cluster

Otherwise it should be better migrate to EE.

It's too hard to extract customizations from config files automatically with a shell/perl/python/... script, you have to do this manually, but if you didn't do much customizations, it should be very easy to get it done. Just give it a try. ![Image 9: smile](https://forum.iredmail.org/img/smilies/smile.png)

### 15 Reply by **jackb**[2025-05-23 00:57:28](https://forum.iredmail.org/post90871.html#p90871 "Permanent link to this post")

*   **jackb**
*   Member
*   Offline

*   From: **Ireland**
*   Registered: **2019-05-06**
*   Posts: **130**

#### Re: A Heartfelt Thank You to Our iRedAdmin-Pro and iRedMail Easy Customers

Thanks for a great solution served us since 2016.

Quick question. What about iredmail? Not enterprise or easy Is that version affected?

Regards

### 16 Reply by **ZhangHuangbin**[2025-05-23 14:20:51](https://forum.iredmail.org/post90874.html#p90874 "Permanent link to this post")

*   ![Image 10: ZhangHuangbin](https://forum.iredmail.org/img/avatars/2.png)
*   **ZhangHuangbin**
*   iRedMail Developers
*   Offline

*   Registered: **2009-05-06**
*   Posts: **31,619**

#### Re: A Heartfelt Thank You to Our iRedAdmin-Pro and iRedMail Easy Customers

jackb wrote:

> What about iredmail? Not enterprise or easy Is that version affected?

We continue maintaining it, no worries.

### 17 Reply by **jackb**[2025-05-23 14:22:42](https://forum.iredmail.org/post90875.html#p90875 "Permanent link to this post")

*   **jackb**
*   Member
*   Offline

*   From: **Ireland**
*   Registered: **2019-05-06**
*   Posts: **130**

#### Re: A Heartfelt Thank You to Our iRedAdmin-Pro and iRedMail Easy Customers

ZhangHuangbin wrote:

> jackb wrote:
> 
> 
> > What about iredmail? Not enterprise or easy Is that version affected?
> 
> 
> We continue maintaining it, no worries.

That's great. Is there anyway we can donate for the free version?

Regards.

### 18 Reply by **ZhangHuangbin**[2025-05-23 14:24:25](https://forum.iredmail.org/post90877.html#p90877 "Permanent link to this post")

*   ![Image 11: ZhangHuangbin](https://forum.iredmail.org/img/avatars/2.png)
*   **ZhangHuangbin**
*   iRedMail Developers
*   Offline

*   Registered: **2009-05-06**
*   Posts: **31,619**

#### Re: A Heartfelt Thank You to Our iRedAdmin-Pro and iRedMail Easy Customers

jackb wrote:

> That's great. Is there anyway we can donate for the free version?

You can send to our PayPal account "paypal _at_ iredmail.org" directly. Thanks in advance.

Pages**1**

You must [login](https://forum.iredmail.org/login.html) or [register](https://forum.iredmail.org/register.html) to post a reply
