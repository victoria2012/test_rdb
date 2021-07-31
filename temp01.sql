create table members(
    id real,
    name text,
    age real,
    address text,
    salary real
);

select id,name,age,address,salary from members;

insert into members(id,name,age,salary,address) values(1,'Paul',32,20000,'California');

select id,name,age from members;

INSERT INTO members (ID,NAME,AGE,ADDRESS,SALARY)
		VALUES (2, 'Allen', 25, 'Texas', 15000.00 );
INSERT INTO members (ID,NAME,AGE,ADDRESS,SALARY)
		VALUES (3, 'Teddy', 23, 'Norway', 20000.00 );
INSERT INTO members (ID,NAME,AGE,ADDRESS,SALARY)
		VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 );
INSERT INTO members (ID,NAME,AGE,ADDRESS,SALARY)
		VALUES (5, 'David', 27, 'Texas', 85000.00 );
INSERT INTO members (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (6, 'Kim', 22, 'South-Hall', 45000.00 );
INSERT INTO members VALUES (7, 'James', 24, 'Houston', 10000.00 );
INSERT INTO members VALUES (8, 'James', 35, 'Texas', 40000.00 );

select id,name,age,address,salary from members;

select count(*) from members;

select * from members where name like '%d%';

select * from members where age >= 25 and name like '%d%';

drop table boston_table;

select * from boston_table;


select count(*) from boston_table;

select count(*) from iris_table;

select count(*) from iris_table it;

select * from members where age >= 25


create table members(
    id real,
    name text,
    age real,
    address text,
    salary real
);

insert into members(id,name,age,salary,address) values(1,'Paul',32,20000,'California');
INSERT INTO members (ID,NAME,AGE,ADDRESS,SALARY)
		VALUES (2, 'Allen', 25, 'Texas', 15000.00 );
INSERT INTO members (ID,NAME,AGE,ADDRESS,SALARY)
		VALUES (3, 'Teddy', 23, 'Norway', 20000.00 );
INSERT INTO members (ID,NAME,AGE,ADDRESS,SALARY)
		VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 );
INSERT INTO members (ID,NAME,AGE,ADDRESS,SALARY)
		VALUES (5, 'David', 27, 'Texas', 85000.00 );
INSERT INTO members (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (6, 'Kim', 22, 'South-Hall', 45000.00 );
INSERT INTO members VALUES (7, 'James', 24, 'Houston', 10000.00 );
INSERT INTO members VALUES (8, 'James', 35, 'Texas', 40000.00 );


select count(*) from iris_table it;


select * from members;

select name, count(name) from members
group by name
;

select name, sum(salary) from members
group by name
;

select name, count(name), sum(salary) from members
group by name
;

select age, count(age), sum(salary) from members
group by age
;