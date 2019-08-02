# coding=utf-8
import subprocess


def system_command(command):
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=None,
                               shell=True)
    result = process.stdout.readlines()
    lists = []
    for line in result:
        output = line.decode('gbk')
        # print(output)
        lists.append(output)
    return lists


if __name__ == "__main__":
    # import locale
    # print(locale.getdefaultlocale())
    # result = system_command('d:/sln/python/Shell2TSql/shell/sql.sh')
    sql = "sqlcmd -U sa -P 123456 -d \"Demo\" -Q \"select * from User_list\" -u -s \",\""
    result = system_command(sql)
    # print(repr(result))
    i = 0
    list_len = len(result)
    tableHead = []
    tableBody = []
    for line in result:
        i += 1
        if i == 1:
            tr = line.split(",")
            for td in tr:
                tableHead.append(td.strip())
            pass

        if (i > 2 and i < list_len - 1):
            tr = line.split(",")
            trRow = {}
            for index in range(len(tr)):
                # trRow.append({tableHead[index]: tr[index].strip()})
                trRow[tableHead[index]] = tr[index].strip()
                # print(trRow)
                # print(repr({tableHead[index]: tr[index].strip()}) + "\r\n")
                pass
            tableBody.append(trRow)
            result = system_command('d:/sln/python/Shell2TSql/shell/redis.sh')
            # rediscli = 'redis-cli -h 127.0.0.1 -p 6379 SET User_list_1 "{\"UserId\": \"1\", \"UserName\": \"钟海\", \"orgid\": \"22\", \"flag\": \"1\", \"isjjr\": \"9\", \"RzRuzhiDate\": \"2019-07-11 14:55:01.690\", \"lasttime\": \"2019-07-11 14:55:01.690\", \"CompanyId\": \"1\"}"'
            # res = system_command(rediscli)
            pass
        pass
    print(tableBody)
