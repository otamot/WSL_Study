# WSL勉強会 20160515
* 日時:2016/0515 Sat.

## DB
* Mongo DB
* MySQL
* Access
* Postgress
* SQLite
* Redies
* RedShift
* Dynamo

## RDBMS vs NoSQL
###  RDBMS(Relational Database Management System)


## MySQLを使う
### インストール方法
```
$ brew install mysql
```

### 使い方
MySQLサーバの起動
```
$ mysql.server start
```

MySQLに入る
```
$ sudo mysql [-u username] [p]
```
|オプション|効果                     |
|:-------|:------------------------|
|-u      |ユーザ名を指定|
|-p      |passwordを入力してログイン。コマンド実行後にpasswordを尋ねられる|


```
mysql> SHOW DATABASES;

+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)

```

### Sequel proからDBをいじる
#### Sequel proとは
GUIでDBをいじれる

#### ダウンロード方法
[download site](http://www.sequelpro.com/)

#### 起動方法
![screenshot1](https://github.com/otamot/WSL_Study20160515/blob/master/screenshot1.png)




## Frameworkとは?
### Frameworkの種類
|Framework|
|---------|
|Node.js(Express)|
|Django|
|Ruby on Rails|


### MVC(Model View Controler)
  + M:Model->データベースとか
  + V:View->クライアント
  + C:Contoler

M↔C↔V

フレームワークとはMとVとCを作ってくれるもの





## 参考ページ
[]
