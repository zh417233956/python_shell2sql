#!/bin/bash 
exe_secelt(){
HOST_NAME="192.168.4.144"
USER_NAME="sa"
PASS_WORD="xxxx"
DBNAME="Demo"
TABLE_NAME=$1
TABLE_NAME=${TABLE_NAME:-"User_list"}
select_sql="select * from ${TABLE_NAME}"
# sqlcmd -S ${HOST_NAME} -U ${USER_NAME} -P ${PASS_WORD} -d ${DBNAME} -q "${select_sql}"
sqlcmd -U sa -P xxxx -d "Demo" -Q "DECLARE @return_value int; EXEC @return_value = [dbo].[procTest];print @return_value"
RETN="$?"
echo $RETN
}
exe_secelt $1

# sqlcmd -U sa -P xxxx -d "Demo" -1"select * from User_list"
