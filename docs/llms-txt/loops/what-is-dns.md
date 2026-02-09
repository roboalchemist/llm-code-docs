# Source: https://loops.so/docs/guides/what-is-dns.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# What is DNS?

> A Beginner's Guide

Have you ever wondered how the internet seems to know precisely where to go when you type a website's name into your browser's address bar? How does your computer know to show you the right page when you type in "[www.loops.so](http://www.loops.so)"? The answer to these questions lies in the Domain Name System or DNS.

DNS is an essential part of the Internet's inner workings, serving as the Internet's equivalent of your iPhone’s address book. But what exactly is DNS, and why is it so important?

To understand DNS, we first need to understand how the Internet works. Let’s dive in!

## What is DNS?

Every device connected to the Internet, including computers, phones, and servers, has a unique IP address.

An IP address is a string of numbers separated by periods that identifies each computer using the Internet Protocol to communicate over a network. For example, an IP address might look like this: "192.168.0.1".

However, humans generally find it much easier to remember names rather than strings of numbers. This is where the **Domain Name System (DNS)** comes in. The DNS translates the domain names that we humans easily understand and remember into the IP addresses that computers use to identify each other on the network!

For instance, when you type in "[www.loops.so](http://www.loops.so)" into your web browser, your computer sends a request to a DNS server asking for the IP address associated with that domain name.

The DNS server responds with the IP address, and your computer then sends a request to that IP address to fetch and display the website.

The process of converting domain names into IP addresses is known as **DNS resolution**, and it usually takes only milliseconds. DNS servers are strategically located around the world and work together to ensure that these requests are processed quickly and accurately.

## Why is DNS important

Now, why is DNS crucial? Firstly, it makes the internet user-friendly.

Without DNS, we would have to memorize complex IP addresses for each website we wanted to visit. Secondly, it ensures the smooth operation of the internet. Every time you send an email, browse a website, or use an app, DNS is working behind the scenes to route your request to the right destination.

And if that wasn’t enough, DNS also provides a level of security. DNS servers can filter and block access to certain websites that might be harmful or inappropriate, providing an essential layer of protection for internet users. It helps you verify the authenticity of a sender via email as we’ll cover in the next section.

## DNS and email

DNS is vital for the functioning of email.

### Sending email

When you send an email, your email client needs to know where to send it.

Let's say you're sending an email to [someone@gmail.com](mailto:someone@gmail.com).

The client doesn't inherently know where "gmail.com" is, just like your web browser wouldn't know where to go if you entered that into the address bar. DNS steps in to resolve "gmail.com" into an IP address that represents the actual server your email needs to reach.

### Routing email to the right location

DNS is used for email routing, particularly through a type of DNS record called the MX (Mail Exchanger) record.

An MX record is a type of record that specifies a mail server responsible for accepting email messages on behalf of a recipient's domain.

A priority value (a number like 10 is typical) is used to prioritize mail delivery if multiple mail servers are available. Without the MX records, your email wouldn't know which server to go to.

### Security

Most importantly, DNS plays a critical role in email security.

For instance, Sender Policy Framework (SPF) and DomainKeys Identified Mail (DKIM) are two methods used to prevent email spoofing, a technique used in phishing and spam campaigns where the sender masquerades as another by forging the header data.

SPF and DKIM utilize DNS to hold text records that a recipient's server can check to verify the sender's identity.

In essence, DNS is a cornerstone for email operations and security. It helps your email find its way to the correct server, ensures the recipient's server can accept the mail, and provides mechanisms to verify the sender's identity to combat fraudulent activities. Without DNS, our email system would be far less reliable and secure.

## Send better email with Loops

In summary, the Domain Name System, or DNS, is a critical component of both the internet and email as a whole, transforming the web from a complicated network of numeric addresses into an accessible and secure environment for users worldwide.

It's the silent hero that allows us to navigate the digital world with ease, translating memorable website names into computer-friendly IP addresses.

So, the next time you browse the internet or send that time-sensitive email, take a moment to appreciate the extraordinary system that makes it all possible: **DNS**.
