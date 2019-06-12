## Double Trouble [Forensics | HSCTF 6 | 2019]


1. Run `zsteg koala.png`, we get a link, go to it and download file `hmmm.txt`.
2. Run `zsteg koala2.png`, we get a string `whatdowehavehere`
3. On running `file hmmm.txt`, we can see it is  `GPG: AES encrypted`
4. Run `gpg -d hmmm.txt` and use password: `whatdowehavehere` (obtained from step 2)


		Flag: hsctf{koalasarethecutestaren'tthey?}
