import random
import sys


# he_life_count - число жизней рыцаря
# he_force - сила удара рыцаря
# vi - кол-во побед рыцаря
# sw_force - сила атаки меча
# mo_force - сила удара чудовища
# mo_life_count - кол-во жизней чудовища

# выбор следующего хода
def next_move() -> int:
    # 1-встреча монстра;2-получение меча;3-получение яблока
    return random.randint(1, 3)


# встреча монстра
def meet_mon(h_lc, h_force, v_count) -> tuple:
    m_force = random.randint(5, 20)
    m_life_count = random.randint(5, 20)
    print("Вы встретили чудовище с", m_life_count,
          "жизнями и с силой удара", m_force,
          "\nНажмите 1 или 2.\n1-атаковать чудовище,2-убежать")
    ans = input()
    if ans == '1' or ans == '2':
        return ans, m_force, m_life_count
    else:
        while ans != '1' and ans != '2':
            print("Введите 1 или 2")
            ans = format(input())
        return ans, m_force, m_life_count


# получение меча
def sword_getting() -> tuple:
    s_force = random.randint(5, 20)
    print("Вы получили меч с силой атаки", s_force,
          "\nВзять меч? Нажмите 1 или 2."
          "\n1-взять меч себе выбросив старый,2-пройти мимо меча")
    ans = input()
    if ans == '1' or ans == '2':
        return s_force, ans
    else:
        while ans != '1' and ans != '2':
            print("Введите 1 или 2")
            ans = format(input())
        return s_force, ans


# получение яблока
def apple_getting(h_life_count) -> tuple:
    bonus = random.randint(5, 20)
    h_life_count += bonus
    return h_life_count, bonus


# результат боя с чудищем
def battle_result(h_lc, h_force, m_lc, m_force, vi_count) -> tuple:
    if h_force >= m_lc:
        h_lc -= m_force
        if h_lc > 0:
            print("Победа!")
            vi_count += 1
            return h_lc, vi_count
        else:
            defeat()
    else:
        defeat()


# завершение игры/проигрыш
def defeat():
    input("К сожалению, вы проиграли. Попробуйте ещё раз."
          "Нажмите любую клавишу и Enter для завершения\n")
    sys.exit()


# главная функция
def game_playing(h_life_count, h_force, vi):
    while vi < 10:
        a = next_move()
        if a == 1:
            answer = meet_mon(h_life_count, h_force, vi)
            mo_force = answer[1]
            mo_life_count = answer[2]
            if answer[0] == '1':
                answer1 = battle_result(h_life_count, h_force,
                                        mo_life_count, mo_force, vi)
                vi = answer1[1]
                h_life_count = answer1[0]
                if h_life_count <= 0:
                    defeat()
        if a == 2:
            answer2 = sword_getting()
            if answer2[1] == '1':
                h_force = answer2[0]
        if a == 3:
            m = apple_getting(h_life_count)
            h_life_count = m[0]
            print("Вы получили яблоко. Ваше количество жизней увеличилось на",
                  m[1], "и стало равным", h_life_count)


game_playing(10, 10, 0)
