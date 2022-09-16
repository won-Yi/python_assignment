import random
import time
from datetime import datetime, timedelta

#게임 시작 시간
start_time = datetime.now()

n = int(input())

# 입력받은 갯수만큼 랜덤한 숫자 생성

num_list = []
for _ in range(n):
    num = random.randint(1,10)
    num_list.append(num)
print(num_list)


# 정답을 맞출때까지 몇번 반복되었는가?
try_number = 0

go_on = True
while go_on:

    strike_count = 0
    out_count = 0
    ball_count = 0

    # guess_num = list(map(int,input().split()))
    guess_num = list(input().split())

    if guess_num[0] == 'e':
        go_on = False

    else:
        guess_num= list(map(int, guess_num))
        for i in range(len(num_list)):
            if guess_num[i] == num_list[i]:
                strike_count +=1
                print("strike")
            elif guess_num[i] != num_list[i]:
                if num_list.count(guess_num[i]): #true면
                    ball_count +=1
                    print("ball")
                else:
                    out_count +=1
                    print("out")

        try_number +=1
        print(try_number)

        #정답을 맞추면 프로그램 종료
        if strike_count == len(num_list):
            end_time = datetime.now()
            total_time = end_time - start_time
            # time = datetime.strftime(total_time, "%y,%m,%d,%H,%M,%S")

            print(f'총 {try_number}번의 도전 끝에 정답을 맞추셨습니다.')
            print(f'총 {total_time}의 시간 동안 도전하셨습니다.')
            print(f'게임을 마친 시간은 {end_time}입니다.')

            go_on = False