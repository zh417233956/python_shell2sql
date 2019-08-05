# coding=utf-8
import subprocess


def system_command(command):
    lists = []
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    # for line in iter(process.stdout.readline, 'b'):
    result = process.stdout.readlines()
    for line in result:
        output = line.decode('gbk')
        print(output)
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
            jsonStr = repr(trRow).replace("'", "\\\"")
            redisCli = "redis-cli --raw -h 127.0.0.1 -p 6379 -n 1 SET " + "User_list_" + tr[
                0].strip() + " \"" + jsonStr + "\""
            system_command(redisCli)

            # # 使用redis.sh传参数
            # jsonStr = repr(trRow).replace("'", "\"").replace(": ", ":").replace(", ", ",").replace(" ", "\\T")
            # print(jsonStr)
            # system_command([
            #     'd:/sln/python/Shell2TSql/shell/redis.sh',
            #     "User_list_" + tr[0].strip(), "'" + jsonStr + "'"
            # ])
            pass
        pass
    print(tableBody)
