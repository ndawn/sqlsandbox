select most_recent_orders.user_id,
       most_recent_orders.id as order_id,
       items.name                                  as item_name,
       oi.price                                    as item_price,
       oi.quantity                                 as item_quantity,
       round((oi.price * oi.quantity)::numeric, 2) as item_overall_price
from (select o1.*
      from orders o1
               left join orders o2
                         on o1.user_id = o2.user_id
                             and o1.created_at < o2.created_at
      where o2.created_at is null
      order by o1.created_at desc) most_recent_orders
         join ordered_items oi on most_recent_orders.id = oi.order_id
         join items on items.id = oi.item_id
;
