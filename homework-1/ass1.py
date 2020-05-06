# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

################################ Q1 ##############################
def trifeca(word):
    for i in range(len(word)-5):
        if word[i]==word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
            return True
    return False

# x=''
# print(trifeca(x))

################################ Q2 ##############################

def compare_subjects_within_student(
    subj1_all_students,
    subj2_all_students
):

    best_score_dict = {}
    subject_1_name = subj1_all_students[0]
    subject_2_name = subj2_all_students[0]
    subj1 = subj1_all_students[1]
    subj2 = subj2_all_students[1]
    students = set(subj1.keys()).intersection(set(subj2.keys()))
    for student in students:
        if max(subj1[student])>max(subj2[student]):
            best_score_dict[student] = subject_1_name
        elif max(subj1[student])<max(subj2[student]):
            best_score_dict[student] = subject_2_name
        else:
            best_score_dict[student] = 'same'
    for name in best_score_dict:
        print(name,' : ',best_score_dict[name])
    return best_score_dict


history = ['history',{'Roy':[80,90],'Guy':[60,100], 'Roni':[40,75], 'Danny':[85, 100], 'Shimon':[65,80]}]
math = ['math',{'Roy':[80,90],'Guy':[80,85], 'Roni':[40,80], 'Danny':[75, 90]}]

x = compare_subjects_within_student(history,math)

################################ Q3 ##############################
def check_palindrome():
    
    def is_palindrome(word):
       return word ==word[::-1]
    
    for i in range(100_000,1_000_000): 
        if is_palindrome(str(i)[-4:]) and is_palindrome(str(i+1)[-5:]) and is_palindrome(str(i+2)[-5:-1]) and is_palindrome(str(i+3)):
            print(i)

check_palindrome()





