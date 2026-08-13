SELECT
    ip,
    COUNT(*) AS invalid_count
FROM Logs
WHERE
    ip NOT REGEXP '^([0-9]*[.]){3}[0-9]*$'
    OR ip REGEXP '(^|[.])0[0-9]'
    OR ip REGEXP '(^|[.])(256|25[7-9]|2[6-9][0-9]|[3-9][0-9][0-9])([.]|$)'
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;