# Source: https://docs.xano.com/xanoscript/function-reference/security.md

# Source: https://docs.xano.com/xanoscript/filter-reference/security.md

# Source: https://docs.xano.com/the-function-stack/functions/security.md

# Source: https://docs.xano.com/the-function-stack/filters/security.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Security

* [**create\_uid**](/the-function-stack/filters/security#create_uid) - Returns a unique 64bit unsigned int value seeded off the value.
* [**decrypt**](/the-function-stack/filters/security#decrypt) - Decrypts the value and returns the result.
* [**encrypt**](/the-function-stack/filters/security#encrypt) - Encrypts the value and returns the result.
* [**hmac\_md5**](/the-function-stack/filters/security#hmac_md5) - Returns a MD5 signature representation of the value using a shared secret via the HMAC method
* [**hmac\_sha1**](/the-function-stack/filters/security#hmac_sha1) - Returns a SHA1 signature representation of the value using a shared secret via the HMAC method
* [**hmac\_sha256**](/the-function-stack/filters/security#hmac_sha256-hmac384-hmac512)[\*\* / hmac\_sha384 / hmac\_sha512\*\*](/the-function-stack/filters/security#hmac_sha256-hmac384-hmac512) - Returns a SHA256/384/512 signature representation of the value using a shared secret via the HMAC method
* [**jwe\_decode**](/the-function-stack/filters/security#jwe_encode-jwe_decode) - Decodes the value represented as JWE token and returns the original payload.
* [**jwe\_encode**](/the-function-stack/filters/security#jwe_encode-jwe_decode) - Encodes the value and returns the result as a JWE token.
* [**md5**](/the-function-stack/filters/security#md5) - Returns an MD5 signature representation of the value.
* [**secureid\_decode**](/the-function-stack/filters/security#secureid_decode) - Returns the id of the original encode.
* [**secureid\_encode**](/the-function-stack/filters/security#secureid_encode) - Returns an encrypted version of the id.
* [**sha1**](/the-function-stack/filters/security#sha1-sha256-sha384-sha512) - Returns a SHA1 signature representation of the value.
* [**sha256 / sha384 / sha512**](/the-function-stack/filters/security#sha1-sha256-sha384-sha512) - Returns a SHA256/384/512 signature representation of the value.

#### create\_uid:

Returns a unique 64bit unsigned int value seeded off the value.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/5b122d87-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=df0c055427b5ff73562eae5fb32dd417" width="1101" height="356" data-path="images/5b122d87-image.jpeg" />
</Frame>

#### decrypt:

Decrypts the value and returns the result.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c3bae617-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=4247a96f6b4a1255f5b1be26eade4249" width="443" height="756" data-path="images/c3bae617-image.jpeg" />
</Frame>

#### encrypt:

Encrypts the value and returns the result in raw binary form. Find more details on the encrypt function page.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f1de3f85-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=17fd824140993431ad178da4811e1c75" width="444" height="853" data-path="images/f1de3f85-image.jpeg" />
</Frame>

#### hmac\_md5

Returns a MD5 signature representation of the value using a shared secret via the HMAC method. The secret key is a unique piece of information that is used to compute the HMAC and is known both by the sender and the receiver of the message. This key will vary in length depending on the algorithm that you use.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/1962aaec-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=a14a421de32913c02ab830fd1cba519b" width="546" height="438" data-path="images/1962aaec-image.jpeg" />
</Frame>

#### hmac\_sha1

Returns a SHA1 signature representation of the value using a shared secret via the HMAC method. The secret key is a unique piece of information that is used to compute the HMAC and is known both by the sender and the receiver of the message. This key will vary in length depending on the algorithm that you use.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/WBQXG-4Ngk82eYAW/images/ffc38e97-image.jpeg?fit=max&auto=format&n=WBQXG-4Ngk82eYAW&q=85&s=85528e01af9bf3973d82ee3c3b29aa90" width="530" height="441" data-path="images/ffc38e97-image.jpeg" />
</Frame>

#### hmac\_sha256 / hmac384 / hmac512

Returns a SHA256/384/512 signature representation of the value using a shared secret via the HMAC method. The secret key is a unique piece of information that is used to compute the HMAC and is known both by the sender and the receiver of the message. This key will vary in length depending on the algorithm that you use.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/2b758d35-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=5565a32cf4a47257b330b805bae4d222" width="537" height="458" data-path="images/2b758d35-image.jpeg" />
</Frame>

#### jwe\_encode / jwe\_decode:

Encodes the value and returns the result as a JWE token.

HEADERS: Any custom headers to include in the JWE token Sample: `{"kid": "12345"}`

KEY: The encryption key for the JWE token Sample: `a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6`

KEY\_ALGORITHM: Choose one of the algorithms used to encode the token.

CONTENT\_ALGORITHM: Choose one of the algorithms used to encode the token.

TTL: Token expiration time in seconds Sample: `3600` (1 hour), `0` means no expiration

#### md5

Returns an MD5 signature representation of the value. A salt value can be added to the text to provide an extra layer of security.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/3ff3270c-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=5252bc8ac639a96445ac32e4d7877fb1" width="1075" height="211" data-path="images/3ff3270c-image.jpeg" />
</Frame>

#### secureid\_decode

Returns the id of the original encode. If a salt was added to encode this value the same salt needs to be added to decrypt it.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/147478a4-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=1df6d039880734fef818db3749a1ee65" width="1079" height="217" data-path="images/147478a4-image.jpeg" />
</Frame>

#### secureid\_encode

Returns an encrypted version of an integer. A salt value can be added to the text to provide an extra layer of security.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/59a77172-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=aca6bd10c0bd20715cbac467cc26b9b3" width="1081" height="214" data-path="images/59a77172-image.jpeg" />
</Frame>

#### sha1 / sha256 / sha384 / sha512

Returns a SHA1 signature representation of the value. A salt value can be added to the text to provide an extra layer of security.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f1ce9336-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=96332a16b19518ee4f5d37278f5c9ffa" width="528" height="203" data-path="images/f1ce9336-image.jpeg" />
</Frame>


Built with [Mintlify](https://mintlify.com).