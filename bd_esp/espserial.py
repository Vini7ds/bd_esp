import serial
import time
from insert_bd import insert,update_state,check_exi
import sqlite3

ser = serial.Serial('COM3', 9600)
var_com = ''
#######################################################################
while True:
    var = str(ser.read(1))
    var_com = str(var_com+var)
    if var == "b\'\\n\'":
        break
var_com = var_com.replace("b\'", '').replace("\'", '').replace("\\r", '').replace("\\n", '')
############################################################################

if (check_exi("banco.db","ESP","DADO_LIDO",var_com)) == True:
    update_state("banco.db","ESP",var_com)
    print("Objeto atualizado no BD")
else:
    insert("banco.db", "ESP", var_com, "Viado")
    print("Objeto cadastrado no BD")