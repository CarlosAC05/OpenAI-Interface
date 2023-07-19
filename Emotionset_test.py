import Emotionset


def testneutrals():
    """
    checks the neutral cases
    """
    TempE=Emotionset.emotionSetter()
    TempE.neutralcheck(1,2,1,1)
    TempE.neutralcheck(1,1,1,1)
    


def testbounds():
    """
    tests whether the code function even if the int values are below 1 or above 3
    """
    TempE=Emotionset.emotionSetter()
    TempE.generate_greeting(0,0,0,0)
    TempE.generate_greeting(4,4,4,4)


testneutrals()
testbounds()