
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
            morse = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",
            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-","-.--","--.."
            ]

            output=[]

            for word in words:
                morese_patter=''
                for letter in word:
                    value=ord(letter)-ord('a')
                    morese_patter+=morse[value]
                if morese_patter not in output:
                    output.append(morese_patter)
            return len(list(set(output)))