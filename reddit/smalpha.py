# Reddit challenge
# https://www.reddit.com/r/dailyprogrammer/comments/cn6gz5/20190807_challenge_380_intermediate_smooshed/
def reduce(smooshed, characters):
    # if 0 characters left return true
    if len(characters) == 0:
        return True
    # search for the character that has the lowest number of occurences across all smooshed
    mincount = (characters[0], smooshed.count(mc[characters[0]]))
    for c in characters:
        count = smooshed.count(mc[c])
        if count < mincount[1]:
            mincount = (c, count)
    # if lowest is 0 return false
    if mincount[1] == 0:
        return False
    # For each occurence reduce without that character in character list and replace the character morse code with the character
    start = 0
    charcode = mc[mincount[0]]
    l = len(charcode)
    for i in range(0,mincount[1]):
        loc = smooshed.find(charcode, start)
        res = reduce(smooshed[0:loc] + mincount[0] + smooshed[loc+l:], characters.replace(mincount[0], ''))
        start = loc+l
        # if return is false then continue
        if res == False:
            continue
        # if return is true then the last character was found so return the smooshed strings with the morse code
        #   of the character replaced by the character itself
        elif res == True:
            return smooshed[0:loc] + mincount[0] + smooshed[loc+l:]
        else:
            return res
    return False


# Alternately try reading first 4 characters at a time and matching on them
