while IFS="" read -r lines || [ -n "$lines" ]
do
	echo "Password tried:" ${lines}
	steghide extract -sf file.jpg -p ${lines} > /dev/null
done < rockyou.txt