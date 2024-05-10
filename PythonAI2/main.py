import requests
def classify(text):
    key = "6396e8b0-0558-11ef-8488-8fa1b8b668f704394702-d603-4f91-9803-5d55d2917d33"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"
    response = requests.get(url, params={ "data" : text })
    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def answer_question():
    question = input(">")
    answer = classify(question)
    answerclass = answer["class_name"]
    confidence = answer["confidence"]

    if confidence <75:
        print("我们不太明白你的意思，你可以尝试问我其他问题")
    elif answerclass == "address":
        print("我们学校位于上海市徐汇区龙吟路99号")
    elif answerclass == "class":
        print("我们学校有4个班级，每个年级8个班级，一共有32个班级")
    elif answerclass == "lab":
        print("我们学校除了常规实验室以外，还有不少创新型实验室，一共有15间如：电子工程、3D打印、微生物、VR、无人机、人工智能等等")
    elif answerclass == "student":
        print("我们学校每个班级大约50人左右，全校大概有1500多人")
    elif answerclass == "teacher":
        print("我们学校有各学科老师100多人")
print("你想了解关于我们学校的什么")
while True:
    answer_question()