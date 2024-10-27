ch_1 = int(input())
ch_2 = int(input())

ch_1_1 = ch_1 // 10
ch_1_2 = ch_1 % 10
ch_2_1 = ch_2 // 10
ch_2_2 = ch_2 % 10

max_ch = max(ch_1_1, ch_1_2, ch_2_1, ch_2_2)
min_ch = min(ch_1_1, ch_1_2, ch_2_1, ch_2_2)
sr_ch = ch_1_1 + ch_1_2 + ch_2_1 + ch_2_2 - max_ch - min_ch

print(max_ch * 100 + sr_ch % 10 * 10 + min_ch)
