login = input("login: ")
password = input("password: ")


if login in logins and logins[login] == password:
    print("Вы успешно вошли в систему.")
    import socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
    sock.connect(('localhost', 7070))  # подключемся к серверному сокету

    sock.send(bytes('Hello, world', encoding='UTF-8'))  # отправляем сообщение
    data = sock.recv(1024)  # читаем ответ от серверного сокета
    sock.close()  # закрываем соединение
    print(data)


else:
    print("Неверный логин или пароль.")

