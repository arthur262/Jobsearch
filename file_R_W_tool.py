def write_file(pageSource,filename):
    with open('./'+filename, 'w',encoding='utf-8') as f:
        f.write(pageSource)
        
def readfile(filename):
    with open('./'+filename, 'r',encoding='utf-8') as f:
        return f.read()
        
