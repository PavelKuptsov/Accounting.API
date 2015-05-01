DROP FUNCTION IF EXISTS currency_get(p_id INT);

CREATE FUNCTION currency_get(
    p_id INT
)
RETURNS TABLE (
    id INT,
    name VARCHAR(100),
    short_name VARCHAR(3)
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.name,
        c.short_name
    FROM currency c
    WHERE c.id = p_id;
END; $$
LANGUAGE PLPGSQL;