$sql = "SELECT name, email, video_path, upload_date FROM videos";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        echo "<div>";
        echo "<h3>" . htmlspecialchars($row['name']) . " (" . htmlspecialchars($row['email']) . ")</h3>";
        echo "<video controls width='400'>
                <source src='" . htmlspecialchars($row['video_path']) . "' type='video/mp4'>
                Your browser does not support the video tag.
              </video>";
        echo "<p>Uploaded on: " . $row['upload_date'] . "</p>";
        echo "</div><hr>";
    }
} else {
    echo "No videos found.";
}
$conn->close();
