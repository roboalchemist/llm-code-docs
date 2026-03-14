# Source: https://virustotal.readme.io/reference/ip-object.md

# IP addresses

IPv4 and IPv6 addresses are other of the network locations that VirusTotal stores information about. A description of the fields stored within these objects follows.

IP addresses are, as domains, network locations related to File and URLs objects in many ways. That is why it is possible to retrieve them by its relationship with other objects, by other means when searching in VT Enterprise services, or just by searching an already existing IP.

## Object Attributes

A IP address object contains the following attributes:

* `as_owner`: <*string*> owner of the Autonomous System to which the IP belongs.
* `asn`: <*integer*> autonomous System Number to which the IP belongs.
* `continent`: <*string*> continent where the IP is placed (ISO-3166 continent code).
* `country`: <*string*> country where the IP is placed (ISO-3166 country code).
* `jarm`: <*string*> IP address' [JARM hash](https://engineering.salesforce.com/easily-identify-malicious-servers-on-the-internet-with-jarm-e095edac525a).
* `last_analysis_date`: <*integer*> UTC timestamp representing last time the IP was scanned.
* `last_analysis_results`: <*dictionary*> result from URL scanners. dict with scanner name as key and a dict with notes/result from that scanner as value.
  * `category`: <*string*> normalized result. can be:
    * "harmless" (site is not malicious),
    * "undetected" (scanner has no opinion about this site),
    * "suspicious" (scanner thinks the site is suspicious),
    * "malicious" (scanner thinks the site is malicious).
  * `engine_name`: <*string*> complete name of the URL scanning service.
  * `method`: <*string*> type of service given by that URL scanning service (i.e. "blacklist").
  * `result`: <*string*> raw value returned by the URL scanner ("clean", "malicious", "suspicious", "phishing"). It may vary from scanner to scanner, hence the need for the "category" field for normalisation.
* `last_analysis_stats`: <*dictionary*> number of different results from this scans.
  * `harmless`: <*integer*> number of reports saying that is harmless.
  * `malicious`: <*integer*> number of reports saying that is malicious.
  * `suspicious`: <*integer*> number of reports saying that is suspicious.
  * `timeout`: <*integer*> number of timeouts when checking this URL.
  * `undetected`: <*integer*> number of reports saying that is undetected.
* `last_https_certificate`: <\_[SSL Certificate](#ssl-certificate) \_> SSL Certificate object certificate information for that IP.
* `last_https_certificate_date`: <*integer*> date when the certificate shown in `last_https_certificate` was retrieved by VirusTotal. UTC timestamp.
* `last_modification_date`: <*integer*> date when any of the IP's information was last updated. UTC timestamp.
* `network`: <*string*> IP network range to which the IP belongs.
* `regional_internet_registry`: <*string*> RIR (one of the current RIRs: AFRINIC, ARIN, APNIC, LACNIC or RIPE NCC).
* `reputation`: <*integer*> IP's score calculated from the votes of the VirusTotal's community.
* `tags`: <*list of strings*> identificative attributes.
* `total_votes`: <*dictionary*> unweighted number of total votes from the community, divided in "harmless" and "malicious".
  * `harmless`: <*integer*> number of positive votes.
  * `malicious`: <*integer*> number of negative votes.
* `whois`: <*string*> whois information as returned from the pertinent whois server.
* `whois_date`: <*integer*> date of the last update of the whois record in VirusTotal. UTC timestamp.

> 📘 About reputation
>
> The reputation for a given domain is determined by VirusTotal's Community (registered users). Users sometimes vote on domains, these users in turn have a reputation themselves: the *community score* condenses the votes performed on a given item weighted by the reputation of the users that casted these votes. Negative (red) scores indicate maliciousness, whereas positive (green) scores reflect harmlessness. The higher the absolute number, the more that you may trust a given score. You can read more about this at this [community article](https://virustotal.readme.io/docs/community).

```json "ip_address" object
{
  "data": {
    "attributes": {
      "as_owner": "<string>",
      "asn": <int>,
      "continent": "<string>",
      "country": "<string>",
      "jarm": "<string>",
      "last_analysis_date": <int:timestamp>,
      "last_analysis_results": {
        "<engine name:string>": {
          "category": "<string>",
          "engine_name": "<string>",
          "method": "<string>",
          "result": "<string>"
        }
      },
      "last_analysis_stats": {
        "harmless": <int>,
        "malicious": <int>,
        "suspicious": <int>,
        "timeout": <int>,
        "undetected": <int>
      },
      "last_modification_date": <int:timestamp>,
      "network": "<ip_range>",
      "regional_internet_registry": "<string>",
      "reputation": <int>,
      "total_votes": {
        "harmless": <int>,
        "malicious": <int>
      },
      "tags": ["<string>"],
      "whois": "<string>",
      "whois_date": <int:timestamp>
    },
    "id": "<ip>",
    "links": {
      "self": "https://www.virustotal.com/api/v3/ip_addresses/<ipv4>"
    },
    "type": "ip_address"
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "as_owner": "Strato AG",
            "asn": 6724,
            "continent": "EU",
            "country": "DE",
            "jarm": "27d40d40d29d40d1dc42d43d00041d4689ee210389f4f6b4b5b1b93f92252d",
            "last_analysis_date": 1671691600,
            "last_analysis_results": {
                "ADMINUSLabs": {
                    "category": "harmless",
                    "engine_name": "ADMINUSLabs",
                    "method": "blacklist",
                    "result": "clean"
                },
                "AegisLab WebGuard": {
                    "category": "harmless",
                    "engine_name": "AegisLab WebGuard",
                    "method": "blacklist",
                    "result": "clean"
                },
                "AlienVault": {
                    "category": "harmless",
                    "engine_name": "AlienVault",
                    "method": "blacklist",
                    "result": "clean"
                },
                "Antiy-AVL": {
                    "category": "harmless",
                    "engine_name": "Antiy-AVL",
                    "method": "blacklist",
                    "result": "clean"
                },
                "AutoShun": {
                    "category": "harmless",
                    "engine_name": "AutoShun",
                    "method": "blacklist",
                    "result": "clean"
                },
            },
            "last_analysis_stats": {
                "harmless": 5,
                "malicious": 0,
                "suspicious": 0,
                "timeout": 0,
                "undetected": 0
            },
            "last_https_certificate": {
                "cert_signature": {
                    "signature": "97ef5af5e6e898ba4ec4b04644954ed60ba16b82e6f9c56967b90b5abc9a559bc3a912af382a1073c4793d75749035597b341efec1073c17bd8b5e03714781c6e9f11b1ce39ecc74afcb8319b9f6f1d9f6c484400bd58374fc0addf7d05f743cdba94a21ebee3d4ea074282a7662eec26171092a69fd60158cd72dd647146de7eb8ae2b5db6257588acc98429eb40f6b393fcbad71139ba11671370d41cbb5f6ca6a18506fccf26d05c3c555377d03946d9e01cdefedbd55c66f34276113885a77babb64ccea9fe16bfac6f2be823bce6d698aed09c3cc02c2c39127d6418c21dbacd723d8f5fa465ce72a8778eee58bf5603a8f42d4afc4c10b0470cef4b244",
                    "signature_algorithm": "sha256RSA"
                },
                "extensions": {
                    "1.3.6.1.4.1.11129.2.4.2": "0481f300f1007700e2694bae26e8e94009e8861bb63b83d43ee7fe7488fba48f",
                    "CA": true,
                    "authority_key_identifier": {
                        "keyid": "a84a6a63047dddbae6d139b7a64565eff3a8eca1"
                    },
                    "ca_information_access": {
                        "CA Issuers": "http://cert.int-x3.letsencrypt.org/",
                        "OCSP": "http://ocsp.int-x3.letsencrypt.org"
                    },
                    "certificate_policies": [
                        "2.23.140.1.2.1",
                        "1.3.6.1.4.1.44947.1.1.1"
                    ],
                    "extended_key_usage": [
                        "serverAuth",
                        "clientAuth"
                    ],
                    "key_usage": [
                        "ff"
                    ],
                    "subject_alternative_name": [
                        "www.ufos-hosting.de"
                    ],
                    "subject_key_identifier": "f522cd9c9a4ccdf5d1ec3f925013bf1185e0bc0c"
                },
                "issuer": {
                    "C": "US",
                    "CN": "Let's Encrypt Authority X3",
                    "O": "Let's Encrypt"
                },
                "public_key": {
                    "algorithm": "RSA",
                    "rsa": {
                        "exponent": "010001",
                        "key_size": 2048,
                        "modulus": "00d1722efe2a2605072f27013b4f9371f1926464dc1c4285f38138a523dc09f0b9ae8578aa70934141bf14893921a2b754a5747a7c71ef9a29501f839a2fe3d052b1434a2fbd0d3149eb1bbe4eef14583791ea7cde3bee2babc5f7114a0fe1ab0c5c5f07701330056b510e020154cca0385a93955684d4d99b74904a44e1ad93f035ebe02bd6e9721285855cbe8f6ce4aaf83ade044b6bc8bd8424ce41f21cf72a1d4ce42ae539fb202efcc791ef810fa49e1c791d4edf4fb83f468cc78b76b5f70333280681f034b80613438f1b0a387e3bdb0dd324e63905d96d1dc810498d5d157d12fc87d4dee9b2abc264b5b6bd7b1e00b838735270e614e15c2c72babb99"
                    }
                },
                "serial_number": "36feb381e87e4ed9b5ee53c76bdaccfabc0",
                "signature_algorithm": "sha256RSA",
                "size": 1379,
                "subject": {
                    "CN": "www.ufos-hosting.de"
                },
                "thumbprint": "b796e1d3210edcf97290e147d1245cfc9a78132c",
                "thumbprint_sha256": "988858e7387a90af438c9d1edad64fa01e0e85666ebf88ae458b1ceb553c5760",
                "validity": {
                    "not_after": "2019-10-10 14:36:27",
                    "not_before": "2019-07-12 14:36:27"
                },
                "version": "V3"
            },
            "last_https_certificate_date": 1566463571,
            "last_modification_date": 1591890478,
            "network": "81.169.128.0/17",
            "regional_internet_registry": "RIPE NCC",
            "reputation": 0,
            "tags": [],
            "total_votes": {
                "harmless": 0,
                "malicious": 0
            },
            "whois": "NetRange: 31.0.0.0 - 31.255.255.255\nCIDR: 31.0.0.0/8\nNetName: 31-RIPE\nNetHandle: NET-31-0-0-0-1\nParent: ()\nNetType: Allocated to RIPE NCC\nOriginAS: \nOrganization: RIPE Network Coordination Centre (RIPE)\nRegDate: \nUpdated: 2009-03-25\nComment: These addresses have been further assigned to users in\nComment: the RIPE NCC region. Contact information can be found in\nComment: the RIPE database at http://www.ripe.net/whois\nRef: https://rdap.arin.net/registry/ip/31.0.0.0\nResourceLink: https://apps.db.ripe.net/search/query.html\nResourceLink: whois.ripe.net\nOrgName: RIPE Network Coordination Centre\nOrgId: RIPE\nAddress: P.O. Box 10096\nCity: Amsterdam\nStateProv: \nPostalCode: 1001EB\nCountry: NL\nRegDate: \nUpdated: 2013-07-29\nRef: https://rdap.arin.net/registry/entity/RIPE\nReferralServer: whois://whois.ripe.net\nResourceLink: https://apps.db.ripe.net/search/query.html\nOrgTechHandle: RNO29-ARIN\nOrgTechName: RIPE NCC Operations\nOrgTechPhone: +31 20 535 4444 \nOrgTechEmail: hostmaster@ripe.net\nOrgTechRef: https://rdap.arin.net/registry/entity/RNO29-ARIN\nOrgAbuseHandle: ABUSE3850-ARIN\nOrgAbuseName: Abuse Contact\nOrgAbusePhone: +31205354444 \nOrgAbuseEmail: abuse@ripe.net\nOrgAbuseRef: https://rdap.arin.net/registry/entity/ABUSE3850-ARIN\ninetnum: 31.139.365.0 - 31.139.365.255\nnetname: STRATO-RZG-DED\norg: ORG-SRA1-RIPE\ndescr: Strato Rechenzentrum, Berlin\ncountry: DE\nadmin-c: SRDS-RIPE\ntech-c: SRDS-RIPE\nremarks: ************************************************************\nremarks: * Please send abuse complaints to abuse-server@strato.de *\nremarks: * or fax +49-30-88615-755 ONLY. *\nremarks: * Abuse reports to other e-mail addresses will be ignored. *\nremarks: ************************************************************\nstatus: ASSIGNED PA\nmnt-by: STRATO-RZG-MNT\ncreated: 2004-02-03T18:37:52Z\nlast-modified: 2013-07-06T09:34:25Z\nsource: RIPE\norganisation: ORG-SRA1-RIPE\norg-name: Strato AG\norg-type: LIR\naddress: Pascalstrasse 10\naddress: 10587\naddress: Berlin\naddress: GERMANY\nphone: +4930398020\nfax-no: +493039802222\nadmin-c: CM265-RIPE\nabuse-c: SRAC-RIPE\nmnt-ref: RIPE-NCC-HM-MNT\nmnt-ref: STRATO-RZG-MNT\nmnt-by: RIPE-NCC-HM-MNT\nmnt-by: STRATO-RZG-MNT\ncreated: 2004-04-17T11:12:39Z\nlast-modified: 2019-02-06T12:46:35Z\nsource: RIPE # Filtered\nrole: RIPE contact Dedicated Server\naddress: STRATO AG\naddress: Pascalstr. 10\naddress: D-10587 Berlin\naddress: Germany\nphone: +49 30 39802-0\norg: ORG-SRA1-RIPE\nabuse-mailbox: abuse-server@strato.de\nadmin-c: XX1-RIPE\ntech-c: XX1-RIPE\nnic-hdl: SRDS-RIPE\nremarks: ************************************************************\nremarks: * Please send abuse complaints to abuse-server@strato.de *\nremarks: * or fax +49-30-88615-755 ONLY. *\nremarks: * Abuse reports to other e-mail addresses will be ignored. *\nremarks: * *\nremarks: * For peering requests or operational issues please look *\nremarks: * at the information in the AS6724 RIPE database object. *\nremarks: ************************************************************\nmnt-by: STRATO-RZG-MNT\ncreated: 2010-01-15T08:35:31Z\nlast-modified: 2019-02-06T12:47:52Z\nsource: RIPE # Filtered\nroute: 81.169.165.0/24\ndescr: STRATO AG\ndescr: prefix only advertised in case of DDoS\norigin: AS6724\nmnt-by: STRATO-RZG-MNT\ncreated: 2014-02-18T16:19:05Z\nlast-modified: 2014-02-18T16:19:05Z\nsource: RIPE\n",
            "whois_date": 1565760528
        },
        "id": "31.139.365.245",
        "links": {
            "self": "https://www.virustotal.com/api/v3/ip_addresses/31.139.365.245"
        },
        "type": "ip_address"
    }
}
```

## Relationships

In addition to the previously described attributes, IP address objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](https://virustotal.readme.io/reference/relationships) section. The available relationships are described in the following table:

| Relationship                  | Description                                            | Accessibility             | Return object type                                 |
| :---------------------------- | :----------------------------------------------------- | :------------------------ | :------------------------------------------------- |
| comments                      | Comments for the IP address.                           | Everyone.                 | List of [Comments](https://virustotal.readme.io/reference/comments).                  |
| communicating\_files          | Files that communicate with the IP address.            | Everyone.                 | List of [Files](https://virustotal.readme.io/reference/files).                        |
| downloaded\_files             | Files downloaded from the IP address.                  | VT Enterprise users only. | List of [Files](https://virustotal.readme.io/reference/files).                        |
| graphs                        | Graphs including the IP address.                       | Everyone.                 | List of [Graphs](https://virustotal.readme.io/reference/graph-object).                |
| historical\_ssl\_certificates | SSL certificates associated with the IP.               | Everyone.                 | List of [SSL Certificate](https://virustotal.readme.io/reference/ssl-certificate).    |
| historical\_whois             | WHOIS information for the IP address.                  | Everyone.                 | List of [Whois](https://virustotal.readme.io/reference/whois).                        |
| related\_comments             | Community posted comments in the IP's related objects. | Everyone.                 | List of [Comments](https://virustotal.readme.io/reference/comments).                  |
| related\_references           | References related to the IP address.                  | VT Enterprise users only. | List of [References](https://virustotal.readme.io/reference/references).              |
| related\_threat\_actors       | Threat actors related to the IP address.               | VT Enterprise users only. | List of [Threat Actors](https://virustotal.readme.io/reference/threat-actors-object). |
| referrer\_files               | Files containing the IP address.                       | Everyone.                 | List of [Files](https://virustotal.readme.io/reference/files).                        |
| resolutions                   | IP address' resolutions                                | Everyone.                 | List of [Resolutions](https://virustotal.readme.io/reference/resolution-object).      |
| urls                          | URLs related to the IP address.                        | VT Enterprise users only. | List of [URLs](https://virustotal.readme.io/reference/url-object).                    |

These relationships are detailed in the subsections below.