from flask import Flask, render_template
import json
import pandas as pd


app = Flask(__name__)

df = pd.read_csv('d:/thinkquant/Data/2016-2016/A.csv', header=0, index_col=0, parse_dates=True)
df['datetime'] = df.index
data = df.iloc[:100].to_dict('records')

#jdata=json.dumps(data)

@app.route('/')
def index():
    return render_template("table.html", data=data)


if __name__ == '__main__':
	#print jdata
  app.run(debug=True)