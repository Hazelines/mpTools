
<?php 
    // include './assets/menu.php';

    $param1 = "MDMS";

    $command = escapeshellcmd('python assets/python/connection.py '.$param1);
	$output = shell_exec($command);

    echo $output
?>

<link rel='stylesheet' href='./assets/bootstrap/css/bootstrap.min.css' />

<script src="./assets/js/jquery-3.6.0.min.js"></script>
<script src="./assets/bootstrap/bootstrap.min.js"></script>
<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>