-- CHAPTER 12
-- PostgreSQL and SQL fundamentals

begin;
create temporary table lesson_posts (
 id integer primary key,
 title text not null,
 views integer not null default 0
) on commit drop;

-- Worked example 1: Insert records
insert into lesson_posts (id, title, views)
values (1, 'Hello', 3), (2, 'Launch', 12);
select count(*) as post_count from lesson_posts;

-- Worked example 2: Select and filter
select id, title
from lesson_posts
where views >= 10
order by id;

-- Worked example 3: Update a record
update lesson_posts
set title = 'Launch day'
where id = 2;
select title from lesson_posts where id = 2;

-- Worked example 4: Delete and inspect
delete from lesson_posts where id = 1;
select id, title from lesson_posts order by id;
