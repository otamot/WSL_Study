# WSL勉強会 20160522
* 日時:2016/05/22 13:30-18:00
* 場所:WSL研究室

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
