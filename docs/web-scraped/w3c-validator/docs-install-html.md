# Source: https://validator.w3.org/docs/install.html

Title: Installation Documentation for The W3C Markup Validation Service

URL Source: https://validator.w3.org/docs/install.html

Markdown Content:
The W3C Markup Validator provides Perl/CGI/SGML/XML/DTD-based validation of a variety of document types. SGML and DTDs are older technologies that never found wide use on the Web, so for checking of HTML documents using modern technologies, you probably want to instead use the [W3C HTML Checker](https://validator.w3.org/nu/). To do that,

If for some reason you'd rather install and run a service based on the same source as the W3C Markup Validator, this page provides the following information:

The installation guide we provide here is a rather generic set of instructions, which should work on most systems. To our knowledge, the following platform-specific guides are also available and can be of interest :

*   [Mac OS X and OS X Server](http://www.456bereastreet.com/archive/201105/installing_the_w3c_markup_validator_on_mac_os_x/) by Roger Johansson,
*   [Windows](https://validator.w3.org/docs/install_win.html), by David Tibbe
*   [Linux (Slackware)](http://lists.w3.org/Archives/Public/www-validator/2003Dec/0023.html) by Nick Talbott

#### Related documentation

This installation guides presumes knowledge of the [source availability](https://validator.w3.org/source/) for the Markup Validator.

We recommend that [developers](https://validator.w3.org/docs/devel.html) wishing to contribute on the Markup Validator or modify it go through this installation procedure once, to get familiar with the system.

### Installing on packaged systems

The easiest way to install released versions of the Markup Validator is to use the packages created for some platforms by contributors: Mac OS X, openSUSE/SUSE Linux, Debian GNU/Linux and Fedora/Red Hat packages are [available](https://validator.w3.org/source/).

### Installing from source (generic case)

These instructions are strongly inspired from Nick Talbott's guide for Slackware Linux. Thanks Nick!

The installation guide assumes that you have a working Web server. We suggest the popular Apache server, which is used for the W3C Markup Validation service. The validator may work with other Web servers than the popular Apache, but we cannot guarantee that it will. You will also need a working installation of the Perl language (standard on most Web servers).

#### Step 0: Prerequisites

Apart from a properly configured Web server, the Validator needs a SGML parser -- that does all the hard work --, Perl (version 5.8.0 or newer) and several Perl modules used by the "check" CGI script.

The following few steps will guide you through installing those prerequisites, and then the validator itself

#### Step 1: install OpenSP, the SGML (and XML) parser

The SGML parser we're currently using is `OpenSP 1.5.2`, which can be found on the [OpenJade home page](http://sourceforge.net/projects/openjade/). Note that the validator will not work with any version of OpenSP earlier than 1.5.2.

If you install opensp from source, make sure to enable HTTP retrieval of DTDs. Disabling the building of documentation

Run the following as root/administrator, or under sudo

[unpack opensp]
./configure --enable-http --disable-doc-build
make
make install

#### Step 2: install required Perl Modules

##### Quick and Easy: install the CPAN bundle

One easy - and strongly recommended - way to take care of all these Perl module dependencies is to install [Bundle-W3C-Validator](http://search.cpan.org/dist/Bundle-W3C-Validator/) from CPAN. See the [documentation included with it](http://search.cpan.org/dist/Bundle-W3C-Validator/lib/Bundle/W3C/Validator.pm) for more details.

Run the following as root/administrator, or under sudo

perl -MCPAN -e shell
[cpan shell starts, you may need to answer configuration questions]
install Bundle::W3C::Validator

##### For reference: List of required Perl module distributions

**You may skip this if you have successfully installed the bundle above**.

Below are the Perl modules required to run the Markup Validator. This list is informative, you do not need to install them individually if you follow the [CPAN instructions](https://validator.w3.org/docs/install.html#install-prereq-perl) above.

[CGI.pm](http://search.cpan.org/dist/CGI.pm/)>= 3.40 The all-singing, all-dancing, everything-_and_-the-kitchen-sink, Perl CGI library. This takes care of all those niggly little bits of CGI for us and make options parsing and file upload a breeze. [Config-General](http://search.cpan.org/dist/Config-General/)>= 2.32 Configuration file handling. [Encode](http://search.cpan.org/dist/Encode/) and [Encode-HanExtra](http://search.cpan.org/dist/Encode-HanExtra/) Support for multiple character encodings. [HTML-Parser](http://search.cpan.org/dist/HTML-Parser/)>= 3.60 Minimal HTML parser used for preparse and finding metadata. [HTML-Encoding](http://search.cpan.org/dist/HTML-Encoding/) Determine the encoding of HTML/XML/XHTML documents. [HTML-Template](http://search.cpan.org/dist/HTML-Template/)>= 2.6 Template system which allows us to separate Validator's logic and presentation. [JSON](http://search.cpan.org/dist/JSON/)>= 2.00 JSON output support. [libwww-perl](http://search.cpan.org/dist/libwww-perl/)>= 5.802 Gisle Aas' most excellent WWW library for Perl. This is where our support for downloading pages off the net comes from. Version 5.802 or newer is required, however we strongly suggest a (much) newer version. Validator's support for compressed responses is announced using the `Accept-Encoding` HTTP header with version 5.816 and later, depending on if the modules required for libwww-perl's compression facilities are installed. If you want your Validator to support SSL/TLS, see [README.SSL](http://search.cpan.org/dist/libwww-perl/README.SSL) included in the libwww-perl distribution. [Net-IP](http://search.cpan.org/dist/Net-IP/) IP address manipulation. [SGML-Parser-OpenSP](http://search.cpan.org/dist/SGML-Parser-OpenSP/)>= 0.991 Interface to the [OpenSP parser](https://validator.w3.org/docs/install.html#install-prereq-sp). [URI](http://search.cpan.org/dist/URI/)>= 1.53 Library to handle URIs and escaping special characters in them. [XML-LibXML](http://search.cpan.org/dist/XML-LibXML/)>= 1.73 The Perl binding for [libxml2](http://xmlsoft.org/), used to check the syntax of XML-based document types. In addition to the version requirement, XML-LibXML needs to be built with support for libxml2 structured errors, i.e. libxml2 >= 2.6.21. 
###### For reference: List of optional Perl module distributions

The Perl modules listed below are optional; the validator will use them to provide some extra functionality if they're available.

[Encode-JIS2K](http://search.cpan.org/dist/Encode-JIS2K/) Support for additional Japanese character encodings. [HTML-Tidy](http://search.cpan.org/dist/HTML-Tidy/) HTML-Tidy is used for generating a cleaned up version of the submitted markup. 
#### Step 3: Download the validator and DTDs

Download the Validator code, configuration and DTD library from the [Github repository](https://github.com/w3c/markup-validator/) master branch.

#### Step 4: Unpack the validator

1.   Create a directory for the validator's installation. On Unix-based systems, we suggest to use the default folder `/usr/local/markup-validator`. This directory will be referred to as `[validatorpath]` throughout this guide.

2.   ```
cd /usr/local ; git clone https://github.com/w3c/markup-validator.git
```
.

The `[validatorpath]` directory should now have subdirectories named `cgi-bin`, `htdocs`, and and `share`.

#### Step 5: Configure the Validator

1.   Create the directory `/etc/w3c` and copy all the files from `[validatorpath]/htdocs/config/` to it. You may keep the configuration files in place, but would have to modify the Web Server's environment variables to point to the configuration directory. As this may be tedious, we recommend using `/etc/w3c`.

2.   Edit `/etc/w3c/validator.conf` to reflect where files are in your installation, and configure other parameters there as you wish. This file is well commented and modifying it should be relatively straightforward.

In general you will only need to check that the Base path is set to where you have unpacked the validator files. If you have used `/usr/local/validator` you do not need to change anything

Base = /usr/local/validator

If you plan to validate documents on a private network, you will need to enable the following option in the `validator.conf` file:

Allow Private IPs = yes
3.   If you want to check documents with the (external and experimental) HTML5 conformance checker, you may want to [install the validator.nu](https://about.validator.nu/) engine and enable it with the following in your validator.conf file:

<External>
## Enable checking documents via external services
HTML5 = http://localhost:8888/html5/   
</External>    
4.   You may now test the validator script, before plugging it into the Web Server:

# cd /usr/local/validator/
# cd cgi-bin/
# ./check uri=http://www.w3.org/
…

The script should output the raw HTML results of validation. If this does not work, double-check that you have properly followed all the steps so far.

##### For reference: list of configuration files

**You may skip this, unless you plan to modify the validator's default behavior.**.

validator.conf The validator's **main configuration file**. This will generally be the only file you need to edit. It sets various parameters, such as: the address of the maintainer, various file paths and locations, whether the [API](https://validator.w3.org/docs/api.html) is enabled, etc. charset.cfg Maps character sets to conversion parameters for validator's internal UTF-8 conversion. types.conf Maps MIME/HTTP Content-Types to an internal "document type" which is used for treating HTML, XML, and XHTML in different ways. 
#### Step 6: Configure the Web server

The following instructions are for the Apache Web server, and should be adapted if you plan on using another server.

1.   If you are using the Apache server, you may use the validator under mod_perl2. This should happen automatically if you are using the httpd.conf snippet distributed with the validator or something similar, and your Apache server has mod_perl2 installed and enabled. Using mod_perl2 will bring important performance benefits, but has not been tested extensively. If you are successfully running the validator under mod_perl, or run into issues doing so, [contact us](https://validator.w3.org/feedback.html).

Also worth enabling within Apache is mod_expires, which will allow caching of the validator's static documents, stylesheets, and images.

2.   Edit the configuration of your Web server to refer to the specific configuration file for the validator.

This can be done by inserting the contents of the `httpd/conf/httpd.conf` file in your `httpd.conf`, or by copying the file somewhere and including it like:

Include /where/you/copied/it/httpd.conf
Then, start editing the validator specific part.

3.   You may want to set up a "virtual server" for the service. This can be done by adding something similar to the following :

<VirtualHost 127.0.0.1>                                                               
	DocumentRoot [validatorpath]/htdocs/                        
	ServerName validator.example.org
</VirtualHost>
**AND/OR** you may want to have the service at a specific location on your Web server, which can be configured as follows :

Alias /validator/ [validatorpath]/htdocs/
4.   Configure environment variables affective validator's outside connectivity if needed (such as `http_proxy`), see examples in the supplied `httpd.conf` and [LWP](http://search.cpan.org/dist/libwww-perl/lib/LWP.pm#ENVIRONMENT) and [Net::FTP](http://search.cpan.org/dist/libnet/Net/FTP.pm#CONSTRUCTOR) documentation.

5.   Finish editing this HTTP server configuration file, adapting all the directory references to reflect the paths used in your installation.

6.   Now restart the Web server to activate the updated configuration.

For Apache this is done by typing into a shell, as System Administrator: `apachectl graceful` (or, for older versions of Apache `apachectl configtest` then `apachectl restart`)

#### Step 7: Check the installation

1.   Point your browser at the new site.

2.   Check the error log of the Web server to get clues on what may be wrong if you get any server errors.

**Help us** improve this installation guide by sending us your feedback if you install the validator on your local system!

### Troubleshooting a new installation

It is not always easy to troubleshoot an incomplete, or failed, installation of the Markup Validator. While the instructions given in this page should help most people install the validator successfully on their system, bad luck, a forgotten step or a broken component can make things go sour.

#### Double check the installation steps

The first sound thing to do if the installation failed would be to check that you did not forget any step while installing. properly copying and editing the configuration file is among the common mistakes, for example.

#### Check the logs

The error logs for your Web server should be a good first place to look for hints on what is wrong with your installation.

#### Check the dependencies

A common problem with a newly installed validator is a validator that is apparently running but marking anything as "invalid", without giving any error message as output.

This is somewhat typical of a problem with OpenSP. Cross-check that you actually have a version above 1.5, by running onsgmls --version.

#### The miracle debug options

If the validator is misbehaving, you can try forcing various debug options by appending to the URL the following string: &debug=1

This can sometimes provide you with error messages that would not have appeared anywhere in non-debug mode, and can be helpful to diagnose the problem

#### If all fails...

Don't hesitate to contact the public mailing-list www-validator@w3.org with all the details you can provide on what you did, tried, and what went wrong...

### Post-install options

if the installation succeeded, you should be able to now use the Markup Validator on your own system and network. You may want to give the validator a look and feel specific to your Web site. The easiest way to achieve this is to edit `header.html` and `footer.html` (in the `htdocs` directory), the header and footer markup snippets used to build all pages for the validator.

You may also edit the Style Sheets (in the same directory), especially `base.css` You may however want to avoid editing the other CSS files too heavily, there is a risk you could make the output of the validator unusable.

If you edit any *.css or *.js files, make sure that you update the gzipped versions of the edited files as well if they're installed and content negotiation for them is enabled in your setup (both are usually true if the validator was installed following these instructions).

### Credits and Acknowledgments

The Validator Team wishes to thank Nick Talbott and Stephen Yoch for their help in creating these installation instructions. Thanks also to all the people who use and review the guide to make it better and better!
