# Passwords

In Java based applications, passing passwords as `String` objects has the
disadvantage [https://stackoverflow.com/a/8881376/11150851] that you have to rely on garbage collection to clean up
once they are no longer used.
For that reason, `char[]` is the preferred method for dealing with passwords.
Once a password is no longer used, the character array can simply be overwritten to remove the sensitive data from
memory.

## Passphrase

PGPainless uses a wrapper class `Passphrase`, which takes care for the wiping of unused passwords:

```
Passphrase passphrase = new Passphrase(new char[] {'h', 'e', 'l', 'l', 'o'});
assertTrue(passphrase.isValid());

assertArrayEquals(new char[] {'h', 'e', 'l', 'l', 'o'}, passphrase.getChars()):

// Once we are done, we can clean the data
passphrase.clear();

assertFalse(passphrase.isValid());
assertNull(passphrase.getChars());

```