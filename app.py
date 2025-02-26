from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def input_page():
    return render_template('input.html')

@app.route('/view')
def view_page():
    # This will be implemented later
    return "View page coming soon!"

if __name__ == '__main__':
    app.run(debug=True)
