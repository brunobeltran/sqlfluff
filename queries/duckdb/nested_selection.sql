WITH ex AS (
    SELECT
        1 AS w,
        { 'hi': 'there' } AS x
)

SELECT
    ex.w,
    ex.x,
    ex.x.hi
FROM ex
