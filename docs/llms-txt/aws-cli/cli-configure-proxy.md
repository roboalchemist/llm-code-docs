# HTTP proxies

> Learn how to configure the AWS CLI to use an HTTP proxy through environment variables using DNS domain names, IP addresses, and port numbers.

**Source:** https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-proxy.html

---

# Using an HTTP proxy for the AWS CLI

To access AWS through proxy servers, you can configure the `HTTP_PROXY` and
      `HTTPS_PROXY` environment variables with either the DNS domain names or IP
    addresses and port numbers that your proxy servers use.

###### Topics

- 
[Using the examples](#cli-configure-proxy-using)

- 
[Authenticating to a proxy](#cli-configure-proxy-auth)

- 
[Using a proxy on Amazon EC2 instances](#cli-configure-proxy-ec2)

- 
[Troubleshooting](#cli-configure-proxy-tshoot)

## Using the examples

###### Note

The following examples show the environment variable name in all uppercase letters.
        However, if you specify a variable twice using different cases, the lowercase letters take
        precedence. We recommend that you define each variable only once to avoid system confusion
        and unexpected behavior.

The following examples show how you can use either the explicit IP address of your proxy
      or a DNS name that resolves to the IP address of your proxy. Either can be followed by a colon
      and the port number to which queries should be sent.

## Authenticating to a proxy

###### Note

The AWS CLI doesn't support NTLM proxies. If you use an NTLM or Kerberos protocol proxy,
        you might be able to connect through an authentication proxy like [Cntlm](http://cntlm.sourceforge.net).

The AWS CLI supports HTTP Basic authentication. Specify the username and password in the
      proxy URL, as follows. 

## Using a proxy on Amazon EC2 instances

If you configure a proxy on an Amazon EC2 instance launched with an attached IAM role, ensure
      that you exempt the address used to access the [instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html). To do this, set
      the `NO_PROXY` environment variable to the IP address of the instance metadata
      service, 169.254.169.254. This address does not vary.

## Troubleshooting

If you come across issues with the AWS CLI, see [Troubleshooting errors for the AWS CLI](./cli-chap-troubleshooting.html)
      for troubleshooting steps. For the most relevant troubleshooting steps, see [SSL certificate errors](./cli-chap-troubleshooting.html#tshoot-certificate-verify-failed).

 **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Retries

Endpoints