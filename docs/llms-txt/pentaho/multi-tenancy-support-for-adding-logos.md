# Source: https://docs.pentaho.com/pba/pentaho-interactive-reports-cp/add-logos-to-interactive-reports/multi-tenancy-support-for-adding-logos.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-interactive-reports-cp/add-logos-to-interactive-reports/multi-tenancy-support-for-adding-logos.md

# Multi-tenancy support for adding logos

When there are different tenants on the same server, you can add different logos for each one. The attribute `tenantId` is stored in the session.

The default `tenantId` is `/pentaho/tenant0`. The **Change Me!** logo image is stored in `/pentaho-server/pentaho-solutions/system/pentaho-interactive-reporting/resources/images/pentaho/tenant0` with the name`Logo.png`. When you have multiple tenants, each tenant is represented by a folder with a unique tenantId in place of "tenant0". Each tenant folder must contain the logo of the respective tenant named `Logo.png`.
