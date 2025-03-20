<?php
$numbers = $_GET['mac'];
$threshold = $_GET['version'];

$command = escapeshellcmd("python3 network_config.py $mac $version");

$output = shell_exec($command);
echo $output;
?>