import string

def switch_dict(raw_headers):
    
    '''将键值对转换成字典'''
    
    data = [line.split(": ",1) for line in raw_headers.strip().split("\n")]
    headers = dict((x for x in data))
    return headers


def Form(file_name):
    
    '''识别汉字，注释代码'''
    
    letters = string.ascii_letters + string.digits + "#"
    with open(file_name,"r",encoding="utf-8") as f:
        file_re = f.readlines()
    with open(file_name,"w+",encoding="utf-8") as f:
        for i in file_re:
            if i[0] in letters:
                f.write(i)
            else:
                f.write("# "+i)
    return "over!"
