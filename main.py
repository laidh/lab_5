import re
from pprint import pprint

def main():
    log_file = 'C:/Users/admin/Desktop/IoT/math/lab_5_fixed/log.txt'
    count = 0

    with open(log_file, mode="r") as file:
        text = file.read()
        result1 = re.findall(r'\[02/Mar/2004:09:[1-5][4-9]:5[6-9] \+0200] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result2 = re.findall(r'\[02/Mar/2004:09:[1-5][5-9]:[0-5][0-9] \+0200] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result3 = re.findall(r'\[02/Mar/2004:1[0-9]:[0-5][0-9]:[0-5][0-9] \+0200] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result4 = re.findall(r'\[02/Mar/2004:2[0-4]:[0-5][0-9]:[0-5][0-9] \+0200] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result5 = re.findall(r'\[0[3-9]/Mar/2004:[0-1][0-9]:[0-5][0-9]:[0-5][0-9] \+0200] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result6 = re.findall(r'\[0[3-9]/Mar/2004:2[0-4]:[0-5][0-9]:[0-5][0-9] \+0200] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result7 = re.findall(r'\[15/Mar/2004:0[0-9]:[0-5][0-9]:[0-5][0-9] \+0200] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result8 = re.findall(r'\[15/Mar/2004:1[0-4]:[0-5][0-9]:[0-5][0-9] \+0200] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result9 = re.findall(r'\[15/Mar/2004:12:0[0-9]:[0-5][0-9] \+0200] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result10 = re.findall(r'\[15/Mar/2004:12:10:[0-5][0-9] \+0200] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result11 = re.findall(r'\[15/Mar/2004:12:11:[0-4][0-9] \+0200] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result12 = re.findall(r'\[15/Mar/2004:12:11:5[0-5] \+0200] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        #result100 = re.findall(r'\[\d\d/Mar/\d\d\d\d:\d\d:\d\d:\d\d \+0200] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)

        result1_1 = re.findall(r'\[02/Mar/2004:09:[1-5][4-9]:5[6-9] \+0100] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result2_1 = re.findall(r'\[02/Mar/2004:09:[1-5][5-9]:[0-5][0-9] \+0100] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result3_1 = re.findall(r'\[02/Mar/2004:1[0-9]:[0-5][0-9]:[0-5][0-9] \+0100] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result4_1 = re.findall(r'\[02/Mar/2004:2[0-4]:[0-5][0-9]:[0-5][0-9] \+0100] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result5_1 = re.findall(r'\[0[3-9]/Mar/2004:[0-1][0-9]:[0-5][0-9]:[0-5][0-9] \+0100] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result6_1 = re.findall(r'\[0[3-9]/Mar/2004:2[0-4]:[0-5][0-9]:[0-5][0-9] \+0100] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result7_1 = re.findall(r'\[15/Mar/2004:0[0-9]:[0-5][0-9]:[0-5][0-9] \+0100] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result8_1 = re.findall(r'\[15/Mar/2004:1[0-4]:[0-5][0-9]:[0-5][0-9] \+0100] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result9_1 = re.findall(r'\[15/Mar/2004:12:0[0-9]:[0-5][0-9] \+0100] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result10_1 = re.findall(r'\[15/Mar/2004:12:10:[0-5][0-9] \+0100] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result11_1 = re.findall(r'\[15/Mar/2004:12:11:[0-4][0-9] \+0100] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        result12_1 = re.findall(r'\[15/Mar/2004:12:11:5[0-5] \+0100] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)
        #result100_1 = re.findall(r'\[\d\d/Mar/\d\d\d\d:\d\d:\d\d:\d\d \+0200] "GET /\w*/\w*/\w*\.\w* \w*/\d\.\d" 200', text)

    result = []
    result.extend(result1)
    result.extend(result2)
    result.extend(result3)
    result.extend(result4)
    result.extend(result5)
    result.extend(result6)
    result.extend(result7)
    result.extend(result8)
    result.extend(result9)
    result.extend(result10)
    result.extend(result11)
    result.extend(result12)
    #result.extend(result100)

    result.extend(result1_1)
    result.extend(result2_1)
    result.extend(result3_1)
    result.extend(result4_1)
    result.extend(result5_1)
    result.extend(result6_1)
    result.extend(result7_1)
    result.extend(result8_1)
    result.extend(result9_1)
    result.extend(result10_1)
    result.extend(result11_1)
    result.extend(result12_1)
    #result.extend(result100_1)

    for item in result:
        count += 1
        result.sort()

    print(f"Accomplished GET requests: {count}")
    pprint(result)

if __name__ == '__main__':
     main()