try:
    import time
except ModuleNotFoundError:
    print("Unfortunately, the module requires the module time")

def countdown(*args, print_time=False, round_digits=1, only_exact_time=False, only_convenient_time=False):
    """
    - US:
        Countdown timer that accepts either a single argument (seconds) or three arguments (hours, minutes, seconds).

        Args:
            args: Either one argument (seconds) or three arguments (hours, minutes, seconds).
            print_time (bool): Whether to print the remaining time.
            round_digits (int): Number of decimal places to round the time if only_exact_time is True.
            only_exact_time (bool): Print time with exact seconds.
            only_convenient_time (bool): Print time in HH:MM:SS format.

        Raises:
            ValueError: If the input arguments are invalid.

    - UA:
        Countdown timer, який приймає або один аргумент (секунди), або три аргументи (години, хвилини, секунди).

        Аргументи:
            args: Або один аргумент (секунди), або три аргументи (години, хвилини, секунди).
            print_time (bool): Чи потрібно друкувати залишковий час.
            round_digits (int): Кількість десяткових знаків для округлення часу, якщо only_exact_time є True.
            only_exact_time (bool): Друкувати час з точністю до секунд.
            only_convenient_time (bool): Друкувати час у форматі HH:MM:SS.

        Піднімає:
            ValueError: Якщо вхідні аргументи є недійсними.

    - RU:
        Countdown timer, который принимает либо один аргумент (секунды), либо три аргумента (часы, минуты, секунды).

        Аргументы:
            args: Либо один аргумент (секунды), либо три аргумента (часы, минуты, секунды).
            print_time (bool): Нужно ли печатать оставшееся время.
            round_digits (int): Количество знаков после запятой для округления времени, если only_exact_time равно True.
            only_exact_time (bool): Печатать время с точностью до секунд.
            only_convenient_time (bool): Печатать время в формате HH:MM:SS.

        Вызывает:
            ValueError: Если входные аргументы недействительны.

    - ES:
        Temporizador de cuenta regresiva que acepta un solo argumento (segundos) o tres argumentos (horas, minutos, segundos).

        Argumentos:
            args: Ya sea un argumento (segundos) o tres argumentos (horas, minutos, segundos).
            print_time (bool): Si se debe imprimir el tiempo restante.
            round_digits (int): Número de decimales a redondear el tiempo si only_exact_time es True.
            only_exact_time (bool): Imprimir el tiempo con segundos exactos.
            only_convenient_time (bool): Imprimir el tiempo en formato HH:MM:SS.

        Lanza:
            ValueError: Si los argumentos de entrada no son válidos.
    """
    def format_time(seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return int(hours), int(minutes), int(seconds)

    if len(args) == 1:
        total_seconds = args[0]
    elif len(args) == 3:
        total_seconds = args[0] * 3600 + args[1] * 60 + args[2]
    else:
        raise ValueError("countdown() expects either one argument (seconds) or three arguments (hours, minutes, seconds)")

    if only_convenient_time and only_exact_time:
        raise ValueError("You cannot enable both exact time and convenient time at the same time")

    start_time = time.time()

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        remaining_time = total_seconds - elapsed_time

        if remaining_time <= 0:
            if print_time:
                if only_convenient_time:
                    print("0:00:00")
                else:
                    print("0")
            break

        if print_time:
            if only_exact_time:
                print(f"{remaining_time:.{round_digits}f}")
            elif only_convenient_time:
                hours, minutes, seconds = format_time(remaining_time)
                print(f"{hours}:{minutes:02}:{seconds:02}")
            else:
                if remaining_time > 30:
                    hours, minutes, seconds = format_time(remaining_time)
                    print(f"{hours}:{minutes:02}:{seconds:02}")
                else:
                    print(f"{remaining_time:.{round_digits}f}")

        if remaining_time <= 30 and only_convenient_time:
            time.sleep(1)
        elif remaining_time <= 30 or only_exact_time:
            time.sleep(0.1)
        else:
            time.sleep(1)
