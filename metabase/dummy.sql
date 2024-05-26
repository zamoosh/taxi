SELECT *,
    CASE
        WHEN l.vendorid = 1 THEN 'Creative Mobile Technologies, LLC'
        WHEN l.vendorid = 2 THEN 'VeriFone Inc'
    END AS "فروشنده"
FROM
    logs l
WHERE
    l.trip_distance <= 0
    AND l.total_amount > 0
;


SELECT
    CASE
        WHEN l.vendorid = 1 THEN 'Creative Mobile Technologies, LLC'
        WHEN l.vendorid = 2 THEN 'VeriFone Inc'
    END      AS "فروشنده",
    COUNT(*) AS "count"
FROM
    logs l
WHERE
    l.trip_distance <= 0
    AND l.total_amount > 0
GROUP BY
    l.vendorid
;


SELECT *
FROM
    logs l
WHERE
    l.pulocationid = l.dolocationid
;


SELECT
    COUNT(*)
FROM
    logs l
WHERE
    l.extra > 1
;



SELECT
    l.extra
FROM
    logs l
WHERE
    l.extra > 1
;


SELECT
    COUNT(*)
FROM
    logs l
WHERE
    l.total_amount < 0
;



