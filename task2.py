# воспользуемся готовым решением для доступа к Wiki API
# https://pypi.org/project/Wikipedia-API/
import wikipediaapi
# начнем с получения наших названий из страницы категорий
wiki = wikipediaapi.Wikipedia('ru')
c_page = wiki.page('Категория:Животные по алфавиту')
d = dict()
# получаем всех членов категории животных
members = c_page.categorymembers
for i in members.values():
    if i.ns == wikipediaapi.Namespace.CATEGORY:
        # подкатегории нам не интересны
        pass
    else:
        page_title = i.title
        # получаем первую букву названия животного
        letter = page_title[0].upper()
        # принимаем ее за ключ в словаре и устанавливаем/инкрементируем в нем значение
        if letter in d.keys():
            d[letter] += 1
        else:
            d[letter] = 1

# примечание: на русской Вики есть названия на английском, так что русским алфавитом словарь не ограничится
for k in d.keys():
    print(k, ':', d[k])


