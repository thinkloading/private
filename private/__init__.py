import string

def switch_dict(raw_headers):
    data = [line.split(": ",1) for line in raw_headers.strip().split("\n")]
    headers = dict((x for x in data))
    return headers

letters = string.ascii_letters + string.digits + "#"
def Form(file_name):
    with open(file_name,"r",encoding="utf-8") as f:
        file_re = f.readlines()
    with open(file_name,"w+",encoding="utf-8") as f:
        for i in file_re:
            if i[0] in letters:
                f.write(i)
            else:
                f.write("# "+i)
    return "over!"
