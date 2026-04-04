# Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff

Title: backoff package - go.temporal.io/server/common/backoff - Go Packages

URL Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff

Markdown Content:
backoff package - go.temporal.io/server/common/backoff - Go Packages
===============

[![Image 1: Go](https://pkg.go.dev/static/shared/logo/go-white.svg)](https://go.dev/)

[Skip to Main Content](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#main-content)

![Image 2](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)![Image 3](https://pkg.go.dev/static/shared/icon/search_gm_grey_24dp.svg)

*   [Why Go ![Image 4: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#)
    *   [Case Studies](https://go.dev/solutions#case-studies) 
Common problems companies solve with Go

    *   [Use Cases](https://go.dev/solutions#use-cases) 
Stories about how and why companies use Go

    *   [Security](https://go.dev/security/) 
How Go can help keep you secure by default

*   [Learn](https://go.dev/learn/)
*   [Docs ![Image 5: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#)
    *   [Effective Go](https://go.dev/doc/effective_go) 
Tips for writing clear, performant, and idiomatic Go code

    *   [Go User Manual](https://go.dev/doc/) 
A complete introduction to building software with Go

    *   [Standard library](https://pkg.go.dev/std) 
Reference documentation for Go's standard library

    *   [Release Notes](https://go.dev/doc/devel/release) 
Learn what's new in each Go release

*   [Packages](https://pkg.go.dev/)
*   [Community ![Image 6: submenu dropdown icon](https://pkg.go.dev/static/shared/icon/arrow_drop_down_gm_grey_24dp.svg)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#)
    *   [Recorded Talks](https://go.dev/talks/) 
Videos from prior events

    *   [Meetups _![Image 7](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go) 
Meet other local Go developers

    *   [Conferences _![Image 8](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences) 
Learn and network with Go developers from around the world

    *   [Go blog](https://go.dev/blog) 
The Go project's official blog.

    *   [Go project](https://go.dev/help) 
Get help and stay informed from Go

    *    Get connected  [![Image 9](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts "Get connected with google-groups (Opens in new window)")[![Image 10](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang "Get connected with github (Opens in new window)")[![Image 11](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang "Get connected with twitter (Opens in new window)")[![Image 12](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/ "Get connected with reddit (Opens in new window)")[![Image 13](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/ "Get connected with slack (Opens in new window)")[![Image 14](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

[![Image 15: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)

*   [Why Go _![Image 16](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#)

[_![Image 17](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Why Go](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#) 
    *   [Case Studies](https://go.dev/solutions#case-studies)
    *   [Use Cases](https://go.dev/solutions#use-cases)
    *   [Security](https://go.dev/security/)

*   [Learn](https://go.dev/learn/)
*   [Docs _![Image 18](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#)

[_![Image 19](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Docs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#) 
    *   [Effective Go](https://go.dev/doc/effective_go)
    *   [Go User Manual](https://go.dev/doc/)
    *   [Standard library](https://pkg.go.dev/std)
    *   [Release Notes](https://go.dev/doc/devel/release)

*   [Packages](https://pkg.go.dev/)
*   [Community _![Image 20](https://pkg.go.dev/static/shared/icon/navigate\_next\_gm\_grey\_24dp.svg)_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#)

[_![Image 21](https://pkg.go.dev/static/shared/icon/navigate\_before\_gm\_grey\_24dp.svg)_ Community](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#) 
    *   [Recorded Talks](https://go.dev/talks/)
    *   [Meetups _![Image 22](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://www.meetup.com/pro/go)
    *   [Conferences _![Image 23](https://pkg.go.dev/static/shared/icon/launch\_gm\_grey\_24dp.svg)_](https://github.com/golang/go/wiki/Conferences)
    *   [Go blog](https://go.dev/blog)
    *   [Go project](https://go.dev/help)
    *   Get connected [![Image 24](https://pkg.go.dev/static/shared/logo/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)[![Image 25](https://pkg.go.dev/static/shared/logo/social/github.svg)](https://github.com/golang)[![Image 26](https://pkg.go.dev/static/shared/logo/social/twitter.svg)](https://twitter.com/golang)[![Image 27](https://pkg.go.dev/static/shared/logo/social/reddit.svg)](https://www.reddit.com/r/golang/)[![Image 28](https://pkg.go.dev/static/shared/logo/social/slack.svg)](https://invite.slack.golangbridge.org/)[![Image 29](https://pkg.go.dev/static/shared/logo/social/stack-overflow.svg)](https://stackoverflow.com/collectives/go) 

1.   [Discover Packages](https://pkg.go.dev/)
2.   [go.temporal.io/server](https://pkg.go.dev/go.temporal.io/server@v1.30.0)
3.   [common](https://pkg.go.dev/go.temporal.io/server/common@v1.30.0)
4.   [backoff](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff)![Image 30](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[![Image 31: Go](https://pkg.go.dev/static/shared/logo/go-blue.svg)](https://go.dev/)
backoff
=======

package![Image 32](https://pkg.go.dev/static/shared/icon/content_copy_gm_grey_24dp.svg)

[Version: v1.30.0](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff?tab=versions)

 Opens a new window with list of versions in this module. 

Latest Latest 

![Image 33: Warning](https://pkg.go.dev/static/shared/icon/alert_gm_grey_24dp.svg)
This package is not in the latest version of its module.

[Go to latest](https://pkg.go.dev/go.temporal.io/server/common/backoff) Published: Feb 4, 2026  License: [MIT](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff?tab=licenses)

 Opens a new window with license information. 

[Imports: 12](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff?tab=imports)

 Opens a new window with list of imports. 

[Imported by: 5](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff?tab=importedby)

 Opens a new window with list of known importers. 

Details
-------

*   ![Image 34: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Valid [go.mod](https://github.com/temporalio/temporal/tree/v1.30.0/go.mod) file ![Image 35](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go. 
*   ![Image 36: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Redistributable license ![Image 37](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed. 
*   ![Image 38: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Tagged version ![Image 39](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
Modules with tagged versions give importers more predictable builds. 
*   ![Image 40: checked](https://pkg.go.dev/static/shared/icon/check_circle_gm_grey_24dp.svg) Stable version ![Image 41](https://pkg.go.dev/static/shared/icon/help_gm_grey_24dp.svg)
When a project reaches major version v1 it is considered stable. 
*   [Learn more about best practices](https://pkg.go.dev/about#best-practices)

Repository
----------

[github.com/temporalio/temporal](https://github.com/temporalio/temporal "https://github.com/temporalio/temporal")

Links
-----

*   [![Image 42: Open Source Insights Logo](https://pkg.go.dev/static/shared/icon/depsdev-logo.svg) Open Source Insights](https://deps.dev/go/go.temporal.io%2Fserver/v1.30.0 "View this module on Open Source Insights")

 Jump to ... 

*   [Documentation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#section-documentation)
    *   [Index](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#pkg-index)
    *   [Examples](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#pkg-examples)
        *   [ExponentialRetryPolicy.WithMaximumInterval](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#example-ExponentialRetryPolicy.WithMaximumInterval "ExponentialRetryPolicy.WithMaximumInterval")

    *   [Constants](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#pkg-constants)
    *   [Variables](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#pkg-variables)
    *   [Functions](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#pkg-functions)
        *   [CalculateExponentialRetryInterval(retryPolicy, attempt)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#CalculateExponentialRetryInterval "CalculateExponentialRetryInterval(retryPolicy, attempt)")
        *   [ExponentialBackoffAlgorithm(initInterval, backoffCoefficient, currentAttempt)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialBackoffAlgorithm "ExponentialBackoffAlgorithm(initInterval, backoffCoefficient, currentAttempt)")
        *   [FullJitter(input)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#FullJitter "FullJitter(input)")
        *   [GetBackoffForNextSchedule(cronSchedule, scheduledTime, now)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#GetBackoffForNextSchedule "GetBackoffForNextSchedule(cronSchedule, scheduledTime, now)")
        *   [GetBackoffForNextScheduleNonNegative(cronSchedule, scheduledTime, now)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#GetBackoffForNextScheduleNonNegative "GetBackoffForNextScheduleNonNegative(cronSchedule, scheduledTime, now)")
        *   [IgnoreErrors(errorsToExclude)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#IgnoreErrors "IgnoreErrors(errorsToExclude)")
        *   [Jitter(input, coefficient)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#Jitter "Jitter(input, coefficient)")
        *   [ThrottleRetry(operation, policy, isRetryable)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ThrottleRetry "ThrottleRetry(operation, policy, isRetryable)")
        *   [ThrottleRetryContext(ctx, operation, policy, isRetryable)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ThrottleRetryContext "ThrottleRetryContext(ctx, operation, policy, isRetryable)")
        *   [ThrottleRetryContextWithReturn(ctx, fn, policy, isRetryable)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ThrottleRetryContextWithReturn "ThrottleRetryContextWithReturn(ctx, fn, policy, isRetryable)")
        *   [ValidateSchedule(cronSchedule)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ValidateSchedule "ValidateSchedule(cronSchedule)")

    *   [Types](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#pkg-types)
        *   [type BackoffCalculatorAlgorithmFunc](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#BackoffCalculatorAlgorithmFunc "type BackoffCalculatorAlgorithmFunc")
            *   [MakeBackoffAlgorithm(requestedDelay)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#MakeBackoffAlgorithm "MakeBackoffAlgorithm(requestedDelay)")

        *   [type ConstantDelayRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ConstantDelayRetryPolicy "type ConstantDelayRetryPolicy")
            *   [NewConstantDelayRetryPolicy(delay)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#NewConstantDelayRetryPolicy "NewConstantDelayRetryPolicy(delay)")
            *   [(p) ComputeNextDelay(_, attempt, _)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ConstantDelayRetryPolicy.ComputeNextDelay "(p) ComputeNextDelay(_, attempt, _)")
            *   [(p) WithJitter(jitterPct)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ConstantDelayRetryPolicy.WithJitter "(p) WithJitter(jitterPct)")
            *   [(p) WithMaximumAttempts(maximumAttempts)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ConstantDelayRetryPolicy.WithMaximumAttempts "(p) WithMaximumAttempts(maximumAttempts)")

        *   [type ErrorDependentRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ErrorDependentRetryPolicy "type ErrorDependentRetryPolicy")
            *   [NewErrorDependentRetryPolicy(delayForError)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#NewErrorDependentRetryPolicy "NewErrorDependentRetryPolicy(delayForError)")
            *   [(p) ComputeNextDelay(_, attempt, err)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ErrorDependentRetryPolicy.ComputeNextDelay "(p) ComputeNextDelay(_, attempt, err)")
            *   [(p) WithJitter(jitterPct)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ErrorDependentRetryPolicy.WithJitter "(p) WithJitter(jitterPct)")
            *   [(p) WithMaximumAttempts(maximumAttempts)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ErrorDependentRetryPolicy.WithMaximumAttempts "(p) WithMaximumAttempts(maximumAttempts)")

        *   [type ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy "type ExponentialRetryPolicy")
            *   [NewExponentialRetryPolicy(initialInterval)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#NewExponentialRetryPolicy "NewExponentialRetryPolicy(initialInterval)")
            *   [(p) ComputeNextDelay(elapsedTime, numAttempts, _)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy.ComputeNextDelay "(p) ComputeNextDelay(elapsedTime, numAttempts, _)")
            *   [(p) WithBackoffCoefficient(backoffCoefficient)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy.WithBackoffCoefficient "(p) WithBackoffCoefficient(backoffCoefficient)")
            *   [(p) WithExpirationInterval(expirationInterval)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy.WithExpirationInterval "(p) WithExpirationInterval(expirationInterval)")
            *   [(p) WithInitialInterval(initialInterval)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy.WithInitialInterval "(p) WithInitialInterval(initialInterval)")
            *   [(p) WithMaximumAttempts(maximumAttempts)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy.WithMaximumAttempts "(p) WithMaximumAttempts(maximumAttempts)")
            *   [(p) WithMaximumInterval(maximumInterval)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy.WithMaximumInterval "(p) WithMaximumInterval(maximumInterval)")

        *   [type IsRetryable](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#IsRetryable "type IsRetryable")
        *   [type Operation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#Operation "type Operation")
        *   [type OperationCtx](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#OperationCtx "type OperationCtx")
        *   [type Retrier](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#Retrier "type Retrier")
            *   [NewRetrier(policy, timeSource)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#NewRetrier "NewRetrier(policy, timeSource)")

        *   [type RetryLockedSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryLockedSource "type RetryLockedSource")
            *   [NewRetryLockedSource()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#NewRetryLockedSource "NewRetryLockedSource()")
            *   [(r) Int63()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryLockedSource.Int63 "(r) Int63()")
            *   [(r) Seed(seed)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryLockedSource.Seed "(r) Seed(seed)")

        *   [type RetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryPolicy "type RetryPolicy")

*   [Source Files](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#section-sourcefiles)

![Image 43](https://pkg.go.dev/static/shared/icon/code_gm_grey_24dp.svg) Documentation [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#section-documentation "Go to Documentation")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Index [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#pkg-index "Go to Index")

*   [Constants](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#pkg-constants)
*   [func CalculateExponentialRetryInterval(retryPolicy *commonpb.RetryPolicy, attempt int32) time.Duration](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#CalculateExponentialRetryInterval)
*   [func ExponentialBackoffAlgorithm(initInterval *durationpb.Duration, backoffCoefficient float64, ...) time.Duration](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialBackoffAlgorithm)
*   [func FullJitter[T ~int64 | ~int | ~int32 | ~float64 | ~float32](input T) T](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#FullJitter)
*   [func GetBackoffForNextSchedule(cronSchedule string, scheduledTime time.Time, now time.Time) time.Duration](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#GetBackoffForNextSchedule)
*   [func GetBackoffForNextScheduleNonNegative(cronSchedule string, scheduledTime time.Time, now time.Time) time.Duration](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#GetBackoffForNextScheduleNonNegative)
*   [func IgnoreErrors(errorsToExclude []error) func(error) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#IgnoreErrors)
*   [func Jitter[T ~int64 | ~int | ~int32 | ~float64 | ~float32](input T, coefficient float64) T](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#Jitter)
*   [func ThrottleRetry(operation Operation, policy RetryPolicy, isRetryable IsRetryable) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ThrottleRetry)
*   [func ThrottleRetryContext(ctx context.Context, operation OperationCtx, policy RetryPolicy, ...) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ThrottleRetryContext)
*   [func ThrottleRetryContextWithReturn[T any](ctx context.Context, fn func(context.Context) (T, error), policy RetryPolicy, ...) (T, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ThrottleRetryContextWithReturn)
*   [func ValidateSchedule(cronSchedule string) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ValidateSchedule)
*   [type BackoffCalculatorAlgorithmFunc](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#BackoffCalculatorAlgorithmFunc)
*       *   [func MakeBackoffAlgorithm(requestedDelay *time.Duration) BackoffCalculatorAlgorithmFunc](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#MakeBackoffAlgorithm)

*   [type ConstantDelayRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ConstantDelayRetryPolicy)
*       *   [func NewConstantDelayRetryPolicy(delay time.Duration) *ConstantDelayRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#NewConstantDelayRetryPolicy)

*       *   [func (p *ConstantDelayRetryPolicy) ComputeNextDelay(_ time.Duration, attempt int, _ error) time.Duration](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ConstantDelayRetryPolicy.ComputeNextDelay)
    *   [func (p *ConstantDelayRetryPolicy) WithJitter(jitterPct float64) *ConstantDelayRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ConstantDelayRetryPolicy.WithJitter)
    *   [func (p *ConstantDelayRetryPolicy) WithMaximumAttempts(maximumAttempts int) *ConstantDelayRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ConstantDelayRetryPolicy.WithMaximumAttempts)

*   [type ErrorDependentRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ErrorDependentRetryPolicy)
*       *   [func NewErrorDependentRetryPolicy(delayForError func(err error) time.Duration) *ErrorDependentRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#NewErrorDependentRetryPolicy)

*       *   [func (p *ErrorDependentRetryPolicy) ComputeNextDelay(_ time.Duration, attempt int, err error) time.Duration](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ErrorDependentRetryPolicy.ComputeNextDelay)
    *   [func (p *ErrorDependentRetryPolicy) WithJitter(jitterPct float64) *ErrorDependentRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ErrorDependentRetryPolicy.WithJitter)
    *   [func (p *ErrorDependentRetryPolicy) WithMaximumAttempts(maximumAttempts int) *ErrorDependentRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ErrorDependentRetryPolicy.WithMaximumAttempts)

*   [type ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy)
*       *   [func NewExponentialRetryPolicy(initialInterval time.Duration) *ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#NewExponentialRetryPolicy)

*       *   [func (p *ExponentialRetryPolicy) ComputeNextDelay(elapsedTime time.Duration, numAttempts int, _ error) time.Duration](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy.ComputeNextDelay)
    *   [func (p *ExponentialRetryPolicy) WithBackoffCoefficient(backoffCoefficient float64) *ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy.WithBackoffCoefficient)
    *   [func (p *ExponentialRetryPolicy) WithExpirationInterval(expirationInterval time.Duration) *ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy.WithExpirationInterval)
    *   [func (p *ExponentialRetryPolicy) WithInitialInterval(initialInterval time.Duration) *ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy.WithInitialInterval)
    *   [func (p *ExponentialRetryPolicy) WithMaximumAttempts(maximumAttempts int) *ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy.WithMaximumAttempts)
    *   [func (p *ExponentialRetryPolicy) WithMaximumInterval(maximumInterval time.Duration) *ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy.WithMaximumInterval)

*   [type IsRetryable](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#IsRetryable)
*   [type Operation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#Operation)
*   [type OperationCtx](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#OperationCtx)
*   [type Retrier](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#Retrier)
*       *   [func NewRetrier(policy RetryPolicy, timeSource clock.TimeSource) Retrier](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#NewRetrier)

*   [type RetryLockedSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryLockedSource)
*       *   [func NewRetryLockedSource() *RetryLockedSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#NewRetryLockedSource)

*       *   [func (r *RetryLockedSource) Int63() int64](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryLockedSource.Int63)
    *   [func (r *RetryLockedSource) Seed(seed int64)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryLockedSource.Seed)

*   [type RetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryPolicy)

### Examples [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#pkg-examples "Go to Examples")

*   [ExponentialRetryPolicy.WithMaximumInterval](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#example-ExponentialRetryPolicy.WithMaximumInterval)

### Constants [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#pkg-constants "Go to Constants")

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/cron.go#L12)const NoBackoff = [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)(-1)

NoBackoff is used to represent backoff when no cron backoff is needed

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L13)const (
// NoInterval represents Maximim interval	NoInterval = 0
)

### Variables [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#pkg-variables "Go to Variables")

This section is empty.

### Functions [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#pkg-functions "Go to Functions")

#### func [CalculateExponentialRetryInterval](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retry.go#L200)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#CalculateExponentialRetryInterval "Go to CalculateExponentialRetryInterval")added in v1.30.0

func CalculateExponentialRetryInterval(retryPolicy *[commonpb](https://pkg.go.dev/go.temporal.io/api/common/v1).[RetryPolicy](https://pkg.go.dev/go.temporal.io/api/common/v1#RetryPolicy), attempt [int32](https://pkg.go.dev/builtin#int32)) [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)

CalculateExponentialRetryInterval calculates the retry interval using exponential backoff algorithm

#### func [ExponentialBackoffAlgorithm](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retry.go#L183)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialBackoffAlgorithm "Go to ExponentialBackoffAlgorithm")added in v1.30.0

func ExponentialBackoffAlgorithm(initInterval *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration), backoffCoefficient [float64](https://pkg.go.dev/builtin#float64), currentAttempt [int32](https://pkg.go.dev/builtin#int32)) [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)

ExponentialBackoffAlgorithm calculates the backoff duration using exponential algorithm. The result is initInterval * (backoffCoefficient ^ (currentAttempt - 1)). If the calculation overflows int64, it returns the maximum possible duration. A negative result will also never be returned.

#### func [FullJitter](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/jitter.go#L10)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#FullJitter "Go to FullJitter")added in v1.20.0

func FullJitter[T ~[int64](https://pkg.go.dev/builtin#int64) | ~[int](https://pkg.go.dev/builtin#int) | ~[int32](https://pkg.go.dev/builtin#int32) | ~[float64](https://pkg.go.dev/builtin#float64) | ~[float32](https://pkg.go.dev/builtin#float32)](input T) T

FullJitter return random number from 0 to input, inclusive, exclusive

#### func [GetBackoffForNextSchedule](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/cron.go#L33)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#GetBackoffForNextSchedule "Go to GetBackoffForNextSchedule")added in v0.6.0

func GetBackoffForNextSchedule(cronSchedule [string](https://pkg.go.dev/builtin#string), scheduledTime [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time), now [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)) [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)

GetBackoffForNextSchedule calculates the backoff time for the next run given a cronSchedule, current scheduled time, and now.

#### func [GetBackoffForNextScheduleNonNegative](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/cron.go#L67)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#GetBackoffForNextScheduleNonNegative "Go to GetBackoffForNextScheduleNonNegative")added in v0.28.0

func GetBackoffForNextScheduleNonNegative(cronSchedule [string](https://pkg.go.dev/builtin#string), scheduledTime [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time), now [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)) [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)

GetBackoffForNextScheduleNonNegative calculates the backoff time and ensures a non-negative duration.

#### func [IgnoreErrors](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retry.go#L164)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#IgnoreErrors "Go to IgnoreErrors")

func IgnoreErrors(errorsToExclude [][error](https://pkg.go.dev/builtin#error)) func([error](https://pkg.go.dev/builtin#error)) [bool](https://pkg.go.dev/builtin#bool)

IgnoreErrors can be used as IsRetryable handler for Retry function to exclude certain errors from the retry list

#### func [Jitter](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/jitter.go#L15)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#Jitter "Go to Jitter")added in v0.3.14

func Jitter[T ~[int64](https://pkg.go.dev/builtin#int64) | ~[int](https://pkg.go.dev/builtin#int) | ~[int32](https://pkg.go.dev/builtin#int32) | ~[float64](https://pkg.go.dev/builtin#float64) | ~[float32](https://pkg.go.dev/builtin#float32)](input T, coefficient [float64](https://pkg.go.dev/builtin#float64)) T

Jitter return random number from (1-coefficient)*input to (1+coefficient)*input, inclusive, exclusive

#### func [ThrottleRetry](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retry.go#L40)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ThrottleRetry "Go to ThrottleRetry")added in v1.17.1

func ThrottleRetry(operation [Operation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#Operation), policy [RetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryPolicy), isRetryable [IsRetryable](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#IsRetryable)) [error](https://pkg.go.dev/builtin#error)

ThrottleRetry is a resource aware version of Retry. Resource exhausted error will be retried using a different throttle retry policy, instead of the specified one.

#### func [ThrottleRetryContext](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retry.go#L49)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ThrottleRetryContext "Go to ThrottleRetryContext")added in v1.17.1

func ThrottleRetryContext(
	ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context),
	operation [OperationCtx](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#OperationCtx),
	policy [RetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryPolicy),
	isRetryable [IsRetryable](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#IsRetryable),
) [error](https://pkg.go.dev/builtin#error)

ThrottleRetryContext is a context and resource aware version of Retry. Context timeout/cancellation errors are never retried, regardless of IsRetryable. Resource exhausted error will be retried using a different throttle retry policy, instead of the specified one. TODO: allow customizing throttle retry policy and what kind of error are categorized as throttle error.

#### func [ThrottleRetryContextWithReturn](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retry.go#L107)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ThrottleRetryContextWithReturn "Go to ThrottleRetryContextWithReturn")added in v1.30.0

func ThrottleRetryContextWithReturn[T [any](https://pkg.go.dev/builtin#any)](
	ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context),
	fn func([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) (T, [error](https://pkg.go.dev/builtin#error)),
	policy [RetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryPolicy),
	isRetryable [IsRetryable](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#IsRetryable),
) (T, [error](https://pkg.go.dev/builtin#error))

ThrottleRetryContextWithReturn is a context and resource aware version of Retry. Context timeout/cancellation errors are never retried, regardless of IsRetryable. Resource exhausted error will be retried using a different throttle retry policy, instead of the specified one. TODO: allow customizing throttle retry policy and what kind of error are categorized as throttle error.

#### func [ValidateSchedule](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/cron.go#L15)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ValidateSchedule "Go to ValidateSchedule")added in v0.6.0

func ValidateSchedule(cronSchedule [string](https://pkg.go.dev/builtin#string)) [error](https://pkg.go.dev/builtin#error)

ValidateSchedule validates a cron schedule spec

### Types [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#pkg-types "Go to Types")

#### type [BackoffCalculatorAlgorithmFunc](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retry.go#L178)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#BackoffCalculatorAlgorithmFunc "Go to BackoffCalculatorAlgorithmFunc")added in v1.30.0

type BackoffCalculatorAlgorithmFunc func(duration *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration), coefficient [float64](https://pkg.go.dev/builtin#float64), currentAttempt [int32](https://pkg.go.dev/builtin#int32)) [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)

BackoffCalculatorAlgorithmFunc is a function type that calculates backoff duration based on initial duration, coefficient, and current attempt number.

#### func [MakeBackoffAlgorithm](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retry.go#L190)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#MakeBackoffAlgorithm "Go to MakeBackoffAlgorithm")added in v1.30.0

func MakeBackoffAlgorithm(requestedDelay *[time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)) [BackoffCalculatorAlgorithmFunc](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#BackoffCalculatorAlgorithmFunc)

MakeBackoffAlgorithm creates a BackoffCalculatorAlgorithmFunc that returns a fixed delay if requestedDelay is non-nil, otherwise falls back to exponential backoff algorithm.

#### type [ConstantDelayRetryPolicy](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L65)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ConstantDelayRetryPolicy "Go to ConstantDelayRetryPolicy")added in v1.25.0

type ConstantDelayRetryPolicy struct {
	// contains filtered or unexported fields
}

#### func [NewConstantDelayRetryPolicy](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L242)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#NewConstantDelayRetryPolicy "Go to NewConstantDelayRetryPolicy")added in v1.25.0

func NewConstantDelayRetryPolicy(delay [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)) *[ConstantDelayRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ConstantDelayRetryPolicy)

#### func (*ConstantDelayRetryPolicy) [ComputeNextDelay](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L260)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ConstantDelayRetryPolicy.ComputeNextDelay "Go to ConstantDelayRetryPolicy.ComputeNextDelay")added in v1.25.0

func (p *[ConstantDelayRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ConstantDelayRetryPolicy)) ComputeNextDelay(_ [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration), attempt [int](https://pkg.go.dev/builtin#int), _ [error](https://pkg.go.dev/builtin#error)) [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)

#### func (*ConstantDelayRetryPolicy) [WithJitter](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L255)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ConstantDelayRetryPolicy.WithJitter "Go to ConstantDelayRetryPolicy.WithJitter")added in v1.25.0

func (p *[ConstantDelayRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ConstantDelayRetryPolicy)) WithJitter(jitterPct [float64](https://pkg.go.dev/builtin#float64)) *[ConstantDelayRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ConstantDelayRetryPolicy)

#### func (*ConstantDelayRetryPolicy) [WithMaximumAttempts](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L250)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ConstantDelayRetryPolicy.WithMaximumAttempts "Go to ConstantDelayRetryPolicy.WithMaximumAttempts")added in v1.25.0

func (p *[ConstantDelayRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ConstantDelayRetryPolicy)) WithMaximumAttempts(maximumAttempts [int](https://pkg.go.dev/builtin#int)) *[ConstantDelayRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ConstantDelayRetryPolicy)

#### type [ErrorDependentRetryPolicy](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L59)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ErrorDependentRetryPolicy "Go to ErrorDependentRetryPolicy")added in v1.25.0

type ErrorDependentRetryPolicy struct {
	// contains filtered or unexported fields
}

ErrorDependentRetryPolicy is a policy that computes the next delay time based on the error returned by the operation. The delay time to use for a particular error is determined by the delayForError function.

#### func [NewErrorDependentRetryPolicy](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L214)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#NewErrorDependentRetryPolicy "Go to NewErrorDependentRetryPolicy")added in v1.25.0

func NewErrorDependentRetryPolicy(delayForError func(err [error](https://pkg.go.dev/builtin#error)) [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)) *[ErrorDependentRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ErrorDependentRetryPolicy)

#### func (*ErrorDependentRetryPolicy) [ComputeNextDelay](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L232)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ErrorDependentRetryPolicy.ComputeNextDelay "Go to ErrorDependentRetryPolicy.ComputeNextDelay")added in v1.25.0

func (p *[ErrorDependentRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ErrorDependentRetryPolicy)) ComputeNextDelay(_ [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration), attempt [int](https://pkg.go.dev/builtin#int), err [error](https://pkg.go.dev/builtin#error)) [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)

#### func (*ErrorDependentRetryPolicy) [WithJitter](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L227)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ErrorDependentRetryPolicy.WithJitter "Go to ErrorDependentRetryPolicy.WithJitter")added in v1.25.0

func (p *[ErrorDependentRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ErrorDependentRetryPolicy)) WithJitter(jitterPct [float64](https://pkg.go.dev/builtin#float64)) *[ErrorDependentRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ErrorDependentRetryPolicy)

#### func (*ErrorDependentRetryPolicy) [WithMaximumAttempts](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L222)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ErrorDependentRetryPolicy.WithMaximumAttempts "Go to ErrorDependentRetryPolicy.WithMaximumAttempts")added in v1.25.0

func (p *[ErrorDependentRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ErrorDependentRetryPolicy)) WithMaximumAttempts(maximumAttempts [int](https://pkg.go.dev/builtin#int)) *[ErrorDependentRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ErrorDependentRetryPolicy)

#### type [ExponentialRetryPolicy](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L49)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy "Go to ExponentialRetryPolicy")

type ExponentialRetryPolicy struct {
	// contains filtered or unexported fields
}

ExponentialRetryPolicy provides the implementation for retry policy using a coefficient to compute the next delay. Formula used to compute the next delay is:

min(initialInterval * pow(backoffCoefficient, currentAttempt), maximumInterval)

#### func [NewExponentialRetryPolicy](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L82)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#NewExponentialRetryPolicy "Go to NewExponentialRetryPolicy")

func NewExponentialRetryPolicy(initialInterval [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)) *[ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy)

NewExponentialRetryPolicy returns an instance of ExponentialRetryPolicy using the provided initialInterval

#### func (*ExponentialRetryPolicy) [ComputeNextDelay](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L141)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy.ComputeNextDelay "Go to ExponentialRetryPolicy.ComputeNextDelay")

func (p *[ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy)) ComputeNextDelay(elapsedTime [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration), numAttempts [int](https://pkg.go.dev/builtin#int), _ [error](https://pkg.go.dev/builtin#error)) [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)

ComputeNextDelay returns the next delay interval. This is used by Retrier to delay calling the operation again

#### func (*ExponentialRetryPolicy) [WithBackoffCoefficient](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L115)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy.WithBackoffCoefficient "Go to ExponentialRetryPolicy.WithBackoffCoefficient")added in v1.17.3

func (p *[ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy)) WithBackoffCoefficient(backoffCoefficient [float64](https://pkg.go.dev/builtin#float64)) *[ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy)

WithBackoffCoefficient sets the coefficient used by ExponentialRetryPolicy to compute next delay for each retry All retries are computed using the following formula: initialInterval * math.Pow(backoffCoefficient, currentAttempt)

#### func (*ExponentialRetryPolicy) [WithExpirationInterval](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L129)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy.WithExpirationInterval "Go to ExponentialRetryPolicy.WithExpirationInterval")added in v1.17.3

func (p *[ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy)) WithExpirationInterval(expirationInterval [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)) *[ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy)

WithExpirationInterval sets the absolute expiration interval for all retries

#### func (*ExponentialRetryPolicy) [WithInitialInterval](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L107)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy.WithInitialInterval "Go to ExponentialRetryPolicy.WithInitialInterval")added in v1.17.3

func (p *[ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy)) WithInitialInterval(initialInterval [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)) *[ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy)

WithInitialInterval sets the initial interval used by ExponentialRetryPolicy for the very first retry All later retries are computed using the following formula: initialInterval * math.Pow(backoffCoefficient, currentAttempt)

#### func (*ExponentialRetryPolicy) [WithMaximumAttempts](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L135)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy.WithMaximumAttempts "Go to ExponentialRetryPolicy.WithMaximumAttempts")added in v1.17.3

func (p *[ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy)) WithMaximumAttempts(maximumAttempts [int](https://pkg.go.dev/builtin#int)) *[ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy)

WithMaximumAttempts sets the maximum number of retry attempts

#### func (*ExponentialRetryPolicy) [WithMaximumInterval](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L123)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy.WithMaximumInterval "Go to ExponentialRetryPolicy.WithMaximumInterval")added in v1.17.3

func (p *[ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy)) WithMaximumInterval(maximumInterval [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)) *[ExponentialRetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#ExponentialRetryPolicy)

WithMaximumInterval sets the maximum interval for each retry. This does *not* cause the policy to stop retrying when the interval between retries reaches the supplied duration. That is what WithExpirationInterval does. Instead, this prevents the interval from exceeding maximumInterval.

Example [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#example-ExponentialRetryPolicy.WithMaximumInterval "Go to Example")

ExampleExponentialRetryPolicy_WithMaximumInterval demonstrates example delays with a backoff coefficient of 2 and a maximum interval of 10 seconds. Keep in mind that there is a random jitter in these times, so they are not exactly what you'd expect.

Output:

Attempt | Delay| Capped Delay 0 | 0.0s| 0.0s 1 | 0.8s| 0.9s 2 | 1.7s| 1.6s 3 | 3.3s| 3.2s 4 | 7.2s| 7.2s 5 | 15.1s| 9.6s 6 | 26.2s| 8.8s 7 | 62.8s| 9.4s 8 | 112.8s| 9.5s 9 | 219.7s| 8.3s 

#### type [IsRetryable](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retry.go#L35)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#IsRetryable "Go to IsRetryable")

type IsRetryable func([error](https://pkg.go.dev/builtin#error)) [bool](https://pkg.go.dev/builtin#bool)

IsRetryable handler can be used to exclude certain errors during retry

#### type [Operation](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retry.go#L28)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#Operation "Go to Operation")

type Operation func() [error](https://pkg.go.dev/builtin#error)

Operation to retry

#### type [OperationCtx](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retry.go#L32)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#OperationCtx "Go to OperationCtx")added in v1.12.1

type OperationCtx func([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) [error](https://pkg.go.dev/builtin#error)

OperationCtx plays the same role as Operation but for context-aware retryable functions.

#### type [Retrier](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L41)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#Retrier "Go to Retrier")

type Retrier interface {
 NextBackOff(err [error](https://pkg.go.dev/builtin#error)) [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) Reset() }

Retrier manages the state of retry operation

#### func [NewRetrier](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L95)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#NewRetrier "Go to NewRetrier")

func NewRetrier(policy [RetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryPolicy), timeSource [clock](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock).[TimeSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/clock#TimeSource)) [Retrier](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#Retrier)

NewRetrier is used for creating a new instance of Retrier

#### type [RetryLockedSource](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L300)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryLockedSource "Go to RetryLockedSource")added in v1.28.0

type RetryLockedSource struct {
	// contains filtered or unexported fields
}

#### func [NewRetryLockedSource](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L315)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#NewRetryLockedSource "Go to NewRetryLockedSource")added in v1.28.0

func NewRetryLockedSource() *[RetryLockedSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryLockedSource)

#### func (*RetryLockedSource) [Int63](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L305)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryLockedSource.Int63 "Go to RetryLockedSource.Int63")added in v1.28.0

func (r *[RetryLockedSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryLockedSource)) Int63() [int64](https://pkg.go.dev/builtin#int64)

#### func (*RetryLockedSource) [Seed](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L311)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryLockedSource.Seed "Go to RetryLockedSource.Seed")added in v1.28.0

func (r *[RetryLockedSource](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryLockedSource)) Seed(seed [int64](https://pkg.go.dev/builtin#int64))

#### type [RetryPolicy](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go#L36)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryPolicy "Go to RetryPolicy")

type RetryPolicy interface {
 ComputeNextDelay(elapsedTime [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration), numAttempts [int](https://pkg.go.dev/builtin#int), err [error](https://pkg.go.dev/builtin#error)) [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)}

RetryPolicy is the API which needs to be implemented by various retry policy implementations

var (
// DisabledRetryPolicy is a retry policy that never retries	DisabledRetryPolicy [RetryPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#RetryPolicy) = &disabledRetryPolicyImpl{}
)

![Image 44](https://pkg.go.dev/static/shared/icon/insert_drive_file_gm_grey_24dp.svg) Source Files [¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/backoff#section-sourcefiles "Go to Source Files")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[View all Source files](https://github.com/temporalio/temporal/tree/v1.30.0/common/backoff)

*   [cron.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/cron.go "cron.go")
*   [jitter.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/jitter.go "jitter.go")
*   [retry.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retry.go "retry.go")
*   [retrypolicy.go](https://github.com/temporalio/temporal/blob/v1.30.0/common/backoff/retrypolicy.go "retrypolicy.go")

 Click to show internal directories. 

 Click to hide internal directories. 

[Why Go](https://go.dev/solutions)[Use Cases](https://go.dev/solutions#use-cases)[Case Studies](https://go.dev/solutions#case-studies)

[Get Started](https://learn.go.dev/)[Playground](https://play.golang.org/)[Tour](https://tour.golang.org/)[Stack Overflow](https://stackoverflow.com/questions/tagged/go?tab=Newest)[Help](https://go.dev/help)

[Packages](https://pkg.go.dev/)[Standard Library](https://pkg.go.dev/std)[Sub-repositories](https://pkg.go.dev/golang.org/x)[About Go Packages](https://pkg.go.dev/about)

[About](https://go.dev/project)[Download](https://go.dev/dl/)[Blog](https://go.dev/blog)[Issue Tracker](https://github.com/golang/go/issues)[Release Notes](https://go.dev/doc/devel/release.html)[Brand Guidelines](https://go.dev/brand)[Code of Conduct](https://go.dev/conduct)

[Connect](https://www.twitter.com/golang)[Twitter](https://www.twitter.com/golang)[GitHub](https://github.com/golang)[Slack](https://invite.slack.golangbridge.org/)[r/golang](https://reddit.com/r/golang)[Meetup](https://www.meetup.com/pro/go)[Golang Weekly](https://golangweekly.com/)

![Image 45: Gopher in flight goggles](https://pkg.go.dev/static/shared/gopher/pilot-bust-1431x901.svg)
*   [Copyright](https://go.dev/copyright)
*   [Terms of Service](https://go.dev/tos)
*   [Privacy Policy](http://www.google.com/intl/en/policies/privacy/)
*   [Report an Issue](https://go.dev/s/pkgsite-feedback)
*   ![Image 46: System theme](https://pkg.go.dev/static/shared/icon/brightness_6_gm_grey_24dp.svg)![Image 47: Dark theme](https://pkg.go.dev/static/shared/icon/brightness_2_gm_grey_24dp.svg)![Image 48: Light theme](https://pkg.go.dev/static/shared/icon/light_mode_gm_grey_24dp.svg)
Theme Toggle

*   ![Image 49](https://pkg.go.dev/static/shared/icon/keyboard_grey_24dp.svg)
Shortcuts Modal

[![Image 50: Google logo](https://pkg.go.dev/static/shared/logo/google-white.svg)](https://google.com/)

Jump to
-------

![Image 51](https://pkg.go.dev/static/shared/icon/close_gm_grey_24dp.svg)

Close

Keyboard shortcuts
------------------

![Image 52](https://pkg.go.dev/static/shared/icon/close_gm_grey_24dp.svg)

**?**: This menu
**/**: Search site
**f** or **F**: Jump to
**y** or **Y**: Canonical URL

Close

go.dev uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay
