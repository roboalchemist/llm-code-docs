# Source: https://docs.unifygtm.com/best-practices/introduction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unifygtm.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Best Practices

> Unify's recommendations for high-performance GTM.

export const SequencesIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M10 14l11 -11"></path>
    <path d="M21 3l-6.5 18a.55 .55 0 0 1 -1 0l-3.5 -7l-7 -3.5a.55 .55 0 0 1 0 -1l18 -6.5"></path>
  </svg>;

export const PlaysIcon = ({size = 24}) => <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height={size} width={size} xmlns="http://www.w3.org/2000/svg">
    <path d="M3 19a2 2 0 1 0 4 0a2 2 0 0 0 -4 0"></path>
    <path d="M19 7a2 2 0 1 0 0 -4a2 2 0 0 0 0 4z"></path>
    <path d="M11 19h5.5a3.5 3.5 0 0 0 0 -7h-8a3.5 3.5 0 0 1 0 -7h4.5"></path>
  </svg>;

<CardGroup cols={2}>
  <Card title="Book Meetings with Plays" icon={<PlaysIcon />} href="/best-practices/plays">
    Learn how to use Plays effectively to automate your outbound.
  </Card>

  <Card title="Optimizing Outreach" icon={<SequencesIcon />} href="/best-practices/deliverability">
    Design your Sequences to maximize response rates and deliverability.
  </Card>
</CardGroup>
