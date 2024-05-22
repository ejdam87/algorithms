
Matching = dict[int, int]
Preference_list = dict[list[int]]

def is_matched(m: Matching, s: int) -> int | None:
    for h, s_present in m.items():
        if s == s_present:
            return h
    
    return None

def stable_matching(h_preferences: Preference_list, s_preferences: Preference_list) -> Matching:
    
    # hospital -> set of students
    proposals = {}  # hospitals make proposals
    for h in h_preferences.keys():
        proposals[h] = set()

    m = {}

    change = True
    while change:

        change = False
        for h, preferences in h_preferences.items():
            if h in m:
                continue
            
            if len(proposals[h]) == len(s_preferences): # h proposed to everyone
                continue
            
            for s in preferences:
                if s in proposals[h]:
                    continue

                # first student which was not proposed by h
                proposals[h].add(s)
                change = True

                # if s unmatched
                h_dash = is_matched(m, s)
                if h_dash is None:
                    m[h] = s
                    break
                else:
                    # if s is matched (with a hospital h'), but h is higher in his preferences than h'
                    for pref in s_preferences[s]:
                        if pref == h:
                            m[h] = s
                            del m[h_dash]
                            break
                        # else he rejects h
                        if pref == h_dash:
                            break

    return m


ATLANTA = 1
BOSTON = 2
CHICAGO = 3

XAVIER = 4
YOLANDA = 5
ZEUS = 6

h_pref = { ATLANTA: [XAVIER, YOLANDA, ZEUS],
           BOSTON:  [YOLANDA, XAVIER, ZEUS],
           CHICAGO: [XAVIER, YOLANDA, ZEUS] }

s_pref = {
    XAVIER:  [BOSTON, ATLANTA, CHICAGO],
    YOLANDA: [ATLANTA, BOSTON, CHICAGO],
    ZEUS:    [ATLANTA, BOSTON, CHICAGO]
}

print(stable_matching(h_pref, s_pref))
