网上的资料都只是介绍python连接数据库，其他的什么都没说，让我这没接触过数据库的小白摸爬滚打研究了两天。。

1.首先，得下载MySQL并安装，然后初始化（ip，用户名，密码），相当于注册账号，这个百度有教程。

2.先用MySQL创建一个数据库和表（python只能连接，不能创建），创建流程：

        打开命令提示符窗口，输入mysql -h localhost -u root -p，输入密码，相当于登陆账号
        创建数据库db1：create database db1;
        在db1中创建表table1: use db1;   create table table1(id int primary key, code text);

    创建完两列的空表，剩下的让python来完成就行了

3.网上有很多用MySQLdb的，我费死牛劲安装不上，又查了一下python3.x直接用pymysql就行，两个东西用法完全一样。pip install pymysql，剩下的看代码就ok了