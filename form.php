<form action="process.php" method="GET">
Mac Address<input type="text" name="mac" required>
<br>
DHCP Version
<select name="version" required>
    <option value="4">DHCPv4</option>
    <option value="6">DHCPv6</option>
</select>
<br>
<input type="submit" value="Submit">
</form>