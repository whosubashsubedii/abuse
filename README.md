


### 🛡️ IP Abuse Notification Generator

This Python script helps generate a pre-written abuse report email when a malicious IP address is reported. It is especially useful for network administrators or security personnel at ISPs like WorldLink.

---

### 🧰 Features

* Prompts for user input to collect:

  * Malicious IP address
  * Reporter’s name
  * Customer name
  * Customer address
* Outputs a structured, formal abuse notification email.
* Ideal for handling botnet-related IP abuse reports.

---

### 🖥️ How to Use

1. Open your terminal or command prompt.

2. Run the script using Python 3:

   ```bash
   python3 abuse_report_generator.py
   ```

3. Enter the requested information:

   ```
   Enter the IP of customer: 203.0.113.45  
   Enter the IP reporter name: Spamhaus  
   Enter the name of customer: ABC Pvt. Ltd.  
   Enter the address of customer: Baneshwor, Kathmandu  
   ```

4. The script will generate a formatted email ready to copy and send.

---

### 📝 Example Output

```
Dear Sir / Madam, 

Warm Greetings from WorldLink..!

We have detected malicious requests from the IP:203.0.113.45 as reported by Spamhaus.

While checking from our database, this IP is of ABC Pvt. Ltd.-Baneshwor, Kathmandu

It is due to “bot” attacks. Bot is created when a device is penetrated by software from a malware (malicious software) distribution.

Server is being used as a “bot” to send malicious attacks over the internet.

Some of the PCs or end devices at your end may be affected by botnet which may be cause for the attacks.

So, we would request you to check the devices at your internal n/w and implement proper firewall / security.
```

---

### 📦 Requirements

* Python 3.x
* No external libraries needed

---

### 👨‍💻 Author

**Subash Subedi**
