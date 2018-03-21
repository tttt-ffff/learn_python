class prm_num:
    def print_prm_num( self, x ):
        for i in range(x+1):
            if i == 0:
                continue
        for j in range(i):
            if j <= 1:
                continue
            if i % j == 0:
                if i == j:
                    print('prm_num:'+str(i))
                else:
                    break


test_num = prm_num()
test_num.print_prm_num(10)