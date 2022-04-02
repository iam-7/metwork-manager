create database network_manager;

use network_manager;

create table users(
username varcharacter(50),
email varcharacter(50),
password varcharacter(50)
);

create table inventory (
hostname varcharacter(50),
ip varcharacter(50),
devtype varcharacter(50)
);

insert into users values("admin", "mssd.group2@gmail.com", "password");
insert into inventory values("R1", "192.168.1.2", "Router");
insert into inventory values("R2", "192.168.1.3", "Router");
insert into inventory values("SW1", "192.168.1.4", "Switch");
insert into inventory values("SW2", "192.168.1.5", "Switch");
insert into inventory values("FW1", "192.168.1.6", "Firewall");

select * from users;
select * from inventory;

