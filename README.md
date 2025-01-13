________________________________________
Tiktok clone
TikTok clone is a TikTok-like web application that allows users to register, log in, upload videos, and interact with content by liking, sharing, and commenting on videos. It is built using Flask, HTML, CSS, and JavaScript, with SQLite for database management.
________________________________________
Features
•	User Registration and Login: Secure user authentication system.
•	Video Upload: Users can upload short videos.
•	Interactive Features: Like, share, and comment on videos.
•	Responsive Design: Works on desktops, tablets, and mobile devices.
•	Swipe Functionality: Swipe left or right to navigate videos.
________________________________________
Installation
Prerequisites
•	Python 3.8+
•	Pip (Python package manager)
Clone the Repository
git clone https://Cypherx360@pikone.scm.azurewebsites.net/pikone.git
cd pikone
Install Dependencies
Install all required dependencies from requirements.txt:
pip install -r requirements.txt
________________________________________
Directory Structure
PikOne/
│
├── static/
│   ├── css/                # Stylesheets
│   ├── js/                 # JavaScript files
│   ├── uploads/            # Uploaded videos
│
├── templates/              # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│
├── app.py                  # Flask application
├── database.db             # SQLite database
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
________________________________________
Usage
Start the Development Server
Run the Flask app using the following command:
python app.py
Access the App
Open your web browser and navigate to:
http://127.0.0.1:5000
________________________________________
API Endpoints
Endpoint	Method	Description
/	GET	View home page with videos.
/login	GET/POST	User login.
/register	GET/POST	User registration.
/upload	POST	Upload a new video.
/like/<video_id>	POST	Like a video.
/comment/<video_id>	POST	Add a comment to a video.
/share/<video_id>	POST	Share a video.
________________________________________
Technologies Used
•	Frontend: HTML, CSS, JavaScript
•	Backend: Flask
•	Database: SQLite
•	Frameworks/Libraries: 
o	Flask-SQLAlchemy
o	Flask-WTF (for forms)
o	Bootstrap 5 (for styling)
________________________________________
Future Features
•	Advanced search and filtering for videos.
•	User profiles and follower system.
•	Real-time notifications.
•	Enhanced video editing options.
________________________________________
Contributing
We welcome contributions! If you'd like to contribute to this project:
1.	Fork the repository.
2.	Create a feature branch.
3.	Submit a pull request.
________________________________________
License
This project is licensed under the Ulster University Birminham Campus License. See the LICENSE file for details.
________________________________________
Contact
For inquiries or feedback, please contact us at:
•	Email: olasupooladotun6@gmail.com
•	GitHub: https://github.com/Ola-Domain
________________________________________
