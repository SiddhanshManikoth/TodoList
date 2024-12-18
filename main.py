from flask import  Flask
from flask import render_template,request,redirect




app=Flask(__name__)

item_list=[]
check_list=[]

@app.route('/',methods=["GET","POST"])
def home():
    global item_list
    if request.method=="POST":
        try:
            if request.form['add']=='add':
                input = request.form.get('item')
                if input in item_list:
                    item_list.remove(input)
                item_list.append(input)
                print(item_list)
        except:
            pass
            for item in item_list:
                try:

                    if request.form[f'del{item}']== f'del{item}':
                        item_list.remove(item)
                        check_list.remove(item)
                        print("delete")
                except:
                    pass
                try:


                    if request.form[f'check{item}']==f'check{item}':
                        if item in check_list:
                            check_list.remove(item)
                        else:
                            check_list.append(item)

                except:
                    pass

    return render_template("index.html",item_list=item_list,check_list=check_list)



if __name__=="__main__":
    app.run(debug=True)