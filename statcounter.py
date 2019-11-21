def statcounter():
    f = {}
    f_new = yield f

    def counter(passed):
        f.setdefault(passed, 0)

        def wrap(*args, **kwargs):
            f[passed] += 1
            res = passed(*args, **kwargs)
            return res

        return wrap

    while f_new:
        f_new = yield counter(f_new)
