select o1.*
from orders o1
         left join orders o2
                   on o1.user_id = o2.user_id
                       and o1.created_at < o2.created_at
where o2.created_at is null
order by o1.created_at desc
;


with order_sums as (select orders.user_id,
                           orders.id                                      as order_id,
                           round(sum(oi.price * oi.quantity)::numeric, 2) as order_sum
                    from orders
                             join ordered_items oi on orders.id = oi.order_id
                    group by orders.id)
select os1.*
from order_sums os1
         left join order_sums os2
                   on os1.user_id = os2.user_id
                       and os1.order_sum < os2.order_sum
where os2.order_sum is null
order by os1.order_sum desc
;
