# Source: https://docs.sinch.com/glossary.md

# Glossary

## **A**

**Account or Customer ID**

Usually, each customer number has an account identifier; this number is also referred to as Customer ID.

## **API**

API, or Application Programming Interface, is a set of [routines](https://en.wikipedia.org/wiki/Subroutine) and standards established by a [software](https://en.wikipedia.org/wiki/Software) for the use of its features by applications that do not intend to involve themselves with the software’s [implementation](https://en.wikipedia.org/wiki/Software_implementation) details, but only use its services.

## **B**

### **Blocklist**

Unlike the Whitelist, the Blocklist are numbers that the company adds and classifies as numbers that may not receive messages. E.g.: numbers from competitors.

## **C**

### **Carrier**

You are also the customer of a Carrier! By Carrier we mean the Service Provider that holds the number in question. I.e., if I have a TIM number, then the Carrier of my MSISDN is TIM.

### **Closed Session?**

A closed session is when more than 24 hours have passed from the user’s last contact or when there has been no contact from the user.

This way, in order for the company to open the session with the user once again, it needs to actively trigger an HSM, for example.

### **Conversion Rate**

Conversion rate (used especially by international customers) is the formula used to measure the number of messages sent and received VS the delivery volume. When there is a decrease in the DR, customers are directly affected in the conversion rate, and it may direct traffic to another SMS broker that has a better conversion rate.

## **D**

### **Deploy**

A Deploy is every update, release or new version of a feature. It can be under approval or in production, and all deploys improve or remove a certain feature.

### **DR or DLR (Delivery Report)**

DR, or Delivery Report, is the successful delivery confirmation status at the carrier. If the MT was successfully delivered, the DR will confirm the time of delivery of this SMS to the user. Note that if, at the time the SMS is sent, the device is turned off or has no signal, the DR time will be delayed.

## **F**

### **FTP**

FTP or File Transfer Protocol is a form of transferring files. It can refer to both the protocol and the program that implements said protocol. Transferring data in computer networks usually involves transferring files and accessing remote file systems (source: Wikipedia). This system is often used at Sinch for uploading large batches. Each platform (WA or SMS) must respect a pre-established format.

## **L**

### **LA**

LA, or Large Account, is a short number (up to digits) that is used to send the SMS. The numbers belong to the carriers and may only be used by approved partners.

## **M**

### **MO**

MO, or Mobile Originated, is every message that originates from a device to the company in question. It is used in the case of questions and answers via messages, when user confirmation is required.

### **MSISDN**

You certainly own an MSISDN! A Mobile Station International Subscriber Directory Number, or MSISDN, is a number that exclusively identifies a subscription to a GSM or UMTS mobile network. To make it even simpler, it is your cell phone number. In technical terms, all numbers of a carrier are referred to as MSISDNs. So, whenever you read MSISDN, you already know it refers to the cell phone number in question.

### **MT**

MT, or Mobile Terminated, is every message that is destined for the user’s device. I.e., the company sends a message to the number in question.

## **O**

### **Open Session**

When we initiate a contact or the user initiates the contact organically, we start counting it as an open session, as the company has 24 hours after the user’s interaction as a channel “open” for communication.

It also means, in the case of WhatsApp, that the company can send the user any MT and not just HSM (which requires approval from Facebook) like when the session is closed.

### **Opt-in**

Opt-in is the permission given by the user for a company to contact them through a given channel. This permission can be, for instance, through the website of the company itself, via email or SMS.

### **Opt-out**

Opt-out is when the user chooses to no longer receive messages from that contact through a given channel. When a user opts out of a contact list, our system blocks any delivery attempts that may occur to the user from that contact.

## **S**

### **Subaccount**

Within Sinch, we have an architecture that enables our customers to use the same number to serve multiple purposes.

Within an Account, you can have multiple Subaccounts with customized “departments” and settings, where you can trigger many different options such as service, CRM, Request Status, among others.

Each subaccount can have its own users and webhook, this enables the optimization of a customer’s number.

## **V**

### **VPN**

A VPN, or Virtual Private Network, is a private communications network built on a public communications network (such as the [Internet](https://en.wikipedia.org/wiki/Internet)). Data traffic is carried by the public network using standard [protocols](https://en.wikipedia.org/wiki/Communication_protocol), not necessarily secure. In summary, it creates a secure and encrypted connection, that can be considered a tunnel, between your computer and a server operated by the VPN service.

## **W**

### **WhatsApp Template**

A template used to send active messages to your customers. Every template must be approved by WhatsApp prior to its usage – this way, they ensure that you are following their guidelines for allowed content.

### **Webhook**

A webhook is the information bridge between our Sinch system and the company that owns the Webhook.

This bridge is done through a URL where information passes between our system and the system desired by our customer.

### **Whitelist**

Users on the Whitelist are users that the company adds and classifies as users that may receive messages. This does not mean that said user has given permission at any time.
