from unittest import result
from flask import Flask, render_template, request
import m1, m2, m3

app = Flask(__name__)



@app.route('/')
def home():
   return render_template("index.html")

@app.route('/model1')
def model1():
   return render_template("model1.html")

@app.route('/model1/predict', methods=["POST"])
def predict1():
   if request.method=="POST":
      num = request.form["num"]
   result = m1.recommend(int(num))
   return render_template("model1.html",result=result, num=num)


@app.route('/model2')
def model2():
   my_file = open("title.txt", "r")
   content = my_file.read()
   content_list = content.split("\n")
   my_file.close()
   return render_template("model2.html", contents = content_list)

@app.route('/model2/predict', methods=["POST"])
def predict2():
   if request.method=="POST":
      title = request.form["title"]
      num = request.form["num"]

   my_file = open("title.txt", "r")
   content = my_file.read()
   content_list = content.split("\n")
   my_file.close()
   if title not in content_list:
      result=0
   else:
      result = m2.get_recommendations(title, int(num))
   return render_template("model2.html",result=result, num=num, title=title, contents = content_list)

@app.route('/model3')
def model3():
   my_file = open("title.txt", "r")
   content = my_file.read()
   content_list = content.split("\n")
   my_file.close()
   return render_template("model3.html", contents = content_list)

@app.route('/model3/predict', methods=["POST"])
def predict3():
   if request.method=="POST":
      title = request.form["title"]
      num = request.form["num"]
   my_file = open("title.txt", "r")
   content = my_file.read()
   content_list = content.split("\n")
   my_file.close()
   if title not in content_list:
      result=0
   else:
      result = m3.get_recommendations(title, int(num))
   return render_template("model3.html",result=result, num=num, title=title, contents = content_list)


@app.route('/hybridmodel')
def model4():
   my_file = open("title.txt", "r")
   content = my_file.read()
   content_list = content.split("\n")
   my_file.close()
   return render_template("hybridmodel.html", contents = content_list)

@app.route('/hybridmodel/predict', methods=["POST"])
def predict4():
   if request.method=="POST":
      title = request.form["title"]
      num = request.form["num"]
   my_file = open("title.txt", "r")
   content = my_file.read()
   content_list = content.split("\n")
   my_file.close()
   if title not in content_list:
      result=0
   else:
      result1 = m1.recommend(int(num))
      result2 = m2.get_recommendations(title, int(num))
      result3 = m3.get_recommendations(title, int(num))
      i=0
      j=0
      k=0
      result=[]
      title_only = []
      for n in range(0, (int(num))//3):
         while result3[i][0] in title_only:
            i=i+1
         result.append(result3[i])
         title_only.append(result3[i][0])
         while result2[j][0] in title_only:
            j=j+1
         result.append(result2[j])
         title_only.append(result2[j][0])
         while result1[k][0] in title_only:
            k=k+1
         result.append(result1[k])
         title_only.append(result1[k][0])
         i=i+1
         j=j+1
         k=k+1
      if int(num) % 3 == 1:
         while result3[i][0] in title_only:
            i=i+1
         result.append(result3[i])
         title_only.append(result3[i][0])
      if int(num) % 3 == 2:
         while result3[i][0] in title_only:
            i=i+1
         result.append(result3[i])
         title_only.append(result3[i][0])
         while result2[j][0] in title_only:
            j=j+1
         result.append(result2[j])
         title_only.append(result2[j][0])
   
   return render_template("hybridmodel.html",result=result, num=num, title=title, contents = content_list)


if __name__ == '__main__':
   app.run(debug=True)