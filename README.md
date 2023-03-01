<h1>Тестовое задание от компании "IT-парк Питерский мостик"</h1>

Требуется разработать два сетевых приложения для работы с сокетами tcp через библиотеку asyncio(Python)

<h3>Детальные требования к первому приложению(сервер):</h3>
<ul>
<li>1. Приложение должно работать асинхронно с сокетом tcp через библиотеку asyncio. Приложение должно являться сервером и ожидать подключения клиента(2-ого приложения).
При получении запроса от клиента, приложение выполняет вычисления и отправляет ответ.
Запрос от клиента представляет собой простейшее математическое выражение. После вычисления выражения и отправки ответа сервер закрывает подключение к клиенту.</li>

  <li>2. Обмен данными предлагается осуществлять в формате json.</li>

  <li>3. Работа приложения должна логироваться в файл подробно и человеко-читаемом формате.</li>
  </ul>

<h3>Детальные требования ко второму приложению (клиент):</h3>
<ul>
<li>1. Приложение должно работать асинхронно с сокетом tcp через библиотеку asyncio. Приложение должно являться клиентом и подключаться к серверу(1-ого приложения).
Приложение подключается к серверу, отправляет запрос в виде математического простейшего выражения, ожидает результат от сервера, получает его и закрывает соединение.</li>

  <li>2. Выражение вводится с консоли или с файла.</li>

  <li>3. Обмен данным предлагается осуществялть в формате json.</li>

  <li>4. Работа приложения должна логироваться в файл подробно и человеко-читаемом формате.</li>
</ul>



