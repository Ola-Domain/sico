$sql = "INSERT INTO videos (name, email, video_path) VALUES ('$name', '$email', '$target_file')";
if ($conn->query($sql) === TRUE) {
    echo "Record saved successfully.";
} else {
    echo "Error: " . $conn->error;
}
$conn->close();
