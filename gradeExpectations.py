def get_flaot(msg, fail = "Invalid."):
    try:
        ans = float(input(msg))
    except Exception as e:
        print(fail)
        return get_flaot(msg, fail)
    return ans

def get_int(msg, fail = "Invalid."):
    try:
        ans = int(input(msg))
    except Exception as e:
        print(fail)
        return get_int(msg, fail)
    return ans

def get_grade():
    num_probs = get_int("How many total standard problems are there? ")
    num_challenges = get_int("How many total challenge problems are there? ")

    probs_done = get_int("How many standard problems have you complete? ")
    challenges_done = get_int("How many challenge problems have you complete? ")

    prob_ratio = probs_done / num_probs
    challenge_ratio = challenges_done / num_challenges
    
    print(prob_ratio)
    print(challenge_ratio)

    if prob_ratio >= 1:
        if challenge_ratio >= (2.0/3.0):
            print("Student earned: A")
        elif challenge_ratio >= (1.0/3.0):
            print("Student earned: B")
        else:
            print("Student earned: C")
    else:
        print("Student earns: F")
    
get_grade()
            
            
    