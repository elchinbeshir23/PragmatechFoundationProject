from flask import Flask , request,render_template


app=Flask(__name__)

posts=[
    {
        "title":"post 1",
        "data_posted":"10.10.2021",
        "author":"farid"

    },
    {
        "title":"post 2", 
        "data_posted":"11.10.2021",
        "author":"memmed"

    },
    {
        "title":"post 3",
        "data_posted":"12.13.2021",
        "author":"fariz"

    }
]

@app.route('/')
def index(): 
    return render_template("index.html",my_data=posts )

@app.route('/main')
def main():
    return render_template ("main.html")

@app.route('/contact')
def contact():
    return render_template ("contact.html")

@app.route('/about')  
def about():
    return render_template ("about.html")


if __name__=='__main__':
    app.run(debug=True)