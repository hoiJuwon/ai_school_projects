# -*- coding:utf-8 -*-

import json
import getpass

students_file_path = './students_info.json'

# print(students_json_data['students'])


student = {
    "userid": 'abcd1234',
    "password": '1234'
}

userid = student['userid']

print(userid)
# abcd1234


def read_students_json():
    with open(students_file_path, "r") as json_file:
        students_json_data = json.load(json_file)

    return students_json_data


def write_students_json(students_json_data):
    with open(students_file_path, 'w') as outfile:
        json.dump(students_json_data, outfile, ensure_ascii=False, indent=4)


def make_input_validate(input_text):
    if len(input_text) > 12:
        return 'validate_err'

    else:
        validated_input = input_text.lower()

        return validated_input


def get_user_input(input_type):

    is_validate = False

    input_count = 0

    result = ''

    # 유저 id
    while is_validate is False and input_count < 4:

        if input_count == 3:
            print('규칙을 3번 틀리셨습니다! 보안을 위해 프로그램이 종료됩니다.')
            exit()

        if input_count != 0:
            print(f'{input_count}번 틀리셨습니다. 규칙을 확인해주세요')

        print(f'{input_type} - 12 자 이하, 소문자만 가능')

        if input_type == '아이디':
            raw_input = input(f'* {input_type}를 입력하세요 : \n')
        else:
            raw_input = getpass.getpass()

        user_input = make_input_validate(raw_input)

        if user_input == 'validate_err':
            input_count += 1
        else:
            is_validate = True
            input_count = 0
            result = user_input

            break

    return result


def signup():

    user_schema = {
        'userid': '',
        'password': '',
        'username': '',
        'contents': '',
        'interested': ''
    }

    # user_schema 로 만들기

    user_schema['userid'] = get_user_input('아이디')

    students_json_data = read_students_json()
    # print(students_json_data['students'])

    for student in students_json_data['students']:
        # 아이디 존재하는지 찾기
        if student['userid'] == user_schema['userid']:
            print('\n ********** 같은 아이디가 존재합니다! ')
            return 'same_id_exist'

    user_schema['password'] = get_user_input('비밀번호')
    user_schema['username'] = input('이름을 입력해주세요 : \n')
    user_schema['contents'] = input('5개월 간의 다짐을 입력해주세요 : \n')
    user_schema['interested'] = input('관심분야를 입력해주세요 : \n')

    # json 파일에 write
    students_json_data['students'].append(user_schema)

    write_students_json(students_json_data)

    print('\n회원가입이 완료되었습니다! 로그인 후 사용해주세요.\n')

    # 회원가입이 완료되었다면 로그인 진행
    run_login()


def login():

    students_json_data = read_students_json()

    login_user_input = {
        'userid': '',
        'password': '',
    }

    login_user_input['userid'] = get_user_input('아이디')
    login_user_input['password'] = get_user_input('비밀번호')

    students_json_data['students']

    for student in students_json_data['students']:

        # 아이디 존재하는지 찾기
        if student['userid'] == login_user_input['userid']:

            if student['password'] == login_user_input['password']:
                username = student['username']
                print(f'\n {username}님, 로그인에 성공하셨습니다.!')

                return student

            # 비밀번호 틀린 경우
            else:
                print('비밀번호를 확인해주세요!')
                return 'wrong_password'

        elif students_json_data['students'][-1]['userid'] == student['userid']:
            print('존재하지 않는 아이디 입니다 !')
            return 'no_exist_id'

    return


def run_login():

    # 로그인 과정 실행
    login_count = 0

    while True and login_count < 4:

        if login_count == 3:
            print('규칙을 3번 틀리셨습니다! 보안을 위해 프로그램이 종료됩니다.')
            exit()

        login_count += 1

        login_student = login()

        if login_student == 'wrong_password' or login_student == 'no_exist_id':
            continue
        else:
            break

    after_authenticated(login_student)


def after_authenticated(login_student):

    # 로그인 성공
    which_page = input('1 - 마이페이지 보기 / 2 - 다른 유저 보기 : / 3 - 로그아웃')

    if (which_page == '1'):
        print(login_student)

    elif (which_page == '3'):
        exit()
    else:
        students_json_data = read_students_json()

        student_order = 1

        students_key_order = {}

        print('디테일을 보고싶은 학생의 번호를 입력하세요')

        for student in students_json_data['students']:
            student_name = student['username']
            print(f'{student_order} - {student_name}')
            students_key_order[student_order] = student
            student_order += 1
            print('-------------------------')

        target_key_order = int(input("번호 : "))

        print(students_key_order[target_key_order])

    exit()


def main():
    while True:
        print('\n')
        print('\n')
        print("******** 광주 인공지능 사관학교 ************************")
        print("** 광주 인공지능 사관학교의 정보를 담은 페이지 입니다.**")
        print("********************************************************\n")

        # 1 - 회원가입 / 2 - 로그인

        signup_or_login = input('1 - 회원가입 / 2 - 로그인 : \n')

        if signup_or_login == '1':
            # 회원가입 과정 실행
            signup()
        elif signup_or_login == '2':
            run = run_login()
        else:
            print('잘 못 입력하셨습니다! ')


main()
