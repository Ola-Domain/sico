from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database Configuration
db_config = {
    'host': 'sico.mysql.database.azure.com',
    'port': 3306,
    'user': 'sico',
    'password': 'Ola-Mide&2',
    'database': 'your_database_name'  # Replace with your actual database name
}

# Connect to the database
def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

@app.route('/')
def home():
    return "Welcome to the Video App API"

# Example route: Fetch all videos
@app.route('/videos', methods=['GET'])
def get_videos():
    connection = get_db_connection()
    if connection is None:
        return jsonify({'error': 'Failed to connect to the database'}), 500

    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM videos")
        videos = cursor.fetchall()
        return jsonify(videos)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({'error': 'Failed to fetch videos'}), 500
    finally:
        cursor.close()
        connection.close()

# Example route: Add a new video
@app.route('/videos', methods=['POST'])
def add_video():
    data = request.json
    title = data.get('title')
    description = data.get('description')
    url = data.get('url')

    if not all([title, description, url]):
        return jsonify({'error': 'Missing required fields'}), 400

    connection = get_db_connection()
    if connection is None:
        return jsonify({'error': 'Failed to connect to the database'}), 500

    cursor = connection.cursor()
    try:
        query = "INSERT INTO videos (title, description, url) VALUES (%s, %s, %s)"
        cursor.execute(query, (title, description, url))
        connection.commit()
        return jsonify({'message': 'Video added successfully'}), 201
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({'error': 'Failed to add video'}), 500
    finally:
        cursor.close()
        connection.close()

# Example route: Fetch all comments for a video
@app.route('/videos/<int:video_id>/comments', methods=['GET'])
def get_comments(video_id):
    connection = get_db_connection()
    if connection is None:
        return jsonify({'error': 'Failed to connect to the database'}), 500

    cursor = connection.cursor(dictionary=True)
    try:
        query = "SELECT * FROM comments WHERE video_id = %s"
        cursor.execute(query, (video_id,))
        comments = cursor.fetchall()
        return jsonify(comments)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({'error': 'Failed to fetch comments'}), 500
    finally:
        cursor.close()
        connection.close()

# Example route: Add a new comment
@app.route('/videos/<int:video_id>/comments', methods=['POST'])
def add_comment(video_id):
    data = request.json
    user_id = data.get('user_id')
    comment_text = data.get('comment')

    if not all([user_id, comment_text]):
        return jsonify({'error': 'Missing required fields'}), 400

    connection = get_db_connection()
    if connection is None:
        return jsonify({'error': 'Failed to connect to the database'}), 500

    cursor = connection.cursor()
    try:
        query = "INSERT INTO comments (video_id, user_id, comment) VALUES (%s, %s, %s)"
        cursor.execute(query, (video_id, user_id, comment_text))
        connection.commit()
        return jsonify({'message': 'Comment added successfully'}), 201
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({'error': 'Failed to add comment'}), 500
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
