def blotto(A,B, a_name='', b_name=''):
    """execute a colonel blotto battle between A & B players"""
    if(len(A) != len(B)):
       print 'fronts mismatch'
       return
    if (a_name == '') & (b_name == ''): 
        text = False 
    else: text = True
    
    battles = [0,0]

    for i in range(len(A)):
        if A[i] > B[i]: battles[0] += 1
        if A[i] < B[i]: battles[1] += 1

    if battles[0] > battles[1]: 
        if text: print a_name, " wins vs ", b_name
        return [1,0]
    if battles[0] < battles[1]: 
        if text: print b_name, " wins vs ", a_name
        return [0,1]
    if battles[0] == battles[1]: 
        if text: print a_name, " ties ", b_name
        return [0,0]

    
def battle(L):
    end = len(L)
    N = range(end) 

    score = [0 for i in N]

    for i in N:
        for j in N[i+1:]:  
            score[i] += blotto(L[i],L[j], 'team' + str(i+1), 'team'+ str(j+1))[0] 
            score[j] += blotto(L[i],L[j])[1]
                
    return score

def contest(players):
    
    for match in players:
        num = players.index(match)
        num += 1
        team = 'team{}'.format(num)
        strategy = ''
        for j in match:
            strategy = strategy + '\t' + str(j)
        
        print team, strategy, '\n'
    
    results = battle(players)
    scores, banner = '\t', '\t'
    
    for i in range(len(players)):
        banner = banner + 'team{}'.format(str(i+1)) + '\t'
        scores = scores + str(results[i]) + '\t'
    
    print '\nSCOREBOARD\n', banner, '\n', scores, '\n'
    
    return '\n\n\n'

# To run a sample contest, first enter a few strategies in a list:

match_a = [
            [2,0],
            [1,1],
          ]

match_b = [
            [20,20,20,20,20],
            [30,30,30,10,0],
          ]

match_c = [
            [1,2,3],
            [2,3,1],
            [3,1,2],
          ]

match_d = [
            [0,0,6],
            [2,4,0],
            [3,3,3],
          ]

match_e = [ 
            [10,10,10,10,10,10,10,10,10,10],
            [9,9,9,9,9,9,9,9,9,19],
            [9,11,9,11,9,11,9,8,0,20],
            [20,0,19,1,18,2,17,3,16,4],
          ]

match_f = [ 
            [10,10,10,10,10,10,10,10,10,10, 0],
            [9,9,9,9,9,9,9,9,9,19, 0],
            [9,11,9,11,9,11,9,8,0,20, 0],
            [20,0,19,1,18,2,17,3,16,3,1],
          ]

match_g = [
            [2,2,2,2,2],
            [4,3,3,0,0],
          ]

      
print contest(match_a)
print contest(match_b)
print contest(match_c)
print contest(match_d)
print contest(match_e)
print contest(match_f)
print contest(match_g)
