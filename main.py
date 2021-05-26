import re
from datetime import datetime

def main():
    log_file = 'C:/Users/admin/Desktop/IoT/math/lab_5_fixed/log.txt'
    count = 0
    time_format = '%d/%b/%Y:%H:%M:%S'
    start_time = datetime.strptime("02/Mar/2004:09:14:56", time_format)
    end_time = datetime.strptime("15/Mar/2004:12:11:55", time_format)


    with open(log_file, mode="r") as file:
        patern = re.compile(r".+ .+ .+ \[(\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2}).+\] \"GET (.+) HTTP.+")
        for line in file:
            match = patern.search(line)
            if match:
                timestamp = datetime.strptime(match.group(1), time_format)
                if start_time < timestamp < end_time:
                    print(line)
                    count += 1
                if timestamp > end_time:
                    break

        print(f"Accomplished GET requests: {count}")

if __name__ == '__main__':
     main()