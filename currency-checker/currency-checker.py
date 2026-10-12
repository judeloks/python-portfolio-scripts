import requests


def get_exchange_rates():
    # Используем бесплатный API для получения курсов валют
    url = "https://open.er-api.com/v6/latest/USD"

    try:
        response = requests.get(url)
        # Проверяем, успешно ли прошёл запрос (код 200 означает успех)
        if response.status_code == 200:
            data = response.json()
            return data.get("rates")
        else:
            print("Ошибка при получении данных с сервера.")
            return None
    except Exception as e:
        print(f"Произошла ошибка соединения: {e}")
        return None


def main():
    print("Получаем актуальные курсы валют...")
    rates = get_exchange_rates()

    if not rates:
        return

    # Покажем курс рубля по отношению к USD и EUR
    rub_rate = rates.get("RUB")
    eur_rate = rates.get("EUR")

    print("\n--- Актуальные курсы валют ---")
    if rub_rate:
        print(f"• 1 USD = {rub_rate:.2f} RUB")
    if eur_rate and rub_rate:
        # Пересчитаем кросс-курс для евро
        eur_to_rub = rub_rate / rates.get("EUR")
        print(f"• 1 EUR = {eur_to_rub:.2f} RUB")

    # Интерактив с пользователем
    print("\n")
    try:
        usd_amount = float(input("Введите сумму в USD для конвертации в Рубли: "))
        result = usd_amount * rub_rate
        print(f"{usd_amount} USD = {result:.2f} RUB")
    except ValueError:
        print("Пожалуйста, введите число!")


if __name__ == "__main__":
    main()
