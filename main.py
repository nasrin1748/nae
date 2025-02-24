from pyscript import display,HTML
import os
#display(HTML("""<div id="div-01"><h1>Addition Calculator</h1>
#<p>input 1: <input id="input1" size="5"/></p><br>
#<p>input 2: <input id="input2" size="5"/></p><br>
#<button py-click="myFunction" id="add">Submit</button>
#<p></p></div>"""))
#def myFunction():
#       from js import document
#       num1 = document.getElementById("input1").value
#       num2 = document.getElementById("input2").value
#       print(num1)      
def click_handler(): 
    x = int(input("enter the value of a: "))
    y = int(input("enter the value of b: "))
    #c = x+y
    #print("Answer is:"+(c))
    c = f"{int(x)+int(y)}"
    print(c)


