const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

// Middleware to parse incoming JSON bodies
app.use(bodyParser.json());

// MySQL connection configuration
const connection = mysql.createConnection({
  host: 'sico.mysql.database.azure.com',  // Azure MySQL host
  user: 'sico',                          // Azure MySQL user
  password: 'Ola-Mide&2',                // Azure MySQL password
  database: 'sici',                      // Database name
  port: 3306,                            // MySQL port
  ssl: true                              // SSL for secure connection
});

// Establish connection to MySQL
connection.connect(err => {
  if (err) {
    console.error('Error connecting to MySQL:', err);
    return;
  }
  console.log('Connected to MySQL');
});

// Create users table if it doesn't exist
const createUsersTable = `
  CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    followers INT DEFAULT 500
  );
`;

connection.query(createUsersTable, (err, results) => {
  if (err) {
    console.error('Error creating users table:', err);
    return;
  }
  console.log('Users table created or already exists');
});

// Register endpoint for user sign-up
app.post('/register', (req, res) => {
  const { username, email, password } = req.body;
  const query = 'INSERT INTO users (username, email, password) VALUES (?, ?, ?)';
  connection.query(query, [username, email, password], (err, results) => {
    if (err) {
      console.error('Error registering user:', err);
      res.status(500).send('Error registering user');
      return;
    }
    res.status(200).send('User registered successfully');
  });
});

// Login endpoint for user authentication
app.post('/login', (req, res) => {
  const { username, password } = req.body;
  const query = 'SELECT * FROM users WHERE username = ? AND password = ?';
  connection.query(query, [username, password], (err, results) => {
    if (err) {
      console.error('Error logging in:', err);
      res.status(500).send('Error logging in');
      return;
    }
    if (results.length > 0) {
      res.status(200).json(results[0]);  // Send the user data back if credentials are correct
    } else {
      res.status(401).send('Invalid credentials');
    }
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
