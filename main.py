import math

def h(x,n,q):
    R = -(x * x) * (2 * n - 1) / (2 * n + 1)
    q *= R
    return q

def k(x,eps,d,x2):
    n=0
    q=-x
    s=q
    while 1>0:
        n+=1
        q=h(x,n,q)
        s+=q
        if math.fabs(q) >= eps:
            continue
        else:
            break
    print(str(round(x,1)) + '     ' + str(math.pi / 2 - math.atan(x)) + '    ' + str(s + math.pi / 2) + '     ' + str(n))
    if x<x2:
        k(x + d, eps, d)

def main():
    x1 = float(input('x1='))
    x2 = float(input('x2='))
    d = float(input('d='))
    eps = float(input('eps='))
    x = x1
    print('X=            Ctg=                 S=                   n=')
    k(x,eps,d,x2)

if __name__=='__main__':
    main()
