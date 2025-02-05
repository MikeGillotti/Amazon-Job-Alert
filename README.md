## Amazon Alerts
A simple script that generates an output when warehouse jobs are available nearby.

Job opportunities come and go immediately, and I've found the built-in email alert system to not be reliable, so I wanted to create a solution for that.
## Usage

```python
#Enter your zipcode here
zipcode=90210

#Distance in miles
distance=30
```
## Customize Functionality
At the moment, the alert is just printed in the console. Feel free to implement additional functionality for email/text alerts.

```python
while search:
    if jobs:
#For added functionality, implement a script that sends you the results by email here
        for job in jobs:
            print(job['jobTitle'])
            print(job['locationName'])
            print(job['totalPayRateMinL10N'])
            print("https://hiring.amazon.com/app#/jobDetail?jobId="+job['jobId'])
            print("---")
        search=False
    else:
        print("no jobs found")
#Adjust update time here
        time.sleep(5)
```
