# WSL勉強会 20160515
* 日付:2016/0515 Sat. 13:00-
* 場所

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


#### Table作成
##### WSL_Projectテーブル
|Project_id ^|Project_name|
|:--|:---|
|0|"REC"|
|1|"MS"|
|2|"CL"|
|3|"CA"|

##### WSL_Memberテーブル
|member_id^|member_name|project_id .|
|:--|:---|:--|
|0|"SG"|1|
|1|"KI"|0|
|2|"TH"|2|
|3|"YT"|3|

^: 主キー
.: 外部キー


##### SQL文
```SQL
Create table WSL_Project(
  `Project_id` int(11),
  `project_name` varchar(10),
  primary key(Project_id)
);

Create table WSL_Member(
  `member_id` int(11),
  `member_name` varchar(10),
  `project_id` int(11),
  primary key(member_id),
  foreign key(Project_id) references WSL_Project(Project_id)
);

Insert into WSL_Project values(0,"REC"),(1,"MS"),(2,"CL"),(3,"CA")
Insert into WSL_Member values(0,"SG",1),(1,"KI",0),(2,"TH",2),(3,"YT",3)
```




![screenshot2](https://github.com/otamot/WSL_Study20160515/blob/master/screenshot2.png)

![screenshot3](https://github.com/otamot/WSL_Study20160515/blob/master/screenshot3.png)


![screenshot4](https://github.com/otamot/WSL_Study20160515/blob/master/screenshot4.png)







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


構想：startとgoalの駅名を入力すると乗換駅を含めた最適な経路を表示してくれるアプリ

* View側で出発地と目的地を入力
* Controlerで出発地と目的地を基にデータベース(Model)から必要な情報をリクエストして、もらう。
* Controlerでデータから計算をして最短経路を求める。結果をJSONでViewに渡す。
* ViewではXMLをもとに表示する(UI設計？？)


リクエスト：localhost/s=登戸&g=渋谷:3000
レスポンス：登戸->下北沢->渋谷

[乗り換え検索アプリを作ろう!]()

## gitでチーム開発
* 1.fork
* 2.clone
* 3.switch branch
* 4.add->commit->push switched branch
* 5.pull request






## 参考ページ
[]
