Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Interface MaskingKeyGenerator

---

@Beta
public interface MaskingKeyGenerator
Can be implemented to generate masking keys.

 The implementation must be thread safe.

 Tyrus by default uses the following implementation:

```

     new MaskingKeyGenerator() {

          private final SecureRandom secureRandom = new SecureRandom();

          public int nextInt() {
              return secureRandom.nextInt();
          }
      };
 
```

Author:
Petr Janouch

-

## Method Summary

Modifier and Type
Method
Description
`int`
`nextInt()`

Return next random int similarly to `Random.nextInt()`.

-

## Method Details

-

### nextInt

int nextInt()
Return next random int similarly to `Random.nextInt()`.

Returns:
next random value.
