# 10th December 2024 Update
I recreated the venv using `uv` with Python 3.13.1
When I re-ran `first_text.py` I got an exception stating that the number I was using didn't match my account.
Logging in to Twilio I can no longer see any text numbers.
I'm not sure if they only have paid numbers now or if free numbers expire. In any case I'm leaving it for now as I'm not using Twilio SMS at the moment.

# Twilio SMS
My first play with Twilio SMS

# Status Update
I had a bunch of issues getting started with my Trial Account.  
Eventually I got it all working and I believe the issues were due to:
- System Outages (I guess I was just unlucky)
- An issue with adding Verified Caller IDs

# Pricing
There are several moving parts and I'm not certain of them all:
- Each SMS costs about 4p
- You need to lease a Twilio Phone Number to send from which costs $1.15 per month (Yes, it was listed in dollars)
- There is an additional carrier charge to be added to each SMS. I think that is about 1 or 2 pence per SMS but I don't know how to predetermine the exact cost.
- I don't know if upgrading to a Paid Account means that there is another additional charge, or if it simply means that you need to add some kind of payment method.

# Conclusion
I got this all working and it's pretty cool.  
However I'm unsure of the complete pricing and Shayne Sivley on PyBites told me about nty.sh which allows free alerts (with some caveats)
So I think I'll give nty.sh a go first.