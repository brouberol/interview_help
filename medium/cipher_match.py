# Determine if two strings are a cipher match.  Two strings are a cipher match
# if they have the same ordering of characters, even if the characters themselves
# are not the same.  For example, “aabb” and “ccdd” are a cipher match, as are
# “abccd” and “efggh”

def cypher_equals(str1, str2):
    return string_to_cypher(str1) == string_to_cypher(str2)


def string_to_cypher(s):
    cypher = []
    previous = s[0]
    for i, char in enumerate(s[1:]):
        delta = ord(char) - ord(previous)
        cypher.append(delta)
        previous = char
    return cypher
