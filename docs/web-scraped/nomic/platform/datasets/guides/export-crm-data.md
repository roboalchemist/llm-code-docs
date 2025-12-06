# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/guides/export-crm-data

Atlas is particularly valuable for analyzing CRM and customer support data, as it helps teams uncover patterns and insights across large volumes of customer interactions. By visualizing customer descriptions, support tickets, and sales notes in Atlas's interactive maps, teams can better understand customer segments, common pain points, and emerging trends. This semantic analysis of customer data can inform product decisions, improve customer service, and guide sales strategy. Below are steps to help you export your data from common CRM and support platforms to analyze in Atlas.

## Hubspot​

- Navigate to CRM > Contacts, Companies, or Deals in your HubSpot account
- Open the view you want to export (e.g., "All Contacts")
- Click Export in the top right of the table
- Configure export settings:

Choose CSV as the file format
Select language for column headers
For Contacts: Include descriptive fields like "About Us", "Bio", or "Notes"
For Companies: Export "Description" or combine "Industry" + "About Us" fields
For Deals: Include "Deal Description" and "Notes" fields
- Choose CSV as the file format
- Select language for column headers
- For Contacts: Include descriptive fields like "About Us", "Bio", or "Notes"
- For Companies: Export "Description" or combine "Industry" + "About Us" fields
- For Deals: Include "Deal Description" and "Notes" fields
- Click Export and download the file from the email link when ready
Note: Exports are limited to 300 per 24 hours. Large exports may be split into multiple CSV files and zipped if over 2MB.

Hubspot export documentation

## Salesforce​

- From Setup, enter "Data Export" in Quick Find box and select Data Export
- Choose "Export Now" for immediate export or "Schedule Export" for recurring backups
- Select data to export:

Check "Include all data" for complete export
Or select specific objects like Leads, Contacts, Accounts, Opportunities
Enable "Include images, documents and attachments" if needed
- Check "Include all data" for complete export
- Or select specific objects like Leads, Contacts, Accounts, Opportunities
- Enable "Include images, documents and attachments" if needed
- Configure export settings:

Choose encoding format (UTF-8 recommended)
Set scheduling options if doing recurring export
- Choose encoding format (UTF-8 recommended)
- Set scheduling options if doing recurring export
- Click "Start Export" or "Save" for scheduled exports
- Download zip file from email link when export completes (available for 48 hours)
Salesforce Data Export Guide

## Zendesk​

- In Admin Center, click Account in the sidebar, then select Tools > Reports
- Choose export format:

JSON export (recommended for >200k tickets): Select date range and data type
CSV export: Select date range only
XML export: Request file for each data type
- JSON export (recommended for >200k tickets): Select date range and data type
- CSV export: Select date range only
- XML export: Request file for each data type
- When export completes, download zip file from email link
Zendesk Export Guide

- Hubspot
- Salesforce
- Zendesk
