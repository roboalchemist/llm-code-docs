# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier/internal/fftpack

Title: fftpack package - gonum.org/v1/gonum/dsp/fourier/internal/fftpack - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier/internal/fftpack

Markdown Content:
Package fftpack implements Discrete Fourier Transform functions ported from the Fortran implementation of FFTPACK.

*   [func Cfftb(n int, c, work []float64, ifac []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier/internal/fftpack#Cfftb)
*   [func Cfftf(n int, r, work []float64, ifac []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier/internal/fftpack#Cfftf)
*   [func Cffti(n int, work []float64, ifac []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier/internal/fftpack#Cffti)
*   [func Cosqb(n int, x, work []float64, ifac []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier/internal/fftpack#Cosqb)
*   [func Cosqf(n int, x, work []float64, ifac []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier/internal/fftpack#Cosqf)
*   [func Cosqi(n int, work []float64, ifac []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier/internal/fftpack#Cosqi)
*   [func Cost(n int, x, work []float64, ifac []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier/internal/fftpack#Cost)
*   [func Costi(n int, work []float64, ifac []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier/internal/fftpack#Costi)
*   [func Rfftb(n int, r, work []float64, ifac []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier/internal/fftpack#Rfftb)
*   [func Rfftf(n int, r, work []float64, ifac []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier/internal/fftpack#Rfftf)
*   [func Rffti(n int, work []float64, ifac []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier/internal/fftpack#Rffti)
*   [func Sinqb(n int, x, work []float64, ifac []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier/internal/fftpack#Sinqb)
*   [func Sinqf(n int, x, work []float64, ifac []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier/internal/fftpack#Sinqf)
*   [func Sinqi(n int, work []float64, ifac []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier/internal/fftpack#Sinqi)
*   [func Sint(n int, x, work []float64, ifac []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier/internal/fftpack#Sint)
*   [func Sinti(n int, work []float64, ifac []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier/internal/fftpack#Sinti)

This section is empty.

This section is empty.

Cfftb computes the backward complex Discrete Fourier Transform (the Fourier synthesis). Equivalently, Cfftf computes the computes a complex periodic sequence from its Fourier coefficients. The transform is defined below at output parameter c.

Input parameters:

n      The length of the array c to be transformed. The method
       is most efficient when n is a product of small primes.
       n may change so long as different work arrays are provided.

c      A complex array of length n which contains the sequence
       to be transformed.

work   A real work array which must be dimensioned at least 4*n.
       in the program that calls Cfftb. The work array must be
       initialized by calling subroutine Cffti(n,work,ifac) and a
       different work array must be used for each different
       value of n. This initialization does not have to be
       repeated so long as n remains unchanged thus subsequent
       transforms can be obtained faster than the first.
       The same work array can be used by Cfftf and Cfftb.

ifac   A work array containing the factors of n. ifac must have
       length of at least 15.

Output parameters:

c      for j=0, ..., n-1
         c[j]=the sum from k=0, ..., n-1 of
           c[k]*exp(i*j*k*2*pi/n)

       where i=sqrt(-1)

This transform is unnormalized since a call of Cfftf
followed by a call of Cfftb will multiply the input
sequence by n.

The n elements of c are represented in n pairs of real
values in r where c[j] = r[j*2]+r[j*2+1]i.

work   Contains results which must not be destroyed between
       calls of Cfftf or Cfftb.
ifac   Contains results which must not be destroyed between
       calls of Cfftf or Cfftb.

Cfftf computes the forward complex Discrete Fourier transform (the Fourier analysis). Equivalently, Cfftf computes the Fourier coefficients of a complex periodic sequence. The transform is defined below at output parameter c.

Input parameters:

n      The length of the array c to be transformed. The method
       is most efficient when n is a product of small primes.
       n may change so long as different work arrays are provided.

c      A complex array of length n which contains the sequence
       to be transformed.

work   A real work array which must be dimensioned at least 4*n.
       in the program that calls Cfftf. The work array must be
       initialized by calling subroutine Cffti(n,work,ifac) and a
       different work array must be used for each different
       value of n. This initialization does not have to be
       repeated so long as n remains unchanged thus subsequent
       transforms can be obtained faster than the first.
       the same work array can be used by Cfftf and Cfftb.

ifac   A work array containing the factors of n. ifac must have
       length of at least 15.

Output parameters:

 c     for j=0, ..., n-1
         c[j]=the sum from k=0, ..., n-1 of
           c[k]*exp(-i*j*k*2*pi/n)

       where i=sqrt(-1)

This transform is unnormalized since a call of Cfftf
followed by a call of Cfftb will multiply the input
sequence by n.

The n elements of c are represented in n pairs of real
values in r where c[j] = r[j*2]+r[j*2+1]i.

work   Contains results which must not be destroyed between
       calls of Cfftf or Cfftb.
ifac   Contains results which must not be destroyed between
       calls of Cfftf or Cfftb.

Cffti initializes the array work which is used in both Cfftf and Cfftb. the prime factorization of n together with a tabulation of the trigonometric functions are computed and stored in work.

Input parameter:

n      The length of the sequence to be transformed.

Output parameters:

work   A work array which must be dimensioned at least 4*n.
       the same work array can be used for both Cfftf and Cfftb
       as long as n remains unchanged. Different work arrays
       are required for different values of n. The contents of
       work must not be changed between calls of Cfftf or Cfftb.

ifac   A work array containing the factors of n. ifac must have
       length 15.

Cosqb computes the Fast Fourier Transform of quarter wave data. That is, Cosqb computes a sequence from its representation in terms of a cosine series with odd wave numbers. The transform is defined below at output parameter x.

Cosqf is the unnormalized inverse of Cosqb since a call of Cosqb followed by a call of Cosqf will multiply the input sequence x by 4*n.

The array work which is used by subroutine Cosqb must be initialized by calling subroutine Cosqi(n,work).

Input parameters:

n       The length of the array x to be transformed. The method
        is most efficient when n is a product of small primes.

x       An array which contains the sequence to be transformed.

work    A work array which must be dimensioned at least 3*n
        in the program that calls Cosqb. The work array must be
        initialized by calling subroutine Cosqi(n,work) and a
        different work array must be used for each different
        value of n. This initialization does not have to be
        repeated so long as n remains unchanged thus subsequent
        transforms can be obtained faster than the first.

ifac    An integer work array of length at least 15.

Output parameters:

x       for i=0, ..., n-1
          x[i]= the sum from k=0 to k=n-1 of
            4*x[k]*cos((2*k+1)*i*pi/(2*n))

        A call of Cosqb followed by a call of
        Cosqf will multiply the sequence x by 4*n.
        Therefore Cosqf is the unnormalized inverse
        of Cosqb.

work    Contains initialization calculations which must not
        be destroyed between calls of Cosqb or Cosqf.

Cosqf computes the Fast Fourier Transform of quarter wave data. That is, Cosqf computes the coefficients in a cosine series representation with only odd wave numbers. The transform is defined below at output parameter x.

Cosqb is the unnormalized inverse of Cosqf since a call of Cosqf followed by a call of Cosqb will multiply the input sequence x by 4*n.

The array work which is used by subroutine Cosqf must be initialized by calling subroutine Cosqi(n,work).

Input parameters:

n       The length of the array x to be transformed. The method
        is most efficient when n is a product of small primes.

x       An array which contains the sequence to be transformed.

work    A work array which must be dimensioned at least 3*n
        in the program that calls Cosqf. The work array must be
        initialized by calling subroutine Cosqi(n,work) and a
        different work array must be used for each different
        value of n. This initialization does not have to be
        repeated so long as n remains unchanged thus subsequent
        transforms can be obtained faster than the first.

ifac    An integer work array of length at least 15.

Output parameters:

x       for i=0, ..., n-1
          x[i] = x[i] + the sum from k=0 to k=n-2 of
              2*x[k]*cos((2*i+1)*k*pi/(2*n))

        A call of Cosqf followed by a call of
        Cosqb will multiply the sequence x by 4*n.
        Therefore Cosqb is the unnormalized inverse
        of Cosqf.

work    Contains initialization calculations which must not
        be destroyed between calls of Cosqf or Cosqb.

Cosqi initializes the array work which is used in both Cosqf and Cosqb. The prime factorization of n together with a tabulation of the trigonometric functions are computed and stored in work.

Input parameter:

n       The length of the sequence to be transformed. the method
        is most efficient when n+1 is a product of small primes.

Output parameters:

work    A work array which must be dimensioned at least 3*n.
        The same work array can be used for both Cosqf and Cosqb
        as long as n remains unchanged. Different work arrays
        are required for different values of n. The contents of
        work must not be changed between calls of Cosqf or Cosqb.

ifac    An integer work array of length at least 15.

Cost computes the Discrete Fourier Cosine Transform of an even sequence x(i). The transform is defined below at output parameter x.

Cost is the unnormalized inverse of itself since a call of Cost followed by another call of Cost will multiply the input sequence x by 2*(n-1). The transform is defined below at output parameter x

The array work which is used by subroutine Cost must be initialized by calling subroutine Costi(n,work).

Input parameters:

n       The length of the sequence x. n must be greater than 1.
        The method is most efficient when n-1 is a product of
        small primes.

x       An array which contains the sequence to be transformed.

work    A work array which must be dimensioned at least 3*n
        in the program that calls Cost. The work array must be
        initialized by calling subroutine Costi(n,work) and a
        different work array must be used for each different
        value of n. This initialization does not have to be
        repeated so long as n remains unchanged thus subsequent
        transforms can be obtained faster than the first.

ifac    An integer work array of length at least 15.

Output parameters:

x       for i=1,...,n
          x(i) = x(1)+(-1)**(i-1)*x(n)
            + the sum from k=2 to k=n-1
              2*x(k)*cos((k-1)*(i-1)*pi/(n-1))

        A call of Cost followed by another call of
        Cost will multiply the sequence x by 2*(n-1).
        Hence Cost is the unnormalized inverse
        of itself.

work    Contains initialization calculations which must not be
        destroyed between calls of Cost.

ifac    An integer work array of length at least 15.

Costi initializes the array work which is used in subroutine Cost. The prime factorization of n together with a tabulation of the trigonometric functions are computed and stored in work.

Input parameter:

n       The length of the sequence to be transformed. The method
        is most efficient when n-1 is a product of small primes.

Output parameters:

work    A work array which must be dimensioned at least 3*n.
        Different work arrays are required for different values
        of n. The contents of work must not be changed between
        calls of Cost.

ifac    An integer work array of length at least 15.

Rfftb computes the real perodic sequence from its Fourier coefficients (Fourier synthesis). The transform is defined below at output parameter r.

Input parameters

n      The length of the array r to be transformed. The method
       is most efficient when n is a product of small primes.
       n may change so long as different work arrays are provided.

r      A real array of length n which contains the sequence
       to be transformed.

work   A work array which must be dimensioned at least 2*n.
       in the program that calls Rfftb. The work array must be
       initialized by calling subroutine rffti(n,work,ifac) and a
       different work array must be used for each different
       value of n. This initialization does not have to be
       repeated so long as n remains unchanged thus subsequent
       transforms can be obtained faster than the first.
       The same work array can be used by Rfftf and Rfftb.

ifac   A work array containing the factors of n. ifac must have
       length of at least 15.

output parameters

r      for n even and for i = 0, ..., n
         r[i] = r[0]+(-1)^i*r[n-1]
           plus the sum from k=1 to k=n/2-1 of
             2*r(2*k-1)*cos(k*i*2*pi/n)
             -2*r(2*k)*sin(k*i*2*pi/n)

       for n odd and for i = 0, ..., n-1
         r[i] = r[0] plus the sum from k=1 to k=(n-1)/2 of
           2*r(2*k-1)*cos(k*i*2*pi/n)
           -2*r(2*k)*sin(k*i*2*pi/n)

This transform is unnormalized since a call of Rfftf
followed by a call of Rfftb will multiply the input
sequence by n.

work   Contains results which must not be destroyed between
       calls of Rfftf or Rfftb.
ifac   Contains results which must not be destroyed between
       calls of Rfftf or Rfftb.

Rfftf computes the Fourier coefficients of a real perodic sequence (Fourier analysis). The transform is defined below at output parameter r.

Input parameters:

n      The length of the array r to be transformed. The method
       is most efficient when n is a product of small primes.
       n may change so long as different work arrays are provided.

r      A real array of length n which contains the sequence
       to be transformed.

work   a work array which must be dimensioned at least 2*n.
       in the program that calls Rfftf. the work array must be
       initialized by calling subroutine rffti(n,work,ifac) and a
       different work array must be used for each different
       value of n. This initialization does not have to be
       repeated so long as n remains unchanged. Thus subsequent
       transforms can be obtained faster than the first.
       The same work array can be used by Rfftf and Rfftb.

ifac   A work array containing the factors of n. ifac must have
       length of at least 15.

Output parameters:

r      r[0] = the sum from i=0 to i=n-1 of r[i]

       if n is even set l=n/2, if n is odd set l = (n+1)/2
         then for k = 1, ..., l-1
           r[2*k-1] = the sum from i = 0 to i = n-1 of
             r[i]*cos(k*i*2*pi/n)
           r[2*k] = the sum from i = 0 to i = n-1 of
             -r[i]*sin(k*i*2*pi/n)

       if n is even
         r[n-1] = the sum from i = 0 to i = n-1 of
           (-1)^i*r[i]

This transform is unnormalized since a call of Rfftf
followed by a call of Rfftb will multiply the input
sequence by n.

work   contains results which must not be destroyed between
       calls of Rfftf or Rfftb.
ifac   contains results which must not be destroyed between
       calls of Rfftf or Rfftb.

Rffti initializes the array work which is used in both Rfftf and Rfftb. The prime factorization of n together with a tabulation of the trigonometric functions are computed and stored in work.

Input parameter:

n      The length of the sequence to be transformed.

Output parameters:

work   A work array which must be dimensioned at least 2*n.
       The same work array can be used for both Rfftf and Rfftb
       as long as n remains unchanged. different work arrays
       are required for different values of n. The contents of
       work must not be changed between calls of Rfftf or Rfftb.

ifac   A work array containing the factors of n. ifac must have
       length of at least 15.

Sinqb computes the Fast Fourier Transform of quarter wave data. That is, Sinqb computes a sequence from its representation in terms of a sine series with odd wave numbers. The transform is defined below at output parameter x.

Sinqf is the unnormalized inverse of Sinqb since a call of Sinqb followed by a call of Sinqf will multiply the input sequence x by 4*n.

The array work which is used by subroutine Sinqb must be initialized by calling subroutine Sinqi(n,work).

Input parameters:

n       The length of the array x to be transformed. The method
        is most efficient when n is a product of small primes.

x       An array which contains the sequence to be transformed.

work    A work array which must be dimensioned at least 3*n.
        in the program that calls Sinqb. The work array must be
        initialized by calling subroutine Sinqi(n,work) and a
        different work array must be used for each different
        value of n. This initialization does not have to be
        repeated so long as n remains unchanged thus subsequent
        transforms can be obtained faster than the first.

ifac    An integer work array of length at least 15.

Output parameters:

x       for i=0, ..., n-1
          x[i]= the sum from k=0 to k=n-1 of
            4*x[k]*sin((2*k+1)*i*pi/(2*n))

        A call of Sinqb followed by a call of
        Sinqf will multiply the sequence x by 4*n.
        Therefore Sinqf is the unnormalized inverse
        of Sinqb.

work    Contains initialization calculations which must not
        be destroyed between calls of Sinqb or Sinqf.

Sinqf computes the Fast Fourier Transform of quarter wave data. That is, Sinqf computes the coefficients in a sine series representation with only odd wave numbers. The transform is defined below at output parameter x.

Sinqb is the unnormalized inverse of Sinqf since a call of Sinqf followed by a call of Sinqb will multiply the input sequence x by 4*n.

The array work which is used by subroutine Sinqf must be initialized by calling subroutine Sinqi(n,work).

Input parameters:

n       The length of the array x to be transformed. The method
        is most efficient when n is a product of small primes.

x       An array which contains the sequence to be transformed.

work    A work array which must be dimensioned at least 3*n.
        in the program that calls Sinqf. The work array must be
        initialized by calling subroutine Sinqi(n,work) and a
        different work array must be used for each different
        value of n. This initialization does not have to be
        repeated so long as n remains unchanged thus subsequent
        transforms can be obtained faster than the first.

ifac    An integer work array of length at least 15.

Output parameters:

x       for i=0, ..., n-1
          x[i] = (-1)^(i)*x[n-1]
            + the sum from k=0 to k=n-2 of
              2*x[k]*sin((2*i+1)*k*pi/(2*n))

        A call of Sinqf followed by a call of
        Sinqb will multiply the sequence x by 4*n.
        Therefore Sinqb is the unnormalized inverse
        of Sinqf.

work    Contains initialization calculations which must not
        be destroyed between calls of Sinqf or Sinqb.

Sinqi initializes the array work which is used in both Sinqf and Sinqb. The prime factorization of n together with a tabulation of the trigonometric functions are computed and stored in work.

Input parameter:

n       The length of the sequence to be transformed. The method
        is most efficient when n+1 is a product of small primes.

Output parameter:

work    A work array which must be dimensioned at least 3*n.
        The same work array can be used for both Sinqf and Sinqb
        as long as n remains unchanged. Different work arrays
        are required for different values of n. The contents of
        work must not be changed between calls of Sinqf or Sinqb.

ifac    An integer work array of length at least 15.

Sint computes the Discrete Fourier Sine Transform of an odd sequence x(i). The transform is defined below at output parameter x.

Sint is the unnormalized inverse of itself since a call of Sint followed by another call of Sint will multiply the input sequence x by 2*(n+1).

The array work which is used by subroutine Sint must be initialized by calling subroutine Sinti(n,work).

Input parameters:

n       The length of the sequence to be transformed. The method
        is most efficient when n+1 is the product of small primes.

x       An array which contains the sequence to be transformed.

work    A work array with dimension at least ceil(2.5*n)
        in the program that calls Sint. The work array must be
        initialized by calling subroutine Sinti(n,work) and a
        different work array must be used for each different
        value of n. This initialization does not have to be
        repeated so long as n remains unchanged thus subsequent
        transforms can be obtained faster than the first.

ifac    An integer work array of length at least 15.

Output parameters:

x       for i=1,...,n
          x(i)= the sum from k=1 to k=n
            2*x(k)*sin(k*i*pi/(n+1))

        A call of Sint followed by another call of
        Sint will multiply the sequence x by 2*(n+1).
        Hence Sint is the unnormalized inverse
        of itself.

work    Contains initialization calculations which must not be
        destroyed between calls of Sint.
ifac    Contains initialization calculations which must not be
        destroyed between calls of Sint.

Sinti initializes the array work which is used in subroutine Sint. The prime factorization of n together with a tabulation of the trigonometric functions are computed and stored in work.

Input parameter:

n       The length of the sequence to be transformed. The method
        is most efficient when n+1 is a product of small primes.

Output parameter:

work    A work array with at least ceil(2.5*n) locations.
        Different work arrays are required for different values
        of n. The contents of work must not be changed between
        calls of Sint.

ifac    An integer work array of length at least 15.

This section is empty.
