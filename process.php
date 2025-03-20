<?php
$mac = $_GET['mac'];
$version = $_GET['version'];

$command = escapeshellcmd("python3 network_config.py $mac $version");

$output = shell_exec($command);
echo $output;
?>