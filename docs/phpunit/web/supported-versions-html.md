# Source: https://phpunit.de/supported-versions.html

Title: Supported Versions of PHPUnit

URL Source: https://phpunit.de/supported-versions.html

Markdown Content:
| Major Version | PHP Compatibility | Initial Release | End of Bugfix Support | End of Life |
| --- | --- | --- | --- | --- |
| [PHPUnit 13](https://phpunit.de/announcements/phpunit-13.html) | >= PHP 8.4 | February 6, 2026 | February 4, 2028 | To be determined |
| [PHPUnit 12](https://phpunit.de/announcements/phpunit-12.html) | >= PHP 8.3 | February 7, 2025 | February 5, 2027 | To be determined |
| [PHPUnit 11](https://phpunit.de/announcements/phpunit-11.html) | >= PHP 8.2 | February 2, 2024 | February 6, 2026 | To be determined |
| [PHPUnit 10](https://phpunit.de/announcements/phpunit-10.html) | >= PHP 8.1 | February 3, 2023 | February 7, 2025 | To be determined |
| [PHPUnit 9](https://phpunit.de/announcements/phpunit-9.html) | >= PHP 7.3 | February 7, 2020 | February 2, 2024 | To be determined |
| [PHPUnit 8](https://phpunit.de/announcements/phpunit-8.html) | >= PHP 7.2 | February 1, 2019 | February 3, 2023 | To be determined |
| [PHPUnit 7](https://phpunit.de/announcements/phpunit-7.html) | PHP 7.1 - PHP 7.3 | February 2, 2018 | February 7, 2020 | February 7, 2020 |
| [PHPUnit 6](https://phpunit.de/announcements/phpunit-6.html) | PHP 7.0 - PHP 7.2 | February 3, 2017 | February 1, 2019 | February 1, 2019 |
| [PHPUnit 5](https://phpunit.de/announcements/phpunit-5.html) | PHP 5.6 - PHP 7.1 | October 2, 2015 | February 2, 2018 | February 2, 2018 |
| [PHPUnit 4](https://phpunit.de/announcements/phpunit-4.html) | PHP 5.3 - PHP 5.6 | March 7, 2014 | February 3, 2017 | February 3, 2017 |

*   Bugfix Support
*   Life Support
*   End-of-Life

* * *

**Bugfix Support** means that bugs will be fixed for a version of PHPUnit. Bugfix Support for major version `X` ends two years after its initial release (when major version `(X+2)` is released). Bugfix Support for minor version `X.Y` ends when minor version `X.(Y+1)` is released.

When Bugfix Support ends for a major version, Life Support for this major version begins.

**Life Support** means that changes will be made for an otherwise unsupported version of PHPUnit to be compatible with new versions of PHP. Life Support ends when an old version of PHPUnit cannot be made compatible with a new version of PHP without breaking [backward compatibility](https://phpunit.de/backward-compatibility.html).

The fact that a version of PHPUnit supports a specific PHP version means that this version of PHPUnit works on that PHP version for PHP code that is compatible with the version of PHP required by the PHPUnit version in question. For example, PHPUnit 8.5 requires PHP 7.2. PHPUnit 8.5 works for PHP code compatible with PHP 7.2 on PHP 8. However, PHPUnit 8.5's test double code generator does not support PHP 8's union types syntax, for example.

* * *

Juliette Reinders Folmer maintains [phpunit-polyfills](https://github.com/Yoast/PHPUnit-Polyfills), a library that "offers a number of polyfills for functionality which was introduced, split up or renamed in PHPUnit". Use this if you must be able to run your tests using PHPUnit 4 through PHPUnit 9, for instance.
