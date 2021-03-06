from flask import Flask, render_template, request, url_for
import cx_Oracle  as DB

app = Flask(__name__)

@app.route('/')
def render_static_html():
    return render_template('index.html')

@app.route("/photos", methods=['POST', 'GET'])
def mainpage_photos():
    if request.method == 'POST':
        title = request.form['Title']
        author = request.form['Author']
        description = request.form['Description']
        date = request.form['Date']
        conn = DB.connect()
        cursor = conn.cursor()
        to_db = ("", title, author, description, date)
        cursor.execute("INSERT INTO photos VALUES (%s, %s, %s, %s, %s)", to_db)
        conn.commit()
        cursor.close()
    cursor = DB.connect().cursor()
    cursor.execute("SELECT * from photos")
    data = cursor.fetchall()
    cursor.close()
    return render_template('mainpage_photos.html', data = data)

if __name__ == "__main__":
    app.run(debug=True)

