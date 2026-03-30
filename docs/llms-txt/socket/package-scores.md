# Source: https://docs.socket.dev/docs/package-scores.md

# Package Scores

<HTMLBlock>
  {`
  <!DOCTYPE html>

  <html>

  <body>
      <h1>Socket Scores and Alerts</h1>
      <p>Socket scores and alerts are broken down into the following categories:</p>
      <ul>
          <li>Supply chain risk</li>
          <li>Quality</li>
          <li>Maintenance</li>
          <li>Vulnerabilities</li>
          <li>License</li>
      </ul>
      <p>Socket scores packages across several categories, with alert severity playing a major role. Each type of alert (Critical, High, Medium, or Low) affects the score differently through normalization functions and soft caps. The final score is raised to the power of γ, a scaling factor based on the size and popularity of the project. This exponent compresses low scores and softens the impact of penalties, especially for large or popular packages. Each metric may also optionally apply a limit.</p>
    
  <p>
    <strong>Critical Alerts:</strong><br>
  When any critical alerts are present, this metric is limited to the minimum of 0.25 and a weighted average of other scoring signals. The limit of 0.25 acts as a soft cap because the final score is calculated as 100 × (min(limit, weighted-average))^γ. For example, when γ = 0.8, a cap of 0.25 leads to a final score of about 33%. However, if the weighted average is lower than 0.25, the final score can fall even further.<br></p>
  <p>
    <strong>High Alerts:</strong><br>
  High alerts reduce the score using an exponential decay, e^−x. The metric is capped at max(0.25, 1 − x/10), bottoming out at 0.25 when there are 8 or more alerts. The actual contribution can go lower due to weighted averaging. If this metric becomes the lowest among all, it can pull down the overall score significantly.<br></p>
  <p> <strong> Medium Alerts:</strong><br>
  Medium alerts  decay more slowly using e^−x/20, with a cap of max(0.5, 1.15 − x/20), which levels off at 0.5 after about 13 alerts. Even though the limit flattens, the normalized value can fall below 0.5 and continue decreasing.<br></p>
  <p>  <strong>Low Alerts:</strong><br>
  Low alerts have the least impact. They decay gently with e^−x/40 and have no cap, so their effect on the score remains small and gradual.
    Other Factors:<br></p>
  <p>  <strong>Package scores</strong> are also influenced by project attributes like popularity, size, and maintenance activity. These affect the γ exponent. Larger or more widely used packages tend to have a smaller γ, which reduces the impact of negative metrics and allows those packages to maintain relatively higher scores even when some alerts are present.
   </p>

  <p><strong>Breakdown:</strong></p>
  <p> Given a category <i>i</i>, let <i>x<sub>i,j</sub></i> be the value of metric <i>j</i> with normalization function <i>N<sub>j</sub></i> and weight <i>w<sub>j</sub></i> and limit <i>l<sub>i,j</sub></i>. </p>

  <p>Then the score <i>S<sub>i</sub></i> is</p>
      <p style="text-align:center;">S<sub>i</sub> = 100 &middot; min ( max (0, min<sub>j</sub> l<sub>i,j</sub>), <sup>&sum;<sub>j</sub> w<sub>j</sub> N<sub>j</sub>(x<sub>j</sub>)</sup>/<sub>&sum;<sub>j</sub> w<sub>j</sub></sub> )<sup>&#x3B3;</sup></p>
      <p>Where &#x3B3; is a power scaling constant based on the size and popularity of the project:</p>
      <p style="text-align:center;">&#x3B3; &asymp; <sup>1</sup>/<sub>2</sub> + c<sub>0</sub> log(lines of code) + c<sub>1</sub> log(popularity)</p>
      <p>Currently socket supports the following metrics:</p>

  <table>
          <tr>
              <th>Metric</th>
              <th>Category</th>
              <th>Weight</th>
              <th>Normalization</th>
              <th>Limit</th>
          </tr>
          <tr>
              <td>Critical Alerts</td>
              <td>Any</td>
              <td>1</td>
              <td>e<sup>-10x</sup></td>
              <td>{ <sup>1</sup>/<sub>4</sub> if x &gt; 0 <br> 1 otherwise }</td>
          </tr>
          <tr>
              <td>High Alerts</td>
              <td>Any</td>
              <td>2</td>
              <td>e<sup>-x</sup></td>
              <td>max { <sup>1</sup>/<sub>4</sub>, 1 - <sup>x</sup>/<sub>10</sub> }</td>
          </tr>
          <tr>
              <td>Medium Alerts</td>
              <td>Any</td>
              <td>2</td>
              <td>e<sup>-x/20</sup></td>
              <td>max { <sup>1</sup>/<sub>2</sub>, 1.15 - <sup>x</sup>/<sub>20</sub> }</td>
          </tr>
          <tr>
              <td>Low Alerts</td>
              <td>Any</td>
              <td>3</td>
              <td>e<sup>-x/40</sup></td>
              <td>1</td>
          </tr>
          <tr>
              <td>License Quality</td>
              <td>License</td>
              <td>12</td>
              <td><sup>x</sup>/<sub>100</sub></td>
              <td>1</td>
          </tr>
          <tr>
              <td>Maintainer Count</td>
              <td>Maintenance</td>
              <td>5</td>
              <td>-(e<sup>x/3</sup> - 1)</td>
              <td>{ 0 if x = 0 <br> 1 otherwise }</td>
          </tr>
          <tr>
              <td>Versions Last Year</td>
              <td>Maintenance</td>
              <td>5</td>
              <td>-(e<sup>-x/12</sup> - 1)</td>
              <td>1</td>
          </tr>
          <tr>
              <td>Versions Last Two Months</td>
              <td>Maintenance</td>
              <td>3</td>
              <td>-(e<sup>-x</sup> - 1)</td>
              <td>1</td>
          </tr>
          <tr>
              <td>Versions Last Month</td>
              <td>Maintenance</td>
              <td>2</td>
              <td>-(e<sup>-x</sup> - 1)</td>
              <td>1</td>
          </tr>
          <tr>
              <td>Versions Last Week</td>
              <td>Maintenance</td>
              <td>1</td>
              <td>-(e<sup>-x/0.25</sup> - 1)</td>
              <td>1</td>
          </tr>
          <tr>
              <td>Open Issues</td>
              <td>Maintenance</td>
              <td>1</td>
              <td>e<sup>-x/100</sup></td>
              <td>1</td>
          </tr>
          <tr>
              <td>Closed Issues</td>
              <td>Maintenance</td>
              <td>1</td>
              <td>-(e<sup>-x/1000</sup> - 1)</td>
              <td>1</td>
          </tr>
          <tr>
              <td>Commits Last Week</td>
              <td>Maintenance</td>
              <td>1</td>
              <td>-(e<sup>-x/4</sup> - 1)</td>
              <td>1</td>
          </tr>
          <tr>
              <td>Commits Last Month</td>
              <td>Maintenance</td>
              <td>1</td>
              <td>-(e<sup>-x/6</sup> - 1)</td>
              <td>1</td>
          </tr>
          <tr>
              <td>Commits Last Two Months</td>
              <td>Maintenance</td>
              <td>1</td>
              <td>-(e<sup>-x/32</sup> - 1)</td>
              <td>1</td>
          </tr>
          <tr>
              <td>Commits Last Year</td>
              <td>Maintenance</td>
              <td>1</td>
              <td>-(e<sup>-x/208</sup> - 1)</td>
              <td>1</td>
          </tr>
          <tr>
              <td>Commits</td>
              <td>Maintenance</td>
              <td>1</td>
              <td>-(e<sup>-x/300</sup> - 1)</td>
              <td>1</td>
          </tr>
          <tr>
              <td>Version Count</td>
              <td>Maintenance</td>
              <td>0.5</td>
              <td>-(e<sup>-x/10</sup> - 1)</td>
              <td>1</td>
          </tr>
          <tr>
              <td>Readme Length</td>
              <td>Quality</td>
              <td>5</td>
              <td><sup>x</sup>/<sub>100</sub></td>
              <td>1</td>
          </tr>
          <tr>
              <td>Bundle Size</td>
              <td>Quality</td>
              <td>2</td>
              <td>e<sup>-x/16384</sup></td>
              <td>1</td>
          </tr>
          <tr>
              <td>Stargazers</td>
              <td>Quality</td>
              <td>1</td>
              <td>-(e<sup>-x/100</sup> - 1)</td>
              <td>1</td>
          </tr>
          <tr>
              <td>Forks</td>
              <td>Quality</td>
              <td>1</td>
              <td>-(e<sup>-x</sup> - 1)</td>
              <td>1</td>
          </tr>
          <tr>
              <td>Watchers</td>
              <td>Quality</td>
              <td>1</td>
              <td>-(e<sup>-x</sup> - 1)</td>
              <td>1</td>
          </tr>
          <tr>
              <td>Lines of Code</td>
              <td>Quality</td>
              <td>0.5</td>
              <td><sup>x</sup>/<sub>50</sub></td>
              <td>1</td>
          </tr>
          <tr>
              <td>Download Count</td>
              <td>Supply Chain Risk</td>
              <td>5</td>
              <td>-(e<sup>-x/10000</sup> - 1)</td>
              <td>1</td>
          </tr>
          <tr>
              <td>Transitive Dependency Count</td>
              <td>Supply Chain Risk</td>
              <td>1</td>
              <td>e<sup>-x/1000</sup></td>
              <td>1</td>
          </tr>
          <tr>
              <td>Total Dependency Count</td>
              <td>Supply Chain Risk</td>
              <td>1</td>
              <td>e<sup>-x/1000</sup></td>
              <td>1</td>
          </tr>
          <tr>
              <td>Dependency Count</td>
              <td>Supply Chain Risk</td>
              <td>1</td>
              <td>e<sup>-x/50</sup></td>
              <td>1</td>
          </tr>
          <tr>
              <td>Dev Dependency Count</td>
              <td>Supply Chain Risk</td>
              <td>0.5</td>
              <td>e<sup>-x/100</sup></td>
              <td>1</td>
          </tr>
          <tr>
              <td>Dependency Vulnerability Count</td>
              <td>Vulnerability</td>
              <td>1</td>
              <td>1 - x</td>
              <td>{ <sup>0.5</sup> if x &gt; 0 <br> 1 otherwise }</td>
          </tr>
          <tr>
              <td>Vulnerability Count</td>
              <td>Vulnerability</td>
              <td>1</td>
              <td>1 - <sup>x</sup>/<sub>3</sub></td>
              <td>1</td>
          </tr>
      </table>
  </body>
  </html>
  `}
</HTMLBlock>

Please note that these metrics are subject to change and may be revised as we make changes to our system. The contents of this document may not exactly represent the scoring system as deployed in Socket at this point in time as we are continuously making adjustments to these systems.