<?php
$hexColor = $_POST['hexColor'];

$pythonScript = "index.py";  // Path to your Python script

exec("python3 $pythonScript $hexColor", $output);

$result = json_decode($output[0]);

echo json_encode($result);
?>
