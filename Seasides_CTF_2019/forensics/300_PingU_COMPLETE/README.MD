
On analyzing traffic.pcap with wireshark, we can easily get the answer to the first few questions(see `wireshar_ss.png`).

After that,
`wireshark -> File -> Export Objects -> as HTTP -> export actiV.bin`
<br/>
Drop the file on this link: `https://emn178.github.io/online-tools/sha256_checksum.html`
and get the sha256.

We can see the 'type of infection' from the given `alerts.txt` file.

```

What is the IP address of the infected Windows host :- 172.17.8.109 
What is the MAC address of the infected Windows host :- 14 fe b5 d4 15 ca 
What is the host name of the infected Windows host:- Dunn-Windows-PC 
What is the Windows user account name for the infected Windows host :-timbershade 
What is the SHA256 file hash of the Windows executable file sent to the infected Windows host? :-9f6e3e65aedca997c6445329663bd1d279392a34cfda7d1b56461eb41641fa08 
Based on the IDS alerts, what type of infection is this? :- Trojan.Dridex

```

Mail this to the admin and they sent us the flag !

flag: 
