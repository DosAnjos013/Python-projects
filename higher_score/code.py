people = [
    ("Mike", 17, 80),
    ("Sarah", 20, 45),
    ("John", 22, 60),
    ("Anna", 18, 50),
    ("Tom", 16, 90)
]

score_and_age = [(nome, pontuacao) for nome, age, pontuacao in people if age >= 18 and pontuacao >= 50]
print(score_and_age)