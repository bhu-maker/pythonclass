alpha = 0
beta = 0
def fn1(chance=1):
    global alpha,beta
    try :
        alpha=int(input("enter the alpha value : "))
        beta=int(input("enter the beta value : "))
        alpha=alpha*beta
        beta=alpha//beta
        alpha=alpha//beta

    except ValueError as ve :
        print(ve,"\n enter the whole number ")
        raise ve
    finally:
        print(alpha,beta)

try :
    fn1()
except ValueError as ve :
    alpha=int(input("enter the alpha value : "))
    beta=int(input("enter the beta value : "))
    alpha=alpha*beta
    beta=alpha//beta
    alpha=alpha//beta
finally:
        print(alpha,beta)

