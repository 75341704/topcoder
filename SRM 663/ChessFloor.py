# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class ChessFloor:
    def minimumChanges(self,floor):
        a=[]
        for s in floor:
            t=set(s)
            a=list(t)+a
            a=list(set(a))

        def changes(c1,c2,f):
            n=len(f)
            t=0
            for k in range(n):
                for l in range(n):
                    tmp=f[k][l]
                    if k%2==0 and l%2==0 and tmp!=c1:
                        t=t+1
                    elif k%2==1 and l%2==1 and tmp!=c1:
                        t=t+1
                    elif k%2==1 and l%2==0 and tmp!=c2:
                        t=t+1
                    elif k%2==0 and l%2==1 and tmp!=c2:
                        t=t+1
            return t
        mmin=None
        al=len(a)
        for i in range(al):
            c1=a[i]
            for j in range(i+1,al):
                c2=a[j]
                t1=changes(c1,c2,floor)
                t2=changes(c2,c1,floor)
                mm=min(t1,t2)
                if mmin==None:
                    mmin=mm
                elif mmin>mm:
                    mmin=mm
        return mmin    
    def get(self,f,x,y):
        x=chr(ord('a')+x)
        y=chr(ord('a')+y)
        want=(x,y)
        ret=0
        n=len(f)
        for i in xrange(n):
            for j in xrange(n):
                if f[i][j]!=want[(i+j)&1]:
                    ret+=1
        return ret
    def minimumChanges2(self, floor):
        ans=100500
        for fi in range(26):
            for se in range(26):
                if fi!=se:
                    ans=min(ans,self.get(floor,fi,se))
        return ans

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(floor, __expected):
    startTime = time.time()
    instance = ChessFloor()
    exception = None
    try:
        __result = instance.minimumChanges(floor);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("ChessFloor (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("ChessFloor.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            floor = []
            for i in range(0, int(f.readline())):
                floor.append(f.readline().rstrip())
            floor = tuple(floor)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(floor, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1437703540
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
