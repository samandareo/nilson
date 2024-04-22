from flask import Flask, jsonify, render_template
import psycopg2
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['JSON_AS_ASCII'] = False

try:
    db_host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    conn = psycopg2.connect(
        host=db_host,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
except psycopg2.OperationalError as e:
    print(f"Error connecting to the database: {e}")

# @app.route('/users', methods=['GET'])
# def get_users():
#     try:
#         with conn.cursor() as cur:
#             cur.execute("SELECT * FROM users_wolf")
#             rows = cur.fetchall()
#             users = []
#             for row in rows:
#                 user = {
#                     'id': row[0],
#                     'user_id':row[1],
#                     'name': row[2],
#                     'contact': row[3],
#                     'location': row[4],
#                 }
#                 users.append(user)
#         return render_template('index.html', users=users)
#     except psycopg2.Error as e:
#         print(f"Error fetching users from the database: {e}")
#         return "An error occurred while fetching users", 500


# @app.route('/media/<int:user_id>', methods=['GET'])
# def get_media(user_id):
#     try:
#         with conn.cursor() as cur:
#             cur.execute("SELECT video_url FROM video_table WHERE user_id = %s", (user_id,))
#             rows = cur.fetchall()
#             media_urls = [row[0] for row in rows]
#             return render_template('index.html', media_urls=media_urls)
#     except psycopg2.Error as e:
#         print(f"Error fetching media from the database: {e}")
#         return "An error occurred while fetching media", 500


@app.route('/media', methods=['GET'])
def get_media():
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT video_url FROM video_table WHERE video_url LIKE '%.mp4' OR video_url LIKE '%.avi'")
            rows = cur.fetchall()
            media_urls = [row[0] for row in rows]
            return render_template('index.html', media_urls=media_urls)
    except psycopg2.Error as e:
        print(f"Error fetching media from the database: {e}")
        return "An error occurred while fetching media", 500

@app.route('/feedback', methods=['GET'])
def get_feedbacks():
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id,user_id,name,feedback FROM feedbacks")
            rows = cur.fetchall()
        
            cur.execute("SELECT id,name, date, feedback FROM feedbacks")
            rows2 = cur.fetchall()
            print(rows2)
            return render_template('feedback.html', user_infos=rows, feedback=rows2)
    except psycopg2.Error as e:
        print(f"Error fetching user info from the database: {e}")
        return "An error occurred while fetching media", 500

if __name__ == '__main__':
    app.run(debug=True)
