/**
 * @Author: Абделлах Улахияне
 * @Date:   2021-04-11 02:46:11
 * @Last Modified by:   Абделлах Улахияне
 * @Last Modified time: 2021-04-11 16:43:51
 */
create database chess;
use chess;


create table figure(
    id int primary key not null,
    name varchar(55) not null unique,
    imgpath varchar(255) not null,
    description varchar(255) not null
);
create table guide(
    id int primary key  not null,
    label varchar(255) not null,
    description varchar(255) not null
);
create table commands(
    id int primary key not null,
    label varchar(55) not null,
    description varchar(255) not null
); 