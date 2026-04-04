# Source: https://render.com/docs/hipaa-best-practices.md

# Building HIPAA-Compliant Apps on Render — Follow best practices to help keep PHI secure.


> *[HIPAA-enabled workspaces](hipaa-compliance) require an Organization or Enterprise plan.*
>
> Interested in [Enterprise capabilities](enterprise-orgs)? Reach out:

Healthcare applications that handle US Protected Health Information (PHI) must adhere to strict HIPAA compliance requirements to ensure patient data security and privacy.

This guide outlines best practices for developing HIPAA-compliant applications, covering both infrastructure-level security measures provided by Render and application-level implementations that you'll need to consider.

We'll explore key aspects of HIPAA compliance, including user access controls, emergency access procedures, PHI access logging, and data encryption.

## Example app

This guide includes examples and code snippets that demonstrate how to implement HIPAA Security Rule requirements in your healthcare applications.

To view a more complete example implementation, see the `patient-api` project repo:

## HIPAA Security Rule application checklist

With a [HIPAA-enabled workspace](hipaa-compliance), here's a summary of what Render handles for you and what you'll need to implement at the app layer:

------

###### *Access Controls*

---

###### HIPAA Control

Unique user identification

###### Specification type

Required

###### Render

Render provides infra-level access controls to platform components.

###### Customer

App must implement secure app authentication and unique user identifiers, such as `userId` or email addresses.

---

###### HIPAA Control

[Emergency access procedure](#emergency-access-procedure)

###### Specification type

Required

###### Render

Databases feature point-in-time backups with checksums, stored across multiple availability zones for redunancy.

###### Customer

App should have access roles that allow for emergency access to data.

---

###### HIPAA Control

[Automatic logoff](#automatic-logoff)

###### Specification type

Addressable

###### Render

N/A

###### Customer

Authorization at the application level may set the JWT or session expiry time to allow for automatic logoff for the user.

---

###### HIPAA Control

[Encryption and decryption](#encryption-and-decryption)

###### Specification type

Addressable

###### Render

Render provides minimum AES-128 encryption at rest for database systems and OCI images.

###### Customer

App may implement application level encryption and data tokenization (such as tokenizing SSN before database writes).

---

###### *Audit Controls*

---

###### HIPAA Control

[Audit controls](#phi-access-logging)

###### Specification type

Required

###### Render

Render provides audit logging and monitoring for platform components. For system logs, Render offers OpenTelemetry-compatible logging.

###### Customer

App should [log when PHI is accessed](#phi-access-logging) and by which user.

---

###### *Integrity*

---

###### HIPAA Control

Mechanism to authenticate ePHI

###### Specification type

Addressable

###### Render

All database backups implement checksum to ensure date integrity.

###### Customer

App may implement versioning or data checksum when loading data into the database.

---

###### *Person or Entity Authentication*

---

###### HIPAA Control

[Person or entity authentication](#user-access-controls-person-or-entity-authentication)

###### Specification type

Required

###### Render

All services and resources hosted on Render are regulated with role-based access control.

###### Customer

App should implement industry standard authentication (such as JSON Web Tokens (JWT)) for any data access function.

---

###### *Transmission Security*

---

###### HIPAA Control

Integrity controls

###### Specification type

Addressable

###### Render

Private networking between services. Every host runs IDS (intrusion detection system) to detect unauthorized access attempts in real time

###### Customer

N/A

---

###### HIPAA Control

[Encryption](#encryption-and-decryption)

###### Specification type

Addressable

###### Render

HTTPS/TLS 1.2+ encryption for all traffic

###### Customer

Customer should ensure that all API endpoints that deal with PHI are authentication protected.

------

For more details on the HIPAA Security Rule, we recommend the [HIPAA security series](https://www.hhs.gov/sites/default/files/ocr/privacy/hipaa/administrative/securityrule/techsafeguards.pdf) published by HHS.

## User access controls & person or entity authentication

HIPAA Security Rule requires that users have unique identification and that data access is restricted to the right users.

Render handles access control at the infrastructure level with role-based access (RBAC) to platform components, but it's also necessary to restrict access on the service level.

In addition to user authentication (which is usually done with either session-based or JWT-based authentication), role-based data access (authorization) is also recommended.

This can be does with simple role check as in the example below. After authenticating the user, we can check if the role permission is sufficient to access the resource.

```javascript
const user = await getUser(req)

if (user.role !== 'ADMIN' && user.role !== 'BILLING') {
  logger.warn('User is not authorized to access this resource', {
    userId: user.id,
    userRole: user.role,
  })
  throw new AuthorizationError('User is not authorized to access this resource')
}
```

In our [example app](#example-app), an `ADMIN` or `BILLING` user can access all patient records, but a `PROVIDER` user cannot.

This example illustrates a simple way to implement role based access, but in a production system, we recommend a more robust implementation. Options range from hosted solutions like [Permit.io](https://www.permit.io/), or library solutions like [Auth.js.](https://authjs.dev/)

### Automatic logoff

Automatically terminating user sessions after a set time can be easily done by adjusting the expiration of a JWT token. Review the configuration of your auth provider and set the expiration accordingly. The expiration length is a balance between security (shorter expiration) and better user experience (longer expiration).

The HIPAA Security Rule does not define a specific expiration requirement, so this configuration can be tuned to your specific use case.

### Emergency access procedure

In addition to user access controls, HIPAA requires "procedures for obtaining necessary
electronic protected health information during an emergency."

In our [example app](#example-app), we satisfy this requirement with the addition of the `ADMIN` role, which can access all patient records:

```javascript
const user = await getUser(req)

// check if user is admin
if (user.role !== 'ADMIN') {
  logger.warn('User is not authorized to access this resource', {
    userId: user.id,
    userRole: user.role,
  })
  throw new AuthorizationError('User is not authorized to access this resource')
}

const patients = await patientService.getAllPatients()
```

## PHI access logging

Render provides built-in audit logging and monitoring for platform events, as well as intrusion detection (IDS) to detect unauthorized access and facilitate authorized access audits.

To satisfy HIPAA requirements around ePHI, add application-level logs that record who is accessing what records. For reference, the HIPAA Security Rule states:

> Implement hardware, software, and/or procedural mechanisms that record and examine activity in information systems that contain or use electronic protected health information.

In our [example app](#example-app), we log the `userId` and `role` of every record access request, as well as the `patientId`. In the event of a suspected data breach, this monitoring could be used to analyze the affected data.

[image: Reviewing PHI access logs in the Render Log Explorer]

> *Do not include PHI in logs!* Only log internal IDs and operational data.

## Encryption and decryption

Regarding data security, the HIPAA Security Rule states:

> Implement technical security measures to guard against unauthorized access to electronic protected health information that is being transmitted over an electronic communications network.

### Render-provided infrastructure safeguards

Render provides TLS 1.2+ encryption for all traffic, plus private networking between services, as well as minimum AES-128 encryption for databases, backups, and secrets.

### Implementing zero-trust security in your app

We recommend implementing additional data security mechanisms on the app level to produce a "zero-trust" system, where a breach of one component does not allow full access to sensitive data.

The [example app](#example-app) includes an encryption function that encrypts the patient's SSN before inserting into the database and decrypts it only upon retrieval.

This means that even if an unauthorized user gains access to the database or the app, they still wouldn't be able to access the encrypted data. You can find the full implementation in the example app repo.

```typescript
// Methods of class PatientService

public async createPatient(patientData: Omit<Patient, 'id'>): Promise<Patient> {

  // Encrypt sensitive data before inserting into the database.
  const patientEncrypted = this.encryptSSN(patientData)

  return this.prisma.patient.create({
    data: patientEncrypted
  });
}

public async getPatientById(id: number): Promise<Patient> {
  const patient: Patient | null = await this.prisma.patient.findFirst({
    where: { id },
  });

  if (!patient) {
    throw new NotFoundError(`Patient with id ${id} not found`);
  }

  // Decrypt data after database retrieval
  const patientDecrypted = this.decryptSSN(patient, patient.ivKey)

  if (!patientDecrypted) {
    throw new NotFoundError(`Patient with id ${id} not found`);
  }

  return patientDecrypted;
}
```

> *As with the previous examples, these are simple methods to showcase how these safeguards could be implemented.*
>
> Production systems will benefit from more robust solutions.

## Wrapping up

Building HIPAA-compliant applications requires careful attention to security measures at both the infrastructure and application levels. While Render provides robust infrastructure-level security features, you must implement appropriate application-level controls to ensure HIPAA compliance.

By following the best practices outlined in this guide, implementing proper user access controls, maintaining detailed access logs, and utilizing encryption for sensitive data, you can build secure healthcare applications that protect patient information.

Remember that these examples serve as starting points, and production systems should employ more robust implementations based on specific security requirements and threat models. Regular security audits will help maintain the integrity and compliance of your healthcare applications.

For assistance migrating your HIPAA-compliant application to Render, please reach out:

