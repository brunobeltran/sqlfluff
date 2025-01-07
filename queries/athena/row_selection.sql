WITH ex AS (
    SELECT
        1 AS w,
        CAST(ROW('there') AS ROW (hi STRING)) AS x
)

SELECT
    ex.w,
    ex.x,
    ex.x.hi
FROM ex
