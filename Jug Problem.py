def jugProblem(cap1, cap2):
    jug1 = 0
    jug2 = 0
    cap1 = cap1
    cap2 = cap2


    jug1 = cap1
    print "jug1",jug1
    jug2 = cap2
    print "jug2",jug2
    jug1 = jug1-cap2
    print "jug1", jug1
    jug2 = jug1
    print "jug1",jug1
    jug1 = 0
    print "jug2", jug2
    jug1 = cap1
    print "jug1", jug1

    jug1 = cap1 - (cap2-jug2)
    print "jug1", jug1
    print "End"
    
jugProblem(5,3)