from Question import Question

question_prompts = [
    "Jakie są złącza internetowe?\n(a) RJ45\n(b) RJ11\n(c) RJ14\n\n",
    "Jaki jest najlepszy protokół poczty przychodzącej?\n(a) POP3\n(b) IMAP\n(c) STMP\n\n",
    "Najlepsze wyjście na karcie graficznej?\n(a) D-Sub\n(b) S-VHS\n(c) DP\n\n",
    "DO CZEGO UŻYWANY JEST PROTOKÓŁ SMTP?\n(a) Przesyłania plików\n(b) Wysyłania poczty\n(c) Przeglądarka Internetowa\n\n",
    "CZY POTRAFISZ ROZWINĄĆ SKRÓT WWW?\n(a) Wide World Web\n(b) World Wide Web\n(c) Whole World Web\n\n",
    "Urządzenia peryferyjne komputera?\n(a) HDD, SSD i Pendrive\n(b) Klawiaturę, skaner, myszkę\n(c) Płytę główną, drukarkę, procesor\n\n",
    "Jakie jest Rozszerzenie obrazu płyty?\n(a) HDD\n(b) ISO\n(c) PDF\n\n",
    "Który system nie jest systemem?\n(a) Unix\n(b) Word\n(c) Windows\n\n",
    "W jakim rozszerzeniu zapiszesz obraz?\n(a) RAW\n(b) TXT\n(c) DOC\n\n",
    "Jeden BAJT to?\n(a) 10 bitów\n(b) 8 bitów\n(c) 12 bitów\n\n",
]



questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "b"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Twój wynik " + str(score) + "/" + str(len(questions)) + " prawidłowo")

run_test(questions)
