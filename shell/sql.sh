
#!/bin/bash
 
exe_secelt(){
HOST_NAME="192.168.4.144";
USER_NAME="sa";
PASS_WORD="123456";
DBNAME="Demo";
TABLE_NAME="User_list";
select_sql="select * from ${TABLE_NAME}"; 
 
sqlcmd -S ${HOST_NAME} -U ${USER_NAME} -P ${PASS_WORD} -d ${DBNAME} -Q "${select_sql}"
# sqlcmd -U sa -P 123456 -d "Demo" -Q "select * from User_list"
}
exe_secelt "$HOST"

# sqlcmd -U sa -P 123456 -d "Demo" -Q "select * from User_list"