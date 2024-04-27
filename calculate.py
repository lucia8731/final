from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# 計算結果を表示するページのルートURL
@app.route('/result')
def result():
    # 仮の計算結果データ（本来はここで実際の計算処理を行う）
    data = {
        'totalTax': 50000,
        'incomeTax': 30000,
        'residentTax': 20000,
        'incomeDeduction': 10000,
        'taxDeduction': 5000
    }
    # HTMLテンプレートに計算結果データを渡してレンダリング
    return render_template('result.html', data=data)

# フォームの入力を受け取るルートURL
@app.route('/calculate', methods=['POST'])
def calculate():
    # フォームからのデータを取得（ここで計算を行う）
    # 仮の計算結果を計算（本来はここで実際の計算処理を行う）
    # 仮の計算結果データ
    data = {
        'totalTax': total_tax,
        'incomeTax': income_tax,
        'residentTax': resident_tax,
        'incomeDeduction': income_deduction,
        'taxDeduction': tax_deduction
    }
    # 計算結果を表示するページにリダイレクト
    return redirect(url_for('result'))

if __name__ == '__main__':
    app.run(debug=True)
