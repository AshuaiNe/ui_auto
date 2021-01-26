import time


def wrapper(func):
    def count_time(*args, **kwargs):
        print("计算时间的装饰器")
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("函数运行的时间为：{:.5f}".format(end_time - start_time))

    return count_time


users = {"token": "1"}


def login_check(func):
    def ado(*args, **kwargs):
        print("登录校验的装饰器")
        if not users["token"]:
            print("-----登录页面-------")
            username = input("账号：")
            password = input("密码：")
            if users["user"] == username and users["pwd"] == password:
                users["token"] = True
                func(*args, **kwargs)
        else:
            func()

    return ado


@login_check  # 第二步进行装饰  count_time---->func=login_check(func)    func指向的是ado这个函数
@wrapper  #  第一步进行装饰  func=wrapper(func)  func指向的是count_time这个函数。
def func():
    time.sleep(3)
    print("这是是需要被装饰器的函数")


#  从下往上装饰，从上往下执行
func()
