from flask import Flask, render_template, request
import requests as r
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def statistics():
   if request.method == 'GET':
      result  = {}

      df = pd.read_csv('workforce.csv')

      # print(df)

      a = df['Headcount'].agg(['sum', 'mean']) 
      # print(a)



      s = a.plot(kind = 'hist')
      fig = s.get_figure()
      fig.savefig("output.png")

      result['result1'] = a.T

      print(result['result1'])
      agg_func_math = {
          'Headcount': ['sum']
      }

      agg_func_math_min_max = {
          'Headcount': ['min','max']
      }


      b = df.groupby(['Broad grade']).agg(agg_func_math).round(2)

      # print(b)
      s = b.plot()
      fig = s.get_figure()
      fig.savefig("output1.png")
      b = b.T
      result['result2'] = b


      c = df.groupby(['Role type']).agg(agg_func_math).round(2)

      # print(b)
      s = c.plot()
      fig = s.get_figure()
      fig.savefig("output2.png")

      result['result3'] = c.T


      d = df.groupby(['Ethnicity']).agg(agg_func_math).round(2)

      new = d.plot()
      fig = new.get_figure()
      fig.savefig("output3.png")

      result['result4'] = d.T


      e= df.groupby(['Ethnicity']).agg(agg_func_math_min_max).round(2)
      new = e.plot()
      fig = new.get_figure()
      fig.savefig("output4.png")
      result['result5'] = e.T
      # print(result)
      return render_template('index.html', result = result)

if __name__ == '__main__':
   app.run(debug = True)




