# WSL勉強会 20160522
* 日時:2016/05/22 13:30-18:00
* 場所:WSL研究室

## YutaTomomatsu
資料：[k-means.ppt](https://github.com)
### k-meansの話
[コチラ](https://github.com/otamot/MachineLearning/tree/master/clustering/KMeans)のページを参照

### javadocのお話
アノテーション


|アノテーション|説明|
|:---|:---|
|@author|著者|
|@version|バージョン|
|@param|メソッドの引数の説明|
|@return|メソッドの返り値の説明|
|@throws|どんなときにエラーをthrowするかの説明|




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
