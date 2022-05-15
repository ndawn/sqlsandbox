select categories.name          as category_name,
       items.name               as item_name,
       category_parameters.name as parameter_name,
       item_parameters.value    as parameter_value
from categories
         join items
              on categories.id = items.category_id
         join item_parameters
              on items.id = item_parameters.item_id
         join category_parameters
              on categories.id = category_parameters.category_id
where categories.id = 9  -- or any desired category id
;
