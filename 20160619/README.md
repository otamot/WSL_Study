# WSL勉強会 20160619
* 日時:2016/06/19 13:30-18:00
* 場所:WSL研究室

## Isshu
### 今回考える問題
* Positiveな発言をする人
* Negativeな発言をした人

### ナイーブベイズ分類器
* ベイズの定理に基づく分類器


### ベルヌーイモデル
#### 分類フェーズ
### 多孔モデル
#### 分類ゲーム





## YutaTomomatsu
資料：[パワーポイント資料](http://www.slideshare.net/tomo_otamot/kmeansk)

### k-meansの話
[コチラ](https://github.com/otamot/MachineLearning/tree/master/clustering/KMeans)のページを参照

### javadocのお話
#### Javadoc何がいい？
ソースコード内にソースコードの説明が記述できる
(これだけじゃないですが・・・)

#### コメントと何が違うの?
* HTML形式のドキュメンテーションファイルを出力できる。
* 他にも…	コンパイル時の警告の抑制,非推奨メソッドの警告表		示,スレッドセーフかどうかなど様々なことを記述で		きる。

#### javadocの書き方
```Java
/**
*
* この部分にJavadocを記載する。
* @アノテーション //アノテーションを使って様々な説明を加えられる。
*/
```

#### アノテーション



|アノテーション|説明|
|:---|:---|
|@author|著者|
|@version|バージョン|
|@param|メソッドの引数の説明|
|@return|メソッドの返り値の説明|
|@throws|どんなときにどんなエラーをthrowするかの説明|


この他にもいろいろあります。



#### Javadocの例

```java
package annotation;

/**
 * @author YutaTomomatsu
 * @version ver0.0
 */
public class AnnotationTest{
	/**
	 * 2つの整数値を受け取ってその和をint型で返す。
	 * @param x 底。int型で与える。
	 * @param n 指数 0以上の整数。
	 * @return a^bの値
	 * @throws IllegalArgumentException nに負の値を渡した時。
	 */
	public static int pow(int x,int n){
		if(n < 0){
			throw new IllegalArgumentException("nが負の値です。");
		}
		int ans = 1;
		for(int i = 0; i < n; i++){
			ans*=x;
		}
		return ans;
	}
}
```


#### HTML形式のドキュメンテーションの作り方
* Eclipseを使うことによって簡単にドキュメンテーションを作れる。
* 上の例から作成してみる


* Project->Generate Javadoc...->private,publicを選択->Finish


* [できた!!!](https://htmlpreview.github.io/?https://github.com/otamot/WSL_Study/blob/master/20160619/doc/annotation/AnnotationTest.html)<-



### chan-p
[gitのページ](https://github.com/chan-p/Scala/tree/master/MachineLearning/LatentDirichletAllocation)<-

キーワード
* きょうえきぶんお

#### ぴーはやのMFまとめ


|種類|
|:-:|
|MF|
|SVD|

#### MF
* 通常に言われる行列因子分解
* 更新アルゴリズム:SGD,GD
* 評価値予測モデル
* $r=U_k^TI_k$
* 誤差関数: $\frac{1}{2}\sum(r-r)^2+$正則化項<-目的関数
##### 予測モデル
* $r = \alpha + U_b + I_b + U_K^TI_k$
* 誤差関数(r-(\alpha * U_b + I_b + U_k^))

#### SVD


### Inuken
* ニューラルネットワークについて
* 出力値->いろいろいじれる
* リカレントニューラルネットワーク→可変長の入力に対応できる
* LSTM

#### アンサンブル学習
##### バギング
* S = {S1,S2,,...,SN}
* N個からランダムで10個のサンプルを取り出して、それぞれモデルにかける
*

##### ブースティング
*

### boss
#### 3つの役割
##### プロダクトオーナー
* プロダクトの責任者
* ROIの最大化
* プロダクトバックログの管理
* ゴールを決める


##### スクラムマスター
* チームの成長を促す
* PO含め,チーム全員が共通認識を持てるようにコミュニケーションをする
* 中立性と客観性を発揮し,チームの問題か行けるできるよう導く
* 仕事の妨げとなる障害を取り除く

##### 開発チーム
* プロダクトの開発を行う
* 出荷可能な製品として実装することに責任を持つ
* 毎日の「検査」と「適応」でゴールの達成とプロセスの成長を行う
* 完了の定義を決め。


#### 5つのセレモニー

##### デイリースクラム
* 開発チーム全員で、スプリントゴールに対する進捗を確認するMTG
* 朝会,夕会
* 機能の作業,今日の予定,現在の障害の共有

##### スプリントレビュー
* スプリントの成果物のレビューを行う；。
* プロダクトの今後についてディスカッションする
* ステークホルダーも参加が可能

##### スプリント振り返り
* KPT
* 次のスプリントを計画的に行う。

##### スプリント計画
* スプリントのゴールを設定する
* プロファクトバックログからスプリントバックログからスプリントバックログを作成
* プランニングポーカー(見積もり)
* 1スプリントの最適期間は1~2週間

##### バックログリファインメント
* プロダクト
