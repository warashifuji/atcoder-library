ok = 10 ** 10
ng = -1
def is_ok(arg):
    pass

def meguru_bisect(ng, ok):
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok