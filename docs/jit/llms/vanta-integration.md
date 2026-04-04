# Source: https://docs.jit.io/docs/vanta-integration.md

# Vanta Integration

## Overview

The Vanta integration allows you to automatically sync Jit’s security findings and vulnerable assets into your Vanta environment. This helps keep your compliance evidence fresh and ensures your risk posture inside Vanta reflects the latest results from Jit's security testing.

Once connected, Jit continuously updates Vanta with relevant vulnerabilities and assets, enabling smoother audits and more complete compliance coverage.

***

## What This Integration Provides

The integration currently supports:

### **Automated Security Finding Sync**

Jit sends updated security findings to Vanta **daily**, ensuring your Vanta evidence and controls reflect your real, current security posture.

### **Multiple Vulnerability Types**

Jit syncs findings across:

* **SAST** – Static code analysis findings
* **DAST** – Runtime application testing findings
* **SCA** – Dependency and third-party library vulnerabilities

### **Vulnerable Asset Tracking**

The integration syncs vulnerable assets into Vanta, including:

* Repositories
* APIs
* Web applications

This enhances Vanta’s asset inventory with real security context.

### **Context Enrichment**

Jit adds metadata and severity context to synced findings, improving prioritization and auditability inside Vanta.

***

## Setup Requirements

Before you begin, ensure:

* You have an active **Vanta** account with admin or integration permissions
* Your **Jit** account has admin permissions to connect integrations
* You are logged into both platforms

The integration uses **OAuth**, so no API keys or tokens are required.

***

## How to Connect Vanta to Jit

1. In the Jit app, go to **Integrations**
2. Locate the **Vanta** integration card
3. Click **Connect**
4. You will be redirected to Vanta’s OAuth authorization page
5. Log in to Vanta and approve the connection
6. You will be redirected back to Jit, and the integration will show as **Connected**

After setup, Jit will start syncing data to Vanta within the next scheduled cycle.

***

## What Jit Syncs to Vanta

### **1. Vulnerable Assets**

Synced as Vanta *VulnerableComponent* resources:

* Repositories
* Web applications
* APIs

### **2. Security Findings**

Grouped by vulnerability type:

* **SAST** – Code vulnerabilities
* **DAST** – Runtime and application security vulnerabilities
* **SCA** – Dependency vulnerabilities

Jit does *not* sync resolved issues retroactively; Vanta will reflect the current state during each sync.

***

## Sync Frequency

Jit syncs data to Vanta **daily** via Paragon workflows:

1. Sync vulnerable assets
2. Sync security findings (SAST, DAST, SCA)
3. Update context and metadata

This ensures Vanta has up-to-date evidence for monitoring and certification work.

***

## Troubleshooting

If the integration is not syncing as expected:

### **Verify OAuth Connection**

Check that the Vanta integration shows as **Connected** in Jit.

### **Check Vanta Permissions**

Ensure the Vanta user who connected the integration still has permission to receive synced data.

### **Check Sync Timing**

Syncs occur once per day. Recent updates may take until the next scheduled run to appear.

### **Contact Support**

If issues persist, reach out to Jit Support.

***

## Need Help?

For assistance with configuration or troubleshooting, contact **Jit Support**.