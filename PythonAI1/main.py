import requests
def classify(text):
    key = "2ed3c350-048b-11ef-b72a-2d0baa07efe99e026781-799e-49b2-bf6b-91863bd06b6f"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"
    response = requests.get(url, params={ "data" : text })
    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

demo = classify("太好了")

label = demo["class_name"]
confidence = demo["confidence"]

print ("result: '%s' with %d%% confidence" % (label, confidence))