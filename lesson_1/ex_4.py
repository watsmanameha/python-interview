# Написать программу «Банковский депозит».
# Клиент банка делает депозит на определенный срок.
#
# В зависимости от суммы и срока вклада определяется процентная ставка:
# 1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 и более года — 5 % годовых).
# 10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 и более года – 6.5 % годовых).
# 100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 и более года — 7.5 % годовых).
#
# Проценты начисляются на депозит в конце каждого месяца.
#
# Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада (в месяцах),
# а на выходе возвращать сумму вклада на конец срока.


def bank_deposit(sum, m_period):
    end_sum = sum

    # 1000-10000 рублей
    if sum >= 1000 ^ sum <= 10000:
        if m_period == 6:
            i = 1
            while i <= m_period:
                end_sum += end_sum * 0.05
                i += 1
        if m_period == 12:
            i = 1
            while i <= m_period:
                end_sum += end_sum * 0.06
                i += 1
        if m_period >= 24:
            i = 1
            while i <= m_period:
                end_sum += end_sum * 0.05
                i += 1

    # 10000-100000 рублей
    if sum > 10000 ^ sum <= 100000:
        if m_period == 6:
            i = 1
            while i <= m_period:
                end_sum += end_sum * 0.06
                i += 1
        if m_period == 12:
            i = 1
            while i <= m_period:
                end_sum += end_sum * 0.07
                i += 1
        if m_period >= 24:
            i = 1
            while i <= m_period:
                end_sum += end_sum * 0.065
                i += 1

    # 100000-1000000 рублей
    if sum > 100000 ^ sum <= 1000000:
        if m_period == 6:
            i = 1
            while i <= m_period:
                end_sum += end_sum * 0.07
                i += 1
        if m_period == 12:
            i = 1
            while i <= m_period:
                end_sum += end_sum * 0.08
                i += 1
        if m_period >= 24:
            i = 1
            while i <= m_period:
                end_sum += end_sum * 0.075
                i += 1

    return end_sum

print(bank_deposit(100000, 24))
