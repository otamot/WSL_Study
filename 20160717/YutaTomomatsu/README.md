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

	public SimpleLinearRegression(double[] x,double[] y){
		this.x = x.clone();
		this.y = y.clone();
		this.b0=0;
		this.b1=0;
	}


	/**
	 * 単回帰を行う。
	 */
	public void learn(){
		b1 = covariance(x,y)/variance(x);
		double ave_x = 0, ave_y = 0;
		for(int i = 0; i < x.length; i++){
			ave_x += x[i];
			ave_y += y[i];
		}
		ave_x/=x.length;
		ave_y/=y.length;
		b0 = ave_y - b1*ave_x;
	}

	public void print(){
		System.out.println("y = " + b0 + " + " + b1 + "x");
	}


	/**
	 * aの分散を求める
	 * @param a doubleの1次元配列
	 * @return aの分散値
	 */
	public double variance(double[] a){
		double ave_a = 0;
		for(double a_i: a){
			ave_a += a_i;
		}
		ave_a/=a.length;

		double var_a = 0;
		for(int i = 0; i < a.length; i++){
			var_a += Math.pow((a[i] - ave_a),2);
		}
		var_a/=a.length;
		return var_a;
	}


	/**
	 * aとbの共分散を求める。
	 * @param a doubleの1次元配列
	 * @param b	doubleの1次元配列
	 * @return aとbの共分散値
	 */
	private double covariance(double[] a, double[] b){
		double cov_ab = 0;
		double ave_a = 0,ave_b = 0;
		for(int i = 0; i < a.length; i++){
			ave_a += a[i];
			ave_b += b[i];
		}
		ave_a/=a.length;
		ave_b/=b.length;

		for(int i = 0; i < a.length; i++){
			cov_ab += (a[i] - ave_a)*(b[i] - ave_b);
		}

		cov_ab /= a.length;

		return cov_ab;
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
