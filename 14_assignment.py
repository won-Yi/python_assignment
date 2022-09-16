class Calculrator:

    def set_number(self, num1, num2):
        try:
            self.num1 = int(num1)
            self.num2 = int(num2)
        except ValueError:
            print("숫자만 입력해주세요.")
            while True:
                try:
                    num1, num2 = map(int, input("값을 입력해주세요. : ").split())
                    self.num1 = num1
                    self.num2 = num2
                    break
                except ValueError:
                    print("다시 입력하세요.")

    def plus(self):
        return self.num1 + self.num2

    def minus(self):
        return self.num1 - self.num2

    def multiple(self):
            return self.num1 * self.num2


    def divide(self):
        try:
            return (self.num1 / self.num2)
        except ZeroDivisionError:
            return "0 으로 나눌 수 없습니다."


    def plus(self):
        try:
            return self.num1 + self.num2
        except:
            return "잘못된 값이 들어왔습니다."
    def minus(self):
        try:
            return self.num1 - self.num2
        except:
            return "잘못된 값이 들어왔습니다."
    def multiple(self):
        try:
            return self.num1 * self.num2
        except:
            return "잘못된 값이 들어왔습니다."
    def divide(self):
        try:
            try:
                return (self.num1 / self.num2)
            except ZeroDivisionError:
                return "0 으로 나눌 수 없습니다."
        except:
            return "잘못된 값이 들어왔습니다."

cal = Calculrator()
cal.set_number(20,"num")

print(cal.plus())
print(cal.minus())
print(cal.multiple())
print(cal.divide())

###################################################################################
from pprint import pprint

people = [
    ("Blake Howell", "Jamaica", 18, "aw@jul.bw"),
    ("Peter Bowen", "Burundi", 30, "vinaf@rilkov.il"),
    ("Winnie Hall", "Palestinian Territories", 22, "moci@pacivhe.net"),
    ("Alfred Schwartz", "Syria", 29, "ic@tolseuc.pr"),
    ("Carrie Palmer", "Mauritius", 28, "fenlofi@tor.aq"),
    ("Rose Tyler", "Martinique", 17, "as@forebjab.et"),
    ("Katharine Little", "Anguilla", 29, "am@kifez.et"),
    ("Brent Peterson", "Svalbard & Jan Mayen", 22, "le@wekciga.lr"),
    ("Lydia Thornton", "Puerto Rico", 19, "lefvoru@itbewuk.at"),
    ("Richard Newton", "Pitcairn Islands", 17, "da@lasowiwa.su"),
    ("Eric Townsend", "Svalbard & Jan Mayen", 22, "jijer@cipzo.gp"),
    ("Trevor Hines", "Dominican Republic", 15, "ev@hivew.tm"),
    ("Inez Little", "Namibia", 26, "meewi@mirha.ye"),
    ("Lloyd Aguilar", "Swaziland", 16, "oza@emneme.bb"),
    ("Erik Lane", "Turkey", 30, "efumazza@va.hn"),
]

people = list(filter(lambda x: x[2] > 20, people))
people.sort(key=lambda x : x[2])
pprint(people)








