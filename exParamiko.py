from paramiko import client
import time
server = "10.78.216.104"
username = "root"
password = "generic@123"


command_seq = ["cat /root/rajarajan/aurora_cdvr_sanity_tests/config/chn_nfr/config.yaml | grep 'ssh_userid'"]
def initial():

    con = client.SSHClient()
    con.set_missing_host_key_policy(client.AutoAddPolicy())
    con.connect(hostname=server, username=username, password=password)

    print dir(con)
    print con.get_transport()
    sh = con.invoke_shell()
    print dir(sh)
    #i,o,e = sh.exec_command("pwd")
    #print o.read()

    if con:
        for cmd in command_seq:
            i, o, e = con.exec_command(cmd)
            print "Output :", o.read()
            if e.read():
                print "Error :", e.read()
            time.sleep(1)

    else:
        print "Error in making a connection"


if __name__ == "__main__":
    initial()