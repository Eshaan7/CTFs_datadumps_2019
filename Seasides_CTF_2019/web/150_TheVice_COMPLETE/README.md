on visiting the given link, we get JSON data with 

	uuid=202cb962ac59075b964b07152d234b70

which is the md5 hash of *'123'* 
so 
fire up `burpsuite -> intruder -> bruteforce md5 of 1-100.` 

For,

	uuid=6c8349cc7260ae62e3b1396831a8398f

i.e. md5 hash of `45`, we get the flag! (check `uuid_flag_ss.png`)

	flag = SEA{intriguing_idawwr}SIDES
