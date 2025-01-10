CREATE TABLE user(
id integer primary key AUTOINCREMENT,
name text not NULL,
password text not NULL,
expert boolean not NULL,
admin boolean not NULL,
);
create TABLE questions(
id integer primary key AUTOINCREMENT,
question_text text not NULL,
ans text not NULL,
ask_by_id integer not NULL,
expert_id integer not NULL,
);