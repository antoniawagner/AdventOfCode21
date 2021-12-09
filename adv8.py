#%%
with open('/home/antonia/Documents/AdventCode/adv8.dat', 'r') as f:
    data=f.read()
    signal_output_list=[[[entry for entry in signal_output.split(' ') if entry!=''] for signal_output in line.split('|') if signal_output!=''] for line in data.split('\n') if line!='']
#%%
output_occurence_1478=0
for n in range(len(signal_output_list)):
    for m in range(len(signal_output_list[n][1])):
        if len(signal_output_list[n][1][m]) in (2,4,3,7):
            output_occurence_1478+=1
print(output_occurence_1478)
#%%
output_list=[]
for m in range(len(signal_output_list)):
    output_list_line=''
    unique_signal_patterns=[None]*10
    for i in range(len(signal_output_list[m][0])):
        if len(signal_output_list[m][0][i])==2:
            unique_signal_patterns[1]=signal_output_list[m][0][i]
        if len(signal_output_list[m][0][i])==3:
            unique_signal_patterns[7]=signal_output_list[m][0][i]
        if len(signal_output_list[m][0][i])==4:
            unique_signal_patterns[4]=signal_output_list[m][0][i]
        if len(signal_output_list[m][0][i])==7:
            unique_signal_patterns[8]=signal_output_list[m][0][i]
    for i in range(len(signal_output_list[m][0])):
        if len(signal_output_list[m][0][i])==5:
            #2 or 3 or 5
            if all(num in signal_output_list[m][0][i] for num in unique_signal_patterns[1]):
                unique_signal_patterns[3]=signal_output_list[m][0][i]
            elif all(str(num) in signal_output_list[m][0][i] for num in set(unique_signal_patterns[4])-set(unique_signal_patterns[1])):
                unique_signal_patterns[5]=signal_output_list[m][0][i]
            else:
                unique_signal_patterns[2]=signal_output_list[m][0][i]
    for i in range(len(signal_output_list[m][0])):
        if len(signal_output_list[m][0][i])==6:
            #0 or 6 or 9
            if all(num in signal_output_list[m][0][i] for num in unique_signal_patterns[4]):
                unique_signal_patterns[9]=signal_output_list[m][0][i]
            elif all(str(num) in signal_output_list[m][0][i] for num in set(unique_signal_patterns[8])-set(unique_signal_patterns[1])):
                unique_signal_patterns[6]=signal_output_list[m][0][i]
            else:
                unique_signal_patterns[0]=signal_output_list[m][0][i]
    for n in range(len(signal_output_list[m][1])):
        output=[str(unique_signal_patterns.index(k)) for k in unique_signal_patterns if sorted(signal_output_list[m][1][n])==sorted(k)][0]
        output_list_line+=str(output)
    output_list.append(int(output_list_line))
#%%
answer2=sum(output_list)
print(answer2)