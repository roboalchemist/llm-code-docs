# Source: https://docs.oxla.com/sql-reference/sql-functions/aggregate-functions/overview-statistics.md

# Overview

Aggregate functions for statistics are typically used for statistical analysis. Oxla supports the following functions:

| **Functions**                                                                      | **Description**                                                                                                      |
| ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| [CORR](/sql-reference/sql-functions/aggregate-functions/corr)                      | Calculates the Pearson correlation coefficient between two sets of number pairs                                      |
| [COVAR\_POP](/sql-reference/sql-functions/aggregate-functions/covar-pop)           | Calculates the population covariance between two sets of number pairs                                                |
| [COVAR\_SAMP](/sql-reference/sql-functions/aggregate-functions/covar-samp)         | Calculates the sample covariance between two sets of number pairs                                                    |
| [REGR\_AVGX](/sql-reference/sql-functions/aggregate-functions/regr-avgx)           | Calculates the average of the independent variable (sum(X)/N)                                                        |
| [REGR\_AVGY](/sql-reference/sql-functions/aggregate-functions/regr-avgy)           | Calculates the average of the dependent variable (sum(Y)/N)                                                          |
| [REGR\_COUNT](/sql-reference/sql-functions/aggregate-functions/regr-count)         | Calculates the number of input rows in which both expressions are non-null                                           |
| [REGR\_INTERCEPT](/sql-reference/sql-functions/aggregate-functions/regr-intercept) | Calculates the y-intercept of the univariate linear regression line for a group of data points                       |
| [REGR\_R2](/sql-reference/sql-functions/aggregate-functions/regr-r2)               | Calculates the coefficient of determination (R<sup>2</sup>) for a linear regression model                            |
| [REGR\_SLOPE](/sql-reference/sql-functions/aggregate-functions/regr-slope)         | Calculates slope of the least-squares-fit linear equation determined by the (X, Y) pairs                             |
| [REGR\_SXX](/sql-reference/sql-functions/aggregate-functions/regr-sxx)             | Calculates the sum(X<sup>2</sup>) - sum(X)<sup>2</sup>/N ("sum of squares" of the independent variable)              |
| [REGR\_SXY](/sql-reference/sql-functions/aggregate-functions/regr-sxy)             | Calculates the sum(X<sup>\*</sup>Y) - sum(X) \* sum(Y)/N ("sum of products" of independent times dependent variable) |
| [REGR\_SYY](/sql-reference/sql-functions/aggregate-functions/regr-syy)             | Calculates the sum(Y<sup>2</sup>) - sum(Y)<sup>2</sup>/N ("sum of squares" of the dependent variable)                |
| [STDDEV](/sql-reference/sql-functions/aggregate-functions/stddev)                  | Calculates the sample standard deviation of a set of numeric values                                                  |
| [STDDEV\_POP](/sql-reference/sql-functions/aggregate-functions/stddev-pop)         | Calculates the population standard deviation of the input values                                                     |
| [STDDEV\_SAMP](/sql-reference/sql-functions/aggregate-functions/stddev-samp)       | Calculates the sample standard deviation of the input values                                                         |
| [VARIANCE](/sql-reference/sql-functions/aggregate-functions/variance)              | Calculates the the sample variance of a set of numeric values.                                                       |
| [VAR\_POP](/sql-reference/sql-functions/aggregate-functions/var-pop)               | Calculates the population variance of the input values (square of the population standard deviation)                 |
| [VAR\_SAMP](/sql-reference/sql-functions/aggregate-functions/var-samp)             | Calculates the sample variance of the input values (square of the sample standard deviation)                         |
