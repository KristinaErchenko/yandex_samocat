SELECT c.login, COUNT(o."inDelivery") AS count_orders
FROM "Couriers" AS c
INNER JOIN "Orders" AS o ON c.id= o."courierId"
WHERE o."inDelivery"=true
GROUP BY c.login;

SELECT finished, cancelled, "inDelivery",
CASE WHEN finished = true THEN 2
     WHEN cancelled = true THEN -1
     WHEN "inDelivery" = true THEN 1
     ELSE 0
END
FROM "Orders";

 UPDATE "Orders" SET cancelled = true WHERE id=1