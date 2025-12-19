"""Seed database with 50 real movies, reviews, ratings, and users"""
import sys
from pathlib import Path
import hashlib
import time

sys.path.insert(0, str(Path(__file__).parent))

from app import db

# 10 viewer users
viewers_data = [
    {"email": "ivanov@mail.ru", "username": "Иванов Игорь", "password": "viewer123"},
    {"email": "petrov@mail.ru", "username": "Петров Петр", "password": "viewer123"},
    {"email": "smirnov@mail.ru", "username": "Смирнов Сергей", "password": "viewer123"},
    {"email": "sokolov@mail.ru", "username": "Соколов Сергей", "password": "viewer123"},
    {"email": "lebedev@mail.ru", "username": "Лебедев Лев", "password": "viewer123"},
    {"email": "novikov@mail.ru", "username": "Новиков Николай", "password": "viewer123"},
    {"email": "volkov@mail.ru", "username": "Волков Виктор", "password": "viewer123"},
    {"email": "solovyev@mail.ru", "username": "Соловьев Станислав", "password": "viewer123"},
    {"email": "antonov@mail.ru", "username": "Антонов Андрей", "password": "viewer123"},
    {"email": "pavlov@mail.ru", "username": "Павлов Павел", "password": "viewer123"},
    {"email": "user@kinovzor.ru", "username": "user", "password": "user123"},
]

# Moderator and admin users
admin_user = {"email": "moderator@kinovzor.ru", "username": "moderator", "password": "moderator123", "is_moderator": True}

# Real movies with posters
movies_data = [
   {
    "title": "Шоу Трумэна",
    "year": 1998,
    "genre": "Драма",
    "poster": "https://avatars.mds.yandex.net/get-mpic/11399770/2a00000199e2bea2c18991f4b242b7dbf6bd/orig",
    "desc": "История человека, жизнь которого - один огромный телевизионный спектакль"
  },
  {
    "title": "Жизнь прекрасна",
    "year": 1997,
    "genre": "Драма",
    "poster": "https://avatars.mds.yandex.net/get-mpic/4413406/2a00000199e2cb1df32974608ec0ae308cae/orig",
    "desc": "Отец защищает своего сына от ужасов войны через игру и воображение"
  },
  {
    "title": "Форрест Гамп",
    "year": 1994,
    "genre": "Драма",
    "poster": "https://avatars.mds.yandex.net/get-kinopoisk-image/1599028/3560b757-9b95-45ec-af8c-623972370f9d/1920x",
    "desc": "История простого человека, который достиг невероятных высот"
  },
  {
    "title": "Зелёная миля",
    "year": 1999,
    "genre": "Драма",
    "poster": "https://mediaproxy.tvtropes.org/width/1200/https://static.tvtropes.org/pmwiki/pub/images/109760605_316461969762895_1909735586776424983_n.jpg",
    "desc": "Исправительная камера и чудо в виде сверхъестественных способностей"
  },
  {
    "title": "Спасение рядового Райана",
    "year": 1998,
    "genre": "Боевик",
    "poster": "https://avatars.mds.yandex.net/i?id=1c198a5b8249f7af2591632fc70e55a8_l-9741045-images-thumbs&n=13",
    "desc": "Эпическая история о спасении солдата во время Второй мировой войны"
  },
  {
    "title": "Бойцовский клуб",
    "year": 1999,
    "genre": "Триллер",
    "poster": "https://s1.afisha.ru/mediastorage/a6/a0/81e2d43fa763441294fad29fa0a6.jpg",
    "desc": "Психологический триллер о подпольном клубе бойцов"
  },
  {
    "title": "Матрица",
    "year": 1999,
    "genre": "Фантастика",
    "poster": "https://avatars.mds.yandex.net/i?id=5774dfaf7ad1e433fe9bcf64506616e0_l-5875611-images-thumbs&n=13",
    "desc": "Революционный фантастический боевик о реальности и иллюзии"
  },
  {
    "title": "Список Шиндлера",
    "year": 1993,
    "genre": "Драма",
    "poster": "https://ir.ozone.ru/s3/multimedia-1-w/c1000/7053206828.jpg",
    "desc": "История немецкого бизнесмена, спасившего тысячи евреев"
  },
  {
    "title": "Звёздные войны: Эпизод I",
    "year": 1999,
    "genre": "Фантастика",
    "poster": "https://ru-images-s.kinorium.com/movie/1080/109444.jpg?1656591249",
    "desc": "Новое начало саги о войне галактик"
  },
  {
    "title": "Титаник",
    "year": 1997,
    "genre": "Мелодрама",
    "poster": "https://images.kinorium.com/movie/poster/108983/w1500_51624372.jpg",
    "desc": "Эпическая романтическая драма о гибели лайнера"
  },
  {
    "title": "Красота по-американски",
    "year": 1999,
    "genre": "Драма",
    "poster": "https://avatars.mds.yandex.net/i?id=d70271ce63e65f10b49ba86abda1f3b1_l-10355125-images-thumbs&n=13",
    "desc": "Тёмная комедия о мечтах и идеалах в пригороде"
  },
  {
    "title": "Хороший, плохой, злой",
    "year": 1966,
    "genre": "Боевик",
    "poster": "https://avatars.mds.yandex.net/i?id=b8c5c8497d62e9d5a10c1ea3bd78d195_l-12855379-images-thumbs&n=13",
    "desc": "Культовый вестерн про три стрелка в поисках сокровища"
  },
  {
    "title": "Криминальное чтиво",
    "year": 1994,
    "genre": "Триллер",
    "poster": "https://images.kinorium.com/movie/fanart/100973/w1500_44851415.jpg",
    "desc": "Нелинейное повествование о криминальной жизни Лос-Анджелеса"
  },
  {
    "title": "Молчание ягнят",
    "year": 1991,
    "genre": "Триллер",
    "poster": "https://avatars.mds.yandex.net/i?id=dc924a2ba0b766b3a2b1bcf30c18eb3c_l-4900773-images-thumbs&n=13",
    "desc": "Психологический триллер про охоту на серийного убийцу"
  },
  {
    "title": "Назад в будущее",
    "year": 1985,
    "genre": "Комедия",
    "poster": "https://citaty.info/files/posters/4343.jpg",
    "desc": "Приключенческая комедия о путешествиях во времени"
  },
  {
    "title": "Пираты Карибского моря",
    "year": 2003,
    "genre": "Приключения",
    "poster": "https://avatars.mds.yandex.net/i?id=74ef0fe9edc3390feda4f199213f6952_l-5602191-images-thumbs&n=13",
    "desc": "Веселое приключение капитана Джека Воробья"
  },
  {
    "title": "Великий Гэтсби",
    "year": 2013,
    "genre": "Драма",
    "poster": "https://i.ebayimg.com/images/g/AtMAAOSwRMJnqG3o/s-l1600.jpg",
    "desc": "Роман о любви, амбициях и американской мечте"
  },
  {
    "title": "Интерстеллар",
    "year": 2014,
    "genre": "Фантастика",
    "poster": "https://avatars.mds.yandex.net/get-mpic/11763878/2a0000018b4350ed816ef542700f80914efa/orig",
    "desc": "Космическая эпопея о спасении человечества"
  },
  {
    "title": "Темный рыцарь",
    "year": 2008,
    "genre": "Боевик",
    "poster": "https://avatars.mds.yandex.net/get-mpic/11368570/2a0000018b432a99ba8ec8e273d023b83486/orig",
    "desc": "Второй фильм о Бэтмене с легендарным Джокером"
  },
  {
    "title": "Социальная сеть",
    "year": 2010,
    "genre": "Драма",
    "poster": "https://files.itv.uz/uploads/content/poster/2022/07/02/a05889c9d6e44cf2dddd7f89d05c7dab-q-700x1002.jpeg",
    "desc": "История создания Facebook и его основателя"
  },
  {
    "title": "Лучший стрелок",
    "year": 1986,
    "genre": "Боевик",
    "poster": "https://www.kino-teatr.ru/movie/poster/17292/190188.jpg",
    "desc": "История летчика истребителя и его романтичного пути"
  },
  {
    "title": "Лиловые холмы",
    "year": 2006,
    "genre": "Драма",
    "poster": "https://m.media-amazon.com/images/I/51WqNFIw1uL._AC_UF894,1000_QL80_.jpg",
    "desc": "Трогательная история любви и разлуки"
  },
  {
    "title": "Джанго освобожденный",
    "year": 2012,
    "genre": "Боевик",
    "poster": "http://images-s.kinorium.com/movie/poster/573253/w1500_55126597.jpg",
    "desc": "Западный боевик о борьбе с рабством"
  },
  {
    "title": "Земля обетованная",
    "year": 2012,
    "genre": "Драма",
    "poster": "https://ru-images-s.kinorium.com/movie/1080/612007.jpg?1517248331",
    "desc": "История двух семей, связанных газом и экологией"
  },
  {
    "title": "Гренада Испанская",
    "year": 2011,
    "genre": "Драма",
    "poster": "https://avatars.mds.yandex.net/get-kinopoisk-image/1599028/d4b03e7c-3643-44ea-9e45-84ef06153965/orig",
    "desc": "Историческая драма об Испании и её культуре"
  },
  {
    "title": "Мёртвые поэты общества",
    "year": 1989,
    "genre": "Драма",
    "poster": "https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p11671_p_v8_ad.jpg",
    "desc": "Вдохновляющая история учителя и его учеников"
  },
  {
    "title": "Миллион",
    "year": 2006,
    "genre": "Триллер",
    "poster": "https://www.hancinema.net/photos/fullsizephoto91357.jpg",
    "desc": "История о том, что можно купить за миллион долларов"
  },
  {
    "title": "Непрощенный",
    "year": 1992,
    "genre": "Западный",
    "poster": "https://m.media-amazon.com/images/M/MV5BNmZmMzM3YWMtZjg5Yi00M2MxLTg3ZGItNGU4YjQxNDAxM2Q4XkEyXkFqcGc@._V1_.jpg",
    "desc": "Мрачный вестерн про старого стрелка"
  },
  {
    "title": "Холодная гора",
    "year": 2003,
    "genre": "Драма",
    "poster": "https://avatars.mds.yandex.net/i?id=1a68383bc6e70a15bfb68ffd90731794_l-5161502-images-thumbs&n=13",
    "desc": "История любви и войны в период Гражданской войны"
  },
  {
    "title": "Один дома",
    "year": 1990,
    "genre": "Комедия",
    "poster": "https://avatars.mds.yandex.net/get-kinopoisk-image/1900788/dba96a96-1a6b-42d8-a976-d4e8d6180b56/1920x",
    "desc": "Семейная комедия о мальчике, оставшемся защищать дом"
  },
  {
    "title": "Ловушка для родителей",
    "year": 1998,
    "genre": "Комедия",
    "poster": "https://avatars.mds.yandex.net/i?id=961dd217291012ae4b97aa78f0a8be48-3887886-images-thumbs&n=13",
    "desc": "Комедия про близнецов, разлученных при рождении"
  },
  {
    "title": "Город грехов",
    "year": 2005,
    "genre": "Боевик",
    "poster": "https://www.timeout.ru/wp-content/uploads/kpposters/77443.jpg",
    "desc": "Нуаровский боевик про преступный город"
  },
  {
    "title": "Любовь в эпоху холеры",
    "year": 2007,
    "genre": "Мелодрама",
    "poster": "https://media.kg-portal.ru/movies/l/loveinthetimeofcholera/posters/loveinthetimeofcholera_4.jpg",
    "desc": "История долгой и верной любви через годы"
  },
  {
    "title": "Лихорадка субботнего вечера",
    "year": 1987,
    "genre": "Мелодрама",
    "poster": "https://avatars.mds.yandex.net/get-kinopoisk-image/1777765/c1e17101-0f36-4809-a893-4ee49565b8ab/1920x",
    "desc": "О рабочем парне из Бруклина, который всю неделю трудится, а в субботу отправляется на дискотеку, чтобы танцевать, забыв о правилах."
  },
  {
    "title": "Водный мир",
    "year": 1995,
    "genre": "Фантастика",
    "poster": "https://avatars.mds.yandex.net/get-kinopoisk-image/1599028/e58c353c-2e18-4e4a-a254-f4dfe6b0f9cb/1920x",
    "desc": "Постапокалиптический фантастический боевик"
  },
  {
    "title": "Люди в чёрном",
    "year": 1997,
    "genre": "Комедия",
    "poster": "https://resizer.mail.ru/p/62502c24-6e9f-545d-baa5-17bdf54f6217/AQACEpyuPsaqC7Wh98ccjCkcwxag96e4xO1IvGSPcW-eOarBwhXjnciN5sVSNOdaUM8P1Xsv0d6UXEfDV-0du9Kiuto.jpg",
    "desc": "Весёлая комедия про инопланетян и секретных агентов"
  },
  {
    "title": "Парк Юрского периода",
    "year": 1993,
    "genre": "Приключения",
    "poster": "https://s1.afisha.ru/mediastorage/ef/7b/e786c2aba1484b47b4142bd97bef.jpg",
    "desc": "Культовая фантастика про парк динозавров"
  },
  {
    "title": "Челюсти",
    "year": 1975,
    "genre": "Ужасы",
    "poster": "https://avatars.mds.yandex.net/get-kinopoisk-image/10703959/7f2cc04c-310b-4660-b407-df58594f7443/1920x",
    "desc": "Классический фильм про огромную белую акулу"
  },
  {
    "title": "Хвост тигра",
    "year": 1986,
    "genre": "Комедия",
    "poster": "https://images-s.kinorium.com/movie/1080/367350.jpg?1634284364",
    "desc": "Комедийный боевик про лучших друзей"
  },
  {
    "title": "Деньги",
    "year": 1983,
    "genre": "Комедия",
    "poster": "https://resizer.mail.ru/p/c8c7fe76-8e3c-5de2-856a-bdea05f43f8c/AQACG2sd2sBpTkxD0CvavI351o-vZ2D3glHW0iIFTun09VObX0EKmYtculsTUXYDFF4J0NxVejXLGd52F5PI1KieGRU.jpg",
    "desc": "Комедия про преступление и большие деньги"
  },
  {
    "title": "Ликвидатор",
    "year": 1988,
    "genre": "Боевик",
    "poster": "https://images-s.kinorium.com/movie/1080/86287.jpg?1634530476",
    "desc": "Боевик про рокера, ставшего киллером"
  },
  {
    "title": "Четыре комнаты",
    "year": 1995,
    "genre": "Комедия",
    "poster": "https://main-cdn.sbermegamarket.ru/big2/hlr-system/132/971/241/447/171/6/100050708368b0.jpg",
    "desc": "Нелепая комедия про гостиницу в последнюю ночь года"
  },
  {
    "title": "Диктатор",
    "year": 1940,
    "genre": "Комедия",
    "poster": "https://avatars.mds.yandex.net/get-kinopoisk-image/1599028/848a5838-b3aa-499b-a38a-5489916252f2/1920x",
    "desc": "Политическая сатира Чарли Чаплина"
  },
  {
    "title": "Дневник Бридджит Джонс",
    "year": 2001,
    "genre": "Комедия",
    "poster": "https://ru-images-s.kinorium.com/movie/1080/197257.jpg?1578002705",
    "desc": "Романтическая комедия про женщину в поисках любви"
  },
  {
    "title": "Ночь музеев",
    "year": 2006,
    "genre": "Комедия",
    "poster": "https://ru-images-s.kinorium.com/movie/1080/358342.jpg?1517243207",
    "desc": "Семейная комедия про оживающих музейных экспонатов"
  },
  {
    "title": "Аватар",
    "year": 2009,
    "genre": "Фантастика",
    "poster": "https://i.pinimg.com/736x/4e/2c/91/4e2c91fd28b78bccb36b7048bf80f3aa.jpg",
    "desc": "Эпическая фантастика про войну за планету"
  },
  {
    "title": "Начало",
    "year": 2010,
    "genre": "Фантастика",
    "poster": "https://sxodim.com/uploads/almaty/2016/04/447301.jpg",
    "desc": "Умный триллер про краже идей из снов"
  },
  {
    "title": "Когда Гарри встретил Салли",
    "year": 1989,
    "genre": "Комедия",
    "poster": "https://ir.ozone.ru/s3/multimedia-1-b/6976018775.jpg",
    "desc": "Классическая романтическая комедия про дружбу"
  },
  {
    "title": "Миссия спасения",
    "year": 1994,
    "genre": "Драма",
    "poster": "https://m.media-amazon.com/images/M/MV5BYjUzZTAwYzYtZGU1Yi00ZTY1LTg5OGQtYTcxMzJhMzQ1MTRjXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
    "desc": "История узника, обретшего надежду и свободу"
  },
  {
    "title": "Рокки",
    "year": 1976,
    "genre": "Драма",
    "poster": "https://cdn1.ozone.ru/s3/multimedia-1-z/7475869691.jpg",
    "desc": "Вдохновляющая история борца, ставшего чемпионом"
  }
]

reviews_templates = {
    "Драма": [
        {"text": "Глубокий фильм, который трогает за душу. Актёры играют великолепно!", "rating": 5},
        {"text": "Эмоциональная история, не могу оторваться от экрана.", "rating": 5},
        {"text": "Хорошая драма, но местами медленновато.", "rating": 4},
        {"text": "Интересный сюжет, но концовка предсказуема.", "rating": 3},
        {"text": "Мощная история, оставляет впечатление.", "rating": 5},
        {"text": "Неплохо, но мне кажется, лучше читать книгу.", "rating": 3},
    ],
    "Боевик": [
        {"text": "Динамичный и захватывающий боевик! Отличные трюки!", "rating": 5},
        {"text": "Супер! Не скучал ни секунды, экшена на всё 100%", "rating": 5},
        {"text": "Хороший боевик, но сюжет немного слабый.", "rating": 4},
        {"text": "Много взрывов и стрельбы, без особого смысла.", "rating": 3},
        {"text": "Классический боевик! Есть всё - действие, герой, девушка!", "rating": 5},
        {"text": "Предсказуемо, но развлечения ради годится.", "rating": 3},
    ],
    "Фантастика": [
        {"text": "Поражающий воображение фильм! Великолепная визуализация!", "rating": 5},
        {"text": "Научная фантастика на высшем уровне. Просто восхитительно!", "rating": 5},
        {"text": "Интересные идеи, но реализация могла быть лучше.", "rating": 4},
        {"text": "Слишком много компьютерной графики, мало сюжета.", "rating": 3},
        {"text": "Инновационный и захватывающий фильм!", "rating": 5},
        {"text": "Хорошая фантастика, но местами скучновато.", "rating": 3},
    ],
    "Комедия": [
        {"text": "Очень смешная и весёлая! Перенеслась в прекрасное настроение!", "rating": 5},
        {"text": "Отличная комедия! Смеялась весь фильм!", "rating": 5},
        {"text": "Забавная комедия, хорошо помогает расслабиться.", "rating": 4},
        {"text": "Юмор не очень, но что-то смешное есть.", "rating": 3},
        {"text": "Гениальная комедия! Просто шедевр юмора!", "rating": 5},
        {"text": "Попытка комедии, но юмор странноват.", "rating": 2},
    ],
    "Триллер": [
        {"text": "Напряженный и захватывающий триллер! На краю кресла!", "rating": 5},
        {"text": "Держит в напряжении всё время. Отличный триллер!", "rating": 5},
        {"text": "Хороший триллер, но предсказуем в некоторых местах.", "rating": 4},
        {"text": "Ничего особенного, стандартный триллер.", "rating": 3},
        {"text": "Невероятно напряженный и интересный фильм!", "rating": 5},
        {"text": "Можно посмотреть, но лучше есть.", "rating": 3},
    ],
    "Мелодрама": [
        {"text": "Трогательная история любви. Со слезами на глазах!", "rating": 5},
        {"text": "Красивая любовная история. Очень романтично!", "rating": 5},
        {"text": "Мелодрама хороша, но местами слишком сладкая.", "rating": 4},
        {"text": "Стандартная история любви, ничего нового.", "rating": 3},
        {"text": "Волшебный фильм про вечную любовь!", "rating": 5},
        {"text": "Слишком много слёз, мало действия.", "rating": 2},
    ],
    "Приключения": [
        {"text": "Захватывающее приключение! Магия и чудеса!", "rating": 5},
        {"text": "Веселое путешествие полное сюрпризов!", "rating": 5},
        {"text": "Хороший фильм про приключения, развлечение гарантировано.", "rating": 4},
        {"text": "Неплохо для семейного просмотра.", "rating": 3},
        {"text": "Шикарный фильм про путешествия и дружбу!", "rating": 5},
        {"text": "Неплохо, но могло быть ещё лучше.", "rating": 3},
    ],
    "Ужасы": [
        {"text": "Леденящий ужас! Не спал всю ночь после просмотра!", "rating": 5},
        {"text": "Классический фильм ужасов! Пугает по настоящему!", "rating": 5},
        {"text": "Страшный фильм, хорошо сделан, но не очень оригинален.", "rating": 4},
        {"text": "Попытка ужаса, но скорее смешно чем страшно.", "rating": 2},
        {"text": "Ужасающий и прекрасный фильм!", "rating": 5},
        {"text": "Слишком кровавый и насильственный.", "rating": 2},
    ],
}

def hash_password(password: str) -> str:
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def seed_movies_and_reviews():
    """Load all 50 real movies with reviews, ratings, and users into database"""
    print("\n🍋 Loading 50 movies, reviews, ratings, and users...\n")
    
    # Create users first
    print("👥 Creating users...")
    user_ids = []
    
    # Create 10 viewers
    for viewer in viewers_data:
        try:
            user = db.create_user(
                email=viewer["email"],
                username=viewer["username"],
                password=hash_password(viewer["password"])
            )
            user_ids.append(user['id'])
            print(f"   ✅ Created viewer: {viewer['username']}")
        except Exception as e:
            print(f"   ⚠️  Error creating user {viewer['username']}: {str(e)}")
    
    # Create moderator
    try:
        admin = db.create_user(
            email=admin_user["email"],
            username=admin_user["username"],
            password=hash_password(admin_user["password"]),
            is_moderator=admin_user["is_moderator"]
        )
        print(f"   ✅ Created moderator: {admin_user['username']}")
    except Exception as e:
        print(f"   ⚠️  Error creating moderator: {str(e)}")
    
    print(f"\n🎬 Creating movies, reviews, and ratings...\n")
    
    total_reviews = 0
    total_ratings = 0
    
    for i, movie_info in enumerate(movies_data):
        try:
            # Create movie
            movie = db.create_movie(
                title=movie_info["title"],
                description=movie_info["desc"],
                genre=movie_info["genre"],
                year=movie_info["year"],
                poster_url=movie_info["poster"]
            )
            movie_id = movie['id']
            
            # Get reviews for this genre
            genre_reviews = reviews_templates.get(movie_info["genre"], reviews_templates["Драма"])
            
            # Add 4-7 reviews per movie from different users
            review_count = 4 + (i % 4)  # 4-7 reviews
            for j in range(review_count):
                review = genre_reviews[j % len(genre_reviews)]
                # Assign to different user (cycle through user_ids)
                user_id = user_ids[j % len(user_ids)] if user_ids else 1
                
                try:
                    db.create_review(
                        movie_id=movie_id,
                        user_id=user_id,
                        text=review["text"],
                        rating=review["rating"]
                    )
                    total_reviews += 1
                    
                    # Create corresponding rating in ratings table
                    db.create_or_update_rating(
                        movie_id=movie_id,
                        user_id=user_id,
                        value=float(review["rating"])
                    )
                    total_ratings += 1
                except Exception as e:
                    print(f"   ⚠️  Error creating review for movie {movie_id}: {str(e)}")
                    continue
        except Exception as e:
            print(f"   ⚠️  Error creating movie: {str(e)}")
            continue
        
        # Print progress
        if (i + 1) % 10 == 0:
            print(f"  ✅ {i + 1}/50 movies loaded")
    
    print("\n✅ All data loaded!")
    print(f"🎬 50 настоящих фильмов")
    print(f"👥 {len(user_ids)} зрителей + 1 модератор")
    print(f"🗣️  {total_reviews} рецензий")
    print(f"⭐ {total_ratings} оценок в таблице ratings")
    print(f"\n📁 Учётные данные:")
    print(f"   Модератор:")
    print(f"   Email: {admin_user['email']}")
    print(f"   Password: {admin_user['password']}")
    if viewers_data:
        print(f"\n   Зритель пример ({viewers_data[0]['username']}):")
        print(f"   Email: {viewers_data[0]['email']}")
        print(f"   Password: {viewers_data[0]['password']}")
    print(f"\n📁 file: kinovzor.db\n")

if __name__ == "__main__":
    seed_movies_and_reviews()
