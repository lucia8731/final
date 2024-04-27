from flask import Flask, render_template, request

app = Flask(__name__)

# ホームページ
@app.route('/', methods=['GET', 'POST'])
def home():
    total_tax = None  # 初期値としてNoneを設定
    if request.method == 'POST':
        # フォームから入力された情報を取得
        income = int(request.form['income'])
        dependents = int(request.form['dependents'])

        # ここで計算を行う（仮の計算）
        total_tax = calculate_tax(income, dependents)

    # 計算結果を同じページに表示
    return render_template('index.html', total_tax=total_tax)

# 計算関数（仮の関数）
def calculate_tax(income, dependents):
    # 仮の計算
    total_tax = income * 0.1 - dependents * 1000
    return total_tax

if __name__ == '__main__':
    app.run(debug=True)
