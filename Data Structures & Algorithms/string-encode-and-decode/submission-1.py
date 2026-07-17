class Solution:
    def encode(self, strs: list[str]) -> str:
        # 1. Create an empty string to hold our final encoded message
        res = ""
        
        # 2. Loop through every word in the list
        for s in strs:
            
            # 3. Glue together: Length of word + "#" + the actual word
            # We must wrap len(s) in str() to convert the number to text!
            res += str(len(s)) + "#" + s
            
        # 4. Return the final glued string
        return res
        

    def decode(self, s: str) -> list[str]:
        # 1. Create an empty list for our final decoded words
        res = []
        
        # 2. 'i' is our main pointer scanning the string. It starts at index 0.
        i = 0
        
        # 3. Keep scanning until we reach the end of the string
        while i < len(s):
            
            # 4. 'j' is a scout pointer. We set it to 'i' and send it forward to find the '#'
            j = i
            while s[j] != '#':
                j += 1
                
            # 5. Now 'j' is pointing at the '#'. 
            # Everything between 'i' and 'j' is our length number!
            length = int(s[i:j])
            
            # 6. The actual word starts immediately after the '#' (which is j + 1).
            # The word ends at exactly (j + 1) + length.
            # We slice that word out and append it to our results!
            res.append(s[j + 1 : j + 1 + length])
            
            # 7. Move our main pointer 'i' forward so it sits right after the word we just grabbed,
            # ready to read the length of the next word!
            i = j + 1 + length
            
        return res

        
