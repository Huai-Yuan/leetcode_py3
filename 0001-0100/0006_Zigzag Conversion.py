class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        len_s = len(s)
        sp = numRows + numRows - 2
        list_sp = list(range(sp-2, 0, -2))
        # head
        s_ = s[::sp]
        # mid
        if numRows > 2:
            temp = 1
            for i in list_sp:
                temp_1 = s[temp::sp]
                temp_2 = s[temp+i::sp]
                while True:
                    if len(temp_1)==0 and len(temp_2)==0:
                        break
                    s_ += temp_1[0]
                    temp_1 = temp_1[1:]
                    if len(temp_1)==0 and len(temp_2)==0:
                        break
                    s_ += temp_2[0]
                    temp_2 = temp_2[1:]

                temp += 1
        # tail
        s_ += s[numRows-1::sp]
        return s_