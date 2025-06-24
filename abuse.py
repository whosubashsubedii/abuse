ip = input("Enter the ip of customer: ")
report =input ("Enter the ip reporter name: ")
cust = input("Enter the name of customer: ")
add = input("Enter the address of customer: ")

print (f""" 
Dear Sir / Madam, 

Warm Greetings from WorldLink..!


We have detected malicious requests from the IP:{ip} as reported by {report}.

While checking from our database, this IP is of {cust}-{add}

It is due to “bot” attacks. Bot is created when a device is penetrated by software from a malware (malicious software) distribution.

Server is being used as a “bot” to send malicious attacks over the internet.

Some of the PCs or end devices at your end may be affected by botnet which may be cause for the attacks.

So , we would request you to check the devices at your internal n/w and implement proper firewall / security.
""")

a = input()