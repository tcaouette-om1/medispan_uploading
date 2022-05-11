import os, shlex, subprocess
from subprocess import call
import put_file
import medispan_qc
import medispan_use_db_create_tables
import medispan_copyinto
# VPN needs to be connected :)
# need to build main controller main()
# this file is used to connect to snowsql client and run the files denoted by -f flag. these directories need to be updated for each new user.
# change location of the files before running. check the files for complete setup.
# files being passed - put_file.sql, medispan_create_tables.sql, medispan_copyinto.sql
# scripts being used - medispan_use_db_create_tables.py, medispan_copyinto.py

#param below into a function and passing in my_conn, and the following sql file locations

#os.system('''snowsql -c my_conn -f /Users/tobiascaouette/Documents/put_file.sql  -f /Users/tobiascaouette/Documents/medispan_create_tables.sql -f /Users/tobiascaouette/Documents/medispan_copyinto.sql -f /Users/tobiascaouette/Documents/medispan_qc.sql''')


dir = r"/Users/tobiascaouette/Documents/"
def find_files(dir):
    list_files=[]
    for file in os.listdir(dir):
        if file.endswith("put_file.sql"):
            list_files.append(os.path.join(dir, file))
        if file.endswith("medispan_create_tables.sql"):
            list_files.append(os.path.join(dir, file))
        if file.endswith("medispan_copyinto.sql"):
            list_files.append(os.path.join(dir, file))
        if file.endswith("medispan_qc.sql"):
            list_files.append(os.path.join(dir, file))
    return sorted(list_files)


print(find_files(dir))

def os_system(list_files):
    for i in list_files:
        if i.endswith("put_file.sql"):
            put = i
        if i.endswith("medispan_create_tables.sql"):
            create = i
        if i.endswith("medispan_copyinto.sql"): 
            copyinto = i
        if i.endswith("medispan_qc.sql"): 
            qc = i
    gravy = f""" snowsql -c my_conn -f {put} -f {create} -f {copyinto} -f {qc}"""
    os.system(gravy)




    
def main():
    put_file
    medispan_use_db_create_tables
    medispan_copyinto
    medispan_qc
    files = find_files(dir)
    os_system(files)

if __name__ == "__main__":
	main()