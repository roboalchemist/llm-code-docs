# Source: https://docs.wiremock.io/delays.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Response Delays

> Adding delays to stub responses

Calls over a network to an API can be delayed for many reasons e.g. network congestion or excessive server load. For applications
to be resilient they must be designed to cope with this inevitable variability, and tested to ensure they behave as expected
when conditions aren't optimal.

In particular it is important to check that timeouts work as configured, and that your end user's experience is maintained.

WireMock Cloud stubs can be served with a fixed or random delay, or can be "dribbled" back in chunks over a defined time period.

## Fixed delay

A fixed delay straightforwardly adds a pause for the specified number of milliseconds before serving the stub's response.

<img src="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/fixed-delay.png?fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=3383378c11bb976a18ceef3b58f7234e" title="Fixed delay" width="50%" data-og-width="327" data-og-height="155" data-path="images/screenshots/fixed-delay.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/fixed-delay.png?w=280&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=b3a9907d385e179369a8c353ee920faf 280w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/fixed-delay.png?w=560&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=b2ddc1236417c9106a6405871c503a56 560w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/fixed-delay.png?w=840&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=892987277d2c8c7c2a3921af3624027d 840w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/fixed-delay.png?w=1100&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=1fd9cebaf8a8cec193c32cc6378cc930 1100w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/fixed-delay.png?w=1650&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=b0e03ba1e6039352d5a44fa36b927528 1650w, https://mintcdn.com/wiremockinc/m5hvbZSijetQGAV3/images/screenshots/fixed-delay.png?w=2500&fit=max&auto=format&n=m5hvbZSijetQGAV3&q=85&s=ed7a18114bb3f0a10fe0753370720a83 2500w" />

## Random delay

Random delay adds a random pause before serving the response. Two statistical distributions are available:

### Uniform

<img src="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/random-uniform-delay.png?fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=bf5593c2daf7a8b629bffe73c5d843aa" title="Random uniform delay" width="50%" data-og-width="496" data-og-height="157" data-path="images/screenshots/random-uniform-delay.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/random-uniform-delay.png?w=280&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=fd19b20bef1363b9412d2be9367a0864 280w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/random-uniform-delay.png?w=560&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=576e46bc37f8c388b70445efd82565a3 560w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/random-uniform-delay.png?w=840&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=7b8180a1abd49663a3aae3e294a103dc 840w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/random-uniform-delay.png?w=1100&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=1942f9f9e48cbfdba128cb9251d89fed 1100w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/random-uniform-delay.png?w=1650&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=0b45b366ce98841c14fc10b0896bc85d 1650w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/random-uniform-delay.png?w=2500&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=d8e5b59c906e8af1cbaf421436992811 2500w" />

### Log normal

<img src="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/random-lognormal-delay.png?fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=293272cba3883c23a3b8f4695fe16c0a" title="Random lognormal delay" width="50%" data-og-width="500" data-og-height="158" data-path="images/screenshots/random-lognormal-delay.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/random-lognormal-delay.png?w=280&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=3ea4b3757e5023b83dbe144177f5c9db 280w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/random-lognormal-delay.png?w=560&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=d43fa28cdb247e50e676d4593cbc5912 560w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/random-lognormal-delay.png?w=840&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=eee2e7057d13946da8c205b5550672a2 840w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/random-lognormal-delay.png?w=1100&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=b889c1996793dc336ceedaebc8e5ebd6 1100w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/random-lognormal-delay.png?w=1650&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=ec1993009a2749d579792dbe559190e6 1650w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/random-lognormal-delay.png?w=2500&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=20d8cd6db898de7752b64280727d56d9 2500w" />

## Chunked dribble delay

Chunked dribble delay flushes the response body out in chunks over the total defined period:

<img src="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/chunked-dribble-delay.png?fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=f13baa40b56a97985b9b9a2911297bd1" title="Chunked dribble delay" width="50%" data-og-width="500" data-og-height="149" data-path="images/screenshots/chunked-dribble-delay.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/chunked-dribble-delay.png?w=280&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=24a57f4128267dc111fdde07cbc20815 280w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/chunked-dribble-delay.png?w=560&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=666e17907c6e56212d34a6c26cdd7641 560w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/chunked-dribble-delay.png?w=840&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=534c5478a611fb6b77fa14c2f8da161e 840w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/chunked-dribble-delay.png?w=1100&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=a08b42f991d1d52678575419060a3b35 1100w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/chunked-dribble-delay.png?w=1650&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=82342f4da193057a6eb8a4b20f7104b3 1650w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/chunked-dribble-delay.png?w=2500&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=a0f8c42d06f4c5d93edc5b89cad97359 2500w" />

## Delays and proxying

Fixed or random delays can be added to proxy responses in addition to direct responses, however chunked delays cannot at present.
