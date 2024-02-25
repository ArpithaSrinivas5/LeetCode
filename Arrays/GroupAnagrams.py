import collections


class GroupAnagrams:
    def Group_Anagrams (self, strs: list[str]) -> list[list[str]] :
        ans = collections.defaultdict(list)

        for s in strs :
            count= [0] * 26

        for c in s:
            count[ord(c)- ord("a")] +=1
            print(count)
            ans[tuple(count)].append(s)
        return ans.values()

    


# Example usage:
if __name__ == "__main__":
    anagram_grouper = GroupAnagrams()
    strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = anagram_grouper.Group_Anagrams(strings)
    print(result)
