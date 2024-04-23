from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/route_finder', methods=['GET', 'POST'])
def route_finder():
    if request.method == 'POST':
        start_station = request.form['start_station']
        end_station = request.form['end_station']
        # ここに乗り換え情報を取得するコードを追加します
        route_info = get_route_info(start_station, end_station)
        return render_template('route.html', route_info=route_info)
    return render_template('route_finder.html')

def get_route_info(start_station, end_station):
    # ここで路線情報を取得し、適切な形式で返します
    # 仮のデータを返す例
    return {
        'start_station': start_station,
        'end_station': end_station,
        'route': 'Take Ginza Line, 5 stops.'
    }

if __name__ == '__main__':
    app.run(debug=True)
