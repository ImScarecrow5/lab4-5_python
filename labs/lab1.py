import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# --- Функция для Задания 1 ---
def task_1():
    print("Выполняется Задание 1...")
    a = 5
    b = 3
    c = 7

    x = np.arange(-7, 7.5, 0.5)
    y1 = a * x + b
    y2 = (a + x) ** 2 + c * np.cos(b * x)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot(x, y1, color='green', linestyle='-.', linewidth=1.5, label='y1(x): линейный')
    ax.scatter(x, y2, color='blue', marker='*', s=15, label='y2(x): точечный')

    ax.set_title('Лабораторное задание 1 (Вариант 3)', fontsize=16, color='red')
    ax.set_xlabel('Ось X', fontsize=16)
    ax.set_ylabel('Ось Y', fontsize=16)
    ax.grid(True)
    ax.legend()
    plt.show()


# --- Функция для Задания 2 ---
def task_2():
    print("Выполняется Задание 2...")
    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь']
    sales_1 = [120, 150, 170, 200, 180, 210]
    sales_2 = [90, 130, 160, 140, 190, 220]

    fig, axs = plt.subplots(2, 2, figsize=(12, 10))

    # 1. Линии
    axs[0, 0].plot(months, sales_1, marker='o', color='blue', label='Предприятие 1')
    axs[0, 0].plot(months, sales_2, marker='s', color='orange', label='Предприятие 2')
    axs[0, 0].set_title('1. Линейные графики продаж')
    axs[0, 0].set_xlabel('Месяц')
    axs[0, 0].set_ylabel('Объем продаж')
    axs[0, 0].grid(True)
    axs[0, 0].legend()

    # 2. Столбики рядом
    x = np.arange(len(months))
    width = 0.35
    axs[0, 1].bar(x - width / 2, sales_1, width, label='Предприятие 1', color='blue')
    axs[0, 1].bar(x + width / 2, sales_2, width, label='Предприятие 2', color='orange')
    axs[0, 1].set_title('2. Столбиковая диаграмма продаж')
    axs[0, 1].set_xlabel('Месяц')
    axs[0, 1].set_ylabel('Объем продаж')
    axs[0, 1].set_xticks(x)
    axs[0, 1].set_xticklabels(months)
    axs[0, 1].grid(axis='y')
    axs[0, 1].legend()

    # 3. Круговая 1
    axs[1, 0].pie(sales_1, labels=months, autopct='%1.1f%%', startangle=140)
    axs[1, 0].set_title('3. Доли продаж: Предприятие 1')

    # 4. Круговая 2
    axs[1, 1].pie(sales_2, labels=months, autopct='%1.1f%%', startangle=140)
    axs[1, 1].set_title('4. Доли продаж: Предприятие 2')

    plt.tight_layout()
    plt.show()


# --- Функция для Задания 3 ---
def task_3():
    print("Выполняется Задание 3...")
    np.random.seed(42)
    data = np.random.randint(1, 101, size=50)
    data[10] = 150  # замена произвольного элемента

    mean_val = np.mean(data)
    median_val = np.median(data)
    std_val = np.std(data)

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Гистограмма
    axs[0].hist(data, bins=5, edgecolor='black', color='skyblue')
    axs[0].axvline(mean_val, color='r', linewidth=2, label=f'Среднее: {mean_val:.2f}')
    axs[0].axvline(median_val, color='g', linewidth=2, label=f'Медиана: {median_val:.2f}')
    axs[0].axvline(mean_val + std_val, color='y', linestyle='dashed', linewidth=1.5, label=f'Ст. откл.: {std_val:.2f}')
    axs[0].axvline(mean_val - std_val, color='y', linestyle='dashed', linewidth=1.5)
    axs[0].set_title('Гистограмма распределения')
    axs[0].set_xlabel('Значения')
    axs[0].set_ylabel('Частота')
    axs[0].legend()
    axs[0].grid(True)

    # Boxplot (исправлено vert=True на orientation='vertical')
    axs[1].boxplot(data, orientation='vertical', patch_artist=True, boxprops=dict(facecolor='skyblue'))
    axs[1].set_title('Диаграмма размаха (Boxplot)')
    axs[1].set_ylabel('Значения')
    axs[1].grid(True)

    plt.tight_layout()
    plt.show()


# --- Функция для Задания 4 ---
def task_4():
    print("Выполняется Задание 4...")
    a = 5
    b = 3
    c = 7

    x = np.linspace(-7, 7, 100)
    y = (a + x) ** 2 + c * np.cos(b * x)
    z = np.sin(x)

    fig = plt.figure(figsize=(8, 6))
    # Исправление: вместо add_axes используется add_subplot с projection='3d'
    ax = fig.add_subplot(projection='3d')
    ax.plot(x, y, z, color='purple', linewidth=2)

    ax.set_title('Лабораторное задание 4: 3D график y2(x) (Вариант 3)')
    ax.set_xlabel('Ось X')
    ax.set_ylabel('Ось Y')
    ax.set_zlabel('Ось Z')
    plt.show()


# --- Функция для Задания 5 ---
def task_5():
    print("Выполняется Задание 5...")
    x = np.arange(-5, 5.2, 0.2)
    y = np.arange(3, 18.3, 0.3)

    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = (xgrid ** 2 + 5) / (2 * ygrid - 1)

    fig, ax = plt.subplots(figsize=(10, 7), subplot_kw={'projection': '3d'})

    surface = ax.plot_surface(xgrid, ygrid, zgrid, cmap='coolwarm', edgecolor='none')
    fig.colorbar(surface, shrink=0.5, aspect=5)

    ax.set_title('Лабораторное задание 5: 3D Поверхность (Вариант 3)')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


# --- Функция для Задания 6 ---
def task_6():
    print("Выполняется Задание 6...")
    np.random.seed(42)
    img_original = np.random.rand(10, 10)

    # Вариант 3: правый верхний угол 4x4
    img_cropped = img_original[0:4, 6:10]

    # Инвертирование
    img_inverted = 1.0 - img_original

    # Размытие
    img_blurred = img_original.copy()
    for i in range(1, 9):
        for j in range(1, 9):
            img_blurred[i, j] = (img_original[i, j - 1] + img_original[i, j] + img_original[i, j + 1]) / 3

    fig, axs = plt.subplots(2, 2, figsize=(8, 8))

    axs[0, 0].imshow(img_original, cmap='gray')
    axs[0, 0].set_title('1. Исходное (10x10)')

    axs[0, 1].imshow(img_cropped, cmap='gray')
    axs[0, 1].set_title('2. Правый верхний угол (4x4)')

    axs[1, 0].imshow(img_inverted, cmap='gray')
    axs[1, 0].set_title('3. Инвертированное')

    axs[1, 1].imshow(img_blurred, cmap='gray')
    axs[1, 1].set_title('4. Размытое')

    for row in axs:
        for ax in row:
            ax.axis('on')

    plt.tight_layout()
    fig.savefig('lab6_variant3_result.png', dpi=300)
    print("Результат сохранен в файл 'lab6_variant3_result.png'")
    plt.show()


# --- Главное меню с циклом и выбором через match-case ---
def main():
    while True:
        print("\n" + "=" * 50)
        print("Выберите номер лабораторного задания для выполнения:")
        print("1 - Задание 1: Линейный и точечный графики (Вариант 3)")
        print("2 - Задание 2: 4 графика на одной сетке 2x2 (продажи)")
        print("3 - Задание 3: Гистограмма и Boxplot для массива")
        print("4 - Задание 4: 3D график функции y2(x) (Вариант 3)")
        print("5 - Задание 5: 3D поверхность (Вариант 3)")
        print("6 - Задание 6: Работа с массивами и изображениями (Вариант 3)")
        print("0 - Выход из программы")
        print("=" * 50)

        try:
            task_num = int(input("Введите номер задания (0-6): "))
        except ValueError:
            print("Ошибка: введите целое число от 0 до 6.")
            continue

        if task_num == 0:
            print("Выход из программы. До свидания!")
            break

        match task_num:
            case 1:
                task_1()
            case 2:
                task_2()
            case 3:
                task_3()
            case 4:
                task_4()
            case 5:
                task_5()
            case 6:
                task_6()
            case _:
                print("Неверный номер задания. Пожалуйста, выберите число от 0 до 6.")


if __name__ == '__main__':
    main()