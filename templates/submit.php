<?php
// Database connection parameters
$host = "sico.mysql.database.azure.com";
$port = 3306;
$username = "sico";
$password = "Ola-Mide&2";
$database = "your_database_name";

// Create connection
$conn = new mysqli($host, $username, $password, $database, $port);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $conn->real_escape_string($_POST['name']);
    $email = $conn->real_escape_string($_POST['email']);

    $sql = "INSERT INTO user (name, email) VALUES ('$name', '$email')";

    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully!";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

$conn->close();
?>
