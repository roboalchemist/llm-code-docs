# Specify Parameter Values

> Specify and pass parameters as values for the AWS CLI command options.

**Source:** https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters.html

---

# Specifying parameter values in the AWS CLI

Many parameters used in the AWS Command Line Interface (AWS CLI) are simple string or numeric values, such as
        the key-pair name `my-key-pair` in the following `aws ec2
            create-key-pair` command example. 

`$ ``aws ec2 create-key-pair --key-name my-key-pair`Formatting for command can vary between terminals. For example, most terminals are case
        sensitive but Powershell is case insensitive. This means the two following command examples
        would yield different results for case sensitive terminals as they view
            `MyFile*.txt` and `myfile*.txt` as **different** parameters. 

However, PowerShell would process these requests as the same as it sees
            `MyFile*.txt` and `myfile*.txt` as the **same** parameters.  The following command example demonstrates
        these paramaters using the `aws s3 cp` command:

`$ ``aws s3 cp . s3://amzn-s3-demo-bucket/path --include "MyFile*.txt"`
`$ ``aws s3 cp . s3://amzn-s3-demo-bucket/path --include "myfile*.txt"`For more information on PowerShell's case insensitivy, see [about_Case-Sensitivity](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_case-sensitivity) in the *PowerShell
            documentation*.

Sometimes you need to use quotation marks or literals around strings that include special
        or space characters. The rules around this formatting can also vary between terminals. For
        more information about using quotation marks around complex parameters, see [Using quotation marks and literals
            with strings in the AWS CLI](./cli-usage-parameters-quoting-strings.html).

These topics cover the most common terminal formatting rules. If you are having issues with
        your terminal recognizing your parameter values, be sure to review the topics in this
        section and also to check your terminal's documentation for their specific syntax
        rules.

###### Parameter topics

- 
[Common parameter types in the AWS CLI](./cli-usage-parameters-types.html)

- 
[Using quotation marks and literals
            with strings in the AWS CLI](./cli-usage-parameters-quoting-strings.html)

- 
[Loading a parameter from a file in the
            AWS CLI](./cli-usage-parameters-file.html)

- 
[AWS CLI skeletons and input files in the AWS CLI](./cli-usage-skeleton.html)

- 
[Using shorthand syntax in the AWS CLI](./cli-usage-shorthand.html)

 **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Command Structure

Common Parameter Types