-- County-level turnout rate by party
SELECT
    county,
    party,
    COUNT(*) AS total_registered,
    SUM(voted) AS total_voted,
    ROUND(SUM(voted) * 100.0 / COUNT(*), 2) AS turnout_percentage
FROM
    voting_records_demo
WHERE
    election_year = 2024
GROUP BY
    county, party
ORDER BY
    county, turnout_percentage DESC;



-- Export the turnout summary to CSV for reporting
COPY (
    SELECT
        county,
        party,
        ROUND(SUM(voted) * 100.0 / COUNT(*), 2) AS turnout_pct
    FROM
        voting_records_demo
    WHERE
        election_year = 2024
    GROUP BY
        county, party
)
TO '/Users/analyst/Documents/voting_turnout_report.csv'
WITH CSV HEADER;
