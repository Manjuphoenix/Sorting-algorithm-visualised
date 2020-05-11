
from flask import Flask, redirect, render_template,request, url_for


#import Sorting as sort
import random
import sys
sys.path.insert(1,'/home/Manjunath/deploy/static')
from static import Sorting as sort


#A=[1141, 1749, 448, 1211, 1218, 1369, 264, 1075, 1960, 887, 445, 456]




app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response





@app.route('/')
def index():
    return render_template('index.html')





@app.route("/actual_test" , methods=['GET', 'POST'])
def actual_test():
    option=request.form.get("option")
    A=[]
    start = 10
    end = 2000
    n = int(request.form.get("Size"))
    print(option)
    print(n)


    def Rand(start,end,n):
        for j in range(n):
            A.append(random.randint(start,end))

    Rand(start,end,n)

    print(A)
    if option == 'bubblesort':
        print(option)
        title='BubbleSort'
        sort.bubble(A,n,title)
    elif option == 'insertionsort':
        print(option)
        title='InsertionSort'
        sort.insert(A,title)
    elif option == 'selectionsort':
        print(option)
        title='SelectionSort'
        sort.select(A,title)
    elif option == 'quicksort':
        print(option)
        title='QuickSort'
        sort.quick(A,0,n-1,title)
    elif option == 'mergesort':
        print(option)
        title='MergeSort'
        sort.MERGE(A,0,n-1,title)
    #response = url_for('static' , filename="sorted.mp4")
    return redirect(url_for('static' , filename='%s.mp4'%title))
if __name__=='__main__':
    print("IM HERE")
    app.run(debug=True)
