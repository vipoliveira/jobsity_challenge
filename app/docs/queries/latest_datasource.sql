SELECT DISTINCT * FROM(
SELECT region, 
datasource, 
datetime,
RANK() OVER(PARTITION BY region ORDER BY datetime DESC) AS rank
FROM `jobsity-challenge-375918.jobsity.trips`
  WHERE region IN
    (SELECT region FROM
    (SELECT region, COUNT(*) qtde, FROM `jobsity-challenge-375918.jobsity.trips` GROUP BY 1 ORDER BY 1 DESC LIMIT 2
    ))
)
WHERE rank = 1