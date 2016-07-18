# YutaTomomatsu

[資料](http://www.slideshare.net/tomo_otamot/reggression)

## 実装

### SimpleLinearRegressionクラス
```Java
package linearRegression;

public class SimpleLinearRegression {
	private double[] x;
	private double[] y;
	private double b0;
	private double b1;
	private boolean learnFlg;

	/**
	 *
	 * @param x 説明(独立)変数の観測点
	 * @param y 目的(従属)変数の観測点
	 */
	public SimpleLinearRegression(double[] x,double[] y){
		if(x.length != y.length || x.length == 0)
			throw new IllegalArgumentException("変数の指定が正しくありません");
		this.x = x.clone();
		this.y = y.clone();
		b0=0;
		b1=0;
		learnFlg = false;
	}

	/**
	 * 単回帰を行う。
	 */
	public void learn(){
		b1 = covariance(x,y)/variance(x);
		b0 = average(y) - (b1*average(x));
		learnFlg = true;
	}


	/**
	 * 回帰を行って求めた重みを標準出力する
	 */
	public void print(){
		if(learnFlg)
			System.out.println("y = " + b0 + " + " + b1 + "x");
		else{
			throw new UnsupportedOperationException("learnメソッドを実行してからprintメソッドの呼び出しを行ってください。");
		}
	}

	/**
	 * aの平均を求める
	 * @param a doubleの1次元配列
	 * @return aの平均値
	 */
	private double average(double[] a){
		double ave_a = 0;
		for(double a_i: a)
			ave_a+=a_i;
		return ave_a/=a.length;
	}

	/**
	 * aの分散を求める
	 * @param a doubleの1次元配列
	 * @return aの分散値
	 */
	private double variance(double[] a){
		double ave_a = average(a);
		double var_a = 0;
		for(int i = 0; i < a.length; i++)
			var_a += Math.pow((a[i] - ave_a),2);
		return var_a/=a.length;
	}


	/**
	 * aとbの共分散を求める。
	 * @param a doubleの1次元配列
	 * @param b	doubleの1次元配列
	 * @return aとbの共分散値
	 */
	private double covariance(double[] a, double[] b){
		double cov_ab = 0;
		double ave_a = average(a);
		double ave_b = average(b);
		for(int i = 0; i < a.length; i++)
			cov_ab += (a[i] - ave_a)*(b[i] - ave_b);
		return cov_ab /= a.length;
	}
}

```

###　SimpleLinearRegressionMain クラス
```Java
package linearRegression;

public class SimpleLinearRegressionMain {

	public static void main(String[] args){
		double[] x = {100,200,300,400,500,600,700};
		double[] y = {40,50,50,70,65,65,80};

		SimpleLinearRegression slr = new SimpleLinearRegression(x, y);
		slr.learn();
		slr.print();
	}

}
```
