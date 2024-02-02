import requests
import json

if __name__ == "__main__":
    json_dump = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    # print(json_dump)

    file_name = "jsonplaceholder.txt"
    limit = 100

    writed_dict = []
    for index, item in enumerate(json_dump):
        if index >= limit:
            break
        writed_dict.append(item)


    with open(file_name, "w", encoding="utf-8") as f:
        for i in writed_dict:
            f.write(str(i) + ",\n" )