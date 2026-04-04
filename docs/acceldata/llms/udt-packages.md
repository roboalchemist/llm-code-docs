# Source: https://docs.acceldata.io/api/udt-packages.md

# UDT Packages

UDT Packages combine multiple UDTs/UDFs into reusable bundles.
 They are typically used for:

- Versioned rule libraries
- Cross-team distribution of templates
- CI/CD-based template deployment

## Available Endpoints

| Action | Endpoint | 
| ---- | ---- | 
| Create Package | `POST /catalog-server/api/udt-packages` | 
| List Packages | `GET /catalog-server/api/udt-packages` | 
| Get Package | `GET /catalog-server/api/udt-packages/:id` | 
| Update Package | `PUT /catalog-server/api/udt-packages/:id` | 
| Delete Package | `DELETE /catalog-server/api/udt-packages/:id` | 
