def Atbash_cipher(pre_cypher):
    """
    The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter
     A <=> Z; B <=> Y; C <=> X; etc.
     """

    alphabet_low_first = "abcdefghijklm"
    alphabet_low_second = "zyxwvutsrqpon"
    alphabet_cap_first = "ABCDEFGHIJKLM"
    alphabet_cap_second = "ZYXWVUTSRQPON"

    post_cypher = ""
    for character in range(0, len(pre_cypher)):
        if alphabet_low_first.find(pre_cypher[character]) != -1:
            post_cypher += alphabet_low_second[alphabet_low_first.find(pre_cypher[character])]
        elif alphabet_low_second.find(pre_cypher[character]) != -1:
            post_cypher += alphabet_low_first[alphabet_low_second.find(pre_cypher[character])]
        elif alphabet_cap_first.find(pre_cypher[character]) != -1:
            post_cypher += alphabet_cap_second[alphabet_cap_first.find(pre_cypher[character])]
        elif alphabet_cap_second.find(pre_cypher[character]) != -1:
            post_cypher += alphabet_cap_first[alphabet_cap_second.find(pre_cypher[character])]
        else:
            post_cypher += str(pre_cypher[character])
    return post_cypher
