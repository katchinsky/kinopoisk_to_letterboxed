Это простой скрипт, чтобы конвертировать оценки с Кинопоиска в csv-шкy, которую можно засунуть в Letterboxd. 

1. Зайти на страничку со своими оценками на кинопоиске (https://www.kinopoisk.ru/user/{user_id}/votes/). Открыть дев-консоль, в ней зайти во вкладку network и найти в ней json с названием last_vote_{user_id}__all.json. В нем лежит вся история оценок, прикинь! 
2. Сохранить ее содержимое, убрав jsonplast_vote_{user_id}__all( из начала и закрывающую скобку в конце, в файлик ratings.json в директории со скриптом
3. Запустить скрипт командой python3 kp_to_lb_converter.py
4. Получившуюся csv-шку загрузить сюда https://letterboxd.com/import/ 
Там че-то придется поправить руками, но у Леттербоксда очень симпатично устроена миграция, поэтому это должно быть не сложно
