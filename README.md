# D2SemiAutoFisher
Полуавтоматический макрос для рыбалки (S21) в Destiny 2.<br/>
Предугадывая вопросы почему "полуавтоматический" - перемещение между точками появления прудов не предусмотрено. <br/>
Создано специально для [Discord](https://elderly-clan.ru/discord) сервера клана ElderLy. <br/>
Отдельная благодарность Nohi.

# Использование
- Скачать последний релиз приложения [отсюда](https://github.com/ArchSat/D2SemiAutoFisher/releases).
- Для использования макроса должен быть выбран активным английский язык.
- Кнопка взаимодействия в игре должна быть Е.
- Игра должна быть в окне без рамки или во весь экран. 
- Поддерживаемые разрешения:
  - 2560х1440 
  - 2560х1080
  - 1920х1080
- Перед запуском желательно занять положение перед мостиком для ловли рыбы (если возможно), поскольку макрос незначительно двигает игрока назад.
- Запустить исполняемый файл макроса.
- Наслаждаться автоматической ловлей рыбы.

# Описание алгоритма
При запуске программы происходит инициализация переменных (подобраны вручную) для обнаружения областей с кнопкой взаимодействия. <br/>
После инициализации всех переменных начинается непрерывный захват двух областей - "Идеальная подсечка" и "Рыбачить". <br/>
Процесс преобразования захваченного изображения: <br/>
|Оригинальное изображение|Первое преобразование|Второе преобразование|
|:-------------:|:------------------:|:-----:|
|![Image alt](https://github.com/archsat/D2SemiAutoFisher/raw/master/readme/original_image.png)|![Image alt](https://github.com/archsat/D2SemiAutoFisher/raw/master/readme/first_transform.png)|![Image alt](https://github.com/archsat/D2SemiAutoFisher/raw/master/readme/second_transform.png)|
<br/>
На изображении полученном в ходе последнего преобразования выполняется подсчет пикселей белого цвета. <br/>
Если полученное значение попадает в заранее заданный интервал, то выполняется нажание кнопки взаимодействия (Е).
