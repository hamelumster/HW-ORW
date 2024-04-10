#Задача №3
#Список файлов, над которыми работаем в рамках задачи
files = ['1.txt', '2.txt', '3.txt']

#Функция считывания файлов из списка files и возвращающая отсортированный список по кол-ву строк в файле
def read_file(files):
    list_ = []
    for file in (files):
        with open (file, 'r', encoding='utf-8') as f:
            str_ = f.readlines()
            str_count = len(str_)
            list_.append([str_count, file, str_]) #В список добавляем список, состоящий из кол-ва строк в файле, названия файла и его строк

    sorted_list = sorted(list_)
    return sorted_list


"""
Функция записи отсортированного списка в файл result.txt в формате: 
- наименование файла
- кол-во строк в файле
- строка файла"""
def write_file(sorted_list):
    with open ('result.txt', 'w', encoding='utf-8') as f:
        for i in sorted_list:
            f.write(f'{i[1]}\n')
            f.write(f'{i[0]}\n')
            for j in i[2]:
                f.write(f'{j}')
            f.write('\n')

#Вызов функции для записи итогового файла в result.txt
write_file(read_file(files))