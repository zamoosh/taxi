SELECT
    COUNT(*)
FROM
    logs;


SELECT
    vendorid,
    COUNT(*)
FROM
    logs l
GROUP BY
    vendorid;


SELECT
    l.passenger_count,
    COUNT(*)
FROM
    logs l
GROUP BY
    l.passenger_count;


SELECT
    l.pulocationid AS "pulocationid",
    COUNT(*)       AS "count"
FROM
    logs l
GROUP BY
    l.pulocationid
ORDER BY
    count DESC;


SELECT
    l.dolocationid,
    COUNT(*) c
FROM
    logs l
GROUP BY
    l.dolocationid
ORDER BY
    c DESC;


SELECT DISTINCT
    l.vendorid

FROM
    logs l;


SELECT DISTINCT
    l.payment_type AS "value",
    CASE
        WHEN l.payment_type = 1 THEN 'CREDIT CARD'
        WHEN l.payment_type = 2 THEN 'CASH'
        WHEN l.payment_type = 3 THEN 'NO CHARGE'
        WHEN l.payment_type = 4 THEN 'DISPUTE'
        WHEN l.payment_type = 5 THEN 'UNKNOWN'
        WHEN l.payment_type = 6 THEN 'VOIDED TRIP'
    END            AS "name"
FROM
    logs l;


SELECT DISTINCT
    l.store_and_fwd_flag                                                                          AS "record was held in vehicle memory?",
    CASE WHEN l.store_and_fwd_flag = 'Y' THEN 'YES' WHEN l.store_and_fwd_flag = 'N' THEN 'NO' END AS "sdlkjfwe"
FROM
    logs l;


SELECT
    CASE
        WHEN l.vendorid = 1 THEN 'Creative Mobile Technologies, LLC'
        WHEN l.vendorid = 2 THEN 'VeriFone Inc'
    END                                          AS "فروشنده",
    SUM(l.total_amount) ::float8::NUMERIC::money AS "مبلغ فروش به دلار"
FROM
    logs l
GROUP BY
    l.vendorid
;



SELECT
    CASE
        WHEN l.payment_type = 1 THEN 'کارت اعتباری'
        WHEN l.payment_type = 2 THEN 'نقدی'
        WHEN l.payment_type = 3 THEN 'غیر نقدی'
        WHEN l.payment_type = 4 THEN 'اختلاف'
        WHEN l.payment_type = 5 THEN 'نامشخص'
        WHEN l.payment_type = 6 THEN 'سفر خالی'
    END      AS "name",
    COUNT(*) AS "count"
FROM
    logs l
GROUP BY
    l.payment_type
ORDER BY
    count DESC
;



SELECT
    CASE
        WHEN l.vendorid = 1 THEN 'Creative Mobile Technologies, LLC'
        WHEN l.vendorid = 2 THEN 'VeriFone Inc'
    END                                         AS "فروشنده",
    SUM(l.tolls_amount)::float8::NUMERIC::money AS "هزینه‌ی عوارض در سفر"
FROM
    logs l
GROUP BY
    l.vendorid
;


SELECT
    MAX(total_amount)::NUMERIC::money amount
FROM
    logs l
ORDER BY
    amount DESC
;


SELECT
    MIN(l.trip_distance),
    AVG(l.trip_distance),
    MAX(l.trip_distance)
FROM
    logs l
;



SELECT
    COUNT(*)
FROM
    logs l
WHERE
    l.trip_distance = 0
;



SELECT *
FROM
    (
        SELECT TRUNC(l.trip_distance, 0) AS d FROM logs l WHERE l.trip_distance > 0
    ) AS sq
WHERE
    TRUNC(sq.d, 0) > 1
;

SELECT
    l.trip_distance
FROM
    logs l
WHERE
    TRUNC(l.trip_distance, 0) > 0;


SELECT
    l.trip_distance AS distance,
    COUNT(*)        AS count
FROM
    logs l
GROUP BY
    l.trip_distance
;



SELECT
    l.total_amount AS distance,
    COUNT(*)       AS count
FROM
    logs l
GROUP BY
    l.total_amount
;


SELECT
    AVG(l.tip_amount) AS avg,
    COUNT(*)          AS "تعداد کل"
FROM
    logs l
;


SELECT
    AVG(l.tip_amount) AS avg,
    COUNT(*)          AS "تعداد کل"
FROM
    logs l
WHERE
    l.trip_distance > 0
    AND l.total_amount > 0
;



SELECT *
FROM
    (
        SELECT COUNT(*) AS count, l.passenger_count AS passenger_count FROM logs l GROUP BY l.passenger_count
    ) AS sq
;


SELECT
    COUNT(*) AS count,
    l.passenger_count
FROM
    logs l
WHERE
    l.passenger_count > 0
GROUP BY
    l.passenger_count
ORDER BY
    count DESC
;



SELECT
    l.pulocationid,
    COUNT(*) AS count
FROM
    logs l
GROUP BY
    l.pulocationid
ORDER BY
    count DESC
;


SELECT
    l.dolocationid,
    COUNT(*) AS count
FROM
    logs l
GROUP BY
    l.dolocationid
ORDER BY
    count DESC
;






