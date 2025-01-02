
CREATE TABLE log_date(
id INTEGER primary key AUTOINCREMENT ,
entry_date date not NULL);
CREATE TABLE food (
id INTEGER PRIMARY key AUTOINCREMENT,
name TEXT not null,
protein INTEGER not null,
carbohydrate INTEGER not null,
fat INTEGER not null,
calories INTEGER not null
);
CREATE TABLE food_date(
food_id INTEGER not null,
log_date_id INTEGER not null,
PRIMARY key(food_id ,log_date_id)
);
 