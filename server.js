const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');
const bcrypt = require('bcrypt');
const multer = require('multer');
const path = require('path');
const app = express();
const port = 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

// MySQL connection
const db = mysql.createConnection({
  host: 'sico.mysql.database.azure.com', // Your database host
  user: 'sico', // Your database user
  password: '{Ola-Mide&2', // Your database password
  database: 'your_database_name', // Replace with your database name
  port: 3306,
  ssl: { rejectUnauthorized: true }
});

// Connect to the database
db.connect(err => {
  if (err) {
    console.error('Database connection failed: ' + err.stack);
    return;
  }
  console.log('Connected to database.');
});

// Multer setup for file uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/');
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + path.extname(file.originalname));
  }
});
const upload = multer({ storage });

// User registration
app.post('/api/register', async (req, res) => {
  const { email, password } = req.body;
  const hashedPassword = await bcrypt.hash(password, 10);
  db.query('INSERT INTO users (email, password) VALUES (?, ?)', [email, hashedPassword], (err, results) => {
    if (err) {
      return res.status(500).send(err);
    }
    res.status(201).send('User registered successfully');
  });
});

// User login
app.post('/api/login', (req, res) => {
  const { email, password } = req.body;
  db.query('SELECT * FROM users WHERE email = ?', [email], async (err, results) => {
    if (err) {
      return res.status(500).send(err);
    }
    if (results.length === 0) {
      return res.status(401).send('Invalid email or password');
    }
    const user = results[0];
    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
      return res.status(401).send('Invalid email or password');
    }
    res.json({ id: user.id, email: user.email, bio: user.bio, profile_pic: user.profile_pic });
  });
});

// Upload video
app.post('/api/upload', upload.single('video'), (req, res) => {
  const { userId } = req.body;
  const videoUrl = `/uploads/${req.file.filename}`;
  db.query('INSERT INTO videos (user_id, video_url) VALUES (?, ?)', [userId, videoUrl], (err, results) => {
    if (err) {
      return res.status(500).send(err);
    }
    res.status(201).send('Video uploaded successfully');
  });
});

// Example route to get videos
app.get('/api/videos', (req, res) => {
  db.query('SELECT * FROM videos', (err, results) => {
    if (err) {
      return res.status(500).send(err);
    }
    res.json(results);
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
