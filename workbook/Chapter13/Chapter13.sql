-- CHAPTER 13
-- Relationships, joins, constraints and transactions

begin;
create temporary table lesson_authors (
 id integer primary key, name text not null
) on commit drop;
create temporary table lesson_posts (
 id integer primary key,
 author_id integer references lesson_authors(id),
 title text not null check (length(trim(title)) between 1 and 160)
) on commit drop;

-- Worked example 1: Related rows
insert into lesson_authors values (1, 'Ada'), (2, 'Lin'), (11, 'Sam');
insert into lesson_posts values (10, 1, 'Hello'), (11, 1, 'Launch'), (545, 11, 'What'), (100, 11, 'Down'), (200, 2, 'WORK'), (123, 1, 'Monday');
select count(*) from lesson_posts;
-- select count(*) from lesson_authors;

-- Worked example 2: Join posts to authors
select p.title, a.name as author
from lesson_posts p
join lesson_authors a on a.id = p.author_id
order by p.id;

-- Worked example 3: Rollback part of a transaction
savepoint before_edit;
update lesson_posts set title = 'Temporary' where id = 123;
rollback to savepoint before_edit;
select title from lesson_posts where id = 123;

-- Worked example 4: Index and ownership predicate
create index lesson_posts_author_idx on lesson_posts(author_id);
select id from lesson_posts
where author_id = 11 order by id;
