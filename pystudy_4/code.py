while True:
    string_input = input("정수 입력> ")
    if string_input.isdigit():
        number_input_a = int(string_input)
        print("원의 반지름:", number_input_a)
        print("원의 둘레", 2 * 3.14 * number_input_a)
        print("원의 넓이:", 3.14 * number_input_a * number_input_a)
        break
else:
        print("정수를 입력해주세용")


# 변수를 선언합니다.
list_input_a = ["52", "273", "32", "스파이", "103"]

# 반복을 적용합니다.
list_number = []
for item in list_input_a:
    # 숫자로 변환해서 리스트에 투가합니다.
    try:
        float(item)
        list_number.append(item)
    except:
        pass

# 출력합니다.
print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))


# 함수를 선언합니다.
def write_test_file(filename, text):
    # try except 구문을 사용합니다.
    try:
        #파일을 엽니다.
        file = open(filename, "w")
        # 여러가지 처리를 수행합니다.
        return
        # 파일에 텍스트를 입력합니다.
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        # 파일을 닫습니다.
        file.close()
#함수를 호출합니다.
write_text_file("test.txt", "안녕하세요!")


def 학생_생성(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }
def 총점(student):
    return student["korean"] + student["math"]+\
        student["english"] + student["science"]
def 평균(student):
    return 총점(student) / 4
def 출력(student):
    print(student["name"], 총점(student), 평균(student))


# --------------------------------------------------------- #
# 학생 리스트를 선언합니다.
students = [
    학생("윤인성", 87, 98, 88, 95),
    학생("연하진", 92, 98, 96, 98),
    학생("구지연", 76, 96, 94, 90),
    학생("나선주", 98, 92, 96, 92),
    학생("윤아린", 95, 98, 98, 98),
    학생("윤명월", 64, 88, 92, 92)
]
# 학생을 한 명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
    student.출력()


class Student:
    def __init__(self, 이름, 나이):
        print("객체가 생성되었습니다.")
        self.이름 = 이름
        self.나이 = 나이
    def __del__(self):
        print("객체가 소멸되었습니다")
    def 출력(self):
        print(self, 이름, self.나이)

    student = Student("윤인성", 3)
    student.출력()