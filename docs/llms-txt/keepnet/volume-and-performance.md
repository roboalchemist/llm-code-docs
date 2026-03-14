# Source: https://doc.keepnetlabs.com/resources/volume-and-performance.md

# Volume & Performance

Keepnet's platform is built to support high-volume operations with optimized performance across all its cybersecurity simulations and training services. Our infrastructure ensures seamless scalability, allowing organizations to conduct phishing, smishing, vishing simulations, and security training efficiently and securely. Below is a detailed breakdown of our platform's capacity and speed across different services.

## **Email Phishing Simulation**

* Handles thousands to millions of emails per day via **SMTP**, with a delivery speed of up to 100,000 emails per minute under ideal conditions.
* If **Direct Email Campaign (DEC)** is selected, the sending limit is **130,000 requests per 10 seconds**, but this is configurable based on requirements.
* Configurable in **Phishing Campaign > Campaign Settings > Delivery**, optimized automatically for better delivery.
  * [Phishing Simulator Delivery Settings](https://doc.keepnetlabs.com/next-generation-product/platform/phishing-simulator/phishing-campaign-manager#delivery-settings)

## **SMS Phishing Simulation (Smishing)**

* **U.S. & Canada**:
  * **Toll-Free Numbers**: 3 MPS (scalable upon request).
  * **10DLC**: 1-75 MPS (carrier-dependent).
  * **Short Codes**: 100 MPS (default, scalable).
* **International SMS**:
  * Varies by country (1-100 MPS).
  * Twilio automatically optimizes messages for compliance.
* **Scalability Features**:
  * Multiple number pooling.
  * Adaptive routing for efficient delivery.
  * Configurable in **Smishing Simulator > SMS Settings**.
  * [Smishing Campaign Manager Settings](https://doc.keepnetlabs.com/next-generation-product/platform/smishing-simulator/smishing-campaign-manager#sms-settings)

## **Voice Phishing Simulation (Vishing)**

* **Default Call Speed**: 1 CPS (scalable to 100+ CPS for enterprises).
* **Concurrent Calls**: No hard limit, automatically scales with demand.
* **Call Routing & Scaling**:
  * Elastic SIP Trunking supports thousands of concurrent calls.
  * WebRTC & Twilio Client support high-volume browser-based calls.
* **Configurable in Vishing Campaign Manager > Call Settings**.
  * [Vishing Campaign Manager Settings](https://doc.keepnetlabs.com/next-generation-product/platform/vishing-simulator/vishing-campaign-manager#call-settings)

## **Training Enrollment via Email**

* Handles thousands to millions of emails per day via **SMTP**, with a delivery speed of up to 100,000 emails per minute under ideal conditions.
* If **Direct Email Campaign (DEC)** is selected, the sending limit is **130,000 requests per 10 seconds**, but this is configurable based on requirements.
* Optimized automatically for high-speed, reliable delivery.

## **Training Content Delivery (AWS CloudFront CDN)**

Keepnet utilizes **Amazon CloudFront** for secure, high-speed training content distribution.

* **Throughput & Data Transfer**:
  * Can handle **terabits per second (Tbps)**.
  * Low-latency delivery with AWS backbone optimization.
* **Requests Per Second (RPS)**:
  * Scales across **600+ AWS edge locations**.
  * Supports **millions of RPS**.
* **Latency & Performance**:
  * Cached requests served in **<50ms**.
  * Origin fetch latency depends on backend response time.
