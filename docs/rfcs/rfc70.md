---
title: "The padding on a message is a string of the form 10*.  For Hosts with"
---

# 2. If the divisor is a small power of 2, say 2  for j < n-1, it will

not generate n distinct remainders; if the divisor is a larger power of
n-1     n
2, the correspondence table is either 2    or 2  in length.  We can

thus rule out zero as a remainder value, so the divisor must be at

least one more than the word length.  This bound is in fact achieved

for some word lengths.

Let R(p) be the number of distinct remainders p generates when divided
into successively higher powers of 2.  The distinct remainders all occur
for the R(p) lowest powers of 2.  Only odd p are interesting and the
following table gives R(p) for odd p between 1 and 21.

p     R(p)                                p     R(p)

1      1                                 13     12

3      2                                 15      4

5      4                                 17      8

7      3                                 19     18

9      6                                 21      6

This table shows that 7, 15, 17 and 21 are useless divisors because
there are smaller divisors which generate a larger number of distinct
remainders.  If we limit our attention to p such that p > p' =>
R(p) > R(p'), we obtain the following table of useful divisors for
p < 100.

Network Working Group      A Note on Padding                      RFC 70

p     R(p)                                p     R(p)

1      1                                 29     28

3      2                                 37     36

5      4                                 53     52

9      6                                 59     58

11     10                                61     60

13     12                                67     66

19     18                                83     82

Notice that 9 and 25 are useful divisors even though they generate only
6 and 20 remainders, respectively.

Determination of R(p)

If p is odd, the remainders

mod(2 ,p)
mod(2 ,p)

.
.
.
t
will be between 1 and p-1 inclusive.  At some power of 2, say 2 , there
k    t
will be a repeated remainder, so that for some k < t, 2  = 2  mod p.
t+1    k+1
Since 2    = 2    mod p
t+2    k+2
and   2    = 2    mod p

.
.
.
etc.

# 0. t-1

all of the distinct remainders occur for 2 ...2   .  Therefore, R(p)=t.

Network Working Group      A Note on Padding                      RFC 70

Next we show that

R(p)
2     = 1 mod p
R(p)    k
We already know that 2     = 2  mod p

for some 0<=k<R(p).  Let j=R(p)-k so 0<j<=R(p).  Then

k+j           k
2           = 2  mod p
j  k          k
or   2 *2        = 2  mod p
j     k
or   (2 -1)*2    =  0 mod p
k                                     j
Now p does not divide 2  because p is odd, so p must divide 2 -1.  Thus

j
2 -1        =  0 mod p
j
2           =  1 mod p

Since j is greater than 0 by hypothesis and since ther is no k other
than 0 less than R(p) such that

k    0
2  = 2  mod p,

R(p)
we must have j=R(p), or 2     = 1 mod p.
k
We have thus shown that for odd p, the remainders mod(2 ,p) are unique
for k = 0, 1,..., R(p)-1 and then repeat exactly, beginning with

R(p)
2     = 1 mod p.

We now consider even p.  Let

q
p = p'*2 ,
k                     k          k
where p' is odd.  For k<q, mod(2 ,p) is clearly just 2  because 2 <p.

For k>=q,
k       q      k-q
mod(2 ,p) = 2 *mod(2   ,p').

Network Working Group      A Note on Padding                      RFC 70

From this we can see that the sequence of remainders will have an
q-1
initial segment of 1, 2, ...2    of length q, and repeating segments of

length R(p').  Therefore, R(p) = q+R(p').  Since we normally expect

R(p) ~ p,

even p generally will not be useful.

I don't know of a direct way of choosing a p for a given n, but the
previous table was generated from the following Fortran program run
under the SEX system at UCLA.

CALL IASSGN('OC ',56)
1       FORMAT(I3,I5)

```
                    M=0
                    DO 100 K=1,100,2
                    K=1
                    L=0
            20      L=L+1
                    N=MOD(2*N,K)
                    IF(N.GT.1) GO TO 20
                    IF(L.LE.M) GO TO 100
                    M=L
                    WRITE(56,1)K,L
            100     CONTINUE
                    STOP
                    END

      Fortran program to computer useful divisors

```

In the program, K takes on trial values of p, N takes on the values of
the successive remainders, L counts up to R(p), and M remembers the
previous largest R(p).  Execution is quite speedy.

Network Working Group      A Note on Padding                      RFC 70

Results from Number Theory

The quantity referred to above as R(p) is usually written Ord 2 and is
p
read "the order of 2 mod p".  The maximum value of Ord 2 is given by
p
Euler's phi-function, sometimes called the totient.  The totient of a

positive integer p is the number of integers less than p which are

relatively prime to p.  The totient is easy to compute from a

representation of p as a product of primes:

n      n        n
Let p = p  1 * p  2 ... p  k
1      2        k

where the p  are distinct primes.  Then
i
k -1               k -1                 k -1
phi(p) = (p - 1) * p  1   * (p - 1) * p  2   ... (p - 1) * p  k
1        1         2        2           k        k

If p is prime, the totient of p is simply

phi(p) = p-1.

If p is not prime, the totient is smaller.

If a is relatively prime to p, then Euler's generalization of Fermat's
theorem states

phi(m)
a       = 1 mod p.

It is this theorem which places an upper bound Ord 2, because Ord 2 is
p              p
the smallest value such that

Ord 2
2   p  = 1 mod p

Moreover it is always true that phi(p) is divisible by Ord 2.
p

Network Working Group      A Note on Padding                      RFC 70

# Acknowledgements

Bob Kahn read an early draft and made many comments which improved the
exposition.  Alex Hurwitz assured me that a search technique is
necessary to compute R(p), and supplied the names for the quantities
and theorems I uncovered.

[ This RFC was put into machine readable form for entry ]
[ into the online RFC archives by Guillaume Lahaye and  ]
[ John Hewes 6/97 ]
