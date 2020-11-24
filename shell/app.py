# coding=utf-8
import subprocess
import time
from time import strftime, localtime


def system_command(command):
    lists = []
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    result = process.stdout.readlines()
    for line in result:
        output = line.decode('gbk')
        print(output)
        lists.append(output)
    return lists


if __name__ == "__main__":
    while True:
        # print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
        # sql = "sqlcmd -S 192.168.6.99 -U sa -P 123!@#qwe -d \"test_pub\" -Q \"select @@SERVERNAME;select top 1 * from test_tab_2 order by id desc\" -u -s \",\""
        sql = "sqlcmd -S 192.168.6.99 -U sa -P 123!@#qwe -d \"test_pub\" -Q \"select @@SERVERNAME,GETDATE()\" -s \",\""
        sql = "sqlcmd -S 192.168.6.99 -U testuser1 -P 123 -d \"test_pub\" -Q \"select @@SERVERNAME,GETDATE()\" -s \",\""
        system_command(sql)
        time.sleep(1)
