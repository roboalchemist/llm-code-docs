# Source: https://ebean.io/docs/features/encryption

Title: Encryption | Ebean

URL Source: https://ebean.io/docs/features/encryption

Markdown Content:
Ebean has support for transparent Encryption/Decryption of specific properties. We make mark the properties we want encrypted with `@Encrypted` and these properties will be automatically encrypted and decrypted as needed.

Encryption/decryption can occur either on the client/application side or by the database. When we use database encryption then we can use these properties in queries as part of the `where` and `order by` clause. Effectively the encryption of the property is fully transparent to the application.

When we use client/application side encryption/decryption then we should only use the **EQ** (equal to) operator in the `where` clause.

Client/Application encryption
-----------------------------

When using client/application encryption the properties are encrypted/decrypted by a Java function - an implementation of the `io.ebean.config.Encryptor` interface. The default implementation uses AES 128 bit based implementation and we can also configure Ebean to use another implementation.

Properties encrypted with client/application encryption should **ONLY** be used with **EQ (equal to)** operator in `where` clauses - other operators should not be used with client side encrypted properties.

package io.ebean.config;

/**
 * Used for Java side encryption of properties when DB encryption is not used.
 *
 * By default this is used on non-varchar types such as Blobs.
 */
public interface Encryptor {

  /**
 * Encrypt the data using the key.
 */
  byte[] encrypt(byte[] data, EncryptKey key);

  /**
 * Decrypt the data using the key.
 */
  byte[] decrypt(byte[] data, EncryptKey key);

  /**
 * Encrypt the formatted string value using a key.
 */
  byte[] encryptString(String formattedValue, EncryptKey key);

  /**
 * Decrypt the data returning a formatted string value using a key.
 */
  String decryptString(byte[] data, EncryptKey key);

}

Database encryption
-------------------

When using Database side encryption/decryption we use database stored procedures to encrypt and decrypt the properties. For example with Postgres Ebean uses `pgp_sym_encrypt()` and `pgp_sym_decrypt()`.

#### Database encryption functions

The default DB encryption decryption functions used for each platform are:

*   **Postgres, YugabyteDB** - pgp_sym_decrypt(), pgp_sym_encrypt()
*   **MySql, MariaDB** - aes_encrypt(), aes_decrypt()
*   **SQL Server** - DecryptByPassPhrase(), EncryptByPassPhrase()
*   **Oracle** - requires dbms_crypto and uses custom functions for encryption and decryption
*   **H2** - encrypt() and decrypt() with 'AES' option

Supported types
---------------

The following are the types supported by database encryption. Any type not supported by database encryption will use client/application encryption.

*   Enum (if based on VARCHAR)
*   String (VARCHAR, CHAR, CLOB, LONGVARCHAR)
*   Date types - LocalDate, Date, Joda LocalDate
*   Timestamp types - Timestamp, Instant, OffsetDateTime, ZonedDateTime

Important: The following types are currently not supported:

*   primitive types
*   Timestamps

EncryptKeyManager
-----------------

Whenever a property is encrypted or decrypted a "Key" must be used. Ebean will internally ask the EncryptKeyManager for a key given the table and column name.

We must supply an implementation of the EncryptKeyManager.

package io.ebean.config;

/**
 * Determine keys used for encryption and decryption.
 */
@FunctionalInterface
public interface EncryptKeyManager {

  /**
 * Initialise the EncryptKeyManager.
 *
 * This gives the EncryptKeyManager the opportunity to get keys etc.
 */
  default void initialise() {}

  /**
 * Return the key used to encrypt and decrypt a property mapping to the given
 * table and column.
 */
  EncryptKey getEncryptKey(String tableName, String columnName);
}

@Encrypted
----------

Mark a property to be encrypted with the `@Encrypted` annotation. By default the property will be `dbEncryption = true` and we explicitly set that false for client/application side encryption.

// use database side encryption
@Encrypted
String name;

// use client side encryption (not db functions)
@Encrypted(dbEncryption=false)
String description;

#### Example

// Use @Encrypted annotation to mark the encrypted properties

@Entity
@Table(name="patient")
public class Patient {

  @Id
  long id;

  // database side encryption
  @Encrypted
  String name;

  // client side encryption
  @Lob
  @Encrypted(dbEncryption=false)
  String description;

  @Encrypted
  LocalDate dob;
  ...

Limitations
-----------

*    Properties using Java client encryption should only use **EQ** (equal to) operator in WHERE clauses 
*    DB Encryption support built in for H2, Postgres, YugabyteDB, MySql, MariaDB, Sql Server and Oracle. 
*    We can not use Encryption with positioned (1,2,3...) parameters. We must use named parameters or the criteria api to define queries. 

### Examples:

List<Patient> list =
  new QPatient()
    .name.eq("Rob")
    .findList();

Results in the following Postgres SQL:

select t0.id, pgp_sym_decrypt(t0.name,?)
from patient t0
where pgp_sym_decrypt(t0.name,?) = ?

Configuration
-------------

Specify the EncryptKeyManager implementation in the ebean.properties file like below:

ebean.encryptKeyManager=org.example.BasicEncyptKeyManager

Programmatically configure using DatabaseConfig.

DatabaseConfig config = DatabaseConfig();
...
EncryptKeyManager keyManager = ...;
config.setEncryptKeyManager(keyManager);
...
Database database = DatabaseFactory.create(config);

An example EncryptKeyManager is:

package org.example.encrypt;

import io.ebean.config.EncryptKey;
import io.ebean.config.EncryptKeyManager;

public class BasicEncyptKeyManager implements EncryptKeyManager {

  public void initialise() {
    // can load keys or initialise source resources ...
  }

  public EncryptKey getEncryptKey(String tableName, String columnName) {
    // get the key for the given table and column
    String keyValue = ...;
    return new BasicEncryptKey(keyValue);
  }

}

Internals
---------

Ebean detects when an encrypted property is being used. It will call the EncryptKeyManager with the table and column of the property to get the encryption key. This key is then added as a bind variable to the prepared statement.

As the key is added as a bind variable into the statement we cannot use encryption with 'positioned' parameters because it can effectively change the position of other parameters. We can use named parameters or the criteria api for building queries but, we can't use positioned (1,2,3,4..) parameters.
