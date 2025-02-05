import requests
import datetime
import time
from geopy.geocoders import Nominatim

#Enter your zipcode here
zipcode = 

#adjust the distance
distance = 30

geolocator = Nominatim(user_agent="my_geocoder")
location = geolocator.geocode({"postalcode": zipcode})
x = datetime.datetime.now()

start_date=x.strftime("%Y")+"-"+x.strftime("%m")+"-"+x.strftime("%d")

#retrieve token
url = "https://auth.hiring.amazon.com/api/csrf?countryCode=US"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept": "application/json",  
}
#token
response = requests.get(url, headers=headers)
#request parameters
data={
        "operationName":"searchJobCardsByLocation",
        "variables":{
            "searchJobRequest":{
                "locale":"en-US",
                "country":"United States",
                "geoQueryClause":{
                    "lat":location.latitude,
                    "lng":location.longitude,
                    "unit":"mi",
                    "distance":distance
                },
                "keyWords":"","equalFilters":[{
                    "key":"scheduleRequiredLanguage",
                    "val":"en-US"
                }],
                "containFilters":[{
                    "key":"isPrivateSchedule",
                    "val":["false"]
                }],
                "rangeFilters":[{
                    "key":"hoursPerWeek",
                    "range":{"minimum":0,"maximum":80}}],
                "orFilters":[],
                "dateFilters":[{
                    "key":"firstDayOnSite",
                    "range":{
                        "startDate":f"{start_date}"}
                }],
                "sorters":[{
                    "fieldName":"totalPayRateMax",
                    "ascending":"false"}],
                "pageSize":100,
                "consolidateSchedule":"true"
            }},
    "query":"query searchJobCardsByLocation($searchJobRequest: SearchJobRequest!) {\n  searchJobCardsByLocation(searchJobRequest: $searchJobRequest) {\n    nextToken\n    jobCards {\n      jobId\n      language\n      dataSource\n      requisitionType\n      jobTitle\n      jobType\n      employmentType\n      city\n      state\n      postalCode\n      locationName\n      totalPayRateMin\n      totalPayRateMax\n      tagLine\n      bannerText\n      image\n      jobPreviewVideo\n      distance\n      featuredJob\n      bonusJob\n      bonusPay\n      scheduleCount\n      currencyCode\n      geoClusterDescription\n      surgePay\n      jobTypeL10N\n      employmentTypeL10N\n      bonusPayL10N\n      surgePayL10N\n      totalPayRateMinL10N\n      totalPayRateMaxL10N\n      distanceL10N\n      monthlyBasePayMin\n      monthlyBasePayMinL10N\n      monthlyBasePayMax\n      monthlyBasePayMaxL10N\n      jobContainerJobMetaL1\n      virtualLocation\n      poolingEnabled\n      __typename\n    }\n    __typename\n  }\n}\n"}
#API endpoint
job_data_url="https://e5mquma77feepi2bdn4d6h3mpu.appsync-api.us-east-1.amazonaws.com/graphql"
data_headers = { 
    "Authorization": f"Bearer {response.json()['token']}",
    "Content-Type": "application/json"
}
job_data = requests.post(job_data_url, json=data, headers=data_headers)
search = True
jobs=job_data.json()['data']['searchJobCardsByLocation']['jobCards']

#continuously searches until match is found.
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
