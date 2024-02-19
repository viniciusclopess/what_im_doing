import time

def get_atual_datetime():
    atual_datetime = time.localtime()
    watch = time.strftime('%H:%M:%S', atual_datetime)
    date = time.strftime('%Y-%m-%d', atual_datetime)
    return date, watch

def write_file(date, watch, answer):
    with open("whatimdoing.txt", "a") as arquivo:
        arquivo.write(f'{date}-{watch} - {answer}\n')

def go():
    date, watch = get_atual_datetime()
    print(f'{date} - {watch}')
    input('O que você está fazendo agora?')
    answer = input('->')
    if len(answer) == 0:
        answer = 'Não informado!'
        write_file(date, watch, answer)
        return date, watch, answer
    elif answer == 'kk':
        answer = 'Estou jogando!'
        write_file(date, watch, answer)
        return date, watch, answer
    else:
        write_file(date, watch, answer)
        return date, watch, answer