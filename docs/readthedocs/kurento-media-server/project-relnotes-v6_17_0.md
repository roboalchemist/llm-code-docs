# 6.17.0 (March 2022)

This is a very small release, made to incorporate the ability to inherit new modules from *RtpEndpoint*.

To install Kurento Media Server: Installation Guide.

## Changed

### Inheritable RtpEndpoint

The Kurento *RtpEndpoint* classes were *final*, meaning that it was not possible to inherit from them in order to create new, specialized versions of the endpoint. This was a problem for the fellow contributors at Naeva Tec [https://www.naevatec.com/], who were trying to write SipRtpEndpoint [https://github.com/naevatec/kms-siprtpendpoint], a new endpoint that contains specific behaviors to make it work well with SIP communications.

This limitation got solved in this release. With the reorganization of several classes and introduction of a new internal library for the *RtpEndpoint*, it can now be inherited to create new classes based on it.

Thanks to @slabajo [https://github.com/slabajo] (Saúl Labajo) for Kurento/kms-elements#32 [https://github.com/Kurento/kms-elements/pull/32] (*prepare for siprtp_module*) and Kurento/kms-elements#33 [https://github.com/Kurento/kms-elements/pull/33] (*RtpEndpoint library*).

## Other changes

This list includes other changes and fixes contributed by users and/or fellow developers, who merit our sincere appreciation and thanks for sharing their work with the Kurento project:

- 

@pabs3 [https://github.com/pabs3] (Paul Wise) for Kurento/kurento-module-creator#3 [https://github.com/Kurento/kurento-module-creator/pull/3] (*Add KurentoModuleCreatorConfig with path to FindKurentoModuleCreator*).