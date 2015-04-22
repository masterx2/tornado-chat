<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Tornado Test server</title>
	<script src="static/js/main.js"></script>
</head>
<body>
<ul>
	{% for item in [x for x in range(10)] %}
		<li>
		<b>{{item}}</b> <span style="color: red;"> => </span> {{item*3}} 
		</li>
	{% end %}
</ul>
</body>
</html>