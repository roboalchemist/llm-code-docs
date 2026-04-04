:github_url: hide



# CryptoKey

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A cryptographic key (RSA or elliptic-curve).


## Description

The CryptoKey class represents a cryptographic key. Keys can be loaded and saved like any other [Resource<class_Resource>].

They can be used to generate a self-signed [X509Certificate<class_X509Certificate>] via [Crypto.generate_self_signed_certificate()<class_Crypto_method_generate_self_signed_certificate>] and as private key in [StreamPeerTLS.accept_stream()<class_StreamPeerTLS_method_accept_stream>] along with the appropriate certificate.


## Tutorials

- [../tutorials/networking/ssl_certificates](SSL certificates .md)


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`               | :ref:`is_public_only<class_CryptoKey_method_is_public_only>`\ (\ ) |const|                                                                                      |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`load<class_CryptoKey_method_load>`\ (\ path\: :ref:`String<class_String>`, public_only\: :ref:`bool<class_bool>` = false\ )                               |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`load_from_string<class_CryptoKey_method_load_from_string>`\ (\ string_key\: :ref:`String<class_String>`, public_only\: :ref:`bool<class_bool>` = false\ ) |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`save<class_CryptoKey_method_save>`\ (\ path\: :ref:`String<class_String>`, public_only\: :ref:`bool<class_bool>` = false\ )                               |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`           | :ref:`save_to_string<class_CryptoKey_method_save_to_string>`\ (\ public_only\: :ref:`bool<class_bool>` = false\ )                                               |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[bool<class_bool>] **is_public_only**\ (\ ) |const| [🔗<class_CryptoKey_method_is_public_only>]

Returns `true` if this CryptoKey only has the public part, and not the private one.


----



[Error<enum_@GlobalScope_Error>] **load**\ (\ path\: [String<class_String>], public_only\: [bool<class_bool>] = false\ ) [🔗<class_CryptoKey_method_load>]

Loads a key from `path`. If `public_only` is `true`, only the public key will be loaded.

\ **Note:** `path` should be a "\*.pub" file if `public_only` is `true`, a "\*.key" file otherwise.


----



[Error<enum_@GlobalScope_Error>] **load_from_string**\ (\ string_key\: [String<class_String>], public_only\: [bool<class_bool>] = false\ ) [🔗<class_CryptoKey_method_load_from_string>]

Loads a key from the given `string_key`. If `public_only` is `true`, only the public key will be loaded.


----



[Error<enum_@GlobalScope_Error>] **save**\ (\ path\: [String<class_String>], public_only\: [bool<class_bool>] = false\ ) [🔗<class_CryptoKey_method_save>]

Saves a key to the given `path`. If `public_only` is `true`, only the public key will be saved.

\ **Note:** `path` should be a "\*.pub" file if `public_only` is `true`, a "\*.key" file otherwise.


----



[String<class_String>] **save_to_string**\ (\ public_only\: [bool<class_bool>] = false\ ) [🔗<class_CryptoKey_method_save_to_string>]

Returns a string containing the key in PEM format. If `public_only` is `true`, only the public key will be included.

