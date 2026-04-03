:github_url: hide



# TLSOptions

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

TLS configuration for clients and servers.


## Description

TLSOptions abstracts the configuration options for the [StreamPeerTLS<class_StreamPeerTLS>] and [PacketPeerDTLS<class_PacketPeerDTLS>] classes.

Objects of this class cannot be instantiated directly, and one of the static methods [client()<class_TLSOptions_method_client>], [client_unsafe()<class_TLSOptions_method_client_unsafe>], or [server()<class_TLSOptions_method_server>] should be used instead.


> **TABS**
>

    # Create a TLS client configuration which uses our custom trusted CA chain.
    var client_trusted_cas = load("res://my_trusted_cas.crt")
    var client_tls_options = TLSOptions.client(client_trusted_cas)

    # Create a TLS server configuration.
    var server_certs = load("res://my_server_cas.crt")
    var server_key = load("res://my_server_key.key")
    var server_tls_options = TLSOptions.server(server_key, server_certs)




## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TLSOptions<class_TLSOptions>`           | :ref:`client<class_TLSOptions_method_client>`\ (\ trusted_chain\: :ref:`X509Certificate<class_X509Certificate>` = null, common_name_override\: :ref:`String<class_String>` = ""\ ) |static| |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TLSOptions<class_TLSOptions>`           | :ref:`client_unsafe<class_TLSOptions_method_client_unsafe>`\ (\ trusted_chain\: :ref:`X509Certificate<class_X509Certificate>` = null\ ) |static|                                            |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                   | :ref:`get_common_name_override<class_TLSOptions_method_get_common_name_override>`\ (\ ) |const|                                                                                             |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`X509Certificate<class_X509Certificate>` | :ref:`get_own_certificate<class_TLSOptions_method_get_own_certificate>`\ (\ ) |const|                                                                                                       |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`CryptoKey<class_CryptoKey>`             | :ref:`get_private_key<class_TLSOptions_method_get_private_key>`\ (\ ) |const|                                                                                                               |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`X509Certificate<class_X509Certificate>` | :ref:`get_trusted_ca_chain<class_TLSOptions_method_get_trusted_ca_chain>`\ (\ ) |const|                                                                                                     |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                       | :ref:`is_server<class_TLSOptions_method_is_server>`\ (\ ) |const|                                                                                                                           |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                       | :ref:`is_unsafe_client<class_TLSOptions_method_is_unsafe_client>`\ (\ ) |const|                                                                                                             |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TLSOptions<class_TLSOptions>`           | :ref:`server<class_TLSOptions_method_server>`\ (\ key\: :ref:`CryptoKey<class_CryptoKey>`, certificate\: :ref:`X509Certificate<class_X509Certificate>`\ ) |static|                          |
> +-----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[TLSOptions<class_TLSOptions>] **client**\ (\ trusted_chain\: [X509Certificate<class_X509Certificate>] = null, common_name_override\: [String<class_String>] = ""\ ) |static| [🔗<class_TLSOptions_method_client>]

Creates a TLS client configuration which validates certificates and their common names (fully qualified domain names).

You can specify a custom `trusted_chain` of certification authorities (the default CA list will be used if `null`), and optionally provide a `common_name_override` if you expect the certificate to have a common name other than the server FQDN.

\ **Note:** On the Web platform, TLS verification is always enforced against the CA list of the web browser. This is considered a security feature.


----



[TLSOptions<class_TLSOptions>] **client_unsafe**\ (\ trusted_chain\: [X509Certificate<class_X509Certificate>] = null\ ) |static| [🔗<class_TLSOptions_method_client_unsafe>]

Creates an **unsafe** TLS client configuration where certificate validation is optional. You can optionally provide a valid `trusted_chain`, but the common name of the certificates will never be checked. Using this configuration for purposes other than testing **is not recommended**.

\ **Note:** On the Web platform, TLS verification is always enforced against the CA list of the web browser. This is considered a security feature.


----



[String<class_String>] **get_common_name_override**\ (\ ) |const| [🔗<class_TLSOptions_method_get_common_name_override>]

Returns the common name (domain name) override specified when creating with [client()<class_TLSOptions_method_client>].


----



[X509Certificate<class_X509Certificate>] **get_own_certificate**\ (\ ) |const| [🔗<class_TLSOptions_method_get_own_certificate>]

Returns the [X509Certificate<class_X509Certificate>] specified when creating with [server()<class_TLSOptions_method_server>].


----



[CryptoKey<class_CryptoKey>] **get_private_key**\ (\ ) |const| [🔗<class_TLSOptions_method_get_private_key>]

Returns the [CryptoKey<class_CryptoKey>] specified when creating with [server()<class_TLSOptions_method_server>].


----



[X509Certificate<class_X509Certificate>] **get_trusted_ca_chain**\ (\ ) |const| [🔗<class_TLSOptions_method_get_trusted_ca_chain>]

Returns the CA [X509Certificate<class_X509Certificate>] chain specified when creating with [client()<class_TLSOptions_method_client>] or [client_unsafe()<class_TLSOptions_method_client_unsafe>].


----



[bool<class_bool>] **is_server**\ (\ ) |const| [🔗<class_TLSOptions_method_is_server>]

Returns `true` if created with [server()<class_TLSOptions_method_server>], `false` otherwise.


----



[bool<class_bool>] **is_unsafe_client**\ (\ ) |const| [🔗<class_TLSOptions_method_is_unsafe_client>]

Returns `true` if created with [client_unsafe()<class_TLSOptions_method_client_unsafe>], `false` otherwise.


----



[TLSOptions<class_TLSOptions>] **server**\ (\ key\: [CryptoKey<class_CryptoKey>], certificate\: [X509Certificate<class_X509Certificate>]\ ) |static| [🔗<class_TLSOptions_method_server>]

Creates a TLS server configuration using the provided `key` and `certificate`.

\ **Note:** The `certificate` should include the full certificate chain up to the signing CA (certificates file can be concatenated using a general purpose text editor).

