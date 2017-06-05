# black-list-parser
This little script for forming hosts at our system.

Requirements:
independency from any other devices
consistency on all of places
little and fast

Solution:
1. I plan to use python. Because it popular and present at almost every my device.
2. I found that best way is to create blocking at end device - because they are mobile -> change network connection time to time.
3. For consistency need that blocklist be newest - weekly or mounthly updating.

So for implement this I get blocklist from popular resources. Parse them into temp file (clear dublicates and formating all FQDN to one view). After copy temp file to hosts.
After all need only do manual-reboot device.
