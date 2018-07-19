import sys
import os.path
import re
from datetime import datetime

try:
    if len(sys.argv) > 1:
        print "IP file name:", sys.argv[1]
        ip_file = sys.argv[1]
    else:
        assert False, "Specify input file"

    if not os.path.isfile(ip_file):
        assert False, "Input file not present"
    with open(ip_file, 'r') as fp:
        fd = fp.read()

        match = re.findall('^[0-9]{4}/[0-9]{2}/[0-9]{2}\s+(.*)\s+UTC\s*#+\s*[STARTED|ENDED].*:\s*(.*)\s+#+', fd, re.M)

        # print match
        # print len(match)

    di = {}
    for i in match:
        if i[1] in di.keys():
            di[i[1]].append(i[0])
        else:
            di[i[1]]=[i[0]]

    print "#" *20
    print di
    print "#" * 20

    tm_frmt = '%H:%M:%S'
    op_file = os.path.splitext(ip_file)[0]+"_out.txt"
    with open(op_file, 'w') as fp:
        for k, v in di.items():
            if len(v) == 2:
                tdelta = datetime.strptime(v[1], tm_frmt) - datetime.strptime(v[0], tm_frmt)
                # print "{0: <80}:{1}".format(k, tdelta)
                # print tdelta.total_seconds()
                fp.write("{0: <80} > {1}".format(k.strip(), tdelta.total_seconds()))
                fp.write("\n")
            else:
                print k, " : ", v

    print "Completed"

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
